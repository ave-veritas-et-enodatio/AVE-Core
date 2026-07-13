# Genesis node-birth discriminators D1–D4 — RESULT (REBINNED)

**Date:** 2026-07-12 · **Branch:** `analysis/genesis-node-birth-d14`
**Prereg (FROZEN by push on #654):** `research/2026-07-12_genesis-node-birth-discriminator_prereg_FROZEN.md`
**Driver:** `src/scripts/vol_1_foundations/genesis_node_birth_discriminator.py`
**Class:** architecture discrimination. **No chord. No `genesis_v{N}`. No graph-growth.**

α-CLEAN. Rule-14: reuses `CrystalEngine` / `MasterEquationFDTD` / `loop_gap_harness.run_loop_gap_probe`.

> **2026-07-12 REBIN (adversarial-review repair, R1–R8).** The shipped verdict
> below (bin (ii) A-WEAKENED) rested on a **battery-of-one**: a single seed mode
> (`photon_lock`), single fidelity (`fast=True`), which failed. The frozen bin (i)
> criterion is *"D1 invariant + D2 persistence PASS on **≥1** landed fixed-N path"*.
> Re-running the battery at the banked config across **all three** landed seed
> modes gives a **per-fidelity SPLIT**:
>
> - **SMOKE** (`fast=True`, short drive-off window `n_quiet=12`): **2/3 persist**
>   (`pair`, `graded_a0`) ⇒ **bin (i) A-SUPPORTED at smoke fidelity**.
> - **PRODUCTION** (`fast=False`, longer window `n_quiet=52`): **0/3 persist** —
>   every landed seed mode falls below the 0.85 `E_persist` floor (pair 0.86→0.69,
>   graded_a0 0.85→0.68) ⇒ **bin (ii) A-WEAKENED at production fidelity**.
>
> The smoke persistence **does not survive grid/window refinement**: the longer
> production drive-off lets the energy decay further, and the coarse-grid PASS is a
> short-window artifact. Production (the more physically faithful read) **vindicates
> the original (ii) direction** — but now on the properly broadened 3-mode battery,
> not a battery-of-one. Per Rule 11 the headline is the **per-fidelity table**;
> **ruling-grade banking (which fidelity Grant banks as the fork verdict) is
> DEFERRED to Grant** — the frozen bins do not name a fidelity authority, and lane
> discipline forbids me ruling the fork. The original bin (ii) text is preserved
> verbatim (KEEP-BOTH), superseded-in-reasoning not erased. The FROZEN prereg on
> `main` is untouched; every deviation is a dated note here.

---

## Re-adjudicated verdict (per-fidelity)

| fidelity | D1 | D2 (≥1 of 3 landed paths persists) | D3 | frozen bin |
|---|---|---|---|---|
| **smoke** (`fast=True`, `n_quiet=12`) | invariant | **PASS** — `pair` + `graded_a0` persist (**2/3**) | not-entailed | **(i) A-SUPPORTED (smoke)** |
| **production** (`fast=False`, `n_quiet=52`) | invariant | **FAIL** — all three fall below floor (**0/3**) | not-entailed | **(ii) A-WEAKENED (production)** |

**Ruling-grade banking DEFERRED to Grant — production does NOT rubber-stamp smoke;
it reverses it.** Both fidelities ran the full 3-mode battery at the banked config.
At **smoke** 2/3 persist ⇒ (i); at **production** 0/3 persist ⇒ (ii). The smoke
persistence is a **short-drive-off-window artifact**: extending the quiescence
window from `n_quiet=12` to `52` lets `E_persist` decay below the 0.85 floor on
every seed mode (`pair` 0.8639→0.6929, `graded_a0` 0.8544→0.6764,
`photon_lock` 0.8198→0.7750). This matches the 2026-06 prior-art direction
(`E_persist` 0.60→0.47, `research/2026-06-12_loop-gap-harness-phase2_result.md`).
Per Rule 11 the headline is the **per-fidelity table**, not a single bin. The
production read at first looks like it **vindicates the original (ii) A-WEAKENED
direction** on the broadened battery — **but a boundary-vs-physics discriminator
(decision-point (b), below) shows the production E-collapse is substantially a
domain-leakage artifact**: a domain-size sweep recovers `E_persist` monotonically
(0.6929→0.7984→0.8449 as N goes 10→12→14, PML fixed at 3), so at N=10 the interior
is only 4³ cells inside the absorbing shell and the "decay" is boundary absorption,
not bulk dissipation (ARTIFACT-LEANING). So **both** the smoke (i) and the production
(ii) reads at N=10 are boundary-confounded. **Which bin Grant banks is DEFERRED to
Grant** (frozen bins name no fidelity authority; ruling the fork is not the
implementer lane's call), and a clean adjudication needs N≥14 / closed-box first.
Neither reading rules fork (A) or (B).

### KEEP-BOTH — original (superseded) verdict, preserved verbatim

> | bin | outcome |
> |---|---|
> | **(ii) A-WEAKENED** | **LANDED** |
>
> | **D2** Fixed-N persistence | **FAIL** on declared harness battery (`N=10`, `fast=True`, photon_lock + bulk density) | `C_consistency` |
> …
> **Meaning (frozen):** Fixed-N pattern is insufficient for lasting localization
> on the declared battery. This does **not** auto-select fork (B). R10 remanence
> remains open under (A). KEEP-BOTH continues until Grant rules.

(Full original result preserved in git at `730cd431`. The "declared harness
battery" above was the single `photon_lock`/`fast=True` leg — R7.)

The above stood on the single-leg `photon_lock`/`fast=True` FAIL. R1 (below) shows
that leg was the seed mode **most expected to fail** — its φ-channel was
structurally dead at write-time (R5). Two things are now true and both are recorded
(KEEP-BOTH): (a) the original single-leg **reasoning** was unsound — at smoke the
*broadened* battery would have flipped to **(i)** (2/3 persist); (b) the original
**verdict** (ii) is nonetheless **vindicated at production fidelity** (0/3 persist),
which is the more faithful read. So (ii) survives as a conclusion, not as its
original battery-of-one argument.

**Refuse:** never bank D1 PASS as `ClaimClass.EMERGENCE` / node genesis (#653).
**Refuse:** never bank (i) A-SUPPORTED as fork-(A) *ruled*, and never bank (ii)
A-WEAKENED as fork-(B) *selected* — (i) means (A) remains viable for *pattern*;
(ii) weakens (A)-as-sufficient for lasting localization but does **not** auto-select
(B); (B) is not forced either way; R10 remanence still open.

---

## D1 — cardinality (2 measured + 1 structural)

R3 repair (2026-07-12): the shipped harness D1 row was a **declared literal**
(`n_sites_t0`/`tend` the same expression, `invariant=True` hard-coded, no engine
step). Route chosen: **re-label as structural, exclude from the measured count**
(the cheap+honest option — genuinely stepping a rank-4 harness here would push
`run_suite` into the slow `engine_sim` lane for zero new information: a fixed numpy
mesh cannot mutate cardinality on this platform). The two crystal/ME legs remain
**measured** — cardinality read after 40 genuine `.step()` calls.

| path | N | sites t0 | sites tend | invariant | class |
|---|---:|---:|---:|---|---|
| crystal_engine | 16 | 4096 | 4096 | yes | **measured** (40 steps) |
| master_equation_fdtd | 16 | 4096 | 4096 | yes | **measured** (40 steps) |
| loop_gap_harness | 10 | 1000 | 1000 | yes | **structural** (config-invariant by construction — install-tautology, mesh cannot mutate on this platform) |

**Measured paths: 2. Structural paths: 1.** Fireable content of D1 is the
**labeling discipline** (refuse EMERGENCE-as-genesis) + the new adjudicator halt
(R2) that would surface any *future* cardinality mutation instead of mis-binning it.

---

## D2 — persistence battery (R1: all three landed seed modes)

R7 note: the battery composition was a **post-freeze free parameter**. The FROZEN
prereg §Gates 2 says only *"D2 drive-off persistence battery (reuse harness
ablation idiom)"* — it does **not** pin the seed-mode set or fidelity. The shipped
driver chose n=1 (`photon_lock`, `fast=True`); this repair broadens it to all three
landed seed modes at the banked config. Banked drive-off config (unchanged):
`run_loop_gap_probe(N=10, rank_target=4, bulk_density_on=True, front_target=A_YIELD,
n_drive_mult=0.5, n_quiet_mult=1.5)`.

### Smoke fidelity (`fast=True`)

| seed_mode | E_persist (≥0.85) | φ_persist (≥0.80) | rank4 | v_inc_peak | persist | runtime |
|---|---:|---:|---|---:|---|---:|
| `pair` | 0.8639 | 7.7295 | true | 0.0122 | **PASS** | 161.2 s |
| `photon_lock` | 0.8198 | 0.0000 | false | 0.0000 | **FAIL** | 160.4 s |
| `graded_a0` | 0.8544 | 1.9636 | true | 0.0188 | **PASS** | 142.9 s |

(`n_drive=6`, `n_quiet=12` on every smoke leg; N=10, rank 4, bulk on, front=A_YIELD.
`pair`/`graded_a0` reproduce the adversarial-review live-fire exactly; `photon_lock`
reproduces the shipped FAIL — E=0.8198 vs the doc's 0.820.)

**Smoke read:** **2 of 3** landed paths persist (`pair`, `graded_a0`) ⇒ D2 PASS on
≥1 path ⇒ **bin (i) A-SUPPORTED at smoke fidelity**.

### Production fidelity (`fast=False`) — full battery ran; 0/3 persist

The full 3-mode production battery ran (clean sequential timing under quiet load):

| seed_mode | E_persist (≥0.85) | φ_persist (≥0.80) | rank4 | v_inc_peak | persist | runtime |
|---|---:|---:|---|---:|---|---:|
| `pair` | **0.6929** | 0.8734 | false | 0.0122 | **FAIL** | 183.0 s |
| `photon_lock` | **0.7750** | 0.0000 | false | 0.0000 | **FAIL** | 212.1 s |
| `graded_a0` | **0.6764** | 0.8905 | false | 0.0188 | **FAIL** | 324.3 s |

(`n_drive=18`, `n_quiet=52` at production vs 6/12 at smoke — ~4× the step count.)

**Read (load-bearing).** At production grid **every** seed mode's `E_persist` falls
below the 0.85 floor (`pair` 0.8639→0.6929, `graded_a0` 0.8544→0.6764,
`photon_lock` 0.8198→0.7750). **0/3 persist ⇒ bin (ii) A-WEAKENED at production
fidelity** ("D1 invariant but D2 FAIL across declared battery; D3 holds"). The
smoke 2/3 PASS is a **short-drive-off-window artifact**: with `n_quiet=12` the
energy has not yet decayed below floor, but with `n_quiet=52` it does. Note φ
persists on `pair`/`graded_a0` (0.87–0.89) even at production — the localization's
*winding/phase* memory outlives the *energy*, but the frozen persistence gate
requires BOTH E **and** φ above floor, so the E-collapse alone flips every leg to
FAIL.

**Runtime receipts (clean, quiet-load).** 183.0 s / 212.1 s / 324.3 s — all under
the ~5-min budget. (An earlier `pair` production probe read 390 s but was inflated
by concurrent `make verify`; the physics is identical, E=0.6929 either way — the
390 s was wall-clock contention, not a different result.) Because all three came in
under budget, no production leg is owed.

### Boundary-vs-physics discriminator (decision-point (b), 2026-07-12)

Is the production `E_persist` collapse **genuine bulk dissipation** or **domain
leakage** into the fixed absorbing boundary? On a lossless-reactive interior (Ax3)
the only dissipation channel is the `pml=3` absorbing shell (`total_H` sums the
whole domain, so PML damping removes energy from H over the quiet window). The
`φ_persist`-alive / `E_persist`-collapse pattern is the classic boundary-absorption
signature. **Discriminator chosen:** domain-size sweep (option 2 — the harness
exposes `N` directly; no engine edit). PML is fixed at 3 cells, so the interior
`(N−6)³` grows while the boundary shell stays constant — boundary leakage must
shrink with N; genuine bulk decay would be ~N-flat. (Option 1 closed-box / `pml=0`
and option 3 interior-vs-shell energy split both need per-cell energy density not
exposed by the public API → engine edit; not run.)

Pair seed, production fidelity, banked config otherwise unchanged
(`n_drive=18`, `n_quiet=52` at every N):

| N | interior `(N−6)³` | `E_persist` (floor 0.85) | `φ_persist` | runtime |
|---:|---:|---:|---:|---:|
| 10 | 64 | 0.6929 | 0.8734 | 183.0 s |
| 12 | 216 | **0.7984** | 0.9087 | 467.8 s |
| 14 | 512 | **0.8449** | 0.7266 | 597.7 s |

**Reading — ARTIFACT-LEANING (strong), no over-claim.** `E_persist` recovers
**monotonically** with domain size (0.6929 → 0.7984 → 0.8449), climbing back toward
the smoke value (0.8639) / the 0.85 floor as the boundary fraction shrinks. That is
the domain-leakage signature: the production E-collapse is **substantially PML
boundary absorption, not bulk dissipation**. Per regime/phase-state discipline, a
FAIL driven by an absorbing boundary at a domain so small the interior is only 4³
cells (inside a 3-cell PML shell) is **artifact-class** — the "decay" is where the
energy *leaked*, not where it *dissipated*. By the coordinator's own criterion
(E recovers toward smoke ⇒ leakage), the production **bin (ii) is evidence-weakened
toward void**: at N=14 the pair `E_persist`=0.8449 essentially recovers to the smoke
value, so the N=10 production E-FAIL is a small-domain boundary artifact.

**Caveats (honest).** (1) Only the `pair` seed was swept (budget); `photon_lock`
(φ dead) and `graded_a0` not swept. (2) `φ_persist` is non-monotonic
(0.87→0.91→0.73) — at N=14 the sub-floor is now **φ-limited**, not E-limited, so
the *E*-channel artifact is demonstrated but a *clean PASS* at N=14 is not (φ dips).
(3) Budget: the sweep ran ~18 min (N=12 468 s + N=14 598 s), over the ~15-min
target — flagged; the third point was kept because it lands `E_persist` at the floor
and makes the trend dispositive. (4) This does not by itself prove the localization
persists — it shows the production **bin (ii) E-FAIL is boundary-confounded**, so a
proper adjudication needs N≥14 (or a closed-box variant) before either fidelity's
bin is banked.

### φ-channel honesty (R5)

The shipped `photon_lock` FAIL reported `φ_persist=0`. That zero was **structurally
dead at write-time**, not a live physics miss on the φ arm:

- `research/2026-06-12_loop-gap-harness-phase2_result.md:39–41` — *"V_inc nucleation
  still needs converter+pair path"*: `photon_lock` produces `v_inc_peak=0`, so there
  is no V-sector amplitude for the φ-link ratio to persist from.
- `src/ave/core/cross_sector_coupling.py:136–137` — the bounded trilinear arm
  (`photon_deplete=False`, the default) *"does NOT transfer (~2 %, inert)"*.

So the only **live** content of the original D2 FAIL was the **E-miss** (0.820 vs
0.85 floor — a 3.5 % shortfall, at **smoke** fidelity). The `pair` and `graded_a0`
legs fire both E **and** a nonzero φ, which is why they persist **at smoke**; at
production their φ stays alive (0.87–0.89) but their E collapses below floor, so the
φ-channel is never the failure mode for those two — the E-decay is.

---

## D3 — cite table (not entailed)

| leaf | point |
|---|---|
| `manuscript/ave-kb/common/historical-precedents.md` | Kelvin lacked confinement + scale; AVE names both on fixed N — does not derive N→N+1 necessity |
| `manuscript/ave-kb/common/engine-capability-map.md` | node-creation empty on every engine; after remanence+boost in build-order |
| `research/2026-06-24_engine-stage2-native-cage_result.md` | Mode-III DISPERSE; Γ=−1 cavity on fixed mesh |
| `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` | ranks 1–4 fixed platforms; R10 constitutive, not graph-growth |

No load-bearing leaf found that **derives** Compton-scale N→N+1 as necessary for
charged-soliton existence. D3 unchanged by this repair.

---

## D4

**SKIPPED-WITH-REASON.** Numeric OOM fence is post-(B)-ruling only. Phase-0 remains
KEEP-BOTH.

---

## Gate-structure repair (R2, 2026-07-12)

The shipped `adjudicate_bin` terminal fall-through returned `ii_A_WEAKENED` for
**every** `d1_ok=False` case. A real cardinality mutation — the fork-(B) signature,
the single most consequential possible firing — would have been labelled as an
(A)-*weakening*. REPAIR: an explicit OUT-OF-BIN outcome
`D1_CARDINALITY_VIOLATION_HALT`, returned whenever `d1_ok=False`, checked **first**
(it dominates D2/D3/D4). It is deliberately **not** in the frozen bin table — that
is the point: it **halts for Grant adjudication** rather than mis-binning. Unit
test `test_adjudicate_d1_violation_halts_all_combinations` asserts the halt for all
16 `(d2,d3,d4_ran,d4_absurd)` combinations, plus that `d1_ok=True` never returns it.

---

## Gates checklist (prereg §Gates)

1. D1 cardinality — done (2 measured + 1 structural; R3).
2. D2 drive-off persistence battery — done (all 3 landed seed modes at BOTH smoke
   and production fidelity; R1). Smoke 2/3 persist ⇒ (i); production 0/3 ⇒ (ii).
3. D3 cite table — done.
4. D4 SKIPPED-WITH-REASON — done.
5. `ClaimClass` tags — done (refuse EMERGENCE-as-genesis).
6. **`make verify` PASS** — **PASS** (run 2026-07-12 in the worktree; exit 0,
   *"[Verify] ALL PHYSICS PROTOCOLS PASSED"*, incl. Kernel Check + KB claim-id +
   md-links + provenance-stamps). **mass = A1** untouched.
   > **Deviation note (2026-07-12):** the shipped doc silently replaced frozen
   > gate 6 (*"`make verify` PASS"*) with *"Fast pytest keepers green"*. That was a
   > gate substitution, not a gate. Restored here with the real `make verify` result.

---

## Out of scope (still forbidden)

- Graph-growth / fourth engine / `genesis_v{N}` / srs v18+.
- Merging #652 X44 as reconciled.
- Ruling (A) or (B) from this result alone — **smoke (i) keeps (A) viable for
  *pattern*; production (ii) weakens (A)-as-sufficient for lasting localization.
  Neither rules (A), closes R10, or selects (B).**

## Dependency (R8)

**#661's G-PERSIST ruling banks this PR's bin.** Its confirmation must **postdate**
this re-adjudication — coordinated with the #661 repair lane. If #661 lands a
G-PERSIST verdict before this per-fidelity table is settled, that ordering is a
conflict to surface, not to resolve silently.

## Next (orchestration)

Grant: keep KEEP-BOTH; neither fidelity by itself escalates to graph-growth. The
ruling-grade banking decision is yours. Decision-point (b) has now been **probed**
(boundary-vs-physics discriminator, above): the production E-decay is
**ARTIFACT-LEANING** — a domain-size sweep recovers `E_persist` 0.69→0.80→0.84 as
N grows 10→12→14 (PML fixed), so the N=10 production FAIL is substantially boundary
leakage, not bulk dissipation. Implication: **do not bank either N=10 bin as the
fork verdict** — both are boundary-confounded at a 4³-cell interior. Recommended
path before any banking: re-run the persistence battery at **N≥14** (or a closed-box
`pml=0` variant, which needs a small harness passthrough) so the interior is not
PML-dominated; then adjudicate. Either way: no (B) ruling, no fourth engine, R10
still open, `#661` G-PERSIST must postdate this.
