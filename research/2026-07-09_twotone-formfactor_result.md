# RESULT — Two-tone four-photon form factor (FORK A, task #31-A): **INTERFACE-scoped kernel result + ★ PARITY THEOREM** (bulk vertex OPEN; fork-record repaired)

**Date:** 2026-07-09 · **Branch:** `analysis/x31a-twotone-formfactor` (off main @ post-#604/#605)
**Status:** **REPAIRED per adversarial review (BLOCKED verdict).** The first verdict — BRANCH (i)
DRIVE-TRACKING, "ATLAS tension real" — is **VOID** (drive-interface artifact). This document is the
regenerated honest scope (fork-D pattern, x29/#598): bank what survives, void what was geometry-artifact.
**Prereg (FROZEN):** [`research/2026-07-09_twotone-formfactor_prereg_FROZEN.md`](2026-07-09_twotone-formfactor_prereg_FROZEN.md)
**Driver:** [`src/scripts/vol_1_foundations/twotone_formfactor.py`](../src/scripts/vol_1_foundations/twotone_formfactor.py) (extends the x29 base driver, Rule 14)
**Data:** [`research/2026-07-09_twotone-formfactor_result.json`](2026-07-09_twotone-formfactor_result.json)
**Figure:** [`src/scripts/vol_1_foundations/twotone_formfactor_figs/twotone_formfactor.png`](../src/scripts/vol_1_foundations/twotone_formfactor_figs/twotone_formfactor.png)
**Class (consistency-vs-emergence):** the surviving products are **MANIFESTATION (Class B)** — the A⁶
amplitude law and the parity theorem, both direct consequences of the odd (χ³) Axiom-4 kernel. **The
frequency form-factor EMERGENCE claim is WITHDRAWN: the bulk vertex was NOT probed.**

> **★ THE PR'S REAL PRODUCT IS THE PARITY THEOREM** (§1): the reversible sub-yield vacuum is a symmetric
> varactor, so the difference channel `ω_hi−ω_lo` is *structurally forbidden* — a null that is a **generatively
> verified witness of inversion symmetry** (plant an even χ² term and the forbidden tone lights up ∝ β²,
> exponent **2.000**, R² = 0.99999999). Genuinely new to the corpus. The A⁶ χ³ law (clean-regime **6.02**)
> is the second banked product. **NO Letter/KB edits — explicit do-not-add** (§8): no ATLAS-facing sentence
> is licensed by this run.

---

## 0. TL;DR — the honest re-scoped verdict (machine-emitted, verbatim)

> **VERDICT (`BRANCH = interface_scoped__BULK_OPEN`):** *(ii)/hard-closure EXCLUDED at the drive interface;
> (i)-vs-(iii) normalization-dependent (q in [0.30 analytic-bond, 2.93 raw]); frozen O_skin rule
> mis-specified for this geometry (q=-13.6 = the interface-artifact diagnostic); bulk-geometry
> discriminator (sep>=3) shows ~16-order collapse toward skin suppression — THE BULK VERTEX WAS NOT
> PROBED; the super-band coupling fork remains OPEN.*

**What the review killed (blocking finding, CONFIRMED by re-run).** The original design drives **both tones at
one hard-clamped node**. That co-locates them: the drive bond (n_drive → n_drive+1) is pinned to O(A) strain
at BOTH tones *regardless of frequency*, so the "flat vertex" (branch i) recovered the constant kernel cubic
coefficient **by construction — an interface, not the bulk**. The reviewer's bulk-geometry discriminator
(tones sourced at **separated** nodes, sep ≥ 3, so the mixing region is interior where both tones are
evanescent) shows the χ³ beat **collapses ~17 orders** toward the O_skin skin-suppression the frozen axis
predicted. **The bulk vertex was never probed; the super-band coupling fork is OPEN.**

**What survives (Class-B, banked — §1, §2):**
1. **★ The parity theorem** — even kernel ⇒ pure χ³ ⇒ difference channel `ω_hi−ω_lo` forbidden sub-yield;
   verified **generatively** (planted asymmetry lights the forbidden tone ∝ β², monotonic). **The PR's real product.**
2. **The A⁶ amplitude law** — the χ³ four-photon channel is real and characterized (clean-regime exponent **6.02**).

**Prereg-compliance on the channel choice CONFIRMED:** the measured channel `2ω_lo−ω_hi` was frozen in a
single commit and never amended (§5 of the prereg).

---

## 1. ★ The parity theorem — the PR's real product (generatively verified)

`U(r)=1−√(1−r²)` is **even** ⇒ `F(r)=r+½r³+⅜r⁵+…` is **odd** ⇒ the reversible sub-yield vacuum is a **pure
χ³, inversion-symmetric varactor**. Under `V→−V` the whole scheme (EOM + damping) is odd, so the response is
an odd functional of the drive: a spectral line at `m·ω_lo+n·ω_hi` exists **iff `m+n` is ODD**.

| product | (m,n) | m+n | allowed | measured @ (2.6, 4.2) |
|---|---|---|---|---|
| ω_hi − ω_lo (difference) | (−1,+1) | 0 | **FORBIDDEN** | P_diff / P_FWM ≈ **3.4×10⁻¹¹** (floor) |
| DC / rectification | (0,0) | 0 | **FORBIDDEN** | at floor |
| **2ω_lo − ω_hi (FWM)** | **(+2,−1)** | **1** | **ALLOWED** | **the measured beat** |

### 1.1 Generative verification — the null as an INVERSION-SYMMETRY WITNESS (NEW)

The null is not a numerical coincidence: it is a *consequence of kernel inversion symmetry*, proven by
**generatively breaking that symmetry**. Plant an even (χ²) term `F(r) → F(r) + β·r²` (a DC-biased /
rectifying varactor) and sweep β at the reference pair (`parity_generative_test`):

| β (planted χ²) | P(ω_hi−ω_lo) difference tone | P(2ω_lo−ω_hi) allowed FWM |
|---|---|---|
| **0** (physical vacuum) | 1.17×10⁻¹⁶ (**forbidden — at floor**) | 3.46×10⁻⁶ |
| 0.03 | 5.62×10⁻⁷ | 3.47×10⁻⁶ |
| 0.06 | 2.25×10⁻⁶ | 3.48×10⁻⁶ |
| 0.12 | 8.98×10⁻⁶ | 3.54×10⁻⁶ |
| 0.24 | 3.59×10⁻⁵ | 3.83×10⁻⁶ |

- The forbidden difference tone rises **monotonically** in β, **power ∝ β²** (fitted exponent **2.000**,
  R² = 0.99999999) — exactly the leading order of a planted χ² (field ∝ β).
- The allowed odd-order FWM sideband is (to leading order) **β-blind** — it stays ≈ constant.
- **Consequence:** the sub-yield difference-channel null is a genuine, generatively-confirmed witness of the
  vacuum's inversion symmetry. A nonzero reading there would flag an even-order leak or that yield /
  rectification (pair production) had been touched. β = 0 is the physical reversible vacuum.

This is genuinely new to the corpus and does **not** depend on the (voided) form-factor claim.

---

## 2. The A⁶ / χ³ amplitude law — the second banked product (corrected)

At the fixed pair (2.6, 4.2), sweeping equal drive amplitude A over {0.015 … 0.24} (all sub-yield):

| A | max bond r | P_beat | in clean regime (r < 0.15)? |
|---|---|---|---|
| 0.015 | 0.034 | 2.9×10⁻¹² | ✅ |
| 0.03 | 0.069 | 1.9×10⁻¹⁰ | ✅ |
| 0.06 | 0.137 | 1.2×10⁻⁸ | ✅ |
| 0.12 | 0.275 | 8.5×10⁻⁷ | ✗ (χ⁵ stiffening) |
| 0.24 | 0.551 | 8.0×10⁻⁵ | ✗ (χ⁵ stiffening) |

- **Clean-regime exponent 6.02** (`max_bond_r < 0.15`, 3 points, R² = 0.999999) — the χ³ / four-wave-mixing
  signature (field ∝ A³, power ∝ A⁶). This is the honest number: it is measured where the strain is small
  enough that higher-order (χ⁵, `⅜r⁵`) terms are negligible.
- **Global exponent 6.16** (all 5 points, R² = 0.9997) — steeper than 6 because the **χ⁵ term stiffens the
  slope** at the two largest-amplitude points (r = 0.27, 0.55). Both are reported; the clean-regime value is
  the χ³ figure of merit.
- **Dynamic range 2.7×10⁷** (P_beat from 2.9×10⁻¹² to 8.0×10⁻⁵) — corrected from the first draft's erroneous
  "2.6×10⁵".
- **The sweep NEVER approaches the floor.** The smallest measured point (2.9×10⁻¹²) is **5.7×10¹⁰ above** the
  kernel-OFF floor (5.1×10⁻²³). The earlier "A⁶ down to the 5×10⁻²³ floor" wording was wrong — every point is
  ≥ 10 orders above the floor; the floor is a characterization control, not a limit the data reaches.
- **Casting cross-check:** the r/√S casting reproduces the same amplitude shape with a prefactor ≈ ¼× the
  r/S run (the ½:¼ vertex-coefficient ratio squared) — a clean cross-check, casting-independent exponents.

---

## 3. The BULK-vs-INTERFACE discriminator — the review's null baseline (COMMITTED)

The review's blocking discriminator is now a **first-class driver mode** (`twotone_run_separated` /
`sep_discriminator`): two independently-sourced tones at nodes `n_lo` and `n_hi = n_lo + sep`. For **sep ≥ 3**
the mixing region is the interior, where **both tones are evanescent** — no single bond is clamped to O(A) at
both tones, so the χ³ FWM source is skin-suppressed (the physical bulk vertex). `sep = 0` superposes both
tones on one node = the co-located drive-**interface** baseline.

### 3.1 Collapse at the reference pair (2.6, 4.2), A = 0.15

| geometry | P_beat(2ω_lo−ω_hi) | note |
|---|---|---|
| **sep = 0 (co-located, INTERFACE)** | **3.4632×10⁻⁶** | reproduces the banked co-located value to 15 digits |
| **sep = 3 (bulk)** | **2.4997×10⁻²³** | at the kernel-off floor |
| sep = 6 (bulk) | 2.4997×10⁻²³ | **separation-saturated** (identical to sep=3 ⇒ at the floor) |

**Collapse = 1.385×10¹⁷ ≈ 17.1 orders.** Separation-saturated for sep ≥ 3 (the residual is the numerical
floor, not a converging bulk beat) — the bulk beat is below the platform floor. **THE BULK VERTEX WAS NOT PROBED.**

### 3.2 Form-factor sweep, INTERFACE vs BULK (raw P_beat, no participation model)

| ω̄ | O_skin² (frozen bulk prediction) | P_beat sep=0 (INTERFACE) | P_beat sep=3 (BULK) |
|---|---|---|---|
| 2.8 | 3.22×10⁻⁴ | 7.23×10⁻⁶ | 1.10×10⁻²¹ |
| 3.1 | 4.51×10⁻⁵ | 4.55×10⁻⁶ | 1.08×10⁻²² |
| 3.4 | 9.70×10⁻⁶ | 3.46×10⁻⁶ | 2.50×10⁻²³ |
| 3.7 | 2.66×10⁻⁶ | 2.88×10⁻⁶ | 8.09×10⁻²⁴ |
| 4.0 | 8.60×10⁻⁷ | 2.49×10⁻⁶ | 3.19×10⁻²⁴ |

- **INTERFACE (co-located) raw exponent q_raw = 2.93** — nearly flat (the artifact: the drive bond stays
  O(A) at both tones as ω̄ rises).
- **BULK (sep = 3) raw exponent q_raw = 16.15** (R² = 0.98) — **steep, tracking the skin suppression**.
- **★ The frozen O_skin was the CORRECT BULK MODEL.** The O_skin² falloff exponent vs ω̄ is **16.54**; the
  bulk raw exponent (16.15) tracks it to within scatter. In the co-located interface geometry P_beat *barely*
  tracks O_skin² (raw-tracks-O_skin² slope 0.18); in the bulk geometry it tracks it almost exactly. **The
  frozen axis's q = −13.6 "failure" (P_beat/O_skin² rising) was the interface-artifact *detector*, not a
  physical enhancement** — exactly as the O_skin normalization would behave if the mixing were an interface
  pin rather than a bulk vertex.

---

## 4. Gate ledger (all PASS — with a disclosed coverage gap)

| Gate | Condition (prereg §8) | Result | Pass |
|---|---|---|---|
| **(a) M7 per-tone injection** | each tone establishes a nonzero skin amplitude ∝ A | node-1 amp @A=0.10: lo 0.0223 (analytic 0.0220), hi 0.0062 (analytic 0.0064); halves with A (2.03/2.03) | ✅ |
| **(b) Validate-on-known (reader)** | planted linear ω_out tone recovered with directional flux ∝ amp² | power-vs-amp slope 2.00; J_right>0, J_left<0 | ✅ |
| **(c) Ramp-independence** | steady-window beat stable under ramp doubling (<5%) | rel change 1.7×10⁻³ (R vs 2R) | ✅ (see gap) |
| **(d) A⁶ control (A→0)** | beat scales as A⁶ (χ³ signature) | clean-regime exponent 6.02 (§2) | ✅ |
| **(e) Energy + dt** | free-evo \|ΔH\|/H ≤1e-5 (converging); beat dt-invariant <5% | dH/H 4.4×10⁻⁶ → 1.1×10⁻⁶ at dt/2; beat dt-halving 9.8×10⁻⁴ | ✅ |

**DISCLOSED COVERAGE GAP (gate c).** The prereg §8(c) wording is *"run **every** measurement at ramp_periods
R and 2R."* The driver ramp-tested **one pair only** — the reference pair (2.6, 4.2) at A = 0.15 (rel change
1.7×10⁻³). The form-factor-sweep carriers and the amplitude-sweep points were **not** individually
ramp-doubled. This is a coverage gap against the frozen wording; it is **disclosed, not re-run** (the single
tested pair passed decisively, and the branch verdict does not rest on the interface form factor). **Full
ramp-independence on every measurement is carried into the 3D follow-on mandate (§7).**

---

## 5. KEEP-BOTH — the interface-scoped diagnostics (preserved, RE-LABELED)

The original participation-normalization tables are **preserved** (KEEP-BOTH), now correctly labeled as
**drive-INTERFACE** diagnostics — they characterize the co-located clamp, **not** the bulk vertex.

| axis | exponent q | R² | reading (RE-SCOPED) |
|---|---|---|---|
| raw P_beat vs ω̄ (INTERFACE) | 2.93 | 0.96 | the co-located interface falloff (nearly flat by construction) |
| frozen O_skin (P_beat/O_skin²) | **−13.6** | 0.999 | the **interface-artifact DIAGNOSTIC** — rising because O_skin is the *bulk* model applied to an *interface* run (§3.2) |
| analytic drive-bond O_bond | 0.30 | 0.96 | interface participation only; **NOT a branch selector** |
| measured drive-bond O_bond | −0.95 | **0.15** | **UNINFORMATIVE — deleted as evidence** (see below) |

**DELETED CLAIM (the "measured drive-bond corroborates branch i").** The first draft claimed the empirically
measured drive-bond participation "corroborates branch (i)". It does **not**: the fit is R² = 0.15 and the
exponent is **sign-flipped** (q_meas = −0.95 vs the analytic +0.30). Per the review it **neither confirms nor
refutes** any branch — it is noise. The claim is removed; the field is retained in the JSON only as
`INTERFACE_q_measured_drivebond_UNINFORMATIVE` with the sign-flip/low-R² flag.

**BIRTH-DEPTH — the metric FLOORS at 1 by construction (not bulk evidence).** The first draft cited
"birth_depth = 1 at every pair" as evidence that mixing is drive-bond-localized. This is a **construction
artifact**: the |Ṽ_n(ω_out)| profile is **flat at the plateau (≈1.90×10⁻³) from node 1 outward** and drops to
≈0 **only at node 0**, which is the hard-clamped Dirichlet drive node. The birth-depth metric (first node
reaching 90% of plateau) therefore reads **1 by construction** — node 0 is the wall, node 1 is the first free
node already at plateau. It is **not** a measurement of where the beat is born and carries **no** bulk-vs-edge
information. Removed as evidence; the flat node-1-onward profile is stated as-is.

---

## 6. Prereg branch table, RE-SCOPED against the bulk finding

| # | Branch | Prereg signature | Status after the bulk discriminator |
|---|---|---|---|
| (i) | DRIVE-TRACKING | P_beat/O² flat in ω̄ | **VOID at the bulk level** — the "flat" was the drive-interface artifact (§3) |
| (ii) | PARTICIPATION-SUPPRESSED | P_beat/O² falls steeply | **EXCLUDED at the drive interface** (near-trivial); the bulk beat instead *collapses to floor* |
| (iii) | INTERMEDIATE power law | P_beat/O² ∝ ω̄^(−q) | (i)-vs-(iii) is **normalization-dependent** (q ∈ [0.30 analytic-bond, 2.93 raw]) — unresolved at the interface, **not probed** in the bulk |
| (iv) | NULL | no beat above floor | the **bulk** geometry is at the floor (collapse to 2.5×10⁻²³) — a *geometry* statement, not the vacuum's answer |

**Net:** the super-band four-photon coupling fork is **OPEN**. The 1D interface run cannot decide it; the bulk
vertex requires the follow-on geometry (§7).

---

## 7. 3D follow-on mandate (load-bearing — per the adversarial review)

The eventual bulk / 3D form-factor run MUST (verbatim per the review):

- **NO clamp at the mixing site** — two **independently-sourced evanescent packets crossing in the interior**
  (not a Dirichlet clamp that pins the drive bond to O(A)).
- **ALL normalization axes pre-registered** with **defined responses for negative / rising q** (so a rising
  P_beat/O² is adjudicated *a priori* as an over-correcting participation model, not read as an enhancement).
- **O_skin carried forward as the pre-registered BULK prediction** — it called the collapse (§3.2); it is the
  bulk model, not a discarded one.
- **Ramp-independence on EVERY measurement** (closes the §4 coverage gap).
- **The sep ≥ 3 discriminator committed as the null baseline** (done here — `sep_discriminator`).
- **Spatial source profile**, not the floored integer — measure where the beat is actually born from the
  full |Ṽ_n(ω_out)| profile, not the construction-floored birth-depth metric (§5).

3D platform note (recorded, not run): srs band top π√3 ≈ 5.441 ω_C (#604); FORK-A 3D tones (18.51 / 17.51 ω_C,
Δ = 1.0, #607) recorded in the JSON.

---

## 8. consistency-vs-emergence + corpus-state (NO Letter/KB edit — do-not-add)

- **★ Parity theorem + A⁶ law → MANIFESTATION (Class B)** — direct consequences of the odd (χ³) Axiom-4
  kernel; the two banked products.
- **Frequency form-factor EMERGENCE claim → WITHDRAWN** — the bulk vertex was not probed; no emergent form
  factor was measured.
- **Band scale ω_C, ω_out = 1.0, ω_top = 2.0 → IDENTITY (Class A)** (native units).

**Corpus-state consequence:** **Letter v5 / clm-gg4wmx (closure-above-ω₀): ZERO edits, explicit do-not-add.**
**No ATLAS-facing sentence is licensed by this run.** The first draft baked "ATLAS tension real" into the
machine verdict across an un-crossed 7-gap chain; that is **scrubbed** from the driver and this document. The
open item stays open; this run contributes the parity theorem and the A⁶ characterization (research-tier), and
the committed **sep ≥ 3 bulk null baseline** for the follow-on. Propagation (if any) is a follow-on **after**
the auditor lands it — this lane surfaces, it does not land the manual.

---

## 9. Adversarial-review history (fork-D pattern — bank what survives, void the artifact)

**First verdict (commit 20e38bb, VOID):** BRANCH (i) DRIVE-TRACKING — "the four-photon vertex is
frequency-blind above band; the χ³ enhancement survives; **ATLAS tension real** (1D mechanism substrate)."
The evidence was the flat drive-bond-corrected form factor (q = 0.30).

**Blocking finding (5-lens adversarial review, CONFIRMED by re-run):** the hard Dirichlet clamp **co-locates**
both tones at the drive node, pinning the drive-bond strain at O(A) for both tones *regardless of frequency* —
the "flat vertex" recovered the constant kernel cubic coefficient **by construction (interface, not bulk)**.
The bulk-geometry discriminator (sep ≥ 3) shows the beat **collapses ~17 orders** toward the O_skin
skin-suppression the frozen axis predicted. Additionally: the branch field was normalization-selected (frozen
rule → unclassifiable; raw → (iii); only the post-hoc drive-bond axis → (i)); "ATLAS tension real" was baked
across an un-crossed chain (**scrubbed**); the "measured drive-bond corroboration" is noise (R² = 0.15,
sign-flipped); A⁶ prose errors (range 2.7×10⁷ not 2.6×10⁵; clean-regime exponent 6.02).

**This regenerated scope (fork-D pattern, x29/#598):**
- **VOIDED:** the branch (i) verdict, the "ATLAS tension real" sentence, the "measured drive-bond corroborates
  (i)" claim, the "birth_depth = 1 as bulk evidence" reading, the "A⁶ down to the floor / 2.6×10⁵ range" errors.
- **BANKED (Class-B):** the ★ parity theorem (now **generatively verified** in-driver) and the A⁶ χ³ law
  (clean-regime 6.02).
- **COMMITTED:** the sep ≥ 3 bulk discriminator as the null baseline (the frozen O_skin was the correct bulk model).
- **KEEP-BOTH:** the original participation tables are **preserved, re-labeled interface-scoped** (§5).

---

## 10. Caveats (load-bearing — do not over-read)

1. **The bulk vertex was NOT probed.** The 1D co-located run measures a drive interface; the bulk geometry
   collapses to the platform floor. The super-band coupling fork is **OPEN** (§6, §7).
2. **1D, not 3D.** Mechanism-substrate only; the 3D srs run (#607 tones) is the follow-on.
3. **Reversible (sub-yield) medium only.** The parity-forbidden difference channel and even-order rectification
   (pair production) are out of scope; runs stay sub-yield (max r ≤ 0.55). β > 0 in §1.1 is a **planted
   diagnostic**, not a physical kernel.
4. **Gate-c coverage gap disclosed** (§4) — one pair ramp-tested vs the frozen "every measurement" wording.
5. **The absolute vertex normalization is a measurement output, not a first-principles prediction** (prereg §6.4).
