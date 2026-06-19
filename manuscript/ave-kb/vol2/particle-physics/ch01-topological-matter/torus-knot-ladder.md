[↑ Ch.1 — Topological Matter](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-k6olj8]
-->

## The Torus Knot Phase Winding Ladder

The $(2,q)$ torus knots classify the phase winding number of stable topological defects. Each odd crossing number $q$ defines a unique 🔴 *[dimensional-provenance relabel 2026-06-08 — LADDER-LEVEL ROOT; the per-particle leaves inherit from here]* ~~soliton confinement radius~~ **dimensionless soliton coupling-budget ratio** $r_{opt} = \kappa_{FS} / q$, where $\kappa_{FS} = 8\pi$ is the cold Faddeev--Skyrme coupling constant — a **pure geometric (dimensionless) constant** (`src/ave/core/constants.py:683-687`), so $r_{opt}$ is a **pure number, NOT a length** (the $\ell_{node}$ units previously attached to it were spurious). It is the fraction of the total coupling allocated per crossing. The ladder is:

| $(2,q)$ phase portrait | $q$ | $r_{opt}$ (dimensionless) | Gauge Symmetry | Particle (real-space body) |
|---|---|---|---|---|
| $(2,3)$ trefoil ($3_1$) | 3 | $8.317$ | SU(2) | Electron ($0_1$ unknot) |
| $(2,5)$ cinquefoil ($5_1$) | 5 | $4.990$ | SU(3) | Proton ($6^3_2$ Borromean) |
| $7_1$ knot | 7 | $3.564$ | SU(4) | $\Delta(1232)$ |
| $9_1$ knot | 9 | $2.772$ | SU(5) | $\Delta(1600)$ |
| $11_1$ knot | 11 | $2.268$ | --- | $\Delta(1900)$ |
| $13_1$ knot | 13 | $1.919$ | --- | $N(2190)$ |

The crossing number $q$ constrains the phase gradient by absorbing a fraction of the total coupling; the $r_{opt}$ column is the **dimensionless coupling-budget ratio, NOT a length** (these are pure numbers, not multiples of $\ell_{node}$ — neither the electron at "$8.317$" nor the proton at "$4.990$" is a real-space $8\,\ell_{node}$ / $5\,\ell_{node}$ extended object; the only measured baryon size is the sub-node proton $D_p = 0.841$ fm, $\approx 460\times$ smaller than $\ell_{node} = 386$ fm). Higher $q$ gives a smaller dimensionless budget ratio. The proton's $(2,5)$ phase portrait gives $r_{opt} = \kappa_{FS}/5 \approx 4.99$ (dimensionless). **Real-space vs phase-space:** Rolfsen names ($3_1$, $5_1$, …) label $(2,q)$ **phase-space winding portraits** on the bond-pair LC tank, not real-space body knots (electron body = $0_1$ unknot; proton body = $6^3_2$ Borromean).

**Stale-value fix (2026-06-19):** the $9_1$/$11_1$/$13_1$ ($c=9$/$11$/$13$) rows above were updated $\Delta(1620) \to \Delta(1600)$, $\Delta(1950) \to \Delta(1900)$, $N(2250) \to N(2190)$ to match the adjudicated 2026-05-18 walk-back on the canonical ch02 baryon leaf ([`../ch02-baryon-sector/torus-knot-ladder-baryons.md`](../ch02-baryon-sector/torus-knot-ladder-baryons.md), "Stale-framing correction (2026-05-18 walk-back)"; both carry `clm-k6olj8`). The driver `baryon_ladder_pdg_2024_anchor.py` confirms $(2,9)\to\Delta(1600)$ at $+0.779\%$, $(2,11)\to\Delta(1900)$ at $+1.876\%$, $(2,13)\to N(2190)$ at $+4.506\%$. *(The $c=11$/$c=13$ rows were previously flagged-not-fixed here pending review; aligned 2026-06-19 in lockstep with the manuscript twin `vol_2_subatomic/chapters/01_topological_matter.tex` per the same walk-back — value corrections, not new claims.)*

> 🔴 **SCOPE FLAG (2026-06-19, crossing-ladder-overclaim walk-back):** This $(2,q_{odd})$ ladder classifies the **$S=0$ $N/\Delta$ single-Regge sector** winding only. Strange baryons ($\Lambda, \Sigma, \Xi, \Omega$) and **all mesons** are **off-ladder and NOT natively derived** (open GAP). The integer-$q$ classification and the odd-$q$-only / no-$(2,4)$ link-exclusion are genuine structural chords and are preserved; no row may be read as covering "all baryons / all matter". 🔴 **FLAG (cold-vs-thermal convention — surfaced, not harmonized):** the table values use the **thermal** $\kappa_{FS} = 8\pi(1 - 1/(14\pi^2)) \approx 24.951$ from `ave.core.constants` (proton $\to 4.990$), whereas the canonical proton leaf `../ch02-baryon-sector/proton-identification.md` quotes the **cold** $8\pi/5 \approx 5.03$; both are dimensionless and the difference is purely the thermal-softening convention, not a value error — flagged for adjudication. Zero empirical fits.

---
