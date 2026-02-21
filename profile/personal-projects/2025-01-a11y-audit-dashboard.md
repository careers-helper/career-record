---
project_id: a11y-audit-dashboard
name: a11y-audit-dashboard
type: personal-project
status: active
start: 2025-01
end:
repo: https://github.com/elenavasquezuk/a11y-audit-dashboard
location: N/A
domain: accessibility tooling
keywords: [accessibility, wcag, react, nextjs, typescript, tailwind, sqlite, axe-core, audit, dashboard]
---
# a11y-audit-dashboard — Personal Project (January 2025 – Present)

## Snapshot

A lightweight web dashboard for tracking accessibility audit results across multiple applications over time. Built to replace the spreadsheet-based WCAG compliance tracking Elena was doing during the Aegon migration, where monitoring 15 applications manually was tedious and error-prone. The tool ingests axe-core JSON reports, categorises violations, tracks remediation status, and displays trend data. Currently functional but rough — used personally for Aegon migration tracking. Not yet published as open source. Approximately 20 hours of development time invested as of February 2026.

## Context & constraints

- Solo personal project, developed in spare time alongside full-time employment.
- Time-constrained: approximately 20 hours invested total, spread across evenings and weekends since January 2025.
- Originated from a real workflow problem: tracking WCAG compliance across 15 applications during the Aegon migration using spreadsheets was error-prone and difficult to maintain.
- Single-user tool — Elena is currently the only user.
- No budget for hosting beyond an existing personal VPS.
- No requirement for multi-tenancy, high availability, or enterprise features.

## Goals & non-goals

**Goals:**
- Replace spreadsheet-based accessibility tracking with a structured, queryable tool.
- Ingest axe-core JSON reports and persist violation data over time.
- Visualise accessibility trends per application and per WCAG criterion.
- Track remediation status of individual violations.
- Generate summary reports suitable for sharing with stakeholders.

**Non-goals:**
- Not intended as a SaaS product or commercial offering.
- Not attempting to replace axe-core or other scanning tools — this is a reporting and tracking layer only.
- Multi-user authentication is not currently a goal (acknowledged as a backlog item but not prioritised).
- Real-time scanning or browser extension functionality is out of scope.

## User journeys / use-cases

1. **Manual report upload:** Elena runs axe-core against an application (or receives a report from a CI pipeline), exports the JSON, and uploads it via the dashboard's upload interface. The report is parsed, violations are extracted and stored, and the dashboard updates to reflect the new data.
2. **Violation triage:** Elena reviews newly ingested violations, categorised by WCAG criterion, severity, and component. She assigns a remediation status to each (open, in progress, resolved, won't fix).
3. **Trend review:** Elena views per-application accessibility scores over time via trend charts to identify whether compliance is improving or regressing.
4. **Stakeholder reporting:** Elena generates a summary report for a specific application or across all tracked applications, suitable for sharing with project stakeholders during the Aegon migration.
5. **Multi-project tracking:** The dashboard supports tracking multiple projects and organisations, allowing Elena to keep Aegon migration applications separate from other work.

**Planned but not yet implemented:**
- CI webhook integration: a CI pipeline would POST axe-core JSON directly to the dashboard, removing the manual upload step.

## Architecture overview

- **Next.js 14 (App Router)** serves as the full-stack framework, handling both the UI and API routes.
- **SQLite** (via better-sqlite3) provides persistence. The database file lives on the local filesystem.
- **Tailwind CSS** handles styling.
- **Recharts** provides data visualisation (trend charts, score summaries).
- A **custom axe-core report parser** extracts violations, passes, and metadata from axe JSON output and maps them to the internal data model.

Data flows:
1. Axe-core JSON report → upload endpoint (API route) → report parser → SQLite.
2. Dashboard pages (Server Components) → SQLite queries → rendered views with Recharts charts.
3. Summary report generation → SQLite aggregate queries → formatted output.

There are no external service dependencies. The application is self-contained.

## Key components

### Report parser
- **Purpose:** Transforms raw axe-core JSON output into the dashboard's internal violation model.
- **Interface:** Accepts an axe-core JSON object; returns structured violation records ready for database insertion.
- **Responsibilities:** Extracts violation ID, description, WCAG criteria tags, severity (impact level), affected DOM nodes, and help URL. Maps axe-core's structure to the dashboard's schema.
- **Error handling:** Limited. Malformed reports may cause unhandled errors — this is a known gap.

### Report upload API route
- **Purpose:** Accepts axe-core JSON reports via HTTP POST (file upload).
- **Interface:** Next.js API route accepting multipart form data.
- **Responsibilities:** Receives the uploaded file, passes it to the report parser, writes parsed violations to SQLite, and associates the report with a project.
- **Error handling:** Basic validation that the uploaded file is JSON. No robust handling of malformed axe-core output.

### Dashboard views (Server Components)
- **Purpose:** Display per-application accessibility scores, violation breakdowns, and trend charts.
- **Interface:** Next.js pages using the App Router. Server Components query SQLite directly.
- **Responsibilities:** Aggregate queries for scores and trends, render Recharts charts, display violation tables with remediation status.

### Remediation tracker
- **Purpose:** Allows the user to update the status of individual violations.
- **Interface:** UI controls on the violation detail view (open → in progress → resolved / won't fix).
- **Responsibilities:** Updates violation status in SQLite.

### Summary report generator
- **Purpose:** Produces a formatted summary of accessibility status for stakeholder review.
- **Interface:** Accessible via the dashboard UI.
- **Responsibilities:** Aggregates violation counts by severity and WCAG criterion, calculates compliance percentages, formats output for sharing.

## Data model & persistence

- **Database:** SQLite, accessed via better-sqlite3. Single file on the local filesystem.
- **Key entities:**
  - **Projects/organisations:** Logical grouping for tracked applications.
  - **Applications:** Individual applications being audited, belonging to a project.
  - **Reports:** Ingested axe-core report records, timestamped, linked to an application.
  - **Violations:** Individual accessibility violations extracted from reports, linked to a report and application. Fields include axe-core rule ID, description, WCAG criteria, severity/impact, affected nodes, help URL, and remediation status.
- **Schemas/migrations:** Not documented. It is unclear whether formal migration tooling is in place or whether schema changes are applied manually.
- **Backup/restore:** No evidence of automated backup. The SQLite file can be copied manually.
- **Export/import:** Summary reports can be generated. No evidence of a full data export/import mechanism.

## Integrations

- **axe-core:** The dashboard consumes axe-core JSON report output. It does not run axe-core itself — reports are generated externally and uploaded.
- **CI webhook (planned, not implemented):** Intended to accept POST requests from CI pipelines containing axe-core JSON output. Currently, all reports are uploaded manually.
- No authentication providers, third-party SDKs, or external APIs are used.

## Development workflow

- **Language/framework:** TypeScript, Next.js 14 (App Router).
- **Dev server:** Next.js development server (`npm run dev` or equivalent).
- **Testing:** Vitest. Test coverage is limited — mostly integration tests for the report parser. No evidence of end-to-end or UI tests.
- **Linting/formatting:** Not documented. Likely present via Next.js defaults but not confirmed.
- **CI:** None. Development is entirely local.
- **Debugging:** No specific debugging tooling documented.

## Deployment & operations

- **Hosting:** Personal VPS.
- **Containerisation:** Docker Compose. The application and its SQLite database run in a container.
- **Release process:** No formal release process. Likely deployed via manual `docker compose up` or equivalent.
- **CI/CD:** None.
- **Monitoring/logging/alerting:** None documented.

## Notable decisions & trade-offs

### SQLite over PostgreSQL
- **Problem:** Needed a database for persisting audit data.
- **Options considered:** PostgreSQL, SQLite.
- **Decision:** SQLite via better-sqlite3.
- **Trade-offs:** Zero-dependency deployment (no separate database server), simpler operations, single-file backup. Limits future multi-user or concurrent-write scenarios. Acceptable because this is a single-user personal tool, not a SaaS product.

### Next.js App Router over Pages Router
- **Problem:** Chose a framework for the dashboard UI.
- **Options considered:** Next.js Pages Router (familiar), Next.js App Router (newer).
- **Decision:** App Router.
- **Trade-offs:** Wanted to learn the new patterns. Server Components are used for data-heavy dashboard views, which suits the read-heavy nature of the dashboard. App Router was relatively new at the time, so some patterns were less well-documented.

### No authentication
- **Problem:** Whether to implement user authentication.
- **Decision:** No authentication. The application runs behind a VPN or locally.
- **Trade-offs:** Simplifies development and deployment significantly. Prevents sharing the tool with others or deploying it publicly. Adding authentication is on the backlog but has not been prioritised.

### Manual report upload over automated ingestion
- **Problem:** How to get axe-core reports into the dashboard.
- **Decision:** Manual file upload initially, with CI webhook integration planned.
- **Trade-offs:** Faster to implement. Adds friction to the workflow — Elena must manually export and upload reports. The CI webhook would remove this friction but has not been built yet.

## Change history & status

- **January 2025:** Project started. Core functionality built: report ingestion, violation storage, basic dashboard views.
- **Status as of February 2026:** Active but development is sporadic. Core features (report ingestion, violation tracking, trend charts, summary reports) are functional. The tool is used personally for Aegon migration tracking. Key gaps remain: CI webhook integration, multi-user authentication, robust error handling for malformed reports. Elena is considering open-sourcing the project but has not done so yet.

## Tech & skills used

**Languages:**
- TypeScript

**Frameworks & libraries:**
- Next.js 14 (App Router)
- React (Server Components and Client Components)
- Tailwind CSS
- Recharts
- better-sqlite3

**Tooling:**
- Vitest (testing)
- Docker, Docker Compose (containerisation and deployment)
- Node.js

**Infrastructure:**
- Personal VPS
- SQLite

**Practices:**
- Integration testing (limited, focused on report parser)
- Containerised deployment

## Stakeholders & collaboration

Solo project. Elena is the sole developer and only user. No external contributors.

## Positioning notes

- This project demonstrates a genuine interest in accessibility beyond compliance-driven requirements — Elena built it voluntarily to solve a real workflow problem.
- It also demonstrates willingness to build internal tooling to address practical pain points rather than accepting manual processes.
- The use of Next.js App Router with Server Components shows currency with modern React patterns.
- The project is smaller and less polished than react-migrator. It is a personal utility, not a portfolio piece.
- Most appropriate to surface on CVs where accessibility is a meaningful part of the job description.
- The tool is functional but rough — it should not be presented as production-grade or open-source-ready.
- Test coverage is limited and there is no CI pipeline; these are acknowledged gaps, not oversights.
