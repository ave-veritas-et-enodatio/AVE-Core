[↑ Ch.18 Universal Vacuum Cell](index.md)
<!-- leaf: verbatim -->

<!-- kb-frontmatter
kind: leaf
claims: [clm-vjv4zf]
-->

<!-- kb-frontmatter
kind: leaf
claims: [clm-vjv4zf]
-->

# SPICE Subcircuit Specification

**Volume:** 4 (Applied Vacuum Engineering)
**Chapter:** 18

## `AVE_VACUUM_CELL` Subcircuit

```spice
.subckt AVE_VACUUM_CELL A B
+ params: L0=1n C0=1p R0=0 V_YLD=43651.85 I_YMAX=124.384

* (a) Metric Varactor — charge-based behavioral source
B_VAR A B Q = {C0 * V(A,B) / sqrt(1 - min((V(A,B)/V_YLD)**2, 0.9999))}

* (b) Relativistic Inductor — small linear L + behavioral correction
L_BASE A N_L {L0}
B_REL_V N_L B V = {L0 * idt(V(A,B)) * (1/sqrt(1 - min((I(L_BASE)/I_YMAX)**2, 0.9999)) - 1) / (L0 + 1e-30)}

* (c) Optional Damping
R_DAMP A B {R0 + 1e-15}

.ends AVE_VACUUM_CELL
```

> **↗ FLAG-2 sector tag (2026-07-03, RESOLVED-BY-EXISTING-RULING; Grant-ratified 2026-06-15, `research/2026-06-15_ceff-epsilon-monotonicity_result.md` Q1=(B)).** The `B_VAR` metric varactor `$C_{eff}=C_0/S$` (divergent) is the **longitudinal-A1 bond compliance** ($1/k_a$), NOT the transverse dielectric permittivity. The ch15/ch17 KB netlists' reciprocal `$C_0\cdot S$` (collapse) form is the **transverse-T2** dielectric permittivity ($C_{diel}\propto S$, the LCR bench capacitance). Orthogonal reactances (A1 ⊥ T2), same EE name — **NOT reciprocal laws of one object**; the SPICE-charter FLAG-2 is this name-collision, resolved by the ratified split. Source: [`nonlinear-vacuum-capacitance.md:14`](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md).

## Numerical Stability Notes

- `min((V/V_YLD)^2, 0.9999)` clamps the ratio below 1.0 to prevent `sqrt` of negative values
- `1e-30` added to denominators to avoid division by zero
- `1e-15` added to R0 to ensure a finite numerical path always exists

## Usage Example

```spice
.INCLUDE ave_vacuum_cell.lib
V_SRC N_IN GND AC 1

* Two-section cascaded transmission line
X1 N_IN N_MID AVE_VACUUM_CELL L0=1nH C0=1pF
X2 N_MID N_OUT AVE_VACUUM_CELL L0=1nH C0=1pF
R_TERM N_OUT GND 50

.AC DEC 1000 1e9 1e15
.END
```

## Linear Variant

```spice
.subckt AVE_VACUUM_CELL_LINEAR A B
+ params: L0=1n C0=1p R0=0

L1 A B {L0}
C1 A B {C0}
R1 A B {R0 + 1e15}

.ends AVE_VACUUM_CELL_LINEAR
```

Any deviation between `AVE_VACUUM_CELL` and `AVE_VACUUM_CELL_LINEAR` runs is due to Axiom 4 saturation effects.

## Level-2 memristor arm (`AVE_VACUUM_CELL_L1`)

```spice
.subckt AVE_MEMRISTOR_S_STATE A B N_S
+ params: TAU_REL=1n V_YLD=43651.85
* dS/dt = (S_eq - S) / TAU_REL; S_eq = sqrt(1 - (V/V_YLD)^2)
.ends AVE_MEMRISTOR_S_STATE
```

`TAU_REL` is **simulation-scaled** (default 1 ns). Canonical vacuum $\tau_{\mathrm{relax}}=\ell_{\mathrm{node}}/c\approx 1.288\times 10^{-21}$ s is below ngspice timestep — constitutive-loop tests use the Python ODE harness with dimensionless $\omega\tau$.

*Implementation*: `src/ave/solvers/spice_models/ave_vacuum_cell.lib`

> **⚠ FLAG-1 value-drift note (2026-07-03, ave-canonical-source).** The `V_YLD` / `I_YMAX` literals in the subckt-param lines above are **hand-written** and were drifted (`43653.7` / `124.4`); corrected here to the `ave.core.constants` canonical `V_YIELD = 43651.851844… V` (`≈ 43651.85`) and `I_MAX = 124.384 A`. These are NOT generated from `constants.py` and will drift again if hand-edited. The **durable fix** is to GENERATE the `.lib` (and this spec) from `constants.py` — SPICE-charter design-(d) (`_orchestration/2026-07-03_spice-lane-charter.md` §2(d): `.lib.template` + substitute-at-test-time + a FORM/VALUE-drift CI gate). Generator not built here; values fixed + warned only.
