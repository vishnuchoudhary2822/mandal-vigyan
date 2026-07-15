#!/usr/bin/env python3
"""Build PDF and EPUB from SUMMARY.md using Pandoc."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
if not shutil.which("pandoc"):
    sys.exit("Pandoc is required. Install it from https://pandoc.org/.")
lines = (ROOT / "SUMMARY.md").read_text(encoding="utf-8").splitlines()
chapters = [ROOT / line.split("](", 1)[1].rstrip(")") for line in lines if line.startswith("- [")]
for folder, suffix in (("pdf", "pdf"), ("epub", "epub")):
    output = ROOT / folder / f"mandal-vigyan.{suffix}"
    command = ["pandoc", "--from", "gfm", "--metadata", "lang=hi", "--toc", "--output", str(output), *map(str, chapters)]
    if suffix == "pdf":
        command[1:1] = ["--pdf-engine=xelatex", "-V", "mainfont=Noto Sans Devanagari"]
    subprocess.run(command, check=True)
    print(f"Created {output.relative_to(ROOT)}")
