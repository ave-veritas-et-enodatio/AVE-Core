# Crystal-Graft v2 — the winding gets its OWN Cosserat-ω carrier (RESULT)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-crystal-graft-v2` · **Lane:** implementer
**Prereg (FROZEN):** [`2026-06-09_crystal-graft-v2_prereg.md`](2026-06-09_crystal-graft-v2_prereg.md)
**Engine:** [`src/ave/core/crystal_graft_v2.py`](../src/ave/core/crystal_graft_v2.py) ·
**Driver:** [`src/scripts/vol_1_foundations/crystal_graft_v2_run.py`](../src/scripts/vol_1_foundations/crystal_graft_v2_run.py) ·
**Results:** `crystal_graft_v2_results.json`

## VERDICT — C (honest, well-localized; the double-count is FIXED)

> **The re-scoped engine closes the genesis-24/crystal double-count** — the ω winding carrier is now
> structurally able to host `w_pol ≠ 0` (SMOKE-3 PASS). But the de-novo `(2,3)` does **not** self-assemble:
> the buckle sources real ω ENERGY (E_ω=13.7, high contour reliability 0.69/0.77) yet **no coherent
> winding** (`w_tor=w_pol=0`). The residual is now **MODE-SELECTION** (the buckle deposits micro-rotation
> energy but does not imprint the toroidal-2/poloidal-3 knot), **NOT** the double-count. α is **refused**
> by the joint-ledger guard (no real `(2,3)` → no resonator). This is the most-informative C in the
> genesis-23→24→crystal→graft-v2 arc: it removes the structural obstruction the prior run was pinned to,
> and pins the new one one level deeper.

| Quantity | Result | Bar | Pass |
|---|---|---|---|
| SMOKE-1 wall hardens | `Γ_min = −0.849` (deepest; monotone toward −1) | `< −0.7`, vs genesis-24 `−0.08` | ✅ |
| SMOKE-2 buckle conservative | linear-bulk stencil-energy drift **−0.007%**, span 0.66% | `< 2%` | ✅ |
| SMOKE-2 energize-LOCK | `\|L_ω\|` bounded oscillation (max 16.2, non-monotone); max\|V\|=0.88 max\|ω\|=0.45 | no detonation / no secular | ✅ |
| SMOKE-3 carrier hosts (2,3) | known-seed reads `(2,3)` at rel `(0.80, 0.59)` | `(2,3)` | ✅ |
| SMOKE-3 ω independent of V | winding read UNCHANGED under large V perturbation | unchanged | ✅ |
| **Double-count fixed** | **w_pol structurally able to be nonzero = True** | True (prior: ≡0) | ✅ |
| Full run (2,3) de-novo | `(w_tor,w_pol)=(0,0)` both chiral arms; control null | `(2,3)`, control null | ❌ |
| Golden-torus self-assembles | `R/r_meas = 1.75` vs `φ² = 2.62` (33% off; **r independently measured**) | within 25% + real (2,3) | ❌ |
| α⁻¹ emerges (α-free) | **REFUSED by joint-ledger guard** (no real (2,3)) | `4π³+π²+π` | ❌ |

## §0 — The two distinct "3"s (Grant-ratified, recorded verbatim)

The "3" is **TWO DISTINCT objects**, orthogonal (A1 ⊥ T2):

- **MASS = the longitudinal DILATATION** (Heaviside-excised compression scalar, the A1 breather). `mₑc²` =
  trapped acoustic compression energy. In the engine this is the bulk scalar `V` with `c_eff(V)=c0·S^{−1/2}
  →∞` in the saturated core (refractive `n=S^{1/4}→0`) self-creating a **hardened Γ=−1 acoustic wall**.
  (`trampoline:249` "pure radial dilation, the only mode with no rotational character".)
- **WINDING = the (2,3)-knot poloidal circulation** living in the Cosserat **MICRO-ROTATION ω sector**
  (T2, couple-stress, Axiom-1 intrinsic-spin DOF). The `(2,3)` = toroidal "2" + poloidal "3"; charge =
  Beltrami helicity `H_bel = ∫ω·(∇×ω)`.

**NEVER wire the winding into the breather's own phasor `(V_inc, V_ref)`** — that is a read-only projection
of the SAME scalar `V` (`master_fdtd_phasor_bridge.py:14-18`; `k4_tlm.py:346` `V_ref=0.5·ΣV_inc−V_inc` is
NOT independent). Doing so self-inflicts `w_pol=0` (the genesis-24/crystal double-count the pressure-test
caught). **This build gives the winding its own Cosserat-ω carrier so `w_pol` CAN be nonzero.**

## §1 — The fluid-dynamics / vacuum-engineer carrier spec (recorded verbatim)

> The vacuum is a compressible chiral Cosserat continuum. Helmholtz split: irrotational (∇·u, bulk K = the
> DILATATION/breather) + solenoidal (∇×u shear G = the transverse photon; micro-rotation ω couple-stress =
> the intrinsic spin/winding). The electron = a KNOTTED VORTEX RING whose entrained-compression (added-mass)
> is its rest MASS and whose vortex-line linking (helicity) is its CHARGE/spin, held at a Γ=−1 acoustic-
> impedance wall it generates by over-saturating the medium.
>
> - MASS = trapped DILATATION (∇·u, bulk-modulus K, the A1 monopole breather). mₑc² = trapped acoustic
>   compression energy.
> - PHOTON = transverse shear wave (∇×u, shear G).
> - WINDING = the Cosserat MICRO-ROTATION ω (couple-stress sector, Axiom-1 intrinsic-spin DOF); the (2,3) =
>   its toroidal "2" + poloidal "3" circulation numbers; charge = Beltrami helicity H_bel = ∫ω·(∇×ω).

## §2 — The diagnosis this build acted on (verified in code, not assumed)

The prior crystal engine (`6af430cd`) was a clean Outcome C pinned to one mechanism: *the scalar
Master-Equation bulk has no multi-component U(1)-fibre carrier*. Verified this session:

- `crystal_engine.py:304-318` `phase_space_vinc_vref` → `(V, ∂_tV/ω, V, −∂_tV/ω)`: V_inc and V_ref are BOTH
  projections of the ONE scalar `V` (a single complex scalar `V+i∂_tV` traces a **circle**, not a torus).
- One of the two windings is therefore structurally forced to 0. That is the genesis-24/crystal double-count.

## §3 — The re-scoped engine (3 orthogonal sectors + conserved buckle)

`CrystalGraftV2(CrystalEngine)` — `src/ave/core/crystal_graft_v2.py`:

1. **(V) bulk dilatation = MASS.** Reuses the validated `c_eff(V)` trap → hardened Γ=−1 wall. SMOKE-1.
2. **(w) transverse shear = PHOTON.** Linear vector wave at `c_T`; carries the seed helicity `h`.
3. **(ω) Cosserat micro-rotation = WINDING — NEW, INDEPENDENT U(1).** Own 3-vector field + own conjugate
   momentum `π_ω=∂_tω` + own **mass-gap LC reactance `ω_0²`** (the decoupled couple-stress reactance — what
   makes the ω tank independent of the bulk V). Evolved by its OWN wave eq `∂²_tω = c_ω²∇²ω − ω_0²ω +
   f_ω` (substrate-native CP9: a dynamically-evolved state variable, NOT a heuristic formula — so it CAN
   carry emergence).
4. **ADD-2 buckle** (one Hamiltonian coupling term, conserved): `H_couple = κ̃∫ g_wall·V·[n̂_χ·(∇×ω)]`,
   `κ̃=6/5` α-FREE. Forces are the functional derivatives:
   - `f_V = −κ̃ g_wall (∇×ω)_x` (back-reaction ω→V),
   - `f_ω = −κ̃ ∇×(g_wall·V·n̂_χ)` (BUCKLE: blocked compression → micro-VORTICITY = the winding carrier).
   The wall window is **frozen** at seed time (`freeze_wall_window()`) so `H_couple` is exactly bilinear ⇒
   the leapfrog conserves `E_V+E_ω+H_couple` (verified −0.007% with stencil-consistent energy). This is
   energize-LOCK (ave-conserved-vs-pumped), the opposite of genesis-24's EMF pump (`E_V→6.8e8`, `|L| 2.7→43`).

## §4 — SMOKE results (Rule 10; all PASS — gate to proceed)

**SMOKE-1 — the Γ=−1 wall HARDENS.** Static depth sweep (c_eff trap, integer-centered seed):

| A_core | 0.9 | 0.99 | 0.999 | 0.9999 | 0.9999999 | 0.99999999 | 0.999999999 |
|---|---|---|---|---|---|---|---|
| Γ_min | −0.10 | −0.24 | −0.37 | −0.49 | −0.75 | −0.80 | **−0.85** |

Γ_min drives **monotonically toward −1** as the core saturates (the c_eff trap works), vs genesis-24's flat
`|Γ|<0.08` (no trap). Breather **confines** (localization sustained over 400 steps). The floor is set by
`S_min` (named engineering knob; `Γ_min,floor = (S_min^{1/4}−1)/(S_min^{1/4}+1)`); the asymptote to −1 is the
rupture boundary A→1.

**SMOKE-2 — the buckle is CONSERVATIVE (energize-LOCK).** Two-part:
- *(A) conservation proof* (linearize bulk so the only cross-coupling is the buckle; measure
  stencil-consistent energy): `H_total` drift **−0.007%**, span 0.66% over 1800 steps; `E_V 33.46→33.06`,
  `E_ω 0.000→0.409` — **compression energy flows INTO rotation while total stays flat.** (Note: the naive
  `np.gradient` energy showed a spurious dt-independent ~43% "drift" — a pure measurement-basis mismatch vs
  the 7-point `_laplacian`/roll-`_curl` stencils the dynamics use; the continuum cancellation is exact.)
- *(B) energize-LOCK with the real nonlinear bulk*: `max|V|=0.88`, `max|ω|=0.45` (no detonation; genesis-24
  was `E_V→6.8e8`); `|L_ω|` is a **bounded oscillation** (max 16.2, non-monotone), NOT genesis-24's monotone
  `2.7→43`. Buckle-OFF baseline: `|L_ω|=0` (κ̃ inert ⇒ ω≡0).
- *FINDING (deferred to ledger):* `H_bel = ∫ω·(∇×ω)` is **quadratic in ω**, so a scalar handedness sign
  cannot flip it (RH and LH give equal `H_bel ≈ −1.4e-15 ≈ 0`). The fixed-axis buckle `∇×(g·V·h·x̂)`
  therefore sources micro-vorticity but **no net helicity / charge** — charge-sign = helicity-flip needs a
  genuinely chiral source structure, not a scalar `h`. This is part of the mode-selection residual (§6).

**SMOKE-3 — the ω winding sector is INDEPENDENT (the anti-double-count check, the LOAD-BEARING deliverable).**
- *(a) carrier gate:* a KNOWN-imposed `(2,3)` in ω reads back `(w_tor,w_pol)=(2,3)` at reliability
  `(0.80, 0.59)`, raw `(1.99, 2.99)` — where the old scalar bulk read `(*,0)`. **w_pol CAN be nonzero.**
- *(b) independence:* a large V perturbation leaves the ω winding read **UNCHANGED** `(2,3)` — ω carries its
  own phase; it is NOT a projection of V_inc.

## §5 — FULL RUN (de-novo (2,3) in the ω carrier)

Seed = CP8 generative precursor (helical transverse photon + pre-compressed dilatation seed, **NOT** a
planted (2,3)); drive the buckle 1400 steps; read the ω-sector `(2,3)` on the hosted shell (rel>0.1).

| arm | shell R | E_ω | (w_tor,w_pol) | rel | is(2,3) |
|---|---|---|---|---|---|
| photon + radial breather | 2.73 | 13.7 | **(0,0)** | (0.69, 0.77) | False |
| photon + 1-twist breather | 2.92 | 4.3 | **(0,0)** | (0.45, 0.67) | False |
| no-photon (null control) | 11.44 | 0 | (0,0) | (0.00, 0.00) | False |

**(2,3) closes de-novo: False. Matched no-photon control: null (True).** The buckle deposits significant ω
energy at HIGH contour reliability (0.69/0.77 — a coherent ω field exists on the shell) but with **zero net
winding**: the sourced micro-rotation is a coherent x-axis circulation, not a toroidal-2/poloidal-3 knot.
**w_pol is structurally able to be nonzero (SMOKE-3) but the buckle does not populate it (full run).** Those
two facts are the whole result: carrier capable, source structure wrong.

## §6 — α-EMERGENCE + the JOINT-LEDGER GUARD

α-free inputs (κ̃=6/5 AND V_yield≡1 — both circularity vectors removed):
- **Golden-Torus:** `R = 2.73`, `r_meas = 1.56` (**independently measured** tube half-thickness — NOT the
  tautological `r_walk = R/φ²`). `R/r_meas = 1.75` vs `φ² = 2.62` → **33% off; does NOT self-assemble.**
  (An earlier pass reported "R/r=φ² at 0.0% error" — that was the `r_walk=R/φ²` definitional artifact, caught
  and fixed by measuring r independently. Recorded as an honesty correction.)
- **α⁻¹ leak-rate Q:** **REFUSED by the joint-ledger guard** — there is no real `(2,3)` resonator, so any
  near-137 Q would be a geometric fluke (the genesis-24/crystal failure the guard exists to refuse). No
  α⁻¹=4π³+π²+π is claimed.

## §7 — Honest closure (Rule 11 / substitution-not-retraction)

This is a **clean Outcome C** and the **most-informative C in the arc**: it **closes the obstruction the
prior run was pinned to** (the double-count: w_pol is now structurally able to be nonzero — SMOKE-3 PASS,
carrier reads (2,3) independently of V) and **pins the new residual one level deeper**:

> **The new residual is MODE-SELECTION, not the double-count.** The conserved fixed-axis buckle
> `f_ω=−κ̃∇×(g·V·h·x̂)` sources ω ENERGY (the column-buckle-into-vorticity is real and conservative) but,
> from a radial breather with a *scalar* handedness, it produces a simple x-axis circulation — not the
> knotted toroidal-2/poloidal-3 structure, and (H_bel quadratic in ω) no net helicity. The `(2,3)` selection
> needs the **golden-torus resonance** (a genuinely chiral, geometry-selecting source — a Beltrami/helical
> drive whose handedness lives in its spatial structure), which this minimal buckle does not provide.

No framework failure; no debug-toward-A; no dropped legs; no emergence over-claim. The α near-137 fluke is
**refused** by the joint-ledger guard. Per substrate-native-check CP8 the next-layer question — *give the
buckle a chiral (Beltrami/helical) source structure so the (2,3) can geometry-select* — is **surfaced for
Grant/auditor, NOT auto-pivoted** (Rule 16). Per Rule 12, this doc retracts nothing it didn't earn; the
double-count fix is a real positive result and the mode-selection residual is the honest new boundary.

**Skills fired:** `ave-prereg` (corpus-grep + frozen prediction before build); `substrate-native-check`
(CP1 wave-not-minimization; CP2 winding lives in the ω phase-space; CP4 measured in matching coords; CP8
generative precursor seeded, structural-capability finding = mode-selection; CP9 ω is a dynamically-evolved
state variable; CP10 wall + buckle as boundary-localized, not bulk force — no detonation);
`ave-conserved-vs-pumped` (buckle = energize-LOCK, one Hamiltonian term, |L| bounded; genesis-24 pump is the
named failure fixed); `phase-space-coordinate-check` (the (2,3) read in the ω reactance-pair, not real-space
or the bulk-V phasor); `consistency-vs-emergence` (α-emergence REFUSED; the structural fix is the
manifestation-class deliverable); `verify-before-cite` (the double-count grepped at
`master_fdtd_phasor_bridge.py:14-18`, `k4_tlm.py:346`, `crystal_engine.py:304-318`; genesis-24 detonation;
κ̃=6/5, ALPHA_COLD_INV from constants.py); `ave-driver-script-honesty` (every number from the EVOLVED field;
NO optimizer onto (2,3); the R/r tautology caught and fixed; figures captioned to ACTUAL data).

**Figures** (`src/scripts/vol_1_foundations/`, data-derived captions):
- `crystal_graft_v2_fig1_smokes.png` — SMOKE-1 Γ_min→−0.85 hardening sweep; SMOKE-2 H_total flat while E_ω
  grows from 0; |L_ω| bounded oscillation.
- `crystal_graft_v2_fig2_winding.png` — carrier gate reads (2,3) (rel 0.80/0.59); de-novo arms all (0,0) at
  high reliability (0.69/0.77) — the carrier-capable-vs-source-wrong split.
- `crystal_graft_v2_fig3_alpha.png` — R/r_meas=1.75 vs φ²=2.62 (no self-assembly); joint-ledger guard
  REFUSING α (no real (2,3) → no resonator).

## §8 — Corpus-state updates queued (implementer SURFACES; auditor LANDS)

- **`research/2026-06-09_crystal-engine_result.md` §9 residual — REFINED, not refuted.** That doc pinned the
  obstruction to "the scalar bulk has no multi-component U(1)-fibre carrier." This build **confirms** that
  diagnosis (the independent ω carrier removes it — SMOKE-3) and **refines** the residual to mode-selection
  (the buckle source structure, not the carrier). Auditor decides whether to annotate.
- **`vol4/claim-quality.md:232` α-emergence-circularity strengthen-by — still REFINED, not discharged.** Both
  circularity vectors (κ̃=6/5, V_yield≡1) are α-free inputs here; α-emergence remains untestable because no
  real (2,3) hosts. The guard refusing the fluke is the correct behavior. Auditor updates the caveat.
- **No new axiom drafted** (per A44 missing-axiom-vs-engine-bug + Rule 16): the residual is an engine source-
  structure gap, surfaced for Grant/auditor, not a missing postulate.
