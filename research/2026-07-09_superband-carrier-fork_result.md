# RESULT — Super-band carrier fork test (task #29): substrate adjudicates **BRANCH A**

**Date:** 2026-07-09 · **Branch:** `analysis/x29-superband-carrier-test`
**Prereg (FROZEN):** [`research/2026-07-09_superband-carrier-fork_prereg_FROZEN.md`](2026-07-09_superband-carrier-fork_prereg_FROZEN.md)
**Framing (OUTRANKED by this run):** [`research/2026-07-09_highE-carrier-fpb-corner_walked-framing.md`](2026-07-09_highE-carrier-fpb-corner_walked-framing.md) (origin/analysis/highE-carrier-fpb-framing)
**Driver:** [`src/scripts/vol_1_foundations/superband_carrier_fork.py`](../src/scripts/vol_1_foundations/superband_carrier_fork.py)
**Data:** [`research/2026-07-09_superband-carrier-fork_result.json`](2026-07-09_superband-carrier-fork_result.json) · **Figure:** `src/scripts/vol_1_foundations/superband_carrier_figs/superband_carrier_fork.png`
**Class (consistency-vs-emergence):** CONSISTENCY (scope-closure). NOT an emergence claim.

---

## 0. TL;DR — both branches recorded, substrate adjudicates

> **VERDICT: BRANCH A (aliased-Bloch power-law), with strong NULL character. BRANCH B (mobile
> discrete breather / hard-closure) is FALSIFIED on this platform.**

A super-band drive (ω_drive > band top ω_top) on the lossless saturable-varactor K4 bond-line:
1. **is physically evanescent** — no propagating linear carrier; measured skin rate matches the
   analytic lattice-gap `cosh κ = ω²/2 − 1` to **< 1 %** (ω=3: 1.924 vs 1.925; ω=4: 2.641 vs 2.634);
2. **self-localizes into a discrete breather** at kernel-engaged sub-yield amplitude (width → 3 nodes
   at bond-strain 0.81) — but that breather is **Peierls–Nabarro-PINNED**: momentum kicks up to
   1.0 leave its centroid at node 500.4 (v = 0.0004 c), radiating the kick away as phonons. It
   **transports no energy**;
3. **couples to the in-band smooth sector by a steep POWER law**, not an exponential:
   clean-window (ω/ω_C ∈ {2.5,3,4,5}) linear-baseline fit **p = 8.3, R² = 0.963** beats the
   exponential (γ = 2.24, R² = 0.921); and the residual leaked energy is minuscule (E_far ~ 10⁻⁹–10⁻¹¹).

Branch B requires **both** a mobile luminal carrier **and** exponential coupling. This run finds
**neither**. Therefore the closure hope dies and the ATLAS tension the Letter v5 EFT-scope names is
**REAL** (Branch A): the constitutive channel does **not** hard-close above ω₀.

**Numerical honesty (the subtle point, head-on):** the evanescence, the pinned breather, and the
steep coupling are **PHYSICAL** (spatial-lattice), not numerical. G5 confirms: dt-halving changes the
above-band transported fraction by **2.6 %** (< 5 % gate), and total energy is conserved to
**4 × 10⁻⁶** on every valid run (< 1 % gate). A numerical temporal-integration artifact would fail both.

---

## 1. Gate ledger (frozen criteria — no post-hoc drops, Rule 11)

| Gate | Frozen condition | Result | Pass |
|---|---|---|---|
| **G1 — band validated** | gapless acoustic band, v_g→0 at edge, low-k v=c | ω_top=2ω_C; low-k v=1.000 c; v_g(edge)=0; gapless | ✅ |
| **G2 — linear evanescence physical** | small-A above-band far-flux ≈0 AND skin κ matches analytic | far-flux max **0.0034** (<1e-2); κ_meas=κ_analytic to <1 % (ω≤4) | ✅ |
| **G3 — coupling-law fit** | power vs exponential separable by R² | **power** wins (clean-window R² 0.963 vs 0.921; full-set 0.815 vs 0.714) | ✅ (power) |
| **G4 — mobility** | breather hops (v≈c) OR PN-pinned — reported either way | **PN-pinned**; kicks {0.2,0.5,1.0} → v=0.0004 c; no mobile carrier | ✅ (immobile) |
| **G5 — dt-convergence / energy** | above-band T & speed change <5 % under dt→dt/2; \|ΔH\|/H<1 % | T Δ **2.6 %**; \|ΔH\|/H **4e-6** | ✅ |

**Decision rule (frozen §5) applied:** G5 ✅ and G2 ✅ ⇒ not indeterminate/artifact. G4 = no mobile
carrier AND G3 = power-law ⇒ **BRANCH A** (`not mobile AND law==power`). Branch B (`mobile AND
exponential`) fails on both conjuncts. The result is machine-emitted in the JSON `verdict` block.

---

## 2. The three branches, scored against the run

### Branch A — aliased-Bloch (power-law) — **SELECTED**
The super-band drive couples to in-band smooth modes with **power-law suppression**. Measured:
the linear-regime leaked energy E_far(ω) falls as **(ω/ω_C)^−p with p ≈ 8** (clean window,
R²=0.963), steeper than the exponential and steeper than the framing note's naive
Branch-A estimate of `(ω₀/ω)²` (p=2) — a **flag**, §5. No propagating carrier and no exponential
tail. **⇒ ATLAS: the EFT-scope statement stands; the closure hope dies; the tension is REAL.**

### Branch B — mobile discrete breather (exponential) — **FALSIFIED (this platform)**
Predicted: the kernel self-localizes super-band energy into a **hopping** packet with exponentially
suppressed ε-coupling → hard closure / ATLAS EVADES. **What the substrate did:** the kernel DOES
self-localize (a discrete breather forms above a kernel-engagement threshold — existence confirmed),
but the breather is **immobile** (Peierls–Nabarro-pinned). It transports zero energy; a momentum
kick radiates away as in-band phonons rather than translating the packet. The framing-note gate
(§3) — "PN-barrier-free luminal hopping … needs the lossless K4 + kernel" — is **not met**: the
chain here **is** lossless (ΔH/H = 4e-6) and **has** the kernel, yet the PN barrier is **not**
killed. Branch B's two requirements (mobile carrier + exponential coupling) are **both** unmet.

### Null / third — "smooth sector carries nothing above the edge" — **SUBSTANTIALLY TRUE**
The linear above-band carrier is evanescent (skin depth ~0.5–1.6 nodes); no energy propagates.
The residual in-band coupling is a tiny power-law-suppressed boundary/nonlinear leak (E_far ~
10⁻⁹–10⁻¹¹, T ~ 10⁻⁴–10⁻⁸), **not** a genuine propagating carrier. So Branch A here is
"Branch A with strong null character": there is no super-band carrier; there is only
power-law-suppressed leakage. (The null and Branch-A verdicts coincide physically — the
distinction is only whether the tiny residual leak is called "power-law coupling" or "≈nothing";
either reading kills Branch B and confirms the ATLAS tension is real.)

---

## 3. The decisive numbers

**In-band controls (carrier exists below the edge):** ω/ω_C = 0.5 → T = 0.916; 1.5 → T = 0.894.
Energy propagates freely below ω_top. (ω/ω_C = 1.5 at A=0.3 **ruptures** — bond strain reaches
yield — and is excluded; the near-boundary staggered field there is past-yield = pair regime.)

**Above the band top (ω_top = 2 ω_C) — evanescent, skin-depth-confirmed (linear A=0.02):**

| ω/ω_C | κ measured | κ analytic | E_far (leaked) | T = far/total |
|---|---|---|---|---|
| 2.1 (marginal, near-edge) | 0.629 | 0.630 | 2.2e-06 | 3.4e-03 |
| 2.5 | 1.383 | 1.386 | 1.5e-09 | 1.2e-05 |
| 3.0 | 1.923 | 1.925 | 1.2e-10 | 5.1e-07 |
| 4.0 | 2.661 | 2.634 | 1.3e-11 | 2.5e-07 |
| 5.0 | 3.075 | 3.134 | 4.3e-12 | 2.6e-08 |
| 6.0 (floor-limited) | 3.311 | 3.525 | 2.2e-12 | 3.8e-08 |

**Coupling law (linear baseline):** clean window ω∈{2.5,3,4,5}: **power p = 8.29 (R²=0.963)** vs
exp γ = 2.24 (R²=0.921). Full frozen set (incl. marginal ω=2.1, floor ω=6): power p = 11.4
(R²=0.815) vs exp γ=2.88 (R²=0.714). Power favored in every window.

**Nonlinear down-conversion excess** (E_far − linear∝A² baseline): grows with amplitude
(nl-fraction 0.02→0.30 as A: 0.1→0.3 at ω=2.5) but is itself power-law-suppressed in ω. Even the
kernel's own coupling is Branch-A, not exponential.

**Breather (O4):** self-localizes at kernel-engaged amplitude (loc-width 59→9→3 nodes as bond
strain 0.10→0.35→0.81), energy-conserving (ΔH/H ~ 4e-6). Kicked {0.2,0.5,1.0}: centroid
500.5→500.4, **v = 0.0004 c** (PN-pinned). PN-barrier energy site-vs-bond difference ≈ 0
(both configs radiate to the same pinned state; the mobility/kick test is the decisive read).

---

## 4. Physical vs numerical aliasing — separated head-on (prereg §3.5)

This is the subtlest point of the test and it is addressed directly:

- **PHYSICAL (spatial-lattice) aliasing = evanescence.** The node pitch ℓ_node is fixed and IS the
  AVE substrate. A drive above ω_top has no propagating lattice mode → the response is evanescent
  `V_n ∝ (−1)^n e^{−κn}`. This is confirmed as physical, not assumed: the **measured** decay rate
  reproduces the **analytic** lattice-gap continuation `cosh κ = ω²/2 − 1` (from k → π + iκ) to
  **< 1 %** across ω/ω_C = 2.1–4.0. This is a real consequence of Axiom-1 discreteness.
- **NUMERICAL (temporal-integration) artifact = avoided + verified absent.** The equation of motion
  is a continuous-time ODE; dt is an accuracy knob decoupled from the spatial lattice (≥ 60 substeps
  per drive period). G5's dt-halving moves the above-band transported fraction by only 2.6 % and the
  packet centroid by 0.06 % → the physics is dt-converged. Total energy conserves to 4e-6 (symplectic
  velocity-Verlet on H = Σ½p² + ΣU(r)) → the self-localization is a real Hamiltonian breather, not a
  numerical-instability blow-up (contrast: a naïve non-conservative `1/S`-stiffness scheme grew
  energy 4× — that pilot artifact is exactly what the conservative Born-Infeld potential + symplectic
  integrator + the G5 energy gate rule out).

The two are cleanly distinguished: the above-band suppression is spatial-lattice evanescence
(physical), and it survives dt-refinement (not numerical).

---

## 5. Flags (flag-don't-fix — the run outranks the framing note)

1. **"Band edge" ≠ ω_C.** The framing note calls ω₀ = ω_C "the band edge," but the lattice's linear
   acoustic band extends to **ω_top ≈ 2 ω_C**. Drives at 1.5 ω_C are **in-band** (T ≈ 0.89, they
   propagate), not above-edge. The genuine above-edge tests are ω/ω_C ≥ 3 (plus the marginal 2.1–2.5
   near-edge band). The framing note's six-marker "~MeV corner" conflates the temporal Compton scale
   ω_C with the acoustic band top; they differ by a factor ~2 (or ~π for the diamond net, ref. the
   zone-edge-settle result). Surfaced for Grant; the run measures against the true ω_top.
2. **Self-trapping happens but pins — this REVERSES the framing-note lean.** The note's open gut-check
   (§3): "does a GeV quantum self-rectify/self-trap because it exceeds both ratings (Branch B
   necessary), or merely available?" The substrate answer: it self-**traps** (breather exists) but the
   trapped state is **immobile** — self-trapping produces a **pinned defect, not a propagating
   carrier**. This supports Branch A / null, the OPPOSITE of the note's Branch-B lean. Self-trapping
   is necessary-and-present; luminal hopping is absent.
3. **Measured Branch-A exponent (p ≈ 8) is steeper than the framing note's `(ω₀/ω)²` (p = 2).** The
   boundary-evanescent coupling falls faster than the note's bulk capacitive-participation estimate.
   Same branch (power-law), different magnitude — the note's per-leg estimate under-counts the
   suppression.

---

## 6. Caveats (load-bearing — do not over-read the verdict)

1. **Platform is a 1D K4 bond-line reduction, not the full 3D K4.** The framing note explicitly
   conjectured PN-barrier-free hopping "needs the lossless K4 + kernel." This run supplies lossless +
   kernel on a **1D** chain and gets a **pinned** breather. That WEAKENS the Branch-B hope
   substantially (the generic nonlinear-lattice expectation — PN pinning — holds even with the exact
   AVE kernel), but it does **not** prove the full 3D diamond-cubic K4 cannot kill the PN barrier. If
   Branch B is to be revived, the burden is now explicit: **demonstrate that the 3D K4 geometry
   specifically eliminates the PN barrier** (not shown; the default from this test is that it does not).
2. **Power vs exponential discrimination is soft over a factor ~2–3 in ω** (R² 0.963 vs 0.921 clean
   window). The **robust, platform-independent** discriminator is not the exponent — it is the
   **absence of a mobile carrier** (G4) plus the **physical evanescence** (G2/G5). Those kill Branch B
   regardless of the exact fit.
3. **Above-yield (rupture / pair-production) is a separate regime, not tested.** When the bond strain
   reaches yield (|r|→1) the reversible dynamics break (energy conservation fails; the ω=1.5·A=0.3 and
   any staggered-field-past-yield runs are flagged RUPTURED and excluded). The framing note's "pair
   production = AC→DC rectification of the vacuum" (§5) lives in that regime and is out of scope here.
4. **The μ-slew kernel (S_B = √(1−A_I²)) was not tested** (KEEP-BOTH follow-on). Note the ε-varactor
   used here is the **hard/stiffening** nonlinearity that most favors above-band breathers, and even it
   pins; a slew-rate cap is a further softening constraint, so it is unlikely to rescue Branch-B
   mobility. This is an expectation, not a result — the μ-arm remains formally open.

---

## 7. Consistency-vs-emergence + provenance

Per the frozen classification (prereg §7): this is a **CONSISTENCY-class scope-closure test**. The
band scale ω_C = c/ℓ_node is an IDENTITY (ℓ_node := ℏ/m_ec, `constants.py:282`); the acoustic band +
evanescence + breather physics are Class-B MANIFESTATIONs (substrate re-statements of standard
discrete-lattice facts); the A-vs-B exponent is a consistency input to the ATLAS EFT-scope. **Not
headlined as AVE-distinct emergence.**

- Canonical kernel `S(A)=√(1−A²)` imported by SYMBOL from `ave.core.universal_operators.universal_saturation`
  (Axiom 4 / Born-Infeld n=2; `universal_operators.py:75`); band scale ω_C, ℓ_node, c from
  `ave.core.constants` by symbol. No hard-coded constants, no fitted targets, forward simulation only.
- Verified-not-trusted: the evanescence is checked against an independent analytic form (lattice-gap
  `cosh κ = ω²/2−1`), not asserted; energy conservation and dt-convergence are computed gates, not claims.

## 8. Corpus-state consequence (for the auditor to land, not this lane)

The named-open-item in Letter v5 (PR #594) — "the constitutive channel's closure above ω₀" — is
addressed: **the engine finds no hard closure** (no mobile exponentially-decoupled carrier); the
super-band → in-band coupling is power-law, so the EFT-domain scoping is the correct posture and the
ATLAS tension is real, not evaded. This is an empirical finding to be surfaced to the auditor's
manuscript / COLLABORATION_NOTES queue; the manual entry is the auditor's to land (lane discipline).
The framing note remains FRAMING; flags §5.1–5.3 are corrections to it that this run establishes.
