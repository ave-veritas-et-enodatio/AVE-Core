[↑ Ch.17: Hardware Netlists](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-vjv4zf]
-->

## The EE Bench: Dielectric Yield Plateau

The EE Bench (detailed in Book 4) utilizes a $100\,\mu\text{m}$ sub-millimeter vacuum gap driven to $V_{yield} \approx 43.65\,\text{kV}$. The fundamental objective is to measure the asymptotic plateau of the effective capacitance ($C_{eff}$) as the localized metric approaches its absolute structural strain limit.

Standard electromagnetism predicts a perfectly linear capacitance: $C_{meas} = C_0$ at all voltages until catastrophic arc-discharge. The AVE framework predicts a smooth, measurable rolloff governed by Axiom 4:

$$
C_{eff}(V) = C_0 \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}
$$

> **↗ FLAG-2 sector tag (2026-07-03, RESOLVED-BY-EXISTING-RULING; Grant-ratified 2026-06-15, `research/2026-06-15_ceff-epsilon-monotonicity_result.md` Q1=(B)).** This `$C_{eff}=C_0\cdot S$` (**collapse**) form is the **transverse-T2 dielectric permittivity** ($\varepsilon_{eff}=\varepsilon_0 S\Rightarrow C_{diel}=\varepsilon_{eff}A/d\propto S$) — exactly the LCR-bench-measured capacitance this leaf describes. It is the RECIPROCAL of the ch18/`.lib` metric-varactor `$C_0/S$` (**divergent**) — but the two are **NOT** contradictory: `$C_0/S$` is the **longitudinal-A1 bond compliance** (a different, orthogonal reactance; A1 ⊥ T2), not this transverse permittivity. The SPICE-charter FLAG-2 "sign contradiction" is this name-collision between two orthogonal reactances sharing the EE name "capacitance," resolved by the ratified split. Source: [`nonlinear-vacuum-capacitance.md:14`](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md).

This non-linear saturation is detectable with a precision LCR meter well before any spark occurs. The meter reports the small-signal **tangent** capacitance $C_{ss}=dQ/dV=C_0\,(S-A^2/S)$ (with $S\equiv\sqrt{1-(V/V_{yield})^2}$, $A\equiv V/V_{yield}$), which falls faster than the large-signal chord $C_0 S$ of Eq. above ($1-\tfrac32 A^2$ vs $1-\tfrac12 A^2$ to leading order). The measurable **tracking window** — where $C_{ss}$ deviates by more than $10\%$ from the linear baseline — opens near $0.255\,V_{yield}\approx 11.1\,\text{kV}$ and runs up to the **stability boundary** at $V_{yield}/\sqrt2\approx 30.9\,\text{kV}$, where $C_{ss}$ crosses zero. Past $V_{yield}/\sqrt2$ the differential capacitance is **negative** (negative differential capacitance; the series-$R$ static fixed point has eigenvalue $-1/(R\,C_{ss})>0$), so a statically-held bias **cannot be sustained** — a bias-collapse/snap-back onset at the parameter-free fraction $1/\sqrt2$. (The chord $C_0 S$ itself first deviates $10\%$ at $\sqrt{0.19}\,V_{yield}\approx 19.0\,\text{kV}$.) Standard physics predicts no such instability (stable linear response is expected up to arc-discharge), so the collapse onset at $1/\sqrt2$ is the discriminating signature.

## SPICE Netlist: EE Bench Yield Plateau (ee_bench.cir)

The SPICE model evaluates the non-linear capacitance using a behavioral charge equation ($Q = C_{eff} \times V$):

```spice
* EE Bench Dielectric Yield Shift SPICE Model *
* -------------------------------------------- *

* Parameters
.param C0=10pF V_yield=43650

* DC Sweep Source (0 to 45 kV)
V_SWEEP N_GAP GND DC 0

* Non-Linear Vacuum Capacitance
* Q = C_eff * V = C0 * sqrt(1 - (V/V_yield)^2) * V
B1 N_GAP GND Q = {C0 *
+ sqrt(1 - min((V(N_GAP)/V_yield)**2, 0.999))}
+ * V(N_GAP)

* Parasitic series resistance (connector + trace)
R_PAR N_GAP GND 1G

.DC V_SWEEP 0 45000 100
.PROBE I(V_SWEEP)
.END
```

The DC sweep from $0$ to $45\,\text{kV}$ in $100\,\text{V}$ steps produces a charge accumulation curve $Q(V)=C_0\,S(V)\,V$ whose slope is the small-signal **tangent** $dQ/dV=C_0\,(S-A^2/S)$ (the chord $C_0 S$ of Eq. above; the two differ). The tangent departs the linear baseline by more than $10\%$ above $\sim 11.1\,\text{kV}$, rolls to zero at the stability boundary $V_{yield}/\sqrt2\approx 30.9\,\text{kV}$, and is formally **negative** beyond in the constitutive model — though a real statically-biased gap cannot hold bias past that point (negative differential capacitance / bias collapse). Plotting $C_{ss}/C_0$ vs. $V$ up to $\sim 0.7\,V_{yield}$ reveals the characteristic AVE saturation roll-off; the loss of a trackable bias past $1/\sqrt2$ is itself the prediction.

---
