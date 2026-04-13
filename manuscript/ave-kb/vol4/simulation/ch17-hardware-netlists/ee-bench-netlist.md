[↑ Ch.17: Hardware Netlists](../index.md)
<!-- leaf: verbatim -->

## The EE Bench: Dielectric Yield Plateau

The EE Bench (detailed in Book 4) utilizes a $100\,\mu\text{m}$ sub-millimeter vacuum gap driven to $V_{yield} \approx 43.65\,\text{kV}$. The fundamental objective is to measure the asymptotic plateau of the effective capacitance ($C_{eff}$) as the localized metric approaches its absolute structural strain limit.

Standard electromagnetism predicts a perfectly linear capacitance: $C_{meas} = C_0$ at all voltages until catastrophic arc-discharge. The AVE framework predicts a smooth, measurable rolloff governed by Axiom 4:

$$
C_{eff}(V) = C_0 \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}
$$

This non-linear saturation is detectable with a precision LCR meter well before any spark occurs. The "Anomaly Window" (approximately $0.85 \times V_{yield}$ to $V_{yield}$) represents the measurable regime where $C_{eff}$ deviates by more than $10\%$ from the linear baseline.

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

The DC sweep from $0$ to $45\,\text{kV}$ in $100\,\text{V}$ steps produces a charge accumulation curve $Q(V)$ whose slope ($dQ/dV = C_{eff}$) smoothly deviates from linear above $\sim 37\,\text{kV}$. Plotting $C_{meas}/C_0$ vs. $V$ reveals the characteristic AVE saturation plateau.

---
