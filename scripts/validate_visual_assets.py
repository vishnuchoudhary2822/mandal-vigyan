#!/usr/bin/env python3
"""Validate locally embedded visual assets, captions, and SVG accessibility metadata."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
errors: list[str] = []
markdown_image = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
html_image = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>', re.I)

for page in DOCS.rglob("*.md"):
    lines = page.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        matches = [(alt, source) for alt, source in markdown_image.findall(line)]
        matches += [(alt, source) for source, alt in html_image.findall(line)]
        for alt, source in matches:
            if not alt.strip():
                errors.append(f"{page.relative_to(ROOT)}:{index + 1}: image has no Hindi alt text")
            if source.startswith(("http://", "https://")):
                errors.append(f"{page.relative_to(ROOT)}:{index + 1}: external image must not be embedded without local attribution review")
                continue
            asset = (page.parent / source).resolve()
            if not asset.is_file():
                errors.append(f"{page.relative_to(ROOT)}:{index + 1}: missing image {source}")
            context = "\n".join(lines[index:min(len(lines), index + 12)])
            if "चित्र " not in context:
                errors.append(f"{page.relative_to(ROOT)}:{index + 1}: image has no nearby figure caption")

for svg in (DOCS / "assets").rglob("*.svg"):
    try:
        root = ET.parse(svg).getroot()
        title = root.find("{http://www.w3.org/2000/svg}title")
        if title is None or not (title.text or "").strip():
            errors.append(f"{svg.relative_to(ROOT)}: SVG has no descriptive title")
    except ET.ParseError as exc:
        errors.append(f"{svg.relative_to(ROOT)}: invalid SVG: {exc}")

if errors:
    print("Visual asset validation failed:\n" + "\n".join(errors))
    sys.exit(1)
print("Visual asset validation passed.")
