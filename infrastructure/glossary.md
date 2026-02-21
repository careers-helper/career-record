# Career Record Glossary and Standards

This file defines shared conventions used by repository tooling and AI workflows.

## Folder naming

### Output (application) folders

- Pattern: `YYYYMMDD-company-role`
- Example: `20260214-bbc-staff-engineer`
- Lives under `output/`

### Profile files

- Pattern: `YYYY-MM-descriptor.md`
- Applies to `profile/work-experience/` and `profile/personal-projects/`

## Role status markers

Application folders in `output/` must contain exactly one empty status file.

Allowed stage tokens:

- `_REVIEW`
- `_NOAPP`
- `_APP`
- `_INT`
- `_OFF`
- `_ACC`
- `_REJ`
- `_WDR`

Compound statuses join stage tokens with underscores, for example:

- `_APP_INT_REJ`
- `_APP_INT_WDR`
- `_APP_INT_OFF_ACC`

## Frontmatter normalisation

### Personal projects

`type` must be:

- `personal-project`

### Locations

Prefer one style per location over time, and avoid introducing near-duplicates unless meaningfully different (for example, `London, UK` vs `London, United Kingdom`).

### Keywords

- Use kebab-case
- Avoid duplicates that differ only by regional spelling unless both spellings are intentionally required
- Fix obvious typos when found

## Role file format

For all new and updated files under `profile/work-experience/`:

- H1 format: `# Role: <Company> — <Title> (<Start Month Year> – <End Month Year>)`
- Snapshot format: `## Snapshot` followed by exactly four bullets:
	- `**One-liner:**`
	- `**Scope:**`
	- `**Team / org context:**`
	- `**What success looked like:**`

Legacy prose snapshots are acceptable for untouched historical files, but should be normalised when a file is materially revised.

## Repository layout

The three functional top-level folders form a workflow pipeline:

| Folder | Purpose |
|--------|---------|
| `inbox/` | Temporary staging area for unprocessed job descriptions (any readable format) |
| `profile/` | User-owned career data, read when generating CVs and assessing fit |
| `output/` | Everything produced from processing a job application |

### profile/ subfolders

| Subfolder | Contents |
|-----------|---------|
| `profile/work-experience/` | Employment history (`YYYY-MM-descriptor.md`, one per role) |
| `profile/personal-projects/` | Personal project documentation (`YYYY-MM-descriptor.md`, one per project) |
| `profile/cross-cutting/` | Experience spanning multiple roles (AI usage, speaking, mentoring) |
| `profile/articles/` | Published articles and writing |
| `profile/job-preferences.md` | Personal job fit preferences (user-maintained; read by AI when screening) |

### output/ application folder contents

Each `output/YYYYMMDD-company-role/` folder contains:

| File | Description |
|------|-------------|
| `job-description.<ext>` | Original job posting (moved here from `inbox/` during triage; extension preserved) |
| `suitability.md` | AI-generated fit assessment |
| `cv.md` | AI-generated tailored CV (Markdown source) |
| `cv.docx` | AI-generated tailored CV (Word output) |
| `automated-review.md` | AI-generated recruiter-perspective CV review |
| `_<STATUS>` | Application status marker (empty file) |

## Repository checks

The lint script validates these conventions:

- role folder naming
- role status file presence and format
- personal project `type` frontmatter value
- obvious keyword issues (duplicate keyword entries and selected typo patterns)
- role header and snapshot format drift (warning-level)

Run with:

- `pnpm lint:career-record`
- `pnpm lint:career-record:strict`
