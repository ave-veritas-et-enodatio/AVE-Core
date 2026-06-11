# RESEARCH — The Chiral Angle of Attack: the slats, the four surfaces, and the mirror from inside

**Date:** 2026-06-11 · **Branch:** `analysis/2026-06-11-chiral-angle-of-attack` (worktree `/tmp/ave-chiralaoa` off `origin/main` = `f6ffd98d`)
**Lane:** implementer (synthesis doc). **This is NOT a promotion.** It lands as a research-doc synthesis that
(a) names a mechanism (the chiral boundary as helical *slats*), (b) class-tags four observable surfaces with the
number each one OWES, and (c) records a hypothesis-class reading of the v5–v7 genesis failures. Promotion of any
row into `manuscript/ave-kb` is **auditor-gated** — the implementer surfaces, the auditor lands the manual.

**Governing discipline:** `substrate-native-check`, `pre-test-physics-check`, `phase-space-coordinate-check`
(A46), `consistency-vs-emergence`, `verify-before-cite` (A43 v2), `ave-coincidence-magnet`, Rule 12.
**Class-tag legend (used per surface, no exceptions):**

| tag | meaning |
|---|---|
| **canonical** | grep-verified in `manuscript/ave-kb` or `src/ave/core/constants.py` at a cited file:line |
| **consistency-class** | a standard-physics fact (optics, knot geometry) cited as a validated *analog*, not an AVE claim |
| **measured-in-engine** | a number a driver actually produced, with its instrument floor stated |
| **hypothesis-class** | a forward picture; owes a number or a discriminator before it can headline |
| **virgin** | the corpus contains zero content; any number used must be derived fresh or carried requires-verification |
| **verified-external** | a published external bound, source named + WebFetch/Crossref-confirmed this session |

> **⚠ COINCIDENCE-MAGNET FLAG (load-bearing, stated up front).** The phasor-coordinate pitch angle below comes out
> at **ψ = 29.81°**, **0.19° short of 30°**. A round number near an exact algebraic result is a coincidence-magnet:
> the 30° is **not** used as an anchor anywhere in this doc. The *exact* algebra `ψ = arctan(3/(2φ²))` is the claim;
> the proximity to 30° is logged and quarantined.

---

## 1. THE SLATS MECHANISM

**Grant's framing (2026-06-11).** The chiral particle boundary is a set of **helical slats** — a venetian blind
wound to a screw pitch. A wave is *admitted* (passes between the slats into the trapping region) or *rejected*
(reflected) according to a single product: **admission = handedness × angle-of-attack, read against the screw
pitch.** A wave whose handedness *and* whose incidence angle line up with the slat pitch slips through; flip the
handedness, or change the attack angle, and the same boundary turns into a mirror. The boundary is therefore not a
scalar reflector with one reflectivity — it is an **oriented admittance** whose value is a function of `(handedness,
ψ_attack, pitch)`. This is the geometric kernel under everything that follows: the four observable surfaces in §2
are the four places this same admittance shows up, and §3 is what the slats look like from the *inside*.

**The validated analog class (consistency-class — standard optics, cited as analog, NOT as an AVE result).** The
cholesteric (chiral-nematic) liquid-crystal mirror is exactly this device in the lab: it Bragg-reflects the
circular-polarization band whose handedness *co-rotates* with the cholesteric helix and transmits the
counter-handed band, the reflected band centered on the helix pitch and selected by incidence angle. That a
helically-pitched dielectric stack performs handedness-and-angle-selective reflection is settled photonics; it is
the **validated analog class** that licenses the slats picture. It is **not** evidence for the AVE mechanism — it
is the existence proof that a structure of this *class* can do what the picture asks.

**The corpus form is hypothesis-class, partial-asymmetry by construction.** The cholesteric reading enters the
corpus as **hypothesis 0(c)** of the sonic-horizon prereg, verbatim (`research/2026-06-10_sonic-horizon-closure_prereg.md:18`):

> "The reflector is HANDEDNESS-SELECTIVE — partial-asymmetry version. Co-handed reflected with a different
> efficiency (Q) than counter-handed; both signs trappable (the **partial** version). The **strict** version
> (one handedness perfectly transmitted) is **NOT built in** — it would contradict positron stability (a
> counter-handed electron-analog must still be trappable)."

The strict one-way valve is forbidden: a positron is a counter-handed electron-analog and **must still be
trappable**, so the slats are a *Q-asymmetry* (co-handed cheaper to trap), never a perfect gate. The canonical
substrate root of the handedness itself is the freeze-chirality (`manuscript/vol_9_vacuum_datasheet/chapters/11_topological_characteristics.tex:95`,
**canonical**): "Right-handed `I4₁32` chirality at the substrate level is the canonical AVE substrate-mechanism for
ALL observed parity-violation phenomena … selected at lattice genesis by the direction of `Ω̂_freeze`." The
handedness *selects a mode* rather than *driving collapse* — the asymmetric-collapse rule, verify-before-cite-checked
in `research/2026-06-09_crystal-engine-elastodynamic-graft_design-prereg.md:84` (quoting archived L3 doc `66:87`):
"Chirality is not the collapsing mechanism — it's the mode selector … one handedness loses `Z₀` while the other
preserves it, creating the `Γ=−1` walls that bind the electron." The slat is the `Γ=−1` wall, set at the chiral
pitch.

**The measured lab instance — frame-dragging SELECTIVE (measured-in-engine; PR #174, merge `74dd8b13`, MERGED to
origin/main).** A driver has produced a handedness-selective reflection once, with a stated floor
(`research/2026-06-10_sonic-horizon-closure_result.md` §4-bis):

| config | R_co (m=+1) | R_counter (m=−1) | asym (co−counter) | vs floor 5.5e-12 |
|---|---|---|---|---|
| static pressure-release mirror | 0.5434504928408977 | 0.5434504928463568 | **5.46e-12** (the floor) | — |
| M=0.9, χ=1.0 | 0.014726 | 0.012860 | **+0.001866** | ~3.4e8× floor |
| M=1.0, χ=1.0 | 0.017596 | 0.014930 | **+0.002667** | ~4.9e8× floor |
| M=0.9, χ=0.0 | 0.014726 | 0.012860 | **+0.001866** | ~3.4e8× floor |

`R_co > R_counter` in every config; the asymmetry **scales with the drive** (+0.00187 at M=0.9 → +0.00267 at M=1.0)
and is **`χ_shock`-independent** (a property of the conserved circulation Γ, not of the dissipation knob); the
static-mirror control sits at the 5.5e-12 floor. **Two honesty fences carried with it:**

1. **SCOPE = frame-dragging ONLY, NOT cholesteric-Bragg.** The continuum bulk-flow engine "carries NO lattice
   handedness — it cannot represent cholesteric-Bragg selectivity" (prereg `:85`). What it measured is the
   *rotational-Doppler / acoustic-superradiance* frame-dragging asymmetry of a circulating pocket — a **different
   mechanism** that happens to share the slats geometry. A SELECTIVE here supports "the reflector has a handedness";
   it does **not** confirm the `I4₁32` cholesteric rule.
2. **WEAK.** Absolute `R_co ≈ 0.015–0.018` is only ~3% of the 0.54 static-mirror reference, because the LOCK pocket
   is transient — "do not headline v5 on this frame-dragging SELECTIVE" (`result.md` Addendum queue #4).

**Net for §1.** The slats are one geometric picture admitting **two distinct physical mechanisms**: the canonical
lattice cholesteric-Bragg rule (substrate `I4₁32`, *not representable* in any engine run to date) and the measured
frame-dragging rotational-Doppler rule (weak, scoped, merged). The validated optics analog says a slat-class
structure *can* do this; the corpus says the strict valve is forbidden by positron stability; the one lab instance
is real but weak and off-mechanism. Everything in §2 inherits exactly this tiering.

<!-- SECTION 1 -->

## 2. THE FOUR SURFACES

### 2.1 Surface A — black-hole Stokes-V spin-correlation

<!-- SECTION 2.1 -->

### 2.2 Surface B — gravitational-wave amplitude birefringence

<!-- SECTION 2.2 -->

### 2.3 Surface C — the v8/v9 injection blade angle (exact algebra)

<!-- SECTION 2.3 -->

### 2.4 Surface D — the freeze sign-selection mechanism (the slat-setting)

<!-- SECTION 2.4 -->

## 3. THE MIRROR FROM INSIDE

<!-- SECTION 3 -->

## 4. THE DARK-SECTOR ONE-LINER

<!-- SECTION 4 -->

## 5. OWED-NUMBERS TABLE

<!-- SECTION 5 -->

---

## Appendix — anchors verified this session (verify-before-cite log)

<!-- APPENDIX -->
