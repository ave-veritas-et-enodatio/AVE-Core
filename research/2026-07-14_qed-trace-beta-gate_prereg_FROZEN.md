# PRE-REG (FROZEN) — QED-TRACE Beta-Function Gate

**Date:** 2026-07-14 · **Branch:** `analysis/qed-trace-beta-gate` · **Worktree HEAD at freeze:** `db06ba82`
**Program:** QED-TRACE (read QED's math as compressed medium data; ontology fence intact).
**Charter card:** the QED-TRACE grounding synthesis (task `wu9i1ev8o`). This gate is the program's
**only chord-class candidate**.

> **FREEZE DISCIPLINE.** This document is pushed as its own commit BEFORE the driver runs. The
> adjudication criteria (§4 bins, §6 gates, §3 register definitions) are frozen here. Post-hoc bin
> re-definition or criterion-dropping to convert ❌→✅ is a Rule-11 violation. Any change after the
> result run lands as a DATED AMENDMENT below the frozen body (frozen bytes untouched; git is the trail).

---

## 0. Anchor + re-verification note

All receipts below were grep/read-re-verified at THIS worktree HEAD `db06ba82` (the charter card was
anchored at `c12f2bdb`, one merge ahead; the receipts I load-bear on reproduce at `db06ba82`). Anchor
drift is flagged, not silently carried.

---

## 1. MISSION + a-priori expectation

**The one question:** does the **kernel-ON** lattice (Axiom-4 saturation active) produce any
**NON-POWER-LAW (logarithmic) scale dependence** in the **effective coupling**, with **QED's sign**
(coupling GROWS at short distance / high energy)?

This is the QED-TRACE program's only chord-class gate. Every other traced structure (propagator =
driving-point impedance, Ward = Noether bookkeeping, gauge = reference freedom) is dictionary/consistency
class and originates no number. The vacuum-polarization "match" is the sole derivation-target, and the
KB itself records it as **ASSERTED, not computed** (`vol2/claim-quality.md:1485-1488`, solidity 0.60,
strengthen-by = literally this gate).

**A-priori expectation (stated up front, per the consensus-bias rail): WRONG-FORM or NULL is the
LIKELY outcome — the category-mismatch verdict.** Rationale, mechanism-level:

- Every scale-dependent object the corpus has actually **computed** is a **power law**: Bloch anisotropy
  `(qℓ)⁴` (`k4-bloch-dispersion-quartic_result.md`), monotone band-edge `R(k)`
  (`srs-vertex-ksweep-backscatter_RESULT.md`), the A44 pair force `p=−3`
  (`lanew-pair-field-form_prereg.md:22`).
- The corpus **already considered and refuted a log route**: "the measured `|φ| ~ r^{−1.4..−2.6}` is 3D
  multipole falloff, **not a 2D log**" (`lanew-pair-field-form_prereg.md:117`).
- The Axiom-4 saturation kernel `S(r) = √(1−(r/r_yield)²)` is **analytic in `r²`** ⇒ its Taylor
  expansion `F(r) = r + ½r³ + …` and the derived pairwise dress
  `Z(r)/Z₀ = 1/(1−(d_sat/r)²)^{1/4}` (`universal_operators.py:229`) are **algebraic in `(d_sat/r)²`** —
  a genuine `ln(q)` cannot emerge from an analytic-in-`r²` kernel by any finite manipulation.
- The one prior driver (`simulate_running_alpha.py:5-10`) collapsed to depth=1 with negligible running
  AND the **wrong sign**.

**A clean WRONG-FORM/NULL is corpus-improving, not a shame result** (Rule 11 honest-closure): it converts
the KB's argued-not-computed "Identical (RT-equivalence)" rows (`q-g20f-vacuum-polarization.md:28,32,47`)
from an unexamined assertion into a **scoped import**, which is exactly the honesty-lag the register
(solidity 0.60, "don't build deeper") already demands. The scoped-import re-tag is routed to the auditor,
not landed here.

**Sector header (as-designed).** MODE: static/quasi-static two-body interaction (force/transfer class)
+ analytic pairwise-dress evaluation. REGIME: cold, **KERNEL ON** (Op14/Axiom-4 saturation active) —
with a **kernel-OFF linear control** (bare Coulomb) as the null. PHASE-STATE: sub-yield reversible
(`|r| < r_yield`; the `r = d_sat` wall is the short-distance endpoint). SECTOR: the graded-Coulomb dress
around a Cosserat (2,q) micro-rotation winding = the charge screening cloud (the winding-pair force IS
the vacuum-polarization-corrected Coulomb law). Platform firewall: analytic Op14 kernel operator
(`universal_pairwise_energy`, clm-gdd70j) as the derivation backbone + `CosseratField3D` seeded-winding
pair (`charge_sector_two_winding.py`) as the empirical anchor. NO new engine.

---

## 2. THE PROBE HIERARCHY (Grant ruling 2026-07-14, incorporated pre-freeze)

The planted bare monopole is a **CLOSED route** — the sourced-charge no-go (`clm-nogo4l`) forbids
SOURCING `div-E` (a static exterior monopole in the translational sector). Its scope guard, verbatim
load-bearing:

> "No claim that charge fails. The claim is that charge is **UNSOURCED** — that no *sourced static
> exterior monopole* emerges … **Topology and pairs remain live.** The winding's `Q = Link(∂Ω,F) ∈ ℤ`
> label (`clm-ze4clw`) is not touched; it lives in the harmonic sector (lane Z) … The inter-winding pair
> force (`clm-wcoul2`, lane W) is **not touched**." (`the-sourced-charge-no-go-cascade.md`, scope guard)

The no-go **leaves the inter-winding pair force explicitly OPEN**. The gate therefore runs the following
re-ranked probe hierarchy:

### (b) ★ SEEDED WINDING PAIR — the NEW PRIMARY probe (Grant's micropolar insight)

**Grant framing (verbatim-faithful, 2026-07-14):** *the sourced-charge no-go forbids SOURCING div-E
(a bare Coulomb monopole planted in the translational sector) — it does NOT forbid SEEDING topological
windings, which is how charge actually exists in this framework. The faithful QED-analog measurement:
seed TWO windings, measure the TRANSFER coupling between them vs separation — the graded Coulomb dress
around each winding IS the screening cloud, so the two-winding force-vs-separation curve is literally the
lattice's vacuum-polarization-corrected Coulomb law. Deviations of its FORM from bare 1/r² vs scale =
the running. Nothing is sourced; windings are legitimate lattice objects, so this sidesteps the no-go
entirely.*

**Instrument:** `charge_sector_two_winding.py` (LANE A PATH-b; seeder = electron-unknot-cosserat-seeder)
for the field-engine leg, and the canonical Op14 pairwise dress `universal_pairwise_energy` (clm-gdd70j)
for the analytic backbone.

**★ COMPUTE / INSTRUMENT DISCLOSURE (receipts — this is heavier than A44, and the existing instrument
has two documented limitations that bound what the field-engine leg can deliver):**

1. **Force-blind-to-charge** (audit `w1ni1axfg`, 2026-06-23, baked into `charge_sector_two_winding.py:20-25`):
   the force path's energy density calls the SYMMETRIC `_reflection_density`
   (`cosserat_field_3d.py:706`); the charge-distinguishing `_reflection_density_asymmetric`
   (κ_chiral·h, `:554`) is NEVER wired into the force. ⇒ like-charge Arm A ≡ achiral Arm C **by
   construction**; the field-engine force is the **generic Op14 saturation form-factor**, not a
   charge-distinct force.
2. **Dispersion-dominated** (same script, `:378-382`): the Cosserat field engine carries the winding
   DOF but NOT the A1 cage, so the windings DISPERSE and the centroid-drift force is
   dispersion-dominated (Arms A≈C HALT). The real charge-distinct chord is explicitly **deferred to the
   unbuilt cage⊗winding engine**.
3. **Sub-decade separation reach:** at box `N≈44`, usable winding separations span `~6–20` cells
   ≈ **0.5 decade** — the field-engine leg CANNOT reach ≥2 decades.

**Consequence for the design (drop-with-disclosure):** the **≥2-decade scale coverage comes from the
analytic Op14 dress** (the derived graded-Coulomb screening cloud, `r/d_sat` from `1.02` to `1000` =
~3 decades). The **field-engine seeded-winding pair provides a sub-decade empirical anchor** confirming
the operator's exponent, run at a compute-bounded subset of separations, with limitations (1)–(3)
disclosed. Both legs are reported KEEP-BOTH. This is the honest reading of "if the full (2,3) seeded pair
is too expensive at multiple separations, say so with receipts and state what subset runs."

### (a) A44 NEUTRAL POLARIZATION FORM-FACTOR — DEMOTED to the cheap CONTROL leg

Measures the neutral dipole response (globally-neutral texture ⇒ monopole = 0 ⇒ dipole-lowest;
`lanew-pair-field-form_prereg.md:22`, `p=−3`). Power-law expected. Retained as the **null-comparator**:
the existing two-tone four-photon form factor (`twotone_formfactor.py`, bulk sep≥3 collapses toward the
`O_skin` skin-suppression = power law). We report the analytic `O_skin` frequency-form-factor exponent
as the live control number and cite the existing bulk result.

### (c) MICROPOLAR POINT-TWIST — CONDITIONAL; RESOLVED BY CANON CHECK → collapses into (b)

**Grant verbatim:** *"wouldn't the micropolar action be the monopole?"* — a bare twist/rotation
point-source, lighter than the full winding. **Gated on one canon check before use:** does the
sourced-charge no-go scope the MICROPOLAR/rotational sector, and do the disclination/Frank quantization
rules forbid an unquantized bare twist?

**Canon-check result (this session, receipts):**
- The no-go is framed entirely on the SOURCED STATIC MONOPOLE in the `div-E`/Gauss **translational**
  sector; a repo grep of `the-sourced-charge-no-go-cascade.md` for `micropolar|rotation|twist|
  disclination|Frank` returns **0 hits** — the no-go does NOT scope the rotational/micropolar sector.
- BUT the rotational sector is **quantized**: winding charge `Q = Link(∂Ω,F) ∈ ℤ` (`clm-ze4clw`;
  `test_winding_charge_closure.py:19,29,34` — self-linking closes to an integer, sign flips with
  handedness; Lane-D `winding-charge-quantization_result`), and the spin/rotation content is the
  **discrete binary-tetrahedral group 2T (order 24)** via `K₄→A₄→2T⊂SU(2)`
  (`electron-unknot-cosserat-seeder.md:72`); charge sign / windings are **Burgers/Frank-analog boundary
  data** (`:85`), i.e. Frank-vector-quantized by the point-group symmetry.
- **Verdict:** a bare UNQUANTIZED continuous twist point-source is **NOT lattice-legal** — the only
  legal twist source is the quantized winding. Therefore, per Grant's own stated fallback, **option (c)
  collapses into option (b): the quantized twist source IS the seeded winding.** (c) is NOT a separate
  probe leg.

**Frozen probe hierarchy: (b) PRIMARY / (a) CONTROL / (c) resolved → (b).**

---

## 3. ★ THE TRANSFER-REGISTER REQUIREMENT (Grant-prompted, load-bearing)

**Requirement (verbatim-class rationale, recorded):** QED's running α is defined off the **scattering
amplitude** — a transduction/through-coupling quantity. A reactive dress can INCREASE local energy
storage while DECREASING through-coupling, **flipping the sign by REGISTER rather than by physics**
(Grant's diagnosis of the prior driver's wrong-sign result: *"is that just reactance into
transduction?"*). Therefore:

**(a) `α_eff(k)` is defined as the TRANSFER reading — a force/scattering-class through-coupling
between two disturbances vs separation/scale:**

> `α_eff^transfer(r) ≡ F(r) · r² / K`, where `F(r) = −dU/dr` is the inter-winding force from the
> graded-Coulomb dress and `K` is the bare coupling. Bare Coulomb `F = K/r²` ⇒ `α_eff^transfer ≡ 1`
> (flat; NO running by construction). Running = scale-dependence of `α_eff^transfer(r)`. Short distance
> (high energy) ↔ `r → d_sat`; long distance ↔ `r ≫ d_sat`. **QED sign = `α_eff^transfer` GROWS as
> `r → d_sat`.**

**(b) ALSO report the REACTIVE/stored-energy reading as a KEEP-BOTH second column per scale:**

> `α_eff^reactive(r) ≡` built from the local impedance/stored-energy dress
> `Z(r)/Z₀ = 1/(1−(d_sat/r)²)^{1/4}` — the SAME register `simulate_running_alpha.py` used
> (`C_eff → Z = √(L/C)` ratio). Reported alongside the transfer column at every scale.

**Fit target (frozen, applied identically to both registers):** map to the QED running form
`1/α_eff(scale) = 1/α_eff(0) − b·ln(scale)` and test log-linearity vs power law. Concretely: fit the
departure `Δ(r) ≡ α_eff(r) − α_eff(r_∞)` against BOTH models —
`M_log: Δ = c·ln(r_ref/r)` and `M_pow: Δ = a·(d_sat/r)^p` — and select by ΔBIC (§6). The QED chord
requires `M_log` selected AND the coefficient sign matching α-grows-at-short-distance AND (for the full
chord) coefficient → `−α/3π`.

**(c) FIRST DELIVERABLE — the `simulate_running_alpha.py` autopsy (its own RESULT section):** determine
which register its `α_eff` was keyed on, and whether its wrong-sign result is a register artifact.
- If its observable was **reactive-class**, say so — that **re-opens the sign question honestly** (the
  wrong sign was a register artifact, not a physics datum).
- If it was **transfer-class**, the wrong-sign result stands as a **physics datum**.
This autopsy is delivered BEFORE any new-physics binning.

---

## 4. THE FIVE FROZEN BINS (verbatim-class from the charter, with consequences)

Binned **on the TRANSFER register** (primary); the reactive column is reported alongside and its own
form/sign noted. The `INCONCLUSIVE-RANGE` bin (§6) can pre-empt any of these if the achieved scale range
cannot statistically separate log from a small-exponent power law.

| Bin | Signature (transfer register) | Consequence (frozen) |
|---|---|---|
| **LOG-EMERGES** | genuine `ln(q)`, QED sign (α GROWS at short distance), coefficient → `−α/3π` | The program's one chord: QED's log IS homogenization data; `clm-bqtasn` strengthen-by closes positive. **RIGHT-FORM / WRONG-COEFFICIENT** sub-case (log, right sign, wrong prefactor) = **FORM-chord / VALUE-echo**, files into the forces-FORMS-imports-VALUES meta-finding. |
| **WRONG-FORM** | power law in `(d_sat/r)` / `(qℓ_node)`, **no log** — the a-priori-expected outcome | Category mismatch CONFIRMED for this route; structure-(1) demotes permanently to dictionary status; the "Identical (RT-equivalence)" rows survive only as a consistency-scaffold appeal → the **scoped-import re-tag is routed to the auditor**. |
| **WRONG-SIGN** | any running with α **WEAKENING** at short distance **ON THE TRANSFER READING** | Fires AGAINST the asserted `q-g20f` sign (which was inherited from the RT appeal, not computed) → triggers demotion of the "Identical (RT-equivalence)" rows. Worse than wrong-form. |
| **NULL-FLAT** | negligible running (the depth=1 collapse repeated) | Category mismatch confirmed at the kernel-ON route too; gate closes; running-α stays imported. |
| **INCONCLUSIVE-RANGE** | the achieved scale range cannot statistically separate log from small-exponent power law (§6 separability gate FAILS) | Gate is honestly INCONCLUSIVE on form; report the range limit; no bin claimed. Fires before any of the above if the discriminator can't resolve. |

**Scope of a null verdict (frozen concession, part of what the gate tests):** a null is scoped to
"**the classical + kernel-ON lattice probed neutrally / via seeded windings**." The **sourced-probe
question stays closed by its own no-go**, not by this gate. The gate does not re-open or re-close the
sourced monopole; it tests only the lattice-legal winding/neutral probes.

---

## 5. INSTRUMENT (extend the #669 ksweep harness; kernel ON; A44 probe pair; transfer coupling ≥2 decades)

Driver: `src/scripts/vol_2_subatomic/qed_trace_beta_gate.py` (new; reuses the #669 ksweep-harness
scale-sweep + fit discipline, the Op14 kernel operator `universal_pairwise_energy`, and the
`charge_sector_two_winding.py` seeded-winding primitives — no new engine).

**Legs (all in the frozen driver):**

1. **PRIMARY (b) — analytic Op14 graded-Coulomb dress, kernel ON.** Sweep `r/d_sat ∈ [1.02, 1000]`
   (~3 decades). At each scale compute `α_eff^transfer(r) = F(r)r²/K` (transfer) AND
   `α_eff^reactive(r)` from `Z(r)/Z₀` (reactive). Fit both against `M_log` vs `M_pow`. Report the
   `Δ(1/α_eff)`-vs-`ln(scale)` table (both registers) and the bin.
2. **PRIMARY (b) empirical anchor — field-engine seeded winding pair, kernel ON.** Run
   `charge_sector_two_winding.run_pair` at a compute-bounded subset of separations (≤~0.5 decade),
   `use_saturation=True`, extract the force-law exponent + the reactance pair (C-state `∫|ω|²`,
   L-state `∫|ω̇|²`). Report with limitations (1)–(3) from §2 disclosed. Confirms the operator's power/no
   free params; does NOT extend the decade reach.
3. **CONTROL (a) — A44 form factor.** Analytic `O_skin` frequency-form-factor exponent across the
   two-tone carrier sweep (power-law null-comparator) + citation of the existing bulk two-tone result.
4. **KERNEL-OFF null control.** Bare Coulomb (`Γ→0`, saturation off): `α_eff^transfer ≡ 1` at all scales
   ⇒ MUST show NO running (fit exponent ≈ 0, no log). If the kernel-OFF control shows running, the
   instrument is broken (gate G-null fires).

**Achieved scale coverage is reported honestly in the RESULT** (the analytic leg reaches ≥2 decades;
the field-engine leg is sub-decade — stated, not hidden).

---

## 6. MACHINE GATES (fire on plants)

| Gate | Test | Fires when |
|---|---|---|
| **G-null (kernel-OFF)** | bare-Coulomb control shows NO running | fit exponent \|p\| > 1e-6 OR `M_log` selected on the linear control ⇒ instrument artifact |
| **G-plant-log** | a synthetic QED-form log `Δ(1/α) = (1/3π)ln(r_ref/r)` injected into the fitter is DETECTED as log with the right sign | fitter fails to select `M_log` or gets the sign wrong on a known log ⇒ fitter is blind |
| **G-plant-pow** | a synthetic power law `Δ = a(d_sat/r)^4` is DETECTED as power law, NOT mis-fit as log | fitter selects `M_log` on a known power law ⇒ fitter over-privileges the log (consensus-bias failure) |
| **G-separability** | at the achieved ≥2-decade range with realistic sampling, ΔBIC between a planted true-log and a planted small-exponent (`p=0.3`) power law exceeds the decisive threshold (\|ΔBIC\|>10) in BOTH directions | if 2 decades cannot separate ⇒ the **INCONCLUSIVE-RANGE** bin exists and fires honestly |

**Model-selection statistic (frozen):** ΔBIC = BIC(M_pow) − BIC(M_log). ΔBIC > +10 ⇒ decisive for
`M_log`; ΔBIC < −10 ⇒ decisive for `M_pow`; |ΔBIC| ≤ 10 ⇒ INCONCLUSIVE. The consensus-bias rail binds:
the fit does NOT privilege the log — G-plant-pow proves the fitter will reject a spurious log, and both
models get the same free-parameter budget (2 each: {c, r_ref-offset} vs {a, p}).

---

## 7. RAILS (frozen)

- **Consensus-bias (binding):** I carry QED priors by training volume. The fit must not privilege the
  log (G-plant-pow enforces). QED actually COMPUTES its log from a quantized-fluctuation postulate the
  classical substrate does not carry — the symmetric standard does NOT rescue an uncomputed match; but a
  clean lattice negative is an ontology difference, not a demerit.
- **No α seeding on the FORM path.** `α` (CODATA) is a legitimate operating INPUT (the coefficient
  target `−α/3π`, the `simulate_running_alpha` reproduction). It is firewalled off the FORM/sign
  determination: the log-vs-power-law verdict is read from the kernel geometry, not from any imported α.
- **Consistency-vs-emergence tags:** the Op14 saturation form-factor is **CONSISTENCY / ECHO**
  (charge-agnostic — same kernel as gravity `K=Gm²` and chemistry `d_sat`=Slater radius;
  `charge_sector_two_winding.py:363-371`, audit `w1ni1axfg`). No emergence claim is headlined. The gate's
  earnable content is the FORM/SIGN category answer, not a value.
- **FORM/VALUE tags** applied throughout. **Pure physics** — no external context in any tracked file.

---

## Discipline skills applied (Posture B reference-walk, pre-build)

- **substrate-native-check:** the transfer coupling is a force-class through-coupling between two Cosserat
  (2,q) micro-rotation windings (the carrier), measured via the Op14/Ax4 saturation kernel — NOT a
  Lagrangian/gradient-descent/continuum-Helmholtz default. The kernel-ON saturation is the only candidate
  all-scales scale-mixing source. K4/Cosserat/Op14 checkpoints walked.
- **pre-test-physics-check:** the plumber-physical question (transfer vs reactive register) was surfaced
  by Grant BEFORE design and is the load-bearing §3 requirement.
- **phase-space-coordinate-check (A46):** the winding-pair force-vs-separation is a REAL-SPACE
  measurement of a REAL-SPACE claim (the graded-Coulomb dress lives in real space); coordinates match
  (A46-clean). No phase-space φ² vs real-space Cartesian mismatch.
- **consistency-vs-emergence:** tagged CONSISTENCY/ECHO (§7); the `simulate_running_alpha` reproduction
  uses CODATA α as operating input (not an emergence claim).
- **verify-before-cite:** every file:line receipt above was grepped this session at `db06ba82`.

---

## Receipts table (grep/read-verified this session at HEAD db06ba82)

| Claim | Receipt |
|---|---|
| Vac-pol match ASSERTED not computed; strengthen-by = this gate; solidity 0.60 | `vol2/claim-quality.md:1485-1488` |
| `q-g20f` asserted sign + "Identical (RT-equivalence)" rows; sub-Compton "α stops running" | `q-g20f-vacuum-polarization.md:28,32,47,55` |
| Log route already refuted in-corpus | `lanew-pair-field-form_prereg.md:117` (+ `:22` p=−3 dipole) |
| Sourced-charge no-go scope guard (charge UNSOURCED; pairs+topology OPEN; lane-W pair force not touched) | `the-sourced-charge-no-go-cascade.md` scope guard (`clm-nogo4l`) |
| Winding charge integer-quantized `Q=Link(∂Ω,F)∈ℤ` | `clm-ze4clw`; `test_winding_charge_closure.py:19,29,34` |
| Rotation content = discrete 2T (order 24) via K₄→A₄→2T⊂SU(2); charge=Burgers/Frank boundary data | `electron-unknot-cosserat-seeder.md:72,85` |
| Op14 pairwise dress `Z/Z₀=1/(1−(d_sat/r)²)^{1/4}`, `U=−(K/r)(T²−Γ²)`, charge-agnostic ECHO | `universal_operators.py:140-234`; `charge_sector_two_winding.py:363-426` (clm-gdd70j, audit w1ni1axfg) |
| Field-engine winding force is force-blind-to-charge + dispersion-dominated | `charge_sector_two_winding.py:20-25,378-382` |
| Prior running-α driver: negligible + WRONG SIGN, depth=1 collapse | `simulate_running_alpha.py:5-10,88` |
| #669 ksweep harness (scale-sweep + fit discipline reused) | `srs_vertex_ksweep_backscatter.py`; `srs-vertex-ksweep-backscatter_RESULT.md` |

---

*Frozen 2026-07-14. Result + autopsy + PR follow in a subsequent commit. Amendments (if any) appended
below this line with date + rationale; frozen body bytes above are untouched.*
