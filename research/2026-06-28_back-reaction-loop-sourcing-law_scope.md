# Scoping / Prereg-class: Two-Way Gravitational Back-Reaction Loop (T_munu -> A(r) sourcing law)

**Status:** DESIGN/SCOPING pass. No file writes, no build. Verified at HEAD `21b7be95`.
**Verdict:** BUILDABLE-WITH-FIXES (Stages 1-2, the GR-replacement loop); BLOCKED (Stage 3, the DE read-out, pending a depletion primitive).

---

## 0. Substrate-native framing (FIRST)

The vacuum is a real, compressible, saturable LC medium on the z=4 diamond net. Gravity is not a metric handed to the engine; it is the **settled (or rung-down) dilatation strain field A(r) = eps11(r)** of that medium, sourced by the integrated field energy of matter/EM, with the Axiom-4 saturation kernel `S(A)=(1-A^2)^p` setting the per-cell stiffness `c_eff^2/c0^2 = 1/S(A)` -> per-cell L,C of the EM network. The Schwarzschild radius is a **read-out** of the field's own integrated energy, not an input.

This is mundane vacuum-engineering pumping, NOT exotic curvature. The crank-check throughout is the energy-momentum ledger.

**Sector discipline:** mass = A1 dilatation (PR#260). The source is the A1 grade, isolated from the Cosserat winding (charge) grade via the a1/omega energy split (`srs_cage_winding.py:494-505`). NEVER cross-wire A1-bulk with Cosserat-winding.

**Net choice (substrate-walk settles it, NOT a fork):** target the **z=4 diamond net**. The bulk strain A and S(A) already live there (TETRA_OFFSETS, `graded_vacuum_network.py`); Schwarzschild-radius emergence / lensing is a macroscopic chirality-blind observable that BOTH D1 adjudications route to diamond; building on srs would inherit the undischarged P1 alpha/Lorentz-survival dependency. **Leave `eq_axiom_1.tex` UNTOUCHED (flag-don't-fix).** One ratification to surface: ratify 'gravity/bulk back-reaction = diamond regime' independently of the open D1 .tex reconciliation, so this work is not held hostage to the carrier-unification fork.

---

## 1. The sourcing law (final, fixes folded in)

A **single nonlinear saturated elastic-Poisson equation**, static, on the native diamond divergence operator:

```
-div[ (c^4/7G) * (1/S(A(r))) * grad eps11(r) ] = T00(r)
```

| step | object | source |
|---|---|---|
| amplitude | `A(r) = eps11(r)/eps_yield`, `eps_yield = 1` (NOTE: `eps11(r_s)=3.5`, NOT in [0,1); rupture `eps11=1` at `r_sat=7GM/c^2=3.5 r_s` — A is the NORMALIZED strain) | — |
| kernel | `S(A)=(1-A^2)^p` clipped [S_min,1], p PENDING Fork 3 | `graded_vacuum_network.py:222` |
| operator | `adjoint_div(D-grad)`, `D=1/S(A)`, TETRA_OFFSETS | `graded_vacuum_network.py:255,248` |
| **source** | `T00 = (1/2 eps0|E|^2 + 1/2 mu0|H|^2)` + `(2/3)G(tr eps)^2` + kinetic, A1-grade isolated | `k4_tlm.py:530`, `cosserat_field_3d.py:701/:1789`, `srs_cage_winding.py:494-505` |
| medium | `c_eff^2/c0^2 = 1/S(A)` -> per-cell L,C | `graded_vacuum_network.py:248`; `master_equation_fdtd.py:66` |
| index | `n = 1 + (2/7)eps11` (Op19, UNCHANGED) | `universal_operators.py:1056` |
| radius | `M_eff c^2 = integral T00 dV`; `r_s := 2G*M_eff/c^2` READ OUT | emergent diagnostic |

### 1.1 Emergent-mass closure (the load-bearing repair)

M_eff emerges because T00 is a SPATIAL operator and the field self-energy is a GRADIENT/integral quantity:

```
M_eff c^2 = integral_V T00 dV = integral rho_matter c^2 dV - (1/c^2) integral u_bind dV
u_bind = (1/2)(c^4/7G)|grad eps11|^2   (SUBTRACTED — a well deficits its own ADM mass)
```

ADDING the self-energy double-counts and produces a non-contractive 2pi-4pi geometric artifact (the most valuable catch). For a STATIC single mass the nonlinear elliptic solve **IS** the fixed point — no outer T00-resource loop needed. The outer iteration is required only at O(1) compactness (BH) and for the DE read-out.

### 1.2 Three conditional fixes (from the pressure-test)

- **FIX-A (relabel):** strike 'replaces GR' and 'r_s never input' from any header. The build is 'two-way back-reaction making M_eff emergent'. The coefficient `c^4/7G` is forced only RELATIVE to the imported G (embeds back-solved `xi=hbar*c/(7 G m_e^2)`); the 'two 7s cancel' (`NU_VAC*7=2.0`, verified to 1e-18) is an INTERNAL-CONSISTENCY identity, NOT a forward determination of gravity's coupling. Docstring must NOT imply the loop derives its own '8pi-analog'.
- **FIX-B (validate-on-known):** the gate is NOT 'reproduce eps11=7GM/c^2r' (tautological — modulus calibrated to it). Demote to a necessary-but-not-sufficient floor; replace with the four at-risk checks (Stage 1).
- **FIX-C (boundedness):** discharge boundedness-below FROM FIRST PRINCIPLES. The self-energy source `+|grad eps11|^2` is sign-positive (self-reinforcing -> runaway-collapse hazard, OPPOSITE of the `crystal_graft_v4` detonation). Do NOT cite `cauchy-implosion-resolution.md` for contractivity — it proves linear-medium incompressibility (`ch03-macroscopic-relativity`, verified; the synthesis mis-pathed it to ch01), which is NOT Picard contractivity.

### 1.3 Honesty gates (no metric bought by damping)

(i) STATIC elliptic relaxation, not damped time-integration (no dt to clamp, no velocity reservoir to pump). (ii) `min S(A) > S_min` outside r_sat — if the clip binds, the CLAMP set r_s. (iii) M_eff INDEPENDENT of S_min over [1e-4,1e-2] — if it moves, FAIL. (iv) report empirical Picard contraction factor; must equal ~compactness, NOT ~1 held down by under-relaxation.

---

## 2. Derived-vs-imported ledger (ruthless)

**DERIVED (FORM forced):** Poisson form (canonical, `gordon-optical-metric.md:24`); native div(D-grad) (`graded_vacuum_network.py:255`); constitutive `sigma=K theta delta + 2G dev(eps)`, `nu_vac=2/7` (clm-x19btt); 1/7 projection (clm-wx5324); Op19 strain->index (clean); kernel S(A) (Axiom-4).

**IDENTIFICATION (the what, not the how):** `T00 = LC energy density` (clm-y9old1) — the per-cell densities exist but were never aggregated into one T00 observer.

**NEW PHYSICS (ZERO prior art):** the sourcing arrow T00->eps11; M_eff with binding-deficit subtraction; the fixed-point driver; emergent r_s.

**IMPORTED (honestly):** the modulus VALUE `c^4/7G` (embeds G, MIXED, back-solved xi; `optical-refraction-gravity.md:52,81`); the K=2G coupling (settled GR-IMPORTED 'end of line', PR#261 two-phase closed-negative — on the K=2G branch `rho=L_eff/C_eff=Z0^2 for ALL S`, so saturation CANNOT select the 2:1; verified verbatim); eps11=7GM/c^2r magnitude (back-inversion; deriving from primitives logged OPEN at `vol3/claim-quality.md:65`).

**Symmetric-standard (do NOT AVE-comedown):** GR ALSO imports its source (T_munu hand-specified, G measured) and does NOT derive r_s from self-energy in the test-mass limit. 'Imports a coefficient' is NOT an AVE-specific deficiency. The AVE-distinct prize is narrowly: emergent M_eff, strong-field channel-split interior, matter<->DE coupling. Do NOT claim the loop derives gravity's coupling from substrate.

---

## 3. Forks for Grant (physical-intuition calls)

1. **Statics vs dynamics** — settled mattress (statics, elliptic, no velocity reservoir to pump) vs rung-down string (dynamics, dt-clamp + pump hazards). *Lean: HYBRID — statics for Stages 1-2, dynamics only for the inherently history-dependent Stage 3.*
2. **S vs 1/S vs 1/S^2 exponent** — code is `c_eff^2=c0^2/S` (1/S, verified `master_equation_fdtd.py:66`); GOAL's L,C~S under SYM co-scaling (Z=Z0 invariant) forces 1/S^2. One is mis-stated. *Lean: trust the code (1/S), re-derive whether only one channel saturates. Substrate-direction call for Grant, not an implementer guess.*
3. **Which A + pin p** — three amplitude defs; DEC-1 p=0.5/0.25 still flagged. *Lean: A=eps11/eps_yield (eps_yield=1), p=0.5 primary.*
4. **Three-way n(r) divergence** (2.0/1.5/1.627 at 2r_s) — fixed point yields ONE n. *Lean: LINEAR weak-field canonical; repoint three consumers + ALL THREE schwarzschild_radius defs (incl. `orbital_resonance.py:125`, a third the digest missed). Strong-field departure = PREDICTION.*
5. **Contractivity at O(1) compactness** — provable weak-field, untested BH. *Lean: restrict Stage-1 to weak/moderate field; BH separate gated stage; any under-relaxation REPORTED.*
6. **The depletion primitive (DE make-or-break)** — fuse (irreversible lock-out, the ONLY route to the DE chord) vs spring (reversible, DE = null). *Lean: a leaky-fuse route exists (latent-heat-of-crystallization), but the depletion operator must be DERIVED first; Stage 3 gated on it. Plumber-physical: does locking matter into a strain well permanently blow a fuse, or hold a spring that returns?*

---

## 4. Staged build plan

- **Stage 0 (prereqs):** rule Forks 1-4; ratify diamond-regime; assemble single T00(r) observer. **Gate:** all forks ruled (no implementer guesses) + T00 integration conserves a known blob's energy to machine precision.
- **Stage 1 (static single-mass closure + non-trivial validate):** wire T00->source(eps11) into div(D-grad); read M_eff with binding-deficit subtraction; repoint all three r_s defs. **Gate (ALL FOUR at-risk checks; tautological floor DEMOTED):** (1) extended non-delta source -> 1/r exterior; (2) emergent r_s S_min-INDEPENDENT over [1e-4,1e-2]; (3) deflection 4GM/bc^2 as a RAY-TRACED OUTPUT (NOT the hard-coded `gravity/__init__.py:185` return — verified asserted, no Snell integral exists), reporting which n(r) packaging; (4) two-mass superposition proves the nonlinearity is engaged.
- **Stage 2 (energy-honesty gate):** prove boundedness from first principles (NOT from cauchy-implosion). **Gate:** boundedness proven not asserted; `min S(A)>S_min` outside r_sat; Picard factor ~compactness not ~1; STATIC relaxation used.
- **Stage 3 (DE read-out, BLOCKED):** GATED on Fork 6 — derive an irreversible depletion operator FIRST. **Gate:** BLOCKED until Fork 6 ruled; if 'spring', DEAD + retract convergence claim; if depletion derived, PASS = DE inhomogeneity tracks matter AND is SM/LambdaCDM-distinct (ave-discrimination-check).

---

## 5. DE-chord read-out path

PATH: `T00^matter -> source(A(r)) -> S(A) locks reactive energy into the well -> free reactive store depleted where matter is dense -> rho_Lambda(r) tracks -rho_matter(r) -> coincidence problem resolved`.

BROKEN LINK (Lens 5 FAIL, verified decisive): the kernel `S(A)=(1-A^2)^p` is a pure REVERSIBLE pointwise state-function (ZERO hysteresis/history/memory/irreversible/deplete hits across both kernel homes, grep-confirmed). 'Captured reactive energy depletes a free remainder' corresponds to NO TERM in the law. Independently bracketed twice: bemf-smoke ('the missing primitive is depletion, not reaction', verified verbatim) and cosmic-epsilon (`mechanism.md:87`, microscopic-energy->rho_Lambda closed-negative).

VERDICT: the 'same build does GR AND DE, doubly matters' framing is a seductive-narrative conflation of TWO DISTINCT builds. Stages 1-2 are a closure win (emergent M_eff) whose ONLY guaranteed output is GR reproduction — that is a closure win, NOT a chord. The DE chord is a separate, genuinely-new, currently-unbuilt route that the loop ENABLES but does not CONTAIN. Do not promise the chord from Stages 1-2.

---

## 6. Prior-art honesty

The elastic field equation ALREADY exists in one-way form (`gordon-optical-metric.md:24`, hand-placed `Mc^2 delta^3(r)` source). This build is precisely: (i) replace the delta-source with integrated T00; (ii) make the modulus come from the per-cell S(A) rather than the back-solved xi; (iii) iterate to a fixed point so M_eff emerges. The closed fixed-point loop has NEVER been attempted (grep-confirmed). Two WALLS, honestly: the K=2G coupling is settled GR-imported (the loop cannot derive its own '8pi-analog'); the DE chord has zero prior art AND zero closed magnitude pieces (rho_latent, Gamma_cryst open since 2026-05).

---

## 7. Honest derived-vs-imported summary (one line)

The loop is **self-consistent in FORM while importing its coupling VALUE** — the framework-wide FORM-derives/VALUE-imports pattern. K=2G is the homogeneous LHS (the metric/Einstein-tensor analog), NOT the source coupling. The sourcing arrow T00->eps11 is genuinely new physics; its strength is set by the imported modulus. The AVE-distinct prize is emergent M_eff + the strong-field departure + the (still-unbuilt) matter<->DE coupling — not deriving gravity's coupling from nothing.