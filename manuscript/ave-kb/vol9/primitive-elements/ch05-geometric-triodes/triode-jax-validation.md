[↑ Ch.5: Geometric Triodes](./index.md)
<!-- leaf: verbatim -->

# Geometric Triode JAX Validation

[Figure: triode_transconductance — Geometric Triode Transconductance Curves. Each curve plots $I_D/I_{D0} = S(\sqrt{V_{lon}^2 + V_{gate}^2}/V_{snap})$ for three values of longitudinal drive amplitude. Pinch-off (cutoff) occurs at $V_{gate} = \sqrt{V_{snap}^2 - V_{lon}^2}$, marked by the vertical dashed lines. No empirical fitting is involved: all curves are exact evaluations of the Axiom 4 kernel. The classical FET quadratic law is recovered as the leading-order Taylor expansion of $S$ in Regime I.]

The simulation validates the analytic transconductance formula across the full operating range:
- $V_{lon}/V_{snap} = 0.1$: near-full channel capacity; cutoff at $V_{gate}/V_{snap} \approx 0.995$
- $V_{lon}/V_{snap} = 0.5$: medium drive; cutoff at $V_{gate}/V_{snap} \approx 0.866$
- $V_{lon}/V_{snap} = 0.8$: heavy drive; early cutoff at $V_{gate}/V_{snap} \approx 0.6$

All three curves exactly match Equation $I_D(V_{gate}) = I_{D0}\sqrt{1 - (V_{lon}^2 + V_{gate}^2)/V_{snap}^2}$, confirming zero-parameter-fit transconductance from first principles.
