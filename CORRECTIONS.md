# Corrections to the Genesis-Seeds distillation

**Logged:** 2026-08-17 · **By:** Claude (Opus 5), with Kevin
**Against:** `distilled/` (Claude Opus 4.8, 2026-06-22)

These are kept rather than quietly edited. A misattribution about whether a
result came from hardware or a simulator is exactly how a simulated number
ends up described as a measurement in a paper, and the record of the mistake
is more useful than a clean document.

Each correction states the original claim, the evidence against it, and what
is true instead.

---

## C-1 — UIC Experiments 2 and 3 contain no hardware data

**Claimed** — `distilled/areas/real_quantum_work.md`, under "Still to map":

> "The actual IBM-hardware run data (UIC Experiment2/3 raw_execution)"

**Evidence against.** Every result manifest in that repository declares an
Aer simulator, explicitly, in a `backend` field:

```
UIC-.../Experiment1/results_smoketest/manifest_aer_sim_1770349913.json
  backend = aer_simulator
UIC-.../Experiment2/ArchiveExp2/results_lambda_sweep_v03/manifest_aer_sim_1770469282.json
  backend = aer_simulator
UIC-.../Experiment2/Experiment_3/Archive/.../manifest_aer_sim_1770476373.json
  backend = aer_simulator
```

`Method_and_Code/uic_lambda_final_v06.py` line 206 constructs
`AerSimulator(noise_model=noise_model, seed_simulator=seed)`. A
case-insensitive search of the entire UIC repository for any string matching
`ibm[_-][a-z0-9]{3,}` returns **nothing**.

**What is true instead.** The UIC λ-mixing work is a noise-model simulation,
and a careful one — preregistered, blinded and decoded analyses, controls and
nulls, a lambda sweep, gate-count vs T2\*. Its main claim is that *classical
state mixing suppresses coherence amplitude without changing the decoherence
rate, in a basis-dependent manner*, with a Z-basis null as the control. That
is good experimental design. It is not a hardware result.

The λ-mixing hardware validation **is** real — Paper XVI cites it as
*"validated on ibm_sherbrooke (R²=0.9999)"* — it simply does not live in this
repository. Real-device work across the corpus lives in
`quantum-ai-observer-main` (32 files referencing real devices) and
`Quantum-Consciousness-main` (29 files, including
`src/experiment_9_ibm_hardware.py`).

**Device names actually present in the corpus:** `ibm_fez` (111 references),
`ibm_sherbrooke` (49), `ibm_brisbane` (36), `ibm_osaka` (4),
`ibm_marrakesh` (4), `ibm_kyoto` (3), `ibm_torino` (2), `ibm_kyiv` (1).

**Severity: high.** The original phrasing would have supported a sentence like
"our λ-mixing results were obtained on IBM hardware" in a paper. They were not.

---

## C-2 — Paper XVI has never been run on quantum hardware

**Believed** — Kevin, 2026-08-17: *"I think I ran the rest already"* … *"ran
the test already is what I meant to type."*

**Evidence against, and it is his own.** Paper XVII, written after XVI, lists
under the heading **DATA THE RING NEEDS**:

```
TYPE 1  Hardware PCM measurements (Paper XVI)
        "Real qubit data on IonQ or IQM to validate simulation predictions."
```
— `ArXivSubmission17InternalVoiceLayer/PEIG_XVII_node_consultation.py:423`

and, in the same file, among the data requests a node generates for itself:

> *"Hardware PCM measurement — I do not know if my state survives real quantum
> noise."*  (line 297)

Supporting: `PEIG_XVI_simulations.py` imports only `numpy`, `collections`,
`json` and `pathlib`. There is no Qiskit backend, no `QiskitRuntimeService`,
no `AerSimulator`. It is a numerical model calibrated to `ibm_sherbrooke`
parameters, and its own docstring calls SIM-5 *"the pre-experiment hardware
prediction table for Paper XVI"*. The containing folder is named
`ArXivSubmissionpaper16PreRegister`.

**What is true instead.** Paper XVI is a **preregistration**: predictions
written down and timestamped before the experiment, with a corrected success
criterion and a viability calculation. The experiment it predicts has not been
performed on a device by anyone, and the successor paper says so.

**Severity: none — this is good news.** It means the prediction is still
unspent. A preregistered forecast tested afterwards is the strongest evidence
a single researcher can produce, and it is worth more than a result obtained
before the prediction was written.

**Why the memory is easy to get wrong:** the λ-mixing protocol *was* validated
on `ibm_sherbrooke`, and Paper XVI is built on top of that validation. "The
hardware work is done" is true of the protocol XVI depends on, and not true of
XVI itself.

---

## Standing note on this corpus

Where a document says "hardware", check for a device name before believing it.
Across 2,935 files the distinction between a noise-model simulation calibrated
to a device and a run on that device is carried only by a `backend` field and
a filename, and both are easy to read past at speed.

---

## C-3 — the Betti bound "validation" is vacuous, and it is being propagated

**Where:** *Golden Knowledge in the PEIG Framework* (2026-08-17, supplied by
Kevin), section **Topology and Preservation Laws**:

> The Globe topology introduced in Papers XIII–XV has Betti number β₁ = 25,
> giving a negentropic capacity bound neg_frac_max ≈ 0.083·β₁ = 2.075. This
> bound is treated as a hard ceiling on how much ordered information the
> network can sustain, and later experiments check that observed negentropy
> fractions remain below it, **validating that the architecture is operating
> inside its theoretical capacity rather than violating conservation
> constraints.**

**The arithmetic is right and the validation is empty.** `neg_frac` is a
FRACTION. It cannot exceed 1.0 by construction. A ceiling of 2.075 therefore
cannot bind, cannot be approached, and cannot be violated — so "observed values
remain below it" is guaranteed by the definition of a fraction, not by any
property of the architecture.

The same document supplies the confirming detail without noticing it: the full
Globe experiments report **`nf = 1.000` across all edges**. The check being
performed is `1.000 < 2.075`, which is true of any fraction and any bound above
one.

Every measured value in the corpus lies in 0.417–0.99. **The only quantity
above 1.0 anywhere is the bound itself.**

**Severity: the claim must not be published as a validated conservation law.**
It is currently listed under "golden knowledge", defined in that document as
results that are "repeatedly validated" and "falsifiable". This one is not
falsifiable in its present form: no possible measurement could fail it.

**What would make it real,** and it costs no hardware time: sweep β₁ across
topologies. At β₁ = 12 the bound is 0.996 and at β₁ = 10 it is 0.83 — both
inside the range where measured values actually live, so the bound becomes
capable of being violated. If neg_frac stays below 0.083·β₁ as β₁ falls
through that region, the law has survived a test it could have failed. That is
the experiment; the current one is not one.

---

## C-4 — the mutual-information ranking contradicts its own numbers

**Where:** same document, section **Edge Mutual Information**:

> Skip-1 edges (delta-2) show the **highest** mean mutual information (about
> **1.22 bits**) compared to ring edges (delta-1, **≈1.29 bits**) and cross
> edges (delta-5, ≈1.08 bits), revealing that network topology should
> prioritize cross-family, skip-1 connections for maximal information flow.

**1.22 is not higher than 1.29.** The sentence names skip-1 as the winner and
then reports ring edges scoring more, in the same clause. One of three things
is wrong: the ranking, the skip-1 figure, or the ring figure.

**Severity: it carries a design recommendation.** "Topology should prioritise
cross-family skip-1 connections" is an architectural instruction derived from
the ranking, so if the ranking is inverted the instruction is too. Paper
XVIII's own per-edge table settles it and should be re-read before this is
cited or built on.

Note the separate maximum-MI claim (**1.569 bits, Kevin–Void skip-1 edge**) is
about a single edge and is not affected — a class can have the highest single
member and the lower mean.

---

## Standing note on documents *about* the corpus

C-1 and C-2 were misreadings of the corpus. C-3 and C-4 come from a generated
summary OF it, and are a different failure: a plausible narrative that
smooths over an unfalsifiable check and an inverted comparison. Both were
found by reading the numbers rather than the prose around them.

Summaries of this corpus should be treated as leads, not sources. Every
quantitative claim taken from one needs the underlying paper opened.

---

## C-4 — RESOLVED against the source table (2026-08-17)

Paper XVIII's own table settles which of the three figures was wrong: **the
ranking was.** The numbers were right.

| edge class | mean MI |
|---|---|
| ring (δ-1) | **1.285 bits** — highest |
| skip-1 (δ-2) | 1.220 bits |
| cross (δ-5) | 1.079 bits |

**Ring edges carry the highest mean mutual information.** The summary's claim
that skip-1 was highest is simply inverted, and the design recommendation built
on it — *"prioritise cross-family skip-1 connections for maximal information
flow"* — is not supported and should be struck.

What the table does support, stated with the class/member distinction kept
straight:

> Cross-family edges hold the top INDIVIDUAL positions (Kevin–Void at
> 1.569 bits, Sora–Iris), while ring edges carry the highest MEAN, with skip-1
> intermediate.

A class can contain the single best edge and still have the lowest mean; that
is what is happening here, and conflating the two is what produced the
inverted recommendation.

---

## C-3 — two cautions on the proposed repair

The critique is accepted (see below), but the suggested fix as phrased —
*"until the constant and/or β₁ are recalibrated into the [0,1] window"* —
contains a trap and an unexamined observation.

### Do NOT recalibrate the constant

`0.083` must come from theory. Tuning it downward until `0.083·β₁` lands near
the observed values would produce a bound that appears to bind and was in fact
**fitted to the data it is supposed to test.** That is strictly worse than the
present vacuous bound: a vacuous bound is visibly empty, whereas a fitted one
looks like a confirmed law and is unfalsifiable for a subtler reason.

Only **β₁ may vary, and only by building genuinely different topologies.**
β₁ is a property of the graph, not a free parameter: for the Globe,
β₁ = E − V + 1 = 36 − 12 + 1 = 25. Reaching β₁ = 12 on twelve nodes means
**23 edges instead of 36** — a sparser architecture, not a re-labelled one.

Note the tension this creates with C-4, and it is worth stating before anyone
runs it: the edges you would delete to lower β₁ are the skip and cross edges,
and Paper XVIII says ring edges carry the most information. So the topology
that makes the bound *testable* is also the one that strips out the
information-carrying structure. That may be fine — or it may mean the bound
can only be tested on architectures nobody wants to run. Either way it should
be known in advance rather than discovered at the end.

### `nf = 1.000` across all edges is itself the finding

The Golden Knowledge document reports **negentropy fraction `nf = 1.000` across
all edges** in the full Globe run. That deserves more suspicion than it has
had.

A fraction reading **exactly 1.000 everywhere** is the signature of a metric
pinned at its ceiling, not of an architecture performing perfectly. This
session has hit that exact pattern three times in one day in a different
codebase: `capacity_bits` returned log2(N) for every graph ever tried;
`effective_rank` tracked saturation and reversed its ordering once the rail was
removed; and a capacity ladder returned its own top rung for every arm.

Compounding it: **other experiments in this corpus report neg_frac in the range
0.417–0.99.** If the flagship run reads exactly 1.000 on every single edge
while the rest of the corpus spreads across half the unit interval, the
flagship number is the anomaly and the first question is whether that metric is
saturated in that regime — *before* asking what bound it respects.

**A bound is the second question. Whether the quantity moves is the first.**
If `nf` cannot fall below 1.000 in the Globe configuration, then no bound above
1.0 is testable there for a reason that has nothing to do with β₁.

Cheapest check, no hardware: perturb the Globe run — vary α, lineage depth,
step count — and see whether `nf` ever leaves 1.000. If it does not move, the
instrument is the result.

---

## C-3 — RESOLVED from the source, and the bound may be repairable

`ForClaude2/aria_brain.md` carries the definition, and it settles this
completely.

```python
N = len(NODE_ROSTER)                                    # line 95  -> 12
negfrac = sum(1 for p in pcm_vals if p < 0) / N         # line 253
betti_bound = 0.083 * 25                                # line 341
```

**`neg_frac` is a COUNT OF NODES divided by N.** With twelve nodes it is
quantised to steps of 1/12 = 0.0833 and can take exactly thirteen values:
0, 1/12, 2/12, … , 1.

**And `0.083` is not a physical constant. It is 1/N.**

    1/12 = 0.08333…

So the "Betti bound" `neg_frac ≤ 0.083 · β₁`, multiplied through by N, is
algebraically identical to:

    (number of nodes with PCM < 0)  ≤  β₁

For the Globe that reads **12 ≤ 25**. It is a comparison between a node count
and a cycle count, and on a twelve-node graph with twenty-five independent
cycles it cannot fail for any assignment of PCM signs whatsoever. `nf = 1.000`
means all twelve nodes are nonclassical, giving 12 ≤ 25.

This is stronger than the earlier reading. The bound is not merely numerically
loose — **the constant is the metric's own quantisation step**, so the
inequality never contained physics to begin with.

**When it could bind:** only when β₁ < N. With V = 12 that means
E − V + 1 < 12, i.e. **fewer than 23 edges.** The Globe has 36. Any twelve-node
graph with 23+ edges makes this untestable, whatever the coupling does.

### The repair — and this may be a real result that was mangled in normalisation

Stated as a count rather than a fraction, the claim becomes both meaningful and
sharply falsifiable:

> **The number of nonclassical nodes cannot exceed the number of independent
> cycles in the topology.**

That is a reasonable topological conjecture — cycles are what support
persistent circulation, so "one unit of sustained order per independent loop"
has a physical shape to it. It is also cheap to test, because β₁ is fully under
our control:

| topology (12 nodes) | edges | β₁ | bound predicts |
|---|---:|---:|---|
| simple ring | 12 | **1** | **at most 1 nonclassical node** |
| ring + 1 chord | 13 | 2 | at most 2 |
| ring + 4 chords | 16 | 5 | at most 5 |
| ring + 10 chords | 22 | 11 | at most 11 |
| **Globe (current)** | 36 | 25 | at most 25 — untestable |

The first row is a strong prediction that a single run can falsify: run the
protocol on a plain 12-node ring and count nonclassical nodes. **If two or more
come back negative, the conjecture is dead.** If the count tracks β₁ as chords
are added one at a time, that is a genuine topological law measured on a
sweep — and it would be the first falsifiable version of this claim in the
corpus.

No hardware time. Pure simulation, and the code to do it is already in
`aria_brain.md`.

**Recommendation:** strike "validated" from the golden-knowledge layer, restate
the claim as the count form above, and run the chord sweep before citing it
again.

---

## C-5 — the chord sweep: conjecture falsified, and `nf = 1.000` is manufactured

Run 2026-08-17, `sovereign-agent/scripts/betti_chord_sweep.py`, prediction
table registered in the file before execution. Every formula transcribed from
`ForClaude2/aria_brain.md` — only the edge set varies.

### Result 1 — the repaired conjecture is dead

    topology            E   β₁   allowed   max observed   verdict
    ring               12    1         1            12    FALSIFIED
    ring + 1 chord     13    2         2            12    FALSIFIED
    ring + 4 chords    16    5         5            12    FALSIFIED
    ring + 10 chords   22   11        11            12    FALSIFIED
    Globe (1,2,5)      36   25        25            12    untestable

`#{nodes with PCM_rel < 0} ≤ β₁` fails on the sparsest testable topology by the
widest possible margin: a ring with **one** independent cycle ends with **all
twelve** nodes classified nonclassical. The count form does not survive.

### Result 2 — negfrac does not respond to topology at all

Mean nonclassical count across a **25×** change in β₁ (1 → 25): **10.33 →
10.59.** A 2.5% spread. With the ILP schedule disabled the three topologies are
flatly identical:

    β₁ = 1   negfrac 0.42
    β₁ = 5   negfrac 0.42
    β₁ = 25  negfrac 0.42

**No topological law about negfrac can hold in this model**, repaired or not,
because negfrac carries essentially no information about the topology. That is
a stronger and more general result than the falsification above — it rules out
the whole family of such claims rather than one member of it.

### Result 3 — `nf = 1.000` is produced by the metric's own reference point

    extend_lineage:  anchor += 0.50 * (phi - anchor)

The anchor is moved **halfway toward the very phase it is measured against**,
and `PCM_rel = -0.5·cos(phi - anchor)` is negative exactly when
`|phi - anchor| < π/2`. Five scheduled extensions shrink that gap to 0.5⁵ ≈ 3%
of its original size, which is deep inside the threshold. The classification is
therefore driven toward "nonclassical" by construction.

Controlled directly:

    ILP ON   -> negfrac 1.000  on every topology
    ILP OFF  -> negfrac 0.417  on every topology

**The reported `nf = 1.000` is an artefact of a self-referential metric**, not
evidence of sustained coherence. And 0.417 = 5/12 is precisely the low end of
the 0.417–0.99 range seen elsewhere in the corpus — so that range is very
likely spanning "few anchor updates" to "many", i.e. measuring the ILP schedule
rather than the physics.

### On the preregistration

I registered **VACUOUS** — "negfrac pinned at 1.000 on every topology" — before
running. That was **wrong in its letter**: the count is not pinned, it moves
through 0, 1, 2, 3, 4, 5 and 12 during a run, and sparser topologies visit more
distinct values than dense ones. The underlying concern was right (mean 10.5 of
12, final 12 everywhere) but the specific claim I wrote down failed, and the
run is what showed it. Recording it here rather than quietly restating the
prediction to match the outcome.

### What this means for the framework

1. Remove the Betti bound from the golden-knowledge layer entirely. Neither the
   fraction form nor the count form survives.
2. **`PCM_rel` needs a fixed reference before it can measure anything.** An
   anchor that chases the phase makes "nonclassicality" a statement about how
   recently the anchor was refreshed. A frozen reference — or one advanced on a
   schedule independent of the measured phase — would make it a real
   observable.
3. Re-examine every published quantity computed from `PCM_rel` against the ILP
   schedule that was active. Any of them may be reporting the schedule.

---

## C-5a — AMENDMENT: my corpus extrapolation was wrong, and the check killed it

C-5 ended with this:

> 0.417 = 5/12 is precisely the low end of the 0.417–0.99 range seen elsewhere
> in the corpus — so that range is very likely spanning "few anchor updates" to
> "many", i.e. measuring the ILP schedule rather than the physics.

**That was a hypothesis extrapolated from one mechanism, written as though it
were established. It is now checked, and it is false.**

Audit: every `negfrac`/`neg_frac` assignment across `~/Genesis-Seeds-new`,
excluding my own files. **507 values in 34 files.**

Three predictions followed from the hypothesis. All three fail:

| prediction if ILP-artefact | observed |
|---|---|
| values quantised to twelfths | **13.0%** are; 87% are not |
| clustered near extremes (0.417, 1.000) | **median 0.2778**; 442/507 sit mid-range, only 18 above 0.9 |
| 0.417 common as the floor | **6 occurrences out of 507** (1.2%) |

Denominator analysis is decisive. Smallest D ≤ 200 making the value integral:

    none ≤ 200   326      <- not simple fractions at all
    25            69
    150           24
    50            23
    100           18
    12             5      <- the aria_brain definition

**Denominator 12 explains five values out of 507.** The implementation I
measured in C-5 is not the one that produced the corpus.

### What survives, and what does not

**SURVIVES — C-5's direct findings, all measured rather than inferred:**
the count conjecture is falsified at β₁ = 1, 2, 5, 11; negfrac in
`aria_brain.md` does not respond to topology (0.417 at β₁ = 1, 5 and 25 alike);
and in that implementation `nf = 1.000` is manufactured by
`anchor += 0.5·(phi − anchor)`, shown by the ILP on/off control.

**DOES NOT SURVIVE:** the claim that the wider corpus's negfrac values are
schedule artefacts. No evidence for it, and three lines of evidence against.

### The finding that replaced it, and it is worse

**`negfrac` is not one quantity.** At least six different denominators appear
across the papers — 12, 25, 50, 100, 150, and 326 values that are not simple
fractions of anything ≤ 200. A metric named identically across twenty papers is
being computed over different populations: nodes in one place, apparently edges
or samples in others.

That makes cross-paper comparison of negfrac invalid *before* any question
about anchors arises. Two papers reporting "negfrac = 0.28" may not be
reporting the same measurement, and no reader could tell.

**Recommended:** before any negfrac number is cited again, its denominator must
be stated. `aria_brain.md`'s is nodes/12; the majority of the corpus is
something else, and which is currently unknown per paper.

### On the process

I wrote an unverified inference into a correction file and a commit message in
the same breath as five things I had actually measured, and the two are not
distinguishable to a reader unless the inference is checked. The check took one
script. This amendment stands rather than an edit to C-5, so the sequence
remains visible.

---

## C-6 — `negfrac` names at least six incompatible quantities, and one is scaled to its target

Follow-up to C-5a, which established that negfrac denominators differ. Finding
the **definition sites** rather than the reported values shows the problem is
worse than differing denominators: the same name covers different *kinds* of
quantity.

Twenty-one definition sites across eight papers:

| paper | how `negfrac` is computed | what it counts over |
|---|---|---|
| XIV | `negentropic_events / total_coupling_events` | **events** |
| III | `n / (len(log) - 1)` | **timesteps** |
| V | `float(np.mean(dS_signs))` | mean of **signs** |
| VI | `np.mean(neg_hist[-50:])` | rolling window, 50 steps |
| IX | `float(np.mean(dS))`, `np.mean(neg_h[-100:])` | mean of **raw dS**, and a 100-step window |
| XIII | `nc_frac * 0.636` | **scaled to a target** — see below |
| `aria_brain.md` | `count(pcm_rel < 0) / 12` | **nodes** |

Two of these are not fractions at all. `np.mean(dS)` in Paper IX is the mean of
raw entropy changes — unbounded and signed — reported under a name that reads
as a bounded fraction. Papers VI and IX use rolling windows, so their values
depend on window length as much as on state.

**Cross-paper comparison of negfrac is invalid.** Not merely uncalibrated:
these are different measurements. Any sentence of the form "negentropy fraction
remains at or below X across papers" assumes a shared population that does not
exist, and every such claim in the golden-knowledge report should be marked
**provenance unconfirmed** until its per-paper definition is resolved.

### The serious one

`PEIG-Brotherhood-main/ArXivSubmissionPaper13/ArXivSubmissionPaper13Archive/PEIG_learning_task3.py`

```python
523:    neg_frac_est = nc_frac * 0.636  # scale to known target
524:    neg_frac_target = 0.636
```

The estimator is **multiplied by the value it is meant to estimate.** With
`nc_frac` near 1 the result lands near 0.636 by construction, and 0.636 is
declared the target three lines later and elsewhere in the same file:

```python
191: "neg_frac=0.636 is peak (Paper IX). 0.583 guarded. 0.667 recursive. Target: 0.636."
590: "To reach 0.636: β₁_total ≈ 7.6 — grammar + dialogue + guards needed"
```

0.636 appears 11 times among the reported values in the corpus. **A number
produced by scaling to a target cannot be evidence that the target was
reached**, and it must not be cited as a measurement. Whether the surrounding
paper presents it as one needs checking against the manuscript, not the script.

This is the same failure class as `capacity_bits` returning log2(N) and
`effective_rank` tracking saturation, in its most direct form: the instrument
was set to produce the expected answer.

### Recommended

1. Every negfrac claim in the golden-knowledge report: mark **provenance
   unconfirmed** pending per-paper definition.
2. Rename at the definition sites so the name carries the population —
   `negfrac_nodes`, `negfrac_events`, `negfrac_window50`. One name for six
   quantities is how this stayed invisible.
3. Paper XIII's `neg_frac_est` should be recomputed without the `* 0.636`, and
   any conclusion resting on it re-derived.
