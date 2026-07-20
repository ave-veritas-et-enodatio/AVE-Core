# A1 Amplitude Trace — Result (constitutive identification of the MOND kernel amplitude)

**Date:** 2026-07-20
**Prereg:** [`2026-07-20_a1-amplitude-trace_prereg.md`](2026-07-20_a1-amplitude-trace_prereg.md) (frozen-by-push, this branch)
**Checks:** [`2026-07-20_a1-amplitude-trace_checks.py`](2026-07-20_a1-amplitude-trace_checks.py) (sympy — C1–C4 all PASS)
**Verdict:** **`A = g_N-FORCED`.** The Axiom-4 kernel amplitude at a node in a galaxy's static
gradient-index profile is `A = g_N/a_0` (linear-in-field → the QUADRATIC kernel). #748's canonical
form is CONFIRMED and its amplitude identification upgrades **leaf-asserted → substrate-derived**,
conditional on one corpus-native mapping named explicitly in §5.

**Class (consistency-vs-emergence):** this is a FORM identification (which node coordinate is `A`),
not a value-emergence — **MANIFESTATION / identity-class**. `a_0` itself remains Class-E
operating-point-projection (`mond-hoop-stress.md:13`); this trace does not touch
that. No CODATA/SI value is emergent here; the deliverable is the amplitude's substrate identity.

---

## §0 — Sector header + what #748 left open

**Header (frozen):** A1 dilatation; static / DC operating point; sub-yield lossless-reactive
(Regime I–II, `g_N ≪ a_0` at the SPARC eval radius); galactic scale. DC operating-point
identification, NOT a modal problem.

#748 (`2026-07-20_mond-kernel-adjudication_result.md`, branch `feat/mond-kernel-adjudication`, NOT
yet on `main`) found the two kernels SPARC-DEGENERATE and resolved the FORM to QUADRATIC on the
ground that the leaf's own setup identifies `g_N` as the amplitude. Its R3 note is explicit
[verbatim [sic]]: *"this adjudication canonicalizes the leaf's own identification, it does not derive
it … The substrate-level question (is the drag keyed on the acceleration itself, or on a strain ∝
√g_N?) is SURFACED TO GRANT as an open walk item."* **This trace is that derivation.**

---

## §1 — The static substrate state around a galaxy, in substrate-native terms

`[canon-read]` The gradient-index / trampoline canon
(`einstein-field-equation.md:37,49`, `trampoline-analogy-primer.md` Step 5.5) fixes the static
substrate state around a mass distribution. Enumerate **every** node-level state variable at radius
`r`, so the trace cannot smuggle in the answer by naming only one:

| # | Node-level state variable | Substrate-native identity | Radial form | Character |
|---|---|---|---|---|
| **V1** | local index / impedance offset | `δn ∝ Φ/c²`, `n(r)=1+2GM/(rc²)` (`einstein-field-equation.md:37`) | `∝ 1/r` (potential-like) | **displacement / DC bias level** |
| **V2** | local field = gradient of V1 | `g_N = −∇Φ = GM/r²` (`galactic_rotation.py:116`) | `∝ 1/r²` (gradient of V1) | **field (E-analog)** |
| **V3** | A1 dilatation strain (bond stretch) | `θ ∝ δn ∝ Φ/c²` (dilatational displacement) | `∝ 1/r` (= V1) | **oscillator displacement coord** |
| **V4** | orbital-motion Lorentz strain | `A_v = v/c`, `v²=g_N r` (`trampoline-analogy-primer.md:197`) | `∝ √(g_N r) ∝ √(1/r)` | **kinetic / modal amplitude** |
| **V5** | reactive energy density of the DC field | `∝ g_N²` (field², the ½εE²-analog) | `∝ 1/r⁴` | **energy (= A², not A)** |

Three physical families are present, and they are **not interchangeable**: a **potential/displacement**
family (V1=V3, `∝Φ`), a **field** family (V2, `∝g_N`), and a **kinetic** family (V4, `∝v/c∝√(g_N r)`).
The two prereg candidates map cleanly: **(i) `A=g_N/a_0`** picks the **field** V2; **(ii) `A∝√(g_N/a_0)`**
is the algebraic square-root of the field ratio, whose only physical-amplitude reading is the
**kinetic** V4. The trace must decide which family the kernel's `A` belongs to.

---

## §2 — The kernel's own definition of `A` (canon-read, two independent anchors)

`[canon-read]` **Anchor A — the L2-norm / phase-plane definition** (`common/axiom-register.md:188`,
Axiom-4 provenance): the shape `S(A)=√(1−A²)` is forced by the lossless bond-LC tank conserving
`E = ½CV² + ½Φ²/L`, so the **dynamical phase-plane vector `(V/V_max, Φ/Φ_max)` traces a circle** —
`A = V/V_max` is the **normalized amplitude of the tank's field coordinate** (the voltage/E-side),
and `A² = ½CV²/E` is the **capacitive energy fraction**. **So `A` is FIELD-LIKE (linear in the field
coordinate); `A²` is the energy.** Anything whose *square* is the load (an energy) is `A²`, not `A`.

`[canon-read]` **Anchor B — the DC-operating-point definition** (`ave-kb/CLAUDE.md:75`, INVARIANT-S2
Axiom-4 elaboration): *"`A_0 = V_DC/V_yield` is a per-node ratio (the field across ONE cell `ℓ_node`
relative to the yield FIELD `E_yield = V_YIELD/ℓ_node`)."* I.e. at a **DC operating point**,
`A_0 = V_DC/V_yield = E_local/E_yield` = **field / yield-field**, LINEAR in the field. This is the
matching-regime definition (the galactic node is a DC bias point). The bench realization of exactly
this DC-static row is PONDER-05 / the DC-biased piezoelectric catalog row
(`universal-saturation-kernel-catalog.md:72`), also `V_DC/V_yield`, also linear.

**Both anchors agree:** the kernel's `A` is the **normalized field amplitude** (linear), and the
**energy is `A²`**. This is the L2-norm content, not a stylistic convention.

---

## §3 — The trace: which node-level family is `A`?

**Step 1 `[canon-read]` — exclude the potential/displacement family (V1/V3).** If `A ∝ Φ` (index
depth), the saturation would be keyed on the **potential well**, and the MOND transition would occur
at a fixed Φ-threshold. But `a_0` is empirically and derivationally an **acceleration** threshold
(`mond-hoop-stress.md:34`, `a_0 = c H_∞/(2π) ≈ 1.07e-10 m/s²`), and MOND is an acceleration-keyed
phenomenon (flat curves persist to large `r` where Φ is log-large but `g_N` is small). **V1/V3
excluded** — the amplitude must be a function of the FIELD `g_N`, not the potential Φ. *(This also
excludes the `A_metric = √2·v/c ∝ √Φ` SYM-gravity time-dilation amplitude, whose saturation event is
the BH horizon at `r_s`, `einstein-field-equation.md:49` — a DIFFERENT channel from the MOND drag.)*

**Step 2 `[canon-read]` — the field family (V2) is the E-analog the kernel keys on.** The DC-operating-
point definition (§2 Anchor B) keys `A` on the **field** `E_local = V_DC/ℓ_node` = potential-gradient
across the cell. In gravity the potential is Φ (↔ index/metric), and its gradient is `g_N = −∇Φ` — so
`g_N` is the **exact sector-analog of `E`** (both are `−∇(potential)`; the corpus states this directly
— "Gravity is macroscopic dielectric refraction," `einstein-field-equation.md:76`). The yield field is
the critical acceleration `a_0`. Therefore the field-family amplitude is
`A = E_local/E_yield → g_N/a_0`, **linear in `g_N`.** `[derived]`

**Step 3 `[derived]` — the field reading is L2-norm-consistent; the √g_N reading is not.** With
`A = g_N/a_0`, the energy fraction is `A² = (g_N/a_0)² ∝ g_N²` = the reactive energy density of the DC
field (V5) — exactly the `½εE²`-analog. **Consistent with Anchor A** (A = field, A² = field² = energy).
For reading (ii), `A = √(g_N/a_0)` ⇒ `A² = g_N/a_0 ∝ g_N` (LINEAR) ⇒ the "energy" would be linear in
the field. A reactive/lossless energy `∝ field¹` violates the quadratic reactive-energy structure the
L2-norm axiom rests on — UNLESS the true field-coordinate is some `X` with `X² ∝ g_N`. The only
substrate `X` with `X² ∝ g_N` is the **orbital velocity** (`v² = g_N r`, V4): the **kinetic** family.
So (ii) is only physical if the tank saturates on the **orbital kinetic energy**, not the static field.

**Step 4 `[derived]` — the DC-static framing selects the field over the kinetic.** The kinetic reading
(V4) makes `A` a **modal amplitude** (`v/c` of orbital motion). The prereg header (Grant-walked
2026-07-20) fixes this as a **STATIC / DC operating point — "not a modal problem."** At DC the node
sits in a static field bias; there is no driven orbital oscillation loading the tank. The load is the
static field `g_N` (V2/V5), whose reactive energy is `∝ g_N²`. **The DC-static framing selects the
field family → `A = g_N/a_0`.** `[derived]`

**Step 5 `[derived]` — the kinetic reading additionally fails to normalize to the canonical `a_0`.**
Even granting the kinetic amplitude V4, `A_v = v/c = √(g_N r)/c` uses the **variable `r`**, not the
**constant `a_0`**. Forcing `A_v = √(g_N/a_0)` requires `r = c²/a_0` (check C3), and with
`a_0 = cH_∞/(2π)` that is `r = 2π·(c/H_∞) = 2π·R_Hubble ≈ 8.4×10²⁶ m` — a **cosmic** length, not a
galactic radius. So at galactic `r`, the object `√(g_N/a_0)` is **not** `v/c` and has **no clean
physical-amplitude reading** — it is merely the algebraic square-root of the field ratio. The retired
linear form's kernel argument is thus a bare algebraic operation, not a substrate coordinate. `[derived]`

**Convergence:** four independent lines (L2-norm energy structure, DC-operating-point field/yield-field
definition, `a_0`-as-acceleration, and the kinetic reading's cosmic-scale collapse) all select the
**field** family. `A = g_N/a_0`.

---

## §4 — Where the √g_N object actually lives (relocation, not deletion — Rule 12 spirit)

The `√g_N` in `galactic_rotation.py:135` is a **real and correct** substrate object — it is just
attached to the wrong slot. Two legitimate homes, neither of which is the kernel argument:

1. **The deep-MOND drag PREFACTOR.** `g_drag = √(g_N·a_0)·S(A)`; check C2 gives
   `√(g_N·a_0) = a_0·√A` with `A = g_N/a_0`. So the drag **amplitude** genuinely scales as `√g_N` in
   deep MOND — this is the geometric-mean interpolation that yields flat curves (`v⁴ = GM·a_0`). The
   docstring's "strain ∝ √g_N" is **TRUE of the prefactor.** It becomes the retired linear kernel ONLY
   if the same `√g_N` is (incorrectly) fed to the kernel ARGUMENT (check C1: `√(1−(√(g_N/a_0))²)
   = √(1−g_N/a_0)`).
2. **The SYM-gravity metric / time-dilation amplitude.** `A_metric = √2·v/c ∝ √(g_N r)` is the
   Lorentz-strain of orbital motion whose saturation is the horizon (`einstein-field-equation.md:49`,
   `S = c_shear/c = √(1−r_s/r)`). A real amplitude — for a DIFFERENT channel and event.

The trace's diagnosis: the docstring narrative **conflates the deep-MOND drag prefactor `√g_N` (or the
metric strain) with the saturation-gate argument `A`.** Prefactor and gate are distinct roles; only the
gate is `A`, and the gate is linear `g_N/a_0`.

---

## §5 — FROZEN VERDICT: `A = g_N-FORCED`

**Selected bin: `A = g_N-FORCED`.** `A = g_N/a_0` (linear-in-field) → the QUADRATIC kernel
`S = √(1−(g_N/a_0)²)`.

**The decisive step** is §2 Anchor B + §3 Step 2: the Axiom-4 kernel's amplitude at a **DC operating
point** is *defined* (`ave-kb/CLAUDE.md:75`) as `A = V_DC/V_yield = E_local/E_yield` = **field /
yield-field**, and the gravitational field's sector-analog of `E_local` is `g_N` (both `= −∇potential`;
gravity-as-dielectric-refraction), with yield `a_0`. Linear. The DC-static framing (§3 Step 4) and the
`a_0`-as-acceleration provenance (§3 Step 5) close the two escape routes to the kinetic (√g_N) reading.

**The single named conditional (fail-closed honesty).** The forcing rests on **one** corpus-native
identification: *`g_N` is the A1-tank's DC field-bias (the `E_local`-analog), with `a_0` the yield
field.* This is NOT a fresh posit — it is the standard AVE gravity-as-dielectric-refraction mapping
(`einstein-field-equation.md:76`) plus Axiom-2 scale-invariance (one kernel, all scales, the
field/yield-field grammar of all 26 catalog rows). Under that identification, `A = g_N/a_0` is FORCED
with no free alternative at a DC operating point. **The ONLY way (ii) could win** is the additional
axiom-level statement: *"the galactic MOND drag saturates on the orbital KINETIC energy (a modal `v/c`
amplitude), not on the static field bias"* — which would also require re-deriving `a_0` as a
velocity-scale rather than the critical acceleration `cH_∞/(2π)`. Both the DC-static framing and the
hoop-stress `a_0`-as-acceleration derivation affirmatively exclude that statement. So (ii) is not
merely unsupported; it is **counter-indicated** by two independent canon anchors.

**Anti-anchoring audit (per prereg fence):** the verdict does NOT rest on "everything else does it that
way." Catalog uniformity is CORROBORATING, not load-bearing — the load-bearing chain is the
DC-operating-point `A`-definition (Anchor B) + the L2-norm energy structure (Anchor A) + the kinetic
reading's cosmic-scale collapse (§3 Step 5), each of which would select `g_N/a_0` even with zero other
catalog rows. Reading (ii) was steel-manned to its strongest substrate story (the orbital-Lorentz-strain
V4) and set aside on substrate grounds (Steps 4–5), not on prior grounds.

---

## §6 — Consequence statement (as realized)

**For the #748 canonical form:** CONFIRMED. `g_eff = g_N + √(g_N·a_0)·√(1 − (g_N/a_0)²)` stands; the
amplitude identification `A = g_N/a_0` upgrades from **leaf-setup-asserted → substrate-derived**
(DC-operating-point field/yield-field, `CLAUDE.md:75` + L2-norm energy, `axiom-register.md:188`). #748's
form-level resolution is **not** reopened; it is strengthened. `clm-u86caq`
(`effective-galactic-acceleration-mond.md`, `vol3/claim-quality.md:260`) can be re-tagged
leaf-asserted → derived by the auditor lane. *(This lane does NOT edit the KB — surfaced for landing.)*

**For the R3 docstring follow-on** (`galactic_rotation.py:135`): the sentence *"Orbital shear creates a
strain proportional to √(g_N)"* corrects **TOWARD `A = g_N/a_0`** — exactly as #748 R3 surmised, now
with the derivation it said it lacked. The precise correction: the `√g_N` is the deep-MOND drag
**prefactor** `√(g_N·a_0)` (correct where it is), and must NOT be read as the kernel **argument** `A`
(which is `g_N/a_0`). A future "fix" aligning the *kernel* to the √g_N narrative would silently
re-introduce the retired linear form (check C1) — the trace confirms #748 R3's warning. *(Engine
docstring edit is a routed engine-hygiene follow-on; NOT landed by this research lane per
engine-byte discipline.)*

**For the leaf's derivation-chain status:** `effective-galactic-acceleration-mond.md` — the amplitude
identification is now substrate-derived, not merely leaf-asserted. The QUADRATIC kernel form is the
axiom-forced consequence. (The `a_0` VALUE stays Class-E; the kernel FORM + amplitude are derived. The
framework's usual FORM-derived / VALUE-imported split holds.)

---

## §7 — Deviations + contradictions (flag, don't fix)

- **CORPUS-STATE FLAG (load-bearing context).** The #748 adjudication docs
  (`research/2026-07-20_mond-kernel-adjudication_{prereg,result}.md`) and the QUADRATIC-form KB sweep
  are on branch **`origin/feat/mond-kernel-adjudication`, NOT merged to `main`.** On `main` @ `64f1894d`
  the leaf `effective-galactic-acceleration-mond.md:15` still shows the **LINEAR** form
  `√(1 − g_N/a_0)` with the OPEN 2026-07-19 CONTRADICTION FLAG (`:20-24`) — unresolved on main. This
  trace runs *under* #748 (assumes its QUADRATIC form-resolution lands); its own result (`A=g_N/a_0`)
  is what makes that resolution substrate-derived rather than leaf-asserted. Surfaced so the
  orchestrator sequences the #748 merge + this trace together.
- **CITE-PRECISION FLAG (minor).** #748's R2 erratum places the "strain ∝ √g_N" narrative at
  `galactic_rotation.py:136`. On `main` @ `64f1894d` (and on the feat branch, same base) the sentence
  is verified at **`:135`** (grep, 2026-07-20). Off-by-one; non-load-bearing (the sentence
  demonstrably exists). Flagged, not fixed.
- **SECTOR-FRAMING NOTE (not a contradiction).** The task header assigns A1 dilatation; the engine
  docstring frames the drag as μ-sector "mutual inductance" (`galactic_rotation.py:14,21`); the catalog
  classifies MOND **SYM** (both sectors, `universal-saturation-kernel-catalog.md:51`). The amplitude
  verdict is **sector-invariant**: `A = g_N/a_0` (field/yield-field) is the same whether the saturating
  reactance is the A1 stretch, the μ inductance, or both (SYM). The `√g_N`-vs-`g_N` question is settled
  independently of the ε/μ/A1 sector attribution. No fix needed; noted for completeness.
- **No adjudication-criterion drop.** The frozen bins + selection criteria + anti-anchoring fence are
  exactly as pushed in the prereg; the verdict was reached by the frozen chain, and reading (ii) was
  run as a live possibility (steel-manned in §3–§4) before being set aside.
