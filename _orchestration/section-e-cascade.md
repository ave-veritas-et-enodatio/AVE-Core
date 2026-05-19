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
  - Driver: [`src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py`](../src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py)
  - Result JSON: [`cmb_axis_alignment_executable_observer_results.json`](../src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer_results.json)
  - Execution-session prereg: [`research/2026-05-19_c5-cmb-axis-executable-observer-prereg.md`](../research/2026-05-19_c5-cmb-axis-executable-observer-prereg.md)
  - Result doc: [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](../research/2026-05-19_c5-cmb-axis-executable-observer-result.md)

### Phase E1b-prime (PENDING) — Pantheon+ raw-SN bulk-flow re-fit

**Briefing status**: NOT YET DRAFTED. To be appended to this phase entry when Grant greenlights kickoff.

**Scope intent** (sketch; subject to full briefing once greenlit):
- Target: tighter Hubble-flow direction via Pantheon+ raw-SN re-fit at AVE-substrate-native priors
- Mechanism: replace literature σ_Hubble ~30° with self-derived bulk-flow uncertainty using Pantheon+ DR1 raw light-curve fits + AVE-axis prior
- Acceptance criteria: if CMB-Hubble separation tightens such that empirical separation (74.6° per E1b) crosses 3σ on either side → C5 settles to A (PASS — tension) or C (NULL)
- Implementor session pattern: single deliverable on `analysis/c5-pantheon-tightening` (or similar) off `analysis/integration`; standard skill discipline; ~1-2 sessions; push without merge for orchestration review

**Gates**: Grant adjudication required before drafting full briefing.

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
| [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) | 33-row matrix at HEAD; C3 row + C5 row + D4-A034 row + C4 three-route |
| [`manuscript/ave-kb/common/closure-roadmap.md`](../manuscript/ave-kb/common/closure-roadmap.md) | Running changelog §0.5; E1a + E1b entries dated 2026-05-19 |
| `audit/2026-05-19_c3-muon-delta-driver-rerun` | Immutable audit tag, E1a |
| `audit/2026-05-19_c5-cmb-axis-driver` | Immutable audit tag, E1b |
| [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](../research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md) | E1b's frozen methodology prereg (commits `fb9d9c0` + `1b2ef6d` + `fc05b5c`) |

## Provenance

- Section E cascade tracked as one epic per orchestration convention promoted 2026-05-19 EOD
- E1a + E1b implementor sessions originally kicked off via loose handoff docs at `~/.claude/plans/` (pre-convention-promotion); historical artifacts preserved at those paths
- This doc consolidates orchestration state for the epic; the next orchestration session reads from this doc + `index.md`, not from loose plans/ files
