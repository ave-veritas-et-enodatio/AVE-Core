[↑ Orchestration Index](index.md)

# C_eff↑ vs ε_eff↓ inverse-monotonicity root (INVARIANT-S2)

**Lane:** ONE derivation. Arc: corpus-grep prereg → Rule-11 freeze → auditor-gate → derivation → result → adjudicate to Grant.
**Branch:** `analysis/2026-06-15-ceff-epsilon-monotonicity` off `main` (worktree `AVE-Core-ceffeps-wt`). **PR, not merge — main PROTECTED, Grant merges.**
**Status (2026-06-15):** evidence map VERIFIED · derivation DONE · prereg FROZEN · auditor-gate DONE (5 corrections folded — F-A/F-B/F-C; all 6 citations + Lemma verified; flag-don't-fix clean) · Grant-adjudication PENDING.

---

## The target (verbatim canonical pair)

INVARIANT-S2 ([`manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md):58), Axiom-4 dielectric specialization:

> $C_{eff} = C_0/S$, $\quad\varepsilon_{eff} = \varepsilon_0 S$, $\quad\mu_{eff} = \mu_0 S$ &nbsp; where $S = \sqrt{1-(A/A_{yield})^2}$.

As $A\to A_{yield}$ ($S\to0$): $C_{eff}\to\infty$ (↑), $\varepsilon_{eff}\to0$ (↓), $\mu_{eff}\to0$ (↓). **C_eff is the lone ÷S; ε and μ are both ×S.** That asymmetry is the whole question.

## Why it matters (premise — VERIFIED, refined from the brief)

The brief framed this as the root of the capacitive Z→0-vs-Z→∞ contradiction. Grep confirms the premise **and sharpens it**: the contradiction is *intra–electric-sector* and pivots exactly on the C/ε inverse pair.

| Reading | Source | Electric saturation ($S\to0$) gives | Impedance used | Outcome |
|---|---|---|---|---|
| **Z→0 (short, Γ=−1, confinement)** | [`resonant-lc-solitons.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):29-39 (clm-kezk9z) | $C_{eff}=C_0/S\to\infty$ | $Z=\sqrt{\mu_0/C_{eff}}\to0$ | electric sector **confines** |
| **Z→∞ (open, Γ=+1, rupture)** | [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):84 + [`nonlinear-vacuum-capacitance.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md):17 (clm-8nkvwy, clm-vjv4zf) | $\varepsilon_{eff}=\varepsilon_0 S\to0$ | $Z=\sqrt{\mu_0/\varepsilon_{eff}}\to\infty$ | electric sector **ruptures** (τ_yield) |

Same physical event (electric saturation, $S\to0$). Read through **C** → Z→0 confinement; read through **ε** → Z→∞ rupture. The opposite directions exist *only* because `C_eff=C_0/S` and `ε_eff=ε_0·S` move opposite ways. **Premise confirmed.**

The canonical line that makes the inverse pair INTENTIONAL (not hidden), [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):69:
> "the wave speed *increases* as permittivity drops … while the measured capacitance *diverges* ($C_{eff}=C_0/S\to\infty$)."

## Corpus is internally SPLIT on the sign of C_eff (the load-bearing new finding)

The same quantity $C_{eff}(V)$ appears with **opposite monotonicity**, and the split is **ragged — it crosses every layer**, not a clean theory-vs-bench partition (auditor-gate F-B correction):

- **÷S (diverges, ↑):** `C_eff = C_0/√(1−(V/V_yield)²)` — theory: [`nonlinear-vacuum-capacitance.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md):21, [`resonant-lc-solitons.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):32, INVARIANT-S2, `master-equation.md:69`, `entry-point.md:29`; **AND bench/sim/engine:** universal-cell SPICE [`spice-subcircuit.md`](../manuscript/ave-kb/vol4/simulation/ch18-universal-vacuum-cell/spice-subcircuit.md):26 (`Q=C0·V/√…`), falsification predictions [`dielectric-plateau-prediction.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md):27 + [`ee-bench-plateau.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/ee-bench-plateau.md):18, engine `src/ave/topological/cosserat_field_3d.py:411`.
- **×S (rolls off, ↓):** `C_eff = C_0·√(1−(V/V_yield)²)` — [`ee-bench-netlist.md`](../manuscript/ave-kb/vol4/simulation/ch17-hardware-netlists/ee-bench-netlist.md):15, [`simulation/index.md`](../manuscript/ave-kb/vol4/simulation/index.md):24 (`Q = C_0√(…)·V`), [`ch15-autoresonant-breakdown/index.md`](../manuscript/ave-kb/vol4/simulation/ch15-autoresonant-breakdown/index.md):17 ("as $C_{eff}$ **drops**"), [`ch17-hardware-netlists/index.md`](../manuscript/ave-kb/vol4/simulation/ch17-hardware-netlists/index.md):19 ("**rolloff**").

So the corpus carries both signs of $C_{eff}(V)$ **within the same layers** (the SPICE universal cell ÷S, the EE-bench netlist ×S — both in vol4/simulation). This is not an interpretive convention (as FLAG-2 frames it); it is a **literal, large ($1/S^2$), divergent sign discrepancy in the written corpus.**

**Sharpest form (auditor-gate F-A):** the discrepancy lives **under one adjudicated claim id.** `clm-vjv4zf` rules `C_eff=C_0/S` canonical (`vol4/claim-quality.md:70-92`), yet its own Leaf-references footer (`:82`) cites **both** `ee-bench-netlist` (×S) and `spice-subcircuit` (÷S). The claim-quality entry does not notice. That is the concrete defect; the sign is *nominally* adjudicated to ÷S but a ×S leaf rides the same id.

## The existing flag (already deferred)

[`cvr-dc-operating-point.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-dc-operating-point.md):55-57 (AUDITOR_STATE **FLAG-2**):
> "$C_{eff}\to\infty$ (capacitive …) and $\mu_{eff}\to0$ (magnetic …) BOTH give $Z=Z_0\sqrt{S}$; … sector attribution is the open flag. **Magnetic is PRIMARY** per the handoff; the capacitive route is the flagged co-attribution."
> "The $C_{eff}=C_0/S$ ($C\uparrow$) vs $\varepsilon_{eff}=\varepsilon_0 S$ ($\varepsilon\downarrow$) convention pair … is internal to the kernel's dielectric specialization; the $Z=Z_0\sqrt{S}$ trajectory used here is convention-independent."

FLAG-2 routes *around* the pair (Z₀√S is convention-independent — this is what PR #260's wall-fork did) but never resolves whether the pair is a benign convention or a real sign error. **This lane resolves it.** The bench-vs-theory ×S/÷S split (above) shows it is not benign.

## The derivation (constitutive — the discriminator)

**Claim (derived, EE-native):** For ONE nonlinear dielectric cell, the small-signal capacitance $C$ and the small-signal permittivity $\varepsilon$ are bound by the cell geometry, $C = \varepsilon\,(A_{area}/d)$. With $A_{area}, d$ fixed at the $\ell_{node}$ scale, **$C$ and $\varepsilon$ co-move with the same sign, for any constitutive law $Q(V)$.** Worked both ways:

- Saturating-displacement law $D = D_{yield}\sin(\tfrac{\pi}{2}E/E_{yield})$: $\varepsilon_{inc}=dD/dE\to0$ **and** $C_{inc}=dQ/dV\to0$ → both ↓ ⟹ `C_0·S`.
- Soft-mode law $D = \varepsilon_0 E_{yield}\arcsin(E/E_{yield})$: $\varepsilon_{inc}=\varepsilon_0/S\to\infty$ **and** $C_{inc}=C_0/S\to\infty$ → both ↑.

In **neither** standard small-signal case does one rise while the other falls. **Therefore `C_eff=C_0/S` (↑) and `ε_eff=ε_0·S` (↓) cannot both be the small-signal response of one fixed-geometry dielectric cell.** They are consistent only if:

- **(B) different objects** — `C_eff` is the **longitudinal bond compliance** ($C_e \equiv \xi_{topo}^2 k^{-1}$, [`resonant-lc-solitons.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):12, literally $1/k$), which diverges as the bond softens at yield ($k\to0$); `ε_eff` is the **transverse permittivity**, which collapses. Inverse pair is REAL; the Z→0/Z→∞ split is a **name-collision** between $Z_{tank}=\sqrt{L/C}$ and $Z_{wave}=\sqrt{\mu/\varepsilon}$ (both give $|\Gamma|=1$ confinement; they differ only in boundary *phase* — short Γ=−1 vs open Γ=+1).

- **(A) same object → sign error** — `C_eff` IS the dielectric cell capacitance $\varepsilon A/d$. Then the physically-correct saturating sign is $\varepsilon_{eff}=\varepsilon_0 S$ (↓, dipoles max out) ⟹ `C_eff` must be `C_0·S` (↓), the **bench/sim form**. `C_eff=C_0/S` is the **sign error**; fix to `C_0·S`. Consequence: electric saturation drops both → $Z\to\infty$ (rupture) consistently; resonant-lc-solitons' "C→∞→Z→0 confinement" collapses (its premise C→∞ is wrong) and confinement is purely the magnetic branch (μ→0).

**Auxiliary evidence for (A)-flavored trouble:** `C_eff=C_0/S` is **asserted, never derived from a $Q(V)$ law** ("follows directly from the saturation kernel applied to the electric sector", [`nonlinear-vacuum-capacitance.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md):14) — S is placed in the denominator by symmetry with ε's numerator, with the *word* "compliance" as the only justification. The `×S` leaves carry a **different constitutive law** (`C_0·S` / `Q=C_0 S V`), and are themselves muddled secant-vs-incremental (`ee-bench-netlist.md:48` names $dQ/dV=C_{eff}$ the observable, which for $Q=C_0 S V$ diverges) — so they vote "a different law lives here," i.e. the disorder itself.

**Auxiliary evidence for (B):** the substrate genuinely carries a longitudinal-dilatation (A1) sector distinct from the transverse EM sector ([`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):18-20, the A1 "3"); the corpus *names* C_eff a "compliance" (1/stiffness) — TWICE canonically: `resonant-lc-solitons.md:12` ($C_e\equiv\xi^2/k$) and the general **Capacitance↔Compliance Identity** [`topological-kinematics.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md):81-87 ($C=\xi^2\kappa$, $\kappa=1/k$). A compliance ÷S sitting beside moduli ×S is dimensionally the natural pairing.

**The hinge that could collapse the fork (auditor-gate F-C, E10):** [`topological-kinematics.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md):89 — right after defining `C=ξ²/k` (compliance ⟶ B) — states *"Dielectric breakdown occurs when the lattice displacement exceeds its yield limit ($x>\ell_{node}$), which is structurally isomorphic to capacitor voltage exceeding the breakdown threshold,"* **welding the compliance-C's yield to the dielectric breakdown.** If that weld is binding, (B)'s two-objects premise fails and the fork collapses to (A). This single leaf is the most decision-relevant; it is genuinely two-faced and is surfaced for Grant's Q1.

## Discriminator (pre-registered) & recommendation

**Discriminator:** does `C_eff` denote the SAME electric DOF as `ε_eff` (then C must co-move → `C_0/S` is a sign error, fix to `C_0·S`), or a DIFFERENT DOF (longitudinal bond compliance vs transverse permittivity → both correct, name-collision, document)?

**Recommendation to Grant (not a ruling — flag-don't-fix):** the derivation does not by itself pick A vs B; it proves they are the only two survivors and that **the choice is an ontology call about whether the AVE node's LC-tank "C" is the elastic-bond compliance (1/k) or the dielectric capacitance (εA/d).** The corpus currently *says both* ("compliance (capacitance)", `nonlinear-vacuum-capacitance.md:14`) — that synonym is the unadjudicated hinge. Lean: **(B) different-objects is the most corpus-consistent** (C_eff is named a compliance twice canonically — `resonant-lc-solitons.md:12` + the general identity `topological-kinematics.md:81-87` `C=ξ²/k`; A1⊥transverse is canonical). **BUT the lean is checked by the F-C hinge:** `topological-kinematics.md:89` welds the compliance-C's yield to the *dielectric* breakdown — if Grant rules that weld binding, (B) collapses to (A). If (B) holds it REQUIRES (i) renaming `C_0/S` "bond compliance" corpus-wide, (ii) reconciling the ragged ÷S/×S leaves, (iii) cleaning `resonant-lc-solitons.md`'s $\sqrt{\mu_0/C_{eff}}$ slip + wrong-sector confinement.

## Grant's call (the fork — see adjudication block in the result doc)

- **Q1 (ontology — the hinge):** Does the corpus's own weld (`topological-kinematics.md:89`: compliance-C's yield IS dielectric breakdown) make `C_eff=C_0/S` the **same object** as ε (→ SIGN ERROR, fix to `C_0·S`), or is it just the name-collision restated, leaving `C_eff` the bond **compliance** (1/k, distinct DOF — keep `C_0/S`, rename)?
- **Q2 (downstream, follows from Q1):** Is the Z→0/Z→∞ split a name-collision (document the two reactances) or a sign error (delete resonant-lc-solitons' electric-confinement, confinement = magnetic only)?
- **Q3 (bench reconcile):** Are the `×S` leaves (`ee-bench-netlist`, sim-index) a different (dielectric) C, or the corpus already sign-fixing? Note the ÷S/×S split is ragged (it also collides under one claim id, `clm-vjv4zf`).
- **Q4 (independent of Q1):** Flag `resonant-lc-solitons.md:35-39`'s $\sqrt{\mu_0/C_{eff}}$ dimensional slip + electric-sector confinement (contradicts canonical magnetic-branch confinement) for repair?

## Deliverables (this branch)

- This tracker.
- [`research/2026-06-15_ceff-epsilon-monotonicity_prereg_FROZEN.md`](../research/2026-06-15_ceff-epsilon-monotonicity_prereg_FROZEN.md) — Rule-11 frozen discriminator + bins.
- [`research/2026-06-15_ceff-epsilon-monotonicity_result.md`](../research/2026-06-15_ceff-epsilon-monotonicity_result.md) — full constitutive derivation + evidence ledger + adjudication block.

## NOT done in this lane (flag-don't-fix)

No corpus edit applied. No sign flipped, no leaf rewritten, no INVARIANT-S2 change. The ontology is Grant's; the propagation (which is large — ~10+ leaves + INVARIANT-S2 + constants/engine) is a *separate* implementor session gated on his ruling.
