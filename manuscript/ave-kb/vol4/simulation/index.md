[↑ Vol 4: Engineering](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-9sujp8, clm-c54kdd, clm-cbwd77, clm-vjv4zf]
subtree-experiments: []
-->

> ⛔ **Bootstrap.** Leaves are canonical; this index, the volume index, and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this subtopic, load [`../claim-quality.md`](../claim-quality.md) (volume scope) and [`../../claim-quality.md`](../../claim-quality.md) (cross-cutting). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.

# Simulation

SPICE circuit simulations that model AVE vacuum phenomena as analog transmission-line transients. Each chapter defines a physical mechanism — particle decay, autoresonant dielectric breakdown, Sagnac inductive drag — and provides a complete, runnable SPICE netlist derived from zero free parameters.

> **🔴 SCOPE-CORRECTION (2026-06-15, zero-parameter register reconciliation; Rule 12 — the description above is preserved unedited).** "Derived from zero free parameters" reads in the **downstream** sense: the netlist component values follow with **zero free parameters *beyond the 3 interlocked calibration inputs* $\{m_e, \alpha, G\}$ + 4 axioms** — they are not parameter-free outputs. Per the keystone register, $\alpha$, $m_e$, and $G$ are *retained inputs* (with $\alpha$ a Class-B named geometric identification, value-scoped echo), not derived values; AVE reduces the SM's $\sim$26 empirical parameters to those 3 inputs. Same correction as the child leaf `ch17-hardware-netlists/index.md`. Canonical scope: `vol1/ch8-alpha-golden-torus.md:11` (manuscript `backmatter/03_geometric_inevitability.tex` Scope-correction 2026-06-14).

## Key Results

| Result | Expression | Source |
|---|---|---|
| Leaky cavity decay | Muon modeled as LC tank at $150\,\text{kV}$ IC; voltage-controlled switch at $V_{yield} = 43.65\,\text{kV}$ triggers $R_{eff} = 50\,\Omega$ dissipation; exponential RC-decay envelope reproduces radioactive half-life | Ch.14 |
| Autoresonant PLL bypass | Fixed-frequency drive detunes from nonlinear vacuum ($C_{eff}(V) = C_0\sqrt{1-(V/V_{yield})^2}$); phase-locked loop tracks shifting resonance, breaching $60\,\text{kV}$ Schwinger limit at fraction of brute-force power | Ch.15 |
| Sagnac inductive drag | Directional inductance $L_{eff} = L_0(1 \pm S_{DRAG})$ on 50-node LC ring reproduces Sagnac arrival-time shift via Lenz's law without Lorentz transformations | Ch.16 |
| EE Bench yield plateau | Behavioral capacitor $Q = C_0\sqrt{1-(V/V_{yield})^2} \cdot V$ swept DC to $45\,\text{kV}$; $C_{eff}/C_0$ deviates $>10\%$ above $\sim 37\,\text{kV}$ | Ch.17 |
| Universal AVE_VACUUM_CELL | Single canonical subcircuit implementing Axiom 4 saturation kernel; all domain models are wiring topologies of this one cell | Ch.18 |

## Derivations and Detail

| Chapter | Contents |
|---|---|
| [Ch.14: Leaky Cavity Particle Decay](ch14-leaky-cavity-particle-decay/index.md) | LC tank model of fermion decay; voltage-controlled switch at $V_{yield}$; complete `leaky_cavity.cir` netlist |
| [Ch.15: Autoresonant Breakdown](ch15-autoresonant-breakdown/index.md) | Nonlinear $\mathcal{M}_A$ lattice detuning; PLL bypass of Schwinger limit; complete `pll_breakdown.cir` netlist |
| [Ch.16: Sagnac Inductive Drag](ch16-sagnac-inductive-drag/index.md) | Rotating LC frame; directional behavioral inductor; complete `sagnac_ring.cir` netlist |
| [Ch.17: Hardware Netlists](ch17-hardware-netlists/index.md) | EE Bench dielectric yield plateau (`ee_bench.cir`). *PONDER-01 cascaded transmission-line thrust model migrated to AVE-PONDER private repo per REPO-ARCH-8 (2026-05-17 night).* |
| [Ch.18: Universal AVE Vacuum Cell](ch18-universal-vacuum-cell/index.md) | Canonical `AVE_VACUUM_CELL` subcircuit; metric varactor + relativistic inductor + TVS; SPICE netlist compiler |

---
