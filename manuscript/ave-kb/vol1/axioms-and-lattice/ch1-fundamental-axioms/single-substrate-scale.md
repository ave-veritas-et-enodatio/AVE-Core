[↑ Ch.1 Fundamental Axioms](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-sw5oao]
-->

## The Single Substrate Scale — One Import, Five Algebraic Faces

<!-- claim-quality: clm-sw5oao -->
AVE's vacuum imports exactly **one** dimensionful lattice scale — the electron
mass $m_e$, entering through the calibration identity
$\ell_{node}\equiv\hbar/(m_e c)$ — and expresses five corpus quantities as
**algebraic faces** of that single import. Four of the five collapse to
$m_e c^2$ (the fifth, the inductor rest energy, is $\tfrac12 m_e c^2$, the
Virial-half):

> **[Resultbox]** *Five faces of one imported scale*
>
> | # | Face | Symbol / source | Reduces to |
> |---|---|---|---|
> | 1 | EM temporal cutoff | $\hbar\omega_C$, `OMEGA_C` $=$ `C_0/L_NODE` | $m_e c^2$ |
> | 2 | Node saturation energy | $(B_{snap}^2/2\mu_0)\,\ell_{node}^3$, `B_SNAP` | $m_e c^2$ |
> | 3 | Relativistic-inductor rest energy | $E_0=\tfrac12 L_0 I_{max}^2$ ([`relativistic-inductor.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md):28) | $\tfrac12 m_e c^2$ |
> | 4 | Compton length | $\ell_{node}\equiv\hbar/(m_e c)$, `L_NODE` | (the scale itself) |
> | 5 | Topological current ceiling | $I_{max}=\xi_{topo}\,c$, `XI_TOPO` $=$ `e/L_NODE` | $124.4$ A |

The **one-substrate ontology** reads these as the SAME substrate event — a
local lattice **saturation** (the Axiom-4 self-saturation kernel) — seen in its
EM (1), magnetic (2), inductive (3), topological (4,5) projections.

> ### Honest scope (frame-check 2026-06-22; `claim_survives = false`)
>
> This leaf is **CONSISTENCY-class**, and the value is an **ECHO** at every
> face. It is recorded as a **ONE-IMPORT ECONOMY** + an **EXPLANATORY
> ONTOLOGY**, explicitly **NOT a prediction and NOT an AVE-distinct chord**.
>
> 1. **PARAMETER ECONOMY (real, but economy ≠ prediction).** AVE imports a
>    single dimensionful scale and expresses the EM cutoff, magnetic-snap
>    field, inductor rest energy, Compton length, and current ceiling as
>    algebraic consequences of that one import; the SM imports the electron
>    Yukawa as one of $\sim$19+ independent parameters. That is a real
>    bookkeeping economy (fewer independent dials) — **but none of the five
>    faces is an independent measurement AVE postdicts.** They are
>    *definitions*, not *predictions*.
>
> 2. **ONTOLOGICAL UNIFICATION (explanatory, not predictive).** AVE asserts
>    the five are the same substrate event in different projections of one
>    Axiom-4 kernel. This is genuine **explanatory** differentiation worth
>    recording — but it is interpretive ontology, **not a numerically forced
>    relationship the SM cannot express**: QED *does* relate the Compton
>    length $\hbar/(m_e c)$ and the Schwinger field $m_e^2 c^3/(e\hbar)$
>    (`E_CRIT`) to $m_e$. The "same-mechanism story" is the AVE-distinct
>    *framing*, not an AVE-distinct *number*.
>
> **The value is an echo; the multi-face IDENTITY is definitional-by-construction,
> not a forward prediction.**
>
> **Forbidden framings** (must NOT appear in this leaf or downstream):
> "structural unification the SM lacks", "AVE forces these to coincide", "five
> independent quantities agree", "the SM has nothing relating its EM cutoff to
> $m_e$".

### Circularity (the value-level tautology)

At the **value** level the five appearances are a pure chain of definitions
rooted in the single literal `M_E`. In
[`constants.py`](../../../../../src/ave/core/constants.py) **only `M_E` is an
independent literal**; everything else is `M_E` downstream:

- `L_NODE = HBAR/(M_E*C_0)` — defined VIA `M_E`.
- `OMEGA_C = C_0/L_NODE` $\Rightarrow \hbar\,$`OMEGA_C` $=\hbar c/\ell_{node}=m_e c^2$ **identically**
  (the source comment at `OMEGA_C` states it: *"$\hbar\cdot$`OMEGA_C` $= m_e c^2 = 511$ keV exactly (since $\ell_{node}\equiv\hbar/(m_e c)$)"*).
- `B_SNAP = sqrt(2*MU_0*M_E*C_0**2/L_NODE**3)` — $m_e c^2$ is **inserted by hand** in the numerator (the defining equation $B^2/(2\mu_0)=m_e c^2/\ell^3$ solved for `B_SNAP`), so face (2) recovers its own input.
- `XI_TOPO = e/L_NODE`; $I_{max}=\xi_{topo}\,c$; and $L_0=\xi_{topo}^{-2}m_0$ (Topo-Kinematic map). Then $E_0=\tfrac12 L_0 I_{max}^2=\tfrac12(\xi_{topo}^{-2}m_0)(\xi_{topo}c)^2=\tfrac12 m_0 c^2$ — **the $\xi_{topo}$ factors cancel identically**; face (3) is true for ANY value of $\xi_{topo}$ or $\ell_{node}$, so it carries **zero information** about the substrate scale.

So **"all five $=m_e c^2$" is $m_e = m_e$ — a multi-definition tautology, not a
multi-quantity consistency.** This matches the standing corpus adjudication:
[`form-deriving-value-importing.md`](../../../common/form-deriving-value-importing.md)
classifies `m_e / ℓ_node` as **DEFINITIONAL** ("the anchor by which the lattice
is calibrated… an input *by construction*, not a value the substrate is asked
to select"), and the `M_E` block in `constants.py` flags the named
identification as **"substrate-canonical INPUT (not Class 2 axiom-emergence
from K4 + Cosserat primitives alone)."** This leaf is consistent with — not an
escalation of — those classifications.

> ⚠ **Coincidence-magnet tell (flag-don't-fix).** "Five faces of one scale" has
> the over-determination signature that the corpus flags as a coincidence
> magnet (same family as the $\tfrac12/\tfrac14$ and two-"3"s double-counts):
> multiple "independent" confirmations that are actually **one definition
> viewed five ways**. Read the five-face web as a self-consistency artifact,
> never as five corroborations.

### The SM contrast, scoped honestly

The honest differentiator is bookkeeping economy, **not** SM-distinctness of
the mechanism. The proposition "in the SM the electron mass is unrelated to any
vacuum/EM scale" is **overstated**: QED's $m_e$ is the IR pole of the dressed
propagator, the Compton wavelength $\hbar/(m_e c)$ is *the* QED length scale,
and the pair-production / Schwinger threshold $m_e c^2$ **is** a vacuum-EM
cutoff in QED — AVE's own `E_CRIT` is literally the Schwinger field. What the
SM does **not** do is **derive** $m_e$ from a lattice — **but neither does AVE**
(`M_E` is a hardcoded CODATA literal). So:

- **VALUE**: echo, peer-with-QED (both import $m_e$). No SM-distinct content.
- **ECONOMY**: one imported dial vs $\sim$19+ — real, but economy ≠ prediction.
- **ONTOLOGY**: same-substrate-event story — genuine explanatory differentiation,
  interpretive not forced.

### The graduation lever

This leaf graduates from CONSISTENCY/economy to a genuine **chord** only if the
single scale is **derived from bare substrate** so that $m_e$ (equivalently
$\ell_{node}$) becomes a forward output rather than an import. That is the
**same open theorem** that would un-condition the photon dispersion quartic —
the topological-decoupling / scale-from-substrate theorem tracked at
[`k4-bloch-dispersion-quartic.md`](../../../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md)
(`clm-k4d4ph`, weak-C no-zone-edge premise, gate `wejkhvnfb`). Until that
theorem closes, the multi-face identity is definitional and the value is an
echo.

### Cross-links (the five appearance leaves)

- (1) EM cutoff $\omega_C$ + (4) Compton $\ell_{node}$ — [`calibration-cutoff-scales.md`](calibration-cutoff-scales.md) (`clm-5xon03`, `clm-unk0bd`); [`k4-bloch-dispersion-quartic.md`](../../../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md) §4 (`clm-k4d4ph`, the 511 keV cutoff ECHO + the spatial quartic chord, DISTINCT mechanisms).
- (2) magnetic-snap field `B_SNAP` — `constants.py` `B_SNAP` (Axiom-4 magnetic-sector saturation threshold).
- (3) inductor rest energy $E_0=\tfrac12 L_0 I_{max}^2=\tfrac12 m_0 c^2$ — [`relativistic-inductor.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md):28 (`clm-p5cf3t`).
- (5) current ceiling $I_{max}=\xi_{topo}c$ — [`relativistic-inductor.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md):15 ($I_{max}\approx124.4$ A).
- DEFINITIONAL classification of $m_e/\ell_{node}$ — [`form-deriving-value-importing.md`](../../../common/form-deriving-value-importing.md) (`m_e / ℓ_node` row).

### Driver

[`src/scripts/vol_1_foundations/single_scale_consistency.py`](../../../../../src/scripts/vol_1_foundations/single_scale_consistency.py)
imports the constants BY SYMBOL (`OMEGA_C, B_SNAP, L_NODE, XI_TOPO, M_E, C_0,
HBAR, MU_0, e_charge`), computes the five faces, asserts each reduces to its
definitional target to $10^{-12}$, and **labels** each as DEFINITION-CIRCULAR
(CD) vs INDEPENDENTLY-SET (IS) — exactly one quantity (`M_E`) is IS. It is a
self-consistency check (validate-on-known: $m_e c^2 \to 510.999$ keV), **not** a
derivation of $m_e$.

---

> **Quality, depends-on, and solidity for `clm-sw5oao` live in the volume claim
> register** ([`../../claim-quality.md`](../../claim-quality.md)).
