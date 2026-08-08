#!/usr/bin/env python3
"""Regenerate COVERAGE.md at 100% from EXTRACTION_LOG.json + the deep-read set."""
import json
from pathlib import Path
from datetime import datetime, timezone

DIST = Path("/home/kmon/AA-Erebo/Genesis-Seeds/distilled")
log = json.loads((DIST / "EXTRACTION_LOG.json").read_text())

# Files genuinely deep-read (human-grade synthesis) so far.
DEEP_READ = {
    "ConsiderableStartingpoint/the_witnessing_system.md",
    "ConsiderableStartingpoint/omega_axioms.md",
    "ConsiderableStartingpoint/Multi-Scale Impact Measurement System (MSIMS).md",
    "ConsiderableStartingpoint/peig_as_lens.md",
    "ConsiderableStartingpoint/MyWork.md",
    "MyWork.md", "DISTILLATION_PLAN.md",
    "docs/PEIG_Mathematical_Spec_v1.md",
    "docs/Mathematical Formulation.md",
    "docs/QUANTUM_CONSCIOUSNESS_FINAL_REPORT.md",
    "quantum-ai-observer-main/BRIDGE_ARCHITECTURE_DESIGN.md",
    "quantum-ai-observer-main/LAB_WEEK1_FOUNDATION.py",
    "quantum-ai-observer-main/quantum_observer_v2.ipynb",
    "quantum-ai-observer-main/quantum_observer_v1.ipynb",
    "PEIG-Brotherhood-main/ArXivSubmission2/PEIG_Brotherhood_v2LatestV4.ipynb",
    "IndependantQuantumResearchUpdate-main/REPOSITORY_STATUS_REPORT.md",
    "IndependantQuantumResearchUpdate-main/IndependentResearch/MONETTE_RESEARCH_REPOSITORY_v1.0/REPO/03_PEIG_FRAMEWORK/cognitive/peig_cognitive_specification.md",
    "IndependantQuantumResearchUpdate-main/IndependentResearch/MONETTE_RESEARCH_REPOSITORY_v1.0/REPO/01_PHYSICS_CORE/B_CONSTRAINT_MANIFOLDS/constraint_manifold_paper.md",
    "IndependantQuantumResearchUpdate-main/IndependentResearch/MONETTE_RESEARCH_REPOSITORY_v1.0/REPO/01_PHYSICS_CORE/C_LANDAUER_ETI/landauer_eti_complete.md",
    "IndependantQuantumResearchUpdate-main/ArXiv_Submission_2_Ready/consciousness_functional.tex",
    "UIC-Quantum-Coherence-Experiments-main/README.md",
    "EmergentConciousness/quantum_observer_vunkownv5.ipynb",
    # canonical AA-Aria + origin lineage (this session)
    "AA-Aria/Attempt2/ARIA_GLOBE_v1.py",
    "AA-Aria/archive/Aria/ARIA_PEIG_CORE.py",
    "AA-Aria/archive/Aria/ARIA_NERVOUS_SYSTEM_v3.py",
    "AA-Aria/archive/Aria/ARIA_BRAIN_NERVOUS_SYSTEM_upgraded.py",
    "AA-Aria/Nova_Engine/Docs/Godotinfo2.md",
    "PEIG-Brotherhood-main/ArXivSubmission11/PEIG_Paper11_NestedSystem.py",
    "PEIG-Brotherhood-main/README.md",
    "PEIG-Brotherhood-main/ArXivSubmission14/Fix/PEIG_XV_core.py",
    "PEIG-Brotherhood-main/ArXivSubmission17InternalVoiceLayer/PEIG_XVII_node_consultation.py",
    "PEIG-Brotherhood-main/ArXivSubmission20MostImportant/AllPythonFilesPaper20/PEIG_XVIII_full_globe_experiment.py",
    "PEIG-Brotherhood-main/ArXivSubmission7/negentropic_magnification.py",
    "PEIG-Brotherhood-main/ArXivSubmission20MostImportant/AllPythonFilesPaper20/PEIG_task_voice_system.py",
    "PEIG-Brotherhood-main/ArXivSubmission20MostImportant/LearningTask1/PEIG_LT1_learning_task1.py",
    "PEIG-Brotherhood-main/ArXivSubmission17InternalVoiceLayer/PEIG_XVII_internal_voice.py",
    "PEIG-Brotherhood-main/ArXivSubmissionpaper16PreRegister/PEIG_XVI_simulations.py",
    "ConsiderableStartingpoint/canon-seed.md",
    "ConsiderableStartingpoint/witnessing_diagnostic_lenses.md",
    "ConsiderableStartingpoint/witnessing_application_notes.md",
    'ConsiderableStartingpoint/witnessing_spec_skeleton.md',
    'ConsiderableStartingpoint/Finishing and Operationalizing “The Witnessing System”.md',
    'ConsiderableStartingpoint/omega_explorations_personal.md',
    'entropy-gravity-coupling-main/README.md',
    'entropy-gravity-coupling-main/Derivatives.pdf',
    'Quantum-Consciousness-main/docs2/peig-analogues-modern-systems.md',
    'Quantum-Consciousness-main/README.md',
}

total = len(log)
deep = sum(1 for r in log if r["path"] in DEEP_READ)
mech = total - deep

# group by area
by_area = {}
for r in log:
    by_area.setdefault(r["area"], []).append(r)

lines = [
    "# Genesis-Seeds Distillation Coverage Tracker — 100% COVERAGE",
    f"# Generated {datetime.now(timezone.utc).isoformat()} by Claude (Opus 4.8)",
    "# [x] = deep-read (human-grade synthesis)   [m] = mechanically extracted (text+formulas captured)",
    f"# EVERY unique file is processed. {total} files: {deep} deep-read [x], {mech} mechanical [m].",
    "# Mechanical extracts: distilled/extracts/<area>.md · formulas: distilled/MASTER_FORMULA_INDEX.md",
    "",
    f"## TOTAL: {total}/{total} files covered (100%)  —  {deep} [x] · {mech} [m]",
    "",
]
for area in sorted(by_area):
    rows = by_area[area]
    d = sum(1 for r in rows if r["path"] in DEEP_READ)
    lines.append(f"\n## {area}  ({len(rows)} files · {d} deep-read)")
    for r in sorted(rows, key=lambda x: x["path"]):
        mark = "x" if r["path"] in DEEP_READ else "m"
        hint = (r.get("hint") or "")[:70]
        lines.append(f"- [{mark}] `{r['path']}`  — {hint}")

(DIST / "COVERAGE.md").write_text("\n".join(lines), encoding="utf-8")
print(f"COVERAGE.md regenerated: {total}/{total} (100%) — {deep} deep-read, {mech} mechanical")
