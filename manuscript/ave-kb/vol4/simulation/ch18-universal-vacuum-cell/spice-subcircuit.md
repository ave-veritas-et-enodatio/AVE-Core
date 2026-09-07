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

> **✅ NGSPICE-LIVE STATUS (2026-07-04, PR #513 — the validate-on-known ladder passes 5/5).**
> The canonical `.lib` (`src/ave/solvers/spice_models/ave_vacuum_cell.lib`) and this spec had
> **never been parsed by a SPICE engine** — the lane was emit-only (charter §1). ngspice-46 is
> now installed and the five-rung validation ladder ran live and **PASSES 5/5** (HALT-gate never
> tripped): rung-1 RC/LC analytic transients; rung-2 the Ax4 kernel `S(V)=√(1−(V/V_x)²)` in BOTH
> orthogonal sectors (A1-divergent `C₀/S` keyed **V_SNAP**, T2-collapse `C₀·S` keyed **V_YIELD**,
> both to ~1e-7 vs `ave.axioms.scale_invariant.saturation_factor`); rung-3 Poisson `.OP` ==
> numpy MNA == graph-Laplacian (4.17e-10 V); rung-4 the 1D LC-chain band `ω(k)=2ω₀|sin(ka/2)|`
> (sub-percent median); rung-5 the first live **bias-couples-to-wave** DC→AC measurement
> (`C_eff=C₀/S³`, shift tracks S(A)). Class INFRASTRUCTURE / consistency+manifestation — no
> physics chord/echo minted; `mass = A1` untouched. Full ladder + provenance:
> `research/2026-07-04_spice-phase1-ladder_result.md`.
>
> **Three ngspice-46 `.lib` syntax bugs were caught + fixed at first live parse** (mechanical
> corrections, physics expressions preserved verbatim — no physics adjudication): (1) a bare
> standalone `IC=1` line parsed as a phantom element → folded onto the cap line `C_S N_S 0 1 IC=1`;
> (2) the charge behavioral source `B..Q={expr}` is unsupported → converted to the native charge
> element `C..Q={expr}` (`B_VAR`→`C_VAR`; sector keying A1↔V_SNAP / T2↔V_YLD UNCHANGED); (3) the
> relativistic inductor's `idt()` (time-integral) is unsupported → replaced with the native flux
> element `L_REL A B Flux={L0·i(L_REL)/S(I)}` (physics unchanged). The full nonlinear composite
> cell + the L2 memristor-relaxation arm PARSE cleanly but do NOT converge a full nonlinear
> `.TRAN` in ngspice-46 (near-short `R_DAMP`, self-referential flux inductor) — a genuine
> composite-design numerical limitation, `xfail`'d not papered over; the kernel itself (rung-2)
> is validated via the isolated per-point `.op` path.

## `AVE_VACUUM_CELL` Subcircuit

```spice
.subckt AVE_VACUUM_CELL A B
+ params: L0=1n C0=1p R0=0 V_SNAP=510998.95 V_YLD=43651.85 I_YMAX=124.384

* (a) Metric Varactor — charge-based behavioral source (A1 compliance, knee at V_SNAP)
B_VAR A B Q = {C0 * V(A,B) / sqrt(1 - min((V(A,B)/V_SNAP)**2, 0.9999))}

* (b) Relativistic Inductor — small linear L + behavioral correction
L_BASE A N_L {L0}
B_REL_V N_L B V = {L0 * idt(V(A,B)) * (1/sqrt(1 - min((I(L_BASE)/I_YMAX)**2, 0.9999)) - 1) / (L0 + 1e-30)}

* (c) Optional Damping
R_DAMP A B {R0 + 1e-15}

.ends AVE_VACUUM_CELL
```

> **⚠ SECTOR-KEYING FIX (2026-07-03, follow-up batch; VALUE CHANGE).** The metric
> varactor `B_VAR` is now keyed on **`V_SNAP` (≈ 511 kV)**, not `V_YLD` (≈ 43.65 kV).
> Per the Grant-ratified grade-fork (2026-06-30, `def-vyvsn1`,
> [`nonlinear-vacuum-capacitance.md:18`](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md))
> the **divergent `C₀/S` metric varactor is the longitudinal-A1 bond compliance**,
> which diverges at `V_SNAP = m_e c²/e`, *not* at the transverse-T2 yield wall
> `V_YLD`. The prior keying was a mis-scoping by the factor `1/√α ≈ 11.7`. **This
> CHANGES the divergence voltage of the A1 varactor from 43.65 kV to 511 kV.** The
> `V_YLD` parameter remains the yield/rupture threshold for the TVS Zener and the
> thixotropic memristor `S_eq` (the transverse-T2 yield wall — those stay on `V_YLD`).

> **↗ FLAG-2 sector tag (2026-07-03, RESOLVED-BY-EXISTING-RULING; Grant-ratified 2026-06-15, `research/2026-06-15_ceff-epsilon-monotonicity_result.md` Q1=(B)).** The `B_VAR` metric varactor `$C_{eff}=C_0/S$` (divergent) is the **longitudinal-A1 bond compliance** ($1/k_a$), NOT the transverse dielectric permittivity. The ch15/ch17 KB netlists' reciprocal `$C_0\cdot S$` (collapse) form is the **transverse-T2** dielectric permittivity ($C_{diel}\propto S$, the LCR bench capacitance). Orthogonal reactances (A1 ⊥ T2), same EE name — **NOT reciprocal laws of one object**; the SPICE-charter FLAG-2 is this name-collision, resolved by the ratified split. Source: [`nonlinear-vacuum-capacitance.md:14`](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md).

## Numerical Stability Notes

- `min((V/V_SNAP)^2, 0.9999)` (A1 metric varactor) / `min((V/V_YLD)^2, 0.9999)` (T2 memristor `S_eq`) clamps the ratio below 1.0 to prevent `sqrt` of negative values
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

> **⚠ FLAG-1 value-drift note (2026-07-03, ave-canonical-source).** The `V_YLD` / `I_YMAX` literals in the subckt-param lines above are **hand-written** and were drifted (`43653.7` / `124.4`); corrected here to the ~~`ave.core.constants` canonical `V_YIELD = 43651.851844… V` (`≈ 43651.85`) and `I_MAX = 124.384 A`~~ **canonical `ave.core.constants.V_YIELD = 43651.851844… V` (`≈ 43651.85`) and `ave.core.fdtd_3d.I_MAX_MU = 124.384 A`** *(attribution repaired 2026-08-03 — see the dead-cite note below; the VALUES are unchanged)*. These are NOT generated from their source modules and will drift again if hand-edited. The **durable fix** is to GENERATE the `.lib` (and this spec) from those modules — SPICE-charter design-(d) (`_orchestration/2026-07-03_spice-lane-charter.md` §2(d): `.lib.template` + substitute-at-test-time + a FORM/VALUE-drift CI gate). Generator not built here; values fixed + warned only.

> ⚑ **DEAD-CITE REPAIR (2026-08-03, `imax-mechanical` lane) — naming/attribution only, no value moves and nothing is minted.** The FLAG-1 note above attributed `I_MAX = 124.384 A` to `ave.core.constants`. **`ave.core.constants.I_MAX` DOES NOT EXIST**, and never has. Two-method verified at `origin/main` `66fc7e69`: (A) `hasattr(ave.core.constants, "I_MAX")` returns `False`; (B) `grep -n I_MAX src/ave/core/constants.py` exits `1` (no match). The struck clause is preserved verbatim above (Rule 12). The **live** symbol is [`src/ave/core/fdtd_3d.py`](../../../../../src/ave/core/fdtd_3d.py)`:69` — `I_MAX_MU: float = XI_TOPO * C_0  # ≈ 124.384 A — μ-grade circulation threshold` — i.e. **the μ-grade threshold lives in the engine module, not the constants module.** `V_YIELD` and `V_SNAP` *are* `ave.core.constants` symbols; only the `I_MAX` row was dead. **No `I_MAX` is minted in `constants.py` by this repair, deliberately** — minting one would force the open A4 / `I_max` homonym ruling described next.  <!-- rule12-freeze: base=99994c97857cc8e9a825339f754763777d71789e region=above offset=0 lines=126 bytes=6994 sha256=478918fd43c76e088d9ff2069107dc9389fa41aa0b734fd2913cbe4ee901f256 -->
>
> ⚑ **The VALUE it carries sits on an OPEN fork.** `124.384 A` is the **convection** reading of `I_max` ($\xi_{topo}c$; Ax2 TKI evaluated at $v=c$). The corpus uses the same name `I_max` for a **displacement** reading, $V_{yield}/Z_0 = 115.870$ A — the *"FPB slew rating, $I_{max}\simeq116$ A"* ([`operators.md`](../../../common/operators.md):145; same sentence at [`universal-saturation-kernel-catalog.md`](../../../common/universal-saturation-kernel-catalog.md):171). The two differ by **exactly $4\pi\sqrt\alpha = 1.073476$**, which is **$+15.2\%$ in the quadratic kernel argument** $(I/I_{max})^2$. Which reading the $\mu$-grade denominator should carry is **Grant's A4 ruling and is still open** (`research/2026-07-10_operator-typing-pass_result.md`:112, verbatim: *"**Grant's physical ruling — still OPEN.**"*). Three-sense map + hazard box: [`theorem-thesaurus.md`](../../../common/theorem-thesaurus.md) §6, the `I_max` row. **This spec keeps `124.384 A`** — the repair is to the cite, not to the number, and it **rules nothing** on the fork.
