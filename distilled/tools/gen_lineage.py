#!/usr/bin/env python3
"""Build LINEAGE_ORDER.txt: the 2,993 unique files ordered by earliest signal.

Lineage signal = (modification time, then path) — earliest first ("file 1" = the seed).
Version markers (vN, Paper N, ArXiv_N, LatestUpdateVN, Attempt2) are surfaced as hints.
"""
import re
from pathlib import Path

ROOT = Path("/home/kmon/AA-Erebo/Genesis-Seeds")
manifest = [l.strip() for l in (ROOT / "distilled" / "UNIQUE_MANIFEST.txt").read_text().splitlines() if l.strip()]

def mtime(rel: str) -> float:
    p = ROOT / rel
    try:
        return p.stat().st_mtime
    except OSError:
        return 0.0

def version_hint(rel: str) -> str:
    m = re.search(r"(Paper[_ ]?[IVXLC0-9]+|ArXiv_?Submission_?\d+|ArXiv_Submission_\d+|LatestUpdateV\d+|Attempt\d+|v\d+\.\d+|_v\d+|vunkownv\d+)", rel)
    return m.group(1) if m else ""

ordered = sorted(manifest, key=lambda r: (mtime(r), r))
lines = ["# LINEAGE_ORDER — 2,993 unique files, earliest signal first (file 1 = the seed)",
         "# Read in this order to follow the lineage forward from the origin.", ""]
for i, rel in enumerate(ordered, 1):
    h = version_hint(rel)
    lines.append(f"{i}\t{rel}" + (f"\t[{h}]" if h else ""))
(ROOT / "distilled" / "LINEAGE_ORDER.txt").write_text("\n".join(lines), encoding="utf-8")
print(f"LINEAGE_ORDER.txt written: {len(ordered)} files")
print("First 5 (the seed / earliest):")
for rel in ordered[:5]:
    print("  ", rel)
print("Last 3 (most recent):")
for rel in ordered[-3:]:
    print("  ", rel)
