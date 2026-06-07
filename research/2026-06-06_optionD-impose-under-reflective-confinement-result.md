# Option-D (2,3) pair IMPOSE re-tested under the (II) moving-Γ=−1 reflective wall — RESULT

**Date:** 2026-06-07 · **Branch:** `analysis/2026-06-06-saturation-tir-moving-boundary` (off `main`)
**Driver:** `src/scripts/vol_1_foundations/phase5_optionD_under_reflective_confinement.py`
**Reuses:** `PairNucleationGate` (Option-D impose, pre-marked) + `AutoresonantCWSource` +
the (2,3) torus-knot seeder/bond-finder from `phase5_topological_pair_injection.py`
(the **MODE-III prior**, frozen `1c89fa1`) + the (II) `use_impedance_boundary` moving-Γ=−1
confinement (committed `688cc14d`/`34264a26`), ported to the coupled K4⊗Cosserat engine.
**Engine delta:** `cosserat_field_3d.py` + `k4_cosserat_coupling.py` + `vacuum_engine.py`
(`use_impedance_boundary` coupled port + `couple_v_sector` toggle + `impedance_implicit`
reactance-rotation integrator — KEEP-BOTH, default OFF, `make verify` green, 227 tests pass).
**Discipline:** `ave-prereg` (reuse + cite MODE-III prior) · `substrate-native-check` (CP1/2/4/6/8) ·
`phase-space-coordinate-check` · `consistency-vs-emergence` (**IMPOSE/STABILITY test, class =
consistency — NOT emergence**) · `ave-driver-script-honesty` · `ave-evidence-framing` · KEEP-BOTH.

---

## §0 Headline — VERDICT (III), with a precise two-regime mechanism

> **(III) The imposed (2,3) pair does NOT persist as a stable bound state under the (II)
> reflective wall. Swapping the native confinement for the moving Γ=−1 boundary — with or
> without the V-sector coupling — does NOT rescue the MODE-III dissolution. The wall is not
> the missing "coupling depth" as realized.** Two distinct failure regimes, one mechanism each:
>
> 1. **Amplitude-gating (at the impose amplitude).** At the m_ec²-calibrated (2,3) impose
>    (peak `|ω|≈1.5`, `A²_μ≈0.23`), the wall **never engages** (`Γ_min=−0.011 ≈ 0`, a matched
>    bulk). The imposed pair **under-drives its own saturation front**, so native / wall_only /
>    wall_sector are near-identical (all disperse: `loc_min_post` 0.231 / 0.203 / 0.194).
> 2. **Parametric pumping (when forced to engage).** Scaled up 4× so the wall *does* form a hard
>    short (`Γ_min=−0.994`), the moving clamp **parametric-pumps** in the coupled+driven engine
>    (`peak|ω|→4.8×10³` wall_only, `→1.0×10⁵` wall_sector; energy `→4.9×10⁴` / `1.7×10⁷×`). The
>    (II) §6 hard-wall instability is **NOT tamed** by the ported implicit reactance-rotation
>    integrator in this configuration. No **stable** confinement of the imposed pair was reached
>    at any amplitude.

**This is honest closure (Rule 11), not a rescue.** The pre-registered question — *does the
imposed pair persist past step ~11 under the (II) reflective confinement?* — fails decisively,
and a single coherent mechanism (the wall is amplitude-gated below saturation and parametric-
pumps above it) explains every config. The branch closes; the two mechanisms are named.

**What this is NOT:** it is **not** evidence that the (II) wall is wrong (the (II) result stands:
the wall confines a *high-amplitude helical photon* in the *standalone* engine). It is evidence
that the **m_ec²-calibrated (2,3) impose**, in the **coupled+driven** engine, sits in neither
the wall's working regime: too weak to form it, and unstable when forced to.

---

## §1 What was built (minimal delta, KEEP-BOTH, default OFF)

The (II) `use_impedance_boundary` mechanism lived only on the **standalone** `CosseratField3D`
(`cos.step()`). The coupled engine `CoupledK4Cosserat` runs its **own** Cosserat sub-step
(`_cosserat_sub_step`) and never calls `cos.step()`, so the (II) wall was **unreachable** in the
coupled K4⊗Cosserat engine where the Option-D impose runs. Three changes (the WIP `git stash`
reference port + one new variable):

1. **Coupled port** — `CoupledK4Cosserat` gains `use_impedance_boundary`: when ON, the Cosserat
   sub-step runs the **linear-elastic bulk** (`k_op10=k_refl=k_hopf=0`) + the **Op3 Γ=−1 node-
   clamp** at the moving μ-side saturation front, integrated by the **exact reactance-pair
   rotation** (`_rotate_clamp`, CP6 energy-conserving) at a CFL-safe sub-dt (`impedance_implicit`,
   `impedance_cfl_safety=0.4`). The K4 V-sector reflects via the existing `z_local→0` Op3 bond
   short. (Ported from the WIP stash; the implicit integrator is the (II) §6 anti-pumping fix.)
2. **The one new variable — `couple_v_sector`** (the §9 sector coupling). The shared front
   `_update_saturation_kernels(u, ω, V_sq)` is fed the **live K4 `V_sq`** when `True` (the
   Cosserat-ω "2" wall is co-determined by the V-sector "3"=U(1) fibre) and **`V_sq=0`** when
   `False` (the decoupled (II)-standalone wall). This is the isolation knob for the
   which-fix-mattered attribution.
3. **Plumbing** — `EngineConfig` exposes both flags; default OFF → the energy-saturation /
   self-term path is **byte-identical** (`make verify` green; 227 cosserat/coupling/engine/gate
   tests pass unchanged).

`substrate-native-check`: **CP1** — the wall is a reactive reflection (node-clamp) inside the
velocity-Verlet propagation, not the gradient-descent settle or an energy multiplier. **CP2** —
the shared `(S_μ,S_ε)` front couples both sectors (`couple_v_sector`). **CP4** — the "2" is read
in Cosserat-ω real-space, the "3" in K4 `(V_inc,Φ_link)`, never conflated. **CP6** — the
`(ω=C-state, ω̇=L-state)` reactance pair is rotated together (and recorded every step). **CP8** —
the bulk is the clean linear wave, so any confinement is attributable to the wall alone.

---

## §2 PRIMARY — the exact phase5 (2,3) impose: the wall NEVER engages

The (2,3) torus-knot pair is hand-placed at the central A→B bond (seed `|ω|_A=0.1244`,
**byte-identical to the MODE-III prior** `omega_seed`), the gate is pre-marked nucleated (so it
never re-fires — the pair is *imposed*, Option-D), the head-on `AutoresonantCWSource` collision
drives at `0.5·V_SNAP`, then drive-off + free evolution to ≥10 Compton periods. `N=24, pml=4`.

Two adjudication axes are reported (KEEP-BOTH discriminator discipline): the **legacy fixed-site
`|ω|_A/B`** (apples-to-apples with the MODE-III prior) and a **new position-independent
localization** (density-peak, PML-excluded — the honest "held *anywhere*" axis, since the
fixed-site metric cannot tell a pair that *moved off the bond* from one that *dissolved*).

| config (scale 1.0) | `Γ_min` (wall) | `loc` seed→end | `loc_min_post` | `c_cos`_end | `peak|ω|` | `E_end/seed` | bounded |
|---|---|---|---|---|---|---|---|
| **native** (MODE-III control) | — (no wall) | 0.492 → 0.351 | **0.231** | 3 | 1.50 | 0.22 | ✅ |
| **wall_only** (V_sq=0) | **−0.011** | 0.492 → 0.320 | 0.203 | 1 | 1.50 | 0.46 | ✅ |
| **wall_sector** (live V_sq) | **−0.011** | 0.492 → 0.310 | 0.194 | 2 | 1.50 | 0.46 | ✅ |

**Reading.** `Γ_min=−0.011 ≈ 0` for *both* wall configs across the whole run: the moving Γ=−1
short **never forms**. At the impose amplitude the curvature gives `A²_μ=κ²/ω_yield²≈0.23`
(`ω_yield=π`), so `S_μ≈0.88`, `Z_eff≈0.94`, `Γ≈−0.03` — a *matched bulk*, not a reflective wall.
With the wall absent, all three confinements are the **same dispersive bulk**: the imposed pair
spreads and is PML-absorbed (`E_end/seed`≈0.2–0.5), `loc` decaying gently `0.49→0.31–0.35`. The
legacy fixed-site `|ω|_A` "dissolves @step 4" identically in all three — but that is mostly the
knot **shifting off the exact A-site**: the localization shows ~65–70 % of the structure persists
to drive-end before slowly dispersing. The `(2,3)` **winding is topologically retained** in native
(`c_cos`_end=3) even as the amplitude bleeds away. **The wall-vs-native swap changes nothing,
because the wall is sub-threshold.**

K4 V-sector "3" (read in its own coordinate, CP4): the drive energizes `max_V_sq→0.249`
(`V≈0.5·V_SNAP`, identical across configs — the K4 step is impedance-flag-independent), but the
bond flux `max|Φ_link|_bond→0.036` stays tiny: the U(1) fibre does not assemble at the bond.

---

## §3 DIAGNOSTIC (scale-up) — when forced to engage, the hard wall PARAMETRIC-PUMPS

To separate *"the wall failed"* from *"the wall never formed,"* the seed is scaled
(`seed_amp_scale=4`, peak `|ω|=6.0`) until the front saturates. Calibration of the engagement:

| `seed_amp_scale` | peak `|ω|` | `Γ_min` | regime |
|---|---|---|---|
| 1.0 (the impose) | 1.50 | −0.011 | matched — **wall never forms** |
| 2.0 | 3.00 | −0.050 | soft |
| 3.0 | 4.50 | −0.170 | soft-moderate |
| **4.0** | 6.00 | **−0.994** | **hard Γ=−1 short forms** |

At `scale=4` the wall engages hard (`Γ_min=−0.994`). The result, with the drive on:

| config (scale 4.0, drive) | `Γ_min` | `loc` seed→end | `peak|ω|` | `E_end/seed` | bounded |
|---|---|---|---|---|---|
| **native** | — | 0.492 → 0.385 | 6.00 | 0.20 | ✅ disperses (PML-absorbed) |
| **wall_only** | −0.994 (engaged) | 0.492 → 0.403 | **4 784** | **4.9×10⁴** | ❌ **PUMPS** |
| **wall_sector** | −0.994 (engaged) | 0.492 → 0.181 | **101 950** | **1.7×10⁷** | ❌ **PUMPS HARDER** |

**Reading.** The hard moving Γ=−1 clamp **injects energy** (`peak|ω|` and total energy explode
10³–10⁷×) — the §6 parametric-pumping instability the (II) result flagged as needing an
implicit integrator. The ported `impedance_implicit` reactance-rotation (validated for the
*standalone, undriven* photon at `Emax/E₀≈2.6`) does **NOT** bound the **coupled+driven** hard
wall here. **Critical metric caveat:** the blowup concentrates energy into a near-single-cell UV
spike, which reads as *high* `loc` (0.403 for wall_only) — a **confinement imposter**. The
adjudication therefore **gates every "helps"/"persists" claim on `energy_bounded`**; the pumped
configs are excluded. (Without that gate the run *mislabels* itself MODE II — corrected here.)

`sector-coupling makes it WORSE`: `wall_sector` pumps to `1.0×10⁵` vs `wall_only` `4.8×10³` —
feeding the live K4 `V_sq` into the moving front **amplifies** the parametric drive (the V-sector
modulation of `Ω₀(r)` resonates with the ω oscillation). The §9 "3↔2" coupling does not stabilize
the imposed pair; at the engaging amplitude it **destabilizes** it further.

---
