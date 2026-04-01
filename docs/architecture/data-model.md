# Data Model

18 DynamoDB tables + 1 OpenSearch domain.

## D1 Tables (Meeting Management)

### Users
| Field | Type | Key |
|---|---|---|
| user_id | String | PK |
| email | String | |
| username | String | |
| role | String | |
| created_at | String (ISO 8601) | |

### Projects
| Field | Type | Key |
|---|---|---|
| project_id | String | PK |
| name | String | |
| email | String | |
| description | String | |
| s3_arn | String | |
| bot_credential_id | String | |
| agent_id | String | FK → Agents |
| created_at | String (ISO 8601) | |
| updated_at | String (ISO 8601) | |

### ProjectUsers
| Field | Type | Key |
|---|---|---|
| project_user_id | String | PK |
| project_id | String | |
| user_id | String | GSI: user-index |
| created_at | String (ISO 8601) | |

### Sessions
| Field | Type | Key |
|---|---|---|
| session_id | String | PK |
| project_id | String | GSI: project-index |
| is_active | String | GSI: active-sessions-index |
| name | String | |
| meeting_link | String | |
| bot_status | String | |
| task_arn | String | |
| dispatch_mode | String | |
| connection_id | String | |
| last_activity_at | String | |
| last_transcript_update_at | String | |
| last_gap_analysis_at | String | |
| created_at | String (ISO 8601) | |
| updated_at | String (ISO 8601) | |

### Transcripts
| Field | Type | Key |
|---|---|---|
| session_id | String | PK |
| transcript_id | String | SK |
| speaker | String | |
| speaker_role | String | |
| text | String | |
| timestamp | String | |

> **Note:** The `speaker_role` field IS now populated by the processing pipeline using Cohere Embed v3 speaker classification. Values are `"user"`, `"client"`, or `"unknown"`. See [Speaker Role Classification](../features/speaker-role-classification.md) for details.

### BotCredentials
| Field | Type | Key |
|---|---|---|
| credential_id | String | PK |
| email | String | GSI: email-index |
| verification_status | String | validating → verified / verification_failed |
| verification_error | String | Error message (present only on failure) |
| available_status | String | inactive → active (auto-set on verification) |
| warm_pool_size | Number | Default 1 |
| created_at | String (ISO 8601) | |
| updated_at | String (ISO 8601) | |

> **EventBridge integration:** Creating a bot credential publishes a `BotCredentialValidation` event to EventBridge. The `ValidateBotCredentialWorker` Lambda is triggered by an EventBridge rule to perform async SMTP validation and update the credential status.

### BotPool
| Field | Type | Key |
|---|---|---|
| pool_id | String | PK |
| credential_id | String | GSI: credential-status-index |
| status | String | GSI: credential-status-index (SK) |
| task_arn | String | |
| created_at | String (ISO 8601) | |

## D2 Tables (AI Agent Engine)

### Agents
| Field | Type | Key |
|---|---|---|
| agent_id | String | PK |
| agent_name | String | |
| role_prompt | String | |
| behavior_guidelines | String | |
| task_prompt | String | Deprecated — alias for `behavior_guidelines`. Accepted on write, included in read responses for backward compatibility. |
| personality_id | String | FK → Personalities |
| model_id | String | |
| use_case | String | |
| created_at | String (ISO 8601) | |
| updated_at | String (ISO 8601) | |

### Personalities
| Field | Type | Key |
|---|---|---|
| personality_id | String | PK |
| personality_name | String | |
| personality_prompt | String | |
| created_at | String (ISO 8601) | |
| updated_at | String (ISO 8601) | |

### QAPairs
| Field | Type | Key |
|---|---|---|
| qa_pair_id | String | PK |
| session_id | String | GSI: session-index |
| project_id | String | GSI: project-index |
| question | String | |
| answer | String | |
| source | String | |
| created_at | String (ISO 8601) | |

### SuggestedQuestions
| Field | Type | Key |
|---|---|---|
| question_id | String | PK |
| session_id | String | GSI: session-index |
| question_text | String | |
| embedding | List (Decimal) | |
| matched | Boolean | |
| created_at | String (ISO 8601) | |

### Skills
| Field | Type | Key |
|---|---|---|
| skill_id | String | PK |
| agent_id | String | GSI: agent-index |
| skill_name | String | |
| description | String | |
| s3_key | String | |
| file_type | String | |
| status | String (pending/active/failed) | |
| created_at | String (ISO 8601) | |
| updated_at | String (ISO 8601) | |

### AgentSkills (Junction Table)
| Field | Type | Key |
|---|---|---|
| agent_id | String | PK |
| skill_id | String | SK |
| assigned_at | String (ISO 8601) | |

GSI: `skill-index` (PK: skill_id) for reverse lookups.

Enables many-to-many relationships between agents and skills. A single skill document can be shared across multiple agents.

### GapAnalysisResults
| Field | Type | Key |
|---|---|---|
| session_id | String | PK |
| gaps | List of Maps | |
| suggested_questions | List of Strings | |
| analyzed_at | String (ISO 8601) | |

### KbDocuments
| Field | Type | Key |
|---|---|---|
| document_id | String | PK |
| project_id | String | GSI: project-index |
| file_name | String | |
| description | String | |
| s3_key | String | |
| file_type | String | |
| file_size | Number | |
| status | String (pending/active) | |
| doc_type | String (user_upload/meeting_summary) | |
| session_id | String | Optional, present for meeting summaries |
| created_at | String (ISO 8601) | |
| updated_at | String (ISO 8601) | |

## OpenSearch

### Index: knowledge-vectors

| Field | Type | Description |
|---|---|---|
| embedding | knn_vector (1024) | Titan Embed Text V2 vector |
| text | text | Source text chunk |
| project_id | keyword | Scoping to project |
| doc_type | keyword | `user_upload`, `meeting_summary`, or `agent_skill` |
| agent_id | keyword | Scoping for agent skills |
| source_file | keyword | Original filename |
| chunk_index | integer | Position in source document |

## Entity Relationships

- Agents → Personalities (FK: personality_id, enforced on delete with 409)
- Agents ↔ Skills (many-to-many via AgentSkills junction table)
- Sessions → Transcripts (1:many via composite key PK=session_id)
- Sessions → QAPairs (1:many via session-index GSI)
- Sessions → SuggestedQuestions (1:many via session-index GSI)
- Projects → Sessions (1:many via project-index GSI)
- Sessions → GapAnalysisResults (1:1 via session_id)
- BotCredentials → BotPool (1:many via credential-status-index GSI)
- Projects → KbDocuments (1:many via project-index GSI)
- Projects → Agents (FK: agent_id)
- BotCredentials → EventBridge → ValidateBotCredentialWorker (async SMTP validation)

## Audit & Tracking Tables

### AgentConfigHistory
| Field | Type | Key |
|---|---|---|
| agent_id | String | PK |
| version | Number | SK |
| agent_name | String | |
| role_prompt | String | |
| behavior_guidelines | String | |
| personality_id | String | |
| personality_name | String | Resolved at snapshot time |
| model_id | String | |
| use_case | String | |
| skill_names | List of Strings | Resolved at snapshot time |
| changed_fields | List of Strings | |
| created_at | String (ISO 8601) | Original agent creation time |
| snapshot_at | String (ISO 8601) | When this snapshot was taken |

Snapshots are created on agent update and skill assign/unassign, with a 5-second debounce to avoid duplicates from rapid frontend calls.

### AdminChangelog
| Field | Type | Key |
|---|---|---|
| changelog_id | String (UUID) | PK |
| entity_type | String | GSI PK (entity-type-index) |
| timestamp | String (ISO 8601) | GSI SK (entity-type-index) |
| entity_id | String | |
| entity_name | String | Human-readable name at time of action |
| action | String | create / update / delete / login_success / login_failed / login_locked |
| admin_user_id | String | |
| admin_username | String | |
| data | Map | Entity snapshot or changed fields |
| previous_data | Map | Previous values (update/delete) |
| changed_fields | List of Strings | Update only |
| ip_address | String | Login events only |

Covers all CRUD operations on users, projects, agents, personalities, skills, bot credentials, and project-user assignments. Also records login attempts (success, failure, lockout).

### TokenUsage
| Field | Type | Key |
|---|---|---|
| usage_id | String (UUID) | PK |
| session_id | String | GSI PK (session-index) |
| timestamp | String (ISO 8601) | GSI SK (session-index) |
| project_id | String | |
| action | String | e.g. sendMessage, detectQuestion, titanEmbed |
| model_id | String | e.g. amazon.nova-pro-v1:0 |
| input_tokens | Number | |
| output_tokens | Number | |
| total_tokens | Number | |
| estimated | Boolean | True for embedding calls where count is estimated |

Tracks Bedrock model token consumption per action. Embedding calls (Titan Embed, Cohere Embed) use estimated token counts (~4 chars per token).
