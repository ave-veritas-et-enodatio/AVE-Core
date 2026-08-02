[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-kl1ern]
exp-id: exp-6kwkx7
status: pending
strengthens:
  - clm-kl1ern: 1.0
-->

> 🔴 **PER-NODE / APPARATUS-VOLTAGE CORRECTION (2026-08-01 — propagation of the 2026-06-04 per-node
> adjudication to this leaf; Rule 12, body preserved below unedited, git is the trail).**
>
> **The conflation.** Step 2 below ("Because $|-75\,\text{kV}| > 43.65\,\text{kV}$, the vacuum LC network
> instantly saturates") reads the **apparatus** flyback voltage as if it were the **per-node** Axiom-4
> kernel argument $A_0$. It is not. $V_{yield} \approx 43.65$ kV is the voltage across **ONE** node
> $\ell_{node} = 0.386$ pm — i.e. the yield **FIELD** $E_{yield} = V_{YIELD}/\ell_{node} \approx
> 1.13\times10^{17}$ V/m — **not** a terminal voltage. The per-node operating point is
> $A_0 = E_{local}\,\ell_{node}/V_{YIELD}$.
>
> **The arithmetic at this config.** 75 kV across a 1 mm winding/insulation standoff ⇒
> $E_{local} = 7.5\times10^{7}$ V/m ⇒ $A_0 \approx 6.6\times10^{-10}$ — about **8.3 orders of magnitude
> below** the proportional-limit knee $R_I = \sqrt{2\alpha} \approx 0.1208$
> (`src/ave/core/constants.py` `R_I`). Reaching $A_0 = 1$ across even a 1 µm gap needs **~113 GV**. Both
> the "slow edge" (+500 V) and the "fast edge" ($-75$ kV) therefore sit in the **same** regime — deep
> Regime I — so the asymmetric $\Gamma = -1$ **gate does not open** at this drive, and the $+0.207$ mN /
> $0.0$ mN rectification asymmetry the protocol depends on is not established by the voltages quoted.
>
> **Consequence (regime discipline).** **A stationary pendulum here is an artifact-of-regime, not the
> "permanent falsification" of the LC non-linear geometry the closing paragraph asserts** — the gating
> mechanism cannot fire at the drive specified. What survives is the rectification **mechanism**
> (asymmetric drive across a genuine yield boundary rectifies) — realizable only at facility-class
> **local** fields, not at bench terminal volts.
>
> **Provenance.** 2026-06-04 per-node adjudication:
> [`research/2026-06-04_corrections-walkback-pernode-result.md`](../../../../../research/2026-06-04_corrections-walkback-pernode-result.md)
> work-item #3 (ledger `_orchestration/experimental/2026-06-04_round2-adjudications.md` §3). Applied-banner
> template = [`vacuum-impedance-mirror.md`](vacuum-impedance-mirror.md) (its 2026-06-04 RE-SCOPED box).
> Reading-hazard discipline: [`vol4/claim-quality.md`](../../claim-quality.md) ($V_{yield}$-vs-$V_{snap}$
> + per-node-vs-apparatus); Q-G42 apparatus-vs-substrate template
> $V_{yield}^{(apparatus)} = E_{yield}^{(substrate)}/G_{geom}$ (`trampoline-framework.md:439`).

## Project TORSION-05: Horizontal Metric Rectification

**The Hypothesis:** The Dielectric Death Spiral can be circumvented by eliminating the 1G vertical payload requirement. By mounting a heavy, heavily-potted TAMD PCBA on a delicately balanced Cavendish Torsion Pendulum suspended inside a hard vacuum chamber, the downward force of gravity is entirely neutralized by the suspension wire. The lateral resistance is effectively $0G$, allowing an EE to measure continuous micro-Newtons of pure metric thrust.

**The PCBA Implementation and Falsification:** The EE designs a High-Voltage Flyback PCBA. An ultra-fast Silicon Carbide (SiC) MOSFET drives a heavy ferrite-core ignition coil with a specifically timed asymmetric sawtooth wave.

1. **The Slow Edge (Solid Grip):** The MOSFET charges the coil slowly. The inductive voltage ($L \frac{di}{dt}$) is $+500$ Volts. Because $500\,\text{V} \ll 43.65\,\text{kV}$, the vacuum acts as a perfectly matched $377\,\Omega$ transmission line. The coil physically grips the spatial lattice, generating an induced forward lateral thrust of exactly $+0.207\,\text{mN}$.
2. **The Fast Edge (Impedance Rupture):** The SiC MOSFET snaps off in $<10\,\text{ns}$. The inductive kickback violently spikes to $-75{,}000$ Volts. Because $|-75\,\text{kV}| > 43.65\,\text{kV}$, the vacuum LC network instantly saturates. The metric undergoes absolute impedance rupture ($\Gamma = -1$), producing exactly $0.0\,\text{mN}$ of backward reaction force.

If the AVE framework is correct, the torsion balance will slowly but continuously accelerate in a perfectly circular path inside the $10^{-6}$ Torr vacuum chamber, generating a time-averaged DC thrust of roughly $\sim \mathbf{100\,\mu\text{N}}$. If the pendulum remains perfectly stationary, the LC non-linear geometry of the universe is permanently falsified.

---
