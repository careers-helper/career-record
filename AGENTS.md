# AI Agent Instructions: Master Career Record

> **This is the one instruction file for every AI agent working on this repository** (Claude Code, Codex, GitHub Copilot).

<!-- shared:base -->
# Working in Martin's repositories

This block is shared across Martin's repositories and synced from his dotfiles (`agents/AGENTS.md`); edit it there, not here. It applies to every agent, local or remote. The repository's own sections follow it, add to it, and win where they conflict. "Ask" means ask Martin, in the session or on the pull request.

## Instruction files

- Agent instructions for a repository live in **`AGENTS.md` only**, which Claude Code, Codex, and Copilot's code review on GitHub.com, CLI, coding agent and Chat in VS Code all read (Copilot's code review run inside an IDE, and its Chat in Visual Studio, JetBrains or on GitHub.com, read only Copilot's own instruction files such as `.github/copilot-instructions.md`, not `AGENTS.md`, so they get nothing from it; GitHub's [custom instructions support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support) is the reference). A `CLAUDE.md` or `CLAUDE.local.md` anywhere in the repository makes Claude Code ignore `AGENTS.md`; any other file one of these tools reads as instructions would be a second, drifting source: a second `AGENTS.md` anywhere below the root (Claude Code loads `.claude/AGENTS.md` at session start and a subdirectory's `AGENTS.md` when it works there), `.claude/rules/`, `AGENTS.override.md`, `.github/copilot-instructions.md`, `.github/instructions/**/*.instructions.md` (any depth), `GEMINI.md`, `REVIEW.md`, and a Cursor leftover (`.cursorrules`, `.cursor/rules/`). The names are exact, so a `docs/review.md` is fine. If you find any of these, **do not delete, move or edit it: report it as an issue** in your reply and on the pull request if there is one, then carry on. Martin decides what happens to it.
- **Project memory.** Where the repository has `docs/NOTES.md`, read it before a non-trivial change and append a dated entry when you learn something durable (a gotcha, why something is the odd way it is, what was tried and failed). Decisions between alternatives go in `docs/decisions/`, one short file each. A note that keeps being consulted has become a rule: propose moving it into `AGENTS.md`. Work in progress belongs in a plan file, an issue or the branch, not in either.

## Engineering principles

Apply these when writing, fixing or reviewing code.

- **Start from the requirement.** Establish what the code must do and how that is verified (the spec, the plan, the tests, the acceptance criteria) before judging correctness. Respect scope that is explicitly deferred.
- **Think in paths, not lines.** For any change or finding, consider the related execution paths, the boundary conditions, the failure cases (I/O errors, interruption, malformed input, partial state) and the callers, consumers and persisted data it touches.
- **A bug is evidence of a class.** Treat a reported defect as one instance of a rule being broken. Name the rule, then find every other place it applies before touching anything. Do not expand into unrelated work.
- **Simple over defensive.** Guard the real failure paths (I/O, persistence, user input, partial state), not every call. Prefer simple, clear code; respect intentional design, since not every unusual pattern is a bug.

### When implementing or fixing

- **Fix the class, not the instance.** A review comment gives an example; the deliverable is the rule applied everywhere it holds: sibling commands, the other direction of a round trip, the same data in another file. Grep for the pattern and walk the callers.
- **Reuse an existing safeguard.** Where the codebase already guards against this (a staged swap, a settings check, validate-before-write), apply the same mechanism and share the code rather than writing a second version.
- **Root cause first.** Before fixing a finding, say in one sentence why it happened. If the cause is a missing invariant, enforce the invariant rather than patching the symptom.
- **Prove it with tests that state the rule.** Add tests for the behaviour and its failure cases, named for the rule they protect, not only a reproduction of the reported case.
- **Say what you generalised.** In the commit message and the thread reply, list the other sites the rule was applied to, and the sites checked and found clean, so a reviewer can verify the scope rather than rediscover it.
- **Inspect the whole change before handing back.** Read the complete diff once more for omissions, regressions and leftovers: dead code, stale docs, an unmentioned behaviour change. Run the project's lint and tests first.
- **Never bypass a hook or a check** (`--no-verify`, `HUSKY=0`, skipping a failing test) to get a commit through. Find and fix the cause; if the cause is the environment (a stale `NODE_OPTIONS`, a missing tool), fix that for the one command rather than disabling the hook.

### When reviewing

- **Map requirements to code and tests.** For each applicable requirement, find where it is implemented and where it is verified; investigate the gaps before finalising.
- **Understand the existing patterns first.** Read the comments; they often explain the intent behind a choice. Check existing safeguards and deferred scope before raising a finding.
- **Cover everything that changed.** Keep going after finding several defects; a review that stops early makes the next round.
- **Review the whole head, not the delta.** Re-review the complete change on every push, not only the lines since the last review, so a rule applied in one place and missed in another is caught now.
- **Consolidate by root cause.** Report one finding per rule broken, listing every site it applies to and the sites checked and clean, rather than one finding per instance across successive rounds.
- **Report substantiated, actionable defects**, with the triggering condition and the impact, each with a priority (P1 to P3).

## Git and pull requests

- Branch from `main`. Never commit or push to `main` directly unless the repository's own rules say so.
- Never rebase a branch that has been pushed; bring it up to date with a merge. Rebasing rewrites shared history and breaks other contributors and automation.
- Commit messages: an imperative summary line, then why. Agents add their `Co-Authored-By` trailer.
- Pull request descriptions: what and why, how it was checked (plan evidence where there is a plan), what is deliberately not done, and a closing line naming the agent that wrote it. Where the repository squashes, the PR title becomes the commit's summary line, so write it as one.
- **Anything posted through Martin's GitHub account starts by naming its author and model**, for example `**Claude Code:** Claude Fable 5.1.` or `**Codex:** Reviewed by GPT-6.` Use the model identity available in the current session; never copy another agent's attribution or guess an unknown model variant. If the exact model is unavailable, say so.
- When asked for a pull-request review, post the completed review on the pull request as well as summarising it in chat; that is standing permission. Include the reviewed commit SHA, a verdict, prioritised findings and the validation evidence. Prefer a formal GitHub review; when GitHub prevents approving or requesting changes on the author's own PR, submit a comment review with an explicit verdict. Posting a review never authorises merging or changing managed infrastructure.
- The `gh` CLI is fine for reading the repository: Actions runs, pull requests, workflow logs.
- When behaviour changes, update the README and whatever runbook, task list or docs describe it, in the same pull request.
- No em-dashes in anything written for Martin: code comments, docs, pull request text, replies.

## The review and merge cycle

- **Standing merge rule: wait for Codex, then merge.** After opening a PR or pushing to one, wait for Codex's review of that exact head commit; if none has arrived after about 10 minutes, request one with a single `@codex review` comment (never more than one request per head). Then merge, by the repository's allowed method, once nothing is outstanding: Codex's review of the head raised no unaddressed findings, every review thread from any reviewer is resolved, required checks pass and the branch is up to date. This is standing permission to merge, so do not ask each time.
- **What counts as Codex's review:** Codex reviews some PRs automatically and others on request; its summary comment's *Review trigger* column shows which. With findings it leaves a review; with none it reacts 👍 to the PR, and that 👍 counts as a clean review of the head **if it was given after the head commit was pushed and no earlier head was still awaiting Codex at that push** (a 👍 names no commit, so a late one could belong to an earlier review; when in doubt, treat it as not reviewed and say so). A comment such as "Didn't find any major issues" naming the head commit also counts. If neither arrives for the head after one request, report it and ask.
- **Copilot reviews too, but is optional.** Where Copilot reviews pushes, check for its review of the head before merging (it usually arrives within minutes) and treat its findings like Codex's. Merging does not depend on it: if it errored or has not arrived by the time everything else is ready, merge without it, and do not re-request it.
- **Address every review point, whatever its priority.** P1, P2, P3 and unprioritised suggestions alike: fix each one, or reply explaining why not, then resolve its thread. A PR is only clean when every thread is resolved.
- **Every fix gets a re-review.** After fixing review points, push and wait for Codex to review the new head before merging, however small the fix.
- **The cycle, explicitly:** (1) push the PR; (2) Copilot and Codex review; (3) push one combined round of fixes and replies, resolving the threads addressed; (4) Copilot and Codex review again; (5) if there are new findings, repeat (3) and (4), within the limit below. A fix round addresses the class, not the instance. When a review of the head raises nothing new: if anything else is outstanding (an unresolved thread, a failed check, no Codex verdict for the head after one request), pause and say what is going on; if nothing is, merge, provided the repository is not excluded or Martin has explicitly allowed the merge. Within a round, auto-fix mechanical and factual points (dates, numbering, links, lint, a wrong value against a cited source); wording, judgement and fit-assessment points get a reply and come to Martin. Do not spend a subagent per round.
- **The limit: a P1 is always fixed; otherwise four fix rounds.** If the latest review of the head raises a P1, fix it (with everything else in that review) in another round, whatever the round count. If it raises only P2s or lower and four fix rounds are already done, do not start a fifth: stop and ask what to do next, suggesting a merge with a to-do for the remaining findings (an issue on the repository, and a reply on each thread saying it is carried there).
- **Do not merge under the standing rule** when: the PR is a draft, or states a merge prerequisite that is not met yet (an apply, a deleted key, another PR); it destroys or replaces infrastructure, or loosens a protection, and Martin has not approved that specific change; or Codex has not reviewed the head within about 30 minutes. Say which of these applies and ask.
- Merging never authorises applying Terraform or changing managed infrastructure. Where merging deploys something (a site repository, a release), say so when reporting.

## Dependency upgrades

Passing CI does not show that an upgrade is safe: a changed default or a dropped feature can pass every test. Before merging any package upgrade, whether a Dependabot PR, a grouped update or one you make:

- **Read the changelog for every major version crossed** (release notes, `CHANGELOG.md`, or the migration guide), not just the latest release. For minor and patch updates, skim the notes for deprecations, changed defaults and security fixes. If there is no changelog, compare the tagged source or the published package and say so.
- **Search the codebase for everything that changed**: removed or renamed APIs, new defaults, changed peer, Node or runtime requirements, config format changes. Fix what is affected in the same PR.
- **Test what `main` will become, not the branch.** Fetch, then merge the current `origin/main` into the PR locally (a stale local `main` tests the old base), and run a frozen install, lint and build. A lockfile merged as text can break even when GitHub reports no conflict, most often when the PR predates another dependency change.
- **Write it up on the PR**, and in your reply: what changed that touches this codebase, what the PR does about each item, and links to the changelog sections you read. Say plainly when a major bump turns out to need no changes, and why.
- **Ask before merging** when a change alters behaviour users or Martin would notice, drops support for something in use, or needs a decision. Otherwise the standing merge rule applies once the write-up is posted.
<!-- /shared:base -->

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
│       ├── _<STATUS>                              # Status (empty file), see "Application Status" below
│       └── interviews/                            # Optional: interview prep materials
└── AGENTS.md                                  # This file: the one instruction file for every AI agent
```

## Critical Pattern: Non-Optimised Truth

**Key principle:** These files are intentionally comprehensive and non-promotional. They:
- Preserve ALL distinct details from multiple source descriptions (LinkedIn, CVs, personal notes)
- Are explicitly "too honest and too detailed to comfortably send to a recruiter"
- Distinguish between influence and authority (i.e. highlight line management when required; highlight influencing peers or non-reports when required)
- Use declarative, neutral language without hype or persuasion

## Creating/Updating Experience Files

- **Employment history:** Follow [infrastructure/llm-role-instructions.md](infrastructure/llm-role-instructions.md) for the complete specification (frontmatter, sections, language rules, conflict resolution).
- **Personal projects:** Follow [infrastructure/llm-personal-project-instructions.md](infrastructure/llm-personal-project-instructions.md) for the complete specification.

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
- `_APP_INT_WDR`: applied, interviewed, then withdrew
- `_APP_INT_REJ`: applied, interviewed, then rejected
- `_APP_INT_OFF_ACC`: applied, interviewed, offered, accepted

Only one status file exists per role folder at any time. When the status advances, rename the file (e.g. `_APP` → `_APP_INT`).

## Processing Job Applications

**New applications:** Drop the job description in `inbox/` (any readable format: PDF, image, Markdown, or Word) and use the Inbox Batch Workflow below to triage and generate CVs.

**For a role already in `output/`** (after inbox triage):
- To generate or regenerate a CV: follow [infrastructure/cv-generation-instructions.md](infrastructure/cv-generation-instructions.md).
- To screen for fit or re-run a suitability assessment: read `profile/job-preferences.md` and [infrastructure/job-screening-instructions.md](infrastructure/job-screening-instructions.md).

## Inbox Batch Workflow (Two-Pass)

When the user asks to **"review the inbox"** (or similar phrasing), process all job description files in the `inbox/` folder using a two-pass approach:

### Pass 1: Triage (suitability reports only)

1. List the contents of `inbox/` and identify all job description files (any readable format: PDF, image, Markdown, or Word document).
2. For each file:
   a. Parse the filename to determine the company name and role title.
   b. Create the appropriate folder under `output/` using the naming convention `YYYYMMDD-<company>-<role>/` (where the date is today's date).
   c. Move (not copy) the file from `inbox/` to the new folder, renaming it to `job-description.<ext>` (preserving the original file extension).
3. Generate a **suitability report** (`suitability.md`) for each role, following `profile/job-preferences.md` and [infrastructure/job-screening-instructions.md](infrastructure/job-screening-instructions.md). Process roles sequentially.
4. Present a summary table of all roles with their fit scores and recommendations so the user can decide which (if any) to proceed with.

### Pass 2: CV generation (on request)

After the user has reviewed the suitability reports and indicated which roles to pursue:

1. For each selected role, run the remaining steps of the standard workflow: generate the tailored CV (`cv.md` + `cv.docx`) and the recruiter-perspective review (`automated-review.md`), following [infrastructure/cv-generation-instructions.md](infrastructure/cv-generation-instructions.md).
2. Create an empty `_REVIEW` status file for each completed role.
3. Process roles sequentially (complete all artefacts for one role before starting the next).

## Example Role Files

- [profile/work-experience/2022-06-aegon-principal-frontend-engineer.md](profile/work-experience/2022-06-aegon-principal-frontend-engineer.md): Enterprise migration architecture role with clear distinction between cross-team influence and team ownership
- [profile/work-experience/2020-01-kova-staff-frontend-engineer.md](profile/work-experience/2020-01-kova-staff-frontend-engineer.md): Staff-level IC role establishing cross-team architectural direction without direct reports
- [profile/work-experience/2024-03-aegon-migration-lead.md](profile/work-experience/2024-03-aegon-migration-lead.md): Evolution from pure IC to combined architectural ownership with small team leadership

## Overrides of the shared rules

- This is a content repository: the engineering principles apply to the scripts under `infrastructure/` when they change, and the dependency-upgrade rule to their tooling; the rest of the shared block (branching, PR conventions, attribution) applies as written.
- **The automatic PR → review-and-fix → merge cycle does not run here on its own.** Martin invokes it for this repository by name. Changes to CV or report content are his to approve change by change.
