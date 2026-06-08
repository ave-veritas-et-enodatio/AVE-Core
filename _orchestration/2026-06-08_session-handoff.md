# 2026-06-08 session handoff — electron-synthesis + α-route + soliton-size arc

**Scope.** Distills the §16–§47 arc of the electron-structure synthesis epic
([`2026-06-07_electron-synthesis-epic.md`](2026-06-07_electron-synthesis-epic.md))
into a clean-state handoff. That epic is the detailed phase log (carried by **PR
#120**); this doc is the orientation layer: what resolved, what is scoped-and-
gated, what stays open, the open Grant decisions, the new infrastructure, and the
worktree-prune list.

**Headline.** The session pushed the electron picture to a defensible Class-A/B
consistency structure and then ran the α-value derivation to a clean negative on
every closed route — including walking back the "α to 1.5%" claim. The
honest closing: AVE constrains α's **scale and functional form** (substrate
geometry) but does **not** derive its **value**; the framing (α = a vacuum loss-
tangent / a relationship, not a fundamental constant) is the chord, the value is
a datasheet calibration entry. The new frontier is the soliton-size definition
gap, which surfaced a cluster of dimensional/category errors and is now scoped
for a gated adoption.

**State of the board at handoff:** 21 open PRs (#117–#137), all `MERGEABLE`
against `main` (`origin/main` HEAD `63e6671a`, Merge PR #116). 46 worktrees (21
KEEP / 22 prune-safe / 3 HOLD). Grant reviews each PR himself — see the
companion [`2026-06-08_pr-review-guide.md`](2026-06-08_pr-review-guide.md).

---

## 1. The arc in one screen (§16–§47)

The epic ran two interleaved threads: the **α-value-derivation thread** (does
the substrate read α out?) and the **electron-structure / soliton-size thread**
(what IS the object, and how big is it?). Both closed to honest negatives or
gated-scoped states; nothing in the arc claims an α readout or a derived
soliton size.

| § | topic | verdict |
|---|-------|---------|
| §16 | Water-chapter lessons | z=4 achiral diamond CONFIRMED (water builds it); chirality/spin forced onto the **Cosserat microrotation**, not the net. 2 over-reaches corrected (ice≠dark-energy; voids≠α-valleys). |
| §17 | α-valley-fraction (PR #121) | α-free NEAR-MISS; real-space envelope RULED OUT as the 137-source (valley fraction ~0.49 both frames). |
| §18 | Golden-Torus 137 audit | **FIT** at the exact-value level (1 knob `R·r` hand-set to ¼; substrate's own α-free value forces `R·r→4π²α`). |
| §19 | Paper-#4 extension | one genuine extension: trap → marginal **limit-cycle** (rings at ω_C forever), not a dissipative settle. |
| §20–§22 | φ-winding-stability route (PR #125) | EXHAUSTED. (2,3) is the LEAST-stable golden convergent (corpus selects it by MINIMALITY); (2,3) does NOT force `R/r=φ²`; lepton-tower discriminator does not exist. §18 FIT no longer contingent. |
| §23 | first-principles z₀ (archive pointer) | claimed α derived to 1.5% (z₀=4·(1+\|T\|)=52). **[Later WALKED BACK — see §31.]** |
| §24 | electron-as-cog | belt-trick in gear clothing; NOT a new mechanism. Nyquist-sampling-→½ is wrong 3 ways. |
| §25 | α-derivation history sweep | 15-route ledger; chiral-matching reframe DEAD (chirality is an α-CONSUMER); 2 murky open routes (Path A chirality-EMT; LC-tank Q=1/α). |
| §26 | session-close (first) | interim clean-state; superseded by §31's α walk-back + the soliton-size thread (§42–§47). |
| §27 | PR #126 audit | SOUND code; over-claims in the doc/description layer; walk-backs APPLIED + verified (`891d0f36`). |
| §28 | electron-modeling close-out of record | defensible Class-A/B structure; derives the CONDITIONS for a (2,3) electron, does NOT show the substrate dynamically SELECTS it. Spin-½/Dzhanibekov = 2 facts (T_d point-group + FM topology), NOT 1 mechanism. |
| §29 | Path C amorphous-EMT | Outcome D: z₀→51.65 (0.74%, route confirmed). **[Superseded by §31.]** |
| §30 | force-projection + piezoelectric | force=stress=∂W/∂strain (2 conjugate sectors); vacuum = chiral piezoelectric Cosserat solid; "EM = the vacuum's piezo response" = CONSISTENCY-class. |
| §31 | **Path C physical-lattice verdict (WALK-BACK)** | z₀=52 is NOT physically forced — it counts 48 secondary PATHS to 12 distinct atoms (path-multiplicity, not coordination). Physical z≈16 → 1/α≈49. **α NOT derived even to 1.5%; stays Class-B / calibration.** Supersedes §23/§25/§26/§29. |
| §32 | recent-results carry-forward | wave-impedance (c_L=√(10/3)c P-wave); GW=transverse shear at c; piezo doc (PR #127). |
| §33 | QM-foundations trio (PR #128) | superposition=ALIASING (synthesis) · collapse=SAMPLING/Born-derived (derived) · entanglement=THREAD (canonical). Origin-mislabel fix: aliasing→superposition (Bell-surviving). |
| §34 | phase-space→carrier-envelope mapping | lepton arm clean ((2,3) preserved, Cosserat-torsion ladder); proton (2,5) **real-vs-phase-space TYPE CONFLICT** flagged for Grant. |
| §35 | neutrino + high-E scale-check | ℓ_node = electron reduced Compton (NOT Planck); "electron at cutoff" = IDENTITY; aliasing→fractal-zoo UNGROUNDED; neutrino = GAP. |
| §36 | proton/vacuum/mass cluster | proton=PHASE-space CONFIRMED (walk-back); sub-node body = OPEN tension; +2281× size category-error caught (8π/5 coupling-ratio worn as length). |
| §37 | bulk/shear/torsion channel | muon-vs-proton is NOT bulk-vs-shear (both T2/transverse-EM); the distinction is topology+torsion, **torsion on the LEPTON side**; orchestrator mapping was inverted. |
| §38 | high-E aliasing prereg (PR #131) | well-formed + honest; testable content RELOCATED to the **topological-selection rule** (stable (2,4) would falsify). Adjudication conflict #10: emergence (leaf) vs consistency (prereg). |
| §39 | proton-mass I_scalar=1162 | **DERIVED, not fitted** (forward Faddeev-Skyrme output, no 1836 in loop). Honest magnitude = **+0.74% topology-only**, NOT −0.002% (that rides 1 thermal correction δ_th). Leans CHORD. |
| §40 | mass-spectrum pattern-test | PARTIAL: no-numerology bar 5/5 PASS (echo-killer); strong-chord (forward + ~1% + ≤1 correction) PROTON-ONLY 1/5. Proton's ppm = COINCIDENCE (δ_th over-cancel), not a spectrum property. |
| §41 | lepton-sector audit (PR #135) | μ-α¹/τ-α² premise REFUTED (both α⁻¹); no-numerology holds 5/5, tier degrades to matched-closed-form-no-solver; **√(3/7) MISLABEL confirmed** (dilatational √(1−2ν), not torsion-shear) — flagged for Grant. |
| §42 | r_opt dimensional propagation (PR #133) | self-audit found the r_opt-as-length error in **26 sites** (vs 4 named); 10 fixed, 2 in #132, 14 surfaced; cold-vs-thermal κ_FS split flagged. |
| §43 | r_opt code-use audit | REAL code-level scale bug in 2 files; 6 baryon STLs wrong-scale (~2290–4583×). **[Reopened by §45 as an A-vs-B fork.]** |
| §44 | code-provenance index prototype (PR #136) | 6-seed registry + drift-gate verifier; caught a §41 error (leptons LOOSELY-gated, not ungated). |
| §45 | soliton-size definition | **GAP CONFIRMED** — no canonical soliton-size definition; the conflation is CANONICAL. §43 reopened as an unadjudicated **A (sub-node) vs B (supra-node)** canonical fork. |
| §46 | node-Nyquist size resolution | **COHERENT-BUT-SYNTHESIS** — spine supported (node = spatial Nyquist boundary), A46 refinement (do NOT fuse spatial-Brillouin and phase-space-carrier axes), 3 tensions. SCOPED adoption gated on vocab-disambiguation + greenlight. |
| §47 | soliton-size vocab disambiguation | pedantic directive VINDICATED: **14 ambiguous load-bearing terms**; r_opt has a 2nd genuine-LENGTH meaning (so "r_opt is dimensionless" was half the story). Canon gated on Grant's review of the 14 clarity-risk terms. |


## 2. DONE — resolved / closed this session

- **Fork A (genesis amplitude crux) RESOLVED.** Electron = a parametric
  oscillator at threshold = a marginal Hopf **limit cycle** on the gain=loss
  locus, ringing at ω_C (the Compton clock). The "4× pump" was the lossless-
  parametric tongue with the dark-wake loss switched off; the real α-free loss
  bounds the pump and the m_ec² point sits ~on the locus. [§9/§12/§13/§19.]
- **Lattice = z=4 achiral diamond, water-confirmed.** Spin/chirality lives in
  the **Cosserat microrotation** (the 3 ω-sectors), NOT the net connectivity;
  the z=3 srs "chiral K4" name is decorative for the computational chain
  (λ_G=4/21, Lorentz, trampoline all on z=4). [§8.1/§16/§28.]
- **α-value derivation = NEGATIVE on every closed route (the honest closing).**
  Parametric loss = calibration · dark-wake far-field = 4π not 137 ·
  real-space valley = near-miss · Golden-Torus = FIT · twist = clean negative ·
  φ-winding = wall · z₀-EMT = α-circular · **z₀=52 "1.5%" WALKED BACK** as an
  unforced path-multiplicity count (physical z≈16 → 1/α≈49). **AVE constrains
  α's SCALE (~10², Compton-trap + π³ 3-volume) and FUNCTIONAL FORM
  (`aπ³+bπ²+cπ`, all coefficients forced) but does NOT derive its VALUE.** The
  framing (α = a vacuum loss-tangent / a relationship, not a constant) is the
  chord; the value is a datasheet calibration entry. α stays **Class-B**. [§18/§22/§25/§31.]
- **proton = PHASE-space (2,5)** (per-loop polarization winding in (V_inc,V_ref)),
  parallel to electron (2,3); real-space = 6₂³ Borromean tube-path. Walk-back of
  `proton-identification.md:19,30,32` confirmed (Rule-12). [§36 → PR #132.]
- **proton-mass I_scalar=1162 is DERIVED, not reverse-fitted** (forward
  Faddeev-Skyrme output; no 1836 in the loop). Honest emergence claim =
  **+0.74% topology-only** (κ=8π, c=5, V=2, p_c=8πα); the −0.002% rides one
  named thermal correction δ_th=1/(14π²) and is proton-specific (δ_th over-
  cancels = coincidence), NOT a spectrum property. Leans CHORD (1st datapoint). [§39/§40.]
- **mass-spectrum no-numerology bar holds 5/5** (every mass = a shared named
  constant or an inserted measured value — echo-killer); the forward-derived-
  to-~1% strong-chord is PROTON-ONLY (1/5). [§40/§41.]
- **QM-foundations trio** mechanisms fixed: superposition=aliasing (synthesis,
  consistency-tagged), collapse=sampling/saturation (Born p=2 derived), entangle-
  ment=topological thread (canonical, Bell-surviving). May-2025 origin seed
  re-targeted aliasing→superposition (one slot). [§33 → PR #128.]
- **Piezoelectric framing** (vacuum = chiral piezoelectric Cosserat solid; EM =
  the vacuum's piezo response) landed as CONSISTENCY-class. [§30/§32 → PR #127.]
- **Force-projection grounded** (force=stress=∂W/∂strain, 2 conjugate sectors;
  gravity = REFRACTION not pull). [§30 → folded in #130/#137.]

## 3. SCOPED — planned, gated on Grant

- **Soliton-size adoption (the recommended next workstream).** Verdict
  **COHERENT-BUT-SYNTHESIS** (§46): adopt the node-Nyquist spine + refine
  labels, do NOT promote-as-is. Gated on **(a)** the `w1pc27h3k` vocab-
  disambiguation lock (§47, 14 clarity-risk terms) AND **(b)** Grant's
  greenlight. Full plan in §7 below. SEPARATE from the multi-node-vs-single-node
  call (Grant decision, §4).
- **High-E aliasing prereg FROZEN** (PR #131): testable content RELOCATED from
  the ungrounded fractal-morphology to the **topological-selection rule** (a
  stable (2,4) baryon would falsify). No driver/result yet; corpus-testable now. [§38.]
- **Physics-flag resolutions** (PR #130): c_L=√(10/3)c P-wave canon + piezo
  force-dilution coordination-z0 link — Grant-accepted, staged as a corpus edit. [§32/§37.]

## 4. OPEN — Grant decisions awaiting adjudication

These are the framing-level calls this implementer lane does NOT make. Each is
load-bearing; several gate the soliton-size adoption.

1. **Soliton-size adoption mode** — adopt the node-Nyquist two-size framing
   (two SPATIAL sizes across the Nyquist node + winding as a distinct identity
   axis)? COHERENT-BUT-SYNTHESIS; gated on the vocab-disambiguation lock +
   greenlight. [§46/§47.]
2. **Multi-node-vs-single-node proton** — "proton spans MULTIPLE nodes"
   (`02_baryon_sector.tex:40`) vs "nucleus inside a SINGLE node"
   (`semiconductor_binding_engine.py:68`). SEPARATE from the size adoption;
   decides the §43/§45 A-vs-B fork below. [§46 tension 2.]
3. **§43/§45 A-vs-B canonical fork** — proton body is **A (sub-node**, D_p=0.84fm
   IS the body, r_opt-as-length is a BUG) or **B (supra-node**, r_opt≈5 ℓ_node
   IS the envelope, 0.84fm is an internal RMS feature, STLs are correct-scale)?
   Both canonical, opposite answers — do NOT collapse. Decides whether §43 is a
   code bug or the STLs are right. [§43/§45.]
4. **√(3/7) dilatational-vs-torsion** — √(3/7)=√(1−2ν_vac) at ν=2/7 is EXACTLY
   the DILATATIONAL/compressional (bulk) signature; the muon leaf labels it
   "torsion-shear." Does a torsion route independently reach √(3/7), or is it
   dilatational and the label is wrong? The identity is exact; only the label is
   at-issue. Flag-don't-fix. [§40/§41.]
5. **cold-vs-thermal κ_FS** — the proton leaf quotes COLD 8π/5=5.03 (#132); the
   baryon ladder quotes THERMAL κ_eff/5=4.990. Two proton r_opt numbers, both
   dimensionless + per-file-consistent, cross-file inconsistent. Single canonical
   convention = Grant's call. [§42.]
6. **Manuscript-figure reference** — which figure(s) the electron-genesis /
   photon-engine runs (#129, #134) feed into the manuscript, and at what scale-
   claim tier (the §43/§45 fork gates whether baryon-scale figures assert
   physical or rendering-only scale).
7. **Emergence-vs-consistency for m_p/m_e** (adjudication conflict #10) — the
   prereg classifies 1836.12 (−0.002%) as CONSISTENCY; the canonical leaf
   `torus-knot-ladder-baryons.md:41` self-classifies it as Class-4 EMERGENCE.
   Prereg is stricter; the ratio uses 8πα + topology (not clean single-m_e). [§38.]

## 5. NEW INFRASTRUCTURE

- **2 new skills (drafted + live-validated this session, §40):**
  - `ave-dimensional-provenance-check` — the coupling/count-as-length guard.
    Would have pre-empted the three category-errors of this class: 8π/5 (coupling
    ratio as length), z₀=52 (path-count as coordination), (2,5) (phase as
    real-space). Lint rule it carries: a dimensionless budget-ratio is NEVER
    multiplied by ℓ_node.
  - `ave-live-fire-derivation-provenance` — the dead-input + forward-vs-fit
    residual guard. Caught node_pitch DEAD (I_scalar identical at 1 vs 1e6) and
    the proton/Δ forward-not-fit signature (forward misses exact CODATA by
    0.0019% = the derivation signature; a reverse-fit hits machine precision).
- **Code-provenance index prototype (PR #136, §44).** 6-record registry
  (m_p/m_e, m_Δ, m_μ/m_e, m_τ/m_e, m_n, r_opt) + `verify_code_provenance.py`
  drift-gate + honest "6-seed PROTOTYPE, NOT all-code-tracked" framing; mirrors
  `claims.jsonl`. It caught a §41 error on its first run (leptons are
  LOOSELY-gated at ±2%, not ungated). 4 verifier-robustness WARNs queued.

## 6. OPEN TENSIONS (carry into next effort)

- **A46 two-axes — do NOT fuse.** The corpus restricts "aliasing" to the
  SPATIAL/Brillouin axis (q>π/ℓ_node); extending it onto the PHASE-SPACE
  CARRIER axis (ω=mc²/ℏ) is the conflation the corpus forbids. They coincide
  NUMERICALLY at c/ℓ_node but are PHYSICALLY distinct. "phase-space = sub-node"
  fuses the two. [§35/§46/§47.]
- **crossing→radius law runs OPPOSITE** (more crossings → SMALLER r_opt:
  electron 8.38, proton 5.03) — self-consistent ONLY if r_opt is not a real-space
  size (i.e. only under the κ_share reading). [§46 tension 3.]
- **The proton spatial-extent / 2281× fork** (= the §43/§45 A-vs-B Grant
  decision). The sub-node body (D_p=0.84fm = ℓ_node/459) is genuinely sub-
  Nyquist; the winding survives (phasor-invariant), the body is aliased. [§36/§45.]
- **√(3/7) elastic-type** (dilatational vs torsion-shear; Grant decision #4).
- **Recurring session pattern (load-bearing meta).** The orchestrator
  repeatedly inflated Grant's good INTUITIONS into "new mechanisms" and reasoned
  from a partial archive slice — multiple corrections from Grant's pointers
  (φ-premise inverted; z₀ "untouched"/the 2026-05-18 z₀ effort missed;
  chiral-matching ungrounded; cog→belt-trick; spherical-vs-cubic envelope). Next
  effort: GROUND intuitions + SWEEP the archive BEFORE framing a result. [§24/§28/§31.]

## 7. The scoped soliton-size adoption plan (the recommended next workstream)

Gated on the §47 vocab-disambiguation lock + Grant greenlight. When unblocked,
the adoption deliverable is (from §46/§47):

1. **Canonical soliton-size leaf** — two SPATIAL sizes across the Nyquist node
   (real-space body above ℓ_node / sub-node SPATIAL charge-core below) + the
   phase-space WINDING ((2,3)) recorded as a DISTINCT identity axis, NOT a size.
2. **`r_opt → κ_share` rename** (0 corpus hits; dimensionless coupling-budget;
   lint: NEVER × ℓ_node) — completes the §43 walk-back.
3. **A SEPARATE name for the 2nd genuine length** (`r_env` / saturation-boundary)
   — §47 found r_opt also denotes a real soliton HWHM/tube-radius in live
   fit-params; "r_opt is dimensionless" was only half the story.
4. **§43 A/B resolution recorded** (once Grant decides #2/#3) — bug (A) vs
   correct-scale STLs (B).
5. **§45 GAP closure** — name the ≥6 length scales the corpus conflates
   (ℓ_node=substrate-spacing, D_p=charge-radius, Compton=localization, …).
6. **Cross-section-vs-radius fix** — `02_baryon_sector.tex:40` equates an AREA
   (L²) to a LENGTH (L); the 0.84fm is the charge RADIUS, mislabeled.
7. **`ACCURATE_SCALING.md` two-size update** + **`dimensional-provenance-check`
   κ_share lint** + **`ave-walk-back` propagation** across the 14 surfaced sites.

## 8. SKILL-CANDIDATE (watch list)

- **`lock-vocab-before-canonizing`** (§46) — verify-before-cite extended to
  definitional clarity: a 5-way term cross-check (corpus-usage + axis +
  dimension + collision + ambiguous-usage hunt) BEFORE locking a new canonical
  term. Applied first to this adoption (the `w1pc27h3k` disambiguation IS the
  skill in action — it found 14 ambiguous load-bearing terms before the canon
  was written). Draft if it recurs / earns tenure.

## 9. WORKTREE-PRUNE list (list-only — do NOT prune this session)

AVE-Core carries **46 worktrees**: 21 KEEP (open-PR) + 22 PRUNE-SAFE + 3 HOLD.
Reproduced via `git worktree list`, `gh pr list`, `git branch --merged
origin/main`, `git cherry origin/main <branch>`, `git status --short`.
`origin/main` HEAD = `63e6671a`. **This session lists only — it prunes nothing.**

### KEEP (21) — one per open PR; do NOT prune

Every open PR (#117–#137) maps 1:1 to a live worktree (table in the PR review
guide). All clean except the main checkout. **The main checkout
`/Users/grantlindblom/AVE-staging/AVE-Core` is parked on `analysis/2026-06-07-
two-node-alpha-projection` (= PR #126)** and carries 1 untracked stray not part
of #126: `_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-state-
audit-2026-06-06.md`. KEEP regardless; flagging the stray.

### PRUNE-SAFE (22) — merged OR stale-no-PR, working tree CLEAN

**A. Merged-to-origin-main + clean (12):**
- `/private/tmp/ave-bemf-long` (PR #89) · `/private/tmp/ave-ds-build` (PR #86)
- `…/AVE-Core-coherence-reynolds-wt` (#109) · `…/AVE-Core-doc-reconciles-wt` (#102)
- `…/AVE-Core-entrainment-wt` (#115/#112) · `…/AVE-Core-holonomy-wt` (#110)
- `…/AVE-Core-nb-wt` (#84) · `…/AVE-Core-quaternion-wt` (#99)
- `…/AVE-Core-skindepth-wt` (#97) · `…/AVE-Core-trampoline-wt` (#106)
- `…/.claude/worktrees/agent-a78af06c7311976b7` — gravity-ppn-coherence (#91
  MERGED — corrects the MEMORY stale-belief that recorded this branch "not merged")
- `…/.claude/worktrees/agent-a7f46b8c6ecb22523` — electron-rotor-synthesis (#116,
  == origin/main parent)

**B. Merged-by-ancestry + clean + LOCKED (3) — need `git worktree unlock` first:**
- `…/.claude/worktrees/agent-a69468dce2e62b5d4` — casimir-coldfusion-walkbacks
- `…/.claude/worktrees/agent-a93319e705a22375f` — placeholder branch
- `…/.claude/worktrees/agent-ac61b174858eddb7b` — qg42-resume

**C. Stale (no PR, real unmerged commits) + clean (7)** — branch ref retains
commits after `git worktree remove`; no data loss:
- `/private/tmp/ave-bemf` — motion-stability-bemf [5 commits, 2026-06-04]
- `/private/tmp/ave-bemf-cos` — motion-stability-bemf-cosserat [2, 2026-06-04]
- `/private/tmp/ave-ii-build` — moving-electron-probe [9, 2026-06-04]
- `…/AVE-Core-integrator-wt` — cosserat-geometric-integrator [7, 2026-06-06]
- `…/AVE-Core-obs-battery-wt` — genesis-armB-flywheel-seed [2, 2026-06-06]
- `/private/tmp/ave-vol0-recon-wt` — vol0-kb-reconciliation-ledger [4, **2026-06-08
  = today**] ⚠ RECENT — confirm not mid-flight before prune
- `…/AVE-Core-pathc-wt` — pathc-z0-amorphous-emt [2, **2026-06-08 = today**] ⚠
  RECENT — confirm not mid-flight before prune (this is the §29/§31 Path C branch)

### HOLD (3) — uncommitted changes present; do NOT prune (protects un-saved work)

- `…/AVE-Core-genesis2-wt` — saturation-tir-moving-boundary (STALE, 4 unmerged
  commits) — **4 MODIFIED tracked files (un-saved work):**
  `assets/sim_outputs/trefoil_alpha_qfactor.png`,
  `src/ave/topological/cosserat_field_3d.py`,
  `src/ave/topological/k4_cosserat_coupling.py`,
  `src/ave/topological/vacuum_engine.py`
- `…/AVE-Core-fbd-wt` — fluxtube-dynamics-fbd (MERGED) — **1 untracked research
  doc:** `research/2026-06-07_electron-flux-tube-dynamics-fbd.md`
- `…/AVE-Core-2-3-wt` — 2-3-winding-extractor (MERGED) — **2 untracked sim
  artifacts (likely regenerable):** `…r10_2_3_winding_extractor_coordinate_
  capture.npz`, `…_coordinate_results.json`

**Scope note:** AVE-Core worktrees only (the 46 in `git worktree list`). Sibling
repos (HOPF, PONDER, …) not triaged this turn.

## 10. Cross-references

- **Detailed phase log:** [`2026-06-07_electron-synthesis-epic.md`](2026-06-07_electron-synthesis-epic.md)
  §0–§47 (carried by PR #120) — the full session narrative, all workflow IDs,
  every walk-back and correction.
- **Per-PR review:** [`2026-06-08_pr-review-guide.md`](2026-06-08_pr-review-guide.md)
  — the 21-PR fast-review checklist, dependency + risk ordered.
- **Orchestration index:** [`index.md`](index.md) — the 2026-06-08 reconciliation
  section carries the priority-ladder + open-decisions + PR-queue deltas.

## Post-consolidation addendum (2026-06-08)

Three items closed/clarified after the §16–§47 handoff above was frozen.

- **(i) Double-slit capstone — the QM-trio made empirical (PR #139, epic §48).**
  The §33 trio (superposition=aliasing / collapse=sampling / entanglement=thread)
  now has its empirical capstone: a real FDTD interference field read out by a
  competing-Poisson **click detector** that recovers the Born statistic
  `p ∝ |ψ|²` from discrete clicks with **NO Born / `p=|ψ|²` / multinomial /
  inverse-CDF anywhere in the detector** — click placement is an FDT
  threshold-crossing first-passage race (no observer, no projection postulate).
  **Auditor verdict: GENUINE-EMERGENCE.** Killer non-circularity = the
  regime-dependence probe: a low-contrast ramp gives a **3.47× ratio**, NOT the
  **25× of hidden rate-squaring** NOR a **regime-invariant fixed-χ² |ψ|²-sampler**;
  validation χ²/dof=1.02, KS=0.009, corr=0.968, n=6000 on a real field with deep
  `|E|²=0` nulls. **HONEST SCOPE:** what emerges is the **collapse mechanism**
  (discrete clicks out of a continuous field) + **click-density ∝ power**; the
  exponent **"2" is the EM energy-vs-amplitude power-law — physically forced, NOT
  topology-derived** (the (2,3) winding is not shown here). consistency-vs-
  emergence: **Class-2 emergence** (clicks + |ψ|² stats) + **Class-4 consistency**
  (Born + Fraunhofer). 2 auditor nits being closed on #139 (commit-verb
  "DERIVED"→"energy-forced"; argmax-fallback asserted-zero counter).
- **(ii) #127 vacuum-piezoelectric — CONFLICTING → RESOLVED, MERGEABLE/CLEAN.**
  origin/main advanced (`translation-circuit.md` gained §10, the 2026-06-07
  reframes), putting #127 in conflict on that leaf. Resolved via a **KEEP-BOTH
  merge of origin/main**: main's §10 reframes kept verbatim + the piezo section
  **renumbered §10→§11** ("The vacuum as a chiral piezoelectric Cosserat solid");
  **nothing dropped** (merge diff `+21/−0`, `make verify` green). #127 has since
  MERGED to main (commit `2e12040`, mergedAt 2026-06-08T17:52Z).
- **(iii) The Vacuum Datasheet already exists — it IS Vol 9.** The "vacuum =
  chiral piezoelectric Cosserat solid" prose (§30/§32, PR #127) is a *consistency
  reframe of one operating point*, not a new datasheet: **Vol 9 IS the canonical
  Vacuum Datasheet.** Ch.1 (`vol_9_vacuum_datasheet/chapters/01_general_description.tex:18`)
  carries the substrate **IDENTITY** — "a 3D chiral Laves K4 Cosserat crystal …
  with right-handed `I4₁32` chiral space group, 4-fold K4 nearest-neighbour
  connectivity, and intrinsic LC oscillators at every node". Ch.14
  (`chapters/14_phase_diagrams.tex`) carries the **PHASE DIAGRAM** — the
  operating-point axis (Regime I linear / II saturating / III avalanche / IV
  rupture, along the Ax 4 kernel) AND the cosmic axis (standard / ruptured-plasma
  / lattice-genesis). **The prior prose "solid" description is Regime I** (linear /
  small-signal: `r < √(2α) ≈ 0.1208`, `S > 0.993`, "standard Maxwell/Newton
  recovered") **of that phase-diagram** — one cell of Vol 9 ch14, not a standalone
  characterization. Reframes the datasheet-program question (#124): the program is
  a Vol 9 cross-check, not a net-new artifact.
