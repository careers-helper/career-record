# Suitability Report: Principal Engineer — Web Modernisation, John Lewis Partnership

## Overall

- **Fit score:** Strong fit
- **Recommendation:** Pursue
- **One-line summary:** This role is an almost exact match for Elena's career specialism: leading a large-scale Angular-to-React migration across multiple teams in an enterprise retail environment, using incremental strategies and codemods.

## Key Alignments

- **Migration expertise is the core requirement.** Elena has been leading an Angular-to-React migration across 15 applications and 45+ developers at Aegon UK since 2022. The JD describes essentially the same problem at a comparable scale (6+ teams, ~30 frontend engineers, AngularJS/Angular 1.x to React).
- **Incremental migration strategy.** The JD explicitly requires experience designing incremental approaches that avoid feature freezes. Elena's strangler fig approach at Aegon, validated through a pilot and now 50% complete across the portfolio, is a direct answer.
- **Codemods and automated tooling.** Listed as desirable in the JD. Elena has built production codemods at Aegon (jscodeshift, ~60% boilerplate automation) and published an open-source CLI tool (react-migrator, 340 GitHub stars) that generalises these patterns. This is unusually strong evidence for a desirable criterion.
- **React and TypeScript depth.** Elena has worked with React since 2018 (Wellframe) and TypeScript since the Northgate Angular 2 PoC in 2013. Her current role uses React 18/19 with TypeScript across all migration work.
- **Design systems and component libraries.** Elena has built or scaled design systems at three organisations (Wellframe, Kova, Aegon). The Aegon React UI library (80+ components, design tokens, WCAG 2.1 AA compliance testing) is directly relevant to the JD's requirement for a unified design system.
- **Micro-frontend and modular patterns.** Module federation architecture at Kova; Web Components interop layer at Aegon. Both are relevant to the JD's micro-frontend requirement.
- **Cross-team influence at scale without direct authority.** Elena currently coordinates migration across 8 teams and ~45 developers at Aegon, influencing through tooling, process, and demonstrated value. The JD asks for experience influencing 20+ engineers across multiple teams.
- **Seniority match.** Principal Engineer title, held since 2022. The JD asks for Principal or equivalent.
- **Retail and e-commerce adjacency.** Elena's Northgate Building Society role was in retail banking (mortgage platform). Her Aegon roles serve customer-facing insurance and pensions products. While not retail/e-commerce directly, enterprise consumer-facing digital platforms are closely adjacent.
- **Conference speaking on migration.** The JD lists conference speaking as desirable. Elena has spoken at React Summit (2025) and Frontend Connect (2024) on exactly this topic.
- **Accessibility.** WCAG 2.1 experience from GDS, embedded into the Aegon component library. The JD lists WCAG 2.1/2.2 knowledge as desirable.
- **Angular/AngularJS familiarity.** Listed as desirable. Elena has worked with Angular versions 8 through 14 in the migration context and AngularJS 1.x at Northgate. The migration source at JLP is Angular 1.x/AngularJS, which is older than Elena's primary Angular experience, but the migration patterns transfer.
- **CI/CD and build tooling.** Experience with Vite, Nx, Jenkins, Azure DevOps, GitHub Actions across multiple roles.
- **Benefits package is strong.** Partnership pension (up to 8%), private medical, learning budget, enhanced parental leave all align with Elena's preferences.

## Key Concerns

- **Salary range starts at Elena's minimum.** The range is £125k-£150k. Elena's hard minimum is £130k. The bottom of the range (£125k) is below her floor, but the range comfortably extends above it. She should clarify salary expectations early to avoid proceeding at the bottom of the band.
- **Hybrid, not remote.** The role requires 2 days per week in either London (Victoria) or Bracknell. Elena's strong preference is fully remote. London Victoria is accessible from Bristol (Temple Meads to Paddington, then Victoria line), making 2 days per week workable but not ideal. Bracknell is less convenient from Bristol. This is a significant but not disqualifying concern: the hybrid arrangement falls within Elena's stated tolerance for London-based hybrid roles.
- **AngularJS 1.x specifics.** The JLP migration source is Angular 1.x/AngularJS, which is structurally different from the Angular 8-14 estate Elena has been migrating at Aegon. The migration patterns (incremental adoption, codemods, interop layers) transfer, but there may be AngularJS-specific challenges (no module system, different DI patterns, template syntax differences) that require adjustment. Elena has some AngularJS 1.x exposure from Northgate but it is not deep.
- **Next.js / SSR experience.** Listed as desirable. Elena has used Next.js 14 (App Router) on her a11y-audit-dashboard personal project but has no professional Next.js experience. If JLP's target architecture is Next.js-based, this could be a gap.
- **Monorepo tooling.** Listed as desirable (Nx, Turborepo). Elena has production Nx experience at Aegon, which covers this.
- **Meeting load unknown.** The role involves reporting to senior leadership and the Partnership Board, coordinating across 6+ teams, and working with UX/Design. The meeting load could be significant. Elena's preference is a maximum of one third of her time in meetings.
- **"Complex organisational environments."** JLP is the UK's largest employee-owned business (80,000 Partners). The governance and decision-making structures may be more complex than Aegon's. Elena has enterprise experience but has not worked in an employee-owned partnership model.

## Experience Highlights

If applying, emphasise:

- **Aegon Migration Lead role (2024-present):** The closest parallel to what JLP needs. Angular-to-React migration, 15 apps, 45 developers, 8 teams, incremental strategy, codemods, design system, governance framework. Lead with this.
- **Aegon Principal Frontend Engineer role (2022-2024):** The strategy and architecture phase. Strangler fig approach, Web Components interop, pilot validation, community of practice for building consensus. Shows the full lifecycle from strategy through to execution.
- **react-migrator (personal project):** Open-source codemod tool for Angular-to-React migration. Directly relevant to the JD's desirable criterion around codemods and jscodeshift. Include the GitHub URL.
- **Kova Staff Frontend Engineer role:** Micro-frontend architecture (module federation), design system from scratch, cross-team influence without authority at a smaller scale.
- **GDS Frontend Developer role:** Accessibility foundations (WCAG 2.1 AA), GOV.UK Design System contributions. Relevant to the desirable accessibility criterion.
- **Conference talks:** "The Strangler Fig in Practice" at React Summit (2025) and "Codemods at Scale" at Frontend Connect (2024) are directly on-topic for this JD.
- **Northgate Building Society:** AngularJS 1.x and Angular 2 experience in a financial services context. Relevant given the AngularJS migration source at JLP.

## Questions to Ask

1. **Salary band positioning.** The range is £125k-£150k. Where does JLP typically place candidates with extensive, directly relevant experience? Elena's minimum is £130k; she would want to understand where in the band this role would sit before proceeding.
2. **Office location flexibility.** Is the role London (Victoria) or Bracknell, or is there a choice? From Bristol, London is significantly more convenient. Can the hybrid arrangement accommodate Bristol-to-London commuting?
3. **Target architecture.** Is the target stack React with client-side rendering, or is Next.js/SSR part of the plan? This affects both the migration approach and the relevance of Elena's experience.
4. **Meeting load.** How much of the Principal Engineer's time is typically spent in meetings, governance forums, and stakeholder reporting versus hands-on technical work?
5. **Migration timeline.** What is the expected timeline for the migration? Is there an existing strategy or is the Principal Engineer expected to define it from scratch?
6. **Current state of the legacy stack.** How old is the Angular 1.x/AngularJS codebase? Are there server-rendered templates alongside AngularJS, or is it purely SPA? This affects the migration approach significantly.
7. **Team structure.** Will the Principal Engineer have a dedicated migration team, or is the expectation to coordinate migration work within existing product teams' capacity?
8. **Autonomy.** How much latitude does the Principal Engineer have to define the migration approach, versus working within an already-decided strategy?

## Compensation Note

The salary range of £125k-£150k overlaps with Elena's requirements, but the bottom of the range (£125k) is below her £130k hard minimum. The Partnership bonus (3-5%) and strong pension (up to 8% employer contribution) add meaningful value beyond base salary. Elena should confirm early that the base salary would be at least £130k. The pension contribution and Partnership discount are notable benefits that differentiate this from typical private-sector packages.
