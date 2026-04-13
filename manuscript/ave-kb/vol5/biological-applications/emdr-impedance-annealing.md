[↑ Biological Applications](./index.md)
<!-- leaf: verbatim -->

# EMDR as Impedance Annealing of Trauma Defects

## Hypothesis

Eye Movement Desensitisation and Reprocessing (EMDR) therapy uses bilateral sensory stimulation---horizontal eye movements, alternating taps, or auditory tones---to alleviate the distress associated with traumatic memories. Despite robust clinical evidence, the mechanism of action remains poorly understood in conventional psychology.

The AVE framework provides a structural explanation. Traumatic memories are *impedance defects* in the neural coupled resonator network. The extreme emotional intensity at the time of encoding produces a localised, high-impedance synaptic cluster:

$$Z_{\mathrm{trauma}} \gg Z_{\mathrm{surrounding}}, \qquad |\Gamma_{\mathrm{trauma}}| = \left|\frac{Z_{\mathrm{trauma}} - Z_{\mathrm{cortex}}}{Z_{\mathrm{trauma}} + Z_{\mathrm{cortex}}}\right| \to 1$$

When the global consciousness standing wave encounters this defect, it *reflects* rather than coupling---producing the characteristic avoidance, hyperarousal, and dissociation responses of post-traumatic stress.

## Mechanism: Bilateral Impedance Annealing

EMDR's bilateral stimulation is an externally applied oscillating drive at the brain's natural interhemispheric frequency ($\sim$0.5--2 Hz, matching the saccadic rhythm). This drive forces the consciousness standing wave to repeatedly sweep across the impedance defect.

Each sweep partially softens the impedance mismatch:

$$Z_{\mathrm{trauma}}^{(n+1)} = Z_{\mathrm{trauma}}^{(n)} \cdot \bigl(1 - \eta\,S_n\bigr)$$

where $\eta$ is a small coupling factor and $S_n$ is the saturation at the defect boundary during pass $n$.

Over $N$ bilateral cycles, the defect impedance gradually converges toward the surrounding cortical impedance: $Z_{\mathrm{trauma}} \to Z_{\mathrm{cortex}}$, $|\Gamma| \to 0$. The memory can then be accessed without producing a reflected (distress) response.

This is isomorphic to the annealing of flux-pinning defects in a superconductor via oscillating field cycling, and to the impedance smoothing of lattice defects during metal annealing.

## Testable Predictions

1. The bilateral stimulation frequency should have an optimum that matches the interhemispheric cavity mode frequency, measurable via EEG coherence spectrum.
2. Pre- and post-EMDR EIS measurements of the cortical impedance profile (via transcranial electrical impedance spectroscopy) should show reduced impedance contrast at the trauma-associated cortical region.
3. The number of EMDR sessions required for resolution should correlate with the initial $|\Gamma|$ of the trauma defect---more severe trauma (higher $|\Gamma|$) requires more annealing cycles.
4. Other bilateral stimulation modalities (auditory, tactile) should be equally effective if they excite the same interhemispheric cavity mode, consistent with clinical observations.

---
