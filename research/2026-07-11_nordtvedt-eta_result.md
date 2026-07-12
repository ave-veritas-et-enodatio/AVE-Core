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
`M_matter + U_bind` (a DIFFERENT route). **Verdict: bin (i) — the frozen |η| < 1×10⁻³
bin PASSES at every resolution (N=24: +8.3×10⁻⁵; N=32: −6.5×10⁻⁴; N=40: −4.7×10⁻⁴,
§4a), but the BANKING BASIS is the ANALYTIC ENTAILMENT (§6), NOT the numeric leg.**
η=0 is ENTAILED by the solver's single-`T₀₀^total` Gauss construction: the far-field
gravitating charge IS the total-energy ledger by identity. The numeric instrument is
**RESOLUTION-LIMITED** — its own systematic floor (~5–6.5×10⁻⁴ at N=32/40) sits AT the
imported-observational LLR bound |η| ≲ 4.4×10⁻⁴, so the numeric leg ALONE cannot
certify the LLR-Nordtvedt null; it is CONSISTENT with the entailment (N=40 |η| < N=32
⇒ slow convergence toward 0, claimed no further). CERTIFICATION-class; the value is
converting A7's Nordtvedt leg from a retrieval ASSUMPTION into an engine-CERTIFIED
prediction. Detector teeth: the mixed-register leg fires on genuine **SOLVER-FED**
data (η=2.28), and a P11 **SYNTHETIC** ledger-injection separately recovers a planted
slope (ε=0.10 → 0.0999; ε=0 null). A **flag is surfaced and UPGRADED** (§5): the mixed
pairing is the engine's OWN-LABELED pairing — its far field (M+U) disagrees with its
OWN designated ADM mass `M_eff` (M−U, `backreaction.py:33`) at O(2f); #86 never
reconciled the two, so this is a **LATENT #86 DEFECT EXPOSURE** (flag-don't-fix,
Rule-14; the fix is a NAMED future arc).

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
  the source integral to a per-radius RELATIVE residual **~1×10⁻⁶** — measured
  6.7×10⁻⁷ .. 4.4×10⁻⁶, review R5 [the earlier "~1e-8" was the absolute residual,
  mislabeled] — confirming Gauss on the native operator.)
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

- **CERTIFICATION η(N=24) = +8.28×10⁻⁵** (slope of `(m_g/m_i − 1)` vs f), **< the
  frozen |η| < 1×10⁻³**. But this N=24 slope is **statistically UNRESOLVED** — its OLS
  standard error is **8.9×10⁻⁴** (≫ |η|), i.e. consistent with zero AND with the
  larger-N values (§4a). The per-member offsets in the `(m_g−m_i)/m_i` column are
  truncation-shaped (near −9×10⁻⁴, the outermost Gaussian tail sits in the 1-cell
  Dirichlet layer excluded from the flux sum) but the SLOPE is NOT — the earlier
  "constant offset cancels in the slope ⇒ η≈0" reading was an **N=24 accident**
  (review R1), corrected in §4a.
- **Monopole plateau: PASS** — the enclosed flux is radius-independent over the outer
  two enclosing radii (rel change < 0.05) ⇒ a genuine far-field monopole.
- **Field-side Gauss identity: PASS** — `Σ_{r≤R}(L@ε) == Σ_{r≤R}T₀₀^total` per radius
  to < 1×10⁻⁴ (measured 6.7×10⁻⁷ .. 4.4×10⁻⁶; the native-K4 divergence theorem holds
  on the converged field).
- **All converged, weak field** (max A = 0.194 < 0.2 — the frozen REGIME bound,
  restored per review R4; safely contractive).

**VERDICT: PASS (bin i) at every N (all three |η| < the frozen 1×10⁻³) — but the
BANKING BASIS is the ANALYTIC ENTAILMENT (§6), NOT the numeric leg** (review R1/R2).
The certification tolerance 1×10⁻³ does **NOT** undercut the imported-observational
LLR bound `|η| ≲ 4.4×10⁻⁴` — it sits **ABOVE** it (review R2: 1×10⁻³ > 4.4×10⁻⁴), and
the numeric instrument's own resolution floor (~5–6.5×10⁻⁴ at N=32/40, §4a) sits AT
the LLR-bound scale, so the numeric leg ALONE cannot certify the LLR-Nordtvedt null.
What certifies it is the single-`T₀₀^total` Gauss **ENTAILMENT** (§6): the far-field
gravitating charge IS the total-energy ledger by construction, so register-2 energy
carries the SAME one ledger by identity, independent of the numeric floor. The
numeric legs are CONSISTENT with that entailment (N=40 |η| < N=32 ⇒ slow convergence
toward 0; claimed no further).

### 4a · η-vs-N convergence receipt (review R1)

Same physical family (fixed rest energy, `SIGMAS`) at N ∈ {24, 32, 40}; η via the
frozen ref-normalized estimator, with the OLS slope standard error:

| N | f-range | η | slope std-err | max A | fit |
|---|---|---|---|---|---|
| 24 | [0.0240, 0.0602] | +8.28×10⁻⁵ | 8.87×10⁻⁴ | 0.194 | **UNRESOLVED** (se ≫ \|η\|) |
| 32 | [0.0269, 0.0630] | −6.50×10⁻⁴ | 4.13×10⁻⁵ | 0.200 | clean (sign-flipped; **> LLR 4.4×10⁻⁴**) |
| 40 | [0.0287, 0.0647] | −4.74×10⁻⁴ | 4.35×10⁻⁵ | 0.203 | clean (\|η\| < N=32; still ≳ LLR) |

- **N=24 is noise** (se 8.9×10⁻⁴ ≫ |η| 8.3×10⁻⁵) — consistent with 0 AND with the
  larger-N values; the frozen bin passes but the slope is not resolved.
- **N=32/40 are clean fits** (se ~4×10⁻⁵) and NEGATIVE at the ~5–6.5×10⁻⁴ scale — the
  instrument's **resolution-limited systematic floor** (finite-box + finite-source),
  which sits AT/ABOVE the imported LLR bound 4.4×10⁻⁴. So the numeric instrument
  cannot, alone, certify the LLR null.
- **N=40 magnitude (4.74×10⁻⁴) < N=32 (6.50×10⁻⁴)** ⇒ **consistent-with-slow-
  convergence-to-0** (the expected one-ledger limit); claimed no further than
  "consistent-with".
- The N=32/40 points sit at the frozen REGIME edge (max A ≈ 0.200–0.203, the same
  physical family is marginally deeper at higher resolution); the SHIPPED gate runs at
  **N=24** (max A 0.194 < 0.2, inside the frozen sub-yield bound).

**Banking basis: the analytic entailment (§6), not the numeric leg.** The frozen
`_ETA_TOL = 1×10⁻³` is therefore **RESOLUTION-LIMITED** (margin ~1.5–2× over the
~5–6.5×10⁻⁴ floor), NOT the "boundary-truncation-limited, 10× margin" the frozen
prereg table stated — corrected here (deviation-ledger §9, R1b).

## 5 · P11 (SYNTHETIC teeth) + the mixed-register FLAG (LATENT #86 DEFECT)

**P11 — SYNTHETIC ledger-level injection-recovery: PASS.** This is POST-SOLVE LEDGER
ARITHMETIC (disclosed + frozen — not smuggled, NOT a re-solve; review R3): weight the
field-energy's contribution to the GRAVITATING register only by (1+ε)
(`m_g_planted = m_g + ε·U`, helper-level, m_i held fixed). It validates the
**DETECTOR'S injection-recovery arithmetic** — a synthetic ledger-level two-ledger
injection ⇒ η = ε — NOT a solver-fed physical coupling:

| arm | η | verdict |
|---|---|---|
| negative control (ε=0) | +8.28×10⁻⁵ | null (< 10⁻³) ✓ |
| injected (ε=0.10) | **+0.09994** | RECOVERS ≈ ε (|Δ| = 6×10⁻⁵ < PLANT_TOL 0.02) ✓ |

The GENUINE **SOLVER-FED** detector proof is the mixed-register leg below (η=2.2792,
read from the CONVERGED field itself) — that is what makes the LEG-1 null a real null,
not a blind zero.

**FLAG — a LATENT #86 DEFECT EXPOSURE (flag-don't-fix; Rule-14 — engine NOT touched;
the fix is a NAMED future arc).** Pairing the far-field flux (M+U) against the
binding-deficit `M_eff = M−U` yields **η_mixed = +2.2792**. This is **NOT a free
convention choice** (review R6): the "mixed" pairing is **the engine's OWN-LABELED
PHYSICAL pairing** — `backreaction.py:33` designates `M_eff` as the **inertial/ADM
mass**, while the far field provably reads M+U (the `+u_field` source ADD,
`backreaction.py:303-304`). So **the as-built engine's far field disagrees with its
OWN designated ADM mass at O(2f)**, and η_mixed=2.28 IS the engine's current
far-field-vs-inertial-mass statement. #86's own at-risk checks **never reconciled the
two** (all ratio/shape, sign-agnostic —
`test_grqed_stage3_backreaction.py::test_binding_deficit_subtracts_not_adds` asserts
only the `M_eff` DEFINITION; `…grqed-stage3-backreaction_result.md:339` admits the
sign-agnosticism); **this arc is the FIRST reconciliation and it FAILS at O(2f)** ⇒ a
LATENT #86 DEFECT, surfaced for Grant/auditor.

It does **NOT falsify the one-ledger PRINCIPLE** — but the earlier "η=0 holds for
EITHER self-consistent register choice" was **arithmetic relabeling** (review R7):
η=0 is measured **two-route on the ADD side only** (LEG-1: field-flux vs energy
ledger); the SUBTRACT/`M_eff` side has **NO independent field-side route today** (the
flux is pinned to M+U by the +u_field source), so "both = deficit ledger" would
substitute the ledger for the flux, not measure it.

**The three-way resolution (review R8; ★RULED (c) — Grant 2026-07-12; KEEP-BOTH — all
three recorded).** Not the "+u_field vs −u_field" binary: **(a) keep ADD** (far field
= M+U; contradicts the designated ADM mass); **(b) bare −u_field** (makes the Picard
self-energy source sign-indefinite — likely unstable); **(c) ★ RULED — the
ruling-implied reading** of Grant's own 2026-06-29 text ("the positive strain energy is
not a separate ledger to ADD — it is already accounted in the down-regulated
frequency"): source = **REDSHIFT/KOMAR-weighted `T₀₀^matter`** (matter's local clock
`ω√S` down-regulates in the well; the strain energy stays positive but is NOT
separately added — no double-count) → the far field then reads the DEFICIT mass,
reconciling with `M_eff`. **Grant RATIFIED (c) on 2026-07-12**; (a)/(b) stay recorded
(KEEP-BOTH). The engine implementation of the ruled weighting + the #86 gate re-runs +
this η re-run = the **NAMED + AUTHORIZED follow-on arc X44** (docket), which fires
AFTER #651 merges — **NOT this PR** (Rule-14).

The naive exterior a+b/r K-fit (diagnostic only, NOT a gate) reads K = [0.332, 0.323,
0.305, 0.277] — it carries the documented #86 finite-source window systematic (a
diffuse blob's tail contaminates the fixed exterior window and under-reads b), which
is WHY the artifact-free Gauss flux, not the K-fit, is the certification instrument.

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
(2) the mixed-register leg fires the detector on **genuine SOLVER-FED data**
(η=2.28, from the converged field's own register difference), and the P11 SYNTHETIC
injection-recovery separately validates the detector arithmetic (η=ε); (3) the
construction-dependence (bin iii) genuinely manifests as that mixed-register gap,
surfaced as the flag (a LATENT #86 DEFECT, §5). **VALUE:** A7's Nordtvedt leg becomes
an engine-certified prediction rather than an imported assumption. **Honest caveat
(R1):** the certification rests on the ENTAILMENT, not the numeric slope — the numeric
instrument is resolution-limited at the LLR-bound scale (§4a).

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
   verbatim; no chord minted. **Banking basis = the entailment, NOT the numeric leg**
   (§4a): the numeric instrument is resolution-limited at the LLR-bound scale.
2. **The frozen `eta_slope` is ref-normalized** (ref = smallest-f member), so it
   recovers a planted slope up to an O(η·f₀) normalization (exact, documented in the
   gating detector unit-test); immaterial to every verdict.
3. **Numeric η is resolution-limited** (§4a, review R1) — clean N=32/40 slopes are
   NEGATIVE at ~5–6.5×10⁻⁴ (at/above the LLR bound); the frozen |η|<10⁻³ bin passes at
   every N but the numeric leg cannot alone certify the LLR null.
4. **Mixed-register gap = a LATENT #86 DEFECT** (§5, review R6) — the engine's far
   field disagrees with its OWN designated ADM mass at O(2f); surfaced, flag-don't-fix,
   engine untouched (Rule-14); the fix is the NAMED + AUTHORIZED follow-on arc **X44**
   (Grant **RULED (c)** Komar-weighted source, 2026-07-12; three-way, §5).
5. **U6 tension** (§7) — surfaced for the auditor, KEEP-BOTH, not edited.
6. **Scope:** register-2 (strain-field) only; sub-yield weak field (shipped N=24 max
   A = 0.194 < 0.2, provably contractive per #86 §8). NOT the near-yield/BH regime.

**Runtime:** the shared family solve (4 converged two-way solves, N=24) = ~10 s; the
P11 injection + mixed-register flag REUSE it (no extra solve). Same cost+role tier as
the #86 at-risk checks ⇒ the 3 heavy legs register in the `engine_sim` partition
(`conftest.py`); the fast pure-arithmetic detector unit-test STAYS gating. (The §4a
N=32/40 convergence receipt was measured out-of-band — not shipped as a gate.)

**Gates:** the 4 Nordtvedt tests GREEN; the engine_acceptance gating-lane suite (91
tests) GREEN; `make verify` PASS. `mass = A1` (PR#260/#311) untouched; α-CLEAN.

## 9 · Deviation ledger (post-freeze; frozen prereg byte-untouched)

The FROZEN prereg (`…_prereg_FROZEN.md`) is NOT edited. These are dated post-freeze
deviations / corrections, disclosed per the adversarial-review repair round:

| date | ref | deviation / correction | verdict impact |
|---|---|---|---|
| 2026-07-11 | R1b | `_ETA_TOL=1e-3` provenance: frozen table said "boundary-truncation-limited, 10× margin" → **RESOLUTION-LIMITED** (~5–6.5×10⁻⁴ floor at N=32/40; margin ~1.5–2×). Banking basis = analytic entailment. | none (bin passes at every N); framing corrected |
| 2026-07-11 | R2 | §4 headline "\|η\|<10⁻³ far below LLR 4.4×10⁻⁴" was **numerically inverted** (10⁻³ > 4.4×10⁻⁴) → corrected: the tolerance does NOT undercut the LLR bound; the null rests on the entailment. | none; claim corrected |
| 2026-07-11 | R3 | P11 relabeled **SYNTHETIC ledger-level injection-recovery** (post-solve arithmetic); solver-fed teeth credited to the mixed-register leg. | none; wording |
| 2026-07-11 | R4 | `max_A` gate **0.3 → 0.2** (RESTORED to the frozen REGIME bound; family actual 0.194). No silent loosening. | gate tightened (still PASS) |
| 2026-07-11 | R5 | §2 residual "~1e-8" (absolute, mislabeled) → **~1×10⁻⁶** relative (measured 6.7×10⁻⁷ .. 4.4×10⁻⁶). | none; number corrected |
| 2026-07-11 | R5 | `_FLUX_IDENTITY_TOL=1e-4` **post-freeze materialization** (absent from the frozen parameter table) — disclosed; measured residual ≪ tol. | none; new disclosed constant |
| 2026-07-11 | R6 | mixed-register flag **upgraded** to a LATENT #86 DEFECT EXPOSURE (engine's own-labeled ADM mass vs far field; first reconciliation, FAILS at O(2f)). | none; characterization strengthened |
| 2026-07-11 | R7 | "η=0 holds for EITHER register choice" corrected — measured two-route on the ADD side ONLY; deficit side has no field-side route. | none; claim corrected |
| 2026-07-11 | R8 | "+u_field vs −u_field" binary → **three-way** {keep-ADD · bare −u_field · ★Komar/redshift-weighted T₀₀}; engine impl = NAMED follow-on arc. | none; Grant question re-posed |
| 2026-07-11 | R1a | ADDED the η-vs-N convergence receipt (§4a; N=24/32/40 + slope std-errs). | none; new receipt |
| 2026-07-12 | R8/X44 | **Grant RATIFIED option (c)** — Komar/redshift-weighted `T₀₀^matter` source (no-double-count reading of the 2026-06-29 SUBTRACT ruling). Three-way KEEP-BOTH recorded; status "PENDING" → "★RULED (c)". Follow-on arc **X44** NAMED + AUTHORIZED (fires after #651 merges). | none; ratification recorded |

---

**Branch:** `analysis/nordtvedt-eta` · **next:** Grant merges via reviewed PR (NOT
merged here). Deliverables: this result + the FROZEN prereg + the acceptance
test/helper + the docket ONE-EP-carve record. **Named + AUTHORIZED follow-on arc
X44** (out of scope, Rule-14; Grant **RULED (c)** 2026-07-12; fires after #651
merges): implement the ruled Komar/redshift-weighted-source in `backreaction.py` +
re-run the #86 gate suite + GR-recovery + the η family + the mixed-register
reconciliation (η_mixed → 0 expected but GENUINELY FIREABLE — whether the ruled
clock-weighting deficit equals `U_bind` at leading order is a real derivation risk) +
an η_mixed-vs-N convergence gate (the R1 lesson); own prereg.
