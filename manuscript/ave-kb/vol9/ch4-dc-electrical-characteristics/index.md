[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.4 DC Electrical Characteristics

Chapter 4 of the Vol 9 datasheet documents the substrate's canonical DC electrical primitives at the cold-lattice limit ($T \to 0$, $A_0 = 0$, $S(0) = 1$, no internal-boundary $\Gamma$). The chapter populates the engineers' Page-1 reference: eight substrate-primitive constants ($\varepsilon_0$, $\mu_0$, $Z_0$, $c_0$, $\ell_{node}$, $T_{EM}$, $\alpha$, $\xi_{topo}$) clustered into three coherent groups — vacuum impedance trio, propagation primitives, coupling primitives — each row carrying a canonical-source pointer to `src/ave/core/constants.py` + the canonical KB leaf where the substrate-physics derivation lives.

The chapter content is **Class B substrate-mechanism manifestation** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitives are introduced; the content consolidates the canonical engine constants and per-constant derivation leaves into datasheet DC-spec-table format. Per Grant 2026-05-28 directive, no constant in this chapter is framed as "engineered" or "chosen": the substrate is natural; engineering measures; AVE derives. Every numerical value traces to an engine-constant line in `src/ave/core/constants.py` (cited inline in the spec table).

## Primary canonical sources

| Source | Content |
|---|---|
| `src/ave/core/constants.py` lines 78-81 (`C_0`, `MU_0`, `EPSILON_0`, `Z_0`) | Vacuum impedance trio + cold-lattice EM wave speed |
| `src/ave/core/constants.py` lines 101, 164 (`ALPHA`, `ALPHA_COLD_INV`) | Fine-structure constant (CODATA + cold-lattice Golden-Torus derivation $4\pi^3 + \pi^2 + \pi$) |
| `src/ave/core/constants.py` lines 194, 206, 329-330 (`L_NODE`, `XI_TOPO`, `T_EM`) | Lattice pitch + topological transduction + EM string tension |
| CLAUDE.md INVARIANT-S2 (Axioms 1–4 + two-effective-wave-speeds clause + SYM/ASYM scaling) | Substrate-axiom anchor for every primitive |
| `manuscript/ave-kb/common/natural-units-cheatsheet.md` | Natural-units cheatsheet; four-base convention ($\ell_{node} = c = \hbar = m_e = 1$) + SI ↔ Native conversion table |
| `manuscript/ave-kb/common/translation-tables/translation-circuit.md` §1 (`clm-fy05jc`) | Six-row $\xi_{topo}$ EE↔mechanical identity |
| `manuscript/ave-kb/common/translation-tables/translation-circuit.md` §2 (`clm-eemap1`) | EE-as-substrate-native META framework; canonical methodology for the chapter's EE Translation Table |
| `manuscript/ave-kb/common/xi-topo-traceability.md` | $\xi_{topo}$ cross-domain traceability map + namespace de-collision ($\xi_{topo}$ vs Machian $\xi$) |
| `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` (`clm-0ktpcn`) | Cold-lattice $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ derivation (Golden Torus geometry; Theorem 3.1 cross-link) |
| `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md` | Bond TLM characteristic impedance $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ canonical derivation |
| `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` | Cosmic-LC-tank Q-factor at $S_{11}$-minimum Golden Torus operating point |
| `manuscript/ave-kb/vol4/claim-quality.md` `clm-i9l284` (solidity 0.90) | $\xi_{topo} = e/\ell_{node}$ Topological Conversion Constant canonical quality entry |
| `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` (`clm-3zz0f6`) | SYM-class $\alpha$-invariance under gravitational scaling (load-bearing for the chapter's two-effective-wave-speeds reference) |
| `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` (`clm-hp7nlm`) | $\delta_{strain}$ at $T_{CMB}$ — Cosserat-rotation-sector mass-gap thermal-mode-population ASYM (the thermal correction acknowledged in the $\alpha$ row but quantified in Ch.6) |

## Cross-volume invariant references

- **INVARIANT-S2 (Axioms 1–4)**: every spec-table row cites the source axiom.
- **INVARIANT-C2 ($\xi_{topo} = e/\ell_{node}$)**: cross-volume electromechanical transduction constant; canonical at the Ch.4 coupling-primitives cluster.
- **INVARIANT-N3 (Op-numbering)**: Op1 (Universal Impedance) and Op16 (Universal Wave Speed) cited as the cross-scale operator forms of $Z_0$ and $c_0$.

## Forward-pointers (Ch.4 → other Vol 9 chapters)

- **Ch.5 AC Electrical Characteristics**: $S(A_0)$-modulated effective parameters $\varepsilon_{eff}$, $\mu_{eff}$, $c_{EM}$, $c_{shear}$.
- **Ch.6 Temperature Characteristics**: Cosserat-Curie thermal-asymmetry δ_strain at $T_{CMB}$; TCC of substrate dielectric.
- **Ch.7 Saturation Characteristics**: Ax 4 kernel $S(A_0)$ characteristic curves; PONDER-05 (quartz 27.4% at ~30 kV) as a consistency-class material varactor analog of the kernel SHAPE — "$V_{DC}/V_{yield} = 0.687$" is a per-node ratio, not a vacuum-kernel reading (`vol4/claim-quality.md:51`).
- **Ch.8 Breakdown Characteristics**: $V_{snap}$, $V_{yield}$, $E_S$ Schwinger limit (downstream consequences of the cold-lattice DC primitives at finite-amplitude regimes).

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/04_dc_electrical_characteristics.tex` (canonical Vol 9 chapter file).

---
