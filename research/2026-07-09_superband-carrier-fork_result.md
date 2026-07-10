# RESULT — Super-band carrier fork test (task #29): **NULL-mobility banked**

**Date:** 2026-07-09 · **Branch:** `analysis/x29-superband-carrier-test`
**Prereg (FROZEN):** [`research/2026-07-09_superband-carrier-fork_prereg_FROZEN.md`](2026-07-09_superband-carrier-fork_prereg_FROZEN.md)
**Framing (OUTRANKED by this run):** [`research/2026-07-09_highE-carrier-fpb-corner_walked-framing.md`](2026-07-09_highE-carrier-fpb-corner_walked-framing.md) (origin/analysis/highE-carrier-fpb-framing)
**Driver:** [`src/scripts/vol_1_foundations/superband_carrier_fork.py`](../src/scripts/vol_1_foundations/superband_carrier_fork.py)
**Data:** [`research/2026-07-09_superband-carrier-fork_result.json`](2026-07-09_superband-carrier-fork_result.json) · **Figure:** `src/scripts/vol_1_foundations/superband_carrier_figs/superband_carrier_fork.png`
**Class (consistency-vs-emergence):** CONSISTENCY (scope-closure). NOT an emergence claim.

> **⚠️ REGENERATED EVIDENCE (adversarial review, 2026-07-09).** The FIRST version of this
> result (commit `ecd65547`) headlined **BRANCH A** on a **G4 momentum kick that was a no-op**
> (`sin(π·n)` ≡ 0 at integer nodes → the "kicked" runs were the un-kicked run relabeled) and a
> **p=8.29 coupling law that was a ramp turn-on transient** over an in-band-contaminated fit
> window. Both were found non-functional under re-run and are **RETRACTED**. This document is the
> regenerated evidence from the repaired driver. See §9 for the full review history.

---

## 0. TL;DR — the mobility NULL survives; nothing else is banked

> **VERDICT: NULL-mobility-banked.** No mobile super-band carrier in 1D. An above-band drive is
> **evanescent-only** in steady state; the saturable kernel **does self-localize** a discrete
> breather, but that breather **PN-pins** under real, energy-injecting momentum kicks. The
> **coupling-law / form-factor question is UNMEASURED** — a single-tone driver structurally cannot
> measure the γγ 2→2 vertex; the two-tone difference-frequency protocol is **FORK A (queued)**.
> **Closure-above-ω₀ remains the named open item** (no BRANCH-A/BRANCH-B adjudication is claimed).

Three findings, each independently checked:

1. **Evanescent-only above the 1D band top.** No propagating linear carrier; the measured skin
   rate matches the analytic 1D-chain gap `cosh κ = ω²/2 − 1` to **< 1 %** for ω/ω_C ≤ 3
   (ω=3: 1.924 vs 1.925) and to **1.04 %** at ω=4 (**2.661** vs 2.634). Far-region flux ≈ 0
   (max 3.4×10⁻³ at the marginal near-edge point).
2. **The kernel self-localizes but PN-pins.** A discrete breather forms at kernel-engaged sub-yield
   amplitude (width → 3 nodes at bond strain 0.81). Under **corrected** momentum kicks that inject
   **0.12 %–4.2 %** of the breather energy (nonzero, ∝ kick²), the core drifts at
   **|v| ≤ 0.063 c** (peak) / **≤ 0.040 c** (COM) — **non-monotonic and sign-flipping** in kick
   strength (the phonon-radiation-recoil signature of a pinned core, *not* coherent translation).
   A mobile luminal carrier would translate at v ≈ c with a consistent direction; it does not.
   **The null is force-law-robust:** under the canonical Op14 e-load `F=r/√S` (matched potential)
   the breather also pins (≤ 0.031 c). PN site-vs-bond barrier ≈ 0.
3. **The coupling law is NOT measured here** (retracted, not recomputed). A single-tone drive of an
   odd (χ³) kernel emits only odd harmonics, all above the band; the in-band 2→2 channel requires a
   **two-tone** drive (ω_a, ω_b above band; ω_a−ω_b in-band; A⁶ scaling) — FORK A, not run.

**Numerical honesty:** the evanescence and the pinning are **PHYSICAL** (spatial-lattice), not
numerical. G5: dt-halving moves the above-band transported fraction by **2.7 %** (< 5 % gate);
total energy conserves to **7.8×10⁻⁶** on every valid run (< 1 % gate). The kick-injected energy
(4.2 % at kick=3.0) is tracked *separately* from the conserved evolution.

---

## 1. Gate ledger (post-review re-adjudication — KEEP-BOTH over the frozen prereg §5)

The frozen prereg body is unchanged (§5 stays as committed). Per KEEP-BOTH, the coupling-law gate
(old G3) is **dropped as structurally unmeasurable** by a single-tone driver, and the verdict is
driven by G4 (mobility) + G2 (evanescence) + G5 (validity). See the prereg's appended
post-review re-adjudication section and §9 below.

| Gate | Condition | Result | Pass |
|---|---|---|---|
| **G1 — band validated** | gapless 1D acoustic band, v_g→0 at edge, low-k v=c | ω_top(1D)=2ω_C; low-k v=0.999 c; v_g(edge)=0; gapless | ✅ |
| **G2 — evanescent-only** | small-A above-band far-flux ≈0 AND skin κ matches analytic within **15 %** (frozen tol, restored) | far-flux max **3.4e-3** (<1e-2); κ err 0.07–1.9 % (ω≤5), 6.1 % (ω=6) | ✅ |
| **G3 — coupling law** | — | **DROPPED** (single-tone cannot measure the 2→2 vertex; FORK A) | n/a |
| **G4 — mobility (BANKED)** | kicked breather translates at v≈c (mobile) OR PN-pins (immobile) | **PN-pinned**; kicks inject 0.12–4.2 % energy → \|v\|≤0.063 c, non-monotonic; no mobile carrier | ✅ (immobile) |
| **G5 — dt / energy** | above-band T change <5 % under dt→dt/2; \|ΔH\|/H<1 % | T Δ **2.7 %**; \|ΔH\|/H **7.8e-6** | ✅ |

**Decision rule applied:** kick energy injection > 0 (no-op repaired) AND G5 ✅ AND no mobile
carrier AND G2 ✅ ⇒ **NULL-mobility-banked** (machine-emitted in the JSON `verdict` block).

---

## 2. What the corrected kicks measured (the banked leg — finding #1 repair)

The old kick `Vd = kick·amp·env·sin(π·n)` was **machine-zero** at integer nodes (a no-op); the
committed "kicked" rows were the un-kicked run relabeled. The repaired kick is the **translation
(Goldstone) mode** of the zone-edge carrier, `Vd = −kick·∇V`, with an explicit **cos-staggered**
cross-check `Vd = −kick·(∇env)·cos(π·n)` (algebraically the same object — the pure-carrier stagger
cancels in a central difference; they agree to machine precision). Energy **injected** by the kick
is reported per run and must be nonzero and scale with kick²:

**Gradient kick, seeded breather amp=0.25 (bond strain 0.81), tmax=350:**

| kick | energy injected (frac) | KE injected | \|ΔH\|/H (evolution) | COM drift | COM v | core (peak) drift | peak v | core-energy frac |
|---|---|---|---|---|---|---|---|---|
| 0.5 | 0.12 % | 1.36e-3 | 7.7e-6 | +13.9 | +0.040 c | +20 | +0.057 c | 0.82 |
| 1.0 | 0.47 % | 5.43e-3 | 6.0e-6 | +10.0 | +0.029 c | +13 | +0.037 c | 0.92 |
| 2.0 | 1.88 % | 2.17e-2 | 7.4e-6 | −6.2 | −0.018 c | +14 | +0.040 c | 0.19 |
| 3.0 | 4.23 % | 4.89e-2 | 5.4e-6 | −11.8 | −0.034 c | −22 | −0.063 c | 0.78 |

- **Energy injection is nonzero and scales as kick²** (0.12 % → 4.2 % across kick 0.5 → 3.0) — the
  no-op is repaired. Injected energy is tracked separately from the conserved (\|ΔH\|/H~6e-6)
  Hamiltonian evolution.
- **The core does not translate.** |v| ≤ 0.063 c (peak) / 0.040 c (COM) — **≥ 16× below c** — and
  the drift **reverses sign** between kick=1.0 (+) and kick=3.0 (−) and is **non-monotonic**. A
  mobile carrier would move ~c·tmax ≈ 350 nodes in a consistent direction scaling with the kick;
  instead the core stays within ±22 nodes of its origin and the kick radiates away as phonons.
- **cos-staggered cross-check:** kick=1.0 → |v_peak|=0.037 c; kick=3.0 → |v_peak|=0.063 c —
  matching the gradient-kick magnitudes (confirms the kick is correctly implemented).
- **Force-law robustness (finding #5):** under the canonical Op14 e-load `F=r/√S` (matched
  potential, energy-conserving) the same kicks give |v_peak| = 0.009 c (kick=1.0), 0.031 c
  (kick=3.0) — **also pinned**. The banked null does not depend on the r/S-vs-r/√S casting.
- **PN barrier:** site-centred vs bond-centred static-breather energy differ by 1.5e-6 (relative),
  i.e. ≈ 0 — both relax to the same pinned state; the kick test (above) is the decisive read.

**Reading:** the kernel self-localizes (a discrete breather exists), but the localized state is an
**immobile pinned defect, not a propagating carrier**. This is the banked result.

---

## 3. Evanescence verification (kept — clean; re-scoped to the correct band top)

The above-band linear response is spatially evanescent `V_n ∝ (−1)^n e^{−κn}`, verified against the
analytic 1D-chain gap continuation `cosh κ = ω²/2 − 1` (k → π + iκ). This leg was clean in the
first version and is retained (linear drive A=0.02):

| ω/ω_C | κ measured | κ analytic | err | E_far | T = far/total | above true 3D srs band? |
|---|---|---|---|---|---|---|
| 2.1 | 0.629 | 0.630 | 0.14 % | 2.2e-06 | 3.4e-03 | **no** (below srs top) |
| 2.5 | 1.383 | 1.386 | 0.23 % | 1.5e-09 | 1.2e-05 | **no** |
| 3.0 | 1.924 | 1.925 | 0.07 % | 1.2e-10 | 5.1e-07 | **no** (≈ srs top) |
| 4.0 | **2.661** | 2.634 | 1.04 % | 1.3e-11 | 2.5e-07 | yes |
| 5.0 | 3.075 | 3.134 | 1.88 % | 4.3e-12 | 2.6e-08 | yes |
| 6.0 | 3.311 | 3.525 | 6.08 % | 2.2e-12 | 3.8e-08 | yes |

This confirms the **1D-chain** evanescence gap to < 1 % for ω ≤ 3 and to ~1–2 % through ω=5 (the
ω=6 point is floor-limited: the field has decayed into round-off within the fit window). The
last column is per finding #4: only ω ≳ 3.5 ω_C is unambiguously above the **true 3D srs** band
top — see §5. **The far-flux (E_far) column is used ONLY as the G2 evanescent-only witness
(far-flux ≈ 0); it is NOT fit to any coupling law** (see §4).

**In-band controls (carrier propagates below the edge):** ω/ω_C = 0.5 → T = 0.916; 1.5 → T = 0.894.
(ω = 1.5 at A=0.3 **ruptures** — bond strain reaches yield — and is excluded; that near-boundary
staggered field is past-yield = pair regime, out of scope.)

---

## 4. The coupling-law leg — **DROPPED** (findings #2, #3)

The first version fit the far-region leaked energy E_far(ω) to a power law (p = 8.29, "clean
window") and headlined **BRANCH A** ("the ATLAS tension is REAL"). **This is retracted and NOT
recomputed.** Two independent reasons:

- **#2 — E_far is a turn-on transient, not a vacuum channel.** E_far collapses ~15× per
  ramp-doubling with **no floor**: it measures the raised-cosine drive envelope's spectral tail,
  not a physical super-band → in-band coupling. The fit window {2.5,3,4,5} was also cherry-picked
  against the frozen primary set {2.1,…,6} (which gave p = 11.4), and the frozen G3 separability
  gate was silently dropped in the first driver.
- **#3 — a single-tone driver structurally cannot measure the γγ 2→2 vertex.** An odd (χ³) kernel
  driven at one tone emits only **odd harmonics**, all *above* the band. The in-band 2→2 channel
  that the ATLAS EFT-scope question is about is a **two-tone difference-frequency** process: drive
  ω_a and ω_b both above band, read the in-band product at ω_a − ω_b, expect **A⁶** amplitude
  scaling. That protocol was never driven here.

**The two-tone protocol is FORK A — a future arc, explicitly NOT attempted in this repair.** The
amplitude-exponent-vs-QED-box question is therefore **OPEN, not resolved**.

---

## 5. Band-top honesty (finding #4)

Two DISTINCT band tops must not be conflated:

- **This platform (1D K4 bond-line reduction):** ω_top = **2 ω_C** exactly (ω = 2|sin(kℓ/2)|,
  Laplacian λ_max = 4, √4 = 2). The `cosh κ = ω²/2 − 1` evanescence check (§3) is exact for **this
  1D chain** and rests on this edge — it is a clean check of the 1D-chain gap.
- **True 3D srs (diamond-cubic K4) band top:** **≈ 3.3–3.5 ω_C** per the review's three methods,
  consistent with the repo's own srs graph-Laplacian **λ_max = 6.000** (verified here:
  `build_srs_net` is 3-regular, mean degree 3.000, λ_max = 6.0000; √6 ≈ 2.449 in the bare ω²=λ
  normalisation, raised to ~3.3–3.5 ω_C once the srs bond-length / 1/√3-network factor is applied).

**Consequence:** drives at ω/ω_C ∈ {2.1, 2.5, 3.0} are above the **1D-chain** top (2.0) but
**at/below** the true 3D srs top. **No "above the physical 3D band" claim may rest on the 2.0
edge.** The first version's blanket "above-band" language over 2.1–3.0 is corrected: those points
verify 1D-chain evanescence (valid), but only ω ≳ 3.5 ω_C is unambiguously above the 3D band.

---

## 6. Force-law honesty (finding #5)

The bond force is stated precisely. **Default:** `F(r) = r/S = r/√(1−r²)` from the potential
`U(r) = 1 − √(1−r²) = 1 − S` — a **conservative Born–Infeld n=2 casting**, chosen because it
derives from the cleanest single-valued potential (the Axiom-4 kernel itself), giving an **exact
Hamiltonian** for the symplectic integrator + the |ΔH|/H gate. **This is NOT the Op14 ε-load force
law**, which is `F = r/√S = r/(1−r²)^{1/4}` (from `Z_eff = Z_0/√S ⇒ C_eff = C·S`,
`universal_operators.py:831`). The two are tagged explicitly in the driver's `FORCE_LAW` note.
Per §2, the banked null is **verified robust** to the choice: an `r/√S` robustness leg (with its
matched potential `U = (2/3)(1−(1−r²)^{3/4})`, energy-conserving) also PN-pins. The **G2 skin
tolerance is restored to the frozen 15 %** (the first driver had silently relaxed it to 30 %);
the measured κ passes at 15 % for all ω ≤ 5.

---

## 7. Physical vs numerical aliasing — separated head-on (prereg §3.5)

- **PHYSICAL (spatial-lattice) = evanescence.** The node pitch ℓ_node is fixed and IS the AVE
  substrate. A drive above the 1D top has no propagating lattice mode → evanescent response, and the
  **measured** decay rate reproduces the **analytic** 1D-chain gap `cosh κ = ω²/2 − 1` to < 1 %
  (ω ≤ 3). This is a real consequence of Axiom-1 discreteness.
- **NUMERICAL (temporal-integration) = avoided + verified absent.** The equation of motion is a
  continuous-time ODE; dt is an accuracy knob (≥ 60 substeps/drive period) decoupled from the
  lattice. G5's dt-halving moves the above-band transported fraction by only 2.7 % and the packet
  centroid by 0.02 %; total energy conserves to 7.8e-6 (symplectic velocity-Verlet on the exact H).
  A naïve non-conservative `1/S`-stiffness scheme grew energy ~4× — exactly the pilot artifact the
  matched Born–Infeld potential + symplectic integrator + G5 energy gate rule out.

---

## 8. Caveats + open items (load-bearing — do not over-read the null)

1. **Platform is a 1D K4 bond-line reduction, not the full 3D K4.** This run supplies lossless +
   kernel on a **1D** chain and gets a **pinned** breather (the generic nonlinear-lattice PN-pinning
   holds even with the exact AVE kernel). It does **not** prove the full 3D diamond-cubic K4 cannot
   kill the PN barrier. Reviving mobility carries an explicit burden: **demonstrate that the 3D K4
   geometry specifically eliminates the PN barrier** (not shown; the default from this test is that
   it does not).
2. **The coupling-law / form-factor question is UNMEASURED** (§4). The ATLAS-scope
   amplitude-exponent question is **open**. The measurement that could close it is the **two-tone
   difference-frequency protocol (FORK A)**, queued.
3. **Closure-above-ω₀ remains the named open item** in Letter v5 (clm-gg4wmx) — this run does **not**
   resolve it in either direction. No Letter edit, no leaf correction (v5 pre-registered exactly this
   open-item situation).
4. **Above-yield (rupture / pair production) is a separate regime, not tested** (energy conservation
   fails at |r|→1; ruptured runs excluded).
5. **The μ-slew kernel (S_B = √(1−A_I²)) was not tested** (KEEP-BOTH follow-on; formally open).

---

## 9. Adversarial-review history (record of the evidence-void + regeneration)

The first committed evidence (`ecd65547`) was found **non-functional** on 5-lens adversarial
review (findings CONFIRMED by re-run). Blocking findings and their disposition:

| # | Finding | Disposition in this repair |
|---|---|---|
| 1 | G4 kick `sin(π·n)` ≡ 0 (no-op); "kicked" runs = un-kicked relabeled | **REPAIRED** — real translation-mode + cos-staggered kicks, energy-injection diagnostic (§2) |
| 2 | p=8.29 coupling law = ramp turn-on transient; frozen G3 gate dropped | **DROPPED** — leg removed, not recomputed (§4) |
| 3 | single-tone cannot measure the 2→2 vertex (needs two-tone) | **ACCEPTED** — two-tone = FORK A, queued; question OPEN (§4) |
| 4 | 1D band top ≠ true srs band top (2.1/2.5/3.0 were mislabelled above-band) | **FIXED** — 1D top 2.0 vs true srs ≈3.3–3.5 (λ_max=6.000) (§5) |
| 5 | force law mislabelled canonical; G2 tol silently 15→30 %; two TL;DR misquotes | **FIXED** — force law tagged + robustness leg; 15 % restored; TL;DR = run (§6) |

Adjudication moved **from BRANCH A to NULL-mobility-banked**: the mobility null is independently
confirmed by the corrected kicks; the amplitude-exponent question is OPEN, not resolved.

---

## 10. Consistency-vs-emergence + corpus-state consequence

Per the frozen classification (prereg §7): **CONSISTENCY-class scope-closure**. Band scale
ω_C = c/ℓ_node is an IDENTITY; the acoustic band + evanescence + breather physics are Class-B
MANIFESTATIONs (substrate re-statements of standard discrete-lattice facts). **Not headlined as
AVE-distinct emergence.** Canonical kernel imported by SYMBOL (`universal_saturation`, Axiom 4 /
Born–Infeld n=2); constants from `ave.core.constants` by symbol; forward simulation only; every
gate computed, not asserted (evanescence checked against an independent analytic form; energy and
dt-convergence are computed gates).

**Corpus-state consequence (for the auditor to land, not this lane):** the Letter v5 named-open-item
— "the constitutive channel's closure above ω₀" — remains **OPEN**. The engine banks a **mobility
null** (no mobile super-band carrier in 1D) but **does not measure** the coupling law (single-tone
cannot; two-tone = FORK A). So the corpus consequence is a **ledger row recording the evidence-void
+ regeneration**, NOT a Letter edit or leaf correction (v5 pre-registered this open-item situation).
This is surfaced to the auditor's manuscript / COLLABORATION_NOTES queue; the manual entry is the
auditor's to land (lane discipline). The framing note remains FRAMING; the flags in §5–§6 correct
it and this run establishes them.
