# RESULT — Mass-Sector Field-Momentum T^{0i}: the §390 R3 false-null hatch

**Status:** RUN-COMPLETE. **OVERALL VERDICT: PASS / FM-DIFFRACTION** at all three separations. The net momentum the field TRANSPORTS between two head-on mass-blobs is **zero**; the only field-momentum imbalance is phase-DEPENDENT, AC-dominated generic-soliton breathing interference. **Gravity is FREQUENCY MODULATION (diffraction) of the carrier via c_eff(A²), NOT a momentum-transport pull** — Grant's prediction confirmed, and the corpus ontology (`optical-refraction-gravity.md:17`) made measurable.
**Prereg:** [`2026-06-23_mass-sector-two-body-scattering_T0i_prereg.md`](2026-06-23_mass-sector-two-body-scattering_T0i_prereg.md)
**Driver:** [`src/scripts/vol_1_foundations/mass_sector_field_momentum_T0i.py`](../src/scripts/vol_1_foundations/mass_sector_field_momentum_T0i.py)
**Regression:** [`src/tests/test_mass_sector_field_momentum_T0i.py`](../src/tests/test_mass_sector_field_momentum_T0i.py) (3/3 PASS)
**Closes:** the §390 result R3 OPEN false-null hatch (`2026-06-23_mass-sector-two-body-scattering_result.md` §1.7), per Grant's run-or-defer ruling (2026-06-23: RUN).
**Branch:** `analysis/soliton-mass-scattering` (PR for orchestrator audit + Grant merge; NO self-merge).

---

## 1. The verdict (PASS / FM-DIFFRACTION)

The §390 centroid-drift readout was SNR<1 against the radiation floor → the null was OBSERVABLE-LIMITED, not substrate-closed (§390 R2). The R3 hatch was the transport-independent field-momentum integral `T^{0i}=(∂_t V)(∂_i V)` — the momentum the field ITSELF transports, computable directly from the engine's stored state (V, V_prev) with ZERO engine change. Grant ruled RUN, with the physical call: **gravity = frequency modulation / diffraction, not a momentum-transport pull.**

Per-separation results (b=0 head-on, symmetric about the true grid center XC=11.5, both relative phases):

| d₀ (cells) | M0 P_total (in) | M2 Φ_x transported (in / out) | M1 dP delivered (in / out) | M1 phase-dep | AC/DC (in) | verdict |
|---|---|---|---|---|---|---|
| 6 | 0.00 | +0.00e+00 / +0.00e+00 | +76.1 / +0.86 | 88.6× | 2.34 | PASS / FM-DIFFRACTION |
| 8 | 0.00 | +0.00e+00 / +0.00e+00 | +102.3 / +2.75 | 37.3× | 1.94 | PASS / FM-DIFFRACTION |
| 10 | 0.00 | +0.00e+00 / +0.00e+00 | +146.1 / +5.88 | 24.8× | 1.50 | PASS / FM-DIFFRACTION |

Source: `mass_sector_field_momentum_T0i_results.json` (`overall_verdicts`, `per_separation[*]`).

**Read of the three observables:**

- **M0 — P_total = 0.0000e+00 EXACTLY** at both phases, all separations. The observable conserves momentum (Newton's 3rd law on the symmetric pair). This is the sanity gate a field-momentum readout lives or dies by; it passes exactly. (Cross-validated: a blob with imposed +x velocity registers P_total = +414.8 — the observable is NOT trivially zero, it responds to real bulk motion. See `test_known_motion_registers_nonzero_momentum`.)

- **M2 — Φ_x (momentum TRANSPORTED across the gap) = 0**, exactly, at both phases. *But this zero is SYMMETRY-FORCED* (see §2): for a head-on b=0 symmetric pair, V is exactly even/odd about the gap face, so T^{0x} is exactly odd and the face-flux is zero by reflection symmetry. M2 alone is necessary, not sufficient — flagged, and the verdict does NOT rest on it.

- **M1 — dP=(P_L−P_R) (momentum DELIVERED to each blob) is the load-bearing discriminator, and it says NO PULL:**
  - **Phase-DEPENDENT** (in/out ratio 25–89×): the in-phase imbalance is large, the out-of-phase imbalance is ~0. A true gravity pull is driven by A²(r) (sign-blind) → it would be phase-INDEPENDENT. Phase-dependence is the textbook generic-soliton coherent-overlap signature (the §390 O2 finding, now confirmed on the momentum channel).
  - **AC-dominated** (ac/dc = std/|mean| = 1.50–2.34 > 1): the in-phase dP swings MORE than its own mean — the imbalance breathes with the soliton and time-averages toward nothing, not a sustained DC pull. (The in-phase mean is also below the single-blob breathing floor: 76–146 vs floor 120–172.)

**Combined:** no momentum is transported across the gap (M2), and the delivered-momentum imbalance is phase-dependent breathing interference (M1), not a phase-independent DC pull. **There is no compression-sector momentum-transport force.** Grant's prediction (P0) is confirmed: gravity is the c_eff(A²) gradient frequency-modulating the carrier phase — diffraction — NOT a mechanical pulling stress tensor.

---

## 2. The symmetry caveat (flag-don't-fix, load-bearing)

The M2 transported-flux zero is **exact** because the setup is exactly mirror-symmetric, not because the driver tuned anything. Verified at a mid-window step: `max|V(x) − V(N−1−x)| = 0.000e+00` for the in-phase pair. For an even-about-XC field:
- ∂_t V is even about XC, ∂_x V is odd about XC,
- so T^{0x}=(∂_t V)(∂_x V) is **odd** about XC,
- so the face-flux (mean of the two mirror planes) is **zero by antisymmetry**.

This means M2=0 would hold for ANY mirror-symmetric configuration — gravity or not. **So the verdict deliberately rests on M1 (delivered-momentum dP), which is NOT symmetry-forced to zero** and which directly tests whether a phase-independent DC pull exists. It does not (phase-dependent, AC-dominated → no pull). The honest framing: M2 confirms momentum-conservation and the absence of any symmetry-breaking transport; M1 is the discriminator that distinguishes "no pull (diffraction)" from "symmetric pull," and it lands on "no pull."

A transport-capable, ASYMMETRIC follow-on (impact parameter b≠0, or a moving frame) would break the symmetry and let M2 register a nonzero flux if a real pull existed; on this transport-less scalar-A1 engine that is out of reach (DEV-6), and M1 already settles the phase-independence question.

---

## 3. Two substrate-native corrections surfaced at driver-time (Rule 10, flag-don't-fix)

Both emerged from running the driver early (Rule 10), via the observable's own momentum-conservation sanity check failing until they were fixed. Neither is a §390 error of physics; both are the difference between a centroid-difference readout (which tolerates them) and a field-momentum readout (which does not).

**CORRECTION 1 — TRUE-CENTER (half-integer) placement.** An N=24 grid has no single center cell; the true center is the FACE between cells 11 and 12, XC=(N−1)/2=11.5. Seeding a blob at integer N//2=12 gives a stationary isolated breather a SPURIOUS net field-momentum: **P_total = +21.6** (the discretization asymmetry). At XC=11.5 the discrete field is bit-symmetric and **P_total = +0.0000e+00 exactly**. The whole test is centered on XC. (Locked by `test_isolated_blob_carries_zero_net_momentum`.)

**CORRECTION 2 — EVEN separations.** The §390 odd-d0 placement (`cxB = N//2 + d0//2 + (d0%2)`) puts the pair off-center about x=N/2 (center at 12.5, midplane at 12) for odd d0 → breaks the LEFT/RIGHT split symmetry and P_total conservation. Even d0 ∈ {6,8,10} with blobs at XC∓d0/2 straddles the gap face symmetrically (distA=distB). Verified: odd d0 → distA≠distB; even d0 → distA=distB.

*Both corrections are fine to skip for a centroid-difference readout (§390 was not wrong to use the odd, integer-centered placement for ITS observable) but are mandatory for a T^{0i} field-momentum readout, which is sensitive to exactly the sub-cell symmetry these fix.*

---

## 4. Substrate-native framing (EE-native): gravity = frequency modulation, not transport

The substrate-native, quotable result:

> **Gravity does not transport momentum between masses; it frequency-modulates the vacuum carrier.** Two A1 dilatation-mass blobs, head-on at b=0, deliver EXACTLY zero net field-momentum to each other (M0 P_total=0, M2 Φ_x=0 by symmetry, M1 delivered-momentum imbalance phase-dependent + AC-dominated → no DC pull). The mechanism is the c_eff(A²)=c₀·(1−A²)^(−1/4) gradient each mass raises in the other's neighborhood: a passing carrier's phase/frequency is modulated (slowed, bent) — it diffracts. There is no mechanical pulling stress tensor doing momentum transport.

This is `optical-refraction-gravity.md:17` made measurable: *"it does not 'fall' due to a mechanical pulling stress tensor; it **diffracts**... Gravity is physically identical to the optical refraction of light propagating through a non-linear dielectric medium."* The T^{0i} integral IS the test of the "mechanical pulling stress tensor," and it reads zero net transport.

**This completes the §390 re-scope.** §390 R2 demoted the null to OBSERVABLE-LIMITED (the centroid readout was SNR<1). The T^{0i} hatch resolves WHY the centroid readout saw nothing: not because the engine can't transduce a force, but because **there is no momentum-transport force to transduce — gravity here is frequency modulation, which moves no net momentum.** The null is REAL for the right reason (momentum-pull-absent), not apparatus-limited. The quotable substrate fact: *gravity only frequency-modulates; it does not pull.*

---

## 5. CONSISTENCY-vs-EMERGENCE label (consistency-vs-emergence skill)

**Class C consistency check — NOT a chord, NOT emergence.** AVE-gravity is FORM-derived / VALUE-imported (MIXED, `optical-refraction-gravity.md:52`, G-ruling `ilk-gravmb`). The FM/diffraction (momentum-pull-absent) result reproduces the corpus gravity ontology via the engine's own c_eff(V) dynamics — a consistency check, not independent AVE-distinct evidence. All inputs engine-natural (T^{0i} from V, V_prev; no CODATA target; natural units; a SIGN/PHASE/AC-DC test, no magnitude pin). No over-claim: this is NOT "AVE gravity confirmed" — it is "the momentum-transport pull is absent; gravity here is frequency modulation," on a scalar-A1 engine, for a symmetric head-on pair.

---

## 6. What survives

- A validated **T^{0i} field-momentum driver** (`mass_sector_field_momentum_T0i.py`) with a passing momentum-conservation sanity gate (P_total=0 exact) and a known-motion positive control — reusable for any mass-sector momentum-transport question.
- The **two substrate-native placement corrections** (true-center half-integer centering; even symmetric separations) — load-bearing for any future field-momentum readout on this engine.
- The **substrate fact**: gravity here transports no net momentum (M2=0, M1 phase-dependent/AC) → it is frequency modulation / diffraction (`optical-refraction-gravity.md:17`), not a stress-tensor pull. The §390 null is REAL for the right reason.
- **Honest caveat**: the M2 transported-flux zero is symmetry-forced; the discriminator is M1 (delivered-momentum, phase + AC/DC), which is not symmetry-trivial and lands on "no pull." A b≠0 / moving-frame asymmetric follow-on (transport-capable engine) is the way to register M2 directly — out of reach on this transport-less scalar-A1 engine.
