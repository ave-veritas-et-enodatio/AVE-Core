# RESULT — Genesis-v7 PHASE 3: the QUADRATURE-DEPOSIT MATRIX (D13 deposit + D14 lock-survival discriminator)

**Date:** 2026-06-10
**Prereg (FROZEN, committed ALONE @ `d4b4af4b`):** `research/2026-06-10_genesis-v7-quadrature_prereg.md`
**Engine (FROZEN @ `09d47e45`):** `src/ave/core/unified_genesis_engine.py` — v7 D13 quadrature deposit (the ω-deposit `(2c)` branch, `unified_genesis_engine.py:662-680`); v6 byte-identical when `quadrature_deposit=False` (the D-INHERIT keeper `test_unified_quadrature_v7.py::K-OFF`).
**Driver:** `src/scripts/vol_1_foundations/genesis_v7_quadrature_run.py` (parallel via `genesis_parallel_runner`; seed `20260610`)
**Raw numbers:** `research/2026-06-10_genesis-v7-quadrature-run_results.json` (every number below read FROM it — ave-driver-script-honesty)
**Figures:** `research/figures/fig_v7_{A46_coordinate,D14_survival,emergent_vs_planted,full_assembly_swamp}.png`

---

> 🔴 **VERDICT RE-BINNED — DEPOSIT-SURVIVES-NO-QUANTIZATION → DEPOSIT-DRAINED-AGAIN (2026-06-10 demotion addendum, §11 below).** Per the prereg's OWN frozen F-NETFIELD survival gate (gap-to-accumulator ≲ 1 OOM, `prereg:147,183-184`) — which the driver NEVER COMPUTED (docstring-only, `genesis_v7_quadrature_run.py:388`). Computed from the raw JSON the gate FAILS: **ISO 3.34 OOM, FULL 4.03 OOM**, both in the prereg's ≈4-OOM DRAINED band. The §1 "D14 SURVIVES (not DEPOSIT-DRAINED-AGAIN)" headline is SUPERSEDED. Per Rule 12 §§0–10 are PRESERVED UNCHANGED — read them through §11; the frozen prereg (`d4b4af4b`) is untouched.

## 0. THE QUESTION — answered from the numbers

> *Does the photon's helicity become a quantized WINDING — `w_pol ≠ 0` DE NOVO, helicity-odd, transducer-OFF-absent, above the calibrated floor — once the deposit is a poloidal-projecting LC quadrature (the mode the lock does NOT drain) instead of the v6 rigid-azimuthal mode (which the lock drains)?*

**The deposit-geometry hypothesis is CONFIRMED at the field/mechanism level, but the winding does NOT quantize.** The v7 poloidal LC-quadrature deposit **SURVIVES the lock** (D14: `C_pol(lock-ON)/C_pol(lock-OFF) = 1.0000`, lock_eta-independent; the v6 rigid control DRAINS, `0.0014`) — so the v6 "structural block" (the lock draining the rigid-azimuthal deposit) **is real and is RESOLVED by the quadrature geometry.** The deposit is winding-CAPABLE and helicity-odd in the matched read coordinate (a fresh 200-step deposit reads `w_pol = q_dep`, tracks `q ∈ {2,3,4}` exactly, `C_pol` sign-flips RH/LH, absent in OFF/rigid/achiral, N-robust). **But the winding does NOT lock:** it decoheres `3 → 1` within one LC quarter-period (~907 steps) even with the deposit continuously live, it merely reads back the *deposited* `q` (consistency, not an emergent `(2,3)` attractor), and in the full electron-genesis assembly it is **swamped to `w_pol ≡ 0`** (the v6 result reproduced exactly). T1 is UNBROKEN.

## 1. VERDICT — **DEPOSIT-SURVIVES-NO-QUANTIZATION** (the prereg §6 anticipated bin; two named missing closures)

Per the FROZEN §6 ordered bins (floors first; Rule 11, no post-hoc criterion drop). **F-T1 passes in every arm → not T1-BROKEN. D14 SURVIVES (not DEPOSIT-DRAINED-AGAIN). The net field LC-quadrature deposit survives lock-ON above floor, BUT `w_pol` does not quantize → DEPOSIT-SURVIVES-NO-QUANTIZATION.** This is the discipline at full strength (A44: the diagnosis is an engine coupling-family / closure gap, NOT a missing axiom — no Ax-5 drafted). NOT-ELECTRON (the v5 panel) is NOT reopened; the v6 DEMOTED-PARTIAL record stands; v7 is the structural-block hypothesis's own Rule-12 chain.

| § | claim | floor-check (first) | result | bin contribution |
|---|---|---|---|---|
| **F-T1** | D-INHERIT regression: the converged mass survives the deposit | `E_V^cons → ~12.9`, drift < 2% | FULL arms `E_V^cons` **12.87–12.93**, drift < 1% (baseline 12.87) | **PASS** — not T1-BROKEN |
| **D14** | poloidal deposit survives lock-ON; rigid drains | `C_pol(ON)/C_pol(OFF)` vs rigid `L_ω(ON)/L_ω(OFF)` | poloidal **1.0000** (survives), rigid **0.0014** (drains, ~726×); lock_eta-INDEPENDENT | **SURVIVES** — block resolved |
| **de-novo (matched, fresh)** | `w_pol ≠ 0`, helicity-odd, OFF-absent | F-WPOL: rel > 0.1, r ≥ 3, known-positive at scale | `w_pol = q_dep` (200 steps), rel 0.24, `C_pol` flips RH/LH, OFF/rigid/achiral = 0 | winding-CAPABLE, but… |
| **quantization (K3 time)** | the winding LOCKS to an integer | persists/sharpens over the build | decoheres **3 → 1** by step 907, settles at 1 (rel 0.235); **reads back deposited `q`** | **NO LOCK** (closure 1) |
| **full assembly (mandate)** | de-novo `w_pol` on the D-INHERIT product | matched read, column+buckle live | `w_pol ≡ 0` (lone achiral `w_pol=1` floor-grazer rel 0.167 — v6 reproduced) | **SWAMPED** (closure 2) |

**The two named missing closures (A44, engine coupling-family):**
1. **No topological lock-in.** The deposited integer winding de-coheres `3 → 1` within one LC quarter-period and is stable at 1 thereafter — the isolated LC tank has no nonlinear quantizer to protect the deposited `q`. The read TRACKS `q_dep` (reads the deposit, not a self-organized `(2,3)` attractor) — consistency-class, not emergence-class.
2. **Column + buckle dominance.** In the full electron-genesis assembly the transducer's poloidal deposit is sub-dominant by ~2 OOM to the energized rotation column + the buckle's own ω (`C_pol`: MAIN `+4.1e-5` vs OFF `-4.3e-3`), so the de-novo read sees the column structure → `w_pol ≡ 0`, exactly the v6 outcome.

---

## 2. THE A46 COORDINATE FINDING — the PHASE-2 smoke headline was a read-coordinate artifact (SURFACED, flag-don't-fix)

**This is load-bearing and contradicts the PHASE-2 smoke's headline number — surfaced, not reconciled-away.** The PHASE-2 smoke (`2026-06-10_genesis-v7-quadrature-smoke_results.json`) fired **QUADRATURE-LIVE** on `C_pol = −6.122e-6` "surviving the lock" at N=28, read at the **deposit-default `pol_R = 0.30·N`**. That `pol_R` is the **WRONG read coordinate** (A46): the read torus scales with N (`pol_R ∝ N`) while the near-core saturation shell does NOT (it sits at real-space `ρ ~ 2.5`, set by the seed `sigma`, ~N-independent). So `C_pol` at the default `pol_R` **N-COLLAPSES** — measured this run (plant-at-scale, deposit pattern at run scale):

| N | 28 | 40 | 48 | 56 |
|---|---|---|---|---|
| `C_pol` @ default `pol_R=0.30N` | **−3.06e-6** | −1.52e-9 | −9.83e-12 | **−2.61e-13** |

A **7-OOM collapse** over `N=28→56` — the §5-sweep-#8 N-tracking CLIP telltale. **The smoke's −6.122e-6 was the deposit's near-core tail leaking into a reading-torus whose inner edge happened to be close at N=28; it is not the physics, and it does not scale.** Read in the **matched coordinate** (`pol_R = 5.0`, `pol_r = 3.0` — the field-matched torus that brackets the saturation shell AND clears the r ≥ 3 floor) the de-novo `w_pol = q_dep` is **N-ROBUST** (`w_pol = 3` at N = 40, 48, 56, identical rel 0.240). *(`fig_v7_A46_coordinate.png`.)*

**Geometry root cause (substrate, surfaced):** the genesis saturation pocket at the 3200-step stop is a **near-core SPHERE shell** (`ρ ∈ [0.71, 2.55]`, `z ∈ [−2.5, 2.5]`, filled center — 24 cells at `ρ < 0.8`; pocket_cells = 0, the snap onset is ~3396 as in v6), **not a torus.** It has no field-defined major radius — so the deposit's `pol_R` is a CHOICE, not a field-derived quantity (the prereg §3.3 "the saturated seed defines the major radius" is ill-posed for a spherical pocket). The default `0.22..0.30·N` places the read torus OUTSIDE the sphere; the matched `(5, 3)` is the minimal r ≥ 3 torus bracketing it. **The survival CONCLUSION (D14) is robust to this choice** (the lock cannot drain a zero-net-L mode regardless of where it is read); only the smoke's specific `C_pol` value and its N-scaling were coordinate artifacts.

---

## 3. D14 LOCK-SURVIVAL — the structural-block hypothesis CONFIRMED (the v7 half-win)

The discriminator FIRES at production scale (N=48, 3200 steps, matched read). The lock drains precisely the rigid mode and leaves the poloidal LC quadrature — exactly the `_lock_relax` mechanism (`crystal_graft_v4.py:186-204` docstring: *"damp ONLY the rigid-rotation (net angular-momentum) mode … leaving the local LC quadrature — hence the poloidal winding — intact"*). *(`fig_v7_D14_survival.png`.)*

- **poloidal quadrature SURVIVES:** `C_pol(lock-ON) = −1.741e-4`, `C_pol(lock-OFF) = −1.741e-4` → **ratio 1.0000** (field-to-field, gross-vs-field — NOT the accumulator).
- **rigid v6 control DRAINS:** `L_ω,axial(lock-ON) = +3.27e-4`, `L_ω,axial(lock-OFF) = −0.2368` → **drain ratio 0.0014** (~726×; the v6 4-OOM lock-drain reproduced).
- **survival is lock_eta-INDEPENDENT:** `C_pol = −1.676e-4` FLAT across `lock_eta ∈ {0, 0.05, 0.08, 0.12}` (max-min/max < 0.05) — genuinely zero-net-L, NOT a residual net-L leaking into the drain (the DEPOSIT-DRAINED-AGAIN mechanism is ruled out).
- **the `lock × alpha` 2×2 (the D14 core):** rigid (α=0) `L_ω` drains `−0.486 → −0.0107` under lock; poloidal (α=1) `C_pol = −1.676e-4` IDENTICAL lock-OFF vs lock-ON. **The lock sees the rigid mode and is blind to the poloidal quadrature** — the structural-block hypothesis, confirmed.
- **substep keeper (K-LOCK-PRESERVES):** one `_lock_relax` contracts a planted rigid net-L by exactly `(1−η)` while the planted poloidal L-state norm is preserved to > 0.999 (`test_unified_quadrature_v7.py`, green).

**This is the genuine v7 advance over v6:** v6 showed the rigid deposit is lock-drained; v7 shows a poloidal quadrature deposit is lock-IMMUNE. The block WAS the deposit geometry (rigid → η-drain), and the quadrature geometry removes it. The photon's mechanical axial AM still goes to the rigid mode (lock-drained — `L_ω,axial(MAIN−OFF) = −3.61e-5`, the v6 net-field number reproduced EXACTLY); its HELICITY is imprinted as the surviving poloidal content. AM ledger closes 1:1 (`ratio = 1.000000000`), passive (`E_absorbed = +0.542 ≥ 0`).

---

## 4. THE WINDING DOES NOT QUANTIZE — it reads back the deposit and DE-COHERES (closure 1)

The de-novo `w_pol` in the ISO matched coordinate over build time (K3 stop-time sweep — the §3.5(1) LC-rotation argument tested directly):

| build step | 200 | 907 (¼-period) | 1800 | 3200 |
|---|---|---|---|---|
| de-novo `w_pol` | **3** | **1** | 1 | 1 |
| `w_pol_rel` | 0.240 | 0.221 | 0.238 | 0.235 |
| `C_pol` | −1.68e-4 | −1.95e-4 | −1.82e-4 | −1.74e-4 |

**The integer winding decoheres `3 → 1` within one LC quarter-period and settles at 1** (the build series confirms: `w_pol` = 0,2,1,1,1,1,1,1,1 at steps 0..3200). The `C_pol` FIELD content holds (`−1.7e-4`-class throughout) — so the deposit's poloidal *content* survives (consistent with D14), but its *integer winding order* does NOT lock: the LC tank + dispersion unwind the deposited `q=3` faster than the transducer re-imprints it, and there is no buckle nonlinear quantizer in the isolated config to protect it.

**Consistency, not emergence (the consistency-vs-emergence tag):** the fresh-deposit read TRACKS `q_dep` exactly (`q ∈ {2,3,4} → w_pol ∈ {2,3,4}`, plant-at-scale + the live §5.3 sweep) — i.e. it reads back the *deposited* winding, NOT a self-organized topological `(2,3)` attractor (an electron winding should be `(2,3)` independent of `q_dep`). The winding is the planted deposit being faithfully read in the matched coordinate, then de-cohering — a **consistency-class** read, not an **emergence-class** quantization.

**Honest caveat on the persistence sub-flag (flag-don't-fix):** the driver's `quantizes_locked` sub-flag reads `True` because the drive-off/transducer-off persistence phase starts at step 3200, by which point the winding has ALREADY decohered to `w_pol=1` (it then stays 1 through 3800). The persistence window therefore shows "no further unwinding" — but the real decoherence (`3 → 1`) happened DURING the build, captured unambiguously by the K3 time-series above. The VERDICT (DEPOSIT-SURVIVES-NO-QUANTIZATION) is unaffected; the sub-flag is measuring the wrong window and is not load-bearing. *(`fig_v7_emergent_vs_planted.png`.)*

---

## 5. THE FULL D-INHERIT ASSEMBLY — `w_pol ≡ 0` (column + buckle swamp), T1 UNBROKEN (closure 2)

The mandated D-INHERIT config (snap + buckle + energized rotation column + `seed_lane1` — the v6 electron-genesis assembly), N=48, 3200 steps, matched read. *(`fig_v7_full_assembly_swamp.png`.)*

| arm | `w_pol` | rel | `C_pol` | `L_ω,axial` | `E_V^cons` |
|---|---|---|---|---|---|
| FULL-MAIN-RH | **0** | 0.176 | +4.12e-5 | −3.61e-5 | 12.91 |
| FULL-LH | 0 | 0.177 | +8.77e-5 | +3.61e-5 | 12.91 |
| FULL-achiral | 1 | 0.167 | −3.09e-3 | −7.9e-16 | 12.93 |
| FULL-OFF | 0 | 0.200 | −4.34e-3 | +6.1e-16 | 12.87 |
| FULL-rigid-a0 | 0 | 0.174 | +3.72e-5 | −3.61e-5 | 12.91 |

- **`w_pol ≡ 0`** — the v6 result reproduced exactly. The lone `w_pol=1` is the **achiral** arm at rel 0.167 (a floor-grazer, exactly the v6 false-positive: the same floor-grazing read in the achiral arm, not coupling-driven).
- **`C_pol` is BUCKLE-DOMINATED:** OFF `−4.34e-3` and achiral `−3.09e-3` (the inherited buckle sources ω from helicity — the v6 DEMOTION-2 contaminant, `director = photon w`) are ~2 OOM LARGER than the transducer's MAIN `+4.12e-5`. The deposit's poloidal content (clean and lock-surviving in isolation) is sub-dominant to the column + buckle here, so the de-novo read cannot resolve it.
- **`L_ω,axial(MAIN − OFF) = −3.61e-5`** — the v6 net-field rigid deposit reproduced to 3 sig-figs (the K-OFF byte-identical inheritance: the v7 poloidal add-on rides on top of the v6 1:1 rigid transfer, untouched).
- **T1 UNBROKEN:** `E_V^cons` = 12.87–12.93 across all arms (drift < 1%), the converged ~12.9 dilatation mass — the deposit is passive in the full assembly despite the boundary-locality. **F-T1 PASS → not T1-BROKEN.**

---

## 6. FLOORS + FAIL-FAST + PLANT-AT-SCALE (ORDERED BINS — evaluated FIRST)

- **F-T1** (D-INHERIT, first of all): baseline `E_V^cons = 12.87`, drift < 1% — every arm holds (§5).
- **F-EXCHANGE / F-ACHIRAL** (structural zeros, matched read): chi=0 transducer-OFF `C_pol = 0.0`; helicity=0 achiral `C_pol = 0.0` — exact structural nulls (ISO config). Every positive `C_pol` is above this zero floor.
- **F-WPOL known-positive (plant-at-scale, BEFORE any de-novo read):** the deposit pattern at run scale reads `w_pol = q_dep` for `q ∈ {2,3,4}` at the matched torus (tracks-q [True,True,True]); the **rigid v6 pattern reads `w_pol = 0`** (the read distinguishes poloidal from rigid — K-RIGID-NULL); the default-`pol_R` read N-collapses (§2). The extractor is known-positive at scale AND known-negative on the rigid mode.
- **D12 fail-fast (BEFORE the matrix):** handedness ALIVE (RH ≠ LH in ω within 200 steps), achiral null (`C_pol = 0`), transducer-OFF null (`C_pol = 0`), helicity-odd (`C_pol` sign-flips RH/LH). All pass — no dead coupling.
- **6/6 v7 keepers green** (`test_unified_quadrature_v7.py`): K-OFF, K-PLANT-AT-SCALE, K-RIGID-NULL, K-HELICITY-ODD, K-AM-LEDGER, K-LOCK-PRESERVES.


---

## 7. §210-COMPLIANCE — every mandated §5 sweep executed (numbers FROM the field)

All §5 knobs swept (sweeps at n_build=200 = the FRESH-deposit read, before the build-time decoherence of §4; K3 and frac at full build). **The verdict-critical invariances (helicity-oddness, the structural/transducer/achiral nulls, the rigid-control null) hold at every swept point; only the deposit MAGNITUDE scales with the coupling knobs (§210-clean).**

| # | knob | grid → result | gate verdict |
|---|---|---|---|
| 1 | `alpha_pol` | `C_pol` LINEAR 0→−1.68e-4 (1e-22, −4.2e-5, −8.4e-5, −1.3e-4, −1.7e-4); `w_pol` = 0 at α=0, **3** at α>0 | control axis CLEAN (rigid α=0 = null) |
| 2 | `lock × alpha` (D14) | rigid `L_ω` 0.486→0.0107 (drains); poloidal `C_pol` identical ON/OFF | SURVIVES (§3) |
| 3 | `q_dep` | `w_pol` = **2,3,4** for q = 2,3,4 (tracks-q [T,T,T]) | tracks the design (reads the deposit) |
| 4 | `chi_exch` | `C_pol` scales −2.0e-5→−2.25e-4 (9e-4..0.08); `w_pol` = 3 (=2 at 0.08, the strongest coupling) | magnitude scales, oddness/null invariant — §210-clean |
| 5 | `lock_eta` | `C_pol` FLAT −1.676e-4 at {0,0.05,0.08,0.12} | eta-INDEPENDENT (zero-net-L) |
| 6 | `omega_recipient_frac` | `C_pol` 0 → −1.68e-4 → −3.35e-4 (0,0.5,1.0) | needs the ω channel (0 at f_ω=0) |
| 7 | `wall_width` | `w_pol` = 1,3,3 (0.06,0.12,0.20); `C_pol` scales | sharpest shell (0.06) degrades the read |
| 8 | `N` matched | `w_pol` = **3,3,3** (40,48,56) — N-ROBUST | matched read invariant |
| 8' | `N` default | `C_pol` −1.5e-9, −9.8e-12, −2.6e-13 — **N-COLLAPSE** | the A46 CLIP (§2) |
| 9 | `K3` stop-time | `w_pol` 3→1→1→1 (200,907,1800,3200) | the decoherence (§4) |
| 11 | `frac` (full) | `w_pol` ≡ 0/floor-graze (1,0,0,1) across {0.30,0.60,0.85,0.95}; `E_V^cons` 1.5→16.6 | no winding at any saturation depth (full swamp, §5) |

**§210 deviation (stated):** the §5 sweeps run at n_build=200 (the fresh deposit) rather than the full 3200 — the headline ISO-MAIN + the K3 sweep carry the full-build decoherence; the per-knob sweeps establish the fresh-deposit invariances (magnitude-scaling vs verdict-invariance) at lower cost. No bin depends on a sweep being at full build (the decoherence is the K3 axis, executed at full build).

---

## 8. THE §2.4 PLUMBER-PHYSICAL FLAG — RESOLVED IN THE AM-CONSERVING DIRECTION (surfaced to Grant, not self-adjudicated)

The prereg's one plumber-physical question (the chiral-mirror AM over-constraint: a net-swirl deposit the lock bleeds vs a zero-net-swirl poloidal ripple the lock ignores) is answered by the build: **the channels SEPARATE.** The photon's mechanical axial AM goes to the rigid mode (lock-drained: `L_ω,axial(MAIN−OFF) = −3.61e-5`, the v6 number), and its HELICITY is imprinted as the surviving zero-net-axial-AM poloidal content (`C_pol = −1.74e-4`, lock-immune, helicity-odd). The AM ledger closes 1:1 by construction (`ratio = 1.000000000`) and the wall stays passive (`E_absorbed = +0.542 ≥ 0`).

**The open framing question for Grant (NOT self-resolved):** the engine keeps the rigid component carrying the full extracted `δL` at *all* `alpha_pol` (so axial-AM conservation is strictly honest — no AM routed to a sink), and the poloidal winding is an INDEPENDENT helicity imprint (amplitude ∝ `alpha_pol·Ω_ω·pol_r`). This DEVIATES from the prereg §2.4 `alpha_pol` semantics (where α_pol=1 was meant to route the axial AM to a sink). **Which is the physical chiral-mirror torque — (a) a pure poloidal ripple with the axial AM dumped to a passive sink (the prereg's S-poloidal), or (b) the rigid axial-AM transfer + an independent helicity-imprinted poloidal winding (the build's choice)?** The empirical verdict (DEPOSIT-SURVIVES-NO-QUANTIZATION) does not depend on this — but the physical interpretation of "what the chiral mirror does per bounce" does. Surfaced for adjudication.

---

## 9. HONEST CAVEATS

1. **The matched `pol_R` is a CHOICE, not field-derived** (§2) — the spherical pocket has no major radius. The de-novo `w_pol = q_dep` read requires choosing a torus that brackets the shell AND clears the r ≥ 3 floor; the default `pol_R ∝ N` does not, and N-collapses. The survival conclusion is choice-robust; the winding read is not.
2. **The de-novo `w_pol` reads back the deposit** (tracks `q_dep`) — it is consistency-class, not an emergent topological `(2,3)`. A genuine electron winding would be `(2,3)`-fixed regardless of `q_dep`.
3. **The winding does not survive the build** (decoheres 3→1 by step 907) NOR the full assembly (swamped to 0). The lock-surviving quantity is the `C_pol` *content*, not the integer *order*.
4. **The full-assembly `C_pol` is buckle-contaminated** (OFF/achiral `~−4e-3` >> MAIN `+4e-5`) — the v6 DEMOTION-2 carry-forward; the transducer's own poloidal deposit is not isolable above the buckle there.
5. **`chi_exch=0.08` reads `w_pol=2`** (not 3) and `wall_width=0.06` reads `w_pol=1` — the read has O(1) sensitivity to the strongest-coupling / sharpest-shell edges of the grids; the central grid is `w_pol=3`.

---

## 10. CORPUS STATE + LANE DISCIPLINE

- **OPEN → DEPOSIT-SURVIVES-NO-QUANTIZATION (a clean, mechanism-named partial).** v7 does NOT promote an electron claim and does NOT reopen NOT-ELECTRON (v5). It tested ONE structural hypothesis (the v6 deposit-geometry block) and ANSWERED it: the block WAS the lock-drain of the rigid mode, and the quadrature geometry RESOLVES it (D14 confirmed) — but quantization needs two further closures it does not supply (no topological lock-in; column/buckle dominance). Rule 11: clean negative on the quantization question, named mechanism, branch closes on the named closures. NO debugging toward a rescue, NO `alpha_pol` tuning to force a lock, NO post-hoc bin-criterion drop.
- **Rule 12:** v7 is the structural-block hypothesis's OWN chain (this prereg + result). It does NOT refill the v6 slot; the v6 DEMOTED-PARTIAL + v5 NOT-ELECTRON / SNAP-LOCKED 🔴 demotions stand UNCHANGED.
- **A44 (missing-axiom vs engine-bug):** the diagnosis is engine coupling-family / closure (the two named closures), NOT a missing axiom — **no Ax-5 candidate drafted** (lane discipline).
- **Lane discipline:** this result SURFACES the empirical finding (incl. the A46 smoke-headline flag §2, the §2.4 AM-conservation flag §8). The auditor lands any manual / manuscript / `COLLABORATION_NOTES` entry; the §2.4 framing question is for Grant. This doc does NOT draft those.
- **The PHASE-2 smoke result (`QUADRATURE-LIVE`) is SUPERSEDED on its headline `C_pol` number** (§2, the A46 N-collapse) but CONFIRMED on its survival/discriminator CONCLUSION (D14). The smoke's gate verdict stands as a smoke gate; the production numbers and the quantization answer are this doc's.

---

*Run executed on worktree `/tmp/ave-v7` (branch `analysis/2026-06-10-genesis-v7-quadrature`, off `d11b0923`). `make verify` PASS this session. Engine + keepers FROZEN at the PHASE-2 commit `09d47e45` (no engine/test change in PHASE 3 — run + result only). Every number read FROM `2026-06-10_genesis-v7-quadrature-run_results.json` (ave-driver-script-honesty). verify-before-cite: every engine/v6 anchor grep/line/JSON-confirmed this session.*

---

## 11. DEMOTION ADDENDUM (2026-06-10) — 🔴 RE-BINNED to DEPOSIT-DRAINED-AGAIN; §§0–10 PRESERVED UNCHANGED (Rule 12 / KEEP-BOTH)

**This addendum RE-BINS the §1 verdict. Per Rule 12 the bodies of §§0–10 are preserved verbatim; the frozen prereg (`d4b4af4b`) is untouched. Every number below was re-verified against `research/2026-06-10_genesis-v7-quadrature-run_results.json` and `src/scripts/vol_1_foundations/genesis_v7_quadrature_run.py` this session (verify-before-cite).**

**(a) RE-BIN: DEPOSIT-SURVIVES-NO-QUANTIZATION → DEPOSIT-DRAINED-AGAIN, on the prereg's OWN frozen gate.** The frozen §6 / F-NETFIELD survival gate (`prereg:147,183-184`): the net-field poloidal deposit SURVIVES iff its **gap to the accumulator is ≲ 1 OOM**; a ≈4-OOM gap is DEPOSIT-DRAINED-AGAIN (the v6 band). **The driver NEVER COMPUTED this gate** — it appears only in the `analyze()` docstring (`genesis_v7_quadrature_run.py:388`; `grep -i netfield` over the driver returns that line ONLY), with no executable assertion. Computed here from the raw JSON, the gate **FAILS in both configs**:
- **ISO:** `pol_deposit_accum = 0.3783` vs `|C_pol| = 1.741e-4` → **3.34 OOM**.
- **FULL:** `pol_deposit_accum = 0.4403` vs `|C_pol| = 4.116e-5` → **4.03 OOM** (squarely the prereg's ≈4-OOM v6 DRAINED band).

Neither clears the ≲1-OOM survival threshold. **On the frozen gate the verdict is DEPOSIT-DRAINED-AGAIN.** The §1 "D14 SURVIVES (not DEPOSIT-DRAINED-AGAIN)" line is superseded.

**(b) RULE-11 DEVIATION DECLARED + KEEP-BOTH.** The run silently substituted a lock-**ON/OFF field-to-field** survival criterion (`C_pol(ON)/C_pol(OFF) = 1.000000`, η-flat at −1.6758e-4 across `lock_eta ∈ {0, 0.05, 0.08, 0.12}`) for the frozen gap-to-accumulator gate, without registering the deviation (a Rule-11 criterion swap). It is now REGISTERED as a deviation. Per KEEP-BOTH it stands as a **NEW axis ALONGSIDE the frozen gate (not replacing it)** — and **on that new axis the lock IS exonerated**: the lock cannot drain a zero-net-L poloidal mode (`C_pol` identical ON/OFF, η-independent). Both axes are now on the record: frozen gap-to-accumulator gate → DRAINED (a); ON/OFF field-to-field axis → lock-blind (exonerated). They measure different quantities and the result must carry both.

**(c) RETRACT "§210 FULL / every mandated sweep executed."** §7's title sentence ("§210-COMPLIANCE — every mandated §5 sweep executed") is RETRACTED: the **mandated `ν_art` sweep (prereg §5 row 10, {1e-4, 5e-4, 1e-3, 2e-3, 5e-3}, 50× span)** was NEVER RUN — `nu_art` is pinned at `5e-4` in every arm (`make_cfg` default, `genesis_v7_quadrature_run.py:151`,`156`) and is absent from all 11 swept axes (the §7 table runs rows 1–9 + 11; **row 10 is missing**; the JSON `sweeps` keys carry no `nu_art` axis). Because §5 row 10 is the sweep that separates a physical lock-survival from an `ν_art`-tracked apparatus drift (and §3.5(3) explicitly leans on the ν_art-invariant non-lock-sink level), **the surviving lock-blindness lemma (e) is CLIP pending that sweep.**

**(d) D13 FIDELITY: the implemented deposit DEVIATED from the frozen §3.3/§2.4 definition — the D13 hypothesis was NEVER TESTED.** The frozen deposit (`prereg §3.3`, the α_pol=1 "S-poloidal" of §2.4) routes the **photon's own extracted δL into the poloidal quadrature** ("the axial AM is depleted into the passive sink rather than transferred as net swirl... the photon's HELICITY is imprinted", `prereg:66`). The engine did NOT do this: per the doc's own §8, the rigid component kept carrying the **full** extracted δL at *every* α_pol, so the photon's spin was still deposited **RIGID** — still lock-drained (~724×: ISO-rigid `L_ω,axial` +3.27e-4 lock-ON vs −0.2368 lock-OFF), reproducing v6's −3.61e-5 net field **exactly**. The surviving poloidal content was a **separately-added, energy-budget-sourced helicity imprint** (amplitude ∝ α_pol·Ω_ω·pol_r, §8), NOT the photon's δL. **State plainly: the D13 hypothesis — route the photon's OWN spin into the poloidal quadrature — was never tested.** What ran was the v6 rigid δL-transfer (unchanged) + an independent decorative poloidal ripple.

**(e) STRUCTURAL-BLOCK HYPOTHESIS: NOT CONFIRMED.** The v6 rigid residual stands UNCHANGED (−3.61e-5, byte-inherited). §3's "structural-block hypothesis CONFIRMED" headline is withdrawn. The narrow surviving lemma — **`_lock_relax` drains only net-L rigid modes and is blind to zero-net-L poloidal L-states** (the K-LOCK-PRESERVES substep keeper: a planted rigid net-L contracts by exactly (1−η); a planted poloidal-mode norm is preserved > 0.999) — is **consistency-class** and **CLIP pending the (c) ν_art sweep**. It establishes that the lock *would* preserve a true poloidal deposit; it does NOT establish that the v7 run *made* one (d), nor that the accumulator-gap is a lock drain rather than instrumental (f).

**(f) THE SINK-ATTRIBUTION OBLIGATION (outstanding).** The prereg requires the DRAINED bin to NAME the sink (`prereg:56,184`). Candidates, with the evidence in hand — but the decomposition NOT YET RUN:
- **A46 read-coordinate dilution (the leading candidate).** `pol_R` is a CHOSEN coordinate; the genesis pocket is a **SPHERE** (ρ ∈ [0.71, 2.55], filled center, `pocket_cells = 0`, §2) with **no major radius — the A46 obstruction**. The deposit-default read N-collapses (§2: ~7 OOM over N=28→56; run-internal **3.77 OOM** over N=40→56). So the accumulator→field gap **may be substantially instrumental** (the field number is read at a torus that misses the spherical shell), not a physical drain.
- **LC dephasing.** The deposited `w_pol = 3` decoheres **3 → 1 within one LC quarter-period (~907 steps)** (§4 K3 series) — a real loss of deposited content into the tank, independent of the lock.
- **damping / PML** (the §3.5(3) non-lock sinks).

The gap of (a) is some sum of these; **the decomposition was never run.** Named as the follow-up (own prereg, Rule 12).

**(g) WHAT STANDS (unchanged from §§0–10).** `w_pol ≡ 0` de novo in the full assembly (floor-calibrated, plant-at-scale; the lone achiral `w_pol = 1` floor-grazer = the v6 artifact reproduced); the ISO fresh-deposit reads (`w_pol = q_dep` for q ∈ {2,3,4}) = **consistency-class** (reads back the deposited q in the deposit's own matched coordinate; helicity-odd; N-robust at matched `pol_R`; decohering); T1 UNBROKEN in every arm (`E_V^cons` **12.87–12.93**, drift < 1%); AM ledger **1.000000000**; the v6 rigid residual byte-inherited at **−3.61e-5**. **Net: not an electron, and not measurably closer than v6.**

**(h) PROCESS LESSON (skill queue — the auditor lands any entry).** A frozen gate that exists only as a DOCSTRING is not a gate. The F-NETFIELD survival gate — the single headline discriminator of this prereg — lived only in the `analyze()` docstring (`genesis_v7_quadrature_run.py:388`) and was never computed or asserted, which let the run report SURVIVES on a substituted criterion (b) while the frozen gate FAILED (a). **Every prereg gate must have an executable assertion in the driver** (the "gate-as-comment" failure class).

**FINAL BIN (this addendum): 🔴 DEPOSIT-DRAINED-AGAIN, sink unattributed (f) — the structural-block hypothesis is NOT confirmed; the v6 residual is unchanged.** The §1 DEPOSIT-SURVIVES-NO-QUANTIZATION bin is RE-BINNED. NOT-ELECTRON (v5) stays closed; the v6 DEMOTED-PARTIAL stands; v7 closes as DRAINED-AGAIN with three carried follow-ups, each its OWN prereg (Rule 12, no slot refilled): (1) the sink-attribution decomposition (f), (2) the mandated `ν_art` sweep (c), (3) a faithful D13 deposit that actually routes the photon's δL into the quadrature (d). A44: still an engine coupling-family / instrumentation gap, NOT a missing axiom — no Ax-5 drafted (lane discipline; the auditor lands any manual/manuscript entry).

*Addendum numbers re-verified against `2026-06-10_genesis-v7-quadrature-run_results.json` + `genesis_v7_quadrature_run.py` this session (verify-before-cite). §§0–10 and the frozen prereg `d4b4af4b` preserved unchanged (Rule 12).*
