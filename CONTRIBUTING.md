# Contributing

## Branch Strategy

- `main` — production-ready code
- `dev` — integration branch for active development
- Feature branches: `feature/{description}`
- Bugfix branches: `fix/{description}`

## Pull Request Guidelines

1. Create a feature or fix branch from `dev`
2. Keep PRs focused on a single change
3. Include documentation updates for any new features or API changes
4. Ensure all unit tests pass: `pytest tests/unit/ -v`
5. Run CDK synth to validate infrastructure: `npx cdk synth`

## Code Standards

- Python Lambda code follows the conventions in `.kiro/steering/coding-standards.md`
- CDK infrastructure follows `.kiro/steering/architecture-patterns.md`
- All Lambdas use AWS Powertools for logging and tracing
- CRUD handlers follow the standard response envelope pattern
- Timestamps use `datetime.now(timezone.utc)` (not `datetime.utcnow()`)

## Testing

- Unit tests live in `tests/unit/`
- Integration test scripts live in `scripts/`
- See `.kiro/steering/testing-standards.md` for test conventions
- Run unit tests: `pytest tests/unit/ -v`
- Run integration tests after deployment: see `docs/runbooks/end-to-end-tests.md`

## Documentation

- Follow the Docs-as-Code approach in `.kiro/steering/documentation-guide.md`
- Update docs in the same PR as code changes
- Use Mermaid for diagrams, Markdown for prose
- ADRs go in `docs/architecture/adr/`
