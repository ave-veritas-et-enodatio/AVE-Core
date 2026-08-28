# X44-UNBLOCK — the √S disambiguation and a REACHABLE reconciliation test — FROZEN prereg

**Date:** 2026-08-27 · **Branch:** `research/2026-08-27-x44-unblock` · **Base:** `a3f4fef7`
**Status:** FROZEN by push — pushed as its own commit BEFORE any engine edit, driver,
or test code exists (methods P9–P11 freeze-by-push pattern).
**Replaces:** `research/2026-07-12_x44-komar-source_prereg_FROZEN.md` (byte-untouched;
git is the trail). The prior prereg is superseded, not amended — its bin set had a
structurally unreachable PASS bin (§1).
**Class:** consistency / **CERTIFICATION-class** ledger reconciliation. **No chord.**
α-CLEAN (gravity sector).
**Routing:** ROUTED-TO-GRANT via `_orchestration/open-items/2026-08-27-x44-unblock.md`.

---

<!-- SECTIONS -->

## 0 · Sector header (mandatory)

- **CHANNEL / SECTOR.** **A1 dilatation — gravity / radial-bulk longitudinal.** Strain
  measure `ε₁₁ = 7GM/(c²r)`
  (`manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md:14`,
  verbatim: "The principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ compresses
  the lattice asymmetrically"). Mass = A1 (PR #260/#311) — **untouched by this arc.**
  The EM channel is the matched spectator (`Γ_EM = 0`) and is **out of scope**;
  the Cosserat carrier sector is not addressed.
- **AXIS.** Ledger-register axis: **far-field Gauss flux `m_g`** vs **strain-energy ADM
  label `M_eff = M − U_bind`**. This is a bookkeeping-consistency axis, not a
  carrier axis.
- **PHASE-STATE.** **Static, cold, sub-yield, lossless-reactive.** No port crossed, no
  dissipative channel invoked, no loss word used. The yield wall (`A → 1`) enters
  ONLY as the boundary of the accessible regime (§5) — never as an operating point.
- **DOES THE ENGINE CARRY THE DOF?** YES — `src/ave/gravity/backreaction.py`
  two-way Picard loop over the Stage-1 saturating bulk operator
  `L = Div·diag(D)·Grad` (`src/ave/gravity/gw_propagation.py:700`, verified this
  session: `L = (Div @ Dexp @ Grad).tocsr()`), Dirichlet-zero faces
  (`gw_propagation.py:671-677`).
- **INSTRUMENT CARRIER.** Diamond-K4 Grad/Div (`_build_native_grad_div`,
  `gw_propagation.py:514`) — inherits the `#86` non-canonical instrument (the D1
  production carrier is srs-z=3). **FLAG, do not migrate in this arc** — migration
  is a separate charter, and this prereg's verdicts are stated as carrier-conditional.
- **REAL-SPACE vs PHASE-SPACE (A46).** All quantities REAL-SPACE. Clean.
- **CONSISTENCY vs EMERGENCE (A47).** **CONSISTENCY / CERTIFICATION.** This run does
  not claim emergence of `η`, of `G`, or of the weight. It asks whether two ledger
  registers the engine already computes are mutually consistent, and if not, whether
  the inconsistency is a property of the *weight* or of the *register normalization*.

## 1 · ★ THE PRIOR PREREG'S DEFECT — and the structural change that avoids it

## 2 · What was actually blocking X44: a DEFINITIONAL obstruction

## 3 · THE FROZEN WEIGHT

## 4 · The ledger algebra — exact, before any run

## 5 · ★ THE ACCESSIBLE REGIME, and the demonstration that the PASS bin lies inside it

## 6 · Scope — the 91/9 split, and what this run is NOT about

## 7 · Pre-registered predictions

## 8 · What would FALSIFY the derived weight, in the run's own terms

## 9 · The honest expected outcome — what a non-zero residual would MEAN

## 10 · ★ FROZEN BINS — exact edges, fixed evaluation order

## 11 · ★ NON-TRIVIALITY / STRUCTURAL-NULL GATE

## 12 · ★ ANTI-FITTING GUARD — the k = 1/2 trap, declared in advance

## 13 · Disclosure — what is pre-registered vs what is already measured

## 14 · Method, blind spots, and the completeness statement

## 15 · Out of scope · Deliverables · Gates
