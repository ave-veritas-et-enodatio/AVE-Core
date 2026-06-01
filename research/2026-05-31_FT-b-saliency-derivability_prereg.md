# Prereg — FT-b: is the (2,3)-trefoil saliency δ = −3α/2 DERIVABLE from substrate dynamics, or a 1-point fit?

**Date**: 2026-05-31
**Branch**: `analysis/b-trefoil-saliency-derivability` (off `main` @ a743d84d, isolated worktree `AVE-Core-saliency-wt`)
**Status**: PREREG FROZEN — corpus inventory complete; derivation NOT executed (this commit freezes the prereg; the attempt + result land in a later commit on this branch).

**Skills fired**: `ave-prereg` (this prereg + corpus inventory); `ave-canonical-leaf-pull` (Q-G47 + saliency + Virial leaves enumerated below); `substrate-native-check` (K4 + Cosserat checkpoint, §6); `ave-fundamental-ground-up-implementation` (derive from substrate primitives, do NOT engineering-default or plug geometric ratios — §6 names the known-wrong route explicitly); `consistency-vs-emergence` (classify a successful derivation, §7); `ave-evidence-framing-discipline` (Outcome C is a fully valid result; do NOT force a positive).

---

## §1 — Target (precise)

The g-2 50-ppm closure (`q-g19a-petermann-saliency-closure.md`) rests on the saliency

$$\delta = -\frac{\alpha\, n_q}{2} = -\frac{3\alpha}{2}, \qquad n_q = 3 = \text{q-axis poloidal winding of the }(2,3)\text{ trefoil.}$$

Per doc 115 (`research/_archive/L3_electron_soliton/115_q_g19alpha_saliency_first_principles_derivation.md`), the three-factor chain decomposes as:

| Factor | Source | Status (per doc 115) |
|---|---|---|
| **α** | Ax-4 saturation-kernel expansion $S(A)\approx 1-A^2/2\approx 1-\pi\alpha$ at $A^2\approx 2\pi\alpha$ | DERIVED ✓ (rigorous, corpus-canonical, doc 115 §3) |
| **1/2** | Vol 4 Ch 1:175-184 LC-equipartition Virial sum | DERIVED ✓ (rigorous, corpus-canonical, doc 115 §4) |
| **n_q-LINEAR additivity** | each of $n_q$ windings contributes ONE independent α-order kernel-shift unit; δ scales LINEARLY in $n_q$ | **UN-DERIVED** "single remaining intuitive step" (doc 115 §6) |

**The question (and ONLY the question):** can the **n_q-LINEAR additivity** be DERIVED from the K4-Cosserat Lagrangian (the same unit-cell integration as Q-G47 Sessions 19+ ξ_K1/ξ_K2, per doc 115 §9) — **WITHOUT assuming it** — and **independent of the g-2 target value**?

α and 1/2 are NOT re-litigated here; they are taken as corpus-derived. The entire load is on whether linearity-in-$n_q$ falls out of substrate dynamics or must be postulated.

## §2 — Physical picture (mechanical, pre-derivation)

- The electron is the $0_1$ unknot in real space, carrying a phase-space $(2,q)$ Clifford-torus winding in the bond-pair LC tank's $(V_{\text{inc}}, V_{\text{ref}})$ phasor space (doc 79 §1-§2). Two axes: d-axis (toroidal, $n_d=2$, substrate-universal bipartite-K4) and q-axis (poloidal, $n_q=q$, particle-locked half-twist count).
- The saliency δ is the **small α-order asymmetry** in the peak strain amplitudes between these two axes: $A_{d,\text{peak}}^2 = (1+\delta)\cdot 2\pi\alpha$, $A_{q,\text{peak}}^2 = (1-\delta)\cdot 2\pi\alpha$, total budget $4\pi\alpha$ preserved (Schwinger).
- Plumber framing: the d-axis is the "substrate's own bipartite oscillation" (the lattice doesn't know which particle is in it); the q-axis carries the particle-specific twist count. The kernel feedback (Ax-4 back-reaction) "loads" the q-axis differently from the d-axis. **The open question is whether $n_q$ identical twists each pull on the kernel feedback independently (→ δ ∝ $n_q$, linear), or collectively (→ δ ∝ $\sqrt{n_q}$), or with interference (→ δ ∝ $n_q^2$).**
- The bisection (verified §3) locks δ* = −0.01093 = −1.498·α, matching the LINEAR law (−3α/2 = −1.5α) to 0.12%. √n_q gives −0.65% (64% off); n_q² gives −3.3% (200% off). So linearity is the *fitted* winner; the question is whether it is the *derived* winner.

## §3 — Corpus state + numerical verification (this session)

**Bisection re-verified this session** (`AVE-QED/scripts/g2_research/q_g19_alpha_saliency_sweep.py`, ran 2026-05-31):
```
δ* = -0.010933,  C_2(δ*) = -0.328479 (= PDG target),  δ*/α = -1.498
δ*/(−3α/2) = 0.9988  → 0.12% structural agreement with the LINEAR law
candidate δ scan: √α-order +35.3% off; α-order +6.7% off; α/π +4.9% off;
                  geometric Beltrami 1/(2π) (δ≈−0.84) → +303% off; Cosserat-PCA δ≈+0.111 → +44.7% off
```
The geometric candidates (Beltrami 1/(2π), Cosserat-PCA, winding-fraction) ALL miss by 10-300× — confirming doc 115 §3's claim that those are the WRONG mechanism (O(1) geometric anisotropy, not α-order kernel-feedback).

**The named closure machinery (doc 115 §9): Q-G47 Sessions 19+ unit-cell Lagrangian integration.** Re-verified this session by reading the actual derivation script `src/scripts/verify/q_g47_sessions_19_xi_K_derivation.py` + result `research/2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md`:
- That machinery computes **static linear-elastic moduli** at the K=2G operating point: $K_0 = 4k_a+8k_s = 16/7$, $G_0 = 8k_s = 8/7$, $\xi_{K1}=(\mu+\kappa)/T_{EM} = 8/3$, $\xi_{K2}=12\,\xi_{K1}=32$ (clean rationals, topology-locked).
- It is a **constitutive-tensor** calculation (Eringen micropolar moduli via Lamé identities + χ_K=12 path-count). The saturation kernel enters only via the *operating point* ($S(A^*)=0$ at K=2G), **NOT Taylor-expanded to α-order for per-mode back-reaction.**
- It contains **no (2,q) torus-knot phase-space decomposition, no per-winding term, and no bilateral d/q split.** It is the substrate-scale static-elasticity layer; the saliency is a particle-scale α-order phase-space kernel-feedback quantity. **Whether these two layers connect is exactly what the derivation attempt must establish.**

**Enumerated canonical/research inputs (ave-canonical-leaf-pull):**
| Ingredient | Location | Role |
|---|---|---|
| 3-factor chain + n_q-additivity open step | doc 115 §5, §6, §9 | the claim under test |
| substrate-universal-d vs particle-locked-q | doc 79 §4, §5 (Layer 2 χ=α·pq/(p+q)) | structural motivation for "n_q not n_d" |
| Beltrami/FOC d-q, 1/(2π) pitch | doc 85 §5.2 | the KNOWN-WRONG geometric route (§6 guard) |
| canonical saliency δ statement | `q-g19a-petermann-saliency-closure.md:82,110` | "single remaining intuitive step" verbatim |
| K4 unit-cell Cosserat-Lagrangian framework | `q-g47-substrate-scale-cosserat-closure.md` §"Substrate-scale prefactors" | the named closure machinery |
| ξ_K derivation (what the machinery actually computes) | `q_g47_sessions_19_xi_K_derivation.py`; result-v2.md | re-verified: static moduli, not α-order |
| Virial 1/2 equipartition | Vol 4 Ch 1:175-184 (via doc 79 §3.5) | the derived 1/2 factor |
| δ* bisection + candidate sweep | `q_g19_alpha_saliency_sweep.py` | re-verified δ*=−0.01093 |
| Layer-2 parallel-impedance χ = α·pq/(p+q) | doc 79 §5; doc 20 | the OTHER substrate winding-composition law on record (note: NOT linear-in-q; see §6) |

## §4 — The derivation attempt (what §2 of the result doc will execute)

Attempt, in order of decreasing rigor-likelihood, WITHOUT assuming linearity:

1. **Kernel back-reaction per phase-space winding (the core attempt).** Set up the Ax-4 kernel $S(A)=\sqrt{1-A^2}$ acting on the $(2,q)$ phase-space currents $I_d=\cos(2\omega_C t)$, $I_q=\sin(q\,\omega_C t)$ (the canonical Route-B trefoil currents). Expand $S$ to α-order. Ask: does the q-axis kernel-shift $\Delta A_q^2$ scale as $n_q$, $\sqrt{n_q}$, or $n_q^2$ as a STRUCTURAL consequence of how $q$ enters $I_q=\sin(q\omega_C t)$ — with the total budget $A_d^2+A_q^2=4\pi\alpha$ fixed? This is a closed analytical/numerical computation; run it for q ∈ {1,3,5,7} and read off the power law.
2. **Independent-vs-coupled twist criterion.** doc 115 §6 asserts cross-twist coupling is $O(\alpha^2)$ (sub-leading), so at leading α-order the windings add linearly. Test this: does the leading-α-order kernel feedback factorize over the $q$ crossings, or do the $\sin(q\omega_C t)$ harmonics produce cross-terms at α-order? If the cross-terms vanish by parity/orthogonality → linear is derived. If they survive → not linear.
3. **Map onto Q-G47 unit-cell integration (the named §9 route).** Determine whether the static ξ_K1/ξ_K2 machinery can be extended to carry an α-order kernel-feedback term that resolves per-winding. Characterize precisely the missing step (what Lagrangian term, at what order, with what (2,q) phase-space coupling).
4. **Cross-check against the OTHER substrate composition law.** doc 79 §5 / doc 20 give χ = α·pq/(p+q) for the chirality coupling — a DIFFERENT (non-linear, p-q-symmetric) winding-composition law that IS derived. If two different substrate winding-compositions exist (one linear for saliency, one pq/(p+q) for chirality), the derivation must say WHY the saliency takes the linear one and not the pq/(p+q) one. A derivation that can't distinguish them is incomplete.

The attempt is bounded: if step 1's analytical/numerical kernel computation does not produce linearity without an inserted independence assumption, AND step 3 confirms the Q-G47 machinery structurally lacks the α-order term, that is Outcome C — recorded honestly, not rescued.

## §5 — Prereg block (FROZEN)

```
PREREG (target: derive n_q-LINEAR α-order saliency δ=−3α/2 from K4-Cosserat substrate,
        WITHOUT assuming additivity, INDEPENDENT of the g-2 target value):

  Corpus state: n_q-additivity is the explicitly-OPEN "single remaining intuitive step"
                (doc 115 §6; q-g19a-petermann-saliency-closure.md:110 verbatim).
                α ✓ and 1/2 ✓ are corpus-derived; only linearity-in-n_q is at issue.
                The named closure machinery (Q-G47 Sessions 19+) re-verified this session to
                compute STATIC linear-elastic moduli (ξ_K1=8/3, ξ_K2=32), NOT α-order
                per-winding kernel-feedback.

  Prediction: UNCERTAIN BY DESIGN. Pre-registered prior (honest):
    P(A) ~ 25%  — kernel back-reaction on (2,q) phase-space currents yields δ ∝ n_q linearly
                  as a parity/orthogonality consequence, no independence assumption needed.
    P(B) ~ 15%  — kernel computation yields a DIFFERENT clean power law (√n_q, n_q², or
                  pq/(p+q)-type) ≠ linear → g-2 50ppm is coincidental.
    P(C) ~ 60%  — linearity cannot be derived without inserting the independence postulate,
                  OR the Q-G47 machinery structurally lacks the α-order term this session.

  Discriminating outcomes:
    A (CHORD):    derivation yields δ = −n_q·α/2 (LINEAR) without assuming additivity →
                  g-2 50ppm is a real closure, not a fit. δ becomes a derived winding law.
    B (DIFFERENT): derivation yields a DIFFERENT α-order coefficient/scaling (√n_q, n_q², other)
                  → g-2 50ppm coincidental; honest parameter-free result stays +4.0% (Stage-1).
    C (FIT/NOT-DERIVABLE): n_q-additivity can't be derived without assuming it (out of reach
                  this session OR structurally requires the postulate) → δ=−3α/2 is a 1-POINT FIT
                  dressed as a winding law; g-2 50ppm is an echo. MUST characterize precisely what
                  a full derivation would need (the exact Q-G47 unit-cell Lagrangian-integration step).

  Falsifier of framing (do-NOT-mis-frame guard, per brief + doc 115 §3):
    The geometric saliency estimates — Beltrami 1/(2π)→δ≈−0.84, Cosserat-PCA 1.25:1.0→δ≈+0.111,
    (2,3)-winding-fraction→±0.2 — are the WRONG mechanism (raw O(1) geometric anisotropy). A
    derivation that arrives at linear-in-n_q by plugging a geometric ratio into δ is NOT a valid
    Outcome A; it is a category error. The target is the α-ORDER kernel-feedback n_q-scaling.

  Anti-rescue guard (Rule 11 + ave-evidence-framing-discipline):
    Outcome C is a fully valid and important result. Do NOT debug toward A. Do NOT refill the
    "linear-is-derived" slot with a new unverified mechanism (Rule 12 substitution-not-retraction).
    If C: name the mechanism (which postulate is load-bearing) and characterize the gap.
```

## §6 — substrate-native-check (K4 + Cosserat checkpoint)

Walked BEFORE any derivation code (per skill discipline; this is the substrate-walk that prevents SM/QED defaults leaking in):

- **K4 checkpoint**: the saliency lives on the bond-pair LC tank's PHASE-SPACE (V_inc, V_ref) Clifford torus, NOT on real-space lattice-Cartesian axes. n_q = 3 is the q-axis poloidal winding count, sourced from the (2,q) torus-knot label (Op10 c-count = q), NOT from a spatial-trefoil real-space embedding (which doc 79 §6.2 flags as the "creeper" category error). The d-axis n_d = 2 is the bipartite-K4 lobe count.
- **Cosserat checkpoint**: the d/q split maps to the Cosserat translation/rotation DOF split (doc 85 §4.1, Vol 1 Ch 4:21-26). The kernel S(A) acts on the strain amplitude A, the Ax-4 saturation-state (not a 7th spatial DOF; the gauge-relative operating-point modulation per INVARIANT-S2).
- **Phase-space-coordinate discipline (A46)**: the test/derivation MUST stay in phase-space (V_inc/V_ref amplitudes A_d, A_q), matching the corpus claim's coordinates. Real-space measurements are uninformative here. The derivation operates on the phase-space currents $I_d=\cos(2\omega_C t)$, $I_q=\sin(q\omega_C t)$ — phase-space-native. ✓
- **Op14 checkpoint**: the kernel back-reaction is the Op14-class saturation-driven impedance modulation (the same mechanism as the α-suppression in doc 115 §3). The α-order-ness of δ is non-negotiable: any candidate that is O(1) is geometric anisotropy, the wrong mechanism.
- **KNOWN-WRONG ROUTE (explicit guard)**: doc 85 §5.2 plugs the geometric (1,1)-Beltrami pitch ratio |A_tor|/|A_pol| = 1/(2π) directly as the d/q amplitude ratio → δ ≈ −0.84 (10-80× off). This is the SM/geometry-default leak the brief warns against. The derivation must produce an **α-order** shift from kernel FEEDBACK, not an O(1) shift from geometric pitch. Plugging any geometric ratio into δ is disqualified as Outcome A.

## §7 — consistency-vs-emergence classification (of a successful derivation)

If the derivation succeeds (Outcome A), how should it be classed? Pre-registered so the result doc can't drift the framing post-hoc:

- The δ formula combines α (Class-2 axiom-manifestation: from Ax-4 kernel), 1/2 (Class-1 definitional: LC-equipartition normalization), and n_q (Class-2: from Ax-2 TKI winding count = Op10 c-count). A successful n_q-linearity derivation would be **Class-2 emergence (axiom-manifestation)**: δ = −3α/2 follows from Ax-2 (winding count) + Ax-4 (kernel) + LC-equipartition, with NO CODATA/PDG input feeding the derivation.
- **It is NOT Class-4 free-prediction emergence** because the inputs (α value, n_q=3) are themselves substrate-quantities, and the 50-ppm MATCH is a comparison against PDG (the match is a consistency check; the derivation of the FORM is the emergence claim). Headline discipline: a successful Outcome A is "the n_q-linear winding LAW is axiom-derived," NOT "we predicted g-2 from nothing."
- **If Outcome C**: δ=−3α/2 stays Class-1/consistency — a one-point fit to the bisection δ*, dressed in winding-law clothing. The g-2 50-ppm match is then an echo (post-hoc curve-through-one-point), and the honest forward result is the Stage-1 parameter-free +4.0% (per the saliency-closure leaf's own two-stage honesty note).

## §8 — Close-out plan

1. This commit: freeze prereg (§5 block frozen, no execution).
2. Next: execute §4 derivation attempt (analytical + numerical kernel computation).
3. Result doc `2026-05-31_FT-b-saliency-derivability_result.md`: Outcome A/B/C + the derivation OR the precise gap-characterization (the exact Q-G47 unit-cell Lagrangian-integration step a full derivation would need).
4. Commit result on this branch; `git push -u origin analysis/b-trefoil-saliency-derivability`. Do NOT merge, do NOT open PR.

## §9 — Cross-references

- doc 115 [`research/_archive/L3_electron_soliton/115_q_g19alpha_saliency_first_principles_derivation.md`](_archive/L3_electron_soliton/115_q_g19alpha_saliency_first_principles_derivation.md) §5, §6, §9
- doc 79 [`research/_archive/L3_electron_soliton/79_l3_branch_closure_synthesis.md`](_archive/L3_electron_soliton/79_l3_branch_closure_synthesis.md) §4, §5
- doc 85 [`research/_archive/L3_electron_soliton/85_kelvin_beltrami_foc_axiom_grounded_derivation.md`](_archive/L3_electron_soliton/85_kelvin_beltrami_foc_axiom_grounded_derivation.md) §5.2 (known-wrong geometric route)
- saliency closure leaf [`manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md):82,110
- Q-G47 closure leaf [`manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md)
- ξ_K derivation result [`research/2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md`](2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md) + script `src/scripts/verify/q_g47_sessions_19_xi_K_derivation.py`
- sweep `AVE-QED/scripts/g2_research/q_g19_alpha_saliency_sweep.py`
