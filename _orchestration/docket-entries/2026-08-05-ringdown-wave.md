# The ringdown wave — execution record (2026-08-05, ONE PRINT-TOUCH)

Lane: documentation / manuscript-reconciliation implementer. Branch `docs/ringdown-wave-0805`
off `origin/main` @ `773fe007`. Fires the whole staged ringdown set as a single print touch per
the one-print-touch rule (`_orchestration/docket-entries/2026-08-04-rulings-ringdown-wave-batch.md`
item 6).

**Governing artifacts, read at execution time (pointers, not values):**

- `_orchestration/2026-08-04_doc-lane-reconciliation-handoff.md` — R7 (rendered current-status
  notes stay; verbatim prior-wording `%` duplication drops), R11 (the `07` seam fires here).
- `_orchestration/docket-entries/2026-08-04-rulings-ringdown-wave-batch.md` — the ten-item
  ruling record.
- `_orchestration/2026-08-02_manuscript-reconciliation-board.md` §3 cribs / §4 gating register /
  §5 per-finding dispositions / §6 close-out.
- `research/2026-08-03_coldq-pole-v2.4-root_result.md` + its frozen prereg — the coldQ authority.
- `research/2026-08-04_coldq-axial-rhob_result.md` — the FORK-3(b) AXIAL run (see the staleness
  flag below).
- `research/2026-08-04_echo-delay-regulated-sum_result.md` — the current timing authority.
- `manuscript/ave-kb/common/wall-taxonomy.md` §9 (sign-relativity ruling) — the signed-Γ
  declaration frame.

---

## ★ STALENESS FLAG, SURFACED NOT SILENTLY RESOLVED — the FORK-3(b) axial clause

The staging brief for this wave specifies a three-clause coldQ status note whose second clause
reads that **FORK-3(b) is owed an axial run** (its polar run having adjudicated nothing).

**That clause was true when the wave was staged and is no longer true at execution time.** PR
**#876** (`research/coldq-axial-rhob`) merged into `main` at `773fe007` on 2026-08-05, i.e.
between the staging and this branch's base. It IS the FORK-3(b) axial run. Its verdict, verbatim
from `research/2026-08-04_coldq-axial-rhob_result.md:21`:

> **Certification: `ROOT-NOT-CERTIFIED` on every configuration that has a root.** Not one gate
> failed on the RHO-B primary. **Three self-tests failed to FIRE** — `FT-2`, `FT-2c` and `FT-W` —
> each because **this lane sized its firing threshold wrong at freeze** … **The thresholds are
> NOT retuned. No physics bin is adjudicated.**

**What this changes and what it does not.** The clause's *intent* — that FORK-3(b) is not
settled, so the v2.4 misses may not be read as a falsification of the profile — is **unchanged
and if anything strengthened**: the axial run exists, and it adjudicated no physics bin. What
changes is that printing "owed an axial run" would ship a statement the corpus contradicts as of
this branch's base. **The status notes in this wave therefore say what is true at HEAD:
FORK-3(b)'s axial run has landed `ROOT-NOT-CERTIFIED` with no bin adjudicated, so the fork
remains open.** No number from that lane is printed anywhere — every one of its `ω_R M_g` / `Q`
figures is a NOT-ADJUDICATED diagnostic by its own freeze and must not be carried into print.

Flagged for the orchestrator rather than resolved in-lane: whether the ruling's three-clause
content should be formally re-issued against the post-#876 state, or whether this lane's
truth-at-HEAD rendering discharges it.

---

## Scope register — what this wave carries

| # | Category | Sites | Status |
|---|---|---|---|
| A | coldQ-class status notes (R7 current-status form) | ch15 `18/49` + cold-`Q=ℓ`; `backmatter/07` | this wave |
| B | toroidal-vs-fundamental carve, verbatim from the v2.4 scope section | every ringdown site touched | this wave |
| C | B1-class per-occurrence rewrites (~80% of the work) | ch15 ×4 + −0.45/−0.47 + 10–18% + near-extremal + Q=ℓ spin-scope | this wave |
| D | self-obsoleting interim notes | ch15 `:31` blanket; `backmatter/07` seam disclosure | same commits as the work |
| E | the `07` seam (R11) | `backmatter/07` withdrawal vs the sites still printing the withdrawn claim | this wave |
| F | FLAG-ECO conditional tags | dated surface-note beside the FROZEN 2026-06-17 prereg; KB scope caveat | this wave |
| G | memory-rescope Variant B (latch-null scope) | ch15 GW-memory subsection + companions | this wave |
| H | `hulse_taylor` regenerate + place | generator + vol3 ch08 | this wave |
| I | signed-Γ print sweep (new register row) | print `.tex` corpus | this wave |
| J | out-of-set register extension (KEEP-BOTH, ruled in) | `common/translation_gravity.tex`; vol3 `04:375` | this wave |
| K | `wall-taxonomy.md` currency + anchor-checker stale pins | KB + `tools/archival` | this wave |
| L | the `bh_untapped_predictions.png` raster | vol_2 asset path, used by vol_3 | this wave |
| — | vol9 `03_pin_port_configuration.tex` held bullet | the `linewidth ∝ 1/ℓ` bullet | this wave |

## Verified ALREADY-DONE — not re-fired (double-reconcile guard)

Each re-verified by content at this branch's base before being skipped:

| Site | Where the discharge lives at HEAD | PR |
|---|---|---|
| `vol_9…/07_saturation_characteristics.tex` "Tightest validations" | the cold `a_* = 0` single-point anchor clause + the Rule-12 retraction note below it | #842 |
| `vol_9…/03_pin_port_configuration.tex` Γ = −1 row | the inline spin-scope parenthetical on the BH-ringdown fire | #842 |
| `vol_1…/04_continuum_electrodynamics.tex` | the "Ring-down scope (2026-08-02, per Ruling B1…)" block | #836 |
| `vol_1…/07_regime_map.tex` | the "Ruling B1, 2026-07-21; the spinning-remnant / LIGO-catalog comparison is …" clause | #820/#836 |
| `vol_5…/02_organic_circuitry.tex` | the "Ring-down scope (2026-08-02, per Ruling B1…)" block | #846 |
| `vol_3…/04_generative_cosmology.tex` list header + list item | the "Ring-down scope (2026-08-02…)" block covering the itemize | #848 |

## EXPLICITLY EXCLUDED, byte-untouched

- `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex` — the sentence
  *"Gravitational waves propagate **exclusively** as lossless, trace-free, transverse impedance
  modulations of the macroscopic LC vacuum lattice."* This is **route-to-core** (the Q1 / bulk
  admixture fork), NOT gated-ringdown; the board's own §5 verify note says so. Editing it would
  silently adjudicate a live physics fork. **Left byte-untouched by this wave.** The only ch08
  bytes this wave adds are the Hulse-Taylor figure placement (category H), which is in a
  different section and touches no channel-attribution prose.
- `manuscript/predictions.yaml` — handled by the concurrent lane on branch
  `docs/predictions-ruled-batch-0805`. Collision checked before start; **not touched here**.
