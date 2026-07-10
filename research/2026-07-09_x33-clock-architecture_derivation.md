# DERIVATION — X33: why the honest synchronous coined walk PINS (and the continuum LIFTS)

**Date:** 2026-07-09 · **Branch:** `analysis/x33-clock-architecture` · Companion to the
[prereg](2026-07-09_x33-clock-architecture_prereg_FROZEN.md) and
[result](2026-07-09_x33-clock-architecture_result.md).

This note shows **algebraically WHERE the stiffness enters** (the survey's "S^{-1/2} normalization divides out the
stiffness" tell) and why the normalized-arccos ceiling is pinned — as claimed in the prereg §6, to be confirmed,
not assumed. Every step is verified numerically by the driver (`x33_clock_architecture.py`, gates G2/G5/G6).

---

## 1. The coin, derived from the per-channel transmission coefficients (NOT assumed)

At an Op5 shunt node, bonds `b` meet; each bond is a transmission line whose **matrix wave admittance** for the
3-vector displacement is `Y_b = (m Φ_b)^{-1/2}`, `Φ_b = k_a d̂⊗d̂ + k_s(I − d̂⊗d̂)` the rank-2 bond tensor
(`chiral_lattice_dynamics.py` / survey). Shunt continuity (all bonds share the node displacement `U`) + Kirchhoff
current balance give the reflection

    U_b^ref = U_node − U_b^inc,   U_node = (Σ_b Y_b)^{-1} · 2 Σ_b Y_b U_b^inc.

**Power conservation forces energy-normalized wave variables** `a_b = √Y_b · U_b` (the closed-TLM energy is
`Σ_b |a_b|²`, the invariant `connect_is_permutation` already proves conserved). In those variables the coin is a
**Householder reflection** about the stiffness-weighted symmetric mode:

    C_i = 2 |w_i⟩⟨w_i| − I,   |w_i⟩ = stacked blocks  √Φ_b · S_i^{-1/2},   S_i = Σ_b Φ_b,   ⟨w_i|w_i⟩ = I_3.   (★)

The `√Φ_b` weighting and the `S_i^{-1/2}` normalization are **the √Y symmetrization** — they are not a modelling
choice, they are the unique power-conserving (unitary) form of the physical shunt scatter. At `k_a = k_s` (★)
collapses to the scalar Grover coin `S_ij = 2/z − δ_ij` (`scatter_matrix`, eigs {+1, −1×(z−1)}), reproducing #604.

## 2. The pin locus #1 — the coin eigenvalues are ±1 for ANY ρ* (driver G6)

`C_i = 2|w_i⟩⟨w_i| − I` with `⟨w_i|w_i⟩ = I_3` (an isometry) is a reflection: **eigenvalues +1 (3-fold, the
symmetric block) and −1 ((z−1)·3-fold), independent of ρ\***. Driver G6 confirms `eig(C_i) = {+1×3, −1×6}` for
ρ* ∈ {1, 9.77, 100, 1000} to 1e-9. **The stiffness ρ\* enters ONLY the eigenVECTOR** `|w_i⟩` (through `√Φ_b` and
`S_i^{-1/2}`), never the spectrum. This is the algebraic locus the survey's tell pointed at: the normalization that
makes the coin a well-defined unitary reflection is exactly what divides the stiffness out of its eigenvalues.

## 3. Walk = normalized-arccos, EXACTLY (spectral mapping theorem, driver G2)

The one-step walk `U(k) = Shift(k)·C`, `Shift` = arc-reversal permutation with Bloch phase `e^{ik·δ}`
(channel-blind, topological, one bond per tick). By the Grover-walk spectral mapping theorem, the non-flat
eigenphases of `U` satisfy

    cos θ = eig( Ã(k) ),   Ã(k) = S^{-1/2} A(k) S^{-1/2}   (the stiffness-weighted normalized adjacency),

i.e. `θ = arccos(eig Ã) = ω_walk/ω_link`. Since the survey's normalized Laplacian is
`D̃ = S^{-1/2} D S^{-1/2} = I − Ã`, we have `arccos(1 − eig D̃) = arccos(eig Ã) = θ` — **the survey's
normalized-arccos map IS the honest scatter+connect walk.** The driver builds the LITERAL walk unitary (★) and
diagonalizes it: `‖U U† − I‖ < 4e-14` (unitary) and the eigenphases match `±arccos(eig Ã)` to `1.2e-13` for every
ρ*. The arccos map is DERIVED here, not asserted (prereg §5 G2).

## 4. The pin locus #2 — bipartite π-mode saturates the eigenphase at π (driver G5)

The srs graph is **bipartite**, so the stiffness-weighted normalized adjacency has `eig_min(Ã) = −1` for ANY ρ*
(the fully-antisymmetric π-mode, every neighbour out of phase). Equivalently `λ̃_max = eig_max(D̃) = 2` exactly.
Driver G5: `λ̃_max = 2.000000` (dev 2e-15) for ρ* ∈ {1, 9.77, 100, 1000}. Therefore

    ω_top^walk = ω_link · arccos(eig_min Ã) = ω_link · arccos(−1) = π · ω_link = π√3 · ω_C = 5.44140 ω_C,   ∀ ρ*.

**The ceiling is the tick Nyquist, ρ\*-independent — the walk PINS.** (Combines §2: eigenvalues can't move; §4:
the −1 mode always exists.)

## 5. The continuum LIFTS — the contrast partner (driver G4)

The continuous (lumped) architecture is `ω = √eig(D(k))`, a Hamiltonian flow with NO tick. Its ceiling is
`√λmax(D)`, and for a bipartite lattice `λmax(D) = 2·(self-block)` scales with the bond stiffness. Driver: the
continuous top rises `2.45 → 5.58 → 17.37 → 54.79` (elastic units) across ρ* ∈ {1, 9.77, 100, 1000} — a 22× lift.
The stiffness enters `D` linearly, so `√eig(D)` lifts as `√stiffness`; there is no bipartite `arccos(−1)` cap
because there is no unitary tick to bound the eigenphase.

## 6. Both agree at long wavelength; they diverge ONLY at the zone edge (driver G3)

Low-k: `arccos(1 − λ̃) ≈ √(2λ̃)`, so `ω_walk ≈ ω_link√(2/s)·ω_cont` with `s` the (isotropic) self-block scale.
This is a **single constant rescaling** — the walk and continuum acoustic velocities share one factor across all
branches and directions. Driver G3: the walk/continuum acoustic-slope ratio is constant to spread `9.2e-7` over 9
samples (3 branches × 3 directions), reproducing the VRH velocity table (shear branch = c₀ = c_link/√3). **The two
architectures are indistinguishable at the zone center**; the pin-vs-lift split is entirely a zone-EDGE
phenomenon — which is exactly why an engine that only checks long-wave velocities cannot type the clock.

## 7. Consequence: the discriminating observable + the Op5 clock type

Because the walk pins ALL branches at π·ω_link while the continuum lets the stiff longitudinal branch top out at
`√(2·stiffness_axial) > π·ω_link`, the **longitudinal-only window** `[shear_top, axial_top]` — a frequency band
where only the k_a-dominated branch propagates — **exists under continuous/lifted and is ABSENT under
walk/pinned**. In MeV (using the survey's per-channel-link √ρ* upper bracket): continuous = **[2.78, 8.69] MeV**;
walk = absent (all branches end at π√3·ω_C = 2.78 MeV).

**Op5 is a PINNING clock** (synchronous discrete-time unitary walk). It will report 5.441 ω_C for any ρ* and cannot
see the lift; the lifted reading needs a continuous-time solver. The bracket [5.441, 17.011] ω_C is therefore an
**architecture fork**, in-engine-undecidable — resolved only by anchoring which clock the vacuum runs (Branch S).
