# RESULT — C_eff↑ vs ε_eff↓ inverse monotonicity: constitutive derivation + adjudication

**Date:** 2026-06-15 · **Prereg:** [`2026-06-15_ceff-epsilon-monotonicity_prereg_FROZEN.md`](2026-06-15_ceff-epsilon-monotonicity_prereg_FROZEN.md) · **Lane:** [`_orchestration/2026-06-15_ceff-epsilon-monotonicity.md`](../_orchestration/2026-06-15_ceff-epsilon-monotonicity.md)
**Classification (consistency-vs-emergence):** corpus-coherence / definitional adjudication. No new physical claim; resolves a sign/ontology ambiguity in an existing axiom specialization. **No empirical discriminator** between the survivors — this is settled by ontology (Grant), not by data.

---

## 1. The pair, exactly

INVARIANT-S2 Axiom-4 dielectric specialization (`CLAUDE.md:58`), with $S(A)=\sqrt{1-(A/A_{yield})^2}$:

$$C_{eff} = \frac{C_0}{S}, \qquad \varepsilon_{eff} = \varepsilon_0 S, \qquad \mu_{eff} = \mu_0 S.$$

As $A\to A_{yield}$, $S\to0$: $C_{eff}\to\infty$, $\varepsilon_{eff}\to0$, $\mu_{eff}\to0$. **ε and μ both ×S; C_eff alone ÷S.**

## 2. The constitutive derivation (the discriminator)

**Lemma (one cell, fixed geometry).** For a single dielectric cell of plate area $A_{area}$ and gap $d$, the small-signal capacitance and permittivity are bound by geometry:
$$C = \varepsilon\,\frac{A_{area}}{d}, \qquad \varepsilon \equiv \frac{dD}{dE}, \qquad C \equiv \frac{dQ}{dV}.$$
With $A_{area}, d$ fixed at the $\ell_{node}$ scale, $C(V) = (A_{area}/d)\,\varepsilon(E)$ — a positive constant times $\varepsilon$. **Hence $C$ and $\varepsilon$ have the same sign of variation, for any constitutive law $Q(V)$ / $D(E)$.** Worked at both extremes of saturable behavior:

| Constitutive law $D(E)$ | $\varepsilon_{inc}=dD/dE$ | $C_{inc}=dQ/dV$ | both → |
|---|---|---|---|
| **saturating displacement** $D=D_{y}\sin(\tfrac{\pi}{2}E/E_{y})$ | $\to 0$ | $\to 0$ | `ε_0·S`, `C_0·S` (↓) |
| **soft-mode** $D=\varepsilon_0 E_{y}\arcsin(E/E_{y})$ | $\varepsilon_0/S\to\infty$ | $C_0/S\to\infty$ | `ε_0/S`, `C_0/S` (↑) |

**In neither standard small-signal case does one rise while the other falls.** The corpus pair (`C_0/S` ↑ with `ε_0·S` ↓) is **not realizable as the small-signal response of a single fixed-geometry dielectric cell.** ∎

Three — and only three — ways out:

### (A) Same object → SIGN ERROR
`C_eff` *is* the dielectric cell capacitance $\varepsilon A_{area}/d$. Physically, a saturating dielectric (dipoles maxing out) has $dD/dE\to0$, so `ε_eff=ε_0·S` (↓) is the **correct** saturation sign. By the Lemma, the SAME cell's capacitance must then be **`C_eff=C_0·S`** (↓). The canonical `C_eff=C_0/S` is a **sign error** (an S misplaced into the denominator by symmetry with ε's numerator). Fix → `C_0·S`. Downstream: electric saturation drops both ε and C → $Z=\sqrt{\mu_0/\varepsilon_{eff}}=\sqrt{L/C_{eff}}\to\infty$ consistently (rupture, Γ=+1); the `resonant-lc-solitons` electric-confinement (Z→0) collapses because its premise ($C\to\infty$) is false; confinement is the **magnetic branch only** (μ→0), as `master-equation.md:85` (clm-lv3uw1) already says.

### (B) Different objects → NAME-COLLISION
`C_eff` is the **longitudinal bond compliance** $C_e\equiv\xi_{topo}^2 k^{-1}$ — asserted twice canonically: `resonant-lc-solitons.md:12` (the electron's $C_e$) and the general **Capacitance↔Compliance Identity** `topological-kinematics.md:81-87` ($C=Q/V=\xi_{topo}^2\kappa$, $\kappa=1/k$) — which **diverges** as the bond softens at yield ($k\to0$). `ε_eff=ε_0·S` is the **transverse dielectric permittivity**, which collapses. Two different DOF of the Cosserat node (longitudinal-elastic vs transverse-EM); the kernel acts on each, giving a reciprocal (compliance ÷S) beside a modulus (permittivity ×S). The inverse pair is **REAL and intended**. The Z→0/Z→∞ "contradiction" is then a **name-collision** between two distinct impedances (§3). Action: rename `C_eff` "bond compliance" wherever it means $1/k$ (stop calling it "capacitance"), and reconcile the bench `C_0·S` leaves as the *dielectric* capacitance (a genuinely different C — see §4).

### (C) Same object, geometry co-moves → GEOMETRY-COMOVE
`C_eff` is the dielectric DOF, but the effective gap $d(S)$ collapses faster than ε drops, so $C=\varepsilon A_{area}/d$ rises while ε falls. Requires a **derived $d(S)$ law** ($d\propto S^2$ would give $C\propto S/S^2=1/S$). No such law exists in the corpus; `master-equation.md:69`'s parenthetical "(thinner dielectric → faster propagation)" gestures at it but derives nothing. Survivable only if Grant asserts a geometric-collapse mechanism; otherwise it reduces to (A) or (B).

## 3. The Z→0/Z→∞ split is boundary-PHASE, not boundary-existence

Under (B), the two readings use different impedances of the same node:
- $Z_{tank}=\sqrt{L_{eff}/C_{eff}}$ — lumped node-resonator. $C_{eff}\to\infty\Rightarrow Z_{tank}\to0$ (**short**, Γ=−1).
- $Z_{wave}=\sqrt{\mu_{eff}/\varepsilon_{eff}}$ — propagating wave. $\varepsilon_{eff}\to0\Rightarrow Z_{wave}\to\infty$ (**open**, Γ=+1).

**Both give $|\Gamma|=1$ → total reflection → confinement.** They differ only in the *phase* of the reflection (short Γ=−1 puts a voltage node at the wall; open Γ=+1 puts a current node). This is why PR #260's wall-fork routed the physical wall through **$Z_0\sqrt S$**, which is convention-independent: the *magnitude* of confinement is the same either way; only "which field antinodes at the wall" flips. So the corpus "contradiction" never threatened the confinement result — it threatened the **boundary type** (short vs open), which is a real physical distinction (it sets which sector — E or B — is clamped at the particle surface) and is exactly the `master-equation` two-branch table (`dual-reactance-storage-taxonomy.md:195-196`): electric branch = open/rupture (Γ=+1), magnetic branch = short/confinement (Γ=−1).

**Cross-check against the canonical two-branch:** `master-equation.md:84-85` already assigns electric→Z→∞ (open) and magnetic→Z→0 (short). That is *consistent with (B)*: the electric sector's **wave** impedance opens (ε↓), the **magnetic** sector's wave impedance shorts (μ↓). The only leaf that breaks this is `resonant-lc-solitons.md:35-39`, which routes electric-sector **confinement** (Z→0) by feeding the lumped `C_eff` into a wave-like $\sqrt{\mu_0/C_{eff}}$ — a **lumped/distributed dimensional slip** ($\mu_0$ [H/m] where $L$ [H] belongs) AND a wrong-sector attribution. **This single leaf is the corpus's actual defect regardless of A/B/C.**

## 4. Evidence ledger (grep-verified 2026-06-15)

| # | Evidence | Points toward |
|---|---|---|
| E1 | `master-equation.md:69` notes the inverse pair explicitly as a feature ("permittivity drops … capacitance diverges") | intended (B or C), not accidental |
| E2 | `nonlinear-vacuum-capacitance.md:14` names it "effective **compliance (capacitance)**" — synonym, unadjudicated | the hinge; supports neither alone |
| E3 | TWO canonical witnesses that the AVE "C" IS the bond compliance $1/k$: `resonant-lc-solitons.md:12` ($C_e\equiv\xi_{topo}^2 k^{-1}$) and the general **Capacitance↔Compliance Identity** `topological-kinematics.md:81-87` ($C=Q/V=\xi_{topo}^2\kappa$, $\kappa=1/k$) | **(B)** |
| E4 | `C_0/S` is **asserted**, never derived from a $Q(V)$ law (`nonlinear-vacuum-capacitance.md:14`) | weakens "derived"; opens (A) |
| E5 | **The corpus literally carries BOTH signs of the same $C_{eff}(V)$, ragged across all layers** (not a clean theory-vs-bench split): **÷S (↑):** theory leaves + universal-cell SPICE `spice-subcircuit.md:26` (`Q=C_0 V/S`) + falsification predictions `dielectric-plateau-prediction.md:27`, `ee-bench-plateau.md:18` + engine `cosserat_field_3d.py:411`. **×S (↓):** `ee-bench-netlist.md:15`, `simulation/index.md:24`, `ch15/index.md:17` ("C_eff drops"), `ch17/index.md:19` ("rolloff") | the pair is **NOT a settled convention** — a real, large ($1/S^2$), divergent discrepancy needing adjudication |
| **E5′** | **F-A locus — the sign contradiction lives UNDER ONE adjudicated claim:** `clm-vjv4zf` rules `C_eff=C_0/S` canonical, yet its Leaf-references footer (`vol4/claim-quality.md:82`) cites **both** `ee-bench-netlist` (×S) and `spice-subcircuit` (÷S). The claim-quality entry does not notice. | the concrete defect; sign is *nominally* adjudicated to ÷S but a ×S leaf rides the same id |
| E6 | ε and μ both ×S (moduli soften); C alone ÷S | (B) (reciprocal = distinct quantity) **or** (A) (misplaced reciprocal) |
| E7 | `master-equation.md:84-85` two-branch already routes electric→Z→∞, magnetic→Z→0 (clm-lv3uw1) | consistent with (B); makes `resonant-lc-solitons` electric-confinement the outlier |
| E8 | FLAG-2 `cvr-dc-operating-point.md:55-57`: "magnetic PRIMARY," C↑/ε↓ a "convention," Z₀√S convention-independent | corpus already *deferred* this; never resolved the sign |
| E9 | `cosserat_field_3d.py` docstring: node = "4-port LC tank with BOTH a nonlinear varactor C_eff AND a nonlinear varinductor L_eff" | tank-lumped framing (B-leaning), but engine builds Z from √(S_μ/S_ε) i.e. √(μ/ε), not √(L/C) |
| **E10** | **The Q1 hinge — `topological-kinematics.md:81-89`** gives `C=ξ²/k` (compliance, ⟶ B) **and then welds** that compliance-C's yield to *dielectric breakdown* (:89, "$x>\ell_{node}$ … structurally isomorphic to capacitor voltage exceeding the breakdown threshold") | **ambiguous / load-bearing both ways** — names C a compliance (B) yet treats compliance-yield AS dielectric-yield (A). This single leaf may already decide Q1; see adjudication Q1. |

**Net:** E3/E7/E9 lean (B); E10 is the hinge that could collapse the fork (if the corpus's own weld of compliance-yield to dielectric-breakdown is taken as binding, the two are one object ⟶ (A)). E5/E5′ are the hard datum: the **opposite sign already exists in the corpus**, ragged across every layer and colliding under one claim id — decisive that the pair is NOT a settled convention. Adjudicate, don't route around.

## 5. Recommendation (flag-don't-fix — Grant rules the ontology)

The derivation does not pick A vs B by itself; it proves they are the **only survivors** (C needs an absent $d(S)$ law) and localizes the choice to a single ontology question: **is the AVE node's LC-tank "C" the elastic-bond compliance $1/k$ (distinct DOF) or the dielectric capacitance $\varepsilon A/d$ (same DOF as ε)?**

- If **compliance** → BIN-NAME-COLLISION: keep `C_0/S`, but rename it "bond compliance" corpus-wide (stop "capacitance"), document the $Z_{tank}$/$Z_{wave}$ collision (§3), and treat the bench `C_0·S` as the *separate* dielectric capacitance.
- If **dielectric capacitance** → BIN-SIGN-ERROR: `C_0/S`→`C_0·S`; the corpus bench layer is then already correct and the theory layer is stale; electric sector ruptures only; magnetic sector is the sole confiner.

**Independent of A vs B:** `resonant-lc-solitons.md:35-39` carries a real defect — the $\sqrt{\mu_0/C_{eff}}$ lumped/distributed slip and the electric-sector confinement that contradicts the canonical magnetic-branch confinement (`master-equation.md:85`). Recommend it be flagged for repair in whichever propagation session follows, regardless of the Q1 ruling.

---

## ADJUDICATION BLOCK (Grant)

> **✅ RESOLVED 2026-06-15 — Q1 = (B)** (Grant, TKI sector picture). `C_comp=C₀/S=1/k` = longitudinal/A1/mass reactance; `ε_eff=ε₀S` = transverse/T2/charge reactance — orthogonal, not the same object; the `:89` weld is a SAME-WALL coincidence, not a same-object identity. Propagation (Tasks 1-4) applied as Rule-12 annotations across INVARIANT-S2 + 7 leaves; **Task 5 (K=2G constitutive) = NEGATIVE → GR-imported** (PR #261, confirmed). One new flag to Grant: the **EE-bench LCR measurement-sector** (spike-vs-rolloff = a (B)-surfaced discriminator). See the lane tracker's [Ratification + propagation log](../_orchestration/2026-06-15_ceff-epsilon-monotonicity.md#ratification--propagation-log-2026-06-15). The original (pre-ratification) fork below is preserved for the audit trail.

> **Q1 — ontology of the LC-tank "C".** The corpus's own hinge (`topological-kinematics.md:89`) says the bond-compliance C's yield *is* dielectric breakdown ("$x>\ell_{node}$ isomorphic to capacitor voltage exceeding breakdown"). Is that weld binding (→ one object → A), or is it just the name-collision restated (→ B)?
> - [ ] **(B) bond compliance** $1/k$, distinct DOF → keep `C_0/S`, rename "compliance," document the name-collision. *(author's lean — most corpus-consistent; survives only if the :89 weld is NOT binding)*
> - [ ] **(A) dielectric capacitance** $\varepsilon A/d$, same DOF as ε (the `:89` weld is binding) → `C_0/S` is a SIGN ERROR, fix to `C_0·S`.
> - [ ] **(C) same DOF, geometry collapses** → I assert a $d(S)$ mechanism (specify): __________
>
> **Q2 — the Z→0/Z→∞ split (follows from Q1):**
> - [ ] name-collision — document two reactances (if B)
> - [ ] sign error — delete `resonant-lc-solitons` electric-confinement; confinement = magnetic only (if A)
>
> **Q3 — the bench/sim `C_0·S` leaves:**
> - [ ] they are the *dielectric* C (legit, different from the compliance) — keep both
> - [ ] they are the already-sign-fixed C; theory `C_0/S` leaves are stale — propagate `C_0·S`
>
> **Q4 — `resonant-lc-solitons.md` slip** (independent of Q1): flag $\sqrt{\mu_0/C_{eff}}$ + wrong-sector confinement for repair? [ ] yes [ ] no
>
> Grant: __________________________  Date: __________
