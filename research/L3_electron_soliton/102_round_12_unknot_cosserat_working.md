# Round 12 working doc: unknot Cosserat seeder + canonical-electron layer-1+2 test

**Date:** 2026-05-01
**Predecessor:** [doc 101 §9+§10 three-layer canonical](101_round_12_unknot_cosserat_entry.md)
**Status:** working doc — Steps 1-6 documented as work proceeds per Grant directive 2026-04-30 ("document as you go and proceed")

---

## §1 — Round 12 plan reference

Per doc 101 §9.7 + §10.4 (post-auditor-pass-3-corrections):

- **Layer 1** (real-space curve): unknot 0₁ at horn torus R_loop = r_tube
- **Layer 2** (field bundle over curve): SU(2) double-cover via Cosserat ω-field's SO(3) → SU(2) projection (per A-008)
- **Layer 3** (phase-space (V_inc, V_ref) on Clifford torus): NOT in scope of Round 12 — separate K4 V-sector work
- **α-derivation chain audit**: NOT in scope of Round 12 — separate audit lane

Round 12 builds the Cosserat unknot seeder for layers 1+2; verifies via Cosserat-only tests; defers layer 3 + full coupled engine to Round 13+.

Steps:
1. Substrate walk + analytical Beltrami structure (§2)
2. Engine code: `initialize_electron_unknot_sector` (§3)
3. Unit tests (§4)
4. Validation driver (§5)
5. Engine cleanup: rename old seeder (§6)
6. Closure summary (§7)

---

## §2 — Step 1: substrate walk + analytical structure

### §2.1 — Coordinate system: toroidal coords on horn-torus

Standard toroidal coordinates around a loop centered at origin in the xy-plane with major axis = z-axis:

- ρ_xy = √(x² + y²) — distance from z-axis
- φ = atan2(y, x) — toroidal angle (around major circle), φ ∈ [0, 2π)
- ψ = atan2(z, ρ_xy − R_loop) — poloidal angle (around tube cross-section), ψ ∈ [0, 2π)
- ρ_tube = √((ρ_xy − R_loop)² + z²) — distance from tube centerline

Cartesian recovery: x = (R_loop + ρ_tube · cos ψ) · cos φ, y = (R_loop + ρ_tube · cos ψ) · sin φ, z = ρ_tube · sin ψ.

Tube center (where the seeded ω-field peaks): {ρ_tube = 0} = {ρ_xy = R_loop, z = 0} = circle of radius R_loop in xy-plane.

For horn-torus (R_loop = r_tube): the tube cross-sections meet at ρ_xy = 0 (donut hole closes to a point at the z-axis center). The poloidal coordinate ψ becomes ill-defined at the donut-hole point but is well-defined elsewhere on the tube surface.

### §2.2 — Ansatz: ω-field is toroidal-tangent with localization profile

For the unknot's Beltrami eigenmode at fundamental Layer 2 mode (no (p, q) winding — this distinguishes the unknot from torus-knot ansatze):

**ω-vector:** points along the toroidal direction ê_φ = (−sin φ, cos φ, 0). This is the "loop tangent" direction — ω circulates around the loop axis everywhere.

**Localization profile:** Concentrated on the tube centerline ρ_tube = 0, decaying outward. AVE-canonical hedgehog form (matching existing `initialize_electron_2_3_sector`):

g(ρ_tube) = π / (1 + (ρ_tube / r_opt)²)

where r_opt = r_tube (the tube radius parameter). This is power-law decay; smoother than Gaussian; matches the (2,3) seeder's profile family.

**Full ansatz:**

ω(x) = A · g(ρ_tube(x)) · ê_φ(x)

where A is the amplitude scale. Component form:
- ω_x = −A · g(ρ_tube) · sin φ
- ω_y = +A · g(ρ_tube) · cos φ
- ω_z = 0

### §2.3 — 2π closure of the ω-field; SU(2) closure is observable

Under φ → φ + 2π:
- sin φ → sin(φ + 2π) = sin φ
- cos φ → cos(φ + 2π) = cos φ
- ω → ω

So ω returns to itself after 2π toroidal revolution. **This is the SO(3) full-cover period** — consistent with the Cosserat ω-field being SO(3)-valued by construction (per A-008).

The Layer-2 SU(2) double-cover (4π closure) is NOT a property of ω directly — it's a property of the SPINOR observable obtained by projecting ω onto SU(2) via the Rodrigues map (existing at [`cosserat_field_3d.py:102`](../../src/ave/topological/cosserat_field_3d.py#L102) `_project_omega_to_nhat`). The spinor projection is 2-to-1 onto SO(3): ω and −ω map to the same n_hat. Transporting around the loop, the SU(2) spinor accumulates a phase that closes after 4π.

**Implication for seeder:** the ansatz encodes Layer 1 + Layer 2's GEOMETRIC carrier (the loop with toroidal-tangent ω). Layer 2's spin-1/2 character is observable via post-processing (extract spinor phase along loop axis and verify 4π closure). Seeder doesn't need to encode 4π directly.

### §2.4 — Beltrami fundamental k for the unknot

The Beltrami equation ∇×ω = kω gives the eigenmode condition. For a smooth toroidal-tangent ω = A·g(ρ_tube)·ê_φ with g power-law-decaying:

**Analytical estimate (dimensional):** k ~ 1/R_loop. The Beltrami eigenvalue scales inversely with the longest spatial dimension; for a closed loop, that's the loop's major radius.

For unknot canonical (Reading A, doc 101 §2): R_loop = ℓ_node/(2π). So k_canonical = 2π/ℓ_node, which corresponds (via k·c = ω) to angular frequency 2π·c/ℓ_node = 2π·ω_C — i.e., one Compton-wavelength fits one full loop circumference. **Self-consistent with the corpus's reduced-Compton-wavelength = unknot-circumference identification.**

**Practical seeder note:** the seeder doesn't need to FIX k; the relax_to_ground_state algorithm will find the actual Beltrami eigenvalue from the ansatz seed. Pre-register that the relaxed eigenmode should sit at k ≈ 1/R_loop within ~50% (numerical Beltrami eigenvalue analysis on torus has known geometric corrections).

### §2.5 — Sub-grid resolution caveat

Reading A canonical: R_loop = r_tube = ℓ_node/(2π) ≈ 0.16 ℓ_node. At dx = 1.0 in the Cosserat solver (one grid cell = one ℓ_node), R = 0.16 cells. **Sub-grid.**

This is the same Flag 2 substrate-physics scenario from E-094: the corpus electron is sub-ℓ_node, and lattice solvers at ℓ_node sampling can't resolve it. CosseratField3D's continuous-coordinate JAX-autograd architecture is supposed to be sub-grid-capable, but the discretized field still suffers aliasing at sub-grid scales.

**Pragmatic protocol:**
- Run validation at LATTICE-RESOLVED scale (R = r = 4 cells, say, or 8 cells) as the primary diagnostic — verifies the seeder produces correct topology + SU(2) bundle structure on a grid that resolves it
- Run secondary test at SUB-GRID scale (R = r ≈ 0.5 cells) to probe whether the JAX-autograd handles sub-cell features
- Document both; the lattice-resolved test is the seeder's correctness validation; the sub-grid test is the canonical-electron validation per E-094 Flag 2

### §2.6 — Pre-registered binary criteria for seeder correctness

For the lattice-resolved primary test (R = r = 4 cells; eventually 32³ + 64³ per A40 multi-N):

- **C1 — Topology preservation (Layer 1):** `extract_crossing_count` on the seeded + relaxed ω-field returns c = 0. (Unknot has zero crossings; torus-knot seed would return c ≥ 2.)
- **C2 — Hopf charge zero (Layer 1):** `extract_hopf_charge` returns Q_H ≈ 0 (within ~10% — Chern-Simons integral has discretization error for sub-cell features). Unknot has zero linking with itself.
- **C3 — Loop localization:** `extract_shell_radii` returns R ≈ R_target ± 5%. The seeded ω-field stays localized on the loop axis under relaxation.
- **C4 — Tube-thickness consistency:** `extract_shell_radii` returns r ≈ r_target ± 10% (loose since r-extraction has known sensitivity to convention per doc 100 §17 + §23). For horn torus (R = r), r and R should both extract the same value.
- **C5 — Energy finite + non-negative:** total_energy returns finite positive value for both seeded state and post-relaxation state.
- **C6 — Energy non-trivial:** total_energy ≫ vacuum-floor noise (i.e., seeded + relaxed state has detectable energy, not collapsed to vacuum).
- **C7 — Layer-2 SU(2) bundle character (post-processing):** extract spinor n_hat at points equally spaced around the loop circumference; verify the spinor phase progresses smoothly with toroidal angle and closes after 4π (≈ 2 full loops).
  - Sub-criterion: if spinor closure is 2π not 4π, the seeded field has SO(3) structure but not SU(2) double-cover at this scale — Layer 2 is not validated, would need Round 13 work to add explicit SU(2) bundle structure to the seed.

Pass-criterion set: PASS if C1, C2, C3, C5, C6 all hold + at least one of C4/C7. STRICT FAIL if C1, C2, or C5 fail. Methodology disciplines: A39 v2 dual-criterion (frequency + topology) → here it's amplitude + Q_H + c jointly.

### §2.7 — What this substrate walk does NOT do

- Does NOT analytically solve ∇×ω = kω on horn torus closed-form (handed off to numerical relaxation + post-processing measurement)
- Does NOT pre-register specific λ_Beltrami value (let relaxation find k; pre-register the dimensional scaling k ≈ 1/R)
- Does NOT address sub-grid R = r = ℓ_node/(2π) ≈ 0.16 cells canonical scale beyond a flagged secondary test
- Does NOT test Layer 3 (phase-space (V_inc, V_ref) winding) — that's Round 13+ K4 sector work
- Does NOT modify or test the existing `initialize_electron_2_3_sector` (other than rename in Step 5)

§2 closes Step 1. The ansatz is concrete enough to implement. Beltrami fundamental k is estimated dimensionally; validation is numerical via relax + measure.

---

## §3 — Step 2: engine code (`initialize_electron_unknot_sector`)

[Pending — next section to write as Step 2 work proceeds.]

---

## §4 — Step 3: unit tests

[Pending — Step 3 work.]

---

## §5 — Step 4: validation driver

[Pending — Step 4 work.]

---

## §6 — Step 5: engine cleanup

[Pending — Step 5 work.]

---

## §7 — Step 6: closure summary

[Pending — Step 6 closes Round 12.]
