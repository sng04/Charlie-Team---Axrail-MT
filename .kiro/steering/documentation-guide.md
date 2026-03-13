---
inclusion: auto
name: documentation-guide
description: Guide for writing technical documentation. Only use when prompted to generate or review techical documentation for a project.
---
# Documentation Standards & Best Practices

## 1. Core Philosophy: Docs-as-Code
Documentation is a first-class citizen in this project. We adhere strictly to the **Docs-as-Code** philosophy:
- Documentation lives in the same Git repository as the source code.
- Documentation updates must be included in the same Pull Request (PR) as the code changes they describe.
- A PR without updated documentation for new features or altered architecture will not be approved.

## 2. Standard Formats
- **Prose & Guides:** Markdown (`.md`).
- **Diagrams:** [Mermaid.js](https://mermaid.js.org/) embedded directly inside Markdown files (avoids outdated, uneditable `.png` or `.jpg` files).
- **API Specifications:** OpenAPI 3.0+ (`.yaml`).

## 3. Standard Repository Structure
All repositories must follow this documentation hierarchy at the root level:

```text
<repository_root>/
├── README.md                 # Project entry point (Setup, installation, quickstart)
├── CONTRIBUTING.md           # Guidelines for branching, PRs, and code formatting
└── docs/                     # Comprehensive documentation directory
    ├── architecture/         # High-level architecture and data flow diagrams
    │   └── adr/              # Architecture Decision Records (ADRs)
    ├── api/                  # OpenAPI specs and Postman collections
    ├── runbooks/             # Incident management and operational guides
    └── product/              # Product requirements, PRDs, and user personas
```

## 4. Required Document Types

### 4.1. Architecture Decision Records (ADRs)
Whenever a significant architectural change is made (e.g., "Switching from RDS to DynamoDB" or "Implementing multi-repo CI/CD"), an ADR must be created in `docs/architecture/adr/`.
**Required ADR Format:**
- **Title:** Short noun phrase.
- **Context:** What is the problem we are trying to solve?
- **Decision:** What is the change we are making?
- **Consequences:** What becomes easier? What becomes harder? (Trade-offs).

### 4.2. Runbooks (Operational Guides)
Every critical background job, CI/CD pipeline, and automated process must have a corresponding Runbook in `docs/runbooks/`.
**Required Runbook Sections:**
- **Trigger:** How and when does this process run?
- **Expected Outcome:** What should happen if it succeeds?
- **Failure Scenarios:** What are the known failure modes?
- **Resolution Steps:** Step-by-step commands to mitigate or fix the failure.

### 4.3. API Documentation
Do not document API routes manually in Markdown.
- All REST APIs must be defined using an OpenAPI `swagger.yaml` file.
- The OpenAPI spec serves as the single source of truth and should be used to generate Postman collections or static API pages.

## 5. Writing Guidelines
- **Keep it DRY (Don't Repeat Yourself):** Avoid duplicating information. Link to other Markdown files instead of copying content.
- **Assume Context is Lost:** Write documentation assuming the reader is a new hire who just joined the team today. Define acronyms and avoid assumed institutional knowledge.
- **Maintainability over Perfection:** A short, accurate bulleted list is infinitely better than a perfectly formatted, multi-page document that is out of date.
- **Code Blocks:** Always specify the language in Markdown code blocks for syntax highlighting (e.g., ` ```python `, ` ```bash `, ` ```json `).