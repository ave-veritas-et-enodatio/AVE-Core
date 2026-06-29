# RESULT — Stage-1 GR-Extension: the Saturating-Modulus Correction on the Linear GR Core

**Date:** 2026-06-29 · **Lane:** implementer · **Branch:** `analysis/grqed-stage1-gr-extension`
**Status:** Stage-1 increment landed (code + two-test doctrine + clip-independence gate; both test lanes green)
**Scope:** A saturating-modulus correction ON the inherited GR (elastic-Poisson) solver — the FIRST
increment of the GR/QED-extension engine. The inherited linear core is the weak-field limit and is NOT
re-derived here.

---

## 0 · One-paragraph summary

The vacuum is a real saturable elastic medium. The inherited linear core — elastic-Poisson
$-(c^4/7G)\nabla^2\varepsilon_{11}=T_{00}\Rightarrow\varepsilon_{11}=7GM/c^2r$, $n=1+(2/7)\varepsilon_{11}$
— is the **weak-field limit**. Stage-1 adds a **saturating modulus** to the elliptic operator,
$-\nabla\!\cdot[(c^4/7G)\,D(A)\,\nabla\varepsilon_{11}]=T_{00}$ with $A=\varepsilon_{11}/\varepsilon_{yield}$
($\varepsilon_{yield}=1$), $D=1/S(A)$, and the **one** canonical Op14 kernel $S(A)=(1-A^2)^{1/2}$ (REUSED,
not minted). The bulk channel **stiffens** ($D=1/S\to\infty$ at $A=1$, halting the collapse); the shear
channel **softens** ($c_{shear}=c_0\sqrt S\to0$, a derived projection); EM stays **matched**
(`refractive_index()` untouched, spectator). Both two-test-doctrine legs pass — recover-the-known
(consistency) at $r\gg r_{sat}$ and activate-at-the-extreme (manifestation) at $r_{sat}=3.5\,r_s$ — and the
**load-bearing clip-independence gate PASSES**: the yield-shell radius and the integrated source $M_{eff}$
are bit-identical across $S_{min}\in[10^{-4},10^{-2}]$, so the yield-physics (not the numerical clamp) set
the wall.

**Honest framing (do NOT overclaim):** the point singularity is **replaced by a strain-saturated SHELL** at
$r_{sat}=3.5\,r_s$; the density **still diverges** there ($\rho_{eff}=\rho_0/S^3\to\infty$). True removal
needs the yield→rupture→genesis physics (a separate frontier). The strain-cap here is a numerical clip, NOT
modeled yield-physics. This is **RELOCATION** of the singularity to a shell, not regularization / removal of
the infinity.

---

## 1 · Spec (what was built)

| Element | Spec | Where |
|---|---|---|
| Inherited linear core (NOT re-derived) | $-(c^4/7G)\nabla^2\varepsilon_{11}=T_{00}\Rightarrow\varepsilon_{11}=7GM/c^2r$; $n=1+(2/7)\varepsilon_{11}$ | `gw_propagation.refractive_index()` (UNCHANGED); Op19 `universal_refractive_index` |
| The correction | $-\nabla\!\cdot[(c^4/7G)\,D(A)\,\nabla\varepsilon_{11}]=T_{00}$, $A=\varepsilon_{11}/\varepsilon_{yield}$ ($\varepsilon_{yield}=1$) | `relax_finite_core_strain()` |
| The ONE kernel (F1) | $S(A)=(1-A^2)^{1/2}$ — REUSED, not minted; $c_{shear}=c_0\sqrt S=c_0(1-A^2)^{1/4}$ is a DERIVED $\sqrt S$ projection (NOT a 2nd kernel) | `graded_vacuum_network.saturation_kernel` / `stiffness_profile` (exponent=0.5) |
| Per-channel sign (INVARIANT-S2) | BULK **stiffens** $D=1/S$; SHEAR **softens** $c_{shear}=c_0\sqrt S\to0$; EM **matched** $Z_{EM}=Z_0,\Gamma_{EM}=0$ | `bulk_stiffness_D()`; `shear_wave_speed()` (pre-existing); `refractive_index()` (untouched) |
| Saturation radius | $r_{sat}=3.5\,r_s=7GM/c^2=(2/\nu_{vac})\,r_s$ | `saturation_radius()` (pre-existing, reused) |
| Finite-core demo | static **elliptic relaxation** on the native tetrahedral stencil; **distributed** $T_{00}$ (NOT the inherited δ-source); NOT a damped time-march | `relax_finite_core_strain()` + `distributed_source_T00()` |
| Two-test doctrine | recover-the-known (consistency) + activate-at-the-extreme (manifestation) | §4, §5 |
| ★ Load-bearing gate | $M_{eff}$ and the shell radius must be CLIP / $S_{min}$-independent (sweep $[10^{-4},10^{-2}]$) | `clip_independence_gate()`; §6 |

## 2 · Substrate-native-check (walked before numerical code)

- **K4 / stencil.** The elliptic operator is the divergence-form $\mathrm{Div}\cdot\mathrm{diag}(D)\cdot\mathrm{Grad}$
  on the **diamond-K4 tetrahedral** stencil (`TETRA_OFFSETS`, 4 diagonals) — the SAME factored sparse build as
  `graded_vacuum_network._build_sparse_stiffness`. The Cartesian 7-pt Laplacian is **never called**.
- **Cosserat sector ownership.** $\varepsilon_{11}$ is relaxed on the **radial/shear** channel ONLY. The BULK
  modulus $D=1/S$ stiffens; the SHEAR projection $c_{shear}=c_0\sqrt S$ softens (opposite signs — NEVER a
  uniform $C\cdot S$). The EM channel (A1-transverse, `refractive_index()`) is a spectator and is untouched.
- **Op14.** The confinement / saturation kernel is the **one** canonical $S(A)=(1-A^2)^{1/2}$ (exponent=0.5),
  reused from `graded_vacuum_network`. No second kernel; $(1-A^2)^{1/4}$ is never used **as** the kernel.
- **phase-space vs real-space.** Stage-1's claim is in **real-space** (strain magnitude vs radius); it is
  measured in real-space (the relaxed $\varepsilon_{11}(r)$ field). No phase-space $\phi^2$ claim is at issue —
  coordinate-discipline clean (A46).
- **consistency-vs-emergence (A47).** Test 1 = **CONSISTENCY** (reproduce the inherited linear core). Test 2 =
  **MANIFESTATION** (the kernel's saturation extreme produces a shell). No CODATA / α inputs; **α-CLEAN** (a
  source-level guard test asserts no `ALPHA` / `Q_TANK` in the Stage-1 functions).

## 3 · Code delivered (file:line)

All on the host `src/ave/gravity/gw_propagation.py` (a new STAGE-1 section after the shear channel block):

| Function | Role |
|---|---|
| `saturated_radial_strain(r, r_s, *, S_min)` | closed-form saturated strain $\min(r_{sat}/r,1)$ on the radial channel; calls the **canonical** `saturation_kernel` for the cap |
| `bulk_stiffness_D(A, *, S_min)` | BULK elliptic coefficient $D=1/S(A)$ via the canonical `stiffness_profile` (the channel that **stiffens**) |
| `distributed_source_T00(N, *, sigma, amplitude)` | a smooth Gaussian $T_{00}$ blob (REPLACES the inherited δ-source) |
| `relax_finite_core_strain(N, ...)` | static elliptic relaxation: sparse Picard + direct `spsolve` of $-\nabla\!\cdot[D\nabla\varepsilon_{11}]=T_{00}$ on the native tetrahedral stencil; observable-convergence on the shell radius |
| `clip_independence_gate(s_min_values, ...)` | the ★ load-bearing gate: sweeps $S_{min}$, asserts shell radius + $M_{eff}$ invariant |

`refractive_index()` (the EM channel) is **UNCHANGED** — verified by an EM-spectator guard test. Tests live in
`src/tests/test_grqed_stage1_gr_extension.py`; the heavy relaxation/gate tests are routed to the `engine_sim`
lane via `src/tests/conftest.py` (`_ENGINE_SIM_TESTS`, #411 OOM-class discipline).

## 4 · Test 1 — RECOVER-THE-KNOWN (consistency-class)

## 5 · Test 2 — ACTIVATE-AT-THE-EXTREME (manifestation-class)

## 6 · ★ LOAD-BEARING GATE — clip-independence verdict

## 7 · Honesty — the singularity is RELOCATED, not removed

## 8 · How this integrates: GR's linear core + the saturating-modulus shell

## 9 · Honest flags + spec deviations
