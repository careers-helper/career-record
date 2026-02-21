---
role_id: northgate-software-engineer
company: Northgate Building Society
title_public: Software Engineer
title_internal: Software Engineer
start: 2013-06
end: 2016-02
location: Leeds, UK
domain: retail banking
keywords: [java, spring-boot, angular, angularjs, typescript, javascript, webpack, gulp, rest-apis, soap, swagger, postgresql, frontend-migration, mortgage-platform]
---
# Role: Northgate Building Society — Software Engineer (Jun 2013 – Feb 2016)

## Snapshot
- **One-liner:** Backend-hired software engineer who increasingly gravitated toward frontend work during a mortgage platform modernisation, culminating in leading the Angular 2 proof of concept.
- **Scope:** Individual contributor within the backend team, later straddling backend and a newly formed frontend team.
- **Team / org context:** Mid-size UK building society (~1,500 employees, headquartered in Leeds) modernising its mortgage application platform away from a legacy Struts-based Java application.
- **What success looked like:** Reliable delivery of backend services, a credible Angular 2 prototype that informed the team's frontend direction, and a separated frontend build pipeline that improved developer feedback loops.

## Context & constraints

Northgate Building Society was a mid-size UK building society undergoing a technology modernisation programme centred on its mortgage application platform. The existing platform was a legacy Struts-based Java application. The organisation was conservative and risk-averse, as is typical of UK financial services — changes to production systems required careful justification and extensive QA sign-off.

Elena joined as her first permanent in-house role after leaving consulting. She was hired into the backend team to work on Java/Spring services supporting the mortgage application workflow. The team was relatively small: six backend developers, with a separate frontend team of three developers formed partway through her tenure as the frontend workload grew.

The frontend ecosystem was in flux during this period. The team initially used AngularJS 1.5, but Angular 2 was emerging in beta/RC and the team needed to evaluate whether to adopt it. This created a window for Elena to move toward frontend work. The conservative environment meant that any framework migration needed thorough justification — a proof of concept was the mechanism for building confidence in the decision.

## Core responsibilities

- Maintained and extended Java/Spring REST APIs serving the mortgage application workflow, including eligibility calculations, document upload services, and integration with credit reference agencies.
- Contributed to both backend and frontend codebases, becoming the informal bridge between the two teams as the frontend team was established.
- Participated in cross-team discussions about API design and contract consistency.
- Supported QA processes for changes to the mortgage platform.

## Initiatives

### Mortgage application backend services

- **Problem:** The mortgage application platform required ongoing maintenance and extension of its backend services, including eligibility calculations, document upload handling, and integration with external credit reference agencies via SOAP APIs.
- **What I did:** Maintained and extended the Java/Spring REST APIs that served the mortgage application workflow. This included working on eligibility calculation logic, building and maintaining document upload services, and integrating with credit reference agencies through SOAP-based interfaces.
- **Technical details:** Java 8, Spring Boot, REST APIs, SOAP integrations with external credit reference agencies, PostgreSQL for data persistence. Standard enterprise Java work — nothing architecturally unusual.
- **Outcome:** The backend services continued to support the mortgage application workflow reliably. This was steady, necessary work rather than a transformative initiative.

### Angular 2 migration proof of concept

- **Problem:** The team's existing AngularJS 1.5 frontend needed a long-term replacement strategy. Angular 2 was in beta/RC and the team needed to evaluate whether it was a viable path forward, particularly within a risk-averse financial services environment where framework choices carry long-term consequences.
- **What I did:** Volunteered to lead the proof of concept. Built a working prototype of the mortgage eligibility calculator in Angular 2 with TypeScript. This was Elena's first substantial TypeScript work.
- **Technical details:** Angular 2 (beta/RC), TypeScript, component-based architecture. The prototype replicated a real piece of the mortgage workflow — the eligibility calculator — to demonstrate that Angular 2 could handle the domain's requirements.
- **Outcome:** The proof of concept provided the team with a concrete basis for evaluating Angular 2. It demonstrated that the framework was viable for the mortgage platform's needs. This initiative cemented Elena's shift from backend toward frontend work.

### Frontend build pipeline

- **Problem:** Frontend assets were previously compiled as part of the Java Maven build, meaning frontend developers had to run the entire Java build to see changes. This slowed feedback loops and created unnecessary coupling between frontend and backend development workflows.
- **What I did:** Established the team's first dedicated frontend build pipeline, initially using Gulp and later migrating to Webpack as the tooling ecosystem matured.
- **Technical details:** Gulp (initial implementation), Webpack (later replacement), decoupled from the existing Maven build process. The pipeline handled compilation, bundling, and asset processing independently of the Java backend build.
- **Outcome:** Frontend developers could iterate without waiting for the full Java build cycle. Developer feedback loops improved significantly. The separation also made it easier to reason about frontend and backend deployments independently.

### Cross-team API contract discussions

- **Problem:** As the backend and frontend teams operated increasingly independently, inconsistencies in API response shapes created friction. There was no formal documentation of internal API contracts.
- **What I did:** As someone straddling both teams, Elena became the informal bridge for API design discussions. She advocated for consistent API response shapes and introduced Swagger/OpenAPI documentation for internal APIs.
- **Technical details:** Swagger/OpenAPI for API documentation, applied to the internal REST APIs serving the mortgage platform frontend.
- **Outcome:** Internal APIs gained formal documentation, reducing ambiguity in cross-team communication. API response shapes became more consistent. This was influence-based rather than authority-based — Elena did not own the API design process, but her position across both teams gave her visibility into the friction points.

## Tech & skills used

- **Languages:** Java 8, TypeScript, JavaScript (ES6)
- **Frameworks:** Spring Boot, Angular 2 (beta/RC), AngularJS 1.5
- **Build tools:** Gulp, Webpack, Maven
- **APIs & integration:** REST APIs, SOAP, Swagger/OpenAPI
- **Data:** PostgreSQL
- **Testing:** JUnit, Jasmine, Karma
- **Infrastructure & tooling:** Git, Jenkins, IntelliJ IDEA

## Stakeholders & influence

- **Engineering manager:** Direct reporting line. Supported Elena's move toward frontend work and approved the Angular 2 proof of concept.
- **Backend team (6 developers):** Peers. Elena was a full member of this team for the duration of the role, contributing to shared backend services.
- **Frontend team (3 developers):** Formed mid-tenure as frontend workload grew. Elena collaborated closely with this team and increasingly contributed to their codebase, though she was never formally reassigned.
- **Product owner (mortgage platform):** Stakeholder for feature priorities and requirements across the mortgage application workflow.
- **QA team:** Collaborated on testing for changes to the mortgage platform.

Elena's influence was informal and situational rather than structural. Her position across both backend and frontend teams gave her visibility that others lacked, and she used this to advocate for better API contracts and frontend tooling. She did not hold any formal coordination or leadership role.

## Positioning notes

This was the pivotal transitional role in Elena's career. She entered as a backend Java developer and left as someone whose primary interest and growing expertise was in frontend architecture. The Angular 2 proof of concept was the turning point — it combined her enterprise Java discipline with the emerging frontend ecosystem in a way that felt natural rather than forced.

The role also planted the seed for Elena's later migration expertise. She experienced first-hand the challenges of moving from one frontend framework to another within a conservative, risk-averse financial services environment — including the need to build organisational confidence through prototyping, the importance of separating build tooling, and the value of clear API contracts when frontend and backend teams operate independently.

This should not be read as a leadership role. Elena was an individual contributor throughout, with no line management responsibilities. Her cross-team influence was a product of circumstance — she happened to be working across both codebases — rather than a deliberate organisational mandate. The "bridge" role emerged organically and was never formalised.
