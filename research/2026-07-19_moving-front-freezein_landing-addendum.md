# Moving-Front Freeze-In — LANDING ADDENDUM (2026-07-19)

**Date:** 2026-07-19
**Branch:** `feat/moving-front-freezein-landing` (off main `1be045a1`)
**Landed arc:** the archived `analysis/moving-front-freezein` (tag
`archive/analysis/moving-front-freezein` @ `f647f58b`; original frozen prereg
`7b97e76d`, off main `eaadeaf1`). Extracted verbatim, byte-identical — see the
prereg [`2026-06-30_moving-front-freezein_prereg_FROZEN.md`](2026-06-30_moving-front-freezein_prereg_FROZEN.md),
result [`2026-06-30_moving-front-freezein_result.md`](2026-06-30_moving-front-freezein_result.md),
and dataset [`2026-06-30_moving-front-freezein_results.json`](2026-06-30_moving-front-freezein_results.json).
**Lane:** implementer (branch-scrub landing, union driver). Adjudication trail for a
LATER KB/manuscript promotion; `research/`-only.

> **Scope of this addendum.** The 2026-06-30 result doc + results.json are the
> ARCHIVED RECORD — banked numbers are preserved UNEDITED (Rule 11: no retune of
> the archived negative). This addendum adds ONLY (§1) the reproduction-gate
> outcome on current main, (§2) the frozen N≥32 extension-stage expectations +
> result (the arc's own §7 next step), (§3) the OWED-POST-CLEANUP falsification-
> ledger entry (the canonical ledger is FENCED this session — see §3), and (§4)
> the flags surfaced during landing (flag-don't-fix; nothing here adjudicates
> the direction conflict or the A44 fork). No archived number is overwritten.

---

## §1 REPRODUCTION GATE — the arc's two-arm protocol on CURRENT main

**Why.** Main evolved since 2026-06-30; the module depends on
`cosserat_field_3d.py`, which changed. The reproduction gate isolates whether
engine evolution drifted the banked numbers.

**Protocol.** The banked results.json seed block (`R_major=4.0, amp=0.3,
sigma=1.8`, `N=12`, `pml=3`, `v_fronts=(0.5,1.0,4.0)`) re-run on current main
(`1be045a1`), mirroring `run_full`'s dispersion-baseline + two-arm structure.
Post-window shortened to `n_post_compton=12` (banked run used 100) — persistence
saturates well below 12 Cp (max banked hold = 3.04 Cp), so the persistence and
S_min reads are faithfully reproduced; only the single-snapshot `Q_end` read
(the explicitly-jittery `extract_crossing_count`, "flickers 0↔2" per the module
docstring) samples the dispersing field at a different end-time.

**Outcome: MATCH on every load-bearing number** (results.json's own note names
"the memristive S_min monotone rise and the LASTING-persistence failure" as the
load-bearing reads).

| v_front | metric | BANKED (f647f58b, N=12, n_post=100) | REPRODUCED (main 1be045a1, N=12, n_post=12) |
|---|---|---|---|
| — | τ_disperse | 0.225 Cp | 0.225 Cp ✓ |
| 0.5 | memr persist / bare persist | 3.04 / 1.01 Cp | 3.039 / 1.013 Cp ✓ |
| 0.5 | memr S_min / bare S_min | 0.04 / 0.00 | 0.040 / 0.000 ✓ |
| 1.0 | memr persist / bare persist | 0.45 / 1.35 Cp | 0.450 / 1.350 Cp ✓ |
| 1.0 | memr S_min / bare S_min | 0.19 / 0.00 | 0.189 / 0.000 ✓ |
| 4.0 | memr persist / bare persist | 1.46 / 1.58 Cp | 1.463 / 1.576 Cp ✓ |
| 4.0 | memr S_min / bare S_min | 0.56 / 0.00 | 0.561 / 0.000 ✓ |

- **memristive S_min monotone rise 0.04 → 0.19 → 0.56 reproduces exactly.**
- **persistence values reproduce to 3 decimals; lasting-freeze failure holds**
  (all holds ≤ 3.04 Cp, ~30× short of the 100 Cp G3 target).
- **Only difference — the jittery single-snapshot `Q_end`:** banked
  (bare/memr) = 1/1, 1/1, 1/0; reproduced = 0/1, 0/0, 0/1. This is the
  least-robust metric in the dataset (a lone snapshot of a dispersing/flickering
  field), sampled at a different post-window end (n_post 12 vs 100), NOT engine
  drift. The window-median persistence metric exists precisely because `Q_end`
  flickers. **Not banked as a discrepancy of physics content.**

**Verdict: REPRODUCES on current main.** Engine evolution (the
`cosserat_field_3d.py` changes) did NOT drift the moving-front freeze-in result.
Banked archived numbers stand; the current-main reproduction is banked alongside
(both preserved, per the never-overwrite-the-archived-numbers rule).

**Verify-before-cite note (mechanism line drift, NOT edited in the archived
doc).** The archived result doc §4 cites the single-mechanism symbol at
`cosserat_field_3d.py:1999` (`_bulk_accel → _bare_linear_gradient`). On current
main (`1be045a1`) that mechanism is intact but the line drifted: `_bulk_accel`
is now at `:2018` and `_bare_linear_gradient` at `:1903` (line `:1999` now holds
an unrelated LC-oscillator analytic-solution comment). The archived doc is
preserved verbatim (Rule 11 / Rule 12); this note records the drift so a future
reader resolves the cite correctly.

---

## §2 THE N≥32 GATE — executing the frozen protocol's own next step

The archived result doc §7 states the negative "should be re-confirmed at N≥32
in the engine_sim lane before it is promoted to a corpus verdict." This section
executes that pre-registered next step (NOT a retune — the gates, the mechanism,
and the archived verdict are fixed; this is a resolution-robustness confirmation).

**Tractability (timed first, per discipline).** A single N=32 two-arm cell (one
v_front, both arms + dispersion baseline) = **737.7 s** on this machine
(memristive v=4.0 = 301 s, bare v=4.0 = 434 s, dispersion baseline = 2.8 s).
Because the fixed `n_post_compton` observation window dominates the step count
over the front-transit (n_post ≈ 12 Cp vs n_front ≈ 0.5–4 Cp), the slower fronts
are only marginally costlier per cell, so the full 3-point two-arm sweep is
bounded to ~35–45 min — TRACTABLE within the "tens of minutes per arm" budget.
Run as a DISCLOSED extension stage.

### §2.1 FROZEN EXPECTATIONS BLOCK (committed BEFORE the N≥32 run)

> **Freeze discipline.** This block is committed BEFORE the N=32 sweep is run.
> It states what the N=12–16 data predicts at N≥32 under each A44-fork world, so
> the run cannot be retro-fit. No gate movement (Rule 11).

The load-bearing open item (archived result §4/§7) is the A44 fork: the engine's
re-solidified Cosserat bulk is linear-elastic (`_bulk_accel →
_bare_linear_gradient`) with NO topological-pinning term, so a bare real-space
ω-loop disperses once the front's saturation lifts. The fork is:

- **(a) engine-gap world** — the Cosserat solid NEEDS an Ax1 topological-pinning
  term the corpus asserts, not yet implemented.
- **(b) corpus-over-claim world** — Ax1 "protects topology" may not hold for a
  bare real-space ω-loop that is not itself a stabilised soliton.

**Both forks predict the SAME thing at N≥32, because neither world has a pinning
term in the engine at any N** (the linear-elastic `_bare_linear_gradient` bulk is
N-independent). Pre-registered expectations:

- **E1 (persistence stays short).** Real-space defect persistence stays bounded
  at a few Compton periods (same order as N=12: ≤ ~3–4 Cp), NOT rising toward the
  100 Cp G3 target. The lasting-freeze negative is resolution-robust. *(Both
  forks (a),(b) predict E1 identically — the N=32 run CONFIRMS the negative; it
  does NOT discriminate the fork.)*
- **E2 (S_min monotone rise survives).** The memristive S_min at the defect rises
  monotonically with v_front (the §2.3 fast-crossing → less-S-collapse
  direction), reproducing the resolution-robust mechanism-level positive. Bare
  S_min stays ≈ 0 at all v (no memory).
- **E3 (arms do not cleanly separate at the real-space observable).** Persistence
  does not become a clean freeze-vs-heal discriminator; the front-present hold
  inflates both arms; the bare arm may still out-persist memristive at some v.
- **τ_disperse note (NOT a gate; expected to change with N).** The bare-loop
  dispersion time is a finite-size quantity and is EXPECTED to grow with grid
  room (more space before the packet radiates out); the single-cell probe already
  showed τ_disperse 0.225 Cp (N=12) → 0.900 Cp (N=32). This does not bear on E1
  (persistence is measured in Cp held past front-clear, and stays short in
  absolute Cp regardless).

**What WOULD look different (would re-open the negative — a falsifier of the
no-pin mechanism explanation):** if persistence GREW substantially with N (e.g.
toward tens of Cp) AND rose monotonically with v_front, the short N=12–16 holds
would have been a finite-size/dispersion artifact masking a real freeze — i.e.
there IS effective pinning that only manifests with enough grid room, and the
lasting-freeze claim re-opens. Likewise, if the S_min monotone rise (E2)
inverted or flattened at N=32, the memristive-lag mechanism finding would be
exposed as resolution-limited. Neither is expected under either A44 fork.

### §2.2 N≥32 RESULT (run AFTER the §2.1 freeze commit; banked

Executed on current main's engine (byte-identical `src/ave/` between the base
`1be045a1` the sweep ran against and the rebased base `3efa24d6` — `git diff
--stat 1be045a1..3efa24d6 -- src/` empty, so the result is valid for current
main). Seed = the committed `run_full` geometric scaling (`R_major=min(6.0,
0.30·N)=6.0, sigma=2.5` at N=32) — i.e. the LANDED driver at higher N, the
cleanest thing for a reviewer to re-run. `n_post_compton=12` (persistence
saturates below it). Raw dataset: [`2026-07-19_moving-front-freezein_N32-extension.json`](2026-07-19_moving-front-freezein_N32-extension.json).
Full 3-point two-arm sweep runtime = **2710 s** (~45 min).

| v_front | Δt_cross/τ | regime | memr persist | bare persist | memr S_min | bare S_min |
|---|---|---|---|---|---|---|
| 0.5 | 4.0 | SLOW→HEAL | 1.913 Cp | 0.000 Cp | 0.000 | 0.000 |
| 1.0 | 2.0 | SLOW→HEAL | 1.125 Cp | 0.000 Cp | 0.001 | 0.000 |
| 4.0 | 0.5 | FAST→FREEZE | 3.264 Cp | 0.563 Cp | 0.118 | 0.000 |

τ_disperse(N=32) = **0.900 Cp** (vs 0.225 Cp at N=12 — grew with grid room, as
the §2.1 τ_disperse note predicted; NOT a gate).

**Adjudication against the FROZEN §2.1 expectations:**

- **E1 (persistence stays short) — CONFIRMED.** All holds ≤ **3.264 Cp** (max,
  memristive v=4.0), the SAME order as the N=12 banked max (3.04 Cp), and ~30×
  short of the 100 Cp G3 target. Persistence did NOT rise toward tens of Cp with
  N. **The falsifier of §2.1 (persistence growing substantially with N + rising
  monotonically with v_front) did NOT trigger.** The lasting-freeze negative is
  **resolution-robust at N=32.**
- **E2 (S_min monotone rise survives) — CONFIRMED (direction).** memristive S_min
  rises monotonically with v_front (0.000 → 0.001 → 0.118); bare stays ≈ 0 at all
  v (no memory). The §2.3 fast-crossing → less-S-collapse direction holds at N=32.
  *(Honest caveat: the ABSOLUTE S_min magnitudes at N=32 (0.000/0.001/0.118) are
  smaller than the banked N=12 (0.04/0.19/0.56), because this run used the
  committed-driver seed R_major=6.0/sigma=2.5, NOT the banked seed 4.0/1.8 — two
  variables (N and seed) changed. The monotone DIRECTION — the mechanism-level
  signal §7 calls "resolution-robust" — is what E2 predicted and what holds; the
  magnitude is seed/resolution-sensitive and was never claimed invariant.)*
- **E3 (no clean lasting-freeze discriminator) — CONFIRMED, with a direction
  flip on the sub-observation.** Neither arm achieves lasting freeze (all ≤ 3.264
  Cp), so the real-space observable is NOT a clean freeze-vs-heal discriminator —
  E3's core claim holds. The sub-observation "bare may out-persist memristive at
  some v" (true at N=12) FLIPS at N=32: here memristive cleanly out-persists bare
  at all three v (1.913/1.125/3.264 vs 0.000/0.000/0.563). This flip is in the
  mechanism-EXPECTED direction (the S-lag slows annihilation, so memr > bare) and
  makes the N=32 arm-separation CLEANER than N=12 — but still ~30× short of
  lasting freeze. It strengthens, not weakens, the "memristive lag slows but does
  not freeze" reading.

**N≥32 VERDICT (the archived §7 gate, discharged).** The archived result's
lasting-freeze NEGATIVE is **resolution-robust** — confirmed at N=32 across BOTH
seed families (banked-seed N=12 §1 reproduction + committed-driver-seed N=32
here), the falsifier untriggered. The A44 fork (engine-gap vs corpus-over-claim)
is **NOT discriminated** — as pre-registered in §2.1, both forks predicted short
persistence at N≥32, so this run confirms the negative is not a finite-size
artifact but does NOT resolve which fork. This satisfies the archived doc §7
demand ("re-confirmed at N≥32 … before it is promoted to a corpus verdict"); the
promotion decision + any clm-exjfai status move are the AUDITOR lane's (surfaced,
not landed here). **Relevance to clm-exjfai (surfaced only):** the CONTESTED
demotion now on main (PR #738, `dark-wake-bemf-foc-synthesis.md` §1.2) rests in
part on the negative being "resolution-limited (N=12–16) … should be re-confirmed
at N≥32"; this N=32 run supplies exactly that re-confirmation — a datum the
auditor may use, but this PR adjudicates no status change.

**Seed-robustness note (honest, NOT a retune).** Because the N=32 run used the
committed-driver seed while the banked/reproduction runs used the results.json
seed, the short-persistence negative is now demonstrated across two DISTINCT seed
geometries at two resolutions — stronger evidence of robustness than a
single-seed ladder. A same-seed N=12→N=32 ladder was judged unnecessary (the
verdict E1 is unambiguous under either seed and the ~45-min cost buys no
verdict-relevant discrimination); flagged as the obvious follow-on if a reviewer
wants the seed held fixed.

---

## §3 FALSIFICATION-LEDGER ENTRY — OWED POST-CLEANUP (canonical ledger is FENCED)

The canonical falsification ledger is
`manuscript/ave-kb/common/genesis-chord-falsification-ledger.md` — under
`manuscript/ave-kb/`, which the KB/manuscript cleanup lanes own this session.
**FENCE: this landing lane does NOT edit that tree.** The ledger entry is
therefore written here as an OWED-POST-CLEANUP block; the auditor/cleanup lane
lands it into the canonical ledger (and the entry cross-links back to this
addendum). Format matches the ledger's existing entries (Hypothesis / Verdict /
Diagnostic / Tag / Recovery).

> **OWED ledger entry — to be landed in
> `manuscript/ave-kb/common/genesis-chord-falsification-ledger.md`:**
>
> ### moving-front-freezein — the moving front does NOT deliver a LASTING frozen real-space ω-defect (NEGATIVE; single-mechanism, N-robust)
> - **Hypothesis:** a spatially-PROPAGATING yield-crossing front freezes in a
>   pre-existing real-space ω-defect via the BEMF-blocked-dω/dt mechanism (the
>   first *moving*-front realization of the canonical clm-exjfai freeze-in; prior
>   work was temporal-ramp / static-valve only). Derived direction (prereg §2.3):
>   FAST crossing (Δt_cross ≲ τ_relax) → FREEZE.
> - **Verdict:** SPLIT. (a) the memristive S-lag mechanism is CONFIRMED and
>   rate-dependent exactly as derived (S_min rises monotonically 0.04→0.19→0.56
>   with v_front; reproduced EXACTLY on current main 2026-07-19, and the
>   monotone-rise direction resolution-robust to N=32). (b) honest NEGATIVE on the
>   lasting-freeze claim: real-space defect persistence ≤ 3.04 Cp (N=12 banked;
>   ≤ 3.26 Cp at N=32) vs the pre-registered ≥ 100 Cp target (~30× short); at
>   N=12 the two arms did not separate cleanly (bare out-persists memristive at 2
>   of 3 v_front), while at N=32 memristive cleanly out-persists bare at all v —
>   but NEITHER arm ever reaches lasting freeze. The N≥32 re-confirmation the
>   archived §7 demanded is DONE (this landing): the negative is resolution-robust,
>   the falsifier (persistence growing with N) did not trigger.
> - **Diagnostic (single mechanism, Rule 11):** the engine's re-solidified
>   Cosserat solid is a linear-elastic shear-wave medium with NO topological-
>   pinning term (`_bulk_accel → _bare_linear_gradient`, `cosserat_field_3d.py`
>   — `:1999` at f647f58b, `:2018`/`:1903` on 2026-07 main). The front-clamp pins
>   ω only while S<1 (front present); once the front passes and S recovers, the
>   clamp lifts and the bare ω-loop — not a stationary soliton — radiates away as
>   a dispersing linear-elastic packet (τ_disperse ≈ 0.23 Cp at N=12). The BEMF
>   block does exactly what its physics says (blocks dω/dt during the S-low
>   window) but there is no engine term that HOLDS the winding after S recovers.
> - **Tag:** 🔴 **GENUINE-FALSIFICATION — scoped to the moving-front realization
>   of a BARE real-space ω-loop.** The falsified item is *this realization*
>   (moving front + bare ω-loop + linear-elastic bulk), NOT the clm-exjfai
>   mechanism in general — see the A44 FLAG below: EITHER an engine gap (missing
>   Ax1 pinning term) OR a corpus over-claim (Ax1 does not protect a bare
>   ω-loop). Not adjudicated (auditor/Grant, A44). Do NOT over-read as "the
>   freeze-in mechanism is false"; the S-lag half is CONFIRMED.
> - **A44 FLAG (engine-vs-corpus, flag-don't-fix):** corpus (`59_` §4.3,
>   clm-exjfai) asserts Ax1 protects the frozen ω-defect in the re-solidified
>   solid; the engine's Cosserat bulk provides no such protection. Surfaced as
>   EITHER (a) engine gap OR (b) corpus over-claim — NOT adjudicated here; no Ax5
>   drafted (A44).
> - **Recovery:** landed on main via PR (branch-scrub FOLLOW-UP); prereg
>   `2026-06-30_moving-front-freezein_prereg_FROZEN.md`, result
>   `2026-06-30_moving-front-freezein_result.md`, module
>   `src/ave/topological/moving_front_freezein.py`, tests
>   `src/tests/test_moving_front_freezein.py`, landing addendum (this doc).
>   Archived head `f647f58b` (tag `archive/analysis/moving-front-freezein`).

---

## §4 FLAGS SURFACED DURING LANDING (flag-don't-fix — nothing here adjudicates)

**FLAG-1 — the direction conflict (Grant's Rule-12 direction ruling is
PENDING; this PR adjudicates it in NEITHER direction).** Both directions are
preserved verbatim:

- **clm-exjfai, `manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md`
  §1.2** — the claim BODY (still asserting SLOW-crossing → freeze + ≥100 Cp
  persistence) is preserved verbatim, now under a **🔴 CONTESTED dated-demotion
  banner landed on main** by PR #738 (merged `31bf34d4`, 2026-07-19; register
  confidence 0.50→0.20 ⇒ solidity 0.30→0.20). **Temporal update (verify-before-
  cite):** at the time this landing lane was briefed the demotion was on PR
  #738's branch `docs/post-merge-auditor-batch`; between the branch-point
  (`1be045a1`) and this rebase (`3efa24d6`) PR #738 MERGED, so the demotion — and
  the preserved claim body — are BOTH on main now. This landing changes NOTHING
  in that KB file. Verified two-method: the CONTESTED banner + preserved body at
  `dark-wake-bemf-foc-synthesis.md` §1.2, and the propagated dated pointers at
  `substrate-hysteresis-index.md` §1/§2. The preserved claim body reads:
  > "When $V(t)$ drops through $V_{\text{yield}}$ in the Cosserat sector at a
  > rate $\|dV/dt\|$ such that the crossing takes $\geq \tau_{\text{relax}}$, any
  > topologically non-trivial $\omega$ configuration present at the start of the
  > crossing window **FREEZES** … Residues persist for $\geq 100$ Compton periods
  > in the post-heal solid regime."
  → reads **SLOW crossing (duration ≥ τ_relax) → FREEZE.**

- **The arc's ODE-derived direction (prereg §2.3, result §1):**
  > "**FAST crossing (Δt_cross = ℓ_front/v_front ≲ τ_relax, high v_front) →
  > FREEZE; SLOW crossing (Δt_cross ≫ τ_relax) → HEAL.**" … "The grounding-pass
  > direction (fast → freeze) is CORRECT per the memristive-lag mechanism;
  > `dark-wake-bemf:54` is BACKWARDS as literally stated."
  → reads **FAST crossing → FREEZE.**

These are literally opposite. Per the arc's own flag-don't-fix posture, the
resolution is surfaced (the ODE derivation leans fast→freeze) but NOT landed as a
correction: the clm-exjfai prose direction is a candidate for a Rule-12 dated
correction that the auditor/Grant lands. **Status of the clm-exjfai handling
(distinct from THIS direction question):** PR #738 (merged `31bf34d4`) already
landed a CONTESTED demotion of clm-exjfai on the PERSISTENCE-MAGNITUDE axis
(≥100 Cp contested by the arc's ≤3.04 Cp) — but it explicitly routed the
DIRECTION conflict (slow→freeze vs fast→freeze) to Grant, unresolved (docket
ENTRY 22 D1: "the direction conflict … routed to Grant, not resolved"). So the
direction ruling remains PENDING even post-#738. **This PR changes NOTHING in the
KB and adjudicates NEITHER direction.** Note also: the
arc's lasting-freeze negative (§1/§3) means the two-arm run did NOT deliver a
clean freeze at either direction to arbitrate the conflict at the real-space
observable — the direction call rests on the ODE derivation + the S_min-rise
mechanism read, not on an observed lasting freeze.

**FLAG-2 — a FOLLOW-UP numbering SWAP between two _orchestration docs (surfaced,
not resolved).** The two tracked docs disagree on the follow-up numbers:
- `_orchestration/2026-07-19_branch-scrub-inventory.md` calls
  `analysis/moving-front-freezein` **FOLLOW-UP #2** and
  `analysis/2026-06-06-open-short-relabel` (trampoline-primer hunk) **FOLLOW-UP #1**.
- the docket `_orchestration/2026-07-10_rulings-docket.md` ENTRY 22 (landed via
  PR #738) SWAPS them: D1 calls this arc's landing "the still-open remainder of
  **FOLLOW-UP #1**" and D6 calls the primer fix "scrub **FOLLOW-UP #2** discharged."

The launching brief follows the docket (FOLLOW-UP #1). The tag + head SHA
(`archive/analysis/moving-front-freezein` @ `f647f58b`) are unambiguous and
identify THIS arc regardless of the label, so the work target is not in doubt.
The inventory-vs-docket numbering swap is a genuine corpus inconsistency flagged
for the orchestrator to reconcile — NOT silently renumbered here (flag-don't-fix).

**FLAG-3 — committed driver vs banked dataset provenance (surfaced).** The
banked `results.json` records `"driver": "…run_full / warm_sweep"` and a seed
block `R_major=4.0, sigma=1.8`, but the committed `run_full` (a) exposes no
`warm_sweep` entry point and (b) computes its seed internally as
`R_major=min(6.0,0.30·N)=3.6, sigma=2.5` at N=12 — neither matches the banked
seed. So the authoritative dataset was produced by a bespoke driver path not
fully captured in the committed test file. The reproduction (§1) therefore
re-ran the banked seed via a harness mirroring `run_full`'s structure (exact
MATCH), and this addendum discloses that a reviewer invoking the committed
`run_full` at N=12 will get the same NEGATIVE but with the committed-seed
absolute numbers, not the banked-seed table. Flagged, not fixed (the archived
record is preserved; retrofitting the committed driver to the banked seed would
be a Rule-11 retune).

