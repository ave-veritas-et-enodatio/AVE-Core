# G2 photon-family relabel — the photon is the transverse-TRANSLATIONAL pair (u-family), not the node micro-rotation

**Date:** 2026-07-03 · **Type:** ruling + verification-rider + relabel record
**Branch:** `analysis/g2-photon-relabel`
**Ruling author:** Grant Lindblom (2026-07-03, verbatim: *"a it is!"*)
**Resolves:** corpus GAP **G2** ("CHANNEL→DOF MAPPING INVERTED", `_orchestration/2026-06-07_electron-synthesis-epic.md:319`), the pair of `⚠ CHANNEL→DOF LABEL COLLISION — ADJUDICATION PENDING — Grant` tags dated 2026-07-03 at `cosserat-mass-gap.md:153` + `vol1/claim-quality.md:1136`.

---

## 0. Sector header (mandatory, before any standard-physics word)

- **WHICH SECTOR.** The K4 two-sublattice Cosserat lattice, 6 DOF/node = 3 translational `u` (A1 compression + transverse shear) + 3 micro-rotational `ω` (Cosserat couple-stress). The question the ruling settles: **which DOF sector is the photon** — the translational-`u` branches or the micro-rotational-`ω` branches?
- **REGIME.** Cold linear (small-signal) band structure. Saturation OFF. The node-ω mechanical sector's mass gap is the cold `m² = 4G_c/I_ω` gap; the photon pair is the massless acoustic-shear family.
- **PHASE-SPACE vs REAL-SPACE (A46).** Real-space / spatial-Brillouin. The ruling is a real-space DOF-composition claim (which sector carries the massless amplitude), matched by a real-space eigenvector read — NOT a phase-space φ² claim.

---

## 1. THE RULING (Grant 2026-07-03, verbatim)

> the photon = the two massless transverse-TRANSLATIONAL branches (u-family); its magnetic content = the EM-inductive circulation of the u-wave (bond-level curl content), NOT the node micro-rotation; the node ω = the GAPPED mechanical Cosserat sector (home of the static winding topology, Yukawa-screened, short-range).

Three load-bearing pieces:

1. **The photon lives in the translational-`u` sector** — specifically the two massless *transverse*-translational branches. Not the A1 longitudinal/scalar mode (which dissipates via Gauss), and not the micro-rotational `ω`.
2. **The photon's magnetic content is the EM-inductive circulation of the u-wave** — the bond-level curl of the translational wave (∇×u at bond scale), the Axiom-1 μ₀-family **B** field. It is *not* the node micro-rotation. (Two rotation-flavored objects share the loose word "rotation": the massless EM-inductive circulation of the u-wave, vs the gapped mechanical node ω.)
3. **The node micro-rotation `ω` is the GAPPED mechanical Cosserat sector** — the home of the *static* (2,3) winding topology, Yukawa-screened, short-range (`clm-wcoul2`). This is the mass-gap sector, NOT the photon.

---

## 2. THE EVIDENCE STACK

The ruling was made on a stack of prior evidence; the Step-1 rider adds the decisive direct read.

| Evidence | What it shows | Anchor |
|---|---|---|
| Two-sublattice band structure | massless transverse branches at `c=√(G/ρ)=1` (translational-shear speed) + gapped rotational manifold at `ω_m=2`; the massless family tracks the translational sector | `research/2026-06-23_cosserat-band-structure-two-sublattice_prereg-result.md` (V1 c_EM=1, V3 gap m²=4 bit-exact) |
| Winding-pair Coulomb screening | the static (2,3) winding rides the GAPPED ω sector; two windings interact with Coulomb sign structure mediated by the gapped ω (Yukawa-screened, short-range) — ω is mechanical/short-range, not the massless photon | `clm-wcoul2` (`vol4/claim-quality.md`), `master-equation.md:26` cross-link |
| **STEP-1 eigenvector read (this branch, DECISIVE)** | the massless transverse photon-family branches are **u-DOMINATED** (ω-fraction max = **2.5e-7**, u-fraction = **1.000000** at k→0); the 6 gapped branches are **ω-DOMINATED** (ω-fraction min = mean = **1.000000**) | `src/scripts/vol_1_foundations/g2_photon_eigvec_composition.py` + `_output/g2_photon_eigvec_composition.json` |

**The Step-1 read is the fork-to-computable rider:** rather than accept the label change on the corpus prose, it computes the actual DOF composition of each eigenvector off the *genuine* two-sublattice A→B bond operator (imported verbatim from the validated `cosserat_band_structure_two_sublattice.py` — the same operator that recovers the gap bit-exact). The frozen prereg-expectation was the ruling itself (both results recorded): if the massless branches had come back ω-dominated, the driver HALTs and the relabel is *not* authorized — a contradicting eigenvector read would be new evidence Grant must see. It did **not** contradict: massless = u-dominated to 1e-7, gapped = ω-dominated to machine precision. **Relabel AUTHORIZED.**

### 2.1 Flag: the original GAP-G2 statement had the DOF mapping BACKWARDS (flag-don't-fix)

`_orchestration/2026-06-07_electron-synthesis-epic.md:319` (the orchestrator's GAP-G2 diagnosis) states, verbatim:

> canonical k4-port … transverse/SHEAR mode T2 IS the MICROROTATIONAL ω sector (= photon, c=√(G/ρ)); longitudinal/BULK mode A1 is TRANSLATIONAL u (√2c=√(K/ρ), DISSIPATES — Gauss forbids longitudinal EM).

The Step-1 eigenvector read **contradicts this specific mapping**: the massless branch at `c=√(G/ρ)=1` is **u-dominated** (translational transverse shear), not ω/microrotational. The orchestrator's GAP-G2 note pinned "photon = microrotational ω" as the canonical side; the ruling + the eigenvector read establish the opposite — **photon = transverse-translational u**. This is surfaced, not silently reconciled: the orchestrator's :319 line is an in-`_orchestration/` diagnosis (not a KB leaf); the KB relabel here follows the ruling + the measured composition. The orchestrator entry is left for the orchestrator lane to reconcile (not edited by this implementer branch).

---

## 3. THE RELABEL — sites corrected (KEEP-BOTH, dated notes preserved)

Each site gets a dated KEEP-BOTH note (prior text preserved per Rule 12 / audit-trail-in-git); only the family LABEL changes — the surviving physics (transverse survives, Gauss kills longitudinal, gap in the rotational sector) stands.

| Site | Prior label | Corrected to |
|---|---|---|
| `photon-identification.md:11` | "T₂ transverse triplet survives as the photon … `u=0`, `ω≠0`" | surviving pair is transverse-**TRANSLATIONAL** (u-family); physics stands, family label corrected |
| `k4-port-irrep-decomposition.md:26` | "Microrotational ω … THIS IS THE PHOTON" | per ruling: the massless photon family is transverse-translational u; the #491 disambiguation tag gets its ADJUDICATED update |
| `cosserat-mass-gap.md:145` | "the photon per photon-identification … A1 … translational u massless … T₂ … ω carries mass-gap" | had the RIGHT family (translational massless); parenthetical updated to full ruling wording; G2 collision RESOLVED |
| `vol1/claim-quality.md:1126,1131` (`clm-g0mkne`) | "K4 scalar sector … stays massless — the photon" | RIGHT family; updated to full ruling wording; #491 tag → RESOLVED, dated |
| `master-equation.md` (driver-validation hedge, 2026-06-20 note) | mass=A1 vs Verlet-driver-attributes-T2 hedge | dissolution note: the rotational BAND gap (ω sector, Yukawa mass) and the electron's REST-ENERGY store (A1 breather) are different questions; no conflict post-relabel; mass=A1 (PR#260) unchallenged |
| `common/vocabulary-register.md` | (no T₂ disambiguation entry) | mint **INVARIANT-S12** def-entry: T₂ names TWO objects — (1) transverse-translational photon pair vs (2) Cosserat microrotational family (gapped, mechanical, the winding's home); watch-list qualifier rule |

**The #491 `ADJUDICATION PENDING — Grant` tags** at `cosserat-mass-gap.md:153` and `vol1/claim-quality.md:1136` are marked **RESOLVED** (dated 2026-07-03, ruling quoted).

---

## 4. CLAIM-ID updates

- **`clm-g0mkne`** (`vol1/claim-quality.md:1123`, "Cosserat Rotational Mode as the Structural Electron-Mass Mechanism") — the Specific-Claim wording ":1131" labels the massless translational-u sector "the photon." This is the RIGHT family (translational, not ω); the KEEP-BOTH note upgrades the parenthetical to the full ruling wording (transverse-translational u-family) and marks the #491 collision RESOLVED. No confidence change — the mass-mechanism content is untouched; only the photon-family label on the massless sector is clarified.
- No other vol1 claim carries the old "photon = ω/microrotational" wording (verified by grep; see §5).

---

## 5. Verification (verify-before-cite)

- Sites confirmed by grep before edit; the two `ADJUDICATION PENDING` tags are the only two G2 collision markers in the KB (`cosserat-mass-gap.md:153`, `vol1/claim-quality.md:1136`).
- The "THIS IS THE PHOTON" ω-labels: `k4-port-irrep-decomposition.md:26` (and the §-opening line 11 mapping `T₂ ↔ microrotational ω`).
- Step-1 rider reproduces: `PYTHONPATH=src:src/scripts/vol_1_foundations python3 src/scripts/vol_1_foundations/g2_photon_eigvec_composition.py`.

## 6. Scope / non-claims

- This relabel changes **which DOF family is the photon** (translational-u, per the eigenvector read). It does **not** change: the free-vs-locked regime split (weak-C), the PROVENANCE-vs-STATE reading, the mass=A1 grade-assignment (PR#260), or the mass-gap VALUE (`m²=4G_c/I_ω`, bit-exact). Those are orthogonal to the family label.
- The "magnetic content = EM-inductive circulation of the u-wave (bond-level curl)" half of the ruling is recorded as the ruling's physics; a driver directly reading `∇×u` at bond scale for the massless pair is a proposed NEXT rider (not built this branch — the Step-1 read of the DOF composition is what authorizes the label change; the curl-content read refines *how* the u-wave carries B).
- The relationship between this "photon = transverse-u" family label and the earlier 2026-07-03 rotation-flavor KEEP-BOTH tags (which called the photon "massless EM-inductive rotation") is reconciled by piece (2) of the ruling: the photon's *magnetic/inductive rotation* is the **circulation of the u-wave**, not an independent ω DOF — so "EM-inductive rotation" and "transverse-translational u-family" name the same object (the u-wave and its bond-curl), distinct from the gapped mechanical node ω. Surfaced here so the two tag families are not read as contradictory.

## Cross-references

- Ruling anchor: this note (Grant 2026-07-03)
- Step-1 rider: `src/scripts/vol_1_foundations/g2_photon_eigvec_composition.py`, `_output/g2_photon_eigvec_composition.json`
- Band structure: `research/2026-06-23_cosserat-band-structure-two-sublattice_prereg-result.md`
- Genuine bond operator: `src/scripts/vol_1_foundations/cosserat_band_structure_two_sublattice.py`
- Relabeled leaves: `photon-identification.md`, `k4-port-irrep-decomposition.md`, `cosserat-mass-gap.md`, `master-equation.md`, `vol1/claim-quality.md`
- Vocabulary: `common/vocabulary-register.md` (INVARIANT-S12)
- GAP-G2 origin: `_orchestration/2026-06-07_electron-synthesis-epic.md:319` (orchestrator lane; not edited here)
