# Why your frontend migration keeps stalling (and what to do about it)

**Elena Vasquez**
Principal Frontend Engineer · Migration & Frontend Architecture

*November 4, 2025*

---

## The pattern I keep seeing

Every large organisation I have worked with has at least one frontend migration that has stalled. The symptoms are always the same: an ambitious plan was announced, a proof of concept was built, a few pages were converted, and then momentum quietly died. Six months later, the legacy framework is still running in production and the migration is "in progress" on a roadmap that nobody updates.

I have been leading frontend migrations for seven years now, across health tech, fintech, and insurance. The technical problems are real, but they are rarely the reason migrations fail. The reason migrations fail is that they are treated as technical projects when they are actually organisational change programmes.

## The three mistakes

### 1. Treating migration as a separate workstream

The most common mistake is creating a dedicated "migration team" that works in isolation from the product teams who own the applications. This feels logical: let the specialists handle it. But in practice, it creates a handover problem. The migration team converts pages, but the product team does not understand the new patterns. When the migration team moves on, the product team reverts to what they know.

The better approach is to embed migration capability within product teams. At Aegon, we run "migration sprints" where members of our small accelerator team pair directly with application team engineers for two weeks. The goal is not just to convert pages, but to transfer the skills and confidence needed for the team to continue independently.

### 2. Waiting for the perfect architecture

I have seen migrations delayed by months while architects debate state management libraries, folder structures, and component patterns. The desire to "get it right" before starting is understandable, but it is counterproductive. You will learn more from migrating three real pages than from six months of architectural discussion.

Start with a minimal, opinionated foundation and expect it to evolve. The first version of our React architecture at Aegon was deliberately simple. We made significant changes after the pilot, and again after the third application. Each change was informed by real migration experience rather than theoretical preference.

### 3. Underestimating the interop problem

If your migration strategy requires a feature freeze, it is not a migration strategy. It is a rewrite with extra steps. The hardest technical problem in any incremental migration is making the old and new frameworks coexist in the same application without the user noticing.

This is where most proofs of concept fall apart. They demonstrate the new framework in isolation, but they do not solve the integration problem: shared state, routing, event propagation, styling conflicts, and the hundred small details that make two frameworks coexist peacefully.

Invest heavily in the interop layer. It is unglamorous work, but it is the foundation that makes everything else possible. At Aegon, we spent nearly three months building our Web Components interop layer before migrating a single production page. That investment paid for itself many times over.

## What actually works

The migrations I have seen succeed share three characteristics:

**They are incremental.** New features are built in the new framework. Existing pages are migrated when they come up for maintenance. There is no "migration phase" that competes with product delivery; migration is simply how work gets done.

**They are automated where possible.** Repetitive conversion patterns should be handled by codemods, not by humans. At Aegon, our jscodeshift-based tooling handles roughly 60% of the boilerplate conversion for each page. This is not glamorous work either, but it dramatically reduces the per-page cost of migration and makes the economics viable.

**They have organisational sponsorship.** Someone with budget authority has agreed that migration is worth doing and has committed to protecting the time and resources needed to sustain it. Without this, migration will always lose to the next feature request.

## A realistic timeline

If you are planning a migration across 10+ applications and 20+ developers, plan for years, not months. Our migration at Aegon is a three-year programme and we are roughly halfway through after two years. That is on track, but it is slower than some stakeholders expected.

Be honest about this from the start. Unrealistic timelines create pressure to cut corners, which creates technical debt in the new codebase, which undermines the entire purpose of the migration.

## Final thought

The technical tools for frontend migration are better than they have ever been. Web Components, module federation, AST-based codemods, and modern build tools make incremental migration genuinely feasible in ways that were not possible five years ago.

But the tools are not the hard part. The hard part is sustaining organisational commitment to a multi-year programme of incremental improvement when there is always something more urgent to do. If you can solve that problem, the technical side will follow.
