[↑ Ch.15: Autoresonant Breakdown](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-9sujp8]
-->

## SPICE Netlist: Autoresonance (pll_breakdown.cir)

```spice
* Autoresonant PLL (Schwinger Limit) SPICE Model *
* ---------------------------------------------- *

* Parameters
.param L0=1mH C0=1nF V_yield=60000 Drive_Amp=80uA

* The Shifting Vacuum Capacitance (Behavioral Equation)
* C_eff = C0 * sqrt(1 - (V/V_yield)^2)
* Implemented in SPICE via behavioral charge equation Q = C*V
B1 N_VAC GND Q = {C0 * sqrt(1 - min((V(N_VAC)/V_yield)**2, 0.999))} * V(N_VAC)
L1 N_VAC GND {L0}

* The Autoresonant PLL Driver (Behavioral Current Source)
* I = Amp * cos( INTEGRAL( 1/sqrt(L*C_eff) dt ) )
* An integrator sub-circuit is used to track the phase angle (theta)
B_FREQ N_FREQ GND V = 1 / sqrt({L0} * {C0 * sqrt(1 - min((V(N_VAC)/V_yield)**2, 0.999))})
C_INT N_FREQ GND 1  ; Integrates frequency into phase
R_INT N_FREQ GND 1G ; Parasitic drain

* Output to Vacuum
B_DRIVE 0 N_VAC I = {Drive_Amp} * cos(V(N_FREQ))

.TRAN 10ns 200us
.END
```

> **↗ FLAG-2 sector tag (2026-07-03, RESOLVED-BY-EXISTING-RULING; Grant-ratified 2026-06-15, `research/2026-06-15_ceff-epsilon-monotonicity_result.md` Q1=(B)).** The "Shifting Vacuum Capacitance" `$C_{eff}=C_0\cdot\sqrt{1-(V/V_{yield})^2}=C_0\cdot S$` (**collapse**) form above is the **transverse-T2 dielectric permittivity** ($\varepsilon_{eff}=\varepsilon_0 S\Rightarrow C_{diel}\propto S$), matching the ch17 EE-bench leaf. It is the RECIPROCAL of the ch18/`.lib` metric-varactor `$C_0/S$` (**divergent**), but the two are **NOT** contradictory: `$C_0/S$` is the **longitudinal-A1 bond compliance** (orthogonal reactance, A1 ⊥ T2). The SPICE-charter FLAG-2 "sign contradiction" is this name-collision, resolved by the ratified split. Source: [`nonlinear-vacuum-capacitance.md:14`](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md).

---
