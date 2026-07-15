[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "WALK-LEVEL / PROPOSED-DEFINITIONAL framing (2026-07-15 thermal/phase-register walk, Entry 14). Heat / entropy / temperature phase-definitions are gated on the unbuilt two-tank decoherence check; nothing above consistency-class is asserted. The one axiom-derived line (heat = decoherence not dissipation, from Ax3) rides the existing kernel; the canonical anchors (clm-hp7nlm δ_strain/TCC, translation-stochastics FDT / Johnson-Nyquist, clm-3zz0f6 √S Komar weight) carry the load. No new value; KB claim-candidacy is Grant-gated on the registered check."
-->

# Thermal Phase Registers — heat / entropy / temperature as clock phase-diffusion (WALK-LEVEL)

> **★ STATUS: WALK-LEVEL / PROPOSED-DEFINITIONAL — LOW SOLIDITY, GATED.** This leaf records the 2026-07-15 thermal/phase-register walk (docket Entry 14). The phase-definitions of heat / entropy / temperature below are **PROPOSED-DEFINITIONAL, not solid until measured** — gated on the registered **two-tank decoherence check** (§4). Nothing here is asserted above **consistency-class**; the single axiom-derived line is "heat = decoherence, not dissipation" (from Axiom 3). The mean-vs-variance split rides canonical anchors that already exist. **No numerical value is promoted.**
>
> **🔴 UPDATE 2026-07-15 — the two-tank check has FIRED (PR #707, `analysis/two-tank-decoherence-check`): verdict `ADDITIVE-ARTIFACT`.** The ★#1 "temperature = phase-diffusion width/rate" definition **DEMOTES to NOT-DEMONSTRATED-AS-POSED / RE-GATED on the unbuilt F6 irreversible $\varepsilon\to T2$ depletion channel** (§2). ★#2 (entropy) stays PROPOSED (untested by this check). **The one Ax3 line is CORROBORATED** — the bounded reversible dephasing the check measured IS "heat = reversible phase-scramble, not loss" (§1). Details below carry the dated status; the prior PROPOSED text is preserved (Rule-12).
>
> **Sector / regime / phase-state declaration.** MODE: an ensemble of bound soliton LC tanks (each a clock) immersed in a traveling radiation bath. REGIME: sub-yield, lossless-reactive (Axiom 3) — the bath scrambles *phase*, not amplitude past the wall. PHASE-STATE: incoherent-propagating (the heat register), distinct from coherent-bound (solitons) and coherent-propagating (radiation). This is the **third phase-register** in the unification table below.

## §1 — Heat as measured by bound structures = phase-diffusion between soliton clocks

Heat, as a bound structure feels it, is **phase-diffusion between soliton clocks**. The observable splits cleanly:

- **MEAN shift = the thermal operating point.** The ensemble-mean clock detuning is the substrate's thermal bias point — canonically the $\delta_{strain}$ / TCC-at-$T_{CMB}$ mechanism (Cosserat-rotation-sector mass-gap thermal-mode-population ASYM; Q-DELTA-MAP-1, `clm-hp7nlm`, [`../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md); catalog row [`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md) §4 "$\delta_{strain}$ at $T_{CMB}$"). This is the *operating-point* half — the SIGN-predicted, magnitude-definitional δ_strain residual.
- **VARIANCE = the heat content proper.** The *spread* of the clock-detuning distribution is the heat content — the Johnson-Nyquist $k_BT$-per-mode strain-noise jittering every tank (`translation-circuit.md` §4 "Vacuum thermal noise floor"; [`translation-tables/translation-stochastics.md`](translation-tables/translation-stochastics.md) FDT = boundary-$Z$ thermalization).

**The one axiom-derived line — heat = decoherence, not dissipation (from Axiom 3, the ONLY axiom-derived statement here; now ALSO check-corroborated, PR #707):**

- **heat = phase disorganization of reactive energy, NOT loss** (Ax3-lossless: the substrate does not destroy energy; it scrambles the phase relationship between clocks; the reactive energy is conserved, redistributed to incoherent modes). *(This bullet — and only this bullet — is the axiom-derived line.)* **★ CHECK-CORROBORATED (PR #707):** the two-tank check found the isolated Op14 differential phase is **BOUNDED** (MSD slope ~0.10, Poincaré-recurrent, reversible dephasing forced by Ax3-losslessness, `energy_drift ~10⁻¹³`) — the bounded reversible dephasing measured **IS** this "reversible phase-scramble, not loss" statement. Status: **axiom-derived + check-corroborated.**

**The two PROPOSED-DEFINITIONAL items (walk-level, NOT axiom-derived; gated on the two-tank check, §2/§4):**

- ★ **PROPOSED-DEFINITIONAL #2 — entropy = lost phase information between clocks** (the coherence you can no longer read out, not energy you no longer have). *Not solid until measured.*
- ★ **PROPOSED-DEFINITIONAL #1 — temperature = the width of the clock-detuning distribution.** *Not solid until measured.*

## §2 — The two definitional items after the check fired (★#1 RE-GATED, ★#2 still PROPOSED)

Matching the docket Entry 14 ★#1 / ★#2. **The two-tank check has FIRED (PR #707, verdict `ADDITIVE-ARTIFACT`); the two items now diverge in status.**

**★ #1 — "temperature = clock phase-diffusion width/rate" — 🔴 DEMOTED to NOT-DEMONSTRATED-AS-POSED / RE-GATED (PR #707, 2026-07-15; prior PROPOSED text preserved below, Rule-12).**

> *(Prior status, preserved verbatim, Rule-12):* ★ #1 — "temperature = clock phase-diffusion width." PROPOSED-DEFINITIONAL — not solid until measured; consistent with the FDT anchor (a wider clock-detuning distribution = a hotter bath = more Johnson-Nyquist strain-noise) but not derived.

**Why demoted (the mechanism control killed it, not the naive bar):** the check's built-in Op14 kernel **ON/OFF** control showed the observed relative-phase diffusion is **additive wave-interference**, NOT the proposed `bath → A² → S → clock-rate` mechanism — the pure **linear** lattice (kernel OFF) reproduces the same diffusion. The mechanism attribution (**kernel-excess** $(V_{ON}-V_{OFF})/V_{ON}$) is **median 0.187 < the frozen `EXCESS_MIN` 0.50**, and **collapses to −0.001** when the bath is densified (per-`u` `{+0.02,−0.02,+0.02,−0.42}`) — densifying does not rescue it. The `D_ON(u)` log-log exponent is **p = 0.38** (sub-linear, already off the predicted $D\propto u^1$). The isolated-Op14 readout (spectrally rejecting the additive bath) is **BOUNDED** (MSD slope ~0.10) — reversible dephasing, forced by Ax3-losslessness. **The definition is NOT killed — it is RE-GATED:** a lossless kernel yields only bounded reversible dephasing; a genuine diffusion-**rate** thermometer needs **irreversibility**, which in AVE lives exactly in the **unbuilt F6 irreversible $\varepsilon\to T2$ depletion channel** (§4 flag; docket Entry 14 F6 convergence note). Cite PR #707 `analysis/two-tank-decoherence-check` (`research/2026-07-15_two-tank-decoherence-check_NOTE.md` §4).

**★ #2 — "entropy = lost phase information between clocks" — stays PROPOSED-DEFINITIONAL (UNTESTED by this check; same eventual gate).** Not solid until measured. The two-tank check tested the temperature/diffusion-rate leg only; the entropy definition awaits its own measurement (plausibly the same F6-gated irreversibility, since irreversibly-lost phase information is the entropy).

*(The heat = decoherence line, §1, is the separate one-axiom-derived statement — now check-corroborated — and is NOT part of this PROPOSED/re-gated pair.)*

## §3 — The three-phase-register unification (walk-record)

**One substrate energy, organized by phase.** The three registers are one energy budget read at three coherence grades:

| Phase register | Physical form | Measured as | Clock weight |
|---|---|---|---|
| **coherent-bound** | solitons (matter) | wall observables $\mathcal{M}/\mathcal{Q}/\mathcal{J}$ ([`boundary-observables-m-q-j.md`](boundary-observables-m-q-j.md)) | $\sqrt{S}$ |
| **coherent-propagating** | radiation | fields / the dress | $\sqrt{S}$ |
| **incoherent-propagating** | heat | clock decoherence (phase-diffusion width) | $\sqrt{S}$ |

**All three enter ONE clock-weighted ledger** — which is **why hot things weigh more with no extra postulate** (the incoherent energy is $\sqrt{S}$-weighted in the Komar integral exactly like the coherent energy). In this reading:

- **gravity = the phase-blind interaction** (the ledger counts energy at $\sqrt{S}$ regardless of its coherence grade);
- **the EM correction = dress-bound endpoint physics** (the path-participation asymmetry, `clm-ppasym`);
- **heat = the phase-noise floor** (the incoherent register).

## §4 — Registered checks (gates, not results)

> ★ **REGISTERED — two-tank decoherence check → FIRED 2026-07-15 (PR #707): verdict `ADDITIVE-ARTIFACT`.** **Simulation**, not a physical experiment (INVARIANT-S9): seed two identical soliton tanks + a random traveling bath; measure relative-phase variance growth vs bath energy density, with an Op14 kernel **ON/OFF mechanism control**. Result: the control (bath off) is machine-clean (`ctrl_span ~7–9×10⁻¹³` rad `≪` `CTRL_FLOOR` 1e-3; `energy_drift ~10⁻¹³`); the relative phase DOES diffuse (diffusive-shaped), but the diffusion is **kernel-independent** (kernel-excess median 0.187 `<` 0.50, collapsing to −0.001 on bath densification) ⇒ **additive wave-interference, NOT the Op14 bath→A²→S→clock mechanism**. ★#1 DEMOTED / RE-GATED on F6 (§2); the Ax3 line CORROBORATED (§1). Source: `research/2026-07-15_two-tank-decoherence-check_NOTE.md` §4.
>
> ⚑ **CRITERION UPGRADE (orchestrator adjudication, 2026-07-15 — Grant may veto).** The leaf's originally-registered bar — "a monotone variance-growth-vs-bath-energy relation confirms the definition" — is **INSUFFICIENT**: it **passes on the additive artifact** (the naive measurement met the bar; the mechanism control failed it). The criterion is therefore upgraded to **mechanism-gated**: confirmation requires **kernel ON/OFF excess ≥ threshold** (the frozen `EXCESS_MIN` 0.50), not merely diffusive shape. *Reasoning:* the looser variance-growth bar is the **unfireable-gate class** — a gate a spectator/additive artifact satisfies is not a gate. The mechanism-attribution (kernel-excess) is the discriminating observable. *(Adjudication recorded per flag-don't-fix; Grant's to ratify or veto.)*
>
> ★ **RECONCILIATION TARGETS owed IF the two definitions canonize (carried so ratification does not silently create manuscript-lockstep debt).** The manuscript already defines these words geometrically/mechanically; on ratification of the phase definitions these sites owe a reconciliation pass (today: **NEAR-SITE, no present contradiction** — the new defs are PROPOSED/no-claim, and deterministic geometric spreading is compatible with lost inter-clock phase information): `vol_3_macroscopic/chapters/11_thermodynamics_and_entropy.tex`:44,:68,:415,:416 (entropy = irreversible spherical FDTD spreading; temperature = RMS transverse-noise amplitude), `vol_3_macroscopic/chapters/12_ideal_gas_law_and_fluid_pressure.tex`:34 (temperature = RMS displacement-current-noise amplitude), `vol_3_macroscopic/chapters/13_geophysics.tex`:156 (temperature = kinetic energy per node DOF). The RMS-noise framing is arguably the bath-side twin of the clock-detuning width.

> ★ **REGISTERED — thermal-ledger consistency note.** The incoherent (heat) energy enters the Komar integral at the **same $\sqrt{S}$ weight** as coherent energy (`clm-3zz0f6`; the RULED-(c) `komar_weight`, Ruling 1, `src/ave/gravity/backreaction.py`). **Consistency-class** — GR does likewise (all stress-energy gravitates, thermal included); this is not an AVE-distinct chord, it is the AVE reading of a standing GR fact.

## §5 — Open walk (named, not walked)

The **core-holding blob** is a candidate first sighting of **"phase-organization without circulation — coherent but not winding"** — a *dynamical* (puddle) rather than *topological* (soliton) binding. See the docket **Entry 15** (the core-holding blob walk; the (A) linear-mode-sorting vs (B) nonlinear-self-trapping fork, discriminating ablation IN FLIGHT). If the blob is a genuine puddle, it would be the first clean member of a fourth phase-organization class (coherent-bound-without-winding), between the coherent-bound soliton and the coherent-propagating field. **Named, not walked here** — routed to the census Stage-2 design and Grant.

## §6 — Status recap + what is NOT claimed

- **The whole leaf is WALK-LEVEL / consistency-class or below**, except the one Ax3-derived line (heat = decoherence, not dissipation) — now **axiom-derived + check-corroborated** (PR #707: the bounded reversible dephasing measured IS that statement).
- **No numerical value is promoted**; the mean-shift half rides the definitional δ_strain residual, the variance half rides FDT, both already in canon.
- **Post-check status of the two definitions (§2):** ★#1 "temperature = phase-diffusion width/rate" is **DEMOTED / RE-GATED on the unbuilt F6 irreversible $\varepsilon\to T2$ channel** (PR #707 verdict `ADDITIVE-ARTIFACT` — the diffusion is kernel-independent additive interference; a lossless kernel gives only bounded reversible dephasing). ★#2 "entropy = lost phase information" **stays PROPOSED** (untested by this check, same eventual F6-class gate). The registered criterion is upgraded to mechanism-gated (kernel ON/OFF excess ≥ 0.50; §4, orchestrator adjudication, Grant-vetoable). The thermal-ledger note (§4) is consistency-class, GR-degenerate; the manuscript reconciliation-target sites (§4) are carried so a future ratification does not silently create lockstep debt.
- **No AVE-distinct chord is claimed** — hot-things-weigh-more is the AVE reading of a standing GR fact, not a new prediction.

## Cross-references

- [`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md) §4 — the δ_strain (TCC) and Johnson-Nyquist (thermal-noise-floor) rows this leaf's mean/variance split rides; and the new "heat = clock phase-diffusion" row (PROPOSED).
- [`translation-tables/translation-stochastics.md`](translation-tables/translation-stochastics.md) — FDT as boundary-$Z$ thermalization (the variance / heat-content anchor).
- [`../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) — δ_strain / Q-DELTA-MAP-1 (the mean-shift / thermal operating point; `clm-hp7nlm`).
- [`envelope-anatomy.md`](envelope-anatomy.md) — the $\sqrt{S}$-clock-weighted ledger (path-participation asymmetry `clm-ppasym`) the three registers share.
- [`statistics-under-ave.md`](statistics-under-ave.md) — entropy / randomness under AVE (emergent coarse-graining over a deterministic substrate); the worked δ_strain Cosserat thermal-mode instance.
