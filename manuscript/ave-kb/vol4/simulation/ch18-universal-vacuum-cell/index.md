[↑ Simulation](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-vjv4zf]
subtree-experiments: []
-->

# Ch.18: Universal AVE Vacuum Cell

**Volume:** 4 (Applied Vacuum Engineering)
**Chapter:** 18 (Simulation Architecture)

All domain-specific SPICE models — nuclear decay, molecular bonds, protein folding, hardware thrust — are wiring topologies of a single canonical subcircuit: the `AVE_VACUUM_CELL`.  This cell implements the Axiom 4 saturation kernel $S(V) = \sqrt{1 - (V/V_{yield})^2}$ as ngspice behavioral sources.

## Key Results

| Result | Statement |
|---|---|
| Universal cell | `AVE_VACUUM_CELL` — single subcircuit for all AVE SPICE models |
| Metric Varactor | $Q = C_0 \cdot V / \sqrt{1 - (V/V_{SNAP})^2}$ — Axiom 4, longitudinal-A1 compliance (knee at $V_{SNAP}$; sector-keying fix 2026-07-03) |
| Relativistic Inductor | $\Phi = L_0 \cdot I / \sqrt{1 - (I/I_{YMAX})^2}$ — Axiom 4, magnetic sector |
| TVS Zener | $R_{eff} = 0$ when $\|V\| \ge V_{YLD}$ — dielectric rupture |
| Linear variant | `AVE_VACUUM_CELL_LINEAR` — constant L, C, R for comparison runs |
| EE Bench cell | `AVE_EE_BENCH` — single varactor for DC sweep plateau verification |

## Subcircuit Architecture

### Three Constitutive Models in Parallel

The `AVE_VACUUM_CELL` contains three behavioral elements between nodes A and B:

1. **(a) Metric Varactor** (longitudinal-A1 compliance): Charge-based B-source with $Q = C_0 \cdot V / \sqrt{1 - (V/V_{SNAP})^2}$.  As $V \to V_{SNAP}$, $C_{eff} \to \infty$.  **(Sector-keying fix 2026-07-03: the divergent $C_0/S$ A1 compliance diverges at $V_{SNAP}\approx 511$ kV, not $V_{YLD}$ — `def-vyvsn1`, [`nonlinear-vacuum-capacitance.md:18`](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md); VALUE CHANGE 43.65 kV → 511 kV.)**
   > **↗ FLAG-2 sector tag (2026-07-03, RESOLVED-BY-EXISTING-RULING; Grant-ratified 2026-06-15, `research/2026-06-15_ceff-epsilon-monotonicity_result.md` Q1=(B)).** This diverging `$C_{eff}=C_0/S$` "Metric Varactor" is the **longitudinal-A1 bond compliance** ($1/k_a$, metric-dilatation stretch-reactance) — the "electric sector" label above is the loose EE name. It is **NOT** the transverse dielectric permittivity: the ch15/ch17 KB netlists carry the reciprocal `$C_{eff}=C_0\cdot S$` (collapse) form, which is the **transverse-T2** dielectric permittivity ($\varepsilon_{eff}=\varepsilon_0 S\Rightarrow C_{diel}\propto S$, the LCR-bench capacitance). Orthogonal reactances (A1 ⊥ T2) sharing the name "capacitance" — **NOT reciprocal laws of one object**; the SPICE-charter FLAG-2 "contradiction" is this name-collision, resolved by the ratified split. Canonical source: [`nonlinear-vacuum-capacitance.md:14`](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md).
2. **(b) Relativistic Inductor** (magnetic sector): Flux-based behavioral voltage source with $\Phi = L_0 \cdot I / \sqrt{1 - (I/I_{YMAX})^2}$.  As $I \to I_{YMAX}$, $L_{eff} \to \infty$ and $dI/dt \to 0$ (velocity cannot exceed $c$).
3. **(c) TVS Zener** (optional damping): Linear resistance $R_0$ for material domains; $R_0 = 0$ for free vacuum.
4. **(d) Memristor** (placeholder): $\tau_{relax} \approx 1.29 \times 10^{-21}$ s — below any practical SPICE timestep.

### Parameters (canonical source stated ~~from `ave.core.constants`~~ **PER SYMBOL** — attribution repaired 2026-08-03, see the note below; no value moves)

| Parameter | Value | Origin |
|---|---|---|
| $V_{SNAP}$ | 510,998.95 V | $m_e c^2 / e$ — `ave.core.constants.V_SNAP` |
| $V_{YIELD}$ | 43,651.85 V | $\sqrt{\alpha} \times V_{SNAP}$ (`ave.core.constants.V_YIELD` = 43651.851844… — FLAG-1 fix 2026-07-03; prior 43,653.7 was drifted) |
| $I_{MAX}$ | 124.4 A | $\xi_{topo} \times c$ — **`ave.core.fdtd_3d.I_MAX_MU`, NOT `constants.py`** (see note); the printed `124.4` is a **display rounding** of `124.3840330668883` |
| $Z_0$ | 376.73 Ω | $\sqrt{\mu_0 / \varepsilon_0}$ — `ave.core.constants.Z_0` |

> ⚑ **DEAD-CITE REPAIR (2026-08-03, `imax-mechanical` lane) — naming/attribution only; no value moves and nothing is minted.** The section header above read *"Parameters (from `ave.core.constants`)"* and governed the $I_{MAX}$ row. **`ave.core.constants.I_MAX` DOES NOT EXIST**, and never has. Two-method verified at `origin/main` `66fc7e69`: (A) `hasattr(ave.core.constants, "I_MAX")` returns `False`; (B) `grep -n I_MAX src/ave/core/constants.py` exits `1` (no match). The struck header text is preserved above (Rule 12). The **live** symbol is [`src/ave/core/fdtd_3d.py`](../../../../../src/ave/core/fdtd_3d.py)`:69` — `I_MAX_MU: float = XI_TOPO * C_0  # ≈ 124.384 A — μ-grade circulation threshold` — i.e. **the μ-grade threshold lives in the engine module, not the constants module.** $V_{SNAP}$, $V_{YIELD}$ and $Z_0$ *are* `ave.core.constants` symbols; only the $I_{MAX}$ row was dead. **No `I_MAX` is minted in `constants.py` by this repair, deliberately** — minting one would force the open A4 / `I_max` homonym ruling described next. ★**The `124.4` display rounding is FLAGGED, NOT CHANGED**: it is the same hand-maintained-literal class the FLAG-1 note at [`spice-subcircuit.md`](spice-subcircuit.md):125 names, and moving a number is outside a naming/attribution repair's scope.  <!-- rule12-freeze: base=eb74db9ab0031ca21edc04836089b3477862a9f4 region=above offset=0 lines=47 bytes=4024 sha256=198ff9b6f090df72e0548d38ad035542626e8fc51f445ecb146abd72c5446723 -->
>
> ⚑ **The VALUE it carries sits on an OPEN fork.** `124.384 A` is the **convection** reading of `I_max` ($\xi_{topo}c$; Ax2 TKI evaluated at $v=c$). The corpus uses the same name `I_max` for a **displacement** reading, $V_{yield}/Z_0 = 115.870$ A — the *"FPB slew rating, $I_{max}\simeq116$ A"* ([`operators.md`](../../../common/operators.md):145; same sentence at [`universal-saturation-kernel-catalog.md`](../../../common/universal-saturation-kernel-catalog.md):171). The two differ by **exactly $4\pi\sqrt\alpha = 1.073476$**, i.e. **$+15.2\%$ in the quadratic kernel argument** $(I/I_{max})^2$ *at a fixed numerator convention*. Which reading the $\mu$-grade denominator should carry is **Grant's A4 ruling and is still open** (`research/2026-07-10_operator-typing-pass_result.md`:112, verbatim: *"**Grant's physical ruling — still OPEN.**"*). Three-sense map + hazard box: [`theorem-thesaurus.md`](../../../common/theorem-thesaurus.md) §6, the `I_max` row. **This spec keeps `124.4 A`** — the repair is to the cite, not to the number, and it **rules nothing** on the fork.

### Datasheet device schematic (Vol 9 render)

Vol 9 device-level equivalent circuit and bench protocol: [`vol9/ch3-pin-port-configuration/device-circuit-models.md`](../../../vol9/ch3-pin-port-configuration/device-circuit-models.md) §1 (KB source of truth; PDF figure `fig:vol9_circuit_vacuum_cell`).

### SPICE Netlist Compiler

The `spice_netlist_compiler.py` module translates AVE solver outputs (L, C, R, coupling) into cascaded `AVE_VACUUM_CELL` netlists:

```
Python solver → compile_* → .cir → ngspice → validation
```

Functions:
- `compile_ee_bench_dc_sweep()` — single-cell capacitance plateau test
- `compile_lcr_network()` — generic LCR network, AC or transient
- `compile_amino_acid_network()` — molecular topology from organic mapper
- `write_netlist()` — output to `.cir` file

## Derivations and Detail

| Document | Contents |
|---|---|
| [SPICE Subcircuit Specification](./spice-subcircuit.md) | Full behavioral source equations, numerical stability notes, usage examples |

*Cross-references*:
- `src/ave/solvers/spice_models/ave_vacuum_cell.lib`
- `src/ave/solvers/spice_netlist_compiler.py`
- Backmatter App 6 — SPICE Verification Manual
- [Nonlinear Constitutive Models](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) — varactor, inductor, TVS theory
