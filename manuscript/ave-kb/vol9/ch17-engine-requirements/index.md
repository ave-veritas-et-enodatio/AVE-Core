[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: leaf-as-index
no-claim: "Vol-9 synthesis routing stub for the engine-requirements chapter; consolidates documented engine-failure lessons into a simulator spec. No new substrate-physics claim — every requirement cites its canonical derivation home and its violating-engine lesson."
-->

# Ch.17 Engine Requirements for Faithful Simulation

Chapter 17 of the Vol 9 datasheet reads the datasheet as a specification for the *simulator*, not only for the substrate. It states what a numerical engine must implement, per datasheet line, to simulate the vacuum cell (the Ch.3 DOF/mode table) faithfully. Each requirement is mapped to (a) the datasheet line it enforces and (b) the documented engine failure that taught it.

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitives. Each row consolidates an already-documented engine-failure lesson (A-027 two-engine architecture; the V_ref double-count; the genesis-24 EMF detonation; the graft-v2 source-symmetry lesson) into datasheet-format engine-requirement rows.

## Synthesis content

- **Per-sector wave-speed modulation in the propagation step.** $c_{eff}(V)$ per sector in propagation, not only $Z(V)$ at scatter (A-027; canonical `two-engine-architecture-a027.md`).
- **An independent state carrier per DOF-table row.** Read-only projections (`V_ref`) are observables, never state (the double-count; `master_fdtd_phasor_bridge.py:16-17`).
- **Saturation/confinement/reflection as BOUNDARY conditions** ($\Gamma$, Op17-bounded), never bulk forces (the crystal-engine/graft-v2 CP10 boundary-localized-vs-bulk contrast: a $c_{eff}$ trap $\to \Gamma$-wall via $g_{front}$ confines with **no** detonation, $\Gamma_{core}\to-0.24$; the genesis-24 detonation is the EMF-pump lesson of the next row, **not** bulk-force confinement; `substrate-native-check` CP10).
- **Cross-sector couplings as CONSERVED Hamiltonian pairs** (source + back-reaction from one $H_{couple}$; energize-lock, no non-conservative pump — the EMF `k4_cosserat_coupling.py:550` lesson).
- **Source symmetry class must admit the target topology** (centrosymmetric source cannot select a chiral knot — graft-v2).
- **Conservation canaries on float64** (H-drift, $|\mathbf{L}|$ gates are the pump-vs-lock detectors); fixed $N$ across compared runs; alias-checked extractors with reliability gates **and representation-capability-validated at the sampling scale** (plant-$(2,3)$-at-de-novo-scale $\to$ read-$(2,3)$; minor radius $r \gtrsim 3$ cells — a TRUE $(2,3)$ reads back as $(2,2)$/garbage at $r\approx1.1$ cells, so de-novo $w_{pol}=0$ nulls are partly representation-limited per the extractor-poloidal-misread note); observers strictly read-only.
- **Regime-reachability**: the engine must reach the regime the test requires (bulk near-yield for rectification); sub-yield nulls are artifacts.

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex` (canonical Vol 9 chapter file)

---
