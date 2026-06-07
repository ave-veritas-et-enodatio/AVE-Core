# Electron genesis — "a drop in water" (RESULT)

**Date:** 2026-06-06
**Branch:** `analysis/2026-06-06-electron-genesis-drop` (worktree `AVE-Core-genesis-wt`)
**Prereg (FROZEN):** [`research/2026-06-06_electron-genesis-drop-prereg.md`](2026-06-06_electron-genesis-drop-prereg.md)
**Brief:** [`_orchestration/2026-06-06_electron-genesis-drop.md`](../_orchestration/2026-06-06_electron-genesis-drop.md) §1.6 (TWO-COLLIDING PAIR correction)
**Driver:** [`src/scripts/vol_1_foundations/r11_electron_genesis_drop.py`](../src/scripts/vol_1_foundations/r11_electron_genesis_drop.py)
**Animation:** [`src/scripts/vol_1_foundations/r11_electron_genesis_animation.py`](../src/scripts/vol_1_foundations/r11_electron_genesis_animation.py)
**Engine:** `VacuumEngine3D` (K4-TLM + Cosserat — the only engine with the (2,3) carrier)
**Predecessor:** [`research/2026-06-04_full-electron-option-B-discrete-emergence-result.md`](2026-06-04_full-electron-option-B-discrete-emergence-result.md) (two opposite-handed pulses at amp 0.40, **sub-pinch-off** A²=0.35, DISPERSED; Cosserat ω≡0 exact fixed point)

**Status:** RESULT COMPLETE (2026-06-06). Run: `r11_electron_genesis_drop.py all 40` (N=40, PML=4,
deterministic T=0). Raw: `r11_electron_genesis_drop_results.json` + `r11_genesis_{single,pair,pair_baseline}_capture.npz`.

**RESULT (one line):** Driving to the **A→1 pinch-off** (the missing ingredient vs the 2026-06-04
sub-pinch-off run), the pure-V photon route **does** pinch off into localized **ℓ_node-sized droplets**
(single → 1 drop; pair → **2 distinct drops**, the geometric e⁺e⁻ split) — **but the droplets stay
OVER-yield** (V/V_yield ≈ 8–11, lossy), the **(2,3) does not assemble**, the **chirality split is not
captured** (the sign extractor does not track the drive handedness), and the **Cosserat ω stays exactly
0** in every run (Q0 fixed point holds at the pinch-off, amplitude-independent). **Verdict (III) for
both builds** — the pinch-off *geometry* is hosted; the sub-V_yield (2,3) *electron-state* is not.

---

## §0 HEADLINE (the deliverable)

- **Checkpoint 1 (single photon):** **(III)** — one photon driven to A→1 (A²=2.98) localizes to a
  **ℓ_node-sized lump (FWHM = 1 cell)** that rings, **but stays over-yield** (V/V_yield ≈ 8.4, A²≈1.28),
  *not* a persistent sub-V_yield droplet. It does **not disperse** (it pinches off + localizes) and it
  does **not become the electron** (it stays over-ruptured). It also does not beat the matched baseline
  on energy retention (8.3% vs 29.9% scrambled).
- **The pair (genesis):** **(III)** — two opposite-handed colliding photons (antinode A²=4.18) pinch off
  into **two distinct ℓ_node drops** (x=12 and x=28, separated 16 cells — the geometric pair split
  DID happen), **but both stay over-yield** (V/V_yield ≈ 10–11), the **(2,3) does not assemble**
  (noisy windings (1,2)/(2,0), not (2,3)), and **check-5 fails**: the chirality signs are (+1,+1)
  (same), while the same-handed *baseline* gave (−1,+1) (opposite) — the sign extractor reads **noise**,
  not the drive handedness. **Not full genesis.**
- **The single-vs-pair contrast:** the pair **does** geometrically split into **two** drops (vs the
  single's one) — the collision pinch-off into a *pair* is real. **But charge-needs-the-pair is NOT
  demonstrated:** neither build produces a sub-V_yield (2,3) electron, the pair's chirality split is not
  captured in the live carrier, and the Cosserat ω (the SU(2) charge carrier) stays **exactly 0** in all
  three runs. The charge/(2,3) layer is dormant on the pure-V pinch-off — a single explanatory mechanism
  (§8) covers every failed check.

---

## §1 The plumber-physical question surfaced (pre-test-physics-check + Rule 16)

**Surfaced to Grant (flag-don't-fix); proceeded with the stated default per the brief's build-and-run mandate, since (II)/(III) are pre-committed valid outcomes.**

> **Does "the pair is the chirality split" (check 5, opposite winding signs) live in the
> `(V_inc, V_ref)` phasor handedness (V-sector — where `theory.md:16` places the (2,3) and which
> is dynamically alive), or does it require the Cosserat ω to spin up two opposite-handed vortices
> (Cos-sector — which the 2026-06-04 Q0 finding proved a pure-V photon CANNOT do; ω=0 is an exact
> fixed point because the V→ω coupling is parametric / even-in-ω, amplitude-independent)?**

**Corpus search (the prior that bears on it):**
- `theory.md:16` (verified verbatim): *"an electron is the 0₁ unknot in real space carrying a (2,3)
  Clifford-torus winding pattern in phase space … The trefoil lives in the bond-pair LC tank's
  (V_inc, V_ref) phasor trajectory, not in the real-space flux-tube topology. Its … peak voltage
  sits safely below the 43.65 kV [V_yield] saturation threshold … it can ring forever."* → the
  (2,3) is a **V-sector phasor** object; the stable electron is **sub-V_yield + rings forever**.
- 2026-06-04 Q0 (`research/2026-06-04_full-electron-option-B-discrete-emergence-result.md` §VERDICT):
  the Cosserat ω stayed at **exactly 0** in all arms (emergence, baseline, AND imposed) — a pure-V
  photon cannot spin up the Cos-sector; ω=0 is an exact fixed point (the coupling `W_refl` is even
  in ω → ∂W/∂ω=0 at ω=0, amplitude-independent).

**Default taken (recorded for adjudication):** measure the pair + its chirality split in the
**V-sector `(V_inc, V_ref)` phasor** (the corpus coordinate, alive), and report the Cosserat ω
alongside as a flagged diagnostic (expected dormant per Q0). The NEW ingredient vs 2026-06-04 is
driving to the **A→1 pinch-off** (the predecessor stopped at A²=0.35, below pinch-off) and the
PAIR reframe (charge conservation: a neutral input → a net-neutral e⁻+e⁺ pair, not a single
charged (2,3)).

---

## §2 Substrate-native-check CP8 walk (before code)

| CP | Resolution for the genesis test |
|---|---|
| **1 — dynamics** | Discrete K4-TLM scatter+connect (V-sector) + Cosserat (u,ω) LC-tank. Wave propagation, NOT energy-minimization. The lattice IS the computation; `engine.step()`. |
| **2 — sector** | The droplet (mass/localization) AND the (2,3) charge winding both live in **V-sector (V_inc, V_ref)** (theory.md:16). The Cosserat ω SU(2) carrier exists but is parametrically decoupled from a pure-V photon (Q0). Measure V-sector primary; report ω alongside. |
| **3 — objective** | Self-trap = Op14 saturation (`Z_eff=Z_0/√S`) + Op3 bond-reflection driving local Γ→−1 (TIR). The **pinch-off** = the antinode hitting **A→1** (the saturation skin / `|Γ|=1` wall). NOT minimization. |
| **4 — phase-space vs real-space (load-bearing)** | (2,3) + chirality measured in `(V_inc, V_ref)` phasor (theory.md:16), NOT real-space lattice-Cartesian. Localization + size are real-space; ring frequency is temporal. Each check in its matching coordinate. |
| **5 — local clock** | Op14 active → `ω_local(r) = ω_C·√(1−A²(r))`. The A→1 skin freezes (`ω_local→0`); the sub-V_yield core rings at ~`ω_C`. Check 2 compares the measured ring frequency to BOTH `ω_C` and the CP5-corrected `ω_local`. |
| **6 — reactance pair (load-bearing)** | C-state `V_inc` AND L-state `Φ_link` recorded at each drop's core bond **every step** over the recording window — the slosh. A snapshot at one phase cannot distinguish a ringing droplet from a frozen saturated lump; the pair trace can. |
| **7 — sampling** | PML excluded (`pml ≤ {i,j,k} ≤ N−pml−1`) before any top-K. The PAIR is the **top-2 well-separated interior density peaks** (min-sep ≥ 4 cells), NOT centroid+offset (a shell's centroid is the empty middle). |
| **8 — generative precursor (load-bearing)** | Seed the **photon(s)**, NOT the finished (2,3) or the finished droplet. Single photon = mass-droplet control; two colliding = pair genesis. **Matched baseline** mandatory (Build 1: amplitude-matched permutation-scrambled field; Build 2: same-handed pair). Each non-hostable layer = a structural-capability finding (→ outcome II/III), not a failure. |

## §3 Coordinate + consistency-vs-emergence classification

- **phase-space-coordinate-check:** checks 4/5 (the (2,3) winding + chirality sign) are read in the
  `(V_inc, V_ref)` phasor — the corpus coordinate. The phasor is a **native engine state array**
  (`k4.V_inc/V_ref`), not a fabricated projection (A47-v3 probe-5 guard satisfied).
- **consistency-vs-emergence (Class tags):**
  - checks **2/3** (ring → `ω_C`; size → `ℓ_node`): **consistency-class** — targets are
    framework-internal natural units (`ω_C=1`, `ℓ_node=1` cell, `V_SNAP=1`); NO CODATA input. Per the
    skill's do-NOT-fire clause ("targets sized in framework-internal units without CODATA comparison").
  - checks **4/5** (the (2,3) assembles + opposite chirality): **emergence-class (Class D)** — a
    dimensionless topological observable computed from sim primitives, with the (2,3) **NOT in the
    seed** (the CP sources inject E⊥B⊥k pure-V structure only). No CODATA-derived input reaches the
    target via SI substitution.
- **ave-canonical-source:** `ALPHA`, `V_yield=√α·V_SNAP`, `ω_C`, `ℓ_node`, `R_I=√(2α)` imported from
  `ave.core.constants`; no hardcoded literals.
- **ave-driver-script-honesty:** forward; no fit, no optimizer onto (2,3). The chirality split arises
  (if at all) from the opposite-handed drive, read post-hoc.

---

## §4 Calibration — the A→1 pinch-off amplitude (Rule 10 empirical)

Drive-peak A² vs amplitude (N=40, forward, no fit). **The rupture/pinch-off is a HARD bistable knee,
not a gentle approach to A→1:**

| amp/pulse | single drive-peak A² | pair antinode A² |
|---|---|---|
| 0.40 | 0.273 | 0.298 |
| 0.45 | 0.351 | 0.389 |
| 0.48 | 0.432 | **4.178** ← pair knee |
| 0.50 | **2.982** ← single knee | 10.20 |
| 0.52 | 7.678 | 9.19 |
| 0.55 | 11.14 | 13.15 |

**Load-bearing finding:** A² jumps from ~0.4 (sub-pinch) to ~3–4 (over-rupture) across **~0.02–0.05**
amplitude. There is **no amplitude that sits at A²≈1** — the saturation wall (Op14 `Z_eff = Z_0/√S`,
`S→0` at A→1) is a runaway: once the antinode breaches the wall it spikes far past it. So "drive to
A→1" operationally means "the smallest amp that triggers the rupture," which **overshoots** to A²≈3–4.
This sharp knee IS the pinch-off mechanism (the runaway is the rupture event), and it forces the drops
to be **born over-yield**. Auto-pick (target A²≈2): **single = 0.50** (A²=2.98), **pair = 0.48** (A²=4.18).
This confirms + sharpens the brief's calibration ("A→1 sits between 0.40 and 0.60 → ~0.45–0.50"): the
window is real but a *single* amplitude straddling the knee does not exist.

---

## §5 CHECKPOINT 1 — single-photon mass-droplet CONTROL

One moving CP photon, amp=0.50, driven to drive-peak A²=2.98, then source off + 16-period free-evolve.
Drop detected at `[12,16,20]` (the photon self-trapped near its source-side focus).

| Check | Measure | Result | PASS? |
|---|---|---|---|
| persistence | energy retention (post-shutoff) | 0.083 (vs scrambled baseline 0.299) | does not beat baseline |
| **1 sub-V_yield ring** | V/V_yield (settled) = **8.38**; rings=True; react_corr=−0.004 | **over-yield** (8× V_yield), reactance ≈ 0 | **FAIL** |
| **2 rings at ω_C** | meas/ω_C = **4.44** | rings at 4.4× ω_C (over-driven; ω_local degenerate at A²>1) | **FAIL** |
| **3 size ≈ ℓ_node** | FWHM = **1 cell** = 1 ℓ_node | exactly the minimum droplet | **PASS** |
| localization | FWHM bounded + peak > 5× mean interior | localized=True | (geometric) PASS |

**Checkpoint-1 answer:** a single photon driven to the A→1 pinch-off **does NOT make a persistent
sub-V_yield mass droplet.** It pinches off + **localizes to exactly ℓ_node** (the geometric self-trap
is real — it does NOT disperse), but the core stays **over-yield** (V/V_yield ≈ 8.4, lossy), so by the
prereg-§3 / theory.md:16 criterion ("peak voltage safely below V_yield … rings forever") it is **not
the electron** — it is an over-ruptured lossy lump. **Verdict (III).** It also does not out-retain the
amplitude-matched scrambled baseline (8.3% vs 29.9%) — the localization is not structure-driven in the
energy-retention sense (the coherent photon radiates its splash; the incoherent scramble just sits).

---

## §6 BUILD 2 — two-colliding PAIR genesis (the 5-check gate)

Two counter-propagating **opposite-handed** CP photons (RH +x at x≈12, LH −x at x≈28), amp=0.48/pulse,
antinode drive-peak A²=4.18, then source off + 16P free-evolve. **The collision pinched off into TWO
distinct drops** — `drop[0] @ [12,16,18]` and `drop[1] @ [28,16,20]`, separated 16 cells = the geometric
e⁻/e⁺ split. Energy retention (post-shutoff) = 0.156.

| Check | drop[0] (e⁻ side) | drop[1] (e⁺ side) | PASS? |
|---|---|---|---|
| **1 sub-V_yield ring** | V/V_yield = **10.4**, rings=True, react_corr=−0.002 | V/V_yield = **10.9**, rings=True, react_corr=+0.009 | **FAIL (both over-yield)** |
| **2 rings at ω_C** | meas/ω_C = **4.44** | meas/ω_C = **4.44** | **FAIL** |
| **3 size ≈ ℓ_node** | FWHM = **1 cell** | FWHM = **1 cell** | **PASS (both = ℓ_node)** |
| **4 (2,3) assembles** | (n1,n2)=(1,2), c=20 | (n1,n2)=(2,0), c=19 | **FAIL (not (2,3); extractor unvalidated)** |
| **5 charge (opposite sign)** | chirality sign = **+1** | chirality sign = **+1** | **FAIL (same sign, not opposite)** |

**Carrier-2 (Cosserat ω):** ω_max = **0.00**, Op10 c = **0**, Hopf = **0.00** — exactly dormant
(Q0 fixed point holds at the A→1 pinch-off; amplitude-independent).

**The check-5 control inversion (the decisive tell that check-5 is noise):** the **opposite-handed**
genesis gave **same** signs (+1,+1); the **same-handed** baseline gave **opposite** signs (−1,+1). The
phasor-rotation sign extractor does **not** track the drive handedness — it reads noise, exactly as the
2026-06-04 §AUDITOR #1 caveat warned (the temporal-single-bond extractor could not recover even a
*known-imposed* (2,3)/chirality). So check-5 (and check-4) are **inconclusive as (2,3)/chirality
detectors**, not a clean "absent" — but the chirality split, if present, is **not in the live carrier
the pure-V drive engages.**

**Matched (same-handed) baseline:** also 2 over-yield drops (V/V_yield ≈ 10–12), energy retention 0.196
— i.e. the same-handed pair is **indistinguishable** from the opposite-handed pair on every load-bearing
check (both over-yield ℓ_node lumps; both ω≡0; both no (2,3)). The opposite-handed *chirality split*
buys nothing over the same-handed control. **Verdict (III) — not full genesis.**

---

## §7 The single-vs-pair contrast (the science)

| | single photon | colliding pair (opposite-handed) | same-handed baseline |
|---|---|---|---|
| # drops formed | **1** | **2** (separated 16 cells) | 2 |
| drop size (FWHM) | 1 cell = ℓ_node | 1 cell = ℓ_node (both) | 1 cell (both) |
| sub-V_yield? | no (V/V_yield 8.4) | no (V/V_yield 10–11) | no (10–12) |
| (2,3) assembles? | no | no | no |
| chirality split (check 5) | n/a | **no** (signs +,+) | "yes" (signs −,+) ← noise |
| Cosserat ω (charge carrier) | **0** | **0** | **0** |
| verdict | III | III | — |

**What the contrast shows (and does not):**
- **It DOES show** the geometric pinch-off scales with the input: a single photon makes **one** drop;
  the colliding pair makes **two** distinct drops. The collision-into-a-pair geometry is real and
  hostable — the antinode splits into two ℓ_node droplets straddling the collision plane.
- **It does NOT demonstrate "charge needs the pair."** The brief's hypothesis was that the pair would
  resolve the single-photon (2,3)-non-emergence by supplying the chirality split. It does not: the
  pair's two drops are **over-yield neutral lumps**, the (2,3) does **not** assemble on either, the
  chirality-sign extractor reads **noise** (it inverts between genesis and baseline), and the Cosserat
  ω charge carrier is **exactly 0** in all three runs. The same-handed baseline is indistinguishable
  from the opposite-handed genesis on every load-bearing check — so the *opposite-handedness* (the
  putative chirality seed) changes **nothing** the pure-V drive can carry.

---

## §8 VERDICT (I / II / III)

**(III) NO STABLE (sub-V_yield) DROP — for both builds.** Refined honestly: the engine **hosts the
pinch-off geometry** (photon → localized ℓ_node droplet; pair → two ℓ_node droplets — check 3 PASS for
all) but **does not host the electron-state** — the droplets stay **over-yield** (check 1 FAIL, the
defining "lossy ≠ electron" condition), ring at **4.4× ω_C** not ω_C (check 2 FAIL), the **(2,3) does
not assemble** (check 4 FAIL), and the **chirality split is not captured** (check 5 FAIL / inconclusive).

**The single explanatory mechanism (Rule 11 honest closure — one cause covers every failed check):**
the **pure-V transverse photon engages only the V-sector Op14 amplitude saturation.** That channel can
pinch off the *geometry* (run the antinode to the rupture wall → localize to ℓ_node) but it has
**(a) no cooling/binding channel** to relax the over-ruptured core down to the sub-V_yield "rings-forever"
state (the excess can only leave by *dispersing* the drop, not by *settling* it — so the drop is stuck
over-yield), and **(b) no coupling to the Cosserat ω SU(2) sector** (ω=0 is an exact fixed point because
`W_refl` is even in ω → ∂W/∂ω=0 at ω=0, **amplitude-independent** — confirmed: ω≡0 even at the A→1
pinch-off, A²=4.18). Charge **is** the (2,3) winding (Ax 2) and the (2,3)'s SU(2) carrier is the ω sector
(`06_winding_index_projection.md` §4); a pure-V photon — collision or not, pinch-off or not — **cannot
seed it.** This is the **A→1-pinch-off sharpening of the 2026-06-04 Q0 finding**: the missing ingredient
was hypothesized to be reaching the saturation wall; reaching it changes the *geometry* (now a localized
ℓ_node pair forms) but **not the carrier** (ω still 0, (2,3) still absent, drops still over-yield).

**Not falsified, localized:** this is a clean CP8 structural-capability finding (`ave-evidence-framing`):
the engine carries **layer 1 partially** (localization to ℓ_node — yes; sub-V_yield relaxation — no) and
**does not carry the charge/(2,3) layer** from a pure-V seed. The path that *could* host the (2,3) is an
**ω-seed** (the `PairNucleationGate` / Option-D nucleation — which is the **imposed control**, not
genesis, and which the brief explicitly did **not** direct me to plant). Whether "the pair is the
chirality split" is testable at all on a pure-V drive is the open carrier-question surfaced in §1 — this
result is the empirical evidence that, on the V-sector pinch-off alone, it is **not**.

---

## §9 Honest limitations + discipline walk

**Known limitations (carried from the predecessor + this build):**
1. **The (2,3) phasor extractor is unvalidated, AND this run shows the chirality SIGN is also noise**
   (sharpens 2026-06-04 §AUDITOR #1): the temporal-single-bond extractor did not recover a *known-imposed*
   (2,3) before, and here the **control inverts** — the opposite-handed genesis read signs (+1,+1) while
   the same-handed baseline read (−1,+1). So neither check-4 (the `(n1,n2)` magnitudes) NOR check-5 (the
   rotation sign) is a load-bearing (2,3)/chirality detector on this engine. The (2,3)/chirality
   conclusions rest on the **robust** signals: V/V_yield (over-yield, check 1) and ω≡0 (carrier-2),
   not on the phasor winding numbers.
2. **ℓ_node = 1 lattice cell** (Nyquist limit): the electron sits at the lattice resolution, so the
   size check (FWHM → ~1 cell) is at the resolution floor. A localized droplet reads FWHM ~ 1–3 cells;
   dispersal reads → photon scale (~6+ cells). The discriminator is coarse but directional.
3. **N=40, PML=4** (32 active cells) chosen for tractable runtime across calibration + 4 production
   runs; the pinch-off / sub-V_yield / (2,3) physics is structural, not resolution-limited (the
   2026-06-04 N=48 predecessor found the same ω=0 fixed point + dispersal at sub-pinch-off).
4. **Persistence thresholds are engineering-choices** (`localized`: FWHM < 0.30·N + peak > 5× mean
   interior A²; `rings`: ≥ 4 zero-crossings + both reactance states alive). Tagged as such; the verdict
   is cross-checked against the raw retention + matched-baseline numbers (not blindly auto-verdict —
   per the 2026-06-04 precedent that corrected its driver's auto-verdict).
5. **The over-drive is forced by the sharp rupture knee, and the 16P free-evolve is a finite window**
   (the one genuinely-open caveat against the (III) verdict). Because A² jumps 0.4 → 3–4 across ~0.03
   amplitude (§4), the drops are unavoidably *born* over-yield; whether a **longer** free-evolve (or a
   memristive/cooling Op14 variant, `use_memristive_saturation`) would let an over-ruptured core **relax**
   down to sub-V_yield rather than stay stuck is **not** settled by this run. The robust finding that does
   NOT depend on the window is the **carrier** result: ω≡0 (exact, amplitude-independent) and the
   same-handed/opposite-handed indistinguishability — the *charge/(2,3) layer* is dormant regardless of
   how the amplitude eventually settles. A longer-window / memristive re-run is the cheap follow-up that
   would convert the "stays over-yield" sub-claim from window-bounded to structural.

**Discipline fired (with the load-bearing finding from each):**
- **substrate-native-check CP8** — seeded the precursor photon(s), NOT the finished (2,3)/droplet;
  matched baseline mandatory; layer-by-layer. **CP4** — (2,3)/chirality in (V_inc,V_ref) phasor.
  **CP5** — ω_local = ω_C·√(1−A²) (the saturated skin freezes, the sub-yield core rings). **CP6** —
  C-state V_inc AND L-state Φ_link recorded every step (the slosh). **CP7** — PML excluded, top-2
  density-peak drop selection.
- **phase-space-coordinate-check** — checks 4/5 in the phasor (native engine array, not fabricated).
- **consistency-vs-emergence** — checks 2/3 consistency (framework-internal ω_C/ℓ_node, no CODATA);
  checks 4/5 emergence (Class D, (2,3) not in the seed).
- **ave-canonical-source** — ALPHA, V_yield, ω_C, ℓ_node, R_I from `ave.core.constants`.
- **ave-driver-script-honesty** — forward, no fit; the CP sources inject pure-V E⊥B⊥k only.
- **pre-test-physics-check** — the carrier plumber-question surfaced (§1) before the design locked.
- **verify-before-cite** — `theory.md:16` quoted verbatim after grep; the ℓ_node↔cell mapping
  (1 cell) measured from the live engine, not assumed.
- **ave-evidence-framing** — the matched baseline is mandatory; (II)/(III) reported as valid CP8
  findings; no forced "genesis" claim.

## §10 Cross-references + auditor queue

**Cross-references:**
- Predecessor (the sub-pinch-off / ω=0 finding this corrects): `research/2026-06-04_full-electron-option-B-discrete-emergence-result.md`
- The (2,3)-in-phasor + sub-V_yield + rings-forever corpus anchor: `manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md:16`
- The ω=0 exact-fixed-point analytical side (Q0 / gate-a): `research/2026-06-04_ee-rf-quadrature-coupling-and-alpha-quarter-hypothesis.md` §8
- Reused machinery (counter-propagating CP source + phasor extractor): `src/scripts/vol_1_foundations/r10_vacuumengine3d_transverse_2_3_emergence.py`
- Engine: `src/ave/topological/vacuum_engine.py` (`VacuumEngine3D`, `SpatialDipoleCPSource`)

**Auditor queue (implementer surfaces; auditor lands):**
1. **The carrier plumber-question (§1)** — adjudicate whether "the pair is the chirality split" is a
   V-sector phasor claim (default taken) or a Cos-sector ω claim (provably unreachable from a pure-V
   photon per Q0). Bears on whether check-5 is even testable on the pure-V drive.
2. **The (2,3) extractor validation** (carried from 2026-06-04 #1) — still blocking any standalone
   (2,3)-presence/absence claim built on the phasor winding numbers.
3. **No manuscript/matrix entry drafted by implementer** — this is a CP8 research result; the auditor
   decides corpus-state propagation.
