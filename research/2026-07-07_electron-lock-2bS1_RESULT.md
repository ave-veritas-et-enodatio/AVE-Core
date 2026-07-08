# RESULT — Electron-lock 2b-Stage-1: the BINDING test (parallel coupling-mode sweep)

**Date:** 2026-07-07 · **Lane:** implementer · **Branch:** `analysis/electron-lock-2bS1-fill`
(throwaway worktree off `origin/analysis/electron-equivalent-circuit`, #569 ref `5a7c78cc`).
**Prereg (FROZEN, governs this result):** [`research/2026-07-07_electron-lock-2bS1_prereg_FROZEN.md`](2026-07-07_electron-lock-2bS1_prereg_FROZEN.md)
— freeze commit `977a1bd9`, **precedes** the harness/run commits (freeze-before-results).
**Harness:** `src/ave/solvers/electron_lock_2bS1.py` · **Driver:** `src/scripts/verify/electron_lock_2bS1.py`
· **Tests:** `src/tests/test_electron_lock_2bS1.py` (20 passed) · **JSON:** `…/electron_lock_2bS1_results.json`.

---

## §0 — HEADLINE: the "3" FILLS, but every arm DECAYS. The reactive-fill candidate is DEAD; the "3" needs a NON-reactive mechanism.

> **All three coupling arms POPULATE the empty capacitive "3" (q-tank) from the
> ringing inductive "2" (d-tank) at ZERO drive — a real forward step past
> genesis-23 (`max|V_inc|=0`) and genesis-24 (pump-only). But NONE self-sustains:
> the populated q-energy BEATS BACK OUT (reactive borrow/return), never locking
> into a held (2,3) partition. NEITHER inductive arm routes `[FILLS-AND-SUSTAINS]`.**
>
> **Per the frozen §8 adjudication: NEITHER → the reactive-pump candidate is DEAD.
> The "3" needs a non-reactive mechanism.** This is the cheap, important NEGATIVE
> the prereg anticipated — the gap says *no* to us too, cleanly, at the most
> favorable (lossless, tuned, zero-drive) reduced-order operating point.

**Per-arm routed bins (VERBATIM, at the (2,3) tuning `ω_q/ω_d=3/2`, zero drive):**

| arm | **bin** | fill max / mean / min | H-drift | lock-drift | winding (w_d,w_q) | q-cap reconcile |
|---|---|---|---|---|---|---|
| `mutual_M` (bilinear; A1 slow-bias) | **`[FILLS-BUT-DECAYS]`** | 0.068 / 0.029 / **0.000** | 3.0e-6 | 19.2 | (237, 358) ≈ (2,3) | PASS (can-fire proven) |
| `co_equal` (symmetric nonlinear) | **`[FILLS-BUT-DECAYS]`** | 0.109 / 0.047 / **0.000** | 3.2e-6 | 39.8 | (236, 356) ≈ (2,3) | PASS (can-fire proven) |
| `coupling_varactor` (bridging cap, CONTROL) | **`[FILLS-BUT-DECAYS]`** | 0.132 / 0.060 / **0.006** | 5.1e-6 | 782.3 | (249, 248) → 1:1 | PASS (can-fire proven) |

The load-bearing column is **fill_min** (back-half minimum): every arm's q-tank
returns below the `SUSTAIN_THRESH = 0.01` at some point in the back half — it
empties each beat. `fill_max` clears `FILL_THRESH = 0.05` for all three (the "3"
genuinely populates), but the partition is **not held**.

## §1 — The hierarchy fork ADJUDICATION (§9 fork; the substrate decided, not a fiat)

The prereg §8 routes:
- `mutual_M` sustains ∧ `co_equal` not → **bias-hierarchy real** — **NO** (mutual_M does not sustain).
- `co_equal` sustains ∧ `mutual_M` not → **two-mode resonance** — **NO** (co_equal does not sustain).
- both sustain → both work — **NO**.
- **NEITHER sustains → the reactive-pump candidate is DEAD; the "3" needs a
  non-reactive mechanism** — **YES. This is the routed verdict.**

**So the §9 hierarchy fork is not resolved in favor of either sub-picture — it is
DISSOLVED at a level above it:** neither the slow-bias/fast-signal coupling nor the
co-equal two-mode coupling produces a persistent (2,3) partition, because *no
conservative reactive coupling can* (§2). The bias-vs-co-equal question is moot for
the fill: both are reactive, and reactive-at-zero-drive means beating, not binding.

There is a **weak, consistent selectivity signal** (not load-bearing, reported for
completeness): the (2,3) config fills slightly MORE than its golden-ratio control
in both inductive arms (mutual_M 0.068 vs 0.056; co_equal 0.109 vs 0.089), and the
resonant combination `ψ=3θ_d−2θ_q` is bounded at (2,3) but drifts at golden. But
since neither *sustains*, there is no held state for the coprimality to select —
the selectivity question is downstream of a fill that does not lock.

## §2 — THE MECHANISM (named, single, explains all failures): lossless ⇒ beating ⇒ no remanence

The result is not a tuning accident — it is forced by the anhysteretic kernel:

- **The harness is Hamiltonian by construction.** Every coupling derives from a
  coupling energy `E_c`, so `Ĥ = ê_d+ê_q+ê_c` is conserved. Measured **H-drift is
  3–5×10⁻⁶** across all arms (the canonical derivation is exact; the RK4 ledger is
  a pure numerical diagnostic, not a physics leak). So there is **zero dissipation**
  — the cleanest possible test of the doctrine.
- **In a lossless two-tank system at zero drive, "self-sustain" ≠ "energy
  persists".** Total energy is conserved, so *everything* persists trivially. The
  operative mass-analogue (prereg §9, surfaced to Grant BEFORE the freeze) is
  **partition persistence**: a *held* nonzero q-share. A conservative reactive
  coupling produces **beating** — energy sloshes d→q→d periodically (the q-tank
  empties every beat, `fill_min→0`). Even the resonant 1:1 case (fill_max = **1.005**,
  full Rabi transfer) beats fully back (`fill_min = 0`). Beating is reactive
  storage, **not** a bound partition.
- **This IS the loop-gap doctrine, demonstrated at zero drive:** *"the kernel
  `S=√(1−A²)` is anhysteretic — zero enclosed loop area — so reactive storage
  under drive is not mass; mass requires zero-drive persistence (ferrite `B_r` at
  `H=0`)."* A conservative circuit has **no `B_r`**: with zero loop area there is no
  remanence to hold the q-partition. The "3" is filled and then structurally *must*
  be given back. **One mechanism — the absence of a lossless-forbidden remanence —
  explains all three arms and all five prior failures.**

This directly **answers the pre-test-physics question** surfaced to Grant (prereg
§9): partition-persistence is *structurally impossible* in a lossless tank. The
equivalent-circuit (reactive) register can therefore route `[FILLS-BUT-DECAYS]` at
best — never `[FILLS-AND-SUSTAINS]` — and the real mass-lock requires the **Level-2
`τ_relax` memristive (dissipative) kernel** (doctrine §6, rank-4 constitutive
remanence), which is **out of the reactive-circuit scope by construction.** The
substrate confirmed the hypothesis embedded in the question.

## §3 — Firewall, double-count landmine, scale-invariance (the discipline that rode every arm)

- **FIREWALL (prereg §4) — CLEAN.** `firewall_scan()` AST-extracts the outcome
  functions (`_derivs, _energies, _e_couple, run_arm, classify, S`) and finds **no
  `ALPHA`/`M_E`/`m_e` NAME token** on the FILL/SUSTAIN/SELECT path. Component values
  (`L_cell, C_cell, Z₀, I_max, V_snap, V_yield`) enter only as consistency-class
  scale anchors.
- **Scale-invariance control — PASSES.** The (2,3) bin is **identical** at the
  datasheet `v̂_yield ≈ 0.931` and at `2×v̂_yield` for both inductive arms
  (`FILLS-BUT-DECAYS` → `FILLS-BUT-DECAYS`). The α-echo *magnitude* in
  `V_yield = √α·V_snap` does **not** reach the verdict.
- **DOUBLE-COUNT LANDMINE (prereg §5) — HANDLED, arms NOT double-count-suspect.**
  `mutual_M`/`co_equal` couple through the **inductive flux channel** (`E_c` in the
  currents), **orthogonal** to the q-tank's Op14 collapse cap `C_q(v_q)`. **No
  `∝V_inc` EMF term is added** (that is the exact term that double-counts `C_eff`,
  `k4_cosserat_coupling.py:223` `use_lagrangian_emf_coupling=False`). The q-cap
  collapse energy in the fill metric **reconciles (rtol 1e-3, can-fire proven)**
  against an independent numerical quadrature of `∫v'·C_q(v')dv'` depending on
  `v_q` **alone** — the Op14 varactor is carried **once**. Reconcile PASS for all
  three arms.

## §4 — Controls: every bin is REACHABLE (no dead plumbing) + the tautology detector fires

The negative is informative only if the other bins are attainable — proven:

- **`[DOESN'T-FILL]` reachable:** uncoupled (`κ=0`) → `fill_max = 0.000` →
  `DOESN'T-FILL`. (The fill metric is not spuriously nonzero.)
- **`[FILLS-AND-SUSTAINS]` reachable:** a synthetic locked-partition result routes
  `FILLS-AND-SUSTAINS` — the classifier branch is **live plumbing**, so *"no
  physical arm reaches it"* is an informative negative, not a dead branch. (No
  physical *conservative autonomous* config attains it — §2 explains why.)
- **`[TAUTOLOGY]` detector CAN-FIRE:** a **strong** bridging cap co-keys the tanks
  and correctly routes `TAUTOLOGY` — `c_frac=2.0` (`div_corr=0.91`) and `c_frac=6.0`
  (`div_corr=0.96`) → `TAUTOLOGY`. The **frozen** `coupling_varactor` control
  (`c_frac=0.30`, `div_corr=0.85`) sits **honestly sub-threshold** and routes
  `FILLS-BUT-DECAYS` — its co-keying is diagnostically visible (drags both 3:2 and
  golden to a 1:1 winding `w=(249,248)`, `div_corr=0.85` vs 0.02–0.05 for the
  galvanically-separate inductive arms) but it does **not** manufacture a spurious
  sustain, so there is no false win to reject. **The threshold was NOT lowered to
  force the varactor into `[TAUTOLOGY]`** (flag-don't-fix; Rule 11).

## §5 — Robustness (prereg §7) — the core verdict is fully robust; one qualified sub-verdict

Under the frozen nudges (`κ×{0.7,1.4}`, `seed∈{0.2,0.4}`):
- **`co_equal`:** `FILLS-BUT-DECAYS` at **every** nudge — robust.
- **`mutual_M`:** `FILLS-BUT-DECAYS` at `κ×1.4`, `seed=0.2`, `seed=0.4`; but
  **`DOESN'T-FILL` at `κ×0.7`** — mutual_M sits near the `FILL_THRESH` and drops
  below it at weaker coupling. **Qualified sub-verdict (reported, not headlined):**
  the *fill vs no-fill* boundary is coupling-sensitive for the bilinear arm.
- **The load-bearing verdict — NEITHER arm SELF-SUSTAINS — is invariant across
  EVERY nudge** (no nudge, in any arm, produces `fill_min ≥ SUSTAIN_THRESH`). The
  `DOESN'T-FILL ↔ FILLS-BUT-DECAYS` flip is *below* the sustain question and does
  not touch the §8 route.

## §6 — consistency-vs-emergence classification

- The component VALUES are **consistency-class** (datasheet imports; §3 firewall).
- The FILL (a real q-population, monotone-ish in coupling) is a **manifestation**:
  a reactive-exchange amplitude, supplied by the coupling — not a new emergent number.
- The emergence-scoped output (a *held* de-novo (2,3) partition = zero-drive
  persistence) is **BLOCKED** — it does not close in any arm. **No emergence-class
  claim is made.** The headline is honestly a **negative + a named mechanism**, not
  a genesis.

## §7 — Honest closure (Rule 11) + scope (Rule 12 / substitution-not-retraction)

This is the discipline working at full strength: a pre-registered make-or-break
prediction returned a **clean negative**, a **single mechanism** (lossless ⇒
beating ⇒ no remanence) explains all three arms and all five prior failures, and
the branch is closed. **No debug-toward-a-rescue** (the varactor threshold was not
softened; the sustain criterion was not dropped). The reactive-fill hypothesis is
**falsified for self-sustain**; per Rule 12 the slot is **not refilled** with a new
unverified mechanism — the successor (the Level-2 `τ_relax` dissipative-remanence
kernel) is a **new hypothesis with its own version number and verification chain**,
surfaced for Grant, **not drafted here**.

**Scope boundaries (stated plainly):**
1. **FILLING/BINDING, not selection.** Tanks were TUNED to (2,3); whether (2,3) is
   *selected over 1:1* remains the deferred topological question (Stage-1
   `[DOMINATED]`). This result does not touch it.
2. **Reduced-order equivalent-circuit, not the 3D lattice.** A negative at the most
   favorable reduced operating point (lossless, tuned, zero-drive) is *informative*:
   if the equivalent circuit cannot bind, a reactive lattice channel is unlikely to.
   But the lattice retains channels the lumped model omits (bulk-Γ confinement
   geometry, the real Op14 spatial structure); a Stage-2 lattice run with the
   dissipative-remanence kernel is the honest successor, not a claim that "the
   electron cannot exist."
3. **The negative is about the MECHANISM (conservative reactive fill), not the
   electron.** Mass = zero-drive persistence still stands as the target; this run
   shows the *reactive circuit* is the wrong instrument to demonstrate it.

## §8 — DERIVED / VERIFIED / BLOCKED

**DERIVED (this run):**
- The empty capacitive "3" **does populate** from a pure inductive d-seed at zero
  drive, in all three arms (`fill_max` 0.068 / 0.109 / 0.132) — past genesis-23/24.
- **No conservative reactive coupling holds the partition** — `fill_min → 0` every
  arm, every nudge. Mechanism: anhysteretic kernel ⇒ zero loop area ⇒ no remanence.
- The bilinear `mutual_M` is a 1:1-resonant coupler (full Rabi at 1:1, weak
  off-resonant beating at 3:2); the cubic `co_equal` fills ~1.6× more but still beats.

**VERIFIED (verify-before-cite, this session):**
- doctrine §1/§6 (anhysteretic; reactive storage ≠ mass; `τ_relax`): `loop-gap-electron-resonator-closure-doctrine.md:18,79`. ✓
- genesis-23 GAP-1 (`max|V_inc|=0`): `research/2026-06-09_reflection-genesis-23-self-assembly_result.md`. ✓
- genesis-24 pump-not-lock + the Op14 double-count off-by-default: `research/2026-06-09_genesis-24-saturated-seed_result.md`; `k4_cosserat_coupling.py:223`. ✓
- the #569 circuit + §5 double-count flag: `research/2026-07-07_electron-equivalent-circuit.md`. ✓
- kernel `S(A)=√(1−A²)`: `ave.axioms.scale_invariant.saturation_factor`; `I_max = XI_TOPO·C_0`: `fdtd_3d.I_MAX_MU`. ✓

**BLOCKED / NOT CLAIMED:**
- A held de-novo (2,3) partition (zero-drive persistence) — BLOCKED in every arm.
- Any selection-over-1:1, α, or `m_e` claim — out of scope / firewalled.

## §9 — Skills fired

`substrate-native-check` (K4/Cosserat/Op14/phase-space walk before the ODEs;
saturating `L/S`, collapse `C·S` load-bearing) · `pre-test-physics-check` (the
lossless-tank persistence question surfaced to Grant BEFORE the freeze; §2 confirms
it) · `phase-space-coordinate-check` (A46 — winding + `ψ=3θ_d−2θ_q` measured in the
(V,I) phase plane, matching coordinates) · `consistency-vs-emergence` (values
consistency; fill manifestation; held-(2,3) emergence — BLOCKED) · `verify-before-cite`
(every cite greped/opened) · `flag-don't-fix` (varactor threshold NOT softened; the
mutual_M robustness flip surfaced, not smoothed) · `ave-conserved-vs-pumped` (H-drift
ledger; the reactive fill is conservative-beating, distinguished from a pump).

## §10 — Reproduce

```bash
PYTHONPATH=src python src/scripts/verify/electron_lock_2bS1.py   # JSON + house-WHITE figure + verdict
PYTHONPATH=src pytest src/tests/test_electron_lock_2bS1.py -q     # 20 passed (standing falsifiers)
```

**Figure** (house-WHITE): `src/scripts/verify/electron_lock_2bS1_fill.png` — LEFT:
rolling min/max q-fill envelope per arm (the min-envelope hugs zero = the tank
empties every beat); RIGHT: `fill_max`/`⟨·⟩`/`min` bars vs the FILL and SUSTAIN
thresholds (fills clear the FILL line; back-half minima sit at the SUSTAIN floor).

**Canonical cross-refs:** `research/2026-07-07_electron-equivalent-circuit.md` (#569,
the circuit) · `research/2026-07-07_electron-lock-2bS1_prereg_FROZEN.md` (freeze
`977a1bd9`) · `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md`
(the mechanism) · `research/2026-06-09_reflection-genesis-23-self-assembly_result.md`
+ `research/2026-06-09_genesis-24-saturated-seed_result.md` (the 5 prior failures).
