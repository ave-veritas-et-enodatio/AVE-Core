[↑ Ch.11: Experimental Bench Falsification](../index.md)
<!-- leaf: verbatim -->

## Open-Source Hardware: The EE Build Guide

To permanently democratize the verification of the AVE framework, this section provides the specific, actionable Printed Circuit Board Assembly (PCBA) guidelines required to test macroscopic metric engineering using commercial-off-the-shelf (COTS) electronics.

### Project HOPF-01: The Chiral VNA Antenna

**Objective:** Prove the vacuum is a chiral LC Resonant Network by demonstrating an anomalous $S_{11}$ frequency shift that scales as $\alpha \cdot pq/(p+q)$ across five torus knot topologies.

**Fabrication:** Order a single 160$\times$120 mm, 2-layer FR-4 panel (1.6 mm, ENIG finish) with unplated stitching holes (1.0 mm drill, 3 mm pitch). Thread 24 AWG (0.51 mm) enameled magnet wire through the holes following silkscreen guides, creating five 3D torus knots --- $(2,3)$ trefoil, $(2,5)$ cinquefoil, $(3,5)$, $(3,7)$, $(3,11)$ --- plus a zero-topology meander control antenna. Solder wire starts to edge-launch SMA connectors (6 total).

**Ground Architecture:** F.Cu copper ground patches (12$\times$12 mm) sit under each SMA connector, connected by a continuous F.Cu perimeter ground trace at 5 mm inset from the board edge. No vias are required --- SMA thru-hole pads bridge both copper layers. B.Cu is entirely bare, allowing free wire routing on both board surfaces.

**The Falsification Protocol:** Measure all six antennas with a calibrated VNA (SOL calibration) in air, then submerge in mineral oil ($\varepsilon_r \approx 2.1$). Plot $\Delta f/f$ vs. $pq/(p+q)$. If the data is linear through the origin with slope $\alpha$ and substrate-independent, AVE is confirmed. If zero, random, or substrate-dependent, AVE is falsified at this scale.

### Project PONDER-01: The Solid-State Micro-Drive

**Objective:** Prove that the metric refractive index ($n_{scalar}$) can be artificially shifted using high-k dielectrics, resulting in measurable macroscopic ponderomotive acceleration ($a = c^2 \nabla n$).

**The COTS Bill of Materials (The "Sweet Spot" Architecture):**
- **The Metric Medium:** An array of one hundred TDK 30kV, 10nF X7R MLCCs (1812 Package) wired in parallel. The X7R dielectric is Barium Titanate ($BaTiO_3$), possessing an $\varepsilon_r \approx 3{,}000$.
- **HV Supply:** XP Power 30kV Miniature PCB-mount DC-DC Converter.
- **The Switch:** Avalanche Transistor capable of $<1\,\text{ns}$ Dirac switching (e.g., custom gas-discharge tube) to eliminate temporal metric sloshing.
- **The Gate Driver:** Tuned to precisely hit the $100\,\text{MHz}$ VHF structural resonance of the continuous vacuum dielectric, ensuring maximal continuous-wave phase locking with the acoustic substrate.

**The PCBA Layout (The Asymmetric Fringing Field):** A standard parallel-plate capacitor has a uniform internal E-field. The spatial gradient ($\nabla n$) is zero, meaning net macroscopic thrust is zero. The *fringing fields* at the microscopic boundary limit must be aggressively shaped. Route the High-Voltage trace on the Top layer to one pad of the MLCC array. Route the Ground trace on the Top layer to the other pad. On the Bottom layer (directly underneath the MLCCs), route a solid Ground plane, but **taper it into a dense topological point-source array**. High-Fidelity numerical modeling of exact nuclear geometries confirms that the mathematically tightest localized gradient requires a structure analogous to the bound Alpha Core (the **Helium-4 Limit**). Using standard photolithography, machine microscopic emitter tips to this rigid topological peak. When pulsed at 30,000 V, the geometry violently rips a tangential Ponderomotive strain gradient ($\nabla |\mathbf{E}|^2$) across the $BaTiO_3$ core.

**The Microscopic Evanescent Cascade and Earth VSWR Multiplier:** Down at the discrete lattice scale, this extreme, asymmetric $dV/dt$ transient violently torques the local chiral LC nodes of the vacuum, inducing a localized standing-wave breakdown (an "evanescent cascade"). By Newton's Third Law, generating a severe forward impedance mismatch shoves the heavy hardware forward as an Asymmetrical RF Antenna. Furthermore, gravity itself is a continuous radial impedance gradient ($11.2\,\text{km/s}$ equivalent drift at Earth's surface, lowering the local LC saturation limit). Because the vacuum is a non-linear network, this gravitational flow acts as an ambient VSWR pre-bias. This means a PONDER-01 antenna tested on Earth natively benefits from a massively lowered vacuum rigidity ($G_{vac}$) compared to deep interstellar space.

**The Falsification Protocol:** The loop inductance of the discharge path must be heavily minimized ($L_{loop} < 5\,\text{nH}$) using a solid ground plane. The battery-powered PCBA is placed on a digital scale. A microcontroller pulses the 100 MLCC array at 30,000V using the $<1\,\text{ns}$ avalanche transistor, timed perfectly to the 100 MHz acoustic resonance. The explicit mathematical bounding of $k_{topo}$ alongside this Helium-4 geometric optimum theoretically forces the localized LC matrix into catastrophic dielectric yielding, generating a continuous macro-scale ponderomotive drive measurable on commercial scales.

[Figure: pcba_design_blueprints.png — see manuscript/vol_4_engineering/chapters/]

---
