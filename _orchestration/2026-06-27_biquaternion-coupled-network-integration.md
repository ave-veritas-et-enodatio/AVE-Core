# Biquaternion complex coupled network integration (epic)

**Date:** 2026-06-27 · **Branch:** `analysis/2026-06-27-biquaternion-coupled-network-integration` (off `origin/main`)  
**Status:** ACTIVE — Phase 0 (discipline map + KB leaf scaffold). No merge to `main` without reviewed PR.

---

## Goal

Close the integration gap toward **one published block** of *biquaternion complex coupled network equations* that maps:

- small-signal and large-signal response  
- static and dynamic stress on the vacuum lattice  
- → three propagating wave channels (EM-transverse, shear, bulk-longitudinal) **plus** the mass store (nonlinear A1 cavity at \(\Gamma\to-1\)

**Scope fence (adjudicated):** the block is a **five-layer stacked specification** (operating point + three-channel \(Y(j\omega)\) + biquaternion port/wall notation + small-signal linearization + null-cone wall). Biquaternion is **coupling-layer notation only** — not the substrate primitive, not the sole time-stepped state (`unified-engine-design-doctrine.md` §F; `research/2026-06-06_biquaternion-node-algebra-result.md` G1–G3 FAIL).

**Non-goals (do NOT re-pose):** derive \(Q=1/\alpha\) from the network (circular); promote biquaternion to new physics; collapse EM/mechanical impedance domains; wire charge winding into the A1 phasor (genesis-24).

---

## Canonical anchors (read before editing)

| Piece | Home |
|---|---|
| Node small/large-signal (R1/R2/R3, keyed V/I) | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md` (clm-vca7r1) |
| Graded network response (dispersion, SYM/ASYM, \(\Gamma\)) | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/graded-network-response.md` (clm-gvn4r1) |
| Three-channel impedances | `manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md` |
| Device network schematic + open gates | `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md` §6 |
| Per-DOF tensor (orthogonal axis) | `manuscript/ave-kb/vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md` |
| Engine doctrine (waves vs cavity, biquaternion layer) | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md` |
| Biquaternion verdict | `research/2026-06-06_biquaternion-node-algebra-result.md` |
| Build-A spectral solver (isolation leg) | `src/ave/solvers/graded_vacuum_network.py` |
| \(H_{\mathrm{couple}}\) dynamics | `src/ave/core/cross_sector_coupling.py` |
| Q prereg + α-free guards | `research/2026-06-19_electron-Q-coupled-network_prereg.md` |
| Coupled eigensolve (existence) | `research/2026-06-24_engine-coupled-eigensolve_prereg.md` |

---

## Five-layer equation block (target KB leaf)

Deliverable leaf (not yet written):  
`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/biquaternion-complex-coupled-network-equations.md`

| Layer | Content | Classification |
|:---|:---|:---|
| **0** | Biquaternion port notation \(q=w+F\), \(F=E+\iota B\); cores keep separate fields | Consistency (notation) |
| **1** | Large-signal keyed \(S_\bullet(A_\bullet)\); static/dynamic selectors (R1/R2/R3) | Derived from Ax 4 + node-up |
| **2** | Three-channel complex \(Y_\alpha(j\omega)\); two-domain N-port + \(\mathsf T(\xi_{\mathrm{topo}})\); \(H_{\mathrm{couple}}\) | Consistency re-expression |
| **3** | Small-signal \(n\), \(Z_{\mathrm{eff}}\), \(\Gamma\) linearized at \(A_0\) | Derived (clm-vca7r1) |
| **4** | Wall = null cone \(|\Gamma|=1 \Leftrightarrow N(q)=0\); mass = A1 cavity energy at wall | Consistency + Ax 1+4 |

Include explicit **stress → operating point → channel → wave vs mass** dispatch table (from node-up §0 + doctrine §C).

---

## Phase log

| Phase | Deliverable | Status |
|:---|:---|:---|
| **0** | This epic doc + discipline map | **IN PROGRESS** |
| **1** | KB leaf (Layers 0–4 + dispatch table); `kind: leaf`, `no-claim` or minimal cross-links only | PENDING |
| **2** | Vol. 9 Ch. 3 § render (KB-first); optional Vol. 4 cross-ref | PENDING |
| **3** | Build-B: wire \(H_{\mathrm{couple}}\) into `graded_vacuum_network.py` spectral solve | PENDING |
| **4** | Driver + tests: stress-regime → \((S_\varepsilon,S_\mu,S_{\mathrm{bulk}},S_{\mathrm{shear}})\) → \(\Gamma\), mode-split (no α-chord) | PENDING |
| **5** | P1.3: biquaternion notation at coupling ports in engine (doctrine §F) | PENDING (may follow Phase 3) |

---

## Corpus discipline map — how to work KB, engine, manuscript, research

Use this section as the **implementor briefing** for every session on this epic. Fire skills **before** writing, not after.

### 1. Session types (`CLAUDE.md`)

| Type | Who | Branch | Merge |
|:---|:---|:---|:---|
| **Orchestration** | Grant + orchestrator | `analysis/<topic>` or integration tracker branch | PR review → merge; tag `audit/<date>_<topic>` at implementor tip |
| **Implementor** | Single deliverable | `analysis/<date>-<slug>` off `main` | Push + PR; **do NOT self-merge** |

**Pre-commit (mandatory):** `git branch --show-current` before every commit (especially after subagents).  
**Worktree implementors:** spawn with `isolation: "worktree"` per `_orchestration/README.md`; prepend `PYTHONPATH=$PWD/src` for ad-hoc scripts.

---

### 2. Repo surfaces — what lives where

| Surface | Path | Canonical? | Edit order |
|:---|:---|:---|:---|
| **KB leaves** | `manuscript/ave-kb/` | **YES** (sole canonical prose/results since 2026-05-07) | **Edit first** |
| **LaTeX manuscript** | `manuscript/vol_*/` | Derived publication artifact | Sync **after** KB |
| **Engine** | `src/ave/` | Code truth for numerics | Match KB claims; constants from `constants.py` |
| **Drivers / verify** | `src/scripts/` | Experiment artifacts | Honesty discipline; JSON outputs |
| **Research** | `research/` | Preregs (frozen), results, synthesis | Prereg **first commit** on branch |
| **Orchestration** | `_orchestration/` | Tracked epic state | Phase log updates on orchestration PRs |
| **Scratch** | `.agents/handoffs/` | Gitignored | External context only; not corpus |

**Pure-AVE rule:** no investor/external pitch language in tracked files.

---

### 3. KB workflow (mandatory pipeline)

**Read first:** `manuscript/ave-kb/CLAUDE.md` (INVARIANT-S1–S13), `CONVENTIONS.md`, `entry-point.md` bootstrap.

| Step | Action | Command / artifact |
|:---|:---|:---|
| 1 | Find canonical leaf before deriving | `ave-prereg` corpus-grep; `ave-canonical-leaf-pull` |
| 2 | Edit leaf with frontmatter | `<!-- kb-frontmatter kind: leaf ... -->` |
| 3 | Classify | `consistency-vs-emergence` — default **Class C** for this epic |
| 4 | Vocabulary | `ave-vocab-discipline` — no silent overload of *node*, *mass*, *charge* |
| 5 | Refresh derived metadata | `make refresh-kb-metadata` |
| 6 | Verify | `make verify-kb-metadata` · `make verify-md-links` · `make verify` (full gate) |
| 7 | Manuscript sync | Update `manuscript/vol_*` **downstream** only |

**Leaf rules:** line 1 = up-link `[↑ Parent](index.md)`; leaves canonical, indexes derived.  
**Claim promotion:** this epic starts **`no-claim`** on the new leaf unless Grant adjudicates a new `clm-`; cross-link existing IDs only.  
**Do not** headline consistency re-expression as solidity lift (`graded-network-response.md` tag).

---

### 4. Engine workflow

**Read first:** `src/ave/AGENTS.md`, `unified-engine-design-doctrine.md`, `ave-canonical-source`.

| Rule | Detail |
|:---|:---|
| Constants | Import from `ave.core.constants` — never hard-code \(\alpha\), \(m_e\), \(Z_0\) in verdict paths |
| α-free spectral work | Ratios only in `graded_vacuum_network.py`; no `RHO_BULK` magnitude in Q-determining paths |
| Stencil | Tetrahedral K4 (`cosserat_field_3d.TETRA_OFFSETS`) — **not** Cartesian 7-pt Laplacian |
| Operators | Reuse `universal_operators` / `scale_invariant` — no local reimplementation of \(S(A)\), \(\Gamma\) |
| Driver honesty | `ave-driver-script-honesty` — forward prediction vs fit; no silent 137 |
| Worktree | `ave-worktree-paths`; `Makefile` / `pyproject.toml` pythonpath for local pytest |
| Acceptance | Label tests CONSISTENCY vs CHORD; Q=137 slot stays **EMPTY** |

**Local validation:** `make test` · `make verify` from worktree root.

---

### 5. Manuscript / Vol. 9 datasheet workflow

| Rule | Detail |
|:---|:---|
| KB-first | New prose → KB leaf → `\kbleaf{...}` or sync in `vol_9_vacuum_datasheet/chapters/` |
| Figures | `ave-figure-discipline` — regenerate via driver, don't hand-draw physics |
| Notation | INVARIANT-N2 \(\ell_{node}\) vs \(l_{node}\) per volume; INVARIANT-N1 no \(\mathcal M_A\) glyph |
| Build | PDF is derived; fix KB + build hygiene PRs separately if needed |

Target render slot: `manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex` §6 (after KB leaf exists).

---

### 6. Research / prereg workflow

| When | Skill / artifact |
|:---|:---|
| New numerical claim or gate | `research/YYYY-MM-DD_<slug>_prereg.md` — **first commit** on branch |
| Before derivation | `ave-prereg` corpus-grep |
| After run | `research/..._result.md` + driver JSON |
| Classification | `consistency-vs-emergence`, `ave-evidence-framing-discipline` |
| Falsifiers | `ave-discrimination-check`, `ave-multi-falsifier-triangulation-discipline` |
| Walk-back | `ave-walk-back` if adjudication retires a slot |

This epic reuses frozen preregs for Q (`2026-06-19`) and coupled existence (`2026-06-24`) — **extend**, don't rewrite gates post-hoc.

---

### 7. Skills — when to fire (full inventory)

#### Always (this epic)

| Skill | Trigger |
|:---|:---|
| `verify-before-cite` | Any file:line, quote, or status claim |
| `substrate-native-check` | Prose derivation or new solver — K4 stencil, A1⊥T2, phase vs real |
| `consistency-vs-emergence` | Every result — expect Class C unless auditor promotes |
| `ave-canonical-source` | Any numeric literal in code |
| `phase-space-coordinate-check` | Mixing real-space 720° with phase-space (2,3) |
| `ave-dimensional-provenance-check` | Attach units to \(Z\), length, energy |
| `ave-evidence-framing-discipline` | Verdict language — no "found the number system" |

#### KB / manuscript

| Skill | Trigger |
|:---|:---|
| `ave-vocab-discipline` | New or overloaded terms |
| `ave-figure-discipline` | Figures in vol_9 or KB |
| `ave-walk-back` | Retire or rescope a claim |
| `ave-ip-divide-discipline` | Public corpus vs app leakage |

#### Engine / drivers

| Skill | Trigger |
|:---|:---|
| `ave-driver-script-honesty` | New or audited driver |
| `ave-loop-gap-harness-discipline` | Genesis / VacuumEngine3D work (if touched) |
| `pre-test-physics-check` | Before asserting physics in tests |
| `ave-fundamental-ground-up-implementation` | New engine module |
| `ave-worktree-paths` | Worktree sessions |

#### Claims / evidence

| Skill | Trigger |
|:---|:---|
| `ave-prereg` | Before new derivation |
| `ave-canonical-leaf-pull` | Q-factor, scaling, coupling problems |
| `ave-discrimination-check` | AVE-distinct vs SM framing |
| `ave-discriminator-before-synthesis` | Multi-falsifier synthesis |
| `ave-independence-check` | "N independent confirmations" lists |
| `ave-infinity-discipline` | Continuum limits |
| `ave-resonant-amplification-check` | Q / resonance claims |

#### Audits (orchestration / pre-merge)

| Skill | Trigger |
|:---|:---|
| `ave-audit` | Corpus audit pass |
| `ave-audit-of-audit` | Meta-audit |
| `ave-sweep-audit` | Sweep-style audits |

#### EE / intuition (optional for datasheet prose)

| Skill | Trigger |
|:---|:---|
| `ave-ee-first-mapping` | Protocol / bench mapping |
| `ave-ee-intuition-summary` | 5-beat mechanism summary |

#### Specialized (fire if epic touches them)

`ave-regime-phase-state-check` · `ave-representation-capability-check` · `ave-cavity-class-identification` · `ave-conserved-vs-pumped` · `ave-asymmetric-grip` · `ave-power-category-check` · `ave-analytical-tool-selection` · `ave-module-library-discipline` · `ave-engineering-program-rigor` · `ave-directory-enumeration-discipline` · `ave-live-fire-derivation-provenance` · `ave-apparatus-floor-attribution` · `ave-vca-setup-compliance` · `ave-discipline-translate`

Skills live at `~/.claude/skills/ave-*/SKILL.md` (and `consistency-vs-emergence`, `substrate-native-check`, `phase-space-coordinate-check`, `pre-test-physics-check`, `verify-before-cite`).

---

### 8. Cursor / repo rules (always on)

| Source | Scope |
|:---|:---|
| `CLAUDE.md` (repo root) | Branching, orchestration vs implementor, audit tags, pre-commit, worktree validation |
| `AGENTS.md` / `.cursor/rules/ato.mdc` | ato PCB DSL (orthogonal to AVE physics) |
| User rules | No commit unless asked; PR via `gh`; git safety |
| `manuscript/ave-kb/CLAUDE.md` | Notation, axioms, operating-point W6, claim DAG |

---

### 9. Git / PR discipline

```
analysis/2026-06-27-biquaternion-coupled-network-integration
  → push -u origin HEAD
  → gh pr create --base main
  → review → gh pr merge --no-ff
  → git tag audit/2026-06-27_biquaternion-coupled-network-integration <tip>
  → delete branch after tag on origin
```

Implementor sessions: one deliverable per PR slice (Phase 1 KB leaf, Phase 3 solver, etc.) if scope grows — split per `ave-engineering-program-rigor`.

---

### 10. Epic-specific guards

| Guard | Source |
|:---|:---|
| \(A1 \perp T2\) — never shared \((V_{inc},V_{ref})\) phasor | `master-equation.md`:20 |
| EM (\(\Omega\)) vs mechanical (\(\rho c\)) — transformer, not wire | `device-circuit-models.md`:139 |
| Bulk-port ratio \(\sqrt{2}\) vs medium P-wave \(\sqrt{10/3}\) — disambiguate | `node_2domain_nport.py` header |
| Static \(\mathbf B\) → \(\delta n_\mu = 0\) exactly | clm-pvlas1 / node-up R3 |
| Loaded \(Q=1/\alpha\) derivation **forbidden** | `electron-bound-resonator-coverage.md`:161 |
| Biquaternion **canonized to nothing** as primitive | biquaternion result §0 |

---

## Test plan (PR acceptance)

- [ ] Phase 0 epic doc reviewed (this file)
- [ ] Phase 1: `make verify-kb-metadata` green after KB leaf
- [ ] Phase 3: `pytest src/tests/test_graded_vacuum_network*.py` green + new coupled-arm tests
- [ ] No `alpha` / `Q_TANK` / `137` in new Q-verdict paths (grep gate)
- [ ] Manuscript sync PR separate or stacked with KB leaf PR

---

## Cross-refs

- Prior conversation synthesis: five-layer block + IF-and-only-if verdict (2026-06-27 session)
- P1 scope biquaternion at coupling layer: `research/2026-06-25_unified-engine-P1-scope.md` §3
- H_couple status: `research/2026-06-20_h-couple-status.md`
