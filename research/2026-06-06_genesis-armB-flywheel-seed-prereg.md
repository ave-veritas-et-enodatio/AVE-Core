# Genesis Arm B — the minimal-IC flywheel seed (PREREG, FROZEN)

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-genesis-armB-flywheel-seed` (off `origin/main` `16b6b6b5`)
**Status:** FROZEN — implementor build pending. Session: orchestration (Grant in-session). Parallel arm to genesis Phase-1 Arm A (two-photon collision, `2026-06-06_electron-genesis-drop-prereg.md`).
**Origin:** Grant 2026-06-06 — *"model an electron's IC by the ω/radius of the collimated B-flywheel + the chirality of the local lattice / E field."* The electron in **three numbers**.

---

## §0 Open goal

Does the **minimal IC** `{ω, R of the collimated B-flywheel, chirality of the E field}` **relax** (under the engine's force-free Beltrami dynamics) **into the electron** — the `(2,3)` winding at `J×B→0`, with **charge = the chirality input** and **mass = ½LI²`? This is the `substrate-native-check` CP8 precursor seed in its purest form: **seed the flywheel, NOT the (2,3); the winding must emerge.** It directly tests Grant's parameterization — is `{ω, R, chirality}` the complete electron IC, with everything else derived?

## §1 The IC (the EE nameplate)

| Input | Sets | via |
|---|---|---|
| **R** (flywheel radius) | size `= ℓ_node`; inductance `L ∝ μ₀R` | geometric |
| **ω** (rotation rate) | ring `ω_C`; current `I` | electron: **`ω·R = c`** (Compton) — one scale |
| ω, R together | **mass** `½LI² = m_ec²`; **spin** `Iω = ℏ/2`; **moment** | inductive flywheel |
| **chirality of E** | **charge sign** (LH Beltrami = e⁻, RH = e⁺) | twist = charge polarity |

Amplitude pinned by `½LI² = m_ec²`; so the free IC is really **`{R, chirality}`** with `ω = c/R`. Canonical: `electron-unknot.md:9` (Beltrami `∇×A=kA`), `mass-closure:89` (`ω_C = c/ℓ_node`), `pair-production-axiom:77` (LH/RH handedness = charge).

## §2 Seed (CP8 precursor — NOT the (2,3), NOT two photons)

A **Beltrami-collimated microrotation (Cosserat-ω) flywheel ansatz** at `(ω, R)` with E-chirality `±` — a localized rotating B-blob in a force-free configuration, the simplest precursor the collision would deposit. Build a flywheel-seeder (distinct from `initialize_2_3_voltage_ansatz`). Engine: `VacuumEngine3D` (the only (2,3) carrier). **Matched-distribution baseline** (same amplitude stats, no collimation/chirality) — emergence must beat it.

## §3 Evolve under force-free relaxation — the check battery (forward, no fit)

1. **`J×B → 0`** — does the flywheel **collimate** (reach force-free)? *This is the stability/"held-together" pass-fail (Grant's phrasing: did it collimate).*
2. **(2,3) emerges** — extractor `w1→2, w2→3` (the winding self-assembles from the bare flywheel)?
3. **Charge = chirality input** — read the winding sign; does it match the seeded handedness?
4. **Mass = `½LI²` = `m_ec²`** — read the inductive-flywheel energy.
5. **Spin = `Iω = ℏ/2`** — the flywheel angular momentum.
6. **Sub-V_yield ring at `ω_C`, size `≈ ℓ_node`** (carry-forward gate).

## §4 Discriminators (pre-committed)

- **(I)** the bare flywheel relaxes to the `(2,3)` at `J×B→0`, charge=chirality, mass=`½LI²` → **`{ω,R,chirality}` IS the complete electron IC; the (2,3) is the force-free attractor** (vindicates the 3-number parameterization).
- **(II)** relaxes to a stable-but-not-(2,3) state → `{ω,R,chirality}` underdetermines; the (2,3) needs more than the bare flywheel (localize what).
- **(III)** never collimates (`J×B` stays finite) → no force-free state from this seed (pin why).

`ave-evidence-framing`: report whichever honestly; (II)/(III) are valid CP8 structural-capability findings.

## §5 Discipline

`substrate-native-check` CP8 (flywheel = precursor, (2,3) emerges, matched baseline) + CP4 (phase-space (2,3) extractor) + CP6 (reactance pair) + CP1 (wave/force-free relaxation, NOT gradient-descent) · `phase-space-coordinate-check` · `consistency-vs-emergence` (mass/spin readouts = consistency; (2,3)-emergence = emergence) · `ave-canonical-source` (`ω_C, ℓ_node, m_e, ALPHA`) · `ave-driver-script-honesty` · `ave-evidence-framing`.

## §6 Relation to Arm A + deliverable

**Arm A** (two-photon collision) *grows* the flywheel from the overlapping-B collision; **Arm B** *seeds the flywheel directly* — the minimal, controlled 3-number test of whether the (2,3) is the force-free attractor of a bare collimated B-flywheel. Reuse the engine + the coordinate-correct (2,3) extractor (`r10_2_3_winding_extractor_coordinate.py`).

**Deliverable:** `research/2026-06-06_genesis-armB-flywheel-seed-result.md` (the 6-check battery, the I/II/III verdict, the matched-baseline) + driver. Reviewed PR; no merge.
