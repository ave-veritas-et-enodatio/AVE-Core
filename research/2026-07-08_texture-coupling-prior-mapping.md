# PRIOR-MAPPING — the §5 texture→spin coupling (route to [SPIN-HALF-DERIVED])

**Date:** 2026-07-08 · **Lane:** orchestration recon (pre-build) · **Status:** PRE-BUILD — awaiting mechanism walk
**Purpose:** map the internal + external prior BEFORE attempting to derive a substrate-native term
that would upgrade the electron's spin-½ from POSITED to DERIVED. This is the walk-the-picture-first
recon that precedes any dispatch. It records the terrain and the honest prior; it does **not** build.

**Upstream result:** `research/2026-07-08_electron-pi1-spinhalf_result.md` (branch
`analysis/electron-pi1-spinhalf`, PR #584) — **[SPIN-HALF-POSITED]**. π₁ of the electron's
SO(3)-Cosserat configuration space is ℤ₂ (spin *structure* / double cover DERIVED, lift-free), but the
2π-rotation loop class is winding-INDEPENDENT, so π₁ ADMITS both boson and fermion and cannot FORCE
spin-½. The one open path to [SPIN-HALF-DERIVED] is the §5 texture class: for the (2,3) electron the
[T²,SO(3)] class is **(0,1)** — the odd q=3 cycle is non-SU(2)-liftable. IF a substrate-native ℤ₂ /
Wess-Zumino / Hopf term can be DERIVED (not posited) from the K4 constitutive action and COUPLES the
spin quantization χ(τ) to this odd-winding texture, it forces χ(τ)=−1.

---

## THE QUESTION

Can the sign that selects the fermion sector (χ(τ)=−1, currently the `/2` in `exp(iσ·ω/2)`) be
**derived** from the K4 / Cosserat constitutive action — or must it be **imported** (posited, or matched
to a fermionic ingredient)? The prior mapping establishes how hard this is, whether there is any
precedent, and what a build would have to survive.

---

## EXTERNAL PRIOR (physics literature)

Retrieval via the external-retrieval pipeline (in-session WebSearch pass; hardenable by a redundant
Gemini pass on the same brief). Symmetric-standard: reports where the mainstream ITSELF imports.

**Bottom line: across every soliton model in the literature, the spin-½-forcing topological term is
never conjured from a purely bosonic theory — its coefficient is always either (a) posited as a free
parameter, or (b) inherited by matching to a more microscopic theory that already contains fermions.**
Configuration-space topology admits both statistics; it never forces one.

| Result | Establishes | Sign/coefficient — derived or imported |
|---|---|---|
| **Finkelstein–Rubinstein 1968** (J. Math. Phys. 9, 1762) | soliton spin↔statistics *correlation* from π₁(config space); π₁=ℤ₂ (2π rotation non-contractible) | **ADMITS only.** Selection = a choice of 1-D unitary rep of π₁, i.e. an element of Hom(ℤ₂,U(1))={+1,−1}, supplied from outside. **Directly CONFIRMS the π₁ result's "admits-never-forces" claim.** (Corrob: Krusch hep-th/0610176; review arXiv:0810.2399.) |
| **Witten 1983** (Nucl. Phys. B 223, 422 & 433) | Wess–Zumino term obeys a topological quantization law (integer coeff, from π₅); odd coeff ⇒ Skyrmion is a fermion | *Form/integrality DERIVED*; **VALUE matched** — coeff = N_c (QCD color number, an input). 2π-rotation phase = (−1)^{N_c}. Skyrme Lagrangian alone is silent on N_c. |
| **Wilczek–Zee 1983** (PRL 51, 2250) | (2+1)d Hopf/θ-term gives soliton spin θ/2π + anyonic statistics | **θ POSITED** — free continuous parameter; θ=0 boson, θ=π fermion. Model does not fix θ. *(tentative on exact PRL wording — full text 403'd; substance multiply corroborated.)* |
| **Faddeev–Niemi Hopfions / CP¹ Hopf term** | knotted solitons (π₃(S²)=ℤ); a Hopf/θ-term gives them fractional spin | **POSITED in pure model; MATCHED-to-fermion-content when induced** (integrate out Dirac fermions ⇒ θ fixed by fermion content, "as the θ-term in QCD"). *(tentative on verbatim quotes.)* |
| **Balachandran et al.** | general spin-statistics for solitons; statistics *transmuted* by adding topological terms | **Selection requires an action-level input.** Topology permits; the added term (with a chosen sign/coeff) selects. *(tentative on exact wording; substance corroborated.)* |
| **General consensus** (0810.2399; nLab) | π₁ + Hom(π₁,U(1)) fixes the *menu* of statistics | **π₁ alone cannot force the fermion.** An action-level term (WZ/Hopf/θ/CS/Berry) whose coeff is posited or matched is always required to select. Friedman–Sorkin geons even *violate* the naive correlation — topology permits, does not dictate. |

**No source contradicted the internal result.** The mainstream is in the same boat: it derives the FORM
of the spin-statistics structure but imports the VALUE/sign — structurally identical to AVE's standing
"forces FORMS, imports VALUES" meta-finding.

---

## INTERNAL PRIOR (AVE corpus)

Verbatim file:line map (read-only recon). Attribution: upstream result doc is on branch
`analysis/electron-pi1-spinhalf` (unmerged); everything else is on `main` @ `0341caba`.

1. **§5 texture result** — `research/2026-07-08_electron-pi1-spinhalf_result.md:126-140` +
   `src/scripts/vol_2_subatomic/electron_pi1_spinhalf_topology.py:131-145`. The (0,1) class and odd-q=3
   non-liftability are DERIVED as a homotopy/texture classification. The forcing coupling is
   **explicitly self-declared absent from the corpus** ("That coupling is not in the corpus").

2. **FR-braid spin-statistics** — `research/2026-06-20_fr-braid-spin-statistics_result.md`. DERIVES the
   exchange = 2π-rotation identity (A4-only), a configuration-space *holonomy* argument — **PEER, not a
   chord**, and it carries **no action-level term**. The non-A4 control ALSO reaches −I (the sign is the
   generic π₁(SO(3))=ℤ₂ element, not forced by the (2,3) winding). 3-fold C3 (120°/encircle → −I after
   three steps) lives in the cover, reached by continuity, never a single finite rotation.

3. **The half-angle-lift import** — `research/_archive/L3_electron_soliton/06_winding_index_projection.md:36`
   (`U(r)=exp(iσ·ω/2)`) and `.../03_existence_proof.md:168` ("the spin-1/2 structure is derived from
   experimental observation") + `:174` (the Cosserat energy functional "does not select"). The fermion
   sign is imported; the energy functional is stated in-corpus NOT to select it.

4. **Claim leaves** — `clm-rkisb8` (`vol1/claim-quality.md:992`, solidity 0.72): "establishes the
   double-cover structure but only asserts (does not derive) the spin-½ realization … the dynamical
   selection remains the FM argument, not derived." `clm-salw2h` (`vol2/claim-quality.md:399`, solidity
   0.70): derives the double-cover *structure*; the spin-½ realization is "a disclosed import
   (ontological reinterpretation)", matches SM observables, no novel numerical prediction.

5. **★ Topological-action-term inventory (the load-bearing item):**
   - **Wess-Zumino / θ-term: ABSENT** — 0 hits, two grep methods, both AVE-Core and AVE-HOPF.
   - **Hopf / Chern-Simons: PRESENT but form-imported + coefficient-fitted, entering as ENERGY not a
     sign.** `cosserat_field_3d.py:319-334` `_hopf_density` (a real CS 3-form ½A·B integrating to the
     Hopf invariant); it appears in the energy functional `:708`
     `W = … + W_hopf·k_hopf` with `k_hopf = π/3` **fitted** by matching Q_H = pq = 6 (`:926-928`), from
     an L3 DRAFT doc (`13_hopf_self_inductance.md`) that *proposes* the term.
   - **Faddeev-Skyrme** (`faddeev_skyrme.py`): standard hedgehog Hamiltonian, imported form; an
     energy/mass functional, not a sign term.
   - **Berry/Chern scripts + charge_quantization**: holonomy/charge MEASUREMENTS explicitly disclaimed
     "NOT an energy functional / NOT a Lagrangian"; the direct CS helicity integral does not even
     quantize (~18% of p·q, sign-only).

6. **K4 constitutive action** — `cosserat_field_3d.py:_energy_density_bare:676-709`. The genuinely-derived
   terms (`W_cauchy`, `W_micropolar`, `W_kappa`; Eringen micropolar, K4-pinned moduli) are **quadratic,
   sign-blind energies** — they cannot carry a χ(τ) coupling. The topological terms (Op10/reflection/Hopf)
   are imported-form + fitted/pinned. **No derived χ(τ)↔texture coupling present or structurally staged.**

7. **AVE-HOPF status** — no derived Hopf term. The chiral-coupling *form* is constructive/fit (Path A,
   `open_questions.md:33`: "algebraically reproduces the form to 10⁻¹² but is constructive, not derived …
   the K4-TLM 'verification' is **tautological because α is hardcoded**"). The one rigorous route (Path B,
   the K4 path integral, `13_l3_chirality_review.tex:48`: "**The path integral was never executed**") is
   unexecuted. Live HOPF work is bench hardware, not a field-term derivation.

**HONEST INTERNAL PRIOR:** across AVE-Core and AVE-HOPF there is **no instance of a topological action
term derived from the framework's own constitutive action.** Every candidate is absent, form-imported +
coefficient-fitted (as energy, not sign), a disclaimed measurement, or an unexecuted derivation. The
specific object §5 requires has no corpus precedent to model on.

---

## SYNTHESIS — the honest prior, and the two footholds

**Both fronts converge:** the mainstream and AVE agree that π₁ admits-but-never-forces (so the internal
result is mainstream-confirmed, not out on a limb), and **the honest prior for the build is IMPORT** —
every known instance, in the literature and in the corpus, imports the fermion sign.

**AVE's route (b) is bricked by its own claim.** The mainstream's one "derived" route fixes the sign by
matching to a fermionic microscopic theory (Witten's N_c; induced Hopf). AVE claims the electron *is* the
soliton and the substrate *is* the bottom — there are no sub-electron fermions to integrate out. So AVE
has only: **(a) posit the sign** (the current `exp(iσ·ω/2)` import — honest, peer-with-SM), or **(c) a
route nobody has ever needed** — derive the sign from the K4 *discrete* constitutive action's own
structure.

**Two footholds keep route (c) from being flatly dead:**

1. **The raw material already exists in the action.** The K4 energy functional already carries a
   topological term of the right *kind* — the Hopf/CS density on the ω micro-rotation field
   (`cosserat_field_3d.py:319-334, :708`). What is missing is deriving its coefficient (not fitting
   π/3) and making it act on a SIGN, not a magnitude.

2. **★ The sign lives in the PHASE, and the corpus currently spends the term as ENERGY.** Per
   Witten/Wilczek-Zee, the fermion sign is the phase `e^{iθ·H}` a configuration accrues traversing the
   2π-rotation loop — a topological term in the *action*, typically imaginary in the path integral. The
   AVE corpus took the same CS 3-form and used its *magnitude* as a positive self-inductance ENERGY
   (`+ W_hopf·k_hopf`), which discards precisely the phase that would carry χ(τ). **The sign-carrying
   object exists structurally but is deployed in the wrong channel.** This is the concrete, physical
   handle for the build.

3. **K4 discreteness is the one feature the continuum σ-model lacks.** The external prior's whole reason
   the σ-model can't fix θ is that it is continuous and featureless. AVE's substrate is not featureless:
   it has a discrete K4 symmetry and a real odd-q texture obstruction. The *only* conceivable non-imported
   source of a quantization+matching condition on the CS coefficient is that discreteness.

---

## THE BUILD, IF WE SWING — and the anti-tautology gate it MUST pass

The build is **AVE-HOPF Path B under a hard anti-tautology gate**: promote the Hopf/CS term from a
self-inductance *energy* to a Berry-phase in the *action*, and test whether K4 discreteness FIXES its
coefficient so that the phase on the (2,3)-texture-coupled 2π-rotation loop is exactly −1 (χ(τ)=−1) —
**without importing α, the half-angle lift, or a fitted coefficient.**

**Gate (the same discipline that killed Path A and the n_TKI rescue):**
- **No α** anywhere on the derivation path (Path A died to a hardcoded α → tautology).
- **No half-angle lift** — `exp(iσ·ω/2)` is the import we are trying to eliminate; it must never touch the path.
- **No fitted coefficient** — `k_hopf` must come OUT of K4 discreteness, not be matched to Q_H=6.
- The sign must fall out of the discrete structure ALONE. If it smuggles any of the above → the honest
  read is that we reconstructed the import (echo), and we STOP and say so plainly.

**Honest prior on the outcome:** IMPORT is the overwhelming default (no precedent anywhere; one prior AVE
attempt at exactly this — Path B — was never executed, and its cousin Path A came out tautological). A
genuine derivation would be the first fermion-from-bosons selection in the game — a real chord — which is
exactly why it is worth one disciplined swing and exactly why the gate is non-negotiable.

**STATUS: PRE-BUILD.** Next step = walk the coupling mechanism with Grant in chat (what in the K4 action
physically fixes the phase sign, non-tautologically) BEFORE any dispatch. This doc records the terrain;
it does not authorize the build.
