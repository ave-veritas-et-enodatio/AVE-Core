# DAMA annual-modulation phase-lock check: standard halo vs substrate/CMB frame

**Date:** 2026-07-04
**Arc:** `analysis/figure-incorporation` (D2, queued item)
**Scope:** adjudicate ONE discriminator only — the surviving discriminator #2 of the
dark-sector leaf (`dama-alpha-slew-derivation.md` §11.3 Claim B / §11.4 row 2:
"CMB-velocity phase-lock of annual modulation"). No new claims minted; this note
computes the phase arithmetic that had never been computed and returns a verdict
bin + a status-note for the existing leaf.
**Class:** DISCRIMINATOR ADJUDICATION (falsification arithmetic). No physics
chord/echo/emergence claim.

---

## 1. The discriminator as stated in the leaf (verbatim)

`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`:

- §11.3 Claim B (:188): *"AVE substrate-rate predicts: modulation phase peaks when
  Earth's CMB-frame velocity is maximum. Earth's velocity through CMB is
  |v_Sun-CMB + v_Earth-orbit|; this peaks when Earth's orbital velocity is parallel
  to Sun's CMB-frame velocity, **which occurs around early June (day-of-year ~152)**."*
- §11.4 table (:211): *"CMB-velocity phase-lock (June peak) | Solar-driven:
  December peak (perihelion)... | June peak matching CMB-velocity phase | **CONFIRMED by DAMA**."*
- Datasheet row (:130): *"Annual modulation PHASE (June peak) | **CONFIRMED
  AVE-distinct vs SM solar-driven (December peak)** — DAMA observed phase matches
  CMB-velocity phase (§11)."*

**The load-bearing assumption never checked:** that the peak of |v_Sun-CMB +
v_Earth| lands "around early June (day ~152)" — i.e. that projecting Earth's orbit
onto the **CMB dipole apex** gives the same date as the standard-halo DM-wind. This
note computes both dates from the actual sky geometry.

---

## 2. Inputs (verified 2026-07-04)

| Quantity | Value | Source |
|:--|:--|:--|
| **DAMA/LIBRA-phase2 measured phase** t₀ | **145 ± 5 days** (from Jan 1; ~mid-May) | arXiv:1805.10486 abstract (period 0.999±0.001 yr; amplitude 0.0103±0.0008 cpd/kg/keV; 12.9σ) |
| Standard-halo DM-wind apex (solar motion wrt galactic halo) | (l,b)≈(87.3°,1.8°), v≈232.6 km/s | v_LSR (0,220,0) + v_peculiar (11.1,12.24,7.25) km/s (Schönrich et al.; Freese-Lisanti-Savage RMP 2013 geometry) |
| **CMB dipole apex** (brief value) | (l,b)≈(264°,48°), v=370 km/s | task brief |
| CMB dipole apex (Planck 2018 / Wikipedia cross-check) | (l,b)≈(264.0°,48.3°) [equiv. (271.9°,30°) reported form], v=369.82±0.11 km/s | Planck; en.wikipedia CMB |

Note: the brief's (264°,48°) and one Wikipedia rendering (271.9°,30°) are the same
dipole reported in slightly different conventions; **both give the same peak date to
within ~4 days** (see §4), so the verdict does not depend on which is used.

---

## 3. Method

The count-rate modulation R(t)=R₀+R_m·cos(2π(t−t₀)/T) peaks when the detector's
speed **in the reference frame** is maximal, i.e. when |v_apex + v_Earth(t)| is
maximal. This is convention-free: v_apex is the frame velocity (direction only sets
the DATE; speed only sets the amplitude), and v_Earth(t) is taken directly from the
JPL ephemeris (astropy `get_body_barycentric_posvel('earth')`, ICRS barycentric,
year 2018). No 90°-lead approximation is used. Driver:
`scratchpad/dama_phase{2,3,4}.py` (deterministic; astropy 7.2.0).

**Validation of the method** (reproduce the known answer): the standard DM-wind apex
(l=87.3°, b=1.8°, v=232.6 km/s) yields peak **day 153.1 = June 2** — the canonical
DAMA-halo expectation to <1 day. Method verified.

---

## 4. Result — the three dates

| Hypothesis | Apex direction | Predicted peak (day-of-year, Jan 1 = 1) | Calendar |
|:--|:--|:--:|:--:|
| **(i) Standard halo** (DM-wind toward Cygnus/galactic-rotation) | (l,b)≈(87.3°,1.8°), v≈232 km/s | **153 ± ~2** | **June 2** |
| **(ii) Substrate / CMB frame** (CMB dipole apex, brief) | (l,b)=(264°,48°), v=370 km/s | **348** | **Dec 13** |
| (ii′) Substrate / CMB frame (Planck apex, cross-check) | (l,b)=(271.9°,30°), v=369.82 | **352** | **Dec 17** |
| **DAMA/LIBRA-phase2 MEASURED** | — | **145 ± 5** | **~May 25** |

**Ecliptic geometry (the why):** the DM-wind apex sits at ecliptic longitude λ≈341°;
the CMB dipole apex sits at ecliptic longitude λ≈172°. They are separated by
**≈170° in ecliptic longitude** — nearly antipodal in the plane of Earth's orbit. So
projecting Earth's annual velocity onto them gives peak dates ≈**172 days apart**
(half a year). The CMB apex and the galactic-rotation (Cygnus) apex are NOT the same
direction; the leaf's §11.3 conflated them.

**Comparison to DAMA (145 ± 5 d):**
- (i) standard halo: |153 − 145| = 8 d ≈ **1.6σ** — compatible.
- (ii) substrate/CMB: |348 − 145| = 203 d → on the annual circle = **162 d ≈ 32σ**
  offset — the CMB-frame peak is essentially antiphase (December) to DAMA's observed
  May peak.

---

## 5. Verdict

### **[CMB-PHASE-EXCLUDED]**

The substrate/CMB-frame reading of DAMA's phase **dies**. Projecting the standard
Earth-orbit geometry onto the **CMB dipole apex** predicts a modulation peak in
**mid-December (day ~348)**, ~162 days (≈180°, ~32σ) away from DAMA/LIBRA's measured
**145 ± 5 days** (mid-May). DAMA's phase is compatible with the **standard halo**
DM-wind (June 2, day 153, ~1.6σ) — which is the SM/particulate-DM expectation, NOT
an AVE-distinct one.

**The §11 claim was an arithmetic error, not a confirmation.** §11.3 Claim B
computed "Earth's CMB-frame velocity is maximum ... around early June (day ~152)" by
implicitly using the galactic-rotation/Cygnus apex direction (which does peak in
June) while *labelling* it the CMB apex. The two apexes are ~170° apart in ecliptic
longitude; the CMB apex peaks in December. The phase match that the leaf reported as
"AVE-distinct, CONFIRMED by DAMA" is in fact the **standard-halo** phase — the very
SM prediction it claimed to be distinct from. As a discriminator between the
substrate/CMB frame and the standard halo, DAMA's phase **favours the standard halo
and excludes the CMB frame.**

### Status-note for the existing leaf (§11)

Per the brief's [CMB-PHASE-EXCLUDED] instruction, a dated status-note is added to
`dama-alpha-slew-derivation.md` §11.3 Claim B / §11.4 / the datasheet row demoting
the phase-lock discriminator from "CONFIRMED AVE-distinct" to **EXCLUDED** (the CMB
apex predicts a December peak; DAMA's May peak matches the standard halo). Rule-12
preservation: the body of Claim B is preserved; a 🔴 header records the falsification.
The two OTHER §11 discriminators (Z-independence cross-crystal swap [UNTESTED];
solid-vs-liquid G>0 gate) are **untouched** by this note — this adjudicates the
phase-lock discriminator only.

---

## 6. Sober external context (stated, not adjudicated here)

The DAMA modulation is under heavy external pressure independent of this phase
arithmetic:

- **ANAIS-112** (same NaI(Tl) target, 3 yr): "consistent with the absence of
  modulation and **inconsistent with DAMA's observation at nearly 3σ**" (arXiv:2404.17348),
  projected to reach 5σ within ~8 yr.
- **COSINE-100** (NaI(Tl)): reports weaker / phase-ambiguous results, no confirmation
  of the DAMA modulation at DAMA amplitude.

These already pressure the DAMA signal *as a dark-matter signal at all*, regardless
of frame. **This note does not rest on them** — it adjudicates only the phase-lock
discriminator, which fails on the phase arithmetic alone. The external nulls are
consistent context: even if one grants DAMA's modulation, its phase is the
standard-halo phase, not a CMB-frame phase.

---

## 7. Provenance

- Arithmetic driver (deterministic, astropy 7.2.0):
  `scratchpad/dama_phase2.py` (rigorous |v_apex+v_Earth| ephemeris peak),
  `dama_phase3.py` (method validation → June 2 for DM-wind apex),
  `dama_phase4.py` (ecliptic-longitude separation).
- DAMA phase: arXiv:1805.10486 (DAMA/LIBRA-phase2), t₀ = 145 ± 5 d.
- CMB dipole: task brief (264°,48°,370) + Planck cross-check (369.82 km/s).
- DM-wind apex geometry: Freese, Lisanti, Savage, Rev. Mod. Phys. 85, 1561 (2013).
- ANAIS-112: arXiv:2404.17348. COSINE-100: weaker/ambiguous (context only).
