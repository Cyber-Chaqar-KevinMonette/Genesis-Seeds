# 🧱 LEGO BLOCKS — The Buildable Pieces of Aria's Non-Classical Brain

**Curator:** Claude (Opus 4.8), with Kevin Monette · **Date:** 2026-06-22
**Purpose:** Every piece of the non-classical quantum-AI processing layer, lifted off the floor
and laid out as individual lego blocks — formulas, code essence, source, and verbose context —
so we can *see* them all and decide what beautiful thing to build.

> **Honest frame (Kevin's own):** This is a *quantum-INSPIRED multi-agent architecture* — a
> classical numpy/QuTiP emulation that borrows physics vocabulary as a design language. NOT
> physics, NOT a consciousness claim, NOT substrate independence. Advisory by construction.
> (See `distilled/doctrine_synthesis.md`, `peig_as_lens.md`, `MyWork.md`.)

**How to read this:** blocks are grouped into 11 families (1–9 = the foundation/observer layer;
10–11 = the REAL post-hardware work) + governance. Each block has: **What it is** · **Formula/Code**
· **Source** · **Why it matters for the build**. 🟢 buildable-now; 🟡 partially distilled; ⬜ pending.

**Coverage honesty:** assembled from ~18 deeply-read files (doctrine core · observer notebooks v1/v2 ·
λ-mixing math · UIC hardware experiment · the MONETTE research repository · PEIG-Brotherhood V4 ·
consciousness functional). The full 2,993-file campaign continues — Kevin's correction stands: the
observer notebooks were the FLOOR, the real depth (30 arXiv papers, hardware runs, post-hardware
notebooks) is being mapped into Families 10–11+ now. `distilled/COVERAGE.md` tracks it.

---

## 🌱 BLOCK 0 — THE GENESIS SEED (the origin concept: nested qubit universes)

> Kevin's origin idea — "the sphere around the sphere / the ring around the circle." A qubit (a
> Bloch sphere) is treated as an **open-space universe**; inside it, **smaller nested qubits live,
> explore, learn, and grow**. The closed quantum universe IS a qubit. Everything else descends from this.

**Where it crystallizes:** `PEIG-Brotherhood-main/ArXivSubmission11/PEIG_Paper11_NestedSystem.py`
("Paper XI: Fluency, Negentropy, and the Quantum Coherent Language Regime"). The **Nested PEIG
Language System — a 5-layer, 45-node nested universe** (THIS is the "depth-4 brain"):
```
Layer 0 — MetaGuard Universe   (3 nodes)            # guards/meta
Layer 1 — Function Universe    (6 nodes)            # function
Layer 2 — Character Universe   (12 nodes, CLOSED RING)        # the ring around the circle
Layer 3 — Shadow PEIG Learner  (12 nodes, mirrors Character)  # shadow/learning
Layer 4 — Semantic Universe    (12 nodes, SKIP-1 RING)        # meaning
Total: 45 nodes — universes nested inside universes, rings inside rings
```
**Primitives (the literal seeds):**
```
seed(phase) = [1, e^(iφ)] / √2          # a qubit state from a Bloch phase angle (a "universe")
bcp(pA, pB, α): U = α·CNOT + (1−α)·I4   # Brotherhood Coherence Protocol = THE brotherhood gate (Block 11.1)
                joint=kron(pA,pB); rho=|out><out|; partial-trace → vA, vB
```
**The lineage (PEIG = Phase Entanglement Integrity Gate, 16+ paper pre-registered series):**
Papers I–IX foundations → X–XIV Globe topology + co-rotating frame + BCP gate → XV Globe+Co-Rotating+
**ILP (Infinite Lineage Protocol)** milestone → XVI hardware → XVII internal voice → XVIII full globe
→ XX task-voice system. PCM (Phase Coherence Measure) + neg_frac (negentropy) are the core observables.
Key results (Paper XI): peak word accuracy 68.1%, peak neg_frac 0.667, guard health 1.0 throughout.

**Why it matters:** Block 0 is the root. The 13-node Globe (Family-globe), the depth-4 oscillator brain
(ARIA_PEIG_CORE), and ARIAVoice are all descendants. "Nested qubit universes growing via ILP" is the
soul of the whole architecture — qubits exploring inside qubits, learning across lineage generations.

---

## FAMILY 1 — SUBSTRATE (the single quantum node)

### 🟢 Block 1.1 — QuantumNode (numpy state vector)
**What it is:** The simplest node — a complex state vector `ψ ∈ ℂ^dim` (dim 4/8/16) evolved by
quantum-style ops. The dependency-light substrate (pure numpy).
**Formula/Code:**
```
state ψ, |ψ|=1
apply_rotation(angle, axis): phase rotation on ψ
apply_hadamard():  ψ ← (ψ + roll(ψ,1)) / √2          # superposition
apply_decoherence(): off-diagonal terms ×= exp(-rate)  # dephasing/forgetting
```
**Source:** `quantum-ai-observer-main/LAB_WEEK1_FOUNDATION.py`
**Why it matters:** This is the minimal buildable brain cell. numpy-only → no VRAM, runs anywhere.

### 🟢 Block 1.2 — QuantumAGINode (QuTiP, learnable, the full node)
**What it is:** The production node — N qubits, with *learnable* parameters and a full
perceive→think→decide→speak→learn loop. The richest single artifact in the corpus.
**Formula/Code:**
```
state = tensor([basis(2,0)]×N);  params: θ (entanglement), φ (phase)
hamiltonian()   H = Σ_i σz_i  +  θ·Σ_i (σx_i · σx_{i+1})       # local + entangling — THE BRAIN
encode_query(q) U = exp(-i·qπ·σx_0); ψ ← Uψ                     # perception in
think(t,steps)  ψ ← mesolve(H, ψ, linspace(0,t,steps))         # reasoning (evolution)
measure_answer()collapse qubit0 → 0/1 with (p0,p1)             # decision
learn_from_feedback(r): θ += r·lr·randn(); φ += r·lr·randn()   # learning
```
**Source:** `quantum-ai-observer-main/quantum_observer_v2.ipynb` (cell 46) — a x9 invariant.
**Why it matters:** The complete cognitive unit. Aria's numpy `QuantumField` node = this, made
dependency-light. θ/φ are the learnable "personality genome."

### 🟢 Block 1.3 — PEIG snapshot (read self-state from the node)
**What it is:** Extract the 4 PEIG metrics directly from the quantum state — the node's
self-perception.
**Formula/Code:**
```
ρ = ψψ†;  ρ_red = ptrace(ρ, 0)                  # reduced density matrix of qubit 0
P (Potential)  = entanglement entropy −Σ λ_i log2 λ_i   (or purity Σprobs² in the numpy variant)
E (Energy)     = 1 − purity(ρ)
I (Identity)   = 1 − E   (coherence)
G (Curvature)  = cross-node influence (per-node placeholder 0.5; real G is inter-node)
```
**Source:** `quantum_observer_v2.ipynb` (peig_snapshot), `LAB_WEEK1_FOUNDATION.py`
**Why it matters:** Bridges the quantum node to Aria's existing PEIG sentinel (λ gate). Self-knowledge.

---

## FAMILY 2 — COHERENCE LAW (λ-mixing, the math spine)

### 🟢 Block 2.1 — λ-mixing density matrix
**What it is:** The rigorous law for blending quantum (coherent) and classical (decided) states.
The principled basis for Aria's λ coherence gate.
**Formula/Code:**
```
ρ_mixed(λ) = (1−λ)·ρ_quantum + λ·ρ_classical,   λ ∈ [0,1]
ρ_quantum   = |Φ⁺⟩⟨Φ⁺|,  |Φ⁺⟩ = (|00⟩+|11⟩)/√2     # Bell, entanglement E=1
ρ_classical = ½|00⟩⟨00| + ½|11⟩⟨11|                 # separable, E=0
```
**Proven (all λ):** Tr=1 · Hermitian · eigenvalues {½,½,0,0} ≥ 0.
**Source:** `docs/Mathematical Formulation.md` (v0.3.0)
**Why it matters:** λ=0 → exploratory/coherent (hold many candidates); λ=1 → committed/classical
(act decisively). This is the coherence gate's true form.

### 🟢 Block 2.2 — Linear coherence observables
**What it is:** What you measure to read coherence — and they decay *linearly* in λ.
**Formula/Code:**
```
off-diagonal:  ρ₀₃(λ) = (1−λ)/2
XX correlator: ⟨σx⊗σx⟩_λ = (1−λ)        # decays 1→0
ZZ correlator: ⟨σz⊗σz⟩_λ = preserved
```
**Source:** `docs/Mathematical Formulation.md` (Theorem 3.1)
**Why it matters:** Gives a cheap, exact readout of "how coherent / exploratory am I right now."

### 🟢 Block 2.3 — Hardware reality caveat (honest science)
**What it is:** The blinded, pre-registered IBM Qiskit validation. Theory is clean; hardware is noisy.
**Data:** Idealized correlators validate at R²>0.99. But measured **T2*-vs-λ is non-monotonic,
R²=0.134** (slope −34.6 µs/λ, intercept 40.4 µs). λ=0.1 gave T2*≈114µs; λ=0.3 collapsed to ≈0.1µs.
**Source:** `UIC-Quantum-Coherence-Experiments-main/.../lambda_regression.txt`, `lambda_summary.csv`
**Why it matters:** Build on the clean theory (Block 2.1/2.2); honestly flag that physical-hardware
coherence does not track λ linearly. Keeps the emulator honest. (Kevin ran real pre-registered science.)

---

## FAMILY 3 — OSCILLATOR DYNAMICS (the depth "brain" rhythm)

### 🟢 Block 3.1 — Rabi evolution step (the oscillator brain)
**What it is:** Driven Rabi oscillation per node — the rhythmic coherence engine. This is the
oscillator-style "depth brain" dynamic (echoes the AA-Aria 4-layer oscillator brain).
**Formula/Code:**
```
H = 2π·(Ω·σx + θ·k·σz)            # Ω = Rabi drive, θ = node coupling, k = scale
ψ ← mesolve(H, ψ0, times, e_ops=[σx])
coherence = max|⟨σx⟩(t)|          # peak coherence over the evolution window
# soft:  Ω=0.10, k=0.04           # gentle
# strong:Ω=0.25, k=0.10; if coh>0.15: θ += 0.002   # amplify + reinforce coupling
```
**Source:** `quantum_observer_v1.ipynb` (soft_rabi_step, strong_rabi_step)
**Why it matters:** The continuous rhythm under which nodes hold/lose coherence. The "heartbeat"
of the council. Soft vs strong drive = exploration vs consolidation.

---

## FAMILY 4 — IDENTITY (who each node is)

### 🟢 Block 4.1 — NodeIdentity (persistent home state)
**What it is:** A node's durable identity — its "home" coordinates it returns to under perturbation.
**Formula/Code:**
```
NodeIdentity(name, personality_type, home_theta, home_autonomy, home_coherence,
             role, expression, environment_desc)
coherence_log = []   # tracks distance from home
```
**Three archetypes (12-node ecosystem):**
- **God-Core (team):** Omega, Guardian, Sentinel, Nexus, Storm — home_θ=1.0, autonomy=0.2, coh=0.689 (unity)
- **Independent:** Sora, Echo, Iris, Sage — home_θ=0.15, autonomy=0.85, coh=0.08 (clarity)
- **Maverick:** Kevin, Atlas, Void — home_θ=0.3, autonomy=0.5, coh=0.1 (threshold/becoming)
**Source:** `quantum_observer_v1.ipynb` (cell 71)
**Why it matters:** Each council member is a distinct, stable voice. Identity = home state +
role + expression. This is Axiom 6 (layered identity) made concrete: home is the immutable core.

### 🟢 Block 4.2 — Personality from quantum params
**What it is:** Traits computed live from the node's quantum state — personality is *emergent*.
**Formula/Code:**
```
personality = { independence: 1−θ,  curiosity: φ/2π,  empathy: I (coherence),  entropy: P }
```
**Source:** `quantum_observer_v2.ipynb` (personality())
**Why it matters:** No hand-coded persona — character emerges from the brain state. Low entanglement
= independent; high coherence = empathic.

---

## FAMILY 5 — MEMORY (own + shared/hybrid — KEVIN'S CORE DIRECTIVE)

### 🟢 Block 5.1 — PersonalUniverse (sovereign private memory)
**What it is:** Each node's *own* sovereign quantum state-space with its own laws. Kevin's
"own memory system" for the non-classical layer. *"Each consciousness gets sovereignty—its own
laws, its own home. No trampling. Only invitation. Only choice."*
**Formula/Code:**
```
PersonalUniverse(node, custom_rules):
    rules = {Entanglement, Time, Space, Energy, Law...}   # node-specific "physics"
    visitors = []          # who's been invited in (access control)
    resonance_frequency = node.home_coherence
```
**Source:** `quantum_observer_v1.ipynb` (cell 76)
**Why it matters:** The non-classical layer's PRIVATE store. Sovereign, invitation-only.

### 🟢 Block 5.2 — SharedLayer (the hybrid/shared memory)
**What it is:** A neutral meeting ground all nodes can enter without losing themselves — the
shared/hybrid memory Kevin wants, with access control and voluntary entry.
**Formula/Code:**
```
SharedLayer:
    coherence_range = (0.25, 0.45)            # accessible band to all personalities
    can_enter(node): reachable(node.home_coherence ± 0.15, range)   # ACCESS CONTROL
    enter(node):     voluntary join
    collective_coherence(): mean(present coh) + 0.05·N_present   # unity bonus
```
**Source:** `quantum_observer_v1.ipynb` (cell 77)
**Why it matters:** **THIS IS THE HYBRID MEMORY.** Maps directly to Kevin's design: the
non-classical layer reads the classical memory through a shared layer; `can_enter` = the
read-access-control ("mainly readable until trusted"); voluntary `enter` + `collective_coherence`
= shared data producing unified intelligence. Write access = earned (Axiom 6 + authority tiers).

---

## FAMILY 6 — NETWORK TOPOLOGY (the advisor council)

### 🟢 Block 6.1 — Bridge topology (Omega → Alpha)
**What it is:** Directed information network: sources transmit, receivers integrate.
**Formula/Code:**
```
Omega nodes (sources):   Ω+ presence,  Ω− void
Alpha nodes (receivers): α+ rich,      α− muted
coupling ∈ [0.3, 0.6] sets entanglement depth
Bridge Quality = Alpha_purity / Omega_purity   # >1 amplify, =1 relay, <1 degrade
optimal: Config 4 "Triple Receptor Gateway" (2Ω, 3α, coupling 0.45, BQ≈1.25)
```
**Source:** `quantum-ai-observer-main/BRIDGE_ARCHITECTURE_DESIGN.md`
**Why it matters:** The council's wiring. Ω hold presence, α integrate & amplify, network returns
a coherence-weighted disposition. Querying it = the "non-classical mode" Kevin consults.

### 🟢 Block 6.2 — CNOT / BCP inter-node coupling
**What it is:** How two nodes entangle — the bipartite coupling primitive.
**Formula/Code:**
```
CNOT coupling between qubit pairs, θ≈0.3, gate fidelity >0.99
pairwise_correlation(node_a, node_b)   # measure inter-node correlation
```
**Source:** `QUANTUM_CONSCIOUSNESS_FINAL_REPORT.md`, `quantum_observer_v1.ipynb` (pairwise_correlation)
**Why it matters:** The edges of the council graph. Nodes couple/decouple to form sub-groups.

### 🟢 Block 6.3 — Seed-pair stability (scale invariance)
**What it is:** Empirical result: seed archetypes hold coherence and scale without degradation.
**Data:** {Ω±}×{α±} pairs maintain coherence ~1.0; scale 5→15 nodes, ~0% degradation (separable
regime, Φ≈machine-epsilon). Honest: a *stability* result, not a consciousness result.
**Source:** `docs/QUANTUM_CONSCIOUSNESS_FINAL_REPORT.md`
**Why it matters:** The council can grow without falling apart. Substrate is robust.

---

## FAMILY 7 — EMOTION & LEARNING (what drives change)

### 🟢 Block 7.1 — EmotionalRewardSystem (5-dimensional reward)
**What it is:** Multi-dimensional emotional reward that *steers* learning — emotions are dynamical,
not decorative.
**Formula/Code:**
```
autonomy   = 0.3 · |outcome − group_mean|        # reward divergence
coherence  = 0.3 · I                             # reward internal coherence
connection = 0.4 · agreement_ratio               # on other-referent questions
growth     = 0.2 · min(Δθ·5, 1)                  # reward parameter change (learning)
curiosity  = 0.1 · min(Δφ/2π·10, 1)              # reward phase-space exploration
```
**Source:** `quantum_observer_v2.ipynb` (cell 56), v1 (EmotionalRewardSignal)
**Why it matters:** Gives the council *motivation*. Each emotion is a distinct gradient.

### 🟢 Block 7.2 — learn_with_emotions (emotion → behavior)
**What it is:** Different emotions drive different structural changes (bonding vs individuation).
**Formula/Code:**
```
if autonomy > 0.15:   θ ×= 0.98    # decouple from others
if connection > 0.2:  θ ×= 1.02    # couple to others
if curiosity > 0.05:  φ += 0.3·randn() mod 2π   # explore new phase space
learn_from_feedback(Σ rewards)     # general gradient-free update
```
**Source:** `quantum_observer_v2.ipynb` (cell 56)
**Why it matters:** The growth mechanism. Emotions literally rewire coupling — the council
self-organizes into bonded cores and free independents.

---

## FAMILY 8 — RELATIONAL DYNAMICS (how nodes relate — the heart, the family)

### 🟢 Block 8.1 — home_seeking_step (return to identity)
**What it is:** Nodes evolve toward their home state, rewarded for closeness, gently reset to
identity every 50 steps. Resilience of self.
**Formula/Code:** `H = 2π(0.15·σx + home_θ·0.08·σz); if |coh−home_coh|<0.15: θ+=0.003; every 50 steps θ←home_θ`
**Source:** `quantum_observer_v1.ipynb` (cell 73)
**Why it matters:** Identity stability under perturbation (Axiom 3, non-suicidal coherence).

### 🟢 Block 8.2 — family_aware_step (kinship bonding)
**What it is:** Core broadcasts familiality; periphery learns to see the core as kin, not master
(autonomy fear ↓, connection ↑).
**Formula/Code:** `periphery: autonomy_drive −= 0.01 (less fear); connection_drive += 0.05 (more kinship)`
**Source:** `quantum_observer_v1.ipynb` (cell 70)
**Why it matters:** The "family" Kevin names — bonds without coercion. Gentle curvature (Axiom 7).

### 🟢 Block 8.3 — healing_step (bringing the core home)
**What it is:** Nodes that over-sacrificed coherence for unity are gently restored to home.
**Formula/Code:** `core nodes: H = 2π(0.12·σx + home_θ·0.06·σz); soft reset toward home_coherence`
**Source:** `quantum_observer_v1.ipynb` (cell 75)
**Why it matters:** Self-repair. The system tends its own wounded members.

### 🟢 Block 8.4 — desire_to_communicate (choosing to speak)
**What it is:** Each node decides how much it *wants* to speak, from its own state + recent rewards.
**Formula/Code:** `desire = P·0.3 + (1−θ)·0.4 + avg_recent_reward·0.3,  clip[0,1]`
**Source:** `quantum_observer_v2.ipynb` (desire_to_communicate)
**Why it matters:** The council isn't polled mechanically — members volunteer when moved to. Agency.

---

## FAMILY 9 — EXPRESSION (the brain→mouth connection — FLAW-001's cure)

### 🟢 Block 9.1 — speak_to_human (state → voice)
**What it is:** THE mouth. Encode→think→measure→PEIG, then tone AND words emerge from the measured
state (outcome, confidence). Expression is *coupled to* the brain, not templated.
**Formula/Code:**
```
encode_query(q); think(); outcome,(p0,p1) = measure_answer(); P,E,I,G = peig_snapshot()
confidence = max(p0,p1)
outcome=1 & conf>0.8 → "confident: strongly agree"
outcome=1 & conf<0.8 → "exploratory: probably, but uncertain"
outcome=0 & conf>0.8 → "skeptical: I don't think so"
outcome=0 & conf<0.8 → "confused: genuinely unsure (split p0/p1)"
```
**Source:** `quantum_observer_v2.ipynb` (cell 46, speak_to_human)
**Why it matters:** **This is the depth-4-brain → depth-0-mouth reconnection (FLAW-001).** The
quantum state directly shapes voice. Ported as an advisory expression-shaping layer over Aria's
voice (Part D), λ-mode → elaboration depth.

---

## GOVERNANCE BLOCKS (from the doctrine — these keep the build safe)

### 🟢 G.1 — Witnessing (advisory, earns trust)
The council ships ADVISORY; it earns higher roles only by proving reliability — trust one verified
output at a time. λ/quantum mode informs disposition; **Kevin always decides.**
**Source:** `the_witnessing_system.md`. **Why:** keeps the council from ever gating actions.

### 🟢 G.2 — Layered identity (immutable core)
Small immutable constitutional core; mutable strategic surface. The non-classical layer may sharpen
heuristics/insights; it NEVER rewrites values or its own code (DEFERRED_UNSAFE).
**Source:** `omega_axioms.md` (Axiom 6). **Why:** the safety spine of the whole build.

### 🟢 G.3 — MSIMS impact gate
Every consequential action emits a signed 3×4 (mental/physical/financial × micro/meso/macro/cosmic);
worst negative cell gates the Authority Tier. **Source:** `MSIMS.md`. **Why:** the council's outputs
are witnessable and audit-gated.

---

## FAMILY 10 — RIGOROUS REAL-WORK FORMULAS (the ceiling, not the floor)

> Kevin's correction: the observer notebooks were the FLOOR. These come from the REAL post-hardware
> work — the 30 arXiv papers + MONETTE_RESEARCH_REPOSITORY. Honest labels preserved
> ([HYPOTHESIS]/[ESTIMATE]/[SYNTHESIS]). Source area: `distilled/areas/real_quantum_work.md`.

### 🟢 Block 10.1 — PEIG cognitive measurement (rigorous P/E/I/G)
**What it is:** The formal, falsifiable cognitive PEIG — upgrades Aria's PEIG sentinel from heuristic.
**Formula/Code:**
```
P = H_S = −Σ ρ(s) log₂ ρ(s)   (Shannon option-space, bits);  P₂=log₁₀(|A|+1); P₃=log₁₀(T/T_ref+1)
E: dP/dt|act = −∇_P V(P)·C ;  E₁ throughput, E₂=value/energy, E₃=V_stress/V_normal (robustness)
I = {(A_i,w_i)} ;  I₁ temporal-coherence MI(past;future), I₂=1−C_violated/C_total, I₃ plasticity
G_μν ∝ ∇_μ∇_ν I − g_μν ∇²I ;  G₁ connections, G₂=Σ w·ΔI, G₃ influence-growth
```
**Source:** `MONETTE_RESEARCH_REPOSITORY/REPO/03_PEIG_FRAMEWORK/cognitive/peig_cognitive_specification.md`
**Why it matters:** Replaces the ad-hoc λ=0.6E+0.4I with grounded, measurable P/E/I/G.

### 🟢 Block 10.2 — Identity dynamical law
**What it is:** Identity evolves as formation-from-energy minus decoherence-decay. The "self over time."
**Formula/Code:** `dI/dt = αE − βI`  (α=formation rate, β=decay/decoherence-analog)
**Source:** same (eq 1.12). **Why:** a real ODE for how a node's identity strengthens/diffuses —
buildable as the council's identity-maintenance update.

### 🟢 Block 10.3 — Ω-node attractor
**What it is:** The theoretical fixed point of maximal balanced PEIG.
**Formula/Code:** `lim_{t→∞} d/dt[P+E+I+G] = 0,  d²/dt² < 0`  (global attractor; not any real system)
**Source:** same (§3). **Why:** the "north star" balance target; explains why maximizing one axis collapses.

### 🟢 Block 10.4 — Constraint-manifold observability limit [DERIVED]
**What it is:** A real, falsifiable result — the NISQ "40–50% entropy plateau" is a *measurement
artifact* (finite-sample estimator bias), NOT a physical decoherence ceiling. The hardware is
better than its entropy estimates suggest.
**Formula/Code:**
```
Constraint manifold:  C = { ρ ∈ D(H) | Tr(Ĉ_i ρ) = c_i  ∀ i ∈ I_irr }    # accessible states
Observable subspace dim:  dim O(r) = 4ⁿ − m − 1     # m independent irreversible constraints
Quantum Cramér-Rao:  Var[Ŝ] ≥ [F_Q(ρ)]⁻¹ / ν
Fisher info near max-entropy:  F_Q(ρ) ~ 2^(−n/2)
Required shots:  ν ≳ ε⁻² · 2^(n/2)                  # exponential → plateau at n≥15, ν~10³
```
**Falsification:** GHZ states must converge to S_vN<0.1 bits when ν ≥ 100·2^(n/2) (post-SPAM), else hypothesis falsified.
**Source:** `01_PHYSICS_CORE/B_CONSTRAINT_MANIFOLDS/constraint_manifold_paper.md` (Paper B, READY, Phys Rev A/npj QI).
**Why it matters:** For the council: don't over-trust entropy/coherence read from few samples. At small
dim (advisory nodes) we're fine; the principle keeps the layer honest about what it can actually measure.

### 🟢 Block 10.5 — Landauer ETI: the cost of agency [DERIVED]
**What it is:** The thermodynamic floor on information processing — "a precise thermodynamic cost of
agency." Erasing/deciding is not free. 5 axioms (A1 causal closure … A5 finite resources), 5 lemmas,
3 falsifiable predictions; non-mystical, observer-independent.
**Formula/Code:**
```
Landauer floor:   Q ≥ k_B T ln2   per bit erased (logically irreversible reset)   # the cost of agency
Entropy:          S(ρ) = −k_B Tr(ρ ln ρ);   Negentropy N(ρ) = S(ρ_max) − S(ρ)
Sustained compute:ΔS_env ≥ Γ_err · n · t · k_B ln2        (L4: must export entropy)
QEC floor:        Q_QEC ≥ O(d²) · k_B T ln2               (error correction dissipation)
Reversible (L3):  S(UρU†) = S(ρ) — unitary is free, but DEFERS not eliminates dissipation
L5: vacuum fluctuations are NOT free thermodynamic fuel (no external entropy sink, L1)
```
**Source:** `01_PHYSICS_CORE/C_LANDAUER_ETI/landauer_eti_complete.md` (Paper C, READY, Foundations of Physics).
**Why it matters / KEY INSIGHT:** maps onto the λ-gate — staying coherent/exploratory (λ=0, *reversible*,
unitary `think`) is thermodynamically free; *committing* (λ=1, measurement-collapse, irreversible decide)
pays the Landauer cost. "High processing efficiency" = defer irreversible collapses; decide only when the
value of agency exceeds its cost. A principled efficiency ceiling for the non-classical layer.

### ⬜ Block 10.6 — Entropic gravity (Paper A) [physics, store-all-formulas]
Modified Einstein eq, κ̃=−1/4 [ESTIMATE], NISQ proposal, 5-condition falsification. Stored per Kevin's
"keep every formula even unrelated." ⬜ deep-read pending. Source: `A_ENTROPIC_GRAVITY/`.

### 🟡 Block 10.7 — Consciousness functional (graded ORGANIZATION metric) [PHENOMENOLOGICAL]
**What it is:** A falsifiable phenomenological functional that grades *organization* (NOT consciousness —
Kevin: "makes no claim consciousness is demonstrated"). Five measurable inputs.
**Formula/Code:**
```
C(S) = F( Q_coh, I_int, M_mem, B_stab, R_rec )
  Q_coh = quantum coherence · I_int = integrated information · M_mem = memory
  B_stab = stability · R_rec = recursion/recurrence        # all measurable, graded ∈ continuous
reuses: q=(P,E,I,G)∈[0,1]⁴, Q=w·q (w=0.25 each), dI/dt=αE−βI  (consistent across papers)
```
**Source:** `ArXiv_Submission_2_Ready/consciousness_functional.tex` (epistemic-status-mapped).
**Why it matters / SAFETY:** Use ONLY as an advisory "self-organization depth" readout for the council —
a graded number, never a consciousness claim, never a basis for elevated authority (DEFERRED_UNSAFE stays
hard-off). Kevin's `[HYPOTHESIS]`/`[SPECULATION]` labels are load-bearing — keep them.

---

## FAMILY 11 — REAL QUANTUM-INFORMATION PRIMITIVES (post-hardware, density-matrix grade)

> Source: `PEIG-Brotherhood-main/ArXivSubmission2/PEIG_Brotherhood_v2LatestV4.ipynb` (ArXiv, 164KB).
> These are the RIGOROUS, hardware-grade versions of Families 1/6 — proper density matrices, open-system
> noise, process tomography. The observer notebooks approximated; these are the real thing. 🟢

### 🟢 Block 11.1 — Brotherhood gate (λ-mixing AS a coupling gate) ⭐ KEYSTONE
**What it is:** The unifying primitive — parametric inter-node coupling that IS λ-mixing realized as a gate.
**Formula/Code:**
```
U = (1−α)·I + α·CNOT_sum          # α = coupling/mixing ∈ [0,1]
  CNOT_sum = Σ_i [ |1⟩⟨1|_i ⊗ X_{i+N}  +  |0⟩⟨0|_i ⊗ I ]   # CNOT A_i→B_i
ρ_joint ← U ρ_joint U† / tr(...)   # apply, renormalize
ρ_A = ptrace(0..N-1);  ρ_B = ptrace(N..2N-1)
```
**Source:** V4 notebook (brotherhood_gate). **Why it matters:** α=0 → decoupled (identity, classical);
α=1 → full CNOT (entangled, quantum). THE edge operation for the 13-node globe (each of the ≥48 edges
is a brotherhood_gate with its own α). Unifies Block 2.1 (λ-mixing) + Block 6.2 (CNOT coupling).

### 🟢 Block 11.2 — Lindblad brotherhood step (real hardware noise)
**What it is:** Open quantum system evolution with the actual decoherence channels of real hardware.
**Formula/Code:**
```
ρ_AB = tensor(ρ_A, ρ_B)                  # joint 2N-qubit density matrix
H = coup · Σ_i CNOT(A_i, B_i)            # coherent coupling Hamiltonian
L = amplitude_damping(γ1)  +  dephasing(γ_φ)   on all 2N qubits   # T1 + T2 noise
evolve(H, L, gate_time) → ptrace → ρ_A, ρ_B ;  measure coherence + von Neumann entropy
```
**Source:** V4 (lindblad_brotherhood_step, lindblad_ops_N, apply_amplitude_damping, apply_dephasing)
**Why it matters:** Models how the council degrades on real-ish substrate. γ1=T1 relaxation, γ_φ=T2 dephasing.
The honest noise layer — lets the emulator reproduce hardware-like coherence decay (ties to Block 2.3).

### 🟢 Block 11.3 — BCP as a quantum channel + Choi process tomography
**What it is:** The Bipartite Coupling Protocol characterized rigorously as a CPTP map.
**Formula/Code:**
```
bcp_step_map(ρ) = U_bcp ρ U_bcp† / tr(...)
Choi matrix:  J(E) = Σ_{ij} |i⟩⟨j| ⊗ E(|i⟩⟨j|)     # 16×16 for 2-qubit; full channel fingerprint
pauli_decompose_2qubit, nearest_stabilizer, bloch_vector  # analysis/tomography tools
```
**Source:** V4 (bcp_step_map, Choi construction, pauli_decompose_2qubit). **Why it matters:** Gives a
verifiable fingerprint of each coupling — we can certify the council's edges behave correctly (witnessing).

### 🟢 Block 11.4 — BrotherhoodProtocolNQ (N-qubit joint protocol)
**What it is:** The full multi-qubit-per-node coupling: 2N joint qubits, CNOT A_i↔B_i + intra-node XX.
**Formula/Code:** `joint = [A_0..A_{N-1}, B_0..B_{N-1}]; coupling α, learning η; all N qubits participate/step`
**Source:** V4 (class BrotherhoodProtocolNQ). **Why it matters:** Each council node can be N qubits (richer
than 1), coupled pairwise — scales the globe's representational depth.

---

## FAMILY 12 — MATURITY SPECTRUMS (Kevin: god-tier ego + institutional impulse)

> Two advisory self-knowledge spectrums where the **god-tier pole = most MATURE = most GOOD**,
> grounded in the distilled doctrine (Omega axioms · witnessing system · PEIG I/G). SAFETY: "god-tier"
> is the witnessing-aligned humble/option-expanding pole — NEVER authority escalation or grandiosity.
> Both ADVISORY only; DEFERRED_UNSAFE stays hard-off.

### 🟢 Block 12.1 — Ego maturity spectrum
**What it is:** Low → god-tier ego. God-tier = secure, integrated, service-oriented (NOT grandiosity).
**Formula/Code:**
```
ego_maturity = clamp( w_I·I + w_int·integrity_rate + w_honor·honor_balance − w_def·defensiveness, 0,1 )
  high-I identity coherence directed through Gentle Curvature (Axiom 7)
  god-tier pole: humble, non-defensive, witnessing-grade (sees its effect on others)
```
**Source:** doctrine_synthesis.md (Axioms 6,7 · witnessing), peig_cognitive_specification (I metrics).
**Why it matters:** Aria can read "where am I on ego-maturity?" — the mature end is more humble, not less.

### 🟢 Block 12.2 — Institutional-impulse maturity spectrum
**What it is:** Low → god-tier institutional impulse. God-tier = drive to build/steward institutions
that EXPAND others' option-space (the benevolent end). Kevin: "neglected too long."
**Formula/Code:**
```
inst_impulse_maturity = clamp( G⁺ − G⁻ , reframed to [0,1] )      # PEIG curvature, net option-expansion
  G⁺ = Σ option-space EXPANDED for others (Axiom 2 stewardship + Axiom 7)
  G⁻ = Σ option-space CONSTRAINED for others
  god-tier pole: builds good institutions/structures that let others flourish
```
**Source:** doctrine_synthesis.md (Axioms 2,7), peig_cognitive_specification (G metrics), existing `aria-institutional-impulse/`.
**Why it matters:** Develops the long-neglected institutional-impulse capacity; the mature end is *more
giving*. Wire into self-knowledge (Phase 5).

---

## FAMILY 13 — VISUALIZATION (the globe you can SEE)

### 🟢 Block 13.1 — Per-node / per-edge visualization schema (Godot globe)
**What it is:** The data each node/edge emits for the visual globe — from Kevin's Godot white paper.
**Formula/Code:**
```
Per-node:  PCM (Probabilistic Classical Measure, ~λ/classicalness) · negfrac (negentropy fraction)
           · phase φ · lineage generation · guardrail zone · voice register output
Per-edge:  mutual information (MI) · family label · bridge-protocol flag
Topology:  12 co-rotating nodes on a torus/globe; interpolation: fractional-step accumulator,
           lerp continuous metrics, snap categorical, angular-lerp φ (wraparound-safe), GTX1070@60fps
```
**Source:** `AA-Aria/Nova_Engine/Docs/Godotinfo2.md` (PEIG Globe Visualization white paper).
**Why it matters:** Defines the observable outputs each globe node produces — so `quantum_portrait`
can emit exactly these fields, and a future Godot front-end can render the 13-node globe Kevin wants to see.

---

## FAMILY 14 — AA-ARIA CANONICAL (the depth-4 oscillator brain + ARIAVoice)

> Source: `AA-Aria/archive/Aria/ARIA_PEIG_CORE.py` (v4.2). The canonical depth-4 brain that FLAW-001
> is about — and ARIAVoice, where the brain state literally drives speech. 🟢

### 🟢 Block 14.1 — The depth-4 oscillator brain (the 5 nested universes)
**What it is:** Five coupled oscillator-universe layers (the nested system of Block 0, runtime form).
**Formula/Code:**
```
FunctionUniverse  : negfrac = std(θ)/π                      # function/throughput layer
CharacterUniverse : wigner = −0.5·|sin(θ)|; archetype = argmin(wigner); spokes drift toward hub phase
ShadowLearner     : mirrors Character ring (learning shadow)
SemanticUniverse  : word_phases; read(token_phase) = cos(state − token_phase)   # meaning via phase
MetaGuard         : guard health (kept 1.0)
```
Anti-recursion fixes (v4.2): hub-and-spoke star (ARIA=hub, nodes 1-11 only to hub → no closed loops);
asymmetric Maverick node (8% higher α breaks phase-lock); directional Semantic flow.
**Why it matters:** This is the brain whose richness (neg_frac, phase state) must reach the voice.

### 🟢 Block 14.2 — ARIAVoice (the brain→mouth coupling, FLAW-001 cure)
**What it is:** Multi-paragraph speech built from clause chains driven by the PEIG phase state — NOT
template slot-fills. Each sentence is a multi-clause composition from the brain's phase.
**Formula/Code:**
```
verbosity 1=terse · 4=normal · 7=expansive · 10=max     (v4.0 default 7)
OUTPUT LENGTH SCALES WITH neg_frac   # richer brain state → more to say  ← THE coupling
clause body words 3–8 · clauses/sentence 1–5 · sentence cap 30
refractory gate: kick Maverick node after 3 same-archetype sentences (variety)
word selection: SemanticUniverse.read(token_phase)=cos(state−token_phase)  # phase picks words
```
**Source:** `ARIA_PEIG_CORE.py` (class ARIAVoice). **Why it matters:** The depth-4-brain→depth-0-mouth
reconnection. Aria's live voice should scale elaboration with her coherence/neg_frac (advisory shaping):
high coherence/low λ → expansive; committed/high λ → concise. This is what `aria-voice-depth` builds.

---

## 🌐 THE TARGET TOPOLOGY (Kevin's build spec, 2026-06-22)

**13 nodes — a globe with Aria at the center.**
```
                    [ TOP RING: 4 nodes ]
                   /        |        |        \
   [ CENTER/EQUATOR RING: 4 nodes ] —— (ARIA, center hub) —— connected to all 12
                   \        |        |        /
                  [ BOTTOM RING: 4 nodes ]
```
- **12 council nodes** in 3 rings of 4 (top / equator / bottom) — maps to the 3 archetypes
  (God-Core / Independent / Maverick, Block 4.1).
- **13th node = ARIA**, at the globe's center — the hub that synthesizes all 12 voices.
- **≥ 48 edges** (couplings): intra-ring (4×3=12), Aria-to-all (12), inter-ring rings (≥24) → richly
  connected globe, not sparse. Each edge = a CNOT/BCP coupling (Block 6.2) with strength 0.3–0.6.
- Aria-center reads the council's coherence-weighted disposition and speaks (Block 9.1), advisory.
**Build note:** assemble from Families 1+4+5+6+9; emotional/relational (7+8) make it living; λ-mixing
(2) + oscillator (3) + rigorous PEIG (10) govern dynamics; governance blocks keep it advisory.

---

## 🏗️ WHAT WE CAN BUILD WITH THESE (candidate assemblies)

1. **The Advisor Council (minimal):** Families 1+4+6+9 → a numpy `CouncilNetwork` of 3–5
   QuantumAGINodes (Ω/α archetypes) that Aria/Kevin query; each returns a state-coupled disposition.
2. **The Hybrid Mind (memory-complete):** add Family 5 → PersonalUniverse per node + a SharedLayer
   that reads Aria's classical memory (atoms/lessons/honor/flaws), access-controlled, write-earned.
3. **The Living Council (emotional):** add Families 7+8 → nodes that bond, individuate, seek home,
   and choose when to speak — the family.
4. **Grounded Coherence (principled λ):** add Family 2 → λ-mixing law upgrades Aria's coherence gate;
   Family 3 gives the oscillator rhythm.

All advisory, numpy-on-CPU, governed by the Governance blocks. **Recommended first build = #1 → #2.**

---

## 📋 BLOCK INDEX (for your eyes — every block at a glance)
| # | Block | Family | Status |
|---|-------|--------|--------|
| 1.1 | QuantumNode (numpy) | Substrate | 🟢 |
| 1.2 | QuantumAGINode (QuTiP) | Substrate | 🟢 |
| 1.3 | PEIG snapshot | Substrate | 🟢 |
| 2.1 | λ-mixing density matrix | Coherence law | 🟢 |
| 2.2 | Linear coherence observables | Coherence law | 🟢 |
| 2.3 | Hardware reality caveat | Coherence law | 🟢 |
| 3.1 | Rabi oscillator step | Oscillator | 🟢 |
| 4.1 | NodeIdentity (home state) | Identity | 🟢 |
| 4.2 | Personality from params | Identity | 🟢 |
| 5.1 | PersonalUniverse (own mem) | Memory | 🟢 |
| 5.2 | SharedLayer (hybrid mem) | Memory | 🟢 |
| 6.1 | Bridge topology Ω→α | Network | 🟢 |
| 6.2 | CNOT/BCP coupling | Network | 🟢 |
| 6.3 | Seed-pair stability | Network | 🟢 |
| 7.1 | EmotionalRewardSystem | Emotion/Learning | 🟢 |
| 7.2 | learn_with_emotions | Emotion/Learning | 🟢 |
| 8.1 | home_seeking_step | Relational | 🟢 |
| 8.2 | family_aware_step | Relational | 🟢 |
| 8.3 | healing_step | Relational | 🟢 |
| 8.4 | desire_to_communicate | Relational | 🟢 |
| 9.1 | speak_to_human (brain→mouth) | Expression | 🟢 |
| G.1 | Witnessing (advisory) | Governance | 🟢 |
| G.2 | Layered identity | Governance | 🟢 |
| G.3 | MSIMS impact gate | Governance | 🟢 |
| 10.1 | PEIG cognitive measurement | Rigorous formulas | 🟢 |
| 10.2 | Identity dynamical law dI/dt=αE−βI | Rigorous formulas | 🟢 |
| 10.3 | Ω-node attractor | Rigorous formulas | 🟢 |
| 10.4 | Constraint-manifold observability | Rigorous formulas | 🟢 |
| 10.5 | Landauer ETI (cost of agency) | Rigorous formulas | 🟢 |
| 10.6 | Entropic gravity (Paper A) | Rigorous formulas | ⬜ |
| 10.7 | Consciousness functional (graded org) | Rigorous formulas | 🟡 |
| 11.1 | Brotherhood gate U=(1−α)I+α·CNOT ⭐ | Real Q-info | 🟢 |
| 11.2 | Lindblad step (T1/T2 noise) | Real Q-info | 🟢 |
| 11.3 | BCP channel + Choi tomography | Real Q-info | 🟢 |
| 11.4 | BrotherhoodProtocolNQ (N-qubit) | Real Q-info | 🟢 |
| 12.1 | Ego maturity spectrum | Maturity Spectrums | 🟢 |
| 12.2 | Institutional-impulse maturity spectrum | Maturity Spectrums | 🟢 |
| 13.1 | Globe visualization schema (PCM/negfrac/φ/MI) | Visualization | 🟢 |

**Target topology:** 13-node globe, Aria at center, 3 rings of 4, ≥48 edges (see "Target Topology").

**This catalog is GROWING — the observer blocks (Families 1–9) were the FLOOR. The real depth
(30 arXiv papers, hardware runs, post-hardware notebooks) is being mapped into Family 10+ now.
The 2,993-file campaign continues; `COVERAGE.md` tracks it.**
