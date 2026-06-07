# Genesis Arm B — the minimal-IC flywheel seed (RESULT)

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-genesis-armB-flywheel-seed` (off `main`)
**Prereg (FROZEN):** [`research/2026-06-06_genesis-armB-flywheel-seed-prereg.md`](2026-06-06_genesis-armB-flywheel-seed-prereg.md)
**Driver:** [`src/scripts/vol_1_foundations/genesis_armB_flywheel_seed.py`](../src/scripts/vol_1_foundations/genesis_armB_flywheel_seed.py)
**Results JSON:** `src/scripts/vol_1_foundations/genesis_armB_flywheel_seed_results.json`
**Parallel arm:** Arm A (two-photon collision) — separate worktree, untouched.

---

## §0 The question

Does the minimal IC **`{ω, R of the collimated B-flywheel, chirality of the E
field}`** relax — under the engine's force-free (Beltrami) dynamics — into the
**electron**: the `(2,3)` winding at `J×B→0`, with **charge = the chirality
input** and **mass = ½LI²`? I.e., is the electron just three numbers, with the
`(2,3)` emerging as the force-free attractor of a bare collimated B-flywheel?

## §1 What was seeded (the CP8 generative precursor — NOT the (2,3))

A bare collimated B-flywheel — a localized single-helicity **Lundquist
force-free flux rope** in the Cosserat ω field (the inductive / microrotational-B
flywheel; `dual-reactance-storage-taxonomy.md:72,80`: *"3 microrotational-B DOF →
inductive flywheel"*; `ave-kb/CLAUDE.md:55`: *"3 microrotational → B; Cosserat
rotational DOF IS the substrate-native origin of intrinsic spin"*). In
cylindrical `(ρ, φ, z)` about the lattice centre, with twist `k = ω/c` (native
`c=1`):

```
ω_z(ρ) = A · env(ρ,z) · J₀(kρ)              (collimated axial spin)
ω_φ(ρ) = A · chirality · env(ρ,z) · J₁(kρ)  (azimuthal circulation; ± = handedness)
```

`J₀/J₁` make `∇×ω = ±kω` EXACTLY in the unwindowed column (the seed is force-free
by construction in the core; `chirality=+1 ⇒ ∇×ω=+kω` RH, `−1 ⇒ ∇×ω=−kω` LH —
verified analytically). The localizing envelope (radial scale `R`, gentle
`2.5R` z-column) is the only departure from exact force-free — that is what makes
it a *finite flywheel*. The E-field half (the "chirality of the E field") is the
SAME Beltrami vector field projected onto the K4 ports (T₂ photon pattern) into
`V_inc`, so the precursor deposits one coherent single-helicity EM blob in BOTH
reactance sectors. Amplitude `A` is **pinned by the mass condition
`½·I_ω·Σ|ω|² = m_ec² = 1`** (prereg §1).

**Distinctness from the (2,3) ansatz (CP8 requirement).**
`initialize_flywheel_seed` is provably distinct from
`initialize_2_3_voltage_ansatz` (`tlm_electron_soliton_eigenmode.py:34`): NO
`θ=2φ+3ψ` winding, NO `(2,3)` knot-tangent `chirality_weight` port projection,
NO toroidal shell — a cylindrical Bessel flux rope parameterized by exactly the
three numbers. If the `(2,3)` is the force-free attractor, it must EMERGE.

The electron point is **`ω·R = c`** (Compton, prereg §1): with `R` in cells and
`ω = c/R` native, **`k·R = 1`** — one helical twist per flywheel radius.

## §2 The 6-check battery — numbers

Config: `N=40, PML=4, n_periods=36` (320 steps, `dt=1/√2`), coupled
K4+Cosserat (Arm-C config: asymmetric μ/ε saturation, Cosserat self-terms, A28
LC-force off). Force-free relaxation = the engine's own `step()` wave dynamics
(CP1 — NOT gradient descent). All reads forward, NO fit.

| # | check | flywheel (electron pt) | baseline | result |
|---|---|---|---|---|
| 1 | `J×B→0` (collimate) | **0.60 → 0.92** (residual *grows*) | `k·R=3` ctrl: 0.20→0.82 | **FAIL** — force-free not an attractor; disperses |
| 2 | (2,3) emerges | `w1=w2=0, c=0` | `w1=w2=1, c=0` | **FAIL** — no winding (no false positive either) |
| 3 | charge = chirality | moot (no emergent winding) | — | moot |
| 4 | mass = ½LI² | 1.0 → **0.46** | → 0.15 | consistency — 3× retention, neither holds |
| 5 | spin = Iω = ℏ/2 | net `Sz = −66` (diffuse) | `Sz = −0.9` | consistency — 70× coherent L, but ≫ ℏ/2, not quantized |

`summary.overall_verdict = III`, `summary.any_collimation = False` (JSON-confirmed).

### Check-by-check

- **Check 1 (collimation):** the energy-weighted force-free residual **grows** under the engine's own evolution at *every* config — electron point `0.60→0.92`, and decisively the well-collimated `k·R=3` control `0.20→0.82`. **The force-free Beltrami state is NOT a dynamical attractor of the coupled K4–Cosserat dynamics for a localized flywheel** — a seeded force-free flux rope *de-collimates* and disperses, it does not tighten.
- **Check 2 (winding):** `w1=w2=0, c=0` from the flywheel; `w1=w2=1, c=0` from the random baseline. No (2,3) from either → no amplitude-confound false positive.
- **Check 3 (charge):** the precursor Cosserat helicity is chirality-*determined* at seed (LH→+0.37, RH→−0.37) but **sign-inverts under evolution** (flagged — same family as Arm A's noise-reading sign extractor; helicity is not conserved by the relaxation).
- **Checks 4–5 (mass/spin):** consistency-class. Mass dissipates `1.0→0.46` (vs 0.15 baseline); net `Sz=−66` (vs −0.9). The structured seed carries **~3× the mass and ~70× the coherent angular momentum** of noise — structure is real — but it is **diffuse**, never a quantized `½LI²`/`ℏ/2` soliton.

## §3 Matched-distribution baseline (CP8 MANDATORY)

Matched-distribution (same amplitude statistics, no collimation/chirality): the flywheel **beats** the baseline on retention (mass 0.46 vs 0.15; |Sz| 66 vs 0.9) — so the structure is *not* an amplitude artifact — but **neither produces the (2,3), and both fail collimation.** Structure matters; it just doesn't reach the electron.

## §4 Verdict — discriminator (I)/(II)/(III)

**(III) — the bare flywheel `{ω,R,chirality}` does NOT collimate into the (2,3).** A localized, single-helicity, force-free Cosserat flux rope — even seeded *exactly* force-free in the core — **de-collimates and disperses** under the engine dynamics; the (2,3) is not the force-free attractor of a static flywheel. The 3-number IC carries the right *quantities* (mass, spin, helicity, all out-performing noise) but does not relax into the *quantized topological soliton*.

## §5 Discipline walk (which skills fired)

- **`substrate-native-check` (v1.1)** — full 8-checkpoint walk recorded verbatim
  in the driver module docstring. Load-bearing: **CP8** (seed the generative
  precursor = bare flywheel; the `(2,3)` must emerge; matched-distribution
  baseline) + **CP1** (force-free relaxation = `engine.step()` wave dynamics, NOT
  gradient-descent) + **CP4** (the `(2,3)` read by the coordinate-correct
  phase-space extractor `extract_2_3_spatial`, reused verbatim) + **CP6**
  (reactance pair: C-state `V_inc`/ω AND L-state `Φ_link`/ω̇ recorded every step).
  CP2/CP3/CP5/CP7 recorded.
- **`phase-space-coordinate-check`** — the `(2,3)` is measured on the Clifford
  torus (internal U(1) phase from `V_inc`/`Φ_link`), matching the corpus claim's
  coordinates; the J×B / mass / spin readouts are real-space Cosserat
  diagnostics, tagged consistency.
- **`consistency-vs-emergence`** — mass=`½LI²`, spin=`Iω`, charge=winding-sign vs
  chirality are **CONSISTENCY-class** (amplitude pinned by the mass; reading it
  back is self-consistency). The `(2,3)`-from-bare-flywheel is the
  **EMERGENCE-class** claim.
- **`ave-canonical-source`** — `ALPHA, V_YIELD, V_SNAP` from
  `ave.core.constants`; native `c=ℏ=m_e=ℓ_node=1 ⇒ ω_C=1, ℏ/2=0.5, m_ec²=1`.
- **`ave-driver-script-honesty`** — forward reads only; no optimizer is run onto
  `(2,3)`; the matched baseline is the anti-amplitude-confound control.
- **`ave-evidence-framing`** — `(II)`/`(III)` are valid CP8 structural-capability
  findings; no success is forced.

## §6 The one modeling choice (flag-don't-fix)

Single mechanism: **the test seeds a localized flywheel and relies on *force-free relaxation* to find the (2,3) — but force-free is not a relaxation attractor here.** Cross-referenced against the canonical photon (`photon-identification.md:11,24`): the electron is *"a self-trapped photon,"* formed by **Axiom-4 saturation TIR confinement** (V→V_yield ⇒ Γ=−1 cavity), NOT by force-free relaxation of a blob, and the photon is a transverse Cosserat-ω **shear WAVE** (ω≠0), not a localized flux rope. So Arm B has the right *sector* (ω) but the wrong *geometry* (flywheel vs wave) and *mechanism* (relaxation vs saturation-confinement). The indicated re-aim is the **canonical genesis**: seed the transverse Cosserat-ω shear wave, drive across `V_yield`, watch it self-trap. (See assumptions-audit §8.)

## §7 Relation to Arm A + carry-forward

**Both genesis arms are (III), and consistently so:** Arm A (V-wave collision) hosted the *geometry* (ℓ_node pair) but not the *carrier* (ω≡0 — wrong sector, the photon is ω); Arm B (ω-flywheel) seeded the *carrier* but it does not collimate (wrong geometry + wrong mechanism). Neither seeded the **canonical photon** = the transverse Cosserat-ω shear **wave**, nor used the canonical **saturation-confinement** mechanism. The two nulls *rule out* the two wrong paths and converge on the canonical re-run (audit §8): **self-trap the ω-shear wave.** Carry-forward: (a) the canonical-photon genesis re-run; (b) the helicity sign-inversion (Check 3) is a real non-conservation worth a separate probe.
