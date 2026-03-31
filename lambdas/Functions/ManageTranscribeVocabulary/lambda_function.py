"""
Manage Transcribe Vocabulary

Custom Resource handler for creating, updating, and deleting
Amazon Transcribe custom vocabularies during CDK deployment.
"""

import time
import logging

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

transcribe = boto3.client("transcribe")


def handler(event, context):
    request_type = event["RequestType"]
    props = event["ResourceProperties"]
    vocab_name = props["VocabularyName"]
    language_code = props["LanguageCode"]
    vocab_uri = props["VocabularyFileUri"]

    logger.info(f"{request_type} vocabulary: {vocab_name}")

    if request_type in ("Create", "Update"):
        exists = False
        try:
            transcribe.get_vocabulary(VocabularyName=vocab_name)
            exists = True
        except (
            transcribe.exceptions.NotFoundException,
            transcribe.exceptions.BadRequestException,
        ):
            exists = False

        if exists:
            transcribe.update_vocabulary(
                VocabularyName=vocab_name,
                LanguageCode=language_code,
                VocabularyFileUri=vocab_uri,
            )
        else:
            transcribe.create_vocabulary(
                VocabularyName=vocab_name,
                LanguageCode=language_code,
                VocabularyFileUri=vocab_uri,
            )

        # Wait for vocabulary to become READY
        for _ in range(60):
            time.sleep(5)
            try:
                resp = transcribe.get_vocabulary(VocabularyName=vocab_name)
            except (
                transcribe.exceptions.NotFoundException,
                transcribe.exceptions.BadRequestException,
            ):
                logger.info("Vocabulary not yet available, retrying...")
                continue

            state = resp["VocabularyState"]
            if state == "READY":
                logger.info(f"Vocabulary {vocab_name} is READY")
                break
            if state == "FAILED":
                reason = resp.get("FailureReason", "unknown")
                raise Exception(f"Vocabulary creation failed: {reason}")
        else:
            raise Exception("Vocabulary did not become READY within timeout")

    elif request_type == "Delete":
        try:
            transcribe.delete_vocabulary(VocabularyName=vocab_name)
        except Exception as e:
            logger.warning(f"Delete vocabulary failed (may not exist): {e}")

    return {"PhysicalResourceId": vocab_name}
