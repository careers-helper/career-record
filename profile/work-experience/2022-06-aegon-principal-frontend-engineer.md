---
role_id: aegon-principal-frontend-engineer
company: Aegon UK
title_public: Principal Frontend Engineer
title_internal: Principal Engineer — Frontend Architecture
start: 2022-06
end: 2024-02
location: Edinburgh, UK (Hybrid/Remote)
domain: insurance and pensions platform
keywords: [angular, react, typescript, migration, web-components, strangler-fig, nx-monorepo, vitest, playwright, storybook, jenkins, azure-devops, design-systems, frontend-architecture, enterprise, community-of-practice]
---
# Role: Aegon UK — Principal Frontend Engineer (Jun 2022 – Feb 2024)

## Snapshot
- **One-liner:** First Principal Frontend Engineer at Aegon UK, hired to lead the architectural planning and early execution of a multi-year Angular-to-React migration across 15 customer-facing applications.
- **Scope:** Organisation-wide frontend architecture direction across 8 teams and ~45 frontend developers, with hands-on delivery in pilot migration work.
- **Team / org context:** Large insurance and pensions company (~3,000 UK employees, part of Aegon Group), with a fragmented Angular estate (versions 8–12), a tightly coupled shared component library, and multiple previously stalled modernisation attempts.
- **What success looked like:** An approved and validated migration strategy, foundational React tooling in place, one pilot application migrated, and growing organisational consensus around the approach.

## Context & constraints

Aegon UK's customer-facing platform — encompassing a pensions dashboard, policy management, and claims portal — was built on Angular across approximately 15 applications maintained by 8 teams totalling ~45 frontend developers. The Angular estate was fragmented, with applications ranging from Angular 8 to Angular 12. All applications shared a legacy Angular component library ("Aegon Elements") that was tightly coupled to Angular-specific patterns, creating a deep dependency between the shared library and every consuming application.

Multiple previous attempts to modernise the frontend had stalled. The causes were consistent: lack of architectural consensus across teams, business resistance to feature freezes, and the sheer coupling between applications and the shared library. No one had been able to propose a migration approach that satisfied both the engineering desire for modernisation and the business requirement that feature delivery continue uninterrupted.

Elena was hired specifically because of her track record with incremental migration at Kova and Wellframe. The role was Aegon UK's first Principal Frontend Engineer — a newly created position. She was based in Edinburgh on a hybrid arrangement (one day per week in the Edinburgh office, the rest working remotely from Bristol).

The organisational context added complexity that Elena's previous fintech and health-tech roles had not required. As a large, regulated insurance company, Aegon had layers of governance, risk management, and enterprise architecture review that constrained the pace and approach of technical change. Architectural decisions required formal approval from the enterprise architecture board, and any migration approach needed to account for regulatory and compliance considerations around the customer-facing platform.

## Core responsibilities

- Defined the frontend technical direction for Aegon UK's entire engineering organisation — 15 applications, 8 teams, ~45 frontend developers.
- Conducted a comprehensive audit of the existing Angular estate, including inter-application dependency mapping, shared library usage cataloguing, team lead interviews, and Angular version fragmentation assessment.
- Designed the migration strategy and architecture for the Angular-to-React transition, gaining formal approval from the CTO and VP Engineering.
- Established foundational React architecture, tooling, and standards for use across all teams.
- Designed and built the Angular/React interop layer using Web Components to enable incremental migration.
- Led the pilot migration (claims portal) to validate the approach and produce reusable migration guidance.
- Founded and ran a fortnightly frontend community of practice to build consensus and shared ownership across teams.
- Produced migration guides, starter templates, and documentation so that teams could adopt React without needing to make independent architectural decisions.

## Initiatives

### Migration strategy and architecture design

- **Problem:** Aegon UK's Angular frontend estate was fragmented (Angular 8–12 across ~15 applications), tightly coupled to a shared Angular component library ("Aegon Elements"), and had resisted multiple previous modernisation attempts. There was no consensus on how to proceed, and the business would not accept a feature freeze for migration.
- **What I did:** Spent the first three months conducting a thorough audit of the existing Angular estate. This included mapping inter-application dependencies, cataloguing shared library usage across all 15 applications, interviewing all 8 team leads about pain points and priorities, and assessing the Angular version fragmentation. Produced a 40-page migration strategy document proposing an incremental "strangler fig" approach: new features and pages would be built in React within Angular shells using Web Components as the interop layer, with progressive replacement of Angular pages as they came up for maintenance.
- **Technical details:** The audit covered dependency graphs between applications and the shared library, Angular version distribution, build tooling variation across teams, and patterns of Aegon Elements usage. The strategy document addressed interop architecture, migration sequencing, shared library replacement planning, risk mitigation, and team enablement.
- **Outcome:** The strategy was approved by the CTO and VP Engineering after two rounds of review. It provided the architectural foundation for all subsequent migration work. The "strangler fig" approach was specifically chosen to allow migration to proceed without feature freezes — the key constraint that had blocked previous attempts.

### React foundation and tooling

- **Problem:** With the migration strategy approved, the 8 frontend teams needed a standardised React foundation so they could begin adopting React without each team making independent (and potentially divergent) architectural decisions.
- **What I did:** Established the foundational React architecture: monorepo structure using Nx, shared TypeScript configuration, component library scaffolding (the future "Aegon React UI"), testing strategy, and CI/CD pipeline integration with existing Jenkins/Azure DevOps infrastructure. Created starter templates and migration guides for team use.
- **Technical details:** Nx monorepo with shared TypeScript config. Vitest and React Testing Library for unit and component testing. Playwright for end-to-end testing. Storybook for component development and documentation. Build tooling using Vite. CI/CD integration with the existing Jenkins and Azure DevOps pipelines. Sass and CSS Modules for styling.
- **Outcome:** Teams had a ready-to-use React foundation with clear conventions, removing the need for each team to make independent tooling and architecture decisions. The starter templates and migration guides reduced the barrier to adoption.

### Web Components interop layer

- **Problem:** Migrating 15 Angular applications to React simultaneously was not feasible. An interop mechanism was needed to allow React components to run inside Angular applications (and vice versa), enabling incremental migration at the page or feature level rather than requiring entire application rewrites.
- **What I did:** Designed and built the Angular/React interop layer using Web Components (custom elements). This allowed React components to be embedded within Angular applications and Angular components to be consumed from React contexts, enabling page-level and feature-level migration.
- **Technical details:** The interop layer used the Custom Elements API to wrap React components for consumption by Angular applications and vice versa. Significant engineering challenges included change detection synchronisation (Angular zone.js interactions with React's rendering model), event propagation across the Web Component boundary, shared state management between Angular and React portions of the same page, and handling React concurrent features within an Angular host. The interop layer had to work reliably across the range of Angular versions (8–12) present in the estate.
- **Outcome:** The interop layer was validated in the claims portal pilot and demonstrated that incremental migration was technically viable. It handled the cross-framework boundary without requiring changes to existing Angular application code beyond the integration points.

### Pilot migration: claims portal

- **Problem:** The migration strategy and interop layer needed real-world validation before broader rollout. A low-risk application was needed to test the approach end-to-end and surface practical issues not apparent from the architectural design alone.
- **What I did:** Selected the claims portal as the pilot — it was the smallest application in the estate, maintained by a 2-person team, and carried the lowest business risk. Worked directly with the team to migrate the first 3 pages from Angular to React using the interop layer. Documented every friction point encountered during the migration and updated the migration guides accordingly. Presented findings to the broader frontend community.
- **Technical details:** Three pages migrated from Angular to React within the existing Angular shell using the Web Components interop layer. The pilot covered component migration, routing integration, state management at the boundary, and testing strategy for hybrid pages.
- **Outcome:** The pilot took 6 weeks and validated the strangler fig approach. It confirmed that incremental migration was practical and that the interop layer worked in a production context. The documented friction points and updated migration guides provided the basis for subsequent teams to follow the same process.

### Frontend community of practice

- **Problem:** With 8 teams and ~45 frontend developers, there was no regular forum for building consensus on architectural direction, sharing knowledge, or creating shared ownership of the migration approach. Previous modernisation attempts had partly failed due to lack of buy-in across teams.
- **What I did:** Established a fortnightly frontend community of practice (CoP). Used it to socialise the migration approach, gather feedback on the strategy and tooling, demo progress on the interop layer and pilot migration, and create shared ownership of architectural decisions.
- **Technical details:** Fortnightly sessions covering architecture updates, migration progress, demos, and open discussion. Format evolved based on feedback from attendees.
- **Outcome:** Attendance grew from 12 to 35+ engineers over 12 months. The CoP became the primary venue for frontend architectural discussion across Aegon UK's engineering organisation. It contributed directly to the broader buy-in that the migration strategy achieved.

## Tech & skills used

- **Languages:** TypeScript, JavaScript, HTML, CSS, Sass
- **Frameworks & libraries:** Angular (8–12), React 18, Web Components (Custom Elements API)
- **Build & monorepo tooling:** Nx, Webpack, Vite
- **Testing:** Vitest, React Testing Library, Playwright
- **Component development:** Storybook
- **Styling:** Sass, CSS Modules
- **CI/CD & infrastructure:** Jenkins, Azure DevOps, Azure (Blob Storage, CDN), Node.js
- **Design tooling:** Figma
- **Version control:** Git

## Stakeholders & influence

- **CTO and VP Engineering (regular):** Primary sponsors for the migration strategy. Elena presented the strategy document and architectural approach for formal approval. Interaction was through structured reviews and periodic progress updates. This was influence through expertise and proposal, not reporting authority.
- **8 frontend team leads (regular):** Interviewed during the audit phase, consulted throughout the strategy design, and engaged through the community of practice. Elena influenced their teams' technical direction but had no authority over them — adoption was consensus-driven.
- **~45 frontend developers (community of practice):** Engaged through the fortnightly CoP, migration guides, and starter templates. Influence was exercised through enablement and knowledge sharing.
- **UX design team (4 designers, periodic):** Collaborated on the Aegon React UI component library scaffolding and design token alignment. Interaction was consultative.
- **Backend platform team (periodic):** Coordinated on API contracts and integration points relevant to the migration.
- **DevOps team (periodic):** Worked together on CI/CD pipeline integration for the new React tooling within the existing Jenkins/Azure DevOps infrastructure.
- **Product managers across business lines (periodic):** Engaged to ensure the migration approach accommodated ongoing feature delivery — the strangler fig strategy was specifically designed to address their concern about feature freezes.
- **Enterprise architecture board (periodic):** The migration strategy required formal approval from this governance body. Elena presented the architectural approach and addressed their concerns around risk, compliance, and long-term maintainability.
- All influence in this role was expertise-based. There were no direct reports and no line management responsibility. The scope of influence was organisation-wide — Elena effectively set the frontend technical direction for the entire UK engineering organisation — but this was achieved through consensus, enablement, and formal proposal processes, not through positional authority.

## Positioning notes

This was Elena's highest-impact role to date and the culmination of her migration expertise. The scale was significantly larger than anything she had previously tackled — 15 applications, 45 developers, 8 teams — and the organisational complexity of a large, regulated insurance company added layers of governance and risk management that her previous fintech and health-tech roles had not required.

The role was purely IC with no direct reports, but the scope of influence was broad: she effectively set the frontend technical direction for Aegon UK's entire engineering organisation. The distinction between influence and authority is important here — Elena had no positional power over any of the 8 teams, and adoption of the migration approach depended on building genuine consensus.

The "strangler fig" approach and Web Components interop layer were her most original architectural contributions. The strangler fig pattern — building new features in React within Angular shells, progressively replacing Angular pages as they came up for maintenance — directly addressed the constraint that had blocked all previous modernisation attempts: the business's refusal to accept feature freezes.

However, by the end of this period the strategy was proven but execution was still early. Only one application (the claims portal) had been piloted, and that was the smallest and lowest-risk application in the estate. The harder, higher-traffic applications — the pensions dashboard and policy management portal — remained ahead. The strategy had been validated, the tooling was in place, and organisational consensus had been built, but the bulk of the actual migration work had not yet been done. This role should be read as architectural leadership and enablement rather than as completed delivery of a migration programme.
