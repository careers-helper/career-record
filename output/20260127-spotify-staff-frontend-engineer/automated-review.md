# Automated CV Review: Staff Frontend Engineer — Web Platform, Spotify

## Strong Alignment

- **Large-scale frontend platform experience:** The candidate's current role leading a migration across 15 applications and 45+ frontend developers directly addresses our requirement for someone who can "design and build shared tooling, libraries, and frameworks used by 100+ frontend engineers." The scale is credible and well-evidenced.
- **TypeScript and React expertise:** Both Aegon roles and the Kova role demonstrate deep, sustained React and TypeScript usage across multiple years and contexts. This is not surface-level familiarity.
- **Design systems at scale:** The CV shows two design systems built from scratch (45 components at Kova, 80+ at Aegon) with design tokens, Storybook, and accessibility testing integrated into CI. This directly addresses our requirement for "experience with design systems and component libraries at scale."
- **Micro-frontend architecture:** The module federation work at Kova (independent deployment across 4 applications sharing a common shell) demonstrates practical understanding of micro-frontend trade-offs, which we specifically called out in the JD.
- **Build systems and tooling:** The CV references Vite, Nx, Webpack, Vitest, and jscodeshift codemods. Experience with multiple bundlers and monorepo tooling (Nx) is a strong match for our "experience with build systems, bundlers, and frontend tooling" requirement.
- **Cross-team technical leadership:** The candidate has operated as a Staff/Principal IC influencing 8 teams at Aegon and 3 squads at Kova, with no indication of being a full-time manager. This matches our expectation of a Staff Engineer who can "work across multiple teams to improve developer experience, performance, and reliability."
- **Frontend modernisation:** The entire career narrative centres on large-scale migration and modernisation, which aligns perfectly with "lead large-scale frontend modernisation initiatives across multiple teams and codebases."
- **Performance optimisation:** Core Web Vitals tracking, Lighthouse CI performance budgets at Kova, and concrete performance improvements at Wellframe (load time reduction from 8-10 seconds to under 2) address our nice-to-have around "performance optimisation at scale."
- **Open-source contribution:** The react-migrator project (340 GitHub stars, published on npm) with a plugin architecture addresses our nice-to-have for open-source contributions and also reinforces the developer tooling depth.
- **Communication skills:** A conference talk at React Summit 2025 is not mentioned on the CV, but the profile and experience bullets are clearly articulated, suggesting strong written communication. The community of practice growing from 12 to 35+ engineers indicates an ability to build consensus and communicate technical direction.

## Gaps or Concerns

- **Spotify-scale web infrastructure experience:** While the candidate's scale (45 frontend developers, 15 applications) is substantial, our Web Platform team serves hundreds of millions of users and 100+ frontend engineers. There is a step up in scale that is not fully evidenced. The CV does not mention experience with the kind of web infrastructure challenges specific to consumer-scale applications (service workers, offline capabilities, streaming, real-time updates).
- **No mention of server-side rendering or streaming architectures:** This is listed as a nice-to-have in the JD, and the CV does not reference SSR experience in any professional role. For a web platform role, familiarity with SSR patterns is increasingly expected at Staff level.
- **A/B testing infrastructure:** This nice-to-have is not addressed anywhere in the CV. For a platform team at Spotify, A/B testing infrastructure is a significant concern, and the absence is notable.
- **Title consideration:** The candidate currently holds a Principal Frontend Engineer title. Our role is Staff Engineer. While scope may be comparable, the candidate may perceive this as a title regression, which could affect mutual fit.
- **Enterprise vs consumer context:** The candidate's experience is predominantly in enterprise contexts (insurance, government, fintech, health tech). Spotify is a consumer product with different performance, UX, and scale considerations. The CV does not demonstrate experience building platform infrastructure for consumer-facing, high-traffic web applications.
- **Monorepo tooling depth:** The CV mentions Nx but does not detail specific monorepo scaling challenges (dependency graph optimisation, remote caching, task orchestration at scale). At our scale, monorepo tooling is a significant part of the platform team's remit.
- **No mention of Bazel or Turborepo:** These are listed as nice-to-haves. The candidate mentions Nx only.

## Overall Assessment

This is a strong candidate for the role. The combination of large-scale migration leadership, design systems expertise, micro-frontend architecture experience, and developer tooling depth (including open-source codemods) maps well to the core requirements of the Web Platform Staff Engineer position. The candidate clearly operates at Staff/Principal level with cross-team influence and architectural ownership.

The primary gaps are around consumer-scale web platform experience and some of our nice-to-haves (SSR, A/B testing infrastructure). The enterprise-to-consumer transition is a common adjustment, and the underlying platform engineering skills transfer well. The absence of SSR experience is the most notable technical gap for a web platform role at this level.

Recommendation: progress to a technical phone screen to explore the candidate's approach to platform engineering at consumer scale and to understand their familiarity with web-specific infrastructure challenges beyond the migration domain.
