# FROZEN PREREG — Axiom-4 DP-3: derive the CROSS-SECTOR COMBINE RULE (L2-sum vs L∞-first)

**Date:** 2026-07-02
**Lane:** derivation (foundational; DP-3 follow-on to the Axiom-4 reduction epic). Analysis + adversarial verification. NO engine simulation for the combine rule itself (Fork-B: static observables are shape-blind); engine READ permitted to characterize the Op14/H_couple coupling.
**Branch:** `analysis/axiom4-combine-rule` (off `origin/main` @ `c9a1188c`, post-#455 merge)
**Parent:** the Axiom-4 reduction epic (`research/2026-07-02_axiom4-reduction-epic_result.md`, PR #455 MERGED) — verdict FULL-refuted / CONFIRMED-PARTIAL; residual = the cross-sector combine rule; DP-3 = derive it.
**Disciplines fired:** `ave-prereg`, `substrate-native-check`, `pre-test-physics-check`, `consistency-vs-emergence`.

> **SHA-PIN (Rule-16).** The ontology (§1, Grant-collapsed), the discriminator (§3), the acceptance test (§4),
> and the classification axis (§6) are LOCKED before the verdict. Post-verdict change = new prereg.

---

## 0. The question (DP-3, escalated from the epic)

Does the Axiom-4 saturation kernel's argument combine across the three orthogonal A1⊥T2 sectors by the
**L2-sum** (single-radius total, `A²=ε²+κ²+V²`, wall at total A=1, `trampoline-framework.md:249`) or the
**L∞-first** (per-sector "which constitutive parameter saturates first," `photon-ee-mapping.md:47`,
`dual-reactance-storage-taxonomy.md:172`)? The epic showed L∞ is not structurally excluded and the electron
LEANS L∞; Grant ruled this "shouldn't be a single question but a derivation." **This is that derivation.**

## 1. The ontology (Grant-collapsed 2026-07-02, recorded per pre-test-physics-check Step 5)

> **Grant:** the crux — *"is a bond's saturation one shared-energy rupture, or genuinely different per-sector
> failure mechanisms that trip independently?"* — answered: **"the latter, but coupled."**

Locked reading (the derivation's thesis to prove OR break):
- **"the latter"** = **independent per-sector rupture MECHANISMS**, not one shared-budget rupture: T2 (charge)
  = topological self-trap at `V_yield`; A1 (mass) = dielectric bond-snap at `V_snap`; different physics, own
  yields (`def-vyvsn1`, Grant 2026-06-30; `resonant-lc-solitons.md:127`). ⇒ the rupture TRIGGER is **L∞-first in
  per-yield-NORMALIZED coordinates**: `maxᵢ(Aᵢ/yieldᵢ)=1`.
- **"but coupled"** = the grade-orthogonal sectors couple via the **conserved `H_couple`** (energize-lock,
  no-pump, **never a shared `(V_inc,V_ref)` phasor** — the genesis-24 guard, `master-equation.md:20`;
  `resonant-lc-solitons.md:131`). The Op14 cross-block `A²_total=A²_V+A²_ω` (`substrate-perspective-electron.md:66`)
  is the **RAW coupled strain energy** — additive (looks L2). The coupling redistributes raw strain between
  sectors; it does NOT merge their rupture criteria.
- **The reconciliation thesis:** the two corpus ceilings are the SAME event in two coordinate systems —
  **L2-additive in RAW energy** (`A²_total=A²_V+A²_ω`, the H_couple bookkeeping) vs **L∞-first in
  per-yield-NORMALIZED coordinates** (the rupture trigger). **`√α = V_yield/V_snap` is the coordinate
  conversion** between them, and it is *why* the electron confines (T2 normalized-strain hits 1 while A1 raw
  strain sits at √α of `V_snap`). C2 (the epic's flagged contradiction) dissolves as a coordinate artifact —
  IF the thesis holds.

## 2. Corpus state (ave-prereg — anchors, not green field)

| Anchor | Content |
|---|---|
| `substrate-perspective-electron.md:64-70` | `A²_total=A²_V+A²_ω` = "the substrate-level coupling channel (Op14 cross-block) that connects K4 sector dynamics to Cosserat sector dynamics" — the RAW additive coupled strain |
| `resonant-lc-solitons.md:131` | conserved `H_couple`, energize-lock, no-pump, **never a shared phasor**; exact form a live candidate (graft-v3 χ-source / skew-Hermitian circulator, PR#321) |
| `def-vyvsn1` (`vocabulary-register.md:663`, `resonant-lc-solitons.md:127`) | per-sector yields `V_yield=√α·V_snap`; electron A1 core at `A=√α≈0.085`, sub-saturated; **both CALIBRATION not derived** (√α is a value-level α-echo) |
| `photon-ee-mapping.md:47` / `dual-reactance-storage-taxonomy.md:172` | L∞-first: "two mutually-exclusive, self-terminating branches… which constitutive parameter saturates first" (Grant-adjudicated 2026-06-02) |
| `trampoline-framework.md:249` | L2-sum: "S(A) acts on the total — not on any single mode; at A=1 the Γ=−1 wall forms" (single shared `V_SNAP²` normalization per `substrate-perspective:56`) |
| epic result (PR #455) | within-tank L2 forced airtight; combine rule is the residual; L∞ survives; electron leans L∞ |

## 3. The discriminator (LOCKED)

**A combine rule is FORCED iff the coupled-sector structure UNIQUELY selects it AND it reproduces the electron
`√α` operating point.** Three pre-registered outcomes:

- **Outcome A (expected) — L∞-first-normalized / L2-additive-raw; C2 dissolves.** The rupture trigger is
  `maxᵢ(Aᵢ/yieldᵢ)=1` (L∞ in normalized coords); the raw energy `A²_total=A²_V+A²_ω` is L2-additive (the
  H_couple redistribution); `√α` is the exact conversion; the electron confines at T2's yield with A1 raw at √α.
  The corpus's two ceilings are one event in two frames. **The combine-rule STRUCTURE is a theorem** of
  (conservative-coupling + per-sector-yield-rupture + no-shared-phasor); the per-sector yield RATIO `√α` is an
  imported value (α-echo).
- **Outcome B — coupled-JOINT rupture (neither clean L∞ nor L2).** If the H_couple is strong enough that the
  sectors rupture together (the coupling forces co-saturation), the combine is a genuine joint criterion, not a
  per-sector max. This would REFINE (not confirm) the L∞ lean and re-open the residual.
- **Outcome C (null / thesis breaks — retract-don't-refill).** If characterizing the coupling shows it is NOT
  conservative (it pumps) OR requires a shared `(V_inc,V_ref)` phasor (genesis-24 double-count) OR the electron
  `√α` is NOT reproduced by the L∞-first-normalized rule, then "the latter but coupled" does not derive a clean
  combine rule and the residual stays an un-derived posit. Report the negative; do NOT substitute a hoped-for rule.

## 4. Acceptance test (LOCKED — the electron is the ground truth)

The derived combine rule MUST reproduce, with NO per-sector-yield refit beyond the canonical `V_yield=√α·V_snap`:
the electron confines (T2 self-trap, Γ=−1 wall) when the T2 normalized strain reaches 1 **while the A1 core is
sub-saturated at raw strain `A=√α≈0.085` (S≈0.996)**. An L2-sum single-radius sphere keyed to `V_SNAP²` must be
shown to FAIL this test (it would require total A≈1, not √α). This is the discriminator the epic identified;
here it is the pass/fail gate.

## 5. Method / lanes (LOCKED)

- **Analysis + adversarial verification; engine READ permitted** to characterize the Op14/`H_couple` coupling
  (`cosserat_field_3d.py`, the Op14 cross-block) — the epic flagged this as the un-analyzed load-bearing term.
  Small numpy checks (the √α conversion; the L∞-normalized vs L2-sum ray geometry; the electron operating point)
  in agent scratch. NO engine simulation of the combine rule (Fork-B: shape-blind).
- **substrate-native-check:** coupling via `H_couple` ONLY (conservative, energize-lock, no-pump); NEVER a
  shared `(V_inc,V_ref)` phasor (genesis-24 guard); rupture as a Γ=−1 BOUNDARY (CP10), not a bulk force; the
  ε/κ/V tanks are per-sector lossless reactance stores (CP2/6). Flag any Cartesian/SM leak.
- **Adversarial verify (refute-by-default):** the sharpest attack — does the coupling actually recover L2-sum in
  some limit (Outcome B), or does "L∞-first-normalized" only look clean because √α was smuggled in? Independent
  read-AND-run of the electron acceptance test.
- **Flag-don't-fix; retract-don't-refill; do-not-force-a-positive** (Outcome A is seductive — the clean
  coordinate-reconciliation is exactly the pattern to guard against; it must survive the coupling-characterization
  and the electron test, not be assumed).

## 6. Classification commitment (consistency-vs-emergence)

The outcome names what is DERIVED vs IMPORTED. Expected honest split (per `project_form_value_meta_finding` — AVE
forces FORMS, imports VALUES): the **combine-rule STRUCTURE** (L∞-first-normalized / L2-additive-raw) is a
candidate **theorem** of conservative-coupling + per-sector-rupture (Ax1+Ax3 + the H_couple properties); the
per-sector yield **RATIO `√α`** is an imported calibration value (α-echo, `def-vyvsn1`). Do NOT inflate the
structural derivation into a claim that the `√α` value is derived. A Class-B/consistency structural result with a
value-level α-import is the honest ceiling unless the coupling characterization forces more.

## 7. Decision points → back to Grant (do NOT self-resolve)

1. **If Outcome C (thesis breaks)** — the combine rule stays an un-derived posit; report to Grant, do NOT force A.
2. **If Outcome A/B** — the combine-rule wording that lands in the axiom-register `residual_content` (DP-2's held
   re-pin) is Grant's ratify; recommend, hold.
3. **The C2 reconciliation** (raw-L2 / normalized-L∞ as one event) is a candidate corpus repair — recommend,
   Grant rules whether/how to reconcile the `trampoline:249` vs `photon-ee:47` prose.

## 8. Outputs

This prereg (frozen) + `2026-07-02_axiom4-combine-rule_result.md` (the combine-rule derivation, the coupling
characterization, the electron acceptance-test outcome, the C2-reconciliation recommendation, the derived-vs-imported
split). Branch + PR (research doc, NOT a canon change). Report to Grant with the verdict + DP-2's now-resolvable
`residual_content` wording.
