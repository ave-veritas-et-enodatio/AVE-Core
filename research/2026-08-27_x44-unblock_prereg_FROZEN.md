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

Everything in this section is **exact algebra, derived before any run.** It fixes
what the run can and cannot decide.

### 4.1 · The three registers, and why only two are independent

| register | definition | how it is obtained |
|---|---|---|
| `m_g` | `Σ_interior(L·ε₁₁)` — far-field Gauss flux | **≡ `Σ T₀₀^src` by the discrete divergence theorem — an INSTALL-TAUTOLOGY** |
| `M_eff` | `M − U_bind`, `U_bind = ½ g_self Σ|∇ε₁₁|²` | strain-energy ledger (`backreaction.py:191-194`) |
| `M_ray` | mass inferred from ray-trace deflection `δ = 4GM/(bc²)` | reads the far-field `1/r` coefficient of `ε₁₁` — **collapses onto `m_g` by Gauss** |

**Only `m_g` and `M_eff` are independent, and `m_g` is tautologically the installed
source.** This is the structural fact §9 turns into the run's headline.

### 4.2 · The discrete virial identity — EXACT, by adjointness

Verified by direct read this session: `Grad` is built from the shift blocks
`0.25·p_m·(P_{−p} − I)` (`gw_propagation.py:566-567`) and `Div` from
`0.25·p_m·(P_{+p} − I)` (`:578-579`). Since `P_{−p}ᵀ = P_{+p}`, **`Div = Gradᵀ`**, so
`L = Div·diag(D)·Grad = Gradᵀ·diag(D)·Grad` is positive semi-definite and

```
Σ ε₁₁·(L ε₁₁)  ≡  Σ D·|∇ε₁₁|²                      … (V)  EXACT by adjointness
```

With Dirichlet-zero faces (`gw_propagation.py:671-677`) and `(Lε)_interior = T₀₀^src`
from `spsolve` (`:703`), (V) becomes `Σ T₀₀^src ε₁₁ = Σ D|∇ε₁₁|²`, exact to the
`spsolve` residual, the Picard fixed-point residual, and face leakage.

### 4.3 · `c` — the adjudicated quantity — in closed form

Define `Δ_clock ≡ Σ T₀₀^matter (1 − w)` and `c ≡ Δ_clock / U_bind`. Then, with
`1 − w = kε₁₁/(1 + kε₁₁)` for the frozen `w = 1/n_scalar`:

```
        Δ_clock      2k                                  Σ D|∇ε₁₁|²
c  =  ─────────  =  ────  ·  ⟨D⟩_w  ·  χ ,      ⟨D⟩_w ≡ ────────────  ,
        U_bind      g_self                                Σ |∇ε₁₁|²

                                     χ ≡ ⟨ 1/(1 + k ε₁₁) ⟩   (T₀₀ε₁₁-weighted)
```

Both `⟨D⟩_w ≥ 1` and `χ ≤ 1` are **measured directly from the solved field**, with no
fit and no free parameter. Both → 1 as amplitude → 0.

### 4.4 · `g_self` is NOT a free knob here — the operator fixes it

The elliptic operator carries **no prefactor**: `L = (Div @ Dexp @ Grad).tocsr()`
(`gw_propagation.py:700`) with `rhs = T00` (`:677`) — i.e. `κ_op ≡ 1` in lattice
units. The variational energy whose stationarity gives `∇·(D∇ε) = T₀₀` is
`½∫D|∇ε|²`, so the ledger normalization consistent with the engine's own operator is
`g_self = κ_op = 1`. The shipped default is `g_self = 1.0`
(`backreaction.py:163`). **`g_self = 1` is therefore the CONSISTENT choice, not a
convention — and this prereg freezes it.** §12 records why this matters.

### 4.5 · `η_mixed` is an exact function of `c` — which is why no bin is keyed on it

With `f = U_bind/(M + U_bind)`, `m_g = M − Δ_clock` and `M_eff = M − U_bind`:

```
m_g / M_eff  =  ( 1 − (1+c)·f ) / ( 1 − 2f )
```

`η_mixed` is then the least-squares slope of `(ratio/ratio₀ − 1)` vs `f`
(`src/tests/engine_acceptance/_nordtvedt.py:167-178`, read verbatim). Evaluated on
the frozen `#651` family's own `f` values (0.0561, 0.0397, 0.0300, 0.0234 —
`research/2026-07-12_x44-komar-source_result.md:62-65`):

| `c` | what installs it | `η_mixed` (exact algebra) |
|---|---|---|
| 0 | bare `matter` control (no weight) | **+1.15581** |
| **2/7 = 0.285714** | **the FROZEN weight, `k = 1/7`** | **+0.83127** |
| 4/7 | a `k = 2/7` slope-2 weight | +0.50222 |
| **1** | a `k = 1/2` weight | **0.00000 — EXACTLY** |
| 2 | `k=1/7` at `g_self = 1/7` | −1.21399 |

Two consequences, both load-bearing:

1. **`η_mixed = 0` ⟺ `c = 1` EXACTLY**, identically in `f`. It is not approximately
   zero at `c = 1`: the ratio becomes `(1−2f)/(1−2f) ≡ 1` for every member, so the
   slope vanishes identically. **Reconciliation is the single condition
   `Δ_clock = U_bind`, and nothing about the family can move it.** This is why
   re-freezing the family could never have rescued the old PASS bin.
2. The algebra reproduces the measured engine numbers to <0.5%: predicted
   `η(c=0) = +1.1558` vs X44's measured `matter = +1.1585`
   (`research/2026-07-12_x44-komar-source_result.md:177`) — 0.23%. That agreement is
   the receipt that this closed form is the right model of the instrument.

**Therefore `η_mixed` carries no information beyond `c`, and this prereg reports it
without adjudicating on it.**

## 5 · ★ THE ACCESSIBLE REGIME, and the demonstration that the PASS bin lies inside it

This is the section the superseded prereg did not have. It states what the
configuration can reach, and then shows the PASS bin lies **inside** it.

### 5.1 · The frozen families

- **FAM-A — the frozen `#651` family** (continuity with X44, and the `η_mixed`
  report): `N = 24`, `σ ∈ {1.4, 1.8, 2.2, 2.6}`, `Σ T₀₀^matter = 4.0`,
  `g_self = 1.0`, `S_min = 1e-3`.
- **FAM-B — the amplitude ladder** (the invariance test): `N = 24`, `σ = 1.8`,
  `λ ∈ {0.25, 0.5, 1, 2, 4, 6, 8}`, i.e. `Σ T₀₀^matter = 4λ` — a **32× rest-energy
  span**, every member converged (§1.2).

### 5.2 · Computed accessible bounds (measured, §1.2 driver)

| quantity | FAM-A | FAM-B (converged) | hard ceiling |
|---|---|---|---|
| `max ε₁₁` (= `max A`) | 0.079 – 0.188 | **0.0329 – 0.7827** | `A = 1` (yield cap, `gw_propagation.py:705`) |
| `U_bind/M` | 0.024 – 0.059 | **0.0104 – 0.2283** | ≈0.223 (turns over) |
| `f = U/(M+U)` | 0.0234 – 0.0561 | **0.0103 – 0.1859** | **sup ≈ 0.186, NON-MONOTONE** |
| Picard | converged | converged | fails for λ ≳ 12 |

**The accessible band is `f ≤ 0.186` and `ε₁₁ ≤ 0.783`, at any amplitude.**

### 5.3 · ★ The old PASS bin was OUTSIDE this band; the new one is INSIDE it

**OLD.** PASS required `|η_mixed| < 1e-3` ⟺ `c = 1` (§4.5, exactly) ⟺
`Δ_clock = U_bind` ⟺ `f ~ 0.6`. Reachable supremum of `f` is **0.186**.
**Ratio needed/reachable = 3.2×, and `f` turns over before it — so no amplitude
reaches it.** The bin could not fire.

**NEW.** The PASS bin is a bracket on `c` **computed from the accessible band's own
`ε₁₁` bounds**, via the closed form `c = (2k/g_self)·⟨D⟩_w·χ` (§4.3) with
`⟨D⟩_w ∈ [1, D_max]`, `χ ∈ [χ_min, 1]`, `D_max = (1−max A²)^{−1/2}`,
`χ_min = (1 + k·max A)^{−1}`, `2k/g_self = 2/7 = 0.285714`:

| λ | `max ε₁₁` | `f` | `χ_min` | `D_max` | **PASS bracket for `c`** |
|---|---|---|---|---|---|
| 0.25 | 0.0329 | 0.0103 | 0.99532 | 1.00054 | **[0.2844, 0.2859]** |
| 0.50 | 0.0658 | 0.0204 | 0.99069 | 1.00217 | **[0.2831, 0.2863]** |
| 1.00 | 0.1310 | 0.0397 | 0.98163 | 1.00869 | **[0.2805, 0.2882]** |
| 2.00 | 0.2575 | 0.0749 | 0.96452 | 1.03490 | **[0.2756, 0.2957]** |
| 4.00 | 0.4830 | 0.1298 | 0.93545 | 1.14205 | **[0.2673, 0.3263]** |
| 6.00 | 0.6584 | 0.1654 | 0.91403 | 1.32861 | **[0.2612, 0.3796]** |
| 8.00 | 0.7827 | 0.1859 | 0.89943 | 1.60669 | **[0.2570, 0.4591]** |

**The PASS bracket is DERIVED FROM the accessible band, so it lies inside it by
construction.** That is the structural repair: the old PASS bin was an externally
imposed tolerance on a quantity whose zero sat outside the reachable set; the new one
is a prediction *about* the reachable set, evaluated everywhere on it.

### 5.4 · …and the FAIL side is reachable too — demonstrated by weights that exist

A bracket only PASS can enter is as defective as one only FAIL can enter. Predicted
`c` in the linear limit for the four candidate weights (`c = 2k/g_self`):

| weight | `k` | predicted `c` | inside the λ=1 bracket [0.2805, 0.2882]? |
|---|---|---|---|
| shipped quadratic `(1−ε₁₁²)^{1/4}` | 0 (no linear term) | → 0 (X44 measured 0.046 at λ=1) | **NO — fails by ~6×** |
| **FROZEN `w = 1/n_scalar`** | **1/7** | **0.285714** | **YES** |
| slope-2 propagation index | 2/7 | 0.571429 | **NO — fails by 2×** |
| the reconciling weight | 1/2 | 1.000000 | **NO — fails by 3.5×** |

Every non-frozen candidate misses the bracket by **≥ 2×** while the bracket's own
width is **≤ 3%** at λ=1. The instrument separates all four, and the **shipped
quadratic weight is a live existence proof that the FAIL side fires** — X44 already
measured `c` running from 0.0115 to 0.195 across this ladder, a 17× drift, which the
bracket rejects at every rung.

## 6 · Scope — the 91/9 split, and what this run is NOT about

### 6.1 · The `u_field` deletion is independently justified — carried, not re-litigated

X44's three-mode decomposition (`research/2026-07-12_x44-komar-source_result.md:177-179`,
read verbatim): `ADD = +2.2792`, `matter = +1.1585`, `komar = +1.0479`. Of the total
drop `1.2313`, **91.0% was deleting the double-counted `+u_field`** and **9.0% was
the `√S` weight**.

The deletion stands on **three grounds that do not depend on the weight question at
all**, so this run inherits it and does not re-open it:

1. **Canon's source law has no such term.**
   `saturating-modulus-and-backreaction.md:50-53` (verified verbatim) puts the matter
   source alone on the RHS; the nonlinearity lives in the modulus `D(A)` on the LHS.
2. **Sign.** The engine's `u_field = +½κ|∇ε₁₁|²` is positive-definite and the code
   says so (`backreaction.py:114-115`, verbatim: *"Sign: u_field ≥ 0
   (positive-definite strain energy → self-reinforcing → the runaway-collapse
   risk"*). Gravitational field energy is negative-definite. Canon states the
   consequence directly (`saturating-modulus-and-backreaction.md:130`, verbatim):
   *"capacitor-ADD reading would predict a mass *excess* and *repulsive* gravity —
   falsified by every bound orbit."*
3. **Measured.** Under ADD the flux certifies against `M+U` at
   `η_one = +8.28×10⁻⁵` (`research/2026-07-12_x44-komar-source_result.md:286-288`)
   against a ledger of `M−U` — a `2U` discrepancy, the signature of a sign flip, not
   of a subtle overlap.

**SCOPE: this run is scoped to the remaining 9% — the weight question — and to it
alone.** The `u_field` deletion is a carried premise, and `source_mode="add_field"`
stays callable for KEEP-BOTH regression only.

### 6.2 · ⚠ But the inference "91/9 ⇒ the weight is a 9% correction" DOES NOT FOLLOW

The 9% figure measures the **shipped quadratic** weight, which is a near-no-op **by
construction**: its effect is `O(ε₁₁²)` where every other term in the ledger is
`O(ε₁₁)`. It is a measurement of how little the **wrong** weight does, not of how
little **the weight** matters.

Recomputed against the frozen weight (exact algebra, §4.5; corroborated by the
scoping lane's direct measurement `η_lin = +0.8280`):

| step | `η_mixed` | Δ |
|---|---|---|
| ADD | +2.2792 | — |
| → `matter` (delete `u_field`) | +1.1585 | **−1.1207** |
| → shipped quadratic weight | +1.0479 | −0.1106 |
| → **FROZEN `w = 1/n_scalar`** | **+0.8280** | **−0.3305** |

**ADD → frozen weight: total `−1.4512`, of which deletion 77.2% and weight 22.8%.**
The frozen weight does **3.0× the work of the shipped one.** The prereg carries the
91/9 scoping as instructed, and simultaneously records that 91/9 is not a statement
about the weight's importance.

### 6.3 · Explicitly NOT in scope

- The `T_ij` / stress register and the Tolman `+3∫p` term (the X44b charter's build
  order; still unbuilt at HEAD — §9.3).
- A force-balanced / hydrostatic source family (`gaussian_blob` is a prescribed
  scalar profile, not a self-consistent equilibrium).
- Any change to `g_self` (§12).
- srs-z=3 migration of the gravity Grad/Div instrument.
- The `√g₀₀` vs `1/n_scalar` `O(ε₁₁²)` fork (§3.4) — recorded, not resolved.
- Any edit to a canon leaf, a ruling, or the docket. **FLAG-DON'T-FIX.**

## 7 · Pre-registered predictions

Numbers committed before the run. Each prediction is tagged **ENTAILED** (true by
construction — declared so it cannot be banked as evidence) or **FIREABLE** (can
fail).

| # | prediction | value | status |
|---|---|---|---|
| **P1** | Gauss flux ≡ `Σ T₀₀^src` | rel. residual < 1e-4 | **ENTAILED** (install-tautology) |
| **P2** | virial identity (V): `Σ T₀₀^src ε₁₁ / Σ D\|∇ε₁₁\|²` | `1 ± 1e-6` | **ENTAILED by adjointness**; fires only on face leakage / non-convergence / clip |
| **P3** | `c` inside the §5.3 bracket at every FAM-B rung | see §5.3 table | **FIREABLE** |
| **P4** | `\|c / ((2k/g_self)·⟨D⟩_w·χ) − 1\|`, with `⟨D⟩_w`, `χ` measured independently | ≤ 1e-3 | **FIREABLE** (two-method) |
| **P5** | linear-limit anchor: `c` extrapolated to λ→0 | **0.285714 ± 0.001** | **FIREABLE** |
| **P6** | `η_mixed` on FAM-A (reported, **not adjudicated**) | **+0.831 ± 0.010** | **REPORTED** |
| **P7** | resolution receipt: `c` at `N ∈ {24, 32, 40}` | drift < 1% | **FIREABLE** |
| **P8** | discrimination: install `k ∈ {0, 1/7, 2/7, 1/2}`; each gives `c ≈ 2k/g_self` | 0, 0.2857, 0.5714, 1.0000 | **FIREABLE** (instrument resolving power) |
| **P9** | D-consistent register `c^D ≡ Δ_clock/(½g_self Σ D\|∇ε₁₁\|²) = (2k/g_self)·χ` — the `⟨D⟩` drift vanishes **exactly** | matches `(2/7)·χ` to ≤1e-3 | **FIREABLE** |
| **P10** | **no engine observable discriminates clock weights independently of the install** (§9.1) | — | **FIREABLE by counterexample** |

**P4 and P9 are the load-bearing fireable pair.** P4 says the closed form is the
right model of the instrument; P9 says the residual amplitude drift is entirely the
binding register's omission of `D`, and vanishes exactly when the register the
operator's own variational structure selects (`½∫D|∇ε|²`) is used instead. **P9 can
fail** — if the drift does not vanish under the D-consistent register, the drift is
something else (boundary, convergence, clip) and the closed form is incomplete.

**P8 is the non-triviality leg**, not a physics prediction: it establishes that the
instrument separates the four candidates by ≥2× while the bracket is ≤3% wide
(§5.4). Installing `k = 1/2` is a **probe**, not a proposal — §12.

**P10 is the structural claim** and the one this prereg most expects to survive. Its
falsifier is exhibiting a single engine observable that responds to the weight other
than through the installed source. Candidates to be enumerated and tested in the run:
the ray-trace deflection `δ = 4GM/(bc²)`, the monopole plateau, the two-mass
nonlinearity ratio, `shape_dev` vs Stage-1, and the `S_min`-independence check.

## 8 · What would FALSIFY the derived weight, in the run's own terms

Stated before the run, in the run's own measurable terms. Any ONE of these fires
**FALSIFIED-WEIGHT** (§10 bin D):

- **F1 — WRONG COEFFICIENT.** The linear-limit anchor `c₀` (P5) lands outside
  `0.285714 ± 0.001`. The frozen weight's entire content at leading order is the
  coefficient `k = 1/7`; `c₀ = 2k/g_self` reads it back. A landing at `0.5714` says
  the ledger wants `k = 2/7` (the slope-2 propagation index — i.e. W2's
  disambiguation is inverted); at `1.0`, `k = 1/2` (§12).
- **F2 — WRONG FUNCTIONAL FORM.** `c` drifts with amplitude **beyond** the §5.3
  bracket, or the drift is **not** accounted for by the measured `⟨D⟩_w·χ` (P4
  fails at ≥1e-3). A weight that is not linear-plus-`1/n_scalar`-curvature drifts in
  a way the closed form cannot absorb — the shipped quadratic weight drifts 17× and
  is the worked example.
- **F3 — THE D-REGISTER PREDICTION FAILS.** `c^D` (P9) does **not** collapse to
  `(2/7)·χ`. Then the amplitude structure is not the binding register's missing `D`,
  and §4.3's closed form — on which the entire bracket rests — is wrong.
- **F4 — RESOLUTION.** `c` drifts >1% across `N ∈ {24, 32, 40}` (P7). The verdict
  would then be an N=24 artifact. *(This is a live risk: the scoping lane ran N=24
  only and flagged the absence of a resolution receipt as its own blind spot.)*
- **F5 — THE IDENTITY LEAKS.** P2 fails at >1e-6, i.e. `Σ T₀₀^src ε₁₁ ≠ Σ D|∇ε₁₁|²`.
  Then the ledger comparison is contaminated by boundary flux or an unconverged
  fixed point and **no bin may be entered** (§10 evaluation order puts this first).
- **F6 — DISCRIMINATION FAILS.** The four installed `k` values (P8) do **not**
  produce four separated `c` values. The instrument then has no resolving power and
  every result is an artifact (§11).

**F1 is the sharpest.** It is a direct, single-number read of the clock coefficient
the engine's own ledger requires, with the four candidates separated by ≥2× against
a bracket ≤3% wide.

**What does NOT falsify the weight:** `η_mixed ≠ 0`. That is expected (§9), and the
prereg commits in advance that a non-zero `η_mixed` will not be read as evidence
against `w = 1/n_scalar`, nor as licence to search for a weight that zeroes it.

## 9 · The honest expected outcome — what a non-zero residual would MEAN

**Reconciliation is NOT the only success, and this prereg does not treat it as one.**
The expected outcome is: **the frozen weight PASSES every fireable gate, and
`η_mixed` lands at ≈ +0.83, not 0.**

### 9.1 · Why the two registers can legitimately differ

`Δ_clock` and `U_bind` are **different functionals of different things**.
`Δ_clock = k·Σ T₀₀ ε₁₁` is a **matter-weighted potential** integral — it lives where
the matter is. `U_bind = ½g_self Σ|∇ε₁₁|²` is a **field-gradient** integral — it lives
everywhere the field varies. Nothing requires them to be equal. Via the virial
identity (§4.2) they are related, and the relation is:

```
c  =  Δ_clock / U_bind  =  (2k/g_self) · ⟨D⟩_w · χ  →  2k/g_self  =  2/7
```

`k = 1/7` is **derived** (§3.2); `g_self = 1` is **forced by the engine's own
operator** (§4.4). Neither is free. So `c = 2/7 ≠ 1`, and the residual is
**parameter-free and amplitude-invariant** — a structural property of the two
registers, not a tuning failure and not a weight defect.

**The mismatch factor is exactly `7/2`**, and it is not a new constant: it is the
ratio of the `ε₁₁` register's **7** (`ε₁₁ = 7GM/c²r`,
`temporal-spatial-lattice-decomposition.md:14`) to the Schwarzschild **2** — the same
arithmetic that puts `r_sat = 7GM/c² = 3.5 r_s` (`manuscript/ave-kb/vol3/claim-quality.md:104`,
verified verbatim). **The gap is a register-normalization mismatch between
`Σ T₀₀^src` and `½g_self Σ|∇ε₁₁|²`, not a wrong functional form.**

### 9.2 · What a non-zero `η_mixed` would MEAN — three readings, pre-declared

If the weight passes and `η_mixed ≈ +0.83` stands, the prereg pre-commits that this
is evidence for **one of these three**, and that the run does **not** adjudicate
among them:

1. **THE LABEL IS WRONG, NOT THE WEIGHT.** `M_eff = M − U_bind` may simply not be the
   ADM mass conjugate to the engine's own far field. The clock-native inertial mass
   would be `M − Δ_clock`. This is X44 §7 option 1, and it is *promoted* by this
   result rather than refuted: the far-field register is derived and the
   strain-energy register is a convention.
2. **AN INGREDIENT IS STRUCTURALLY ABSENT.** The Tolman/Komar `+3∫p` stress term
   exists for a static **force-balanced** source; the engine has no stress register
   and `gaussian_blob` is a prescribed profile, not a hydrostatic equilibrium.
   **Verified absent at HEAD by three methods this session:** (A) no `def`/`class`
   matching `sigma_ij|stress_tensor|momentum_flux|force_density|T_ij|tolman` in the
   gravity path — the three hits are `vol_1` prestress-elasticity and a `vol_4`
   acoustic momentum flux, neither of which is the gravity register; (B) no
   `*stress*`/`*tolman*`/`*tij*` filename under the gravity path; (C) **zero**
   `Tolman` or `3∫p` hits anywhere in `src/`. The `2026-07-14_tij-x44b_CHARTER.md`
   got its Grant GO six weeks ago; the build never happened.
3. **THE TWO REGISTERS ARE GENUINELY DIFFERENT PHYSICAL QUANTITIES** and the engine
   should carry both, labelled, rather than force them to agree.

⚠ **The X44b expectation ladder does not survive this, and the prereg says so in
advance.** X44 `§5b(ii)` (`research/2026-07-12_x44-komar-source_result.md:157-162`)
predicts a linear clock gives `η ≈ −1`, from which stress must supply `+1` to reach
0. That prediction holds at `g_self = 1/7`, **not** at the frozen family's
`g_self = 1.0` (§4.5: `c = 2` needs `g_self = 2k = 1/7`). From `+0.83` the stress
term must supply **−0.83 — the OPPOSITE SIGN.** So the ladder's directional logic is
falsified as stated, and a lane reading `+0.83` as evidence about the stress term's
magnitude would be reading a normalization mismatch.

### 9.3 · ★ The deepest expected finding: the engine as built cannot falsify a weight

Per §4.1 the far-field flux is `Σ T₀₀^src` **by construction**, and the ray-trace
register collapses onto it. With a **prescribed** matter source, **only two registers
are independent, and one of them is tautologically the thing you installed.** Their
ratio is therefore a ratio of two *definitions*.

**Pre-registered expectation (P10): no engine observable discriminates among clock
weights independently of the install.** If that survives its falsifier (§7), then the
honest verdict on X44 is not "reconciled" or "unreconciled" — it is that
**the question as posed is not decidable by the engine as built**, and the missing
capability is the force-balanced source with its own stress response. That is a
sharper and more useful outcome than either bin of the old freeze, and this prereg
counts it as a **success**, not a failure.

## 10 · ★ FROZEN BINS — exact edges, fixed evaluation order

### 10.1 · Frozen quantities and their exact definitions

```
w            = 1 / n_scalar = 1 / (1 + ε₁₁/7)          # THE FROZEN WEIGHT (§3)
k            ≡ 1/7 = 0.1428571428…                     # installed clock coefficient
g_self       ≡ 1.0                                     # FROZEN (operator-forced, §4.4)
Δ_clock      ≡ Σ T₀₀^matter · (1 − w)
U_bind       ≡ ½ g_self Σ |∇ε₁₁|²                      # shipped register
U_bind^D     ≡ ½ g_self Σ D |∇ε₁₁|²                    # D-consistent register
c            ≡ Δ_clock / U_bind                        # ★ THE ADJUDICATED QUANTITY
c^D          ≡ Δ_clock / U_bind^D
⟨D⟩_w        ≡ Σ D|∇ε₁₁|² / Σ|∇ε₁₁|²                   # measured from the field
χ            ≡ Σ T₀₀ε₁₁/(1+kε₁₁) / Σ T₀₀ε₁₁            # measured from the field
k_meas       ≡ c · g_self / (2 · ⟨D⟩_w · χ)            # → k if §4.3 is right
V_resid      ≡ | Σ T₀₀^src ε₁₁ / Σ D|∇ε₁₁|² − 1 |      # virial-identity residual
η_mixed      = slope per _nordtvedt.py:167-178          # REPORTED, NOT ADJUDICATED
```

### 10.2 · ★ EVALUATION ORDER — strictly sequential, first match wins, no appeal

**Bins Z and Y are evaluated FIRST and are OVERRIDING. A run that enters Z or Y
STOPS: it may not enter any selecting bin, and its `c`, `k_meas` and `η_mixed`
are reported as UNINTERPRETABLE, not as evidence.**

```
STEP 1 → BIN Z (ARTIFACT)        — if any Z-clause fires, HALT. Report Z.
STEP 2 → BIN Y (INCONCLUSIVE)    — if any Y-clause fires, HALT. Report Y.
STEP 3 → BIN A                   — if all A-clauses hold, report A. STOP.
STEP 4 → BIN B                   — if all B-clauses hold, report B. STOP.
STEP 5 → BIN C                   — if any C-clause holds, report C. STOP.
STEP 6 → BIN D                   — otherwise, report D.
```

### 10.3 · The bins, verbatim

| bin | fires when (exact edges) | meaning |
|---|---|---|
| **Z — ARTIFACT** *(overriding, step 1)* | **ANY** of: **Z1** broadcast-degeneracy — recomputing `Δ_clock` with `w` replaced by its `T₀₀`-weighted scalar mean `w̄` changes it by **< 10%** (`\|Δ_clock^broadcast/Δ_clock − 1\| < 0.10`); **Z2** family degeneracy — FAM-A `max f / min f < 2.0`, **or** FAM-B `max λ / min λ < 8`; **Z3** discrimination failure — the four installed `k ∈ {0, 1/7, 2/7, 1/2}` do not give `c` values whose adjacent gaps each exceed **10×** the §5.3 bracket half-width at that rung; **Z4** field degeneracy — any slope-fit member has `U_bind/M < 1×10⁻³`; **Z5** phase-state breach — any member has `max A ≥ 0.99` (yield-pinned, outside the declared sub-yield state); **Z6** stencil breach — `|∇ε₁₁|²` in ANY ledger term is computed by anything other than the native diamond-K4 `Grad` (`_build_native_grad_div`); a Cartesian `np.gradient` would validate a stencil bug as physics | the null (or the pass) is a property of the configuration or the instrument, **not of the physics.** Nothing is banked. |
| **Y — INCONCLUSIVE** *(overriding, step 2)* | **ANY** of: **Y1** any FAM-A or FAM-B member reports `converged = False`; **Y2** `V_resid > 1×10⁻⁶` on any member; **Y3** Gauss residual `\|m_g/Σ T₀₀^src − 1\| > 1×10⁻⁴`; **Y4** `c` drifts **> 1%** across `N ∈ {24, 32, 40}` at λ=1 | the run did not execute cleanly enough to read. Re-run, do not re-bin. |
| **A — WEIGHT CONFIRMED, GAP STRUCTURAL** | **ALL** of: **A1** `k_meas ∈ [0.142357, 0.143357]` (`1/7 ± 5×10⁻⁴`) at **every** FAM-B rung; **A2** `c` inside the §5.3 pre-computed bracket at **every** FAM-B rung; **A3** `\|c^D / ((2k/g_self)·χ) − 1\| ≤ 1×10⁻³` at every rung *(the D-register prediction, P9)*; **A4** `V_resid ≤ 1×10⁻⁶` | the frozen weight behaves exactly as derived. **`η_mixed ≈ +0.83` is then a STRUCTURAL, parameter-free, amplitude-invariant register gap — not a weight defect and not closable by any substrate-derived weight.** Route §9.2's three readings to Grant. |
| **B — WEIGHT CONFIRMED, RESIDUAL UNEXPLAINED** | **A1 and A2 hold**, but **A3 fails** at `> 1×10⁻³` and `≤ 1×10⁻¹` | the coefficient is right and the bracket holds, but the amplitude structure is **not** the binding register's missing `D`. §4.3's closed form is incomplete. Surface the residual; **do not adjust the weight.** |
| **C — COEFFICIENT MISMATCH** | **A1 fails**, and `k_meas` at λ=1 lies within `±0.01` of one of `{0, 2/7, 1/2}` | the ledger requires a **named** coefficient that is not the derived one. **REPORT WHICH. DO NOT ADOPT IT** (§12). Route as a derivation conflict: canon's `1/7` projection vs whatever the ledger wants. |
| **D — WEIGHT FALSIFIED** | none of the above | `k_meas` matches no named candidate, or the bracket fails with the drift unabsorbed by `⟨D⟩_w·χ`. The ponderomotive derivation (§3.2) is wrong **in the run's own terms** (§8 F1/F2/F3). |

### 10.4 · Which clauses are ENTAILED — declared, so they cannot be banked as evidence

**A1 is near-tautological** and is declared as such: `k_meas` inverts the closed form
that the install itself satisfies, so it recovers what was installed unless the
virial identity leaks. It is a **consistency clause**, not evidence for the weight.
**A2 is partly independent** (its bracket uses no measured field quantity — only the
accessible-band `ε₁₁` bounds). **A3 is the genuinely fireable clause**: nothing about
the install forces the amplitude drift to be exactly `⟨D⟩_w`, and if the drift does
not vanish under the operator's own variational register the closed form is wrong.
**A4 can fail on boundary leakage, an unconverged fixed point, or the yield clip.**

**Bin A is therefore banked on A3 + A4, with A1/A2 as consistency conditions.** No
part of bin A is banked on `η_mixed`.

## 11 · ★ NON-TRIVIALITY / STRUCTURAL-NULL GATE

**A null obtained through a per-node broadcast or a degenerate configuration is an
artifact, not a result.** Bin Z (§10.3) is evaluated first and overrides everything.
This section states what each clause is *for*, and pre-computes what it will read on
the frozen families so the gate cannot be silently satisfied.

### 11.1 · Z1 — the per-node broadcast detector

The failure mode: a weight that is effectively a **scalar broadcast** —
`T₀₀^src = w̄ · T₀₀^matter` for a single number `w̄` — produces a perfectly clean
`Δ_clock`, a perfectly clean `c`, and carries **no spatial physics whatsoever**. The
weight's whole content is that it varies **with `ε₁₁(r)`**.

**Detector:** recompute `Δ_clock^broadcast ≡ (1 − w̄)·M` with `w̄` the `T₀₀`-weighted
mean of `w`, and compare. If the spatially-resolved and broadcast values agree to
better than 10%, **the spatial structure is carrying <10% of the result and bin Z
fires.** This is a genuine gate, not a formality: the blob is compact, so `ε₁₁` is
nearly flat across the matter support, and **Z1 is the clause most likely to fire.**
If it does, the honest reading is that the frozen families cannot resolve the
weight's spatial content and a broader source profile is required — a **design**
change, per §1.3, not a bin change.

### 11.2 · Z2 — configuration non-degeneracy

`η_mixed` is a **slope**; a family with no lever arm in `f` produces a slope that is
pure noise. FAM-A spans `f = 0.0234 → 0.0561`, ratio **2.40** (edge: ≥2.0 — passes,
and by a thin margin, which is itself worth recording). FAM-B spans `λ = 0.25 → 8`,
ratio **32** (edge: ≥8 — passes). Both are stated so the run cannot quietly shrink a
family and still bin.

### 11.3 · Z3 — instrument resolving power

If the four installed coefficients `k ∈ {0, 1/7, 2/7, 1/2}` do not produce four
separated `c` values, the instrument cannot tell weights apart and **every** verdict —
PASS included — is an artifact. Predicted separations in the linear limit are
`c = 0, 0.2857, 0.5714, 1.0000`, i.e. adjacent gaps of ≈0.286 against a λ=1 bracket
half-width of ≈0.004: a margin of **≈74×** against the required 10×. **This gate is
expected to pass with room, and its purpose is to prove the gate could have failed.**

### 11.4 · Z4/Z5/Z6 — degeneracy, phase-state, stencil

- **Z4** guards the `∇ε₁₁ → 0` limit, where `U_bind → 0` and `c` is `0/0`.
- **Z5** guards the declared phase-state. `max A ≥ 0.99` means the core is pinned
  against the yield cap: `D = 1/S → ∞`, the Picard loop stops converging (measured:
  λ ≥ 12, §1.2), and the run is no longer sub-yield. **A result read there would be
  a wrong-regime artifact, which is not a falsification.**
- **Z6** guards the stencil. Every `|∇ε₁₁|²` in every ledger term must come from the
  native diamond-K4 `Grad` (`_build_native_grad_div`); the code names this the
  load-bearing checkpoint (`backreaction.py:110-112`, verbatim: *"a Cartesian
  np.gradient here would be a non-native leak (the load-bearing K4 checkpoint)"*).
  **A structural null read off a Cartesian stencil would validate a stencil bug as
  physics.**

### 11.5 · The anti-tautology probe — can each gate fire in BOTH directions?

| gate | can it FAIL? | demonstrated by |
|---|---|---|
| A1 `k_meas` | YES | installing `k = 2/7` or `1/2` moves it by 2–3.5× (§5.4) |
| A2 bracket | YES | the **shipped** quadratic weight drifts 17× across FAM-B and misses at every rung |
| A3 D-register | YES | if the drift is boundary leakage or clip rather than `⟨D⟩`, `c^D` will not collapse |
| A4 `V_resid` | YES | it fails at λ ≥ 12, where the fixed point does not converge |
| Z1 broadcast | YES | **expected to be the tightest clause** (§11.1) |
| Z3 discrimination | YES | but with ≈74× margin — a receipt, not a risk |

**No gate in this prereg is satisfied by its own construction, and none encodes the
authoring context** (no branch shape, no live line numbers, no self-derived key
values in any fixture).

## 12 · ★ ANTI-FITTING GUARD — the k = 1/2 trap, declared in advance

**The reconciliation is the TEST, never the selection criterion.** This section
records the traps in advance so that no downstream lane can walk into one and call
it a result.

### 12.1 · The selection receipt

The frozen weight was selected by the ponderomotive derivation (§3.2) — five steps,
four of them already printed in canon — and by nothing else. **The check the guard
demands has been run: does the selected weight drive `η_mixed` to zero? IT DOES NOT.**
It moves `η_mixed` from `+1.048` (shipped quadratic) to `+0.831` — a 21% improvement
that still **misses the reconcile tolerance `|η| < 1×10⁻³`
(`src/tests/engine_acceptance/test_nordtvedt_eta.py:78`, verified verbatim) by
~830×**, and misses on the **same side** as the weight it replaces.

**A derivation that were fitted to the reconciliation would have landed on `k = 1/2`.
It landed on `k = 1/7`.** That is the receipt.

### 12.2 · ★ TRAP 1 — the reconciling coefficient is `k = 1/2`, and it is FORBIDDEN

§4.5 is exact: `η_mixed = 0 ⟺ c = 1 ⟺ k = g_self/2 = 1/2`. So there **exists** a
clock coefficient that reconciles perfectly, and it is a suspiciously
respectable-looking number — "half the potential" wears the pedigree of the `½` in
the self-energy integral that avoids counting pairs twice.

**There is no substrate route to `k = 1/2`.** The projection canon derives is `1/7`
(`ponderomotive-equivalence.md:14`). `k = 1/2` is pure fitting dressed in a familiar
factor.

**PRE-DECLARED:** if the run measures `k_meas ≈ 1/2`, that is **bin C**, reported as
*"the ledger requires a coefficient the substrate does not derive"* — a **derivation
conflict routed to Grant**. It is **not** licence to install `k = 1/2`.

### 12.3 · ★ TRAP 2 — `η → 0` is reachable by tuning `g_self`, and `g_self` is FROZEN

`c = 2k⟨D⟩_w·χ/g_self`, so `η → 0` is reachable at
**`g_self = 2k = 2/7`** — and `2/7` is `ν_vac`, a canonical AVE constant living in
the same file (`src/ave/gravity/backreaction.py:646`, verified verbatim:
`nu_vac: float = 2.0 / 7.0`; `:670`: *"trace-reversed Poisson ratio (2/7); maps ε₁₁
→ refractive index"*). A scoping lane measured `η_lin = −0.0005` at exactly
`g_self = 0.2857`.

**This is a COINCIDENCE, not a chord, and the provenance trace dissolves it:**

| side | construction | value |
|---|---|---|
| the reconciling `g_self` | (2 from the **discrete virial identity** on `Gradᵀ D Grad` with Dirichlet faces) × (1/7 from the **ponderomotive isotropic projection**) | 2/7 |
| `ν_vac` | `(3K − 2G)/(2(3K + G))` evaluated at `K = 2G` — a **Poisson ratio** | 2/7 |

Different parts, no shared factor, same number — the ½/¼ over-determination tell.
And the deeper tell: `c = 2k/g_self = 1` **forces** `g_self = 2k` **algebraically**
from the two coefficients that were put in. **Reading `g_self` off a reconciliation
condition is the definition of back-solving.**

**PRE-DECLARED:** `g_self ≡ 1.0` is **FROZEN** for this run (§4.4 shows it is forced
by the engine's own operator, `κ_op ≡ 1`, not chosen). **No `g_self` sweep may enter
any bin.** A `g_self` sweep may be run and reported **only** as a labelled warning
figure, exactly as here. X44 §4b fenced this in words
(`research/2026-07-12_x44-komar-source_result.md:90-92`: *"a retune to force
`U_bind ≈ Δ_clock` would manufacture η→0"*); this prereg makes the fence numeric and
records that the target has **moved closer** — under the shipped quadratic weight the
manufacture required cranking amplitude ~10× out of band, under the derived weight it
requires only `g_self = 2/7`.

### 12.4 · The prohibition list — frozen

For the duration of this arc, **none of the following may be done, and none may enter
a bin**:

1. Changing `k` away from `1/7` because a different value reconciles.
2. Changing `g_self` away from `1.0` for any reason.
3. Re-freezing FAM-A or FAM-B to move `f` toward the reconcile point.
4. Adopting the D-consistent register `U_bind^D` as the *headline* ledger because it
   is tidier — it is a **diagnostic** (A3) in this run; promoting it is a separate,
   Grant-gated decision.
5. Reading `η_mixed` as an adjudication of anything (§4.5, §10).
6. Reporting bin C's named coefficient as a proposal rather than a conflict.

**If a lane finds itself preferring a functional form because it reconciles, that is
fitting: it must say so, and stop.**

## 13 · Disclosure — what is pre-registered vs what is already measured

**A prereg that quietly pre-registers numbers someone already measured is not a
prereg.** Two scoping lanes ran before this document was written, and part of the
primary result is therefore **POST-DICTED**. Stating which part:

### 13.1 · ALREADY MEASURED before this freeze — post-dicted, NOT pre-registered

| quantity | value | source |
|---|---|---|
| `η_lin` under the derived linear weight, FAM-A, N=24 | **+0.8280** | scoping lane, monkeypatched `komar_weight`, this session |
| `c_lin` across a 16× amplitude span | **0.2848 → 0.2780** (2.4% drift) | same lane |
| `Δ_clock/U_bind` under the **shipped** weight | 0.0115 → 0.1950 (∝ λ) | same lane |
| `∫T₀₀ε/U_bind` on FAM-A | 2.0058, 2.0029, 2.0016, 2.0010 | same lane |
| `η` at `g_self = 2/7` | −0.0005 | same lane (run as a warning, §12.3) |
| the accessible-regime bounds (§1.2, §5.2) | the λ-table | **this document's own driver** |

**P6 (`η_mixed = +0.831 ± 0.010`) and the `c ≈ 2/7` anchor are consequently
CONFIRMATORY, not predictive.** They are stated as predictions because the run must
reproduce them under a clean, gated, non-monkeypatched install — but **no lane may
bank them as a successful pre-registration.**

### 13.2 · GENUINELY PRE-REGISTERED — not measured by anyone at freeze time

| # | content | why it is new |
|---|---|---|
| **P9** | the D-consistent register `c^D = (2k/g_self)·χ` collapses the amplitude drift **exactly** | no lane has computed `U_bind^D`; the closed form separating `⟨D⟩_w` from `χ` is derived in §4.3 of this document |
| **P7** | `c` at `N ∈ {24, 32, 40}` | the scoping lane ran **N=24 only** and flagged the missing resolution receipt as its own blind spot |
| **P8** | the four-coefficient discrimination `k ∈ {0, 1/7, 2/7, 1/2}` | only `k = 1/7` was ever installed |
| **P4** | the two-method identity with `⟨D⟩_w` and `χ` measured independently | `⟨D⟩_w` and `χ` have never been separated; the 2.4% drift was attributed to `D` without measuring it |
| **P3** | the pre-computed bracket at every rung | the bracket is derived in §5.3 of this document |
| **P10** | no engine observable discriminates weights independently of the install | not previously posed |
| **Z1** | the broadcast-degeneracy detector | not previously posed; **expected to be the tightest gate** |
| — | the amplitude band above λ=4 (`max A` to 0.783, and the `f` turnover) | the scoping lane stopped at λ=4 |

### 13.3 · What this means for the arc's banking basis

**Bin A, if it fires, banks on P9 + P7 + Z1 — the pre-registered clauses — with the
post-dicted `c ≈ 2/7` and `η ≈ +0.83` reported as reproductions.** The result document
must carry this split verbatim. **Reproducing a known number is a regression receipt,
not evidence.**

## 14 · Method, blind spots, and the completeness statement

### 14.1 · What I read in full this session

`research/2026-07-12_x44-komar-source_prereg_FROZEN.md` (193 lines, complete);
`research/2026-07-12_x44-komar-source_result.md` (295 lines, complete);
`src/ave/gravity/backreaction.py` regions `:95-200`, `:230-300`;
`src/ave/gravity/gw_propagation.py` regions `:514-582`, `:655-730`;
`src/tests/engine_acceptance/_nordtvedt.py` `:96-178`;
`src/tests/engine_acceptance/test_nordtvedt_eta.py` `:60-129`;
`src/ave/solvers/graded_vacuum_network.py` `:222-231`.

### 14.2 · What I verified by targeted read (every file:line in this document)

Each citation below was read this session, in this worktree, at `a3f4fef7`:
`ponderomotive-equivalence.md:14,:19` · `temporal-spatial-lattice-decomposition.md:14,:24,:28` ·
`eq_axiom_4.tex:7,:10` · `saturating-modulus-and-backreaction.md:50-53,:130` ·
`manuscript/ave-kb/vol3/claim-quality.md:104` · `backreaction.py:110-112,:114-115,:163,:191-194,:235-252,:646,:670` ·
`gw_propagation.py:566-567,:578-579,:671-677,:700,:703,:705` ·
`graded_vacuum_network.py:229-230` · `_nordtvedt.py:167-178` ·
`test_nordtvedt_eta.py:78` · `research/2026-08-11_gravity-linearity-audit_result.md:645,:658,:661` ·
`_orchestration/2026-07-10_rulings-docket.md:855,:857-860,:869-871`.

### 14.3 · ★ COMPLETENESS — what my method can and cannot support

**Two-method receipts taken on:**
- the **stress/Tolman register absence** — three methods (§9.2): `def`/`class` regex
  over `src/`, filename scan, and a `Tolman|3∫p` token count (0 hits);
- the **accessible-regime bounds** — measured by driver **and** cross-checked against
  the analytic `⟨D⟩`/`χ` envelope;
- **`η(c)`** — closed-form algebra **and** agreement with X44's measured `η_matter`
  to 0.23%.

**Blind spots, stated:**

1. **This is NOT a corpus census of `√S`.** §2's two-function table is the sweep's
   finding, and a companion lane enumerated **six** distinct functions of `ε₁₁`
   wearing the glyph family across three orthogonal ambiguity axes. **I did not
   re-run that enumeration.** Everything §2 says is a claim about the sites it names
   and I read — not about the corpus.
2. **I did not read the frozen `#651` prereg**, only X44's prereg and result. The
   family's provenance is taken from X44's own restatement.
3. **The regime map is `σ = 1.8` only.** `f_sup ≈ 0.186` is measured at one blob
   width at `N = 24`. A different `σ` or `N` could shift it — **though not by the
   3.2× that would rescue the old PASS bin**, since the ceiling is set by the yield
   cap, not by the profile.
4. **`Div = Gradᵀ` is read off the construction** (`gw_propagation.py:566-567` vs
   `:578-579`), **not** verified numerically. The run must assert
   `‖Div − Gradᵀ‖ = 0` before trusting §4.2. *(Added to the run's gate list, §15.)*
5. **I did not read the 2026-08-11 audit end-to-end**, only the cited lines. Its §9
   is self-tagged `⚑ UN-AUDITED` and is used here as corroboration of the **slope
   only**, never as authority (§3.4).
6. **Grep-completeness.** Where I state a count, it is a count of what the stated
   pattern matched, with the method named. **No claim in this document is of the form
   "the only X" or "no leaf" or "every site".**

### 14.4 · Consensus-bias symmetric standard — applied, both directions

GR itself carries **ADM, Komar and Bondi** masses, which differ, and is not faulted
for it. **"AVE has more than one mass register" is NOT a finding here and is not
reported as one.** The finding is narrower and would be a defect in any framework:
**one symbol denoting two different functions of one variable** (§2), and a ruling
certifying a code object whose slope contradicts the ruling's own word (§3.3).
Conversely, the standard is not relaxed for AVE either: `η_mixed ≈ +0.83` is a real
gap between two of the engine's own registers, and §9 does not explain it away.

## 15 · Out of scope · Deliverables · Gates

### 15.1 · Gates the run must execute (all of them, before binning)

1. **Adjointness assertion** — `‖Div − Gradᵀ‖ = 0` (blind spot 4, §14.3). §4.2's
   closed form is void without it.
2. **Z-gate suite** (§11) — Z1…Z6, evaluated and reported **before** any selecting bin.
3. **Y-gate suite** (§10.3) — convergence, `V_resid`, Gauss residual, resolution.
4. **The four-coefficient discrimination sweep** `k ∈ {0, 1/7, 2/7, 1/2}` (P8).
5. **FAM-B amplitude ladder** at N=24; **FAM-A** for the reported `η_mixed`.
6. **Resolution receipt** `N ∈ {24, 32, 40}` at λ=1 (P7).
7. **The P10 enumeration** — every engine observable that could respond to the weight
   other than through the installed source, listed and tested, with the completeness
   rule applied to the list.
8. Existing `#86` suite and `engine_acceptance` consumers GREEN; `make verify` PASS;
   `mass = A1` untouched.

### 15.2 · Out of scope (flag, do not do)

- Everything in §6.3 and §12.4.
- Editing any canon leaf, ruling, or docket entry — including the two defects this
  prereg flags (Ruling 1's code attribution, §3.3; the 2026-08-11 proposal's
  direction ambiguity, §3.4). **FLAG-DON'T-FIX: the disambiguation is the
  deliverable; the corrections are Grant's.**
- Resolving the `√g₀₀` vs `1/n_scalar` `O(ε₁₁²)` fork (§3.4).
- The corpus-wide `√S` census (a companion lane's six-function enumeration).
- Building the `T_ij` / stress register (the X44b charter's own arc).

### 15.3 · Deliverables

- [x] **This FROZEN prereg** — pushed before any engine edit, driver, or test exists.
- [x] `research/drivers/x44_unblock_regime_map.py` — the reachability arithmetic,
      reproducible.
- [x] `_orchestration/open-items/2026-08-27-x44-unblock.md` — ROUTED-TO-GRANT.
- [x] Board regenerated from the derived sources.
- [ ] Engine leg: the frozen weight behind an explicit mode, legacy modes retained
      (KEEP-BOTH). **Does not exist at freeze time.**
- [ ] `research/2026-08-27_x44-unblock_result.md` — must carry §13's post-dicted /
      pre-registered split verbatim.
- [ ] PR `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` — no self-merge.

### 15.4 · Freeze statement

This document is **FROZEN**. Its bins (§10), its weight (§3), its `g_self` (§4.4),
its families (§5.1), its predictions (§7), its falsifiers (§8) and its prohibitions
(§12.4) may not be edited by the run they govern. Amendments, if any, are **new dated
documents** — the frozen text is never rewritten. The freeze commit records the SHA
of the frozen content.

**Frozen bins enforce; flags do not.**
