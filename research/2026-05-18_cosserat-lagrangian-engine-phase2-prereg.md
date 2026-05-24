# Cosserat-Lagrangian Engine Phase 2 Pre-Registration

**Date**: 2026-05-18
**Target**: minimum-viable Cosserat-Master-Equation-FDTD coupling that reproduces Op14 bond-pair trading signature (Pearson ρ = -0.990) on a coupled engine.
**Parent docs**: [`2026-05-18_cosserat-lagrangian-engine-full-picture.md`](2026-05-18_cosserat-lagrangian-engine-full-picture.md), [`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md`](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md)

## Pre-registration

**Derivation target**: build a minimum-viable Cosserat-coupled extension of [`master_equation_fdtd.py`](../src/ave/core/master_equation_fdtd.py) that reproduces the Op14 bond-pair cross-sector trading signature (Pearson $\rho(H_{\text{cos}}, \Sigma|\Phi_{\text{link}}|^2) \approx -0.99$, per [op14-cross-sector-trading.md:13](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md:13)) on a single-bond-pair test geometry.

**Scope**:
- ADD scalar Cosserat microrotation field $\omega(\vec{r}, t)$ alongside existing scalar V field
- ADD Op14 coupling via $Z_{\text{eff}}(V) = Z_0/\sqrt{S(V)}$ modulating the Cosserat wave equation moduli
- LIMIT to 1-component ω (scalar; full 3-vector Cosserat deferred to Phase 2b)
- LIMIT to bond-pair geometry test (single-soliton Phase 3)
- DEFER full Cosserat micropolar tensor (μ, κ, γ all V-modulated) to Phase 2b

**Corpus state** (per Phase 1 corpus-grep):
- Master Equation FDTD scalar engine: CANONICAL, validated v14 Mode I PASS 4/4 ([breathing-soliton-v14-mode-i.md](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md))
- Cosserat field standalone: VALIDATED at [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py) with factor-of-4 mass-gap per A-008; energy-functional + gradient-descent (NOT wave-equation timestepping)
- Op14 bond-pair Pearson ρ = -0.990: VALIDATED at [op14-cross-sector-trading.md:7](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md:7)
- Cosserat-coupled Master Equation FDTD: EXPLICITLY DEFERRED per [breathing-soliton-v14-mode-i.md:108](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md:108) ("Cosserat re-coupling on Master Equation FDTD ... Deferred; not blocking v14 closure")

**Implementation approach**: minimum-viable coupled engine `CosseratMasterEquationFDTD` (new class, new module) that:

1. Carries V(r,t) state (per existing MasterEquationFDTD)
2. Adds ω(r,t) state (scalar Cosserat microrotation)
3. Couples ω-wave-equation moduli to V via $K_\omega(V) = K_{\omega,0}/S(V)$ (Op14 mechanism)
4. Optional V back-coupling deferred to Phase 2b (test Cosserat-only forward-coupling first)

**Cosserat wave equation** (1-component, simplified Eringen micropolar):
$$I_\omega \frac{\partial^2 \omega}{\partial t^2} = \frac{K_{\omega,0}}{S(V)} \nabla^2 \omega - 2 \kappa_0 \omega$$

where:
- $I_\omega$ = Cosserat microinertia (natural units: 1)
- $K_{\omega,0}$ = Cosserat rotational stiffness baseline (natural units: 1)
- $\kappa_0$ = Cosserat-K4 coupling strength baseline (natural units: 0.1, sub-dominant)
- $S(V) = \sqrt{1 - (V/V_{\text{yield}})^2}$ from Axiom 4

As V drives S → 0 (saturation), Cosserat moduli $K_\omega/S(V) \to \infty$, freezing ω locally (∇²ω → 0). This is the substrate-native back-EMF mechanism.

**Observables to track**:
- $H_{\text{cos}}(t) = \frac{1}{2}\int I_\omega \omega^2 + K_\omega(V) |\nabla\omega|^2 \, d^3r$ (Cosserat total energy)
- $\Sigma|\Phi_{\text{link}}|^2(t) \propto \int V^2 \, d^3r$ (K4-inductive proxy via V field)
- $H_{\text{total}}(t) = H_{\text{cos}} + H_{\text{K4-inductive}}$ (should be approx conserved)

**Test geometry**: 2-node 1D bond-pair (or 32³ FDTD lattice with localized seed at 2 adjacent nodes). Run 5000 timesteps (~5 Compton periods). Probe $H_{\text{cos}}(t)$ and $\Sigma|\Phi_{\text{link}}|^2(t)$. Compute Pearson correlation.

## Predictions

**Pearson ρ between $H_{\text{cos}}$ and $\Sigma|\Phi_{\text{link}}|^2$**:

- **Outcome A (most likely): $\rho \approx -0.99$.** Coupling reproduces bond-pair Op14 signature. Phase 2 succeeds. Engine ready for Phase 3 (dark-wake numerical verification).
- **Outcome B (alternative): $-0.7 < \rho < -0.99$.** Partial trade efficiency. Possible causes: (a) simplified 1-component ω misses cross-coupling terms; (b) coupling mechanism needs to be more direct (energy-flux source term rather than modulus modulation); (c) test geometry doesn't isolate trading. Diagnostic: examine FFT for trading frequency $\omega_{\text{trade}} \approx 0.020$ — if present at correct frequency, mechanism is right but efficiency is degraded; if absent, mechanism is wrong.
- **Outcome C (null): $\rho > -0.5$ or $\rho > 0$.** No anti-correlation. Mechanism is wrong. Diagnostic: check (i) S(V) sign convention matches canonical Vol 1 Ch 4, (ii) Cosserat ω is actually responding to V dynamics, (iii) bond-pair geometry properly isolates the two sectors.

**v14 Mode I breathing-soliton test on coupled engine**:

- **Expected**: still PASS 4/4 criteria. Cosserat coupling should not destabilize the V-side breathing soliton (V dynamics are independent of ω in this MVP).
- **Falsifier**: if breathing soliton destabilizes (FWHM drift or Vpeak decay > 5%), the V→ω coupling is leaking energy out of V dynamics → needs explicit back-coupling implementation.

## Discriminating outcomes

- **Pass**: ρ ≤ -0.95 AND v14 Mode I PASS on coupled engine → Phase 2 closed, proceed to Phase 3 (dark-wake numerical verification).
- **Partial**: -0.95 < ρ ≤ -0.7 → diagnose mechanism, refactor coupling, retry. Document the gap.
- **Fail**: ρ > -0.7 OR v14 Mode I FAIL → Phase 2 mechanism is wrong. Rethink coupling architecture.

## Falsifiers

1. **Cosserat ω does not respond to V dynamics at all** → coupling not wired up; structural bug
2. **ρ goes POSITIVE** (Cosserat energy gains when V gains, not loses) → sign convention bug in coupling direction
3. **FFT shows trading at wrong frequency** (not ~0.020 rad/substrate-fundamental-unit) → mechanism captures qualitative coupling but quantitative scaling is wrong
4. **v14 Mode I destabilizes** → V dynamics being perturbed by Cosserat back-action (which shouldn't exist in MVP)

## Why

The dark-wake τ_zx derivation (Phase 1, [2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md)) used Op14 ρ = -0.990 as a load-bearing assumption to scale from bond-pair to soliton-scale. **Phase 2 validates that the Op14 mechanism actually works on a coupled engine** before Phase 3 uses it for soliton-scale wake predictions.

If Phase 2 fails, the dark-wake τ_zx derivation needs to be revisited with a different scaling argument.

If Phase 2 succeeds, Phase 3 (single-soliton wake test) is straightforward: inject moving soliton, probe trailing-edge (V_neg, ω-related τ_zx_pos) coupled pulse propagating backward at $c_0$.

## Falsifier discipline (per `ave-prereg` Step 4)

Pre-reg committed BEFORE running the validation script. Result of validation will be logged to `research/2026-05-18_phase2-validation-result.md` regardless of outcome (pass, partial, fail).
