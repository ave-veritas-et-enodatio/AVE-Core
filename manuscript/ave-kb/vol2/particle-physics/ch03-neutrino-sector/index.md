[↑ Particle Physics](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [7o8clt, rji99i]
-->

# Ch.3 — The Neutrino Sector: Helical Torsional Screw Defects

The neutrino is defined geometrically as a **pure torsional screw dislocation** — a propagating helical coil in the Cosserat (torsional) sector of the lattice. Its topology is an **open helix with $c$ turns** (paired with the baryon torus-knot ladder: $c = 5, 7, 9$ for the three flavors), *not a closed loop*. Charge neutrality follows from **sector separation**: the neutrino is a pure torsional excitation, not an electromagnetic one, and therefore carries no electromagnetic charge by construction (the EM and Cosserat torsional sectors are distinct lattice degrees of freedom; coupling between them enters only via the dielectric compliance factor $\alpha$). Mass suppression by $\alpha \cdot (m_e/M_W)$ follows from the Cosserat-to-translational coupling ratio multiplied by the dielectric compliance. Parity violation emerges as a structural high-pass filter from the chiral LC lattice's asymmetric dispersion relation. The PMNS mixing matrix is derived from regime-boundary eigenvalues applied to the $c = 5, 7, 9$ torsional-mode space, yielding all four PMNS parameters from three inputs: the torus knot crossing numbers ($c_1 = 5$, $c_3 = 9$), the vacuum Poisson ratio ($\nu_{vac} = 2/7$), and the K4 lattice connectivity (3).

> **Corrigendum (2026-05-06 session):** Earlier editions described the neutrino as a "$0_1$ twisted unknot" (closed loop), tracing to an older Faddeev-Skyrme zero-crossings derivation of mass suppression in [`03_neutrino_sector.tex`](../../../../vol_2_subatomic/chapters/03_neutrino_sector.tex). The closed-loop framing has been **superseded** by the Cosserat torsional screw-dislocation model, which (a) explains charge neutrality cleanly via sector separation, (b) is corroborated by recent 3D model output showing the multi-turn helical structure, and (c) is consistent with the Vol 2 Ch 6 particle-zoo classification ([`06_electroweak_and_higgs.tex`](../../../../vol_2_subatomic/chapters/06_electroweak_and_higgs.tex) line 291: *"open helix with $c$ turns... not a closed loop"*). Any remaining "twisted unknot" prose in cross-references should be read as the obsolete framing. The neutrino body-topology question is therefore distinct from — and unrelated to — the electron body-topology question tracked at `trf3bd` / `unk0bd`: neutrinos are not closed-body solitons in either the unknot or trefoil sense; they are open helical screw defects in a different sector entirely.

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
