[↑ Ch.11 Index](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [cltls0, kl1ern, qsgl7d, wzezvt, ydksh6]
-->

## PCBA Bench Protocols

Five specific PCBA-level experiments, each isolating a single AVE prediction.

<!-- claim-quality: ydksh6 -->
### CLEAVE-01: Femto-Coulomb Electrometer

**Prediction**: Mechanically separating two uncharged plates in vacuum generates $Q = \xi_{topo} \cdot x$.

- PZT actuator steps 1 µm → $Q = 4.149 \times 10^{-7} \times 10^{-6} = 0.415$ pC
- 10 pF parasitic → $V = Q/C = 41.5$ mV step per µm
- Electrometer: ADA4530-1 (20 fA bias), guard rings, Teflon standoffs
- **Falsification**: 0.0 mV → framework killed; 41.5 mV → $\xi_{topo}$ confirmed

<!-- claim-quality: wzezvt -->
### HOPF-02: S-Parameter VNA Falsification

**Prediction**: Hopf coil (torus knot) couples to chiral LC metric → anomalously deep $S_{11}$ notch vs classical toroid.

- Same-inductance Hopf coil vs standard toroid on single PCBA
- VNA sweep 10–100 MHz
- **Falsification**: identical impedance curves → killed; anomalous chiral match → confirmed

**Snell Parallax sub-test**: illuminate torus knot array with planar microwave beam, detect anomalous refraction angle via 2D baseline array.

<!-- claim-quality: qsgl7d -->
### ROENTGEN-03: Solid-State Sagnac Induction

**Prediction**: Spinning non-metallic disk induces B-field via vacuum mutual inductance.

- Dense ceramic disk at 10k RPM, $v_{vac} \approx 0.038$ m/s
- Interdigitated capacitor driven at 10 kV, 1 kHz → $B \approx 4.2$ pT
- Lock-in amplifier extracts $\sim 0.26\;\mu$V signal
- **Falsification**: amplitude must scale linearly with RPM, flip $180°$ on reversal

<!-- claim-quality: cltls0 -->
### ZENER-04: Impedance Avalanche Detector

**Prediction**: Vacuum behaves as TVS Zener — rigid $Z_0 \approx 377\;\Omega$ until $V > V_{yield}$.

- Marx generator PCBA: 80 kV transient, sub-µs rise
- Encapsulated spherical electrode (prevent arc-over)
- Monitor $I_D$ vs $V$: linear charging → **avalanche knee** at 43.65 kV
- **Falsification**: perfectly linear $I_D(V)$ → killed

<!-- claim-quality: kl1ern -->
### TORSION-05: Horizontal Metric Rectification

**Prediction**: Asymmetric flyback bypasses $G/c^2$ gap on a zero-gravity torsion pendulum.

- SiC MOSFET drives ferrite ignition coil with asymmetric sawtooth
- Slow edge (+500 V, $\ll V_{yield}$): vacuum acts as matched $377\;\Omega$ line → forward thrust +0.207 mN
- Fast edge (−75 kV, $> V_{yield}$): impedance rupture $\Gamma = -1$ → 0 mN backward reaction
- Net continuous DC thrust: $\sim 100\;\mu$N
- **Falsification**: pendulum stationary → killed

---
