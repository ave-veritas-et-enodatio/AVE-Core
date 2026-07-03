# RESULT — Localization Re-Adjudication

**Date:** 2026-07-03
**Prereg (frozen):** [research/2026-07-03_localization-readjudication_prereg.md](2026-07-03_localization-readjudication_prereg.md)
**Branch:** `analysis/localization-readjudication`
**Arc:** re-ask the bulk self-trap question with a PROVEN-LIVE instrument on the
Axiom-1 canonical srs-z3 lattice, after the 2026-07-03 verdict-exposure sweep
found the merged Stage-2/S3 DISPERSE falsifications (#403/#404) evidence-exposed.

---

## 0. VERDICT (frozen bin)

> ## `[DISPERSES-ON-SRS-LIVE]`
>
> The bulk self-trap falsification **RE-BOOKS with solid evidence** on the
> canonical carrier. A smooth localized A1 core, seeded on the chiral srs z=3
> lattice with a **proven-live readout**, **DISPERSES** at every box size — while
> the same instrument correctly reads a known-bound positive control as
> **LOCALIZED_PERSIST**. The boundary/topological localization reroute (#403/#404)
> **stands, now grounded** on the Axiom-1 canonical carrier rather than on the
> exposed diamond instrument.

**Seduction-trap check (prereg §1.1):** the exposure did NOT establish "the
electron localizes in the bulk after all." It established that the diamond
instrument's DISPERSE read was muddied by a 93% frozen-nullspace artifact. When
the question is re-asked on a carrier with a clean readout (nullspace dim 1), the
answer for the smooth bulk core is still DISPERSE. The reroute is confirmed, not
overturned.

**Scope-lock (carried verbatim):** mass = A1 (PR#260, PR#311 ECHO-final) is NOT
at stake and is untouched. Only the localization MECHANISM (bulk-pressure basin
vs. boundary/topological pin) was re-adjudicated. The A1-only srs runs evolve the
mass-sector breather alone; ω was not evolved (winding_on=False).

**Grant's standing expectation (recorded):** the corpus prior was that the bulk
does NOT self-trap (localization = BOUNDARY/TOPOLOGICAL; bulk-cage FALSIFIED
+MERGED #403/#404). The engine verdict here **agrees** with that expectation.
Both the expectation and the engine verdict are recorded per the prereg.

---

## 1. THE EXPOSURE, RE-VERIFIED AT HEAD (verify-before-cite)

All three exposure findings re-run by me this session, extracting the ORIGIN
operator verbatim (`native_cage_imex.build_grad_div_periodic` + `assemble_L_D`)
and running it read-only:

| finding | this-session number | operator |
|---|---|---|
| sublattice decoupling | off-diag \|mass\| 100.00% same-parity, 0.0000 cross-parity (N=8/10/12) | diamond L_D |
| nullspace burden | 16 / 8 / 16 near-zero eigenvalues (N=8/10/12); ‖L_D·Nullbasis‖=2.6e-15 | diamond L_D |
| v14 sech dead-leg | 93.5% of L²-energy in the nullspace at N=12 (live = 6.5%) | diamond L_D |
| srs contrast | nullspace dim = **1** (constant mode only) at L=4/6/8 | srs L_srs |

The four diamond TETRA_OFFSETS all have ODD coordinate-sum
(`cosserat_field_3d.py:134-139`; sums 3,−1,−1,−1), so `L_D = Div·diag(D)·Grad`
connects only same-parity nodes → the periodic diamond box is two
non-communicating sublattices, carrying a large frozen kernel a smooth centred
seed dominantly occupies.

---

## 2. STEP 1 — NATIVE-DIAMOND POSITIVE CONTROL (the diamond instrument is NOT dead)

Three known-bind configs pushed through the ORIGINAL Stage-2 `classify()` +
`run_native_imex` IMPORTED VERBATIM (the IDENTICAL pipeline; never redefined).
Nullspace fraction read BEFORE each verdict (Step 3.8a). Full numbers:
[`results/localization_readjudication_step1_diamond_positive_control_results.json`](../results/localization_readjudication_step1_diamond_positive_control_results.json).

| route | construction | null-frac (N=24) | live-frac | verdict | frozen-artifact? |
|---|---|---|---|---|---|
| 1 | low-λ localized L_D eigenmode (λ=0.067, participation 11%) | 3.7e-32 | **1.0** | **MODE_I_PERSIST** | no |
| 2 | even-sublattice-only sech | 0.672 | 0.328 | MODE_III_DISPERSE | no |
| 3 | v14 sech projected OUT of the 16-dim nullspace | 2.0e-29 | 1.0 | MODE_III_DISPERSE | no |

**Step-1 verdict: `INSTRUMENT_CAN_SEE_TRAP`.** Route 1 reads MODE_I_PERSIST with
a GENUINE live fraction (all 6 legacy bins pass, max\|V\|=0.85 bounded) — the
diamond `classify()` CAN register bound for an operator-governed localized input.
So the original DISPERSE verdicts regain PARTIAL standing: the readout was NOT
dead. BUT — route 3 is the key: the v14 sech, with its 93% frozen-nullspace
content removed, leaving only the 6.5% the operator governs, **disperses**. The
original v14 DISPERSE was reading a mix of a spurious frozen dead-leg AND a
genuinely-dispersing live part — never a clean read. This is exactly why the
question needed re-asking on a clean carrier.

**Consistency-vs-emergence tag:** INFRASTRUCTURE (instrument liveness).

---

## 3. STEP 2 — SPECTRAL-LIVENESS DIAGNOSTIC (first-class, reusable)

`src/ave/solvers/spectral_liveness.py` — decomposes any seed against any SPD
div-form operator's spectrum; reports nullspace-energy fraction + spectral-weight
profile. The standing pre-run readout-liveness check (ave-prereg v1.4 Step 3.8
operationalised). Test keepers (`src/tests/test_spectral_liveness.py`, 7 passing)
reproduce the exposure independently:
- diamond L_D N=12: nullspace dim 16, v14 sech nullspace fraction > 0.85.
- srs L_srs: nullspace dim 1; sech core live fraction 0.895 (13.7× the diamond's
  0.065).

**FINDING (flag-don't-fix, L-invariant over L=4/6/8):** the srs sech's ~0.105
nullspace overlap is the seed's **DC/constant content** — an all-positive sech has
a nonzero mean absorbed by the graph Laplacian's single constant-mode nullspace.
This is NOT a frozen dead-leg like the diamond's 8-16 dim kernel; it is the
physical DC overlap, reported-and-subtracted per prereg §6.5.

**Consistency-vs-emergence tag:** INFRASTRUCTURE.

---

## 4. STEP 3 — THE srs-z3 RE-RUN (the physics reading)

A1-only srs core (mass=A1 scope-lock) on the canon `SrsCageWinding` /
`assemble_L_srs` (Rule-14: adapt the certified core). Canon-derived
parameterization (§6.1 of the prereg); dt/L/seed-width tagged ENGINEERING-CHOICE.
Energy-conserving unitary Cayley stepper (no damping can fake a pin). Full numbers:
[`results/localization_readjudication_step3_srs_rerun_results.json`](../results/localization_readjudication_step3_srs_rerun_results.json).

### 4.1 The closed-box localization metric (KEEP-BOTH)

The srs supercell is **fully periodic** (no PML/absorbing boundary; interior mask
= all nodes). The diamond driver's "PML-excluded interior peak" observable has NO
analog. So the srs re-run **ADDS** a closed-system localization metric ALONGSIDE
the legacy peak bins (KEEP-BOTH, never redefine): the **participation number**
PN = 1/Σpᵢ² (pᵢ = per-node energy fraction). SMALL = localized; LARGE (→ n_nodes)
= dispersed. This is LOCAL (per-node), degeneracy-safe (NOT a global sum that
telescopes to zero on the closed graph — the exact EM-readout Stage-1 killer the
Step 3.8 provenance names).

### 4.2 Results

| seed | L | null-frac | verdict (legacy) | verdict (srs) | PN₀ → PN_post | E-drift |
|---|---|---|---|---|---|---|
| **positive control** (λ eigenmode) | 4 | 0.469 | MODE_I_PERSIST | **LOCALIZED_PERSIST** | 48.5 → 13.0 | 2.3e-10 |
| **positive control** (λ eigenmode) | 6 | 0.348 | MODE_I_PERSIST | **LOCALIZED_PERSIST** | 80.2 → 31.4 | 1.6e-10 |
| **smooth core** (v14 sech) | 4 | 0.105 | MODE_I_PERSIST | **DISPERSED** | 9.8 → 162.0 | 6.3e-9 |
| **smooth core** (v14 sech) | 6 | 0.105 | MODE_III_DISPERSE | **DISPERSED** | 32.7 → 801.9 | 2.2e-9 |
| delocalized null | 4/6 | — | — | DISPERSED (floor) | → 256 / 862 | — |
| constant-mode null | 4/6 | — | — | DISPERSED | = 512 / 1728 | — |

**Readout-liveness gate PASSED (Step 3.8a):** the positive-control eigenmode reads
LOCALIZED_PERSIST at both L (it stays localized and sharpens: PN drops 48.5→13.0
and 80.2→31.4). The smooth-core verdict is booked only AFTER this certification.

**The smooth A1 core DISPERSES at every L** with energy conserved (drift ~1e-9,
so no numerical damping is masking or faking the result). PN grows 16.5× (L=4)
and 24.5× (L=6) toward the delocalized floor. The null controls behave (both read
DISPERSED at the full-box PN), so the metric is not trivially calling everything
localized.

### 4.3 KEEP-BOTH payoff (flag)

At L=4 the **legacy peak-bin reads MODE_I_PERSIST** (mean_post 0.239 > 0.2) even
though the core has dispersed 16.5× — because closed-box PBC recirculation returns
energy to the origin and gives a nonzero peak. The **srs-native participation
metric correctly reads DISPERSED**. The added metric caught what the legacy
peak-bin could not in a closed box. This is the KEEP-BOTH discriminator earning
its place: had the srs re-run used the legacy peak-bin alone, L=4 would have
mis-read PERSIST.

**Consistency-vs-emergence tag:** the srs re-run verdict is the PHYSICS reading —
MANIFESTATION class (a time-domain dynamical property of the canon operator on the
canon carrier; α-free, no CODATA input). NOT an emergence claim.

---

## 5. THE D1 EVIDENCE SECTION — the two carriers AS INSTRUMENTS

This section feeds Grant's pending D1 ratification (srs-z3 as production carrier).
**Instrument comparison ONLY. NO lattice-ontology claim** — whether the srs "is"
the vacuum is Grant's D1 call; this provides the instrument evidence.

| axis | diamond z=4 (achiral) | srs z=3 (chiral) |
|---|---|---|
| **statics well-posedness** | sublattice-decoupled: L_D = Div·diag·Grad couples only same-parity nodes (100% same-parity, 0 cross) → two non-communicating manifolds | well-posed graph Laplacian L_srs = Bᵀ·diag·B; Stage-1 EM-readout proved srs statics |
| **nullspace burden** | 8-16 dim FROZEN kernel (N=8/10/12); a smooth centred seed sits 93% in it | **1 dim** (constant mode only) at L=4/6/8 |
| **smooth-core live fraction** | **6.5%** (v14 sech) | **89.5%** (the 10.5% shortfall is the seed's DC content, not a dead-leg) |
| **positive-control constructibility** | YES — a low-λ localized eigenmode reads MODE_I_PERSIST (§2 route 1); the instrument is NOT dead, but the smooth seed's read is muddied by the dead-leg | YES — a localized eigenmode reads LOCALIZED_PERSIST cleanly (live fraction ~0.5-0.65, no dead-leg muddying) |
| **chirality** | achiral (Fd-3m, inversion-symmetric); writhe ≡ 0 → CANNOT carry the (2,3) winding handedness = charge (`srs_cage_winding.py:11-16`) | chiral (I4₁32/I4₃32, no inversion centre); writhe ≠ 0, sign-flips L/R → CARRIES charge/spin/parity |

**Instrument summary:** on all five axes the srs z=3 is the cleaner instrument for
a localization test. The diamond is not DEAD (it can read a bound eigenmode), but
a smooth seed's read is dominated by a frozen dead-leg the smooth core cannot
avoid, and the diamond structurally cannot carry the chirality the electron's
charge lives in. The srs reads a smooth core's fate through an operator with no
dead-leg and a single (physically-meaningful DC) nullspace mode. This is the
instrument evidence for D1; the production-carrier ratification is Grant's.

---

## 6. RELATIONSHIP TO THE EXPOSED STAGE-2/S3 DOCS (cite, do NOT edit)

Per the collision guard, this arc does NOT edit the Stage-2/S3 result docs (a
sibling agent owns the exposure caveats). The relationship:

- **`research/2026-06-24_engine-stage2-native-cage_result.md`** (Stage-2 bulk
  self-trap DISPERSE): **SUPERSEDED-WITH-EVIDENCE + CORROBORATED.** Superseded as
  the *load-bearing* falsification because it ran on the exposed diamond
  instrument (93% dead-leg, no same-pipeline positive control). CORROBORATED in
  *direction*: re-asked on the canonical srs carrier with a proven-live readout,
  the smooth bulk core still DISPERSES. The DISPERSE conclusion survives; its
  evidential basis is now the canonical carrier.
- **`research/2026-06-24_engine-s3-cavity-pinning_result.md`** (S3 cavity-pinning,
  §5 admits the native vector operator unwinds the (2,3) uncoupled): the S3
  cavity-pinning EXTENSION was NOT ported this arc (step-3a was gated on the
  bulk-core result landing cleanly, which it did as DISPERSE — a cavity-pinning
  extension of a dispersing core is a downstream follow-on, not this arc's scope).
  Relationship: **CORROBORATES** the S3 doc's own §5 self-flag that the native
  vector operator is category-mismatched to the winding; the srs carrier is the
  chirality-carrying fix.

Neither exposed doc is edited. The reroute mechanism they support (#403/#404) is
confirmed on the canonical carrier.

---

## 7. HONEST CLOSURE (Rule 11) + WHAT REMAINS OPEN

The pre-registered question got a **decisive answer** via a proven-live
instrument. A single mechanism (frozen-nullspace dead-leg on the diamond)
explains why the original diamond read was muddied, and the clean-carrier re-run
confirms the smooth bulk core disperses. This is the discipline working at full
strength: a clean reading, the boundary/topological reroute grounded, the branch
closed. NOT debugged toward a rescue.

**Open follow-ons (NOT this arc's scope; tracked for later sessions):**
1. The S3 cavity-pinning extension on srs (a dispersing bulk core + an external
   cavity — does the cavity pin what the bulk cannot self-trap?). Downstream.
2. The `[BINDS-ON-SRS]` adversarial panel is NOT triggered (the verdict is
   DISPERSES, not BINDS) — but the prereg's requirement stands if any future run
   flips it.
3. The D1 production-carrier ratification (Grant's call; this arc provides the
   instrument evidence in §5).

---

## 8. CONSISTENCY-VS-EMERGENCE LEDGER

| deliverable | class |
|---|---|
| Step 1 diamond positive control | INFRASTRUCTURE (instrument liveness) |
| Step 2 spectral-liveness diagnostic | INFRASTRUCTURE |
| Step 3 srs re-run VERDICT | PHYSICS reading — MANIFESTATION (α-free, no CODATA) |
| Step 4 D1 section | INFRASTRUCTURE (instrument comparison) |

No emergence-class claim is headlined. The only physics reading is the srs
re-run bin (`[DISPERSES-ON-SRS-LIVE]`), a manifestation of the canon operator's
dynamics on the canon carrier.

---

## 9. ARTIFACTS

- Prereg: `research/2026-07-03_localization-readjudication_prereg.md`
- Diagnostic: `src/ave/solvers/spectral_liveness.py` +
  `src/tests/test_spectral_liveness.py`
- Step-1 driver + results:
  `src/scripts/localization_readjudication_step1_diamond_positive_control.py`,
  `results/localization_readjudication_step1_diamond_positive_control_results.json`
- Step-3 driver + results:
  `src/scripts/localization_readjudication_step3_srs_rerun.py`,
  `results/localization_readjudication_step3_srs_rerun_results.json`
