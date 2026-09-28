# AI Agent Instructions: Master Career Record

> **This is the shared instruction file for all AI assistants working on this repository.**

## Purpose

This is a **private master career record**, not a portfolio or CV. User profile data (career record, articles, job preferences) live in `profile/`; job application outputs live in `output/` (one folder per application); incoming job descriptions are staged in `inbox/`.

## Repository Structure

```
.
├── infrastructure/                            # Instruction specs, templates, and scripts
│   ├── cv-generation-instructions.md              # CV generation rules (JD in, Word-ready CV out)
│   ├── generate-cv-docx.py                        # Markdown → styled docx (Pandoc + post-processing)
│   ├── llm-role-instructions.md                   # Complete spec for creating/updating work experience files
│   ├── llm-personal-project-instructions.md       # Complete spec for creating/updating personal project files
│   ├── sample-cv.docx                             # CV style reference (Word)
│   ├── sample-cv.md                               # CV structure template (Markdown)
│   └── job-screening-instructions.md              # Job screening rubric and output format
├── profile/                                   # User profile data
│   ├── work-experience/                           # Employment history (roles you've held)
│   │   └── YYYY-MM-<descriptor>.md                # One file per role
│   ├── personal-projects/                         # Personal project documentation
│   │   └── YYYY-MM-<descriptor>.md                # One file per project
│   ├── cross-cutting/                             # Experience spanning multiple roles
│   │   └── ai-usage.md                            # Cross-cutting AI tool usage
│   ├── articles/                                  # Published articles and writing
│   │   └── YYYY-MM-<descriptor>.md                # One file per article
│   └── job-preferences.md                         # Personal job fit preferences
├── inbox/                                     # Drop zone for unprocessed job descriptions
│   └── *                                          # Any readable format: PDF, image, Markdown, Word
├── output/                                    # Job application outputs (one folder per application)
│   └── YYYYMMDD-<company>-<role>/                 # One folder per application
│       ├── job-description.<ext>                  # Original job description (extension preserved)
│       ├── suitability.md                         # Job fit assessment ("is this right for me?")
│       ├── cv.md                                  # Tailored CV (Markdown source)
│       ├── cv.docx                                # Tailored CV (Word output)
│       ├── automated-review.md                    # Recruiter-perspective CV review
│       ├── _<STATUS>                              # Status (empty file) — see "Application Status" below
│       └── interviews/                            # Optional: interview prep materials
├── .github/                                   # GitHub-specific configuration
│   └── copilot-instructions.md                    # GitHub Copilot pointer
├── AGENTS.md                                  # This file (shared AI instructions; Claude Code + Codex)
└── .cursorrules                               # Cursor pointer
```

## Critical Pattern: Non-Optimised Truth

**Key principle:** These files are intentionally comprehensive and non-promotional. They:
- Preserve ALL distinct details from multiple source descriptions (LinkedIn, CVs, personal notes)
- Are explicitly "too honest and too detailed to comfortably send to a recruiter"
- Distinguish between influence and authority (i.e. highlight line management when required; highlight influencing peers or non-reports when required)
- Use declarative, neutral language without hype or persuasion

## Creating/Updating Experience Files

- **Employment history:** Follow [infrastructure/llm-role-instructions.md](llm-role-instructions.md) for the complete specification (frontmatter, sections, language rules, conflict resolution).
- **Personal projects:** Follow [infrastructure/llm-personal-project-instructions.md](llm-personal-project-instructions.md) for the complete specification.

## Application Status

Each role folder contains a single empty status file whose name tracks the application journey using abbreviated, compound stages:

| Abbreviation | Meaning |
|---|---|
| `_REVIEW` | Just generated, awaiting user review (temporary; removed once reviewed) |
| `_NOAPP` | Reviewed, decided not to apply (terminal) |
| `_APP` | Application submitted |
| `_INT` | Interviewing |
| `_OFF` | Offered |
| `_ACC` | Accepted |
| `_REJ` | Rejected by company (terminal) |
| `_WDR` | Withdrew (terminal) |

Stages are joined with underscores to show the journey, e.g.:
- `_APP_INT_WDR` — applied, interviewed, then withdrew
- `_APP_INT_REJ` — applied, interviewed, then rejected
- `_APP_INT_OFF_ACC` — applied, interviewed, offered, accepted

Only one status file exists per role folder at any time. When the status advances, rename the file (e.g. `_APP` → `_APP_INT`).

## Processing Job Applications

**New applications:** Drop the job description in `inbox/` (any readable format: PDF, image, Markdown, or Word) and use the Inbox Batch Workflow below to triage and generate CVs.

**For a role already in `output/`** (after inbox triage):
- To generate or regenerate a CV: follow [infrastructure/cv-generation-instructions.md](cv-generation-instructions.md).
- To screen for fit or re-run a suitability assessment: read `profile/job-preferences.md` and [infrastructure/job-screening-instructions.md](job-screening-instructions.md).

## Inbox Batch Workflow (Two-Pass)

When the user asks to **"review the inbox"** (or similar phrasing), process all job description files in the `inbox/` folder using a two-pass approach:

### Pass 1: Triage (suitability reports only)

1. List the contents of `inbox/` and identify all job description files (any readable format: PDF, image, Markdown, or Word document).
2. For each file:
   a. Parse the filename to determine the company name and role title.
   b. Create the appropriate folder under `output/` using the naming convention `YYYYMMDD-<company>-<role>/` (where the date is today's date).
   c. Move (not copy) the file from `inbox/` to the new folder, renaming it to `job-description.<ext>` (preserving the original file extension).
3. Generate a **suitability report** (`suitability.md`) for each role, following `profile/job-preferences.md` and [infrastructure/job-screening-instructions.md](job-screening-instructions.md). Process roles sequentially.
4. Present a summary table of all roles with their fit scores and recommendations so the user can decide which (if any) to proceed with.

### Pass 2: CV generation (on request)

After the user has reviewed the suitability reports and indicated which roles to pursue:

1. For each selected role, run the remaining steps of the standard workflow: generate the tailored CV (`cv.md` + `cv.docx`) and the recruiter-perspective review (`automated-review.md`), following [infrastructure/cv-generation-instructions.md](cv-generation-instructions.md).
2. Create an empty `_REVIEW` status file for each completed role.
3. Process roles sequentially (complete all artefacts for one role before starting the next).

## Example Role Files

- [profile/work-experience/2022-06-aegon-principal-frontend-engineer.md](../profile/work-experience/2022-06-aegon-principal-frontend-engineer.md): Enterprise migration architecture role with clear distinction between cross-team influence and team ownership
- [profile/work-experience/2020-01-kova-staff-frontend-engineer.md](../profile/work-experience/2020-01-kova-staff-frontend-engineer.md): Staff-level IC role establishing cross-team architectural direction without direct reports
- [profile/work-experience/2024-03-aegon-migration-lead.md](../profile/work-experience/2024-03-aegon-migration-lead.md): Evolution from pure IC to combined architectural ownership with small team leadership
