# Coupled A1+winding EIGENSOLVE — RESULT: the confined mass+winding eigenmode DOES-NOT-EXIST; the ladder made physical

**Status:** **RESULT (committed).** Conservative-existence keystone run per the frozen pre-reg.
**Date:** 2026-06-24
**Pre-reg:** `research/2026-06-24_engine-coupled-eigensolve_prereg.md` (commit 54d605f8) — followed exactly.
**Module:** `src/ave/solvers/coupled_eigensolve.py` · **Test:** `src/tests/test_coupled_eigensolve.py` (8/8 pass).
**Class:** CONSISTENCY (existence + ladder clarification). NOT the α-free chord (that is the bench). Q=137 stays EMPTY. mass=A1 (PR#260) UNTOUCHED.
**Reuse (Rule 14):** `coupled_cage_winding._assemble_H()` (the S3 coupled Hermitian H) as the operator; `fork_b_saturation_tank` cluster/gap machinery + ARM-B as the gate; `_winding_host` κ̃=6/5 on the chord path.

---

## 0. HEADLINE

> **VERDICT: DOES-NOT-EXIST.** Eigensolving the COUPLED Hermitian generator H
> (A1 mass-block + b_ω winding-amplitude block + S(A)-front-gated coupling) at the
> saturated operating point, the most-bound eigenstate is a **confined, lossless,
> non-tautological A1 mass-cage** (gates a/b/c/e PASS) — **but the (2,3) winding is
> BLED OUT of it** (gate d FAILS): the b_ω amplitude co-localizes at the A1 stiff
> core (`bw_on_torus ≈ 0.0001`), NOT on the winding torus, and the bound mode does
> NOT carry the (2,3) winding integer. **No bound eigenstate carries BOTH the mass
> AND the charge-winding.** This is the **deeper negative** the pre-reg named as a
> possible BREAK (§1): the conservatively-coupled electron has no confined
> stationary state that is simultaneously mass and (2,3)-charge.

**Single-mechanism honest closure (Rule 11):** the b_ω block `ω_s·I − c²·L_D`
shares the **SAME** stiff-core stiffness `D = 1/S(A)` as the A1 block, so its OWN
most-bound state is a core breather co-localized with A1 — NOT a torus state. The
winding-carrying torus modes live UP in the continuum band, energetically UNBOUND.
One mechanism explains the whole failure. Retract-not-refill (the self-formation
slot stays barred; this was an eigenvalue existence problem, not a formation run).

**NOT inconclusive (resolution ruled out):** the SEEDED (2,3) winding reads (2,3)
exactly at this geometry (`Q_link=3, w_tor=2, raw=2.993`) at ~14.5 cells/turn
(≫ Nyquist 3–4). The winding IS resolved; its absence from the bound manifold is
physics, not a coarse-grid artifact. No bound-cluster member (12 scanned) carries it.

---

## 1. GATE TABLE (pre-reg §1 make-or-break + §6 HALT)

| Gate | Bar | Result | Outcome |
|------|-----|--------|---------|
| **HALT** winding-OFF recovers fork-b | core_frac≥0.50, lossless | `forkb_omega=2.839`, `a1_core_frac=0.995`, `Im(ω)=0`; near cold-cage ω_cutoff≈2.87 | **PASS** (instrument sound) |
| **(a) CONFINED** | core_frac≥0.50 | `a1_core_frac=0.995` | **PASS** |
| **(b) GAPPED+DISCRETE** | separated from continuum | bound level triply-degenerate at `w_H=−7.065`; next level at `−7.058`; band edge at `−4.59` (discrete Hermitian spectrum) | **PASS** |
| **(c) LOSSLESS** | Im(ω)≈0 | `Im(ω)=0` EXACTLY (H Hermitian → real spectrum; structural) | **PASS** |
| **(d) BOTH SECTORS PRESENT** | nonzero A1 mass AND (2,3) winding-charge ON the eigenstate | A1 present (`a1_frac=0.50`) but **winding BLED OUT**: `bw_on_torus=0.0001`, eigenstate winding integer `(−1,2) ≠ (3,2)` | **FAIL** |
| **(e) NON-TAUTOLOGICAL** | ARM-B scramble de-confines | `armB_core_frac: 0.995→0.000`, margin 0.995, histogram-preserved, NOT auto-void | **PASS** |

**EXISTS iff all five.** Four pass, **(d) fails ⇒ DOES-NOT-EXIST** (pre-reg §1
BREAK: the conservative coupling does not produce a confined mass+winding
stationary state — the winding de-localizes off the bound mode).

## 2. THE BOUND MODE

The most-bound eigenstate of the coupled H (winding ON, `rate=0.3`, resonant
`ω_b=ω_s=1`, N=32, canonical (2,3) torus R=7/r=2.3, wide A1 core a1_radius=6):

- **H-eigenvalue** `w_H = −7.065`, triply degenerate (the core breather's symmetry
  multiplicity); gap to the next level `0.0063`.
- **fork-b breathing frequency** `ω_bound = √((ω_b − w_H)/c²) = 2.840` (dimensionless,
  FORM) — sits right on the cold-cage ω_cutoff≈2.87 FORM anchor (`test_l3_mass_cage.py:18`).
- **sector split** `a1_frac = bw_frac = 0.500` — the resonant coupling hybridizes the
  A1 core breather 50/50 with a b_ω **core** breather.
- **localization** `a1_core_frac = 0.995` (deeply confined); BUT `bw_on_torus = 0.0001`
  — the b_ω amplitude is on the A1 core, essentially ZERO on the winding torus.
- **winding integer of the bound mode** `(Q_link, w_tor) = (−1, 2)`, raw `−0.86` —
  NOT the seeded (3,2)=(2,3) winding. (Read via the quadrature-invariant `|b_ω|·ê_w`
  winding-host map, so this is NOT an LC L-state quadrature-zero artifact.)

**The "coupled" bound mode is A1-mass + a core-localized b_ω amplitude — winding-
bled (the genesis-24 guard firing as a FAIL).** The bw_frac=0.50 is a RED HERRING
for gate (d): the b_ω *energy* is present, but it has collapsed onto the A1 core,
abandoning the (2,3) winding template. Gate (d) explicitly requires the winding to
be PRESENT (on the torus, carrying (2,3)), not merely nonzero b_ω norm — exactly
to catch this winding-bled mode.

## 3. THE V_yield / V_snap / m_e LADDER CLARIFICATION (the deliverable Grant asked for)

The eigensolve reads off TWO distinct operating amplitudes — and that two-amplitude
structure IS the ladder clarification:

| Quantity | Value | Class | What it is |
|----------|-------|-------|------------|
| **A\*** (A1 mass-cage core) | `0.991` (→1) | **FORM** | the strain `A=V/V_yield` where the A1 mass cage binds — the **V_snap CAP** |
| **A_front** (coupling shell) | `0.529` (≈4/7=R_II) | **FORM** | the strain where the S(A)-front coupling engages — near the **V_yield FLOOR** |
| **ω_bound** | `2.840` | **FORM** | the mode's dimensionless gap/clock (on the cold-cage 2.87 anchor) |

### 3a. FORM-vs-CALIBRATION map (pre-reg §3.3)

- `V_snap ≡ m_e c²/e` — **DEFINITIONAL calibration** (`constants.py:451`). This IS
  m_e in voltage units, not derived.
- `V_yield ≡ √α·V_snap` — the nonlinearity onset; the √α is the **imported ECHO**
  (`constants.py:460`).
- **the eigenmode binds at A\*≈1** — **FORM** (substrate-set): a stiff-core mass cage
  REQUIRES A→1 (deep saturation S→S_min ⇒ stiffness D=1/S→∞) to bind. The amplitude
  sweep confirms this is physics, not a seed artifact: ω_bound rises **monotonically**
  with A* (A*=0.5→ω=1.16; A*=0.85→1.33; A*=0.95→1.61; A*=0.99→2.06; A*=0.999→2.84),
  i.e. the mass cage binds across the whole ladder, and its clock is set by WHERE in
  the ladder it sits.

So "how V_yield and V_snap relate to m_e" = the dimensionful values ARE m_e (+α) by
**calibration**; what the eigensolve ADDS is the **physical place of the electron in
that ladder**: the MASS cage lives at the **A\*→1 (V_snap) cap**, the coupling FRONT
lives at the **A≈4/7=R_II (V_yield) floor**. The ladder is now a picture you read off
the spectrum, not two asserted voltages.

### 3b. Two-camps reconciliation (pre-reg §3.4)

The corpus carried two readings of where Γ=−1 forms: **V_yield** (electron-
identification.md:26) vs **V_snap** (pair-production §4). The empirical resolution
from A* + A_front: **they are NOT competing readings of one wall — they are TWO
walls.** The A1 **mass cage** is a **V_snap-cap** (A→1) object; the **coupling
front** (where the winding sector *would* engage) is a **V_yield-floor** (A≈R_II)
object. camp-1 names the coupling front; camp-2 names the mass cap. Both are real;
they describe different features of the saturation profile.

### 3c. HARD GUARD — coincidence-magnet discipline (pre-reg §3.1)

A\* lands nearest **unity** (= the V_snap cap). This is reported as a **FORM** result
and is NOT headlined as a chord: A*→1 is the EXPECTED stiff-core physics. A_front lands
on **4/7 = R_II** — but that is **by construction** (the front-gate center IS 4/7;
`coupled_cage_winding.front_gate`), so it is a tautology of the gate window, NOT an
emergent coincidence. **No suggestive value (√α, ½, ¾, 1) is claimed as a chord.**
The eigensolve does **NOT derive m_e / V_snap / V_yield** (`derives_m_e = False`);
those are calibration inputs. The chord-decider stays the α-free dimensionless ratio,
and that is the BENCH, not here.

## 4. SCALE-FREE CHECK (pre-reg §3.5)

Two protocols over the lattice ladder N∈{24,28,32,40}:

| N | ω_bound (self-similar core) | ω_bound (fixed core) |
|---|------|------|
| 24 | 2.734 | 2.840 |
| 28 | 2.787 | 2.840 |
| 32 | 2.840 | 2.840 |
| 40 | 2.942 | 2.840 |

- **SELF-SIMILAR core** (the fork-b scale proxy — core/box ratio fixed): ω_bound
  **DRIFTS** with N (rel. spread 7.3%), reproducing fork-b's scale-free precedent.
- **FIXED core** (box grows, physical core held): ω_bound is **N-INVARIANT** (spread 0.0).

**Reading (EXPECTED honest closure, NOT a failure):** the self-similar drift confirms
the dimensionful values are **m_e-calibration** — the FORM (the mode + A\*) is robust,
the SCALE floats with the geometry ⇒ **the irreducible m_e is the one input.** The
fixed-core invariance complements it: the mode is a genuine **LOCAL stiff-core
breather** (clock set by the local stiffness, not the box) — not a box artifact. This
is exactly the §3.5 "m_e is the one input" outcome; do not over-frame it as a negative.

## 5. α-CLEAN + GUARDS + REPRODUCE

### α-clean (operating principle, pre-reg §0)

The verdict path carries NO α-carrier. The chord-path winding factor routes through
`_winding_host.winding_kappa_tilde(2,3) = 6/5` (κ̃, α-free); the import-time guard
triad (`ALPHA`/`Q_TANK`/`ELECTRON`/`V_SNAP`/`KAPPA_CHIRAL_ELECTRON` absent) fails the
import if a carrier leaks. `V_snap`/`V_yield` appear ONLY as the §3 operating-point
calibration map (prose), never on a verdict read. The operator reads a dimensionless
`A=|a_A1|/V_yield`, so the α-carrying `V_yield` CANCELS structurally. (`test_t0`.)

### Guards walked

- **Self-formation refill (A47 v11b):** this is an eigenvalue EXISTENCE problem; we
  report EIGENPAIRS, never trajectories. The twice-falsified self-formation slot stays
  BARRED. The DOES-NOT-EXIST is retract-not-refill (no new hypothesis planted).
- **Tautological confinement:** ARM-B de-confines (gate e PASS) — confinement is
  S-structure-decided, not a projector artifact.
- **Winding-bled-into-A1 (genesis-24):** this is precisely the gate-(d) failure mode,
  and it FIRED — caught by requiring the winding ON the torus carrying (2,3), not mere
  nonzero b_ω norm.
- **m_e-circularity / derivation over-claim:** `derives_m_e=False`; §3 form-vs-
  calibration split holds; no chord claimed here.
- **Resolution / INCONCLUSIVE:** ruled out — the seeded winding reads (2,3) at ~14.5
  cells/turn; no bound-cluster member carries the winding.

### Honest flags (surfaced, not resolved)

1. **Operator-class note (consistent with S3, flagged for the auditor):** fork-b
   eigensolves a real graph Laplacian `Lψ=ω²ψ` on the native connect-map (diamond/srs);
   this module eigensolves the COUPLED complex Hermitian `H` on the Cartesian-periodic
   native-K4 N³ lattice (`build_grad_div_periodic` + `assemble_L_D`, the Stage-2 native
   stiffness). The HALT gate confirms the A1-block recovers the fork-b confined mode
   (core_frac=0.995, ω≈2.84 on the 2.87 anchor, lossless), so the two are consistent on
   the A1 sector. The two operators are NOT byte-identical (different stencil
   discretization); the HALT recovery is the cross-validation.
2. **Sign-flip vs fork-b (load-bearing):** the A1 block is `ω_b·I − c²·L_D`, so the
   stiff-core breather is the **SMALLEST-algebraic** eigenvalue of H (we solve `which="SA"`),
   the OPPOSITE end from fork-b's highest-ω². Documented in the module header.
3. **bw_frac=0.50 is NOT both-sectors-present.** The b_ω *energy* hybridizes 50/50, but
   it has collapsed onto the A1 core — gate (d) needs the (2,3) winding, which is absent.
   A naive `bw_frac>0` read would have falsely passed (d); the torus+integer witness is
   the load-bearing part.
4. **A_front=4/7=R_II is by-construction** (the front-gate center), not an emergent value.
5. **The result is robust** across coupling rate (0.1–3.0) and detuning (ω_s=0.2–5.0):
   `bw_on_torus` stays ≤0.002 in every case — the winding never enters the bound mode.

### Reproduce

```
cd /tmp/eigensolve
PYTHONPATH=src .venv-or-AVE-Core/.venv/bin/python -m ave.solvers.coupled_eigensolve
# tests:
PYTHONPATH=src <py> -m pytest src/tests/test_coupled_eigensolve.py            # 3 fast keepers
PYTHONPATH=src <py> -m pytest src/tests/test_coupled_eigensolve.py -m engine_sim   # 5 drivers
```

Python: `/Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python`. `make verify` PASSES.
**8/8 tests pass** (5 engine_sim + 3 gating-lane). Branch `analysis/engine-coupled-eigensolve`; branch-only, NEVER self-merge (Grant merges).

