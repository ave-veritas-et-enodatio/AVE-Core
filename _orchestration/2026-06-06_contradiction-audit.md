# Corpus contradiction audit (2026-06-06)

**Trigger:** Grant — "fully audit the work and identify the list of corpus contradictions we should tackle," following the open/short-seam resolution.
**Method:** 3 read-only `ave-auditor` agents (curated-backlog / foundations-particle / gravity-cosmology+cross-repo), each carrying the session meta-lens: *a sign/label/convention disagreement is a contradiction only if the quantity is an INVARIANT, not a COORDINATE.* Every finding grep/Read-verified at file:line. Categories: **(a)** genuine physics conflict · **(b)** invariant-vs-coordinate confusion (doc-reconcile) · **(c)** stale claim · **(d)** cross-leaf drift.

**Top-line:** the corpus is materially healthier than the seam-memory implied — **5 memory-seams are already resolved**. Of the genuinely-open items, only **2 are category-(a) physics forks** (cardinal √2, PONDER scaling); the rest are stale-doc / drift / cross-repo-lag.

---

## ✅ RESOLVED (memory-stale — update the memory entries, NOT the corpus)

| Seam | Resolution | Memory to update |
|---|---|---|
| gravity-PPN (9/7)-light-deflection | W1/W2 relabel landed (PR #90/#91/#92); (9/7) kept for C11 matter-wave parallax, light-deflection corrected to 2/7, fully propagated | `project_gravity_ppn_coherence` → RESOLVED |
| three /7 couplings (1/7,2/7,9/7) | coherent — three projections of one ε₁₁ | (same) |
| (2,5) muon-vs-proton | FI-13 (2026-05-18): muon-(2,5) retracted (muon=(2,3)+Cosserat torsion); proton-(2,5) canonical | (covered) |
| 720° real-space vs (2,3) phase-space | correctly kept in separate coordinate systems | — |
| Op3-vs-Op17 | clean throughout (prereg slip never propagated) | — |

---

## 🔴 OPEN backlog (ranked: load-bearing × effort)

| # | Item | Cat | Bearing | Resolver | Key file:line |
|---|---|---|---|---|---|
| 1 | **Cardinal `v=c√2` ontology** — sold as "Axiom-1 physical signature" (`:11`) AND "continuum-vanishing lattice artifact" (`:50`); downstream keeps only the physical framing, against emergent-Lorentz `(qℓ)⁴` (first anisotropy is quartic) | a | HIGH | **Grant (physics)** | `vol1/.../photon-propagation-baseline.md:11,50`; `preferred-frame-and-emergent-lorentz.md:40,50`; `cubic-k4-empirical-anisotropy.md:30,80` |
| 2 | **AVE-Protein impedance-folding stale-positive** — `main` README + B4 matrix claim it works; verified live-fire **negative** sits on unmerged branch; "Op14 cross-sector cascade" is **vapor** | c | HIGH | **Grant (Q-PROTEIN-21)** + impl | `AVE-Protein/README.md:1,11,13`; `divergence-map:449,535`; neg @ unmerged `2026-06-05_impedance-folding-kinematics-investigation.md` |
| 3 | **Op-namespace collision** — INVARIANT-N3 `Op2/Op8/Op9` (CLAUDE.md) ≠ Vol 1 Ch 6 `Op2/Op8/Op9`; self-flagged | d | HIGH | **Grant** + impl | `common/operators.md:23-25`; `CLAUDE.md` INVARIANT-N3 |
| 4 | **single-bond vs bond-pair electron** — both terms in `electron-identification.md`; `pair-production:45` ("flux tube **is the bond** between two saturated nodes") likely reconciles, unstated | b/d | MED-HIGH | **Grant (physics)** | `electron-identification.md:23,81,96`; `pair-production-axiom-derivation.md:45` |
| 5 | **BH-vs-electron impedance + over-unification** — BH is `Γ=0`/shear (canonical `electron-bh-isomorphism.md:23-34`), not the electron's `Γ=−1`/EM wall; stale title; **primer over-unified** | b/c | MED-HIGH | impl (**primer tweak DONE** this branch; retitle + strengthen-by closes pending) | `black-holes-impedance-mismatch.md:8`; `vol3/cq:129`; `vol1/cq:735` |
| 6 | **SU(2)-vs-K4 provenance drift** — 2 leaves still call `4π` "SU(2) double-cover" vs canonical "K4-bipartite"; `op21` is the correct control | d | MED | impl (relabel-not-retract) | `dama-matched-lc-coupling.md:78-82,182`; `parametric-coupling-kernel.md:107,180` |
| 7 | **`closure-roadmap.md` dead refs** — renamed to `claim-quality-closure-roadmap.md`; refs to `closure-roadmap.md:82`/`§0.5` resolve to nothing across gravity leaves + AVE-Protein | c | MED | impl (link sweep) | `einstein-lensing-deflection.md:14`; `AVE-Protein/README.md:75,88` |
| 8 | **Li ionization residual** `+2.46%` (table) vs `−1.2%` (corrected pipeline), same chapter | c | MED | impl (**verify canonical value first** — ave-walk-back) | `vol2/cq:316,331,335` |
| 9 | **PONDER thrust scaling** `F∝f⁰` vs `V²f²` — genuine functional conflict, cross-repo, extrapolation-only | a | LOW | AVE-PONDER session | `divergence-map:112,464` |
| 10 | **Sagnac stale "contradicts-GR" header** (`vol4/cq:948` didn't follow leaf walk-back); **lunar `Γ_sagnac` "1000 vs 1836"** is itself a false-flag (different quantities) | c/b | LOW | impl + **Grant (Sagnac value?)** | `vol4/cq:948,967`; `lunar-inductive-heating.md:10,16,22` |

**Minor WARNs:** J-row K4-chain parenthetical (optional sharpening, NOT a contradiction — J-spin IS canonically SU(2)); MOND `a₀` dual-value usage-hazard; PONDER 30-vs-35kV stale appendix; gravity-PPN result-doc §8 "NOT applied" stale-status header.

---

## 6 physical questions for Grant (the adjudication surface)

1. **Cardinal `v=c√2`** (#1): real leading-order substrate prediction (→ contradicts emergent-Lorentz, cavity-falsifiable) or grid kinematics that wash out in the continuum (Courant-style)?
2. **Q-PROTEIN-21** (#2): is `S₁₁` the right folding instrument, or does the fold live in the undriven eigenmode solve? (gates the Protein walk-back)
3. **INVARIANT-N3** (#3): stale pre-22-operator scheme to retire, or legitimate vol-5 molecular overload to rename out of `Op#`?
4. **single-vs-pair** (#4): is the electron one bond joining an A–B node-pair, or two bonds?
5. **BH "universal horizon"** (#5): primer mechanism-distinction DONE this branch; OK to also retitle `black-holes-impedance-mismatch.md`?
6. **Sagnac** (#10): does the W-vs-Al `Ψ=7.15` check retain any AVE-vs-GR discriminating value, or fully retire the language?

---

## Status

- **DONE this branch (PR #100):** open/short relabel + the **#5 primer BH-mechanism distinction** (KEEP-BOTH: common saturation, EM-wall vs shear-phase-transition).
- **Dispatched (mechanical, non-gated):** #5 BH-leaf retitle + strengthen-by closes, #6 SU(2)-vs-K4 relabel (2 leaves), #7 closure-roadmap dead-ref repoint.
- **Gated on Grant:** #1, #2, #3, #4, #8 (value-verify), #10-Sagnac-value.
- **Cross-repo (separate session):** #2 Protein walk-back (after Q-PROTEIN-21), #9 PONDER scaling.
