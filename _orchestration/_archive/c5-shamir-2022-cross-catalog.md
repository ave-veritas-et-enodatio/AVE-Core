# C5 Shamir 2022 Cross-Catalog Validation Epic

**Status**: ACTIVE — implementor kickoff ready
**Last updated**: 2026-05-19 EOD
**Originating session**: Orchestration session post-GZ-DECaLS Outcome-E merge at `0275a6a` (audit tag `audit/2026-05-19_c5-gz-decals-spin-orientation`). Walmsley+2022 GZ DECaLS lacked chirality observable; Shamir 2022 retarget identified in scoping doc §5.

## Why this exists

SDSS DR17 epic (merged 2026-05-19 EOD at `9f976e0`) found galaxy spin axis at **(l=129°, b=79°), σ=6.83°** using Galaxy Zoo 1 (Lintott+2011, crowdsourced visual inspection, SDSS DR7 imaging). Randomization-null z = 29.8σ unambiguously real.

GZ DECaLS attempt (#6 epic, merged Outcome E at `0275a6a`) discovered that Walmsley+2022's CNN-based catalog lacks chirality entirely — the chirality question was dropped from the GZ decision tree between GZ1 → GZ2 and never restored. GZ1 is the only Galaxy Zoo catalog with crowdsourced spiral chirality.

**Shamir 2022 (MNRAS 516:2204) — "Analysis of spin directions of galaxies in the DESI Legacy Survey"** — preserves the "different catalog + different methodology + different imaging" requirement of the original #6 spec:
- Ganalyzer algorithmic chirality (NOT crowdsourced, NOT CNN)
- DECaLS DR8 imaging (different from SDSS DR7 used by GZ1)
- Independent author + methodology

If Shamir 2022 independently recovers the (l=129°, b=79°) direction within 1σ, the SDSS DR17 result is robust to catalog/methodology/imaging — operator-output framing strengthened. If disagreement: methodology systematic dominates; SDSS DR17 result needs caveating.

## Scope (single-session implementor)

Same shape as the SDSS DR17 epic (audit tag `audit/2026-05-19_c5-sdss-dr17-spin-orientation`) but with the Shamir 2022 catalog as input.

### Branch + commit

- Branch: `analysis/c5-shamir-2022-cross-catalog` from `analysis/integration` HEAD (verify at session start)
- Multi-commit per SDSS DR17 template (data ingest → driver → result+matrix)
- Push at end
- **DO NOT MERGE** — orchestration handles merge

### Phase plan (mirrors SDSS DR17)

#### Phase 0 — verification + skill upfront fires (20 min)

- Read `_orchestration/_archive/c5-sdss-dr17-spin-orientation.md` (template) — note this is now under `_archive/`
- Read `research/2026-05-19_c5-sdss-spin-orientation-prereg.md` + result doc
- Read `research/2026-05-19_c5-gz-decals-spin-orientation-scoping.md` §5 (which identified Shamir 2022 as the retarget candidate)
- `ave-prereg` corpus-grep for prior Shamir / Ganalyzer / DECaLS DR8 work in 10 AVE-staging repos
- `verify-before-cite` v1.3: verify Shamir 2022 citation (MNRAS 516:2204) + DECaLS DR8 imaging + Ganalyzer methodology citations
- Identify Shamir 2022 catalog availability (paper supplementary material, MNRAS data archive, or author's GitHub/zenodo)
- Create branch `analysis/c5-shamir-2022-cross-catalog`

#### Phase 1 — Shamir 2022 catalog ingest (45-60 min)

- Download + cache catalog at `data/shamir_2022/` with README + MD5 + gitignore allowlist (mirror Pantheon+ / SDSS DR17 / Walmsley pattern)
- LFS-route any file >5MB
- Document Q-cuts methodology in prereg
- Verify chirality convention matches GZ1's (looking down spin axis from above = clockwise / counter-clockwise) — Shamir's Ganalyzer should be conventionally aligned; verify explicitly. If chirality convention is OPPOSITE: STOP and report — Outcome E.

#### Phase 2 — Pre-registration (30 min)

Write `research/2026-05-NN_c5-shamir-2022-cross-catalog-prereg.md` mirroring SDSS DR17 prereg structure.

#### Phase 3 — Driver + live-fire (60-90 min)

Write `src/scripts/vol_3_macroscopic/c5_shamir_2022_spin_orientation.py` adapting the SDSS DR17 driver. Reuse:
- Longo 2011 cos γ axial-dipole estimator with two-stage HEALPix grid
- Hessian-MC + block-bootstrap uncertainty propagation
- Randomization-null with 10000 randoms
- `ave-driver-script-honesty` four-discriminator check

Run end-to-end. Output JSON + diagnostic plots.

#### Phase 4 — Result doc + matrix updates (30-45 min)

Write `research/2026-05-NN_c5-shamir-2022-cross-catalog-result.md`.

Cross-catalog comparison: SDSS DR17 (l=129°, b=79°) σ=6.83° **vs** Shamir 2022 (l=?°, b=?°) σ=?° — pair-separation + significance.

Update matrix:
- `divergence-test-substrate-map.md` C5 row(s) — add Shamir 2022 sub-finding
- `closure-roadmap.md` — new entry

#### Phase 5 — Audit + push (15 min)

Self-audit per the four-discriminator check + `ave-discrimination-check` IF outcome A (catalog-agree). Push branch. Do NOT merge.

## Outcome adjudication table

| Outcome | Criterion | Interpretation |
|---|---|---|
| **A (CATALOG-AGREE)** | Shamir 2022 spin axis within 1σ of SDSS DR17 (l=129°, b=79°) | Robust to catalog/methodology/imaging; operator-output framing strengthened; cascade interpretation methodology-independent |
| **C (CATALOG-DISAGREE)** | Shamir 2022 >2σ from SDSS DR17 | Methodology systematic dominates; both results need caveating; SDSS DR17 conclusion deferred pending resolution |
| **D (CATALOG-MARGINAL)** | 1-2σ separation between catalogs | Systematic at ~σ level; both valid with explicit methodology-uncertainty acknowledged |
| **E (CATALOG-METHODOLOGY)** | Catalogs incomparable (chirality convention mismatch, or other structural issue) | Escalate to orchestration BEFORE retry |

## Skill discipline

- `ave-prereg` upfront — corpus-grep across all 10 AVE-staging repos
- `ave-canonical-leaf-pull` v1.2 — trigger 1-13 for data-fitting class; trigger 16 if any framework structure proposed (none expected — this is catalog-application at existing scale)
- `ave-canonical-source` — constants imports
- `verify-before-cite` v1.3 — all citations
- `ave-driver-script-honesty` — forward-prediction not fit-to-target
- `ave-discrimination-check` — IF outcome A
- `consistency-vs-emergence` v1.1 — Class E for LSS spin direction (operator-output projection)

## Return format

- Branch + tip commit
- Per-phase commit hashes + summaries
- Outcome verdict: A / C / D / E
- σ_Shamir achieved
- Shamir 2022 best-fit axis + comparison to SDSS DR17
- CMB-Shamir separation + significance
- Cascade implications
- ave-auditor verdict (self-audit acceptable)
- Any anomalies surfaced
- Confirmation of push + no merge

## Constraints

- Do NOT modify `_orchestration/*.md` files
- Do NOT merge the branch
- If Outcome E (methodology surface): STOP and report
- If chirality-convention mismatch surfaced at Phase 1: STOP and report
- Forward-prediction discipline: estimate Shamir 2022 direction INDEPENDENTLY; only compare to SDSS DR17 / CMB axis post-fit

## Cross-references

- SDSS DR17 epic (template): `_orchestration/_archive/c5-sdss-dr17-spin-orientation.md`
- GZ DECaLS Outcome-E scoping (identifies Shamir 2022 retarget): `research/2026-05-19_c5-gz-decals-spin-orientation-scoping.md` §5
- omega-freeze cascade Observable 3: `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:52`
- C5 matrix rows: `manuscript/ave-kb/common/divergence-test-substrate-map.md` lines 428/514/554/907
