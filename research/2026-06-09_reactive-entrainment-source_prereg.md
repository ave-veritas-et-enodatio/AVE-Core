# PREREG — The reactive-entrainment V→ω SOURCE (the missing pump leg) + the three-rate balance

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-saturation-temporal-preregs` (off `main`)
**Chain:** pump-derivation (FIXABLE form) → cross-sector run (**B**: confinement works, **source missing**, V on the wrong side of the gate) → **THIS: derive the source.**
**Framing source:** [`2026-06-07_entrainment-vortex-trapping-deep-dive.md`](2026-06-07_entrainment-vortex-trapping-deep-dive.md) (Camassa–McLaughlin–**Mertens** vortex-ring paper #4, arXiv 1110.3435) — §3 reactive/dissipative split, §2.4 three-rate balance, §7 the open plumber question. Grant + the Keith-lens 2026-06-09.
**Documentation home:** `research/` + the arc [epic](../_orchestration/2026-06-09_ion-compression-rectifier-arc.md). No (2,3)/electron claim — derives the SOURCE leg only.

> **SCAFFOLD.** Analytic derivation + a minimal bound-check. Derive-first (does the reactive source exist + the balance close); implement+run is the follow-on if A.

---

## 1. Target (one sentence)
Derive the **reactive added-mass entrainment SOURCE** for the V→ω pump — the **inertial** coupling by which the moving/trapped longitudinal V **entrains** the microrotational ω (the ring dragging its own circulation), routing V's energy into the **μ/microrotational** sector (the RIGHT side of the Γ=−1 `relu(−Γ)` gate, NOT the ε-electric side the cross-sector run found it on) — and determine whether the **three-rate balance** (reactive accumulation + bounded Γ=−1 rebound + dissipative leak) **closes**: V dynamically sources ω, bounded (no detonation), ledger closes.

## 2. The framing (paper #4 + the Keith-lens — the run decides, not assumes)
- **§3:** entrainment splits — **added-mass (REACTIVE) = inertia** vs **viscous-entrainment (DISSIPATIVE) = confinement**. We BUILT the dissipative confinement (the clamp, bounded); the **reactive added-mass = inertia** leg is the missing SOURCE. (Inertia = the surviving dark-wake `M_inertial ≡ L_drag`, clm-jwyy6l.)
- **§2.4:** genesis = a **three-rate balance** — *accumulation* (reactive entrainment, the source) vs *leak* (dissipation) vs *equilibration* (the rebound). The vortex **traps** when accumulation builds a reserve that **rebounds** the core; **detonates/escapes** without it. Our detonation = the no-equilibration (lossless) limit ("lossless engine lacks the equilibration channel; pumps instead of leaking at α").
- **§7 open question (Grant's call, Keith's working answer "both"):** is the over-amplitude resolved by **dissipative-equilibration** (a leak) or **reactive-resolution** (the rebound)? Working hypothesis: **both** — reactive accumulation + dissipative leak + the bounded Γ=−1 rebound. **Hypothesis, not assumption** (ave-discriminator-before-synthesis).
- **Honest ceiling:** the fluid is a **lens** (the deep-dive is consistency-class; AVE confinement is Meissner/Γ=−1, not buoyancy). It supplies the FORM (reactive/dissipative, three-rate), NOT a closed number (the trap/escape boundary is a 2-parameter empirical phase line). The number must come from the substrate (Γ=−1, α).

## 3. Mode / regime / phase-state (ave-regime-phase-state-check)
- **MODE:** longitudinal-scalar V → **μ/microrotational ω** via **reactive entrainment** (added-mass). The cross-sector run's failure was V routed to the **ε-electric** sector (Γ→+1, wrong side); the source must route to the **μ-short** side.
- **REGIME:** at/near the Γ=−1 wall (the rebound surface); the three-rate balance is the near-yield → yield dynamics.
- **PHASE-STATE:** dynamical; **Checkpoint 9** — the evolved ω, NOT the heuristic.

## 4. The derivation
1. **substrate-native-check + canonical pulls:** the added-mass/inertia (`M_inertial ≡ L_drag`, clm-jwyy6l, the entrainment §3); the **Beltrami source** (`85_kelvin_beltrami_foc_axiom_grounded_derivation.md` — V's trapped energy → helical ω = the reactive entrainment, the same object); Op17/Möbius bound (the rebound); grip=loss=R (the leak).
2. **Derive the reactive entrainment source term:** how does V **entrain** ω (drag the medium into circulation)? Is it the Beltrami source (V's trapped longitudinal energy sources a force-free helical ω, `∇×ω=λω`), routed into the **μ** sector? Write the EOM source term (distinct from the `relu(−Γ)·ω` confinement clamp).
3. **The three-rate balance:** reactive **accumulation** (the source) + bounded **rebound** (Γ=−1 reflection, Op17 R=Γ²≤1) + dissipative **leak** (R≈α, grip=loss). Does it **close** — bounded (no detonation), ledger closes (the ω-circulation paid by V's longitudinal energy + the leak)?
4. **Minimal numerical bound-check:** the three-rate balance produces a bounded, V-sourced ω (vs the detonation control)?

## 5. Discriminating outcomes
- **A — SOURCE EXISTS + BALANCE CLOSES:** the reactive entrainment (Beltrami) source is derivable, routes V→ω into the μ sector, the three-rate balance closes (bounded, ledger) → the pump is complete in FORM (source + rebound + leak) → implement + run next (the real V→ω fire).
- **B — SOURCE-BUT-NO-CLOSE:** the source exists but the three-rate balance doesn't close (accumulation outpaces equilibration → detonates, OR no net V→ω) → localize the open rate.
- **C — NO REACTIVE SOURCE:** no distinct reactive entrainment source exists / it collapses into the dissipative confinement → the source is fundamentally missing; the (2,3) genesis stays blocked.

## 6. Falsifier
Three-rate balance requires over-unity (free energy) → C/crank. ∮ V→ω = 0 even with the reactive source → B. Bounded V-sourced ω with a closing ledger → A.

## 7. Figures (ave-engineering-program-rigor)
1. the **three-rate balance** (accumulation / leak / equilibration vs time — does the reserve build + rebound, or run away?); 2. the **bounded V→ω source** (ω sourced by V, bounded) vs the detonation control; 3. the **energy ledger** (ω-circulation paid by V + leak, closes); 4. a **sweep** over the drive amplitude / the leak rate (robust vs tuned).

## 8. Guards / skills
substrate-native-check + CP9 · ave-canonical-leaf-pull (added-mass/inertia, Beltrami, Op17, three-rate) · ave-canonical-source (zero new free params; R≈α, Op17, the canonical inertia) · ave-resonant-amplification-check (bounded by Op17/the rebound, not resonant-amplified) · **ave-asymmetric-grip** (the reactive source vs the dissipative leak — both legs; the ledger is the crank-check) · ave-discriminator-before-synthesis (the "both legs / three-rate" framing is a hypothesis; the reactive-source-is-Beltrami is a hypothesis) · ave-driver-script-honesty (ledger + bound) · ave-discrimination-check (the reactive entrainment AVE-distinct vs ordinary added-mass) · verify-before-cite (clm-jwyy6l, 85_, Op17, the entrainment §3/§2.4 — verify; do NOT cite the retracted 1.009).

## 9. Deliverables
`2026-06-09_reactive-entrainment-source_result.md` — A/B/C + the reactive-source closed form (if it exists) + the three-rate balance (closes/detonates) + the bound-check + ledger + the sweep + figures + DERIVED/VERIFIED/BLOCKED + skills fired. Driver. Own implementor branch off `analysis/2026-06-09-cross-sector-pump-run` (has the pump implementation to build on); do NOT push/merge.
