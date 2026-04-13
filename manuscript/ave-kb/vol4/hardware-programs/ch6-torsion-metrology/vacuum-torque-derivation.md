[↑ Ch.6 Torsion Metrology](index.md)
<!-- leaf: verbatim -->

## The Mineral Oil Dielectric Bath (PONDER-05)

For the DC-biased PONDER-05 configuration ($30 \text{ kV}$ across a $50 \text{ mm}$ quartz cylinder), the dielectric bath provides three simultaneous engineering advantages.

### Corona Suppression

At 30 kV across a 50 mm gap, the applied electric field is $E_{app} = 0.60$ MV/m. The Paschen breakdown thresholds are:

| Medium | $\varepsilon_r$ | $E_{bd}$ (MV/m) | Margin ($E_{app}/E_{bd}$) |
|---|---|---|---|
| Air (STP) | 1.0 | 3.0 | 0.200 (marginal) |
| Mineral oil | 2.2 | 12.0 | 0.050 ($20\times$ safe) |
| Transformer oil | 2.3 | 18.0 | 0.033 ($30\times$ safe) |
| Fluorinert FC-70 | 1.9 | 16.0 | 0.037 ($27\times$ safe) |

### Thermal Management

Quartz possesses an exceptionally low dielectric loss tangent ($\tan\delta \approx 10^{-5}$). At $500 \text{ V}$ RMS and $50 \text{ kHz}$, the power dissipated in the quartz cylinder ($25 \text{ mm}$ radius $\times$ $50 \text{ mm}$) is:

$$
P_{diss} = \omega C V_{rms}^2 \tan\delta \approx 0.001 \text{ mW}
$$

This negligible dissipation produces a temperature rise of $< 0.001$°C even in still air.

### Impedance Step-Down Matching

| Interface | $Z_1$ ($\Omega$) | $Z_2$ ($\Omega$) | Power reflected |
|---|---|---|---|
| Quartz $\to$ Vacuum (direct) | 178 | 377 | 12.9% |
| Quartz $\to$ Oil | 178 | 254 | 3.1% |
| Oil $\to$ Vacuum | 254 | 377 | 3.8% |
| Quartz $\to$ Oil $\to$ Vacuum (net) | --- | --- | $\sim 3.4\%$ |

This $3.7\times$ reduction in reflected acoustic power is analogous to the sapphire GRIN nozzle proposed for PONDER-02.

### Bistatic Plume Diagnostics (PONDER-02 Parallax)

While the torsion balance measures the integrated macroscopic thrust, the **Bistatic Reflection Parallax** explicitly maps the spatial geometry of the acoustic emission. By broadcasting a low-power, high-frequency (e.g., $10\text{ GHz}$) transverse microwave probe across the exhaust plume, the geometric gradient of the vacuum saturation $S(A) < 1$ is isolated. Axiom 4 guarantees the effective wave velocity drops within the plume ($c_{eff} = c_0 S(A)^{1/2}$). An interferometric comparison of the $10\text{ GHz}$ probe against a pure-vacuum control path generates a measurable phase shift ($\Delta \phi$).

---
