# Result — Winding charge-quantization (electron p, quark fractions, confinement)

**Ran:** 2026-06-23
**Lane:** D (derivation implementer, lattice-discovery epic)
**Branch:** `analysis/winding-charge-quantization`
**Prereg (frozen BEFORE the run):** [`2026-06-23_winding-charge-quantization_prereg.md`](2026-06-23_winding-charge-quantization_prereg.md)
**Driver:** `src/scripts/vol_2_subatomic/winding_charge_closure.py`
**Output:** `src/scripts/vol_2_subatomic/winding_charge_closure_results.json`

---

## HEADLINE VERDICT: refute-by-default HELD. No new chord.

Every positive result came back **FIT/ECHO or CONSISTENCY**. The lattice does NOT
force the electron's `p=2`, does NOT force the quark denominator-3, does NOT
independently force confinement (beyond restating the `[Q]≡[L]` posit), and does NOT
fix the up/down split. This is the discipline working: the convergent appealing
story ("p=2 is forced; thirds are forced; confinement falls out") is exactly where
the prior spinor/Hopf route collapsed-to-fit, and the clean parametric helicity
computation refuses to ratify it.

| Result | Verdict | One-line reason |
|---|---|---|
| Electron `p=2` forced? | **FIT / ECHO** | `(1,1)`, `(1,2)`, `(1,3)` all close as single-component unit-charge loops; the substrate does NOT forbid `p=1`. `p=2` is the smallest-coprime **knot-non-triviality** minimality, not a charge-closure forcing. |
| Quark denominator-3 forced? | **FIT / ECHO** | The `ℤ_N` θ-vacuum construction gives denominator `N` for ANY `N`; `N=3` is the proton's **observed** loop count, chosen-to-match, not forced. |
| Confinement forced? | **CONSISTENCY** | A free fractional helicity state is forbidden by the closure requirement — but that is the `[Q]≡[L]` posit restated, not a novel forcing; the Borromean remove-one-falls-apart property is structurally real but does not by itself fix `N=3`. |
| Up/down split (`+2/3` vs `−1/3`) | **FIT / ECHO** | The `θ → {+2/3=up, −1/3=down}` mapping requires hand-labeling to match PDG; no substrate reason a given handedness is "up." |

---

## VALIDATE-ON-KNOWN (wired FIRST — the tool is interpretable, no HALT)

| Anchor | Value | Meaning |
|---|---|---|
| Hopf link (two loops linked once) | `−1` | linking integral recovers `±1` for a genuine link |
| Unlinked loops (far apart) | `0` | recovers `0` for no linking |
| Electron `(2,3)` single-component | `True` | `gcd(2,3)=1` → one closed loop (a knot, not a link) |
| Electron `(2,3)` self-linking | `−6.0001` (= `p·q`) | recovers the integer; the electron's charge-closure integer is recovered |
| Sign = chirality | RH `−6`, LH `+6` | self-linking sign flips with handedness (the charge sign) |

The known electron integer recovers, the Hopf-link and unlinked anchors behave, and
the sign tracks chirality. **The discriminator is interpretable; the FIT/ECHO
verdicts below are not an artifact of a broken tool.**

---

## PART 1 — does the lattice FORCE the electron `p=2`?  →  **FIT / ECHO**

The self-linking ("enclosed helicity") of a `(p,q)` winding is `p·q`, an integer for
EVERY `(p,q)`. The decisive data (driver, fixed `q=3`, plus the sharpening sweep):

| `(p,q)` | single-component (gcd=1)? | self-linking (= `p·q`) | a closed unit-or-more charge? |
|---|---|---|---|
| `(1,1)` | **yes** | `1` | **yes — a unit charge at `p=1`** |
| `(1,2)` | yes | `2` | yes |
| `(1,3)` | yes | `3` | yes |
| `(2,1)` | yes | `2` | yes |
| `(2,3)` (electron) | yes | `6` | yes |
| `(3,3)` | **no** (gcd=3 → 3-component link) | `9` | no (not a single knot) |

**The refutation is `(1,1)`.** A pure unknot with a single toroidal lap and a single
poloidal lap (`p=1`) closes as ONE component and nets self-linking `= 1` — a perfectly
good closed unit-charge loop. The substrate places **no obstruction** on `p=1`
carrying integer charge. (Indeed the electron's *real-space body* IS the `0₁` unknot —
`p=1`-like — per `electron-identification.md:22`.)

So the three PART-1 sub-routes each REFUTE-by-default:

- **(a) NYQUIST-MINIMAL-WINDING — REFUTED.** A `p=1` winding does NOT alias away: it
  closes cleanly and nets an integer. The pre-test physics worry surfaced in the
  prereg was correct — Nyquist sets a *cells-per-wind resolution* floor, NOT a
  *winding-number* floor. A `p=1` loop is fully representable. ≥2-samples-to-resolve
  was conflated with ≥2-windings-to-be-nontrivial. The Nyquist argument does not
  force `p=2`.
- **(b) B-SATURATION→BELTRAMI — does not SELECT `p`.** The Beltrami force-free
  condition `∇×B=λB` admits a winding but is satisfied by `p=1` and `p≥2` alike
  (any closed circulation can be force-free); it is a **consistency container, not a
  forcing** of `p=2`. (The corpus carries the Beltrami framing as a *standing-wave*
  description of the electron at `electron-unknot.md` framing #6, not as a `p`-selector
  — consistent with this finding.)
- **(c) MONOPOLE-DOUBLE-WIND — REFUTED.** A single lap does NOT net zero enclosed
  helicity: `(1,1)` nets `1`, `(1,3)` nets `3`. The "single lap nets zero, so you need
  a double-wind" premise is empirically false in the clean helicity computation.

**What `p=2` ACTUALLY is (the honest corpus reading, `torus-knot-uniqueness.md`).**
`p=2` is forced by **knot-non-triviality minimality**, NOT by charge closure: for the
phase-space winding to be a non-trivial KNOT (not the unknot, not a multi-component
link) you need `gcd(p,q)=1` AND both `≥2`, and the smallest such pair is `(2,3)`.
That is a **minimality selection** ("smallest that holds") — which is precisely a FIT
in the prereg's frozen discriminator #1, not a forcing. The corpus is already honest
about this: `torus-knot-uniqueness.md:127` states *"the knot theory is standard math;
the identification is the AVE physical assertion."* This result CONFIRMS that honest
framing and REFUTES any stronger claim that the substrate forces `p=2` for charge.

> **SYMMETRIC-STANDARD check.** SM does not derive the electron's internal winding at
> all (no internal structure). So AVE is *ahead* in having a structural picture — but
> the specific claim under test ("the lattice FORCES `p=2`") is NOT met; it is a
> minimality assignment. The honest scope is: AVE FORM-derives the winding *skeleton*
> (a non-trivial knot) and SELECTS `(2,3)` by minimality + "electron = lightest
> non-trivial lepton." `p=2` is a **FIT/ECHO**, not a chord.

> **RULE-11 hidden-input check.** The minimality selection of `(2,3)` needs the input
> "electron = lightest stable non-trivial lepton" — i.e. it needs the electron's
> *identity as the ground state*. That is a hidden input: `p=2` is not derived from
> the substrate alone; it is derived from substrate + "this is the lightest one."

---

## PART 2 — quark fractional charge + confinement  →  **FIT / ECHO + CONSISTENCY**

### Q2 — denominator-3 forced?  →  **FIT / ECHO**

The corpus route (`topological-fractionalization.md:12-45`) gets thirds from a `ℤ_N`
permutation symmetry of the Borromean θ-vacuum: `θ ∈ {2πk/N}` → `q_eff = θ/(2π)·e =
k/N`. The driver evaluates this construction for `N ∈ {2,3,4,5}`:

| `N` | `ℤ_N` angles `θ/2π` | fractional charges | denominator |
|---|---|---|---|
| 2 | `0/2, 1/2` | `0, 1/2` | **2** (halves) |
| 3 | `0/3, 1/3, 2/3` | `0, 1/3, 2/3` | **3** (thirds) |
| 4 | `0/4, …, 3/4` | `0, 1/4, 1/2, 3/4` | **4** (quarters) |
| 5 | `0/5, …, 4/5` | `0, 1/5, …, 4/5` | **5** (fifths) |

**The denominator equals `N` for every `N`.** The `ℤ_N` → `1/N` step is generic group
theory; it does NOT prefer `N=3`. `N=3` enters because the **proton is observed to be
a 3-loop (Borromean) structure** — the loop count is read off the proton, then fed in.
So the thirds are **fit to the proton's loop count**, not forced by the substrate. This
is the prereg's frozen discriminator #2 landing on FIT.

> **What WOULD have made it a chord:** if the substrate forced baryons to be exactly
> 3-loop (Borromean) *independently* of observing the proton — e.g. a K4-Cosserat
> stability theorem selecting `N=3` as the minimal stable multi-loop closure. The
> corpus does NOT carry such a theorem (the `6³₂` Borromean is *asserted* as the
> proton's real-space topology, `proton-identification.md:20`; "why exactly 3 loops"
> is not derived). Until that exists, denominator-3 is an echo of the observed proton.

### Q1 / Q3 — confinement forced?  →  **CONSISTENCY** (with one real structural piece)

- **Lone-component self-closure (Q1):** a single component of the symmetric link
  self-links to `0` in the parametric construction — a lone fractional winding does
  NOT self-close to an integer. So "fractional = non-self-closing" is *consistent*.
  BUT this is the `[Q]≡[L]` posit restated (charge = a closed integer winding ⇒ a
  non-closing winding is not an integer charge), not a novel forcing.
- **Borromean pairwise-unlinking (Q3):** the driver confirms the N=3 symmetric link is
  genuinely Borromean-like — **all three pairwise linking numbers are `0`** (`0-1`,
  `0-2`, `1-2` all `≈0`) yet the triple is inseparable. The "remove one → the link
  falls apart" property is **structurally real** in the parametric construction. This
  is the one genuinely substantive piece: it supports the *picture* that no single
  quark can be isolated (remove-one-falls-apart). **BUT** it does not force `N=3`
  (the same pairwise-unlinking can be arranged for other link types), and it inherits
  the `[Q]≡[L]` posit for the charge-closure half. So confinement is **CONSISTENCY**:
  a coherent substrate picture, not a novel forced prediction beyond the posit.

> **SYMMETRIC-STANDARD check.** Confinement is *also* not derived from first principles
> in QCD (it is a conjectured, lattice-observed property; the mass gap is a Millennium
> problem). AVE's topological-irreducibility picture (a stable knot/link cannot
> unlink without infinite energy) is a genuinely appealing *mechanism* and is, in the
> symmetric frame, at least as principled as QCD's. So confinement-as-CONSISTENCY is
> NOT a comedown relative to SM — it is a coherent mechanism that happens not to clear
> the higher bar of "novel forced prediction" set for a CHORD.

### Q4 — up/down split (`+2/3` vs `−1/3`)  →  **FIT / ECHO**

The corpus assigns `θ = +2π/3 → +2/3` (up) and `θ = −2π/3 → −1/3`... but note the
arithmetic: `θ/2π · e` gives `±1/3` for `θ=±2π/3` and `±2/3` for `θ=±4π/3`
(`topological-fractionalization.md:33-43`). Which θ-sector is "up" (`+2/3`) vs "down"
(`−1/3`) is **assigned by hand to match PDG** — there is no substrate-derived reason a
given winding handedness/direction maps to "up." The `n_twist=0` base node assumption
(`topological-fractionalization.md:32`) is also a choice. So the up/down split is a
**FIT/ECHO**: the *set* `{±1/3, ±2/3}` falls out of `ℤ_3` (given `N=3` is chosen), but
the *labeling* of which is up vs down is reverse-engineered to the observed quarks.

---

## 🚩 FLAG-DON'T-FIX — corpus carries TWO incompatible baryon-charge ontologies

Surfaced at prereg, reconfirmed by the PART-2 work. For Grant adjudication; I do NOT
silently pick one.

- **Ontology A (Witten-effect quarks):** `topological-fractionalization.md:12-45` +
  `proton-identification.md:20,43` — the proton's `+1` and the fractional quark
  charges arise via the **Witten Effect on a `ℤ₃` Borromean θ-vacuum**; the three
  Borromean loops ARE the three quarks.
- **Ontology B (no quarks; threaded electron):** `neutron-identification.md:13,22` —
  the neutron is `6³₂ ∪ 0₁` with charge-0 by **literal additive cancellation
  `+1 + (−1)`**, *verbatim* **"NOT Witten-effect quark cancellation"**, and *verbatim*
  **"the corpus uses ZERO udd/uud framing — grep confirmed zero matches for udd."**

These are mutually exclusive ontologies of baryon charge. Ontology B (neutron) treats
baryon charge as integer-additive with the `+1` a single TKI twist at the cage center
(`proton-identification.md:40,67`: *"+1.0 integer topological twist"*) — which is
ALSO how the proton's mass-eigenvalue `+1.0` is sourced. If the proton's `+1` is a
single integer twist (Ontology B / the mass derivation), then the Witten-effect
fractional-quark machinery (Ontology A) is a *parallel, unused* story for the proton —
and the quark fractions are not load-bearing for any AVE mass/charge prediction.

**Consequence for PART 2:** the quark-fractional-charge derivation I scrutinized
(Ontology A) is, by `neutron-identification.md`'s own statement, NOT the ontology the
rest of the baryon sector uses. So even the FIT/ECHO verdict on the thirds is on an
ontology the corpus elsewhere disowns. **This tension should be resolved before the
quark-charge leaf is treated as canonical.** Both file:line citations carried verbatim.

---

## Per-result FORM / VALUE classification (the deliverable axis)

| Result | Class | FORM-forced? | Imported VALUE / fit? |
|---|---|---|---|
| Charge = closed winding integer (`[Q]≡[L]`) — *prior, grounding* | **CONSISTENCY (conditional on the posit)** | the *integer-ness* is FORM (degree theory) given the posit | the posit `[Q]≡[L]` is asserted, not derived (`charge-quantization-gate_result.md` §HONEST SCOPE) |
| **Electron `p=2`** | **FIT / ECHO** | the *non-trivial-knot skeleton* is FORM | `p=2` itself = smallest-coprime **minimality** + "electron = lightest non-trivial lepton" (a hidden input). NOT forced for charge closure (`(1,1)` carries unit charge). |
| **Quark denominator-3** | **FIT / ECHO** | `ℤ_N → 1/N` is FORM (group theory) | `N=3` = **observed** proton loop count, fed in; not forced. |
| **Confinement** | **CONSISTENCY** | Borromean remove-one-falls-apart is a real structural piece | does not force `N=3`; charge-closure half inherits the posit. |
| **Up/down split** | **FIT / ECHO** | the *set* `{±1/3,±2/3}` follows from `ℤ_3` | which θ-sector = "up" is **hand-labeled** to PDG. |

**Net:** the framework FORM-derives the *skeletons* (charge is a closed integer
winding; baryons are multi-loop links; fractions follow from `ℤ_N`) and IMPORTS the
*values* (`p=2` by minimality, `N=3` from the observed proton, up/down by labeling) —
exactly the **FORM-deriving / VALUE-importing** meta-finding the corpus already carries
(`research/2026-06-15_form-deriving-value-importing_meta-finding.md`). This task adds
charge-`p` and quark-fractions as **two more instances** of that pattern, NOT a new
chord.

---

## HONEST SCOPE (do not overclaim)

1. **Parametric, not lattice-field.** The driver computes self-linking on parametric
   `(p,q)` curves (to sidestep the q≲4 lattice-resolution ceiling the prior gate hit,
   `charge-quantization-gate_result.md`). It tests TOPOLOGY (does `p=1` close? does
   `ℤ_N` give `1/N`?), NOT the lattice-field dynamics. A lattice-field confirmation of
   the same conclusions is not in hand and not claimed.
2. **Refute-by-default, not a positive program.** This driver was built to give
   `p=1` / non-3 / free-quark every chance to succeed and report whether they are
   EXCLUDED. They are NOT excluded. This is a clean NEGATIVE result (Rule 11): the
   single mechanism explaining all four FIT/ECHO verdicts is **minimality-and-matched-
   assignment masquerading as forcing** — the same failure mode that sank the prior
   spinor/Hopf route. Branch closes NEGATIVE on the chord question.
3. **NOT a falsification of the charge-as-winding picture.** The `[Q]≡[L]` integer
   picture stands (it is CONSISTENCY-class and a genuine structural advance over QED's
   hand-inserted hypercharge — `charge-quantization-gate_result.md`). What is refuted
   is the *stronger* claim that the lattice FORCES `p=2` / the quark fractions as a
   novel chord.
4. **Witten-effect ontology is internally disputed** (see FLAG above) — the quark
   verdicts are on an ontology `neutron-identification.md` disowns.

---

## Reproduce

```
PYTHONPATH=src python3 -m scripts.vol_2_subatomic.winding_charge_closure
```

Value-echo immunity: the driver imports only the canonical `_gauss_linking_integral`
primitive; no `α` / `-e` / CODATA / `constants` is imported (asserted at module entry
by `_assert_no_value_echo`). Integers + signs only.


