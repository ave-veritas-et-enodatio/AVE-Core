# RESULT — Nordtvedt-η (engine-derived η, strain-field register)

**Date:** 2026-07-11 · **Lane:** implementer · **Branch:** `analysis/nordtvedt-eta`
**Status:** acceptance test landed (4 tests; 3 engine_sim legs + 1 gating detector
unit-test; all GREEN, honest). **NOT merged** (Grant merges via reviewed PR).
**FROZEN prereg:** `research/2026-07-11_nordtvedt-eta_prereg_FROZEN.md` (frozen by
push BEFORE any code; commit ordering: prereg `97358a11` → code `e2ae51c7`).
**Class:** consistency / **CERTIFICATION** (η=0 is ENTAILED — see §6). **No chord.**

---

## 0 · One-paragraph summary

The equivalence principle is ONE identity (energy gravitates exactly as energy
resists acceleration — one ledger), probed in TWO registers: (1) **knot-localized**
energy (WEP; vary composition; infinite-CMRR by identity — the EP-CMRR test #650),
and (2) **strain-field-distributed** energy (the gravitational binding energy
`U_bind = ∫½g|∇ε₁₁|²`, in the substrate strain field, in no knot — the **Nordtvedt**
register). This arc derives the Nordtvedt parameter `η` — `(m_g/m_i − 1) = η·f`,
`f = E_grav/E_total = U_bind/(M+U_bind)` — for register-2, by DRIVING the landed
two-way back-reaction solver (`src/ave/gravity/backreaction.py`, #86) over a family
of IDENTICAL rest energy but VARYING binding fraction. The gravitating mass `m_g` is
read FIELD-side (the Gauss flux `Σ_interior(L @ ε₁₁)` of the solved strain through
the source-enclosing interior); the inertial mass `m_i` is the total-energy ledger
`M_matter + U_bind` (a DIFFERENT route). **Verdict: bin (i) — η = +8.3×10⁻⁵ across
f ∈ [0.024, 0.060], well inside the |η| < 1×10⁻³ certification tolerance — the
far-field gravitating charge tracks the total-energy ledger: ONE LEDGER.** The
result is CERTIFICATION-class: η=0 is ENTAILED by the solver's single-`T₀₀^total`
Gauss construction (§6). The value is converting A7's Nordtvedt leg from a retrieval
ASSUMPTION into an engine-CERTIFIED prediction. The detector has teeth (a planted
two-ledger coupling ε=0.10 fires η=0.0999; the ε=0 negative control is null), and a
**flag is surfaced** (the solver's binding-deficit register `M_eff=M−U` disagrees
with its far-field flux `M+U` at O(2f) — a source-ADD vs ledger-SUBTRACT convention
gap; flag-don't-fix, Rule-14, NOT resolved).

---

## 1 · STEP-0 corpus sweep (did anyone already compute η?)

Grep + read of `backreaction.py`, `test_grqed_stage3_backreaction.py`,
`research/2026-06-29_grqed-stage3-backreaction_result.md`, and the docket:

- The #86 arc computes the **binding-DEFICIT** `M_eff = M_matter − U_bind`
  (`effective_mass()`; U_bind ≈ 2–6% of M across the weak band) at a **single
  configuration**. It **never sweeps f, never compares the gravitating vs inertial
  register, never computes or states η.**
- Nordtvedt lives in the corpus only as an **imported LLR bound** (SEP-CMRR ~1e-4,
  `translation-circuit.md:148`) and the **OPEN docket item A7** ("queued for next
  sweep").

**VERDICT: entailed-but-never-stated-or-probed** ⇒ proceed (no HALT), with the
honest P10 framing. (This is the first time the knot-vs-strain-field register
comparison / an η-equivalent is computed and stated.)

## 2 · Substrate-native-check (walked BEFORE numerical code)

- **K4 / stencil.** `|∇ε₁₁|²` (U_bind) AND the field-side flux operator
  `L = Div·diag(tile(D,3))·Grad` use the SAME native diamond-K4 Grad/Div
  (`_build_native_grad_div`) the solver assembles (`gw_propagation.py:698-701`). NO
  Cartesian gradient — the load-bearing K4 checkpoint. (The field-side flux matches
  the source integral to the relaxation residual ~1e-8, confirming Gauss on the
  native operator.)
- **Cosserat sector ownership.** register-2 is the **radial/bulk ε₁₁ channel
  (A1-dilatation)** — the gravitational well's own strain energy. NOT cross-wired to
  shear/EM. Mass = A1-dilatation (PR#260/#311, untouched).
- **Op14.** the ONE kernel `S(A)=(1−A²)^{1/2}`, `D=1/S` (`stiffness_profile`,
  exponent=0.5). NO new kernel.
- **phase-space vs real-space (A46).** every quantity (∫T₀₀, field flux, f,
  monopole plateau) is REAL-SPACE, measured in real-space. A46 clean.
- **consistency-vs-emergence (A47).** CERTIFICATION (η=0 entailed), NOT emergence.
  α-CLEAN (gravity sector; no ALPHA/Q_TANK).

## 3 · The apparatus (Rule-14 — drive the landed solver as-is; NO engine edit)

Reused public entry points **verbatim** (no `src/ave/` module modified; helper +
test in `src/tests/engine_acceptance/`): `backreaction.solve_backreaction`,
`backreaction.gaussian_blob`, `backreaction.field_energy_density`,
`gw_propagation._build_native_grad_div`, `graded_vacuum_network.stiffness_profile`.
The family holds `Σ T₀₀^matter = 4.0` fixed and sweeps σ ∈ {1.4, 1.8, 2.2, 2.6}
(tight→diffuse), so only `f` varies; `f` is DERIVED from the solver's own energy
ledger. The two registers are measured by **different routes**:

| register | route | value |
|---|---|---|
| m_g (gravitating charge) | FIELD-side: `Σ_interior (L @ ε₁₁)` (Gauss flux of the solved strain) | M+U |
| m_i (inertial / total energy) | ENERGY-side: `M_matter + U_bind` (matter rest + strain-field functional) | M+U |

## 4 · LEG-1 — CERTIFICATION (one ledger): **PASS (bin i)**

| σ | f | m_g (field flux) | m_i (M+U) | (m_g−m_i)/m_i | max A | conv |
|---|---|---|---|---|---|---|
| 1.40 | 0.0602 | 4.25214 | 4.25605 | −9.18×10⁻⁴ | 0.194 | ✓ |
| 1.80 | 0.0417 | 4.17028 | 4.17403 | −8.98×10⁻⁴ | 0.133 | ✓ |
| 2.20 | 0.0310 | 4.12448 | 4.12816 | −8.90×10⁻⁴ | 0.101 | ✓ |
| 2.60 | 0.0240 | 4.09468 | 4.09851 | −9.34×10⁻⁴ | 0.079 | ✓ |

- **CERTIFICATION η = +8.28×10⁻⁵** (slope of `(m_g/m_i − 1)` vs f), **< the frozen
  |η| < 1×10⁻³**. The (m_g−m_i)/m_i column is a near-CONSTANT −9×10⁻⁴ offset (the
  boundary-truncation of the field-side interior flux — the outermost Gaussian tail
  sits in the 1-cell Dirichlet layer excluded from the flux sum); because it is
  constant it **cancels in the slope** ⇒ η ≈ 0.
- **Monopole plateau: PASS** — the enclosed flux is radius-independent over the outer
  two enclosing radii (rel change < 0.05) ⇒ a genuine far-field monopole.
- **Field-side Gauss identity: PASS** — `Σ_{r≤R}(L@ε) == Σ_{r≤R}T₀₀^total` per radius
  to < 1×10⁻⁴ (the native-K4 divergence theorem holds on the converged field).
- **All converged, weak field** (max A ≤ 0.19, safely contractive).

**VERDICT: PASS (bin i).** The far-field gravitating charge tracks the total-energy
ledger across the binding-fraction family ⇒ register-2 (strain-field) energy carries
the SAME one ledger ⇒ **AVE certifies the LLR-Nordtvedt null.** (`|η| < 10⁻³` is far
below the imported-observational `|η| ≲ 4.4×10⁻⁴` LLR bound — but per §6 that
comparison is not the point; the null is ENTAILED, not a fitted margin.)

## 5 · P11 (detector teeth) + the mixed-register FLAG

**P11 — planted two-ledger coupling: PASS.** Weighting the field-energy's
contribution to the GRAVITATING register only by (1+ε) (`m_g_planted = m_g + ε·U`,
helper-level, m_i held fixed) is a genuine Nordtvedt coupling (register-2 energy
gravitates ε-more than it weighs):

| arm | η | verdict |
|---|---|---|
| negative control (ε=0) | +8.28×10⁻⁵ | null (< 10⁻³) ✓ |
| planted (ε=0.10) | **+0.09994** | FIRES ≈ ε (|Δ| = 6×10⁻⁵ < PLANT_TOL 0.02) ✓ |

The detector recovers the planted slope and stays null when nothing is planted ⇒ the
η=0 certification is **risked-in-principle**, not a blind zero.

**FLAG (flag-don't-fix; Rule-14 — NOT resolved, engine NOT touched).** Pairing the
far-field flux (M+U, field energy ADDS to the gravitating source) against the
binding-deficit register `M_eff = M−U` (Grant-RULED SUBTRACT 2026-06-29,
`…grqed-stage3-backreaction_result.md:343`) yields **η_mixed = +2.28**. This is **NOT
a physical two-ledger violation** — the one-ledger η=0 holds for EITHER
self-consistent register choice; η≠0 arises ONLY from MIXING the two. It is the
solver's internal **source-side ADD vs ledger-side SUBTRACT** convention gap (the two
mass registers differ at O(2f)). **Surfaced for Grant / the auditor:** whether the
far-field source should carry `+u_field` or `−u_field` to be consistent with the
`M_eff` deficit is a KB/Grant physics question this test EXPOSES but does not
adjudicate (the exposure doubles as a second teeth check — the detector produces
η≠0 from a genuine register difference, so the LEG-1 null is a REAL null). The naive
exterior a+b/r K-fit (diagnostic only, NOT a gate) reads K = [0.332, 0.323, 0.305,
0.277] — it carries the documented #86 finite-source window systematic (a diffuse
blob's tail contaminates the fixed exterior window and under-reads b), which is WHY
the artifact-free Gauss flux, not the K-fit, is the certification instrument.

## 6 · P10 honesty — η=0 is ENTAILED (certify-and-expose)

The solver sources the far field from a **single** energy density
`T₀₀^total = T₀₀^matter + ½g|∇ε₁₁|²`. By the discrete divergence theorem (Gauss) on
the native-K4 operator `L`, the far-field monopole charge = `∫T₀₀^total` = the total
energy content. Reading BOTH registers off this single ledger gives **η=0 by
construction** — so **bin (i) is the expected fire and the run is
CERTIFICATION-class**, per the X36 install-tautology
(`research/2026-07-09_x36-node-bottleneck_result.md:54,89,215`): the engine returns
whatever ledger is installed; the test makes the installed ledger's Nordtvedt-status
VISIBLE — it does not adjudicate whether one-ledger is physically correct.

**Why it is still a genuine (risked-in-principle) certification:** (1) the two
registers are computed by DIFFERENT routes (a field-operator flux vs an
energy-functional ledger) — their agreement is a real cross-check, not a re-quote;
(2) the P11 plant FIRES on a genuine two-ledger coupling (η=ε); (3) the
construction-dependence (bin iii) genuinely manifests as the mixed-register gap
(η=2.28), surfaced as the flag. **VALUE:** A7's Nordtvedt leg becomes an
engine-certified prediction rather than an imported assumption.

## 7 · A7 consequence (ordering) + U6 tension flag

**If η=0 (this result):** A7's Nordtvedt leg is a **derived-null consistency
channel** — the strain-field self-energy register carries the same one ledger, so
the solar-system SEP/Nordtvedt residual from register-2 is null by identity. **A7
then reduces to the ephemerides / EFE-quadrupole channel alone** (the
external-galactic-field-induced quadrupole class the A7 row already names as the
leading observable). **A7's branch-signature freeze should POSTDATE this result** —
recorded here and in the docket continuation.

**FLAG for the auditor (KEEP-BOTH; NOT edited here).** The U6 register row
(`translation-circuit.md:148`) currently reads the SEP self-energy term as a
"nonzero mismatch / both T4 branches REQUIRE a finite value." That wording is in
tension with the ONE-EP carve's engine-certified η=0 one-ledger prediction. Per
KEEP-BOTH the U6 row **stands as-is with a post-η refinement as a gated follow-on**
— the auditor lands any U6 edit; the reframe is "the field-energy register genuinely
EXISTS and is probeable (finite/measurable channel), and it obeys the SAME one
ledger (η=0 mismatch within it)." Surfaced, not resolved.

## 8 · Honest flags + runtime + gates

1. **η=0 is ENTAILED, not a free measurement** (§6) — CERTIFICATION-class, stated
   verbatim; no chord minted.
2. **The frozen `eta_slope` is ref-normalized** (ref = smallest-f member), so it
   recovers a planted slope up to an O(η·f₀) normalization (exact, documented in the
   gating detector unit-test); immaterial to every verdict (η_cert≈0; ε=0.10 → 0.0999
   within PLANT_TOL).
3. **Mixed-register gap** (§5) — surfaced, flag-don't-fix, engine untouched (Rule-14).
4. **U6 tension** (§7) — surfaced for the auditor, KEEP-BOTH, not edited.
5. **Scope:** register-2 (strain-field) only; sub-yield weak field (max A ≤ 0.19,
   provably contractive per #86 §8). NOT the near-yield/BH regime.

**Runtime:** the shared family solve (4 converged two-way solves, N=24) = ~10 s; the
P11 plant + mixed-register flag REUSE it (no extra solve). Same cost+role tier as the
#86 at-risk checks ⇒ the 3 heavy legs register in the `engine_sim` partition
(`conftest.py`); the fast pure-arithmetic detector unit-test STAYS gating.

**Gates:** the 4 Nordtvedt tests GREEN; the engine_acceptance gating-lane suite (91
tests) GREEN; `make verify` PASS. `mass = A1` (PR#260/#311) untouched; α-CLEAN.

---

**Branch:** `analysis/nordtvedt-eta` · **next:** Grant merges via reviewed PR (NOT
merged here). Deliverables: this result + the FROZEN prereg + the acceptance
test/helper + the docket ONE-EP-carve record.
