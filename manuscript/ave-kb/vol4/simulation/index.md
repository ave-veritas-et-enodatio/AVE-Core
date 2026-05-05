[↑ Vol 4: Engineering](../index.md)
<!-- claim-quality (subtree): 9sujp8, c54kdd, vjv4zf -->

> ⛔ **Bootstrap.** Leaves are canonical; this index, the volume index, and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this subtopic, load [`../claim-quality.md`](../claim-quality.md) (volume scope) and [`../../claim-quality.md`](../../claim-quality.md) (cross-cutting). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.

# Simulation

SPICE circuit simulations that model AVE vacuum phenomena as analog transmission-line transients. Each chapter defines a physical mechanism — particle decay, autoresonant dielectric breakdown, Sagnac inductive drag — and provides a complete, runnable SPICE netlist derived from zero free parameters.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Leaky cavity decay | Muon modeled as LC tank at $150\,\text{kV}$ IC; voltage-controlled switch at $V_{yield} = 43.65\,\text{kV}$ triggers $R_{eff} = 50\,\Omega$ dissipation; exponential RC-decay envelope reproduces radioactive half-life | Ch.14 |
| Autoresonant PLL bypass | Fixed-frequency drive detunes from nonlinear vacuum ($C_{eff}(V) = C_0\sqrt{1-(V/V_{yield})^2}$); phase-locked loop tracks shifting resonance, breaching $60\,\text{kV}$ Schwinger limit at fraction of brute-force power | Ch.15 |
| Sagnac inductive drag | Directional inductance $L_{eff} = L_0(1 \pm S_{DRAG})$ on 50-node LC ring reproduces Sagnac arrival-time shift via Lenz's law without Lorentz transformations | Ch.16 |
| EE Bench yield plateau | Behavioral capacitor $Q = C_0\sqrt{1-(V/V_{yield})^2} \cdot V$ swept DC to $45\,\text{kV}$; $C_{eff}/C_0$ deviates $>10\%$ above $\sim 37\,\text{kV}$ | Ch.17 |
| PONDER-01 cascaded stack | 20-layer alternating Air/FR4 LC ladder ($Z_0 = 376.7\,\Omega$, $Z_{FR4} = 181.6\,\Omega$); $\Gamma = -0.349$ per boundary; asymmetric $\nabla\lvert E\rvert^2$ generates ponderomotive thrust | Ch.17 |
| Universal AVE_VACUUM_CELL | Single canonical subcircuit implementing Axiom 4 saturation kernel; all domain models are wiring topologies of this one cell | Ch.18 |

## Derivations and Detail

| Chapter | Contents |
|---|---|
| [Ch.14: Leaky Cavity Particle Decay](ch14-leaky-cavity-particle-decay/index.md) | LC tank model of fermion decay; voltage-controlled switch at $V_{yield}$; complete `leaky_cavity.cir` netlist |
| [Ch.15: Autoresonant Breakdown](ch15-autoresonant-breakdown/index.md) | Nonlinear $\mathcal{M}_A$ lattice detuning; PLL bypass of Schwinger limit; complete `pll_breakdown.cir` netlist |
| [Ch.16: Sagnac Inductive Drag](ch16-sagnac-inductive-drag/index.md) | Rotating LC frame; directional behavioral inductor; complete `sagnac_ring.cir` netlist |
| [Ch.17: Hardware Netlists](ch17-hardware-netlists/index.md) | EE Bench dielectric yield plateau (`ee_bench.cir`); PONDER-01 cascaded transmission-line thrust model (`ponder_01_stack.cir`) |
| [Ch.18: Universal AVE Vacuum Cell](ch18-universal-vacuum-cell/index.md) | Canonical `AVE_VACUUM_CELL` subcircuit; metric varactor + relativistic inductor + TVS; SPICE netlist compiler |

---
