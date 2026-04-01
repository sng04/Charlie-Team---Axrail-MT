"""Speaker role classification using Cohere Embed v3 on Bedrock.

Classifies transcript lines as 'user' (sales rep / consultant) or 'client'
(customer / prospect) by comparing line embeddings against pre-computed
role exemplar centroids using cosine similarity.

Designed for single-channel audio where Amazon Transcribe assigns the same
speaker label to all lines.
"""

import json
import math
from typing import Optional

import boto3
from aws_lambda_powertools import Logger

from constants import COHERE_EMBED_MODEL_ID, BEDROCK_REGION
from token_tracking import track_token_usage

logger = Logger(child=True)

# ---------------------------------------------------------------------------
# Default role exemplars
# ---------------------------------------------------------------------------

USER_EXEMPLARS = [
    "Let me walk you through our platform.",
    "We offer three pricing tiers for enterprise clients.",
    "Our system handles that with automated reconciliation.",
    "I'll follow up with your team on that action item.",
    "From our side, we'll set up the environments by Friday.",
    "That's a great question. Our SLA guarantees next-day settlement.",
    "We've built compliance in from day one.",
    "Let me show you how the dashboard works.",
    "We can push a firmware update tonight to fix that.",
    "I'll coordinate with your IT team on the rollout.",
]

CLIENT_EXEMPLARS = [
    "What's the pricing for enterprise retailers?",
    "We need this integrated with our Salesforce CRM.",
    "Our team has concerns about data security.",
    "Can you confirm the settlement timeline?",
    "We've been on SAP since 2014 and the data isn't great.",
    "What happens if UAT reveals major issues?",
    "I'll need to check with our IT team on that.",
    "That's a non-negotiable requirement for us.",
    "What's the false positive rate on that?",
    "Our finance team wants to see two weeks of pilot data first.",
]


# ---------------------------------------------------------------------------
# Bedrock client cache
# ---------------------------------------------------------------------------

_bedrock_client = None


def _get_bedrock_client():
    """Return a cached Bedrock Runtime client for the embedding region."""
    global _bedrock_client
    if _bedrock_client is None:
        _bedrock_client = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)
    return _bedrock_client


# ---------------------------------------------------------------------------
# Cohere Embed v3 integration
# ---------------------------------------------------------------------------


def _embed_texts_cohere(
    texts: list[str],
    input_type: str = "search_query",
) -> list[list[float]]:
    """Embed a batch of texts using Cohere Embed v3 on Bedrock.

    Args:
        texts: List of strings to embed.
        input_type: "classification" for exemplars, "search_query" for
                    transcript lines.

    Returns:
        List of 1024-dim embedding vectors, one per input text.
        Returns empty list on error.
    """
    if not texts:
        return []
    try:
        client = _get_bedrock_client()
        response = client.invoke_model(
            modelId=COHERE_EMBED_MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "texts": texts,
                "input_type": input_type,
                "truncate": "END",
            }),
        )
        body = json.loads(response["body"].read())
        total_chars = sum(len(t) for t in texts)
        track_token_usage("", "cohereEmbed", "cohere.embed-english-v3", max(1, total_chars // 4), 0, estimated=True)
        return body.get("embeddings", [])
    except Exception:
        logger.exception("Cohere Embed call failed")
        return []


# ---------------------------------------------------------------------------
# Centroid computation
# ---------------------------------------------------------------------------


def _mean_vector(vectors: list[list[float]]) -> list[float]:
    """Compute the element-wise mean of a list of vectors."""
    if not vectors:
        return []
    dim = len(vectors[0])
    result = [0.0] * dim
    for vec in vectors:
        for i in range(dim):
            result[i] += vec[i]
    n = len(vectors)
    return [v / n for v in result]


def _compute_role_centroids(
    user_exemplars: list[str],
    client_exemplars: list[str],
) -> tuple[Optional[list[float]], Optional[list[float]]]:
    """Compute centroid embeddings for user and client exemplars.

    Embeds all exemplars in a single batch call for efficiency, then
    splits and averages into two centroid vectors.

    Returns:
        (user_centroid, client_centroid) — each a 1024-dim float list,
        or (None, None) on failure.
    """
    all_texts = user_exemplars + client_exemplars
    embeddings = _embed_texts_cohere(all_texts, input_type="classification")
    if len(embeddings) != len(all_texts):
        logger.error(
            "Exemplar embedding count mismatch: expected %d, got %d",
            len(all_texts), len(embeddings),
        )
        return None, None

    user_embeddings = embeddings[:len(user_exemplars)]
    client_embeddings = embeddings[len(user_exemplars):]

    user_centroid = _mean_vector(user_embeddings)
    client_centroid = _mean_vector(client_embeddings)

    return user_centroid, client_centroid


# ---------------------------------------------------------------------------
# Cosine similarity & classification
# ---------------------------------------------------------------------------

# Minimum difference between user and client similarity scores to make a
# confident classification. Below this threshold → "unknown".
ROLE_CONFIDENCE_THRESHOLD = 0.03


def _cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def _classify_role(
    text_embedding: list[float],
    user_centroid: list[float],
    client_centroid: list[float],
    threshold: float = ROLE_CONFIDENCE_THRESHOLD,
) -> str:
    """Classify a line embedding as 'user', 'client', or 'unknown'.

    Compares cosine similarity to both centroids. If the difference
    exceeds the threshold, returns the closer role. Otherwise 'unknown'.
    """
    user_sim = _cosine_similarity(text_embedding, user_centroid)
    client_sim = _cosine_similarity(text_embedding, client_centroid)
    diff = abs(user_sim - client_sim)

    if diff < threshold:
        return "unknown"
    return "user" if user_sim > client_sim else "client"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def init_role_classifier(conn_data: dict) -> bool:
    """Initialize the role classifier for a session.

    Computes exemplar embeddings and stores centroids in conn_data.
    Called once on the first processTranscript batch when single-speaker
    mode is detected.

    Returns True if initialization succeeded, False otherwise.
    """
    if conn_data.get("role_classifier", {}).get("initialized"):
        return True

    logger.info("Initializing role classifier with Cohere Embed")
    user_centroid, client_centroid = _compute_role_centroids(
        USER_EXEMPLARS, CLIENT_EXEMPLARS
    )

    if user_centroid is None or client_centroid is None:
        logger.error("Failed to compute role centroids — classifier disabled")
        conn_data["role_classifier"] = {"initialized": False}
        return False

    conn_data["role_classifier"] = {
        "user_centroid": user_centroid,
        "client_centroid": client_centroid,
        "initialized": True,
    }
    logger.info("Role classifier initialized (user centroid dim=%d)", len(user_centroid))
    return True


def classify_line_role(text: str, conn_data: dict) -> str:
    """Classify a single transcript line's speaker role.

    Uses cached embedding if available, otherwise embeds and caches.
    """
    classifier = conn_data.get("role_classifier", {})
    if not classifier.get("initialized"):
        return "unknown"

    if len(text.split()) < 4:
        return "unknown"

    user_centroid = classifier["user_centroid"]
    client_centroid = classifier["client_centroid"]

    try:
        embeddings = _embed_texts_cohere([text], input_type="search_query")
        if not embeddings:
            return "unknown"
        return _classify_role(embeddings[0], user_centroid, client_centroid)
    except Exception:
        logger.exception("classify_line_role failed")
        return "unknown"


def classify_lines_batch(texts: list[str], conn_data: dict) -> list[str]:
    """Classify multiple transcript lines in a single batch embedding call.

    Much faster than calling classify_line_role per line — one Cohere API
    call instead of N.

    Args:
        texts: List of transcript line texts.
        conn_data: Connection data with cached role_classifier.

    Returns:
        List of roles ("user", "client", "unknown"), one per input text.
    """
    classifier = conn_data.get("role_classifier", {})
    if not classifier.get("initialized"):
        return ["unknown"] * len(texts)

    user_centroid = classifier["user_centroid"]
    client_centroid = classifier["client_centroid"]

    # Split into embeddable (>= 4 words) and short lines
    results = ["unknown"] * len(texts)
    to_embed = []
    indices = []
    for i, text in enumerate(texts):
        if len(text.split()) >= 4:
            to_embed.append(text)
            indices.append(i)

    if not to_embed:
        return results

    try:
        embeddings = _embed_texts_cohere(to_embed, input_type="search_query")
        for j, emb in enumerate(embeddings):
            results[indices[j]] = _classify_role(emb, user_centroid, client_centroid)
    except Exception:
        logger.exception("classify_lines_batch failed")

    return results
