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

---

## Category I — the signed-Γ print sweep (NEW REGISTER ROW). Site count: **31**, and the tail is tagged, not truncated

**Method, two-method as required.** (1) `grep -rn` with quoted patterns over
`--include='*.tex' manuscript/`; (2) an independent Python `pathlib.rglob('*.tex')` +
`re` pass over the same tree with a widened pattern
(`Gamma_\{?\\?(?:text|mathrm)?\{?bulk`). Method 1 with the narrow literal returned 13 sites in
7 files; **method 2 returned 31 sites in 16 files** — the delta is the
`\Gamma_{\mathrm{bulk}}` / `\Gamma_{\text{bulk}}` render variants and the standalone TikZ figure
sources, which the narrow literal missed. **The 31 is the number of record**, and this is a live
instance of the grep-completeness failure mode: a single-form grep under-reports by more than
half.

**Full register (file → lines):**

| File | Lines |
|---|---|
| `vol_1…/04_continuum_electrodynamics.tex` | 105 |
| `vol_3…/04_generative_cosmology.tex` | 173 (section heading) |
| `vol_3…/08_gravitational_waves.tex` | 284, 287, 292 |
| `vol_3…/15_black_hole_orbital_resonance.tex` | 45, 57, **68 ★**, 77 |
| `vol_3…/21_black_hole_interior_regime_iv.tex` | 119, 128, 167, **195 ★** |
| `vol_9…/01_general_description.tex` | 45 |
| `vol_9…/03_pin_port_configuration.tex` | 13, 225 |
| `vol_9…/03a_device_circuit_models.tex` | **77 ★ (declaration home)** |
| `vol_9…/04_dc_electrical_characteristics.tex` | 117, 120 |
| `vol_9…/05_ac_electrical_characteristics.tex` | 121 |
| `vol_9…/09_mechanical_characteristics.tex` | 104 |
| `vol_9…/13_application_examples.tex` | 39, 180 |
| `vol_9…/17_engine_requirements.tex` | 61, 106, 121 |
| `vol_9…/figures/circuit_electron_barrier.tex` | 13, 17, 36 |
| `vol_9…/figures/circuit_three_channel_boundary.tex` | 21 |
| `vol_9…/figures/node_2domain_nport.tex` | 45 |

**What this wave tagged, and why not all 31.** Thirty-one inline copies of a four-clause
declaration would be a duplication defect of exactly the kind R7 exists to prevent, across both
xr-hyper bases. Instead:

- **One canonical print declaration** at `vol_9…/03a_device_circuit_models.tex`
  §"Graded Vacuum Impedance Network" — the print home of the three-channel Γ table that the vol9
  ch09 / ch13 sites already cite as canonical. It carries all three declarations (reference plane
  / projection / profile) verbatim in substance from `wall-taxonomy.md` §9, plus the
  computed-not-chosen rule and the `|Γ| = 1`-only Axiom-3 fence.
- **Two DERIVATION sites tagged in place** (marked ★ above) — the two places in print where the
  signed bulk Γ is *derived* rather than quoted: `ch15:68` (`c_bulk → 0 ⇒ Z_bulk → 0 ⇒ Γ_bulk = −1`)
  and `ch21:195` (the same step in the BH-interior chapter). These are where the profile
  conditionality actually bites, because they multiply a vanishing speed by a constant density.
- **The remaining 27 sites are QUOTING sites** — tables, summary rows, figure labels and
  cross-references that restate a Γ derived elsewhere. **They are tagged in this register and
  explicitly not edited**, so the count is auditable rather than silently truncated.

**Not adjudicated here:** whether the 27 quoting sites should each carry a pointer, or whether the
one declaration home plus the two derivation tags is the right print economy. Surfaced for the
orchestrator.

---

## CITE-SHIFT SWEEP — run AFTER content settled, two-method, 123 cites classified

**Method 1** — enumerate every `file:NNN` cite anywhere in the repo whose target basename is one
of this wave's 16 touched files. **123 cites** into 10 targets.
**Method 2** — per-cite *content* diff rather than a line count: for each cite, compare the line
at `NNN` on `origin/main` against `HEAD`, and classify `STABLE` / `SHIFTED → :M` (base content
found elsewhere in the file) / `REWRITTEN` (base content gone from the file).

| class | count |
|---|---|
| `STABLE` (cite unaffected) | **90** |
| `SHIFTED` (base content moved) | **11** |
| `REWRITTEN` (base content is what this wave replaced) | **22** |

**Mechanical repairs performed: ZERO — and that is the correct outcome, not an omission.** Every
non-`STABLE` cite falls into one of three classes, none of which licenses a renumber:

1. **The wave's own rewrite targets, cited from the frozen sweep record** (18 of the 22
   `REWRITTEN`): `2026-08-02_manuscript-reconciliation-board.md` §5's per-finding entries at
   ch15 `:23/:27/:271/:290/:292/:337/:354/:387`, `backmatter/07:{85,145,211,213}`,
   `vol9 ch03:205`, plus four docket fragments at ch15 `:322`. **§5 is the frozen output of the
   154-finding sweep** — it records what was found, at the state it was found. Renumbering it
   would rewrite the record of the audit this wave discharges. Recorded here instead.
2. **Dated / frozen documents** (all 11 `SHIFTED` bar two, plus the rest): the 2026-06-17
   **frozen prereg** (its cite into `existing-experimental-signatures.md:48` now resolves at
   `:55`), `research/2026-07-17_regime-iv-dissipation-audit_items.json` (a frozen audit artifact;
   ch15 `:392 → :411`), `research/2026-06-06_doc-reconciles-result.md`,
   `_orchestration/_archive/cosmic-axis-glossary.md`, and the ch08 board/docket cites
   (`:250 → :257`, `:355 → :362`, `:364 → :371`, all +7 from this wave's figure environment).
   **Frozen text gets a dated surface-note, never a rewrite** — which is exactly what
   `research/2026-08-05_bh-shear-echo-prereg_surface-note.md` is.
3. **★ BASELINE-STALE — recorded, deliberately NOT renumbered, and this one is a real finding.**
   Two LIVE KB leaves — `manuscript/ave-kb/claim-quality-closure-roadmap.md:115` and
   `manuscript/ave-kb/common/divergence-test-substrate-map.md:211` — cite
   `04_generative_cosmology.tex:467` for the Planck CMB-axis *"(174°, −5°)"* reference. This
   wave shifted that line to `:468`, and the naive repair is to write `:468`. **It would be
   wrong.** `grep -n '174' manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex`
   returns **nothing** — that string is not in the file **at any line**, at base or at HEAD. The
   cite was already pointing at unrelated content (`:467` is the *"A-034 is the recognition that
   they describe ONE mechanism"* sentence) **before this wave touched anything**. Renumbering it
   to `:468` would re-endorse a wrong cite under a fresh date and make it look freshly verified.
   **Sharper still:** the roadmap site labels itself *"★cite-rot repair 2026-08-02"* and says it
   *"read `:153,160,949`, all three wrong-target from the day they were written"* — so `:467` is
   a **repair that landed on a third wrong target**, and a mechanical `+1` here would have been
   the fourth. **Surfaced, not fixed.**

Also recorded, no action needed: `manuscript/backmatter/12_mathematical_closure.tex:197`
(a `%`-comment) cites `07_universal_saturation_kernel.tex:145`. That line's *content* changed
(seam disclosed → seam resolved) but its *position* did not — `backmatter/07` is line-count-neutral
under this wave — so the cite still lands on the paragraph it names.

---

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
