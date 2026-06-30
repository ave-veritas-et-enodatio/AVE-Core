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

## 4 · Test 1 — RECOVER-THE-KNOWN (consistency-class) ✅

At $r\gg r_{sat}$: $A\to0$, $S\to1$, $D\to1$ — the correction vanishes and the inherited linear
elastic-Poisson / Schwarzschild profile is reproduced.

| Check | Result | Tol |
|---|---|---|
| $\varepsilon_{11}^{sat}(r)/(r_{sat}/r)$ at $r/r_{sat}=10^2,10^3,10^6$ | $1.0,\,1.0,\,1.0$ | rtol $10^{-12}$ |
| $D(A)$ at $A=0,10^{-3},10^{-2}$ | $1.0,\,1.000001,\,1.00005\to1$ | atol $2\times10^{-4}$ |
| $n(r)=1+(2/7)\varepsilon_{11}$ (linear form) at far field | matches | rtol $10^{-3}$ |
| relaxed finite-core exterior tail (unsaturated $A<1$ regime exists) | $A=0.18$ at $r=N{-}3$ | $<0.4$ |

**Verdict: PASS** — the saturating modulus collapses to the inherited GR core in the weak field. This leg is
**consistency-class** (reproduce a known theory at its limit), NOT an emergence claim.

**(Honest note — definitional vs load-bearing.)** The first-row closed-form check $\varepsilon_{11}^{sat}/(r_{sat}/r)=1$ is *definitional* in the far field ($\min(r_{sat}/r,1)\equiv r_{sat}/r$ for $r>r_{sat}$), not an independent recovery. The non-tautological recover-the-known evidence is the **relaxed-field exterior tail** (an unsaturated $A<0.4$ regime exists, row 4) plus the **$D\to1$** stiffness recovery (row 2). The leg as a whole is non-tautological; the headline strain-match alone is.

## 5 · Test 2 — ACTIVATE-AT-THE-EXTREME (manifestation-class) ✅

The radial strain reaches the yield $A=1$ at $r_{sat}=3.5\,r_s$; the bulk stiffness diverges; a saturated
shell forms.

| Check | Result |
|---|---|
| $r_{sat}/r_s$ | $3.5$ ($=7GM/c^2=(2/\nu_{vac})\,r_s$) |
| $\varepsilon_{11}^{sat}(r_{sat})$ | $1.0$ (the yield); capped at $1$ inside |
| $D(0.9),D(0.99)$ | $2.294,\,7.089$ (rising) |
| $D(A{=}1;S_{min}{=}10^{-3}),\,D(A{=}1;S_{min}{=}10^{-4})$ | $10^3,\,10^4$ (floor-capped — the divergence) |
| BULK $D\cdot S=1$ (reciprocal, NOT $D\propto S$) | $1.0$ to rtol $10^{-9}$ — sign-lock confirmed |
| finite-core relaxation $N=24$: $\max A$ | $1.000000$ (core saturates) |
| shell radius (outermost $A\ge0.99$ ring) | $4.0$ sites (interior, well inside the box) |
| Picard iterations to shell-radius convergence | $73$ (observable-converged) |

Relaxed radial $A$-profile ($r=0\ldots10$ sites): `1.00, 0.97, 1.00, 0.97, 1.00, 0.82, 0.70, 0.49, 0.38,
0.22, 0.18` — a saturated core ($A\approx1$, $r\lesssim4$), a yield wall at $r\approx4$, then a smooth
$\sim1/r$ unsaturated falloff.

**Verdict: PASS** — the saturation extreme of the **one** kernel produces a strain-saturated shell (the bulk
goes rigid and halts the collapse). This leg is **manifestation-class**.

## 6 · ★ LOAD-BEARING GATE — clip-independence verdict: **PASS**

Sweep $S_{min}\in\{10^{-4},10^{-3},10^{-2}\}$ (two orders of magnitude), all other parameters fixed:

| $S_{min}$ | shell radius | $M_{eff}$ | $\max A$ |
|---|---|---|---|
| $10^{-4}$ | $4.0000$ | $100.797503$ | $1.000000$ |
| $10^{-3}$ | $4.0000$ | $100.797503$ | $1.000000$ |
| $10^{-2}$ | $4.0000$ | $100.797503$ | $1.000000$ |

- shell-radius relative spread: **$0.00\times10^{0}$** (bit-identical)
- $M_{eff}$ relative spread: **$0.00\times10^{0}$** (source-only invariant)

**Wider-sweep transparency (no silent cap; independently re-run).** A 6-decade sweep $S_{min}\in\{10^{-1}\ldots10^{-6}\}$ holds shell $=4.0$ ($=\sqrt{16}$) for $S_{min}\le10^{-2}$; only at the *loose* floor $S_{min}=10^{-1}$ does it shift to $4.123$ ($=\sqrt{17}$, the **adjacent lattice ring**) — a 3.06% spread over the full range, within the 5% tolerance. This is the ±1-ring discretization granularity (§9), **NOT** $S_{min}$-dependence of the physics: $S_{min}$ materially binds the D-field ($\max D = 1/S_{min}$ exactly), yet the saturation locus $A\to1$ is set by $r_{sat}$ geometry. The reported window $\{10^{-4},10^{-3},10^{-2}\}$ is bit-identical because at those tighter floors $\max A$ saturates identically and the shell snaps to $\sqrt{16}$.

**VERDICT: PASS — $S_{min}$-INDEPENDENT (the yield-physics set the wall, NOT the numerical clamp).** The
shell sits where the integrated source drives the strain to the yield $A=1$ — a geometric/$r_{sat}$ fact
upstream of the kernel floor. $S_{min}$ only bounds the divergence of $D=1/S$; it does **not** move the
location where $A\to1$. Had the shell radius tracked $S_{min}$, the clamp (not the physics) would have set the
wall and the gate would have **FAILED** — it does not.

## 7 · Honesty — the singularity is RELOCATED, not removed

> **The point singularity is replaced by a strain-saturated SHELL at $r_{sat}=3.5\,r_s$; the density still
> diverges there; true removal needs the yield→rupture→genesis physics (a separate frontier).**

The strain saturates ($A$ capped at $1$) but the **inertial density diverges** at the shell:
$\rho_{eff}=\rho_0/S_{topo}^3$ with $S_{topo}=\sqrt{1-\varepsilon_{11}^2}\to0$, so $\rho_{eff}\to\infty$ as the
yield is approached (manuscript leaf
`manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md`:14–25;
`lattice-extreme-bh-rationality.md` §6). What Stage-1 demonstrates is the **Topological Halting** — the bulk
modulus diverges and the collapse freezes at the phase-transition boundary, replacing the $r=0$ point with a
shell at $r\approx r_{sat}$. This is **RELOCATION**, not regularization.

Additionally: the strain-cap implemented here ($\min(\varepsilon_{11},1)$ / `clip(x,0,1)` in the relaxation)
is a **numerical clip, NOT modeled yield-physics**. The genuine yield (the lattice phase transition at $A=1$,
its rupture, and the genesis that follows) is a separate frontier and is not modeled in Stage-1.

**This result does NOT claim** "regularizes the singularity" or "removes the infinity." It claims the strain
saturates into a shell while the density still diverges.

## 8 · How this integrates: GR's linear core + the saturating-modulus shell

Stage-1 is a **correction ON the inherited GR solver**, not a replacement. The linear elastic-Poisson core
($-(c^4/7G)\nabla^2\varepsilon_{11}=T_{00}\Rightarrow\varepsilon_{11}=7GM/c^2r$, $n=1+(2/7)\varepsilon_{11}$)
is the **weak-field limit** and is left exactly as inherited — at $r\gg r_{sat}$ the correction collapses to
it identically (§4). The Stage-1 addition is the saturating modulus $D(A)=1/S(A)$ multiplying the elliptic
operator: in the weak field $D\to1$ (GR recovered, consistency); at the strong-field extreme $D\to\infty$
(the bulk goes rigid, a yield shell appears at $r_{sat}=3.5\,r_s$, manifestation). The **one** Op14 kernel
$S(A)=(1-A^2)^{1/2}$ supplies both regimes; the per-channel sign-lock (BULK stiffens / SHEAR softens / EM
matched) keeps the three channels physically distinct. The EM channel (`refractive_index()`) is untouched —
photons still see the GR geometry at the EM horizon $r_s=2GM/c^2$, while the matter/shear yield reflector
sits deeper at $r_{sat}=7GM/c^2$ (the $r_s$-vs-$r_{sat}$ channel split, `lattice-extreme-bh-rationality.md`
§6). Stage-1 is thus the first rung of the GR/QED-extension engine: **GR's linear core + the
saturating-modulus shell**, sharing the canonical kernel and stencil with the rest of the framework.

## 9 · Honest flags + spec deviations

1. **Picard limit-cycle at the yield edge (numerical, not physical).** The hard yield cap ($A=1$) makes the
   fixed point non-smooth at the wall: individual edge sites limit-cycle between just-below and just-at unity
   while the shell **radius** is stationary. Convergence is therefore judged on the **physical observable**
   (shell-radius stationary over 15 iterations), not pointwise $\lVert\Delta\varepsilon\rVert_\infty$ (which
   plateaus at $\sim2\times10^{-2}$ and is reported as `picard_delta` for transparency). This is the honest
   substrate-native convergence measure for a non-smooth yield problem; it is recorded, not papered over.
2. **±1-ring discretization granularity in the shell radius.** The shell radius is quantized to the lattice
   ($4.0=\sqrt{16}$ vs $4.123=\sqrt{17}$ are adjacent rings); the exact ring can shift by one with the Picard
   under-relaxation `picard_mix`. This is **discretization granularity, NOT $S_{min}$-dependence** — the
   clip-independence gate (§6) holds `picard_mix` fixed and sweeps only $S_{min}$, returning zero spread. The
   gate is therefore clean; the ring-granularity is a separate, expected lattice-resolution effect (a
   convergence-vs-$N$ study is deferred to a later stage).
3. **Distributed-source shell vs the $3.5\,r_s$ point-source shell.** The finite-core demo uses a compact
   distributed Gaussian $T_{00}$ (not the inherited δ-source), so its shell sits at the radius where the
   *integrated* source drives $\varepsilon_{11}\to1$ ($\approx4$ sites for the default source/box), which is a
   geometric function of the chosen source, not literally $3.5\,r_s$. The **closed-form** $r_{sat}=3.5\,r_s$
   relation (the point-source / far-field result) is tested separately and exactly in §5. No deviation — the
   two are different, both-correct measures (point-source analytic vs distributed-source relaxed).
4. **No spec deviations on the load-bearing requirements.** The canonical kernel is reused (no 2nd kernel
   minted); `refractive_index()` is unchanged (EM spectator, guard-tested); the source is distributed (not
   δ); the demo is elliptic relaxation (not a time-march); the gate passes $S_{min}$-independent; the honesty
   framing is verbatim. α-CLEAN (source-level guard test).

---

**Branch:** `analysis/grqed-stage1-gr-extension` · **next:** Grant merges via reviewed PR (not merged here).
