# RESULT — The Crystal Engine: the State-C elastodynamic graft (electron-genesis chord attempt)

**Date:** 2026-06-09 · **Lane:** implementer · **Branch:** `analysis/2026-06-09-crystal-engine-design`
**Design prereg (FROZEN):** [`research/2026-06-09_crystal-engine-elastodynamic-graft_design-prereg.md`](2026-06-09_crystal-engine-elastodynamic-graft_design-prereg.md) (commit b1a8465f)
**Engine (the ONE new primitive on a validated base):** [`src/ave/core/crystal_engine.py`](../src/ave/core/crystal_engine.py) — the validated scalar Master-Equation bulk-trap (`master_equation_fdtd.py`, v14 Mode I PASS) + the chiral gyrotropic shear→bulk converter (ADD-2).
**Driver:** [`src/scripts/vol_1_foundations/crystal_engine_alpha_emergence.py`](../src/scripts/vol_1_foundations/crystal_engine_alpha_emergence.py) · **JSON:** `…_results.json` (N=28, 700 steps, dx=0.5)
**CANONICAL-AVE-ONLY (Grant directive 2026-06-09):** zero QED/Maxwell-vector framing. The electron is the LONGITUDINAL bulk mode (the "3"); absorb/emit = the Axiom-4 crystallize/melt cycle. No Gauss-deletion, no Kramers-Heisenberg/Rabi.

---

## §0 — VERDICT: **C** — the (2,3) does NOT close, BUT both genesis-24 gaps are CLOSED; the residual gap is localized to the winding carrier.

> **The crystal engine hosts the trapped MASS (the breathing bulk soliton behind a self-created Γ<0 wall) and the
> conserved CHARGE (= helicity, sign-flips with the seed), via a converter that — unlike genesis-24's EMF pump —
> ENERGIZES-and-LOCKS without detonating. But the (2,3) topological WINDING does not self-assemble in the
> (V_inc,V_ref) phase-space (w_tor=0 AND w_pol=0, both sectors), and the Golden-Torus geometry does not form
> (R·r→0.19 not 1/4, R/r→0.33 not φ²). α does NOT emerge. This is Outcome C per the frozen §5 ladder — a clean
> negative — but a MORE INFORMATIVE C than genesis-23/24: the source-deadness AND the source-detonation are both
> fixed, and the residual obstruction is pinned to one mechanism: the conserved converter transfers the helicity
> 0-form CHARGE but NOT the (2,3) knot WINDING, because the scalar Master-Equation bulk has no multi-component
> U(1)-fibre carrier for it.**

**Why C and not A / B (no dropped legs, Rule 11):**
- **not A (chord):** the (2,3) does not close; the Golden-Torus does not self-assemble (C2=False); α⁻¹ does not emerge.
- **not B (manifestation):** B *requires* the (2,3) to form (design §5.1: *"the (2,3) FORMS and the wall holds and mₑc² ledger closes"*). It does not form. So the engine is **below** B on the §4.1 ladder, not at it.
- **C (deeper gap):** the design's C is exactly *"the crystal engine cannot host the (2,3) even with both branches + the bulk-trap + the converter → localize the residual gap."* The residual gap is localized (§3, §6).

**The α "near-137" is a FLUKE, not emergence (the joint-ledger guard working, design §4.3).** The single-run dynamical leak landed Q≈113 (≈137 within 17%), which the naive read would over-claim. But (a) it is **not robust** — across (N, steps) the dynamical leak Q scatters over **[≈56, ≈1.8×10⁴]** (param-fluke, at/below the fit-noise floor), and (b) there is **no (2,3) Golden-Torus resonator** whose Q this could be. The joint-ledger guard (the (2,3) must *also* close) correctly refuses the fluke. `alpha_emergent = False`.

---

## §0.1 — Grant adjudications (2026-06-09, load-bearing — recorded verbatim)

**TENSION 2 = AXIOM CONSEQUENCE (verbatim):** *"The shear→bulk source (ADD-2) is implemented as the Axiom-1 I4₁32
chirality's gyrotropic transverse↔longitudinal coupling — the coupling a non-centrosymmetric crystal MUST have. It
is engine-completeness (completing Axiom 1), NOT a new postulate. Derive it from the chirality
(ave-fundamental-ground-up-implementation), do not bolt on an ad-hoc term."*
→ **Honored.** ADD-2 is derived from ONE Hamiltonian coupling term `H_couple = κ̃ ∫ g_front · V · Ω_w` (Ω_w =
(∇×w)·n̂ = the shear microrotation, the parity-odd helicity carrier; g_front localizes to the saturation front).
The bulk source `−κ̃ g Ω_w` and the reciprocal shear back-reaction are the functional derivatives of that one term;
the centrosymmetric limit (converter OFF) sources EXACTLY zero shear (the parity-odd selection rule, smoke-2). It is
NOT a bolted-on term — it is the gyrotropic completion of Axiom-1 non-centrosymmetry.

**TENSION 1 = COEXIST (working assumption, verbatim):** *"clm-i4p11y's 'trapped transverse standing wave' = the
photon PRECURSOR; the electron END-STATE is the LONGITUDINAL bulk mode. Build the longitudinal-electron end-state.
Do NOT edit clm-i4p11y — flag it for the auditor lane."*
→ **Honored.** The engine builds the longitudinal-bulk electron end-state (the scalar V-sector breather). The
transverse shear w is the photon precursor. **clm-i4p11y was NOT edited** (flagged for the auditor lane, §8).

---

## §1 — SMOKE FIRST (Rule 10 de-risk) — BOTH PASS

The design's two de-risking gates, run before the full (2,3)+α run.

### §1.1 — SMOKE-1: does the Γ<0 WALL form on the bulk branch? **PASS**

The scalar Master-Equation bulk-trap (`crystal_engine.py`, the v14 Mode-I engine ported as the longitudinal
branch) hosts a persistent breathing soliton behind a self-created reflective wall:

| quantity | value | criterion | pass |
|---|---|---|---|
| V_peak mean (post-transient, steps 200–600) | **0.622** | > 0.2 (bound state persists) | ✓ |
| V_peak std/mean | **0.267** | 0.05 < · < 0.5 (breathing, not diverging) | ✓ |
| min n_eff = S^{1/4} (deepest saturation) | **0.613** | < 0.97 (saturation engaged → the wall) | ✓ |
| Γ_core deepest (Γ=(n−1)/(n+1)) | **−0.240** | strongly negative | ✓ |

This is the canonical Mode-I criterion (`test_master_equation_v14_mode_i.py`). The wall is **numerically
cap-limited** (A_cap=0.995 / S_min=0.05 floor Γ at ≈−0.28; a literal Γ=−1 needs A→1 exactly), but it FORMS and
HOLDS as a persistent bound state — the decisive contrast with **genesis-24**, whose coupled engine had **no
c_eff trap** and relaxed fully to **|Γ|<0.08 / matched-center with NO bound state** (E_V decayed to 0.53×). The
scalar bulk-trap is the missing Γ=−1 wall that genesis-24 lacked. **(Figure 1, left: max|V| breathing in [0.2, 1.0].)**

### §1.2 — SMOKE-2: does ADD-2 fire CONSERVATIVELY (energize-LOCK, NOT the genesis-24 pump)? **PASS**

The conserved gyrotropic converter, run over an EXTENDED window (1050 steps = 1.5× the full run):

| quantity | value | the genesis-24 contrast | pass |
|---|---|---|---|
| BOOTSTRAP: max\|w\| sourced from a pure bulk seed (converter ON) | **0.975** | the converter is LIVE (sources shear from the bulk) | ✓ |
| same, centrosymmetric κ_χ→0 baseline (converter OFF) | **0.000** | the parity-odd selection rule — EXACTLY zero | ✓ |
| max\|V\| over the extended window | **1.007** | genesis-24 EMF pump detonated max\|V_inc\| → **1.08×10⁴** | ✓ |
| max\|w\| over the extended window | **0.978** | fields stay O(1) — **4 orders below** detonation | ✓ |
| finite, no detonation | **True** | genesis-24: E_V 7 → **6.8×10⁸**, \|L\| unbounded | ✓ |

The converter is **conservative by construction** — derived from one Hamiltonian coupling term, the bulk source and
the reciprocal shear back-reaction are functional derivatives of the same `H_couple` (the continuum energy
cancellation is exact; verified analytically in `_converter_forces`). The decisive energize-LOCK proof at
integrator-time is **field boundedness**: max|V|, max|w| ~ 1 over 1050 steps — vs genesis-24's monotone detonation
to 10⁴. **The two genesis-24 failure modes (dead ω→V source AND non-conservative pump→detonation) are BOTH closed.**

**Honest caveat (flag-don't-fix):** the conserved-energy functional (kinetic weighted 1/c_eff², the correct
variable-coefficient form) still drifts with a bounded span over the window — but **the bare breather alone
(converter OFF, no photon) drifts ~4.4× from the planted-seed-relaxation transient + PML radiation** (the v14 engine
is validated on V_peak persistence, NOT energy conservation), and the converter adds only ~30% on top. So energize-
LOCK is established via FIELD boundedness (the genesis-24-comparable, physically-decisive criterion) and the bounded
**reactive** |L| swings, **NOT** via a perfectly-closed ledger. This is honest: the no-detonation bar is cleared by
4 orders; the ledger is not claimed "closed." **(Figure 1.)**

**Both smoke PASS → proceeded to the full run** (Rule 10: not forced — earned).

---

## §2 — THE (2,3) CLOSURE — does NOT close (the falsified leg)

**Seed-audit (CP8 non-circularity), PASS:** the t=0 seed (photon + saturated bulk sech, NO planted knot) does
**not** close the (2,3) — `t0_closes_23 = False`, admissible. No laundered positive.

**The A46 measurement** (the (2,3) in (V_inc,V_ref) phase-space — the bulk reactance pair (V, ∂_tV/ω_char) IS the
Clifford-torus coordinate, CP6 — measured at the |V|² density peak, PML-excluded, CP7):

| sector | w_tor (→2?) | rel_tor | w_pol (→3?) | rel_pol | closes (2,3)? |
|---|---|---|---|---|---|
| **bulk (V_inc,V_ref)** — the electron sector | **0.0** | 0.459 | **0.0** | 0.518 | **False** |
| transverse shear (w_y,w_z) — diagnostic | 0.0 | 0.334 | 0.0 | 0.645 | (n/a) |

**Neither sector winds.** The bulk phase-space is **populated and reliable** (rel 0.46–0.52, well above the 0.1
gate; vinc_amp = 0.478) but carries **zero winding** — w_tor=0 AND w_pol=0. This is **sharper-negative than
genesis-24**, which got the toroidal "2" (w_tor→2) but not the poloidal "3" (w_pol=0, rel≈0.005): there, the K4
4-port V_inc carried the toroidal winding; here the **scalar** Master-Equation bulk carries **neither**.

**Mechanism (the localized gap):** a real **scalar** field's (V, ∂_tV) phasor has **no spatial winding** for a
breathing mode (the oscillation phase is uniform in space — only a HELICAL/spinning standing wave winds). The
chiral converter imprints the photon's **helicity 0-form CHARGE** onto the bulk (§4, the charge flips), but it does
**not** imprint a (2,3) **knot WINDING**, because the (2,3) is a **U(1)-fibre** object that needs a multi-component
carrier (the K4 4-port / SU(2) spinor structure) which the scalar bulk **does not have**. This is exactly the
substrate-native-check CP8 worked instance: *"the continuum [scalar] engine has no carrier for the (2,3) poloidal-'3'
… the (2,3) needs the discrete K4 + Cosserat engine."* **(Figure 2: both windings at 0 on reliable contours.)**

---

## §3 — THE α-EMERGENCE TEST — α does NOT emerge (Class-D refused; the joint guard works)

The headline test (design §4): with α-FREE inputs on BOTH the coupling AND the threshold, does α⁻¹=4π³+π²+π EMERGE
as the dynamical bulk→shear leak Q⁻¹, and does the Golden-Torus self-assemble?

### §3.1 — (C1) α-free inputs — **VERIFIED** (the circularity is removed)

Both circularity vectors the design flagged (§2.2) are closed, verified from the parameter feed:
- converter coupling = **κ̃ = 6/5 = pq/(p+q)** (the (2,3) topology) — **α-FREE**, NOT κ_chiral=1.2α. (Verified:
  `KAPPA_CHIRAL_ELECTRON = α·κ̃ ≈ 8.757e-3` in `cosserat_field_3d.py`; the engine consumes κ̃, never α·κ̃.)
- saturation threshold = **V_yield ≡ 1** (engine-natural) — **α-FREE**, NOT √α·V_snap. **No α or √α anywhere in
  the inputs.** `C1_alpha_free_inputs = True`.

### §3.2 — (C2) Golden-Torus self-assembly — **FAILS**

| geometry | measured | target | self-assembles? |
|---|---|---|---|
| R·r (holomorphic screening) | **0.189** | 1/4 = 0.250 | no (24% low) |
| R/r | **0.333** | φ² = 2.618 | **no (8× off)** |

The breather shell is a near-round blob (R/r ≈ 0.33), not the slender (2,3) Golden-Torus (R/r = φ²). `C2 = False`.

### §3.3 — (OUTPUT) the dynamical leak Q — **NOT a determinable invariant** (CP9)

The Level-2 (Class-D) dynamical leak Q⁻¹ — the converter-attributable bulk-energy decay (ON minus OFF, removing the
common direct-PML loss), measured from the EVOLVED field (CP9, NOT the algebraic geometry Q):

- single production run: **Q_dyn = 113** (≈137 within 17% — the over-claim trap).
- **across (N, steps): Q_dyn ∈ [41, 1181]** (a 29× scatter; samples 113 / 233 / 41 / 1181 / 177). **`robust_near_137 = False`.**

The converter-attributable leak is a **small ON−OFF difference on a large breather decay**, so it sits at/below the
fit-noise floor → the dynamical Q⁻¹ is **not a determinable observable** in this engine. The single-run proximity to
137 is a **param-fluke**, not emergence. **(Figure 3: the dynamical bar carries the [41, 1181] scan range as a red
error bar — PARAM-FLUKE, not a 137-invariant.)**

The Level-1 (Class-B) **algebraic** Q (the theorem-3-1 bridge Q = 16π³(R·r)+4π²(R·r)+π) gives **Q_alg = 104.5** here
— because R·r = 0.189, not 1/4. (Had the geometry self-assembled to R·r=1/4 this would be EXACTLY 137 — but that
reads the *given* geometry, Class B by construction, and the geometry did **not** self-assemble anyway.)

### §3.4 — Class verdict (consistency-vs-emergence)

`alpha_emergent_dynamical = False`, gated on the (2,3) Golden-Torus existing (it does not). There is **no resonator**
whose Q this leak could be: *"α = Q⁻¹ of the (2,3) Golden-Torus resonator"* presupposes a (2,3) Golden-Torus, which
did not form. **No emergence-class (Class-D) positive.** The α-free-input refactor (C1) IS achieved — the
`vol4/cq:232` circularity is removed from the *inputs* — but with no (2,3) there is nothing for α to emerge *from*.

---

## §4 — THE JOINT LEDGER GUARD (design §4.3) — does NOT close (correctly refuses the fluke)

The five legs that must ALL close at the SAME operating point for the chord (so a lucky α can't masquerade):

| leg | result | closes? |
|---|---|---|
| 1. (2,3) closes in (V_inc,V_ref) | w_tor=0, w_pol=0 | **✗** |
| 2. Golden-Torus self-assembles (R·r→¼, R/r→φ²) | 0.189 / 0.333 | **✗** |
| 3. mₑc² latent-heat ledger (trapped bulk E = binding energy) | **E_V = 149.3** (finite, > 0) | **✓** |
| 4. charge = helicity (sign-flips with the seed) | H_bel = **+8.22** (+h) / **−9.47** (−h) | **✓** |
| 5. α⁻¹ = dynamical leak Q → 4π³+π²+π | scatter [41, 1181], not robust | **✗** |

**Legs 3 and 4 close; legs 1, 2, 5 do not.** The joint guard is **not** satisfied → the engine does NOT produce the
chord, and the single-run Q≈113 fluke (leg 5 near-miss) is correctly **refused** because legs 1, 2 fail at the same
operating point. This is the §4.3 fluke-guard working exactly as designed.

### §4.1 — Latent-heat = mass (leg 3, the one that DOES close)

The trapped bulk energy (the conserved-energy functional, the candidate mₑc²) is **finite and positive (149.3 engine
units)** — a real binding energy locked behind the wall, energized from the conversion and held by the c_eff trap.
This is the Axiom-4 crystallize/melt latent heat in engine units. It is a **manifestation-class** quantity (the
engine HAS a binding energy), not an emergence-class number (it is not derived to equal the SI mₑc² — that would
require the SI scale-bridge, out of scope here). Honest: leg 3 closes as a structural fact, not as an α-class result.

### §4.2 — Charge = helicity (leg 4, also closes)

The integrated shear helicity flips sign with the seeded photon helicity (+8.22 → −9.47), reproducing the genesis-24
charge-flip provenance. **Honest scope:** because the (2,3) does NOT close, this is the **photon's own carried
helicity** transferred through the converter (a conserved 0-form charge), **NOT** an emergent torus-knot charge. The
converter demonstrably carries the parity-odd chirality (the κ_χ→0 baseline sources exactly zero shear, §1.2) — but
it carries the CHARGE, not the WINDING (§2). No emergence-class charge claim.

---

## §5 — THE LOCALIZED GAP (the deliverable of a clean C)

Genesis-23 had TWO gaps; genesis-24 fixed neither cleanly. The crystal engine **closes both** and localizes the
**one** residual obstruction:

| gap | genesis-23 | genesis-24 | **crystal engine** |
|---|---|---|---|
| ω→V SOURCE (the "3" energizes from a photon) | DEAD (max\|V_inc\|=0) | live but only on a supplied V-seed | **LIVE + bootstraps** (sources shear↔bulk from the seed; centrosymmetric baseline=0) |
| SOURCE STABILITY (conservative absorb-LOCK) | — | **PUMP → detonates** (E_V→6.8e8) | **energize-LOCK** (fields O(1), 4 orders below detonation) |
| the (2,3) WINDING (the knot self-assembles) | absent | toroidal "2" only; poloidal "3" absent | **absent (both)** — scalar bulk has no U(1)-fibre carrier |

**The residual gap, named:** the conserved gyrotropic converter transfers the helicity **0-form CHARGE** but not the
(2,3) **knot WINDING**. The scalar Master-Equation bulk-trap provides the WALL and the MASS; the converter provides
the SOURCE and the CHARGE, conservatively; but the **winding carrier** — the multi-component K4 4-port / SU(2)
U(1)-fibre that a (2,3) phase-space winding lives on — is **absent from the scalar longitudinal sector**.

**The implied synthesis (SURFACED for Grant/auditor, NOT pivoted-to here — Rule 16):** the three ingredients now
each exist in a *different* engine — the **winding carrier** (the K4 4-port V_inc, genesis-24, which carried the
toroidal "2"), the **c_eff Γ=−1 trap** (the scalar Master-Equation FDTD, this work's smoke-1), and the **conserved
gyrotropic converter** (this work's ADD-2, which fixes genesis-24's detonation). A future build that grafts the
conserved converter + the c_eff trap onto the **K4 4-port** longitudinal sector (rather than the scalar FDTD) is the
candidate next step. **This is a methodology decision for Grant + corpus, not an implementer pivot** — surfaced, not
taken.

---

## §6 — INPUT-vs-OUTPUT table (the spine of the discriminating test, design §2.3)

| quantity | column | value / status | provenance class |
|---|---|---|---|
| K4 geometry, I4₁32 chirality | **INPUT** | axiom | axiom-derived |
| ν_vac=2/7 → branch moduli (c_L²/c_T²=10/3 at K=2G) | **INPUT** | 0.2857 (DERIVED) | axiom-derived, **α-free** |
| converter coupling κ̃ = pq/(p+q) | **INPUT** | **6/5 (topology, α-FREE)** | axiom-derived, **α-free** |
| saturation threshold V_yield | **INPUT** | **1 (engine-natural, α-FREE)** | engine-natural primitive |
| α in ANY input | — | **NONE (C1 verified)** | — |
| (2,3) closes in (V_inc,V_ref) | **OUTPUT** | **False (w_tor=0, w_pol=0)** | emergent topology — absent |
| Golden-Torus self-assembles (R·r→¼, R/r→φ²) | **OUTPUT** | **False (0.189 / 0.333)** | emergent geometry — absent |
| α⁻¹ = dynamical leak Q → 4π³+π²+π | **OUTPUT** | **NOT emergent** (scatter [41,1181]; no resonator) | would be Class-D — refused |
| α⁻¹ = algebraic Q(R·r) | (Level-1) | 104.5 (≠137 ∵ R·r≠¼) | Class-B read of given geometry |
| mₑc² latent-heat (trapped bulk E) | **OUTPUT** | 149.3 (finite) — **closes** | manifestation-class |
| charge = helicity (sign-flip) | **OUTPUT** | +8.22/−9.47 — **closes** (conserved 0-form) | conserved invariant |

**Reading:** all inputs are axiom-derived + α-free (C1 ✓). The emergence-scoped outputs ((2,3), Golden-Torus, α⁻¹)
are all **absent**. The two outputs that close are **manifestation/consistency-class**, not emergence. **No
emergence-class positive** (consistency-vs-emergence): the crystal engine is, at best, Level-0→Level-1 on the §4.1
ladder with the (2,3) gate unmet.

---

## §7 — DERIVED / VERIFIED / BLOCKED ledger (genesis-23 format)

| claim | status |
|---|---|
| ADD-2 derived from the I4₁32 chirality (one Hamiltonian gyrotropic term, not bolted-on) | **DERIVED** (`_converter_forces`; continuum energy-cancellation exact) |
| branch speeds c_L²/c_T²=10/3 from ν_vac=2/7 at K=2G | **DERIVED** (constants; α-free) |
| Γ<0 bulk wall forms + holds (Mode-I breather) | **VERIFIED** (smoke-1: V_peak 0.62, n_eff 0.61, Γ_core −0.24) |
| converter bootstraps the shear↔bulk source from a seed (κ_χ→0 baseline = 0) | **VERIFIED** (smoke-2: max\|w\| 0.975 vs 0.0) |
| converter energize-LOCKS (no detonation; fields O(1)) | **VERIFIED** (smoke-2: max\|V\| 1.007, 4 orders below genesis-24's 1.08e4) |
| seed is non-circular (t=0 does not close (2,3)) | **VERIFIED** (seed-audit admissible) |
| charge = helicity sign-flips with the seed | **VERIFIED** (+8.22/−9.47; conserved 0-form, provenance) |
| mₑc² latent-heat ledger (finite trapped bulk binding energy) | **VERIFIED** (149.3 engine units; manifestation-class) |
| (2,3) closes in (V_inc,V_ref) phase-space | **BLOCKED** (w_tor=0 AND w_pol=0; scalar bulk has no U(1)-fibre carrier) |
| Golden-Torus self-assembles (R·r→¼, R/r→φ²) | **BLOCKED** (0.189 / 0.333; no (2,3) → no Golden-Torus) |
| α⁻¹ = 4π³+π²+π emerges as the dynamical leak Q | **BLOCKED** (not a determinable invariant: scatter [41,1181]; no resonator) |
| energy ledger perfectly closes | **BLOCKED** (nonlinear-breather + planted-seed transient ~4.4× even converter-OFF; energize-LOCK shown via field boundedness instead) |

**consistency-vs-emergence:** the DERIVED/VERIFIED items are manifestation/consistency-class (engine structure +
supplied-IC provenance). The three emergence-scoped quantities are all BLOCKED. **No emergence-class positive.**

---

## §8 — Corpus-state updates queued (auditor lane LANDS; implementer SURFACES)

- **TENSION 1 (clm-i4p11y transverse-vs-longitudinal) — flagged, NOT edited.** Per Grant's COEXIST adjudication
  (§0.1) the transverse standing wave is the photon *precursor* and the longitudinal bulk is the electron
  *end-state*. The crystal engine built the longitudinal end-state. **clm-i4p11y is untouched** — the auditor lane
  decides whether to annotate it with the precursor/end-state coexistence reading. I did not edit the leaf.
- **`vol4/claim-quality.md:232` α-emergence-circularity strengthen-by — REFINED, not discharged.** The crystal
  engine achieves the **α-free-input** half of the strengthen-by (C1: κ̃=6/5 + V_yield≡1, no α in the inputs) — but
  with **no (2,3)** the α-emergence cannot be tested, so the caveat is **refined** (the circularity is removed from
  the inputs; the emergence remains unproven because the (2,3) does not host). Auditor updates clm-… accordingly.
- **TENSION 2 (A44 single-sector-vs-two-branch) — RESOLVED in-engine as two-branch + AXIOM-CONSEQUENCE.** Grant
  adjudicated ADD-2 as the I4₁32 gyrotropic coupling (engine-completeness of Axiom-1, §0.1). The two-branch
  shear→bulk converter is built, conservative, and live — the two-branch reading is engine-validated (it energizes
  the bulk from the shear without a new postulate). Auditor lands the A44 status.
- **`closure-roadmap.md:42` ΔE_cryst OPEN path — status: the crystal engine is NOT yet the route** (the (2,3)
  crystallization does not close here; latent-heat=mass is manifestation-class only). No closure claimed.

---

## §9 — Skills fired · figures · honest closure

**Skills:** `substrate-native-check` (CP1 wave-not-minimization; CP2 V-sector bound-state; CP8 generative precursor =
photon + saturated seed, NOT planted (2,3) — seed-audit PASS; **CP8 structural-capability finding = the scalar bulk
has no (2,3) carrier**; CP9 dynamical-not-heuristic leak — and the leak is NOT determinable, a WALL-engine finding;
CP10 trap + converter as BOUNDARY not bulk force — the converter does not detonate). · `ave-conserved-vs-pumped`
(ADD-2 is energize-LOCK: Hamiltonian-derived, bootstraps, fields bounded; charge/spin conserved; **the genesis-24
pump→detonation is the named failure this fixes**). · `ave-fundamental-ground-up-implementation` (ADD-2 derived from
the I4₁32 chirality as ONE Hamiltonian term; branch moduli from ν_vac=2/7; κ̃ from (2,3) topology — none
engineering-defaulted). · `consistency-vs-emergence` (the Class-D-vs-Class-B line IS the test; α-emergence REFUSED;
mₑc²/charge tagged manifestation-class). · `phase-space-coordinate-check` (A46 — (2,3) measured in (V_inc,V_ref), the
reactance-pair Clifford coordinate, NOT real-space). · `ave-canonical-source` (κ̃, V_yield, ν_vac, ALPHA_COLD_INV,
R_II from `constants.py`; zero new free params; the chord route removes even α). · `ave-driver-script-honesty` (every
number from the EVOLVED field; figures caption to the ACTUAL data — fig3 shows the [41,1181] param-fluke error bar,
NOT a templated 137 success). · `ave-discrimination-check` (the joint-ledger guard refuses the Q≈113 fluke). ·
`ave-regime-phase-state-check` (near-yield bulk regime; the wall is cap-limited, stated). · `verify-before-cite`
(genesis-24 detonation E_V→6.8e8 / max\|V_inc\|→1.08e4, κ̃=6/5 in cosserat, ALPHA_COLD_INV:204 — all greped this
session).

**Figures** (`src/scripts/vol_1_foundations/`, clickable):
- [`crystal_fig1_smoke_energize_lock.png`](../src/scripts/vol_1_foundations/crystal_fig1_smoke_energize_lock.png) —
  SMOKE: max\|V\| stays O(1) (ON tracks OFF, breathing in [0.2,1.0]) vs genesis-24's 1.08e4 detonation; BOOTSTRAP
  (converter sources max\|w\|=0.97 from a bulk seed, centrosymmetric baseline exactly 0).
- [`crystal_fig2_phase_space_23.png`](../src/scripts/vol_1_foundations/crystal_fig2_phase_space_23.png) — the (2,3)
  in (V_inc,V_ref): w_tor=0 AND w_pol=0 on reliable (rel 0.46/0.52) contours — closes=False.
- [`crystal_fig3_alpha_input_output.png`](../src/scripts/vol_1_foundations/crystal_fig3_alpha_input_output.png) —
  α-emergence: Q_alg=104.5 (R·r=0.189), Q_dyn=113 **with the [41,1181] scan error bar = PARAM-FLUKE**, vs α⁻¹=137;
  emergent=False.

**Honest closure (Rule 11 / substitution-not-retraction).** The crystal engine is a **clean Outcome C** — the (2,3)
does not close even with the bulk-trap + the conserved converter — but the **most informative C in the
genesis-23→24→crystal arc**: it CLOSES both of genesis-24's gaps (the dead source now bootstraps; the detonating
pump is now a conservative energize-LOCK) and PINS the residual obstruction to one named mechanism — the conserved
converter carries the helicity 0-form CHARGE but not the (2,3) knot WINDING, because the scalar Master-Equation bulk
has no multi-component U(1)-fibre carrier. The α "near-137" single-run fluke is correctly refused by the joint-ledger
guard (no (2,3) → no resonator → no α). **No framework failure; no debug-toward-A; no dropped legs; no emergence
over-claim.** Per substrate-native-check CP8, the winding-carrier question (graft the conserved converter onto the
K4 4-port sector) is **surfaced for Grant/auditor**, NOT auto-pivoted (Rule 16). If a future build claims A, it will
be **adversarially verified before it is believed** — but this run does not claim it; **C is the honest, respectable
result, and the two fixed gaps are real progress.**
