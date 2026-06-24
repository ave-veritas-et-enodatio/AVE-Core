# Witten-effect via body angular-momentum dressing — Pre-Registration (FROZEN)

**Date**: 2026-06-23
**Lane**: implementer (analysis; reconciliation + chord-vs-fit re-test of the baryon-charge two-ontology)
**Branch**: `analysis/witten-angular-momentum-charge`
**Status**: **PREREG — sector-header + frozen question + frozen outcomes BEFORE the driver runs.**
**Skills applied**: `substrate-native-check`, `pre-test-physics-check`, `phase-space-coordinate-check` (A46), `consistency-vs-emergence`, `verify-before-cite`, `ave-discrimination-check`, `ave-prereg`, `pure-AVE-corpus`.

> **Refute-by-default carried forward.** Lane D (`#393`,
> `2026-06-23_winding-charge-quantization_result.md`) just showed the quark
> thirds are a FIT (the `ℤ_N` θ-vacuum gives denominator `N` for ANY `N`; `N=3`
> is the proton's observed loop count fed in). The DEFAULT verdict on every
> positive result here is **FIT/ECHO** unless the lattice genuinely FORCES it.
> Grant's reframing (below) was NOT tested by Lane D — this prereg tests it,
> with the same brutality.

---

## SECTOR HEADER (mandatory — written before any standard-physics word)

**WHICH SECTOR — the baryon soliton carries TWO distinct circulations.** The
substrate-native statement is the three boundary observables at a `Γ=−1`
saturation surface (`common/boundary-observables-m-q-j.md:20-21`):

- **𝒬 (charge)** = `Link(∂Ω, F) ∈ ℤ` — a **1D line/loop linking number**
  (Ontology B's integer charge). This is the through-linking of the closed
  micro-rotation circulation. It is a counted INTEGER and CANNOT be `1/3`.
- **𝒥 (spin / body angular momentum)** = `Wind(∂Ω)`, half-integer per `SU(2)`
  double-cover — a **2D surface winding**. This is the SEPARATE body-scale
  rotation Grant's reframing invokes (the poloidal `q`-winding + frame twist,
  `finkelstein-misner-spin-half-derivation.md`).

These are **two of the three independently-measurable boundary integrals**
(`M`, `Q`, `J`) — different integration dimensions (1D vs 2D). So "the baryon
carries two distinct circulations, charge-linking and body angular momentum"
is **corpus-correct** at the boundary-observable level. The open question is
the RELATIONSHIP between them under a θ/helicity (Chern-Simons-like) coupling.

**REGIME.** Cold topology for the linking/closure question (the integer is a
property of the field configuration's topology, robust to deformation — same
regime as `2026-06-19_charge-quantization-gate_result.md`). The θ/helicity
coupling is a STATIC structural dressing (a phase the body angular momentum
imposes on the charge sector), not a dynamical-saturation event. No
near-yield / ruptured regime is invoked. If a result secretly needs a driven
or saturated regime, that is flagged.

**TWO-3s GUARD (load-bearing).** The `(p,q)` winding lives on the **T2
micro-rotation grade** (charge `𝒬` = poloidal linking; spin `𝒥` = frame
winding), orthogonal to the **A1 dilatation-mass "3"** (the `m_e c²` breather
phasor `(V_inc, V_ref)`, `master-equation.md:20`). The driver NEVER wires the
winding or the angular-momentum dressing into the A1 phasor (the genesis-24
double-count). Helicity/linking/dressing is computed only on the winding's
own phase-space portrait.

**A46 PHASE-SPACE-COORDINATE GUARD.** The `(p,q)` is a PHASE-SPACE winding
portrait (`def-kn0t01`; Clifford-torus toroidal `p`, poloidal `q`). The
linking, the body angular momentum, and the θ-dressing are ALL computed in
the winding's own phase-space coordinates. I do NOT compare a phase-space
integer against a real-space lattice-Cartesian measurement.

---

## GRANT'S HYPOTHESIS (the thing under test, 2026-06-23)

The Witten-effect "fractional charge" is **NOT** a fractional charge-winding.
Ontology B is fundamental (charge = integer linking). The fraction is the
**EFFECTIVE APPEARANCE** when the soliton's separate **body angular momentum
`𝒥`** dresses the integer charge `𝒬` through a θ/helicity (Chern-Simons-like)
coupling:

$$
q_{\text{eff}} = \underbrace{n}_{\text{integer linking } 𝒬} + \underbrace{\frac{\theta}{2\pi}}_{\text{θ-weighted angular-momentum dressing}}
$$

This claims (a) a **RECONCILIATION**: Ontology B (integer charge) fundamental,
Ontology A (Witten thirds) an effective dressing — and (b) a possible
**CHORD**: if the baryon's **3-fold body angular-momentum structure** (3
constituent windings) FORCES `θ/(2π) = 1/3` per constituent, the thirds are
DERIVED with integer fundamental charge — a chord, not a fit.

---

## What the corpus ALREADY claims (GROUND-FIRST — verified by read)

Verified on `origin/main` HEAD `9309fdbc` + the `#393` PR branch, 2026-06-23.

| # | Claim | Corpus location | Status as carried |
|---|---|---|---|
| G1 | `𝒬, 𝒥` are TWO SEPARATE boundary integrals (1D linking vs 2D winding) | `boundary-observables-m-q-j.md:20-21` | **FORM-derived.** Grant's "two circulations" is corpus-correct. |
| G2 | Charge ≡ integer linking `𝒬` (TKI `[Q]≡[L]`), α-free, sign=chirality | `2026-06-19_charge-quantization-gate_result.md` | **FORM given the posit.** `[Q]≡[L]` asserted, not derived; direct Beltrami integral ~18% of p·q (C.3 OPEN). |
| G3 | For a `(p,q)` torus knot, self-linking `Q_H = p·q` — BOTH windings feed the SAME linking | `torus-knot-uniqueness.md:23,40` | **FORM (knot theory).** ⚠ The `q`-winding is a FACTOR in the linking, NOT a circulation OUTSIDE it. Load-bearing for (b). |
| G4 | Spin-½ `𝒥` = `SU(2)` frame double-cover of the EXTENDED `0₁` unknot (FM kink) | `finkelstein-misner-spin-half-derivation.md:§2-§6` | **FORM (FM theorem).** The `4π` rides the U(1) fibre; the `(2,3)` poloidal `q` carries it. |
| G5 | Witten thirds: `θ ∈ {0, 2π/3, 4π/3}` HARD-CODED in engine | `src/ave/topological/tensors.py:106` | **VALUE-IMPORTED.** `theta_angles=[0,(2*np.pi)/3,(4*np.pi)/3]` — the "3" is a typed-in literal. No θ-from-soliton, no Chern-Simons dynamics. |
| G6 | `ℤ_N` θ-vacuum gives denominator `N` for ANY `N`; `N=3` = observed proton loop count | `#393` `2026-06-23_winding-charge-quantization_result.md` PART 2 | **FIT/ECHO (Lane D verdict).** The mechanism Grant proposes is DIFFERENT and was NOT tested by Lane D. |
| G7 | Neutron `=6³₂∪0₁`, charge-0 by literal `+1+(−1)`, **"NOT Witten-effect quark cancellation"** | `neutron-identification.md:13,22` | Ontology B verbatim. |
| G8 | Neutron §3 SM-row: "The two ontologies make the same predictions about observables; AVE's mechanical picture is the substrate explanation of why the SM ontology works" | `neutron-identification.md:63` | ⚠ **The corpus ALREADY states A and B as COMPATIBLE at the observable level** — the contradiction at `:13,:22` is scoped to neutron charge-NEUTRALITY, not to a flat A-vs-B incompatibility. Load-bearing for the reconciliation verdict. |

> **🚩 The two ontologies are NOT flatly contradictory in the corpus.**
> `neutron-identification.md:13,22` says the NEUTRON's charge-0 is literal
> additive (`+1+(−1)`), NOT Witten cancellation — a statement about the
> neutron's charge BALANCE. The SAME leaf at `:63` explicitly RECONCILES A and
> B as "same predictions, different ontology, AVE = substrate explanation of
> the SM ontology." So the reconciliation Grant proposes is partly ALREADY in
> the corpus; what is NOT in the corpus is a DERIVATION of the thirds from the
> body angular momentum. The chord question is the live one.

---

## FROZEN QUESTION

> **(a) RECONCILIATION.** On the substrate, is the Witten θ-fraction =
> [integer charge-linking `𝒬`] + [a θ-dressing sourced by the separate body
> angular momentum `𝒥`] — with `𝒬` the fundamental quantity and the fraction
> an effective dressing? Or does the construction fail to separate them (the
> `q`-winding is INSIDE the linking, not a separate dressing)?
>
> **(b) CHORD-vs-FIT (the decider).** Does the baryon's 3-fold
> angular-momentum structure (3 constituents / the `(2,3)` windings) FORCE the
> denominator 3 — or does "3" re-enter as a free dial (the proton's observed
> loop count), exactly as Lane D's `ℤ_N` did?
>
> **(c) UP/DOWN split (`+2/3` vs `−1/3`).** Does it follow from the
> constituents' angular-momentum / handedness, or is it hand-labeled to PDG?

---

## FROZEN DISCRIMINATORS + outcome bins

**Discriminator R (reconciliation).**
- **RECONCILED** iff the driver demonstrates, on the winding portrait, that
  (i) the integer linking `𝒬` is recoverable as a counted integer INDEPENDENTLY
  of the angular-momentum dressing, AND (ii) a θ-dressing term sourced by `𝒥`
  can be ADDED to produce an effective `q_eff = n + θ/2π` WITHOUT changing the
  fundamental integer `𝒬`. (This shows A reduces to a dressing of B.)
- **NOT-RECONCILED** iff the `q`-winding that would source `𝒥` is the SAME
  degree of freedom that sets the linking integer `𝒬` (so there is no
  separate circulation to do the dressing — A and B are not two layers but one
  object double-counted).

**Discriminator C (chord-vs-fit on denominator 3).**
- **CHORD** iff `θ/(2π) = 1/3` is FORCED by a substrate property of the body
  angular momentum that is INDEPENDENT of observing the proton to be 3-loop —
  e.g. a K4/Cosserat stability theorem selecting exactly 3 constituent windings
  as the minimal stable closure, with `θ/2π = 𝒥_constituent / 𝒥_total = 1/3`
  coming OUT, not fed IN.
- **effective-reconciliation-but-3-still-FIT** iff the dressing reconciles A
  into B (Discriminator R = RECONCILED) BUT the `3` still enters as the
  observed/posited proton loop count (same free dial as Lane D).
- **full-FIT** iff neither reconciliation nor forcing holds (the `θ` is just
  the hard-coded `2π/3` of `tensors.py:106` re-labeled).

**Discriminator U (up/down).**
- **DERIVED** iff which constituent handedness/`𝒥`-sense is `+2/3` (up) vs
  `−1/3` (down) FALLS OUT of the substrate.
- **FIT** iff it is hand-labeled to PDG.

---

## PRE-TEST PHYSICS CHECK (one plumber-physical question, surfaced to Grant)

**The load-bearing worry (G3, flagged for Grant BEFORE the run).** Grant's
sector header posits the body angular momentum is a circulation "OUTSIDE the
charge circulation." But on a `(p,q)` torus knot the self-linking is
`Q_H = p·q` (`torus-knot-uniqueness.md:23`): the poloidal `q`-winding — the
very DOF that carries the spin `4π` frame-twist (`𝒥`) — is a MULTIPLICATIVE
FACTOR in the charge linking. So for a SINGLE torus-knot soliton the two
"circulations" are not orthogonal: `q` is shared. The dressing picture needs
the body angular momentum `𝒥` to be a SEPARATE additive frame rotation
(a rigid-body spin of the whole soliton, distinct from the internal `q`-lap
that sets the linking). Whether the substrate provides such a separate
frame-rotation DOF — distinct from the `q`-winding — is the plumber-physical
question. The Cosserat per-node micro-rotation (`finkelstein-misner...§6`) DOES
provide a frame DOF; the test is whether it can dress the charge WITHOUT being
the same `q` that sets the linking. If it can't, Discriminator R = NOT-RECONCILED.

---

## THE DRIVER (what it computes)

`src/scripts/vol_2_subatomic/witten_angmom_charge.py`. Reuses the CANONICAL
`_gauss_linking_integral` primitive (ave-canonical-source) — the same rigorous
1D linking integer the `#393` driver and the charge-quantization gate use.

VALIDATE-ON-KNOWN FIRST (the discriminator is interpretable, no HALT):
1. Hopf link → `±1`; unlinked → `0`.
2. Electron `(2,3)` single-component, self-links to the integer `p·q` = `6`,
   sign = chirality. **Recover the electron's INTEGER charge with ZERO dressing**
   (θ-dressing = 0 for the lepton) — this is the validate-on-known the brief
   requires (recover the electron integer charge).

THEN, for Grant's hypothesis:
- **R1 (separability).** Compute the linking integer `𝒬` of a constituent
  winding. Separately compute a candidate body-angular-momentum frame rotation
  `𝒥` (a rigid SO(2) frame twist of the whole curve about its symmetry axis).
  Test: does adding a frame rotation `𝒥` CHANGE the linking integer `𝒬`?
  (If YES → not separable → the dressing is double-counting the same DOF.
  If NO → `𝒬` is invariant under frame rotation → separable → reconciliation
  is structurally possible.)
- **R2 (dressing arithmetic).** GIVEN a posited θ from the frame rotation,
  compute `q_eff = 𝒬 + θ/2π` and confirm it reproduces the Witten arithmetic
  WITHOUT altering the integer `𝒬`. (This is the reconciliation demonstration
  IF R1 says separable.)
- **C1 (the decider — does 3 fall out or get fed in?).** Build the symmetric
  3-constituent Borromean-like link. Compute, from the link's OWN geometry,
  the ratio `θ_constituent/2π = 𝒥_constituent / 𝒥_total`. Test whether this
  ratio is FORCED to `1/3` by a substrate stability/minimality property, or
  whether `N=3` is an INPUT (the number of constituents I chose). The decisive
  sweep: run `N ∈ {2,3,4,5}` and check whether the substrate EXCLUDES `N≠3`
  (a stability theorem) or admits all `N` (then `3` is fed in = FIT).
- **U1 (up/down).** Check whether the sign/handedness of a constituent's frame
  rotation maps to `+2/3` (up) vs `−1/3` (down) by a substrate rule, or only
  by hand-labeling to PDG.

GUARDS (mirror `#393`):
- VALUE-ECHO IMMUNITY: integers + signs + the geometric ratios the construction
  itself produces; NO `α` / `-e` / CODATA / `constants` imported (asserted at
  module entry).
- TWO-3s ORTHOGONALITY: linking/dressing on the winding curve only; never the
  A1 phasor.
- A46 PHASE-SPACE: everything in the winding's own coordinates.

---

## FROZEN FALSIFICATION TABLE (the verdicts are pre-committed to bins)

| Result | If… | Verdict |
|---|---|---|
| R1 separability | frame rotation `𝒥` does NOT change linking `𝒬` | reconciliation STRUCTURALLY POSSIBLE |
| R1 separability | frame rotation IS the `q` that sets `𝒬` | NOT-RECONCILED (double-count) |
| C1 denominator-3 | substrate EXCLUDES `N≠3` (stability theorem, 3 OUT) | **CHORD** |
| C1 denominator-3 | substrate admits all `N`; `3` = chosen constituent count | **effective-reconciliation-but-3-still-FIT** (if R reconciled) or **full-FIT** |
| U1 up/down | substrate rule maps handedness→up/down | DERIVED |
| U1 up/down | hand-labeled to PDG | FIT |

**Rule-11 hidden-input watch.** If C1 needs the input "the proton IS 3-loop"
to get `1/3`, that is the SAME hidden input Lane D caught (`N=3` = observed
loop count). A chord requires `3` to come from a substrate stability/minimality
property, NOT from observing the proton.

**Rule-12 posture.** If Grant's hypothesis is falsified on the chord question,
this prereg is NOT refilled with a new hypothesis; the result doc records the
verdict and the branch closes per Rule 11.
