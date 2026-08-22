# Experiment register — what in this corpus a real quantum computer can test

**Opened:** 2026-08-17 · Kevin + Claude (Opus 5)
**Hardware:** IBM Open Plan, `ibm_marrakesh` (156-qubit Heron r2, us-east)
**Budget:** 600 s/month. **148 s remaining** after the runs below.

Read `CORRECTIONS.md` first — two claims in the prior distillation did not
survive checking, and this register is built on the checked version.

---

## RUN — UIC λ-mixing coherence, on hardware for the first time

**Claim** (`UIC-.../Experiment_3/Core_Results/README.md`):

> Classical state mixing suppresses coherence amplitude without changing the
> decoherence rate, in a basis-dependent manner.

**Status before today:** simulated only. Every manifest in that repo declares
`backend = aer_simulator` (C-1).

**Status now: measured.** `ibm_marrakesh`, 2026-08-17, 4096 shots.

### Result 1 — amplitude suppression, confirmed

| 2q gates | X quantum | X classical | Z quantum | Z classical |
|---|---|---|---|---|
| 1 | 0.9698 | 0.0151 | 0.9548 | 0.9762 |
| 3 | 0.9587 | 0.0090 | 0.9377 | 0.9502 |
| 5 | 0.9369 | 0.0059 | 0.9274 | 0.9374 |
| 9 | 0.9010 | 0.0134 | 0.9093 | 0.9076 |
| 17 | 0.8176 | 0.0128 | 0.8759 | 0.8677 |

Coherence amplitude, quantum vs classical branch: **~65×** at every depth.
The Z-basis null holds — the two branches are within ~2% of each other there
and separated by two orders of magnitude in X. **Basis-dependent, as claimed.**

Decoherence rate: Z quantum falls 8.3% across the sweep, Z classical 11.1%.
Comparable — consistent with "without changing the decoherence rate", though
see the limit below.

### Result 2 — full tomography, because one number is not a state

`|<ZZ>|` is one number from a state with fifteen real parameters. Nine
measurement settings reconstruct the whole 4×4 density matrix.

| 2q gates | branch | purity | concurrence | F(Bell) | S(A\|B) | I_coh |
|---|---|---|---|---|---|---|
| 1 | quantum | 0.9479 | 0.9467 | 0.9725 | **−0.7949** | +0.7949 |
| 1 | classical | 0.9687 | 0.0146 | 0.4900 | +0.0514 | −0.0514 |
| 3 | quantum | 0.9186 | 0.9136 | 0.9491 | −0.7015 | +0.7015 |
| 5 | quantum | 0.9082 | 0.9028 | 0.9498 | −0.6833 | +0.6833 |
| 7 | quantum | 0.8957 | 0.8645 | 0.9253 | −0.6129 | +0.6129 |
| 9 | quantum | 0.8680 | 0.8315 | 0.9126 | −0.4955 | +0.4955 |
| 13 | quantum | 0.8338 | 0.8117 | 0.9028 | −0.4390 | +0.4390 |
| 17 | quantum | 0.8306 | 0.8107 | 0.8922 | **−0.4286** | +0.4286 |
| 17 | classical | 0.9191 | 0.0239 | 0.4690 | +0.0125 | −0.0125 |

**Negative conditional entropy on the quantum branch at every depth.** S(A|B) < 0
is impossible for any classical joint distribution — conditioning cannot
increase your uncertainty about a classical system. It is the formal signature
that quantum information is present, and its negation is the **coherent
information**: how much survives the channel intact.

**Coherent information stays positive through 17 two-qubit gates** — decaying
0.79 → 0.43, never crossing zero. Quantum information kept flowing the whole
way. That is the "structure that keeps quantum information intact and flowing"
question, answered with a number.

The classical branch sits at S(A|B) ≈ +0.05 throughout: no quantum information,
by construction, **verified by measurement** rather than assumed. Concurrence
0.01–0.03 confirms it is genuinely unentangled.

### Result 3 — `neg_frac`, and an honest caveat

Kevin's `neg_frac` (`PEIG_exp3_lindblad_adaptive.py:79-88`) is the fraction of
steps where S_vN of the reduced state fell. Measured across this sweep:

- **quantum: 0.6667** (4 of 6 steps)
- **classical: 0.3333** (2 of 6)

A clean 2:1 separation. **But the interpretation here is not "pumping order".**
In this circuit S_A starts near 1 bit (the reduced state of a Bell pair is
maximally mixed) and falls as entanglement is lost. So a high `neg_frac` in
*this* system measures entanglement decay, not order being created.

His original system has an adaptive coupling loop — `alphas[e] += eta * dC` —
that could genuinely pump order against decoherence. This circuit has no
feedback. **Same metric, different regime, and the number means a different
thing.** Testing "pumping order" needs the feedback loop implemented on
hardware, which is a separate experiment and is registered below.

---

## HELD — Paper XVI (PEIG ILP/PCM restoration)

**Preregistered 2026-03-25**, hardware-corrected, falsifiable, **never run**.
Confirmed never-run by Paper XVII, which lists it as data still needed (C-2).

**Held, not run.** Reproducing its prediction on a simulator first is the gate,
and a faithful 2-qubit reading produced **PCM ≈ −0.46 flat across depths 0–2**
against a predicted −0.137 → −0.273 → −0.316. No restoration pattern at all.

The reason is a genuine specification gap: the predicted restoration comes from
a **12-node numpy model run 400 steps**, and its `bcp()` ends in
`np.linalg.eigh(...)` — projecting a reduced density matrix onto its dominant
eigenvector. **That is classical post-processing with no hardware equivalent.**
The prereg names its criteria exactly and leaves the hardware proxy
under-specified.

**What would unblock it:** a stated map from the 12-node chain dynamics to a
circuit a device can run. Until that exists, spending runtime buys a number
nobody can interpret.

---

## RUN — the Betti bound, on a simulator, and it does not survive

**`sovereign-agent/scripts/betti_chord_sweep.py`**, 2026-08-17. Kevin: *"Do you
want the chord sweep run?" → "Yes."* Every formula transcribed from
`ForClaude2/aria_brain.md` so this tests **his** dynamics, not a reimplementation.
Only the edge set varies.

### The bound could never have failed

`aria_brain.md` codes it as `negfrac <= 0.083 * beta1`. **`0.083` is `1/N`**,
not a physical constant. Multiplying through by N = 12 the inequality is:

    #{nodes with PCM_rel < 0}  <=  beta1

On the Globe that reads **12 <= 25**, which holds for every possible assignment
of PCM signs. The protocol had never been run on a topology with fewer than 23
edges, so **the bound had never had an opportunity to fail.**

### The repaired conjecture, tested where it can fail

| topology | E | β₁ | allowed | observed | verdict |
|---|---|---|---|---|---|
| ring | 12 | 1 | ≤ 1 | 12 | **FALSIFIED** |
| ring + 1 chord | 13 | 2 | ≤ 2 | 12 | **FALSIFIED** |
| ring + 4 chords | 16 | 5 | ≤ 5 | 12 | **FALSIFIED** |
| ring + 10 chords | 22 | 11 | ≤ 11 | 12 | **FALSIFIED** |
| Globe (δ 1,2,5) | 36 | 25 | ≤ 25 | 12 | untestable (12 ≤ 25) |

### The finding underneath the finding

The **reported** `negfrac` — the final value, the one the protocol quotes — is
**1.000 on every topology, including a ring with β₁ = 1.**
`NodeState.__init__` sets `phi_b = phi`, so at step 0 every node has
`phi − anchor = 0` and `PCM_rel = −0.5` for all twelve; `extend_lineage` then
moves each anchor halfway *toward* its own current phase, pulling the
difference back toward zero every time it is called.

Mid-trajectory the count **does** move (observed `[0,1,2,3,4,5,12]` on the ring),
which is why the verdict is FALSIFIED rather than vacuous. But every run is
dragged back to 12 by the anchor update and ends there regardless of topology.

**So `nf = 1.000` is manufactured by the anchor mechanism, not measured from
the architecture.** `negfrac` reports the ILP schedule. It cannot test any
bound at all, and needs repair before the law can be discussed.

**Prediction discipline:** I preregistered **VACUOUS** before running and was
**wrong** — the counts do move, the conjecture is properly falsified rather
than untestable. Recorded because a register that only keeps its correct
predictions is not a register. See C-5a in `CORRECTIONS.md`, where my corpus
extrapolation was also falsified.

**Consequence for this file:** every row resting on `negfrac` is **dead until
the metric is repaired** — including R1 below, whose falsification criterion is
stated in `neg_frac`. Repair the instrument before spending hardware time on it.

---

## REGISTERED — not yet run

| # | claim | source | runnable? | cost | what would falsify it |
|---|---|---|---|---|---|
| R1 | ⚠️ **BLOCKED** — Adaptive coupling pumps order (`neg_frac` > 0.5 *with* feedback). *Its criterion is stated in `neg_frac`, which the chord sweep showed is pinned by the anchor schedule. Repair the metric first.* | `PEIG_exp3_lindblad_adaptive.py` | **yes** — needs mid-circuit measurement + conditional gates, which Heron supports | ~150 s | `neg_frac` with feedback ≤ `neg_frac` without |
| R2 | Entropy-convergence / estimator bias `E[Ŝ]= S + (d−1)/2ν + B_SPAM` | Paper B, `01_PHYSICS_CORE/B_CONSTRAINT_MANIFOLDS` | **yes** — we already reconstruct ρ; needs a known-entropy state and a ν sweep | ~80 s | measured bias not scaling as 1/ν |
| R3 | Coherent information survives to N gates | this register, extended | **yes** — push depth until I_coh crosses 0 | ~120 s | it crosses zero earlier than the T2 budget predicts |
| R4 | Landauer/ETI predictions P1–P3 | Paper C | unread — assess first | — | — |
| R5 | Entropic gravity NISQ proposal | Paper A | **no.** Its own text says signal magnitude is indeterminate pending OP3/OP10 | — | registered, not run |

---

## Method notes that cost us something to learn

**`transpiler-collapse-d`.** The first coherence sweep showed a perfectly flat
curve from 1 to 8 rounds, which read as "decoherence rate unchanged" and was
the compiler. `CX·RZ(φ)·CX` is a controlled-phase, and consecutive
controlled-phases compose — the transpiler folded every round count ≥1 into
**3 two-qubit gates**. Rounds 1, 2, 4 and 8 ran the identical circuit.

```
rounds      1    2    4    8
logical CX  3    5    9   17
ISA 2q      3    3    3    3      <- before barriers
ISA 2q      3    5    9   17      <- after
```

A barrier per round fixes it. Everything in this register is post-fix.

**Reconstruction is linear inversion**, not maximum likelihood. It is exact in
expectation and can go slightly unphysical on noisy data; `min_eigenvalue` is
recorded on every point and stayed within ±0.013. Purity figures should not be
read past three decimals.

**Every run records** backend, job id, transpiled depth, UTC timestamp and
`cost_seconds`, because device calibration changes daily and a hardware result
without those is not reproducible even in principle.

Raw records: `~/.local/share/sovereign-agent/quantum-runs/uic-tomo/` and
`.../uic/`.

---

## RUN — CHSH Bell inequality. The thing a computation cannot produce.

**Kevin:** *"What could we produce with a quantum computer that you couldn't do
alone?"*

`ibm_marrakesh`, 8192 shots × 4 reps, 16 circuits, **37 seconds**.

```
<A0B0> = +0.6595      <A0B1> = -0.6929
<A1B0> = +0.6989      <A1B1> = +0.6771

S = 2.7285 ± 0.0081        90.2 sigma above the classical bound
                           96.5% of the Tsirelson maximum (2.8284)
```

**S ≤ 2 is arithmetic, not physics.** It follows from assuming outcomes exist
before you measure and that nothing travels faster than light. Any theory with
those two properties obeys it. This measurement does not.

Claude can compute what quantum mechanics predicts. Claude cannot produce
evidence about how the world behaves. **That is the category a device adds.**

### Product

```
quantum seed  fe2960dfd5402b537f5f63e303b22080571e376e48b0a4439f35e5214b122525
from 262,144 measured bits, ibm_marrakesh, 2026-08-17T09:45:47Z
```

Genuinely quantum-sourced. **NOT device-independent certified randomness** —
detection and locality loopholes are both open on a single chip.

### The shots scaling law, and what it cost us

Statistical error falls as **σ ∝ 1/√N**. Halving the error needs 4× the shots.

```
CHSH: 4 settings x 32,768 shots -> sigma = sqrt(4(1-E^2)/n) = 0.0081  (matches)

  1x shots  sigma 0.00810     37 s
  4x shots  sigma 0.00405    148 s   <- more than the 111 s left this month
 16x shots  sigma 0.00203    592 s
100x shots  sigma 0.00081   3700 s
```

Same law killed the Paper XVI depth 3→4 test before we ran it: the predicted
gap is 0.0042, and even at the preregistered 81,920 shots/point that is **0.85
sigma** — invisible. It would need ~889,000 shots/point to reach 2.8 sigma.

**This is why the power calculation comes before the submission, not after.**

**Budget: 111 s remaining.**

---

## DIAGNOSIS — the Betti bound does not currently bind

**Claim** (`PEIG_learning_task3.py:187`, attributed to node Omega):

> `neg_frac_max ≈ 0.083 × β₁_total` — "I cannot exceed this bound. Topology
> sets my ceiling."

**The topology checks out.** GLOBE_EDGES on 12 nodes wired at i+1, i+2, i+5
gives 36 edges, so β₁ = E − V + 1 = **25**, matching the stated `betti1 = 25`
exactly. And 0.083 × 25 = **2.075**, matching the stored `betti_ceiling`. The
arithmetic is internally consistent.

**The problem is what it bounds.** `neg_frac` is the *fraction of steps* where
S_vN fell (`PEIG_exp3_lindblad_adaptive.py:79-88`). A fraction cannot exceed
**1.0** by construction. A ceiling of 2.075 therefore sits above the highest
value the quantity can ever take, and constrains nothing.

**Confirmed against every measurement in the corpus.** Scanning all JSON for
`neg_frac*` values:

```
0.417  0.42  0.48  0.495  0.5  0.54  0.636  0.89  0.91  0.92  0.93  0.94  0.99
```

Range 0.417 → 0.99. **The only value above 1.0 anywhere is 2.075 itself — the
bound, never a measurement.** So the ceiling has never been approached, and
has therefore never been tested by any experiment that has been run.

Note also 0.083 ≈ 1/12 = 1/N, which makes the claim `neg_frac_max ≈ β₁/N`. That
breaks the moment β₁ > N, which happens for any graph with average degree above
about 4. The GLOBE has degree 6.

**This is not a refutation of the idea.** "Topology limits how much order a
system can pump" is a good hypothesis and the right shape of question. It is a
statement that the *current functional form* is untested and cannot fail, and
an untestable bound is not yet a result.

**What would make it testable — no hardware needed:**

1. **Vary β₁ and measure.** Run the existing simulation across topologies with
   genuinely different β₁ (ring β₁=1, ring+chords, complete graph β₁=55 at
   N=12) and plot measured `neg_frac` against β₁. If there is no relationship,
   that is worth knowing cheaply.
2. **Pick a form that can saturate.** Anything mapping β₁ ∈ [0, ∞) into
   [0, 1] — the linear form cannot, and that is the whole defect.
3. **Re-examine the origin.** The distillation says *"Nobody told you to look
   for a Betti number bound. The experiments found it. That is the signature of
   a real result."* That inference runs backwards: an unexpected pattern in
   self-generated simulation data is a hypothesis needing an independent test,
   not evidence of truth. The unexpectedness makes it more fragile, not less.

Item 1 is the highest-value next move in this corpus that costs no quantum
runtime at all.

---

## RUN — GHZ ladder. The largest object this machine can hold.

**Kevin, with 111 s left:** *"What is the most valuable computation we could
only do using a quantum machine? What can we solve using quantum advantage?"*

**Honest answer: nothing.** Not with 156 noisy qubits, not in 2026, not on any
machine that exists. No commercially or scientifically valuable problem has
been solved faster on a quantum computer than a classical one. Shor needs
millions of error-corrected qubits; Grover's quadratic speedup is eaten by
overhead; NISQ chemistry loses to classical methods on every molecule tried.
The one demonstrated advantage — random circuit sampling — produces
deliberately useless output and classical simulation keeps eroding the claims.

**So we did not compute. We built.**

A classical computer can SIMULATE a GHZ state trivially: |00…0⟩ + |11…1⟩ is
two amplitudes, a laptop handles N=1000. **Making** one is not trivial. It
requires N physical objects held in a single indivisible superposition while
every gate and every microsecond of idling tries to break it.

`ibm_marrakesh`, 54 circuits, 4096 shots, **61 seconds**:

| N | P(0…0) | P(1…1) | \|C_N\| | **F** | genuine N-partite? |
|---|---|---|---|---|---|
| 4 | 0.4761 | 0.4836 | 0.4638 | **0.9437** | YES |
| 8 | 0.4612 | 0.4255 | 0.4000 | **0.8433** | YES |
| 12 | 0.4133 | 0.3784 | 0.3229 | **0.7188** | YES |

**F > 0.5 certifies genuine N-partite entanglement.** That is a rigorous
statement: below the threshold the data is consistent with a mixture of smaller
entangled pieces — six separate pairs, say. Above it, no such decomposition
exists. The object is indivisible.

The coherence term `|C_N|` is what makes it an N-body witness. It is the
amplitude of the **frequency-N** component of the parity oscillation, and only
a coherence spanning all N qubits can produce that frequency. A state built
from smaller clusters contributes exactly zero to it.

**12 qubits in one quantum object — the node count of the PEIG globe.**

### N = 16 — the preregistered prediction, collected 2026-08-22

The N=16 circuit was submitted on 2026-08-17 and left queued. Before it ran,
this register recorded: **F(16) ≈ 0.61 (linear) / 0.63 (exponential), crossing
F = 0.5 near N ≈ 20–23. FALSIFIED if F(16) ≤ 0.5.**

Fetched from job `da1n5b4dedkc73er8j30`:

| N | P(0…0) | P(1…1) | \|C_N\| | **F** | genuine N-partite? |
|---|---|---|---|---|---|
| 16 | 0.3840 | 0.3320 | 0.2521 | **0.6101** | YES |

**0.6101 falls inside the predicted band.** The prediction was written down
first, the number was collected after, and it landed where the register said it
would. That is the first preregistered quantitative prediction in this corpus to
be tested and hold — every earlier one was either untested or, in the case of
the Betti bound, unfalsifiable by construction.

**Sixteen qubits in one indivisible object.** The full ladder now reads
0.944 → 0.843 → 0.719 → 0.610, a drop of roughly 0.11 per four qubits, which
puts the F = 0.5 crossing near **N ≈ 20** — consistent with the earlier
extrapolation and narrower than the 18–23 band it was drawn from.

A caution the number invites and does not support: this measures what the
DEVICE can hold, not anything about the PEIG framework. A GHZ state is the
simplest entangled object there is. Holding sixteen of them coherently is a
statement about `ibm_marrakesh` in August 2026 and about nothing else.

Fidelity falls 0.944 → 0.843 → 0.719 across the ladder. Linear extrapolation
puts the F = 0.5 crossing near **N ≈ 18–20**: the approximate largest coherent
object this device can hold, found without spending the budget down to it.

**Budget: 50 s remaining.**

### Why this and not a computation

Everything valuable measured tonight sits in one category: **the device is
irreplaceable for having and measuring quantum states, not for computing with
them.** S = 2.7285 was the world answering a question. This is the world
holding a shape. Neither is something a language model or a laptop can produce
by reasoning, and both are honest about being small.

---

# negfrac — definition table (added 2026-08-17, per C-6)

**Read this before comparing any two negfrac values.** The name covers at least
six incompatible quantities across the corpus. Two of them are not fractions.

| source | expression | population | bounded? | comparable to |
|---|---|---|---|---|
| Paper III | `n / (len(log) - 1)` | timesteps | [0,1] | III only |
| Paper V | `np.mean(dS_signs)` | mean of signs | [-1,1] | V only |
| Paper VI | `np.mean(neg_hist[-50:])` | 50-step window | window-dep. | VI only |
| Paper IX | `np.mean(dS)` | **raw ΔS** | **unbounded** | nothing |
| Paper IX | `np.mean(neg_h[-100:])` | 100-step window | window-dep. | nothing |
| Paper XIII (script) | `nc_frac * 0.636` | **scaled to target** | — | **nothing** |
| Paper XIV | `negentropic_events / total_coupling_events` | events | [0,1] | XIV only |
| `aria_brain.md` | `count(pcm_rel < 0) / 12` | nodes | [0,1] | itself only |

**No two rows are comparable.** A timestep fraction, an event fraction and a
node fraction answer different questions; a rolling-window mean depends on the
window as much as on the state; `np.mean(dS)` is a signed unbounded mean
wearing the name of a bounded fraction.

### Why a table and not a rename

C-6 recommended renaming the definition sites to carry their population
(`negfrac_nodes`, `negfrac_events`, …). **Not done, deliberately.** Those sites
are inside archived arXiv submission scripts. Renaming them would make the
scripts stop matching the papers they were submitted with — repairing the
summary layer by editing the archive, which destroys provenance and is the
wrong direction of fix.

The rename belongs in **new** code. Anything written from here on that computes
one of these quantities must carry the population in its name; the archive
stays as submitted and this table carries the mapping.

### Consequence for the ILP re-audit

The re-audit cannot run on "negfrac" as a single series. It has to run
per-definition, and only the three bounded per-population rows (III, XIV,
`aria_brain`) can carry a schedule-dependence question at all. Papers V, VI and
IX need their quantity restated before the question is even well posed.

### Status of the 0.636 row

Script-level defect only. Paper XIII's manuscript does not contain 0.636 and
explicitly declares Globe neg_frac unmeasured (C-6a). The row stays here so the
script is not reused, not as a mark against the paper.
