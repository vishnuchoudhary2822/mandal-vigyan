#!/usr/bin/env python3
"""Fast structural checks for the content-free Markdown manuscript."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["परिचय", "इतिहास", "संस्कृत स्रोत", "मूल संस्कृत", "हिन्दी अनुवाद", "शब्दार्थ", "व्याख्या", "वैज्ञानिक विश्लेषण", "तुलना तालिका", "महत्वपूर्ण टिप्पणियाँ", "आरेख", "सन्दर्भ", "सारांश", "प्रश्न"]
errors = []
for chapter in sorted((ROOT / "chapters").glob("[0-9][0-9]-*.md")):
    text = chapter.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED if f"## {heading}" not in text]
    if missing:
        errors.append(f"{chapter.relative_to(ROOT)}: missing {', '.join(missing)}")
    if not re.search(r"### पुराणिक कथन.*?### पारम्परिक व्याख्या.*?### आधुनिक वैज्ञानिक दृष्टि", text, re.S):
        errors.append(f"{chapter.relative_to(ROOT)}: missing required source-separation headings")
if errors:
    print("Markdown validation failed:\n" + "\n".join(errors))
    sys.exit(1)
print("Markdown validation passed.")
