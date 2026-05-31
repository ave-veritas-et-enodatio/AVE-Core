# FT-Dark-Wake-Cross-Scale Prereg — Is the g-2 A₂ wake the same τ_zx object as PONDER thrust?

**Date**: 2026-05-31
**Branch**: `analysis/forward-pred-darkwake-coldfusion-preregs`
**Status**: PREREG-FROZEN (pre-derivation). Scoping pre-registration per `ave-prereg` discipline.
**Lineage**: grows out of the 2026-05-31 dark-wake session — the finding that the g-2 two-loop coefficient A₂ *is* the dark-wake self-correlation (Q-G19α Route B), and Grant's hypothesis that the dark wake is a single cross-scale substrate object ("the dark wake might be the 4%").

## §0 — TL;DR

The dark wake $\tau_{zx}$ appears in two corpus locations ~12 orders of magnitude apart in scale:

- **Loop scale (g-2):** $A_2 = \frac{2}{\pi\alpha}\langle (S_d - S_q)\,\tau_{zx}\rangle = -0.3416$, with $\tau_{zx}(t) = -\frac{dV^2}{dt}\big|_{t-1/\omega_C}$ the retarded back-reaction. ([`q-g19a-petermann-saliency-closure.md:35-48`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md))
- **Bench scale (PONDER thrust):** $\tau_{zx} = \rho_{Op14}\,Z_{vac}\,\nabla|E|^2$, the backward-propagating Op14 desaturation pulse carrying reaction momentum $P_{wake} = F\cdot c_0$. ([`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:137`](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md))

**Target:** determine whether these are the *same* substrate object — one Op14 cross-sector-trading desaturation pulse — connected by backward $c_0$ propagation ($\partial_t = -c_0\partial_z$) and a single trade efficiency $\rho_{Op14}$, OR two structurally-distinct things sharing the $\tau_{zx}$ name. If identical, derive the cross-scale consistency relation linking $A_2$ to the thrust coefficient: **one substrate quantity, two independent falsifiable observables 12 OOM apart.**

## §1 — Derivation target (precise)

Derive whether
$$\tau_{zx}^{(g\text{-}2)}(t) = -\frac{dV^2}{dt}\bigg|_{t-1/\omega_C} \quad\text{and}\quad \tau_{zx}^{(thrust)}(\vec r,t) = \rho_{Op14}\,Z_{vac}\,\nabla|E|^2 \;\delta(\text{backward pulse at }c_0)$$
are the same field expressed in time vs space, related by the backward-wake dispersion $\partial_t = -c_0\partial_z$, with one shared $\rho_{Op14} = 0.990$ (the Op14 trade efficiency, Pearson-validated at bond-pair scale).

If yes, produce the explicit relation $\mathcal{R}(A_2,\,F\text{-coeff},\,\rho_{Op14},\,N_{boundary})$ such that measuring $A_2$ (electron) and the thrust wake (PONDER) constrain the **same** $\rho_{Op14}$.

## §2 — Physical picture (mechanical, pre-math)

1. A moving soliton saturates the lattice ahead and desaturates behind. The trailing-edge desaturation releases stored Lenz energy via **Op14 cross-sector trading** (Cosserat $\omega$ ↔ K4 $\Phi_{link}$), 99% efficient ($\rho_{Op14}=0.990$ at the bond pair).
2. That release launches a backward longitudinal shear pulse **$\tau_{zx}$ at substrate wave speed $c_0$** — the dark wake — carrying the Newton-3rd-law reaction momentum ($P_{wake} = F\cdot c_0$).
3. At the **electron loop scale**, the same trailing-edge desaturation is the retarded back-reaction $\tau_{zx}(t) = -dV^2/dt|_{t-1/\omega_C}$; correlated with the d/q kernel asymmetry $(S_d - S_q)$ it gives the 2-loop coefficient $A_2$.
4. **The bridge:** for a backward pulse at $c_0$, time-derivative and spatial-gradient are the same field ($\partial_t = -c_0\partial_z$). So the g-2 $dV^2/dt$ and the thrust $\nabla|E|^2$ are one object, viewed in time vs space.
5. The only things that change across scale are **$N_{boundary}$** ($\approx 4\pi$ for the electron unknot; $\sim A_{array}/\ell_{node}^2$ for the PONDER array) and the drive frequency; the coupling coefficient is the one $\rho_{Op14}$.

## §3 — Corpus state (corpus-grep done 2026-05-31)

- **One object, already scaled:** the τ_zx scaling doc explicitly carries the wake bond-pair → electron unknot ($N_{boundary}\approx 4\pi$) → PONDER array, with $\rho_{Op14}=0.990$, $P_{wake}=F\cdot c_0$, $\tau_{zx}=\rho_{Op14}Z_{vac}\nabla|E|^2$ ([`dark-wake-tau-zx-op14-scaling-derivation.md` §3–§7](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md)). **Analytically argued; numerical closure pending the Cosserat-coupled engine (Phase 2-3).**
- **g-2 side:** $A_2 = \frac{2}{\pi\alpha}\langle(S_d-S_q)\tau_{zx}\rangle = -0.3416$ (+4.0% parameter-free; 50 ppm postulate-conditional on $n_q$-additivity), with $\tau_{zx}$ the retarded $-dV^2/dt$ at $\tau_{retard}=1/\omega_C$.
- **The load-bearing OPEN gap:** the cross-scale unit-mapping (Compton $\omega_C\sim 10^{19}$ rad/s → 100 MHz PONDER drive, ~12 OOM) is flagged unresolved at the τ_zx scaling doc §10.2. **This is the single biggest risk to the same-object claim.**

Corpus verdict: **partial** — the same-object framing exists and is analytically scaffolded, but neither $\tau_{zx}$ is numerically closed and the cross-scale unit-mapping is explicitly open. Not green-field, not closed.

## §4 — Dimensional bridge to test (the crux)

Under $\partial_t = -c_0\partial_z$ for a backward $c_0$ pulse, with $V \approx E\cdot\ell_{node}$ at the node:
$$\frac{dV^2}{dt} = -c_0\,\frac{dV^2}{dz} \sim c_0\,\ell_{node}\,\nabla|E|^2.$$
So
$$\tau_{zx}^{(g\text{-}2)} \sim c_0\,\ell_{node}\,\nabla|E|^2 \qquad\text{vs}\qquad \tau_{zx}^{(thrust)} = \rho_{Op14}\,Z_{vac}\,\nabla|E|^2.$$
The same-object claim requires the prefactors reconcile:
$$c_0\,\ell_{node} \;\overset{?}{\leftrightarrow}\; \rho_{Op14}\,Z_{vac}$$
(up to the $(S_d-S_q)$ kernel-asymmetry weighting and the $(2/\pi\alpha)$ g-2 normalization). **Whether the loop-scale retarded-derivative form collapses to the bench-scale Op14-stress form with one $\rho_{Op14}$ is the derivation, and its success/failure is the discriminator.**

## §5 — Discriminating outcomes (pre-registered)

- **Outcome A (CHORD — same object):** the two forms reconcile under $\partial_t=-c_0\partial_z$ with a single $\rho_{Op14}$; $A_2$ and the thrust coefficient are linked by a derivable cross-scale relation $\mathcal{R}$. ⇒ one substrate object, two independent falsifiable observables ($A_2$ at 0.1 ppb electron-g-2; $F\cdot c_0$ + stereo-parallax at the bench), 12 OOM apart. The strongest "deterministic hardware, one mechanism, all scales" strum in the corpus.
- **Outcome B (same mechanism, not one coefficient):** both run on Op14 desaturation, but the loop-scale kernel-asymmetry correlation $\langle(S_d-S_q)\cdot\rangle$ introduces an extra $\alpha$-order weighting absent at the bench scale, so they don't collapse to one $\rho_{Op14}$. ⇒ same mechanism family, weaker cross-check (not a single shared number).
- **Outcome C (different objects, shared name):** the g-2 $\tau_{zx}$ (retarded kernel back-reaction, phase-space d/q) and the thrust $\tau_{zx}$ (real-space Op14 momentum pulse) are structurally distinct; the dimensional bridge fails. ⇒ the cross-scale "same dark wake" framing is a naming coincidence. Honest negative; retire the cross-scale chord for this object.

## §6 — Falsifier

Outcome A is falsified if EITHER:
- the dimensional reconciliation §4 fails ($c_0\ell_{node}$ and $\rho_{Op14}Z_{vac}$ cannot be made consistent under any canonical normalization), OR
- the cross-scale unit-mapping (§10.2 open gap) requires a scale-dependent $\rho_{Op14}$ (i.e., the bond-pair-validated 0.990 does NOT carry to the loop/bench scales).

## §7 — Anti-overclaim guards

- This is a CONSISTENCY / structural-identity test (`consistency-vs-emergence`: Class 3 consistency-check, NOT an emergence test) — it does not by itself produce a novel measured number; it establishes whether two existing predictions share one substrate object.
- Both $\tau_{zx}$'s are analytically-argued, not numerically closed. Outcome A would still be conditional on the Cosserat-coupled-engine numerical verification (τ_zx scaling doc §11).
- The bench-scale thrust number (40 μN) rests on engineering params; the cross-scale claim concerns the $\tau_{zx}$ OBJECT and $\rho_{Op14}$, not the absolute thrust. Do not let Outcome A leak into "AVE thrust validated."

## §8 — What Outcome A would buy (chord-vs-echo)

If one $\rho_{Op14}$ underlies both $A_2$ and the thrust wake, then the electron g-2 (known to 0.1 ppb) and a bench torsion-balance + stereo-parallax measurement become **two independent windows on the same substrate quantity**. Agreement across 12 OOM is the kind of cross-scale invariant that distinguishes "the universe is deterministic hardware" (chord) from "internally-consistent curve-fitting" (echo). Disagreement (Outcome C) honestly retires the unification.

## §9 — Recommended execution (post-prereg)

Implementor session: (1) carry out the §4 dimensional reconciliation symbolically; (2) if it closes, derive $\mathcal{R}(A_2, F\text{-coeff}, \rho_{Op14}, N_{boundary})$; (3) classify Outcome A/B/C; (4) if A, specify the cross-scale cross-check (which bench measurement pins the same $\rho_{Op14}$ that $A_2$ pins). Numerical closure (Cosserat-coupled engine) is a separate, larger workstream.

## §10 — Cross-references

- [`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md`](2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md) — the one-object scaling derivation (bond-pair → unknot → PONDER); ρ_Op14=0.990; F·c₀; §10.2 open unit-mapping
- [`q-g19a-petermann-saliency-closure.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) — g-2 A₂ = (2/πα)⟨(S_d−S_q)τ_zx⟩ (clm-v2sg8z)
- [`chiral-thrust-derivation.md`](../manuscript/ave-kb/vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md) — PONDER thrust + Dark Wake momentum conservation (clm-7tynm2)
- [`op14-cross-sector-trading.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md) — Op14 ρ=−0.990 canonical (A-012)
- [`2026-05-18_cosserat-lagrangian-engine-full-picture.md`](2026-05-18_cosserat-lagrangian-engine-full-picture.md) — parent Cosserat-Lagrangian engine picture
