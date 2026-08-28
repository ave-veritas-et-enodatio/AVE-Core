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

### 1.1 · The defect, stated exactly

The superseded prereg
(`research/2026-07-12_x44-komar-source_prereg_FROZEN.md`, read in full this session)
froze four bins keyed on a single number
(`:150-153`): the PASS bin **(i) RECONCILED** required
`|η_mixed| < 1×10⁻³`, and every other bin was defined by its complement.

**That PASS bin was not reachable by the frozen configuration.** The arc discovered
this itself, in a post-review repair — `research/2026-07-12_x44-komar-source_result.md:84-95`
(§4b), verbatim:

> "In the **frozen family** (`g_self=1.0`, `max A < 0.2`) only bins **(iii)/(partial)**
> were structurally reachable … so RECONCILE (`|η_mixed| < 1×10⁻³`) required
> `Δ_clock/U ~ 1` ⇒ `f ~ 0.6`, **~10× outside the frozen regime**."

So the verdict was fixed by the freeze, not by the substrate. Bin (iii)
UNRECONCILED could not have failed to fire.

### 1.2 · It is worse than "~10× outside the frozen regime"

Measured this session (`research/drivers/x44_unblock_regime_map.py`, N=24, σ=1.8,
`g_self=1.0`, `S_min=1e-3`, amplitude scanned over a **96× rest-energy range**):

| λ | M | max A | U_bind | U/M | **f** | converged |
|---|---|---|---|---|---|---|
| 0.25 | 1.000 | 0.0329 | 0.0104 | 0.0104 | 0.0103 | True |
| 0.50 | 2.000 | 0.0658 | 0.0416 | 0.0208 | 0.0204 | True |
| 1.00 | 4.000 | 0.1310 | 0.1656 | 0.0414 | 0.0397 | True |
| 2.00 | 8.000 | 0.2575 | 0.6480 | 0.0810 | 0.0749 | True |
| 4.00 | 16.000 | 0.4830 | 2.3873 | 0.1492 | 0.1298 | True |
| 6.00 | 24.000 | 0.6584 | 4.7552 | 0.1981 | 0.1654 | True |
| 8.00 | 32.000 | 0.7827 | 7.3060 | 0.2283 | **0.1859** | True |
| 12.00 | 48.000 | **1.0000** | 10.6108 | 0.2211 | 0.1810 | **False** |
| 16.00 | 64.000 | **1.0000** | 14.1658 | 0.2213 | 0.1812 | **False** |
| 24.00 | 96.000 | **1.0000** | 21.4317 | 0.2232 | 0.1825 | **False** |

**`f` is NON-MONOTONE in amplitude. It peaks at `f = 0.1859` (λ=8, `max A = 0.783`,
converged) and then TURNS OVER** — beyond λ≈8 the core pins against the yield cap
`A = 1`, the Picard loop stops converging, and `f` *falls back* to ≈0.181 and stays
there across a further 3× in mass.

So the reachable supremum of `f` at N=24 is **≈0.186**, and
**`f ~ 0.6` is 3.2× above it.** The old PASS bin was not merely outside the *frozen*
regime — it was **outside the engine's entire accessible configuration space at this
resolution, at every amplitude, converged or not.** No amplitude choice, and no
re-freeze of the family, could have reached it.

### 1.3 · The structural change this prereg makes

The defect was not "the bins were too tight." It was that **the adjudicated quantity
(`η_mixed`) has its zero at a place the configuration cannot go.** Tightening,
loosening, or re-centring bins on `η_mixed` reproduces the defect.

Per the dispatch instruction — *if the PASS bin does not lie inside the accessible
regime, change the DESIGN, not the bins* — this prereg **changes the adjudicated
quantity**:

- **`η_mixed` is DEMOTED to a reported, derived diagnostic.** It is still computed and
  still published, but **no bin is keyed on it.**
- **The adjudicated quantity is `c ≡ Δ_clock / U_bind`** — the ratio of the two ledger
  deficits — **and specifically its AMPLITUDE-INVARIANCE and its parameter-free
  predicted value.** §4 shows `η_mixed` is an exact algebraic function of `c`, so
  nothing is lost; §5 shows `c`'s PASS region is reachable everywhere in the accessible
  band, because it is a statement *about* that band rather than a point outside it.

**Both directions of the new PASS bin are demonstrably reachable by an actually-existing
weight** — the shipped quadratic weight drives `c` across a 17× range over the same
scan and would fire the FAIL side (§11). That is the receipt the old bin set could
not produce.

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
