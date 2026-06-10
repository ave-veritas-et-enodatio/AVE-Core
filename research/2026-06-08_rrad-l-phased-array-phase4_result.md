# Result — phased-array u-sector compressional rectification (dark-wake thrust, Phase 4, the closing test)

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-rrad-l-darkwake` (Phase 4; same branch as Phases 1–3)
**Prereg**: [`2026-06-08_rrad-l-phased-array-phase4_prereg.md`](2026-06-08_rrad-l-phased-array-phase4_prereg.md)
**Driver**: [`src/scripts/vol_4_engineering/rrad_l_phased_array_compression.py`](../src/scripts/vol_4_engineering/rrad_l_phased_array_compression.py)
**Phase-3 result (the negative this answers)**: [`2026-06-08_rrad-l-stickslip-phase3_result.md`](2026-06-08_rrad-l-stickslip-phase3_result.md) (OUTCOME B by SECTOR MISMATCH — latch in ω, momentum in u)
**Canonical latch leaves**: [peierls-nabarro-paradox.md](../manuscript/ave-kb/vol2/appendices/app-b-paradoxes/peierls-nabarro-paradox.md) (clm-ghs75o, STZ thixotropic re-freeze) + [saturation-operator.md](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/saturation-operator.md) (clm-gdd70j, Bingham yield τ_y)

> 🟠 **2026-06-09 REGIME-RESCOPE (Rule 12 — header-only addition; every line of the body below is PRESERVED VERBATIM).**
> **Governing discipline:** `ave-regime-phase-state-check`. **Adjudication:** Grant, 2026-06-09 (regime / phase-state discipline).
>
> **(a) This OUTCOME-B is a SUB-YIELD-LINEAR (u/compressional, time-symmetric-carrier) regime null = a WRONG-REGIME ARTIFACT, not a falsification — and the "ALL SECTORS EXHAUSTED" reach is the over-claim this header corrects.** Phase 4 matched the *sector* (u/P-wave, bulk_frac 0.585) but NOT the *regime*: rate-asymmetry / rectification can live ONLY in the BULK NEAR-YIELD (ruptured) regime, and this driver runs a time-symmetric carrier in the sub-yield-linear band — the genuine above-yield ruptured regime is BLOCKED here (the latch-ON velocity-Verlet goes numerically unstable for amp ≳ 2.2, §3 overdrive caveat). Where the Axiom-4 kernel is instantaneous and even-in-A, ∮ = 0 *by construction*. The doc's own "spatial focusing ≠ temporal rectification" IS the correct mechanism; the missing "temporal symmetry-breaker" it names is precisely the bulk-near-yield rate-asymmetry tested in (b). A null in a regime that forbids the effect is uninformative as a falsification (`ave-regime-phase-state-check`).
>
> **(b) The rectification question WAS subsequently closed in the correct (bulk near-yield) regime — by derivation.** Branch `analysis/2026-06-09-thixotropy-bulk-derivation` (2026-06-09, tip `5969bda1`; UNMERGED — cited by branch + date, not a HEAD path), **Outcome B**: the bulk relaxation time τ_bulk(ρ̄) = τ₀/√(1+ρ̄/(1−ρ̄²)) depends on the INSTANTANEOUS ρ̄ ONLY — no sign(dρ̄/dt) memory — so the bulk sat/desat channel has NO rate-asymmetry and cannot rectify a symmetric cyclic drive (dead-by-derivation; clm-7tynm2 walk-back upgrades from empirical → STRUCTURAL for the bulk channel). The bulk near-yield regime Phase 4 could not reach (overdrive instability) is exactly what that derivation closes.
>
> **(c) The in-doc mechanism finding REMAINS CORRECT.** The even-in-amplitude / time-symmetric-streaming + "spatial focusing is not temporal rectification" + "needs a temporal symmetry-breaker" diagnosis below is still the right EXPLANATION of WHY this regime nulls. The rescope is of the FALSIFICATION-STRENGTH interpretation, **not** the mechanics. The non-exotic beam-shaping thrust (path B, §4) is UNAFFECTED.
>
> **(d) Read all "ALL SECTORS EXHAUSTED" / "DEFINITIVELY DEAD" / "refuted across all sectors" / "warp/Alcubierre mechanical basis walks back"-strength language in this doc as REGIME-SCOPED per this header.** These sub-yield-linear nulls do NOT themselves carry a regime-independent falsification; the conclusion that the exotic *mechanical-rectification* (warp) route is unsupported SURVIVES, but its load-bearing basis is the bulk-near-yield derivation in (b), NOT these artifacts. Specific phrases swept (preserved verbatim in-body): the HEADLINE "**ALL SECTORS EXHAUSTED → exotic rectification DEFINITIVELY DEAD → warp/Alcubierre mechanical basis walks back**"; §0 "the exotic chiral/rectification thrust mechanism is refuted **across all sectors**"; §7 "deflated across all sectors" and "The exotic chiral/rectification thrust mechanism — and the warp/Alcubierre mechanical basis that rested on it — is refuted; the warp claim walks back"; §8 "retire the exotic dark-wake/warp-rectification thrust route".

> **HEADLINE — OUTCOME B (prereg §4B): sector-matched u-drive STILL does NOT rectify → ALL SECTORS EXHAUSTED → exotic rectification DEFINITIVELY DEAD → warp/Alcubierre mechanical basis walks back.**
> The Phase-3 sector mismatch is FIXED: the phased-array compressional drive lands the
> energy, the latch, AND the momentum observable all in the **u (translational/P-wave)
> sector** (`bulk_frac = 0.585 > 0.5`, vs the shear-dominated Phases 1–3). The u-sector
> Peierls-Nabarro / Bingham plastic latch **engages** (g_max up to 0.34, the focus
> reaches/crosses A_yield). And it **still does not rectify**: latch-ON vs latch-OFF
> directed momentum is **`latch_gain = 0.99`** — the latch adds *nothing*. The
> focused-vs-non-focusing contrast that DOES exist (`rect_ratio = 2.71`) is **pure
> beam-shaping radiation pressure** (present latch-OFF, scales with array gain), NOT
> exotic rectification. **Flat across the entire τ_relax sweep ×0.25→×4** (latch_gain
> ≈ 1.0 at every τ → no rescue band → not even a C) and **identical coupling-ON vs
> coupling-OFF**. With the **ω sector closed in Phase 3** and the **u sector closed
> here**, the exotic chiral/rectification thrust mechanism is refuted **across all
> sectors**. **The dual payoff stands: the same array beams a directional wake → the
> non-exotic beam-shaping thrust `F = G_geom·P_rad/c_shear` (path B) is real and scales
> with directivity.**

---

## 0. Headline (the prereg §4 verdict)

**B — still NO rectification, now SECTOR-MATCHED.** Phases 2–3 were ambiguous: maybe
rectification failed only because the chiral ω-source trapped the drive in the shear
sector, away from the `ρ⟨u̇²⟩` thrust momentum (Phase-3 FLAG-1). Phase 4 removes that
escape hatch — it drives the **u sector directly** with a phased array (direction from
the **phase gradient, not chirality**), co-locating drive + latch + momentum. The
result is **decisively B**:

Four load-bearing facts (each a guard against "inconclusive null" / "rescue-fill C"):

1. **The sector IS matched now (the Phase-3 fix worked at the sector level).** The
   focused compressional wake is **bulk/P-wave-dominated**: `bulk_frac = 0.585` (vs the
   shear-dominated `~0.0–0.3` of the chiral ω-source in Phases 1–3). The momentum
   observable `ρ⟨u̇²⟩`, the latch (reads u-strain, freezes u/u̇), and the drive are all
   in the **same u sector**. The Phase-3 sector-mismatch escape hatch is closed.

2. **The latch ENGAGES, and adds nothing (engaged-but-no-rect — the strongest B).**
   Focused, canonical τ: `g_max = 0.24` at N=28/focal=9 and **`g_max = 0.32` with the
   focus driven above yield** (`A²_focal = 1.09`, amp=2.0/focal=7). Yet directed
   momentum latch-ON vs latch-OFF is **`5.118` vs `5.147` → latch_gain = 0.994**. The
   latch is real, it grips at yield, and gripping the u sector does **not** rectify the
   u-momentum. (Compare Phase 3 amp=3.0: g_max=0.49, still no rect — same finding, now
   in the right sector.)

3. **No rescue band at ANY τ_relax (rules out C).** τ_relax sweep ×0.25 / ×0.5 /
   **×1.0 (canonical)** / ×2.0 / ×4.0 → latch_gain **0.99 / 0.99 / 0.99 / 1.00 / 1.00**.
   Flat at ≈1.0. There is **no** τ_relax (canonical or otherwise) at which the latch
   rectifies — so this is not "rectifies only when tuned" (C); it is "does not rectify,
   period" (B). The rescue-fill guard (prereg §3) is satisfied by absence.

4. **The focused-vs-random contrast is BEAM-SHAPING, not rectification.** `rect_ratio
   = |Tpp_focused|/|Tpp_random| = 2.71` — but this same ratio is present **latch-OFF**,
   it **equals the array directivity** (coherent delivers ~2.7× the forward momentum of
   incoherent), and it is the non-exotic beam-shaping path B. The exotic discriminator
   is `latch_gain` (the latch's contribution on top of radiation pressure) = **1.0**.

**Single mechanism (Rule 7) — why sector-matching still cannot rectify:** the measured
directed momentum is `ρ⟨u̇²⟩` **acoustic radiation pressure / streaming** — a 2nd-order,
**even-in-amplitude**, time-symmetric quantity (Phase-2 §0). The phased array breaks
*spatial* symmetry (focusing) but the carrier remains *time*-symmetric, so the focused
beam radiates forward by ordinary radiation pressure whether the latch is on or off.
The plastic latch, applied to a time-symmetric drive, freezes the u sector
**symmetrically** in time → no net directed plastic displacement → no DC contribution
beyond radiation pressure. **Spatial focusing ≠ temporal rectification.** Co-locating
the latch with the observable was necessary (Phase-3 lesson) but **not sufficient**: a
substrate rectifier still needs a *temporal* symmetry-breaker the carrier+latch do not
supply.

**Classification:** Class-B manifestation that produced a **null** on the exotic claim.
The non-exotic beam-shaping thrust IS a Class-B manifestation (any phased array does
it). NOT a Class-2 emergence claim either direction.

---

## 1. What was built (substrate-native-check applied)

Driver `rrad_l_phased_array_compression.py` — two new substrate-native pieces, coupling
ENABLED, plus the Phase-2 momentum/stress machinery reused verbatim (no constitutive
drift):

### 1.1 The phased-array u-sector compressional source (`PhasedArrayCompressionalSource`)

`N_elem` Gaussian emitter elements (sunflower/golden-angle placement) tile the
transverse plane at the source slab; **each drives u ALONG the propagation axis**
(longitudinal / compressional / P-wave) — a piston/transducer set, NOT a phenomenological
array model. Direction is set by **inter-element phase**, not chirality:

- **`focused` (ASYM drive):** `φ_n = k_L·(√(F²+r_n²) − F)`, `k_L = ω/c_L`, `c_L = √2`
  native (V_LONG) → all elements arrive in-phase at the focal point → **constructive
  interference = compression peak** (the u-sector excitation).
- **`random` (SYM control):** `φ_n ~ U(0,2π)` (seeded, averaged over 3 seeds) →
  incoherent, no focal peak → the **non-focusing control**.
- **`steered`:** linear phase gradient `φ_n = k_L·sinθ·y_n` → beam **tilts by θ** with
  no chirality (the phase-gradient steering demonstration).

Overwrites u at the source slab each step (Dirichlet piston BC), mirroring
`CosseratBeltramiSource`'s ω overwrite (`vacuum_engine.py:962`). Transverse u zeroed at
the slab → pure compression at the source.

### 1.2 The u-sector plastic latch (`PlasticStickSlipLatch`) — canonical, NOT the ω Lenz-freeze

The **translational/plastic** stick-slip, pulled from the canonical leaves directly
(ave-canonical-leaf-pull):

- **`peierls-nabarro-paradox.md` (clm-ghs75o):** the substrate "mechanically liquefies"
  under local shear above yield (a Shear Transformation Zone slips) and
  **"thixotropically re-freezes"** when the stress drops, trapping the configuration.
- **`saturation-operator.md` (clm-gdd70j):** the **Bingham plastic yield** — "the vacuum
  flows above τ_y = B_snap²/2μ₀"; `S(A) = √(1−(A/A_c)²)`.

(The `common/substrate-hysteresis-index.md` grouping that names these "Class 3" lives
only on the **unmerged** sibling branch `analysis/2026-06-08-hysteresis-index` — it is
**NOT** cited as canon here; the underlying leaves on main are.)

Implementation: a per-cell grip `g(r,t) ∈ [0,1]` — `g=1` re-frozen/stick (du/dt blocked,
holds the plastic displacement), `g=0` STZ-fluid/slip (u flows freely). It uses the
**IDENTICAL canonical machinery as Phase 3's StickSlipLatch** — operating-point lag A₀,
rate_slow threshold (slow crossing ⇒ thixotropic re-freeze), `sat = 1 − S(A₀)`,
backward-Euler memory at canonical τ_relax — with **only one change: the SECTOR**. A is
read from the compressional strain and the freeze acts on **u / u̇** (where the thrust
momentum lives), not ω / ω̇. This is exactly the prereg's sector-match fix: *same latch,
co-located observable.* **Zero tunable knobs** (τ_relax, A_yield, S, backward-Euler all
canonical).

### 1.3 Coupling ENABLED

`disable_cosserat_lc_force=False` (Phase 3 had it `True`) — the u↔ω coupling channel is
ON, the physical configuration. (This is the A28 "runaway-prone" legacy path; it ran
**stable** under the compressional drive in the measured regime, and the verdict is
**identical** coupling-ON vs coupling-OFF — see §3.)

---

## 2. Latch + speed provenance (DERIVED / canonical — the rescue-fill guard)

- **τ_relax** = `TAU_RELAX_NATIVE = ℓ_node/c = 1.0` native (`constants.py:335`; Ax1+Ax3,
  doc-59 §1). PINNED, not a bound. The τ_relax sweep ×0.25→×4 is a CLASSIFY-only
  diagnostic; the headline is at canonical τ.
- **A_yield = 1** — the Cosserat kernel's own zero (`epsilon_yield = 1.0`; S = √(1−A²) →
  0 at A=1), the canonical Γ=−1 saturation/Bingham-yield boundary (Axiom 4).
- **c_shear = c₀ = 1** native — transverse/photon speed (`G_VAC = ρ·c₀²` → √(G/ρ) = c₀).
- **c_L = √2** native — longitudinal/P-wave speed (`V_LONG = √(2G/ρ)`; constants.py),
  sets the focal phase delays.
- **G_geom** — the array directivity (focal field-concentration); Q-G42
  `V_yield^(apparatus) = E_yield^(substrate)/G_geom` (`trampoline-framework.md:455`). The
  phased array IS a `G_geom` realization: constructive interference concentrates the
  macro drive toward the local yield field.

All imported via `verify_constants` (ave-canonical-source Step 4); zero hard-coded
physics; zero tuned latch knobs.

---

## 3. NUMERICALLY VERIFIED (smoke; SIGNS / RATIOS / CONTRAST)

Representative run: N=28, pml=4, amp=2.0, λ=4, N_elem=16, focal=9, R_array=8,
6-cycle average, coupling ON, canonical τ. Random control averaged over 3 seeds.

| cell | Tpp (directed) | conv (ρu̇² stream) | A²_focal | g_max | bulk_frac |
|---|---|---|---|---|---|
| FOCUSED latch-ON | `+5.118` | `+5.154` | 0.46 | 0.239 | **0.585** |
| FOCUSED latch-OFF | `+5.147` | `+5.183` | 0.47 | 0.000 | 0.585 |
| RANDOM latch-ON (avg) | `+1.887` | `+2.167` | 0.48 | 0.340 | 0.581 |
| RANDOM latch-OFF (avg) | `+1.899` | `+2.180` | 0.48 | 0.000 | 0.581 |

- **latch_gain** = |Tpp_FOC_ON| / |Tpp_FOC_OFF| = **0.994** → the latch adds nothing.
- **rect_ratio** = |Tpp_FOC| / |Tpp_RND| = **2.71** → focusing/beam-shaping (latch-OFF
  too); equals the array directivity. (The RANDOM control does **not** null to zero —
  incoherent compressional emitters all push +x, so a radiation-pressure floor remains;
  the discriminating quantity is `latch_gain`, not `rect_ratio`.)

**τ_relax CLASSIFY sweep (canonical = ×1.0; rescue-fill guard):**

| τ_relax × | 0.25 | 0.5 | **1.0 (canon)** | 2.0 | 4.0 |
|---|---|---|---|---|---|
| latch_gain | 0.99 | 0.99 | **0.99** | 1.00 | 1.00 |
| rect_ratio | 2.72 | 2.72 | **2.71** | 2.55 | 2.71 |

→ **Flat. latch_gain ≈ 1.0 at every τ_relax → no rescue band → rules out C.**

**Above-yield engagement (coupling check, N=24 focal=7 amp=2.0):** `A²_focal = 1.09`
(focus crosses yield), `g_max = 0.32` (latch grips hard), and **latch_gain still 0.989**
→ engaged-but-no-rect, the strongest possible B (not "never engaged").

**Coupling ON vs OFF (same config):** latch_gain `0.989` (ON) vs `0.995` (OFF),
rect_ratio `3.89` vs `3.86`, bulk_frac `0.584` vs `0.583` → **identical**; the verdict
is robust to the coupling flag, and coupling-on (the physical config) is stable here.

**Reactance pair (Rule 10), FOCUSED:** C-store strain-energy `3.87e2`, L-store
`ρ⟨u̇²⟩ = 3.92e2` — both present and non-trivial (an active u-sector oscillator, not a
static snapshot). **Local clock (Rule 10):** at the top-A² interior sites
`A²_peak = 0.897` → `ω_local/ω_drive = √(1−A²) = 0.32` (the load-bearing u sites are
near saturation/clock-slowed — consistent with the latch engaging there, yet not
rectifying the far-field `ρ⟨u̇²⟩` momentum).

**Overdrive caveat (numerical, NOT physics):** at amp ≳ 2.2 the latch-ON velocity-Verlet
goes numerically **unstable** (|u| → 1e4, A² → 1e6) at the *canonical* τ only — a
stiff-integrator overdrive artifact, not rectification (the τ-sweep's other four points
stay clean at latch_gain ≈ 0.99). The driver's stability guard flags this **BLOCKED**;
the headline regime (amp ≤ 2.0, focus reaching/just-crossing yield) is the clean,
robust measurement.

---

## 4. DUAL PAYOFF — the non-exotic beam-shaping thrust (path B, reported regardless of A/B/C)

The same phased array beams a directional wake. The **non-exotic** beam-shaping thrust
`F = G_geom · P_rad / c_shear` (directivity × radiated power / slow shear speed) is real
and survives the exotic null:

- **Directivity** (the array gain): the coherent (focused) array delivers **~2.7×** the
  forward momentum of the incoherent (random) array (`rect_ratio` = directivity, momentum
  measure). It **scales with N_elem** (path-B array-gain): N_elem sweep `P_rad` =
  `2.2e-6` (N=4) → `1.7e-4` (N=8) → `1.4e-4` (N=16). The focal-concentration proxy
  `G_geom ≈ 4.4` is consistent but speckle-noisy; the **momentum-ratio directivity ≈ 2.7**
  is the defensible number.
- **Radiated power** `P_rad ≈ 1.4e-4` native (far-slab axial elastic energy flux).
- **Beam-shaping thrust** `F = G_geom·P_rad/c_shear ≈ 6.3e-4` native (c_shear = 1), or
  `≈ 4.4e-4` with the P-wave speed c_L = √2 (the wake is compressional). **SMOKE /
  native units — absolute magnitude (Newtons) BLOCKED** (same gate as Phases 1–3:
  converged radiating sim + source-current normalization).
- **Phase-gradient steering (no chirality):** the `steered` beam (θ=20°) produces a
  directional wake `Tpp = +5.74`, `bulk_frac = 0.586` — confirming **directionality from
  the phase gradient alone**, in the u sector, with no rotational chirality.

So the device's **honest** capability is a directional acoustic/compressional radiator:
`F ≈ N·P/c` (directivity × power / slow speed), the standard beam-shaping thrust any
phased array delivers. This is the path-B fallback the prereg flagged — it stands
independent of the exotic verdict.

---

## 5. consistency-vs-emergence + ave-discrimination-check (result-time)

- **consistency-vs-emergence → the surviving thrust is Class-B manifestation, NOT
  emergence.** `F = G_geom·P_rad/c_shear` is ordinary directed-radiation reaction — any
  focused phased array (acoustic, EM, plasma) produces it. The exotic (substrate-forced
  rectification) claim is **NULLED** (latch_gain = 1.0); there is no emergence-class
  content either direction.
- **ave-discrimination-check → no AVE-distinct thrust signal.** The dominant signal is
  generic `ρ⟨u̇²⟩` radiation-pressure streaming (present in any nonlinear/focusing
  medium); the substrate-forced latch — the one AVE-distinct ingredient — changes
  **nothing**. The SM/QED counterfactual (a focused acoustic transducer beams forward
  momentum ∝ N·P/c) **fully reproduces** the observed contrast. AVE-distinct exotic
  rectification is **not demonstrated** in any sector.

---

## 6. DERIVED / VERIFIED / BLOCKED (honest split)

**DERIVED (analytic / canonical):**
- The u-sector latch = Peierls-Nabarro STZ thixotropic re-freeze (clm-ghs75o) + Bingham
  yield τ_y (clm-gdd70j); A_yield = 1 (ε_yield); canonical τ_relax (constants.py:335);
  doc-59 §9 backward-Euler; zero tunable knobs. Identical to Phase 3 except sector.
- Direction from phase gradient (focal `φ_n = k_L(√(F²+r_n²)−F)`), not chirality;
  c_L = √2, c_shear = 1 (canonical wave speeds).
- Single mechanism: `ρ⟨u̇²⟩` is even-in-amplitude / time-symmetric; spatial focusing
  breaks spatial — not temporal — symmetry; a time-symmetric latch cannot rectify it.

**NUMERICALLY VERIFIED (smoke, qualitative):**
- Sector matched: `bulk_frac = 0.585 > 0.5` (u/P-wave) — the Phase-3 escape hatch closed.
- Latch ENGAGES (g_max 0.24–0.34; A²_focal up to 1.09 above yield) yet **latch_gain =
  0.99** → engaged-but-no-rect.
- τ_relax sweep ×0.25→×4: latch_gain flat ≈ 1.0 → no rescue band (rules out C).
- Coupling ON vs OFF identical; coupling-on stable in the measured regime.
- rect_ratio = 2.71 = beam-shaping directivity (latch-OFF too), scales with N.
- Reactance pair (C strain-E, L ρu̇²) both nonzero; local clock √(1−A²)=0.32 at the
  saturated load-bearing sites (Rule 10 diagnostics recorded).

**BLOCKED:**
1. Absolute thrust magnitude in Newtons (converged radiating sim + source-current
   normalization) — same gate as Phases 1–3; the beam-shaping `F` is native-unit only.
2. The latch-ON integrator is numerically unstable for amp ≳ 2.2 (overdrive artifact);
   the deeply-saturated regime needs an implicit/stabilized integrator to probe — not a
   physics blocker on the verdict (engaged-but-no-rect already shown at A²_focal = 1.09).

---

## 7. Honest closure (Rule 11) + substitution-not-retraction (Rule 12)

The Phase-4 hypothesis — *"sector-matching (phased-array u-drive + u-sector latch +
coupling-on) revives the rectified directed-momentum thrust the ω-sector latch could not
reach"* — is **FALSIFIED** at canonical params, with a single explanatory mechanism
(the measured `ρ⟨u̇²⟩` is even-in-amplitude/time-symmetric; spatial focusing is not a
temporal symmetry-breaker; a time-symmetric plastic latch freezes the u sector
symmetrically → no net directed plastic displacement). This is the discipline at full
strength: a clean negative, one mechanism named, no rescue-debug. The obvious rescues
were run as classifiers and came back null — the τ_relax sweep is **flat** (no value to
tune → C excluded), and pushing the focus above yield only confirms **engaged-but-no-rect**.
**No new hypothesis refills the slot** (Rule 12).

**The exotic dark-wake-as-thruster premise is now deflated across all sectors on the
same branch:** Phase 1 (linear object: reactance-dominated high-Q), Phase 2 (2nd-order
rectified object: even-in-A kernel), Phase 3 (the §1.2 latching rescue: **ω-sector**,
orthogonal to the `u̇²` observable), and **Phase 4 (sector-matched u-drive + u-latch +
coupling-on: the latch adds nothing; the contrast is beam-shaping)**. The ω sector and
the u sector are the two momentum sectors of the Cosserat substrate; both are now closed.
**The exotic chiral/rectification thrust mechanism — and the warp/Alcubierre mechanical
basis that rested on it — is refuted; the warp claim walks back.**

What SURVIVES (preserve, do not over-retract):
- **The sharpened mechanism diagnosis.** Phase 2 said "needs a hysteretic latch." Phase
  3 built it and showed "needs the latch in the **same sector** as the observable."
  Phase 4 puts it there and shows that is **still not sufficient** — a substrate
  rectifier needs **(i)** a latch, **(ii)** in the thrust sector, AND **(iii)** a
  **temporal** symmetry-breaker (the carrier+plastic-latch supply none). This is a
  forward-useful, fully-constrained negative.
- **The non-exotic beam-shaping thrust (path B).** The same array is a genuine
  directional compressional radiator, `F ≈ N·P/c_shear`, scaling with directivity, with
  direction from the phase gradient (no chirality). It does not depend on the exotic
  mechanism and stands.

---

## 8. Corpus-state deltas to queue (auditor lands; I surface only)

- **`clm-7tynm2` (dark-wake τ_zx thrust object):** the exotic rectified-DC thrust is
  now refuted **across both Cosserat momentum sectors** — Phase 3 (ω-sector latch,
  orthogonal observable) and Phase 4 (u-sector latch, **co-located** observable,
  coupling-on: latch adds nothing). Sector-matching was necessary but not sufficient;
  the missing ingredient is a **temporal** symmetry-breaker, which the
  phased-array+plastic-latch config does not provide. **Recommend: retire the exotic
  dark-wake/warp-rectification thrust route; the warp/Alcubierre mechanical basis that
  cited it walks back.** (Rule 12: retract via 🔴 header, preserve the body; the slot is
  NOT refilled.)
- **Path-B survivor (NEW capability):** the phased-array compressional driver yields the
  **non-exotic beam-shaping thrust** `F = G_geom·P_rad/c_shear`, directivity-scaling,
  direction-from-phase-gradient (no chirality), u-sector/P-wave (bulk_frac 0.585). A
  legitimate directional-radiator result, native-unit (absolute magnitude BLOCKED).
- **FLAG-A (the general no-rect mechanism, surfaced for Grant):** acoustic-rectification
  thrust in this engine needs a **time-symmetry-breaker** on top of a sector-matched
  hysteretic latch. The phased array breaks *spatial* symmetry only; the carrier is
  time-symmetric. Whether any substrate-realizable *temporally*-asymmetric drive
  (genuinely asymmetric thixotropy with fast-liquefy/slow-refreeze, or a true flyback
  duty cycle co-located in the u sector) could rectify is the one remaining open door —
  but it is a NEW hypothesis with its own verification chain, not a rescue of this one.
- **Driver capability added:** `rrad_l_phased_array_compression.py` — reusable u-sector
  phased-array compressional source (focused/random/uniform/steered) + canonical
  u-sector Peierls-Nabarro/Bingham plastic latch (zero knobs) + coupling-on +
  beam-shaping/directivity extractor + τ_relax classify sweep + N_elem directivity sweep
  + overdrive stability guard.
