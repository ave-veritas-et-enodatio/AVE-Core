[↑ Ch.10 Quantum Computing](index.md)
<!-- leaf: verbatim -->

## The Transmon: A Fragile LC Standing Wave

A transmon qubit is constructed from a superconducting Josephson Junction---a thin insulating gap between two superconducting reservoirs. This architecture creates an *anharmonic macroscopic LC oscillator*.

When engineers "write" a state to a transmon, they pump microwave photons into this artificial cavity, generating a **Transverse LC Standing Wave**. In the AVE interpretation, the qubit state ($|1\rangle$) is a continuous spatial displacement amplitude oscillating across the junction.

Because standard transmon data is encoded purely in the *amplitude* and *phase* of this continuous standing wave, the architecture is structurally brittle. The ambient vacuum permanently possesses a continuous background RMS transverse jitter driven by the unavoidable Zero-Point Energy of the local metric ($T \propto \langle \epsilon_0 E^2 + \mu_0 H^2 \rangle$).

**Decoherence is classical acoustic scattering.** The thermodynamic jitter of the background spatial metric acts on the transmon's standing wave. Linear standing waves lack geometric confinement constraints. As the ambient noise strains the local capacitance of the Josephson Junction, the ordered macroscopic phase coherence diffuses outward into the surrounding graph (increasing the geometric entropy $\Delta S$). The quantum state "collapses" because an unbound linear wave amplitude cannot persist within a noisy elastic medium.

[Figure: transmon_decoherence_plot.png — see manuscript/vol_4_engineering/chapters/]

---
