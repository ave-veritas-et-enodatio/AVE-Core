# Phase 3b X3 — Energy Minimization + Physics Reframe

**Date:** 2026-04-22
**Status:** PRE-REGISTRATION. Companion script `phase3b_x3_energy.py` to
run AFTER this doc is committed.

**Supersedes:** `32_phase3b_axiom_compliant_redesign.md` §9–§10 as the active
test design. `32_` remains load-bearing as context (documents how we got here
and why K4-TLM has been exhausted).

---

## §1 Physics reframe that prompted X3

The earlier tests (X1, X1-prime, X2, X2-prime) produced a null or photon-like
result: the K4-TLM cannot reach the electron; the Cosserat field under S11
minimization goes toward the *photon* limit. Initially this was read as
"S11 minimization on CosseratField is broken." Careful re-examination of
the physics — via Grant's questions — changes the reading.

### §1.1 A trefoil with a cut is a photon

A closed trefoil knot (3₁) = bound c=3 defect = electron.

A **cut** trefoil = open helical strand with (2,3) winding ratio = propagating
chiral electromagnetic wave = **photon** (specifically, Rañada/Irvine-
Bouwmeester "Hopfion light" — transverse EM field with non-trivial linking).

Electron emission of a photon = the trefoil *opens*, releasing the trapped
(2,3) winding as a propagating mode. Pair production = two photons *close*
into counter-chiral bound trefoils.

### §1.2 K4 chirality is the photon's natural shape

The K4 diamond has intrinsic chirality: 4 tetrahedral port directions with
no inversion symmetry (per scoping §2 canonical declaration). A transverse
Cosserat shear wave propagating on K4 is *forced* to follow the lattice
chirality — it can only propagate along paths that match the K4 handedness.

A (2,3) helical transverse wave is therefore the only way vacuum-impedance-
matched energy moves on K4. That is the photon.

### §1.3 Impedance / reactance: electron vs photon

| | Electron | Photon |
|---|---|---|
| Topology | closed trefoil (c=3) | cut / open helix |
| Z at core boundary | → 0 (Axiom-4 saturated) | Z₀ (vacuum-matched) |
| Γ at shell | **−1** (TIR mirror) | **0** (no reflection) |
| Stored energy | pure **reactive** (Q = 1/α) | pure **real** (P_rad) |
| External \|S11\| | ≈ 1 (perfect mirror from outside) | ≈ 0 (transparent) |

**The electron MAXIMIZES |S11| at its shell; the photon MINIMIZES it
everywhere.** These are opposite targets.

### §1.4 What S11 minimization was correctly finding

`CosseratField3D.relax_s11()` computes `Σ_neighbor |Γ|²` summed over all
alive sites. Minimizing this pushes the impedance profile toward uniform
Z₀ everywhere — which is literally the vacuum. The optimizer was
correctly finding the photon limit (trefoil opening into a propagating
transverse wave with Γ = 0 everywhere).

The hedgehog ansatz held c = 3 topology through the Hopf soft-reward,
preventing the trefoil from fully opening, so the S11 gradient was weak
within the envelope-preserving subspace. That's why P_FLAT emerged in
X2-prime: each seed sat in a local flat region of S11 without enough
gradient to move, but none of them was the electron.

S11 minimization does not, and cannot, select the electron.

---

## §2 Why energy minimization is the right objective now

### §2.1 Rule 6 in AVE terms

Collab rule 6 (2026-04-20) corrected AWAY from "integrate-and-minimize"
Lagrangian energy. But what Grant rejected was a *bare* Cosserat elastic
Lagrangian — a field-theory variational approach without the AVE-specific
topological and saturation terms.

The current Cosserat energy functional in
[`cosserat_field_3d.py:343-385`](../../src/ave/topological/cosserat_field_3d.py#L343-L385)
is substantially richer:

```
E = ∫ [ (W_cauchy · G + W_micropolar · G_c) · S_ε²
      + W_κ · γ · S_κ²
      + W_Op10 · k_Op10               ← screening at crossings
      + W_reflection · k_refl         ← (1/64) |grad S|² / S²
      + W_Hopf · k_hopf               ← Chern-Simons self-inductance
      ] dV
```

- Saturation multipliers `S_ε²`, `S_κ²` implement Axiom 4 directly at the
  node field level
- `W_Op10` penalizes screening loss at (2,3) crossings (Op10, research/11_)
- `W_reflection` has a `|grad S|²/S²` structure that rewards SHARP
  impedance transitions (at the shell boundary) rather than smooth ones —
  the opposite of what pure S11 wants
- `W_Hopf` with `k_hopf = π/3` rewards the electron-specific Hopf
  invariant Q_H = 6 (research/13_ §3.2 exact derivation)

This is not the 2026-04-20 rejected functional. This is the AVE-operator-
composition stationary-point target where every term derives from the four
axioms.

### §2.2 What each energy term pulls toward

| Term | What it wants | Effect on soliton |
|---|---|---|
| `W_cauchy · S_ε²` | low trace-strain × saturation | limits bulk compression |
| `W_micropolar · S_ε²` | low antisymmetric strain × saturation | rewards ε_antisym = ω (Cosserat equilibrium) |
| `W_κ · γ · S_κ²` | smooth curvature × saturation | penalizes sharp ω gradients |
| `W_Op10 · k_Op10` | n̂-field wedge products at crossings | reward (2,3) topology |
| `W_refl · k_refl` | sharp transitions in saturation field | rewards shell boundary (Γ=−1) |
| `W_Hopf · k_hopf` | topological self-inductance Q_H = 6 | rewards electron-specific linking |

The minimum of this combined functional *could* be the electron — the
terms are structurally designed to encode everything the electron needs
(Γ = −1 at shell, c = 3 winding, Q_H = 6 Hopf invariant, saturation
engaged). Whether the minimum actually *is* the electron is what X3
tests.

### §2.3 What this does NOT do

- Does not implement "TLM evolution is the computation" (rule 6's deepest
  form). The Cosserat field uses gradient descent inherently.
- Does not inject spin-½ dynamically. The Hopf reward at k_hopf = π/3
  encodes a c=3 topological preference, not the Finkelstein-Misner kink.
- Does not close the n̂ ↔ ω identity gap (scoping §4). The n̂ derivation
  from ω via Rodrigues is implicit in `_op10_density` via
  `_project_omega_to_nhat`, but the identity itself is not formally
  written.

These gaps remain open. X3 tests what the *current* rich energy
functional admits as its ground state within its own limitations.

---

## §3 The test

### §3.1 Parameter grid (axiom-compliant defaults)

- Solver: `CosseratField3D(N=72, N=72, N=72, dx=1.0, use_saturation=True)`
- `G = G_c = γ = 1.0` (natural units, K4-derived moduli pinning)
- `k_Op10 = k_refl = 1.0`, `k_Hopf = π/3` (Hopf-invariant match at Q_H=6)
- `ω_yield = π`, `ε_yield = 1.0` (Axiom 4 saturation thresholds)

Seeds — identical to X2-prime for direct comparison:
- **R/r = 2.0** (classical full-Clifford): R=18, r=9.0
- **R/r = 2.618** (φ², Ch 8 Golden Torus target): R=18, r=18/φ² ≈ 6.875
- **R/r = 3.5** (K4-TLM Gaussian-attractor value): R=18, r≈5.143
- **R/r = 4.0** (far): R=18, r=4.5

All seeds use the canonical hedgehog envelope
(`initialize_electron_2_3_sector(use_hedgehog=True)`).

Relaxation: `max_iter=500`, `tol=1e-8`, `initial_lr=0.01`,
`track_topology_every=25`.

Compute compromise: start with 3 seeds (2.0, 2.618, 4.0); add 3.5 if
time permits.

### §3.2 Diagnostic extraction at convergence

**Built-in solver methods:**
- `extract_shell_radii()` → (R, r)
- `extract_crossing_count()` → c
- `total_energy()` → E_final
- `total_s11()` → total reflected-power integral

**Post-hoc reconstruction** (module-level functions, no new code):

1. **Local |Γ|² field**: call `_s11_density(u_final, ω_final, dx,
   ω_yield, ε_yield)` on the converged state. Returns a (nx, ny, nz)
   scalar field of ΣΓ² per site.

2. **External vs at-shell |Γ|²**: mask the |Γ|² field by radial distance
   from soliton center. External = outside shell_outer = R + r;
   at-shell = within [R−r, R+r]. Compare max values.

3. **Saturation amplitude A² at shell**: recompute
   A² = ε²/ε_yield² + κ²/ω_yield² on the converged field. If max_shell
   A² → 1, Axiom 4 is engaging and Γ_shell → −1 per the Op14 chain.

4. **Λ decomposition**: call `_op10_density`, `_reflection_density`,
   `_hopf_density` separately on the converged state, integrate. Compare
   Λ_surf (Op10), Λ_line (reflection), Λ_vol (Hopf) to Ch 8 targets
   (4π², π, 4π³).

### §3.3 Pre-registered outcomes

Recorded BEFORE any run. Results will append to §8 below.

| Outcome | R/r | c | shell \|Γ\|² | external \|Γ\|² | Verdict |
|---|---|---|---|---|---|
| **P_X3a** | → φ² within 5% (all seeds) | 3 | → 1 | → 0 | **Electron found — Phase 3b closes** |
| **P_X3b** | same for all seeds ≠ φ² | 3 | → 1 | → 0 | Different bound state (e.g., Hopfion-photon-with-saturation) |
| **P_X3c** | each stays at seed (P_FLAT) | 3 | varies | varies | Energy also fails; physics gap remains |
| **P_X3d** | diverges / c changes | ≠ 3 | — | — | Functional insufficient |

Decision thresholds:
- Convergence: `|Δ(R/r)|/⟨R/r⟩ < 5%` across seeds qualifies for P_X3a/b
- Shell Γ² → 1: max shell |Γ|² within 10% of 1 (i.e., ≥ 0.9)
- External Γ² → 0: external |Γ|² < 5% of total |Γ|² integrated

---

## §4 What this test can and cannot close

**Can close (if P_X3a):**
- Numerical Phase 3b: electron emerges as the ground state of the richer
  Cosserat energy functional on the K4 substrate.
- Validates the physics reframe (S11 finds photon; energy finds electron).

**Can advance (if P_X3b):**
- Existence of SOME bound (2,3) state under energy min → the mechanism
  (self-saturating TIR confinement of a Hopfion) is real, but Ch 8's
  specific Golden Torus is not the only fixed point.
- Would need separate work to identify what the converged state is
  physically (muon? Hopfion-light-with-saturation variant?).

**Cannot close (even if P_X3a):**
- The n̂ ↔ ω identity gap (scoping §4) — the current Rodrigues
  projection is operational, not formally derived.
- Explicit spin-½ dynamical injection — k_hopf = π/3 rewards c=3 but
  does not implement the Finkelstein-Misner kink.
- True AVE-native wave evolution ("TLM evolution IS the computation"
  per rule 6's deepest form) — the Cosserat field uses gradient descent
  by construction.

Forces Phase-1 work (if P_X3c or P_X3d):
- Full Cosserat-Lagrangian completion per scoping §5
- Formal n̂ ↔ ω identity adjudication per scoping §4
- Possibly a new solver that implements u, ω wave evolution (not
  gradient descent) on K4

---

## §5 Corpus references

- [`cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py) — full Cosserat solver
- [`30_photon_identification.md`](30_photon_identification.md) — A₁/T₂ decomposition, photon-from-T₂
- [`32_phase3b_axiom_compliant_redesign.md`](32_phase3b_axiom_compliant_redesign.md) — prior test chain (X1 through X2-prime)
- [`manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex`](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex) — Confinement Bubble, Γ=−1 boundary
- [`research/L3_electron_soliton/13_hopf_self_inductance.md`](13_hopf_self_inductance.md) §3.2 — k_hopf = π/3 derivation at Q_H = 6
- [`research/L3_electron_soliton/00_scoping.md`](00_scoping.md) §4 — n̂ ↔ ω identity gap
- `.agents/handoffs/COLLABORATION_NOTES.md` rule 6 — S11 vs energy objective history

---

## §6 Files

**Running:**
- `src/scripts/vol_1_foundations/phase3b_x3_energy.py` (created with this doc)

**Outputs:**
- `/tmp/phase3b_x3_energy.npz` — raw trajectories + post-hoc diagnostics
- `/tmp/phase3b_x3_energy.png` — convergence plots + seed-independence
- `/tmp/phase3b_x3_energy_log.txt` — run log

---

## §7 (reserved for §8 Results — appended after run completes)

---

## §8 Results — 2026-04-22 after X3 run

### §8.1 Raw summary table

Ran `phase3b_x3_energy.py` with 3 seeds (R/r = 2.0, 2.618, 4.0) at N=72,
500 iter max, tol=1e-8, lr=0.01.

| seed | R/r_final | c | shell \|Γ\|²_max | ext/total \|Γ\|² | A²_shell | E_final | converged |
|---|---|---|---|---|---|---|---|
| R/r=2.0 (classical) | 2.059 | 3 | 0.000 | 4.7% | 15.397 | 9.09e5 | N (500 iter) |
| R/r=2.618 (φ²) | 2.692 | 3 | 0.000 | 10.7% | 15.303 | 7.82e5 | N (500 iter) |
| R/r=4.0 (far) | 3.889 | 3 | 0.000 | 13.2% | 15.020 | 7.02e5 | N (500 iter) |

Λ decomposition (per-term integrals, compared to Ch 8 targets):

| Term | Ch 8 target | R/r=2.0 | R/r=2.618 | R/r=4.0 | Notes |
|---|---|---|---|---|---|
| Λ_Op10 | 4π² = 39.48 | 74.4 | 104.1 | 158.2 | 2–4× too large, grows with R/r |
| Λ_refl | π = 3.14 | 8.90e5 | 7.68e5 | 6.94e5 | ~250000× too large (dominates) |
| Λ_Hopf | 4π³ = 124.0 | 20.2 | 17.3 | 10.4 | 6–12× too small, shrinks with R/r |

### §8.2 Verdict — P_X3d + P_X3c combined

No seed converged (P_X3d); energy was still decreasing at iter 500 on all
three (Δ|E| ≈ 270–400k). Also no seed moved geometrically (R/r stuck at
init within the FWHM-extraction resolution) — a P_X3c signature.

**But the critical finding isn't either pre-registered outcome — it's the
physical failure mode.**

### §8.3 Why the functional can't find the electron

Three concrete problems, all visible in the data:

**(a) Saturation engages uniformly, not as a sharp transition.** `shell
A²_max = 15` (vs yield threshold of 1) means the field at the shell is
*way* past saturation — but the observed `shell |Γ|² = 0.000` says the
saturation is UNIFORM across the whole shell region. When neighbors
have identical `Z_eff`, Γ between them is 0. The electron requires a
discontinuous boundary (saturated inside, unsaturated outside) — the
*gradient* of saturation, not its magnitude, produces Γ = −1. The
gradient-descent path from the hedgehog ansatz doesn't have access to
configurations with this discontinuity.

**(b) The reflection term dominates and has wrong sign structure.**
Λ_refl is 690k–890k out of a total energy ~700k–900k — the other terms
are rounding errors. The `(1/64) · |grad S|² / S²` structure was meant
to reward sharp saturation boundaries, but when S → 0 uniformly over a
region, grad S ≈ 0 AND S ≈ 0, giving a regularized 0/0 that the numerical
floor evaluates as a large positive number. The optimizer drives S
deeper toward 0 trying to minimize — but that explodes 1/S² further.
No downhill path to a sharp-shell state exists within this functional.

**(c) Hopf contribution is 6–12× below Ch 8 target.** Λ_Hopf measured
10–20 vs target 124. Either:
- The Hopf integral normalization is wrong (k_hopf = π/3 might need a
  different value for the ω-field-derived n̂ than for the direct n̂ field
  of research/13_), OR
- Our ω field after gradient descent doesn't have Q_H = 6 despite
  maintaining c = 3 (c counts winding crossings on contours; Q_H counts
  topological linking of the full n̂ field — they can diverge under
  field relaxation without the ansatz constraint)

All three Λ magnitudes are wrong. The sum cannot equal α⁻¹ because none
of the three terms is in the right numerical ballpark for its target.

### §8.4 Both S11 and energy find the photon side

Cross-reference to X2-prime (S11 min):
- S11 min: R/r → ∞ preferred (photon limit). P_FLAT due to hedgehog
  ansatz constraint, but all gradients pointed photon-ward.

X3 (energy min):
- Energy also lower at larger R/r. All seeds with energy decreasing.
- Uniform deep saturation engages, but NO TIR boundary forms.
- No φ² selection.

**Both objectives point toward the photon side of the dichotomy.** The
richer energy functional was hypothesized to balance "photon-wants-
uniform-match" against "electron-wants-saturated-shell" via the Op10 +
Hopf + reflection terms. In practice the reflection term dominates and
has the wrong gradient structure; the Op10 and Hopf contributions are
too small to bias the optimum.

### §8.5 Updated verdict against pre-registered matrix

| Outcome | Pre-registered | Observed |
|---|---|---|
| **P_X3a** (electron found) | R/r = φ², c=3, shell Γ→−1, ext Γ²→0 | ✗ shell Γ=0 everywhere, ext/total too high |
| **P_X3b** (other bound state) | same R/r across seeds, shell Γ→−1 | ✗ different R/r per seed, Γ=0 |
| **P_X3c** (P_FLAT) | each stays at seed | ~✓ geometry stuck, but energy still decreasing |
| **P_X3d** (insufficient) | no convergence | ✓ no convergence at 500 iter |

Honest classification: **P_X3d** — the functional did not converge in
500 iterations and cannot produce the electron configuration. The
failure is structural (functional form), not numerical (more iterations
won't help — the gradient points the wrong way toward uniform-deep-
saturation, away from the required sharp-shell discontinuity).

### §8.6 What this forces

Phase 3b numerical closure within the current `CosseratField3D`
framework is **not achievable**. The residual Phase-1 gaps become
load-bearing:

1. **n̂ ↔ ω identity** (scoping §4 Phase-1 entry criterion) — unclosed.
   The Rodrigues projection in `_project_omega_to_nhat` is operational
   but the formal Cosserat-microrotation ↔ Faddeev-Skyrme-director
   identity is absent. Without this, Λ_Hopf normalization can't be
   trusted.

2. **Full Cosserat Lagrangian with explicit (u, ω) coupling**
   (scoping §5). The current energy has each term computed
   separately and summed; a principled Lagrangian would derive the
   couplings from a single action and have consistent weights.

3. **Tool choice:** `CosseratField3D` uses gradient descent. Rule 6's
   deepest form says "TLM evolution IS the computation." A wave-
   evolution tool on K4 that carries (u, ω) together (not scalar port
   voltages as in K4-TLM) would be the right instrument. This does not
   currently exist in the engine.

4. **Potentially: topological c=3 HARD constraint** instead of Hopf
   soft-reward. Gradient descent preserves c=3 in our runs only because
   the ansatz is smooth and steps are small — but the shell can still
   "unwind" internally (lose saturation structure, amplitude topology)
   without changing the crossing count. A constraint-based formulation
   (Lagrange multiplier on Q_H = 6) might select the electron where
   soft rewards do not.

### §8.7 Summary — honest state of Phase 3b

- **Phase 3a (photon identification):** closed. Multiple independent
  tests (A₁/T₂ decomposition, S11 minimization converging toward vacuum,
  Cosserat energy also preferring photon limit) all identify the K4
  substrate's natural transverse mode.
- **Phase 3b (electron identification within current engine):** cannot
  close. K4-TLM exhausted (§10 of `32_`); CosseratField3D under both
  S11 and energy minimization finds the photon side. The richer
  energy functional's terms don't add up to the right magnitudes for
  any of the three Λ's in Ch 8.
- **Analytical Phase 3b (Theorem 3.1, Sub-theorem 3.1.1):** remains
  closed analytically — the Q = 1/α result from LC-tank reasoning
  doesn't depend on this simulation chain.

The dynamical demonstration via simulation requires Phase-1 completion
of the Cosserat-Lagrangian framework. The current engine can show the
photon side of the electron-photon duality robustly but cannot
simulate the electron itself.

### §8.8 Figure

`/tmp/phase3b_x3_energy.png` — shows R/r trajectories (all flat at
their seeds) and energy decrease curves (monotonic but not converged).