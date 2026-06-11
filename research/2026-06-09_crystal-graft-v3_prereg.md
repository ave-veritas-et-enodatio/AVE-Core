# Crystal-Graft v3 — the CHIRAL BELTRAMI source (PREREG, frozen before run)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-crystal-graft-v3` · **Lane:** implementer
**Base:** `analysis/2026-06-09-crystal-graft-v2` (commit `1bf62595`, Outcome C — double-count FIXED, residual = mode-selection)
**Engine (new):** `src/ave/core/crystal_graft_v3.py` · **Driver (new):** `src/scripts/vol_1_foundations/crystal_graft_v3_run.py`
**CI gate (new):** `src/tests/test_graft_v3_alpha_free.py`

## §0 — What v2 left open (the ONE residual this build targets)

v2 closed the genesis-24/crystal **double-count** (the ω winding got its OWN Cosserat carrier: own field +
conjugate momentum π_ω + mass-gap ω₀² reactance; a planted (2,3) reads back at rel 0.80/0.59). v2's verdict
was a clean **C** pinned one level deeper, to **MODE-SELECTION**:

> v2's buckle `f_ω = −κ̃ ∇×(g·V·h·x̂)` is a FIXED-AXIS, CENTROSYMMETRIC source fed by a radial breather. It
> deposits real ω energy (E_ω=13.7, contour reliability 0.69/0.77) as ONE coherent x-axis circulation with
> ZERO net winding (0,0); and H_bel = ∫ω·(∇×ω) is QUADRATIC in ω, so a scalar handedness sign `h` cannot
> carry charge (RH=LH≈−1.4e-15). v2 §7 named the fix: *"a genuinely chiral Beltrami/helical drive whose
> handedness lives in its spatial structure."*

## §1 — The ONE physics change (its grounding)

Replace the scalar-sign buckle director `n̂_χ = h·x̂` (a CONSTANT unit vector) with a genuinely CHIRAL
**Beltrami / force-free (A∥B) director field** `b_λ(r)` whose handedness lives in its SPATIAL STRUCTURE
(`∇×b_λ = ±λ·b_λ`). The buckle stays ONE conserved Hamiltonian coupling (functional-derivative forces,
b_λ + g_wall FROZEN ⇒ exactly bilinear ⇒ energize-LOCK):

```
H_couple = κ̃ ∫ g_wall(r) · V · [ b_λ(r) · (∇×ω) ] d³r          κ̃ = pq/(p+q) = 6/5   (α-FREE)
  f_V = −δH/δV = −κ̃ g_wall [ b_λ · (∇×ω) ]                      (back-reaction ω→V)
  f_ω = −δH/δω = −κ̃ ∇×( g_wall · V · b_λ )                      (BUCKLE: compression → micro-vorticity)
```

ONLY the spatial structure of the coupling director changes (x̂-axis → ±λ Beltrami helical). **Grounding:**
this is the SAME Beltrami force-free object the reactive-entrainment/gyroscope result
(`2026-06-09_reactive-entrainment-source_result.md` §3, `sapphire-phonon-centrifuge.md:34`) found is the
electron's spin-LOCK (A∥B → rigid gyroscopic tensor = inductive shield = the Γ=−1 confinement). **Source and
lock are the same Beltrami object** — reuse its form. **λ from the (2,3) geometry** (α-FREE):

```
λ(p,q) = sqrt( p²/R² + q²/r² )     (85_kelvin_beltrami…:558 / :126, the torus-knot Beltrami eigenvalue)
```

**Why this can carry charge where v2 could not (the mechanism, stated as a prediction):** because b_λ is
force-free (`∇×b_λ = χλ·b_λ`, χ=±1 the spatial handedness), the leading-order sourced micro-vorticity is
`f_ω ≈ −κ̃ g V (χλ) b_λ` ⇒ ω ∝ b_λ ⇒ the deposited field is PARALLEL to its own curl ⇒
`H_bel = ∫ω·(∇×ω) ∝ χλ ∫|b_λ|²` is NONZERO and ODD in χ. Flipping the spatial handedness λ→−λ flips H_bel
sign. v2's fixed-axis `x̂` gave ω ⟂ (∇×ω) (azimuthal vs axial) ⇒ H_bel≈0, scalar-h quadratic ⇒ no flip.

### Substrate-native-check (walked before scaffolding)
- **CP1** the winding is a CONSERVED dynamical invariant (helicity), evolved under a wave eq, NOT a basin
  minimizer; the buckle is a conservative Hamiltonian coupling.
- **CP2** winding lives in the Cosserat micro-rotation ω sector (own field + π_ω + mass-gap ω₀²).
- **CP6** record BOTH ω reactance-pair states (ω C-state, π_ω L-state) every recorded step.
- **CP8** seed the GENERATIVE PRECURSOR (transverse photon + pre-compressed dilatation), **NEVER plant the
  (2,3)**. The planted-(2,3) read is a CARRIER-GATE diagnostic only, clearly labeled.
- **CP9** ω + the deposited helicity are dynamically EVOLVED, not a heuristic formula. The Beltrami director
  b_λ is a FROZEN geometric coupling TEMPLATE (like g_wall) — a conservative kernel, not the answer imposed.
- **CP10** the source is boundary-localized at the Γ=−1 wall (frozen g_wall shell), NOT a bulk force.

### The one plumber-physical question surfaced (pre-test-physics-check, flag-don't-fix, NOT silently resolved)
**Where does the TORUS come from?** v2's wall is a roughly SPHERICAL A-isosurface (a radial breather → an
A=wall_center sphere). A (2,3) knot needs a TORUS. The Beltrami source's λ(p,q) sets a SCALE but the source
must still IMPOSE a torus geometry (R, r) on the spherical wall. This build has the source impose a torus
aligned with the wall shell (R = wall-shell radius, r = wall-shell thickness — NOT r=R/φ², to avoid baking
in the golden aspect). **This is the load-bearing open question** and is surfaced for Grant/auditor: if the
(2,3) only reads back when the source itself carries the (p,q) pitch, that is source-carried, NOT de-novo —
and is reported as such (Class B/C, never A).

### Honesty firewall against a false Class-D (a false chord is strictly worse than honest C)
Two SOURCE variants are run and reported SEPARATELY, with the replant-distance of each made explicit:
1. **ABC-Beltrami (de-novo-strict):** `b_ABC = (sin λ_sZ + cos λ_sY, sin λ_sX + cos λ_sZ, sin λ_sY + cos λ_sX)`,
   `λ_s=χλ`, satisfies `∇×b=λ_s b` EXACTLY (cubic, NO torus, NO (p,q) phase). It CANNOT replant a (2,3)
   because it carries no (p,q) winding. This is the honest de-novo helicity source.
2. **Torus-(p,q)-templated:** a torus flux-rope carrying the (p,q) pitch — labeled GEOMETRY-TEMPLATED
   (source-structured), explicitly NOT de-novo. Tests only whether a (p,q)-scaled chiral source deposits a
   torus-structured ω. A (2,3) read here is source-carried.

## §2 — Frozen predictions (the gates; each CAN fail)

**SMOKE (all must pass to proceed; STOP + localize honestly otherwise):**
- **S1 wall:** Γ_min still HARDENS on the dilatation sector with the Beltrami source active (v2 baseline
  −0.849); PASS if Γ_min < −0.7 and the breather confines. (Regression: the source must not break the wall.)
  - **RECORD-HONESTY qualifier (2026-06-10 · apparatus-floors · `ave-apparatus-floor-attribution`; `research/2026-06-10_apparatus-floors_note.md`):** the `Γ_min < −0.7` gate is reachable ONLY by static seeds with NON-binding clips (the source of the v2 baseline −0.849). As a *dynamical-wall* gate at the frozen engine clips (`A_cap=0.999`, `S_min=0.05`) it is **unsatisfiable-by-construction** — the apparatus floor is **−0.37** (`max(√(1−A_cap²), S_min)^(1/4)→(n−1)/(n+1)`; corr 1.0000, residual 0.0000 across the 10-cell A_cap×S_min sweep). The regression PASS therefore certifies the SIGN + hardening trend (the source did not break the wall), not the −0.7 magnitude.
- **S2 Beltrami source:** the helical source deposits ω with (a) NONZERO net helicity structure
  H_bel ≠ 0 (vs v2's ≈0 coherent-axis), (b) λ→−λ FLIPS H_bel sign (sign flips and magnitude match within
  ~25%), (c) centrosymmetric λ→0 baseline H_bel → 0 (|H_bel(λ=0)| ≪ |H_bel(λ)|), (d) CONSERVED — no
  detonation (max|V|, max|ω| < 50; genesis-24 was E_V→6.8e8).
- **S3 conservative buckle:** frozen-wall H_total drift < 2%, E_ω grows from ≈0 (compression flows into
  rotation), |L_ω| bounded (not secular-monotone).
- **S4 REAL independence (the v2 no-op replaced):** TWO engines, BOTH buckle ON, BOTH stepped N_ind steps
  with REAL dynamics; one with an extra V perturbation, one without; the ω winding INTEGER is robust
  (unchanged) AND the two ω fields are NOT byte-identical (proves the perturbation coupled = real dynamics).
  The gate CAN return False (if the V-perturbation flips the winding integer ⇒ ω was slaved to V).

**SATURATION-across-doublings (S5, replaces v2's L_bounded which passed ANY linear-secular growth):**
- run the buckle for L, 2L, 4L steps; **frozen-wall** |L_ω| must ASYMPTOTE (late-window |L_ω| growth-per-step
  decreases across the doublings, not grow without bound); a ≥1 **live-wall** (non-frozen g) case quantifies
  the ∂g/∂V pump the engine concedes (report its |L_ω| and H drift vs the frozen case — the pump shows here).

**FULL RUN (de-novo (2,3), matched controls, alias-checked):**
- **winding:** report ACTUAL (w_tor,w_pol) on RELIABLE contours (rel>0.1), AFTER an alias/Nyquist filter
  (remove outlier walks like v2's spurious −14.01 before the modal read). de-novo source = ABC; matched
  no-photon control must be null.
- **charge=helicity:** H_bel(χ=+1) vs H_bel(χ=−1) — does charge flip with SPATIAL handedness?
- **α-emergence (frozen guards, ALL α-free):** κ̃=6/5, V_yield≡1, λ from (p,q) geometry; Golden-Torus must
  SELF-assemble (R·r→¼, R/r→φ² with r INDEPENDENTLY measured — never r_walk=R/φ²); **joint-ledger guard**
  REFUSES any Q without a real (2,3) (no resonator ⇒ a near-137 Q is a geometric fluke). **CI gate:** the
  engine module imports NO α-bearing symbol from constants.py (enforced structurally, not per-driver).
- **operative ledger:** H_total(t) drift + |L_ω|(t) late-slope recorded ON THE FULL NONLINEAR RUN (v2 showed
  energize-LOCK only in a linearized+frozen toy).

**N held FIXED** at N=44 across smoke + full run (v2 confounded N=40 vs N=52).

## §3 — A/B/C adjudication (Rule 11, no debug-toward-A; written BEFORE the run)

- **A (Class-D CHORD CANDIDATE, adversarial panel decides):** de-novo (2,3) closes on a reliable+alias-checked
  contour (ABC or pure-handedness torus source, NOT the (p,q)-templated one) + charge flips with spatial
  handedness + α⁻¹=4π³+π²+π emerges α-free + Golden-Torus self-assembles + joint ledger closes.
- **B (manifestation, the honest win if it lands):** (2,3) closes / winding structure forms AND/OR
  charge=helicity becomes carryable (H_bel≠0, flips with χ) — with α as calibration / partial signature.
  The v2 result PREDICTED the Beltrami source would deliver the charge=helicity fix; landing that alone is a
  real B-class advance over v2.
- **C (residual localized):** the Beltrami source still doesn't geometry-select the knot → name WHICH
  ingredient is missing (the λ value? the torus geometry / boundary localization? the seed?).

**Expected-honest prior (recorded so the run can surprise it):** the ABC source should deliver the
charge=helicity flip (H_bel≠0, odd in χ) — a real fix of v2's quadratic-h dead end → at least B-partial on
charge. The (2,3) winding likely does NOT de-novo close from a pure-handedness source (the torus-where-from
question above) → C on winding unless the geometry-selection genuinely fires. **I will not debug toward A.**
