[↑ Ch.8 Discrete Masking](../index.md)
<!-- leaf: verbatim -->

# Motivation and Experimental Protocol

## Motivation

Having established the Hardware--Software Z--A inversion (Chapter 2), a natural question arises: *can the $S(r)$ saturation compliance function be applied at runtime as a continuous attenuation, or must the action on the software lattice be binary?*

Static baking (Chapter 5) physically excises neuron rows from the weight matrices, reducing the dimensionality of the gate, up, and down projections in tandem. Runtime masking, by contrast, preserves the full matrix dimensions and applies $S(r)$ as an element-wise scaling of the hidden state before the down-projection.

Two runtime masking strategies were hypothesized:

1. **Continuous:** $h_{masked} = h \odot S(r)$, where $S(r) = \sqrt{1-r^2} \in [0,1]$.
2. **Binary:** $h_{masked} = h \odot \mathbf{1}_{S(r)>0}$, performing discrete excision without matrix reshaping.

## Experimental Protocol

Both strategies were tested using the `bench eval` A/B harness against the Qwen3.5-4B model with identical prompts and parameters, with the global thermodynamic yield limit $A_c$ set at the model-wide mean.

| **Pass** | **Output** | **Tokens** | **tok/s** |
|---|---|---|---|
| A: Baseline (no masking) | `4` | 5 | 16.1 |
| B: Continuous $S(r)$ mask | `.` | 50 | 17.9 |
| C: Binary excision mask | (empty) | 0 | --- |
