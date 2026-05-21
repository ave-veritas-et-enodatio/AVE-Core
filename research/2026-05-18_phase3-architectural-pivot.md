# Cosserat-Lagrangian Engine Phase 3 Architectural Pivot

**Date**: 2026-05-18
**Trigger**: Grant insight "this is just carrier wave math with 3D crystals"
**Status**: pivoting away from Cosserat-coupled scalar engine to standard Maxwell FDTD with nonlinear ε(V)
**Engine to use**: existing [`src/ave/core/fdtd_3d.py`](../src/ave/core/fdtd_3d.py) (FDTD3DEngine, 505 lines)

## TL;DR

Grant's EE-simplification reframe reveals that Phase 2 (Cosserat-coupled scalar engine) was over-engineering: the Cosserat ω field IS the magnetic B field per Axiom 1 (microrotation DOF = magnetic), so adding a separate Cosserat coupling layer on top of a scalar V engine double-counts B-field physics that Maxwell's equations already do via $\nabla \times \mathbf{E} = -\partial_t \mathbf{B}$. The existing 3D Yee FDTD Maxwell engine at `src/ave/core/fdtd_3d.py` already implements full-vector Maxwell with nonlinear $\varepsilon(V) = \varepsilon_0\sqrt{1-(V/V_{\text{yield}})^2}$ and μ(H) saturation per Axiom 4 — exactly the engine Phase 3 needs.

Phase 2 (a + b) is HISTORICAL RECORD of the wrong-architecture experiment. Phase 2c (gradient coupling) is unnecessary. Phase 3 proceeds with the existing Maxwell FDTD engine.

## AVE → EE translation (per Grant's reframe)

| AVE term | EE/photonics equivalent |
|---|---|
| Substrate ($\mathcal{M}_A$) | 3D photonic crystal with nonlinear $\varepsilon(V)$ |
| K4 lattice | Diamond crystal primitive cell (or isotropic for simplicity) |
| Axiom 4 saturation $C_{\text{eff}} = C_0/\sqrt{1-A^2}$ | Born-Infeld nonlinear permittivity (squared / n=2) |
| Master Equation | Standard EM wave equation in nonlinear dielectric |
| Soliton | Localized cavity mode / photonic-bandgap defect |
| Cavitation bubble | Self-induced bandgap region around the defect |
| Eigencavity | Cavity's natural resonant mode |
| V field (scalar) | E field component (scalar approximation) |
| **Cosserat ω field** | **B field (microrotation DOF IS magnetic per Axiom 1)** |
| **Op14 trading ρ = -0.99** | **Standard E-B cavity oscillation (textbook LC, ρ(E², B²) ≈ -1)** |
| K=2G operating point | Critical-coupling regime for the photonic bandgap |
| Dark wake τ_zx | Cavity's envelope shedding into bulk crystal at $c_0$ |
| Lorentz from saturation kernel | Group velocity dispersion as cavity approaches bandgap edge |
| Cosmic substrate (bulk universe) | Bulk crystal far-field; PML absorption is the proper substitute |
| Machian inertia M = L_drag | Cavity's mutual inductance with the bulk crystal |

## Why Phase 2 was over-engineering

The Cosserat-coupled scalar engine (Phase 2a forward + Phase 2b shared-flux + proposed Phase 2c gradient) was attempting to add a separate Cosserat ω field with explicit V↔ω coupling to a scalar V Master Equation FDTD.

**The architectural problem**: in AVE, the Cosserat ω field IS the B field per Axiom 1 ("3 microrotational DOF → B"). In standard EM, $\mathbf{B}$ is automatically coupled to $\mathbf{E}$ via Maxwell's curl equations. There's no need to add a separate ω field with manual coupling — the B field is already there in any vector EM engine.

The Phase 2 scalar V engine was a SCALAR APPROXIMATION that didn't have B explicit. To recover Op14 trading, I tried to add ω back manually — but the right move is to use the full-vector Maxwell engine that has B from the start.

**Phase 2 result interpretation in EE terms**:
- Phase 2a (forward only): scalar V engine + manual ω with one-way K_eff modulation → no E-B coupling at all → ρ = 0.06 (decoupled)
- Phase 2b (velocity coupling): scalar V engine + manual ω with bidirectional velocity terms → weak fake E-B coupling → ρ = -0.44 (direction-correct, magnitude weak)
- Standard Maxwell FDTD: automatic E-B coupling via curl equations → ρ = -1 textbook (no manual tuning needed)

## What the existing FDTD3DEngine provides

Per [`src/ave/core/fdtd_3d.py`](../src/ave/core/fdtd_3d.py) (505 lines, already built):

- **Full-vector E (Ex, Ey, Ez) and H (Hx, Hy, Hz)** on a Yee staggered grid
- **Standard Maxwell curl equations**: $\partial_t \mathbf{E} = (1/\varepsilon)\nabla \times \mathbf{H}$, $\partial_t \mathbf{H} = -(1/\mu)\nabla \times \mathbf{E}$
- **Per-cell nonlinear $\varepsilon_{\text{eff}}(\mathbf{E}) = \varepsilon_0 \sqrt{1 - (E \cdot dx / V_{\text{yield}})^2}$** (Axiom 4 dielectric)
- **Per-cell nonlinear $\mu_{\text{eff}}(\mathbf{H}) = \mu_0 \sqrt{1 - (B / B_{\text{yield}})^2}$** (Axiom 4 magnetic)
- **Mur 1st-order ABCs** on all six faces (cosmic substrate substitute)
- **Optional CPML** for stronger absorption
- **Linear-only mode** for benchmarking
- **Configurable V_yield = 43.65 kV, B_yield = B_SNAP**

This is exactly the engine the EE-simplified picture requires. No new code needed for the engine itself.

## Phase 3 test plan with FDTD3DEngine

### Phase 3b: ρ(E², B²) ≈ -1 cavity test (textbook validation)

Set up a simple resonant cavity (rectangular box with PEC walls or just a Gaussian seed in a vacuum lattice), drive it with a brief pulse, then let it ring. The cavity's standing wave has E² and B² in quadrature → textbook Pearson ρ ≈ -1.

Test details:
- Lattice: 32³ vacuum (linear regime to start; ε_r = μ_r = 1.0)
- Seed: Gaussian E_z blob at center
- Run for 1000-5000 timesteps
- Probe Σ|E|² and Σ|B|² each step (B = μ_0·H)
- Compute ρ over post-transient window

Expected: ρ ≈ -0.99 (perfect cavity is -1; small deviation from boundary leakage / FDTD discretization). This validates the canonical Op14 measurement is textbook EE physics on Maxwell FDTD.

**Pass criterion**: ρ ≤ -0.9 (strong anti-correlation, near textbook value).

### Phase 3c: moving soliton dark-wake test

Set up a cavity mode (resonant standing wave), give it forward velocity via boundary perturbation or asymmetric drive, watch for:
- Cavitation bubble forming around the moving cavity (self-induced nonlinear bandgap)
- V_neg trailing-edge signature at L/c₀ delay
- Wake power = F·c₀ measured via Poynting flux integral
- Wake propagating outward without reflecting off PML (cosmic substrate substitute)

### Phase 3d: ω_drive RF emission test

For a stationary cavity driven at ω_drive (PONDER analog at 100 MHz scaled to substrate units):
- Modulate the cavity at ω_drive
- Probe far-field at angles around the cavity
- Verify isotropic emission at ω_drive (transverse envelope photon per Grant's cavitation-bubble + transverse-wave picture)
- Total emitted power should match F·c₀ if there's net forward force from the asymmetric drive

## What this does to the prior phase work

| Prior phase | Status | Disposition |
|---|---|---|
| Phase 1 (analytical dark-wake derivation) | DONE | Stands; the F·c₀ wake-power result is correct (textbook EE result, just under different naming) |
| Phase 2a (forward coupling MVP) | FAIL documented | Historical record; demonstrates the scalar+manual-ω architecture is wrong |
| Phase 2b (shared-flux coupling) | PARTIAL documented | Historical record; demonstrates velocity coupling doesn't recover the missing B-field physics |
| Phase 2c (proposed gradient coupling) | CANCELLED | Was attempt to fix a problem that doesn't exist in full Maxwell |
| Phase 3 (this pivot) | IN PROGRESS | Use existing FDTD3DEngine |
| Phase 4 (α-emergence) | Still gated on Q-4 | Independent workstream |

## Discipline lesson

The pre-reg discipline caught the wrong-architecture problem at Phase 2a → 2b → "needs 2c" pattern. Three iterations of failed coupling architecture made the architectural problem visible. Grant's reframe ("just EE on 3D crystals") was the simplification that resolved it.

**Generalized lesson**: when an engineering attempt produces direction-correct-but-magnitude-weak results across multiple iterations, the issue is often that the engine architecture is duplicating physics that's already implicit in a simpler architecture. The fix is architectural simplification, not parameter tuning or coupling refactor.

For AVE-specific work: **before adding any new field to an engine, check whether that field is already implicit via Axiom 1's microrotation = magnetic field correspondence**. The Cosserat-Maxwell duality is canonical; engines built on scalar V + manual ω almost certainly duplicate what vector Maxwell does automatically.

## Cross-references

- Phase 1 derivation: [`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md`](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md)
- Phase 1 full picture: [`2026-05-18_cosserat-lagrangian-engine-full-picture.md`](2026-05-18_cosserat-lagrangian-engine-full-picture.md)
- Phase 2 prereg: [`2026-05-18_cosserat-lagrangian-engine-phase2-prereg.md`](2026-05-18_cosserat-lagrangian-engine-phase2-prereg.md)
- Phase 2a/2b results: [`2026-05-18_phase2-validation-result.md`](2026-05-18_phase2-validation-result.md)
- Engine: [`src/ave/core/fdtd_3d.py`](../src/ave/core/fdtd_3d.py)
- Axiom 1 microrotation = B field: [`manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) INVARIANT-S2 line ~250
- Two-engine architecture A-027: [`manuscript/ave-kb/common/two-engine-architecture-a027.md`](../manuscript/ave-kb/common/two-engine-architecture-a027.md)
