# Career Record Helper

A template repository for managing your career history and automating job applications using AI coding assistants. You maintain a comprehensive, private master record of your experience, then use LLM-powered agents to screen job descriptions, assess suitability, generate tailored CVs, and produce simulated recruiter reviews — all from a single conversational prompt.

One practical benefit is getting through AI gatekeepers without resorting to lies, keyword stuffing, or fake optimisation tricks. The point is to improve how your real experience is presented so your CV can truthfully say: this is who I am, and this is why I'd be great for your job.

> [!IMPORTANT]
> This repository ships with AI-generated sample content. "Elena Vasquez" and any other names, organisations, or contact details are placeholders. Replace all sample data with your own details before real use.

> [!TIP]
> Treat this repository as private data. Keep it in a private repo and avoid committing sensitive personal information unless you are comfortable storing it in git history.

## How it works

```mermaid
flowchart TD
    A["Your career record (profile/)"] --> C["AI agent reads both"]
    B["Job description (inbox/)"] --> C
    C --> D["Suitability report (suitability.md)"]
    C --> E["Tailored CV (cv.md + cv.docx)"]
    C --> F["Recruiter review (automated-review.md)"]
```

1. **Build your career record** — replace the sample data in `profile/` with your own work history, personal projects, articles, and job preferences.
2. **Drop in a job description** — save the job posting into the `inbox/` folder in any readable format: PDF, image (e.g. a screenshot), Markdown, or Word document.
3. **Ask your AI assistant to "review the inbox"** — the agent reads your career record, parses the job description, and generates three artefacts per role. In practice, this helps you shape a CV that is easier for both recruiters and automated screening systems to understand, while staying grounded in the facts of your record. How you trigger this depends on your tool:
   - **Claude Code (CLI):** run `claude` in the repo root and prompt `"Review the inbox and process all job descriptions"` or similar.
   - **GitHub Copilot or Codex in VSCode:** open the chat panel, set the context to this workspace, and send the same prompt
   - **Cursor:** open the repo and use Composer or Chat with the prompt above
   - **Agentic / automated workflow:** point a GitHub Actions job or any agentic runner at this private repo and issue the prompt programmatically

   The agent produces three artefacts per role:
   - **Suitability report** — a structured assessment of job fit against your stated preferences and experience
   - **Tailored CV** — a role-specific CV in Markdown and styled Word (.docx) format, drawn only from facts in your record
   - **Automated review** — a simulated recruiter critique of the generated CV against the job description
4. **Track your applications** — each role gets a folder under `output/` with a status file that records the application journey, for example `_APP_INT_OFF_ACC` (i.e. applied → interviewed → offered → accepted).

## Who this is for

Any software engineer who wants a repeatable application workflow, regardless of seniority (junior to principal/staff), stack, or specialisation. It is especially useful if you want help translating a detailed, truthful career history into a CV that survives automated screening without turning into fiction. The sample data in this repo is frontend-focused, but the structure is generic — adapt it by replacing the content and preference files.

## Supported AI tools

The repository ships with configuration files for:

- **GitHub Copilot** (`.github/copilot-instructions.md`)
- **Claude Code** and **OpenAI Codex** (`AGENTS.md`, read natively by both; `CLAUDE.md` imports it for older Claude Code versions)
- **Cursor** (`.cursorrules`)

`AGENTS.md` holds the shared instruction set and the Copilot and Cursor files point to it, so the workflow is consistent regardless of which tool you use. Claude Code reads `AGENTS.md` natively from version 2.1.277; the one-line `CLAUDE.md` (`@AGENTS.md`) covers earlier versions and Bedrock, Vertex and Foundry.

## Getting started

### Prerequisites

**Required — for CV docx generation:**

| Tool | Version | Why |
|------|---------|-----|
| [Python](https://www.python.org/) | 3.x | CV docx script runtime |
| [Pandoc](https://pandoc.org/) | latest | Markdown-to-Word conversion |
| [python-docx](https://python-docx.readthedocs.io/) | latest | Word document post-processing |

```bash
pip install python-docx
```

**Optional — only needed for linting and repo checks:**

| Tool | Version | Why |
|------|---------|-----|
| [Node.js](https://nodejs.org/) | 24.x | Script runtime for linting tools |
| [pnpm](https://pnpm.io/) | 10.x | Package manager |

### Setup

```bash
git clone <your-private-fork-or-repo>
cd career-record-helper
pnpm install  # optional — only needed for linting/spellcheck

# Replace sample data with your own
# - profile/work-experience/     → one file per role you've held
# - profile/personal-projects/   → one file per personal project
# - profile/cross-cutting/       → experience spanning multiple roles
# - profile/articles/            → published articles and writing
# - profile/job-preferences.md   → your job preferences and constraints
# - infrastructure/sample-cv.md  → your CV template with real contact details
```

### First run

1. Save one or more job descriptions into `inbox/` (PDF, image, Markdown, or Word).
2. Open this repo with your AI coding assistant. For example:
   - Run `claude` in the repo root (Claude Code CLI)
   - Open the folder in VSCode with the Copilot or Codex extension active
   - Open the folder in Cursor
3. Prompt: **"Review the inbox and process all job descriptions."**

The standard flow:
1. Create `output/<YYYYMMDD-company-role>/`
2. Generate `suitability.md`
3. (On request) generate `cv.md` and `cv.docx`
4. Generate `automated-review.md`
5. Create a status file like `_REVIEW`

## Repository structure

```
.
├── inbox/                     # Drop zone for unprocessed job descriptions (any readable format)
├── profile/                   # Your career record and preferences
│   ├── work-experience/       #   Employment history (one file per role)
│   ├── personal-projects/     #   Personal project documentation
│   ├── cross-cutting/         #   Experience spanning multiple roles
│   ├── articles/              #   Published articles and writing
│   └── job-preferences.md     #   Your job fit preferences and constraints
├── output/                    # Job applications (one folder per application)
│   └── YYYYMMDD-company-role/
│       ├── job-description.<ext>
│       ├── suitability.md
│       ├── cv.md
│       ├── cv.docx
│       ├── automated-review.md
│       └── _<STATUS>          #   Application status tracker
├── infrastructure/            # Instruction specs, templates, and tooling
│   ├── cv-generation-instructions.md # CV generation rules and workflow
│   ├── job-screening-instructions.md # Screening rubric and output format
│   ├── llm-role-instructions.md      # Spec for work experience file format
│   ├── llm-personal-project-instructions.md # Spec for personal project file format
│   ├── generate-cv-docx.py           # Markdown → styled .docx script
│   ├── sample-cv.md / .docx          # CV structure template and style reference
│   └── glossary.md                   # Naming conventions and standards
├── scripts/                   # Repository tooling (linting, validation)
├── AGENTS.md                  # Primary operating guide for AI agents
└── .github/ / CLAUDE.md / .cursorrules  # Copilot, Claude Code (fallback) and Cursor pointers to AGENTS.md
```

## Key docs

- `AGENTS.md` — primary operating guide for AI agents
- `infrastructure/cv-generation-instructions.md` — CV generation workflow
- `profile/job-preferences.md` — your job fit preferences (user-maintained)
- `infrastructure/job-screening-instructions.md` — screening rubric and output format
- `infrastructure/llm-role-instructions.md` — work experience file authoring standard
- `infrastructure/llm-personal-project-instructions.md` — personal project file standard
- `infrastructure/glossary.md` — naming conventions and terminology

## Customising CV styles

The file `infrastructure/sample-cv.docx` is the style reference for all generated CVs. When the docx generation script runs, it passes this file to Pandoc as the `--reference-doc`, so the Word styles defined in it are applied to every output CV.

The script maps CV elements to Word styles as follows:

| CV element | Word style |
|---|---|
| Candidate name | Title |
| Tagline (e.g. "Senior Software Engineer") | Subtitle |
| Contact details line | Quote |
| Section headings (Profile, Experience, Skills) | Heading 2 |
| Role titles | Heading 3 |
| Company, location, and dates | Heading 4 |
| Older role lines (title and dates only) | Heading 5 |
| Experience bullet points | List Paragraph |
| Profile and role description paragraphs | Normal |

To change how your CVs look:

1. Open `infrastructure/sample-cv.docx` in Word (or a compatible editor).
2. Modify the styles you want to change (e.g. update the font for Heading 3, change the colour of Subtitle, adjust margins).
3. Save the file.
4. Regenerate any CVs — the new styles will be picked up automatically.

> [!TIP]
> Edit the Word **styles** (via the Styles pane), not just the text formatting. Pandoc reads style definitions from the reference document, so direct formatting on sample text won't carry over.

## Useful commands

```bash
pnpm lint:career-record          # Structural checks (folder names, status files, frontmatter)
pnpm lint:career-record:strict   # Structural checks + warnings fail build
pnpm spellcheck                  # Markdown spell check
pnpm typecheck                   # TypeScript type check (repo scripts)
```
