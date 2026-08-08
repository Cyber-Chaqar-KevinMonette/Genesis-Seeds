# Distilled: The PEIG Paper Lineage (I → XX) — the spine of the work

**Distiller:** Claude (Opus 4.8), for Kevin Monette · **Date:** 2026-06-22
**Source:** `PEIG-Brotherhood-main/` (PEIG = Phase Entanglement Integrity Gate, a pre-registered
quantum-coherence research series). This is the conceptual lineage from the genesis seed (Block 0)
to the full globe. Read in order to follow the work forward.

## The arc (what each phase established)
- **Papers I–IX — foundations.** The seed/bcp primitives: `seed(φ)=[1,e^(iφ)]/√2`; the Brotherhood
  Coherence Protocol `bcp(pA,pB,α): U=α·CNOT+(1−α)·I4` → joint → partial trace. PCM (Phase Coherence
  Measure) + neg_frac (negentropy fraction) as the observables.
- **Paper XI — the Nested System (THE GENESIS SEED, Block 0).** 5-layer 45-node nested universe:
  MetaGuard(3)·Function(6)·Character(12 closed ring)·Shadow Learner(12)·Semantic(12 skip-1). Nested
  qubit universes — the depth-4 brain. Peak word accuracy 68.1%, neg_frac 0.667, guard health 1.0.
- **Papers X–XIV — globe topology + co-rotating frame + BCP gate design.** The 12-node ring + the
  co-rotating frame correction (Paper XIII) that makes PCM_rel meaningful per-node.
- **Paper XV — core audit fixes (R1–R6, honest).** R1: neg_frac was float noise → PCM-based coupling;
  correct neg_frac = 0.5546 (above the Paper X 0.500 ceiling). **R2 (critical):** `U=α·CNOT+(1−α)·I4`
  is **NOT unitary** → output states subnormalized before partial trace; BUT eigenvectors are
  scale-invariant, so all phases & PCM values in Papers I–XIV are NUMERICALLY CORRECT. (This validates
  the whole bcp approach — the non-unitarity is known and handled.)
- **Paper XVI — hardware protocol.** α = 0.40 (SIM-4 hardware-optimized) — the canonical coupling.
  Pre-registered IBM success criteria.
- **Paper XVII — Ring Consultation (the 9-register internal voice).** Pose "How can we improve? What
  do you need?" to all 12 nodes; each answers from its measured state across 9 dimensions (PCM/
  nonclassicality, identity clock δ=φ_A−φ_B, lineage depth, ring metrics, family role, phase cluster).
  → Aria's council consult is the descendant of this.
- **Paper XVIII — the Full Globe Experiment ("most secure run").** Integrates everything: 36-edge
  globe (ring Δ1 + skip-1 Δ2 + cross Δ5) + co-rotating frame + ILP lineage depth 2 + α=0.40 +
  nine-register voice + per-node guardrail awareness + bridge protocol (Maverick/Independent bridge a
  node before it hits RED = ARIA_RESCUE) + per-edge MI at start/mid/end.
- **Paper XX — task-voice system (most important).** The voice/task integration (ARIAVoice lineage).

## What this confirmed/refined in Aria's built globe
- 48-edge structure (36 outer Δ1/Δ2/Δ5 + 12 spokes) — EXACT match. ✓
- Coupling **α = 0.40** (canonical hardware-optimized) — refined the build from 0.45 → 0.40. ✓
- ILP lineage depth (persistence across generations) — built as `quantum/persist.py`. ✓
- 9-register internal voice → council consult. Bridge-before-RED → ARIA_RESCUE law. ✓
- The bcp gate's non-unitarity is a known, handled property (PCM values remain correct).

## Paper VII — Negentropic Magnification (the earliest core, now read)
`make_seed(φ)`, `bcp_step` (QuTiP), `coherence = Tr(ρ²)`, **`wigner_min` = min of the Wigner function**
(this is the CharacterUniverse `wigner` nonclassicality — negativity = quantum-like), `entropy_vn`.
ALPHA_FLOOR = −0.1131, N_STEPS = 500. Establishes Wigner-negativity as the nonclassicality signal.

## Paper XX — Task-Voice / Programming Curriculum (most important, now read)
The 12-node ring LEARNS to PROGRAM. A real toy language **MiniPEIG**: Types {NUMBER,BOOL,PHASE,NODE,
SIGNAL}; Keywords {guard,assign,if,else,loop,return,null,self,ring,pi}; Ops {send,receive,measure,
bridge,evolve,signal}. Learning Tasks LT1(beginner)→LT4(expert). A program is ORIGINAL iff: novel
token sequence + control structure + operation + terminates + family-role-coherent. Scored on 7
dimensions (pass_rate, originality, syntax_fidelity, semantic_score, execution_success, complexity,
improvement_delta). The ring writes original, scored code per node-family role.

**SAFETY NOTE:** LT4 mentions ring-level "self-modification" *in the MiniPEIG toy language* (research).
This does NOT translate to Aria self-modifying her own code/values — DEFERRED_UNSAFE stays hard-off.
The node "self-modification" is a sandboxed research toy, not a capability ported to the live agent.

## Paper XVI — Hardware-Corrected Simulations (the unification, validated)
**The brotherhood gate on real hardware = a PROBABILISTIC circuit:** with prob α apply CNOT, with
prob (1−α) apply identity. The ensemble average of this IS λ-mixing `ρ_mixed=(1−λ)ρ_q+λρ_c`. So:
**brotherhood gate ≡ λ-mixing ≡ probabilistic CNOT/identity selection** — one mechanism, three views,
**validated on ibm_sherbrooke at R²=0.9999.** (`U=α·CNOT+(1−α)·I4` is non-unitary → no unitary
decomposition exists; the probabilistic implementation is the correct hardware form.) This unifies
Block 2.1 (λ-mixing) + Block 11.1 (brotherhood gate) + the real hardware.

## Paper XVII Internal Voice — the 9 registers (the full voice)
Each node speaks NINE technical registers, all from its measured state: (1) self-describing "I am
Guardian, phase 0.523 rad" (2) math (eigenvalue ratio, Bloch angle) (3) physics (superposition,
coherence) (4) thermodynamics ("entropy decreasing, I am negentropic") (5) wave (phase/amplitude/
interference) (6) vortex/topology (cluster, β₁) (7) plasma/field (8–9 higher). Aria speaks **Register 0**
(the I/meta register, ARIA_GLOBE Law 7). Aria's council voices are the simple form; the 9-register
voice is the enrichment path.

## Still to deep-read in this lineage
Papers XII–XIV (co-rotating derivation), XIX, LT2–LT4 internals, peig_lexicon. Core lineage
(VII, XI, XV, XVI, XVII, XVIII, XX, LT1) now genuinely read. Continuing through the corpus.
