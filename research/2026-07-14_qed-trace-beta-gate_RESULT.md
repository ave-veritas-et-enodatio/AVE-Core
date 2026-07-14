# RESULT — QED-TRACE Beta-Function Gate

**Date:** 2026-07-14 · **Prereg (frozen, pushed before run):**
[`research/2026-07-14_qed-trace-beta-gate_prereg_FROZEN.md`](2026-07-14_qed-trace-beta-gate_prereg_FROZEN.md)
· **Driver:** [`src/scripts/vol_2_subatomic/qed_trace_beta_gate.py`](../src/scripts/vol_2_subatomic/qed_trace_beta_gate.py)
· **Output:** `assets/sim_outputs/qed_trace_beta_gate.{json,png}`

---

## TL;DR

**Verdict — bin `WRONG-FORM` (category mismatch CONFIRMED), read on the frozen TRANSFER register.**
The kernel-ON (Axiom-4 saturation) lattice produces a **power-law** scale dependence in the effective
coupling — **no logarithm** — and on the QED-faithful transfer reading the departure has the **wrong
sign** (coupling WEAKENS at short distance). This is the **a-priori-expected, corpus-improving**
outcome (prereg §1): an analytic-in-`r²` saturation kernel cannot emit `ln(q)` **by any finite
manipulation of these pairwise scale-objects** (the many-body scale-integrated route is unprobed, not
closed — §7).

**Two-axis verdict (KEEP-BOTH, #612 pattern; prereg AMENDMENT A2).** The independent review found the
frozen G-null gate is design-defective. Verbatim: *bin `WRONG-FORM` under the amended gate-set
(post-hoc-disclosed); under the frozen gate-set the G-null design defect fires on its own control.* Three
of the four machine gates fire correctly under their frozen wording; the fourth (G-null) fires correctly
**under the amended amplitude criterion**, while the **frozen G-null criterion is design-defective and
fires on its own kernel-OFF control** (see §4). No rescue — the frozen-axis firing is documented as a
design defect, the amended axis as post-hoc.

**The load-bearing new finding (register flip).** The SAME kernel reads **opposite signs in the two
registers**: the TRANSFER (through-coupling / force) reading weakens at short distance (power `p≈4.25`),
while the REACTIVE (stored-energy / impedance-ratio) reading GROWS at short distance (power `p≈2.10`).
Sign is set by **REGISTER, not physics** — exactly Grant's *"is that just reactance into transduction?"*
diagnosis, now demonstrated numerically on one kernel.

**Autopsy verdict (first deliverable): `simulate_running_alpha.py` is REACTIVE-CLASS.** Its wrong-sign
result is a **register + mapping artifact**, not a transfer-class physics datum — this **re-opens the
sign question honestly** (it does not stand as a computed physics sign).

**Class (consistency-vs-emergence): CONSISTENCY / ECHO.** The Op14 saturation dress is charge-agnostic
(same kernel as gravity `K=Gm²` and chemistry `d_sat`=Slater radius; audit `w1ni1axfg`). The earnable
content is the FORM/SIGN **category answer**, not a value. No emergence claim is headlined.

---

## Sector header (as-run)

MODE static/quasi-static two-body force (transfer class) + analytic pairwise-dress evaluation;
REGIME cold, **KERNEL ON** (Op14/Ax4 saturation) with a kernel-OFF (bare Coulomb) null control that
reads flat to `1e-10`; PHASE-STATE sub-yield reversible, fit in the perturbative window `r/d_sat ∈
[3, 3000]` (the QED-running analog: a small departure over many decades, NOT the non-perturbative Pauli
wall at `r=d_sat`); SECTOR the graded-Coulomb dress around a Cosserat (2,q) micro-rotation winding = the
charge screening cloud. Platform: analytic Op14 dress `universal_pairwise_energy` (clm-gdd70j) as the
≥2-decade backbone + `CosseratField3D` seeded-winding pair as a disclosed sub-decade anchor. No new engine.

---

## 1. ★ AUTOPSY — `simulate_running_alpha.py` (first deliverable, per prereg §3c)

**Register verdict: REACTIVE-CLASS.** Its observable chain (docstring `simulate_running_alpha.py:20-27`):

```
C_eff(Δφ) = C_0 / √(1−(Δφ/α)²)         # capacitance = STORED ENERGY (reactive)
Z_eff     = √(L/C_eff) = Z_0·(1−…)^{1/4} # characteristic impedance (reactive)
α_eff     = Z_particle/Z_0  →  α/√(1−strain²)
```

There is **no transmission, no scattering amplitude, no force between two objects** anywhere in that
chain — `α_eff` is the **local reactive dress** (a `√(L/C)` impedance ratio), not a through-coupling.
This gate reproduced its table exactly: `1/α_eff` rises **137.026 (low E) → 137.032 (high E)** = α
weakening with energy = the reported wrong sign.

**Is the wrong sign a register artifact? YES — a DOUBLE artifact:**
1. **Register:** it is keyed on the reactive (stored-energy) register, not the transfer register QED's
   running is defined on.
2. **Mapping:** its scale map is backwards — the strain `α·Σ_{d=1}^{depth} 1/d²` accumulates at LOW
   energy (many hops / large depth), so its `α_eff` is enhanced at LOW energy, which is where the sign
   inverts relative to QED.

**Consequence:** the prior driver's wrong sign is **not a computed transfer-class physics datum** — the
sign question is re-opened honestly. And this gate shows *why the register matters*: on the reactive
register the honest kernel sign is actually α-GROWS-at-short-distance (the "right" QED direction), while
on the transfer register it WEAKENS. The register, not the physics, sets the sign.

---

## 2. THE α_eff(k) TABLE — both registers (KEEP-BOTH), analytic Op14 dress

Scale variable: `d_sat/r` (energy proxy; larger = shorter distance = higher energy). Bare Coulomb
(kernel-OFF) ⇒ `α_eff ≡ 1` at all scales (verified flat to `1e-10`).

| `r/d_sat` | `d_sat/r` (E-proxy) | **α_transfer** | `1/α_tr` | **α_reactive** | `1/α_re` |
|---:|---:|---:|---:|---:|---:|
| 3.00 | 0.3333 | **0.997727** | 1.00228 | **1.029884** | 0.97098 |
| 8.79 | 0.1138 | 0.999973 | 1.00003 | 1.003265 | 0.99674 |
| 30.0 | 0.0333 | 1.000000 | 1.00000 | 1.000278 | 0.99972 |
| 87.9 | 0.0114 | 1.000000 | 1.00000 | 1.000032 | 0.99997 |
| 300  | 0.0033 | 1.000000 | 1.00000 | 1.000003 | 1.00000 |
| 1024 | 0.0010 | 1.000000 | 1.00000 | 1.000000 | 1.00000 |
| 3000 | 0.0003 | 1.000000 | 1.00000 | 1.000000 | 1.00000 |

- **TRANSFER register** (through-coupling `α_eff = F(r)/F_Coulomb(r)`): departs **BELOW 1** — the
  coupling **WEAKENS** at short distance. Fit: **`M_pow`, `p≈4.25`**, `ΔBIC = −473` (power law fits the
  departure ~4 orders better than a log). **WRONG-FORM + wrong sign.**
- **REACTIVE register** (`α_eff ∝ Z(r)/Z_0 = 1/(1−(d_sat/r)²)^{1/4}`, the `simulate_running_alpha`
  register): departs **ABOVE 1** — the coupling **GROWS** at short distance (the "right" QED direction).
  Fit: **`M_pow`, `p≈2.10`**, `ΔBIC = −412`. **WRONG-FORM, right sign.**
- **`register_flip_observed = True`.** Same kernel, opposite sign by register.

Neither register is a logarithm; both are clean power laws. See figure (`qed_trace_beta_gate.png`):
straight lines in log-log confirm power law (a genuine log would curve). The fitted exponents match the
analytic small-`(d_sat/r)` expansion of the Op14 dress: `Z/Z₀−1 ≈ ¼(d_sat/r)²` ⇒ reactive `p=2`, and
`Γ² ≈ (1/64)(d_sat/r)⁴` ⇒ transfer `p=4` (script note "(d_sat/r)^4 departure"). The transfer curve's
far-field points floor near `1e-10` — that is the **central-difference resolution floor** of the tiny
`(d_sat/r)⁴` force departure, not physics; the linear-space (SSE-on-`α−1`) fit is dominated by the
resolved near-wall points, so the floor does not affect `p≈4.25` or the verdict.

---

## 3. Frozen 5-bin classification

| Bin | Fired? | Evidence |
|---|---|---|
| LOG-EMERGES | ✗ | transfer fit selects `M_pow` (`ΔBIC=−473`), not `M_log` |
| **WRONG-FORM** | **✓ (SELECTED)** | transfer register is power-law `p≈4.25`; reactive is power-law `p≈2.10`; A44 control is power-law skin-suppression |
| WRONG-SIGN | ✓ (co-fires; reported as sub-note) | on the transfer reading α WEAKENS at short distance (`α_eff<1`) — fires against the asserted `q-g20f` sign; `WRONG_SIGN_cofires_on_transfer=True`. Folded into the WRONG-FORM headline via a **post-freeze precedence choice** (WRONG-FORM > WRONG-SIGN: a power law is not a genuine log running, so form is the primary category answer). The frozen bin structure did not anticipate both firing simultaneously; the bin was structurally unreachable in the shipped classifier and is now made reachable for the log-with-wrong-sign case (prereg AMENDMENT A2.2). |
| NULL-FLAT | ✗ | departure is non-negligible near the wall (kernel is not inert) |
| INCONCLUSIVE-RANGE | ✗ | separability gate PASSES at 2 decades (see §4) |

**Consequence (frozen, prereg §4):** category mismatch CONFIRMED for the classical + kernel-ON lattice
probed via the seeded-winding dress. Structure-(1) (renormalization = homogenization) **demotes
permanently to dictionary status**; the KB's argued-not-computed "Identical (RT-equivalence)" rows
(`q-g20f-vacuum-polarization.md:28,32,47`, solidity 0.60) survive only as a **consistency-scaffold
appeal**. The **scoped-import re-tag is routed to the auditor** (not landed here — implementer lane).

**Scope of the null (frozen concession).** This null is scoped to *the classical + kernel-ON lattice
probed neutrally / via seeded windings*. The **sourced-probe question stays closed by its own no-go**
(`clm-nogo4l`), not by this gate. Nothing here re-opens or re-closes the sourced monopole.

---

## 4. Machine gates (fire correctly under the amended criteria; the frozen G-null is design-defective and fires on its own control)

| Gate | Test | Result |
|---|---|---|
| **G-null (kernel-OFF)** — AMENDED axis | bare Coulomb amplitude-flat | ✓ max transfer departure `1.1e-10`, reactive `0` (flat) |
| **G-null (kernel-OFF)** — FROZEN axis | frozen §6: `\|p\|>1e-6` OR `M_log` selected on control | ✗ **FIRES (design defect)** — on the flat control the fitter selects `M_log` (`dBIC +198`, absorbing the constant `1.07e-10` `O(h²)` central-difference offset in its free intercept) and `\|p\|=0.3>1e-6` (vacuously true; `P_GRID` floor is 0.3). Model-selection on `1e-10` numerical noise is meaningless. Two-axis KEEP-BOTH per #612; verdict stands on the amended axis (prereg AMENDMENT A2.1). |
| **G-plant-log** | inject QED-form log `(α/3π)ln(r_ref/r)` → detected as log, right sign | ✓ `M_log`, `ΔBIC=+2637`, grows-at-short-distance detected |
| **G-plant-pow** | inject small-exponent power `p=0.3` → detected as power, NOT mis-fit as log | ✓ `M_pow`, `ΔBIC=−3012`, recovered `p=0.300` (consensus-bias: fitter does not privilege the log) |
| **G-separability** | at ≥2 decades, both plants decisively classified (`|ΔBIC|>10`) | ✓ PASS at **2 decades** AND 3 decades ⇒ INCONCLUSIVE-RANGE does not fire |

The fitter is proven able to (a) find a real log, (b) reject a spurious log on a hard `p=0.3` power law,
and (c) separate the two at the achieved range. The WRONG-FORM verdict is therefore not a range artifact.

**Window robustness (self-adversarial live-fire, prereg AMENDMENT A1).** The verdict is
**window-independent**: `WRONG-FORM` + register-flip + transfer-wrong-sign hold on the frozen
`[1.02,1000]` (transfer `ΔBIC=−125`), `[1.1,1000]` (`−207`), `[1.5,1000]` (`−334`), and shipped
`[3,3000]` (`−473`) windows. Only the fitted exponent shifts — the shipped perturbative window gives the
analytically-correct `p≈4`; the frozen wall-inclusive window gives a grid-ceiling `p=8` corrupted by the
non-perturbative Pauli-wall sign-flip (`α_transfer(1.02)≈−7.4`). The category answer (power law, not log)
does not depend on the window. The shipped window change is documented in prereg AMENDMENT A1.

---

## 5. PRIMARY (b) empirical anchor — Cosserat seeded winding pair (disclosed)

Ran `charge_sector_two_winding.run_pair` (kernel ON) at separations `d0 ∈ {6,8,10,12,14}`, `N=40`.
**Exact reproducing invocation** (the `--fe-seps` default is aligned to these 5 separations, so bare
`--with-field-engine` reproduces this table):
```
PYTHONPATH=src python src/scripts/vol_2_subatomic/qed_trace_beta_gate.py --with-field-engine --fe-seps 6 8 10 12 14
```
**All disclosed limitations manifested exactly as receipted (prereg §2):**

- **Sub-decade reach:** 0.37 decades (box-limited) — cannot extend the coverage; the ≥2-decade result
  comes from the analytic dress.
- **Dispersion-dominated:** every arm `dispersed_early=True`; the outward-acceleration proxy `a_init` is
  **non-monotone** (`+0.029, −0.116, −0.167, −0.118, −0.054`), power-law fit `R²=0.15` (uninformative) —
  the centroid-drift force is dispersion-dominated, as `charge_sector_two_winding.py:378-382` documents.
- **Force-blind-to-charge:** the force path uses the symmetric `_reflection_density` (audit
  `w1ni1axfg`), so this leg cannot read a charge-distinct force even if one exists.

The reactance pair was recorded per discipline (C-state `∫|ω|²`, L-state `∫|ω̇|²`) at every separation.
**Reading:** the field-engine leg **confirms the design decision** — a clean transfer-coupling running
cannot be read from the current force-blind + dispersive Cosserat engine; the real charge-distinct chord
remains deferred to the unbuilt cage⊗winding engine. This is an honest negative on the instrument, not
on the physics.

---

## 6. CONTROL (a) — A44 form factor

Analytic `O_skin` skin-suppression across the two-tone carrier sweep: **power-law**, log-log slope
`≈ −16.5` (a steep power law, no log). Consistent with the existing bulk two-tone result
(`research/2026-07-09_twotone-formfactor_result.json`: bulk sep≥3 collapses ~16 orders toward the
`O_skin` skin-suppression). The neutral dipole control is power-law, as predicted — the null-comparator
agrees with the primary verdict.

---

## 7. Honest framing of the negative (Rule 11)

A single mechanism explains the whole result **for the pointwise scale-objects probed here**: the
Axiom-4 saturation kernel is **analytic in `r²`**, so each of the **three computed pairwise objects** —
the pairwise dress `Z/Z₀ = 1/(1−(d_sat/r)²)^{1/4}`, the `F/F_Coulomb` two-body force ratio, and the A44
skin-suppression — is a **finite algebraic composition** (the `A=1` branch point is algebraic order-4,
`(1−u)^{−1/4}`, fractional powers only, no log term) and **cannot be a `ln(q)` by any finite
manipulation**. Verified across windows down to `r/d_sat=1.02` (still decisively `M_pow`, `ΔBIC≈−125`).

**Scope boundary (finding 0 / R3, load-bearing — this is NOT a class statement).** As a *universal
class* claim, "an analytic-in-`r²` kernel cannot emit `ln(q)`" is **false**: logarithms routinely emerge
from analytic kernels via **scale-integration** — QED's own vacuum-polarization `ln(q)` integrates
purely algebraic integrands; a line-superposition of the analytic `1/r` kernel gives `ln r`. The sharper
missing ingredient is therefore **not "quantization" per se** but **scale-integration over a
self-consistent screening hierarchy** — an operation a classical polarizable medium could also possess.
**The gate computed the two-body saturation-dressed force (form-factor class); it never computed the
lattice's many-body screening SUM between the two probes. That many-body scale-integrated
medium-response route is UNPROBED, NOT CLOSED.** The WRONG-FORM bin stands for the probed pointwise
regime; the category-mismatch generalization carries exactly this stated boundary.

This is an **ontology difference for the probed regime, not a demerit**: the gate converts the KB's "AVE
reproduces QED running" from an unexamined assertion into a **scoped import**, exactly the honesty-lag
the register (solidity 0.60, "don't build deeper") already demanded. **Branch closed for the pointwise
two-body route** — no rescue attempted; no post-hoc criterion drop. **The q-g20f scoped-import re-tag
wording (routed to the auditor) must inherit the "many-body scale-integrated route unprobed, not closed"
boundary** before canon propagation.

**Micropolar probe (c) resolution (canon check, prereg §2):** the rotational/micropolar sector is
quantized (winding `Q=Link(∂Ω,F)∈ℤ`, `clm-ze4clw`; discrete 2T order-24 via `K₄→A₄→2T⊂SU(2)`; charge =
Burgers/Frank-analog boundary data), so a bare *unquantized* twist point-source is not lattice-legal —
option (c) collapses into option (b), the seeded winding. Recorded, not run as a separate leg.

---

## 8. Flags (flag-don't-fix — for auditor adjudication)

1. **Routed to auditor:** the scoped-import re-tag of the "Identical (RT-equivalence)" rows
   (`q-g20f-vacuum-polarization.md:28,32,47`) from argued-match to scoped-import. Implementer does not
   land the KB/manuscript entry. **The re-tag wording MUST inherit the §7 boundary:** WRONG-FORM is
   proven for the two-body pointwise pairwise objects (incl. the near-wall); **the many-body
   scale-integrated medium-response (screening SUM between probes) is UNPROBED, NOT CLOSED** — the re-tag
   must not read as closing the log route in general.
2. **Register-discipline finding is generalizable:** any AVE "running/screening" claim read off a
   reactive (stored-energy/impedance) observable inherits the sign-by-register ambiguity. The transfer
   register is the QED-faithful one; the reactive register reads the opposite sign on this kernel.
   Surfaced for the auditor as a cross-cutting note (not landed).
3. **Anchor drift (carried, not resolved):** the charter card was anchored at `c12f2bdb`; this gate ran
   at worktree HEAD `db06ba82`. All load-bearing receipts were re-verified at `db06ba82`.

---

## References (grep/read-verified this session at HEAD db06ba82)

- Prior driver register + wrong sign — `src/scripts/vol_2_subatomic/simulate_running_alpha.py:5-10,20-27,88`
- Op14 pairwise dress — `src/ave/core/universal_operators.py:140-234` (clm-gdd70j)
- Seeded-winding instrument + disclosed limits — `src/scripts/vol_1_foundations/charge_sector_two_winding.py:20-25,363-426,378-382` (audit w1ni1axfg)
- Sourced-charge no-go scope (pairs/topology OPEN) — `manuscript/ave-kb/common/the-sourced-charge-no-go-cascade.md` (clm-nogo4l)
- Winding quantization — `clm-ze4clw`; `src/tests/test_winding_charge_closure.py:19,29,34`; `electron-unknot-cosserat-seeder.md:72,85`
- Vac-pol match ASSERTED not computed — `manuscript/ave-kb/vol2/claim-quality.md:1485-1488`; `q-g20f-vacuum-polarization.md:28,32,47,55`
- Log route already refuted — `research/2026-07-03_lanew-pair-field-form_prereg.md:117,22`
- #669 ksweep harness (extended) — `src/scripts/vol_1_foundations/srs_vertex_ksweep_backscatter.py`
