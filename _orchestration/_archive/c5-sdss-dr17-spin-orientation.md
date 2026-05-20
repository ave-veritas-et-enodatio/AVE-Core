# C5 SDSS DR17 Spin-Orientation Re-Analysis Epic

**Status**: ACTIVE — implementor kickoff ready (Grant adjudicated Option A 2026-05-19 EOD: SDSS DR17 spin-orientation re-fit only; parallel-runnable with h-infinity-downstream-cascade)
**Last updated**: 2026-05-19 EOD
**Originating session**: Orchestration session post-E1b-prime Outcome Marginal-D + Grant adjudication 2026-05-19 EOD ("yes queue it up" + subsequent "let's proceed")

## Why this exists

E1b-prime (Pantheon+ raw-SN bulk-flow tightening, merged 2026-05-19 EOD at `c587573`, audit tag `audit/2026-05-19_c5-pantheon-tightening`) tightened σ_Hubble from literature ~30° to 24°. Outcome: **Marginal-D** — improved bounds, but NOT 3σ-decisive (would require σ_Hubble < 18.2° to fire the sharpest-falsifier criterion "CMB axis vs Hubble flow misaligned >20° at 3σ"). Per the C5 result doc:

> The Pantheon+SH0ES catalog at z<0.1 cannot reach the required precision due to the small residual bulk-flow magnitude (~155 km/s) after VPEC subtraction (chi²/dof = 0.916 confirms uncertainties well-calibrated; no methodology slack to recover).

The natural next-session move is SDSS DR17 spin-orientation re-analysis — an INDEPENDENT observable on the same cosmic axis (Ω_freeze projection) with comparable tightening potential. The current LSS galaxy-spin-axis literature value comes from Longo 2011 + Shamir 2020 with σ_LSS ~ 30°. SDSS DR17 (2021 release) has tighter spin-orientation data than Longo's 2011 work. A re-analysis with the larger DR17 catalog + AVE-substrate-prior methodology could push σ_LSS to <15°, sufficient to decide CMB-vs-LSS at 3σ.

If CMB-LSS lands 3σ-decisive (PASS or NULL), this UNLOCKS:
- C5 row: Marginal-D → A (PASS) or C (NULL)
- D4-A034 cosmic instance: HELD → strengthening or retirement
- E1c (Route 3 framework-commitment activation): DEFERRED → activation gate clears
- C4 three-route Route 3 ($\mathcal{J}_{\text{cosmic}}$) anchor: DEFERRED → enters active testing
- Foreword anchor list: potential third SPARC-parity anchor (if 3σ-PASS) per `omega-freeze-cosmic-grain-cascade.md:46-58` 8-observable cascade

If CMB-LSS lands NULL, the cosmic-row D-status concentrates the remaining falsification surface on Observables 5-7 (E/B polarization, orbital alignments, G P_2 anisotropy) per `omega-freeze-cosmic-grain-cascade.md`. The framework's other 20+ A-034 instances are unaffected per `universal-saturation-kernel-catalog.md`.

## The math question (precisely stated)

The current SDSS LSS pin at $(l = 32°, b = 32°), \sigma = 30°$ comes from Longo 2011 + Shamir 2020. The E1b empirical CMB axis at $(l = 60.28°, b = 50.48°), \sigma = 0.92°$ sits 27.9° away from the SDSS pin — marginally within 1σ alignment (per `2026-05-19_c5-cmb-axis-executable-observer-result.md:43`). With σ_LSS = 30°, the 27.9° separation does NOT clear 3σ in either direction.

The questions:
- **Q1**: Can σ_LSS be tightened to <15° using SDSS DR17 (the newer, larger catalog)?
- **Q2**: Does the SDSS DR17 spin-orientation pin land at the same central value as Longo 2011 ($l ≈ 32°, b ≈ 32°$), or does it shift?
- **Q3**: Either way, what's the CMB-LSS separation post-DR17 + significance?

## Scope options for Grant adjudication

| Option | Scope | Effort | Outcome decisiveness |
|---|---|---|---|
| **A** | SDSS DR17 spin-orientation re-fit ONLY | ~2-3 hr | Decides CMB-LSS alignment at potentially 3σ |
| **B** | Option A + joint Pantheon+ + SDSS DR17 + (Whitford+2023 baseline) constraint | ~3-4 hr | Joint analysis tightens further; decides CMB-vs-(Hubble∧LSS) pair |
| **C** | Option B + add LiteBIRD / BICEP forecast for Observable 5 (E/B polarization) as a sub-finding | ~4-5 hr | Same as B + flags Observable 5 readiness for next session |

**Recommendation**: Option A. Single-observable session; if PASS / NULL clears at 3σ, downstream cascade activates and Option B+C scope becomes follow-up epic. If A stays in Marginal-D / suggests deeper systematics, Option B is the natural escalation.

## Resolved decisions (Grant adjudication 2026-05-19 EOD)

| # | Decision | Resolution |
|---|---|---|
| G1 | Which scope option (A/B/C)? | **A** — SDSS DR17 spin-orientation re-fit ONLY (~2-3 hr); if outcome stays Marginal-D / surfaces deeper systematics, Option B (joint Pantheon+ + SDSS) is the natural escalation in a follow-up epic |
| G2 | Run in parallel with h-infinity-downstream-cascade? | **PARALLEL** — different repos/files (this epic touches `src/scripts/vol_3_macroscopic/` + research/ + matrix; downstream-cascade touches Vol 1-3 KB leaves + engine annotation). Both via `isolation: "worktree"`. |
| G3 | SDSS DR17 access path | **Implementor responsibility** — verify Q-cuts methodology against Hayes+2017 / Land+2008. Use `verify-before-cite` v1.3 for citations + cross-branch checks on canonical methodology references. |
| G4 | AVE-substrate prior on SDSS spin orientation | **Forward-prediction**: Observable 3 (LSS spin direction) per `omega-freeze-cosmic-grain-cascade.md:48-57` predicted to align with $\hat{\Omega}_{\text{freeze}}$ at (60.28°, 50.48°). Implementor estimates direction INDEPENDENTLY then compares (per `ave-driver-script-honesty`). |

## Phase plan (LOCKED — Option A scope; implementor kickoff input)

**Branch**: `analysis/c5-sdss-dr17-spin-orientation` from `analysis/integration` HEAD `cb43eb5` (or current at session start — verify Phase 0)
**Push**: yes (at end of Phase 4)
**Merge**: NO — orchestration session handles merge after audit

**Phase 0 — verification + skill upfront fires** (20 min)
- Verify SDSS DR17 catalog availability + access path
- Verify Hayes+2017 / Land+2008 methodology citations + AVE-substrate-prior at `omega-freeze-cosmic-grain-cascade.md`
- `ave-prereg` corpus-grep for prior SDSS / LSS / galaxy-spin work
- `ave-canonical-leaf-pull` for relevant problem-class leaves
- Branch creation

**Phase 1 — SDSS DR17 catalog ingest** (45-60 min)
- Download / verify-checksum the relevant DR17 spin-orientation catalog
- Ingest + Q-cuts per Hayes+2017 / Land+2008 methodology
- Update `data/sdss_dr17/README.md` for canonical-cache reproducibility (per Pantheon+ pattern)

**Phase 2 — Spin-axis estimator + uncertainty propagation** (60-90 min)
- Implement spin-axis estimator (max-angular-momentum-dispersion analog, OR L11/S20-methodology depending on Q3 adjudication)
- Bootstrap uncertainty propagation (block-bootstrap per E1b-prime template; Hessian-MC parallel sub-analysis)
- AVE-substrate-prior forward-prediction: predict spin direction independently, then compare

**Phase 3 — Compare to CMB axis + result doc** (30-45 min)
- Compute CMB-LSS separation + significance vs 20° threshold
- Outcome adjudication per pre-registered table: A (PASS) / C (NULL) / D (insufficient) / E (methodology)
- Update C5 row in `divergence-test-substrate-map.md`
- Update closure-roadmap entry

**Phase 4 — Audit + push** (15 min)
- `ave-auditor` review
- Push branch `analysis/c5-sdss-dr17-spin-orientation`
- Do NOT merge

## Skill discipline (per phase plan above)

- `ave-prereg` upfront — corpus-grep across all 10 AVE-staging repos for prior SDSS / LSS / galaxy-spin work
- `ave-canonical-leaf-pull` — enumerate canonical leaves for LSS-direction / data-fitting / propagation-direction problem class
- `ave-canonical-source` — confirm constants imports
- `verify-before-cite` v1.3 — every citation (esp. trigger 8 for commits, trigger 7c for cross-branch state)
- `ave-driver-script-honesty` — forward prediction not fit-to-target
- `ave-discrimination-check` — IF outcome PASS, apply SM-counterfactual + interpretive-alternatives
- `ave-walk-back` — IF outcome closes C5 row decisively, propagate matrix + closure-roadmap updates + 8-observable table at `omega-freeze-cosmic-grain-cascade.md`
- `consistency-vs-emergence` v1.1 — Class E classification for the LSS spin direction (it's one of 8 projections of Ω_freeze; same operating-point projection class as H_∞ + G)

## Expected return summary

- Branch + tip commit
- Per-phase commit hashes + summaries
- Outcome verdict: A / C / D / E
- σ_LSS achieved (degrees)
- CMB-LSS separation + significance
- Cascade implications: C5 row status, E1c unblock/defer
- ave-auditor verdict
- Any anomalies surfaced

## Cross-references

- E1b-prime that surfaced the next-step recommendation: [`section-e-cascade.md`](section-e-cascade.md) Phase E1b-prime (closed via merge `c587573`)
- C5 row state: `manuscript/ave-kb/common/divergence-test-substrate-map.md` lines 428, 514, 554, 907
- 8-observable cascade with LSS spin-direction as Observable 3: [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:48-57`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)
- Cosmic-axes glossary (load-bearing K4-rest-frame ↔ Ω_freeze distinction): [`manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md`](../manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md)
- Parallel-runnable epic: [`h-infinity-downstream-cascade.md`](h-infinity-downstream-cascade.md) (Class E reclassification + 5 anomalies; different files, no conflicts)
