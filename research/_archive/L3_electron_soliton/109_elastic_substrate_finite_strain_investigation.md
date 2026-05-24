# 109 — Boundary-Envelope Reformulation of the L3-Electron Wall

**Date:** 2026-05-14
**Branch:** `research/l3-electron-soliton`
**Author:** Claude (implementer + auditor cross-lane); Grant directive 2026-05-14 morning + evening
**Status:**
- **2026-05-14 morning:** Pre-investigation plan opened on Grant's "elastic stretching" question. Phase 0 engine audit + Phase 1 corpus-grep done. Three readings (A/B/C, with C splitting into C1/C2) framed. Q1-Q3 axiom-author questions surfaced.
- **2026-05-14 evening:** Grant confirmation + sharpening. The boundary-envelope reframing (§13 below) supersedes the dual C1/C2 framing. **Reading C2 is canonical; Reading C1 is deferred as likely unnecessary.** Q1-Q3 are partially resolved by the BH-electron parallel (§13.2). Pre-registered load-bearing test (§14) is the path forward.
**Companions:**
- [doc 92](92_round_11_vi_v10_finer_sampling_structural.md) — Nyquist wall (load-bearing)
- [doc 101 §9-§10](101_round_12_unknot_cosserat_entry.md) — three-layer canonical
- [doc 103](103_substrate_perspective_electron.md) — substrate-perspective view of canonical electron
- [doc 108](108_lattice_fundamentals_emergence_plan.md) — emergence vs consistency reframe
- [Q-G19α Route B closure](../../../AVE-QED/docs/analysis/2026-05-13_Q-G19alpha_route_B_petermann_match.md) — 50 ppm match without lattice-resolved eigenmode
- [Bench K4-TLM validation](../../../AVE-Bench-VacuumMirror/scripts/k4tlm_bench_validation.py) — IM3 slope 2.956 with op3_bond_reflection=True + V_SNAP=1.0
- [Q-G47 buckling derivation](../../../AVE-QED/docs/analysis/2026-05-13_Q-G47_buckling_derivation_setup.md) — r_d = L_spring/d as cosmological-genesis parameter
- [Q-G42 prereg](../../../AVE-QED/docs/analysis/2026-05-13_Q-G42_v_yield_apparatus_scaling_prereg.md) — picture-first prereg under Step 1.5 discipline

---

## §0 Summary

Grant directive 2026-05-14 (post-procurement, post-K4-TLM bench validation, post-Q-G19α Route B closure):

> *"We've defined the center spacing from node to node, but using our trampoline and spring analogy it's really the springs that set that distance right? So the capacitor or the volumetric expansion or contraction. Have we defined the elastic dynamic or inductive stretching of the trampoline material itself? Or is that even a reasonable thing to ask that we could be possibly missing now?"*

**The physical picture:** the K4 substrate is a lattice of LC bonds (springs). Currently the engine treats the inter-node spacing `dx ≡ ℓ_node` as a fixed scalar and modulates only the bond **impedance** Z_eff = Z_0/√S via the saturation kernel S(A) = √(1−A²) and the Op3 per-bond gamma reflection. **The springs change stiffness, but their physical length never changes.** The Cosserat `u` displacement field exists and feeds `_compute_strain = grad_u / dx` for energy/coupling purposes, but it does not deform the K4 grid geometry. Port directions and `dx` are frozen at `__init__`.

**This is a small-strain Eulerian approximation of what AVE physically claims is a finite-strain Lagrangian substrate.** The corpus describes gravity as `n(r) = 1 + 2GM/(rc²)` substrate-strain at Vol 3 Ch 2:35; mass as "inductive deficit in adjacent vacuum" at :45; the Schwarzschild radius as "where local strain reaches Axiom 4 saturation S → 0" at :43. The canonical picture is **compressed substrate around solitons** — but the engine implements compressed *impedance* on rigid grid geometry.

**The wall question:** doc 92 (2026-04-29) found that the corpus electron's predicted Beltrami eigenmode at k ≈ 6.36/ℓ_node is sub-lattice on K4 at vacuum-ℓ_node spacing (Nyquist limit k_max = 0.577/ℓ_node). Round 13 + 8 cumulative Mode III tests confirm this empirically (doc 104). Doc 108 pivots from "emergence" to "consistency" framing as the wall response. **What if the wall is not structural but is the small-strain linearization breaking down?** If the substrate is genuinely elastic and locally compresses around solitons, the local Nyquist limit rises inside the compressed pocket, and the corpus eigenmode becomes lattice-hostable in that pocket.

**The investigation plan tests three things:**
1. Whether the wall dissolves on a uniformly finer grid (cheap probe of Reading B vs C; ~3 hr)
2. Whether a planted static compression region hosts the corpus eigenmode (direct probe of Reading C; ~4 hr)
3. Whether the corpus electron is better understood as a single-cell phase-space soliton (refined-C interpretation; ~4 hr)

Decision gates land each phase before committing to the major engine refactor that adding `dx_local` per bond would require (~1-2 weeks scope).

---

## §1 Step 1.5 picture-first (5 mechanical bullets, no math)

Per ave-prereg Step 1.5 discipline (`~/.claude/skills/ave-prereg/SKILL.md`):

1. **What is saturating, where, in what geometry?** Inside an electron soliton, the substrate is at A → 1 (Axiom 4 saturation). At Schwarzschild-equivalent compression, the bonds physically run out of accommodation length. The electron's "horn torus" at radius `ℓ_node/(2π) ≈ 0.16·ℓ_node` is the canonical core size (doc 101 §10). Whether this represents (a) compressed bond spacing inside the soliton or (b) a sub-cell phase-space structure within a single ℓ_node cell is the load-bearing ambiguity.

2. **Which Γ=−1 boundary, at which scale?** App F multi-scale Machian network: every soliton scale (electron, nucleus, atom, helio, BH, cosmic) has a local Γ=−1 boundary. The electron's boundary is the unknot wall at horn-torus radius. The question is: is each Γ=−1 boundary a region of *compressed substrate* (per-cell `dx` smaller than vacuum), or a region of *modified impedance* (per-cell Z_eff larger, `dx` unchanged)?

3. **Soliton population + topology.** Per doc 101 three-layer canonical: Layer 1 real-space unknot 0₁ + Layer 2 SU(2) double-cover bundle + Layer 3 phase-space (2,3) winding on Clifford torus in (V_inc, V_ref) at each node. The Round-13 Mode III result tested Layer 3 phase-space topology *on a fixed-geometry lattice*. If the soliton physically requires compressed substrate (Layer 1 sub-cell footprint), the fixed-geometry engine cannot host it regardless of Layer 3 phase-space IC.

4. **Scaling.** In the elastic picture: bond inductance `L_bond ∝ ℓ_per_bond`; bond capacitance `C_bond ∝ ε_per_bond × A_cross / ℓ_per_bond`. Under uniform compression by factor `λ < 1`: L scales as λ, C scales as 1/λ, Z = √(L/C) scales as λ, v = 1/√(LC) stays at c. Under non-uniform compression (the soliton scenario): impedance varies along the bond → Op3 reflections → standing-wave bound state. Local Nyquist k_max scales as 1/dx_local — inverse of compression factor. 11× compression → k_max rises from 0.577/ℓ_vacuum to 6.36/ℓ_vacuum, matching the corpus electron's predicted eigenmode.

5. **Discriminating onset event.** PASS (Reading C confirmed): in a planted-compression-region run, the corpus eigenmode hosts inside the compressed region with PCA aspect ≈ φ² (signature cubic anisotropy) but does NOT host outside. FAIL (Reading C falsified): Mode III persists even inside the compressed region, meaning the wall is something deeper than Nyquist. INCONCLUSIVE: numerical pathologies at the compression-region boundary prevent clean adjudication.

---

## §2 Phase 0 engine audit (executed 2026-05-14, results below)

**Goal:** verify whether bond-length / lattice-spacing is a state variable anywhere in the K4-TLM + Cosserat coupled engine.

**Method:** grep `src/ave/` for `dx_local`, `dx_per_bond`, `spacing_field`, `bond_length_field`, `rest_length`, `deformed`, `lagrangian`, `finite_strain`, `eulerian`. Read `K4Lattice3D.__init__`, `CosseratField3D.__init__`, and `k4_cosserat_coupling._compute_strain`.

**Findings (all file:line specific):**

| Engine location | Field | Type | Mutability |
|---|---|---|---|
| `src/ave/core/k4_tlm.py:132` | `self.dx = dx` | scalar float | set once at `__init__`, never reassigned |
| `src/ave/core/k4_tlm.py:144` | `self.dt = dx / (self.c * np.sqrt(2.0))` | scalar float | set once, never reassigned |
| `src/ave/core/k4_tlm.py:371-376` | `port_shifts` | constant integer tuples `(+1,+1,+1)` etc. | hardcoded in `_connect_all`, never rotated |
| `src/ave/topological/cosserat_field_3d.py:760` | `self.dx = float(dx)` | scalar float | set once at `__init__`, never reassigned |
| `src/ave/topological/cosserat_field_3d.py:144-160` | `_compute_strain(u, omega, dx) = grad_u / dx - cross` | linearized infinitesimal strain | grad_u divided by FIXED dx; no deformation gradient F = I + grad_u, no Green-Lagrange tensor |
| `src/ave/topological/k4_cosserat_coupling.py:84` | `_coupling_energy_total(u, omega, V_sq, V_SNAP, dx, ...)` | function | takes scalar dx as input; result is scalar energy used in V→ω coupling force |

**No `dx_local`, `dx_per_bond`, `spacing_field`, `bond_length_field`, `rest_length`, `deformed`, `lagrangian` exists anywhere in `src/ave/` excluding the `simulate_gw_impedance.py` static EMT solver (§3 below).** Confirmed via:
```
grep -rn "dx_local\|dx_per_bond\|spacing_field\|bond_length_field\|rest_length\|deformed_grid" src/ave/ 
# returns: zero hits
```

**Conclusion §2:** the K4-TLM + CosseratField3D coupled engine implements **infinitesimal-strain Eulerian dynamics on a rigid grid**. The Cosserat `u` field is a tracked observable (used in energy / coupling), not a geometric coordinate that deforms the lattice.

---

## §3 Phase 1 corpus-grep (executed 2026-05-14 via ave-corpus-grep agent)

**Cross-repo finding summary:**

### §3.1 Canonical bond-rest-length distinction EXISTS (and is load-bearing)

`AVE-QED/manuscript/vol_qed_replacement/chapters/11_tensioned_trampoline.tex:249-253`:

> *"the bonds of the K4 lattice have a rest length L_spring greater than the lattice site spacing d. When mounted between two nodes at spacing d, each bond is forced into a constrained configuration with L_spring > d."*

The ratio `r_d = L_spring/d` is the canonical parameter (Q-G47 buckling derivation). **But the corpus treats `r_d` as a cosmological-genesis frozen value, not a per-cell dynamic field.** Trampoline.tex:359-372 calls `r_d` "the substrate's rest configuration." Q-G47 setup doc :15 says the cooled-equilibrium hypothesis fixes `r_d*` at lattice crystallization via `∂U/∂r_d = 0` and freezes it.

### §3.2 Saturation kernel IS derived from bond-buckle exhaustion

trampoline.tex:483-502: the Pythagorean derivation of S(A) = √(1−A²) is **explicitly geometric exhaustion of buckled bond swing room**. trampoline.tex:556-562:

> *"A = 0 (rest, buckled) to A = 1 (fully straight at 90°). The remaining elastic capacity has the same functional form as S(A) = √(1−A²) via a Pythagorean relationship between vertical projection and applied strain."*

A = 1 means "bond fully straight" — no further deformation possible. **The bond's chord length stays = d throughout the entire kernel range.** What varies is the buckle angle, not the bond's effective endpoint-to-endpoint distance. This is consistent with the engine's fixed-`dx` implementation.

### §3.3 Gravity IS canonically substrate compression (operationally, refractive-index modulation)

`AVE-Core/manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex:35`:

> *"both constitutive parameters scale with the refractive index n(r) = 1 + 2GM/(rc²): ε_eff(r) = ε_0·n(r), μ_eff(r) = μ_0·n(r)"*

:45: *"When localised topological energy (mass) is present, it draws continuous phase-locked energy from the surrounding LC grid. This creates an inductive deficit in the adjacent vacuum, analogous to a density gradient in fluid dynamics."*

:43: *"the Schwarzschild radius r_s = 2GM/c² marks the point where the local strain reaches the Axiom 4 saturation limit (S → 0)."*

:55, :96: substrate carries gravity as *"acoustic shear-waves propagating through an elastic crystalline matrix"* and *"asymmetric strain footprint in the surrounding dielectric matrix."*

**The CANONICAL gravity-as-compression picture is implemented as ε_eff/μ_eff modulation on a fixed grid, not as actual per-cell `dx` deformation.** This is the structural ambiguity Grant's question surfaces.

### §3.4 ONE Lagrangian finite-strain spring solver exists, decoupled from dynamics

`AVE-Core/src/scripts/vol_4_engineering/simulate_gw_impedance.py:45-101` — explicit spring network with `rest_lengths` per edge, computes `stretch = current_lengths - rest_lengths` as proper Lagrangian finite strain. **Coupled to nothing.** It's a static EMT K/G + packing fraction measurement tool, decoupled from K4-TLM and CosseratField3D. The pipeline that ALREADY HAS finite-strain Lagrangian mechanics is **not the same pipeline** as the soliton dynamics engine.

### §3.5 Doc 108 Layer 3 explicitly identifies this as missing infrastructure

`research/L3_electron_soliton/108_lattice_fundamentals_emergence_plan.md:147-159`:

> *"apply controlled strain to the lattice (compression for K, shear for G). Measure stress response. [...] This is substantive new infrastructure — needs structural simulation (lattice statics under applied stress), not just dynamics."*

**The corpus already knows finite-strain dynamics is unbuilt.** Grant's question is not surfacing a new gap; it's making explicit a gap that doc 108 flagged for future work.

### §3.6 Electron horn torus is SUB-ℓ_node — refined Reading C2

doc 101 §10: electron unknot has `R_loop = r_tube = ℓ_node/(2π) ≈ 0.16·ℓ_node` per "Bounding Limit 1" + ropelength bound. **The entire electron geometry fits inside one K4 cell at canonical scale.** This is a critically different picture from "multi-cell compressed pocket":

- **Reading C1 (multi-cell):** the electron compresses N cells around itself; local `dx_local ≈ vacuum_dx / 11`; corpus eigenmode at k = 6.36/ℓ_vacuum lives in the compressed pocket
- **Reading C2 (single-cell phase-space):** the electron lives entirely within ONE K4 cell; the horn-torus geometry is sub-cell; "wavelength k = 6.36/ℓ_node" from doc 92 may be a spurious quantity from forcing a multi-cell eigenmode analysis on what is canonically a single-cell phase-space soliton

Both pictures are present in the corpus. The investigation needs to probe both.

### §3.7 Verdict from corpus-grep

**Per the (a)/(b)/(c)/(d) classification:**

| Topic | Status | Notes |
|---|---|---|
| Bond rest length ≠ lattice spacing | (a) closed — L_spring > d canonical at trampoline.tex:249-253 | But L_spring is *frozen at genesis* per Q-G47 |
| Electron = compressed substrate region | (b) partial — gravity-as-strain canonical at Vol 3 Ch 2:35-96 | But operationally implemented as ε_eff/μ_eff modulation, not per-cell dx |
| Cosserat finite-strain | (c) structural ingredient | u field exists; small-strain linearization in engine |
| Bond compression limit = Schwinger | (b) partial — A → 1 = bond fully straight | Buckle-angle exhaustion, not length exhaustion |
| App F local Γ=−1 boundaries | (c) structural ingredient | Picture supports compressed pocket but not formally per-cell |
| Engine per-cell dx variation | (d) green-field for K4-TLM, EXISTS in static EMT solver | simulate_gw_impedance.py has rest_lengths spring solver, decoupled from soliton dynamics |
| Horn torus = sub-cell electron geometry | (a) closed — doc 101 §10 + Bounding Limit 1 | Electron R = r = ℓ_node/(2π), fits inside one cell |
| Doc 108 acknowledgement of missing infrastructure | (a) closed — 108:147-159 explicitly says this is unbuilt | "substantive new infrastructure ... needs structural simulation" |

**Net position:** the physical picture Grant just articulated is **partially canonical (gravity-as-compression in Vol 3) + partially missing infrastructure (engine-level)**. It is NOT a new framework claim; it is **operationalizing a canonical picture that doc 108 has already flagged as unbuilt and that simulate_gw_impedance.py has partial machinery for**. This places Reading C at (b)→(c) on the prereg classification — not (d) green-field, but not (a) closed either. The framework already says matter compresses substrate; the engine doesn't model the compression as per-cell geometric deformation.

---

## §4 The dual Reading C: C1 (multi-cell) vs C2 (single-cell)

The corpus-grep surfaces that "Reading C" actually splits into two distinct physical pictures, both partially supported:

### §4.1 Reading C1 — Multi-cell compressed-pocket electron

**Picture:** the electron creates a region of locally-compressed substrate (lower `dx_local`) around its core. The corpus eigenmode at k = 6.36/ℓ_vacuum lives in this compressed pocket where local Nyquist limit is high enough.

**Engine work required:**
- Bond length as per-bond state variable: `dx_local[i, j, k, 4]` (4 ports per active site)
- Local timestep / local CFL: `dt_local[i, j, k] = dx_local / (c · √2)` — substep dynamics needed
- Cosserat `u` feeds back to `dx_local` via finite-strain mapping
- Port directions stay constant (tetrahedral); port LENGTHS vary
- ~1000-1500 LOC engine extension, ~2-3 weeks scope

**Maps to corpus:**
- Gravity-as-substrate-strain (Vol 3 Ch 2:35-96) ✓
- Schwarzschild radius as substrate-saturation boundary (Vol 3 Ch 2:43) ✓
- App F local Γ=−1 boundaries as compressed pockets ✓
- L_spring/d cosmological parameter ✗ (would require r_d to become a field, not a frozen genesis number — axiom-author question for Grant)

### §4.2 Reading C2 — Single-cell phase-space electron

**Picture:** the corpus electron is entirely contained within one K4 cell. The horn-torus geometry (R = r = ℓ_node/(2π)) is sub-cell. What lives in the cell is the (V_inc, V_ref) Clifford-torus phase-space structure with (2,3) trefoil winding. The "wavelength k = 6.36/ℓ_node" measurement in doc 92 is a *mis-framing* — it forces a multi-cell propagating-eigenmode analysis on what is canonically a single-cell phase-space soliton.

**Engine work required:**
- (V_inc, V_ref) at each K4 node already exists as 4-port real-valued arrays in `k4_tlm.py:153-155`
- The Clifford torus (V_inc, V_ref) coupling per node may already be implicit in the K4 scatter dynamics
- Test design: plant a (2,3) trefoil seed in (V_inc, V_ref) at a single K4 cell; run dynamics; verify trefoil persists (Layer 3 test) AND verify single-cell Beltrami eigenmode at horn-torus radius (Layer 1+2 test on Cosserat ω)
- Minimal engine extension; observable / diagnostic work primarily
- ~300-500 LOC of test scaffolding, ~3-5 days scope

**Maps to corpus:**
- Doc 101 three-layer canonical (unknot + SU(2) + (2,3) Clifford) ✓
- Bounding Limit 1: R_loop = r_tube = ℓ_node/(2π) ✓
- Route B Q-G19α closure (50 ppm to PDG) — used dark-wake × kernel-asymmetry on single-cell-scale phase dynamics, not multi-cell propagation ✓
- Doc 92 Nyquist analysis: ✗ may be measuring the wrong thing if electron is single-cell

### §4.3 Why both pictures matter

C1 and C2 are NOT mutually exclusive:
- C2 says: the electron's *primary structure* is single-cell phase-space
- C1 says: the electron's *secondary effect* (gravity) is multi-cell compression of surrounding substrate
- Both can be true: the electron is a single-cell phase-space soliton (C2) that simultaneously compresses the surrounding substrate (C1)
- doc 92's Nyquist wall: ambiguous because it could mean "C2 alone is wrong (we DO need multi-cell wavelength)" OR "C2 alone is right and doc 92 measured the wrong observable"

The investigation tests each picture independently.

---

## §5 Connection to the wall

### §5.1 Doc 92 wall — what was actually measured

`research/L3_electron_soliton/92_round_11_vi_v10_finer_sampling_structural.md:73`:

> *"No discrete operator on K4 at ℓ_node spacing can have eigenvalue at k = 6.36. This is a Nyquist theorem statement, not a refinement issue."*

This statement is TRUE *on a fixed-geometry K4 lattice at vacuum-ℓ_node spacing*. It is silent on:
1. Whether the corpus electron actually has k = 6.36/ℓ_node as its load-bearing wavelength (Reading C2 challenges this)
2. Whether the K4 lattice can locally compress so that effective-k_max rises above 6.36 in some region (Reading C1 challenges this)
3. Whether the corpus electron requires the K4 substrate at all (Reading B challenges this)

### §5.2 Doc 108 emergence vs consistency pivot

`108:13-17`: Grant directive *"shouldn't the constants emerge from the simulation?"* + honest answer *"no, they currently don't."*

Doc 108's response is to reframe Layers 3-7 from emergence to consistency, accepting "3 calibration inputs → 25 derived to PDG tolerance" as the defensible claim. **But doc 108 §11.5 line 224 acknowledges:** *"the L3 arc question that's been Mode III for weeks ... empirically suggested doesn't happen at corpus parameters."* — i.e., Layer 7 bound-state emergence is queued indefinitely.

**The Reading C investigation tests whether Layer 7 was permanently queued for the right reason (genuinely unrealizable) or the wrong reason (engine doesn't model the necessary physics).**

### §5.3 Why the bench K4-TLM validation worked

The 2026-05-14 K4-TLM bench validation (`AVE-Bench-VacuumMirror/scripts/k4tlm_bench_validation.py`) succeeded for D10 IM3 (slope 2.956) and D2 hysteresis (14× emergence ratio) **at sub-saturation amplitudes A ≤ 0.5**. In this regime:
- The kernel modulates Z_eff but doesn't approach the Schwinger boundary
- The substrate compression is small (linear in strain)
- The Eulerian small-strain approximation is *exact* — no bond-length variation needed
- The Op3 bond reflection captures the impedance gradient physics correctly

The bench is **a deliberately sub-saturation experiment** (synthesis doc operating point V_DC = 30 kV = 0.69·V_yield, A ≈ 1e-3 to 1e-5). The Eulerian engine is *adequate* for the bench-prediction regime. **The wall is specifically the bound-state/saturation regime (A → 1)** where finite-strain matters.

This is consistent: the bench-procurement work and the L3-electron-emergence work hit different physics regimes. The engine is fit-for-purpose for the bench but not for bound-state electron emergence.

---

## §6 Investigation plan (4 phases, with decision gates)

### §6.1 Phase 0 — Engine audit (DONE, §2)

✓ Confirmed: K4Lattice3D + CosseratField3D + coupling implement infinitesimal-strain Eulerian on a fixed scalar dx. No bond-length state variable anywhere in soliton dynamics pipeline.

### §6.2 Phase 1 — Corpus-grep (DONE, §3)

✓ Confirmed: r_d = L_spring/d is canonical (trampoline.tex:249) but treated as cosmological-genesis frozen. Gravity-as-substrate-strain is canonical (Vol 3 Ch 2:35). One Lagrangian solver exists (simulate_gw_impedance.py) decoupled from dynamics. Doc 108 explicitly identifies finite-strain dynamics as unbuilt infrastructure. Horn-torus electron is sub-cell (doc 101 §10).

### §6.3 Phase 2 — Cheap probe: rescaled-grid R7.1 (~3 hr execution)

**Pre-registration:**

- **Hypothesis (Reading B vs C):** if doc 92's Nyquist wall is the load-bearing issue, then running R7.1 multi-seed eigsolver on a *uniformly finer* K4 grid (dx = 0.05 in lattice units; ~20× finer than ℓ_node-natural) should host the corpus eigenmode at k = 6.36/ℓ_node. The Nyquist limit at dx = 0.05 is 0.577/0.05 = 11.5, well above 6.36.
- **Caveat:** doc 92 §5.1 line 116-118 estimates this requires ~8000× more cells in 3D (linear factor 20³). At N = 64 → 64×20 = 1280 cells per side, totally infeasible. Realistic test: dx = 0.2 (5× finer), N = 64, k_max = 2.89 — still below 6.36. **A truly Nyquist-clearing test is computationally infeasible at full electron scale.**
- **Modified test:** run R7.1 at dx = 0.5 (2× finer than vacuum), N = 64. k_max rises from 0.577 to 1.15. Still below 6.36, but tests *trend* — does Mode III response *improve* (smaller PCA aspect, larger peak |ω|) as we approach Nyquist resolution? Linear trend → consistent with Reading B/C; flat trend → wall is something deeper.
- **Driver:** new script `src/scripts/vol_1_foundations/r10_path_alpha_v11_rescaled_grid.py`. Reuses R7.1 multi-seed eigsolver framework from `r7_k4tlm_scattering_lctank.py`. ~200 LOC.

**Decision gate:** sigmoid Mode III response vs dx → PASS-trend, commit to Phase 3. Flat Mode III at all dx → Reading C may not be sufficient; revisit Reading A or revisit observable definition.

### §6.4 Phase 3 — Direct probe: planted compression region (~4 hr execution)

**Pre-registration:**

- **Hypothesis (Reading C1):** in a K4 lattice with a *planted* static compression region (a spherical zone where bond lengths are 10× shorter than vacuum), the corpus electron eigenmode at k = 6.36/ℓ_vacuum can be hosted *inside the compression pocket* but not in the surrounding vacuum substrate.
- **Engine extension required:** minimal — add a `dx_field` array shape (nx, ny, nz, 4) that overrides the scalar `self.dx` in `_compute_strain`, `_compute_curvature`, and the K4 port shifts. Plant compression as: `dx_field[in_sphere] = 0.1`, `dx_field[else] = 1.0`. Run with sustained DC seed at the sphere center.
- **Observables:**
  - PCA aspect of ω-field in compressed region (target ≈ φ² for cubic anisotropy)
  - Peak |ω| in compressed region vs vacuum
  - Bound-state persistence time (does the eigenmode survive ≥ 1000 dt vs decay in <100 dt)
- **Driver:** `src/scripts/vol_1_foundations/r10_path_alpha_v12_planted_compression.py`. ~400 LOC.

**Decision gate:**
- PASS (eigenmode hosts in compressed pocket only): commit to scoping the full engine refactor (Phase 5)
- FAIL (still Mode III in compressed region): Reading C1 alone is insufficient; pivot to C2 single-cell test
- INCONCLUSIVE (boundary pathologies): refine the compression-region geometry (use Gaussian profile, not sharp sphere)

### §6.5 Phase 4 — Refined probe: single-cell phase-space soliton (~4 hr execution)

**Pre-registration:**

- **Hypothesis (Reading C2):** the corpus electron is a single-cell phase-space soliton with (2,3) trefoil winding on the Clifford torus in (V_inc, V_ref). The Mode III result from Round 13 is from forcing a multi-cell observable on a single-cell soliton.
- **Test design:**
  - Single active K4 cell at center of small lattice (N=16). Surrounding cells inactive (mask_active = False).
  - Plant (2,3) trefoil seed in (V_inc, V_ref) at the active cell: V_inc[port] = A·cos(2θ_p + 3φ_p), V_ref[port] = A·sin(2θ_p + 3φ_p) where (θ_p, φ_p) are tetrahedral port angles
  - Cosserat ω seeded at horn-torus tangent per `initialize_electron_unknot_sector(R_target=0.16, r_target=0.16)` adapted to sub-cell scale
  - Run dynamics; verify (a) trefoil winding number is conserved at active cell (Layer 3), (b) ω field eigenmode at horn-torus radius is stable (Layer 1+2)
- **Observables:**
  - Winding number `w_p = (1/2π) ∮ d arg(V_inc + i V_ref)` over the (active cell + neighbors loop) — should be 2 (toroidal) and 3 (poloidal) for (2,3) trefoil
  - ω field PCA aspect at horn-torus radius — should match canonical 2.618 (φ²)
  - Bound-state persistence: ≥ 1000 dt without amplitude decay > 50%
- **Driver:** `src/scripts/vol_1_foundations/r10_path_alpha_v13_single_cell_phase_space.py`. ~500 LOC.

**Decision gate:**
- PASS (single-cell soliton stable): doc 92's Nyquist wall was a mis-framing; the corpus electron is a single-cell phase-space object and existing engine can host it; pivot L3 program back to active research
- FAIL (decays to Mode III): C2 alone insufficient; combined C1+C2 (compressed pocket + single-cell phase-space) may be required; major engine extension
- INCONCLUSIVE (winding-number observable poorly defined at single-cell scale): need observable refinement

### §6.6 Phase 5 — Scope engine extension (planning only, gated on Phase 3 or 4 PASS)

If Phase 3 or 4 PASS, scope the full engine refactor:
- **C1 minimal:** `dx_field` per-bond state variable; local dt computed per cell; substep dynamics; finite-strain coupling from u to dx_field. ~1000-1500 LOC, 2-3 weeks scope, pre-registered against R7.1 multi-seed eigsolver at N=32.
- **C2 minimal:** observable diagnostics for single-cell winding-number and (2,3) Clifford-torus structure. ~300-500 LOC, 3-5 days, pre-registered against single-cell persistence + winding-number target.

---

## §7 Three-mode falsification table

| Phase | Mode I (corpus vindicated) | Mode II (engine basin ≠ corpus) | Mode III (no eigenmode at any seed) |
|---|---|---|---|
| 2: rescaled-grid R7.1 | Mode III response improves monotonically with finer dx, PCA aspect → 2.618 at finest scale | Mode III improves but plateaus at non-corpus aspect ratio | Flat Mode III at all dx; wall is deeper than Nyquist |
| 3: planted compression region | Eigenmode hosts inside pocket, PCA aspect ≈ φ² | Eigenmode hosts but at different aspect; framework basin ≠ corpus | Mode III everywhere; C1 alone is insufficient |
| 4: single-cell phase-space | Winding numbers (2, 3) conserved, ω stable at horn-torus | Winding partially conserved but decays; C2 partial | Decays to Mode III at single-cell scale too |

**Adjudication path:**
- Mode I at Phase 2: Reading B sufficient (just need finer FDTD); commit to that path
- Mode I at Phase 3: Reading C1 sufficient; commit to engine refactor
- Mode I at Phase 4: Reading C2 sufficient; doc 92 was a mis-framing
- Mode III everywhere: Reading A may be load-bearing; framework refactor at axiom level needed (Grant adjudication required)

---

## §8 Open questions for Grant (Rule 16)

### §8.1 Q1 — Is `r_d = L_spring/d` permitted to vary locally? (AXIOM-AUTHOR SCOPE)

Per `Q-G47_buckling_derivation_setup.md:15`, the cooled-equilibrium hypothesis fixes `r_d*` at lattice crystallization and freezes it. Per trampoline.tex:359-372, `r_d` is "the substrate's rest configuration" — singular, not a field.

**Question:** does AVE permit `r_d(x, t)` as a local field that varies under substrate strain, OR does the corpus require `r_d` to remain globally constant?

If yes (local field): Reading C1 is structurally compatible; bond compression is `dx_local(x, t) = r_d_local / L_spring` and the engine just needs to track it.

If no (globally frozen): Reading C1 conflicts with the Q-G47 buckling derivation; the picture has to be modified to "L_spring uniform; bonds can buckle differently in different regions; local Z_eff varies via local buckle angle, not via local bond length."

**This is your call — it's a corpus-axiom-author question.**

### §8.2 Q2 — Is the corpus electron primarily multi-cell or single-cell?

Doc 101 §10 + Bounding Limit 1 says R_loop = r_tube = ℓ_node/(2π) — the electron geometry is *sub-ℓ_node*, contained within one K4 cell. Doc 92's Nyquist wall measured a *multi-cell propagating eigenmode* at k = 6.36/ℓ_node. These are inconsistent observables.

**Question:** when the corpus says "the electron has a Beltrami eigenmode at k = 6.36/ℓ_node," does that wavenumber refer to:
- (a) the spatial wavelength of a multi-cell propagating bound-state eigenmode (Reading C1)
- (b) the inverse-radius scale of the sub-cell horn-torus structure (Reading C2)
- (c) something else (Reading A: ℓ_node itself is wrong; or Reading B: K4 isn't the right substrate at all)

This determines which of Phases 2-4 is the load-bearing test.

### §8.3 Q3 — Does App F's "local Γ=−1 boundary" require per-cell substrate compression?

App F (`AVE-QED/manuscript/vol_qed_replacement/appendices/F_local_machian_network.tex:34-99`) enumerates local Γ=−1 boundaries at electron, nucleus, atom, helio, BH, cosmic scales. Each is a "saturation envelope" where A → 1 locally.

**Question:** is the local Γ=−1 boundary
- (a) a region of *physically compressed substrate* (per-cell dx < vacuum dx), making it Lagrangian finite-strain (Reading C1)
- (b) a region of *modified impedance* on rigid substrate geometry, making it Eulerian small-strain (current engine implementation)

If (a): all multi-scale boundaries (BH, cosmic) imply compressed substrate; gravity is fundamentally Lagrangian; engine refactor is canon-mandated.

If (b): current engine implementation is canon-consistent; the wall is at "Layer 7 bound-state in a different sense" and Reading C1 is wrong; pursue C2 single-cell instead.

---

## §9 Decision gates summary

| Trigger | Decision |
|---|---|
| Phase 2 PASS (rescaled-grid Mode III improves with finer dx) | Commit to Reading B or C1 (Phase 3 will discriminate) |
| Phase 2 FAIL (flat Mode III) | Wall is deeper than Nyquist; revisit Reading A or observable definition |
| Phase 3 PASS (eigenmode in compressed pocket only) | Reading C1 confirmed; scope full engine refactor (Phase 5) |
| Phase 3 FAIL + Phase 4 PASS | Reading C2 sufficient; doc 92 mis-framed; pivot L3 program to active research |
| Phase 3 FAIL + Phase 4 FAIL | Reading C alone insufficient; Reading A axiom-level work needed (Grant call) |
| Q1 = "r_d globally frozen" | Reading C1 unavailable as currently framed; revise picture or pursue C2 only |
| Q1 = "r_d as local field" | Engine refactor compatible with axiom layer; proceed with Phase 5 scope |

---

## §10 Cross-references

Doc 109 should be cited from:
- `CURRENT_STATE.md` 2026-05-14 addendum (local-only, .agents gitignored)
- `AVE-Bench-VacuumMirror/.agents/HANDOFF.md` (tracked, for cross-repo continuity)
- `AVE-QED/.agents/HANDOFF.md` (tracked, for Q-G42 / Q-G46 / Q-G47 lineage)

Doc 109 supersedes nothing. It opens a new investigation thread on the Reading C axis identified by Grant 2026-05-14.

Doc 109 connects to:
- doc 92 (Nyquist wall — context for why this investigation matters)
- doc 101 (three-layer canonical — sub-cell horn-torus geometry)
- doc 103 (substrate-perspective view — "trapped, saturated, slowed substrate" picture)
- doc 108 (emergence vs consistency — acknowledged unbuilt infrastructure)
- Q-G47 buckling derivation (r_d cosmological parameter — axiom-author scope question Q1)
- Route B Q-G19α closure (50 ppm to PDG without lattice-resolved eigenmode — supports Reading C2)
- Bench K4-TLM validation (engine works at sub-saturation; wall is specifically at A → 1)

---

## §11 Pre-execution checklist

Before executing Phases 2-4 in the next session:

- [ ] Grant adjudication on Q1 (r_d as field vs frozen) — gates whether Phase 3 is well-posed
- [ ] Grant adjudication on Q2 (multi-cell vs single-cell electron) — gates which of Phase 3 or 4 is load-bearing
- [ ] Grant adjudication on Q3 (App F boundary = compression vs impedance) — gates the canon-compatibility of the refactor
- [ ] Verify simulate_gw_impedance.py spring-solver API is reusable for Phase 3 (don't re-invent the spring relaxation)
- [ ] Update VACUUM_ENGINE_MANUAL.md cross-reference to doc 109
- [ ] Frozen pre-reg for each phase logged to predictions.yaml or local equivalent

Phases 2-4 are NOT executed in this commit. This doc is the *plan* + verified Phase 0 + Phase 1 results. Execution gated on Grant Q1-Q3 adjudication.

---

## §12 What this doc closes vs leaves open

**Closes (this doc, today):**
- Empirical confirmation that the current K4-TLM + Cosserat engine implements infinitesimal-strain Eulerian on rigid grid (§2)
- Corpus-state verification that bond-length-as-dynamic is canonically (b) partial, not (d) green-field (§3)
- The dual Reading C interpretation (C1 multi-cell vs C2 single-cell) as a clean framework for the investigation (§4)
- Connection between the wall (doc 92, doc 108) and the missing finite-strain physics (§5)
- 4-phase investigation plan with decision gates (§6)
- 3-mode falsification framework per phase (§7)

**Leaves open (pending Grant adjudication + future session execution):**
- Q1: Is r_d a local field? (axiom-author scope)
- Q2: Multi-cell or single-cell corpus electron observable?
- Q3: App F boundaries = compression or impedance?
- Phase 2 numerical execution (rescaled-grid R7.1 trend test)
- Phase 3 numerical execution (planted compression region)
- Phase 4 numerical execution (single-cell phase-space soliton)
- Phase 5 full engine refactor scope (gated on Phase 3 or 4 PASS)

**Bottom line:** Grant's question 2026-05-14 is **not green-field framework speculation** — it's surfacing a known gap that doc 108 already flagged as unbuilt. The investigation plan tests whether closing this gap unblocks the L3-electron wall, with cheap probes first and the full refactor gated behind decision gates that require empirical confirmation.

---

## §13 Boundary-envelope reformulation (Grant 2026-05-14 evening — CONFIRMED CANONICAL)

This section SUPERSEDES the dual Reading C1/C2 framing in §4 above. Reading C2 is promoted to canonical; Reading C1 (multi-cell compressed pocket with engine refactor) is deferred as likely unnecessary.

### §13.1 The Grant statement (verbatim)

2026-05-14 evening, after Phase 0 + Phase 1 results landed:

> *"It almost seems like the grid isn't or the spacing of the vacuum lattice isn't actually based on the flux tube inside the envelope of the electron's boundary region, but the boundary region itself. Of course, we say photons are not physical matter. It's the effect of their impedance mismatch boundary condition that causes physical exclusion conditions. Therefore, the lattice doesn't need to support the smallest flux tube, but the smallest envelope containing that smallest flux tube."*

And after auditor confirmation:

> *"You can resolve what's in a black hole, why could you resolve what's in an electron's envelope/boundary?"*

### §13.2 The black-hole / electron parallel

The corpus already canonically pairs these two boundary scales at `Vol 3 Ch 2:43`:

> *"the Schwarzschild radius r_s = 2GM/c² marks the point where the local strain reaches the Axiom 4 saturation limit (S → 0)."*

Same mechanism at both scales:

| | Black hole | Electron |
|---|---|---|
| Boundary | Schwarzschild horizon at r_s = 2GM/c² | Horn torus tube wall at r ≈ ℓ_node/(2π) |
| Substrate condition at boundary | A → 1, S → 0, Γ → −1 | A → 1, S → 0, Γ → −1 |
| Interior visibility from substrate | **Impossible** (causal disconnection) | **Impossible** (impedance-mismatch disconnection at Γ = −1) |
| Externally observable properties | Mass M, charge Q, angular momentum J (no-hair) | Mass m_e, charge e, spin ℏ/2 (no-hair) |
| Number of integrated observables | 3 | 3 |

**The no-hair theorem applied to electrons:** from outside the boundary envelope, only three integrated properties are substrate-observable. The interior flux-tube Beltrami eigenmode, the (2,3) winding number, the Cosserat ω profile — all are interior plumbing that contributes to the integrated observables (m_e, e, ℏ/2) but are not themselves directly substrate-observable.

**Substrate observability rule:** the substrate sees the boundary, not the interior. This is universal across App F's multi-scale Machian network — every local Γ = −1 boundary at every scale has this property.

### §13.3 Why this dissolves the doc 92 wall

`doc 92:73`:
> *"No discrete operator on K4 at ℓ_node spacing can have eigenvalue at k = 6.36. This is a Nyquist theorem statement, not a refinement issue."*

The k = 6.36/ℓ_node is the **interior flux-tube Beltrami eigenmode**. From §13.2, that eigenmode is interior plumbing — not substrate-observable.

**The substrate never propagates a wave at k = 6.36/ℓ_node.** That wave exists ONLY inside the boundary envelope, where the substrate's Γ → −1 reflection condition isolates it from the exterior. From the substrate's perspective, the bounded region is a "black box" with impedance properties (mass, charge, spin) at the boundary surface.

**What the substrate must resolve:**
1. **Boundary envelope scale** ~ ℓ_node (one cell). K4 Nyquist k_max = 0.577/ℓ_node easily resolves a localization of size ℓ_node.
2. **Phase-space (V_inc, V_ref) topology at the boundary** — the (2,3) Clifford-torus winding lives per-cell, entirely within the lattice's native variable structure. No spatial wavelength resolution needed.
3. **Outside-the-boundary impedance gradient** — gravity-as-substrate-strain `n(r) = 1 + 2GM/(rc²)` falls off in neighboring cells via the existing kernel S(A) at each cell. Existing engine handles this.

**Doc 92 measured the wrong observable.** It forced a multi-cell propagating-eigenmode test on what is canonically a single-cell bounded boundary object. Mode III ("DC-dominated quasi-static residual") is the CORRECT substrate response to a bounded interior — the interior IS quasi-static from the substrate's perspective because the boundary reflects all interior dynamics.

### §13.4 Why Reading C1 (multi-cell compressed pocket) is unnecessary

Reading C1 proposed adding `dx_local` per-bond state variable so the lattice could physically compress around solitons. From §13.2, this is unnecessary:

- The substrate's "compression" near a soliton is the **impedance gradient** in neighboring cells via kernel S(A), not geometric bond-length variation
- The canonical gravity prediction is `n(r) = 1 + 2GM/(rc²)` — this is **refractive index** modulation, i.e., impedance modulation, not geometric compression
- The existing Eulerian small-strain engine implements impedance modulation correctly (today's K4-TLM bench validation: IM3 slope 2.956, D2 hysteresis 14× ratio — both via op3_bond_reflection at sub-saturation)
- The single-cell bounded-boundary picture (Reading C2 promoted) doesn't need bonds to physically compress; it needs the kernel to engage at the boundary cell

**Reading C1 was over-engineering driven by the misframed wall.** With the wall reframed, C1 dissolves.

### §13.5 Partial resolution of Q1-Q3

Grant's 2026-05-14 evening confirmation partially answers the three open questions from §8:

**Q1: Is r_d = L_spring/d permitted to vary locally?**
**Provisional answer: NO, r_d remains globally frozen at genesis.** Reading C1 is no longer needed; the canonical Q-G47 cooled-equilibrium hypothesis stands. r_d is a cosmological-genesis parameter, not a field. (Still flagged for explicit Grant adjudication — this is corpus-axiom-author scope per Rule 15.)

**Q2: Multi-cell propagating eigenmode or sub-cell horn torus?**
**Provisional answer: SINGLE-CELL bounded boundary, with sub-cell interior plumbing.** The "wavelength k = 6.36/ℓ_node" from doc 92 is an interior observable. The substrate-observable is the boundary envelope at one-cell scale. Doc 92 measured the wrong observable. (Confirmed by Grant via BH analogy.)

**Q3: App F local Γ=−1 boundaries = compression or impedance?**
**Provisional answer: IMPEDANCE.** All App F multi-scale boundaries (electron, nucleus, atom, helio, BH, cosmic) are saturation-engaged Γ → −1 impedance surfaces. Bonds don't physically compress; the kernel S(A) saturates at the boundary, producing the reflection condition. The existing engine handles this. (Confirmed by Grant via BH analogy + Vol 3 Ch 2:43.)

### §13.6 Connection to Q-G19α Route B and the Q-factor identity

Two prior canonical results corroborate §13:

**Route B Q-G19α closure** (2026-05-13, `AVE-QED/scripts/g2_research/q_g19_alpha_route_b_petermann.py`): C_2 = -0.32846 matching PDG -0.32848 to 50 ppm. The closure used dark-wake × kernel-asymmetry correlation in phase space + saliency δ = -3α/2. It did NOT require lattice-resolving an interior eigenmode of the electron. Route B operates on **boundary-integrated phase-space observables**, consistent with §13's substrate-only-sees-boundary rule.

**Q-factor identity** (`AVE-Core/src/scripts/vol_1_foundations/electron_tank_q_factor.py`): α⁻¹ = 4π³ + π² + π = 137.036. The identity Λ_vol + Λ_surf + Λ_line decomposes the Q-factor into volume + surface + line integrals — all **integrated** quantities, exactly what's substrate-observable per §13.2. The line integral (π = perimeter) corresponds to the boundary itself; the surface integral (π² = horn torus surface) and volume integral (4π³ = horn torus volume) are integrated interior properties that survive as boundary-summarized observables.

Both results are consistent with: the substrate sees integrated boundary-level observables, not interior-resolved eigenmodes.

### §13.7 What changes in the framework documentation

Following Grant's confirmation, the framework documentation should be sharpened:

1. **AVE-QED App F** (`AVE-QED/manuscript/vol_qed_replacement/appendices/F_local_machian_network.tex`): the multi-scale local Γ=−1 boundary network already implies §13's substrate-only-sees-boundary picture. App F should be sharpened with an explicit "substrate observability rule" subsection making this canonical.

2. **AVE-Core Vol 2 Ch 6 / Vol 4 Ch 1**: the K4-Bethe-tree C_2 derivation in `src/ave/solvers/g_minus_2_lattice.py` was already banner-marked SUPERSEDED (commit 2d5c03a). The historical chapter framing of "where continuous QED breaks down against the discrete vacuum hardware" was premised on lattice-resolving interior eigenmodes. Under §13, that framing is wrong: continuous QED can't be wrong about interior eigenmodes because the substrate doesn't resolve interior eigenmodes either; both operate on boundary-integrated observables, which is why Route B's QED-form normalization works.

3. **AVE-Core doc 30 §3.1 photon definition**: doc 107's empirical failure (`u/ω = 0.354 ≠ 0`, helicity sign didn't flip) is partially explained: doc 30 prescribed a *physical-matter* property for the photon (u = 0, "microrotation sector only"). Under §13, photons are propagating boundaries, not physical matter — the engine's empirical "u driven by ω" coupling may be CORRECT physics that doc 30 was wrong to forbid. Worth re-examining.

4. **CURRENT_STATE.md and HANDOFFs**: doc 109 (this doc, with §13) becomes the canonical reference for the L3-electron-soliton wall reformulation. Phase 4 (§14) is the load-bearing test.

### §13.8 What's invariant despite the reformulation

The reformulation doesn't change:
- Phase 0 engine audit findings (§2) — engine still implements Eulerian small-strain on fixed grid. But that's now CORRECT for the substrate's needs, not a limitation.
- Phase 1 corpus-grep findings (§3) — gravity-as-substrate-strain via ε_eff/μ_eff is exactly the impedance-only picture §13 endorses. trampoline.tex L_spring/d remains canonical cosmological parameter.
- Bench K4-TLM validation (today's IM3 slope 2.956) — bench at sub-saturation operates entirely on the exterior-of-boundary regime where kernel + Op3 are correct.
- Doc 108 framework-25 consistency suite (20/20 PASS) — these are all integrated observables, which §13 says are exactly what's substrate-measurable.
- Three-layer canonical (doc 101 §9-§10): Layer 1 real-space unknot + Layer 2 SU(2) bundle + Layer 3 phase-space (2,3) winding. **All three layers are properties of the single-cell boundary object.**

---

## §14 Pre-registered load-bearing test: single-cell bounded-boundary electron

Per ave-prereg discipline (Step 3 prereg before any new derivation/script). This test replaces the deferred Phases 2 + 3 from §6 and refines Phase 4.

### §14.1 Target

**Derive empirically:** does the K4-TLM + CosseratField3D coupled engine host a stable bounded Γ = −1 boundary at one active cell, with (2,3) phase-space winding conserved, with impedance-gradient profile in neighboring cells matching `n(r) = 1 + 2GM/(rc²)` per Vol 3 Ch 2:35, with Q-factor measured as integrated boundary observable matching α⁻¹ = 137.036?

### §14.2 Corpus state from Phase 1 corpus-grep (already done)

- (a) CLOSED: substrate's boundary observability rule (§13.2 confirmed by Grant; canonical via App F + Vol 3 Ch 2:43)
- (a) CLOSED: electron horn torus geometry R = r = ℓ_node/(2π) (doc 101 §10)
- (a) CLOSED: three-layer canonical (doc 101 §9; unknot + SU(2) + (2,3) Clifford)
- (a) CLOSED: Q-factor identity α⁻¹ = 4π³ + π² + π = 137.036 (electron_tank_q_factor.py)
- (b) PARTIAL: which (V_inc, V_ref) parameterization plants the (2,3) Clifford-torus winding correctly at a single cell — corpus has the three-layer description but not the seeder code

### §14.3 Prediction

**Most likely (Mode I PASS):** the engine hosts a stable bounded boundary at one active cell. Three observables (peak |ω|, winding number, outside-cell impedance gradient) match canonical predictions to within 5%. Q-factor integral matches α⁻¹ = 137.036 to within ~1%.

**Why:** the existing engine implements kernel + Op3 + Cosserat dynamics that ARE the correct physics for boundary-only substrate observability. The Mode III result from Round 13 was measuring the wrong observable. The right observable is integrated boundary signatures, which should be present in the engine output if §13 is correct.

**Alternative outcomes (Mode II/III):**
- Mode II (engine basin ≠ corpus): boundary persists but observables don't match canonical predictions. Indicates the engine implements correct boundary-only physics but at the wrong operating point.
- Mode III (no stable boundary): boundary decays. Indicates §13 is wrong, OR the seeder is wrong, OR additional physics (vacuum coupling between Cosserat ω and K4 V at the boundary) is missing.

### §14.4 Discriminating outcomes

| Outcome | Boundary persistence > 1000 dt | (2,3) winding conserved | Outside gradient matches n(r) | Q-factor ≈ 137.036 | Interpretation |
|---|---|---|---|---|---|
| Mode I (corpus vindicated) | ✓ | ✓ | ✓ | ✓ | §13 confirmed canonical; L3-electron program unblocked; pivot to mass spectrum + g-2 + multi-particle tests |
| Mode I-partial | ✓ | ✓ | ✓ | ✗ | Boundary forms and is stable, but Q-factor doesn't integrate correctly. Seeder ω profile is non-canonical. |
| Mode I-partial alt | ✓ | ✓ | ✗ | ✓ | Boundary forms, but gravity profile doesn't match. Engine's outside-cell coupling needs review. |
| Mode II | ✓ | ✗ | ✓ | depends | Boundary forms but (2,3) topology decays. Phase-space coupling at single-cell scale is broken or the (2,3) Clifford-torus seeder is wrong. |
| Mode III | ✗ | n/a | n/a | n/a | No stable bounded boundary in current engine. §13 may be wrong, OR additional physics (vacuum→ω→V_inc coupling beyond current model) is required. |

### §14.5 Falsifier

**§13 (boundary-only substrate observability) is falsified if:**
- Mode III result reproduces across 4+ independent seed parameterizations (saturated-V_inc, Clifford-torus, unknot Cosserat, Beltrami eigenmode at boundary radius)
- AND the engine instabilities are not numerical (verified via CFL reduction, alternative integrators)
- AND no operationally-canonical seed produces a bounded boundary

In which case, the wall is genuinely structural: the K4-TLM + Cosserat coupled engine cannot host even the BOUNDARY of a bounded soliton, and Reading A or B from doc 92 would need to be revisited.

### §14.6 Test driver (to be authored next session)

File: `src/scripts/vol_1_foundations/r10_path_alpha_v14_single_cell_boundary.py`

Pseudocode:
```python
from ave.topological.vacuum_engine import VacuumEngine3D

# §14.6a Setup: small lattice, one active K4 cell at center
N = 16
engine = VacuumEngine3D.from_args(
    N=N, pml=4, temperature=0.0,
    amplitude_convention="V_SNAP",
    enable_op3_bond_reflection=True,  # PER 2026-05-14 K4-TLM bench validation
)

# §14.6b Plant Γ = −1 boundary at one active cell
center = (N//2, N//2, N//2)  # all-even, A-site (active per K4 parity)
amplitude = 0.95  # near saturation; high V_inc on all 4 ports
for port in range(4):
    engine.k4.V_inc[center[0], center[1], center[2], port] = amplitude / 2.0
    # Plant (2,3) Clifford-torus winding in (V_inc, V_ref) phase space:
    # V_ref initialized π/2-out-of-phase per port with (2,3) winding modulation
    port_phase_2 = 2 * (port * np.pi / 2)  # toroidal winding 2
    port_phase_3 = 3 * (port * np.pi / 2)  # poloidal winding 3
    engine.k4.V_ref[center[0], center[1], center[2], port] = \
        amplitude / 2.0 * np.cos(port_phase_2 + port_phase_3)

# §14.6c Plant Cosserat unknot at horn-torus scale
# (existing API; sub-cell scale)
engine.cos.initialize_electron_unknot_sector(
    R_target=0.16,  # ℓ_node/(2π) in lattice units (sub-cell)
    r_target=0.16,
    amplitude_scale=0.35,  # bound-state operating amplitude per Path B Round 6
)

# §14.6d Run dynamics
n_steps = 2000  # ~2 Compton periods at dt = ℓ_node/(c√2)
for step in range(n_steps):
    engine.step()
    if step % 100 == 0:
        # Diagnostic: boundary persistence, winding conservation, outside-cell
        # impedance gradient, Q-factor integral
        log_boundary_persistence(engine, center)
        log_phase_space_winding(engine, center)
        log_outside_impedance_gradient(engine, center)
        log_q_factor_integral(engine, center)

# §14.6e Verdict
adjudicate_mode_i_through_mode_iii(observables, prereg=__file__)
```

Estimated: ~500 LOC including diagnostics + 4 observables. ~1 day to author + debug + run.

### §14.7 Acceptance criteria (frozen pre-reg)

**Mode I PASS (§14.3 most-likely):**
- Boundary peak |V_inc| at center cell > 0.5 of initial amplitude at t > 1000 dt
- Phase-space winding number 2 and 3 conserved to within ±0.1 over the run
- Outside-cell impedance gradient z_local(r=2dx) / z_local(r=4dx) within ±15% of n(2dx)/n(4dx) predicted from `n(r) = 1 + 2GM/(rc²)` with M = m_e in lattice units
- Q-factor integral (V_inc² × volume + V_inc × surface + V_inc × line) at boundary matches α⁻¹·(V_inc_peak)² to within 5%

**Mode III FAIL (§14.5 falsifier):**
- Boundary peak |V_inc| < 0.1 of initial amplitude at t = 500 dt
- AND ω-field at horn-torus radius decays to noise floor
- AND no integrated observable shows bounded-state signature

### §14.8 Pre-execution gating

Before executing §14.6 driver:

1. ✓ Phase 0 engine audit (done, §2)
2. ✓ Phase 1 corpus-grep (done, §3)
3. ✓ Boundary-envelope reformulation framed (§13)
4. ✓ Grant adjudication on §13 framing (CONFIRMED 2026-05-14 evening)
5. ☐ ave-prereg formal pre-registration commit (this section)
6. ☐ Verify `enable_op3_bond_reflection=True` is the canonical flag in VacuumEngine3D.from_args (today's bench validation discovered this is required; needs to be confirmed exposed in the engine constructor)
7. ☐ Verify `initialize_electron_unknot_sector(R, r)` accepts sub-cell scale (R = r = 0.16 in lattice units); current API may need to extend
8. ☐ Author the driver per §14.6 pseudocode
9. ☐ Run + adjudicate

Items 5-9 are next-session work.

---

## §15 Doc 109 status after Grant confirmation

**Promoted to canonical:** §13 boundary-envelope reformulation. Reading C2 = single-cell bounded-boundary picture.

**Demoted to deferred:** Reading C1 (multi-cell compressed pocket with `dx_local` engine refactor). Likely unnecessary; canonically inconsistent with gravity-as-impedance per Vol 3 Ch 2.

**Pre-registered:** §14 load-bearing test (single-cell bounded-boundary persistence + winding + gradient + Q-factor).

**Still open (Rule 16 axiom-author scope, but PARTIALLY answered by Grant's BH analogy):**
- Q1 (r_d as local field): provisional NO (Reading C1 unnecessary)
- Q2 (multi-cell vs single-cell electron): provisional SINGLE-CELL
- Q3 (App F = compression vs impedance): provisional IMPEDANCE

**Cross-references update needed:**
- `AVE-QED/manuscript/vol_qed_replacement/appendices/F_local_machian_network.tex` — add explicit "substrate observability rule" subsection
- `AVE-Core/research/L3_electron_soliton/CURRENT_STATE.md` (local-only) — note this doc as canonical for L3-electron framing post-2026-05-14 evening
- `AVE-Core/research/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md` — annotate engine's Eulerian small-strain dynamics as CORRECT for boundary-only substrate observability, not a limitation

**The wall (doc 92) is reframed, not refuted:** Doc 92's Nyquist analysis was numerically correct for the question it asked (can K4 host k=6.36/ℓ_node propagating eigenmode? No). The question itself was misframed for the substrate's perspective. The right question (does K4 host a bounded boundary at one-cell scale with the right integrated observables?) is empirically open and will be answered by §14's test next session.
