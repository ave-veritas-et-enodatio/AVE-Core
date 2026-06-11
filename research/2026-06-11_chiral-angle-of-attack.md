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

**Class: hypothesis-owing-the-amplitude.** Corpus state: **virgin** — `Stokes-V` / `Stokes V` returns zero
content workspace-wide (the only `Stokes` hits are Navier–Stokes). No AVE number exists.

**The external anchor (verified-external, WebFetch-confirmed this session, source named).** EHT Collaboration,
*First M87 EHT Results IX: Detection of Near-horizon Circular Polarization*, ApJL 2023 (DOI
`10.3847/2041-8213/acff70`; arXiv:2311.10976, abstract fetched verbatim 2026-06-11):

- resolved circular-polarization fraction **⟨|v|⟩ < 3.7 %** (all imaging methods),
- ALMA image-integrated **|v_int| < 1 %**,
- **"Faraday conversion is likely the dominant production mechanism for circular polarization at 230 GHz in M87*"**;
  the result "reinforces the previously reported preference for magnetically arrested accretion flow models."

So the published number class is an **upper limit + presence evidence**, not a resolved CP map. (Sgr A* unresolved
CP is also published — Bower et al. 1999, DOI `10.1086/312246` — but no *horizon-scale* Sgr A* Stokes-V map was
confirmed this session; carried **requires-verification**.)

**The SM-counterfactual, carried honestly (do NOT bury it).** A bare "AVE predicts nonzero Stokes V at the percent
level" is **not discriminating**: GRMHD synchrotron emission + Faraday conversion already lives exactly there, and
the EHT abstract *itself* endorses that as the dominant mechanism. Per the slats picture the chiral boundary radiates
a handedness-biased component — but synchrotron/Faraday make Stokes V too. **The discriminator is not the level; it
is the correlation STRUCTURE.**

**The owed number (the live discriminator axis).** The slats hypothesis owes:

1. **a SIGN RULE** — a v-asymmetry component whose sign is *locked to the BH spin axis* and **flips under spin-axis
   reversal** (the slat pitch is set by the freeze/rotation handedness; reverse the rotation, reverse the admitted
   handedness — §2.4). Faraday conversion's sign is set by the *line-of-sight field geometry + electron
   thermodynamics*, which is **not** rigidly spin-locked. A spin-axis-correlated, spin-flip-odd v-component is the
   structure synchrotron/Faraday does not natively produce.
2. **a MAGNITUDE** for that spin-locked component, to be compared against the verified ceilings ⟨|v|⟩ < 3.7 %
   (resolved) / |v_int| < 1 % (integrated) — it must sit *under* both.
3. **the explicit null/structure contrast vs Faraday conversion** — the statement of what the spin-locked component
   does that the field-geometry component cannot mimic (sign-flip-odd under Ω̂ reversal at fixed field geometry).

Until (1)–(3) carry actual numbers this surface is **hypothesis-owing-the-amplitude**, not a prediction. The
honest one-liner: *the EHT can already see percent-level circular polarization; the slats hypothesis only goes live
when it owns a spin-axis-correlated SIGN that Faraday conversion does not.*

<!-- SECTION 2.1 -->

### 2.2 Surface B — gravitational-wave amplitude birefringence

**Class: hypothesis owing a number against an existing bound.** Corpus state: **virgin** for GW parity — the four
Vol-3 Ch-08 gravitational-wave leaves (`gw-propagation-lossless.md`, `gw-impedance-perturbation.md`,
`gw-detection-antenna.md`, `ligo-gw-saturation-ratio.md`) carry **zero** chiral / parity / handedness /
birefringence content; `amplitude birefringence` returns zero hits workspace-wide. No AVE κ exists.

**The external anchor (verified-external, WebFetch-confirmed this session, source named).** Okounkova, Farr, Isi &
Stein, *Constraining gravitational wave amplitude birefringence and Chern–Simons gravity with GWTC-2*, Phys. Rev. D
**106**, 044067 (2022); arXiv:2101.11153 (abstract fetched 2026-06-11):

- amplitude birefringence = "left versus right circularly polarized modes of gravitational waves are exponentially
  enhanced and suppressed during propagation … absent in GR";
- published bound: **opacity parameter κ ≲ 0.74 Gpc⁻¹**;
- derived **Chern–Simons lengthscale ℓ₀ ≲ 1.0 × 10³ km** (factor-2 improvement on prior long-distance results),
  dataset GWTC-2.

There is a **bound already waiting**; AVE owes a number to put against it.

**The parity-odd lattice mechanism that already exists in-corpus (canonical).** The slats are not new here — the
substrate is chiral at the dispersion level. `manuscript/ave-kb/vol2/particle-physics/ch03-neutrino-sector/chiral-screening.md:11`
(**canonical**): the chiral dispersion relation `ω² = c²k² ∓ γ_c k` is parity-odd — the `∓` is the handedness. The
same leaf (`:22`) gives the evanescent-gap selection rule: "Modes with `Δc > 3`: the compliance channel is screened
(evanescent — same mechanism as right-handed neutrino parity violation)," with `Δc_crit = 3` = K4 connectivity =
trefoil crossing number. Crucially, `γ_c` is **not a free knob**: the same coefficient jointly constrains the
weak-force range (`gauge-boson-masses.md`) and the `δ_strain` sign-mechanism (`vol1/claim-quality.md`), so it is in
principle *pinnable* — which is what would make κ_AVE a forward prediction rather than a fit.

**The owed number.** A GW is a **transverse-shear** mode of the substrate (shear sector, matter-clock band — the
mode-taxonomy note: shear `G` / bulk `K` / EM transverse `c_EM`). The owed derivation:

1. carry the parity-odd `ω² = c²k² ∓ γ_c k` dispersion onto the **GW transverse-shear band** (the step that needs
   doing — `chiral-screening.md` derives it for *torsional* coupling; that it applies to the GW band is **not yet
   shown**, flag-don't-fix), and
2. integrate the resulting L/R attenuation asymmetry over a cosmological propagation distance to get a single
   **κ_AVE in Gpc⁻¹**, then
3. check `κ_AVE ≲ 0.74 Gpc⁻¹`.

If `κ_AVE` lands well below 0.74 the surface is consistent-but-weak; if it lands *near* 0.74 it is a live,
near-term-falsifiable forward prediction (GWTC-3-era bounds are tighter and were **not** fetched this session —
**requires-verification** before any "passes/fails" claim). Until step 2 produces a number this is
**hypothesis-owing-a-number**: the mechanism is canonical, the magnitude is virgin, the bound is published and
waiting.

<!-- SECTION 2.2 -->

### 2.3 Surface C — the v8/v9 injection blade angle (exact algebra)

**Class: exact algebra** (no number invented, no external bound — a closed-form consequence of canonical geometry).
This is the *angle-of-attack* of §1 made literal: the pitch angle at which a wave must be presented to the (2,3)
slats. For a `(p, q)` torus knot wound `p` times toroidally (major radius `R`) and `q` times poloidally (minor
radius `r`), the helix pitch angle measured from the toroidal (azimuthal) direction is

$$\tan\psi \;=\; \frac{q\,r}{p\,R}.$$

The electron is the `(2, 3)` winding (**canonical**: `p = 2` toroidal, `q = 3` poloidal —
`research/2026-06-10_electron-device-datasheet_draft.md:73`), so `q/p = 3/2` and `tan ψ = (3/2)(r/R)`. The geometry
supplies `r/R` — and here the **A46 fence bites**: there are **two** canonical aspect ratios living in **two
different coordinate systems**, and they must **not** be cross-compared (`datasheet_draft.md:61`, the explicit
phase-space/real-space settlement fence).

**(a) Phase-space (phasor) coordinates — `R/r = φ²`.** R and r are the Clifford-torus phasor semi-axes in the
`(V_inc, V_ref)` impedance plane (`constants.py:196` "the Clifford-torus (R, r) phase-space coordinates"; aspect
`R/r = φ² ≈ 2.618`, `datasheet_draft.md:70,175`). Then

$$\boxed{\;\psi_{\text{phasor}} = \arctan\!\frac{3}{2\varphi^{2}} = \arctan(0.5729490169) = 29.8105^{\circ}\;}
\qquad (\varphi^{2} = 2.6180339887).$$

**(b) Real-space (envelope) coordinates — `R/r ≈ 2.27`.** The real-space envelope ratio is a **different canonical
quantity** (the TLM convergence attractor, `datasheet_draft.md:80`, archive `26_step5_phase_space_RR.md:193` /
`78_canonical_phase_space_phasor.md:88`), explicitly `≠ φ²`. Then

$$\boxed{\;\psi_{\text{real}} = \arctan\!\frac{3}{2\cdot 2.27} = \arctan(0.6607929515) = 33.4564^{\circ}\;}.$$

The two pitch angles differ by **Δψ = 3.65°** — they are the *same A46 split* as `φ² = 2.618` vs `2.27`, now read as
an angle. **Cross-comparing them is the coordinate-dilution trap** (`datasheet_draft.md:61`).

> **⚠ COINCIDENCE-MAGNET (the flag promised in the header).** `ψ_phasor = 29.81°` is **0.19° short of 30°**. The
> claim is the *exact* `arctan(3/(2φ²))`; the proximity to 30° is **logged and quarantined**, used as an anchor
> NOWHERE. (`arctan(3/(2φ²)) = 30°` would require `tan 30° = 1/√3 = 0.57735` vs the actual `0.57295` — close but
> false; the 30° is a numerical near-miss, not an identity.)

**Design implication for the polyphase injector (engineering-choice, tagged as such).** The injector that deposits
the (2,3) winding is a **polyphase** drive — `q = 3` poloidal phases threaded across `p = 2` toroidal poles. Two
distinct blade angles fall out, and they govern **two different parts of the same machine**, which is why the A46
fence is load-bearing for the build, not just for the bookkeeping:

- the **drive phasing** (the temporal angle in the `(V_inc, V_ref)` impedance plane — the angle-of-attack the slats
  actually admit) is set by **`ψ_phasor = 29.81°`**, because the (2,3) winding the injector is trying to launch is a
  **phase-space object** (A46: test/build in the coordinate the claim lives in);
- the **physical blade pitch** (the machined helix angle of the real-space envelope shaping) is **`ψ_real = 33.46°`**.

Getting these crossed — phasing the drive at the real-space 33.46° or machining the blade at the phasor 29.81° —
is **exactly the coordinate-dilution failure** §3 argues sank v5–v7. The injection blade angle is therefore the
first place the chiral-AoA picture issues a falsifiable build instruction: **phase at 29.81°, machine at 33.46°,
never average the two to ~31.6°.**

<!-- SECTION 2.3 -->

### 2.4 Surface D — the freeze sign-selection mechanism (the slat-setting)

**Class: mechanism canonical; the sign-selectivity strength owes a number (hypothesis-owing-a-number).** §1's slats
have a pitch; **this surface names what *sets* it.** The slat-setting is `Ω̂_freeze`'s chiral angle projected onto
the freezing front. Canonical, `manuscript/ave-kb/common/trampoline-framework.md:105`:

> "**Direction of `Ω_freeze` → direction of bowing → right-handed chirality** by the right-hand rule applied to
> centrifugal pseudo-force × bond-axis. Mirror-image freeze-in gives left-handed universe with identical magnitude
> `|u_0|` and identical physics."

with `u_0 = ρ Ω_freeze² r_node² / (2 K_0)` (`:102`). So the substrate handedness is **not** a coin-flip frozen by
chance — it is *set by the direction of the cosmic-spin vector at genesis*, via the centrifugal-pseudo-force ×
bond-axis right-hand rule. This is the **sign-SELECTIVE** statement: `Ω̂_freeze` direction **determines** the sign
of the slat pitch (and `vol_9_…/11_topological_characteristics.tex:95` makes it the substrate-mechanism for **ALL**
observed parity violation).

**Why naming it matters — it distinguishes AVE from the sign-BLIND null (the discriminator, carried honestly).**
The standard chemistry benchmark for stir-induced homochirality is **Kondepudi, Kaufman & Singh 1990** (NaClO₃
crystallization, *Science*, DOI `10.1126/science.250.4983.975` — **existence verified-external**; the
sign-blindness *content* is paywalled, carried **requires-verification**). The canonical Kondepudi result is:
stirring drives each batch to near-total **single** handedness (autocatalytic secondary nucleation), **but the sign
is random batch-to-batch — stir direction CW vs CCW does NOT select which handedness wins.** That is *drive →
single domain* but **not** *drive-direction → sign*. The AVE `Ω_freeze` claim is **strictly stronger**: it is
*direction-SETS-sign*. **Canonical Kondepudi neither supports nor contradicts it** — sign-blind ≠ sign-selective;
the experiment that would discriminate has a different mechanism class. The matching literature class is **Ribó et
al. 2001** (vortex-direction sign-selection in stirred J-aggregate mesophases, *Science*, DOI
`10.1126/science.1060835` — **existence verified-external**; replication status **requires-verification**), a
*different system and mechanism* from NaClO₃ secondary nucleation. The `Ω_freeze` claim is **Ribó-class
(direction-sets-sign), not Kondepudi-class (sign-blind).**

**The owed number (feeds the fluid-analog bench's discriminator).** The bench program's discriminator bin (its
"STRONGER" outcome) is: **stirred enantiomeric-excess sign correlates with stir direction** — the Ribó-class result,
*not expected from canonical Kondepudi*. `trampoline-framework.md:105` gives the **mechanism** (right-hand rule,
`u_0`) but **no predicted ee-sign-vs-direction correlation MAGNITUDE** for any bench-realizable analog. So the owed
number is:

> **the predicted ee-sign / stir-direction correlation strength under the centrifugal-bond-stretch mechanism** — the
> quantitative value of the bench's STRONGER bin, so the bench can separate *AVE-mechanism-present* (direction-sets-
> sign) from *canonical-sign-blind*. Without it, even a STRONGER observation is unquantified.

This is the one surface where the slats picture touches a **bench-realizable** test rather than an astrophysical
upper limit — which is why pinning its owed magnitude is the highest-leverage of the four.

<!-- SECTION 2.4 -->

## 3. THE MIRROR FROM INSIDE

**Grant's framing (2026-06-11): "what would the slats look like from the inside? this is the mirror."** §1 looked at
the slats from OUTSIDE — an admission filter, `handedness × angle-of-attack vs pitch`. Turn around and stand inside
the trapped region: the same slats are now a **handedness-preserving mirror**. One structure, two faces — the
admission filter from outside, the **one-way valve / asymmetric-grip** boundary from inside. The wave that was
*admitted* at the chiral angle is now *retained* by the same chiral angle, bounce after bounce. The slats ARE the
particle's cavity wall, seen from within.

### 3.1 The decisive optical fact (consistency-class — standard optics, cited as analog)

This is textbook polarization optics, carried as a **validated analog**, not an AVE claim:

- **A normal (achiral) mirror FLIPS circular polarization per bounce.** On reflection, the helicity of a
  circularly-polarized wave reverses (right-circular → left-circular) — the propagation direction reverses while the
  lab-frame sense of `E`-rotation is preserved, so helicity flips. **Consequence:** in a cavity bounded by *normal*
  mirrors, a circulating wave alternates handedness every bounce; the round trip forces an **equal-handedness
  mixture** → a standing wave with **ZERO net chirality**.
- **A chiral (cholesteric-class) mirror reflects the co-handed band WITHOUT flipping.** The defining optical property
  of cholesteric reflection — the property that distinguishes it from a metal mirror — is that the reflected co-handed
  circular wave **keeps its handedness**. **Consequence:** a cavity bounded by *chiral* mirrors **preserves the
  circulating handedness** → a **persistent net chirality** that survives every round trip.

That contrast is the whole hinge: **only a chiral cavity can hold a circulating handedness.** A normal-mirror cavity
launders chirality to zero by construction.

### 3.2 The unifying hypothesis (hypothesis-class — do NOT overclaim)

> **⚠ THIS IS A COMPETING HYPOTHESIS, NOT A VERDICT (flag-don't-fix).** The v5–v7 genesis panel already has its own
> standing diagnosis for the de-novo failures: **A46 phase-space-vs-real-space coordinate dilution** (well-anchored:
> the (2,3) lives in the `(V_inc, V_ref)` phasor phase-space, real-space measurements of it are uninformative —
> `research/2026-06-04_full-electron-transverse-selftrap-result.md:50,70`; `research/2026-05-18_phase3f-…:8` "A46
> real-space-vs-phase-space failure") **plus LC dephasing** (the panel's named second mechanism). The chiral-cavity
> reading below **must compete with that diagnosis on a discriminator (§5), not silently replace it.** Tagged
> hypothesis-class throughout; the existing diagnosis is preserved, not overwritten.

**The reading.** v5–v7 built their trapping wall by *achiral* wall-replace ("snap" genesis — full
`seed_sech_v_inc` + unknot-sector replace at core, `research/2026-06-08_electron-genesis-snap-prereg.md:65`). An
achiral `Γ=−1` wall is a **NORMAL mirror**. If §3.1 holds, then a normal-mirror cavity **launders the circulating
handedness to zero every bounce** — and the three separate v5–v7 failures collapse into **one mechanism**:

1. **`w_pol ≡ 0`** — the de-novo poloidal "3" never self-assembles (`research/2026-06-10_graft-v4-photon-helicity_result.md:40,120,183`,
   "12/12 zeros"; graft-v2 full run gives `(w_tor, w_pol) = (0,0)`, `datasheet_draft.md:141`);
2. **the 3→1 decoherence** — the (2,3) winding collapses to `(4,0)` / `(0,0)`, the poloidal-3 not persisting (same
   reads);
3. **the v7 standing-wave failure** — "no clean de-novo `L_ω` lock yet" (`datasheet_draft.md:166`).

If the wall is a normal mirror, all three are the **same** statement: *the circulating handedness that IS the
winding cannot survive in an achiral cavity.* The handedness averages to zero per round trip, so `w_pol` reads zero,
the "3" decoheres, and no chiral standing wave locks. **The hypothesis:** the electron requires a **CHIRAL cavity**
(a cholesteric-class wall), because only a chiral mirror preserves the circulating handedness — and that circulating
handedness **is** the (2,3) winding and **is** the charge sign. The achiral snap shell was the wrong mirror.

**Why this is not yet a verdict:** §3.1 is optics for *electromagnetic* circular polarization; the (2,3) winding is a
*Cosserat-fibre* quantity (`full-electron-transverse-selftrap-result.md:41,43` — "structurally not a Maxwell-field
(E,H) observable … a Cosserat-fibre quantity"). That the EM handedness-laundering theorem transfers to the Cosserat
sector is **assumed, not shown** — exactly the kind of cross-sector transfer §2.2 also flags. So this competes with
A46+dephasing on equal footing until the §5 probe is run.

### 3.3 The datasheet map (one table — hypothesis-class mapping)

Reading the electron as a **chiral Fabry–Perot cavity**, every device property maps to a cavity property:

| device property | chiral-cavity reading | class / anchor |
|---|---|---|
| **wall** | the **chiral mirror** (cholesteric-class `Γ=−1` boundary) | hypothesis-class; the mode-selecting `Γ=−1` wall is canonical (`66:87` via graft prereg `:84`) |
| **(2,3) winding** | the **bounce pattern** at the slat/pitch angle `ψ` (§2.3) | hypothesis-class; `ψ = arctan(3/(2φ²))` phasor / `arctan(3/(2·2.27))` real-space |
| **mass** | the **round-trip** — the Compton clock `ω_C = c/ℓ_node` = the cavity **free spectral range** | Compton clock canonical (`theorem-3-1-q-factor.md`); FSR identification hypothesis-class |
| **charge sign** | the **mirror's preserved handedness** | canonical: "Charge sign **= handedness**" (`datasheet_draft.md:47`) |
| **α** | the **per-bounce leak** = `Z₀/(4π)` per spinor cycle = the cavity **finesse** statement | canonical (verbatim below) |
| **precedent** | the **H₂⁺ two-mirror Fabry–Perot** = licensed canon language | canonical (verbatim below) |

**α as a mirror-finesse statement (Theorem 3.1', verbatim, `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:36,38,40`):**

> "Therefore the Q-factor at the impedance-matched boundary `R = Z₀/(4π)`: $Q_{\text{tank}} = \frac{Z_0/(4\pi\alpha)}{Z_0/(4\pi)} = \frac{1}{\alpha}$ … the tank's reactance divided by its natural-per-cycle dissipation impedance is exactly the reciprocal of the fine-structure constant."

The radiation impedance is `Z₀/(4π)` **"averaged over one full observable Compton cycle"** (`dama-matched-lc-coupling.md:80-83`,
verbatim). Read as a cavity: the **finesse is `1/α`**, and `α` is the **per-bounce (per-spinor-cycle) leak fraction**
— the fraction of the circulating energy that escapes the chiral mirror each round trip. The electron is a cavity of
finesse `≈ 137`.

**The H₂⁺ two-mirror precedent (licensed canon language, verbatim, `first-principles-bond-force-constants.md:19,25`):**

> ":19 A covalent bond is a **loaded Fabry–Perot cavity** formed between two atomic resonators. The bond distance
> `d_eq` is the *eigenvalue* — the cavity length at which a standing electron wave satisfies the round-trip phase
> condition … :25 For a single electron bouncing between two atomic mirrors (e.g., H$_2^+$), the standing wave
> condition gives … (one-electron Fabry–Perot eigenvalue)."

The corpus **already** describes a bound electron as an electron *bouncing between two mirrors* in a Fabry–Perot
cavity — the H₂⁺ one-electron eigenvalue. The chiral-cavity reading of §3.2 is the **single-particle** version of
exactly that licensed picture: the electron is its own one-mirror cavity, the mirror chiral, the round trip the
Compton clock, the finesse `1/α`. **What §3.2 adds is the one word the H₂⁺ picture does not need but the free
electron does: the mirror must be *chiral*.**

<!-- SECTION 3 -->

## 4. THE DARK-SECTOR ONE-LINER

<!-- SECTION 4 -->

## 5. OWED-NUMBERS TABLE

<!-- SECTION 5 -->

---

## Appendix — anchors verified this session (verify-before-cite log)

<!-- APPENDIX -->
