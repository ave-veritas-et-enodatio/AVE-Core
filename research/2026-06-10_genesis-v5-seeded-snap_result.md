# RESULT — Genesis-v5 seeded-snap: does a SEEDED region + a snapping bulk + a chiral drive assemble an ELECTRON? And is the lock the SNAP (D1) or the MOTION (D8)?

**Date:** 2026-06-10
**Prereg (frozen, committed alone first):** `research/2026-06-10_genesis-v5-seeded-snap_prereg.md` @ `454acf19` (single file, 285 insertions, zero run artifact between — the cavprobe ordering honored)
**Driver:** `src/scripts/vol_1_foundations/genesis_v5_seeded_snap_run.py` (serial, deterministic, seed `20260610`)
**Raw numbers:** `research/2026-06-10_genesis-v5-seeded-snap_results.json` (every number below is read FROM this file — ave-driver-script-honesty)
**Figures:** `research/figures/fig_v5_{reach,nu_art_attribution,persistence,energy_ledger}.png`
**Scale:** N=40, M=1.8 (the inherited cavitation reach), n_build=3200, n_persist=1200, frac=0.85; wall 481 s.

---

## 0. HEADLINE VERDICT (written from the numbers, not the hope — Rule 11 honest closure)

**SPEC-SHEET = NOT-ELECTRON.** The primary gate T1 (mass converges) **FAILS decisively**: the trapped
dilatation added-mass `E_V` is flat (~13) through the entire reach, then **DETONATES to 50 339** at the
spontaneous-snap cascade (step ~2849) — a 3 870× jump. `H_total` pumps `16 906 → 64 834` during the build
(+283 %) and stays at `35 406` under drive-OFF (energy is created, not conserved). The mass does not
converge; the assembly is a **secular pump / transient**, not a rest mass.

**D8 (the lock question) = BOTH — but on TWO INDEPENDENT CHANNELS** (a clean, informative resolution of
Grant's *"isn't motion the lock?"*):
- the **density void is SNAP-LOCKED** — the snapped pocket persists under forced de-spin (P2: 5968→5952
  cells at the floor) AND requires D1 (the no-snap arm has zero pocket and the deficit either collapses to
  the clamp under P1 or heals under P2);
- the **circulation is MOTION-LOCKED** — the physical angular momentum `L_bulk` is conserved under
  drive-off (P1 ratio 0.97–0.99) in EVERY arm including no-snap, and is **ν_art-INVARIANT** (the deficit is
  identical across a 50× viscosity sweep) → the persistent-current lock is real physics, not an apparatus
  artifact. The prior sonic-horizon "reversible-spring" heal-on-de-spin does NOT carry a hidden viscosity
  component (the D8 re-read resolved: the motion-lock is genuine).

**The locks are real; the object is not an electron.** A single mechanism (§6) explains every spec failure:
the bulk-density sector under the M=1.8 rotation is a runaway cavitating vortex whose snap-vent into the
deep seed detonates the mass, while the inherited winding/charge sector is inert. No charge self-assembles,
spin is apparatus-set, there is no de Broglie scaling, and the "twin" is geometric (identical in the achiral
arm). **Clean negative. Branch closes.**

---

## 1. THE D7 ELECTRON SPEC-SHEET (floors first, frozen bins §4.2) — REAL NUMBERS

| test | floor-check (first) | measured | bin | verdict |
|---|---|---|---|---|
| **T1 mass (primary)** | `E_V` late-window drift vs F0e drift-floor `0.05` | `E_V: 11.70 → 50 339.24`; late-drift `5.175`; `H_total 16 906 → 64 834` | **STILL-RISING** | ❌ FAIL — the frozen falsifier ("still rising at run-end"); mass detonates at the snap cascade |
| **T2 charge** | F0b `r=4 ≥ 3` cells, phase-space Park-along-contours | `w_tor=1, w_pol=0`, sign `0` | **NOT-2-3** | ❌ FAIL — `w_pol≡0`, the inherited graft-v4 winder gap; no de-novo (2,3) |
| **T3 spin** | F0c reactance pair + CP5; DERIVED ½-pole-pair form | `L_bulk=139 360`, ratio-to-½-form `10 844`; `|L_ω|` **tracks lock_eta** (5.38→0.067 over η 0→0.12) | **UNLOCKED / CLIP** | ❌ FAIL — no quantized spin; the locked `|L_ω|` is APPARATUS (tracks the knob, prereg D1/N-clip) |
| **T4 kick** | F0a interior + re-run T1/T3 post-perturb | `E_V 2.25e6 → 1.83e6` (both detonated), `L` sign preserved | RE-VERIFIED | ⚠️ MOOT — "passes" only because the runaway is robust to a kick (re-verifies a non-electron transient) |
| **T5 pairs** | F0a + global handedness-ledger floor | `abs_net_frac=0.0000`, twin RH=2608/LH=1040 **identical in achiral** | BALANCED | ⚠️ MOOT — the ∫ζ=0 Kelvin signature ANY compact flow satisfies; the twin is GEOMETRIC not chiral |
| **T6 de Broglie** | F0a + ≥2 momenta | `λ=[40,40,40]` at p=[0.1,0.2,0.4]; log-slope `−0.000` | **NOT-INVERSE-P** | ❌ FAIL — no `λ∝1/p`; the boosted packet has no momentum-dependent wavelength |

**SPEC-SHEET verdict (frozen bins §4.2): NOT-ELECTRON** — T1 (the primary) fails; the assembly is a
transient/pump. T2/T3/T6 independently fail. T4/T5 "pass" trivially (robustness-of-runaway /
compact-support balance), not electron behavior.

---

## 2. THE D8 DISCRIMINATOR (frozen bins §4.1) — SNAP vs MOTION, per channel

Built state (all snap arms identical): pocket 5968, `rho_core=-0.618` (clamped at the candidate floor),
`Gamma=80.75`, `L_bulk=139 360`.

| channel | observable | P1 (drive-off, L-conserved) | P2 (forced de-spin) | no-snap arm | BIN |
|---|---|---|---|---|---|
| **density void** | pocket cells / `rho_core` | 5968 → **7576** (holds+grows), `rho=-0.618` | 5968 → **5952** (HOLDS at floor despite de-spin) | pocket≡0; P1 deficit **collapses** `-0.704→-0.950` (clamp), P2 **heals** `-0.704→-0.667` | **SNAP-LOCKED** (persists P2, requires D1) |
| **circulation** | `L_bulk` (physical AM) | ratio **0.97–0.99** (conserved) | → `~-97` (de-spun) | conserved too (ratio 0.994); **ν_art-INVARIANT** | **MOTION-LOCKED** (conserved drive-off, no snap needed) |

**D8 = BOTH (independent channels).** The snap holds the void; conservation holds the circulation. The
no-snap+P1 arm (the motion-lock discriminator) shows the circulation persists (rival POSITIVE for the AM
channel) **but the density void does NOT** — without the snap it runs away to the `-0.95` clamp. The
no-snap+P2 must-heal control PASSES (`-0.704→-0.667`, trending to 0).

**Apparatus gate on §4.1 (K1 ν_art sweep, the D8 attribution knob):** deficit deepening `= -0.0516`
**identical** at ν_art ∈ {1e-4 … 5e-3} (50× span); Γ-drift `+0.012→+0.016`. The motion-deficit does NOT
track viscosity → the MOTION-LOCKED claim is **real physics, not a viscosity artifact** (resolves the
prereg §0.1 D8 re-read: the prior LOCK verdict's apparatus-component worry is laid to rest). See
`fig_v5_nu_art_attribution.png`.

> **NOTE — the Γ "pump" is a MEASUREMENT artifact:** `Gamma` over a FIXED mid-plane disk grows 25→80→95
> (ratio 1.18) because the snap-boundary shear layer feeds the fixed Eulerian loop; the physical `L_bulk`
> is conserved (0.97). Reported per ave-apparatus-floor-attribution; the conserved invariant is `L_bulk`.

---

## 3. APPARATUS ATTRIBUTION (§5 CLIP sweeps, run BEFORE the verdicts) — which numbers are physics, which are the bench

| knob | sweep | result | attribution |
|---|---|---|---|
| **K1 ν_art** (D8 attribution) | {1e-4,5e-4,1e-3,2e-3,5e-3} | deficit `=-0.0516` INVARIANT; Γ-drift `+0.012→+0.016` | **PHYSICS** — motion-deficit is viscosity-independent |
| **D1 lock_eta** (T3) | {0,0.05,0.08,0.12} | `|L_ω|` `5.38→0.168→0.103→0.067` (tracks η); `L_bulk`,`Hbel` η-invariant | **CLIP** — the T3 micro-rotation spin VALUE is apparatus-set; T3 cannot claim a physical spin |
| **K2 N-resolution** | {32,40,48} | deepest `rho` `-0.577/-0.430/-0.344` at fixed 2000 steps (tracks N) | **CLIP** — the spontaneous-snap ONSET TIME is resolution-dependent (smaller grid rarefies faster) |
| **N1 rho_cav** (FLASH) | {-0.55,-0.618,-0.68} | latent `8.20/7.42/6.35` (tracks threshold); pocket=136 invariant | latent MAGNITUDE is candidate-floor-dependent; pocket geometry is not |
| **N3 chi_shock** (FLASH) | {0,0.5,1.0} | latent `3.47/5.44/7.42` = chi-INDEPENDENT floor `3.47` + chi-scaled shock | FLASH has a REAL reversible-internal-energy floor + an apparatus shock component |
| **N4 detector thresh** | {1,3,10,1e12} | bursts `1,1,1,0` (monotone) | correct CLIP telltale; floor F0d `=3.84e-5` |

---

## 4. FLASH (D6), COLLIMATION (D3), TWIN (D4), ENERGY LEDGER

- **FLASH burst (D6) — RESOLVED above floor, but riding the runaway.** Calibrated floor F0d `=3.84e-5`
  (known-null free run). MAIN scan: ~170 bursts, **onset step 2849** (the spontaneous-snap cascade),
  magnitudes 0.04–94 (clearing floor×3 = `1.15e-4` by 3–6 orders); total burst energy `1936`. The
  longitudinal latent IS detected in the exact-EOS bulk ledger — the snap signature is real — but it fires
  as a 350-step cascade detonation, not a clean single assembly pulse.
- **Collimation (D3) — columnarity `0.933` (floor `0.025`), CLEARS.** But identical across all arms and
  set by `energize_rotation_column` (z-invariant by construction) → the column is the IMPOSED rotation
  geometry, NOT an emergent chiral collimation. Watched-observable-with-floor passes; the emergence reading
  does not.
- **Twin-pocket (D4/T5) — GEOMETRIC, not chiral.** RH=2608 / LH=1040 cells **byte-identical** in MAIN,
  C-achiral, AND C-opp-helicity. The pocket splits by the rotation column's vorticity sense, present even
  with zero net helicity → the twin is geometry, not pair-canon. The handedness ledger is BLIND (no chiral
  selection). A weak non-quantized `Hbel` sign-carry DOES flip with the photon helicity
  (`-0.117 / 0 / +0.117` for RH/achiral/LH) — the graft-v4 sign-carry survives — but it closes no (2,3).
- **Energy ledger (build → P1) — DOES NOT CLOSE (pump).** `H_total 16 906 → 64 834` (built) `→ 35 406`
  (P1-end). Closure residual `−1.09` (H grew; energy created). Snap ledger: latent-held `968`, vented-to-seed
  `484`, vented-radiated `484`, dissipated `0` (vent-on routes shock to the seed), mass-clamp `0.91`. The
  vent (`484`) is 100× too small to account for the `E_V` growth of `50 326` → the vent merely TRIGGERS the
  deep-seed nonlinear breather, which self-amplifies. See `fig_v5_energy_ledger.png`.

---

## 5. ARM MATRIX — the seed, chirality, and handedness have ZERO bulk effect (a load-bearing finding)

MAIN, C-no-seed, C-achiral, C-opp-helicity are **byte-identical in the bulk** (pocket 5968, `rho=-0.618`,
`Gamma=80.75`, `L_bulk=139 360` — all four). The "seeded snap" object is a **pure rotation-driven cavitation
pocket**: the Lane-1 seed V does not couple to the bulk density (vent is one-way, snap→seed), and the chiral
photon is the inherited inert director (graft-v4 LOCK-FAIL). Charge/handedness live only in the weak
`Hbel`/`Hphoton` sign-carry, which flips correctly but quantizes nothing.

---

## 6. THE SINGLE EXPLANATORY MECHANISM (Rule 11 — one mechanism, all failures)

Every spec failure traces to ONE mechanism with two inert halves:

1. **The bulk-density sector under M=1.8 rotation is a runaway cavitating vortex.** The centrifugal deficit
   reaches the candidate floor `ρ̄_cav=−1/φ` (resolution-dependent onset, K2-CLIP); the snap clamps it
   (real reflector) and the circulation is conserved (real motion-lock). BUT the snap-vent into the
   frac=0.85 deep-saturated seed pushes the V-breather over its `c_eff²=c₀²/√(1−A²)` stiffening singularity
   → the mass DETONATES (`E_V 13→50 339`). This is the **genesis-24 nonlinear-breather detonation**,
   reappearing through the new GAP-C vent coupling. T1 fails here.
2. **The inherited ω/winding/charge sector is INERT** (the standing graft-v4 photon-helicity verdict:
   "photon = non-depleting chiral director; bounded coupling does not transfer helicity"). `w_pol≡0`, no
   de-novo (2,3) → T2 fails; spin is apparatus (lock_eta) → T3 fails; no winding to set a Compton scale →
   T6 fails.

The D1 snap and the D8 motion-lock are BOTH genuine substrate capabilities — the medium CAN hold a snapped
void and a persistent circulation — but together they assemble a **detonating cavitating vortex with no
charge, no quantized spin, no de Broglie, and a geometric (not chiral) twin**. Not an electron.

---

## 7. FLAGS (flag-don't-fix; surfaced for auditor/Grant, NOT silently resolved)

1. **§11.5 v5-build GATE remains OPEN (prereg §0.3, verbatim-preserved).** This run executed the
   directive's gate-LIFTED reading. The framing-doc §11.5 flag (seeded-genesis + snap blessing /
   close-the-loop / energy-weighted gate "not independently anchored in tracked corpus") stands for auditor
   adjudication. The NOT-ELECTRON result does not depend on the gate status.
2. **GAP-C vent coupling is the named detonation trigger.** The D2-ratified snap→seed vent (switchable,
   default-on here) is what destabilizes the deep seed. A vent-off / frac-sweep follow-up would ISOLATE it —
   recorded as a mechanism-naming follow-up, **NOT** a debug-toward-success (Rule 11; the negative stands).
3. **The candidate floor `ρ̄_cav=−1/φ` stays CANDIDATE** (prereg §0.2). The reach crosses it; the snap
   clamps there; nothing here promotes it to canon. Root re-verified `1+ρ̄/(1−ρ̄²)=2.2e-16`.
4. **Spontaneous-snap onset is resolution-dependent (K2-CLIP).** The build-claim "spontaneous assembly"
   timing is partly apparatus; the snap itself (once the floor is crossed) is physics.

---

## 8. CORPUS-STATE (for the auditor lane to land — I surface, the auditor lands)

- **v5 build claim: FALSIFIED (NOT-ELECTRON).** Add a 🔴 Rule-12 header to the v5 hypothesis slot
  (substitution-not-retraction: preserve the body, do NOT refill with a new unverified hypothesis).
- **D8 resolved (BOTH, per-channel):** SNAP-LOCKED density void + MOTION-LOCKED circulation (ν_art-invariant).
  This is a NEW positive sub-result worth its own tracked entry — the persistent-current motion-lock is real
  and viscosity-independent (strengthens, does not overturn, the sonic-horizon predecessor).
- **graft-v4 inert-winder + genesis-24 detonation: BOTH RE-CONFIRMED** in the unified engine (cross-arm
  byte-identity + the `w_pol≡0` / `E_V`-detonation signatures).
- Predecessor verdicts (sonic-horizon LOCK, genesis-24 B-localizes, graft-v4 C→LOCK-FAIL, cavitation CLIP):
  all INHERITED, none overturned.

---

## 🔴 ADDENDUM — 2026-06-10 (Rule-12, append-only; v5 panel ruling)

**Rule 12 / append-only:** the bodies above (§0–§8) are PRESERVED verbatim and SUPERSEDED here, not
rewritten. The frozen prereg `@454acf19` (single file, 285 insertions) is untouched. Every number below
re-verified against `research/2026-06-10_genesis-v5-seeded-snap_results.json` and the engine/driver
(`src/ave/core/unified_genesis_engine.py`, `src/scripts/vol_1_foundations/genesis_v5_seeded_snap_run.py`,
`src/ave/core/longitudinal_burst_detector.py`) before writing (verify-before-cite). **The HEADLINE VERDICT
(§0) — NOT-ELECTRON; the spontaneous-snap cascade detonates T1 — STANDS unchanged.** This addendum revises
ONLY the D8 lock-mechanism reading and scopes four secondary claims.

### A. D8 DEMOTED — supersedes §0 lines 20–29, §2 lines 63–66, §6 line 145, §8 line 171

The prior verdict **"D8 = BOTH — two independent channels"** is DEMOTED to:

> **MOTION-LOCKED CONFIRMED + SNAP-channel UNRESOLVED (construction-dependent).**

The SNAP-LOCKED "positive" CANNOT be binned a positive under §4.1's own floor-gate: it is
**construction-guaranteed, not measured**. Five independent legs of the basis (each re-verified):

1. **The snap's irreversibility is fixed, never swept.** `snap_payback_rate=1.0` in EVERY persistence arm
   (engine default `unified_genesis_engine.py:88`; `build_engine` default `genesis_v5_seeded_snap_run.py:65`;
   `run_arm` never overrides it) and `delta_heal=0.0` (engine default `:87`, never passed). The MAIN arm
   records `unsnap_events=0` (`snap_ledger`): NO cell ever paid back its tally over the entire window. With
   the re-entry width pinned to zero and the payback rate pinned to one and NEITHER swept, "the pocket holds
   under P2 de-spin" is the construction, not a finding.
2. **§210 hard-constraint violation.** The prereg's STEP-5 rule (`prereg:210`) mandates the FULL knob set
   `N1–N6 / D1 / K1–K5` swept BEFORE any §4 verdict. The run swept only `{N1, N3, N4, D1, K1, K2}`. The two
   knobs that gate the SNAP-LOCKED bin — **N2 `Δ_heal`** (`prereg:198`, pre-named CLIP signature *"hysteresis
   tracks Δ_heal (built-in irreversibility)"*) and **K3 stop-time** (`prereg:206`, *"H_total 'converged'
   value tracks stop-time"*) — were never swept. The discriminator the prereg itself named for this exact
   bin was not run.
3. **Engine fiat clamp + de-spin starves the payback.** The held-void is a hard clamp
   (`unified_genesis_engine.py:306–322`: `rho_bar[cm]=rho_cav`, `u_adv[cm]=0`); un-snapping requires
   `paid_ledger ≥ latent_ledger`, where `paid_ledger` accrues from neighbor over-pressure × the (fixed)
   payback rate × dt (`:315`). The P2 protocol forcibly de-spins (`despin_bulk(0.0)`), killing the very
   flow that generates over-pressure → the ledger starves → non-payback is **near-tautological** under P2.
4. **The pocket GROWS under P1, it does not converge.** P1 (drive-off) pocket `5968 → 7576` (`+26.9 %`),
   `rho_core` pinned at the floor `−0.618`. A 27 % runaway read at an arbitrary stop-time is a transient
   caught mid-growth, NOT a converged locked structure (the K3 falsifier exactly).
5. **The energy tally never closes.** Build pumps `H_total 16 906 → 64 834` (`+283 %`), closure residual
   `−1.09` (`energy_ledger.closure_resid_frac`). Energy is created across the build; the snap tally
   (`latent 968`, `vent_seed 484`, `vent_rad 484`) cannot be energy-certified against a non-closing ledger.
   A persistence claim resting on this tally is uncertifiable until the `+283 %` pump is isolated.

### B. MOTION-LOCKED STANDS — the genuine, sweep-backed positive (supersedes-and-strengthens §2 line 64)

This is the real result of the run, and it is the rival D8 hypothesis (*"isn't motion the lock?"*):

- `L_bulk` drive-off ratio (P1) is **0.97–0.99 in ALL arms** — `0.9733` in the four snap arms AND
  **`0.9945` in the no-snap arm** (the MOTION-LOCK discriminator: persistence there is the rival POSITIVE,
  not a control failure, per `prereg:105`/`:129`).
- The motion-deficit deepening is **`≈ −0.0516` INVARIANT** across the K1 `ν_art ∈ {1e-4 … 5e-3}` (50×)
  span (`−0.05157 … −0.05153`); `Γ`-decay `+0.012 → +0.016`. The lock does NOT track viscosity.

**Certified conclusion: as far as this run certifies, THE LOCK IS THE MOTION ITSELF** (conserved,
viscosity-independent circulation), NOT the snap. The snap's remaining live, certified role is the
**latent-burst / genesis-moment** mechanism, not a persistence lock: D6 genuinely detected
**~160 impulsive longitudinal bursts** (the detector-scan list holds exactly 160; the body §4 line 99
*"~170"* reads slightly high — flag-don't-fix, the scan returns 160) at **onset step 2849** (the
spontaneous-snap cascade), magnitudes `0.035–93.95` clearing the known-null floor `3.84e-5` by **3–6 OOM**,
total burst energy `1936` — the **birth flash**, a real detection. Its MAGNITUDE is apparatus-tracked
(N1 latent ∝ candidate floor; N3 ∝ `χ_shock`); the DETECTION (floor-clearance) is physics.

### C. SCOPE the "laid to rest" sentence — supersedes §2 lines 73–74

The §2 claim that the sonic-horizon heal-vs-viscosity worry is "laid to rest" is OVER-SCOPED. v5's K1
invariance is a DIFFERENT engine/regime (the unified-genesis bulk, `M=1.8` seeded/snapping column), not the
sonic-horizon run's artifacts. The sonic-horizon heal-vs-viscosity attribution remains **OPEN on that
branch's own artifacts** (auditor queue). v5 strengthens the motion-lock case; it does not close the
predecessor's attribution.

### D. CAP the K2 onset claim — supersedes §3 K2 row / §7 flag 4; + T6 caveat

The K2 spontaneous-snap-ONSET-TIME claim is CAPPED: in the K2 sweep **no arm actually snapped** —
all three resolutions ran the FIXED `steps_to_snap=2000` cap with `pocket_cells=0` and deepest `rho`
`−0.577/−0.430/−0.344` (never reached the floor `−0.618`). The "onset time tracks resolution" reading is an
**extrapolation from a sweep where nothing snapped**, not a measured onset; spontaneous-assembly TIMING
claims are capped accordingly. Separately, **T6 (de Broglie) is an under-validated leg**: it was evaluated
on a detonating/non-converged object (T1 already FAILED), so its `NOT-INVERSE-P` result is a flat-`λ` read
on a transient — caveat-tagged, carries no independent weight.

### E. COLLIMATION honesty line — supersedes §4 collimation bullet (lines 103–106)

Columnarity `0.9333` clears its floor `0.025` by **37×**, but is **byte-identical (`0.9332873079510086`)
across all four snap arms — including across handedness** (C-achiral and C-opp-helicity carry the identical
value). It is the IMPOSED `energize_rotation_column` geometry (z-invariant by construction), NOT an emergent
chiral collimation. The prereg's D3 horizon→tube→ring sequence **never ran**. Honest instrument (the floor
gates correctly), null emergence.

### F. TWIN / handedness — instrument-null (supersedes §4 twin bullet, lines 107–111)

The twin is an **instrument-null**: the drive's handedness never coupled into the bulk. The pocket split
`RH=2608 / LH=1040` is **byte-identical** across MAIN, C-achiral, AND C-opp-helicity — a geometric split by
the rotation column's vorticity sense, present at zero net helicity. Pair-canon is **untouched** (neither
confirmed nor refuted here). The `±0.11658` `Hbel` sign-carry (`−0.117 / ≈0 / +0.117` for RH/achiral/LH)
confirms the **graft-v4 sign channel exists** but closes no `(2,3)` winding. **Named blocking component for
any future T2/T5: a real photon-helicity → bulk-circulation/ω coupling channel (the transducer)** — absent
here, it is the missing primitive (A44: an engine coupling-family gap, NOT a missing axiom).

### G. NAMED FOLLOW-UPS (verbatim-class; recorded, NOT a debug-toward-success — Rule 11)

1. **Snap-channel adjudication sweep** — `Δ_heal × snap_payback_rate × K3` (Rule-11-safe; it adjudicates the
   LOCK claim, NOT the electron claim, which is closed NOT-ELECTRON).
2. **GAP-C detonation isolation** — vent-off / frac sweep to isolate the snap→seed vent trigger.
3. **The handedness-coupling channel** (the §F transducer) — the load-bearing primitive for T2/T5.
4. **K2 convergence** — drive an arm to an actual snap (lift the 2000-step cap) before any onset-time claim.
5. **The `+283 %` pump isolation** — required BEFORE any T1 retest (the ledger must close first).
6. **The sonic-horizon retroactive heal-vs-viscosity attribution** (§C; that branch's own artifacts).

### H. NET CORPUS-STATE DELTA (I surface; the auditor lands — supersedes §8 bullet 2)

- **v5 build: FALSIFIED (NOT-ELECTRON)** — unchanged; Rule-12 🔴 header on the v5 hypothesis slot stands.
- **D8: MOTION-LOCKED confirmed (sweep-backed, ν_art-invariant) — a real new positive.** The SNAP-LOCKED
  sub-claim is **withdrawn to UNRESOLVED (construction-dependent)**; it is NOT a co-equal second channel.
  The motion-lock is the certified positive; the snap is the certified birth-flash, not a certified lock.
