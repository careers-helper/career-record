import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const strictMode = process.argv.includes('--strict');

const outputDir = join(root, 'output');
const personalDir = join(root, 'profile', 'personal-projects');

const allowedStages = new Set(['REVIEW', 'NOAPP', 'APP', 'INT', 'OFF', 'ACC', 'REJ', 'WDR']);
const roleFolderPattern = /^\d{8}-[a-z0-9]+(?:-[a-z0-9]+)*$/;

const errors: string[] = [];
const warnings: string[] = [];

function isDirectory(path: string): boolean {
  return statSync(path).isDirectory();
}

function readSubdirs(path: string): string[] {
  return readdirSync(path).filter((name) => isDirectory(join(path, name)));
}

function lintRoleFolders(): void {
  if (!existsSync(outputDir)) {
    warnings.push('output/: directory not found');
    return;
  }

  const folders = readSubdirs(outputDir);

  for (const folder of folders) {
    if (!roleFolderPattern.test(folder)) {
      errors.push(`output/${folder}: folder name must match YYYYMMDD-company-role`);
    }

    const files = readdirSync(join(outputDir, folder));
    const statuses = files.filter((name) => name.startsWith('_'));

    if (statuses.length !== 1) {
      errors.push(`output/${folder}: expected exactly one status file, found ${statuses.length}`);
      continue;
    }

    const status = statuses[0];
    if (!/^_[A-Z_]+$/.test(status)) {
      errors.push(`output/${folder}: invalid status filename ${status}`);
      continue;
    }

    const stages = status.slice(1).split('_').filter(Boolean);
    const unknown = stages.filter((stage) => !allowedStages.has(stage));

    if (unknown.length > 0) {
      errors.push(`output/${folder}: unknown status stage(s): ${unknown.join(', ')}`);
    }
  }
}

// NOTE: This parser handles single-line key: value pairs only. YAML arrays
// that wrap across multiple lines (e.g. keywords) will be captured as the first
// line's value. This is acceptable because all frontmatter in this repo currently
// uses single-line values.
function parseFrontmatter(content: string): Map<string, string> {
  const map = new Map<string, string>();
  const lines = content.split(/\r?\n/);

  if (lines[0] !== '---') {
    return map;
  }

  for (let i = 1; i < lines.length; i += 1) {
    const line = lines[i];
    if (line === '---') {
      break;
    }

    const idx = line.indexOf(':');
    if (idx === -1) {
      continue;
    }

    const key = line.slice(0, idx).trim();
    const value = line.slice(idx + 1).trim();
    map.set(key, value);
  }

  return map;
}

function lintPersonalFrontmatter(): void {
  if (!existsSync(personalDir)) {
    warnings.push('profile/personal-projects/: directory not found');
    return;
  }

  const files = readdirSync(personalDir).filter((name) => name.endsWith('.md'));

  for (const file of files) {
    const fullPath = join(personalDir, file);
    const content = readFileSync(fullPath, 'utf8');
    const fm = parseFrontmatter(content);

    if (fm.size === 0) {
      warnings.push(`profile/personal-projects/${file}: missing or malformed frontmatter`);
      continue;
    }

    const type = fm.get('type');
    if (!type) {
      warnings.push(`profile/personal-projects/${file}: missing type field in frontmatter`);
    } else if (type !== 'personal-project') {
      errors.push(`profile/personal-projects/${file}: type must be personal-project (found ${type})`);
    }
  }
}

function lintKeywordTypos(): void {
  const workDir = join(root, 'profile', 'work-experience');
  if (!existsSync(workDir)) {
    warnings.push('profile/work-experience/: directory not found');
    return;
  }

  const files = readdirSync(workDir).filter((name) => name.endsWith('.md'));

  for (const file of files) {
    const fullPath = join(workDir, file);
    const content = readFileSync(fullPath, 'utf8');
    const keywordLine = content
      .split(/\r?\n/)
      .find((line) => line.trimStart().startsWith('keywords:'));

    if (!keywordLine) {
      continue;
    }

    if (keywordLine.includes('typecript-')) {
      errors.push(`profile/work-experience/${file}: keyword typo detected (typecript-*)`);
    }

    const start = keywordLine.indexOf('[');
    const end = keywordLine.lastIndexOf(']');
    if (start === -1 || end === -1 || end <= start) {
      continue;
    }

    const items = keywordLine
      .slice(start + 1, end)
      .split(',')
      .map((item) => item.trim())
      .filter(Boolean);

    const seen = new Set<string>();
    const dupes = new Set<string>();

    for (const item of items) {
      if (seen.has(item)) {
        dupes.add(item);
      }
      seen.add(item);
    }

    if (dupes.size > 0) {
      warnings.push(`profile/work-experience/${file}: duplicate keyword(s): ${Array.from(dupes).join(', ')}`);
    }
  }
}

function lintWorkRoleFormat(): void {
  const workDir = join(root, 'profile', 'work-experience');
  if (!existsSync(workDir)) {
    warnings.push('profile/work-experience/: directory not found');
    return;
  }

  const files = readdirSync(workDir).filter((name) => name.endsWith('.md'));

  for (const file of files) {
    const fullPath = join(workDir, file);
    const lines = readFileSync(fullPath, 'utf8').split(/\r?\n/);

    const h1 = lines.find((line) => line.startsWith('# '));
    if (!h1) {
      warnings.push(`profile/work-experience/${file}: missing H1 role header`);
      continue;
    }

    if (!h1.startsWith('# Role: ')) {
      warnings.push(`profile/work-experience/${file}: role header should use \"# Role: <Company> — <Title> (...)\" format`);
    }

    const snapshotIndex = lines.findIndex((line) => line.trim() === '## Snapshot');
    if (snapshotIndex === -1) {
      warnings.push(`profile/work-experience/${file}: missing ## Snapshot section`);
      continue;
    }

    const nextHeadingIndex = lines.findIndex((line, idx) => idx > snapshotIndex && line.startsWith('## '));
    const snapshotEnd = nextHeadingIndex === -1 ? lines.length : nextHeadingIndex;
    const snapshotLines = lines.slice(snapshotIndex + 1, snapshotEnd).map((line) => line.trim()).filter(Boolean);

    const expected = [
      '- **One-liner:**',
      '- **Scope:**',
      '- **Team / org context:**',
      '- **What success looked like:**',
    ];

    const hasStructuredSnapshot = expected.every((prefix) =>
      snapshotLines.some((line) => line.startsWith(prefix)),
    );

    if (!hasStructuredSnapshot) {
      warnings.push(`profile/work-experience/${file}: snapshot should use structured bullets (One-liner, Scope, Team / org context, What success looked like)`);
    }
  }
}

function printFindings(label: string, findings: string[]): void {
  if (findings.length === 0) {
    return;
  }

  console.log(`\n${label}`);
  for (const finding of findings) {
    console.log(`- ${finding}`);
  }
}

lintRoleFolders();
lintPersonalFrontmatter();
lintKeywordTypos();
lintWorkRoleFormat();

printFindings('Errors', errors);
printFindings('Warnings', warnings);

const shouldFail = errors.length > 0 || (strictMode && warnings.length > 0);

if (shouldFail) {
  process.exit(1);
}

console.log('\ncareer-record lint passed');
