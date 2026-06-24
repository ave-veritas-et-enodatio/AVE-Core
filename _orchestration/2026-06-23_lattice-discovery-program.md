# EPIC — Lattice Dynamic-Regime Discovery Program

**Created:** 2026-06-23 · **Role:** orchestrator-tracked epic (living doc) · **Status:** CHARTERED — lanes pending kickoff
**Origin:** the lattice-characterization white-space survey (workflow `w2jugq7ch`, 5 cartographer lanes + synthesis, 2026-06-23).

---

## 0. North star

Characterize the **dynamic / many-body / finite-frequency / full-spectrum** regime of the chiral micropolar K4 lattice — the white space the survey found wide open — and convert it into **bankable, falsifiable forward predictions**. This is the *discovery* half of the testing pivot ([[project_state_of_ave_and_testing_pivot]]): AVE forces FORMS / imports VALUES, so the AVE-distinct chord lives only in forward predictions, and the predictions live in the regime we have not yet exercised.

**The governing law is settled** — `S(A)=√(1−(A/A_yield)²)`, zero free parameters. The unbuilt artifacts are **driver codes that exercise it dynamically**, not new theory. The white space is engineering, not physics-unknown. That is what makes this tractable.

---

## 1. The meta-finding (survey convergence)

All five domain cartographers independently reported the **same shape**:

> **STATICS + DC/linear regimes are well-characterized** (single-soliton bound states, DC moduli K=2G/ν=2/7, small-k photon dispersion + the (q·ℓ_node)⁴ tell, the saturation kernel pinned at ~21 scales). **The DYNAMIC / MANY-BODY / FINITE-FREQUENCY / FULL-SPECTRUM regimes are wide open** — and the gap is the *absence of driver code*, not the absence of theory.

This is also the focus answer: discovery here *is* the testing-pivot direction. Re-aiming the effort here is alignment, not detour.

---

## 2. White-space map (characterized → open, grep-confirmed)

| Domain | Characterized (evidence) | White space |
|---|---|---|
| **Dispersion / bands** | photon acoustic branch ω=c₀k exact + (q·ℓ)⁴ anisotropy (`k4_bloch_dispersion.py`); Cosserat gap m²=4G_c/I_ω at k=0 (`cosserat-mass-gap.md`, verified 0.35% via uniform-ω) | the **full multi-branch BZ spectrum** (~13 branches), the gapped rotational optical branch ω(k) across k, flat bands, van Hove/DOS, **Chern/Berry topology**, mode-character map |
| **Defect taxonomy** | electron-unknot, proton-Borromean, the (2,q) baryon ladder to c≤19 (`torus-knot-ladder-baryons.md`, `def-kn0t01`) | **constructive a-priori enumeration** of ALL stable (p,q,N,χ); WHY coprime-odd-q; c≥21 continuation; strangeness-as-index; tetra/penta-quark prime-N test |
| **Nonlinear** | birefringence δn∝E⁴ (`birefringence.py`); SHG/FWM **named** as falsification tests (`vol9/ch15`); much walked-back | the vacuum **χ³ SI-coefficient** itself; dynamical mode-mixing — *partly already-banked/demoted, see Lane N* |
| **Constitutive / response** | DC moduli K=2G, ν=2/7, 3 channel speeds, DC Z_eff=Z₀/√S | the **frequency-dependent χ(ω,k)** response, couple-stress resonance poles ω~√(γk²/ρ), translation↔rotation cross-coupling impedance |
| **Thermo / many-body** | δ_strain thermal sliver; single-soliton statics | **soliton-soliton scattering** (σ, θ(b), δ(k), a_s); transport η/κ; substrate phase diagram Ω(T,A,ε); bound states |

The convergence: every "characterized" cell is a *static / DC / single-body* quantity; every "white space" cell is *dynamic / finite-frequency / many-body*.

---

## 3. Ranked discovery veins → lanes

Ranked by novelty × yield × tractability (and bankability). Survey synthesis verdict, lightly re-organized into lanes.

### Lane A — Soliton-soliton scattering **(LEAD, P0)** — novelty H / yield H / tract H / bankable **DIRECT**
The richest seam and the convergence point of three veins (transport, nonlinear interactions, defect fusion). Every AVE soliton is characterized in **statics only**; there is no σ(b) anywhere in `src/` (`build_scattering_matrix` at `k4_tlm.py:64` is a per-node TLM operator, NOT a soliton S-matrix).
- **Deliverables:** scattering length a_s (+ sign), phase shift δ(k), deflection θ(b), differential cross-section σ(b, v_rel).
- **First move / validate-on-known:** build a 2-soliton elastic-scattering driver on `src/ave/core/master_equation_fdtd.py`; seed two Mode-I electron-unknot bound states; run **head-on b=0, low-velocity FIRST** → extract a_s and its **SIGN** as the validate-on-known gate (two electron-solitons must repel — like-charge; **pre-register the expected sign** per `ave-prereg`) **before** opening the σ(b, v_rel) sweep.
- **Why lead:** lowest new-theory cost (pure numerical kinematics of the validated zero-parameter S(A) kernel on the existing FDTD engine); highest leverage (a scattering law is the upstream input that unlocks Lane T transport + Lane D fusion rules); sharply falsifiable (the s-wave scattering-length sign is a first-principles QM pass/fail); cross-sections are *measured* → directly bankable.

### Lane B — Full Cosserat band structure **(P1)** — novelty H / yield M / tract H / bankable indirect
The kinematic fingerprint. Photon acoustic + quartic anisotropy ARE done; the gapped rotational optical branch + the full ~13-branch BZ spectrum are not.
- **Deliverables:** ω(k) for all branches across the BZ; band crossings; flat-band search; van Hove/DOS; **Chern/Berry topological indices** of the chiral I4₁32 lattice; the **mass-gap → structural-mass-spectrum** question (does a gap at E = a mode of mass E/c²?).
- **First move:** extend `k4_bloch_dispersion.py` to the **full 6-DOF-per-node** (3 translational + 3 micro-rotational) Cosserat dynamical matrix, using canonical moduli (G, G_c, γ from `cosserat_field_3d.py`; ℓ_C=√6·L_NODE). Validate-on-known: recover c_EM, c_shear, and the known k=0 Cosserat gap.
- **Folds in Lane C** (dynamic response χ(ω,k) — read the off-diagonal translation↔rotation block + the couple-stress pole ω~√(γk²/ρ) straight off the dynamical matrix; survey rated it a heavy overlap with B).

### Lane D — Constructive defect enumeration **(P2)** — novelty H / yield H / tract M / bankable DIRECT
Derive ALL stable (p,q,N,χ) configurations a-priori from K4 + Cosserat + Axiom-4 (vs the current post-hoc match-to-known-particle taxonomy). Most-bankable-if-it-lands (any un-enumerated stable defect = a candidate particle = a forward prediction); the corpus honestly flags the gaps (strange baryons "NOT natively derived").
- **First move / gate:** before any enumeration, run `ave-canonical-leaf-pull` + `substrate-native-check`, then derive the single load-bearing gate — **WHY** does the K4 lattice admit only coprime-odd-q (2,q) torus knots as stable loops? Everything downstream (c≥21 ladder, strangeness-as-index, tetra(N=4)/penta(N=5)-quark prime-N test) hangs on that selection rule.
- **Partial dependency on Lane A** for defect-fusion rules.

### Lane T — Transport / thermodynamics **(P3, downstream of A)** — bankable direct
Substrate transport coefficients (η_eff, κ_eff) from the scattering collision kernel; the phase diagram Ω(T, A, ε) from equipartition + Axiom-4. **Gated on Lane A** (needs the scattering law as input). Not kicked off until A's validate-on-known passes.

### Lane N — Nonlinear wave-mixing **(DEFERRED / fold-in, NOT a full lane)**
Demoted on symmetric-standard grounds: the survey's nonlinear lane **under-counted** existing work — `vol9/ch15` already names SHG/FWM/parametric-amp as falsification tests, and several pieces are walked-back. **Do NOT re-run an SHG/IMD slope** (echo, already walked-back). If pursued, the only fresh artifact is extracting the vacuum **χ³ coefficient in SI units** (m²/V²) from the Taylor expansion of S(A) (`saturation.py:124`) — a small fold-in, queued behind A/B.

---

## 4. Lane structure + sequencing

```
KICK OFF IN PARALLEL NOW:
  Lane A  (scattering, LEAD)      ── independent, highest yield, unlocks T + D
  Lane B  (band structure + C)    ── independent, the kinematic fingerprint
  Lane D-gate (coprime-odd-q WHY) ── independent derivation (the selection-rule gate only)

GATED / DOWNSTREAM:
  Lane D-full   ← needs the D-gate result (+ partial A for fusion)
  Lane T        ← needs Lane A's scattering law
  Lane N        ← fold-in behind A/B (χ³ SI-coefficient only)
```

Lanes A and B are orthogonal, both are driver-builds on already-validated engines, and both have clean validate-on-known gates — so they run cleanly in parallel. Lane D's selection-rule gate is an independent derivation that can run alongside; the rest of D waits on it. Lane T waits on A. Lane N is a small fold-in.

---

## 5. Per-lane status tracker (living)

| Lane | Priority | Status | Owner | Current phase | Next gate |
|---|:---:|---|---|---|---|
| **A** scattering | P0 | CHARTERED | — | pre-kickoff | build 2-soliton driver → b=0 a_s-sign validate-on-known |
| **B** band structure (+C) | P1 | CHARTERED | — | pre-kickoff | extend dispersion to 6-DOF Cosserat matrix → recover c/gap |
| **D-gate** coprime-odd-q | P2 | CHARTERED | — | pre-kickoff | derive the (2,q) stability selection rule |
| **D-full** enumeration | P2 | BLOCKED | — | — | needs D-gate (+ partial A) |
| **T** transport/thermo | P3 | BLOCKED | — | — | needs Lane A scattering law |
| **N** χ³ coefficient | — | DEFERRED | — | — | fold-in behind A/B |

*(Orchestrator updates this table as lanes report.)*

---

## 6. Orchestration discipline (per lane)

1. **Validate-on-known FIRST.** Every lane has a known-result gate it must recover before any new number counts as a prediction (A: the a_s sign vs known e-e repulsion; B: recover c_EM/c_shear/the k=0 gap; D: recover the known electron/proton/baryon assignments before predicting new ones). A forward prediction made before the validate-on-known passes is not bankable.
2. **Pre-register** the expected outcome (`ave-prereg`) before running the forward sweep — especially the *sign/direction*, which is the cheapest falsifier.
3. **Refute-by-default adversarial audit** before any KB/manuscript landing (deflate-then-document). The orchestrator audits each lane's diffs (read-AND-run, not the self-report — the BenchModel-gate lesson).
4. **CONSISTENCY vs CHORD labeling** on every result (`ave-discrimination-check`): is this peer-with-SM (consistency / echo) or AVE-distinct (chord / forward prediction)? The chord is the prize; honest labeling protects it.
5. **Symmetric-standard** both ways (don't demote AVE for what SM also does; don't let a convergence-narrative inflate an echo — the survey's own Lane-N self-catch is the model).

---

## 7. Standing constraints (non-negotiable)

- `main` PROTECTED; **NO self-merge** — every change via reviewed PR, Grant merges.
- Self-isolate git-mutating work in a `/tmp` worktree off `origin/main`. **NEVER** put the substring `build` in a worktree/branch name (trips `predictions_manifest_validator.py:136`).
- PURE-AVE-CORPUS (physics only). `ave-canonical-source` (import from `constants.py`). verify-before-cite + grep-completeness (auditor not exempt). audit-trail-in-git: do not edit `_archive`, `*_FROZEN`, SESSION_STATE, or result/walk-back docs.
- Drivers land under `src/scripts/vol_<N>_*/`; pre-regs + results under `research/`; canonical results propagate KB-leaf-first then manuscript (lockstep).

---

## 8. Reference

- Survey output (full): workflow `w2jugq7ch` result (5 lanes + synthesis).
- Lane A: `src/ave/core/master_equation_fdtd.py`, `k4_tlm.py:64` (the per-node operator NOT to confuse with a soliton S-matrix), `annihilation_evaporation_run.py` (has an impact-parameter seed knob but no far-field σ readout).
- Lane B: `src/scripts/vol_4_engineering/k4_bloch_dispersion.py`, `src/ave/topological/cosserat_field_3d.py`, `cosserat-mass-gap.md`.
- Lane D: `torus-knot-ladder-baryons.md`, `def-kn0t01`, `claim-quality-closure-roadmap.md` (FI-13 neutrino-as-screw-defect flag).
- Lane N: `saturation.py:124`, `birefringence.py`, `vol9/ch15-falsification-tests/index.md`.
