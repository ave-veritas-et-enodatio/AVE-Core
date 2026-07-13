# Handoff brief — Genesis N≥14 persistence battery (the G-PERSIST gate)

**Date:** 2026-07-13 · **Grant GO:** 2026-07-13 · **Class:** satellite-session driver run
(self-contained). **Gate:** this battery is the number on which **G-PERSIST's ruling
confirmation waits** (G-PERSIST stays **★PROPOSED-RULED**, docket-gated on this outcome —
`_orchestration/2026-07-10_rulings-docket.md` G-PERSIST row; ruling leaf
`_orchestration/2026-07-12_ave-native-rulings_g-persist_x-ledger.md`).

**Sector header (mandatory).** MODE: driven genesis on the saturable K4 lattice, fixed-\(N\)
(no node birth — (B) stays firewalled). REGIME: at/above-yield launch, then anhysteretic
quiet-window relaxation. PHASE-STATE: seed a localized dilatation/topological structure,
de-energize, measure whether it **keeps**. This is a **medium memory / remanence** read, not
a mint probe.

---

## Mission

Re-run the **#655 genesis persistence battery** at **N ≥ 14 AND closed-box**, for **all 3
landed seed modes** (`pair` / `graded_a0` / `photon_lock`) × **both fidelities** (smoke
`n_quiet=12`, production `n_quiet=52`). Report `E_persist` and `φ_persist` per mode × fidelity
× boundary (closed-box vs PML) × N, at matched N.

The #655 re-adjudication left a **per-fidelity SPLIT** at N=10 — smoke **2/3 → bin (i)
A-SUPPORTED**, production **0/3 → bin (ii) A-WEAKENED** — but **both N=10 bins are
boundary-confounded** and ruling-grade banking was **DEFERRED to Grant** pending exactly this
re-run (`_orchestration/2026-07-12_genesis-node-birth-fork.md:3,16-19,31-36`). This battery
converts the deferred read into a boundary-clean one.

---

## Why (the banked confound)

Both N=10 bins sat inside the absorber. Verified against the merged #655 re-adjudication doc
`_orchestration/2026-07-12_genesis-node-birth-fork.md`:

- **SMOKE (`n_quiet=12`): 2/3 persist** — `pair` (E=0.8639), `graded_a0` (E=0.8544);
  `photon_lock` FAILs (φ-channel dead) ⇒ bin (i) A-SUPPORTED (`:16-17`).
- **PRODUCTION (`n_quiet=52`): 0/3 persist** — `pair`→0.6929, `graded_a0`→0.6764,
  `photon_lock`→0.7750, every mode below the 0.85 floor ⇒ bin (ii) A-WEAKENED (`:18-19`).
- **The confound:** an N-sweep (pair, production, PML fixed at 3) shows `E_persist` recovers
  **monotonically 0.6929 → 0.7984 → 0.8449 as N goes 10 → 12 → 14** (interior 4³ → 6³ → 8³).
  The production E-collapse is **substantially PML boundary leakage, not bulk dissipation**
  (ARTIFACT-LEANING); at N=10 the packet sat inside the 3-cell absorber with only a 4³ interior
  (`:31-35`). A clean adjudication needs **N ≥ 14 / closed-box** before banking either bin
  (`:35`).

The recovery trend is the whole reason this is a gate and not a ruling: neither N=10 fidelity
is a clean read.

---

## Discipline (verbatim-class — binding)

**(a) Freeze-by-push.** The prereg is **FROZEN AS ITS OWN COMMIT, PUSHED BEFORE the driver
runs** — the freeze commit precedes the first driver commit in git history (model on
`research/2026-07-12_remanence-r10-fixed-n_prereg_FROZEN.md`, freeze-first). No driver output
lands against an unpushed prereg.

**(b) Bins — KEEP-BOTH on the FROZEN #655 axes, per-fidelity, plus a first-class
boundary-artifact axis.** Preserve the frozen #655 per-fidelity bins: **(i) A-SUPPORTED /
(ii) A-WEAKENED**, scored **separately for smoke and production** (the split is real; do not
collapse the fidelities). ADD, as a **first-class discriminator axis**, the
**boundary-artifact axis: closed-box vs PML at matched N** — the direct test of whether the
production collapse was absorber leakage. Any **post-freeze detector substitution must be
REBINNED on the frozen axis** with the new detector **added as a NEW axis (KEEP-BOTH)**,
**never silently swapped** for the frozen detector.

**(c) Sabotage plants act on EVOLVED observables, not arithmetic-only.** A plant that only
perturbs a post-hoc arithmetic reduction is not a valid adversarial check here — the plant must
corrupt an **evolved** field observable (`E_persist` / `φ_persist` after real quiet-window
evolution) so the detector is exercised on the integrator's output, not on a spreadsheet.

**(d) Adversarial review wrapper (do not use the named-workflow args path).** When invoking the
adversarial-review workflow, **ALWAYS** use a `scriptPath` wrapper script that inlines ARGS and
calls:

```
workflow({scriptPath: '.claude/workflows/ave-adversarial-pr-review.js'}, ARGS)
```

The **named-workflow args path silently drops args** — use the `scriptPath` wrapper every time.

**(e) Carrier = the existing genesis driver.** No new engine class, no fourth engine, **no
retune** — the same `#655` genesis driver, only N and the boundary condition change. (Firewall:
this is not a `genesis_v{N}` / graph-growth probe; (B) node-birth stays closed per G-PERSIST.)

**(f) DO-NOT-MERGE.** PR opens `[DO-NOT-MERGE]`; **only Grant merges.**

---

## Outcome map

- **If the battery re-adjudicates to (i) A-SUPPORTED** (boundary-clean persistence at
  N ≥ 14 / closed-box): **G-PERSIST as drafted is MOOT**, and the
  **remanence-before-node-mint build-order directive loses its banked-fact basis** (that
  directive was banked on the N=10 A-WEAKENED read). **Note the carve:** the **R10 remanence
  question stays OPEN on independent grounds** — the **anhysteretic-kernel zero-loop-area fact
  is corpus-standing regardless** (`research/2026-07-12_remanence-r10-fixed-n_CHARTER.md` Ax3
  carve). A-SUPPORTED retires the *build-order directive*, not the remanence charter.
- **If (ii) A-WEAKENED holds boundary-clean** (persistence still fails once the absorber
  confound is removed): **G-PERSIST confirms** — fixed-\(N\) pattern is insufficient for lasting
  localization on this battery, and remanence-before-node-mint stands on a boundary-clean fact.

Either way: **bin (ii) does not select (B)** — node-mint stays firewalled; this battery reads
(A) fixed-\(N\) only.

---

## References (grep-verified anchors — 2026-07-13, at this PR's base d0037d8f)

- `_orchestration/2026-07-12_genesis-node-birth-fork.md:3,16-19,31-36` — the merged #655
  re-adjudication: per-fidelity split (smoke 2/3, production 0/3); E_persist recovery
  0.6929→0.7984→0.8449 as N 10→12→14; interior 4³; PML fixed at 3; N≥14/closed-box owed.
- `_orchestration/2026-07-10_rulings-docket.md` G-PERSIST row — ★PROPOSED-RULED, confirmation
  postdates this re-run.
- `_orchestration/2026-07-12_ave-native-rulings_g-persist_x-ledger.md:32-43` — G-PERSIST ruling
  + ★FOUNDATION UNDER RE-ADJUDICATION note + the A-SUPPORTED-moots-the-directive clause.
- `research/2026-07-12_remanence-r10-fixed-n_CHARTER.md` — freeze-by-push pattern; the R10
  anhysteretic-kernel zero-loop-area fact that stands regardless of this battery's outcome.
