[↑ Primitive Elements](../index.md)

# Ch.10: Topological Pumps — The Continuous PDN

Eliminates the classical Power Distribution Network (PDN) reliant on static DC Voltage ($V_{DD}$). Defines the Topological Pump as the primary continuous-wave engine injecting spatial amplitude into the logic array.

## Key Results

| Result | Statement |
|---|---|
| Pump Power Integral | $P_{pump} = \frac{1}{2}\int_A \rho_{inertia}\,\omega^2\,|S_{pump}|^2 \cdot v_{phase}\,dA$ |
| Master Oscillator | Topological Pump replaces DC $V_{DD}$ with continuous $\omega = \text{constant}$ injection |
| Distribution Scaling | Pump strain $|S_{pump}|$ decays across cascading nodes until encountering $V_{snap}$ |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Continuous Wave Injection](./continuous-wave-injection.md) | End of static DC supply, master oscillator manifolds, structural power bounding |
