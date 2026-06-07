# Genesis (canonical) — self-trap the ω-shear photon — RESULT

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-genesis-omega-wave` (off `main`; push, do NOT merge)
**Prereg (FROZEN):** [`research/2026-06-06_genesis-omega-wave-prereg.md`](2026-06-06_genesis-omega-wave-prereg.md)
**Driver:** `src/scripts/vol_1_foundations/genesis_omega_wave_selftrap.py`
**Data:** `src/scripts/vol_1_foundations/genesis_omega_wave_selftrap_results.json`
**Discipline:** `substrate-native-check` CP1/4/5/6/7/8 · `phase-space-coordinate-check` · `consistency-vs-emergence` · `ave-canonical-source` · `ave-driver-script-honesty` · `ave-evidence-framing` · `flag-don't-fix` · Rule 11 (honest closure).

---

## §0 Verdict — (III), and the architecture answer to audit §8

**The ω-shear photon does NOT self-trap into the electron under the engine's wave
dynamics.** The third genesis attempt — the *right object* (transverse Cosserat-ω
shear wave) with the *right mechanism* (Axiom-4 saturation) — returns **(III)**, by
a single, clean mechanism, in BOTH engine realizations:

1. **Standalone saturated Cosserat field** (where the saturation IS wired into the
   ω dynamics): the seeded ω-shear wave **disperses** below a curvature threshold
   and **collapses in finite time** above it — it never confines.
2. **Coupled `VacuumEngine3D`** (Arm A/B/C config): saturation is routed **only to
   the K4 V-sector**, never the ω dynamics — so the ω-photon evolves as a bare
   linear wave and leaves the V-sector dark.

**The engine has no wave-dynamics path that turns the saturation impedance-mirror
into a dynamical trap for the ω-photon.** That is the audit §8 architecture answer.

One clean **positive sub-result**: the chiral ω-wave **does carry coherent charge =
Beltrami helicity**, which flips sign with the seeded chirality χ and beats the
matched baseline (§4) — but as a *free* ω-photon, not a confined electron.

---

## §1 The six-check battery (forward, NO fit) — verified numbers

Native units (`ω_C=1`, `ℏ/2=0.5`, `m_ec²=1`, `ℓ_node=1 cell`); engine `ω_yield=π`.
Standalone `CosseratField3D(use_saturation=True)`, N=40, PML=4, 20 Compton periods,
λ=4 cells, sub-CFL `dt=cfl_dt/8`. All values from the results JSON.

| run | A | outcome | A²peak (κ-sector) | H conserved | Γ_min | loc 0→final | signed h 0→final | verdict |
|---|---|---|---|---|---|---|---|---|
| photon_RH_subyield | 0.2 | **disperse** | 0.0029 (no cross) | ✓ (H×0.996) | −0.00 | 0.17→0.04 | −0.98→−0.83 | III |
| photon_LH_subyield | 0.2 | **disperse** | 0.0029 (no cross) | ✓ (H×0.996) | −0.00 | 0.17→0.05 | +0.98→+0.83 | III |
| matched_baseline | 0.2 | disperse | 0.0028 (no cross) | ✓ (H×0.995) | −0.00 | 0.16→0.04 | −0.01→+0.02 | III |
| photon_RH_threshold | 0.5 | **collapse** | 11.6 (crossed) | ✗ (H×919) | −0.99 | 0.17→0.63 | −0.98→−0.26 | III |
| photon_RH_overdrive | 1.0 | **collapse** | 794 (crossed) | ✗ (H×397) | −0.99 | 0.17→0.24 | −0.98→+0.09 | III |

- **Check 1 (self-trap):** ✗ — no clean self-trap at any amplitude. Sub-threshold:
  `loc` DROPS (0.17→0.04, energy spreads/radiates), A² stays ≪1, H conserved →
  **dispersal**. Super-threshold: A² shoots to 11.6 / 794, H blows up ×919 / ×397,
  collapse detected at step 182 / 14 → **finite-time collapse** (a Γ_min=−0.99 forms
  AT the collapse singularity, but it is a blow-up point, not a stable cavity).
- **Check 2 ((2,3)):** ✗ — Cosserat-ω `c=0`, `Q_H≈0` on every photon run (the
  baseline's `c=2` read is noise). No (2,3) emerges. (V-sector probe §3.)
- **Check 3 (charge = helicity):** ✓ as a free-wave property — `h: ±0.98 seed →
  ±0.83` for χ=±1, **flips with χ** (`chirality_flips_helicity=True`), baseline
  `h≈0`. The ω-wave carries coherent helicity; it just does not confine.
- **Check 4 (sub-V_yield ring):** N/A — no settled core forms (disperse or collapse).
- **Check 5 (size/mass/spin):** N/A — no bound object.
- **Check 6 (matched baseline):** ✓ ran — same |ω| stats, randomized directions,
  `h≈0`; disperses like the coherent runs. Emergence had nothing to beat it WITH.

## §2 The mechanism — the saturated ω-energy is non-convex (collapse, not confine)

The Axiom-4 kernel enters the **standalone** ω dynamics as an energy *multiplier*
(`cosserat_field_3d.py:655`): the curvature energy density is
`W_κ·γ·S_κ²` with `S_κ² = 1 − κ²/ω_yield²`, i.e.
`E_curv(κ) = γ·κ²·(1 − κ²/ω_yield²) = γ(κ² − κ⁴/ω_yield²)`.

This is **non-convex**: it rises, peaks at `κ² = ω_yield²/2`, then *falls* — past the
inflection the effective curvature stiffness is **negative**. Energy-conserving
(velocity-Verlet) wave dynamics on a non-convex energy do not confine; they:

- **disperse** when the field stays sub-inflection (`A²_seed ≲ 0.003`; effectively
  linear, `S_κ≈1`), or
- **collapse** (modulational / self-focusing finite-time blow-up) once any region
  crosses the inflection — high-κ becomes energetically *cheap*, so the field
  sharpens without bound.

This is verified, not a CFL artifact: **at fixed physical time, smaller dt makes the
blow-up WORSE** (cfl/16 → H×10³, cfl/32 → 10⁵, cfl/64 → 10⁵; the singularity is
better-resolved, reaching higher A²). The amplitude threshold is sharp: A=0.2
(`A²_seed=0.003`) is stable+disperses; A=0.5 (`A²_seed=0.018`) collapses.

**This is exactly why the engine ships gradient-DESCENT ω-settling** (`relax_to_
ground_state`, the `:1384` settle) and not Hamiltonian wave propagation for bound
states (audit §8 A1.6 flagged the descent as the engine's ω-settler). Descent finds
the bounded minimum; energy-conserving wave dynamics on the same non-convex energy
collapse. The prereg's CP1 directive (wave dynamics, NOT descent) and this engine's
energy are **incompatible for confinement** — and that incompatibility IS the result.

## §3 Architecture finding (the audit §8 question, answered)

> *audit §8: "is the engine's V_inc/V_ref injection a wrong-sector photon, or is the
> TLM-V the correct representation of the transverse mode with the Cosserat-ω a
> separate field the V-side should drive?"*

**Neither engine path carries the ω-shear-wave photon to a self-trapped electron:**

- **Coupled `VacuumEngine3D`** (the Arm A/B/C config): the Cosserat field is built
  `use_saturation=False` (`k4_cosserat_coupling.py:297`) and the coupling force on ω
  is **zero** under `disable_cosserat_lc_force=True` (`:427-428`). So saturation
  modulates **only** the K4 V-sector `z_local`; the ω dynamics are bare/linear.
  **Probe result:** seeding the same ω-photon, `cos.use_saturation=False`,
  `a2_peak 0.07→0.003` (decays, no saturation engagement), `self_trapped=False`,
  and the **V-sector is dark** (`V_inc_max = 0.0`) — the pure-ω seed does not source
  V via the even-in-ω coupling (A1.1), confirmed bidirectionally.
- **Standalone saturated field:** saturation IS in the ω dynamics, but as a
  non-convex energy → disperse/collapse (§2), never a stable trap.

So: **the corpus mechanism "saturation TIR self-traps the photon → electron"
(`photon-identification.md:25`) is not realized as energy-conserving ω-wave dynamics
in this engine.** The (2,3) is two-sector ("2"/Cosserat-ω + "3"/V-sector, audit
A6.3); the pure-ω genesis can only address the Cosserat "2", and even that does not
confine.

## §4 The one positive — charge = helicity is carried by the free ω-photon

EMERGENCE-class, beating the matched baseline (CP8): the chiral ω-shear wave carries
a coherent, signed Beltrami helicity in the **Cosserat-ω sector** (NOT the V-phasor;
audit A3.1):

- RH seed (χ=+1): `h: −0.98 → −0.83`. LH seed (χ=−1): `h: +0.98 → +0.83`.
- Flips sign with χ (`chirality_flips_helicity = True`).
- Matched baseline (randomized directions): `h: −0.01 → +0.02` (≈0).

The seeded ± handedness (charge polarity) is a robust, conserved property of the
free ω-photon. It is the carrier of "charge = helicity" — but the wave never
confines, so this is a property of the **photon**, not yet an electron.

## §5 flag-don't-fix — the load-bearing tension (for Grant)

**Do not silently reconcile** (Grant adjudicates framing-level physics). The corpus
and the engine disagree on what "saturation self-traps the photon" means dynamically:

- **Corpus** (`photon-identification.md:25`): confinement is an **impedance-boundary**
  effect — `V→V_yield ⇒ C_eff→∞ ⇒ Z→0 ⇒ Γ=−1` mirror; a steady-state / boundary-
  condition picture (a self-created TIR cavity wall).
- **Engine** (saturated energy as a Hamiltonian): the same kernel applied as an
  energy multiplier is **non-convex** → Hamiltonian wave dynamics **collapse**, they
  do not build a confining wall.

**Plumber-physical question for Grant:** is the saturation TIR a *boundary-impedance
mirror* that should be imposed as a moving Γ=−1 boundary condition (a wall the wave
reflects off), rather than emerge from energy-conserving evolution of a non-convex
energy? If so, the engine is **missing the boundary-confinement operator** (the
mechanism that turns S_κ→0 into a reflecting wall) — distinct from the energy-
multiplier it currently has. Per A44 (missing-axiom-vs-engine-bug) this reads as an
**engine-mechanism gap**, not a missing axiom; surfaced, not drafted.

## §6 Honest closure (Rule 11) + what this does and does NOT show

- **Falsified (decisively):** "the ω-shear wave self-traps via saturated wave
  dynamics" — across the full sub-yield→over-yield bracket, in both engines.
- **Single mechanism** explains every failure: non-convex saturated energy →
  disperse/collapse; coupling routes saturation off the ω-sector. **No rescue
  attempted; branch closed.**
- **Does NOT show** the corpus claim is wrong — only that THIS engine's wave
  dynamics cannot realize it. A boundary-confinement (moving Γ=−1 wall) mechanism
  is untested and indicated (§5, pending Grant).
- **Does NOT** require a new axiom (A44): the gap is an engine-mechanism gap.
- consistency-vs-emergence: checks 1-2 are the EMERGENCE content (null — no self-
  organized confinement/topology); check 3 is the one EMERGENCE positive (helicity,
  beats baseline); checks 4-5 N/A. All native-unit, NO CODATA.

### The three genesis arms, now consistent

| arm | seed | mechanism | result |
|---|---|---|---|
| A | V-wave (wrong sector) | — | (III) `ω≡0` |
| B | ω-flywheel (wrong geometry) | force-free relaxation (wrong) | (III) de-collimates |
| **C (this)** | **ω-shear WAVE (right object)** | **saturation wave-dynamics (right kernel, wrong dynamics class)** | **(III) disperse / collapse** |

Arm C isolates the remaining gap precisely: the object and the kernel are right; the
**dynamics class** (energy-conserving Hamiltonian on a non-convex energy) cannot
confine. The candidate that remains is **boundary-impedance confinement** (§5).

## §7 References + auditor queue

- Prereg: `research/2026-06-06_genesis-omega-wave-prereg.md`
- Driver + data: `src/scripts/vol_1_foundations/genesis_omega_wave_selftrap.py` (+ `_results.json`)
- Engine citations (verified this session): `cosserat_field_3d.py:655` (saturated κ-energy),
  `:1343` (saturated gradient used by `step()`), `:1384` (descent settle — NOT used);
  `k4_cosserat_coupling.py:297` (coupled `use_saturation=False`), `:427-428` (zero ω-coupling force).
- Corpus: `photon-identification.md:11,24,25` (photon=ω-wave; electron=saturation-TIR self-trap).
- Audit: `research/2026-06-06_simulation-assumptions-audit.md` §8 (sibling branch) — re-aim source.

**Surfaced for the auditor lane to land** (implementer surfaces; auditor lands):
1. Genesis Arm C = (III): ω-shear photon does not self-trap; single mechanism
   (non-convex saturated energy → collapse/disperse). Charge=helicity confirmed for
   the free ω-photon (flips with χ, beats baseline).
2. Architecture (audit §8): the engine has no wave-dynamics confinement for the
   ω-photon — coupled config routes saturation off the ω-sector; standalone saturated
   ω-dynamics collapse. The corpus impedance-mirror (Γ=−1) confinement is a
   **boundary-condition** mechanism the engine does not implement for ω.
3. **Grant adjudication pending** (§5): is the saturation TIR a moving Γ=−1
   boundary wall (impose-as-BC) rather than an emergent energy minimum? Engine-
   mechanism gap (A44), not a missing axiom.
