#!/usr/bin/env python3
"""
Convert a CV markdown file to a styled Word document.

Usage:
    python3 infrastructure/generate-cv-docx.py <input.md> [output.docx]

If output path is not specified, the .md extension is replaced with .docx.

This script:
1. Converts markdown to docx via Pandoc, using infrastructure/sample-cv.docx
   as the reference document for style definitions
2. Post-processes the docx to correct style assignments that Pandoc cannot
   infer from markdown structure alone
3. Sets line spacing to 1.10x on all paragraphs to match the sample CV

Style corrections applied:
    - Heading 1 (name line)              → Title
    - Normal (tagline, contact info)     → Subtitle
    - Normal (company/date after role)   → Heading 4
    - Normal (bullet items)              → List Paragraph
    - Normal (older role lines)          → Heading 5
    - All paragraphs                     → line spacing 1.10x

Requirements:
    - pandoc (system install)
    - python-docx (pip install python-docx)
"""

import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


# ── Helpers ──────────────────────────────────────────────────────────────────


def has_bold_runs(paragraph):
    """Check if any run in the paragraph is bold."""
    return any(run.bold for run in paragraph.runs)


def has_italic_runs(paragraph):
    """Check if any run in the paragraph is italic."""
    return any(run.italic for run in paragraph.runs)


def is_older_role_line(paragraph):
    """
    Detect older-role lines matching the pattern: **Title (Company)** — _Dates_

    These have bold runs, italic runs, and an em-dash separator.
    """
    text = paragraph.text.strip()
    return bool(text) and "\u2014" in text and has_bold_runs(paragraph) and has_italic_runs(paragraph)


def has_numbering(paragraph):
    """Check if Pandoc assigned list numbering XML to this paragraph."""
    pPr = paragraph._element.find(qn("w:pPr"))
    if pPr is not None:
        return pPr.find(qn("w:numPr")) is not None
    return False


def get_style(doc, name):
    """Get a style by name, returning None if not found."""
    try:
        return doc.styles[name]
    except KeyError:
        return None


def section_for(heading_text):
    """Map a Heading 2 text to a state name."""
    return {
        "Profile": "profile",
        "Experience": "experience",
        "Skills": "skills",
        "Personal Projects": "personal_projects",
    }.get(heading_text, "other")


def clear_run_formatting(paragraph):
    """
    Remove all run-level formatting (rPr) so the paragraph style controls
    appearance. Use on paragraphs where Pandoc applied bold/italic from
    markdown syntax but the style should provide all formatting.
    """
    for run in paragraph.runs:
        rPr = run._element.find(qn("w:rPr"))
        if rPr is not None:
            run._element.remove(rPr)


def insert_date_tab(paragraph, date_color_auto=False):
    """
    Rebuild a company/date or older-role paragraph with a right-aligned tab
    before the date portion.

    Pandoc merges **bold** and _italic_ lines into one paragraph. The italic
    runs contain the date. This function splits on that boundary, clears the
    paragraph, and rebuilds as: label [tab] date. The Heading 4/5 styles
    already define a right-aligned tab stop, so the date will sit at the
    right margin.

    If date_color_auto is True (for Heading 5 older roles), the date runs
    get color=auto so they render black, matching the sample.
    """
    runs = list(paragraph.runs)
    if not runs:
        return

    # Find the first italic run — everything from there is the date
    italic_idx = None
    for i, run in enumerate(runs):
        if run.italic:
            italic_idx = i
            break

    if italic_idx is None:
        return

    # Extract label (before italic) and date (italic onwards)
    label = "".join(r.text for r in runs[:italic_idx])
    label = label.rstrip(" \u2014\u2013\u2012-")  # strip trailing separators
    date = "".join(r.text for r in runs[italic_idx:]).strip()

    if not label or not date:
        return

    # Clear all existing runs
    for r_elem in paragraph._element.findall(qn("w:r")):
        paragraph._element.remove(r_elem)

    # Rebuild: label + tab + date (no explicit bold/italic — style provides it)
    paragraph.add_run(label)

    tab_run = paragraph.add_run()
    tab_elem = OxmlElement("w:tab")
    tab_run._element.append(tab_elem)

    date_run = paragraph.add_run(date)

    if date_color_auto:
        # Apply color=auto (black) to date run, matching sample Heading 5
        rPr = date_run._element.find(qn("w:rPr"))
        if rPr is None:
            rPr = OxmlElement("w:rPr")
            date_run._element.insert(0, rPr)
        color = OxmlElement("w:color")
        color.set(qn("w:val"), "auto")
        rPr.append(color)


def ensure_right_tab_stop(doc, style_name, position=9639):
    """
    Ensure a style has a right-aligned tab stop at the given position (twips).
    The sample-cv.docx defines these on Heading 4 and Heading 5.
    If Pandoc didn't carry them over, add them.
    """
    style = get_style(doc, style_name)
    if style is None:
        return

    pPr = style.element.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr")
        style.element.append(pPr)

    tabs = pPr.find(qn("w:tabs"))
    if tabs is not None:
        # Check if a right tab already exists
        for tab in tabs.findall(qn("w:tab")):
            if tab.get(qn("w:val")) == "right":
                return  # already has one
    else:
        tabs = OxmlElement("w:tabs")
        pPr.append(tabs)

    tab = OxmlElement("w:tab")
    tab.set(qn("w:val"), "right")
    tab.set(qn("w:pos"), str(position))
    tabs.append(tab)


# ── Pandoc conversion ───────────────────────────────────────────────────────


def run_pandoc(md_path, docx_path, reference_doc):
    """Run Pandoc to convert markdown to docx with reference styling."""
    cmd = [
        "pandoc",
        str(md_path),
        "-o",
        str(docx_path),
        "--reference-doc",
        str(reference_doc),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Pandoc error: {result.stderr}", file=sys.stderr)
        sys.exit(1)


# ── Post-processing ─────────────────────────────────────────────────────────


def post_process(docx_path):
    """Fix style assignments and line spacing in a Pandoc-generated CV docx."""
    doc = Document(str(docx_path))

    # Verify required styles exist
    required = ["Title", "Subtitle", "Quote", "Heading 4", "Heading 5", "List Paragraph"]
    styles = {}
    for name in required:
        s = get_style(doc, name)
        if s is None:
            print(
                f"Warning: Style '{name}' not found in document. "
                f"Ensure sample-cv.docx defines this style.",
                file=sys.stderr,
            )
        styles[name] = s

    # Ensure right-aligned tab stops exist on heading styles (for date alignment)
    ensure_right_tab_stop(doc, "Heading 4")
    ensure_right_tab_stop(doc, "Heading 5")

    # State tracking
    state = "header"
    expect_company_date = False
    expect_description = False
    in_role_bullets = False

    for p in doc.paragraphs:
        style_name = p.style.name
        text = p.text.strip()

        # Set line spacing on every paragraph (sample uses 1.10x throughout)
        p.paragraph_format.line_spacing = 1.10

        if not text:
            continue

        # ── Header: everything before the first Heading 2 ────────────────
        if state == "header":
            if style_name == "Heading 1" and styles.get("Title"):
                p.style = styles["Title"]
                clear_run_formatting(p)
            elif style_name == "Heading 2":
                state = section_for(text)
            elif has_bold_runs(p) and styles.get("Subtitle"):
                # Tagline line (from **bold** markdown) → Subtitle
                p.style = styles["Subtitle"]
                clear_run_formatting(p)
            elif styles.get("Quote"):
                # Contact info line (from _italic_ markdown) → Quote
                p.style = styles["Quote"]
                clear_run_formatting(p)
            continue

        # ── Section transitions on any Heading 2 ─────────────────────────
        if style_name == "Heading 2":
            state = section_for(text)
            expect_company_date = False
            expect_description = False
            in_role_bullets = False
            continue

        # ── Profile: Normal paragraphs, nothing to change ────────────────
        if state == "profile":
            continue

        # ── Skills: Heading 4 + Normal, already correct ──────────────────
        if state == "skills":
            continue

        # ── Personal Projects: leave as-is for now ───────────────────────
        if state == "personal_projects":
            continue

        # ── Experience section (the complex one) ─────────────────────────
        if state == "experience":

            # New detailed role
            if style_name == "Heading 3":
                expect_company_date = True
                expect_description = False
                in_role_bullets = False
                continue

            # Company/location + dates line → Heading 4 with right-aligned date
            if expect_company_date and style_name in ("Normal", "Body Text"):
                insert_date_tab(p)
                if styles.get("Heading 4"):
                    p.style = styles["Heading 4"]
                expect_company_date = False
                expect_description = True
                continue

            # Role description sentence → stays Normal
            if expect_description and style_name in ("Normal", "Body Text"):
                expect_description = False
                in_role_bullets = True
                continue

            # Bullet zone: list items or transition to older roles
            if in_role_bullets and style_name in ("Normal", "Body Text", "Compact"):
                if is_older_role_line(p):
                    insert_date_tab(p, date_color_auto=True)
                    if styles.get("Heading 5"):
                        p.style = styles["Heading 5"]
                    in_role_bullets = False
                else:
                    if styles.get("List Paragraph"):
                        p.style = styles["List Paragraph"]
                continue

            # Outside a role block: catch remaining older role lines
            if style_name in ("Normal", "Body Text"):
                if is_older_role_line(p) and styles.get("Heading 5"):
                    insert_date_tab(p, date_color_auto=True)
                    p.style = styles["Heading 5"]

    doc.save(str(docx_path))


# ── Main ─────────────────────────────────────────────────────────────────────


def main():
    if len(sys.argv) < 2:
        print(
            f"Usage: python3 {sys.argv[0]} <input.md> [output.docx]",
            file=sys.stderr,
        )
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"Error: {md_path} not found", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) >= 3:
        docx_path = Path(sys.argv[2])
    else:
        docx_path = md_path.with_suffix(".docx")

    # Reference doc is in the same directory as this script
    script_dir = Path(__file__).resolve().parent
    reference_doc = script_dir / "sample-cv.docx"
    if not reference_doc.exists():
        print(f"Error: Reference document not found: {reference_doc}", file=sys.stderr)
        sys.exit(1)

    print(f"Converting: {md_path}")
    print(f"Reference:  {reference_doc}")
    print(f"Output:     {docx_path}")
    print()

    run_pandoc(md_path, docx_path, reference_doc)
    print("Pandoc conversion complete. Post-processing styles...")

    post_process(docx_path)
    print("Done.")


if __name__ == "__main__":
    main()
