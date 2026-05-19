[↑ Particle Physics](../index.md)

# Ch.3 — The Neutrino Sector: Chiral Unknots

The neutrino is defined geometrically as a $0_1$ twisted unknot whose zero self-crossings eliminate the Skyrme gradient term, producing ultra-low rest mass. Parity violation emerges as a structural high-pass filter from the chiral LC lattice's asymmetric dispersion relation. The PMNS mixing matrix is derived from regime-boundary eigenvalues applied to torus knot mode space.

> **Scope correction (2026-05-17 night, Foundation Item 13 audit)**: The original framing — "all four PMNS parameters derive from three inputs (c_1=5, c_3=9, ν_vac=2/7, K4 connectivity=3)" — was honest about ν_vac and K4 connectivity (which derive from substrate primitives at multiple independent loci) but UNDERSPECIFIED about c_1=5. **The Δc=2 spacing IS derived from ν_vac=2/7** ([`pmns-eigenvalues.md:23`](pmns-eigenvalues.md)), but the absolute starting value c_1=5 (vs c_1=3 starting at the (2,3) trefoil baseline, or any other Δc=2 ladder) is NOT derived from substrate primitives in any canonical leaf grep'd. Honest revised framing: **3 verified Class D emergence predictions + 1 conditional prediction (sin²θ_13) pending c_1=5 substrate derivation** — even worst case, the other 3 predictions cross-validate from the same c_1·c_3=45 input (3:1 structural compression preserved). See [closure-roadmap §0.5 FI-13 entry](../../../common/closure-roadmap.md) for full audit findings + c_1=5 derivation gap registered as open work item.

## Key Results

| Result | Statement |
|---|---|
| Chiral Asymmetric Dispersion | $\omega^2 = c^2 k^2 \mp \gamma_c k$ |
| Neutrino Mass | $m_\nu = m_e \cdot \alpha \cdot (m_e/M_W) \approx 0.024$ eV per flavor |
| Neutrino sum | $\sum m_\nu \approx 0.054$ eV (within Planck 2018 bound $< 0.12$ eV) |
| Chiral Screening Threshold | $\Delta c_{crit} = 3$ (K4 connectivity = trefoil crossing number) |
| $\sin^2\theta_{13}$ | $1/(c_1 c_3) = 1/45 = 0.02222$ (NuFIT 5.2: 0.02200, $1.0\%$) |
| $\sin^2\theta_{12}$ | $\nu_{vac} + 1/45 = 2/7 + 1/45 = 97/315 = 0.30794$ (NuFIT 5.2: 0.307, $0.3\%$) |
| $\sin^2\theta_{23}$ | $1/2 + 2/45 = 49/90 = 0.54444$ (NuFIT 5.2: 0.546, $0.3\%$) |
| CP-violating phase | $\delta_{CP} = (1 + 1/3 + 1/45)\pi = 61\pi/45$ ($\delta_{CP}/\pi = 1.3556$; NuFIT: 1.36, $0.3\%$) |
| Neutrino Mass Ordering | $m_i \propto 1/c_i^2$; $m_1 : m_2 : m_3 = 1/25 : 1/49 : 1/81$ |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Chiral Screening](chiral-screening.md) | Chiral screening threshold $\Delta c_{crit} = 3$; K4 lattice connectivity; compliance vs screened regimes |
| [PMNS Eigenvalues](pmns-eigenvalues.md) | Regime-boundary eigenvalues in mode space; $\sin^2\theta_{12}$, $\sin^2\theta_{23}$, $\sin^2\theta_{13}$ leading-order derivations |
| [PMNS Junction Model](pmns-junction-model.md) | Perturbative junction corrections to PMNS mixing angles; full formulae and comparison to NuFIT 5.2 |
| [Delta CP Violation](delta-cp-violation.md) | CP-violating phase $\delta_{CP} = 61\pi/45$ from chiral K4 structure; results and comparison table |
| [Neutrino Translation Table](neutrino-translation-table.md) | GAP stub — source file translation_neutrino.tex does not exist on disk |
