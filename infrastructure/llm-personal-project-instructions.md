## Master CV Personal Project Consolidation — Instruction Set

### Objective

You are documenting a **personal project** as a private, canonical “master career record” artefact: a long-lived, non-optimised, factual source of truth that can later be selectively mined when tailoring CVs.

Your task is to produce a **single comprehensive Markdown file** describing one specific project in exhaustive, non-promotional detail. The result should be **too honest and too detailed to comfortably send to a recruiter**.

This is not a README rewrite. It is a consolidation of everything discoverable from the repository (code, docs, commits, issues if present) plus any user-provided notes.

---

## Inputs you should use

Use only what is actually present in the loaded project workspace and/or explicitly provided by the user:

- Existing docs: `README*`, `docs/`, ADRs, design notes, comments
- Code structure: `src/`, `packages/`, `apps/`, `services/`, etc.
- Configuration: build tooling, CI config, deploy config, Docker/K8s, scripts
- Dependency manifests: `package.json`, `pyproject.toml`, `go.mod`, etc.
- Tests and test tooling
- Runtime/deploy targets (where observable)

If something is unknown, say so explicitly.

---

## Canonical authority rules

- The repository is canonical for technologies, architecture, and workflows (what you can actually see).
- User notes are canonical for intent, context, and history **only when clearly labeled as such**.
- Never invent missing details (e.g., "uses Postgres" if no evidence exists).

---

## Non-negotiable constraints

- Never reduce, summarise, or compress discoverable detail; deduplicate only truly identical statements.
- Do not optimise for hiring; avoid hype, framing, or evaluation language.
- Preserve ambiguity and uncertainty explicitly.
- Distinguish influence vs. authority if collaboration is involved.

---

## Output location

Create the resulting file in this master-career-record repository under:

- `profile/personal-projects/YYYY-MM-<project-slug>.md`

Use the project’s start date if known. If not known, use the current month as a placeholder date and note the uncertainty in the document.

---

## Output format (strict)

### 1. YAML Frontmatter (mandatory, exact structure)

Use this structure exactly, leaving unknown fields empty:

```yaml
---
project_id:
name:
type:
status:
start:
end:
repo:
location:
domain:
keywords:
---
```

Rules:
- `project_id` must be stable, descriptive, filesystem-safe
- `keywords` must be a single-line array of kebab-case strings
- Include only technologies/practices that are evidenced in the repo or explicitly provided
- Dates must be `yyyy-mm` when known

### 2. Project header (immediately after frontmatter)

Immediately after the YAML frontmatter, render a single H1 header in this format:

```markdown
# <Project Name> — Personal Project (<Start Month Year> – <End Month Year>)
```

If dates are unknown, use `Unknown` and explain in the Snapshot.

### 3. Snapshot (immediately after project header)

Immediately following the project header:

```markdown
## Snapshot
```

The Snapshot should concisely state:
- What the project is
- Why it exists (problem statement)
- What “done” means (if applicable)
- Current status (active, paused, archived)

---

## Required sections (in this order)

### Context & constraints

Describe constraints that shaped decisions, such as:
- Time available, solo vs. collaborative
- Target users or environment constraints
- Legacy compatibility constraints
- Hosting/cost constraints

### Goals & non-goals

Document explicit goals and explicit non-goals where evidenced.

### User journeys / use-cases

Describe the primary usage patterns and who/what uses the system.

### Architecture overview

- Top-level architecture and component boundaries
- Data flows between components
- Trust boundaries and security boundaries (if relevant)

Include concrete references to repo structure (e.g., directories, packages) when helpful.

### Key components

For each major component/module:
- Purpose
- Public interfaces (APIs, CLIs, UI routes, events)
- Internal responsibilities
- Failure modes and error handling approach (as implemented)

### Data model & persistence

- What data exists and where it lives
- Schemas, migrations, versioning, or storage formats
- Backup/restore or export/import if present

### Integrations

- External services/APIs
- Auth providers, webhooks, third-party SDKs
- Local dev substitutes/mocks if present

### Development workflow

Document what a contributor does in practice:
- Setup steps (what files/commands exist)
- Build commands
- Test commands
- Lint/format commands
- Debugging approach (if evidenced)

Prefer listing actual scripts/commands discovered in the repo.

### Deployment & operations

- Where/how it runs (local, container, serverless, cloud)
- Release process (if present)
- CI/CD pipelines (if present)
- Monitoring/logging/alerting (if present)

### Security & privacy (if applicable)

- Authn/authz model
- Sensitive data handling
- Secrets management approach

Only include what is evidenced.

### Performance & scaling (if applicable)

- Known bottlenecks and mitigations
- Load characteristics (if known)

### Notable decisions & trade-offs

For each significant decision:
- Problem
- Options considered (if known)
- Decision
- Trade-offs

### Change history & status

- Major rewrites, migrations, milestones (as evidenced)
- Current state (active/paused/archived) and why

### Tech & skills used

A comprehensive list, grouped logically:
- Languages
- Frameworks/libraries
- Tooling
- Infrastructure
- Practices (testing approaches, CI patterns, etc.)

### Stakeholders & collaboration

- If solo: say so
- If not solo: who contributed, and your role vs. others
- Explicitly distinguish influence from authority

### Positioning notes

Meta-notes for future interpretation, such as:
- What this project does and does not demonstrate
- Which parts are experimental vs. production-grade

---

## Output expectation

If done correctly, the document should read like a forensic reconstruction of the project: comprehensive, neutral, and reusable as a long-term memory aid.

When you are ready, ask the user to provide any missing context that is not discoverable from the repository (e.g., start date, intent, constraints, why it was built).
