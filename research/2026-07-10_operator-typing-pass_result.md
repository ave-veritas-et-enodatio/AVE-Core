# X35 — Universal-Operator Typing Pass (result)

**Date:** 2026-07-10 · **Branch:** `analysis/x35-operator-typing` · **PR:** [REVIEW: pending-orchestrator]
**CLASS: registry hygiene + candidate-generation. NOT physics claims.** This pass adds four latent type-axes
(exposed by today's #595/#606/#607 arcs) to the universal-operator registry and produces the GAP TABLE that
tells us *where the predictions hide*. It mints no proposition: every typing either (a) reads a formula already
in [`operators.md`](../manuscript/ave-kb/common/operators.md) §2, (b) cross-references a walked-framing note
**cited as FRAMING, not canon**, or (c) is flagged AMBIGUOUS for Grant rather than silently resolved. The
opener of the collapse-target sweep.

**Provenance of the axes (all today, all FRAMING until their own gates run):**
- **RATING TYPE (swing/slew)** — the slew identity, FPB-corner walked-framing note
  ([`2026-07-09_highE-carrier-fpb-corner_walked-framing.md`](2026-07-09_highE-carrier-fpb-corner_walked-framing.md)
  §5, **PR #595 UNMERGED — framing**), pointer already carried in
  [`lattice-model-register.md:86-93`](../manuscript/ave-kb/common/lattice-model-register.md): "the two ratings
  of one amplifier" — output-swing (ε-kernel $S(A)=\sqrt{1-A^2}$, cap $E\le E_c$) vs slew-rate (μ-kernel keyed
  on $A_I=\dot E/(E_c\omega_0)$, cap $\dot E\le E_c\omega_0$), meeting at the FPB corner $(\omega_0,E_c)$.
- **AXIS OF ACTION (amplitude/frequency/topology)** — the K4-graph/srs-embedding 2×2
  ([`lattice-model-register.md`](../manuscript/ave-kb/common/lattice-model-register.md) Axis A: graph =
  *topology*, frequency-blind AND amplitude-blind, owns winding/Link∈ℤ; embedding = *frequency/scales*, owns
  $\omega_0$, band edge, dispersion) crossed with Axis B (the *amplitude* kernel). Plus the x29 category-error
  lesson ([`2026-07-09_superband-carrier-fork_result.md:162-175`](2026-07-09_superband-carrier-fork_result.md):
  the amplitude-exponent question and the frequency band-top question are DISTINCT axes and must not be conflated).
- **BC-vs-DYNAMICS + settled-sector** — the fast-sector-settling walked-framing note
  ([`2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md`](2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md),
  settling frame per **#606, FRAMING**): "a boundary condition in AVE is the time-averaged settled state of a
  faster channel." BC-implementing operators get a *cross-reference* annotation naming which fast sector settles
  them. The annotation is a cross-reference, **not a canonization**.
- **CLOCK TYPE (Op5 only)** — synchronous-universal-tick vs per-channel-continuous; marked **PENDING-X33** (the
  discriminator running in parallel in the sweep). **Not resolved here.**
- **SECTOR (A1/T2/V)** — standing ownership column, made explicit per operator where intrinsic; marked
  *sector-agnostic* where the operator applies per-invocation.

Precedent for adding an orthogonal axis to a shared registry:
[`temporal-saturation-regime-classifier.md`](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md)
added the temporal $\delta_{\text{AVE}}$ axis to the same kernel catalog the same way (cross-reference per row,
no rewrite). This pass extends the spirit of the §4.5 EE Analytical Tool Tracker
([`translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) §4.5).

---

## §1 — The full typed table (22 operators × 5 axes)

RATING: **swing** = amplitude-keyed ($S(A)$ / output-swing rating) · **slew** = rate-keyed ($A_I=\dot E/(E_c\omega_0)$
/ slew-rate rating) · **neither** = not a saturation-limit operator.
AXIS OF ACTION: **amp** (amplitude/kernel) · **freq** (frequency/spectrum/dispersion/cutoff/band-edge) · **topo**
(winding/counting/Link) · **—** (differential/network/impedance-invariant, none of the three cleanly).
BC/DYN: **dyn** = dynamics operator · **BC** = boundary-condition operator (settled-sector in parens, FRAMING).

| Op | Name (short) | SECTOR | RATING | AXIS | BC/DYN (settled-sector, FRAMING) | CLOCK |
|---|---|---|---|---|---|---|
| Op1 | Impedance $Z=\sqrt{\mu/\varepsilon}$ | cross (embedding value) | neither | — (impedance invariant) | dyn (the ratio both ratings ride) | — |
| Op2 | Saturation $S(A)=\sqrt{1-(A/A_c)^2}$ | sector-agnostic kernel | **swing** | **amp** | dyn; its $S\to0$ event WRITES the $\Gamma=-1$ BC | — |
| Op3 | Reflection $\Gamma$ | boundary (agnostic) | neither | amp (impedance ratio) | **BC** (T2 wall = settled fast T2 self-interference; §(d) note) | — |
| Op4 | Pairwise Potential $U(r)$; $Z(r)$ | cross | **swing** ($Z(r)$ form) | amp (+topo via $T^2{-}\Gamma^2$) | dyn | — |
| Op5 | Multiport Y→S $[S]$ | cross (network) | neither | — (network) | dyn | **PENDING-X33** |
| Op6 | Eigenvalue target $\lambda_{min}\to0$ | cross | neither | freq (mode) | dyn (mode-selection) | — |
| Op7 | Spectral analyser (spatial FT) | cross | neither | **freq** | dyn | — |
| Op8 | Packing Reflection $\Gamma_{pack}$ | cross | neither (reflection) | amp ($R_g$) | **BC** (A1 packing/steric settled — *thin, candidate*) | — |
| Op9 | Steric Reflection $\Gamma_{steric}\to-1$ | cross (Pauli overlap) | neither (reflection) | amp (overlap) | **BC** ($\Gamma{=}{-}1$ wall = settled overlap channel — *thin, candidate*) | — |
| Op10 | Junction Loss $Y_{loss}$; $c{=}3$ | **T2** ((2,3) winding) | neither | **topo** (crossing count) | dyn (topological invariant) | — |
| Op11 | Topological Curl $\nabla\times V$ | T2/B | neither | — (differential, topo-adjacent) | dyn | — |
| Op12 | Topological Divergence $\nabla\cdot V$ | A1/E | neither | — (differential, topo-adjacent) | dyn | — |
| Op13 | D'Alembertian $\Box^2$ | cross | neither (rides Op16 $c_{eff}$) | **freq** (wave/dispersion) | dyn | — |
| Op14 | Dynamic Impedance $Z_{eff}=Z_0/\sqrt S$ | A1-bulk → V/EM net | **swing** | **amp** | **BC-adjacent**: settled $S(A)$ = graded-index BC fast waves see (A1→V; note §(a) #1) | — |
| Op15 | Virtual Strain Radius $r_{v}=\sqrt{1-\sigma^2}$ | A1 (strain) | **swing** | amp ($\sigma$) | dyn | — |
| Op16 | Wave Speed $c_{shear}=c_0\sqrt S$ | **T2/shear** | **swing** | **freq** (amp-KEYED, freq-ACTING) | **BC** (cutoff; A1-bulk settled $S$ sets fast-wave clock $\omega_{loc}=\omega_g\sqrt{1{-}A^2}$) | — |
| Op17 | Power Transmission $T^2=1-\Gamma^2$ | boundary (agnostic) | neither | amp (power) | **BC** (transmission across settled $\Gamma$ wall) | — |
| Op18 | Coupled Frequency $\omega_c=\omega_0/\sqrt{1-\lambda k}$ | cross | neither (kernel-shaped in $\lambda k$) | **freq** | dyn | — |
| Op19 | Refractive Index $n(r)=1+\nu_{vac}\varepsilon_{11}$ | A1 (dilatation) | swing-small-signal (linear-in-$\varepsilon_{11}$) | amp→freq (graded index) | **BC** (settled A1 strain = index fast light sees; note §(a) #1) | — |
| Op20 | Regime Eigenvalue $\omega_{regime}$ | cross | neither | **freq** (regime target) | dyn (regime boundary) | — |
| Op21 | Quality Factor $Q=\ell$ | **T2/V** (tank modes) | neither | **topo** (mode counting) | **BC** ($Q=\ell$ derived at $\Gamma{=}{-}1$ TIR wall; fast T2 winding settles the wall) | — |
| Op22 | Avalanche $M=1/S^2$ | sector-agnostic | **swing** | **amp** | dyn (nonlinear cascade) | — |

Notes: Op15/Op18/Op20 are SYNTHESIS-labelled operators in `operators.md` §2 (single-citation or narrative-only);
their typing inherits that provisional status. Op20's formula is A43-v10-flagged. Op22 uses the canonical
$M=1/S^2$ (A43-v11), not the doc-81 $1/(1-S)$.

---

## §2 — THE GAP TABLE (the interesting part)

Where predictions hide, ranked. G1 is the headline.

| # | Gap | Evidence | Candidate (NOT a claim) |
|---|---|---|---|
| **G1** | **The entire Op1–Op22 registry is SWING-typed. There is NO slew-typed operator.** Every rating-bearing operator (Op2, Op4, Op14, Op15, Op16, Op22) is amplitude-keyed. | The slew-rating kernel $S_B=\sqrt{1-A_I^2}$ / relativistic-inductor $L_{eff}(I)=L_0/\sqrt{1-(I/I_{max})^2}$ IS canonical ([`relativistic-inductor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md), `clm-p5cf3t`) — "the varactor equation with $V\to I$, projections of the single Axiom-4 kernel onto electric and magnetic sectors" — but it is **UN-NUMBERED** and has **no cross-scale catalog**. | Number the slew-rate kernel (an "Op23-class" Universal Slew-Rate / Relativistic-Inductor operator), the μ-side dual of Op2. |
| **G2** | **Saturation-kernel catalog: 26 swing instances, 0 slew instances.** | [`universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md): all 26 rows key on an amplitude ratio $A/A_c$ (voltage, field, strain, $T/T_c$, …). None keys on a rate $\dot A$. | Build the slew-instance catalog. "Relativistic mass" (the $L(I)$ instance) is the *one* slew instance and is currently hiding among the swing rows — pull it out; then ask which of the other 25 have a rate-keyed sibling. |
| **G3** | **Op14 (swing $Z_{eff}=Z_0/\sqrt S$) slew-dual = $Z_{eff}$ via $L_{eff}(I)$ — present but not an Op.** | The μ-side dynamic impedance lives in the relativistic-inductor leaf and the asymmetric-Meissner $Z_{eff}=Z_0\sqrt{S_\mu/S_\varepsilon}$ (`operators.md:54`), but is not consolidated as the slew-dual of Op14. | Consolidate the μ-side dynamic impedance as Op14's slew-dual. |
| **G4** | **Op16 (swing $c_{shear}=c_0\sqrt S$) has no slew-dual.** | No rate-keyed wave-speed operator in the registry. | Does a $\dot E$-keyed propagation-speed limit exist (a slew-side companion to the S-keyed $c_{shear}$)? |
| **G5** | **Op22 (swing avalanche $M=1/S^2$) has no slew-dual.** | No rate-keyed avalanche/breakdown operator. | Is there a $dV/dt$-triggered avalanche (a slew-rate breakdown) distinct from the amplitude-breakdown $M=1/S^2$? (dV/dt-triggered latch-up is the EE analog.) |
| **G6** | **Op5 clock is UNTYPED (PENDING-X33).** The only clock-bearing operator. | `k4_tlm.step()` runs `_scatter_all()` → `_connect_all()` as one global sweep (`k4_tlm.py:461-465`) — a *synchronous* sweep in the *implementation*; whether that encodes a physical synchronous-universal-tick or masks a per-channel-continuous clock is exactly X33's discriminator. | Do not resolve — X33 running in parallel. |
| **G7** | **BC operators previously carried no settled-sector attribution.** Op3, Op8, Op9, Op16, Op17, Op21 all implement boundary conditions. | Before X35 none was cross-referenced to *which fast channel settles it*. Now annotated (col 6). Op8/Op9 attributions are THIN (the "overlap/packing channel" that settles the steric wall is not named in-corpus). | Name the fast channel behind the Op8/Op9 steric walls (candidate; feeds the settling-frame derivation). |
| **G8** | **Axis-of-action mismatch in usage: amplitude-keyed but frequency-acting.** Op16 ($c_{shear}$) and Op19 ($n(r)$) are keyed on an amplitude (S, $\varepsilon_{11}$) but ACT on a frequency-domain observable (wave speed / dispersion / index). | The *keyed variable* and the *acted-on axis* differ — exactly the x29 category-distinction (do not conflate amplitude-axis with frequency-axis). Not a bug; a category to track. | Convention decision (see AMBIGUOUS A2). |

**Reading.** The single biggest gap is not a missing instance — it is a missing *rating*. The registry has fully
mapped the vacuum's **output-swing** rating (Op2 + a 26-instance catalog) and has left its **slew-rate** rating
essentially un-catalogued, present only as one un-numbered leaf ($L_{eff}(I)$). If the slew identity survives its
derivation gate (task #29), the un-built slew catalog is where an entire parallel family of saturation predictions
(rate-triggered, not amplitude-triggered) is currently hiding — G1/G2 are the collapse-sweep's first named target.

---

## §3 — AMBIGUOUS (for Grant — flag-don't-fix, not resolved here)

| # | Ambiguity | The two readings | Why it can't be silently resolved |
|---|---|---|---|
| **A1** | **Is swing/slew the SAME axis as ε/μ, or orthogonal to it?** | (i) FPB note §5: swing = *ε-kernel*, slew = *μ-kernel* — a 1:1 identification. (ii) The catalog's ASYM-N(μ) BCS row ($B_c(T)=B_{c0}\sqrt{1-(T/T_c)^2}$) is amplitude-keyed = **swing**, yet lives in the **μ-sector** — so swing/slew looks ORTHOGONAL to ε/μ (a 2×2: swing-ε, swing-μ, slew-ε, slew-μ). Code: `cosserat_field_3d.py:612-613` gives S_mu and S_eps both the *same* $\sqrt{1-A^2}$ swing form. | The FPB 1:1 identification and the catalog's own μ-sector-swing row directly contradict. Picking one silently would either wrongly relabel BCS as slew or wrongly forbid a slew-ε instance. **Grant's ε↔μ / swing↔slew ruling gates G1's numbering.** |
| **A2** | **Op16 / Op19 primary axis of action: the keyed variable or the acted-on observable?** | (i) amplitude (they are keyed on S / $\varepsilon_{11}$). (ii) frequency (they act on wave-speed / index / dispersion). | Convention choice that decides how the whole registry is indexed on Axis-of-action. The x29 lesson says the two must not be conflated — so the convention must be *stated*, not defaulted. |
| **A4** | **Is the relativistic-inductor $L(I)$ literally the FPB slew kernel $S_B(A_I)$, or merely its dual?** | (i) Identical: displacement current $I=C\dot E$, so keying on $I/I_{max}$ IS keying on the normalized rate $A_I$. (ii) Distinct: $L(I)$ keys on current *amplitude* (= velocity), while $A_I$ keys on the *slew*; the engine keys $L_{eff}$ on **V** (amplitude) yet applies it to **$\dot V$** (`cosserat_master_equation_fdtd.py:19-20,144,238`: $\Phi_{link}=L_{eff}(V)\cdot C\dot V$) — a mixed keying in USE. | Whether they are one kernel or a dual pair decides whether G1 numbers ONE slew-operator or a swing/slew pair — and the engine's mixed V-keyed/$\dot V$-applied inductor shows the corpus has not settled it. **Grant's physical ruling.** |
| **A5** | **Op8/Op9 settled-sector: which fast channel settles the steric/packing $\Gamma$ wall?** | (i) A named Pauli-overlap / packing channel (analog of the electron's T2 self-interference). (ii) No fast sub-channel — the steric wall is a bare $\Gamma\to-1$ divergence, not a settled interference pattern. | The settling-frame note (#606) claims BCs are settled fast states; if Op8/Op9 have no fast settling channel, that is a scope-limit on the settling frame worth surfacing, not papering over. |
| **A3** | **Op1 ($Z$) rating type: "neither" or "the meta-rating pivot"?** (minor) | (i) neither (it is not a saturation limit). (ii) $Z$ is the axis both ratings pivot on (swing caps E, slew caps $\dot E$, both at fixed $Z$) — a meta-rating, not "neither". | Minor labelling; noted so the "neither" is not read as "irrelevant to ratings" (it is the *shared* quantity). |

---

## §4 — Kernel-catalog RATING typing (26 swing / 0 slew)

All 26 instances of the Universal Saturation-Kernel Catalog are **SWING**-typed: each keys the kernel
$S(A)=\sqrt{1-A^2}$ on an *amplitude* ratio $A/A_c$ (dielectric $V/V_{snap}$, BCS $T/T_c$, strain/yield, MOND
$g_N/a_0$, $2GM/c^2r$, …). **Zero** instances key on a *rate* $\dot A$. The slew-rating dual kernel —
$L_{eff}(I)=L_0/\sqrt{1-(I/I_{max})^2}$ (relativistic inductor, `clm-p5cf3t`) — has no row. This is G2: the swing
catalog is complete-looking (26 rows, 21 OOM); the slew catalog is *empty*.

Crucially, the swing/slew RATING axis is **orthogonal to the existing ε/μ SECTOR axis** of the catalog (see A1):
the ASYM-N(μ) BCS row is swing-in-μ, and code gives S_mu/S_eps the same swing form. The kernel-catalog KB edit
therefore records the RATING axis as orthogonal (not a re-labelling of ε/μ) and flags the FPB 1:1 identification
as AMBIGUOUS-for-Grant, per flag-don't-fix.

---

## §5 — USE-verification (verify-before-cite: grep of high-traffic call sites)

Typings checked against operative code, not just formulae:

- **Op2 swing / amp** — `cosserat_field_3d.py:413,473` `S = jnp.sqrt(1.0 - A_sq_clipped)  # Op2 saturation`; ε/μ
  split `:612-613` (S_mu, S_eps both swing form) → confirms swing + supports A1 (rating ⊥ sector).
- **Op14 swing / amp** — `cosserat_field_3d.py:414` comment `# Op14 dynamic impedance Z_eff = Z_0 / sqrt(S)`.
- **Op22 swing / amp** — `scale_invariant.py:522` `avalanche_factor(...)`; `:183` `C_eff = 1/S → ∞ (diverges)` →
  confirms amplitude-triggered divergence (swing).
- **Op5 clock** — `k4_tlm.py:461-465` `step()` = global `_scatter_all()`→`_connect_all()` sweep → the
  synchronous-*implementation* fact behind PENDING-X33 (physics unresolved).
- **Slew side in USE** — `cosserat_master_equation_fdtd.py:19-20,144,238`: $\Phi_{link}=L_{eff}(V)\cdot I$,
  $I=C\dot V$ → the inductive/μ term carries the RATE ($\dot V$) but keys $L_{eff}$ on **V** (amplitude). This
  mixed V-keyed/$\dot V$-applied inductor is the direct engine evidence behind A4.

No operator-number corrections required; all Op# match `operators.md` §2.

---

## §6 — KB edits made + files touched

- **`manuscript/ave-kb/common/operators.md`** — new compact section **§3.5 "Operator type-axis annotations
  (X35, 2026-07-10)"** (Op#-keyed table, same convention as the §3 implementation-pointers table), CLASS-tagged,
  framings cited as framings, X33 pending, GAP+AMBIGUOUS pointers to this doc.
- **`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`** — short **RATING-TYPE (swing/slew)
  annotation** subsection: 26 swing / 0 slew; slew-dual = $L_{eff}(I)$ (un-catalogued, G2); RATING ⊥ ε/μ; FPB
  1:1 identification flagged AMBIGUOUS (A1).
- **This research doc.**
- **Not touched:** `translation-circuit.md` §4.5 (this pass extends its spirit but adds no row); its vol4/vol2
  copies are pure redirect stubs (no mirror needed). `operators.md` and the kernel catalog have single copies
  in `common/` (no secondary-copy mirror).

## §7 — What this is NOT

Not a physics claim. Not a canonization of the slew identity, the settling frame, or any swing/slew duality —
those remain FRAMING pending their own gates (#595 slew, #606 settling, task #29 UV-completion). Not a resolution
of Op5's clock (X33). Not a numbering of any new operator (G1 is a *candidate*). The AMBIGUOUS items go to Grant
un-resolved. This is registry hygiene: four columns and a map of the holes.
