# Data Model

12 DynamoDB tables + 1 OpenSearch domain.

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

> **Note:** The `speaker_role` field is no longer populated by the processing pipeline for single-channel transcripts. It is retained in the schema for backward compatibility with existing data. New transcript entries will not include this field.

### BotCredentials
| Field | Type | Key |
|---|---|---|
| credential_id | String | PK |
| verification_status | String | |
| available_status | String | |
| created_at | String (ISO 8601) | |

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

### GapAnalysisResults
| Field | Type | Key |
|---|---|---|
| session_id | String | PK |
| gaps | List of Maps | |
| suggested_questions | List of Strings | |
| analyzed_at | String (ISO 8601) | |

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
- Agents → Skills (1:many via agent_id GSI)
- Sessions → Transcripts (1:many via composite key PK=session_id)
- Sessions → QAPairs (1:many via session-index GSI)
- Sessions → SuggestedQuestions (1:many via session-index GSI)
- Projects → Sessions (1:many via project-index GSI)
- Sessions → GapAnalysisResults (1:1 via session_id)
