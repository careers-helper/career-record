---
role_id: gds-frontend-developer
company: Government Digital Service
title_public: Frontend Developer
title_internal: Frontend Developer (Senior Developer pay band equivalent)
start: 2016-03
end: 2018-03
location: London, UK
domain: government digital services
keywords: [javascript, nodejs, express, nunjucks, govuk-frontend, govuk-design-system, progressive-enhancement, accessibility, wcag, html, css, sass, bem, mocha, chai, puppeteer, circleci, heroku, govuk-paas, cloud-foundry, server-side-rendering, citizen-services]
---
# Role: Government Digital Service — Frontend Developer (Mar 2016 – Mar 2018)

## Snapshot
- **One-liner:** Frontend developer building and maintaining citizen-facing transactional services within GDS, with a focus on progressive enhancement and accessibility.
- **Scope:** Service-team-level delivery, with contributions to shared cross-GDS component libraries.
- **Team / org context:** Multidisciplinary service team within GDS — the UK government's central digital function — working from the Whitechapel office in London.
- **What success looked like:** Robust, accessible interfaces that worked for all citizens, including those on slow connections, older browsers, and assistive technologies.

## Context & constraints

This was Elena's first purely frontend role. The move to GDS was deliberate — she wanted to build deep frontend expertise in an environment that treated it seriously, and GDS was widely regarded as the gold standard for digital government services in the UK.

GDS's approach to frontend development was disciplined and intentionally conservative. Progressive enhancement was not optional — interfaces had to work without JavaScript. Accessibility to WCAG 2.1 AA was a hard requirement, not an aspiration. The GOV.UK Design System enforced consistency across hundreds of services, and deviation from established patterns required justification through cross-team review.

The tech stack reflected this philosophy: server-rendered Nunjucks templates on Node.js/Express, with minimal client-side JavaScript. There was no React, no SPA architecture, and no client-side routing. This was a deliberate organisational choice — reliability and universal access took precedence over developer experience or modern frontend trends.

The services handled real civic transactions for millions of citizens, including users with low digital literacy, older devices, poor connectivity, and reliance on assistive technologies. The stakes of getting accessibility or progressive enhancement wrong were not abstract.

## Core responsibilities

- Built and maintained citizen-facing transactional services within a multidisciplinary team (interaction designers, content designers, user researchers, delivery manager).
- Implemented frontend changes using Nunjucks templates, GOV.UK Frontend toolkit, and the GOV.UK Design System.
- Ensured all work met WCAG 2.1 AA accessibility requirements.
- Applied progressive enhancement patterns so that all services functioned without client-side JavaScript.
- Contributed components and pattern improvements back to the shared GOV.UK Design System.
- Participated in cross-team design critiques and pattern reviews.
- Became the team's informal accessibility specialist following a series of audits.

## Initiatives

### Register to Vote service improvements

- **Problem:** The Register to Vote service was one of GDS's highest-traffic citizen-facing services and required ongoing maintenance and feature work. It needed to remain accessible, performant, and functional across the full range of devices and browsers used by the UK public.
- **What I did:** Maintained and extended the service, working with Nunjucks templates and progressive enhancement patterns within the GOV.UK frontend toolkit. Built robust interfaces that functioned fully without JavaScript enabled.
- **Technical details:** Server-side rendered Nunjucks templates on Node.js/Express. GOV.UK Frontend toolkit for styling and component behaviour. Strict WCAG 2.1 AA compliance. Progressive enhancement throughout — core journeys worked with HTML and server-side logic alone.
- **Outcome:** The service continued to operate reliably for millions of citizens. Accessibility and progressive enhancement standards were maintained through all changes.

### GOV.UK Design System contributions

- **Problem:** The GOV.UK Design System was the shared component library used by hundreds of government services. Components and patterns needed ongoing improvement based on research findings and real-world usage across teams.
- **What I did:** Contributed improvements to the shared Design System, including work on the date input pattern and the error summary component. Participated in design critiques and cross-team pattern reviews where proposed changes were assessed for broader impact.
- **Technical details:** Contributions followed GOV.UK Design System conventions — accessible-by-default components using semantic HTML, progressive enhancement, and BEM-methodology CSS/Sass. Changes went through a cross-team review process before adoption.
- **Outcome:** Improvements were adopted into the shared Design System and used across multiple government services. This was Elena's first experience contributing to a component library consumed by other teams at scale.

### Assisted Digital support tooling

- **Problem:** Citizens who could not complete digital services independently were supported by call centre staff via the Assisted Digital programme. The internal tooling used by these staff needed to be optimised for a different set of UX requirements than the public-facing services — speed, keyboard navigation, and efficient data entry rather than progressive disclosure.
- **What I did:** Built internal tooling for call centre staff, enabling them to complete transactions on behalf of citizens during phone calls. Designed the interaction model around keyboard-driven workflows and rapid data entry.
- **Technical details:** Node.js and Express on the server side with Nunjucks templates. The UX prioritised keyboard navigation, minimal mouse interaction, and fast task completion. Server-side rendering throughout.
- **Outcome:** Call centre staff had purpose-built tooling that matched their workflow requirements, rather than re-using the citizen-facing interface which was designed for a fundamentally different interaction model.

### Accessibility audit and remediation

- **Problem:** Two legacy services had accumulated accessibility issues over time and had not been systematically audited against current WCAG standards.
- **What I did:** Led an accessibility audit of both services, identifying approximately 40 WCAG violations. Prioritised and fixed the issues, and documented patterns to prevent recurrence.
- **Technical details:** Manual testing with screen readers (JAWS, NVDA, VoiceOver), keyboard-only navigation testing, automated scanning tools, and WCAG 2.1 AA checklist-based assessment. Fixes covered semantic HTML corrections, ARIA attribute usage, focus management, colour contrast, and form labelling.
- **Outcome:** Both services were brought into WCAG 2.1 AA compliance. Elena became the team's informal accessibility specialist as a result of this work. The experience directly informed her later interest in building the a11y-audit-dashboard personal project.

## Tech & skills used

- **Languages:** JavaScript (ES6+), HTML5, CSS, Sass
- **Frameworks & libraries:** Node.js, Express, Nunjucks
- **Design systems & methodologies:** GOV.UK Frontend, GOV.UK Design System, BEM methodology, progressive enhancement
- **Accessibility:** WCAG 2.1 AA, screen reader testing (JAWS, NVDA, VoiceOver), keyboard navigation testing
- **Testing:** Mocha, Chai, Puppeteer
- **Infrastructure & tooling:** Git, GitHub, CircleCI, Heroku (for prototyping), GOV.UK PaaS (Cloud Foundry)

## Stakeholders & influence

- **Service team (daily):** Worked directly with a service owner, interaction designers, content designers, user researchers, and a delivery manager within the multidisciplinary team. Influence was exercised through implementation expertise — advising on what was technically feasible within progressive enhancement and accessibility constraints.
- **Cross-GDS frontend community (regular):** Interacted with other frontend developers across GDS through Design System contribution reviews and pattern critiques. Influence was peer-based — proposing and reviewing component changes that would be used by other teams.
- **GDS accessibility team (periodic):** Engaged with the central accessibility team during audits and for guidance on complex remediation issues. This was a consultative relationship rather than a reporting one.
- All influence in this role was peer-level and expertise-based. There was no line management responsibility or formal authority over other developers.

## Positioning notes

This role was foundational for Elena's frontend identity. GDS instilled a discipline around progressive enhancement, semantic HTML, and accessibility that she carried into every subsequent role. The emphasis on "making things work for everyone" — including users on slow connections, older browsers, and assistive technologies — gave her a perspective that many frontend developers who came up through SPA frameworks lack.

However, the tech stack was deliberately conservative. Two years of server-rendered templates with minimal client-side JavaScript meant Elena was not building skills in React, modern SPA architecture, client-side state management, or component-driven frontend development during this period. That gap became increasingly apparent as the wider industry moved toward single-page application patterns, and it directly motivated her next career move.

This role should be read as a deep investment in frontend fundamentals — HTML, CSS, accessibility, progressive enhancement — rather than as a period of broad frontend technology development. The breadth came later; this was about depth in the areas GDS cared about most.
