[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.15 Falsification Tests

Chapter 15 of the Vol 9 datasheet documents the substrate-physics falsification programme. Every load-bearing substrate-physics claim in this datasheet is tied to at least one bench-falsifiable or observational kill-switch. Vol 9 is a synthesis chapter — no falsification entry originates here; each is routed to its canonical leaf in the cross-volume falsification index.

## Canonical cross-volume home

The canonical cross-volume falsification catalog lives at:

> → Primary: [Appendix: Unified Index of Experimental Falsifications](../../common/appendix-experiments.md) — INVARIANT-S3 cross-volume canonical home (clm-t5ybqw)

> → Primary: [Divergence-test substrate map](../../common/divergence-test-substrate-map.md) — operational tracking layer (33 rows: A1-HOPF, A2-SAGNAC, B7-PONDER-05, C15-CLEAVE-01, C17-PROTOCOL-11-SAGNAC-WIND, …)

## Per-test canonical leaves cited in the chapter

### Bench-scale kill-switches

- **PONDER-05** DC-biased quartz, 27.4% $\varepsilon_{eff}$ collapse at ~30 kV — ⚠ **consistency-class material varactor analog of the kernel SHAPE, NOT a vacuum-kernel kill-switch** (2026-06-04 per-node-conflation correction): $V_{DC}/V_{yield}$ is a **per-node** ratio, and at 30 kV across real quartz the vacuum per-node $A_0 = 10^{-7}$–$10^{-10}$ → vacuum collapse ~0. The 27.4% is the quartz material's own voltage-coefficient; the vacuum-kernel falsifier is facility-class ($\sim 8\times10^{16}$ V/m). Cascade to Ax4 DECOUPLED (a null quartz effect falsifies quartz dielectric data, not the vacuum kernel). Per `vol4/claim-quality.md:51`.
  - [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) — substrate-physics derivation (the §13/§14 amplitude-shape edifice anchors on $a = 0.687$ as the operating point — see borderline-flag note in the 2026-06-04 corrections result doc)
  - [`vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md`](../../vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md) — open-source PCBA build guide
  - Divergence-test row B7-PONDER-05 (reclassified consistency-class)
- **HOPF-01** chiral antenna $S_{11}$ torus-knot shift ($\Delta f/f = \alpha\cdot pq/(p+q)$):
  - [`vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md`](../../vol4/falsification/ch11-experimental-bench-falsification/open-source-hardware.md) (clm-wzezvt)
  - [`vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md`](../../vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md) — HOPF-02 mitigation of pilot-board mutual-coupling confound
  - Divergence-test row A1-HOPF
- **Sagnac-RLVE** rotational lattice mutual-inductance ($\Psi_{W/Al} = 7.15$) — **RETIRED forward "kill-switch" → corroborative-null (2026-06-03 audit)**; surviving piece is the paired W-vs-Al $\Psi$ self-consistency scaling check (Earth-as-rotor $+7\times10^{-4}$ bias excluded by RLG geodesy; `AVE-PONDER/research/2026-06-03_sagnac-rlve-fog-question-verdict.md`):
  - [`vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md`](../../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) (exp-rth12t status pending; strengthens clm-qx9bb8; scope-correction header 2026-06-03)
  - Divergence-test row A2-SAGNAC
- **CLEAVE-01** femto-Coulomb electrometer ($\xi_{topo}$ kill-switch):
  - [`vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md`](../../vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) (clm-ydksh6, exp-742kv5 status pending)

### Right-handed neutrino joint kill-switch

- [`vol4/falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md`](../../vol4/falsification/ch11-experimental-bench-falsification/epistemology-of-falsification.md) (clm-gw2wgc, clm-om0rtq, clm-pp3qwf)
- [`vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md`](../../vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md) (mirror)
- [`vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md`](../../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md) (clm-gw2wgc)
- [`vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm — joint constraint via $\gamma_c$)

### Null-result tests

- **Quasar α-variation (SYM-class null):** [`vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) (clm-3zz0f6)
- **Schwinger pair production at $E_S$:** [`vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md`](../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) (clm-ezai5b); [`vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md`](../../vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md) (clm-lj4ok5)
- **Vacuum birefringence COEFFICIENT discriminator** (~~$E^4$ vs $E^2$ slope~~ retracted false-falsifier; both $E^2$-leading, ratio $\sim 10^6\times$ QED — Rule-12 correction 2026-06-04): [`vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md`](../../vol4/falsification/ch11-experimental-bench/epistemology-kill-switches.md) (clm-pp3qwf)
- **Static-Sagnac galactic-wind anisotropy (corroborative null):** [`vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md`](../../vol4/falsification/ch11-experimental-bench-falsification/sagnac-parallax.md); [`vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md); divergence-test row C17-PROTOCOL-11-SAGNAC-WIND
- **GRB photon dispersion (Trans-Planckian discriminator):** [`vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md`](../../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md) (clm-gw2wgc)
- **Cosmic chirality 8-channel axis:** [`common/omega-freeze-cosmic-grain-cascade.md`](../../common/omega-freeze-cosmic-grain-cascade.md) (clm-dsb560, clm-a7cbqq, clm-pe8lpx, clm-fndptx)

### Three-route $u_0^*$ falsifiability

- [`common/omega-freeze-cosmic-grain-cascade.md`](../../common/omega-freeze-cosmic-grain-cascade.md) §1 (clm-dsb560)
- `src/ave/core/constants.py` header preamble lines 18–24 (three-route framework commitment)
- Vol 9 Ch.12 cosmological characteristics §three-routes

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/15_falsification_tests.tex` — chapter populated 2026-05-28 (Wave 3 of Vol 9 buildout). Synthesis chapter; no substrate-physics derivation originates here. All canonical-leaf cross-references resolve to the per-test sources listed above.

## Evidence-framing discipline

Per `ave-evidence-framing-discipline`: no entry in this chapter is framed as "validated" or "confirmed". Status uses the bench-discipline vocabulary:

- "Not yet observed" — predicted observable not detected at any current bound
- "Current bounds consistent with prediction" — existing data within substrate-predicted range (typically null where substrate predicts null)
- "Pending bench measurement" — apparatus in fabrication or paper-stage; first measurement not yet performed
- "Predicted at $E_S$; terrestrial $E$ inaccessible" — substrate positive prediction applies at unreachable regime; current observation is the predicted null

---
