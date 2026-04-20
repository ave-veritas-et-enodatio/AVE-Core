# L3 Research Bibliography

**Purpose:** Running bibliography of citations that surface during the L3 electron-soliton research. Serves as the single source of truth for references across the Phase 0–N documents and as the skeleton for a formal bibliography when the research produces a publication.

**Discipline:**
- Add a citation when a claim in one of the `research/L3_electron_soliton/` docs invokes it.
- Add a citation when a relevant external work is identified but not yet read (mark **[to read]**).
- Keep entries in full BibTeX-adjacent form (author, title, venue, year, identifier — arXiv or DOI or both where possible).
- Keep per-entry "used in" field to cross-reference L3 doc sections.
- **Do not** auto-cite; Grant adjudicates which references are load-bearing.

---

## §1  Cosserat and micropolar mechanics

### [B1] Cosserat & Cosserat 1909
- **Citation:** Cosserat, E. & Cosserat, F. *Théorie des corps déformables*. Hermann, Paris, 1909.
- **Used in:** `00_` §10 ref [1]; `02_` §3 (kinematics framework).
- **Status:** Historical foundation. Read in secondary form (Eringen / Maugin).

### [B2] Eringen 1999
- **Citation:** Eringen, A. C. *Microcontinuum Field Theories I: Foundations and Solids*. Springer, New York, 1999. ISBN 978-0-387-98620-9.
- **Used in:** `00_` §10 ref [2]; `02_` §3 (constitutive relations); `03_` §2 (defect theory, Ch 5).
- **Status:** Standard modern reference. **[to read Ch 5 in full during Phase-1 wrap-up for the defect sections.]**

### [B3] Maugin 2013
- **Citation:** Maugin, G. A. *Continuum Mechanics Through the Twentieth Century*. Springer, 2013.
- **Used in:** `00_` §10 ref [3]. Historical/conceptual.
- **Status:** Secondary reference.

### [B4] Nowacki 1986
- **Citation:** Nowacki, W. *Theory of Asymmetric Elasticity*. Pergamon Press, 1986.
- **Used in:** `00_` §10 ref [4]. Wave propagation in Cosserat media.
- **Status:** Secondary reference. **[to read for Phase-3 wave-dispersion design.]**

---

## §2  Topological defects in continuum media

### [B5] Kléman & Friedel 2008
- **Citation:** Kléman, M. & Friedel, J. "Disclinations, dislocations, and continuous defects: A reappraisal." *Rev. Mod. Phys.* **80**, 61–115 (2008). DOI: 10.1103/RevModPhys.80.61.
- **Used in:** `00_` §10 ref [5]; `02_` §3.5; `03_` §2.
- **Status:** Foundational. **[to read for the defect-topology classification + relative-homotopy machinery in `03_` §2.]**

### [B6] Kleinert 1989
- **Citation:** Kleinert, H. *Gauge Fields in Condensed Matter*, vols. 1–2. World Scientific, 1989.
- **Used in:** `00_` §10 ref [6]. Dispiration defects, gauge-theoretic interpretation.
- **Status:** Secondary reference.

### [B7] Mermin 1979
- **Citation:** Mermin, N. D. "The topological theory of defects in ordered media." *Rev. Mod. Phys.* **51**, 591 (1979). DOI: 10.1103/RevModPhys.51.591.
- **Used in:** `00_` §10 ref [7]. Homotopy-group classification of defects.
- **Status:** Canonical. **[useful for `03_` §2 rigorous homotopy statement.]**

---

## §3  Faddeev-Skyrme solitons / Hopfions

### [B8] Faddeev 1976
- **Citation:** Faddeev, L. D. "Some comments on the many-dimensional solitons." *Lett. Math. Phys.* **1**, 289 (1976).
- **Used in:** `00_` §10 ref [8]. Knotted-soliton conjecture.
- **Status:** Historical. Secondary reference.

### [B9] Faddeev & Niemi 1997
- **Citation:** Faddeev, L. D. & Niemi, A. J. "Stable knot-like structures in classical field theory." *Nature* **387**, 58–61 (1997). DOI: 10.1038/387058a0.
- **Used in:** `00_` §10 ref [9]. Hopfion Lagrangian.
- **Status:** Load-bearing for Reading (a) framing. **[read for Phase-1 pressure-test; not read in full yet.]**

### [B10] Battye & Sutcliffe 1998
- **Citation:** Battye, R. A. & Sutcliffe, P. M. "Knots as stable soliton solutions in a three-dimensional classical field theory." *Phys. Rev. Lett.* **81**, 4798 (1998). arXiv:hep-th/9808129.
- **Used in:** `00_` §10 ref [10]. First numerical Hopfions.
- **Status:** Numerical baseline for Reading (a). **[to read for Phase-3 discretization comparison.]**

### [B11] Sutcliffe 2007 ⚠ CRITICAL
- **Citation:** Sutcliffe, P. M. "Knots in the Skyrme-Faddeev model." *Proc. R. Soc. A* **463**, 3001–3020 (2007). arXiv:0705.1468.
- **Used in:** `01_` §4 Reading (a); `05_` §2, §5 — pressure-test for Reading (b) ≡ Reading (a) equivalence (found non-equivalent).
- **Status:** Load-bearing for Reading (a); validation target for Reading (a) if adopted. **Primary reference for torus-knot Hopfion numerics.** **[to read in full before Phase 3 if Reading (a) is adopted.]**

### [B12] Hietarinta & Salo 2000
- **Citation:** Hietarinta, J. & Salo, P. "Ground state in the Faddeev-Skyrme model." *Phys. Rev. D* **62**, 081701 (2000). arXiv:hep-th/0005038.
- **Used in:** `00_` §10 ref [12]. Numerical method for Hopfion relaxation on cubic grids.
- **Status:** Methods reference for Phase-3 numerics. **[to read before Phase-2 discretization-design doc.]**

### [B13] Manton & Sutcliffe 2004 ⚠ CRITICAL
- **Citation:** Manton, N. S. & Sutcliffe, P. M. *Topological Solitons*. Cambridge Univ. Press, 2004. ISBN 0-521-83836-3.
- **Used in:** `00_` §10 ref [13]; `03_` §5 (modulus-space uniqueness argument, Ch 8 Skyrmion reference); `05_` §2.
- **Status:** Standard textbook. Ch 9 covers Hopfions. **[to read Ch 9 + Ch 8 (Skyrmions) for Phase-1 wrap-up existence/uniqueness formal proofs.]**

### [B14] Lin & Yang 2004
- **Citation:** Lin, F. & Yang, Y. "Existence of energy minimizers as stable knotted solitons in the Faddeev model." *Comm. Math. Phys.* **249**, 273–303 (2004). arXiv:math-ph/0312043.
- **Used in:** `03_` §3.5 (existence argument for Faddeev-Skyrme functional on R³).
- **Status:** Load-bearing for formal existence proof. **[to read for Phase-1 wrap-up queue item [4].]**

### [B15] Shabanov 2002
- **Citation:** Shabanov, S. V. "On a low-energy bound in a class of chiral field theories with solitons." *J. Math. Phys.* **43**, 4127 (2002). arXiv:hep-th/0202146.
- **Used in:** `03_` §3.5. Coercivity bound for Hopfion-type functionals.
- **Status:** Supporting. **[to read for queue item [4].]**

### [B16] Rauch et al. 1975
- **Citation:** Rauch, H., Treimer, W., & Bonse, U. "Test of a single crystal neutron interferometer." *Phys. Lett. A* **47**, 369–371 (1974). Also: Rauch et al. 1975 subsequent $4\pi$ experiments.
- **Used in:** `01_` §4 (Reading (a) discussion); my conversational explanation of spin-1/2 structure (2026-04-20).
- **Status:** Experimental evidence for spin-1/2 $4\pi$ closure. Not quoted in docs yet.

---

## §4  Electron-as-soliton proposals (prior art)

### [B17] Rañada 1989
- **Citation:** Rañada, A. F. "A topological theory of the electromagnetic field." *Lett. Math. Phys.* **18**, 97–106 (1989). DOI: 10.1007/BF00401864.
- **Used in:** `00_` §10 ref [14]. Hopfion electromagnetism.
- **Status:** Historical priority for electron-as-Hopfion style arguments.

### [B18] Irvine & Bouwmeester 2008
- **Citation:** Irvine, W. T. M. & Bouwmeester, D. "Linked and knotted beams of light." *Nat. Phys.* **4**, 716–720 (2008). DOI: 10.1038/nphys1056.
- **Used in:** `00_` §10 ref [15]. Experimentally realized Hopfion light configurations.
- **Status:** Experimental precedent. Relevant to Vol 4 Ch 11/Ch 13 falsification-and-engineering pathways. **[useful for AVE-framing doc when discussing concrete Hopfion realizations.]**

### [B19] Trueba & Rañada 1996
- **Citation:** Trueba, J. L. & Rañada, A. F. "Electromagnetic knots." *Eur. J. Phys.* **17**, 141 (1996). DOI: 10.1088/0143-0807/17/3/008.
- **Used in:** `00_` §10 ref [16]. Hopfion electromagnetism review.
- **Status:** Secondary.

### [B25] Williamson & van der Mark 1997 ⚠ CRITICAL DIRECT PRIOR ART
- **Citation:** Williamson, J. G. & van der Mark, M. B. "Is the electron a photon with toroidal topology?" *Annales de la Fondation Louis de Broglie* **22**, 133–160 (1997).
- **Used in:** Identified in chat 2026-04-20 as direct prior-art for electron-as-torus models.
- **Why it matters:** Proposes the electron as a confined electromagnetic wave (photon) wound around a closed toroidal path. Addresses spin-1/2 via the 720° phase-closure requirement — the same $4\pi$ spinor-cycle structure AVE uses in Ch 8's $\Lambda_{\text{vol}}$ derivation and in the C3 SU(2) embedding (`01_` §4). This is not Hopfion-literature abstract topology but a concrete physical model of the electron as a toroidal structure. Directly on-topic for the Reading (a) vs Reading (b) question: Williamson-van der Mark's toroidal-photon ansatz uses a single combined field (closer to Reading (a) Sutcliffe-style single-phase topology), but with explicit physical interpretation as an EM wave rather than an abstract S²-valued field.
- **Status:** **[to read — high priority.]** Likely shifts the Reading (a) vs Reading (b) balance: if Williamson-van der Mark's single-field toroidal-photon model matches AVE's ground state (not just topologically but dynamically), Reading (a) gains real prior-art legitimacy beyond pure-math Hopfion literature. Also potentially load-bearing for the separate L3 derivation of $\delta_{\text{strain}}$ (since Williamson-van der Mark's photon-as-electron identity ties the electron's $\alpha$ to photon-frequency content in a way that may illuminate the CMB-thermal coupling).
- **Authors:** John G. Williamson (University of Glasgow, Scotland — UK); Martin B. van der Mark (Philips Research, Netherlands).

---

## §5  Lattice-discretization for micropolar field theories

### [B20] Misra & Poorsolhjouy 2016
- **Citation:** Misra, A. & Poorsolhjouy, P. "Granular micromechanics based micromorphic model predicts frequency band gaps." *Continuum Mech. Thermodyn.* **28**, 215–234 (2016). DOI: 10.1007/s00161-015-0439-0.
- **Used in:** `00_` §10 ref [17]. Discrete-to-continuum bridging.
- **Status:** Relevant for Phase-2 K4 discretization design.

### [B21] Forest & Sab 1998
- **Citation:** Forest, S. & Sab, K. "Cosserat overall modeling of heterogeneous materials." *Mech. Res. Commun.* **25**, 449–454 (1998).
- **Used in:** `00_` §10 ref [18]. Graph-based discretization of Cosserat media.
- **Status:** Direct relevance to K4-graph discretization (Phase 2). **[to read for Phase-2 discretization-design doc.]**

---

## §6  Alternative topological structures — candidates for Reading (b) literature

*Added during Phase-1 equivalence check (`05_` §6, §7).* Reading (b) — the factorized SU(2) sector with U(1) fibre winding — has no direct Hopfion-literature precedent. Candidate fields for analogous structures:

### [B22] Anderson & Toulouse 1977 **[to read]**
- **Citation:** Anderson, P. W. & Toulouse, G. "Phase slippage without vortex cores: Vortex textures in superfluid ³He-A." *Phys. Rev. Lett.* **38**, 508 (1977). DOI: 10.1103/PhysRevLett.38.508.
- **Used in:** `05_` §6 — candidate precedent for SU(2)-fibre winding structure.
- **Status:** **[to read to assess relevance to Reading (b).]**

### [B23] Volovik 2003
- **Citation:** Volovik, G. E. *The Universe in a Helium Droplet*. Oxford Univ. Press, 2003. ISBN 0-19-850782-8.
- **Used in:** `05_` §6 — boojums, SU(2) textures, order-parameter spaces with fibre bundles.
- **Status:** **[to read Chs 12–14 for Cosserat-analogous field-theoretic defect structures.]**

### [B24] Tokura & Kanazawa 2020
- **Citation:** Tokura, Y. & Kanazawa, N. "Magnetic skyrmion materials." *Chem. Rev.* **121**, 2857–2897 (2020). DOI: 10.1021/acs.chemrev.0c00297.
- **Used in:** `05_` §6 — skyrmion-vortex composite structures in chiral magnets.
- **Status:** **[to read for modern skyrmion-vortex hybrid literature.]**

---

## §7  AVE-internal corpus

*Documented in `00_` §10 refs [19]–[31]. Not reproduced here to avoid duplication. See `00_scoping.md` §10 for the full list of AVE-internal references.*

---

## §8  Citations flagged but not yet classified

*Citations that surface in prose but that I have not yet placed in a section above. These are the "add later" backlog.*

### [B26] Eckhardt — "A Dark Future for Dark Matter" (tangential; to verify)
- **Citation:** Eckhardt, D. H. (verification needed — likely a monograph or review article arguing against dark-matter hypothesis in favor of an alternative-substrate or modified-gravity mechanism). Author affiliation: formerly Air Force Geophysics Laboratory (lunar gravimetry background).
- **Used in:** Identified in chat 2026-04-20 as tangential potentially-relevant prior art.
- **Why it matters (speculatively, pending verification):** AVE's Axiom-4 saturation kernel produces galactic-regime deviations from Newtonian gravity at the MOND scale (per operating-regimes phase diagram in `manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex` and cross-references in Vol 3). Any independent work arguing dark-matter phenomenology is better explained by vacuum/substrate effects rather than by a new particle is prior art that AVE should position against and cite — at minimum in the galactic-regime derivation chapters, potentially in L3 if the electron-soliton ground-state framework is eventually scaled up to regime-IV/V_snap phenomenology.
- **Status:** **[to verify + read]** — tentative pending web-search confirmation of title, venue, and thesis. Not load-bearing for Phase-1 L3. Tangential track.

---

## §9  Bibliography maintenance rules

- New L3 doc → scan it for new citations → add entries here with "used in" field.
- New citation in chat/conversation with Grant → add here if it's likely to be load-bearing.
- When a publication manuscript is eventually drafted, this file becomes the seed for the formal `references.bib`.
