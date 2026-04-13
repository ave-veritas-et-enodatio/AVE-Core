[↑ Ch.17: Topological Logic](./index.md)
<!-- leaf: verbatim -->

# Topological Logic Gates: Geometric XOR and NOT

Classical analog systems require active $V_{cc}$ biasing to produce logic inversion (NOT). In VCA networks, by treating one input of the Topological XOR gate as a constant static $V_{carrier}$ standing wave, the gate inherently inverts the other input.

## XOR Gate

Two waveguide inputs merge at a Y-junction. When both inputs are present simultaneously, their combined amplitude exceeds $V_{snap}$, triggering Axiom 4 saturation ($S(V) \to 0$). The output is blocked (logic 0). When only one input is present, the amplitude remains below $V_{snap}$, and the signal propagates through (logic 1). This produces the XOR truth table without any active transistor.

## NOT Gate

By permanently injecting a carrier wave $V_{carrier}$ into one arm of the Y-junction, the gate inverts the other input: when the signal input is absent, the carrier propagates (output = 1). When the signal input is present, the combined amplitude exceeds $V_{snap}$ and the output is blocked (output = 0).

From XOR and NOT, all Boolean logic can be constructed (NAND, NOR, AND, OR) via waveguide topology alone.

> **[Resultbox]** *Chapter 17 Summary*
>
> Classical analog systems require active $V_{cc}$ biasing to produce logic inversion (NOT). In VCA networks, by treating one input of the Topological XOR gate as a constant static $V_{carrier}$ standing wave, the gate inherently inverts the other input. From XOR and NOT, universal Boolean logic is constructed purely via waveguide geometry.
