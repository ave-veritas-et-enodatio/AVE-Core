# Genesis N≥14 persistence battery (the G-PERSIST gate) — RESULT

**Date:** 2026-07-13 · **Branch:** `analysis/genesis-npersist-n14-battery` ·
**Freeze commit (prereg, pushed before driver):** `19f67662` ·
**FROZEN prereg:** [`2026-07-13_genesis-npersist-n14-battery_prereg_FROZEN.md`](2026-07-13_genesis-npersist-n14-battery_prereg_FROZEN.md) ·
**Handoff:** `_orchestration/2026-07-13_genesis-npersist-battery-handoff.md` ·
**Gate:** G-PERSIST ★PROPOSED-RULED (`_orchestration/2026-07-10_rulings-docket.md` row;
leaf `_orchestration/2026-07-12_ave-native-rulings_g-persist_x-ledger.md`).

**Class:** satellite driver re-run. **Detector byte-unchanged** (E_persist ≥ 0.85 AND
φ_persist ≥ 0.80). Carrier change = exactly two knobs (`N`, `pml`); `pml=0` = reflecting
closed box. **(B) node-birth firewalled — reads (A) fixed-\(N\) only.**

---

## TL;DR (brutal-clarity verdict)

1. **Reproduction is byte-exact.** N=10 PML reproduces banked #655 to the digit — smoke
   0.8639 / 0.8544 / (photon_lock φ-dead), production 0.6929 / 0.6764 / 0.7750. The
   invocation is validated; the whole battery is trustworthy.
2. **The N=10 E-collapse WAS boundary leakage — confirmed.** `E_persist` recovers
   monotonically with N under PML: **0.6929 → 0.8449 → 0.8705** (pair, N 10→14→16; crosses
   0.85 at N=16). The handoff's "ARTIFACT-LEANING" premise on the **E-channel** holds.
3. **But persistence still fails boundary-cleanly — on the *structural* channel.**
   `φ_persist` **collapses and worsens with interior size** under PML: **0.8734 → 0.7266 →
   0.5138** (pair, N 10→14→16). The pattern **disperses more as the interior grows** —
   i.e., persistence fails *worse* where the boundary matters *less*. That is the **opposite**
   of a boundary artifact.
4. **Closed-box "A-SUPPORTED" (2/3) is a reflecting-cavity artifact, not localization.**
   Closed-box `E_persist` ≡ **1.0000** exactly — a conservation identity (a reflecting box
   retains all energy regardless of structure). Closed-box `φ_persist` **runs away to ~10.5×**
   — mode-feeding in the cavity, **not** stable retention (a genuinely persistent structure
   holds φ ≈ 1, not 10×). Both channels of the frozen detector are degenerate here.
5. **The frozen E/φ detector is boundary-degenerate.** The **same** seed at the **same** N
   gives φ that *collapses* under the absorber (0.51) and *explodes* under the reflector (10.5).
   The boundary dominates the observable; the detector cannot read *intrinsic* persistence in
   either boundary. Neither boundary is "clean."
6. **Recommendation — G-PERSIST: lean CONFIRMS (bin (ii) A-WEAKENED).** Precise footing:
   *neither boundary is clean* (§5); the only **boundary-insensitive** signal is the cross-N
   **φ-dispersion trend** under PML, and it supports (ii) — it says the fixed-\(N\)
   pattern does **not** achieve lasting localization; the E-leakage confound is real but does
   **not** rescue persistence. **This flips the handoff's expected outcome** (it expected
   closed-box recovery ⇒ A-SUPPORTED ⇒ G-PERSIST moot). Because the closed-box read is a
   cavity artifact, the *mechanical* RECOVERS→(i) is not load-bearing. **The closed-box
   interpretation is a fork for Grant** (§7); a **boundary-insensitive localization observable**
   (KEEP-BOTH new axis, §9) is required to rule with full confidence.
7. **(B) is not selected either way.** Node-mint stays firewalled.

---

## Sector header (recap)

MODE = driven genesis on the saturable K4⊗Cosserat lattice, **fixed-\(N\)**, rank-4 carrier
(impedance Γ=−1 wall + trilinear converter + memristive saturation), `bulk_density_on`,
`front_target=A_YIELD`. REGIME = at/above-yield launch (`n_drive_mult=0.5`) → anhysteretic
quiet-window relaxation (`n_quiet_mult=1.5`). PHASE-STATE = seed → de-energize → does it keep
(medium memory / remanence, **not** a mint probe). Instrument = frozen #655 P11 detector.

---

## 1 · Reproduction validation (N=10 PML vs banked #655) — byte-exact

| fidelity | mode | E_persist (this run) | E_persist (banked) | φ_persist | match |
|---|---|---|---|---|---|
| smoke | pair | 0.8639 | 0.8639 | 7.7295 | ✓ exact |
| smoke | graded_a0 | 0.8544 | 0.8544 | 1.9636 | ✓ exact |
| smoke | photon_lock | 0.8198 | (φ-dead FAIL) | 0.0000 | ✓ (φ-dead) |
| production | pair | 0.6929 | 0.6929 | 0.8734 | ✓ exact |
| production | graded_a0 | 0.6764 | 0.6764 | 0.8905 | ✓ exact |
| production | photon_lock | 0.7750 | 0.7750 | 0.0000 | ✓ exact |

The `pml=3` default reproduces banked #655 to four decimals ⇒ the added `pml` passthrough
did not perturb the physics; the invocation is identical to the banked D2.

---

## 2 · Full battery — E_persist / φ_persist / persists (E≥0.85 ∧ φ≥0.80)

**Production (n_quiet≈52):**

| mode | N | PML E / φ / pass | closed-box E / φ / pass |
|---|---|---|---|
| pair | 10 | 0.6929 / 0.8734 / ✗ | — |
| pair | 14 | 0.8449 / 0.7266 / ✗ | 1.0000 / 10.5197 / ✓ |
| pair | 16 | 0.8705 / 0.5138 / ✗ | 1.0000 / 9.7134 / ✓ |
| graded_a0 | 10 | 0.6764 / 0.8905 / ✗ | — |
| graded_a0 | 14 | 0.8446 / 0.5826 / ✗ | 1.0000 / 10.4218 / ✓ |
| graded_a0 | 16 | 0.8702 / 0.4997 / ✗ | 1.0000 / 9.2894 / ✓ |
| photon_lock | 10 | 0.7750 / 0.0000 / ✗ | — |
| photon_lock | 14 | 0.9498 / 0.0000 / ✗ | 1.0000 / 0.0000 / ✗ |
| photon_lock | 16 | 0.9647 / 0.0000 / ✗ | 1.0000 / 0.0000 / ✗ |

**Smoke (n_quiet≈12):**

| mode | N | PML E / φ / pass | closed-box E / φ / pass |
|---|---|---|---|
| pair | 10 | 0.8639 / 7.7295 / ✓ | — |
| pair | 14 | 0.9610 / 0.0841 / ✗ | 1.0000 / 2.5117 / ✓ |
| graded_a0 | 10 | 0.8544 / 1.9636 / ✓ | — |
| graded_a0 | 14 | 0.9605 / 0.0990 / ✗ | 1.0000 / 2.5488 / ✓ |
| photon_lock | 10 | 0.8198 / 0.0000 / ✗ | — |
| photon_lock | 14 | 0.9834 / 0.0000 / ✗ | 1.0000 / 0.0000 / ✗ |

(`photon_lock` φ ≡ 0 in every cell — the φ-channel is structurally dead for that seed,
boundary-independent, as banked. Discriminating modes = `pair`, `graded_a0`.)

---

## 3 · Per-fidelity frozen bins (mechanical — prereg §Frozen bins)

| N | boundary | fidelity | n_persist | bin |
|---|---|---|---|---|
| 10 | PML | smoke | 2/3 | (i) A-SUPPORTED |
| 10 | PML | production | 0/3 | (ii) A-WEAKENED |
| 14 | PML | smoke | 0/3 | (ii) A-WEAKENED |
| 14 | PML | production | 0/3 | (ii) A-WEAKENED |
| 14 | closed-box | smoke | 2/3 | (i) A-SUPPORTED |
| 14 | closed-box | production | 2/3 | (i) A-SUPPORTED |
| 16 | PML | production | 0/3 | (ii) A-WEAKENED |
| 16 | closed-box | production | 2/3 | (i) A-SUPPORTED |

---

## 4 · Boundary-artifact axis (closed-box vs PML, matched N)

| N | fidelity | PML bin | closed-box bin | boundary-axis outcome |
|---|---|---|---|---|
| 14 | smoke | (ii) | (i) | **RECOVERS** (mechanical) |
| 14 | production | (ii) | (i) | **RECOVERS** (mechanical) |
| 16 | production | (ii) | (i) | **RECOVERS** (mechanical) |

**Mechanically the frozen detector RECOVERS at N=14 and N=16** (removing the absorber flips
the bin from (ii) to (i) for pair/graded_a0). **Recurrence-confound guard passes:** closed-box
is **N-stable** — the same (i) bin and φ ≈ 10× at both N=14 and N=16 (no N=14-vs-N=16
disagreement), so the closed-box result is a *systematic* boundary effect, not a box-size
recurrence artifact. **§5 explains why this mechanical RECOVERS is not load-bearing.**

---

## 5 · The two-sided confound (the finding)

The re-run does **not** deliver the single "boundary-clean" read the handoff sought, because
**both** boundaries confound the frozen detector — in **opposite** directions:

**PML (absorbing) — E recovers, φ collapses, as N grows (production, pair):**

| N | interior | E_persist | φ_persist |
|---|---|---|---|
| 10 | 4³ | 0.6929 | 0.8734 |
| 14 | 8³ | 0.8449 | 0.7266 |
| 16 | 10³ | 0.8705 | 0.5138 |

- **E-channel recovers** (0.69→0.87): larger interior ⇒ less absorber leakage ⇒ the
  N=10 E-collapse **was** boundary leakage. *Handoff premise confirmed.*
- **φ-channel collapses** (0.87→0.51): larger interior ⇒ the pattern **disperses more**.
  Persistence fails **worse** where the boundary matters **less** — a **boundary-clean**
  signature of genuine structural non-persistence, **not** an artifact.

**Closed-box (reflecting) — both channels degenerate:**
- `E_persist ≡ 1.0000` exactly: a reflecting box conserves total energy identically,
  **independent of localization**. Not a persistence read — a conservation identity.
- `φ_persist` **runs away to ~10×** (production: 10.52 / 10.42 at N=14; 9.71 / 9.29 at N=16
  — **N-stable**, so a *systematic* cavity effect, not a box-size recurrence): the Φ_link²
  observable **grows ~10×** during the quiet window. A persistent bound structure holds
  φ ≈ 1; runaway growth is cavity mode-feeding. (Smoke φ ≈ 2.5 over the shorter quiet window
  ⇒ the growth accumulates with quiet time — a cavity signature, not retention.)

**The φ floor is one-sided (adversarial review finding #2 — CONFIRMED).** `φ_persist ≥ 0.80`
is a **lower bound** — it was designed to detect *retention* (φ ≈ 1). Runaway growth (φ ≈ 10)
sails through it. So in the closed box **both** detector channels are degenerate false-positives:
E clears by conservation identity, φ clears by unbounded growth. The closed-box bin (i)
A-SUPPORTED carries **zero discriminating power**.

**Detector boundary-degeneracy:** the same seed at the same N gives φ = 0.51 (absorber) vs
10.5 (reflector). The boundary dominates the observable. The frozen E/φ detector **cannot
read intrinsic persistence** in either boundary — the handoff's "clean adjudication" is not
achievable with this detector alone. The only boundary-**insensitive** signal in the battery
is the **cross-N φ-dispersion trend under PML** (worsening as the interior grows).

---

## 6 · Adversarial sabotage plant (negative control — prereg §Sabotage plant)

Pre-registered plant: re-inject the seed each quiet step (sustained forcing on the **evolved**
field), read E_persist / φ_persist off the real integrator.

| cell | free_E | plant_E | plant_φ | plant false-PASS (full AND-gate)? |
|---|---|---|---|---|
| N=14 closed pair | 1.0000 | 12.51 | 0.0000 | ✗ |
| N=14 closed graded_a0 | 1.0000 | 13046.1 | 0.0000 | ✗ |
| N=14 PML pair | 0.9610 | 6.47 | 0.0000 | ✗ |
| N=14 closed photon_lock | 1.0000 | 1.0000 | 0.0000 | ✗ |

**Honest scope (adversarial review PR #670, finding #5 — CONFIRMED).** The plant drives
`E_persist` far above the free run (up to **13046×** vs 1.0) ⇒ the **E-channel is exercised on
the integrator output**, not a spreadsheet (discipline (c) satisfied for the E-channel). But
re-injecting the seed **clobbers the Cosserat state and zeroes φ** (`plant_φ` = 0 in every
cell), so under the prereg's own criterion — the **full AND-detector falsely PASSes** —
`plant_false_pass` is **False for all four**; the plant does **not** achieve a false PASS. And
the E-channel it validates is exactly the channel shown degenerate in §5. **The load-bearing
φ-channel is never exercised** (the plant destroys φ rather than sustaining it). A proper
φ-channel negative control (sustain φ *without* clobbering the Cosserat state) is a **follow-on**,
alongside the localization axis (§8). The φ-dispersion conclusion (§5) therefore rests on the
**N-monotonic trend + byte-exact reproduction**, not on this plant.

(The earlier "3/4 valid negative control" label used an E-lift proxy, not the prereg's
false-PASS criterion — corrected here and in the driver.)

---

## 7 · Outcome-map application + G-PERSIST — with the fork for Grant

The mechanical frozen-detector output and the physical reading **disagree**, and the
disagreement is exactly the closed-box interpretation:

- **Reading A (mechanical / handoff-literal):** boundary axis RECOVERS at N=14 ⇒ (i)
  A-SUPPORTED boundary-clean ⇒ **G-PERSIST as drafted is MOOT**; the
  remanence-before-node-mint **build-order directive** loses its banked basis. (R10 charter
  stays open independently — anhysteretic zero-loop-area fact.)
- **Reading B (physical / evidence-weighted — recommended):** the closed-box PASS is a
  reflecting-cavity artifact (E≡1.0 identity + φ runaway to 10×), so the RECOVERS is not a
  real localization recovery. The only boundary-**insensitive** signal — φ-dispersion
  worsening with interior size under PML (0.87→0.51) — says the fixed-\(N\) pattern **does not**
  stay localized. ⇒ **bin (ii) A-WEAKENED is supported ⇒ G-PERSIST CONFIRMS.** (Footing note:
  bin (ii) itself is *not* a "boundary-clean bin" — neither boundary is clean, §5; what is
  boundary-insensitive is the *trend*, and the trend supports (ii). This corrects the frozen
  prereg's "(ii) holds boundary-clean" phrasing — see the prereg erratum.)

**Recommendation: Reading B (G-PERSIST CONFIRMS).** The φ-dispersion trend is the cleanest
evidence in the battery — it *worsens* as the boundary influence *shrinks*, which no boundary
artifact does. The E-leakage confound at small N is real (Reading A's kernel of truth) but
does not rescue persistence, because the deeper failure is structural dispersion, not energy
leakage.

**This is a framing-level physics call — surfaced for Grant, not fiated.** The crux question
(plumber-physical): *in the closed reflecting box, is φ growing to 10× the flux self-amplifying
into a bound resonance (genuine, → A-SUPPORTED), or is it the cavity pumping the Φ_link mode
because the flux has nowhere to leave (artifact, → A-WEAKENED holds)?* The φ-collapse-with-N
under PML says the latter, but the closed-box mechanism is not directly instrumented here.

**Either way: bin (ii) does NOT select (B).** Node-mint stays firewalled; this battery reads
(A) fixed-\(N\) only.

---

## 8 · Follow-on (the clean discriminator — KEEP-BOTH new axis)

The frozen E/φ detector is boundary-degenerate; the clean ruling needs a **boundary-insensitive
localization observable** — e.g. the fraction of interior energy / Φ_link² inside a central
core (a genuinely localized structure keeps a high core fraction under **both** boundaries; a
dispersing/sloshing one does not). Per prereg §Detector-substitution rule this is a **NEW
axis added alongside** the frozen E/φ (KEEP-BOTH), **never a swap**. This is the recommended
next driver if Grant wants Reading A vs B settled empirically rather than by intuition.

**Second follow-on — a φ-channel negative control** (adversarial review finding #5): the
sabotage plant here exercises only the E-channel because seed re-injection clobbers φ (§6). A
proper control sustains φ *without* destroying the Cosserat state, to test whether the
load-bearing φ-detector can be fooled by external sustenance.

---

## 9 · Provenance

- Prereg frozen + pushed as its own commit (`19f67662`) **before** any driver code — freeze-by-push.
- Reproduction byte-exact vs banked #655 (§1).
- Carrier: `run_loop_gap_probe` rank-4; the only changes are `N` and `pml` (harness diff = the
  `pml` passthrough; default preserves banked `pml=3`). No retune, no new engine, no `genesis_v{N}`.
- Per-cell JSON + machine summary: `assets/sim_outputs/genesis_npersist_battery/`
  (**gitignored per repo convention** — regenerate with
  `python src/scripts/vol_1_foundations/genesis_npersist_battery.py --all`, or per-cell via
  `--cell N PML MODE FID`; the numbers above are the run of record and are reproducible
  byte-for-byte from the frozen carrier).

---

## 10 · Adversarial review (PR #670 — 5 lenses → per-finding verify)

Ran `ave-adversarial-pr-review` via scriptPath wrapper (handoff discipline (d); never the
named-args path). **5/5 findings confirmed on verify — 1 MAJOR + 4 MINOR, all EVIDENCE-VOID
(documentation-integrity; none corrupt the banked conclusion).** All are consequences of the
closed-box detector degeneracy this RESULT already argues; the **G-PERSIST CONFIRMS
recommendation (via φ-dispersion) is untouched.** Fixes applied this turn:

| # | sev (verified) | finding | fix |
|---|---|---|---|
| 1,3 | MAJOR→MINOR | frozen prereg mechanism-note claimed closed-box E is "**not** a conservation identity" — data refutes it (E≡1.0 mode-independent, incl. structure-dead photon_lock); the boundary-axis E-channel discriminator is vacuous | **prereg erratum** (dated; frozen body byte-untouched) |
| 2 | MINOR | φ≥0.80 floor is one-sided ⇒ closed-box runaway φ≈10× trivially passes a *retention* floor | §5 one-sided-floor note |
| 4 | MINOR | "(ii) holds **boundary-clean**" conflicts with "neither boundary is clean" | §1/§7 reworded: the *φ-dispersion trend* is boundary-insensitive and supports (ii) |
| 5 | **MAJOR** | sabotage plant labeled "valid" via an E-lift proxy, not the prereg's false-PASS criterion; re-injection zeroes φ ⇒ `plant_false_pass`=False for all, and the load-bearing φ-channel is never exercised | §6 rewritten honestly + driver relabeled (`e_channel_integrator_coupled`, `phi_channel_exercised=False`); φ-channel control added as follow-on (§8) |

Full review output: workflow run `wf_8689c70a-98a` (10 agents, 0 errors).
