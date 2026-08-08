# Mechanical extract — area: sovereign_overlay
# 4 files. Text-head + formulas per file. Full formulas in MASTER_FORMULA_INDEX.md.

### `FirstPhase/CHANGELOG-v0.2.4.md`
- status: text · 4560 chars · 0 formulas
- hint: v0.2.4 — 2026-04-29
```
# Changelog

## v0.2.4 — 2026-04-29

**Type:** Documentation and doctrine release. No code changes.

### Added

- `COMMANDS.md` — comprehensive command reference covering every CLI command, every flag, with examples and failure-mode guidance. Addresses the documentation gap that caused users to ask the agent for its own command list.
- `RUNBOOK.md` — operations guide covering daily startup, goal-writing patterns that work vs. fail, three usage patterns (oneshot/timed/live), monitoring during sessions, troubleshooting common issues.
- `DISTILLATION_PLAN.md` — six-phase staged plan for distilling the Genesis-Seeds corpus. Honest about which phases v0.2.4 can execute (1, 2, 4, 5) and which require v0.3 tools (3, 6).
- `docs/doctrine/` — seven doctrine documents:
  - `the_witnessing_system.md` — soul document
  - `witnessing_application_notes.md` — practice notes
  - `witnessing_diagnostic_lenses.md` — seven diagnostic lenses
  - `witnessing_spec_skeleton.md` — spec outline with deferred-work appendix
  - `peig_as_lens.md` — PEIG as computational design language
  - `omega_axioms.md` — alignment essay
  - `omega_explorations_personal.md` — personal vision

### Unchanged

- All Python source files — identical to v0.2.3
- All tests — 88 passing
- Database schema — identical
- Configuration format — identical
- Capability detection (the v0.2.3 fix) — unchanged
- SQLite threading fix (v0.2.2) — unchanged
- Conftest pure pattern (v0.2.1) — unchanged

### Migration from v0.2.3

Purely 
```

### `FirstPhase/COMMANDS.md`
- status: text · 11652 chars · 0 formulas
- hint: Sovereign Agent — Command Reference
```
# Sovereign Agent — Command Reference

**Version:** v0.2.4
**Status:** Comprehensive command reference. Print this. Keep it visible.

---

## Quick orientation

The `sovereign` CLI controls the entire agent. Everything you do with the agent goes through one of the commands below. There is no other way to drive it. The agent does NOT have a "show me my commands" capability built into the model — when you ask the model that question, it doesn't know, because the commands are part of the CLI wrapper, not the model. **This document is the answer to "what can I run."**

All commands have `--help` available. When in doubt: `sovereign <command> --help`.

---

## Setup commands

### `sovereign init`

**Purpose:** First-time setup. Creates config dir, data dir, sandbox, secret.key, atoms.db.

**Run when:**
- First install
- After a clean wipe
- If `sovereign doctor` shows missing infrastructure

**Example:**
ʼʼʼbash
sovereign init
ʼʼʼ

**Idempotent:** Yes. Safe to run multiple times. Will not overwrite an existing `secret.key`.

---

### `sovereign doctor`

**Purpose:** Diagnostic check. Verifies all directories, models, ollama connectivity, bubblewrap availability, VRAM headroom.

**Run when:**
- Anytime something feels off
- Before kicking off long agent sessions
- After upgrading the agent or changing config

**Example:**
ʼʼʼbash
sovereign doctor
ʼʼʼ

**Output:** A table with PASS/WARN/FAIL for each check. Read it. WARNs are usually fine; FAILs need fixing before proceeding.

---


```

### `FirstPhase/RUNBOOK.md`
- status: text · 9155 chars · 0 formulas
- hint: Sovereign Agent — Runbook
```
# Sovereign Agent — Runbook

**Version:** v0.2.4
**Status:** Operations guide. Read once. Reference often.

---

## What this document is

`COMMANDS.md` tells you *what commands exist*. This document tells you *how to actually run the agent for real work*. It's the difference between a man page and an operator's manual.

---

## First-time setup (do this once)

ʼʼʼbash
# 1. Verify infrastructure
sovereign doctor

# 2. If anything fails, run init
sovereign init

# 3. Verify again
sovereign doctor
ʼʼʼ

You want all PASS or PASS/WARN. The `orch thinking` WARN is normal — it means llama3-groq doesn't support thinking, which is fine because the agent auto-disables it.

If `secret.key` is missing or `atoms.db` is missing, `sovereign init` will create them. If models are missing, you need to `ollama pull` them — the doctor output will tell you which.

---

## Daily startup

If you run the agent regularly, do this each morning:

ʼʼʼbash
sovereign doctor                 # quick health check
sovereign events -n 5            # see what happened last
sovereign lessons -n 3           # see what was learned
ʼʼʼ

Three commands. Tells you everything you need to know to start the day.

---

## How to write goals the agent can actually execute

The agent's biggest failure mode is loop-bouncing on vague goals. Here are the patterns that work and the patterns that don't.

### Patterns that work

**Direct tool invocations:**
> "Use list_dir on ~/AA-Erebo/Genesis-Seeds/Genesis-Seed/. For each fil
```

### `FirstPhase/sovereign-agent-v0.2.4-DOCS-OVERLAY/README.md`
- status: text · 5622 chars · 0 formulas
- hint: Sovereign Agent v0.2.4
```
# Sovereign Agent v0.2.4

**A local, authority-tiered, audited, recoverable autonomous agent — yours.**

---

## What's new in v0.2.4

This version doesn't change agent code. It adds the operational and doctrinal scaffolding the agent needs to be actually usable for the Genesis-Seeds work:

- **`COMMANDS.md`** — comprehensive command reference (the missing manual)
- **`RUNBOOK.md`** — practical operations guide
- **`DISTILLATION_PLAN.md`** — staged plan for Genesis-Seeds distillation work
- **`docs/doctrine/`** — the witnessing-system doctrine the agent operates under
- **`CHANGELOG.md`** — version history through v0.2.4

The agent itself is unchanged from v0.2.3 (88 tests passing, capability-detected thinking, SQLite threading fixed, conftest pure). v0.2.4 is documentation + doctrine.

---

## Why no new features

Be honest about it: at v0.2.3 the agent has 88 passing tests but only Tier 0/1 tools and is loop-prone on multi-step planning. Adding new tools (PDF reader, document distiller) without first making the existing agent **drivable** would just add complexity to something that's hard to use.

v0.2.4 makes the existing agent drivable. v0.3 adds the new tools.

---

## Quick start

ʼʼʼbash
# 1. Extract
tar -xzf sovereign-agent-v0.2.4.tar.gz
cd sovereign-agent-v0.2.4

# 2. Install (if not already done)
pip install -e .

# 3. First-time setup
sovereign init
sovereign doctor

# 4. Read the manual
cat COMMANDS.md       # what commands exist
cat RUNBOOK.md         # how to us
```