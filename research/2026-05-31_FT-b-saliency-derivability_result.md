# Result — FT-b: trefoil saliency δ = −3α/2 is a 1-POINT FIT, not a derivable winding law (OUTCOME C)

**Date**: 2026-05-31
**Branch**: `analysis/b-trefoil-saliency-derivability` (off `main` @ a743d84d, isolated worktree)
**Prereg (FROZEN)**: [`2026-05-31_FT-b-saliency-derivability_prereg.md`](2026-05-31_FT-b-saliency-derivability_prereg.md) @ commit `c38d2b7e`
**Attempt scripts**: [`2026-05-31_FT-b-saliency-derivability_attempt.py`](2026-05-31_FT-b-saliency-derivability_attempt.py) + [`2026-05-31_FT-b-saliency-derivability_stresstest.py`](2026-05-31_FT-b-saliency-derivability_stresstest.py)
**Skills fired**: `ave-prereg`, `ave-canonical-leaf-pull`, `substrate-native-check`, `ave-fundamental-ground-up-implementation`, `consistency-vs-emergence`, `ave-evidence-framing-discipline`.

---

## §0 — TL;DR

**OUTCOME C (pre-registered prior P(C) ~ 60%): the n_q-LINEAR additivity CANNOT be derived from the substrate kernel back-reaction without assuming it.** Two independent computations confirm:

1. The α-order kernel back-reaction on the actual (2,q) phase-space currents is **exactly q-independent** — it produces NO q-scaling at all (not linear, not √q, not q²). Linearity-in-q only appears when "q independent unit windings" is **postulated** (the additivity assumption itself).
2. The full Route-B correlation ⟨(S_d − S_q)·τ_zx⟩ — the actual C_2 mechanism — matches the PDG-required saliency at **q = 3 ONLY** (to 0.12%). At q ∈ {1, 5, 7} the linear law `δ = −qα/2` misses by factors of **24× to 780×, including wrong sign** at q = 5, 7.

**Therefore δ = −3α/2 is a single-point fit to the bisection δ* = −0.01093, structurally motivated (α ✓, 1/2 ✓) but with the winding-scaling n_q INSERTED, not derived. The g-2 50-ppm closure is an echo: a curve threaded through one fitted point, dressed as a winding law.** The honest parameter-free forward result remains the Stage-1 **+4.0%** (per the saliency-closure leaf's own two-stage honesty note).

This is the discipline working at full strength (Rule 11): a pre-registered prediction with a clean negative, a single mechanism (q-flat kernel + single-point correlation match) explaining the result, branch closed. **No rescue attempted.**

## §1 — What was tested (and what was NOT)

Tested: can **n_q-LINEAR additivity** — δ scaling LINEARLY in the q-axis winding count — be derived from the K4-Cosserat substrate kernel back-reaction, WITHOUT assuming it, INDEPENDENT of the g-2 target value?

NOT re-litigated (taken as corpus-derived per doc 115 §3-§4):
- **α** from the Ax-4 saturation-kernel expansion $S(A)\approx 1-A^2/2\approx 1-\pi\alpha$ at $A^2\approx 2\pi\alpha$ — DERIVED ✓.
- **1/2** from the Vol 4 Ch 1:175-184 LC-equipartition Virial sum — DERIVED ✓.

The entire load was on the third factor: the **n_q-LINEAR** scaling, doc 115 §6's "single remaining intuitive step."

## §2 — The derivation attempt (Step 1: kernel back-reaction per winding)

**Setup (substrate-native, phase-space coordinates per prereg §6).** The Ax-4 kernel $S(A)=\sqrt{1-A^2}$ acts on the canonical Route-B (2,q) phase-space currents (`q-g19a-petermann-saliency-closure.md` Route-B §1):
$$I_d(t) = \cos(2\omega_C t)\ (n_d=2,\ \text{bipartite-K4}), \qquad I_q(t) = \sin(q\,\omega_C t)\ (n_q=q,\ \text{half-twist count}).$$
At the symmetric Schwinger budget $A_{d,\text{peak}}^2 = A_{q,\text{peak}}^2 = 2\pi\alpha$, the per-axis "kernel load" is the time-averaged kernel deviation $\langle 1 - S(A_{\text{axis}}^2)\rangle$ — how hard the saturation kernel pulls on that axis. The saliency is the asymmetry the back-reaction would introduce; for it to scale with $n_q$, this load must scale with the winding count.

**Result (exact kernel, $N_t = 4\times10^6$):**

| $n$ (winding) | $\langle 1 - S(A^2)\rangle$ (exact) | residual vs $n=1$ |
|---|---|---|
| 1 | $1.1563130196\times10^{-2}$ | — |
| 2 | $1.1563130196\times10^{-2}$ | $0$ |
| 3 | $1.1563130196\times10^{-2}$ | $6.5\times10^{-14}/\alpha^2$ (machine-zero) |
| 5 | $1.1563130196\times10^{-2}$ | $0$ |
| 7 | $1.1563130196\times10^{-2}$ | $0$ |

**The per-axis kernel load is EXACTLY $n$-independent at α-order** — identical to 10 significant figures for every $n$. The reason is structural and unavoidable: $\langle\sin^2(n\omega t)\rangle = 1/2$ for **every** integer $n\ge1$, so $\langle 1 - S\rangle \approx \langle A^2\rangle/2 = (2\pi\alpha)\cdot(1/2)\cdot(1/2)$ regardless of $n$. The only $n$-dependence is at $O(\alpha^2)$ — the $10^{-14}$ residual, i.e. machine-zero in units of $\alpha^2$.

**There is no $n_q$-scaling — linear, $\sqrt{n_q}$, or $n_q^2$ — in the kernel back-reaction acting on the actual single-harmonic (2,q) currents.** The kernel is winding-count-blind at the order the saliency lives.

## §3 — Where linearity actually comes from (Step 2: the postulate, exposed)

doc 115 §6 motivates linearity as: "each q-winding is a distinct twist; cross-twist coupling is $O(\alpha^2)$; so at leading α-order the windings add linearly." The attempt tested what "add" means:

- **(2a) The ACTUAL Route-B q-axis current** is a SINGLE harmonic $\sin(q\omega_C t)$. Its kernel load is q-flat (§2). A single harmonic carries ONE kernel-load unit regardless of its frequency $q$ — **not $q$ units.**
- **(2b) The ADDITIVITY reading** requires the q-axis to host $q$ SEPARATE unit oscillators, each at the budget, each carrying one α-order kernel-shift unit, which then sum to $q\times(\text{unit})$. This IS linear in $q$ — **but only by construction.**

**The step from (2a) to (2b) IS the additivity postulate.** The (2,q) torus knot supplies ONE current at frequency $q$ (the c-count = q crossing structure of a single closed strand), not $q$ independent oscillators. Decomposing one $q$-frequency harmonic into $q$ summed unit windings is an interpretive choice with no substrate-dynamical justification at α-order — the kernel does not "see" the $q$ crossings as $q$ separate loads (§2 proves it sees them as one). Linearity is **inserted at this decomposition step**, exactly as doc 115 §6 admits ("the one structural assumption not yet rigorously derived").

## §4 — Stress-test (anti-confirmation): the full correlation matches at q=3 ONLY

Outcome C from §2-§3 could in principle be an artifact of probing the per-axis *time-average* instead of the full Route-B *correlation* ⟨(S_d − S_q)·τ_zx⟩ (the actual C_2 mechanism, which carries the retarded dark-wake phase). The stress-test generalized the canonical sweep from $q=3$ to $q\in\{1,3,5,7\}$ and asked: **does the correlation SELECT the linear law across the family?**

**Test II — kernel asymmetry at symmetric budget** ($N_t=2\times10^6$): $\langle S_d - S_q\rangle \approx 10^{-19}$ (machine zero) for ALL $q$. The kernel has **zero intrinsic d-vs-q preference** and no q-scaling of that (non)preference. The nonzero correlation comes entirely from the retarded $\tau_{zx}$ phase (dark wake), not a kernel q-asymmetry.

**Test I — does the saliency required for the PDG match scale as $-q\alpha/2$?** This is the decisive table. For each $q$, find the $\delta$ that brings $C_2(q,\delta)$ to the PDG target $-0.328479$, and compare to the linear law $-q\alpha/2$:

| $q$ | $C_2(\delta{=}0)$ | $\delta_{\text{for PDG}}$ | $-q\alpha/2$ (linear law) | ratio |
|---|---|---|---|---|
| 1 | $-1.2234$ | $-2.851$ | $-0.003649$ | **781.4** |
| **3** | $-0.3416$ | $-0.010933$ | $-0.010946$ | **0.9988** ✓ |
| 5 | $+0.6103$ | $+0.4332$ | $-0.018243$ | **−23.75** (wrong sign) |
| 7 | $-4.2734$ | $+1.4218$ | $-0.025541$ | **−55.67** (wrong sign) |

**The linear law matches the PDG-required saliency at $q=3$ alone (0.12%). At $q=1,5,7$ it misses by 24× to 780×, with the WRONG SIGN at $q=5,7$.** Moreover $C_2(\delta{=}0)$ is wildly non-monotonic in $q$ ($-1.22, -0.34, +0.61, -4.27$) — there is no smooth winding-law structure in the correlation at all. $q=3$ simply happens to land near $C_2(0)\approx-1/3$ where the small-$\delta$ linear response of the correlation threads through the $-q\alpha/2$ value.

**The stress-test confirms Outcome C harder than the first pass:** the full correlation, far from rescuing linearity, demonstrates that the $q=3$ match is a single-point coincidence. A genuine winding law would track $-q\alpha/2$ across the family; this tracks it at exactly one $q$.

> **Caveat on the q≠3 rows (honest scoping).** Per `q-g19a-petermann-saliency-closure.md` FI-13 resolution, the AVE taxonomy has NO physical "single-loop (2,5) or (2,7) lepton" — the muon is single-loop (2,3)+torsion, baryons are Borromean 3-loop. So the $q=5,7$ rows are NOT claims about real particles; they are the **falsifier probe for the n_q-additivity LAW** that the saliency-closure leaf itself registers as the test (leaf §"Falsification predictions"). The law, IF real, must scale as $-q\alpha/2$ for the hypothetical family; it demonstrably does not. The physical content is unchanged: there is only ever ONE measured point ($q=3$ electron), and a one-point law is a fit.

## §5 — Cross-check vs the OTHER substrate winding law (Step 4)

The substrate already carries a DERIVED winding-composition law for the SAME (2,q) two-channel structure: the chirality coupling $\chi = \alpha\cdot pq/(p+q)$ (doc 79 §5, doc 20 — parallel-impedance combination of the two channels). For the electron $\chi = \alpha\cdot 6/5 = 1.2\alpha$. This is p-q-symmetric and NON-linear. Compared against $\delta^*/\alpha = -1.498$:

| law | $\delta/\alpha$ | vs $\delta^*$ |
|---|---|---|
| LINEAR $-n_q/2$ (the postulate) | $-1.500$ | **+0.12%** |
| $\sqrt{n_q}$ $-\sqrt{n_q}/2$ | $-0.866$ | $-42.2\%$ |
| $n_q^2$ $-n_q^2/2$ | $-4.500$ | $+200.4\%$ |
| $pq/(p+q)$ $-\tfrac{1}{2}pq/(p+q)$ (parallel, ÷2) | $-0.600$ | $-60.0\%$ |
| $pq/(p+q)$ full chirality $\chi$ | $-1.200$ | $-19.9\%$ |
| $n_q-n_d$ $-(n_q-n_d)/2$ | $-0.500$ | $-66.6\%$ |

Only LINEAR matches. But this sharpens the problem rather than resolving it: **the substrate's own derived winding-composition for this exact object is the DIFFERENT $pq/(p+q)$ law.** A genuine derivation of the saliency would have to explain WHY the saliency takes the linear law while the chirality takes $pq/(p+q)$ — for the same two channels of the same (2,q) knot. Nothing in Steps 1-2 supplies that reason: the kernel load is q-flat (§2), and linearity appears only under the inserted independent-winding postulate (§3). That a different, p-q-symmetric law is the *derived* one for the same structure is positive evidence that the linear law is NOT the substrate-native composition — it is the law that fits the single data point.

## §6 — Precise gap characterization: what a full derivation would need

Per the prereg deliverable (and doc 115 §9's claim that Q-G47 Sessions 19+ unit-cell Lagrangian integration is the closure path), here is exactly what is missing and why the named machinery does not supply it:

**(a) The named machinery computes the wrong order.** The Q-G47 Sessions-19 derivation (`src/scripts/verify/q_g47_sessions_19_xi_K_derivation.py`, re-verified this session) computes **static linear-elastic moduli**: $K_0=4k_a+8k_s=16/7$, $G_0=8k_s=8/7$, $\xi_{K1}=(\mu+\kappa)/T_{EM}=8/3$, $\xi_{K2}=12\xi_{K1}=32$. A targeted grep confirms the script contains **zero** occurrences of "kernel", "saturat", "winding", "n_q", "petermann", or "saliency" (the one "alpha" match is the micropolar modulus name "Cosserat α-equivalent", NOT fine-structure $\alpha$). It evaluates the saturation kernel only at the *operating point* ($S(A^*)=0$ at K=2G), NOT Taylor-expanded to α-order for per-mode back-reaction. **It is the substrate-scale static-elasticity layer; the saliency is a particle-scale α-order phase-space kernel-feedback quantity. The two layers are not connected by this machinery, and it has no term that resolves per-winding.**

**(b) A genuine derivation would need a NEW computation with three pieces the current machinery lacks:**
1. **An α-order kernel-feedback term** in the (2,q) phase-space Lagrangian — the saturation kernel $S(A)$ Taylor-expanded around the operating point to capture the back-reaction on the d-axis vs q-axis strain amplitudes (NOT just evaluated at $S(A^*)$). This is the term that would source a nonzero $\delta$.
2. **A mechanism that makes that α-order back-reaction RESOLVE the $q$ crossings as $q$ separable contributions** — i.e. a substrate-dynamical reason the single $\sin(q\omega_C t)$ harmonic decomposes into $q$ independent kernel-shift units. §2 proves the kernel does NOT do this on its own (it sees the harmonic as one load). Something beyond the kernel time-average — a per-crossing localization of the saturation, or a mode-by-mode eigendecomposition of the saturated (2,q) attractor — would have to supply it. **No such mechanism exists in the corpus, and §4 shows the full correlation does not exhibit the linear scaling such a mechanism would produce.**
3. **A selection principle distinguishing the linear law from the $pq/(p+q)$ chirality law** (§5) for the same two channels.

**(c) The empirical verdict on whether such a derivation could succeed is negative, not merely absent.** This is the strongest part of the gap characterization: it is not only that the integration is "out of reach this session." The stress-test (§4) shows the Route-B correlation — the actual mechanism the saliency is defined through — does NOT scale as $-q\alpha/2$ across the family. So even a completed α-order kernel-feedback Lagrangian integration, IF it faithfully reproduces the Route-B correlation (which is its target), would NOT yield the linear law as a family-wide scaling. It would reproduce the q-3-only match. **The gap is therefore structural, not computational:** linearity is a property of the single fitted point, not of the substrate dynamics, and no unit-cell integration of the existing mechanism will convert it into a derived winding law.

## §7 — consistency-vs-emergence classification (per prereg §7, applied to the actual outcome)

The prereg pre-registered: if Outcome C, δ = −3α/2 stays **Class-1 / consistency** — a one-point fit to the bisection δ*, with the winding-law framing being post-hoc. **That is the landed classification.**

- δ = −3α/2 is NOT a Class-2 axiom-manifestation emergence. Its α and 1/2 factors are axiom-derived, but the load-bearing n_q-scaling that makes the number −3α/2 (rather than −α/2 or −1.2α) is fitted, not derived.
- The g-2 50-ppm match is a **consistency check threaded through one fitted parameter** (δ*), not an emergence prediction. Per the saliency-closure leaf's own two-stage honesty note (`q-g19a-petermann-saliency-closure.md`:16,105), the **forward, parameter-free, emergence-class result is the Stage-1 +4.0%** (symmetric d/q split, no saliency postulate). The Stage-2 50-ppm is postulate-dependent and now confirmed fit-dependent.
- Headline discipline (`ave-evidence-framing-discipline`): the correct statement is *"AVE forward-derives the Petermann coefficient to +4.0% with zero free parameters; the 50-ppm refinement requires a one-point saliency fit (δ = −3α/2) whose winding-law form is structurally motivated but not derivable from substrate dynamics."* It is NOT *"AVE predicts the electron g-2 to 10 ppm from first principles."*

## §8 — Flag (Rule 6, flag-don't-fix): corpus statements this result bears on

Surfaced for auditor adjudication — NOT silently edited (these are the auditor's to land per lane discipline):

1. **doc 115 status header** (`115_q_g19alpha_saliency_first_principles_derivation.md`:5) reads *"Substantial structural closure … The n_q-additivity assumption is the one remaining intuitive step pending K4-Cosserat Lagrangian numerical confirmation."* This result IS that numerical confirmation attempt, and it returns NEGATIVE: the K4-Cosserat kernel does not confirm n_q-additivity; it shows the kernel load is q-flat and the correlation matches at q=3 only. The "pending confirmation" framing should become "confirmation attempted 2026-05-31, returned Outcome C (not derivable; q=3-only fit)." Per Rule 12, preserve the body, add a 🔴 header.

2. **doc 115 §9 recommended next-session work** item 1 (*"K4-Cosserat Lagrangian integration showing per-q-winding α-order kernel feedback contributes additively … the same kind of work as Q-G47 Sessions 19+"*) is now answered: the Q-G47 machinery computes static moduli, NOT α-order per-winding feedback (§6a); and the per-winding additivity it was expected to show is contradicted by the q-flat kernel load (§2) + q-3-only correlation match (§4). This is not "still to do"; it is "attempted and structurally blocked."

3. **saliency-closure leaf** (`q-g19a-petermann-saliency-closure.md`:110) §"What still needs derivation" already honestly scopes n_q-additivity as the "single remaining intuitive step" requiring "K4-Cosserat Lagrangian numerical integration." This result resolves that open item to **NEGATIVE**. The leaf's two-stage honesty framing (Stage-1 +4.0% forward / Stage-2 50-ppm postulate-dependent) is VINDICATED and should be strengthened: Stage-2's postulate is now shown to be fit-dependent, not just unproven. The leaf's headline ("4% forward (no postulate) → 10 ppm (with n_q-additivity postulate)") remains accurate; this result downgrades the postulate from "plausible-pending-computation" to "fit-confirmed-not-derivable."

These three are consistent with each other and with the leaf's existing honesty notes — no contradiction to adjudicate, only a status upgrade from "open/pending" to "closed-negative." The auditor lands the Rule-12 headers + any KB-leaf solidity adjustment.

## §9 — Honest closure (Rule 11)

A pre-registered prediction (P(C) ~ 60%) landed at its most-likely outcome via a clean mechanism: the α-order kernel back-reaction is winding-count-blind (§2, ⟨sin²(nωt)⟩=1/2 ∀n), so linearity is inserted at the single-harmonic→q-unit-windings decomposition (§3); the full correlation confirms by matching at q=3 only (§4); the substrate's own derived winding law for the same object is the different pq/(p+q) (§5). One mechanism explains all of it. **Branch closed. No rescue. No slot-refill (Rule 12): the "linear-is-derived" hypothesis is retracted, not replaced with a new unverified mechanism — if a future per-crossing-localization mechanism is proposed, it gets its own version number and verification chain.**

The chord-vs-echo verdict for THIS link: the g-2 50-ppm closure is an **echo** (one-point fit). The real chord that survives is the parameter-free **Stage-1 +4.0%** forward Petermann derivation — which stands untouched, and is the honest headline.

## §10 — Cross-references

- Prereg (frozen `c38d2b7e`): [`2026-05-31_FT-b-saliency-derivability_prereg.md`](2026-05-31_FT-b-saliency-derivability_prereg.md)
- Attempt: [`2026-05-31_FT-b-saliency-derivability_attempt.py`](2026-05-31_FT-b-saliency-derivability_attempt.py) (Steps 1, 2, 4)
- Stress-test: [`2026-05-31_FT-b-saliency-derivability_stresstest.py`](2026-05-31_FT-b-saliency-derivability_stresstest.py) (Tests I, II)
- doc 115 [`_archive/L3_electron_soliton/115_q_g19alpha_saliency_first_principles_derivation.md`](_archive/L3_electron_soliton/115_q_g19alpha_saliency_first_principles_derivation.md) §3, §4, §6, §9
- doc 79 [`_archive/L3_electron_soliton/79_l3_branch_closure_synthesis.md`](_archive/L3_electron_soliton/79_l3_branch_closure_synthesis.md) §5 (χ = α·pq/(p+q))
- saliency-closure leaf [`../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md):16,82,105,110
- Q-G47 machinery (re-verified static-moduli): `src/scripts/verify/q_g47_sessions_19_xi_K_derivation.py`; result [`2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md`](2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md)
- canonical sweep: `AVE-QED/scripts/g2_research/q_g19_alpha_saliency_sweep.py`
