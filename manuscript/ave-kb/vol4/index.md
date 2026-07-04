[↑ AVE Knowledge Base](../entry-point.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-0vxzfu, clm-1eg13f, clm-4r4jiy, clm-5s5b0d, clm-6t3p6x, clm-7tynm2, clm-8nkvwy, clm-9sujp8, clm-acgyr1, clm-baoa36, clm-bdualb, clm-c54kdd, clm-cbwd77, clm-cltls0, clm-clvchn, clm-cwjd8t, clm-fd1e7a, clm-fgo20a, clm-fh6w3y, clm-fofwr1, clm-fuajdb, clm-gv1wu4, clm-gvn4r1, clm-gw2wgc, clm-h55fy1, clm-hd9bee, clm-i02mhk, clm-i9l284, clm-iz3svl, clm-k4d4ph, clm-k9up5c, clm-kezk9z, clm-kl1ern, clm-n3un96, clm-o2shcn, clm-oiw6cb, clm-om0rtq, clm-p12mem, clm-p2tp9i, clm-p5cf3t, clm-pp3qwf, clm-pvlas1, clm-qagkgy, clm-qsgl7d, clm-qx9bb8, clm-rtdmsn, clm-to41c7, clm-trgqtf, clm-u462e4, clm-ui3m8a, clm-v6ti0v, clm-vca7r1, clm-vjv4zf, clm-wcoul2, clm-wzezvt, clm-ydksh6, clm-yr6tu4, clm-zp4kqr, clm-zp7bds]
subtree-experiments: [exp-0n5p16, exp-1ddtr0, exp-1up5ww, exp-6kwkx7, exp-71uhr0, exp-742kv5, exp-7jekc6, exp-ct4cts, exp-onqclb, exp-po1a0v, exp-rth12t, exp-v6nzcq]
bootstrap: true
-->

> ⛔ **Bootstrap.** Leaves are canonical; this index and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this volume, load [`./claim-quality.md`](./claim-quality.md) and [`../claim-quality.md`](../claim-quality.md). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.

# Vol 4: Applied Vacuum Engineering

Volume 4 translates the AVE theoretical framework into engineering practice. It establishes the Vacuum Circuit Analysis (VCA) framework — an exact dimensional isomorphism between continuum spatial mechanics and electrical network theory via $\xi_{topo} \equiv e/\ell_{node}$ — then applies it to derive falsifiable experimental programs (HOPF-01 chiral antenna, PONDER-01 ponderomotive thruster) and advanced applications (metric-catalyzed fusion, topological SMES, quantum computing, active metamaterials).

> **Repo scope note.** Hardened hardware build programs (PONDER-05, full HOPF-01 build artifacts, torsion metrology) are maintained in a separate private repository within the `ave-veritas-et-enodatio` GitHub organization. This index covers the theoretical and falsification material that lives in this repo; cross-repo content is not surfaced here.

## Key Results

| Domain | Key Result |
|---|---|
| [Circuit Theory](circuit-theory/index.md) | $\xi_{topo} \equiv e/\ell_{node}$; topo-kinematic identity; nonlinear constitutive models |
| [Falsification](falsification/index.md) | Complete experimental programme; Sagnac-RLVE ($\Delta\phi \approx 2.07\,\text{Rad}$); tabletop projects (CLEAVE-01 through TORSION-05); $\sqrt{\alpha}$ yield limit |
| [Future Geometries](future-geometries/index.md) | High-Q chiral impedance antenna; K4-TLM Diamond lattice simulator (unitary to machine epsilon); six CEM methods mapped to AVE lattice |
| [Simulation](simulation/index.md) | SPICE netlists: leaky cavity particle decay, autoresonant PLL Schwinger bypass, Sagnac inductive drag; Universal AVE_VACUUM_CELL subcircuit; SPICE netlist compiler |

## Domains

| Domain | Summary |
|---|---|
| [Circuit Theory](circuit-theory/index.md) | Topo-kinematic identity ($\xi_{topo}$); six-row translation table; nonlinear constitutive models (varactor, relativistic inductor, TVS); $Z_0$ from discrete LC ladder; IMD spectroscopy; solver selection; chiral acoustic rectification thrust; operating regimes; V_YIELD/V_SNAP threshold guide; dark wake; metric streamlining. |
| [Falsification](falsification/index.md) | Experimental falsification programme: Sagnac-RLVE ($\Delta\phi \approx 2.07\,\text{Rad}$, $\Psi = 7.15$); tabletop projects (CLEAVE-01, HOPF-02, ROENTGEN-03, ZENER-04, TORSION-05); $\sqrt{\alpha}$ yield limit ($V_{yield} = 43.65\,\text{kV}$, $m_{max} = 1.846\,\text{g}$); YBCO phased array (2.5 metric tons/m$^2$); vacuum impedance mirror; EE Bench dielectric plateau ($E_{yield} = 1.13 \times 10^{17}\,\text{V/m}$); PONDER-01 asymmetric thrust ($F \propto V^2 f^2$); torus knot baryon predictions; birefringence ~~$E^4$~~ **COEFFICIENT** discriminator (both AVE and QED $E^2$-leading; ratio $\sim 10^6\times$ QED — clm-pp3qwf, Rule-12 correction 2026-06-04, the $E^4$-vs-$E^2$ slope was a retracted false falsifier). |
| [Future Geometries](future-geometries/index.md) | High-Q chiral impedance antenna (Chiral FoM $= Q_u \times \alpha\,pq/(p+q) \times \eta_{\mathcal{H}}$; $(7,11)$ optimal; YBCO $1{,}300\times$ gain); six CEM methods mapped to AVE lattice (MoM $\leftrightarrow$ circuit equation, FDTD $\leftrightarrow$ LC grid, FEM $\leftrightarrow$ $\omega^2 LC = 1$, TLM $\leftrightarrow$ most direct isomorphism); K4-TLM Diamond lattice simulator ($S^{(0)}_{ij} = \frac{1}{2} - \delta_{ij}$, unitary to machine epsilon); open-universe PML boundaries. |
| [Simulation](simulation/index.md) | SPICE circuit simulations: leaky cavity particle decay (LC tank at $V_{yield}$, RC-discharge half-life); autoresonant PLL Schwinger bypass ($C_{eff}(V)$ detuning, behavioral PLL); Sagnac inductive drag (50-node directional LC ring); hardware netlists (EE Bench $C_{eff}$ plateau, PONDER-01 cascaded Air/FR4 stack at 100 MHz). |

---
