# H_∞ Downstream Cascade Epic

**Status**: ACTIVE — implementor kickoff pending
**Last updated**: 2026-05-19 EOD
**Originating session**: Orchestration session post-h-infinity-framing-forward merge + Grant adjudication on Thread 3

## Why this exists

The h-infinity-framing-forward implementor session surfaced 5 corpus anomalies that are downstream consequences of the H_∞ "First principles" → "Geometric consistency" walk-back but were out of scope for that epic. These now need their own implementor session. The trigger is structural: the H_∞ reclassification changes the framing-status of every downstream observable that takes H_∞ as input — Thread 3 is the propagation work.

In parallel, the 2026-05-19 EOD canonization of `consistency-vs-emergence` Class E (operating-point projection / topological equilibrium observable) at v1.1 means the H_∞ work that just landed under Class C is now mis-classified. The Class C → Class E reclassification is the second deliverable of this epic.

## Scope (per Grant adjudication 2026-05-19 EOD)

5 corpus anomalies surfaced + 1 skill-driven reclassification pass = 6 sub-deliverables.

### Anomaly 1 — `cosmological-constant-closure.md:97` internal inconsistency

`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:97` retains "Tier-A prediction P23 at 0.7% off TRGB" framing. Post-walk-back, P23's `predictions.yaml` type is `consistency_check` (or Class E pending reclassification). This needs the line-97 prose updated to match P23's actual classification.

### Anomaly 2 — `ch05-dark-sector/index.md:5` MOND a_0 framing

`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/index.md:5` describes MOND $a_0 = cH_\infty/(2\pi)$ as "derived from first principles." MOND $a_0$ is downstream of H_∞ via the Hoop-stress 2π motif; if H_∞ is Class E (operating-point projection), then $a_0$ is also Class E (same operating-point projection, just multiplied by $c/(2\pi)$). Reframe to match.

### Anomaly 3 — `vol_3_macroscopic/chapters/05_cosmology_dark_sector.tex:239` LaTeX mirror

`manuscript/vol_3_macroscopic/chapters/05_cosmology_dark_sector.tex:239` carries the same MOND $a_0$ "derived directly from first principles" framing as Anomaly 2 — LaTeX mirror of the KB. Apply same reframe.

### Anomaly 4 — `omega-freeze-cosmic-grain-cascade.md:7` Tier-1 framing

`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:7` uses "Tier-1 framework synthesis" framing for $\alpha + G + \mathcal{J}_{\text{cosmic}}$ — broader scope than H_∞-specific. With Class E canonized, this is the CANONICAL Class E example (the leaf that defines the three-route framework at u_0* ≈ 0.187). The framing here needs to update from "Tier-1 framework synthesis" to "Class E operating-point projection at $u_0^*$" with explicit cross-reference to the `consistency-vs-emergence` skill v1.1.

### Anomaly 5 — Engine `src/ave/core/constants.py:432` literal circularity

`src/ave/core/constants.py:432`: `XI_MACHIAN = HBAR * C_0 / (7.0 * G * M_E**2)` — the engine literally inverts the closed-form to compute $\xi$ from $G$. This is ACCURATE to the framework state (G is CODATA-input; $\xi$ is computed from it; then $\xi$ used downstream). NOT a bug; not a correctness fix. But the engine comment + variable docstring should be more explicit about:
- The circularity is intentional and reflects Class E joint-constraint structure
- The "Outstanding Rigour Gap" at `mathematical-closure.md:141` (independent G derivation) is the open path to making this non-circular
- Cross-reference to `consistency-vs-emergence` Class E for full context

Two-line annotation at most; not a code change.

### Anomaly 6 — H_∞ Class C → Class E reclassification pass

The h-infinity-framing-forward epic classified H_∞ as Class C consistency check per the v1.0 `consistency-vs-emergence` skill. With v1.1 canonizing Class E (operating-point projection), the just-landed walk-back is mis-classified. Files needing Class C → Class E update:

- `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md` (prose framing)
- `manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex` (LaTeX mirror)
- `manuscript/predictions.yaml` entry P23 (`type: consistency_check` → `type: operating_point_projection` or similar — verify schema)
- `manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/hubble-tension.md` (KB)
- `manuscript/vol_2_subatomic/chapters/10_open_problems.tex` (LaTeX mirror)
- `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md` (KB)
- `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex` (LaTeX mirror)
- `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` (KB)
- `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex` (LaTeX mirror)
- `manuscript/ave-kb/common/full-derivation-chain.md` (Layer 8)
- `manuscript/backmatter/02_full_derivation_chain.tex` (LaTeX mirror)
- `manuscript/frontmatter/00_foreword.tex` (Common Foreword UV-Completion section)
- `manuscript/ave-kb/common/closure-roadmap.md` entry (annotate the framing-forward entry with the Class E refinement)

For each: the Class C "consistency check" framing should be EXTENDED (not replaced) with the Class E joint-constraint framing. Class C is true (G is CODATA-input → SI substitution recovers H_∞); Class E is ALSO true and STRONGER (the joint constraint on {G, H_∞, Ω_freeze, α} via u_0* is the framework's real testable content). The honest framing is "Class E operating-point projection (which includes Class C consistency-check sub-structure)."

## Resolved decisions (Grant adjudication 2026-05-19 EOD)

| # | Decision | Resolution |
|---|---|---|
| G1 | Address the 5 surfaced anomalies? | **YES** — all 5 in scope |
| G2 | Address H_∞ Class C → Class E reclassification? | **YES** — Class E was canonized 2026-05-19 EOD; the just-landed Class C framing is mis-classified |
| G3 | Engine annotation only, or actual code change? | **Annotation only** — engine behavior is accurate to framework state; circularity is intentional per Class E structure |
| G4 | Scope: single implementor session or split into hygiene-pass batch? | **Single session** — anomalies are structurally coupled (all downstream of H_∞ Class E reclassification) |

## Branch + commit

- Branch: `analysis/h-infinity-downstream-cascade` from `analysis/integration` HEAD (at session start — verify in Phase 0; currently post-merge sequence ~c587573 or later)
- Push: yes (at end of Phase 4)
- Merge: NO — orchestration session handles merge after audit

## Phase plan

### Phase 0 — verification (15 min)

- Verify all 5 anomaly file:line citations resolve at HEAD (`verify-before-cite` v1.3)
- Verify `consistency-vs-emergence` v1.1 (Class E canonized) is at HEAD on the skills repo via `git -C ~/.claude/skills log -1 consistency-vs-emergence/SKILL.md`
- Read v1.1 skill body — specifically the "When Class C vs Class E?" discriminator + the H_∞ in-session-validation example
- Create branch `analysis/h-infinity-downstream-cascade`

### Phase 1 — 5 surfaced anomalies (60-90 min)

Apply `ave-walk-back` skill discipline. Per-anomaly:

1. `cosmological-constant-closure.md:97` — update "Tier-A prediction P23" framing
2. `ch05-dark-sector/index.md:5` + `vol_3_macroscopic/chapters/05_cosmology_dark_sector.tex:239` — MOND $a_0$ Class E framing (paired KB+LaTeX update)
3. `omega-freeze-cosmic-grain-cascade.md:7` — "Tier-1 framework synthesis" → "Class E operating-point projection at $u_0^*$" framing
4. `constants.py:432` — two-line engine annotation explaining intentional circularity + Class E + open-gap reference

Single commit per `ave-walk-back` batch pattern: `kb+engine(downstream-cascade): apply Class E framing to MOND a_0 + cosmological-constant + omega-freeze + engine annotation`

### Phase 2 — H_∞ Class C → Class E reclassification (90-120 min)

Apply `ave-walk-back` to the 13 files from the h-infinity-framing-forward epic + any cascade-grep additions. Use the v1.1 skill's "Class E asymmetry note" + "Honest framing in output" Class E example as the template language.

Key framing template (from skill v1.1 honest-framing section):

> *"H_∞ = 28π m_e³cG/(ℏ²α²) ≈ 69.32 km/s/Mpc: Class E operating-point projection of u_0* ≈ 0.187 at cosmic genesis; joint-constrained with G, Ω_freeze, α via the R_H/ℓ_node ~ 10³⁹ topological bridge per omega-freeze-cosmic-grain-cascade.md:13-16. 0.7% TRGB match is structural consistency, not independent prediction; falsification of any one of {G, H_∞, Ω_freeze, α} from observation kills the operating-point and therefore the entire substrate model."*

Apply this template (adapted to local context) across the 13 files. Per `ave-walk-back` discipline: single commit.

### Phase 3 — Class E candidate corpus sweep (30-45 min)

Per v1.1 skill body, other Class E candidates exist in corpus:
- $M / Q / J$ at $\Gamma = -1$ boundaries (per `boundary-observables-m-q-j.md`)
- 8 projections of Ω_freeze (per `omega-freeze-cosmic-grain-cascade.md:46-58`)
- Hoop-stress $a_0 / v_{\text{substrate}}$ cross-scale motif (per `mond-hoop-stress.md`)
- Possibly other three-route framework patterns

Sweep these for: (a) are they currently classified as Class C/B/A/D? (b) should they be Class E? (c) what's the reclassification scope per candidate?

Deliverable: research doc at `research/2026-05-NN_class-e-candidate-corpus-sweep.md` listing each candidate + current class + recommended class + cascade-implication scope. NO actual reclassification in this phase — just inventory. Reclassification of these candidates is queued for future epic(s) post-Grant adjudication.

### Phase 4 — Audit + push (15 min)

- Run `ave-auditor` review on the branch with prompt: audit branch `analysis/h-infinity-downstream-cascade` against `analysis/integration` for: (a) Phase 1 + Phase 2 walk-back completeness, (b) Class E framing template applied consistently across H_∞ references, (c) engine annotation accurately captures Class E + open-gap reference, (d) Phase 3 inventory completeness (cross-check against `boundary-observables-m-q-j.md`, `omega-freeze-cosmic-grain-cascade.md` 8-observable table, `mond-hoop-stress.md`).
- Address findings before push
- Push branch `analysis/h-infinity-downstream-cascade`
- Do NOT merge — orchestration handles

## Skill discipline

- `verify-before-cite` v1.3 — Required throughout (triggers 7c + 8 for cross-branch + commit-application checks)
- `consistency-vs-emergence` v1.1 — REQUIRED — this epic IS the v1.1 retroactive application per `ave-newly-created-skill-self-audit`
- `ave-walk-back` — REQUIRED for Phase 1 + Phase 2 multi-file propagation
- `ave-newly-created-skill-self-audit` — TRIGGERED for v1.1; this epic IS the retroactive application
- Pure-AVE-corpus rule
- INVARIANTS N1/N2 per file location

## Expected return summary

- Branch + tip commit
- Per-phase commit hashes + summaries
- Phase 1 anomaly walk-back status (5/5 completed)
- Phase 2 Class E reclassification scope (13 files + cascade-grep additions)
- Phase 3 Class E candidate inventory deliverable (research doc path + 1-paragraph summary)
- ave-auditor verdict
- Any new anomalies surfaced

## Cross-references

- Origin epic: [`h-infinity-framing-forward.md`](h-infinity-framing-forward.md) (CLOSED post-merge; this epic is the downstream-cascade follow-up)
- Origin skill canonization: `~/.claude/skills/consistency-vs-emergence/SKILL.md` v1.1 (Grant canonized 2026-05-19 EOD)
- Origin audit: [`research/2026-05-19_h-infinity-derivation-audit.md`](../research/2026-05-19_h-infinity-derivation-audit.md) (Class C verdict; would be Class E under v1.1)
- Pantheon+ epic that referenced the K4-rest-frame ↔ Ω_freeze distinction: [`section-e-cascade.md`](section-e-cascade.md) Phase E1b-prime (closed via merge `c587573`)
