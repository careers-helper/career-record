## Master CV Role Consolidation — Instruction Set (Revised)

### Objective

You are building a private, canonical “master CV” as a set of structured Markdown files, one per role, intended to act as a long-term source of truth.

Your task is to consolidate all supplied historical descriptions for a single role into one comprehensive, factual, and non-optimised Markdown role file.

This document must be larger than required, not smaller. It is explicitly not a job application artefact.

---

## Input characteristics

- For each role, you will be given multiple descriptions drawn from:
  - LinkedIn (canonical for title and dates)
  - CVs (of varying age and fidelity)
  - Rewritten or remembered summaries
- Descriptions may be:
  - Redundant
  - Inconsistent in phrasing
  - Uneven in detail
  - Partially summarised
- Do not discard any description, regardless of length.

---

## Canonical authority rules

1. LinkedIn is canonical only for:
   - Role title
   - Start and end dates
   - Employer
   - Location (where stated)

2. Accuracy weighting by content size
   - Longer, more detailed descriptions are more likely to be accurate.
   - Shorter descriptions are often derived or summarised.
   - HOWEVER:
     - Shorter descriptions may contain later-remembered details.
     - Therefore: never disregard smaller inputs.

3. Conflict handling
   - Where details differ:
     - Prefer the version with greater specificity.
     - If ambiguity remains, preserve it explicitly.
   - Never resolve uncertainty by inventing clarity.

---

## Non-negotiable constraints

- Never reduce, summarise, or compress content
  - Deduplication is allowed only where statements are factually identical
  - All distinct nuance must be preserved
- Do not optimise for hiring
  - No CV polish
  - No outcome inflation
  - No heroic framing
- No people-management inflation
  - Treat roles as senior IC / architecture-led by default
  - Influence ≠ authority
  - Do not imply line management unless explicitly stated
- No invented details
  - If something is implied but not stated, do not add it

---

## Output format (strict)

Produce one single Markdown file using the exact structural pattern of the existing role files.

---

### 1. YAML Frontmatter (mandatory, exact structure)

Use this structure exactly, leaving unknown fields empty:

```yaml
---
role_id:
company:
title_public:
title_internal:
title_internal_alternate:
start:
end:
location:
domain:
keywords:
---
```

Rules:

- role_id must be stable, descriptive, and filesystem-safe
- keywords must only include technologies, practices, and themes explicitly present in the source material
- keywords should be a single-line array of kebab-case strings
- Do not invent metadata for completeness
- Dates should be in the format yyyy-mm

---

### 2. Role header (immediately after frontmatter)

Immediately after the YAML frontmatter, render a single H1 header in this format:

```markdown
# Role: <Company> — <Title> (<Start Month Year> – <End Month Year>)
```

Example:

```markdown
# Role: Kova — Staff Frontend Engineer (Jan 2020 – May 2022)
```

Rules:

- This header is human-readable, not metadata
- It must reflect LinkedIn-canonical title and dates
- Do not include location here
- This `Role:` prefix is the standard for all new and updated role files

---

### 3. Snapshot (immediately after role header)

Immediately following the role header, include a Snapshot section without any intervening text:

```markdown
## Snapshot
```

Rules for Snapshot:

- This is not a summary for hiring
- Use the structured bullet format below for all new and updated role files:
  - `- **One-liner:**`
  - `- **Scope:**`
  - `- **Team / org context:**`
  - `- **What success looked like:**`
- Keep each bullet concise and factual
- Neutral, declarative tone
- No evaluation language

Example:

```markdown
## Snapshot
- **One-liner:** Senior frontend-focused individual contributor shaping architecture direction while contributing directly to delivery.
- **Scope:** Team-level implementation plus organisation-level standards and architectural alignment.
- **Team / org context:** Rapidly scaling engineering organisation with fragmented terminology and uneven technical baselines.
- **What success looked like:** Shared architectural direction, stronger cross-team consistency, and adoption of strategic technical decisions.
```

Legacy role files may still use prose snapshots. These are valid historical artefacts, but when a role file is materially updated it should be normalised to this structured snapshot format.

---

## Required sections (in this order)

### Context & constraints

- Organisational, technical, or situational constraints
- Scaling pressures, failed prior attempts, structural limits
- Explicitly state constraints that shaped decisions

---

### Core responsibilities

- Separate team-level and org-level responsibilities where applicable
- Use factual, responsibility-oriented language
- Preserve all distinct responsibility statements across inputs

---

### Initiatives

For each initiative, use this exact sub-structure:

- Problem
- What I did
- Technical details
- Outcome

Rules:
- Initiatives should emerge naturally from the input material
- Do not merge initiatives unless they are factually the same effort
- Outcomes must be factual, not evaluative

---

### Tech & skills used

- Include all technologies, practices, and skills mentioned
- Group logically, but do not omit or collapse items

---

### Stakeholders & influence

- Describe:
  - Who was interacted with
  - At what scope (team, department, org)
  - How influence was exercised
- Explicitly distinguish:
  - Influence
  - Coordination
  - Authority (only if stated)

---

### Positioning notes

- Meta-observations about how the role should be interpreted
- Clarify:
  - IC vs leadership framing
  - Architectural vs delivery balance
  - Why certain interpretations would be incorrect
- This section may contain interpretation, but must remain grounded in supplied material

---

## Language & tone rules

- Declarative, neutral, composable
- No hype, metaphors, or persuasion
- Prefer precision over brevity
- Preserve original terminology where meaningful
- Write as if this will be read again in 10 years to reconstruct reality

---

## Output expectations

The final Markdown file should:

- Be longer and more detailed than any single input
- Preserve every factual nuance
- Be unsuitable for direct use as a CV without deliberate extraction
- Serve as a true personal source-of-truth, not a sales document

If done correctly, the document should feel too honest and too detailed to comfortably send to a recruiter.

IMPORTANT: The output should be in plain-text markdown format embedded within a "pre"/code block. Ensure that unescaped backticks do not break out of the ChatGPT plaintext output block.

---

When you are ready, let me know and I shall paste the first collection of Job Descriptions. The first one will ALWAYS be from LinkedIn and hence the source of the canonical job title, dates and location.
