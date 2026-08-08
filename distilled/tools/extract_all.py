#!/usr/bin/env python3
"""extract_all.py — Mechanical full-corpus extraction for Genesis-Seeds distillation.

Processes every unique file in distilled/UNIQUE_MANIFEST.txt:
  - extracts text by type (direct / pdftotext / pandoc / ipynb-json)
  - captures a purpose hint
  - extracts all formulas (LaTeX envs, $$...$$, \\[...\\], display math)
  - classifies into an area bucket
Outputs:
  - distilled/EXTRACTION_LOG.json     (path -> area, bytes, hint, n_formulas, status)
  - distilled/MASTER_FORMULA_INDEX.md (all formulas, grouped by area)
  - distilled/extracts/<area>.md      (per-area: hint + text-head + formulas per file)

Robust: per-file errors are recorded, never crash the run. Uses only stdlib + CLI tools
(pdftotext, pandoc) which are confirmed available.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path("/home/kmon/AA-Erebo/Genesis-Seeds")
DIST = ROOT / "distilled"
MANIFEST = DIST / "UNIQUE_MANIFEST.txt"
EXTRACTS = DIST / "extracts"
EXTRACTS.mkdir(exist_ok=True)

TEXT_EXTS = {".md", ".txt", ".py", ".tex", ".json", ".csv", ".yaml", ".yml", ".gd", ".cff"}
HEAD_CHARS = 1500          # text-head stored per file in the area extract
MAX_FORMULA = 600          # cap a single formula's length

# ── Area classification by path ───────────────────────────────────────────────

def classify(rel: str) -> str:
    p = rel.lower()
    if "considerablestartingpoint" in p or "witnessing" in p or "omega_axiom" in p or "msims" in p:
        return "doctrine"
    if "quantum-ai-observer" in p or "quantum_observer" in p:
        return "observer_notebooks"
    if "peig-brotherhood" in p or "brotherhood" in p:
        return "peig_brotherhood"
    if "uic-quantum-coherence" in p or "experiment" in p and "uic" in p:
        return "hardware_experiments"
    if "entropy-gravity" in p:
        return "entropy_gravity"
    if "independantquantumresearch" in p or "arxiv" in p or "monette_research" in p:
        return "real_quantum_papers"
    if "quantum-consciousness" in p:
        return "quantum_consciousness"
    if "aa-aria" in p:
        return "aa_aria_archive"
    if "/docs/" in p or p.startswith("docs/"):
        return "mos_omega_canon"
    if "firstphase" in p or "sovereign-agent" in p:
        return "sovereign_overlay"
    return "misc"


# ── Formula extraction ────────────────────────────────────────────────────────

_LATEX_ENVS = re.compile(
    r"\\begin\{(equation|align|gather|multline|eqnarray|alignat)\*?\}(.*?)\\end\{\1\*?\}",
    re.DOTALL,
)
_DISPLAY_DD = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_DISPLAY_BR = re.compile(r"\\\[(.+?)\\\]", re.DOTALL)

def extract_formulas(text: str) -> list[str]:
    out: list[str] = []
    for m in _LATEX_ENVS.finditer(text):
        out.append(m.group(0).strip()[:MAX_FORMULA])
    for rx in (_DISPLAY_DD, _DISPLAY_BR):
        for m in rx.finditer(text):
            f = m.group(1).strip()
            if len(f) > 3:
                out.append(f[:MAX_FORMULA])
    # dedupe, keep order
    seen, uniq = set(), []
    for f in out:
        k = f[:120]
        if k not in seen:
            seen.add(k); uniq.append(f)
    return uniq[:60]   # cap per file


# ── Text extraction by type ───────────────────────────────────────────────────

def read_text_file(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def read_pdf(p: Path) -> str:
    r = subprocess.run(["pdftotext", "-layout", str(p), "-"],
                       capture_output=True, text=True, timeout=120)
    return r.stdout if r.returncode == 0 else ""

def read_docx(p: Path) -> str:
    r = subprocess.run(["pandoc", "-t", "plain", str(p)],
                       capture_output=True, text=True, timeout=120)
    return r.stdout if r.returncode == 0 else ""

def read_ipynb(p: Path) -> str:
    nb = json.loads(p.read_text(encoding="utf-8", errors="ignore"))
    parts = []
    for c in nb.get("cells", []):
        src = c.get("source", [])
        parts.append("".join(src) if isinstance(src, list) else str(src))
    return "\n\n".join(parts)

def extract(p: Path) -> tuple[str, str]:
    """Return (text, status)."""
    ext = p.suffix.lower()
    try:
        if ext in TEXT_EXTS:
            return read_text_file(p), "text"
        if ext == ".pdf":
            return read_pdf(p), "pdf"
        if ext == ".docx":
            return read_docx(p), "docx"
        if ext == ".ipynb":
            return read_ipynb(p), "ipynb"
    except Exception as exc:  # noqa: BLE001
        return "", f"error:{type(exc).__name__}"
    return "", "skipped"


def purpose_hint(text: str) -> str:
    for line in text.splitlines():
        s = line.strip().lstrip("#%/*-\"' \t").strip()
        if len(s) > 14 and not s.startswith(("import ", "from ", "{", "}", "[")):
            return s[:140]
    return ""


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    files = [l.strip() for l in MANIFEST.read_text().splitlines() if l.strip()]
    log: list[dict] = []
    by_area: dict[str, list[str]] = {}
    formulas_by_area: dict[str, list[tuple[str, list[str]]]] = {}

    for i, rel in enumerate(files):
        p = ROOT / rel
        area = classify(rel)
        if not p.exists():
            log.append({"path": rel, "area": area, "status": "missing", "bytes": 0,
                        "hint": "", "n_formulas": 0})
            continue
        text, status = extract(p)
        formulas = extract_formulas(text) if text else []
        hint = purpose_hint(text) if text else ""
        log.append({"path": rel, "area": area, "status": status,
                    "bytes": len(text), "hint": hint, "n_formulas": len(formulas)})

        # per-area extract entry
        by_area.setdefault(area, [])
        entry = [f"### `{rel}`",
                 f"- status: {status} · {len(text)} chars · {len(formulas)} formulas",
                 f"- hint: {hint}" if hint else "- hint: (none)"]
        if text:
            head = text[:HEAD_CHARS].replace("```", "ʼʼʼ")
            entry.append(f"```\n{head}\n```")
        by_area[area].append("\n".join(entry))

        if formulas:
            formulas_by_area.setdefault(area, []).append((rel, formulas))

        if i % 250 == 0:
            print(f"  ...{i}/{len(files)} processed", flush=True)

    # Write EXTRACTION_LOG.json
    (DIST / "EXTRACTION_LOG.json").write_text(json.dumps(log, indent=1), encoding="utf-8")

    # Write per-area extracts
    for area, entries in sorted(by_area.items()):
        out = EXTRACTS / f"{area}.md"
        header = (f"# Mechanical extract — area: {area}\n"
                  f"# {len(entries)} files. Text-head + formulas per file. "
                  f"Full formulas in MASTER_FORMULA_INDEX.md.\n\n")
        out.write_text(header + "\n\n".join(entries), encoding="utf-8")

    # Write MASTER_FORMULA_INDEX.md
    total_formulas = sum(len(fs) for area in formulas_by_area.values() for _, fs in area)
    lines = ["# 📐 MASTER FORMULA INDEX — every formula in Genesis-Seeds",
             "",
             f"Mechanically extracted from {len(files)} unique files. "
             f"{total_formulas} formulas across {len(formulas_by_area)} areas.",
             "Per Kevin: store ALL formulas, even ones unrelated to the build.",
             ""]
    for area in sorted(formulas_by_area):
        lines.append(f"\n## Area: {area}\n")
        for rel, fs in formulas_by_area[area]:
            lines.append(f"### `{rel}`  ({len(fs)} formulas)")
            for f in fs:
                f1 = f.replace("\n", " ").strip()
                lines.append(f"- `{f1}`")
            lines.append("")
    (DIST / "MASTER_FORMULA_INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    # Summary
    status_counts: dict[str, int] = {}
    area_counts: dict[str, int] = {}
    for r in log:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
        area_counts[r["area"]] = area_counts.get(r["area"], 0) + 1
    print(f"\nDONE. {len(log)} files processed.")
    print("By status:", dict(sorted(status_counts.items(), key=lambda x: -x[1])))
    print("By area:", dict(sorted(area_counts.items(), key=lambda x: -x[1])))
    print(f"Total formulas extracted: {total_formulas}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
