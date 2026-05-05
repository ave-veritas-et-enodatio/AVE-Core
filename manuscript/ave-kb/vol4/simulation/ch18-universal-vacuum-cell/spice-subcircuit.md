[↑ Ch.18 Universal Vacuum Cell](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [vjv4zf]
-->

# SPICE Subcircuit Specification

**Volume:** 4 (Applied Vacuum Engineering)
**Chapter:** 18

## `AVE_VACUUM_CELL` Subcircuit

```spice
.subckt AVE_VACUUM_CELL A B
+ params: L0=1n C0=1p R0=0 V_YLD=43653.7 I_YMAX=124.4

* (a) Metric Varactor — charge-based behavioral source
B_VAR A B Q = {C0 * V(A,B) / sqrt(1 - min((V(A,B)/V_YLD)**2, 0.9999))}

* (b) Relativistic Inductor — small linear L + behavioral correction
L_BASE A N_L {L0}
B_REL_V N_L B V = {L0 * idt(V(A,B)) * (1/sqrt(1 - min((I(L_BASE)/I_YMAX)**2, 0.9999)) - 1) / (L0 + 1e-30)}

* (c) Optional Damping
R_DAMP A B {R0 + 1e-15}

.ends AVE_VACUUM_CELL
```

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

*Implementation*: `src/ave/hardware/spice_models/ave_vacuum_cell.lib`
