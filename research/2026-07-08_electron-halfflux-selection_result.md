# RESULT — Half-flux selection test: does K4 discreteness FORCE the electron's spin-½ sign?

**Date:** 2026-07-08 · **Lane:** orchestration (electron-interior) · **Status:** COMPLETE
**Prior-mapping:** [`2026-07-08_texture-coupling-prior-mapping.md`](2026-07-08_texture-coupling-prior-mapping.md) (same branch)
**Upstream:** the [SPIN-HALF-POSITED] π₁ result (`electron_pi1_spinhalf_topology.py`, PR #584, branch `analysis/electron-pi1-spinhalf`)
**Drivers (this branch, `main`-runnable):**
[`electron_halfflux_k4_quantization.py`](../src/scripts/vol_2_subatomic/electron_halfflux_k4_quantization.py) ·
[`electron_halfflux_texture_weld.py`](../src/scripts/vol_2_subatomic/electron_halfflux_texture_weld.py) ·
[`electron_halfflux_hopf_phase.py`](../src/scripts/vol_2_subatomic/electron_halfflux_hopf_phase.py)
**Reproduction test:** [`test_electron_halfflux.py`](../src/tests/test_electron_halfflux.py) (6/6 green)
**Tree-proof (origin/main):** `0341cababa92fadc8e680710bd3706b113268fa6` · **Workflow run:** `wf_0d1d1602-38b`

---

## ★ VERDICT — [HALF-FLUX-ECHO]

> The odd-q texture does **not** force the electron's fermion sign. Three independent
> substrate-native framings unanimously return **IMPORT**, under a clean anti-tautology
> gate (no α, no half-angle lift `exp(iσ·ω/2)`, `k_hopf=π/3` never used as an input).
> The electron's spin-½ **selection** remains **posited**, at parity with the Standard
> Model — now confirmed **four** independent ways (π₁ admits-never-forces; the entire
> soliton literature; this no-derived-weld run; and the topology argument below).

---

## 1 — THE STRUCTURE: two ℤ₂'s that the substrate keeps independent

The substrate carries two distinct ℤ₂'s, and forcing the electron to be a fermion
would require a derived term **welding** them. It has none.

- **The texture ℤ₂ — q-keyed.** The ψ-cycle monodromy is `(-1)^q`: odd q=3 → −1
  (half flux, the (0,1) non-SU(2)-liftable class), even q=2 → +1 (integer flux, class
  (0,0)). This DOES discriminate by winding parity. (`texture_flux_continuum`,
  `texture_psi_monodromy`.)
- **The spin/statistics ℤ₂ — winding-INDEPENDENT.** The global 2π-rotation loop
  monodromy is −1 for **every** winding tested — (2,3),(2,2),(1,1),(3,5),(1,2) alike.
  It is the generic belt-trick element, present for any SO(3) field. (`spin_loop_monodromy`.)

**The weld test (`electron_halfflux_texture_weld.py` [C]/[D]):** the two signs do not
co-vary. For (2,2) the texture is +1 while the spin loop is −1 — the even-q control
breaks any weld. The two ℤ₂'s are independent. (For (2,3) both happen to be −1; that
is a **coincident sign, not a weld** — the even-q control is the discriminator.)

## 2 — ★ THE DECISIVE RESULT: the "½" is SO(3)-ℤ₂, not K4

`electron_halfflux_k4_quantization.py` [B] runs the texture flux **both** on the K4
lattice (A4 port-permutation holonomy) **and** in the continuum SO(3) σ-model
(full-angle `rot_z`, Shepperd continuity). They are **identical for every winding**:

| winding | continuum flux | K4-lattice flux | match |
|---|---|---|---|
| (2,3) odd | 0.5 | 0.5 | ✓ |
| (2,2) even | 0.0 | 0.0 | ✓ |
| (1,1),(3,5) odd | 0.5 | 0.5 | ✓ |
| (1,2) even | 0.0 | 0.0 | ✓ |

The "½" is present in the featureless continuum, so it is a property of SO(3)'s ℤ₂
double cover (the belt trick), **not sourced by K4 discreteness**. Anti-tautology
gate (4) fails at the root: the discrete lattice does not force the ½.

## 3 — ★ CORRECTED SCOPE (adversarial-audit correction; supersedes an earlier over-narrow claim)

An initial reading of the QED-creep audit proposed that the negative's scope was only
"no weld **in the transverse sector**" — leaving a "longitudinal/V-sector weld
untested." **That was a rescue narrative and is retracted.** An adversarial audit
(read-and-run) refuted it on two grounds:

1. **The winding-independence is a pre-sector homotopy fact.** The spin τ-class is the
   generator of π₁(SO(3))=ℤ₂, established with **no sector object on the path** (a pure
   full-angle SO(3) continuity-lift monodromy). A **local** coupling term — transverse
   *or* longitudinal — adds energy/phase but **cannot change which homotopy class a loop
   is in**. The obstruction is topological, hence sector-agnostic.
2. **Sector ownership.** An A1/longitudinal channel *selecting* the T2 spin-statistics
   sign would cross-wire the A1⊥T2 ownership the framework forbids. Mode-conversion can
   move energy A1↔T2; it cannot make A1 the *owner* of a T2 topological sign.

**Honest scope of the negative:** *no local term in any sector welds a winding-blind
homotopy invariant to a q-keyed winding class.* What genuinely remains open is a
**global** identification (does a real-space 2π spin necessarily traverse the internal
ψ-cycle?) — but that is a re-definition/import (the three gates already name it), not a
new mechanism.

## 4 — THE THREE FRAMINGS (independent, all IMPORT)

| framing | driver | result |
|---|---|---|
| k4-flux-quantization | `electron_halfflux_k4_quantization.py` | K4==continuum ⇒ ½ is SO(3)-ℤ₂; spin loop winding-independent |
| texture-holonomy-weld | `electron_halfflux_texture_weld.py` | the two ℤ₂'s are independent (even-q control); C3→C2 defect moves −I to even n ⇒ not an odd-q selector |
| hopf-action-phase | `electron_halfflux_hopf_phase.py` | Q_H is loop-invariant (spread ~1e-16) ⇒ accrued phase θ·dQ_H = 0 for any θ; static Q_H~p·q carries p·q-parity, not q-parity |

## 5 — QED-CREEP AUDIT OUTCOME (does not flip the verdict)

An adversarial QED-creep audit found real Maxwell-vector creep and cleared the verdict:
- **`_hopf_density` builds A in Coulomb gauge (transverse)** (`cosserat_field_3d.py:353-377`).
  Only the hopf-action-phase framing calls it. But its null (Q_H loop-invariant, p·q-parity)
  is a property of the **gauge-invariant** Hopf invariant, reproduced off the gauge object
  by the analytic `Q_H≈p·q` — so it **corroborates** the echo, it is not contaminated by it.
- **The "flux quantum Φ/Φ0" is cosmetic** — `arg(sign)/2π`, no h/e; a name on a −1 holonomy.
- **The load-bearing framings are creep-free** — the K4==continuum and winding-independence
  results run entirely through full-angle SO(3) + Shepperd continuity (`uses_analytic_qbody`
  False, AST-guarded). Treating the Cosserat frame's SU(2) lift as spin is substrate-native
  (universal cover of the micro-rotation group, Dirac belt), not an imported Dirac spinor.

## 6 — SIDE FINDING (single-framing; Tier-2 verification owed): `k_hopf=π/3` is de-fitted

`electron_halfflux_k4_quantization.py` [A] finds the engine's fitted coefficient
`k_hopf = π/3` (`cosserat_field_3d.py:926-928`, "matched to Q_H=6") is **exactly the
A4 C3 disclination's SU(2) double-cover half-angle** (120° → π/3), lattice-forced by the
C3 order z=3 (three encircles → −I → half flux → π). This is a genuine provenance
upgrade — a fitted number turning out to be group theory — but it is **single-framing**
and is **not** canonized here; it owes its own clean verification before any KB landing.

## 7 — ANTI-TAUTOLOGY LEDGER

| gate | status |
|---|---|
| No α on the path | ✓ (dimensionless homotopy; `kappa_chiral_from_topology` never called) |
| No half-angle lift `exp(iσ·ω/2)` | ✓ (`uses_analytic_qbody()==False`, AST-guarded) |
| `k_hopf=π/3` not used as an input | ✓ (it falls OUT of A4 C3; never imported) |
| ½ from K4 discreteness alone | ✗ — it is SO(3)-ℤ₂ (K4==continuum) ⇒ ECHO |

## 8 — HONEST PRIOR / SYMMETRIC STANDARD

The import prior held and is now confirmed four ways. This is **peer-with-SM**, not an
AVE deficiency: the SM also posits spin-½ (a chosen Lorentz rep; fermionic fields put in
by hand), and no framework — Skyrme/Witten included — derives the fermion sign from a
purely bosonic single-particle theory without matching to fermionic UV input. AVE derives
the spin-½ *structure* (the double cover, mechanically) and imports the one *bit* of
*selection*. See [[project_form_value_meta_finding]].

## 9 — OPEN QUESTION (not a rescue; a re-definition)

The one substrate question left is **global**: is a real-space 2π rotation physically
forced to also traverse the internal ψ-cycle (which would weld the two ℤ₂'s by identity)?
By §3's reasoning that is an import (a re-definition subject to the three gates), and the
prior — four negatives deep — is that it does not pay. Candidate global structures
(pair-creation genesis; host-BH / geon global topology that could *change the menu* rather
than select from it) are recorded in the conversation but **not** developed and **not**
canonized.

## 10 — PROPAGATION

- **Tier-1 (this doc + drivers + test):** DONE — verdict no longer rests on ephemeral artifacts.
- **Tier-2 (SCHEDULED, gated on Grant-go, KB-leaf-first lockstep):** strengthen
  `clm-rkisb8` / `clm-salw2h` with the four-ways-confirmed selection-is-posited finding;
  reconcile the manuscript overstatement flagged at `electron-identification.md:63`
  ("axiom-derived" vs its leaf's "asserts-not-derives"); verify the §6 `k_hopf=π/3` de-fit
  in its own pass before any KB landing.
- **Tier-3 (PARKED, not canonized):** the interpretive walks (Feynman-diagrams-as-finite-
  network-scattering; Navier-Stokes vortex-spinup as a continuum-limit artifact cured by
  ℓ_node; chirality⊥statistics) are framings, not verified derivations — a research note
  at most, and the Feynman one belongs in the AVE-QED sibling repo, not Core's KB.
