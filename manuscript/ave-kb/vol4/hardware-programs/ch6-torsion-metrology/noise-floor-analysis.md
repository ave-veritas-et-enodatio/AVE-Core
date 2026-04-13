[↑ Ch.6 Torsion Metrology](index.md)
<!-- leaf: verbatim -->

## The Eight-Point Artifact Rejection Protocol

The history of anomalous thrust claims is littered with artifacts. Each known artifact class is addressed with a specific mitigation:

1. **Ion Wind:** Eliminated by operating the quartz piezo submerged in degassed mineral oil (no free charge carriers). For PONDER-01 (vacuum operation), the chamber pressure must be $< 10^{-5}$ Torr to suppress Paschen discharge.

2. **Thermal Drift:** With $P_{diss} < 0.001$ mW (quartz) and convective oil cooling, the mass drift rate is $< 0.01$ mg/hour---three orders of magnitude below the $\sim 50 \mu$g signal. The torsion balance arm temperature is monitored by a calibrated thermistor at 1 mK resolution.

3. **Electrostatic Attraction:** The oil bath and torsion balance are enclosed in a grounded Faraday cage. The suspension wire is electrically isolated from the HV circuit. All conductive surfaces within the cage are grounded through $< 1 \Omega$ bonds.

4. **Mechanical Vibration:** The oil bath provides viscous damping of the torsion arm ($Q \approx 5$ in oil vs. $Q > 1000$ in vacuum), critically damping seismic transients. The assembly sits on a pneumatic optical table with $< 1 \mu$m vertical displacement at 1 Hz.

5. **Outgassing:** The oil is degassed under vacuum for 24 hours prior to measurement. The Faraday cage is baked at 60°C for 12 hours to drive off adsorbed water.

6. **Cable Forces:** All electrical connections to the DUT use compliant, multi-strand leads routed symmetrically about the torsion axis. Preferably, the DC bias is delivered through the suspension wire itself (which is electrically conductive), and the AC excitation uses a wireless piezo driver with an onboard battery.

7. **Lorentz Forces (Earth's Field):** The experiment is enclosed in a mu-metal shield ($\mu_r > 20{,}000$) reducing the ambient 50 $\mu$T field to $< 50$ nT. The maximum Lorentz force from residual current loops is thereby reduced to $< 0.01 \mu$N.

8. **Statistical Significance:** Each measurement consists of $\geq 100$ on/off cycles (HV drive enabled/disabled, 30 s per state). The mean thrust is extracted via lock-in analysis at the switching frequency. The null hypothesis (zero thrust) is rejected only if $\chi^2$ exceeds $p < 0.001$ (99.9% confidence). The entire dataset is published in raw form for independent reanalysis.

---
