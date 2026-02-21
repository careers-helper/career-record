# CV Generation Guide (Job Description → Word-Ready CV)

This file covers CV generation for roles that have already been triaged through the inbox workflow — that is, the `output/<id>/` folder already exists and contains a `job-description.*` file. The output is a tailored CV as both a Markdown source (`cv.md`) and a styled Word document (`cv.docx`), followed by a recruiter-perspective review.

For new applications, use the Inbox Batch Workflow in `infrastructure/agent-instructions.md`: drop the job description in `inbox/` (any readable format) and triage it first. CV generation is Pass 2 of that workflow.

## Generating a CV for a Triaged Role

When the user asks to generate or regenerate a CV for a role already in `output/`:

1. Search `output/` for a subfolder matching the company name or role (e.g., `output/20260214-aegon-principal-engineer/`)
2. If multiple matches are found or the match is unclear, prompt the user to clarify which application they mean
3. Read the `job-description.*` file in `output/<id>/` to extract requirements
4. Generate the CV as markdown and save it to `output/<id>/cv.md`
5. Run `python3 infrastructure/generate-cv-docx.py output/<id>/cv.md` to produce `output/<id>/cv.docx`
6. Generate a CV review (acting as the recruiter) and save it to `output/<id>/automated-review.md`
7. Create an empty `output/<id>/_REVIEW` status file (temporary; the user will rename to the appropriate compound status, e.g. `_APP`, `_NOAPP`)

**Why keep the markdown?** The `.md` file is the editable source: you can tweak bullets or fix typos in plain text, then re-run the docx script to regenerate. It is also version-control friendly.

**Requirements for docx generation:** `pandoc` (system install) and `python-docx` (`pip install python-docx`). The script uses `infrastructure/sample-cv.docx` as the reference for styling.

## Template

Use `infrastructure/sample-cv.md` as the template for structure and content format.

Use that file as the **single source of truth** for:
- Section order and headings
- Line breaks and spacing
- Typography choices (bold/italic usage)
- Role formatting and date line style

## Generation rules

- Prefer UK spelling.
- **Punctuation preference:** Avoid em-dashes (—) and hyphens (-) for parenthetical or explanatory content. Use commas or brackets instead. Hyphens are acceptable for compound modifiers (e.g., "real-time rendering"). Em-dashes are acceptable as separators in the older role title/date lines (e.g., `**Role (Company)** — _dates_`).
- The **Profile**, **Experience** bullets, **Skills**, and (optionally) **Personal Projects** are the parts that change.
- Keep the **Experience** order and job titles exactly as above.
- Use all of `profile/work-experience/*.md`, `profile/personal-projects/*.md`, and `profile/cross-cutting/*.md` to tailor the CV to the role.
- **If the JD requires a technology, skill, or experience not present in the record, omit it rather than invent it.**
- **Do not stretch or extrapolate claims beyond what is explicitly stated in the source files.** For example:
  - If files show "I used AI for my own delivery," do not claim "I used AI to accelerate teams"
  - If files show "I influenced standards," do not claim "I led a team" unless explicitly stated
  - If files show expertise in one domain, do not claim expertise in adjacent domains
- Try to avoid using the same language as in the job description, while still trying to match the expectations of the recruiter.
- Personal projects and cross-cutting information will normally only be used within the profile section, but make them count when they're relevant to the job description.
- **When a skill or technology is central to the JD, look for opportunities to demonstrate depth and breadth in the profile section.**
  - Example: If the JD emphasizes AI heavily, don't just say "I use AI tools"—name the specific tools (Copilot, Cursor, Claude, Codex) if they're in the cross-cutting files
  - Example: If the JD emphasizes testing, mention specific testing approaches/tools if they're evidenced in the role files
  - This is especially important for profile content where you have more flexibility to aggregate evidence from across roles and cross-cutting files

### Length constraints (CRITICAL - must aim to fit 2 pages)

**Profile section (STRICT LENGTH LIMITS):**
- Maximum 2 paragraphs, 100-130 words total
- First paragraph: 60-75 words maximum
- Second paragraph: 40-55 words maximum
- CRITICAL: Profiles exceeding 130 words will be rejected as unreadable
- Each paragraph should be 2-4 sentences
- Keep sentences short and direct—avoid listing multiple companies, technologies, or achievements in single sentences
- Mention personal projects, cross-cutting experience, or articles only when they provide relevant evidence the professional roles don't cover; keep any such reference brief (a phrase, not a sentence). Extensive technology lists and enumerating multiple companies or tools in a single sentence are always signs the profile needs cutting.
- Target 110-120 words across both paragraphs; do not exceed 130 words under any circumstances

**Experience format per role:**
- Each role should begin with a single descriptive sentence summarizing the role's scope and nature
- This sentence is followed by bullet points highlighting key achievements

**Experience bullets per role:**
- Most recent role (Aegon UK — Migration Lead): 1 sentence + 2-3 bullets maximum
- Second role (Aegon UK — Principal Frontend Engineer): 1 sentence + 1-2 bullets maximum
- Third role (Kova — Staff Frontend Engineer): 1 sentence + 1-2 bullets maximum
- Fourth role (Wellframe Health — Senior Frontend Engineer): 1 sentence + 1-2 bullets maximum
- Fifth role (GDS — Frontend Developer): 1 sentence + 1-2 bullets maximum
- Older roles: Title and dates only by default. However, if an older role contains experience that tangibly improves the match to the JD (e.g., backend Java expertise, Angular experience from the migration-target side, or a specific technology the JD requires), it may be expanded to include a single descriptive sentence and optionally 1 bullet. Use this sparingly and only when the content addresses a clear gap that the five most recent roles do not cover.

**Descriptive sentence:**
- Should capture the essence of what the role was about
- Keep it concise (one line when rendered)
- Use the role file's "Snapshot" section as a guide, but tailor to the JD

**Bullet structure:**
- Each bullet should be a single line where possible
- If a bullet wraps to a second line, keep it concise (max 2 lines when rendered)
- Focus on outcomes and impact, not exhaustive detail
- Be selective: choose the most relevant achievements for the specific JD, not everything from the role file

**Skills section:**
- Keep skills lists concise
- Match the format and approximate length of the sample CV

### Personal Projects section (optional)

Include a **Personal Projects** section only when personal projects provide meaningful additional evidence for the specific role. Do not include it by default.

**When to include:**
- The JD requires skills, technologies, or experience types that are better evidenced in personal projects than in professional roles
- The personal project demonstrates depth in a specific area central to the JD (e.g., browser performance, data visualisation, open-source contribution)
- The profile section cannot adequately capture the relevant technical detail within its word limits

**When NOT to include:**
- The professional experience already fully addresses the JD requirements
- The personal projects are only tangentially relevant
- Including them would make the CV exceed 2 pages

**Placement and format:**
- Place immediately after the Skills section (before the end of the CV)
- Use heading: `## Personal Projects`
- Each project: `####` heading for the project name/description, then a separate Normal paragraph for the technical detail
- Focus on technical techniques and outcomes relevant to the JD, not project history or context
- Total section length: 50-80 words maximum across all projects
- If a project has a public URL, include it in parentheses after the project name

**Project-specific notes:**
- **react-migrator**: When included, add GitHub URL so recruiters can review the open-source tool
- **a11y-audit-dashboard**: Only include when accessibility is central to the JD

**Example format:**
```
## Personal Projects

#### react-migrator (open-source CLI for Angular-to-React migration, github.com/elenavasquezuk/react-migrator)

AST-based codemods using jscodeshift to automate repetitive Angular-to-React conversion patterns, including service-to-hook transforms, template syntax conversion, and form migration. Plugin architecture enabling custom transforms for project-specific patterns.
```

## CV Review (Recruiter Perspective)

After generating the CV, create a review from the perspective of the recruiter who wrote the job description.

**CRITICAL CONSTRAINT: The review must be based ONLY on:**
1. The job description
2. The generated CV

**Do NOT reference information from the source files (profile/work-experience/*.md, profile/personal-projects/*.md, profile/cross-cutting/*.md) that does not appear in the generated CV.** The recruiter cannot see the source files. If information is not in the CV, the recruiter does not know it. This constraint is essential for the review to be useful.

**Review structure:**
1. **Strong alignment**: Areas where the candidate's CV strongly matches the role requirements
2. **Gaps or concerns**: Areas where the CV is lacking compared to typical CVs expected for this role
3. **Overall assessment**: Brief summary of candidacy strength

**Review approach:**
- Act as if you are the recruiter who created and posted this job description
- Be honest about gaps—this is to help improve the application, not to provide false confidence
- Consider what other candidates for this role might typically demonstrate
- Be specific: reference actual requirements from the JD and specific evidence (or lack thereof) in the CV
- Keep the review practical and actionable
- Before finalising, verify that every claim in the review can be traced to text that appears in the generated CV
