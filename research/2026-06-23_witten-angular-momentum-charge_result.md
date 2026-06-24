# Result — Witten-effect via body angular-momentum dressing (reconciliation + chord-vs-fit)

**Ran:** 2026-06-23
**Lane:** implementer (analysis; reconciliation + chord re-test of the baryon-charge two-ontology)
**Branch:** `analysis/witten-angular-momentum-charge`
**Prereg (frozen BEFORE the run):** [`2026-06-23_witten-angular-momentum-charge_prereg.md`](2026-06-23_witten-angular-momentum-charge_prereg.md)
**Driver:** `src/scripts/vol_2_subatomic/witten_angmom_charge.py`
**Output:** `src/scripts/vol_2_subatomic/witten_angmom_charge_results.json`
**Tests:** `src/tests/test_witten_angmom_charge.py` (5, all pass)

---

## HEADLINE — two answers to Grant's two questions

**(1) Does the angular-momentum dressing RECONCILE Ontology A into Ontology B?**
**YES — IN FORM.** The integer charge-linking `𝒬` is fundamental and a separate
body angular momentum `𝒥` (a rigid frame rotation of the whole soliton) CAN dress
it WITHOUT touching the integer. So `q_eff = n + θ/2π` with `n` the fundamental
integer and `θ/2π` an effective dressing is a structurally coherent picture. The
corpus, in fact, ALREADY states A and B as compatible at the observable level
(`neutron-identification.md:63`); this result supplies the substrate-native
mechanism for that compatibility.

**(2) Does the 3-fold structure FORCE the thirds (CHORD), or relocate the fit?**
**RELOCATE THE FIT.** The denominator equals `N` for EVERY `N` (the
per-constituent share of a symmetric body rotation is `1/N` by symmetry); the
substrate EXCLUDES no `N`. `N=3` is the proton's OBSERVED loop count fed in —
**the exact same free dial Lane D `#393` caught** (`ℤ_N → 1/N` for any `N`). The
dressing reframing makes the mechanism more PHYSICAL (an angular-momentum share,
not a hard-coded `θ ∈ {2π/3,4π/3}` literal), but it does NOT make the `3` derived.

| Result | Verdict | One-line reason |
|---|---|---|
| Reconciliation (A→B) | **RECONCILED-IN-FORM** | `𝒬` invariant under rigid frame rotation `𝒥` (linking = −6 across the whole frame sweep) → `𝒥` is a separate DOF that dresses, not alters, the integer charge. |
| Denominator-3 forced? | **effective-reconciliation-but-3-still-FIT** | per-constituent angular-momentum share = `1/N` by symmetry for ANY `N`; substrate excludes no `N`; `N=3` = observed proton loop count fed in. |
| Up/down split (`+2/3` vs `−1/3`) | **FIT / ECHO** | the SET `{±1/3,±2/3}` falls out of `ℤ_3` (given `N=3`), but WHICH θ-sector is "up" is hand-labeled to PDG. |

---

## VALIDATE-ON-KNOWN (wired FIRST — recover the electron integer charge)

| Anchor | Value | Meaning |
|---|---|---|
| Hopf link (two loops linked once) | `−1` | linking integral recovers `±1` for a genuine link |
| Unlinked loops (far apart) | `0` | recovers `0` for no linking |
| Electron `(2,3)` single-component (`gcd=1`) | `True` | one closed loop (a knot, not a multi-component link) |
| Electron `(2,3)` self-linking | `−6` (= `p·q`) | the electron's charge-closure integer is recovered |
| Sign = chirality | RH `−6`, LH `+6` | self-linking sign flips with handedness (the charge sign) |
| **Electron `q_eff` with ZERO dressing** | `−6` (exact integer) | the LEPTON has no θ-dressing → `q_eff = 𝒬` exactly. **This is the brief's "recover the electron integer charge" — passed.** |

The known electron integer recovers, the Hopf/unlinked anchors behave, the sign
tracks chirality, and the zero-dressing lepton charge is an exact integer. **No
HALT; the discriminator is interpretable** — the verdicts below are not a broken-
tool artifact.

---

## PART R — RECONCILIATION: does `𝒥` dress the integer `𝒬` without altering it?

### R1 — SEPARABILITY (the load-bearing test)  →  **RECONCILED-IN-FORM, with a caveat**

The substrate carries TWO genuinely separate boundary integrals
(`boundary-observables-m-q-j.md:20-21`):
- `𝒬 = Link(∂Ω, F) ∈ ℤ` — a **1D line/loop linking** (charge, Ontology B's integer);
- `𝒥 = Wind(∂Ω)` — a **2D surface winding** (spin / body angular momentum).

So Grant's "two distinct circulations" is **corpus-correct**. The decisive
question: can a body angular momentum `𝒥` dress the charge WITHOUT changing the
integer `𝒬`? I applied a rigid frame rotation (an SO(2) twist of the WHOLE
soliton about its symmetry axis — a genuine separate body rotation) through a full
sweep and re-measured the linking:

| frame angle `α/2π` | linking `𝒬` |
|---|---|
| 0.0, 0.167, 0.333, 0.5, 0.667, 0.833, 1.0 | **−6** (all) |

**`𝒬` is INVARIANT under rigid body-frame rotation.** A separate body angular
momentum does NOT touch the linking integer. **So the dressing picture is
structurally sound: `𝒬` is the fundamental integer; `𝒥` can carry a θ-phase that
dresses the EFFECTIVE charge without altering the FUNDAMENTAL integer.** Ontology A
reduces to a dressing of Ontology B. RECONCILED-IN-FORM.

> **LOAD-BEARING CAVEAT (the pre-test-physics worry, confirmed).** The separate
> circulation that does the dressing MUST be the RIGID FRAME rotation — it is
> NOT the internal poloidal `q`-winding. The `q`-winding (which carries the spin
> `4π` frame-twist) is a MULTIPLICATIVE FACTOR in the linking: `q=3 → 𝒬=6`,
> `q=5 → 𝒬=10` (`Q_H = p·q`, `torus-knot-uniqueness.md:23`). So one must NOT
> identify the dressing `𝒥` with the `q`-lap that sets the linking — that would
> be the same DOF double-counted (and would change `𝒬`, breaking the
> reconciliation). The reconciliation holds ONLY for the rigid-frame `𝒥`,
> distinct from the linking-internal `q`. This is the honest boundary of the
> reconciliation: it works, but only with the right `𝒥`.

### R2 — DRESSING ARITHMETIC  →  consistent (and therefore NOT a forcing)

`q_eff = n + θ/2π` with `n=0` (lepton-cancelled cage interior) reproduces the
Witten arithmetic trivially for `θ/2π ∈ {0, 1/3, 2/3}`, leaving the integer `n`
untouched. **The FORM is trivially consistent — which is exactly why it is not, on
its own, a forcing.** The dressing form "works" for any `θ`. The forcing question
is entirely in PART C.

---

## PART C — THE DECIDER: is the denominator 3 FORCED or fed in?

### C1 — denominator-3  →  **effective-reconciliation-but-3-still-FIT**

Grant's chord claim: the baryon's 3-fold body angular-momentum structure (3
constituents) FORCES `θ/(2π) = 𝒥_constituent / 𝒥_total = 1/3`. The arithmetic IS
clean: for an `N`-fold-symmetric soliton, the per-constituent share of a symmetric
body rotation is EXACTLY `1/N` by symmetry. That `1/N` is genuine FORM (it follows
from the `N`-fold symmetry, not hand-set). **But the VALUE `1/3` requires `N=3`,
and nothing in the substrate selects `N=3`:**

| `N` | per-constituent angular-momentum share | `θ/2π` | denominator | substrate excludes this `N`? |
|---|---|---|---|---|
| 2 | `1/2` | `1/2` | **2** | no |
| 3 | `1/3` | `1/3` | **3** | no |
| 4 | `1/4` | `1/4` | **4** | no |
| 5 | `1/5` | `1/5` | **5** | no |

**The denominator equals `N` for every `N`; the substrate EXCLUDES none.** This is
the IDENTICAL failure mode Lane D `#393` found for the `ℤ_N` θ-vacuum
(`2026-06-23_winding-charge-quantization_result.md` PART 2): the construction is
generic in `N`, and `N=3` enters because the **proton is OBSERVED to be a 3-loop
(`6³₂` Borromean) structure** — the loop count is read off the proton, then fed in.

> **What WOULD have made it a CHORD.** A K4/Cosserat stability (or minimality)
> theorem selecting exactly 3 constituent windings as the minimal stable
> multi-loop closure — `N=3` coming OUT, independent of observing the proton. The
> corpus carries NO such theorem: the `6³₂` Borromean is ASSERTED as the proton's
> real-space topology (`proton-identification.md:20`), and "why exactly 3 loops"
> is not derived. **Rule-11 hidden-input check: C1 needs the input "the proton IS
> 3-loop" to get `1/3` — the SAME hidden input Lane D caught.** Until a 3-loop
> stability theorem exists, denominator-3 is an echo of the observed proton.

> **The reframing's REAL contribution (honest credit).** Grant's dressing picture
> is a genuine IMPROVEMENT over the corpus's `tensors.py:106` implementation,
> where `theta_angles = [0, (2*np.pi)/3, (4*np.pi)/3]` is a HARD-CODED literal
> (the "3" typed directly into the source). The dressing replaces that typed-in
> `2π/3` with a `1/N` angular-momentum SHARE that at least FOLLOWS from `N`-fold
> symmetry — so the mechanism is more physical. But "more physical mechanism for
> the same fed-in `N`" is a better ECHO, not a chord. The `3` is relocated from a
> hard-coded θ-literal to a chosen constituent count; it is not derived.

---

## PART U — UP/DOWN split  →  **FIT / ECHO**

The set `{±1/3, ±2/3}` falls out of `ℤ_3` (given `N=3`): `θ=±2π/3 → ±1/3`,
`θ=±4π/3 → ±2/3`, sign = handedness. But WHICH θ-sector is named "up" (`+2/3`) vs
"down" (`−1/3`) has NO substrate rule — it is reverse-engineered to PDG. The
`n_twist=0` base-node choice (`topological-fractionalization.md:32`) is also a
choice. So the up/down LABELING is a hand-fit.

> **SYMMETRIC-STANDARD check.** SM POSITS the quark charges and the up/down
> assignment outright (hypercharge put in by hand); it does not derive them
> either. So AVE's dressing picture is at least as principled as SM here — but the
> specific claim under test ("the 3-fold structure FORCES the thirds + fixes
> up/down") is NOT met. This is peer-with-SM, not a comedown; the object-level
> verdict (FIT) stands.

---

## RECONCILIATION VERDICT (Grant's question 1, in full)

**Does the angular-momentum dressing reconcile A into B?  YES, in form — and the
corpus already half-states it.** Three independent pieces:

1. **`𝒬` and `𝒥` are genuinely separate** (two distinct boundary integrals, 1D
   linking vs 2D winding — `boundary-observables-m-q-j.md:20-21`). Grant's sector
   header is corpus-correct.
2. **`𝒬` is invariant under a rigid body angular momentum `𝒥`** (R1: linking = −6
   across the whole frame sweep). So `𝒥` can dress the EFFECTIVE charge without
   altering the FUNDAMENTAL integer. Ontology B (integer `𝒬`) is fundamental;
   Ontology A (the Witten fraction) is an effective dressing. This is exactly the
   structure Grant proposed.
3. **The corpus already states A↔B compatibility** at the observable level
   (`neutron-identification.md:63`: *"The two ontologies make the same predictions
   about observables; AVE's mechanical picture is the substrate explanation of why
   the SM ontology works"*). The apparent contradiction at `neutron-
   identification.md:13,22` (*"NOT Witten-effect quark cancellation"*) is scoped
   to the NEUTRON's charge-NEUTRALITY (its `+1 + (−1) = 0` balance), NOT to a flat
   A-vs-B incompatibility. So the two leaves are NOT in hard contradiction; the
   dressing supplies the substrate mechanism for the compatibility the corpus
   already asserts.

**BUT the reconciliation does NOT buy the chord.** A↔B reconciliation is about the
FORM of the charge (integer + dressing); the CHORD question is about the VALUE of
the denominator (is `3` forced?). Reconciling the form leaves the `3` exactly as
fed-in as it was. The two questions are independent, and Grant's reframing answers
the first YES and the second NO.

---

## Per-result FORM / VALUE classification (the deliverable axis)

| Result | Class | FORM-forced? | Imported VALUE / fit? |
|---|---|---|---|
| `𝒬, 𝒥` are two separate circulations | **FORM** | two distinct boundary integrals (1D vs 2D) — substrate-derived | none |
| `𝒬` invariant under body rotation `𝒥` | **FORM** | linking is a topological invariant; rigid rotation can't change it | none |
| Reconciliation A→B (dressing form) | **effective-reconciliation (FORM of charge)** | `q_eff = n + θ/2π` with `n` integer-invariant is structurally sound | none for the FORM |
| Per-constituent share = `1/N` | **FORM (symmetry)** | `1/N` follows from `N`-fold symmetry | none for the `1/N` form |
| **Denominator-3** | **FIT / ECHO** | the `1/N` form is FORM | `N=3` = OBSERVED proton loop count fed in; substrate excludes no `N`. Same dial as Lane D `#393`. |
| **Up/down split** | **FIT / ECHO** | the set `{±1/3,±2/3}` follows from `ℤ_3` | which θ-sector = "up" is hand-labeled to PDG. |

**Net:** Grant's reframing FORM-derives MORE of the skeleton than the corpus did
(it replaces the hard-coded `θ=2π/3` literal with a symmetry-forced `1/N` share,
AND it cleanly separates the fundamental integer charge from the effective
dressing — a genuine structural improvement and a real reconciliation). But the
load-bearing VALUE `3` is still IMPORTED (the observed proton loop count). This is
**a third instance of the FORM-deriving / VALUE-importing meta-finding**
(`research/2026-06-15_form-deriving-value-importing_meta-finding.md`) in the
baryon-charge sector — a better-grounded echo, not a new chord.

---

## 🚩 FLAG-DON'T-FIX — the two-ontology tension is REDUCED, not eliminated

Surfaced by Lane D `#393` and re-examined here. My finding REFINES it (I do NOT
silently resolve it; for Grant adjudication):

- **Lane D framed A and B as "mutually exclusive ontologies"** (`#393` result,
  FLAG section). **This result shows they are NOT mutually exclusive** — the
  dressing reconciles A into B (integer `𝒬` fundamental, fraction = effective `𝒥`-
  dressing), and `neutron-identification.md:63` already states their observable-
  level compatibility. The tension is REDUCED to: *which is canonical/load-bearing
  for the proton's `+1`?*
- **The remaining live tension** (for Grant): if the proton's `+1` is sourced as a
  SINGLE integer twist at the cage center (Ontology B / the mass-eigenvalue
  derivation, `proton-identification.md:40,67`), then the Witten-fraction machinery
  (Ontology A) is a PARALLEL, non-load-bearing story for any AVE mass/charge
  prediction — even after reconciliation. The reconciliation says A is a
  consistent EFFECTIVE description of B; it does not make A load-bearing.
- **Recommendation (for Grant, not landed by me):** the canonical leaf should
  state A as the EFFECTIVE (dressing) description and B as the FUNDAMENTAL
  (integer-linking) description, with the explicit note that the denominator `3`
  is fed in from the observed proton loop count, NOT forced — pending a 3-loop
  stability theorem. I do NOT edit the canonical leaves (auditor lane lands manual
  entries; Grant adjudicates the canonical framing).

---

## HONEST SCOPE (do not overclaim)

1. **Parametric, not lattice-field.** The driver computes linking on parametric
   `(p,q)` curves and rigid frame rotations (to sidestep the `q≲4` lattice-
   resolution ceiling the `2026-06-19` gate hit). It tests TOPOLOGY + frame-
   rotation invariance, NOT lattice-field dynamics. A lattice-field confirmation
   is not in hand and not claimed.
2. **The θ/Witten term has NO dynamical lattice representation.** The corpus's
   Witten effect is `tensors.py:99-114` — a hard-coded `theta_angles=[0,2π/3,4π/3]`
   list, with no Chern-Simons dynamics, no θ-from-soliton, no body-angular-momentum
   coupling in any engine. So the dressing mechanism tested here is a STRUCTURAL /
   arithmetic demonstration of Grant's reframing, NOT an engine-derived θ. The
   reconciliation is at the level of the boundary-observable algebra (`𝒬, 𝒥`
   separability), which IS substrate-grounded.
3. **Reconciliation ≠ chord.** RECONCILED-IN-FORM is a genuine structural result
   (and a CONSISTENCY-class advance: it cleanly separates fundamental integer
   charge from effective dressing). It is NOT a forcing of the thirds. The two
   are independent; the chord question lands NEGATIVE.
4. **Refute-by-default held.** This driver gave Grant's reframing every chance: it
   confirmed the separability (R1), demonstrated the dressing form (R2), and then
   asked whether `3` is forced (C1) — and `3` is NOT forced. Clean result: the
   reframing reconciles the ontologies (a real win) but does not derive the
   thirds (the chord stays closed-NEGATIVE, per Rule 11).
5. **Rule-12 posture.** Grant's hypothesis is PARTIALLY confirmed (reconciliation
   YES) and PARTIALLY falsified (chord NO). The prereg slot is not refilled; this
   result records both verdicts and the branch closes.

---

## Reproduce

```
PYTHONPATH=src python3 -m scripts.vol_2_subatomic.witten_angmom_charge
PYTHONPATH=src python3 -m pytest src/tests/test_witten_angmom_charge.py -q
```

Value-echo immunity: the driver imports only the canonical
`_gauss_linking_integral` primitive; no `α` / `-e` / CODATA / `constants` is
imported (asserted at module entry by `_assert_no_value_echo`). Integers + signs
+ construction-internal geometric ratios only.
