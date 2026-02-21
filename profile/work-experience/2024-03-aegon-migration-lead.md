---
role_id: aegon-migration-lead
company: Aegon UK
title_public: Principal Frontend Engineer
title_internal: Principal Engineer — Migration Lead
title_internal_alternate:
start: 2024-03
end:
location: Edinburgh, UK (Hybrid/Remote from Bristol)
domain: insurance and pensions platform
keywords: [react, typescript, angular, migration, codemods, jscodeshift, web-components, nx-monorepo, vite, vitest, react-testing-library, playwright, storybook, style-dictionary, design-tokens, design-systems, tailwind, css-modules, react-hook-form, tanstack-query, jenkins, azure-devops, github, node, azure, datadog, team-leadership, enterprise, governance, frontend-architecture]
---
# Role: Aegon UK — Principal Frontend Engineer / Migration Lead (Mar 2024 – Present)

## Snapshot
- **One-liner:** Principal engineer leading the execution phase of an Angular-to-React migration across 15 applications, combining architectural ownership with coordination of 8 teams and direct leadership of a small embedded migration accelerator team.
- **Scope:** Organisation-wide migration programme spanning all frontend applications, plus ownership of shared React infrastructure (component library, codemods, migration tooling) and a 3-person direct-report team.
- **Team / org context:** Large insurance and pensions company with ~45 frontend developers across 8 teams, each owning one or more Angular applications. Elena's role sits across all teams rather than within one, with a small dedicated migration accelerator team reporting to her.
- **What success looked like:** Steady, measurable migration progress across the application portfolio without disrupting ongoing business delivery; repeatable migration processes that reduce per-application cost; adoption of shared React infrastructure by all active teams.

## Context & constraints

This role is a direct continuation and expansion of Elena's prior work at Aegon, where she had led the architectural strategy and pilot phase of the Angular-to-React migration. Following the successful claims portal pilot, the scope grew from proving the approach to rolling it out across all 15 Angular applications in the portfolio. Elena's responsibilities expanded correspondingly — from architecture and strategy into active migration execution leadership.

Aegon UK is a large insurance and pensions company. The frontend estate comprises 15 Angular applications (spanning Angular versions 8 through 14) maintained by 8 teams with approximately 45 frontend developers in total. The applications serve both customer-facing and internal functions across pensions and insurance product lines. As a regulated financial services organisation, changes must be made incrementally and without service disruption; full rewrites or feature freezes are not viable.

Elena works remotely from Bristol, with the company's primary office in Edinburgh. This introduces coordination overhead, particularly when embedding with application teams during migration sprints. Travel to Edinburgh is periodic but not routine.

The migration operates within a 3-year plan. As of early 2026, the programme is roughly 50% complete (8 of 15 applications have active React codepaths, 3 fully migrated), which is on track against the original plan but behind some internal expectations. Elena attributes the slower-than-hoped pace primarily to business priority conflicts — application teams are regularly pulled toward feature delivery and regulatory work — rather than technical blockers.

This role includes Elena's first experience with line management. She built and leads a 3-person migration accelerator team (2 mid-level engineers, 1 senior engineer). The team is small and technically focused; the people-management component is genuine but limited.

## Core responsibilities

Elena owns the migration roadmap and is accountable for migration progress across all 15 applications. This includes sequencing which applications migrate when, negotiating migration capacity with application team leads, and escalating business priority conflicts to the VP Engineering and programme management office when necessary.

She maintains the shared React infrastructure used by all migrating teams: the Aegon React UI component library, the automated codemod suite, and the migration sprint format. Changes to shared infrastructure are coordinated across all consuming teams.

She leads the migration accelerator team of 3 engineers. Responsibilities include hiring, mentoring, work allocation, and architectural oversight. Each team member typically embeds with an application team for 2–4 weeks at a time. Elena provides guidance on the most complex migration challenges — shared state, routing, and authentication flows — and steps in directly when needed.

She participates in the enterprise architecture board regarding Angular deprecation governance and technology standards. She works with 2 UX designers to maintain Figma-to-code parity for the component library. She reports migration progress to the PMO and business stakeholders on a regular cadence.

## Initiatives

### Migration execution at scale

**Problem**
The claims portal pilot had validated the incremental migration approach, but scaling from one application to fifteen required a repeatable process. Each application team had different levels of React experience, different codebases, and different business pressures on their time.

**What I did**
Expanded from the claims portal pilot to 5 more applications in the first 12 months. Developed a standardised "migration sprint" format: a 2-week embedded engagement where migration accelerator team members pair with application team engineers to migrate their highest-value pages. Created migration scorecards to track progress per application, covering percentage of pages migrated, percentage of Angular library dependencies removed, and test coverage delta.

**Technical details**
The migration sprint format is structured around pairing: an accelerator team member works alongside an application team engineer, transferring migration knowledge while completing the work. Page selection for each sprint is based on business value and dependency complexity. The scorecards are maintained centrally and reviewed with team leads monthly.

**Outcome**
As of February 2026, 8 of 15 applications have active React codepaths, with 3 fully migrated. The migration sprint format has become the standard mechanism for migration work across the organisation. The pairing model has had the secondary effect of upskilling application team engineers in React, reducing their dependency on the accelerator team for subsequent migration work within their own applications.

### Aegon React UI component library

**Problem**
The foundational component library established during the pilot phase contained 15 starter components. This was insufficient for teams migrating real applications — they were either building ad-hoc components or delaying migration because the shared library lacked what they needed.

**What I did**
Scaled the component library from 15 components to 80+ components, forming a full design system. Introduced design tokens using Style Dictionary to ensure consistent theming across applications. Added dark mode support. Integrated WCAG 2.1 AA compliance testing into CI so that accessibility regressions are caught automatically. Worked with 2 UX designers to maintain Figma-to-code parity.

**Technical details**
React 18/19, TypeScript, Style Dictionary (design tokens), Storybook, CSS Modules, Tailwind CSS (for new applications), Vitest, React Testing Library, axe-core (for automated accessibility testing in CI). The design token architecture allows applications to override theme values while maintaining consistency with the core design language. The library is published via the Nx monorepo and consumed by all 8 active teams.

**Outcome**
The library is now used by all 8 teams with active migration work. The design token approach and Figma-to-code parity have reduced the number of design-related queries from application teams. WCAG 2.1 AA compliance testing in CI catches accessibility regressions before they reach production.

### Automated codemods

**Problem**
A significant portion of migration work involved repetitive, mechanical code transformation: converting Angular service injection patterns to React hooks, translating Angular template syntax to JSX, and replacing Angular form controls with React Hook Form equivalents. This boilerplate conversion was time-consuming and error-prone when done manually.

**What I did**
Built a suite of custom codemods using jscodeshift to automate these repetitive migration patterns. The codemods target three primary transformations: Angular service injection to React hooks, Angular template syntax to JSX, and Angular form controls to React Hook Form. Each codemod was developed iteratively against real application code, with edge cases addressed as they were encountered during migration sprints.

**Technical details**
jscodeshift, AST manipulation, TypeScript. The codemods operate on the TypeScript AST and produce idiomatic React/TypeScript output. They handle approximately 60% of boilerplate conversion. The remaining 40% requires manual intervention — typically where Angular code uses patterns that do not have a direct React equivalent (complex directive composition, certain template reference variable patterns, and tightly coupled Angular module structures).

**Outcome**
The codemods significantly reduce manual migration effort per application. The 60% automation rate means that a typical page migration can focus human effort on the genuinely complex parts — state management, routing integration, and business logic — rather than syntactic transformation. This work directly inspired Elena's open-source react-migrator project.

### Migration accelerator team

**Problem**
Application teams lacked the React migration expertise and dedicated capacity to drive migration work alongside their ongoing feature delivery responsibilities. Without embedded support, migration tended to stall whenever business priorities competed for the same engineers' time.

**What I did**
Built and now leads a 3-person team (2 mid-level engineers, 1 senior engineer) focused entirely on unblocking and accelerating migration across the organisation. Responsible for hiring all three team members, ongoing mentoring, and work allocation. Each team member typically embeds with an application team for 2–4 weeks at a time, working within that team's processes and codebase. Elena provides architectural oversight across all embeddings and steps in directly for the most complex migration challenges (shared state, routing, authentication flows).

**Technical details**
The team operates as a rotating embedded resource. Work allocation is coordinated with application team leads and sequenced according to the migration roadmap. The embedding model means that accelerator team members must quickly orient themselves in unfamiliar codebases — the team maintains internal documentation of each application's architecture, migration status, and known complexities to support this.

**Outcome**
The team has embedded with 6 application teams to date. The model has proven effective at maintaining migration momentum during periods when application teams are under business delivery pressure. Elena's management responsibilities are genuine but bounded: the team is small, technically focused, and operates with significant autonomy. This is not a full-time management role.

### Angular deprecation governance

**Problem**
Without a formal deprecation framework, Angular usage would continue to grow even as migration progressed — new Angular pages and components were still being created, offsetting migration gains.

**What I did**
Established a governance framework for Angular deprecation. Key provisions: no new Angular pages after Q3 2025, the Angular component library moves to maintenance-only mode (security patches and critical bug fixes only, no new components), and a clear sunset timeline communicated to all teams. Worked with the enterprise architecture board to get this formally adopted as organisational policy.

**Technical details**
The governance framework includes a CI-level check that flags new Angular page creation in applications that have begun migration. The Angular component library remains available but is frozen — teams needing new components must use the React library. The sunset timeline is aligned with the overall 3-year migration plan.

**Outcome**
The policy was formally adopted by the enterprise architecture board. The no-new-Angular-pages rule has been in effect since Q3 2025. Compliance has been high, though there have been a small number of exceptions granted for urgent regulatory work where the relevant React components were not yet available.

## Tech & skills used

The primary technology stack is React 18/19 with TypeScript. The migration context means ongoing work with Angular (versions 8 through 14) — reading, understanding, and transforming Angular code rather than writing new Angular code. Web Components are used at the interoperability boundary between Angular and React within hybrid applications.

Build and development tooling includes Nx monorepo, Vite, Vitest, React Testing Library, and Playwright for end-to-end testing. The component library uses Storybook for documentation and visual testing, and Style Dictionary for design tokens. Styling uses CSS Modules for the component library and Tailwind CSS for new applications.

Application-level libraries include React Hook Form (forms) and Tanstack Query (data fetching). The codemod suite uses jscodeshift for AST-based code transformation.

CI/CD uses Jenkins and Azure DevOps. Source control was migrated from Azure Repos to GitHub during Elena's tenure. Infrastructure runs on Azure (Blob Storage, CDN, App Service). Monitoring and observability use Datadog. Node.js is used for build tooling and local development servers.

## Stakeholders & influence

Elena's primary stakeholders are the 8 frontend team leads whose applications are undergoing migration. She coordinates with them on migration sprint scheduling, capacity allocation, and roadmap sequencing. This relationship is one of influence and coordination rather than authority — she cannot direct their teams' priorities and must negotiate migration capacity against competing business demands.

She reports to and works closely with the VP Engineering on programme-level decisions, including escalations when business priority conflicts threaten migration timelines. She engages with the CTO on strategic technology direction, though this interaction is periodic rather than routine.

She has 3 direct reports in the migration accelerator team — her only formal authority relationship. She is responsible for their hiring, mentoring, work allocation, and performance.

She works with 2 UX designers on component library design and Figma-to-code parity. She participates in the enterprise architecture board for Angular deprecation governance and technology standards decisions. She provides regular progress updates to the programme management office (PMO) and business stakeholders across pensions and insurance product lines.

Influence across the ~45 frontend developers is exercised through the migration sprint format (which puts her team members directly alongside application engineers), the shared component library and codemod tooling (which application teams depend on), and the governance framework (which constrains Angular usage). This is influence through tooling, process, and demonstrated value rather than positional authority.

## Positioning notes

This role represents Elena's evolution from a pure individual contributor architect into someone who combines architectural ownership with a degree of people leadership. The progression is genuine but should not be overstated. The migration accelerator team is small (3 people) and technically focused — Elena is not a full-time engineering manager and should not be positioned as one. The more significant dimension of the role is the scale of coordination: influencing 45 developers across 8 teams in a regulated enterprise to adopt a new technology stack without disrupting ongoing business delivery.

The automated codemods and migration sprint format are Elena's most scalable contributions in this role. They reduce the per-application migration cost and make the process repeatable, which is what makes a 15-application migration feasible with a 3-person dedicated team. Without these force multipliers, the programme would require either a much larger dedicated team or a much longer timeline.

The migration is roughly 50% complete as of early 2026. This is on track against the original 3-year plan but behind some internal expectations. The gap between planned and perceived progress is primarily attributable to business priority conflicts: application teams are regularly pulled toward feature delivery and regulatory work, which compresses migration capacity. Technical blockers have been relatively manageable by comparison.

The open-source react-migrator project emerged directly from the codemod work in this role. The relationship between the two is worth noting: the Aegon codemods are proprietary and Aegon-specific, while react-migrator generalises the patterns for public use. Elena developed react-migrator on her own time, though the intellectual lineage is clear.
