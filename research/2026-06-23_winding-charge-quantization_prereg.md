# Winding charge-quantization (electron p, quark fractions, confinement) — Pre-Registration (FROZEN)

**Date**: 2026-06-23
**Lane**: D (derivation implementer, lattice-discovery epic)
**Branch**: `analysis/winding-charge-quantization`
**Status**: **PREREG — sector-header + frozen question + frozen outcomes BEFORE the driver runs.**
**Skills applied**: `substrate-native-check`, `pre-test-physics-check`, `phase-space-coordinate-check` (A46), `consistency-vs-emergence`, `verify-before-cite`, `ave-prereg`, `ave-discrimination-check`, `pure-AVE-corpus`.

> **Prior-route warning carried forward.** A prior spinor/Hopf route to this same
> target COLLAPSED-TO-FIT (it read its source table backwards). Refute-by-default
> is the operating posture: a convergent appealing story is exactly where motivated
> reasoning hides. The DEFAULT verdict on every positive result is FIT/ECHO unless
> the lattice genuinely forces it.

---

## SECTOR HEADER (mandatory — written before any standard-physics word)

**WHICH SECTOR.** CHARGE = Beltrami helicity `H_bel = ∫ ω·(∇×ω)`, the
through-linking of the Cosserat `(2,q)` micro-rotation WINDING (Z_shear / T2 grade;
`A1 ⊥ T2` per `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`).
This is a question about the WINDING TOPOLOGY **in phase space** — the `(2,q)` is a
winding portrait on the Clifford torus (toroidal index `p`, poloidal index `q`),
**NOT a real-space knot**: the electron's real-space body is the `0₁` UNKNOT
(`vol2/.../electron-identification.md:22`, `CLAUDE.md` two-3s note). I do NOT lead
with Hopf/spinor/vortex; I lead with winding/helicity/closure in circuit-native
(EE) language: a charge is a CLOSED loop of micro-rotation circulation whose
self-through-linking is a counted integer.

**REGIME.** The winding-closure question is asked at the COLD topology of the
winding (the integer is a property of the field configuration's topology, robust
to deformation — this is the regime the charge-quantization gate already ran in,
`research/2026-06-19_charge-quantization-gate_result.md`). The DRIVEN/SATURATED core
(the Beltrami force-free state the saturated B-field collapses into) is named as the
candidate SOURCE of the winding in sub-route (b), and is tested as a *source*
hypothesis, not assumed. So: **cold-topology for the closure/quantization question;
saturated-core only where sub-route (b) explicitly invokes it, flagged as such.**

**TWO-3s GUARD (load-bearing).** The `(p,q)` winding is the T2 micro-rotation "3"
(charge/spin), orthogonal to the A1 dilatation-mass "3" (the `m_e c²` breather). The
driver NEVER wires the winding into the A1 `(V_inc, V_ref)` phasor (the genesis-24
double-count). Helicity/linking is computed only on the ω micro-rotation grade /
its parametric winding curve.

**A46 PHASE-SPACE-COORDINATE GUARD.** The `(p,q)` is a PHASE-SPACE winding portrait
(`def-kn0t01`). The helicity/linking computed here is the self-through-linking of
that winding curve (a phase-space-native integer). I do NOT compare a phase-space
`φ²`/winding integer against a real-space lattice-Cartesian measurement. The
parametric helicity computation lives entirely in the winding's own coordinates.

---

## What the corpus ALREADY claims (GROUND-FIRST — do not re-derive)

Verified by read on `origin/main` HEAD `9309fdbc`, 2026-06-23. For each: is it
FORM-derived or VALUE-imported in the corpus as it stands?

| # | Claim | Corpus location | Status as the corpus carries it |
|---|---|---|---|
| G1 | Charge ≡ topological winding/linking integer `𝒬` (TKI `[Q]≡[L]`) | `2026-06-19_charge-quantization-gate_result.md`; `charge_quantization.py` | **FORM-forced GIVEN the posit.** `𝒬` is an integer, α-free, sign=chirality, robust to deformation — but **CONDITIONAL on the asserted `[Q]≡[L]` identification** (the gate explicitly says it does NOT derive the posit). The direct Beltrami integral does NOT normalize at lattice scale (~18% of p·q); closure is **by the `Q_H=p·q` product FORMULA**, not by two integrals agreeing. C.3 STAYS OPEN. |
| G2 | Electron = `0₁` unknot (real-space) carrying `(2,3)` phase-space winding | `electron-identification.md:22-23`; `torus-knot-uniqueness.md` | FORM-claimed. The CHARGE the gate reads is `q=3` (poloidal linking); `p=2` is the toroidal companion. |
| G3 | `(2,3)` is the smallest non-trivial coprime torus knot | `torus-knot-uniqueness.md` | **MINIMALITY argument.** Coprimality + both-≥2 + "electron = lightest stable non-trivial lepton." Explicitly "knot theory is standard math; the identification is the AVE physical assertion." **This is a minimality selection, NOT a forcing — flagged here as the exact thing PART 1 must scrutinize.** |
| G4 | Proton = `(2,5)` phase-space winding + `6³₂` Borromean real-space (3 loops) | `proton-identification.md:19-20` | FORM-claimed. Both electron and proton share `p=2`. |
| G5 | Quark fractional charges via Witten Effect on `ℤ₃` Borromean θ-vacuum: `q_eff = n + θ/(2π)·e`, `θ ∈ {0,±2π/3,±4π/3}` → `{±1/3,±2/3}` | `topological-fractionalization.md:12-45`; `proton-identification.md:43` | **CLASSIFY-ME.** The `ℤ₃` → thirds step is the candidate FORCING; the `θ → up/down` assignment is the candidate FIT. PART 2 scrutinizes both. |
| G6 | Neutron = `6³₂ ∪ 0₁`, charge-0 by **literal additive** `+1+(−1)`, **NOT Witten-effect quark cancellation; ZERO udd/uud framing** | `neutron-identification.md:13,22` | **CONTRADICTION FLAG (see below).** |

> **🚩 FLAG-DON'T-FIX (surfaced at prereg, for Grant adjudication).** G5 and G6 are
> in tension. `topological-fractionalization.md` derives the proton's `+1` and the
> quark content via the Witten Effect on a `ℤ₃` Borromean θ-vacuum (the three loops
> ARE the three quarks). `neutron-identification.md:13,22` says the neutron is
> `6³₂ ∪ 0₁` with charge-0 by **literal additive cancellation `+1+(−1)`**,
> explicitly **"NOT Witten-effect quark cancellation"**, and that the corpus uses
> **"ZERO udd/uud framing — grep confirmed zero matches for udd."** So the proton
> (Witten-effect quarks) and the neutron (proton+threaded-electron, no quarks) use
> **two incompatible ontologies of baryon charge**. PART 2 must declare which
> ontology it is testing and surface this; it must NOT silently pick one. Both
> file:line citations carried verbatim above.

---

## FROZEN QUESTION

> **PART 1.** Does the lattice FORCE the electron's toroidal winding index `p=2`
> (screw-free, kept provably separate from the `q=3` poloidal/spin closure) — or is
> `p=2` merely "the smallest pair that holds" (a minimality SELECTION = a fit)?
>
> **PART 2.** In the same closed-winding / helicity-closure framework: does a quark
> carry a winding that does NOT close on its own (fractional helicity), forced to an
> integer only by the proton's 3-component Borromean closure — and does the
> 3-component linkage FORCE the denominator 3 (thirds), FORCE confinement (no free
> quark), and FIX the up/down split (`+2/3` vs `−1/3`) — or is each of these
> reverse-engineered / fit to the known values?

---

## PART 1 — three candidate sub-routes for electron `p=2` (each tested independently)

Each sub-route is tested SEPARATELY and the spin `4π` double-cover (which rides the
poloidal/short-way `q` via the SU(2) frame holonomy of the real-space unknot, per
`2026-06-19_spin-doublecover-gate_result.md`) must NOT leak onto `p`. If a sub-route
secretly needs the spin closure to force `p`, that is a Rule-11 hidden-input failure.

- **(a) NYQUIST-MINIMAL-WINDING.** On the discrete mesh, ≥2 samples/cycle are needed
  to represent a closed phase-space winding; a `p=1` winding aliases and cannot
  close. CLAIM TO TEST: 2 is the minimal closeable d-axis (toroidal) winding on this
  lattice. REFUTE CONDITION: if `p=1` closes cleanly (recovers a counted integer
  helicity) at the same lattice fidelity as `p=2`, the Nyquist-minimal claim FAILS.
  **Pre-test physics worry (surfaced to Grant):** Nyquist sets a *resolution* floor
  (cells-per-wind), not directly a *winding-number* floor — a `p=1` curve is a plain
  loop and is perfectly representable. So this sub-route is at risk of conflating
  "≥2 samples to resolve a wiggle" with "≥2 windings to be non-trivial." Flagged.

- **(b) B-SATURATION→BELTRAMI.** The saturated core (Z_core→0, C_eff→∞) drives the
  inductive/B-sector force-free (`∇×B=λB`, Beltrami) — a twist. CLAIM TO TEST: this
  SOURCES the winding (charge), not merely admits it. REFUTE CONDITION: if the
  Beltrami force-free condition is equally satisfied by `p=1` and by `p≥2` (i.e. it
  admits any winding without selecting `p=2`), then it does not SOURCE `p=2`; it is a
  consistency container, not a forcing.

- **(c) MONOPOLE-DOUBLE-WIND.** A unit charge (a closed "monopole" of helicity)
  requires a double-wind; a single lap nets zero enclosed helicity. CLAIM TO TEST:
  closure to a unit integer needs exactly `p=2`. REFUTE CONDITION: if a single lap
  (`p=1`) already nets a unit integer helicity in the clean parametric computation,
  the double-wind claim FAILS.

## PART 2 — quark-charge cross-check sub-claims (the stronger test)

- **(Q1) FRACTIONAL = non-self-closing.** A lone quark winding does NOT close to an
  integer on its own; only the 3-component Borromean closure makes an integer.
  REFUTE: if a lone-component winding already closes to an integer in the clean
  helicity computation, "fractional = non-self-closing" FAILS.
- **(Q2) DENOMINATOR-3 forced.** The 3-component linkage FORCES thirds. REFUTE: if
  the denominator could equally be any `N` (the math gives `1/N` for an `N`-component
  closure with no reason `N=3`), then "3" is imported from the observed proton, not
  forced. (Test: does the helicity-closure constraint, applied to an `N`-component
  symmetric link, give `1/N` for general `N` — making `N=3` a CHOICE matched to the
  proton, not a derivation?)
- **(Q3) CONFINEMENT forced.** Open/partial winding (fractional helicity) cannot be a
  stable standalone Beltrami soliton (helicity must close) → no free quark; and the
  Borromean property (remove one → link falls apart) forces it. REFUTE: if a lone
  fractional winding is a valid standalone closed helicity state, confinement is not
  forced by closure.
- **(Q4) UP/DOWN split (`+2/3` vs `−1/3`).** Does it come from winding
  handedness/direction in the link, or is it reverse-engineered? REFUTE (default):
  if the `θ → {+2/3 = up, −1/3 = down}` assignment requires labeling-by-hand to match
  PDG (no substrate reason a given handedness is "up"), it is a FIT.

## FROZEN DISCRIMINATORS (the make-or-break axes)

1. **FORCED vs SMALLEST-THAT-HOLDS** (PART 1). `p=2` is a CHORD only if the lattice
   forbids `p=1` from closing (a positive forcing), NOT merely if `p=2` is the
   smallest pair that works (minimality = a fit). The clean parametric helicity
   computation is the arbiter: does `p=1` close to a unit integer or not?
2. **DERIVED vs FIT-TO-VALUE** (PART 2). The thirds `{1/3,2/3}` are a CHORD only if
   the closure math forces denominator 3 from the Borromean 3-loop structure
   independent of the observed proton — not if `N=3` is chosen to match the proton
   and `{+2/3,−1/3}` labeled by hand.
3. **HIDDEN-INPUT (Rule-11)** on every positive: does the result secretly need the
   electron, the spin closure, or the observed charge value as an input?
4. **SYMMETRIC-STANDARD.** Charge quantization + quark fractions are SM POSITS (SM
   puts them in by hand via hypercharge / quark hypercharge assignments). A genuine
   AVE *derivation* of either is a real win; a re-dressed minimality / fit is not. Do
   not penalize AVE for a gap SM also has — but do not credit a fit as a derivation.

## FROZEN OUTCOMES (per result: electron-p / quark-denominator / confinement / up-down)

For EACH of the four results, the verdict is exactly one of:
- **CHORD (FORM-forced)** — the lattice forces it; `p=1` (resp. non-3 denominator,
  free quark, hand-labeled split) is provably excluded by the substrate.
- **FIT / ECHO (imported VALUE)** — recovers the known value but by minimality /
  matched assignment / fit-to-target, not by forcing.
- **CONSISTENCY** — a true substrate statement with no novel content beyond what the
  posit `[Q]≡[L]` (or the observed proton) already supplies.

Pre-registration priors (honest-closure bookkeeping, not derived):
electron-`p=2` CHORD ~15% / FIT ~70% / CONSISTENCY ~15%;
quark-denominator-3 CHORD ~25% / FIT ~55% / CONSISTENCY ~20%;
confinement CHORD ~40% / FIT ~25% / CONSISTENCY ~35%;
up-down-split CHORD ~10% / FIT ~80% / CONSISTENCY ~10%.

## DRIVER PLAN (validate-on-known FIRST)

A clean PARAMETRIC helicity/linking computation on `(p,q)` torus-knot curves (NOT
the lattice-sampled field — to sidestep the q≲4 resolution ceiling the prior gate
hit and isolate the topology question):
1. **VALIDATE-ON-KNOWN:** recover the electron's integer charge — the `(2,3)` curve's
   self-linking `= p·q = 6` and its Gauss self-linking integer must come out
   integer; an `N=1` (single closed loop) unit-twist nets a unit integer. If the
   known electron integer does NOT recover, HALT (the tool is not interpretable).
2. **PART 1 test:** compute closure/helicity for `p ∈ {1,2,3}` at fixed `q`; does
   `p=1` close to a unit integer (REFUTES double-wind/Nyquist-minimal) or not (admits
   the forcing)?
3. **PART 2 test:** compute the self-linking of a LONE component of an `N`-component
   symmetric link vs the total of the closed `N`-link; does a lone component give a
   fractional (`1/N`) share, and is `N=3` forced or free?

Substrate-native, ave-canonical-source, no `α`/`-e`/CODATA imported (integers + signs
only, same value-echo-immunity guard as `charge_quantization.py`). `make verify`
before commit.

---

**PREREG STATUS: FROZEN — 2026-06-23.** Driver + verdicts in the companion result doc.

