# EM-sector saturation keying functional S_E[·], S_B[·] — derivation PRE-REGISTRATION [FROZEN]

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/em-saturation-keying-functional`
**Class:** DERIVATION of a constitutive functional the substrate adjudicates (derive-or-kill).
No claim minted until the derivation + the six frozen constraint evaluations complete.
**Gates on (verify-before-cite, all grepped at this HEAD `887b44f8`):**
- Fork memo FROZEN `research/2026-07-05_electrostatic-sector-fork-memo_FROZEN.md` (Grant-ratified 2026-07-05):
  [C-EXCLUDED] excludes the continuum static-E kernel `ε_eff=ε₀√(1−(E/E_c)²)` as a *universal* claim to
  atomic scales; explicitly preserves as SEPARATE surviving sectors (§3 [C] ledger) the AC pump-probe
  ε-varactor birefringence and the µ-sector circulation keying.
- Problem-3 RESULT `research/2026-07-05_problem3-muonic-lamb_RESULT.md`: the amplitude key `A²=(E/E_c)²`
  run on the static muonic-H Coulomb field is [C-EXCLUDED] — overshoots the 2.3 µeV CREMA window by
  ~2×10⁴× even scoped to `ℓ_node`; the protective hard cutoff would need `r_cut≈9·ℓ_node≈3.5 pm`.
  Machinery to REUSE (import, not reimplement): `src/scripts/verify/problem3_muonic_lamb_shift.py`
  (`rho_2s`, `rho_2p`, `_norm`, `A_MU`, `shift_pathB`, the level-shift bracket integral).
- Route C (B-sector, MERGED): `manuscript/.../node-up-small-large-signal.md`:§1/§4;
  `.../relativistic-inductor.md`:15,18; `.../pvlas-static-b-verdict.md` (clm-pvlas1);
  `research/2026-06-22_vca-r01-mu-keying-derivation.md`; `research/2026-06-25_vca-mu-circulation-observable-derivation.md`.
- The Letter `papers/2026_birefringence_letter/main.tex` (v2).

---

## 0. SECTOR HEADER (mandatory, per feedback_substrate_native_first_sector_header)

- **Which sector?** The EM channel: the vacuum LC tank's ε-grade (VARACTOR, transverse-T2 permittivity)
  and µ-grade (relativistic INDUCTOR, Cosserat-B microrotation). This is the ε/µ EM sector.
- **This is NOT the mechanical Q-point sector.** The bond-strain / transverse-tangent-stiffness / ρ_eff
  Q-point canon (pump-probe-tslot `research/2026-07-05_pump-probe-tslot_result.md`; matter-stiffening
  #518; channel-resolved-loading `research/2026-07-05_channel-resolved-loading_result.md`) is a DIFFERENT
  sector (translational-elastic bond springs). It supplies a SUBSTRATE PRECEDENT that a traveling wave
  deposits a rectified 2nd-order mean a held field does not (⟨A_bond⟩>0 while ⟨y⟩=0) — but it is cited
  as cross-sector precedent for the MECHANISM CLASS only; NO number crosses the EM/mechanical seam.
- **Cold vs saturated?** Deep-cold vacuum (the pump-probe regime: `A²~6e-7`, far below the yield knee;
  the muon static field `A²~0.025`). Small-signal probe about a large-signal operating point set by the
  drive. The DOF the engine carries: the FDTD ε/µ reactances (`fdtd_3d.py`), the Axiom-4 kernel
  `S(A)=√(1−A²)` (`scale_invariant.py`), the node clock `ω_C=c/ℓ_node` (`constants.py:OMEGA_C`).
- **Homonym guard.** "A²" is overloaded: (i) the Axiom-4 kernel argument (a phase-space reactance
  coordinate, A46), (ii) the Letter's `(E/E_c)²` field-amplitude ratio, (iii) the mechanical bond
  strain. This prereg's derived key is a THIRD, transport-class invariant; it is named `𝒯` (transport
  content) throughout to avoid collision, and its relation to each "A²" is stated explicitly.

## 0.1 PRE-TEST PHYSICS CHECK — the plumber question surfaced to Grant (recorded, not blocking the freeze)

Fired `pre-test-physics-check` (trigger 1 pre-reg freeze; trigger 8 dispatch-ontology; trigger 9
fork-to-computable). Grant's frozen candidate already front-loads the ontology (transport-not-stock),
so the physics-check is satisfied by Grant's fire order for the top-level noun. The residual OPEN fork
the candidate itself flags ("if the derivation lands on a DIFFERENT surviving invariant, follow the
substrate") is converted to a COMPUTABLE DISCRIMINATOR (per trigger 9), not pressed for fiat:

> **Plumber question (surfaced, recorded):** In the node's own rotating clock frame, the thing that
> survives cycle-averaging and distinguishes a wave from a held field at second order — is it the
> POYNTING TRANSPORT (E×H, energy in flight, first-order-in-both-fields, a genuine flux with a
> direction), or is it the FIELD-PAIR BEAT (the co-moving product E·(∂E/∂t) / the temporal-gradient
> content that a static field also lacks)? Both vanish for a static Coulomb field (H=0 ⟹ no Poynting;
> ∂_tE=0 ⟹ no beat). Both are nonzero for the propagating pump. They differ for a STANDING wave
> (Poynting time-averages to zero in a pure standing wave; the beat/∂_t content does not) and for a
> quasi-static-but-slowly-varying lab field. Which one does the node's constitutive response actually
> integrate? — This is left for the substrate to force (the secular-averaging computation, §A), with
> both candidates carried as frozen sub-bins T-POYNT / T-BEAT; NOT resolved by fiat.

The freeze protects the derivation regardless of Grant's answer; if Grant collapses the fork in one
sentence it is recorded as an errata banner and the matching sub-bin is the routed one. Absent a Grant
answer, the substrate (§A secular-averaging + §B invariant survival) adjudicates.

---

## 1. GRANT'S FROZEN CANDIDATE SHAPE (recorded verbatim; derive-or-kill, never assumed)

Recorded verbatim from the 2026-07-05 fire order. This is the CANDIDATE the derivation tests; it is
NOT assumed true. Two pieces:

**(a) DC-BLINDNESS BY NODE-CLOCK ALIASING.** *"every cell runs at its own clock ω_c (ℏω_c = m_ec²).
In the node's rotating (Park) frame, lab-STATIC field content appears as a signal at ω_c itself —
unresolvable, non-secular, averages to zero engagement. DC-blindness forced by the substrate's own
clock (the RWA/secular-averaging mechanism), not assigned. The preferred frame (lattice rest + node
clock) supplies Park's reference — state this as the frame's honest work."*

**(b) THE SURVIVING SECOND-ORDER KEY = TRANSPORT.** *"naive clock-frame averaging also blinds the
optical pump (10¹⁵ vs 10²⁰ — both non-secular), so the key that survives averaging must distinguish a
WAVE from a HELD field at second order. ⟨E²⟩ cannot (both constant). The candidate discriminator:
TRANSPORT content — Poynting flux, energy in flight — vs held stock (static Coulomb: zero flux).
Saturation keys on transported field content. Muon: stock, blind. Pump: flight, engaged."*

**Frame declaration (Grant, honest work of the frame):** the preferred frame is lattice-rest + node
clock ω_C. Park/dq0 (the rotating-frame transform to the ω_C reference) and the RWA (drop terms
oscillating at ±2ω_C after the transform, keep secular) are the EE/physics-native formalisms; they are
the PRIMARY language of this derivation.

## 1.1 THE LOAD-BEARING CONTRADICTION THIS DERIVATION MUST ADJUDICATE (flag-don't-fix)

The corpus R2 "static-E route" currently asserts (VERBATIM, verify-before-cite):

> `node-up-small-large-signal.md:217-218`: *"A static E is a real operating-point bias for the V-keyed
> varactor — it loads ε and shifts n."* Keyed on `A_V=|E|/V_yield` (potential amplitude).
> `pvlas-static-b-verdict.md:128`: *"A static (or DC-biased) electric field E does load the V-keyed
> varactor (ε-grade, regime R2), giving a measurable birefringence."*

This is the SAME amplitude key `A²=(E/E_c)²` that Problem-3 ran on the static muonic-H Coulomb field
and routed **[C-EXCLUDED]** (overshoots CREMA by ~2×10⁴×). So the corpus R2 "static E loads ε on
|E|-amplitude" is **falsified at atomic scales by muonic-H** if taken universally. Grant's candidate
resolves the contradiction by making the E-side ALSO transport-keyed (DC-blind like the B-side), so a
held Coulomb field is BLIND and only transported field content engages. **This prereg does NOT silently
pick a side.** It derives the keying functional from the substrate and lets the result adjudicate:
- If the derived S_E is transport-keyed AND clears muonic-H AND still fires on the pump → the corpus R2
  "static E loads on |E|" statement is SUPERSEDED (surfaced to Grant + auditor lane; the KB leaf is the
  auditor's to land).
- If the derived S_E cannot be made transport-keyed from the substrate → [NOT-DERIVABLE], and the
  contradiction stands as an open exposure (the keying enters only as an assigned postulate; ledger it).

## 2. WHAT IS DERIVED (both pieces, from the substrate — the K4-LC network, the Axiom-4 kernel, node modes)

**(a) Secular-averaging result (§A driver).** In the node's rotating frame at ω_C (Park transform),
compute what a node's Axiom-4 constitutive response integrates over one clock cycle for three drive
classes: (i) lab-static field content (ω=0), (ii) resonant (ω≈ω_C), (iii) optical/probe band
(ω≪ω_C: pump ω/ω_C=3.03e-6, probe ω/ω_C=0.0196 — computed live, §constants). Derive which contributions
are SECULAR (survive averaging) vs NON-SECULAR (average to zero). Grant's claim (a): static content
aliases to ω_C, non-secular, blind. Grant's claim (b): naive averaging ALSO blinds the pump. DERIVE
both, or report where the substrate differs.

**(b) Surviving second-order invariant → S_E[·].** Derive WHICH second-order field invariant survives
the secular average and feeds S. Candidates carried (frozen sub-bins):
- **T-POYNT:** the transport content is the Poynting flux `𝒯 = |⟨E×H⟩|` (energy in flight). Static
  Coulomb: H=0 ⟹ 𝒯=0 ⟹ blind. Pump: 𝒯=I/c ≠ 0 ⟹ engaged.
- **T-BEAT:** the surviving invariant is the co-moving temporal-gradient content
  `𝒯 = ⟨(∂_tE)²⟩/ω_C²` (or the mixed `⟨E·∂_tE⟩`-class). Static: ∂_tE=0 ⟹ blind. Pump: ∂_tE=ωE ⟹ engaged.
- **T-CIRC (the E-dual of Route C):** the surviving invariant is the E-side circulation
  `𝒯 = |∮E·dℓ|²`-class (the dual of the B-side `∮H·dℓ`). Static curl-free Coulomb: ∮E·dℓ=0 ⟹ blind.
If the substrate forces a DIFFERENT invariant, follow it and name it (a new sub-bin). Derive the
COEFFICIENT (from the K4 dispersion / node mode structure, not fitted) and assemble the effective
functional **S_E[𝒯] = √(1 − c·𝒯)** (form to be derived; c the derived coefficient).

**Every step sympy-verified.** Independent code paths for numerics (derive-then-confirm, ReconcileGate,
derived tolerances). No self-verifying control.

## 3. THE DUAL: S_B EXPLICIT (Keith Phase-1b demand)

Write S_B as an explicit functional consuming the MERGED Route-C work: the µ-grade is the relativistic
inductor `L_eff(I)=L_0/√(1−A_I²)`, `A_I=I_cell/I_max=|∮H·dℓ|·(ℓ_node-normalization)/I_max`,
`I_max=ξ_topo·c=124.384 A` (`constants.py`). Static B → curl H=0 → I_cell=0 → A_I=0 → S_μ=1 (transparent,
[C]-preserved, clm-pvlas1). Write S_B[B,∂_tB,∇×B] = √(1−(|∮H·dℓ|_normalized/I_max)²). Demonstrate the
E and B functionals are DUALS under the same transport/secular structure (E-circulation ∮E·dℓ ↔
B-circulation ∮H·dℓ; Poynting is the shared transport current), OR report the duality's failure.
**Blocker-B lesson carried (VCA-R01):** the transport invariant must be an ENVELOPE / cycle-averaged
quantity (∮·dℓ, bounded finite oriented sum), NOT a pointwise ratio (`|∂_tB|/|B|=ω|tan ωt|` diverges at
zero-crossings). The derived S_E must inherit this — 𝒯 must be bounded for a propagating wave.

## 4. FROZEN CONSTRAINT FALSIFIERS (knife armed on ALL; NO parameter chosen to satisfy them)

The derived functional (with its DERIVED coefficient, not tuned) is EVALUATED against each. Bands.

1. **MUONIC-H.** Evaluate derived S_E on the static muonic-H Coulomb field via the reused #539
   bracket-integral machinery. `𝒯=0` for a held Coulomb field (H=0, ∂_tE=0, curl E=0 — all three
   candidates vanish) ⟹ prediction `δ[ΔE]=0` exactly, `⟪ under 2.3 µeV CREMA window`. If the derived 𝒯
   is NONZERO for the static field → evaluate the shift and route (this is the [C]-repeat risk).
2. **THE PUMP.** Evaluate derived S_E at the Letter's pump (optical, 1e21 W/cm², E=8.68e13 V/m,
   BIREF@HIBEF geometry). Report the derived coefficient vs the Letter's `−½A²` for δn_bir. If it
   RESCALES Table I, quantify the energy-dependence across the three probe energies (8766/9835/12914 eV)
   honestly (the `(qℓ_node)²`-class structure Keith predicts).
3. **PVLAS.** Evaluate derived S_B (rotating 2.5 T at Hz-scale). Must sit below the PVLAS bound
   (δn≲ QED-level, `Ejlli2020`) or the sector is bound. Report either way.
4. **BMV.** ms pulses, large ∂B/∂t. Same.
5. **DELLIGHT.** Derived S_E (common-mode δn_iso≈−¼A²-class) at their Sagnac sensitivity
   (`Robertson2021DeLLight`).
6. **BOOST.** Static E ↔ static B map under boosts as zero-sequence (both blind — consistent);
   transport ↔ transport (both keyed). Preferred frame = lattice-rest + node clock, declared plainly.
   The Letter's own soft spot (`main.tex:305-307`: "S depends on |E|², not a Lorentz invariant, stated
   in the lab frame") is the target: a transport-keyed 𝒯 (E×H is a genuine tensor flux) closes the boost
   structurally, not by numerical smallness. Show the zero-sequence (Park d/q/0) mapping.

## 5. BINS (FROZEN verbatim; routed with no post-hoc criterion drops, Rule 11)

- **[FUNCTIONAL-DERIVED]** — both pieces (a secular-averaging + b surviving invariant → S_E, and the
  S_B dual) derive from the substrate; all six constraints pass (bands stated); the Table-I consequence
  quantified (unchanged, or the derived rescaling stated); duality demonstrated; boost closed.
- **[PARTIAL]** — one piece derives, the other underdetermined; name PRECISELY what the substrate does
  not supply (e.g. the coefficient c is forced but the invariant class is not, or vice versa).
- **[CONSTRAINT-KILLED]** — the derived functional (as derived, no dial-turning) violates a constraint
  ⟹ the radiative rescue of the birefringence sector fails as derived. Honest negative; name the single
  mechanism; close the branch (Rule 11). Do NOT refill the slot (Rule 12 — new hypothesis = new version).
- **[NOT-DERIVABLE]** — the keying cannot be forced from the substrate; it enters only as an assigned
  postulate. Ledger the cost explicitly: the new postulate + its parameter floor.

**Knife (armed):** ½/¼ derived-only (the Letter's −½/−¼ are DERIVED coefficients, not tells — but any
NEW ½/¼ that appears in MY coefficient c must be sympy-traced, not asserted); ω_C/9-class thresholds
(the 9·ℓ_node muonic floor is a computed defeat-scale, not to be reproduced coincidentally); 2/7,
9.7734 (mechanical-sector numbers — must NOT appear in the EM coefficient; if they do it is a
cross-wire flag). Any constraint satisfied SUSPICIOUSLY EXACTLY (e.g. `δ[ΔE]=0` to machine precision) is
CHECKED for structural degeneracy (is 𝒯=0 forced by bookkeeping for ANY field, or genuinely because a
held Coulomb field has no transport? — the null-verdict-liveness check, trigger 10: run a POSITIVE
CONTROL, the pump field, through the IDENTICAL S_E→δ[ΔE] pipeline and show it goes nonzero).

## 6. DISCIPLINE STACK (this is the highest-stakes derivation of the program)

Prereg FROZEN before results (this doc; Grant's candidate + fire order verbatim §1); skeleton-first
then one section per commit; sympy on every analytical step; independent code paths for numerics
(derive-then-confirm, ReconcileGate with a LIVE positive control, derived tolerances); no self-verifying
controls; consume merged machinery by import (#539 evaluator, Route C constants, the Axiom-4 kernel);
magnitudes as bands; quote-audit; homonym guard (§0 "A²"); sector headers (§0 — EM channel, NOT the
mechanical Q-point); pure-corpus (no external-context language); `make verify` green; tests split (fast
core + engine_sim); PR titled with the routed bin, `[REVIEW: pending-orchestrator]`, NO SELF-MERGE.
NOTE: Keith's sealed adversarial review may arrive mid-run — do NOT incorporate anything mid-derivation;
the freeze protects the derivation; reconciliation happens at review.

## 7. FROZEN CONSTANTS (verify-before-cite, live @ HEAD 887b44f8)

- `ω_C = c/ℓ_node = 7.76344071105011e20 rad/s`; `ℏω_C = m_ec² = 8.187105776823886e-14 J` (ratio 1.0 exact).
- `ℓ_node = 3.8615926772e-13 m`; `E_c = E_YIELD = √α·E_crit = 1.1304105713e17 V/m`.
- `I_max = ξ_topo·c = 124.3840330669 A`; `ξ_topo = e/ℓ_node = 4.1490047447e-7 C/m`.
- `ω_pump(1.55 eV)/ω_C = 3.0332743e-6`; `ω_probe(10 keV)/ω_C = 0.0195695`.
- Muon: `m_µ/m_e = 206.7682830` (CODATA 2018, EXTERNAL); `a_µ = 284.75 fm` (reduced-mass, #539).
- CREMA window: `202.3706(23) meV`; 1σ = 2.3 µeV (primary), 10 µeV (loose).

---
**FROZEN.** Any change below this line after the first result commit is an ERRATA BANNER ONLY (the body
is a record). The freeze act is this commit; the derivation fires on it.
