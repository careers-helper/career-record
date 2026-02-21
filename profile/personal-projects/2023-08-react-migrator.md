---
project_id: react-migrator
name: react-migrator
type: personal-project
status: active
start: 2023-08
end:
repo: https://github.com/elenavasquezuk/react-migrator
location: N/A
domain: developer tooling
keywords: [codemods, jscodeshift, angular, react, typescript, cli, ast, migration, open-source, npm]
---
# react-migrator — Personal Project (August 2023 – Present)

## Snapshot

An open-source Node.js CLI tool that automates common Angular-to-React migration patterns using AST-based codemods built on jscodeshift. The project originated from repeated manual work at Aegon UK, where Elena was writing the same jscodeshift transforms across multiple applications. The most reliable transforms were extracted and generalised into a standalone, published npm package. The tool handles approximately 60% of boilerplate conversion reliably, with the remainder flagged for manual intervention. Development is sporadic (evenings and weekends), and the 0.9.x versioning reflects that the tool has not reached a fully polished state. The project is active but not under continuous development.

## Context & constraints

- Solo project, developed in personal time (evenings and weekends). No employer involvement or IP entanglement beyond the original observation that these transforms were needed.
- The tool addresses a narrow problem: repeatable, mechanical Angular-to-React conversion patterns. It does not attempt full automated migration.
- Target users are frontend engineers performing incremental Angular-to-React migrations in medium-to-large codebases.
- No hosting costs — the tool is a CLI distributed via npm. Documentation is a static Docusaurus site.
- Must work across a range of Angular versions and project structures, which limits how tightly the tool can rely on specific Angular compiler internals.

## Goals & non-goals

**Goals:**

- Automate the most common, mechanically repeatable Angular-to-React conversion patterns.
- Produce output that is close enough to idiomatic React that a developer can review and finish the conversion, rather than starting from scratch.
- Provide a dry-run mode so engineers can assess the scope of changes before committing.
- Generate a migration report that identifies what was converted and what requires manual attention.
- Support a plugin architecture so users can extend the tool with transforms specific to their codebase.

**Non-goals:**

- Full, end-to-end automated migration. The tool explicitly does not aim to handle 100% of cases.
- Angular animation migration.
- Complex directive composition patterns.
- ngrx store pattern migration.
- Replacing human judgement on architectural decisions during migration (e.g., state management strategy, routing approach).

## User journeys / use-cases

1. **Bulk boilerplate conversion:** A developer runs `react-migrator` against an Angular project directory. The tool processes all eligible files, converts what it can, and outputs a report listing converted files, skipped files, and files requiring manual intervention.
2. **Dry-run assessment:** Before committing to a migration sprint, a tech lead runs `react-migrator --dry-run` to generate a report estimating the scope of automated vs. manual work.
3. **Selective transform execution:** A developer runs a single transform plugin (e.g., services-to-hooks only) against a subset of files, using the plugin architecture to target specific conversion patterns.
4. **Custom transform authoring:** A team writes a custom plugin to handle a codebase-specific pattern (e.g., a proprietary Angular decorator) and composes it with the built-in transforms.

## Architecture overview

The tool is a Node.js CLI application structured around a plugin-based transform pipeline.

- **CLI layer:** Built with Commander.js. Parses arguments, loads configuration from `.react-migrator.json`, and orchestrates the transform pipeline.
- **Transform engine:** Uses jscodeshift for JavaScript and TypeScript AST manipulation. Each transform is a standalone plugin that receives an AST, applies a specific conversion pattern, and returns the modified AST.
- **Angular template parser:** A custom, simplified parser that handles common Angular template syntax (structural directives, pipes, basic bindings). This is deliberately not the full `@angular/compiler` — it covers approximately 90% of template patterns encountered in practice.
- **Plugin system:** Each transform is an independent module that exports a standard interface. Transforms can be run individually or composed into a pipeline. Users can register custom transforms via configuration.
- **Reporting:** After all transforms run, the tool aggregates results and outputs a migration report with statistics (files processed, files converted, files skipped) and notes on items requiring manual intervention.

Configuration is read from `.react-migrator.json` in the target project root, allowing per-project customisation of which transforms to run, file inclusion/exclusion patterns, and output preferences.

## Key components

### CLI (`commander.js` entry point)

- Purpose: Argument parsing, configuration loading, orchestration.
- Public interface: `react-migrator [options] <target-directory>` with flags including `--dry-run`, `--plugins`, `--config`, `--verbose`.
- Loads `.react-migrator.json` if present, merges with CLI flags, and passes the resolved configuration to the transform engine.

### Transform engine

- Purpose: Runs the pipeline of transform plugins against the target files.
- Iterates over eligible files, applies each registered transform in sequence, collects results.
- Each transform receives a jscodeshift API instance and the file source, returns the transformed source or a no-change signal.

### Built-in transform plugins

- **Service-to-hook transform:** Converts Angular `@Injectable()` service classes to React custom hooks. Maps class methods to hook functions, converts constructor-injected dependencies to hook parameters or imported hooks.
- **Template-to-JSX transform:** Converts Angular template syntax to JSX. Handles `*ngIf` to conditional rendering, `*ngFor` to `.map()`, Angular pipes to function calls or inline expressions.
- **Reactive-forms-to-hook-form transform:** Migrates Angular reactive form patterns (`FormGroup`, `FormControl`, validators) to React Hook Form equivalents (`useForm`, `register`, validation schemas).
- **Module-to-component transform:** Converts Angular `@NgModule` and `@Component` declarations to standalone React component files, stripping Angular-specific decorators and metadata.

### Angular template parser

- Purpose: Parses Angular template HTML into a structure the template-to-JSX transform can process.
- Simplified implementation — does not replicate the full Angular compiler. Handles structural directives, property/event bindings, interpolation, and pipes.
- Patterns outside its capability are flagged in the migration report as requiring manual conversion.
- Known to fail on deeply nested structural directives and certain edge cases in microsyntax parsing.

### Migration reporter

- Purpose: Aggregates transform results and outputs a structured report.
- Reports: total files scanned, files converted, files skipped, per-transform success/failure counts, list of items flagged for manual intervention.

## Data model & persistence

The tool is stateless. It reads source files from disk, applies transforms in memory, and writes converted files back to disk (or reports what would change in dry-run mode). Configuration is read from `.react-migrator.json` but the tool does not maintain any persistent state between runs.

The migration report is written to stdout by default, with an option to output as a JSON file.

## Integrations

- **npm:** Published as `react-migrator`. 12 releases to date, latest v0.9.2.
- **jscodeshift:** Core dependency for AST manipulation of JavaScript and TypeScript files.
- **Commander.js:** CLI framework.
- No external service integrations, API calls, or authentication. The tool operates entirely on local files.

## Development workflow

- Language: TypeScript, compiled with tsup.
- Testing: Vitest with a fixture-based approach — each test provides an input Angular file and an expected React output file. The transform is run against the input and the result is compared to the expected output.
- Test coverage: 85% on transform plugins.
- Linting and formatting: not explicitly detailed, but CI runs a lint step (likely ESLint given the TypeScript/Node.js context).
- Local development: standard `npm install`, `npm run build`, `npm test` workflow (inferred from tooling choices).

## Deployment & operations

- **Distribution:** Published to npm. No server deployment — the tool is a CLI that runs locally.
- **CI/CD:** GitHub Actions pipeline with lint, test, and build steps. Publishing to npm is triggered on git tag.
- **Documentation:** A basic Docusaurus site covering installation, usage, available transforms, and plugin authoring.
- **No monitoring or alerting** — not applicable for a CLI tool.

## Notable decisions & trade-offs

### 1. jscodeshift over ts-morph

- **Problem:** Needed an AST manipulation library for writing codemods against JavaScript and TypeScript files.
- **Options considered:** jscodeshift, ts-morph.
- **Decision:** jscodeshift.
- **Trade-offs:** jscodeshift had stronger community support and a larger ecosystem of existing codemods at the time of the decision. ts-morph offers type-aware transforms, which would have been useful for more precise conversions (e.g., inferring types during service-to-hook conversion). This trade-off was accepted — the community ecosystem was valued over type awareness.

### 2. Custom Angular template parser instead of @angular/compiler

- **Problem:** Needed to parse Angular templates to convert them to JSX.
- **Options considered:** Using the full `@angular/compiler` package, writing a custom simplified parser.
- **Decision:** Custom simplified parser.
- **Trade-offs:** The full Angular compiler is heavy, complex, and tightly coupled to specific Angular versions. The custom parser handles approximately 90% of template patterns encountered in practice. The remaining 10% are flagged for manual conversion. This means the tool cannot handle edge cases in Angular template microsyntax, but avoids a large and version-sensitive dependency.

### 3. Plugin architecture

- **Problem:** Every codebase has unique conventions (custom decorators, wrapper patterns, project-specific Angular extensions) that a fixed set of transforms cannot cover.
- **Options considered:** Fixed transform set only, plugin architecture.
- **Decision:** Plugin architecture allowing user-defined transforms.
- **Trade-offs:** Adds complexity to the codebase and requires documenting a plugin API. However, this was considered essential for real-world adoption, since without it the tool would only work for codebases that exactly match the built-in patterns.

## Change history & status

- **August 2023:** Project started. Initial transforms extracted from work done during Angular-to-React migrations at Aegon UK.
- **2023–2024:** Iterative development across 12 npm releases, reaching v0.9.2. Core transforms (services, templates, forms, modules) stabilised. Plugin architecture added.
- **As of February 2026:** 340 GitHub stars, 28 forks. 3 external contributors have submitted pull requests (mostly bug fixes and additional template patterns). At least 2 other companies are using the tool based on GitHub issue reports. Development cadence is sporadic — evenings and weekends only. The 0.9.x version number reflects that the tool works but has not reached a level of polish or completeness that would warrant a 1.0 release.
- **Known limitations:** Does not handle Angular animations, complex directive composition, or ngrx store patterns. The custom template parser has known edge cases.

## Tech & skills used

**Languages:**

- TypeScript

**Frameworks & libraries:**

- jscodeshift (AST manipulation)
- Commander.js (CLI framework)
- React Hook Form (target output patterns)

**Tooling:**

- tsup (TypeScript compilation and bundling)
- Vitest (testing)
- GitHub Actions (CI/CD)
- npm (package distribution)
- Docusaurus (documentation site)

**Practices:**

- Fixture-based testing (input file to expected output file comparison)
- Plugin architecture for extensibility
- Dry-run mode for non-destructive assessment
- Semantic versioning
- Tag-triggered publishing

## Stakeholders & collaboration

Solo project. Elena is the sole maintainer and primary author. Three external contributors have submitted pull requests (bug fixes and additional template patterns), but all architectural decisions and core development are Elena's. There is no formal governance or contribution process beyond standard GitHub pull request review.

## Positioning notes

- This project directly demonstrates migration expertise in a tangible, open-source form. It shows the ability to extract patterns from proprietary work into reusable, generalised tooling.
- It demonstrates depth in AST manipulation, developer tooling, and the specific Angular-to-React migration domain.
- The tool is firmly a side project. Development is sporadic, and the 0.9.x version reflects that it has not reached the polish level of a fully supported open-source project. It should not be presented as equivalent to a professionally maintained tool.
- The 340 stars and external adoption provide evidence that the tool solves a real problem, but the contributor base is small and the maintenance burden is carried by one person.
- Most relevant when applying for roles involving migration, developer tooling, frontend platform work, or open-source contribution. Less relevant for roles focused purely on product feature delivery.
