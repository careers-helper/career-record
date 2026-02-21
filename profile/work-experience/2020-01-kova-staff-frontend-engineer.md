---
role_id: kova-staff-frontend-engineer
company: Kova
title_public: Staff Frontend Engineer
title_internal: Staff Frontend Engineer
start: 2020-01
end: 2022-05
location: London, UK (Remote)
domain: B2B payments platform
keywords: [react, typescript, micro-frontends, module-federation, webpack, design-systems, storybook, chromatic, graphql, apollo, performance, lighthouse, css-in-js, emotion, playwright, aws, github-actions, frontend-platform]
---
# Role: Kova — Staff Frontend Engineer (Jan 2020 – May 2022)

## Snapshot
- **One-liner:** First Staff-level frontend engineer at a Series C fintech, hired to provide architectural direction across a fragmented frontend estate of four independently built React applications.
- **Scope:** Cross-team architectural leadership across 3 squads and 12 frontend engineers, with no direct reports.
- **Team / org context:** ~400-person B2B payments company headquartered in London, with a 12-person frontend team that had no overarching technical leadership prior to Elena's arrival.
- **What success looked like:** A unified micro-frontend architecture, a shared design system adopted by all squads, a credible TypeScript migration path, and an approved frontend platform team to sustain the work.

## Context & constraints

Kova was a Series C fintech building B2B payment processing and reconciliation infrastructure for mid-market businesses. The company had roughly 400 employees and was headquartered in London. Elena joined in January 2020 as the first Staff Frontend Engineer — the role was created specifically to provide technical direction across the frontend organisation.

The frontend estate consisted of four web applications: a merchant dashboard, an internal operations console, a partner integration portal, and a reporting suite. All four were independent React applications with significant code duplication, inconsistent patterns, and no shared infrastructure. Each had been built by its respective squad with no coordination on architecture, component design, or tooling. The frontend team comprised 12 engineers distributed across 3 squads, each with its own engineering manager.

Elena joined on-site in London. When COVID-19 restrictions began in March 2020, the company moved to fully remote working. Elena never returned to the office for the remainder of the role. This transition to remote work changed the coordination model — written communication and documentation became the primary mechanisms for cross-team alignment, which proved to be well-suited to Elena's working style.

The 12-person frontend team, while meaningful in scope, was not large by industry standards. This was not a 40+ developer organisation — the architectural challenges were real but bounded in scale.

## Core responsibilities

- Provided cross-team architectural direction for all four frontend applications, operating as a Staff-level IC with no direct reports.
- Defined and maintained shared technical standards, configurations, and tooling across the frontend estate.
- Reviewed architectural decisions across squads and ensured consistency in patterns and conventions.
- Acted as the primary technical point of contact for frontend concerns in discussions with the VP Engineering, engineering managers, and backend platform team.
- Identified organisational gaps in the frontend engineering function and advocated for structural investment to address them.

## Initiatives

### Micro-frontend architecture adoption

- **Problem:** Four independent React applications duplicated common functionality (navigation, authentication, theming) and could not share runtime dependencies. Each application had its own build and deployment pipeline, and there was no mechanism for squads to share code at runtime without creating tight coupling.
- **What I did:** Designed and implemented a module federation-based micro-frontend architecture using Webpack 5 Module Federation. The architecture introduced a common shell application providing navigation, authentication, and theming, while allowing each squad's application to remain independently deployable. Rolled out the migration incrementally over 6 months, starting with the merchant dashboard and operations console before extending to the partner integration portal and reporting suite.
- **Technical details:** Webpack 5 Module Federation for runtime module sharing. Each application exposed and consumed federated modules through a shared shell. The shell handled cross-cutting concerns (auth, nav, theming) while individual applications retained ownership of their domain-specific functionality. Independent deployment was preserved — each squad could release without coordinating with others, consuming shared dependencies at runtime.
- **Outcome:** All four applications were consolidated under a common shell with shared runtime infrastructure. Squads retained independent deployability. Code duplication for cross-cutting concerns was eliminated. The incremental rollout approach avoided a disruptive big-bang migration.

### Shared design system (Kova UI)

- **Problem:** The four applications contained extensive component duplication with inconsistent visual and behavioural patterns. There was no shared component library, no design tokens, and no systematic approach to UI consistency. Kova had a single product designer whose work was being interpreted differently by each squad.
- **What I did:** Founded and led development of Kova UI, the company's first design system. Started with an audit of existing components across all four applications, identifying 80+ duplicated patterns. Built a shared library of 45 canonical components. Worked closely with the product designer to establish design tokens that codified colour, spacing, typography, and other visual constants. Used Storybook for component documentation and Chromatic for visual regression testing. Published the library to a private npm registry.
- **Technical details:** React component library with design tokens, CSS-in-JS (Emotion) for styling, Storybook for documentation and development environment, Chromatic for visual regression testing, private npm registry for distribution. The 45 components were distilled from 80+ identified duplicated patterns across the four applications.
- **Outcome:** All squads adopted Kova UI within 8 months. Component duplication was substantially reduced. The design system provided a shared vocabulary between engineering and design. Visual regression testing via Chromatic caught unintended changes before they reached production.

### TypeScript migration

- **Problem:** When Elena joined, only 1 of the 4 applications used TypeScript. The remaining three were plain JavaScript with no type safety, inconsistent patterns, and limited tooling support. This made cross-application refactoring risky and slowed onboarding for engineers moving between squads.
- **What I did:** Established a migration strategy: strict TypeScript for all new files, gradual conversion of existing files prioritised by change frequency (files that were modified most often were converted first). Created shared TSConfig presets and ESLint configurations that all four applications consumed, ensuring consistent compiler and linting behaviour across the estate.
- **Technical details:** TypeScript with strict mode, shared TSConfig presets published alongside the design system tooling, shared ESLint configurations with TypeScript-specific rules, Prettier for formatting consistency.
- **Outcome:** By the time Elena left, TypeScript coverage was at approximately 85% across all four applications. The shared configuration presets meant that all applications enforced the same TypeScript strictness and linting rules, reducing friction when engineers worked across squad boundaries.

### Frontend platform team advocacy

- **Problem:** The shared design system, micro-frontend infrastructure, and cross-cutting tooling required ongoing maintenance and development. This work was being absorbed by Elena and by engineers across squads on an ad hoc basis, with no dedicated ownership. This was not sustainable — the infrastructure would degrade without intentional investment.
- **What I did:** Proposed and successfully advocated for a dedicated frontend platform team of 2 engineers to own the design system, shared tooling, and micro-frontend infrastructure. Wrote the team charter defining scope and responsibilities, hiring criteria for the two roles, and an initial roadmap covering the first two quarters of work. Presented the case to the VP Engineering and engineering managers.
- **Technical details:** This was an organisational initiative rather than a technical one. The deliverables were the team charter, hiring criteria, and roadmap documents.
- **Outcome:** The frontend platform team was approved and staffed approximately 4 months before Elena left Kova. The team assumed ownership of Kova UI, the module federation shell, shared configurations, and the CI/CD tooling for frontend deployments.

### Performance monitoring and budgets

- **Problem:** There was no systematic approach to frontend performance. Bundle sizes and load times were not tracked, and regressions could reach production undetected. A specific incident in the merchant dashboard saw a bundle size regression from 890KB to 2.1MB caused by unintended transitive dependencies, which was only discovered after users reported slow load times.
- **What I did:** Introduced Lighthouse CI into the deployment pipeline with defined performance budgets. Established Core Web Vitals tracking via Datadog. Investigated and resolved the merchant dashboard bundle size regression by identifying and removing the unintended transitive dependencies.
- **Technical details:** Lighthouse CI integrated into GitHub Actions deployment pipelines, with performance budgets enforced as pass/fail gates. Core Web Vitals (LCP, FID, CLS) tracked through Datadog. The merchant dashboard bundle regression (2.1MB to 890KB) was caused by transitive dependencies pulled in through improperly scoped imports.
- **Outcome:** Performance budgets prevented future bundle size regressions from reaching production. Core Web Vitals tracking provided ongoing visibility into real-user performance. The merchant dashboard bundle reduction improved load times for the application's primary user-facing surface.

## Tech & skills used

- **Languages:** TypeScript, JavaScript (ES6+)
- **Frameworks & libraries:** React 17/18, Apollo Client (GraphQL), Emotion (CSS-in-JS)
- **Build & tooling:** Webpack 5, Module Federation, ESLint, Prettier, Node.js
- **Testing:** Jest, React Testing Library, Playwright, Chromatic (visual regression)
- **Design systems:** Storybook, design tokens, private npm registry
- **APIs:** GraphQL (Apollo Client), REST APIs
- **CI/CD:** GitHub Actions, Lighthouse CI
- **Infrastructure:** AWS (CloudFront, S3, Lambda@Edge)
- **Monitoring:** Datadog, Core Web Vitals tracking

## Stakeholders & influence

- **VP Engineering:** Primary sponsor for cross-cutting frontend initiatives. Elena reported architectural proposals and platform team advocacy through this relationship.
- **Engineering managers (3 squads):** Elena coordinated with all three squad leads to align on architectural direction, migration timelines, and adoption of shared tooling. This was influence-based — Elena had no authority over squad roadmaps.
- **Product designer (1):** Close collaboration on the design system, particularly on establishing design tokens and canonical component specifications.
- **Product managers (3):** Engaged on performance improvements and migration timelines where these intersected with squad delivery commitments.
- **Backend platform team:** Coordination on API contracts and shared infrastructure concerns, particularly around authentication flows in the micro-frontend shell.
- **DevOps/SRE team:** Collaboration on CI/CD pipeline changes, deployment infrastructure for the micro-frontend architecture, and monitoring setup.
- **Frontend engineers (12 across 3 squads):** The primary audience for Elena's architectural decisions. Adoption of the design system, TypeScript migration, and micro-frontend architecture required buy-in from all 12 engineers. Elena exercised influence through documentation, technical RFCs, and direct pairing — not through positional authority.

Elena operated as a Staff-level IC with cross-team influence but no direct reports and no formal authority over squad priorities or staffing. All adoption of her architectural proposals was achieved through persuasion, documentation, and demonstrated value.

## Positioning notes

This was the role where Elena's professional identity consolidated. It was her first Staff-level position, and the work — bringing order to a fragmented frontend estate through shared architecture, a design system, and platform thinking — became her defining professional narrative.

The micro-frontend and design system work demonstrated a specific and repeatable capability: taking a set of independently built frontend applications with significant duplication and inconsistency, and establishing shared infrastructure that improved consistency without removing squad autonomy. This pattern would recur in later roles.

The transition to fully remote working during COVID was significant. Elena found that her influence actually increased in a remote environment because written communication and documentation became the primary coordination mechanisms. The RFCs, architectural decision records, and design system documentation she produced became the de facto coordination layer — a mode of working that suited her strengths.

The frontend platform team advocacy was notable because it demonstrated the ability to identify organisational gaps and build the case for structural investment, not just technical solutions. Recognising that shared infrastructure requires dedicated ownership — and successfully arguing for headcount to provide it — is a different skill from building the infrastructure itself.

However, the scale should be understood accurately. Kova was a ~400-person company with a 12-person frontend team across 3 squads. This was meaningful cross-team work, but it was not the 40+ developer scale that Elena would encounter in subsequent roles. The architectural challenges were genuine but bounded.
