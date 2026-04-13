[↑ Ch.4 Phase Transitions](../index.md)
<!-- leaf: verbatim -->

# Turbulence Onset as a Regime I $\to$ II Transition

## Hypothesis

The laminar-to-turbulent transition in fluid flow occurs at a critical Reynolds number $\mathrm{Re}_c$ that depends on geometry. The AVE framework identifies this transition as the Regime I $\to$ Regime II boundary crossing, where the driving parameter (flow velocity, or equivalently the viscous stress) exceeds the first universal regime boundary $r_1 = \sqrt{2\alpha}$.

The Reynolds number maps to a normalised drive parameter:

$$
r = \frac{\mathrm{Re}}{\mathrm{Re}_{\max}},
$$

where $\mathrm{Re}_{\max}$ is the geometry-dependent maximum stable Reynolds number. The universal prediction is that the onset of turbulence (first appearance of self-sustaining vortical structures) occurs at $r = r_1 = \sqrt{2\alpha} \approx 0.1208$.

## Mapping to Fluid Variables

The regime boundary $r_1$ sets the ratio of inertial driving to viscous dissipation at which the laminar standing wave (Poiseuille flow) first saturates and begins to shed energy into higher modes (turbulent eddies). The saturation operator governs the transition:

$$
S(\mathrm{Re}, \mathrm{Re}_c) = \sqrt{1 - \left(\frac{\mathrm{Re}}{\mathrm{Re}_c}\right)^2}.
$$

For $\mathrm{Re} < \mathrm{Re}_c$, $S > 0$ and the flow remains laminar. At $\mathrm{Re} = \mathrm{Re}_c$, $S = 0$ and the laminar mode is fully saturated.

## Testable Prediction

The intermittency fraction (fraction of time the flow exhibits turbulent bursts) near the critical Reynolds number should follow $1 - S(\mathrm{Re}, \mathrm{Re}_c)$, measurable via hot-wire anemometry in pipe flow at controlled Reynolds numbers.

---
