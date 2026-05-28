[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.16 Cross-Volume Reference Index

Chapter 16 of the Vol 9 datasheet is the indexical lookup chapter: every substrate parameter cataloged in Chs.~2--12, every engineering observable that maps to a substrate primitive, and every by-volume contribution from Vols~0--6 routes to its canonical-derivation location through this chapter. No new substrate-physics is derived here — it is a navigation map.

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3: every entry is a cross-reference to a canonical leaf in Vols~0--6 or the `common/` cross-cutting subtree. The chapter consolidates the citation graph that Vol~9 Chs.~1--15 build incrementally into a single fast-lookup index.

## Primary canonical sources

Vol 9 Ch.16 cross-references the entire substrate canonical corpus. Load-bearing canonical leaves the index points to (representative set; the full lookup tables in the LaTeX chapter cover the complete catalog):

| Source | Content |
|---|---|
| CLAUDE.md INVARIANT-S2 (Axioms 1–4) | Axiomatic substrate definitions; mirror of `common_equations/eq_axiom_[1-4].tex` |
| `vol1/operators-and-regimes/ch6-universal-operators/reflection-coefficient.md` (`clm-gdd70j`) | Op3 reflection coefficient |
| `vol1/operators-and-regimes/ch7-regime-map/four-regimes.md` (`clm-b2anl4`, `clm-2dwzib`, `clm-82dxbj`) | Four-regimes partition |
| `vol1/ch8-alpha-golden-torus.md` (`clm-0ktpcn`) | Golden-Torus α cold-lattice closure |
| `vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md` (`clm-ezai5b`, `clm-8nkvwy`) | Pair production + SYM/ASYM scaling + two-effective-wave-speed |
| `vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md` (`clm-salw2h`) | FM-kink spin-½ derivation |
| `vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md` (`clm-8c3yhs`) | $(2,3)$ trefoil electron uniqueness |
| `vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md` (`clm-5zuo7g`) | Cosserat couple-stress + $l_c$ weak-force range |
| `vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md` (`clm-x19btt`) | $\nu_{vac} = 2/7$ axiomatic identity |
| `vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` (`clm-3zz0f6`) | SYM-class α-invariance proof |
| `vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md` (`clm-wx5324`) | Cosmic horizon + $H_\infty$ |
| `vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` (`clm-hp7nlm`, `clm-009nkt`) | Cosserat-Curie δ_strain mechanism |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md` | $Z_0$ canonical |
| `vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md` (`clm-0vxzfu`, `clm-trgqtf`) | Two-threshold $V_{snap}/V_{yield}$ |
| `vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md` (`clm-wzezvt`) | HOPF / falsification programme |
| `vol5/molecular-foundations/organic-circuitry/electromechanical-transduction-constant.md` (`clm-i9l284`) | $\xi_{topo} = e/\ell_{node}$ canonical |
| `common/translation-tables/translation-circuit.md` (`clm-fy05jc`, `clm-eemap1`) | EE-as-substrate-native META framework |
| `common/omega-freeze-cosmic-grain-cascade.md` (`clm-dsb560`, `clm-a7cbqq`, `clm-pe8lpx`) | $\hat{\Omega}_{freeze}$ + $u_0^*$ canonical |
| `common/trampoline-framework.md` | Cosserat micro-inertia PDEs; rotation-sector mass-gap |
| `common/operators.md` | Op1--Op21 universal operator catalog |

## Companion repositories

Per the AVE-APU naming-collision fix landed with this PR (recommendation a):

- **AVE-APU** (Axiomatic Processing Unit) — hardware-validation companion repository at sibling-repo scope. Documents $V_{snap}$, $V_{yield}$, $\rho_{kink}$, $P_{drag}$ at hardware-implementation scope. **Note**: legacy framing labeled AVE-APU as "Volume 9: Axiomatic Processing Unit (Experimental Repository)"; that label is retired with the launch of Vol 9 The Vacuum Datasheet (AVE-Core). AVE-APU is now a sibling companion repository, not a numbered volume of AVE-Core. The Vol 9 number is reserved for the Vacuum Datasheet.
- **AVE-PONDER** — bench-scale PONDER-05 falsification hardware (Vol 9 Ch.15 §PONDER-05).
- **AVE-HOPF** — bench-scale HOPF-01 chiral-antenna falsification hardware (Vol 9 Ch.15 §HOPF-01).

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/16_cross_volume_reference.tex` (canonical Vol 9 chapter file). Contains two main `longtable` lookups (Parameter → Canonical Source; Observable → Substrate Mechanism), the by-volume contribution map (Vol 0 through Vol 6 + common), and the companion-repository naming disambiguation.

---
