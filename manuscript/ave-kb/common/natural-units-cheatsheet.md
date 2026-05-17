[↑ Common Resources](index.md)
<!-- leaf: verbatim -->

# Universal Lattice Units — Cheat Sheet

Consolidated reference for AVE natural units + SI conversion factors + cross-domain scaling powers. **Defers to upstream sources for derivations**; this leaf is a navigable cheat-sheet, not a derivation chapter.

**Three upstream sources** consolidated here:
- [`vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md` §2](../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) — Dimensional-analysis table (lattice-native units) + the load-bearing $V_{YIELD} = 1$ vs $V_{SNAP} = 1$ normalization warning
- [`xi-topo-traceability.md` §Physical Meaning](xi-topo-traceability.md) — 6-row cross-domain scaling-power table
- [`src/ave/core/constants.py:260-294`](../../../src/ave/core/constants.py) — Canonical engine SI ↔ Native conversion floats

Per foreword line 34: *"$\ell_{node}$ becomes the unit of length in the substrate's natural unit system, where it evaluates as the integer $\mathbf{1}$ by definition (analogous to setting $c = 1$ in natural units; the dimensional SI value persists as the translation factor back to laboratory measurements)."*

## §1 — Four-base convention

In AVE natural units, **four fundamental scales are set to 1**:

| Symbol | Meaning | SI value | What it pins |
|---|---|---|---|
| $\ell_{node}$ | Lattice pitch | $3.86 \times 10^{-13}$ m | Spatial scale (Compton wavelength of $m_e$) |
| $c$ | Speed of light | $2.998 \times 10^{8}$ m/s | Velocity / time-vs-space conversion |
| $\hbar$ | Reduced Planck constant | $1.054 \times 10^{-34}$ J·s | Action scale |
| $m_e$ | Electron mass | $9.109 \times 10^{-31}$ kg | Mass scale |

**These four are not independent — they are related by $\ell_{node} = \hbar / (m_e c)$ (Compton wavelength).** Setting any three to 1 forces the fourth.

Consequence: $\tau_{relax} = \ell_{node} / c = 1$ (fundamental time unit) and $T_{EM} = m_e c^2 / \ell_{node}$ (electromagnetic string tension) both have natural-unit value 1.

## §2 — Master SI ↔ Native conversion table

Multiply a native-unit quantity by the SI factor to get the SI value. Source: [`vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md` lines 92-112](../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) consolidated with engine [`src/ave/core/constants.py:260-294`](../../../src/ave/core/constants.py).

### Fundamental scales

| Quantity | Symbol | SI units | Native value | SI conversion factor | Engine constant |
|---|---|---|---|---|---|
| Length | $\ell_{node}$ | m | $1$ | $3.86 \times 10^{-13}$ m | `NATIVE_TO_SI_LENGTH = L_NODE` |
| Speed | $c$ | m/s | $1$ | $2.998 \times 10^{8}$ m/s | `NATIVE_TO_SI_VELOCITY = C_0` |
| Mass | $m_e$ | kg | $1$ | $9.109 \times 10^{-31}$ kg | `NATIVE_TO_SI_MASS = M_E` |
| Action | $\hbar$ | J·s | $1$ | $1.054 \times 10^{-34}$ J·s | — |
| Time | $\tau_{relax} = \ell_{node}/c$ | s | $1$ | $1.288 \times 10^{-21}$ s | `TAU_RELAX_SI = L_NODE / C_0`; `TAU_RELAX_NATIVE = 1.0` |
| Energy | $m_e c^2$ | J | $1$ | $8.187 \times 10^{-14}$ J | `NATIVE_TO_SI_ENERGY = M_E * C_0**2` |
| Energy (eV) | $m_e c^2$ | eV | $1$ | $511{,}000$ eV | `NATIVE_TO_SI_ENERGY_EV` |

### Electromagnetic scales

These derive from the four fundamental + Axioms 2/4. Note the $\sqrt{\alpha}$ factors that appear pervasively (consequence of Ax2 TKI: charge $\equiv$ length, with α as the geometric proportionality).

| Quantity | Symbol | SI units | Native value | SI value |
|---|---|---|---|---|
| Characteristic impedance | $Z_0 = \mu_0 c$ | Ω | $1$ | $376.73$ Ω |
| Charge | $e$ | C | $\sqrt{\alpha} \approx 0.0854$ | $1.602 \times 10^{-19}$ C |
| Topo-kinematic scale | $\xi_{topo} = e/\ell_{node}$ | C/m | $\sqrt{\alpha} \approx 0.0854$ | $4.149 \times 10^{-7}$ C/m |
| Snap voltage | $V_{SNAP} = m_e c^2 / e$ | V | $1/\sqrt{\alpha} \approx 11.71$ | $511{,}000$ V |
| **Yield voltage** | $V_{YIELD} = \sqrt{\alpha} \cdot V_{SNAP}$ | V | **$1.0$** (!) | $43{,}652$ V |
| Max current | $I_{max} = \xi_{topo} \cdot c$ | A | $\sqrt{\alpha}$ | $1.244 \times 10^{2}$ A |
| Per-bond inductance | $L_{cell} = \mu_0 \ell_{node}$ | H | depends on $\mu_0$ choice | $4.84 \times 10^{-19}$ H |
| Per-bond capacitance | $C_{cell} = \varepsilon_0 \ell_{node}$ | F | depends on $\varepsilon_0$ choice | $3.41 \times 10^{-24}$ F |

### LOAD-BEARING NORMALIZATION WARNING

Per [`lattice-impedance-decomposition.md` line 114-120](../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md):

> **In lattice units, the engineering yield threshold is $V_{YIELD} = 1$, NOT $V_{SNAP} = 1$.** Engine code typically uses $V_{SNAP} = 1.0$ as the user-facing normalization. When the user sees `amp = 0.5 * V_SNAP`, that's effectively `amp = 0.5/sqrt(alpha) = 5.85` in units where $V_{YIELD} = 1$. **At $0.5 \cdot V_{SNAP}$, the lattice is massively above yield, below rupture.**

> The Axiom 4 operator uses $V_{SNAP}$ as the normalization for $A$, so the "$\sqrt{2\alpha}$ Regime I/II boundary" corresponds to $A = \sqrt{2\alpha} = 0.121$ in $V/V_{SNAP}$ units. In $V_{YIELD}$ units this is $A_{yield-units} = 0.121/\sqrt{\alpha} = 1.42$.

> **This normalization choice (engineer-facing $V_{SNAP}$ vs native $V_{YIELD}$) is load-bearing for amplitude scoping in engine experiments. Always verify which normalization is active.**

## §3 — Cross-domain scaling powers ($\xi_{topo}$ bridge)

Source: [`xi-topo-traceability.md` §Physical Meaning lines 34-42](xi-topo-traceability.md) consolidated with engine [`src/ave/core/constants.py:284-294`](../../../src/ave/core/constants.py).

$\xi_{topo}$ converts between **geometric displacement** (meters) and **charge** (Coulombs); every derived quantity inherits its units from this single scaling. Per Ax2 TKI: $[Q] \equiv [L]$.

| Physical bridge | Mapping | Scaling power | Engine constant |
|---|---|---|---|
| Charge ↔ Displacement | $Q = \xi\, x$ | $\xi^{1}$ | — (direct) |
| Current ↔ Velocity | $I = \xi\, v$ | $\xi^{1}$ | — |
| Voltage ↔ Force | $V = \xi^{-1} F$ | $\xi^{-1}$ | `EE_TO_TOPO_VOLTAGE = XI_TOPO` |
| Capacitance ↔ Compliance | $C = \xi^{2}\, \kappa$ | $\xi^{2}$ | `EE_TO_TOPO_CAPACITANCE = 1.0 / XI_TOPO**2` |
| Inductance ↔ Mass | $L = \xi^{-2}\, m$ | $\xi^{-2}$ | `EE_TO_TOPO_INDUCTANCE = XI_TOPO**2` |
| Resistance ↔ Viscosity | $R = \xi^{-2}\, \eta$ | $\xi^{-2}$ | `EE_TO_TOPO_RESISTANCE = XI_TOPO**2` |

**Cascade implication:** a FAIL on any row testing $Q = \xi_{topo} \cdot x$ (e.g., C15-CLEAVE-01 in the divergence-test-substrate-map on sibling branch `analysis/divergence-test-substrate-map`) propagates immediately to ALL 6 mappings since they share the same conversion constant.

## §4 — Quick-reference identities

In AVE natural units ($\ell_{node} = c = \hbar = m_e = 1$):

- **Mass = energy** ($m_e c^2 = m_e$ when $c = 1$)
- **Length = time** ($\ell_{node} / c = 1$ when both are 1; this IS $\tau_{relax}$)
- **Compton wavelength of electron = 1** by construction
- **Z_0 = 1** (characteristic impedance dimensionless when c = 1)
- **V_YIELD = 1** (engineering yield threshold; see §2 warning)
- **e (charge) = √α ≈ 0.0854** (NOT 1 — fundamental charge is the $\sqrt{\alpha}$-suppressed unit per Ax2)
- **$\xi_{topo}$ = √α** (since $\xi_{topo} = e / \ell_{node}$ and $\ell_{node} = 1$)

**SI conversion shortcut** for working with engine code:

```python
from ave.core.constants import (
    L_NODE, C_0, M_E, HBAR, e_charge, XI_TOPO,
    NATIVE_TO_SI_LENGTH, NATIVE_TO_SI_MASS, NATIVE_TO_SI_ENERGY,
    NATIVE_TO_SI_TIME, NATIVE_TO_SI_VELOCITY, NATIVE_TO_SI_ENERGY_EV,
    EE_TO_TOPO_RESISTANCE, EE_TO_TOPO_VOLTAGE,
    EE_TO_TOPO_INDUCTANCE, EE_TO_TOPO_CAPACITANCE,
    TAU_RELAX_SI, TAU_RELAX_NATIVE,
)
si_value = native_value * NATIVE_TO_SI_LENGTH  # for length, etc.
topo_force = volts * EE_TO_TOPO_VOLTAGE  # Volts → Newtons via ξ
```

## §5 — Namespace caveat (ξ disambiguation)

Per [`xi-topo-traceability.md` §Namespace De-Collision](xi-topo-traceability.md):

The corpus uses Greek letter ξ in **three distinct semantic scopes**:

| Symbol | Magnitude | Scope | Physical meaning |
|---|---|---|---|
| **$\xi_{topo}$** | $\approx 4.149 \times 10^{-7}$ C/m | Ax 2 conversion constant (this cheat-sheet) | Electromechanical bridge |
| **$\xi$** (no subscript) | $\approx 3.455 \times 10^{38}$ (dimensionless) | Vol 3 Ch 1 Machian impedance integral | Cosmological boundary impedance for $G = c^4/(7\xi T_{EM})$ |
| **$\xi_{K1}, \xi_{K2}$** | O(1) dimensionless | Substrate Cosserat prefactors (Vol 1 Ch~\ref{ch:macroscopic_moduli}) | Substrate Cosserat moduli with $\xi_{K2}/\xi_{K1} = 12$ K4-symmetry-forced |

**Same letter, three different magnitudes, three different physical scopes.** This cheat-sheet covers $\xi_{topo}$ only.

## §6 — How to expand this cheat-sheet

If a new natural-unit quantity becomes load-bearing across volumes, add it to the appropriate §2 sub-table here AND in the upstream source ([`lattice-impedance-decomposition.md` §2](../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) and/or [`xi-topo-traceability.md` §Physical Meaning](xi-topo-traceability.md)). **Do not let this leaf drift from the upstream sources** — re-grep on update.

If a new scaling power (a 7th $\xi_{topo}^n$ mapping) is discovered, add to §3 AND to the upstream [`xi-topo-traceability.md` §Physical Meaning](xi-topo-traceability.md) table.

If a new engine constant block is added to [`src/ave/core/constants.py`](../../../src/ave/core/constants.py), surface it here in §4's code snippet.

---

> → Primary: [Lattice Impedance Decomposition](../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) — canonical 6-impedance + dimensional-analysis derivation; this cheat-sheet's §2 table consolidates the §2 source there
> → Primary: [ξ_topo Traceability Map](xi-topo-traceability.md) — canonical cross-domain bridge with namespace de-collision; this cheat-sheet's §3 + §5 consolidate from there
> → Primary: [`src/ave/core/constants.py`](../../../src/ave/core/constants.py) — canonical engine SI ↔ Native conversion floats; this cheat-sheet's §2 + §4 consolidate from there (lines 260-294)
> ↗ See also: [Dimensional Analysis (Vol 1 Ch 7 §7.4)](../vol1/operators-and-regimes/ch7-regime-map/dimensional-analysis.md) — universal dimensionless master equation $\partial_t^2 \phi = c_0^2 \sqrt{1-r^2} \nabla^2 \phi$
> ↗ See also: [Appendix C: Derived Numerology](appendix-derived-numerology.md) — all APU hardware constants ($Z_0, V_{snap}, V_{yield}, \phi_{yield}, \nu_{vac}, z_0, U_{kink}$, …) with full axiom traces
> ↗ See also: [Universal Constants Exchange (Vol 2 App F)](../vol2/appendices/app-f-solver-toolchain/universal-constants-exchange.md) — "currency exchange" framing for fundamental constants
> ↗ See also: `divergence-test-substrate-map.md` ξ_topo cascade (on sibling branch `analysis/divergence-test-substrate-map`, not yet merged to L3) — operational cascade where ξ_topo cross-citations land on test rows
