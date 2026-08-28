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

X44 froze bin (iii) UNRECONCILED with `η_mixed = +1.048` and has sat unowned since.
A sweep this session established that **the obstruction was DEFINITIONAL, not
physics: the glyph `√S` denotes two different functions of `ε₁₁`, and the
reconciliation bridged them on the symbol.**

| | site (verified this session) | form | leading deficit `1 − w` |
|---|---|---|---|
| **engine** | `src/ave/gravity/backreaction.py:250-252` → `src/ave/solvers/graded_vacuum_network.py:229-230` | `w = √( (1−A²)^{0.5} ) = (1−A²)^{1/4}` | **`ε₁₁²/4` — QUADRATIC** |
| **vol-3 canon (W2)** | `temporal-spatial-lattice-decomposition.md:24`, `:28`, with `ε₁₁` at `:14` | `√g₀₀ = √S ≈ 1 − GM/(c²r)` | **`ε₁₁/7` — LINEAR** |

Verified verbatim this session:
`graded_vacuum_network.py:229-230` — `base = np.maximum(1.0 - A**2, 0.0)` /
`S = base**exponent`; `backreaction.py:251-252` — `S = saturation_kernel(A,
exponent=0.5, S_min=S_min)` / `return np.sqrt(S)`. Composed, `w = (1−A²)^{1/4}`,
whose Taylor expansion about `ε₁₁ = 0` has **no linear term at all.**
And `temporal-spatial-lattice-decomposition.md:24` verbatim: *"the proper tick of a
clock sitting at $r$ is $\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/(c^2 r)$"*.

**The two sides of X44's reconciliation were therefore never comparable.**
`η_mixed ≈ +1.05` measured the gap between a linear object and a quadratic object
that share a symbol. That is a bookkeeping defect any framework would own — it is
NOT the observation that AVE has more than one clock notion. GR carries ADM, Komar
and Bondi masses without that being a defect (symmetric-standard check applied, both
directions). The defect here is narrower: **one symbol denoting two different
functions of one variable.**

**The root, one level deeper** (D1 lane, credited): the false link is not the
exponent but the identity `g₀₀ = S` itself. With `g₀₀ = 1 − A` affine in the metric
strain and `S(A) = √(1−A²)` even in `A`, `S = g₀₀` forces `2g₀₀(1−g₀₀) = 0`, i.e.
`A ∈ {0, 1}` and nothing between — and those two points are exactly Axiom 4's two
gravitational anchors. Every canonical check of the identity was performed at the
only two radii where it cannot fail. Axiom 4's own dialect list
(`manuscript/common_equations/eq_axiom_4.tex:10`, verbatim: *"the same $S(A)$
function governs strain expressed as … $r_s/r$ (gravitational metric strain)"`*)
keeps `A` affine in the metric strain under either reading, so **the dialect fork
does not rescue `g₀₀ = S`.**

**Consequence for this prereg.** Every weight below is named by its **function of
`ε₁₁`**, never by the glyph `√S`. The bare glyph `S` appears in this document ONLY
as the Axiom-4 kernel `S(A) = √(1−(A/A_yield)²)` (`eq_axiom_4.tex:7`, verified
verbatim). **This prereg never writes `g₀₀ = S` or `√g₀₀ = √S`.**

## 3 · THE FROZEN WEIGHT

### 3.1 · The frozen form

```
n_scalar(r) = 1 + ε₁₁(r)/7                    # canon, ponderomotive-equivalence.md:14
w(r)        = 1 / n_scalar(r)                 # THE FROZEN KOMAR / REDSHIFT SOURCE WEIGHT
T₀₀^src     = T₀₀^matter · w                  # replaces the Picard source weight
1 − w       = ε₁₁/7 + O(ε₁₁²)                 # LINEAR, coefficient k ≡ 1/7
```

`k` is a **document-local shorthand** for the leading clock coefficient defined by
`1 − w = k·ε₁₁ + O(ε₁₁²)`. It is not a corpus symbol and mints nothing.

**COINAGE-GREP (run this session, `git grep -rIl`, tracked tree @ `a3f4fef7`):**
`n_scalar` 16 files · `n_{scalar}` 18 · `ponderomotive` 110 · `co-scaling` 27 ·
`lapse clock` 2 · `kernel clock` 2. **Every name used in this prereg has prior
corpus hits — ZERO new coinages.** Names follow D1's disambiguation table.

### 3.2 · The derivation that selects it — five steps, each tagged

**(1) DERIVED-from-structure.** Canon's source law
(`manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md:50-53`,
verified verbatim this session:
`-\nabla\cdot[(c^4/7G)D(A)\nabla\varepsilon_{11}] = 4\pi T_{00}`, `D(A) = 1/S(A)`)
puts the matter source alone on the RHS and the nonlinearity in the modulus on the
LHS. The far-field monopole is therefore `∫T₀₀^src` **by Gauss** — an
install-tautology. So the weight question reduces to exactly one physical question:
**what IS a matter element's energy, read from infinity?**

**(2) DERIVED-substrate.** Gravity in this sector is a **reactive frequency
re-tuning of the LC network at invariant characteristic impedance** (`Z = Z₀`,
reflectionless, `Γ = 0`). Ratio holds, product moves: `ω₀ → ω₀/m`. This is a
**bias-point** effect, not a **modulus** effect — which is why a weight built from
the modulus kernel is answering the wrong question.

**(3) DERIVED-canon.** The co-scaling factor for a matter resonator is
`n_scalar = 1 + ε₁₁/7`, via the `1/7` Lagrangian isotropic projection
(`ponderomotive-equivalence.md:14`, verified verbatim: *"it couples to the spatial
volume via the $1/7$ Lagrangian isotropic projection (derived in Chapter 4). The
effective scalar refractive index perceived by mass is $n_{scalar}(r) = 1 +
\epsilon_{11}(r)/7 = 1 + GM/c^{2}r$"*).

**(4) DERIVED-canon-PRINTED.** The energy-read-at-infinity is **already written in
canon** (`ponderomotive-equivalence.md:19`, verified verbatim):
`U_{wave}(r) = \frac{m_i c^{2}}{n_{scalar}(r)} \approx m_i c^{2} - \frac{GM m_i}{r}`.
The same leaf takes its gradient to recover `F = −GMm_i/r²` and WEP (`:22-30`).

**(5) The only new step.** `T₀₀^src = T₀₀^matter / n_scalar`, **because `U_wave` IS
the Komar integrand** — it is precisely "a matter element's energy read from
infinity," which is what step (1) showed the weight must supply.

**This is not a free choice.** Any other weight puts the engine's Picard source in
contradiction with the canon leaf that derives Newtonian gravity and WEP.

### 3.3 · Independent corroboration of the SLOPE (not of the choice)

Four independent routes land on a **slope-1** clock. None of them is
"it makes `η_mixed` small":

1. **The derivation above** (ponderomotive, `n_scalar`).
2. **Grant Ruling 1**, `_orchestration/2026-07-10_rulings-docket.md:855` heading
   verbatim: *"Ruling 1 — F6 Komar-clock register: √S (slope-1) IS the clock —
   CONFIRMED"*, grounded at `:869-871` on exactly the right physics: *"The
   **Komar/Tolman ledger sums per-cell in-place readings** … so it weights by the
   **slope-1** in-place clock"*.
3. **The vol-3 W2 walk-back**, `temporal-spatial-lattice-decomposition.md:28`
   (verified verbatim): the local clock rate / gravitational redshift is
   *"a slope-1 quantity"*, bridged to the slope-2 propagation index by
   `z = (n_temporal − 1)/2`.
4. **The 2026-08-11 linearity audit's** lapse and substrate-side rows.

> ⚠ **FLAG-DON'T-FIX — Ruling 1's code attribution is false by direct algebra.**
> `_orchestration/2026-07-10_rulings-docket.md:858-860` certifies the live
> `komar_weight` (`backreaction.py:235-252`, `return np.sqrt(S)`) as *"on the correct
> side."* That function returns `(1−ε₁₁²)^{1/4}`, whose expansion about `ε₁₁ = 0`
> has **zero linear term**. A ruling that a quantity is slope-1 cannot certify an
> implementation whose slope is identically 0. **The ruling's physics is correct and
> untouched; only its code attribution and its `√g₀₀ = √S` glyph-bridge fail.**
> The ruled physics and the shipped code have been in silent disagreement since
> 2026-07-14, invisible because both sides write `√S`. **This prereg flags it and
> edits nothing** — the docket is a canon leaf and the correction is Grant's.
> **Therefore the frozen weight is not a new proposal: it is the RULED one, written
> in the register the engine actually uses.**

### 3.4 · Which census member this is — and which it is NOT

The frozen weight is the **substrate-side** `1/n_scalar`, **not** the metric lapse
`√g₀₀`. They agree at first order (`k = 1/7` both) and part at `O(ε₁₁²)`. The
substrate-side one is chosen because it **is not a GR import** — it is a substrate
projection with a stated in-corpus derivation, which the lapse is not. At the
engine's accessible amplitudes the two differ by `≈ (3/2)(ε₁₁/7)²`, far below every
bin edge in §10, so **this fork changes no verdict in this run** and is recorded as
a fork, not resolved.

**The 2026-08-11 proposal is a LIVE CANDIDATE, not a settled answer**, and it carries
a defect this prereg refuses to inherit. `research/2026-08-11_gravity-linearity-audit_result.md:658`
(verified verbatim) says *"the source should carry the **co-scaling factor**, not the
kernel"*, and `:645` names that factor as `m = 1 + ε₁₁/7 = 1/√g₀₀` — which is **> 1**.
Taken literally the source would carry `m`, giving a mass **EXCESS**, contradicting
the SUBTRACT ruling and driving `η` **up**. The physics needs `1/m`. **This prereg
freezes `w = 1/n_scalar < 1`, the reciprocal of what that sentence literally says.**
The proposal's own header (`:616-617`) tags §9 *"UN-AUDITED … no adversarial review,
no second reader, no auditor"* and `:661` says *"⚠ **Proposed, not applied.**"* —
so it is cited as corroboration of the slope, never as authority.

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
