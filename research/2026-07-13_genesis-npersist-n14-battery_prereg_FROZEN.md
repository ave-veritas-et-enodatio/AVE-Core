# Genesis N≥14 persistence battery (G-PERSIST gate) — FROZEN prereg

**Freeze discipline.** This prereg is frozen **by push** as its own commit **BEFORE**
the driver runs — the freeze commit precedes the first driver commit in git history
(model: `research/2026-07-12_remanence-r10-fixed-n_prereg_FROZEN.md`, freeze-first;
ave-prereg v1.7 Step 3.11). No driver output lands against an unpushed prereg.
**Frozen bins enforce; flags don't.**

**Handoff.** `_orchestration/2026-07-13_genesis-npersist-battery-handoff.md` (Grant GO
2026-07-13). This battery is the number on which **G-PERSIST's ruling confirmation
waits** (★PROPOSED-RULED, docket-gated — `_orchestration/2026-07-10_rulings-docket.md`
G-PERSIST row; ruling leaf `_orchestration/2026-07-12_ave-native-rulings_g-persist_x-ledger.md`).

**Class.** Satellite-session driver re-run (self-contained). LOOP GAP rank-4 persistence
read on the existing Rule-14 carrier `loop_gap_harness` on `VacuumEngine3D`. **No new
engine, no fourth engine, no `genesis_v{N}`, no srs v18+, no graph-growth, no retune** —
the same #655 D2 battery, **only N and the boundary condition change**.

**Firewall.** Fork **(B)** node-birth (N→N+1) stays **closed**. This battery reads **(A)
fixed-N only**. Bin (ii) does **not** select (B).

---

## Sector header (mandatory)

- **MODE** = driven genesis on the saturable K4⊗Cosserat lattice, **fixed-\(N\)** (no node
  birth). Carrier = `run_loop_gap_probe` rank 4 (impedance Γ=−1 wall + trilinear
  converter + memristive saturation), `bulk_density_on=True`, `front_target=A_YIELD`.
- **REGIME** = at/above-yield launch (`n_drive_mult=0.5`), then anhysteretic quiet-window
  relaxation (`n_quiet_mult=1.5`).
- **PHASE-STATE** = seed a localized dilatation / topological structure, de-energize,
  measure whether it **keeps** — a **medium memory / remanence** read, **not** a mint probe.
- **Instrument** = frozen #655 P11 detector: `E_persist = H_end/H_drive`,
  `φ_persist = Φ_link²_end / Φ_link²_drive`, measured on the PML-excluded interior
  (`_interior_mask`), aggregated by `snapshot_op14` — **byte-unchanged detector**.
- **consistency-vs-emergence** = FIREABLE pattern persistence + boundary ablation. Refuse
  EMERGENCE-as-electron from a PASS alone; a PASS supports (A) *pattern viability*, not
  electron genesis.

---

## Corpus sweep (STEP-0)

| Prior | Finding (grep-verified 2026-07-13) |
|---|---|
| `_orchestration/2026-07-12_genesis-node-birth-fork.md:16-19` | #655 re-adjudication, **per-fidelity SPLIT** at N=10: SMOKE 2/3 → (i) A-SUPPORTED; PRODUCTION 0/3 → (ii) A-WEAKENED |
| same `:31-35` | **Confound:** both N=10 bins boundary-confounded (interior 4³ inside 3-cell PML); `E_persist` recovers **0.6929→0.7984→0.8449** as N 10→12→14 (interior 4³→6³→8³); production E-collapse **ARTIFACT-LEANING** (PML leakage, not bulk dissipation); **N≥14 / closed-box owed** before banking either bin |
| `ave.core.genesis_v18_coupled` | Floors `P11_E_PERSIST_MIN=0.85`, `P11_A_PERSIST_MIN=0.80` (frozen) |
| `ave.core.loop_gap_harness.run_loop_gap_probe` | Carrier exists; boundary set by `EngineConfig.pml` (base=3). Detector `snapshot_op14` measures over `_interior_mask` (PML-excluded) |
| `ave.core.bulk_rarefaction_sector.build_pml_damping` / `k4_tlm` / `cosserat_field_3d` | `pml≤0` ⇒ all-ones mask ⇒ **no absorber ⇒ fully reflecting closed box**; `pml=3` ⇒ absorbing shell |
| `research/2026-07-12_remanence-r10-fixed-n_CHARTER.md` | R10 anhysteretic-kernel zero-loop-area fact is **corpus-standing regardless** of this battery |

**Mechanism note (pre-registered, verified by 2-step engine probe 2026-07-13):** at N=10
`pml=3` interior = 4³=64 sites and `H` drops 5.819→5.578 over 2 steps (absorber leakage
visible); at `pml=0` interior = 1000 sites and `H` holds 5.819→5.821 (conserved). **`pml=0`
removes only the PML absorber (the boundary leak); the physical memristive + impedance-wall
dynamics remain** — so closed-box `E_persist` is a meaningful bulk+wall persistence read,
**not** a trivial energy-conservation identity.

---

## Mission (frozen)

Re-run the #655 D2 persistence battery at **N ≥ 14 AND closed-box**, for **all 3 landed
seed modes** × **both fidelities** × **both boundaries**, reporting `E_persist` and
`φ_persist` per **mode × fidelity × boundary × N** at **matched N**.

**Cells (frozen grid — 24 legs):**

| axis | values |
|---|---|
| seed mode | `pair`, `graded_a0`, `photon_lock` (LANDED_SEED_MODES) |
| fidelity | smoke (`fast=True`, n_quiet≈12) · production (`fast=False`, n_quiet≈52) |
| boundary | **PML** (`pml=3`, banked) · **closed-box** (`pml=0`, reflecting) |
| N | 10 (reproduction anchor, PML-only) · **14 (primary matched-N)** · 16 (box-size robustness) |

- **N=10 × PML × {smoke, production} × 3 modes = 6** — reproduction anchor. Must reproduce
  the banked SMOKE 0.8639/0.8544/(photon_lock fail) and PRODUCTION 0.6929/0.6764/0.7750
  **before** the N≥14 numbers are trusted (live-fire validation gate).
- **N=14 × {PML, closed-box} × {smoke, production} × 3 modes = 12** — the primary battery.
- **N=16 × {PML, closed-box} × production × 3 modes = 6** — PML N-trend endpoint +
  closed-box reflection-recurrence robustness (guards a box-size artifact in the closed
  read).

Carrier change is **exactly two knobs**: `N` and `pml`. Everything else (`rank_target=4`,
`seed_mode`, `bulk_density_on=True`, `front_target=A_YIELD`, `n_drive_mult=0.5`,
`n_quiet_mult=1.5`, all thresholds, the detector) is **byte-identical** to the banked #655 D2.

---

## Detector (FROZEN — byte-unchanged)

A cell **persists** iff **both** frozen floors clear:
```
E_persist ≥ 0.85   AND   φ_persist ≥ 0.80
```
`E_persist = H_end / H_drive`; `φ_persist = Φ_link²_end / Φ_link²_drive`; both from
`snapshot_op14` over the PML-excluded interior. This is the #655 P11 gate, unchanged.

**Detector-substitution rule (binding).** Any post-freeze detector change (e.g. adding a
core-localization fraction to guard the closed-box "sloshing reflecting box" false
positive) must be **REBINNED on this frozen axis with the new detector added as a NEW axis
(KEEP-BOTH)** — **never silently swapped** for `E_persist/φ_persist`.

---

## Frozen bins — per-fidelity, KEEP-BOTH on the #655 axes

Scored **separately for smoke and production** (the N=10 split is real; do not collapse
fidelities). Preserve the frozen #655 per-fidelity bins:

| bin | criterion (per fidelity) | meaning |
|---|---|---|
| **(i) A-SUPPORTED** | persistence PASS (E≥0.85 ∧ φ≥0.80) on **≥1** landed seed mode | (A) viable for pattern; (B) not forced; R10 still open |
| **(ii) A-WEAKENED** | persistence FAIL on **all 3** landed modes | fixed-N pattern insufficient for lasting localization on this battery; does **not** select (B) |

---

## Boundary-artifact axis (NEW — first-class discriminator, KEEP-BOTH)

Added alongside the frozen bins, **not** replacing them. At **matched N** (=14 primary;
=16 corroboration), compare **closed-box vs PML** on `E_persist` per mode × fidelity:

| boundary-axis outcome | reading |
|---|---|
| **RECOVERS** | closed-box `E_persist` clears 0.85 (∧ φ≥0.80) where PML fails, at matched N | production E-collapse was **PML absorber leakage** ⇒ bin (i)-leaning boundary-clean |
| **HOLDS-FAIL** | closed-box `E_persist` **still** < 0.85 (or φ<0.80) with the absorber removed | collapse is **genuine bulk/wall dissipation** ⇒ bin (ii) A-WEAKENED holds boundary-clean |
| **RECURRENCE-CONFOUND** | closed-box result is itself N-dependent (N=14 vs N=16 disagree) | reflecting-box recurrence artifact; report as unresolved, do not bank |

The primary adjudication cell is **N=14, production, closed-box vs PML** — the direct test
of whether the banked production collapse was absorber leakage.

---

## Outcome map (frozen — from handoff)

- **(i) A-SUPPORTED boundary-clean** (persistence clears at N≥14 / closed-box on ≥1 mode):
  **G-PERSIST as drafted is MOOT**; the **remanence-before-node-mint build-order directive
  loses its banked-fact basis** (it was banked on the N=10 A-WEAKENED read). **Carve:** the
  **R10 remanence question stays OPEN on independent grounds** — the anhysteretic-kernel
  zero-loop-area fact is corpus-standing regardless
  (`research/2026-07-12_remanence-r10-fixed-n_CHARTER.md` Ax3 carve). A-SUPPORTED retires
  the *build-order directive*, not the remanence charter.
- **(ii) A-WEAKENED holds boundary-clean** (persistence still fails once the absorber
  confound is removed): **G-PERSIST confirms** — fixed-\(N\) pattern is insufficient for
  lasting localization on this battery; remanence-before-node-mint stands on a
  boundary-clean fact.
- **Either way:** bin (ii) does **not** select (B). Node-mint stays firewalled; this
  battery reads (A) fixed-\(N\) only.

---

## Adversarial sabotage plant (pre-registered — discipline (c))

The negative-control plant must corrupt an **evolved** field observable
(`E_persist`/`φ_persist` after real quiet-window evolution) — **not** a post-hoc arithmetic
reduction. Pre-registered plant: inject a small persistent forcing / disable the drive-off
(so energy is externally sustained) and confirm the detector then **falsely reports PASS**;
a plant that only rescales the printed ratio is **not** a valid check and is rejected.

---

## Deliverables after this freeze push

1. This FROZEN prereg (this commit, pushed first).
2. `pml` boundary passthrough on `run_loop_gap_probe` (the authorized boundary knob;
   default preserves base `pml=3` — no behavior change when unset) + battery driver
   `src/scripts/vol_1_foundations/genesis_npersist_battery.py`.
3. Battery run → per-cell JSON under `assets/sim_outputs/`.
4. RESULT doc `research/2026-07-13_genesis-npersist-n14-battery_RESULT.md` (per-fidelity
   bins + boundary-axis adjudication + outcome-map application).
5. Adversarial PR review (scriptPath wrapper) + PR `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.

---

## Out of scope

- Any (B) node-birth / graph-growth / `genesis_v{N}` / srs v18+ code.
- Retuning thresholds, seed amplitudes, drive/quiet multipliers, or the detector.
- Claiming electron genesis / mass from a persistence PASS (EMERGENCE-as-electron refused).
- Re-litigating mass=A1 (#260/#311) or the R10 remanence charter's independent status.

---

## ERRATUM 2026-07-13 (post-result — frozen body above is BYTE-UNTOUCHED)

Dated erratum appended after the run, per the x40 / remanence amendment pattern. The frozen
prereg body above is left **byte-for-byte unchanged**; these corrections record where the data
**refuted a frozen expectation** (pre-registration working as designed) and where the frozen
prose mis-read its own mechanism probe. Raised by the adversarial review of PR #670
(5/5 findings confirmed on verify). **None affects the RESULT's banked conclusion** — the
G-PERSIST recommendation rests on the boundary-insensitive φ-dispersion trend, not on any of
the items below. The RESULT
(`research/2026-07-13_genesis-npersist-n14-battery_RESULT.md`) **supersedes** the frozen
expectations here.

1. **The Corpus-sweep mechanism note (frozen, "Mechanism note … `pml=0` … closed-box
   `E_persist` is a meaningful bulk+wall persistence read, **not** a trivial
   energy-conservation identity") is REFUTED by the data.** Closed-box `E_persist` ≡ **1.0000**
   *mode-independently* (pair, graded_a0, **and** the structure-dead photon_lock which
   localizes nothing) at N=14 and N=16 ⇒ it **is** a conservation identity (a reflecting box
   retains all energy independent of localization). The frozen 2-step probe (H 5.819→5.821,
   "conserved") in fact **demonstrated** the identity while the prose denied it — an internal
   self-contradiction. Consequence: the **boundary-artifact axis's E-channel discriminator is
   vacuous** (its PASS condition `E≥0.85` cannot fail in the closed box), and the frozen
   "RECOVERS" row is **non-fireable-against** on the E-channel.

2. **The φ ≥ 0.80 floor is one-sided.** It was written to detect *retention* (φ ≈ 1) but is a
   *lower bound*, so closed-box runaway growth (φ ≈ 10×) trivially clears it. In the closed
   box **both** detector channels are degenerate false-positives; the closed-box bin (i)
   A-SUPPORTED carries **zero discriminating power**.

3. **Outcome-map phrasing "(ii) A-WEAKENED holds boundary-clean" is imprecise.** Neither
   boundary is clean (absorber under-counts via leakage; reflector over-counts via
   retention/mode-growth). The boundary-**insensitive** signal is the *cross-N φ-dispersion
   trend* under PML; read the outcome map as "(ii) is supported by the boundary-insensitive
   trend," not "(ii) is a boundary-clean bin."

4. **Sabotage-plant scope.** The plant re-injects the seed, which **clobbers φ** (plant_φ → 0),
   so under the frozen "detector falsely PASSes" criterion `plant_false_pass` is **False for
   every plant** — the plant does **not** achieve a false PASS. It establishes only that the
   **E-channel** is integrator-coupled (plant_E ≫ free_E); the load-bearing **φ-channel is not
   exercised**. A φ-channel negative control (sustain φ without clobbering the Cosserat state)
   is a follow-on.
