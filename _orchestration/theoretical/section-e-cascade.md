# Epic: Section E cascade — multi-anchor validation through C5

**Status**: ACTIVE
**Started**: 2026-05-18 (per `audit/2026-05-18_c3-muon-delta-fermilab-outcome-b` precursor)
**Goal**: Close C3-MUON-DELTA + C5-CMB-AXIS + E1c Route 3 framework-commitment activation in sequence
**Last updated**: 2026-05-19 EOD

## Current state at HEAD `54f0698`

E1a and E1b implementor sessions complete + merged + audit-tagged. E1b returned Outcome D (data-insufficient at 3σ due to wide σ_Hubble ~30°), so E1c is deferred until C5 settles via tighter data. E1b-prime (Pantheon+ raw-SN bulk-flow re-fit) is the natural next implementor session — would push CMB-vs-Hubble to 3σ-decisive and unlock E1c.

The three foreword-promoted scale anchors stand:
- **C13a-GAL-ROT** (galactic kpc, 11.5% Q=1 SPARC residual)
- **C1-BH-RING** (BH-class km, -0.45% ω_R / -0.47% τ)
- **C8-BARYON-LADDER** (hadronic fm, -0.002% proton + 6/6 J^P)

C3 post-walk-back stands as PASS-conditional with deeper-on-BMW tension; C5 stands as D awaiting tightening; E1c gated.

## Phases

### Phase E1a (CLOSED 2026-05-19) — C3-MUON-DELTA driver rerun

- **Orchestration brief origin**: `~/.claude/plans/ok-take-a-fully-golden-flask.md` (historical loose-location artifact; content load-bearing for retrospective audit captured here)
- **Pre-execution amendment audit**: `~/.claude/plans/review-this-message-you-cached-penguin.md` — 5 pre-execution amendments needed before implementor ready (driver state / template path / M_MU import / BMW baseline gap / Phase 0 audit-context / CLAUDE.md atopile)
- **Outcome**: PASS-conditional
  - Forward Δa_μ⁽²⁾ = +501.78×10⁻¹¹ (canonical +502)
  - **+4.59σ ABOVE Fermilab on e+e- baseline**
  - **+6.68σ DEEPER on BMW lattice baseline** per Borsanyi+ 2021 (BMW closes Fermilab anomaly toward ~0σ, leaving AVE +502 unabsorbed — tension worse on BMW, not softer per Q-G27 leaf canonical)
- **Closes walk-back queue item #6** from 2026-05-18 result doc §6: driver code now synchronized to post-walk-back canonical state across leaf + matrix + driver + closure-roadmap
- **Merge**: `e61a3dc` on `analysis/integration`
- **Audit tag**: `audit/2026-05-19_c3-muon-delta-driver-rerun`
- **ave-auditor verdict**: PROMOTE 10/10
- **Artifacts**: driver `src/scripts/vol_2_quantum/c3_muon_delta_forward_prediction.py`; result doc / matrix updates per merge stat

### Phase E1b (CLOSED 2026-05-19) — C5-CMB-AXIS executable observer

- **Orchestration brief origin**: `~/.claude/plans/e1b-c5-cmb-axis-handoff.md` (historical loose-location)
- **Outcome**: **Outcome D (DATA INSUFFICIENT at 3σ)**
  - Empirical Planck PR3 SMICA axis-of-evil at **(l=60.28°, b=50.48°)**
  - Strong intrinsic alignment: ℓ=2 vs ℓ=3 axes 16.9° apart; joint dispersion 1.252 = **88% of theoretical max** (1.417)
  - CMB-Hubble = 74.6° at **1.82σ** (NOT 3σ-decisive)
  - CMB-LSS = 27.9° marginally within 1σ
  - Central values lean toward C (NULL) but literature σ_Hubble ~30° (Whitford+2023) too wide to reject A at 3σ
  - Sharpest single falsifier (CMB-Hubble >20° at 3σ per `closure-roadmap.md:35`) NOT TRIGGERED at 3σ
- **Corpus citation gap EMPIRICALLY PINNED**: corpus (l=174°, b=-5°) yields dispersion 0.571 = only 46% of data max → corpus value is NOT the data's preferred axis. Per `closure-roadmap.md:100` option (c), execution makes the literature citation moot — empirical axis emerges from the data.
- **Cascade implications**:
  - D4-A034 cosmic row HELD PENDING tighter Hubble-flow / SDSS data (no retirement; no strengthening)
  - C4 three-route Route 3 (𝒥_cosmic) anchor REMAINS DEFERRED on A-031 cosmic-parameter-horizon
  - E1c (Route 3 framework-commitment activation) DEFERRED until C5 settles via tighter data
- **Merge**: `54f0698` on `analysis/integration`
- **Audit tag**: `audit/2026-05-19_c5-cmb-axis-driver`
- **ave-auditor verdict**: APPROVED-WITH-NOTES (10/10 audit checklist + A+/E execution-refinement note addressed in result-doc §1.5; minor follow-up unit-test queued)
- **Artifacts**:
  - Driver: [`src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py`](../../src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py)
  - Result JSON: [`cmb_axis_alignment_executable_observer_results.json`](../../src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer_results.json)
  - Execution-session prereg: [`research/2026-05-19_c5-cmb-axis-executable-observer-prereg.md`](../../research/2026-05-19_c5-cmb-axis-executable-observer-prereg.md)
  - Result doc: [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](../../research/2026-05-19_c5-cmb-axis-executable-observer-result.md)

### Phase E1b-prime (PENDING — full briefing below, ready for implementor) — Pantheon+ raw-SN bulk-flow re-fit

**Briefing status**: ACTIVE — Grant adjudicated 2026-05-19 EOD; implementor kickoff ready. Plumber-physical question resolved per the K4-rest-frame ↔ $\hat{\Omega}_{\text{freeze}}$ distinction below.

#### Resolved pre-execution plumber question (Grant adjudication 2026-05-19 EOD)

AVE corpus carries TWO physically distinct cosmological direction concepts (canonical leaf: [`cosmic-axes-and-frames-glossary.md`](../../manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md) — landed on `analysis/cosmic-axis-glossary` branch, pending merge to `analysis/integration`):

1. **K4 lattice rest frame** — where the substrate $\mathcal{M}_A$ sits at rest. Sun's velocity vector through this frame = CMB dipole at $(l \approx 264°, b \approx 48°)$, $\sim 370$ km/s. Local kinematics. **NOT a fundamental cosmological axis.**
2. **$\hat{\Omega}_{\text{freeze}}$** — parent-BH spin axis preserved through K4 crystallization at lattice genesis. Cosmic chirality direction from $I4_132$ space group lock-in. Empirically pinned at $(l = 60.28°, b = 50.48°)$ via Planck PR3 SMICA axis-of-evil. **Cosmological initial condition.**

Angular separation $|\hat{v}_{\odot \to \mathcal{M}_A}, \hat{\Omega}_{\text{freeze}}| \approx 79°$ (minimum, accounting for 180° axis degeneracy).

**Pantheon+ peculiar-velocity correction subtracts $\hat{v}_{\odot \to \mathcal{M}_A}$ at the CMB DIPOLE direction.** It does NOT touch $\hat{\Omega}_{\text{freeze}}$. The two are nearly orthogonal observables of the same substrate at different scales (local kinematics vs. cosmic-genesis chirality). Standard pipeline is therefore structurally non-circular for the test "does Hubble bulk-flow direction align with $\hat{\Omega}_{\text{freeze}}$?"

**Implementor uses standard Pantheon+ pipeline** (heliocentric → CMB-rest-frame transform + 2M++ LSS peculiar-velocity correction). Defense-in-depth: also report a parallel sub-analysis using heliocentric velocities with 2M++ LSS correction only (no CMB-rest-frame transform). Both analyses must give consistent bulk-flow direction (1σ contour overlap) for the result to count as a valid PASS. Divergence between the two is itself diagnostic.

#### Context

E1b returned Outcome D because literature σ_Hubble ~30° (Whitford+2023 MNRAS 526:3051) is too wide to reject the CMB-Hubble separation (74.6° empirical) at 3σ. Per `divergence-test-substrate-map.md:554` "What's needed" column: tighter Pantheon+ raw-SN bulk-flow re-fit (1-2 sessions; would push CMB-Hubble to 3σ-decisive).

Pantheon+SH0ES dataset is already cached locally at `data/pantheon_plus/Pantheon+SH0ES.dat`. The session's job is to re-fit the bulk-flow direction (and its uncertainty) from raw light curves, applying AVE-substrate priors, and produce a tightened σ_Hubble that either decisively rejects or accepts CMB-Hubble alignment.

#### Branch strategy

- **Branch**: `analysis/c5-pantheon-tightening` off `analysis/integration`
- **Base HEAD**: `813b9c3` (or current HEAD at session start — verify in Phase 0)
- **Push without merge** — orchestration session reviews + merges via `--no-ff` + audit tag pattern

#### Assumptions A1-A8 (verify at Phase 0)

A1. **Pantheon+SH0ES data accessible** at `data/pantheon_plus/Pantheon+SH0ES.dat`. Format = whitespace-separated ASCII with header row; ~1700 SNe at z<0.1 expected.

A2. **Existing C5 driver is the template foundation**: [`src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py`](../../src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py) (40125 bytes) — reuse Planck/SMICA-axis ingestion + axis-comparison framework; ADD Pantheon+ bulk-flow estimator + uncertainty propagation.

A3. **E1b empirical CMB axis is the reference**: $(l=60.28°, b=50.48°)$, σ ~ 0.9°, sourced from E1b result doc [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](../../research/2026-05-19_c5-cmb-axis-executable-observer-result.md). The comparison is "Pantheon+ bulk-flow direction vs this CMB axis."

A4. **Bulk-flow estimator class + velocity convention** (RESOLVED 2026-05-19 EOD): maximum-likelihood fit on peculiar-velocity-corrected distances at z<0.1, using the **standard Pantheon+ pipeline** (heliocentric → CMB-rest-frame transform via conventional CMB dipole $(l \approx 264°, b \approx 48°)$ + 2M++ LSS peculiar-velocity correction). Methodology follows Watkins-Feldman-Hudson 2009 ML approach (or Howlett+Said-style velocity tomography if WFH09 lacks fit-precision).

**Justification (per resolved plumber question above)**: the rest-frame correction subtracts solar motion at the CMB DIPOLE direction $(l \approx 264°, b \approx 48°)$, which is angularly separated from $\hat{\Omega}_{\text{freeze}} = (l = 60.28°, b = 50.48°)$ by ~79° (minimum, 180° axis degeneracy). The subtracted direction is nearly orthogonal to the tested direction; standard pipeline does NOT pre-impose AVE prediction. Test is structurally non-circular.

**Defense-in-depth sub-analysis (REQUIRED)**: in parallel with the primary fit, run a sub-analysis using heliocentric velocities with 2M++ LSS correction only (no CMB-rest-frame transform). Both analyses must produce consistent bulk-flow direction estimates (1σ contour overlap on the sky) for the result to count as a valid PASS / NULL adjudication. Divergence between the two analyses is itself a sub-finding and gets reported (could indicate either: K4=CMB-rest-frame Q-G24 identification needing refinement, OR LSS-reconstruction methodology contaminating with rest-frame structure). Both fits' directional outputs (best-estimate + σ_Hubble) reported in the result doc.

A5. **AVE-substrate prior**: forward-prediction — AVE predicts Hubble bulk-flow direction = CMB axis = (60.28°, 50.48°). Implementation MUST NOT fit Hubble direction TO CMB axis (per `ave-driver-script-honesty`); instead estimate Hubble direction independently then compare.

A6. **σ_Hubble target precision**: <15° (half of current ~30°) is the load-bearing precision threshold for 3σ-decisive on the 74.6° separation. If estimator yields σ_Hubble in [15°, 25°], outcome is "marginally improved D"; if <15°, decisive.

A7. **C5 row state in matrix**: `divergence-test-substrate-map.md:428` + `:514` + `:554` shows "OUTCOME D (DATA INSUFFICIENT at 3σ)". Row updates needed at session end.

A8. **Cascade implications**:
- Outcome A (PASS — tension confirmed >3σ) → C5 row updates to PASS; E1c (Route 3 framework-commitment activation) UNBLOCKS for next session
- Outcome C (NULL — alignment confirmed <3σ) → C5 row updates to NULL; E1c needs alternative path (SDSS DR17 spin-orientation re-analysis); cascade re-routes
- Outcome D-sustained → C5 row stays D; next session is SDSS DR17 alternative
- Outcome E (methodology) → surface to Grant before retry

#### Scope boundary (strictly enforced)

**IN SCOPE**:
- Re-fit Pantheon+ bulk-flow direction (per Grant's plumber-question adjudication)
- Self-derive σ_Hubble from the re-fit (replace Whitford+2023 ~30° with new value)
- Recompute CMB-Hubble separation σ using new σ_Hubble
- Update C5 row in `divergence-test-substrate-map.md` (rows :428, :514, :554)
- Update closure-roadmap C5 entry at `closure-roadmap.md:80`
- Result doc at `research/2026-05-19_c5-pantheon-tightening-result.md` (or 2026-05-20 if session spans midnight)
- Driver script at `src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening.py` (or equivalent — Phase 0 verifies naming convention against E1b)
- ave-auditor verdict
- Push branch (do NOT merge)

**OUT OF SCOPE**:
- SDSS DR17 spin-orientation re-analysis (alternative path — separate session if needed)
- Observable 5 (E/B polarization), 6 (orbital), 7 (G P_2 anisotropy) — multi-session each
- E1c Route 3 framework-commitment activation (gated on this session's outcome)
- Any modifications to E1a (`audit/2026-05-19_c3-muon-delta-driver-rerun`) or E1b (`audit/2026-05-19_c5-cmb-axis-driver`) artifacts
- New physics derivations (this is data analysis, not theory work)
- Manuscript edits in `manuscript/vol_*/chapters/*.tex` (KB and closure-roadmap only)

#### Skills required (with trigger timing)

**Upfront fires (formal Skill invocations BEFORE any code):**
- `pre-test-physics-check` — DONE in this briefing (plumber question resolved 2026-05-19 EOD per K4-rest-frame ↔ $\hat{\Omega}_{\text{freeze}}$ distinction at top of brief)
- `ave-prereg` — corpus-grep across all 10 AVE-staging repos for prior bulk-flow / peculiar-velocity / Hubble-flow-direction work
- `ave-canonical-leaf-pull` — enumerate canonical leaves for data-fitting / propagation-direction / cross-section problem class
- `ave-canonical-source` — confirm any constants used (H_0, c, etc.) import from `src/ave/core/constants.py`, not hard-coded
- `verify-before-cite` — verify E1b axis + Whitford σ + Pantheon+ catalog refs at file:line

**Conditionally fired:**
- `ave-driver-script-honesty` — CRITICAL: verify the bulk-flow estimator is a forward-prediction (independent Hubble direction extraction) NOT a fit-to-target (fitting Hubble direction TO CMB axis); the four-discriminator check applies
- `consistency-vs-emergence` — classify the test (consistency-check comparing AVE prediction vs new data uncertainty, NOT an emergence test from axioms)
- `ave-discrimination-check` — before framing the outcome as "AVE-distinct" (the test is SM-counterfactual: SM has no a priori prediction for axis alignment)
- `ave-evidence-framing-discipline` — before any quantitative claim with strength language ("σ_Hubble tightens to X°", "X-σ decisive", "passes/fails at 3σ")
- `substrate-native-check` — if any solver / eigsolver work emerges (unlikely for this data-analysis session)

**Adhere internally (no formal Skill invocation):**
- `ave-handoff-canonical-locale` — this briefing IS the canonical location; the implementor reads it from here; the implementor MUST NOT create a new loose `~/.claude/plans/` file for this session

#### Infrastructure / KB references the agent will use

**Canonical leaves (read-only references)**:
- [`manuscript/ave-kb/common/divergence-test-substrate-map.md:428`](../../manuscript/ave-kb/common/divergence-test-substrate-map.md) + `:514` + `:554` (C5 row state)
- [`manuscript/ave-kb/claim-quality-closure-roadmap.md:80`](../../manuscript/ave-kb/claim-quality-closure-roadmap.md) (C5 entry)
- [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`](../../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md):86-92 (cosmic axis cite — preserved as superseded by empirical pin)
- [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](../../research/2026-05-19_c5-cmb-axis-executable-observer-result.md) (E1b result — empirical axis source)
- [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](../../research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md) (frozen methodology — Pantheon+ comparison axis specified)

**Driver + result-doc artifacts**:
- Existing C5 driver (Phase 1 + Phase 2): [`src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py`](../../src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py) (40125 bytes)
- E1b result JSON: [`src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer_results.json`](../../src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer_results.json)
- Pantheon+ data: [`data/pantheon_plus/Pantheon+SH0ES.dat`](../../data/pantheon_plus/Pantheon+SH0ES.dat) (cached)

**Existing template patterns (study before writing)**:
- C13a-GAL-ROT SPARC gold-standard public-data-ingest pattern (per closure-roadmap.md)
- C8-BARYON-LADDER paper-pinned epistemological grade for literature axes
- E1b C5 driver: full Planck/SMICA handling structure — pattern to mirror for Pantheon+

**Sub-agents available**:
- `ave-corpus-grep` (for cross-repo verification of prior bulk-flow work)
- `ave-auditor` (for final adjudication)

#### Phase plan

**Phase 0 — Session setup (~15 min)**
- Verify HEAD on `analysis/integration` matches handoff expectation (`813b9c3` or later)
- Branch creation: `git checkout -b analysis/c5-pantheon-tightening`
- Verify Pantheon+ data file readable + format understood (`head -5` + `wc -l`)
- Verify E1b empirical axis (60.28°, 50.48°) loaded correctly from result JSON
- Verify Grant's plumber-question adjudication present (heliocentric vs CMB-corrected velocities)
- Verify all assumptions A1-A8 hold; amend briefing in epic doc if any drift detected

**Phase 1 — Upfront skill discipline + corpus-grep (~20 min)**
- `pre-test-physics-check` ✓ (DONE in briefing — Grant's adjudication carried forward)
- `ave-prereg` → corpus-grep across all 10 AVE-staging repos for prior bulk-flow / peculiar-velocity / Hubble-flow-direction work
- `ave-canonical-leaf-pull` → data-fitting / propagation-direction canonical leaves
- `verify-before-cite` → confirm E1b axis + Whitford σ + Pantheon+ catalog refs

**Phase 2 — Bulk-flow estimator design + pre-registration (~30 min)**
- Document the bulk-flow estimator methodology (ML-fit class chosen per A4)
- Define AVE-substrate prior (forward-prediction, NOT fit-to-target)
- Pre-register acceptance criteria (A/C/D-sustained/E per A8)
- Pre-register σ_Hubble target precision thresholds (<15° decisive; [15°, 25°] marginal; ≥25° sustained-D)
- Write pre-registration doc at `research/2026-05-19_c5-pantheon-tightening-prereg.md` BEFORE writing any estimator code

**Phase 3 — Implementation (~60-90 min)**
- Implement bulk-flow estimator script
- Run on Pantheon+ DR1 sample (z<0.1 subset)
- Extract bulk-flow direction (l, b) + σ
- Recompute CMB-Hubble separation σ using new σ_Hubble
- Apply `ave-driver-script-honesty` check before running (four-discriminator)
- Apply `ave-canonical-source` check on any constants (H_0, c, etc.)

**Phase 4 — Result interpretation (~30 min)**
- Compare to E1b result (separation in degrees; new σ_Hubble)
- Apply `ave-discrimination-check` (is the outcome AVE-distinct from SM null?)
- Apply `ave-evidence-framing-discipline` (precise language; no "tightens significantly" without explicit Δσ numbers)
- Determine outcome A / C / D-sustained / E per A8

**Phase 5 — Documentation + audit (~30 min)**
- Result doc: `research/2026-05-19_c5-pantheon-tightening-result.md`
- Update C5 row in `divergence-test-substrate-map.md` (3 line groups: 428, 514, 554)
- Update closure-roadmap C5 entry at `closure-roadmap.md:80` (append new entry below existing 2026-05-19 entry, OR amend existing if outcome supersedes)
- Update `_orchestration/section-e-cascade.md` Phase E1b-prime status → CLOSED with outcome summary + merge commit ref (orchestration session will fill the merge commit hash post-merge)
- Spawn `ave-auditor` for final adjudication; record verdict
- Commit + push branch (do NOT merge)

#### Adjudication criteria (pre-registered, single-table)

| Outcome | σ_Hubble | CMB-Hubble sep | Action |
|---|---|---|---|
| **A — PASS (tension)** | < 15° | > 3σ separation from null | C5 row → PASS; E1c UNBLOCKS |
| **C — NULL (alignment)** | < 15° | < 3σ separation from null | C5 row → NULL; E1c needs alternative path |
| **D-sustained** | ≥ 25° | data still insufficient | C5 row → D; queue SDSS DR17 session |
| **Marginal D** | 15-25° | improved but not decisive | C5 row → D with refined-bounds note; queue joint constraint session |
| **E — methodology** | N/A | estimator fails or surfaces structural issue | Surface to Grant; pause before retry |

#### Verification at session start (Phase 0 checklist)

The implementor MUST verify before any code:

1. `git -C /Users/grantlindblom/AVE-staging/AVE-Core log analysis/integration -1 --oneline` matches expected HEAD (`813b9c3` or later)
2. `wc -l /Users/grantlindblom/AVE-staging/AVE-Core/data/pantheon_plus/Pantheon+SH0ES.dat` returns ~1700+ rows
3. `head -5 /Users/grantlindblom/AVE-staging/AVE-Core/data/pantheon_plus/Pantheon+SH0ES.dat` returns sensible SN data with recognizable Pantheon+ columns
4. `python /Users/grantlindblom/AVE-staging/AVE-Core/src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py --help` exits cleanly (or shows expected usage)
5. C5 row state in matrix matches handoff: `grep -A2 "C5-CMB-AXIS.*OUTCOME D" manuscript/ave-kb/common/divergence-test-substrate-map.md` returns the D state
6. Grant's plumber-question adjudication is present in this briefing (heliocentric vs CMB-corrected) — if NOT present, halt and ping Grant before any work

#### Provenance

Briefing drafted 2026-05-19 EOD by orchestration session immediately after `_orchestration/` promotion (commit `8773db0`) + Pantheon+ data availability confirmation (`data/pantheon_plus/Pantheon+SH0ES.dat` exists). Mirrors E1a/E1b handoff template structure. The empirical-axis reference (60.28°, 50.48°) comes from E1b commit `813624b` on the merged `analysis/c5-cmb-axis-driver` branch (now audit-tagged at `audit/2026-05-19_c5-cmb-axis-driver`). The plumber-physical question is the load-bearing pre-execution adjudication that must be answered before the implementor commits to a methodology direction.

### Phase E1c (DEFERRED) — Route 3 framework-commitment activation

**Status**: gated on E1b-prime outcome.

**Scope** (per pre-existing framework references; not yet implementor-ready):
- Three-route Route 3 (𝒥_cosmic) framework-commitment activation per `closure-roadmap.md` and C4 three-route documentation
- Requires C5 to settle to A or C; D outcome blocks
- If E1b-prime returns A or C decisively → unblock E1c briefing draft

**Trigger to un-defer**: E1b-prime returns 3σ-decisive on C5.

## Open decisions (epic-specific)

| # | Item | Status |
|---|---|---|
| E-1 | E1b-prime kickoff timing | PENDING Grant adjudication |
| E-2 | Whether to update corpus citations for empirical axis (174°, -5° → 60.28°, 50.48°) | DEFERRED — minor inline citation update, can be batched with hygiene pass; out-of-scope for E1b session per its handoff |
| E-3 | Independent SDSS DR17 spin-orientation re-analysis as alternative to Pantheon+ | OPEN — alternative path to C5 tightening; ~1-2 sessions; equivalently un-blocks E1c |

## References

| Path | Purpose |
|---|---|
| [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../../manuscript/ave-kb/common/divergence-test-substrate-map.md) | 33-row matrix at HEAD; C3 row + C5 row + D4-A034 row + C4 three-route |
| [`manuscript/ave-kb/claim-quality-closure-roadmap.md`](../../manuscript/ave-kb/claim-quality-closure-roadmap.md) | Running changelog §0.5; E1a + E1b entries dated 2026-05-19 |
| `audit/2026-05-19_c3-muon-delta-driver-rerun` | Immutable audit tag, E1a |
| `audit/2026-05-19_c5-cmb-axis-driver` | Immutable audit tag, E1b |
| [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](../../research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md) | E1b's frozen methodology prereg (commits `fb9d9c0` + `1b2ef6d` + `fc05b5c`) |

## Provenance

- Section E cascade tracked as one epic per orchestration convention promoted 2026-05-19 EOD
- E1a + E1b implementor sessions originally kicked off via loose handoff docs at `~/.claude/plans/` (pre-convention-promotion); historical artifacts preserved at those paths
- This doc consolidates orchestration state for the epic; the next orchestration session reads from this doc + `index.md`, not from loose plans/ files
