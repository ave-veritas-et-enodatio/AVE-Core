# RESULT — Cleave registry-pump Chern: sliding vs locked

**Date:** 2026-07-02
**Lane:** implementer (dual-reading Chern driver — run complete)
**Branch:** `analysis/cleave-coupling-chern-adjudication` (off main `f556dcdc`)
**FROZEN prereg:** `research/2026-07-02_cleave-registry-pump-chern_prereg.md`
**Receipts:** `research/2026-07-02_cleave-coupling-derivation_adjudication.md`
**Driver:** `src/scripts/vol_4_engineering/cleave_registry_pump_chern.py`
**Tests:** `src/tests/test_cleave_registry_pump_chern.py`
**Class:** adjudication / consistency-class. Solidity: **NULL-DERIVED for the operator-derived
construction** (see §5 scope caveat — this is a construction-specific negative, honestly bounded).

> **Headline.** Both substrate readings give **C = 0** (gapped + converged), the toy validate-on-known
> gate PASSES, and the enantiomorph-odd guard is satisfied. **VERDICT BIN: NULL-DERIVED.** For the
> operator-derived srs screw-registry construction, the plate-displacement → topological-charge
> coupling is DEAD: `Q = ξ_topo·x` is a unit-bridge, not a derived pump. The scope caveat (§5) bounds
> what "NULL-DERIVED" licenses.

---

## 1. Validation gates (must pass before the verdict counts)

| gate | result | pass |
|---|---|---|
| **GATE-TOY** (validate-on-known, Rice-Mele/Thouless) | `pump_sign=+1 → C=−1.0000`, `pump_sign=−1 → C=+1.0000`; flips sign; `max_plaquette=0.072` (well-resolved) | **PASS** |
| **G-SLOPE** (frozen slopes from canonical constants) | `414.9 / 146.7 / 586.8 fC/µm`; ratios `2√2` (bench/full-cell), `√2` (quarter/bench) exact | **PASS** |
| **G-ANCHOR** (OA bulk g₀ = 2.21589 rad/z-unit) | srs-R bare pitch `2.22144` = **0.2505% off** (match=True); srs-L bare pitch `0.74048` (66.58% off — see §3) | **PASS (srs-R)** |
| **convergence** (band gapped + grid-stable per reading) | all four (reading × enantiomorph) gapped (min gap 2.0000 sliding, 0.0676 locked) and integer-stable under 2× grid | **PASS** |

The GATE-TOY pass is the load-bearing one: a Fukui-Hatsugai integrator that reads C=∓1 on a textbook
pump and flips sign with direction can be trusted to report C=0 as a real null, not a false null.

---

## 2. The srs (k_z, θ) registry-torus Chern — both readings

| reading | enantiomorph | C (raw) | C (int) | coarse-grid | min band gap | converged |
|---|---|---|---|---|---|---|
| **sliding**/Eulerian | srs-R | −0.0000 | **0** | 0 | 2.0000 | ✔ |
| sliding/Eulerian | srs-L | +0.0000 | **0** | 0 | 2.0000 | ✔ |
| **locked**/Lagrangian | srs-R | +0.0000 | **0** | 0 | 0.0676 | ✔ |
| locked/Lagrangian | srs-L | −0.0000 | **0** | 0 | 0.0676 | ✔ |

- **Sliding reading:** θ enters the band as a global U(1) phase that factors out of the
  eigenvectors (matter drags no substrate texture — the canonical-engine reading). The Berry
  curvature over `(k_z, θ)` is identically zero → **C_slide = 0** (the flat band, gap 2.0). This is
  what Angles B and C predicted for the canonical sliding engine.
- **Locked reading:** θ co-rotates the transverse frame *through the screw operator* (the finite-strain
  co-moving construction). The band is gapped (0.0676, nonzero → Chern well-defined) but the operator-
  derived winding does **not** enclose the gap point → **C_lock = 0** (converged, stable across
  n = 24/48/96, `max_plaquette = 0.632 < π` — well-resolved, not a grid artifact). This is a
  topologically **trivial** co-moving winding.

**Enantiomorph-odd guard:** both readings give C=0 for both enantiomorphs — consistent (a zero pump
is trivially enantiomorph-consistent). No same-sign-nonzero red flag arises.

---

## 3. Anchor cross-check (Grant's (b) canon-slot decider) — an honest subtlety surfaced

The frozen anchor is bulk g₀ = **∓2.21589 rad/lattice-z-unit** (srs-R/srs-L), an
enantiomorph-**odd** sign flip (`chiral-vector-tlm-phase1_result.md:23`). The driver recomputes it
two ways and surfaces a genuine subtlety:

- **Bare screw pitch** `(π/2)/(t_z·a_cell)`: srs-R (t_z=1/4) → **2.22144** (0.2505% off the anchor
  magnitude, match). srs-L (t_z=3/4) → **0.74048** (66.6% off). The bare-pitch formula shares the
  SAME 4-fold rotation R for both enantiomorphs and differs only through t_z, so it does NOT
  reproduce the published `±` enantiomorph sign-flip — it reproduces only the srs-R magnitude.
- **Signed handedness** (helix signed torsion): srs-R `+0.5223`, srs-L `+0.8329` — the writhe/torsion
  channel that carries R-vs-L handedness. This is the SIGNED channel; the corpus `±2.21589` sign-flip
  lives in the writhe-aware TLM operator (`chiral_vector_tlm_phase1.py`), not the bare-pitch formula.

**Consequence for the canon slot.** In the NULL-DERIVED outcome the anchor decider is moot (no
reading has C≠0 to earn the slot). But the anchor cross-check did its job: it confirmed the srs
ground state the pump ran on **is** the same object that carries the OA g₀ (srs-R reproduces the
anchor magnitude), so the C=0 pump is a null of the *right* texture, not a mis-configured one. **Flag
(links FLAG-1, §4 of the receipts):** the bare-pitch vs writhe-operator sign-channel split is the
same z-unit ↔ physical-length / sign-convention ambiguity called out at
`chiral-vector-tlm-phase1_result.md:105`; it remains **OPEN** (this run did not need to resolve it —
the null does not depend on the sign channel).

---

## 4. The frozen bin + the slope

**VERDICT BIN: NULL-DERIVED** (`C_slide = 0 ∧ C_lock = 0`, both gapped + converged, toy gate PASS,
enantiomorph-odd consistent). Per the frozen outcome bins (prereg §4):

> Coupling is **dead**. Cleave rescopes to an **Axiom-2 null-test** (still worth running as a
> falsifier — a nonzero floor would then falsify AVE). `Q = ξ_topo·x` is retired to unit-bridge
> status; the floor is not a derived pump.

**Slope (had C been nonzero):** the derived slope would have been `C × {146.7 (full cell) | 586.8
(quarter pitch)} fC/µm` — NOT the bench's 414.9, which needs a non-integer C = 2√2 (impossible for a
Chern pump; the pre-frozen G7 FAIL). With C=0 the slope question is moot: there is no integer-C pump.

---

## 5. Scope caveat (honest bound on what NULL-DERIVED licenses)

**This is a construction-specific negative, and I bound it precisely (Rule 11 honesty, not a
rescue):**

- The C=0 result is for the **operator-derived** srs screw-registry Bloch construction (§2): θ as the
  registry rotation advanced through the actual `find_screw_operator` transverse block. It shows that
  *this natural, substrate-native coupling* does not realize a nonzero-Chern pump. It does **not** prove
  C=0 for *every* conceivable locked coupling — a more elaborate multi-band srs eigenmode construction
  could in principle differ. What it does establish: **the simplest operator-faithful reading of the
  registry pump is topologically trivial in both substrate readings.**
- The **sliding** C=0 is stronger — it is structural (θ factors out as a gauge phase when matter drags
  no texture), matching the corpus sliding-engine reading (Angles B/C). The **locked** C=0 is the
  construction-specific one.
- **What would upgrade this:** a full N-band srs cage eigensolve (not the effective 2-band screw block)
  with the readout loop `∂Ω` swept through the genuine `compute_Q_link` / `compute_F_curl` field —
  i.e. compute `Link(∂Ω, F)` directly on an evolved srs ground state rather than through the effective
  Bloch model. That is the heavier follow-on; the effective-model null makes it lower-priority (the
  simplest faithful reading already returns 0), but it is the route if the locked channel is
  revisited. **Not claimed here; flagged as the open upgrade path.**

---

## 6. Corpus impact + what's gated

- **Cleave-01 coupling status:** "analytically derived" (`project-cleave-01.md:32`) is a unit-bridge,
  now with a run behind it: the registry-pump mechanism (the sole surviving candidate) returns C=0 in
  the faithful construction. The bench's chord (gap-independent integer FLOOR) is unaffected as a
  *falsification test* — but the NULL-DERIVED result means the bench is best framed as an **Axiom-2
  null-test** (a nonzero floor would falsify AVE), not a confirmation of a derived pump. Fallout
  inventory: `_orchestration/2026-07-02_cleave-coupling-fallout-scope.md`.
- **Gated:** the full N-band srs `Link(∂Ω, F)` follow-on (§5); the datasheet rewrite (KEEP-BOTH
  cross-ref now, full rewrite gated); the ξ_topo cascade dependents' coupling-vs-unit-bridge audit.
- **FLAG unresolved (surfaced, not fixed):** the bare-pitch vs writhe-operator sign-channel split (§3)
  = the `chiral-vector-tlm-phase1_result.md:105` `2√2` / sign-convention ambiguity, still OPEN.

---

## 7. Reproduce

```
PYTHONPATH=<worktree>/src <main>/.venv/bin/python \
  src/scripts/vol_4_engineering/cleave_registry_pump_chern.py
# tests (gating lane): pytest src/tests/test_cleave_registry_pump_chern.py -m "not engine_sim"
# tests (engine lane): make test-engine   (the torus Chern + gap-scan drivers)
```

All numbers in this doc are the driver's in-run output (n_grid = 48). `make verify` PASSED.
