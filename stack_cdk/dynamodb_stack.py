from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_dynamodb as dynamodb,
    aws_opensearchservice as opensearch,
    aws_ec2 as ec2,
    CfnOutput,
)
from constructs import Construct


class DynamoDBStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, *, env_name: str, env_config: dict = None, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.env_name = env_name
        self.env_config = env_config or {}
        
        self._create_users_table()
        self._create_projects_table()
        self._create_project_users_table()
        self._create_sessions_table()
        self._create_transcripts_table()
        self._create_bot_credentials_table()
        self._create_bot_pool_table()
        # D2 tables
        self._create_agents_table()
        self._create_personalities_table()
        self._create_qa_pairs_table()
        self._create_suggested_questions_table()
        self._create_skills_table()
        self._create_agent_skills_table()
        self._create_gap_analysis_results_table()
        self._create_kb_documents_table()
        self._create_agent_config_history_table()
        # OpenSearch
        self._create_opensearch_domain()
        self._create_exports()

    def _create_users_table(self) -> None:
        self.users_table = dynamodb.Table(
            self,
            "UsersTable",
            table_name=f"{self.env_name}-Users",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )
        
        self.users_table.add_global_secondary_index(
            index_name="email-index",
            partition_key=dynamodb.Attribute(
                name="email",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_projects_table(self) -> None:
        self.projects_table = dynamodb.Table(
            self,
            "ProjectsTable",
            table_name=f"{self.env_name}-Projects",
            partition_key=dynamodb.Attribute(
                name="project_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

        self.projects_table.add_global_secondary_index(
            index_name="name-index",
            partition_key=dynamodb.Attribute(
                name="name",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.KEYS_ONLY,
        )

    def _create_project_users_table(self) -> None:
        self.project_users_table = dynamodb.Table(
            self,
            "ProjectUsersTable",
            table_name=f"{self.env_name}-ProjectUsers",
            partition_key=dynamodb.Attribute(
                name="project_user_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )
        
        self.project_users_table.add_global_secondary_index(
            index_name="project-index",
            partition_key=dynamodb.Attribute(
                name="project_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )
        
        self.project_users_table.add_global_secondary_index(
            index_name="user-index",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_sessions_table(self) -> None:
        self.sessions_table = dynamodb.Table(
            self,
            "SessionsTable",
            table_name=f"{self.env_name}-Sessions",
            partition_key=dynamodb.Attribute(
                name="session_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )
        
        self.sessions_table.add_global_secondary_index(
            index_name="project-index",
            partition_key=dynamodb.Attribute(
                name="project_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

        self.sessions_table.add_global_secondary_index(
            index_name="active-sessions-index",
            partition_key=dynamodb.Attribute(
                name="is_active",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_transcripts_table(self) -> None:
        """Create Transcripts table for meeting bot transcriptions."""
        self.transcripts_table = dynamodb.Table(
            self,
            "TranscriptsTable",
            table_name=f"{self.env_name}-Transcripts",
            partition_key=dynamodb.Attribute(
                name="session_id",
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name="timestamp",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

        self.transcripts_table.add_global_secondary_index(
            index_name="transcript-id-index",
            partition_key=dynamodb.Attribute(
                name="transcript_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

        self.transcripts_table.add_global_secondary_index(
            index_name="speaker-index",
            partition_key=dynamodb.Attribute(
                name="session_id",
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name="speaker",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_bot_credentials_table(self) -> None:
        """Create BotCredentials table for Gmail bot accounts."""
        self.bot_credentials_table = dynamodb.Table(
            self,
            "BotCredentialsTable",
            table_name=f"{self.env_name}-BotCredentials",
            partition_key=dynamodb.Attribute(
                name="credential_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

        self.bot_credentials_table.add_global_secondary_index(
            index_name="email-index",
            partition_key=dynamodb.Attribute(
                name="email",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_bot_pool_table(self) -> None:
        """Create BotPool table for tracking warm pool containers."""
        self.bot_pool_table = dynamodb.Table(
            self,
            "BotPoolTable",
            table_name=f"{self.env_name}-BotPool",
            partition_key=dynamodb.Attribute(
                name="container_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            time_to_live_attribute="ttl",
        )

        self.bot_pool_table.add_global_secondary_index(
            index_name="credential-status-index",
            partition_key=dynamodb.Attribute(
                name="credential_id",
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name="status",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_agents_table(self) -> None:
        """Create Agents table for AI agent configurations."""
        self.agents_table = dynamodb.Table(
            self,
            "AgentsTable",
            table_name=f"{self.env_name}-Agents",
            partition_key=dynamodb.Attribute(
                name="agent_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

        self.agents_table.add_global_secondary_index(
            index_name="name-index",
            partition_key=dynamodb.Attribute(
                name="agent_name",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.KEYS_ONLY,
        )

    def _create_personalities_table(self) -> None:
        """Create Personalities table for agent personality profiles."""
        self.personalities_table = dynamodb.Table(
            self,
            "PersonalitiesTable",
            table_name=f"{self.env_name}-Personalities",
            partition_key=dynamodb.Attribute(
                name="personality_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

        self.personalities_table.add_global_secondary_index(
            index_name="name-index",
            partition_key=dynamodb.Attribute(
                name="personality_name",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.KEYS_ONLY,
        )

    def _create_qa_pairs_table(self) -> None:
        """Create QAPairs table for session Q&A tracking."""
        self.qa_pairs_table = dynamodb.Table(
            self,
            "QAPairsTable",
            table_name=f"{self.env_name}-QAPairs",
            partition_key=dynamodb.Attribute(
                name="qa_pair_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

        self.qa_pairs_table.add_global_secondary_index(
            index_name="session-index",
            partition_key=dynamodb.Attribute(
                name="session_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

        self.qa_pairs_table.add_global_secondary_index(
            index_name="project-index",
            partition_key=dynamodb.Attribute(
                name="project_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_suggested_questions_table(self) -> None:
        """Create SuggestedQuestions table for AI-generated questions."""
        self.suggested_questions_table = dynamodb.Table(
            self,
            "SuggestedQuestionsTable",
            table_name=f"{self.env_name}-SuggestedQuestions",
            partition_key=dynamodb.Attribute(
                name="question_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

        self.suggested_questions_table.add_global_secondary_index(
            index_name="session-index",
            partition_key=dynamodb.Attribute(
                name="session_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_skills_table(self) -> None:
        """Create Skills table for agent skill definitions."""
        self.skills_table = dynamodb.Table(
            self,
            "SkillsTable",
            table_name=f"{self.env_name}-Skills",
            partition_key=dynamodb.Attribute(
                name="skill_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

        # Existing GSI in AWS - keep for now
        self.skills_table.add_global_secondary_index(
            index_name="agent-index",
            partition_key=dynamodb.Attribute(
                name="agent_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

        self.skills_table.add_global_secondary_index(
            index_name="name-index",
            partition_key=dynamodb.Attribute(
                name="skill_name",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.KEYS_ONLY,
        )



    def _create_agent_skills_table(self) -> None:
        """Create AgentSkills junction table for many-to-many agent-skill assignments."""
        self.agent_skills_table = dynamodb.Table(
            self,
            "AgentSkillsTable",
            table_name=f"{self.env_name}-AgentSkills",
            partition_key=dynamodb.Attribute(
                name="agent_id",
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name="skill_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
        )

        self.agent_skills_table.add_global_secondary_index(
            index_name="skill-index",
            partition_key=dynamodb.Attribute(
                name="skill_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_gap_analysis_results_table(self) -> None:
        """Create GapAnalysisResults table for persisting gap analysis."""
        self.gap_analysis_results_table = dynamodb.Table(
            self,
            "GapAnalysisResultsTable",
            table_name=f"{self.env_name}-GapAnalysisResults",
            partition_key=dynamodb.Attribute(
                name="session_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
            point_in_time_recovery=self.env_config.get("point_in_time_recovery", False),
        )

    def _create_kb_documents_table(self) -> None:
        """Create KbDocuments table for tracking knowledge base uploads."""
        self.kb_documents_table = dynamodb.Table(
            self,
            "KbDocumentsTable",
            table_name=f"{self.env_name}-KbDocuments",
            partition_key=dynamodb.Attribute(
                name="document_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
        )

        self.kb_documents_table.add_global_secondary_index(
            index_name="project-index",
            partition_key=dynamodb.Attribute(
                name="project_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_agent_config_history_table(self) -> None:
        """Create AgentConfigHistory table for versioned agent config snapshots."""
        self.agent_config_history_table = dynamodb.Table(
            self,
            "AgentConfigHistoryTable",
            table_name=f"{self.env_name}-AgentConfigHistory",
            partition_key=dynamodb.Attribute(
                name="agent_id",
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name="version",
                type=dynamodb.AttributeType.NUMBER,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
        )

    def _create_opensearch_domain(self) -> None:
        """Create OpenSearch domain for vector storage (KB and skills)."""
        self.opensearch_domain = opensearch.Domain(
            self,
            "KbVectorsDomain",
            domain_name=f"{self.env_name}-kb-vectors",
            version=opensearch.EngineVersion.OPENSEARCH_2_11,
            capacity=opensearch.CapacityConfig(
                data_node_instance_type=self.env_config.get("opensearch_instance_type", "t3.small.search"),
                data_nodes=self.env_config.get("opensearch_data_nodes", 1),
                multi_az_with_standby_enabled=False,
            ),
            ebs=opensearch.EbsOptions(
                enabled=True,
                volume_size=self.env_config.get("opensearch_ebs_volume_size", 20),
                volume_type=ec2.EbsDeviceVolumeType.GP3,
            ),
            removal_policy=self.env_config.get("removal_policy", RemovalPolicy.DESTROY),
        )

    def _create_exports(self) -> None:
        CfnOutput(
            self,
            "UsersTableName",
            value=self.users_table.table_name,
            export_name=f"AXRAIL-UsersTableName-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "UsersTableArn",
            value=self.users_table.table_arn,
            export_name=f"AXRAIL-UsersTableArn-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "ProjectsTableName",
            value=self.projects_table.table_name,
            export_name=f"AXRAIL-ProjectsTableName-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "ProjectsTableArn",
            value=self.projects_table.table_arn,
            export_name=f"AXRAIL-ProjectsTableArn-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "ProjectUsersTableName",
            value=self.project_users_table.table_name,
            export_name=f"AXRAIL-ProjectUsersTableName-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "ProjectUsersTableArn",
            value=self.project_users_table.table_arn,
            export_name=f"AXRAIL-ProjectUsersTableArn-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "SessionsTableName",
            value=self.sessions_table.table_name,
            export_name=f"AXRAIL-SessionsTableName-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "SessionsTableArn",
            value=self.sessions_table.table_arn,
            export_name=f"AXRAIL-SessionsTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "TranscriptsTableName",
            value=self.transcripts_table.table_name,
            export_name=f"AXRAIL-TranscriptsTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "TranscriptsTableArn",
            value=self.transcripts_table.table_arn,
            export_name=f"AXRAIL-TranscriptsTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "BotCredentialsTableName",
            value=self.bot_credentials_table.table_name,
            export_name=f"AXRAIL-BotCredentialsTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "BotCredentialsTableArn",
            value=self.bot_credentials_table.table_arn,
            export_name=f"AXRAIL-BotCredentialsTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "BotPoolTableName",
            value=self.bot_pool_table.table_name,
            export_name=f"AXRAIL-BotPoolTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "BotPoolTableArn",
            value=self.bot_pool_table.table_arn,
            export_name=f"AXRAIL-BotPoolTableArn-{self.env_name}",
        )

        # D2 table exports
        CfnOutput(
            self,
            "AgentsTableName",
            value=self.agents_table.table_name,
            export_name=f"AXRAIL-AgentsTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "AgentsTableArn",
            value=self.agents_table.table_arn,
            export_name=f"AXRAIL-AgentsTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "PersonalitiesTableName",
            value=self.personalities_table.table_name,
            export_name=f"AXRAIL-PersonalitiesTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "PersonalitiesTableArn",
            value=self.personalities_table.table_arn,
            export_name=f"AXRAIL-PersonalitiesTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "QAPairsTableName",
            value=self.qa_pairs_table.table_name,
            export_name=f"AXRAIL-QAPairsTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "QAPairsTableArn",
            value=self.qa_pairs_table.table_arn,
            export_name=f"AXRAIL-QAPairsTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "SuggestedQuestionsTableName",
            value=self.suggested_questions_table.table_name,
            export_name=f"AXRAIL-SuggestedQuestionsTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "SuggestedQuestionsTableArn",
            value=self.suggested_questions_table.table_arn,
            export_name=f"AXRAIL-SuggestedQuestionsTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "SkillsTableName",
            value=self.skills_table.table_name,
            export_name=f"AXRAIL-SkillsTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "SkillsTableArn",
            value=self.skills_table.table_arn,
            export_name=f"AXRAIL-SkillsTableArn-{self.env_name}",
        )

        # GapAnalysisResults table exports
        CfnOutput(
            self,
            "AgentSkillsTableName",
            value=self.agent_skills_table.table_name,
            export_name=f"AXRAIL-AgentSkillsTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "AgentSkillsTableArn",
            value=self.agent_skills_table.table_arn,
            export_name=f"AXRAIL-AgentSkillsTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GapAnalysisResultsTableName",
            value=self.gap_analysis_results_table.table_name,
            export_name=f"AXRAIL-GapAnalysisResultsTableName-{self.env_name}",
        )

        CfnOutput(
            self,
            "GapAnalysisResultsTableArn",
            value=self.gap_analysis_results_table.table_arn,
            export_name=f"AXRAIL-GapAnalysisResultsTableArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "KbDocumentsTableName",
            value=self.kb_documents_table.table_name,
            export_name=f"AXRAIL-KbDocumentsTableName-{self.env_name}",
        )
        CfnOutput(
            self,
            "KbDocumentsTableArn",
            value=self.kb_documents_table.table_arn,
            export_name=f"AXRAIL-KbDocumentsTableArn-{self.env_name}",
        )

        # OpenSearch exports
        CfnOutput(
            self,
            "OpenSearchDomainEndpoint",
            value=self.opensearch_domain.domain_endpoint,
            export_name=f"AXRAIL-OpenSearchDomainEndpoint-{self.env_name}",
        )

        CfnOutput(
            self,
            "OpenSearchDomainArn",
            value=self.opensearch_domain.domain_arn,
            export_name=f"AXRAIL-OpenSearchDomainArn-{self.env_name}",
        )
