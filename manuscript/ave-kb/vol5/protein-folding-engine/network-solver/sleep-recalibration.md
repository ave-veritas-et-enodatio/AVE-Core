[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Sleep as S-Parameter Recalibration

In RF engineering, a network analyser characterises a device by sweeping a test signal across all frequencies and measuring the S-parameter matrix. Sleep may be the biological equivalent: the brain replays activity patterns (hippocampal replay during slow-wave sleep) to *measure and recalibrate* its own S-parameter matrix.

- **Slow-wave sleep**: Low-frequency sweep ($\delta$: 0.5--4 Hz). Tests the global standing wave modes of the cortical cavity. Consolidation occurs when a replayed pattern produces low $|S_{11}|^2$ (good impedance match) --- the corresponding synaptic impedances are reinforced.
- **REM sleep**: Broadband sweep. Tests high-frequency local modes. The characteristic muscle atonia prevents motor output from corrupting the measurement --- identical to terminating unused ports with matched loads during a calibration sweep.
- **Sleep deprivation**: Skipping recalibration causes progressive impedance drift across the network, degrading the fidelity of stored standing wave patterns --- consistent with the observed cognitive impairment.

## Falsifiable Prediction

The frequency spectrum of sleep EEG should correspond to the eigenfrequencies of the cortical standing wave cavity. The dominant slow-wave frequency $f_\delta \approx 1$ Hz should satisfy $f_\delta \approx v_\text{axon} / (2L_\text{cortex})$ where $v_\text{axon}$ is the mean axonal conduction velocity and $L_\text{cortex}$ is the effective cortical path length.

---
