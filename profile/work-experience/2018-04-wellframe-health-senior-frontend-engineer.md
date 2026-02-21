---
role_id: wellframe-senior-frontend-engineer
company: Wellframe Health
title_public: Senior Frontend Engineer
title_internal: Senior Frontend Engineer
title_internal_alternate:
start: 2018-04
end: 2019-12
location: Bristol, UK
domain: digital health platform
keywords: [react, redux, typescript, javascript, component-library, storybook, migration, jquery, accessibility, wcag, performance, react-window, css-modules, jest, react-testing-library, aws]
---
# Role: Wellframe Health — Senior Frontend Engineer (Apr 2018 – Dec 2019)

## Snapshot
- **One-liner:** Senior frontend engineer on a clinician-facing React application within a digital health platform company, responsible for performance work, component library creation, and a jQuery-to-React migration.
- **Scope:** Team-level implementation and technical direction across the UK frontend team, with ownership of cross-application concerns (shared component library, accessibility standards).
- **Team / org context:** UK engineering office (~20 people) within a Series B digital health company (~300 employees), headquartered in Boston. The UK team owned the clinician-facing web dashboard.
- **What success looked like:** A faster, more accessible clinician dashboard; a shared component library adopted across three applications; and the care plan builder migrated from jQuery to React without a feature freeze.

## Context & constraints

Wellframe Health operated a digital health platform connecting healthcare providers with patients through web and mobile interfaces. The company was Series B funded, with approximately 300 employees globally. The UK office in Bristol housed roughly 20 engineers and was responsible for the clinician-facing web dashboard — a React application used by care managers to monitor patient populations, manage care plans, and triage alerts.

Elena joined Wellframe specifically to gain deep React experience, having moved from GDS where her frontend work had been broader but less React-focused. The clinician dashboard had been built quickly during the Series A phase and carried significant technical debt. Parts of the codebase — notably the care plan builder — still used jQuery with React wrappers rather than idiomatic React. The application served care managers working with patient lists of 500+ entries, and performance under that load was a known pain point.

The team was small: two other frontend engineers, four backend developers, a QA engineer, a UX designer, a product manager, and an engineering manager. A clinical advisory team provided domain context but was not part of the day-to-day engineering workflow. The modest team size meant that Elena had significant latitude to identify and drive technical improvements, but also that there was limited peer review depth on frontend-specific decisions.

Work was primarily office-based in Bristol with some remote working.

## Core responsibilities

Day-to-day work involved feature development and maintenance on the clinician-facing React dashboard, including integration with REST APIs serving patient data, care plans, and alert information. Elena was one of three frontend engineers and took on a de facto technical lead role for frontend concerns, though this was not a formal designation.

Responsibilities extended beyond feature delivery to include identifying and addressing cross-cutting concerns: dashboard performance, component reuse across applications, accessibility compliance, and the technical debt associated with legacy jQuery code. Elena also contributed to frontend hiring (reviewing take-home exercises and conducting technical interviews) and participated in architecture discussions with the backend team regarding API design and data fetching patterns.

## Initiatives

### Clinician dashboard performance overhaul

**Problem**
The main dashboard loaded patient lists of 500+ entries with all data fetched upfront, resulting in 8–10 second initial load times. This directly affected care managers' ability to triage alerts efficiently.

**What I did**
Profiled the application using React DevTools and Chrome Performance tools. Identified that unnecessary re-renders were occurring due to prop drilling through six or more component layers. Implemented React Context to manage shared state, which was later migrated to Redux as the state management needs grew more complex. Introduced virtualised list rendering using react-window to avoid rendering the full patient list into the DOM.

**Technical details**
React 16, React Context, Redux, react-window, Chrome DevTools Performance panel, React DevTools Profiler. The prop drilling problem was structural — the component tree had been designed for smaller data sets and had not been refactored as the patient lists grew. The virtualised list implementation required changes to the scrolling behaviour and keyboard navigation to maintain accessibility.

**Outcome**
Reduced initial load time from 8–10 seconds to under 2 seconds. This was Elena's first major React performance project. The profiling and optimisation patterns she developed here — particularly the systematic identification of unnecessary re-renders — became a recurring part of her technical approach in subsequent roles.

### Component library extraction

**Problem**
Approximately 30 UI components were duplicated across three React applications: the clinician dashboard, the admin portal, and the reporting tool. Inconsistencies in behaviour and styling between the duplicated components created user-facing discrepancies and maintenance overhead.

**What I did**
Led the extraction of shared components into a standalone component library. Set up Storybook for documentation and visual testing. Established contribution guidelines, semantic versioning, and a review process for library changes. Worked with the UX designer to reconcile visual inconsistencies between the three applications during extraction.

**Technical details**
React 16, Storybook, CSS Modules, Sass, TypeScript, Jest, React Testing Library, Webpack, npm (private registry). Components were extracted incrementally — starting with the most widely duplicated (buttons, form fields, data tables) and progressing to more complex domain-specific components. Semantic versioning was used to manage breaking changes across consuming applications.

**Outcome**
The library reached 60+ components by the time Elena left. All three applications were consuming from the shared library. This was Elena's first experience building a design system from scratch — the process of establishing governance, versioning, and contribution patterns for a shared library was formative and directly influenced her later design systems work.

### Care plan builder migration (jQuery to React)

**Problem**
The care plan builder was the oldest part of the codebase and still used jQuery with React wrappers. The hybrid architecture made the code difficult to reason about, test, and extend. jQuery event handlers and React state management coexisted in ways that produced intermittent bugs.

**What I did**
Designed and executed an incremental migration strategy. The first phase wrapped existing jQuery components in React containers, establishing clear boundaries and data flow. The second phase replaced the jQuery implementations one by one over approximately four months, working through the component tree from leaf nodes inward. The migration was carried out alongside ongoing feature work with no feature freeze.

**Technical details**
jQuery, React 16, TypeScript, Jest, React Testing Library, Enzyme (for testing legacy wrapper components). The key technical challenge was managing the boundary between jQuery DOM manipulation and React's virtual DOM during the transitional period. Each component migration included writing React tests before removing the jQuery implementation.

**Outcome**
The care plan builder was fully migrated to React. No feature freeze was required during the migration. This was Elena's first large-scale migration project and was career-defining: the experience of devising an incremental migration strategy — rather than a greenfield rewrite — and executing it without disrupting ongoing delivery became a core part of her professional identity and directly informed her later career direction.

### Accessibility improvements

**Problem**
The clinician dashboard had not been built with accessibility as a primary concern. As a healthcare application used in clinical settings, accessibility failures had both ethical and potential regulatory implications.

**What I did**
Applied accessibility knowledge from her prior GDS role. Conducted an informal WCAG 2.1 audit of the clinician dashboard, filed 25+ issues, and personally fixed the critical ones: keyboard navigation throughout the application, screen reader support for data tables (including patient lists and care plan summaries), and colour contrast failures. Advocated for accessibility to be included in the team's definition of done.

**Technical details**
WCAG 2.1 (Level AA as target), ARIA attributes, semantic HTML, keyboard event handling, colour contrast tooling. Screen reader testing was done with NVDA and VoiceOver. The data table accessibility work was particularly involved, as the virtualised lists introduced by the performance work required additional ARIA attributes to remain navigable.

**Outcome**
Critical accessibility issues were resolved. Accessibility was adopted as part of the team's definition of done, meaning new features were expected to meet WCAG 2.1 Level AA before being considered complete. The informal audit was not a comprehensive external assessment, and Elena acknowledged that further work remained beyond what she was able to address during her tenure.

## Tech & skills used

The primary technology stack was React 16 with TypeScript, using Redux and React Context for state management. Styling was handled through CSS Modules and Sass. Testing used Jest, React Testing Library, and Enzyme (the latter for legacy wrapper components during the jQuery migration). The component library used Storybook for documentation and visual testing. Build tooling was Webpack and Babel. The legacy codebase included jQuery, which was progressively removed through the care plan builder migration.

Backend integration was via REST APIs, with a Node.js/Express layer serving the frontend. CI/CD was CircleCI. Hosting used AWS (S3 for static assets, CloudFront for CDN). Version control was Git with GitHub. Design collaboration used Figma. react-window was used for virtualised list rendering in the performance work.

## Stakeholders & influence

Elena's primary working relationships were with the two other frontend engineers on the UK team, the engineering manager (who was her direct report line), the product manager, and the UX designer. She collaborated regularly with the four-person backend team on API design and data fetching patterns. The QA engineer was involved in validating migration work and accessibility improvements.

The clinical advisory team provided domain context — particularly around care plan workflows and clinician expectations for the dashboard — but interaction was periodic rather than continuous.

Influence was exercised at the team level through technical proposals (the migration strategy, the component library RFC, the accessibility audit) and through establishing patterns and standards that the other frontend engineers adopted. There was no formal authority beyond her own work. The small team size meant that adoption of her proposals was achieved through direct collaboration and demonstrated results rather than any governance mechanism.

## Positioning notes

This role marked Elena's full transition into frontend-specialist territory and her first deep engagement with React. The prior GDS role had involved frontend work but across a broader stack; Wellframe was where React became her primary tool and where she began to develop the performance profiling, migration planning, and component library skills that would define her subsequent career.

The jQuery-to-React migration of the care plan builder was the most career-significant initiative. It was the first time Elena had to devise an incremental migration strategy rather than proposing a greenfield rewrite, and the experience of executing it without a feature freeze became a core part of her professional identity. This initiative directly informed her approach to migrations in later, larger-scale roles.

The component library work planted the seed for Elena's later design systems expertise, though at this stage the library was modest in scope and the governance patterns were informal. The patterns she developed here were sound but had not yet been tested at enterprise scale.

The team was small (~20 engineers total, 3 frontend) and the user base, while meaningful in a healthcare context, was not high-traffic consumer scale. The technical challenges were real but bounded. Elena's influence was genuine but operated within a context where a small team and limited competing priorities made adoption of her proposals relatively straightforward — a dynamic that would not hold in larger organisations.
