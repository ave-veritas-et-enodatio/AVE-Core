# The anisotropy observable — FEASIBILITY SCOPING (two axes): GW-band sky pattern + gravitational photoelasticity

> **★ SCOPE FENCE, STATED FIRST AND BINDING ON EVERY LINE BELOW.** This lane is **SCOPING, not
> derivation and not measurement.** No solver was run. No engine file was touched. No corpus file
> was modified. **No claim was minted, no solidity was changed, no magnitude is asserted without a
> named derivation-path, and the outcome bins in §1.9 / §2.8 are explicitly NOT FROZEN** — freezing
> happens in a separate pre-reg at fire time, after the Grant walk (§3). Every number that appears
> below is either (i) a verbatim read of an already-merged shipped artefact, cited file:line, or
> (ii) arithmetic on such reads, labelled as arithmetic and receipted two ways in Appendix B.
> Arithmetic-on-banked-numbers is **not** a result of this lane.

**Provenance.** Frontier tracker item 21 —
[`_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md`](../_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md)
§21 (*"The anisotropy observable — direction-dependent long-wave P-speed of a single-crystal
vacuum (⚑ OPEN frontier candidate, 2026-07-28; NOT fired)"*), itself routed from the merged **#802**
SUBC/KUBC lane's §6.5 measurement plus the 2026-07-28 orchestrator leak-audit fold (docket
`ENTRY 2026-07-28-leak-audit-carves`).

**The second axis is a Grant fold** (2026-07-31, verbatim `[sic]`: *"fold"*), from his question,
verbatim `[sic]`: *"isn't gravity just macroscopic static strain including e and b field? so vacuum
birefringence? if AVE is right?"* Axis 2 scopes exactly that: **gravitational photoelasticity**.

---

## §0 — SECTOR DECLARATION (mandatory header, before any standard-physics word)

| | **AXIS 1 — GW-band sky pattern** | **AXIS 2 — gravitational photoelasticity** |
|---|---|---|
| **Which sector?** | Translational Cauchy grade of the srs-z3 net; the **shear ($T_2$) branch** is the observed-GW channel per the Q1-revert, the **$A_1$ dilatation / P-branch** is the compression carrier | **$T_2$ transverse EM** (the probe photon) propagating **through** a graded $A_1$-dilatation + $T_2$ static strain field (the gravitational DC bias) |
| **Does the engine carry that DOF?** | YES — the rank-4 elastic tensor $C_{ijkl}$ is measured node-up on srs-z3 by two independent merged lanes (#506 Born + long-wave slopes; #802 SUBC/KUBC homogenization) | **PARTIALLY.** The engine carries the cold photon branches node-up (#515) and carries a static strain state (#779/#796), but the corpus has **no measured photoelastic coupling tensor** $p_{ijkl}$ — see §2.4. That absence is the scoping finding, not a gap to paper over. |
| **Cold or saturated?** | Both live. #506/#802 measure **COLD** (uncaged reference) and cold-plus-cage. The gravitational band is a **weak-DC-bias** regime ($A \ll 1$), so the cold tensor is the right leading term. | **Weak DC bias on a cold lattice.** Gravitational $A = \varepsilon_{11} = 7GM/c^2r$ is $\sim10^{-9}$ at the solar limb — deeply sub-yield. NOT the R2 varactor regime the flagship falsifier lives in. |
| **Coordinates (A46)** | **Real-space / spatial-Brillouin.** Both the corpus claim (direction-dependent $c(\hat q)$ against cosmically-fixed lattice axes) and the measurement (acoustic slopes vs $\hat q$) are real-space directional. No phase-space mismatch. | **Real-space / spatial-Brillouin** for the index tensor; the observable (accumulated ellipticity) is a **phase** quantity read on the polarization 2-plane. Matched. |
| **Regime / phase-state** | Regime I (deeply linear), lossless-reactive, cold single crystal, no grains | Regime I, sub-yield, lossless-reactive; the strain is **static DC**, the probe is **AC optical** |

**A1 ⊥ T2 discipline note.** Axis 1 asks about **two different branches** and does not merge them:
the P-branch is $A_1$ dilatation (mass sector), the shear branch is $T_2$ (the observed-GW channel,
[`port-register.md`](../manuscript/ave-kb/common/port-register.md):48 row 2). The tracker's item-21
title says *"P-speed"*; **the observed GW channel is SHEAR**, so this lane reports both branches
separately and does not let the title's word pick the sector.

---

## §1 — AXIS 1: the gravitational-band anisotropy

### §1.1 — What #802 actually measured (the tracker's basis, verified verbatim)

[`research/2026-07-28_subc-kubc-bracket_result.md`](2026-07-28_subc-kubc-bracket_result.md):13, verbatim:

> *"This medium is **CUBIC, not isotropic.** Measured Zener anisotropy of the cold uncaged reference
> at `L = 16`: `A = C44/C′ = 1.330402` (SUBC) and `1.605316` (KUBC) — far from the isotropic
> `A = 1`. **A cubic medium therefore has no single 'longitudinal modulus': it is
> direction-dependent.**"*

Axis alignment is MEASURED two ways that see `Phi` (`:301`, `:303`): a direct uniaxial `C11` probe
agreeing with the assembled `K + 4C′/3` to rel `9.58e-11` (a cubic identity that holds *only* if
`[100]` is an elastic axis), plus the KUBC reaction-stress structure returning `Σ₂₂ = Σ₃₃` to rel
`5.16e-09` (the cubic `C12 = C13` signature). The first version's axis-alignment evidence was
withdrawn as a non sequitur and REPLACED; the replacement is sound.

### §1.2 — The structural carve the question turns on: rank-2 vs rank-4

Cubic point-group symmetry forces a **rank-2** material tensor (a scalar $\varepsilon$, a scalar
$\mu$, a scalar conductivity) to be **isotropic** — one number, no direction dependence, exactly.
It does **not** force a **rank-4** tensor to be isotropic: a cubic $C_{ijkl}$ has **three**
independent constants ($C_{11}, C_{12}, C_{44}$), and isotropy is the extra one-parameter condition
$C_{44} = (C_{11}-C_{12})/2$, i.e. Zener $A = 1$. A cubic crystal with $A \neq 1$ has genuinely
direction-dependent long-wave elastic-wave speeds **at zeroth order in $k$** — this is not a
$(q\ell_{node})^n$ dispersion correction and is **not** suppressed by the corpus's standing
quartic-suppression defence.

★ **This distinction is load-bearing and is where the standing emergent-Lorentz argument does NOT
reach.** [`preferred-frame-and-emergent-lorentz.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md):48
argues *"$q^4$ | $q_x^4 + q_y^4 + q_z^4$ | **first anisotropic invariant for cubic**"*. That
statement is about the **dispersion correction** — the deviation of $\omega(k)$ from linear. The
Zener anisotropy is a direction dependence of the **slope itself**, at $k\to0$. The two are
different objects and the quartic argument does not cover the second one. **Whether the corpus has
ever conflated them is a question for the auditor lane, not a finding this lane lands.**

### §1.3 — (a) Does the lattice-scale anisotropy survive to the long-wave limit? ★IT IS ALREADY MEASURED, AND THE ANSWER IS OPERATING-POINT-DEPENDENT

**★ F-A1 — the corpus already contains the direction-resolved long-wave answer, and the item-21
flag did not consult it.** Merged **#506**
([`research/2026-07-04_srs-elastic-tensor_result.md`](2026-07-04_srs-elastic-tensor_result.md)) ships
a **per-direction acoustic-slope table** at §4 (`:186`–`:199`) — *"the deliverable Born-Huang table"* — computed
from the $k\to0$ acoustic branches of the SAME chiral srs-z3 net, cross-validated against an
independent direct eigensolve (`:112`, verbatim: *"An **independent direct-eigensolve** of the
small-k acoustic branches along [100] recovers the same C11=0.72786, C44=0.24876 at ρ*=9.77 —
cross-validating the long-wave method"*). So **the long-wave limit is where these numbers already
live**: they are $\rho c^2 = \rho(\omega/k)^2$ eigenvalues, not lattice-scale moduli awaiting a
long-wave extrapolation.

Shipped table at $\rho^\ast = 9.7734$ (the $\nu=2/7$ / $K=2G$ point), `:191`–`:195`, verbatim values:

| Direction | T (low) | T (mid/high) | L |
|---|---|---|---|
| `[100]` | `0.24876` | `0.24876` | `0.72786` |
| `[110]` | `0.20235` | `0.24876` | `0.77426` |
| `[111]` | `0.21782` | `0.21782` | `0.78973` |

And `:197`, verbatim: *"The directional split of the transverse slopes ([100]_T = 0.2488 vs
[110]_T1 = 0.2024 vs [111]_T = 0.2178) **IS the Zener anisotropy** (A = 1.229), direction-resolved."*

**★ F-A2 — the answer FORKS on the bond-stiffness operating point $\rho_{bond} = k_a/k_s$, and the
corpus carries BOTH points as live.** From the same #506 table (`:122`-`:135`):

| Operating point | Zener $A$ | Direction dependence of the long-wave speeds | Mechanical status (#506 `:125`, `:135`) |
|---|---|---|---|
| $\rho_{bond} = 1$ (**iso-bond**) | **`1.000`** | **ZERO** — `:197`–`:198` verbatim: *"At the iso-bond point (ρ=1) all directions collapse to 0.17678 (A=1, but K<0 unstable)"* | $K = -0.0589$ — **NEGATIVE**, mechanically unstable |
| $\rho^\ast = 9.7734$ (**matter point**) | **`1.229`** | direction-resolved, §1.3 table | $K = +0.4308$, stable |

And the corpus states the fork explicitly. [`achromatic-impedance-matching.md`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md):33,
verbatim:

> *"(Honest flag, mirrored from the source: the elastic $\rho_{bond}=1$ match is a
> **lossless-reactive photon operating point** — $K<0$, mechanically **unstable** per the
> `srs-elastic-tensor` result ($K<0$ for $\rho<2$) — **not** a stable static elastic solid; the
> matter sector sits at a different, mechanically-stable $\rho^\ast$.)"*

**⇒ Item 21's physics question REDUCES to an already-open corpus fork.** *Which operating point does
the gravitational-band (shear / $T_2$) channel ride?* If it rides $\rho_{bond}=1$, the long-wave
anisotropy is **exactly zero by construction** and there is no observable. If it rides
$\rho^\ast$, the anisotropy is the #506 table and is large (§1.4). **This lane does not pick, and
no default is admissible.** It is Grant walk-question **W1** (§3).

### §1.4 — The magnitude IF the shear channel rides $\rho^\ast$ (arithmetic on merged numbers; NOT a prediction)

> **Class: arithmetic-consistency observation on already-merged shipped numbers. NOT a derivation,
> NOT a claim, NOT a magnitude assertion for item 21.** It exists to answer "is this observable at a
> level anything could see, or is it 20 OOM below every bound?" — the feasibility question this lane
> was chartered to answer. It is conditional on W1 answering "$\rho^\ast$", which is open.

Solving the cubic Christoffel eigenproblem $\Gamma_{ik}(\hat n) = C_{ijkl}\hat n_j \hat n_l$ on the
shipped $C_{11}, C_{12}, C_{44}$ over a 400×800 direction sphere (Appendix B, method 2):

| Branch | $c(\hat n)$ range (lattice units, $\rho=1$) | max/min | fractional spread |
|---|---|---|---|
| **L (P / $A_1$-adjacent)** | `[0.85317, 0.88873]` | `1.0417` | **`4.08 %`** |
| **T-fast (shear)** | `[0.46688, 0.49880]` | `1.0684` | `6.61 %` |
| **T-slow (shear, the observed-GW branch)** | `[0.44983, 0.49880]` | `1.1088` | **`10.32 %`** |
| **shear SPLITTING at one direction** (acoustic birefringence, max at `[110]`-class) | — | — | **`10.32 %`** |

Two things follow, both stated flatly and neither adjudicated:

1. **The anisotropy is LARGER on the shear branch than on the P branch** (`10.3 %` vs `4.1 %`).
   The tracker item is titled *"direction-dependent long-wave **P**-speed"*; the sector-honest
   reading is that **the observed-GW channel is the branch with the bigger effect**, not the smaller
   one. Sector-ownership correction, surfaced.
2. **There is a second observable the tracker does not name: shear-mode SPLITTING.** Along a
   `[110]`-class direction the two shear polarizations travel at speeds differing by `10.3 %` —
   i.e. **acoustic birefringence of the gravitational-band channel**, a *polarization*-resolved
   observable distinct from the sky-pattern *speed* observable. If the GW channel rides $\rho^\ast$
   this is arguably the sharper axis, because LIGO/Virgo measure the two GW polarizations directly.

**Honest ceiling on both:** these are lattice-unit ratios at $\rho^\ast$ with $\rho$ (density)
direction-independent, so the ratios are normalization-free. **They are not a prediction until W1
is answered and until the $c_{shear} \equiv c$ identification (`port-register.md:48`) is reconciled
with a direction-dependent $c_{shear}$** — see §1.5.

### §1.5 — ★ F-A3: the corpus's inter-channel speed ratios ride an ISOTROPIC average of a medium now measured cubic (FLAG, not fixed)

[`port-register.md`](../manuscript/ave-kb/common/port-register.md):48–51 canonizes four channel
speeds: photon $c = \sqrt{G/\rho}$; shear GW $c_{shear} = c$; bulk PORT $\sqrt2\,c$; bulk RADIATIVE
$\sqrt{10/3}\,c \approx 1.83c$. [`research/2026-07-19_deep-space-band-map_derivation.md`](2026-07-19_deep-space-band-map_derivation.md):207
states these are *"[derived from `K = 2G`]"*.

$K$ and $G$ are the **two constants of an ISOTROPIC solid**. A cubic solid has **three**. Reducing
$\{C_{11},C_{12},C_{44}\}$ to $\{K, G\}$ requires an averaging choice, and #506 names it: `:147`,
verbatim — *"So 'a single ν' is a Voigt/Reuss/Hill averaging choice, not a bare lattice output (the
[ANISOTROPIC-BREAKDOWN] condition)."* The **Hill** average is a **VRH** average.

★ And the 2026-07-28 leak-audit fold — the very ruling that generated item 21 — declares a VRH
average **inadmissible on this medium**. [`research/2026-07-28_subc-kubc-bracket_result.md`](2026-07-28_subc-kubc-bracket_result.md):327,
verbatim:

> *"explicitly **NOT** a VRH/polycrystal average: the vacuum is a **single crystal**; there are no
> grains to average over, and 'average over grain orientations' and 'average over propagation
> directions of a fixed crystal' are different objects."*

**The contradiction, stated with both paths and NOT resolved here:** the $\sqrt2$ and $\sqrt{10/3}$
inter-channel ratios (and the $c_{shear}=c$ identification that the Q1-revert's whole shear-channel
bookkeeping rides) are built through $K$ and $G_{Hill}$ — a VRH average — of a medium the same
corpus now measures as cubic with $A = 1.23$ (#506) / `[1.330, 1.605]` (#802), and whose own
leak-audit ruling forbids the VRH route. This is **flag-don't-fix**: both statements are on the
record verbatim, neither is reframed to match the other, and the disposition is routed to Grant /
the auditor lane. **Nothing in this scoping doc depends on which way it goes.**

*(Sanity note, so the flag is not over-read: at $\rho^\ast$ the VRH ν-spread is small —
`ν_Voigt=0.2848, ν_Reuss=0.2867, ν_Hill=0.2857`, #506 `:148`–`:149` — so the **averaged** number is robust
as an average. The flag is that an average is the wrong object here, not that the average is
imprecise.)*

### §1.6 — ★ F-A4: #802's Zener bracket does NOT contain #506's Born value — and that is expected, not an error

| Source | Zener $A$ (cold uncaged reference) | Method |
|---|---|---|
| #506 (merged) | `1.2293` at $\rho^\ast$ | infinite-lattice Born / long-wave acoustic slopes |
| #802 (merged) | `1.330402` (SUBC) / `1.605316` (KUBC) at $L=16$ | finite-box static homogenization, two boundary conditions |

`1.2293` sits **BELOW** #802's *lower* (SUBC) arm. This is **not** an inconsistency: $A$ is a
**ratio** of two separately-bracketed moduli, and #802's own §2.1 states the bound-ordering does not
transfer to ratios — verbatim `:53`: *"the frozen §2.1 says the same-instrument ratio `is NOT
theorem-grade on the RATIO, because the uncaged reference is itself boundary-conditioned`"*. The
SUBC/KUBC pair brackets $C_{44}$ and $C'$ **individually** (each from below and above); the ratio of
a lower bound to a lower bound is bracketed by nothing.

★ **Consequence for any future magnitude work: the #802 pair is the WRONG instrument for the
anisotropy magnitude, and the #506 Born value is the right one.** The finite-box KUBC over-stiffens
$C_{44}$ and $C'$ by different amounts, so its $A$ is a boundary-condition artifact of unknown sign
relative to the infinite-medium value. A pre-reg that headlines `A = 1.605` as *the* vacuum's Zener
number would be banding on the wrong measurement. **Surfaced, not fixed** — #802's own scope fence
already says the anisotropy block is `SUPPLEMENTARY_anisotropy_NOT_FROZEN` and enters no frozen
read, so nothing needs walking back; only a future consumer needs warning.

### §1.7 — ★ F-A5: the "EM is protected because it is rank-2" argument is NOT supported by the corpus's own EM measurement

The natural way to save Axis 1 is: *the photon is rank-2-protected (isotropic $\varepsilon,\mu$),
the mechanical sector is rank-4 and is not — so light stays isotropic while GWs go anisotropic.*
**The corpus does not support the premise**, for a specific and checkable reason.

[`port-register.md`](../manuscript/ave-kb/common/port-register.md):47, verbatim, row 1 — the photon
row: *"**EM-transverse** (photon; $T_2$ shear-EM, the transverse-$u$ circulation) … $c = \sqrt{G/\rho}$
… G2 relabel: photon $=$ transverse-$u$, not micro-$\omega$"*. **The photon IS the transverse
translational branch** — i.e. the photon's long-wave speed is governed by the same rank-4 $C_{ijkl}$
as the shear GW, not by an independent rank-2 $\varepsilon\mu$ pair.

And #515's isotropy measurement was taken **at $\rho_{bond}=1$**:
[`research/2026-07-04_lorentz-on-srs_result.md`](2026-07-04_lorentz-on-srs_result.md):84, verbatim —
*"transverse (u-dominated, massless) acoustic branches at the isotropic-bond point k_s=k_a"*; `:120`
— *"The two transverse (u-dominated) photon branches at the isotropic-bond point k_s=k_a"*. At
$k_s=k_a$ the elastic tensor has $A = 1.000$ **exactly** (#506 `:125`), so *every* branch is
isotropic there and the measurement **cannot distinguish** rank-2 protection from
iso-bond-point coincidence.

**Stated precisely, so nobody over-reads it in either direction:**
- #515's results — `c(k\to0)` direction-independent to machine precision including `[110]`/`[210]`,
  the two transverse branches DEGENERATE to `1.7e-14` (`:24`–`:29`, `:127`) — **stand exactly as
  measured**. Nothing is walked back.
- What they do **not** establish is that the photon's isotropy is *symmetry*-protected. On the
  corpus's own G2 relabel it is **operating-point**-protected, and #516 derives that operating point
  as Axiom-3-forced ($\rho_{bond}=1$ to machine precision, knob-free, `Γ_min = 1.5e-8`,
  [`research/2026-07-04_parent-condition-match-forces-balance_result.md`](2026-07-04_parent-condition-match-forces-balance_result.md):24,`:119`).
- **So the emergent-Lorentz isotropy and the item-21 anisotropy are the SAME question asked twice**,
  and both are answered by W1. That is the single most useful thing this scoping produced: item 21
  is not a new frontier, it is a consequence of the $\rho_{bond}$ fork the corpus has already flagged
  as unresolved (photon wants 1, matter wants 9.77, one medium).

### §1.8 — (b) What already constrains direction-dependent GW propagation observationally

**Discipline honoured:** the corpus's standing rule is that external bound values are
WebFetch-verified before citing, never invented
([`research/2026-06-11_alpha-hand-of-god-framing.md`](2026-06-11_alpha-hand-of-god-framing.md):255,
verbatim: *"any bound number must be WebFetch-verified before citing, NOT invented"*). Below,
constraint **classes** are enumerated with their discriminating structure; every magnitude is tagged
`[requires-external-retrieval]` **except** the two already carried in the corpus.

| # | Constraint class | What it constrains | Sky-pattern sensitivity | Status |
|---|---|---|---|---|
| **O1** | **GW170817 / GRB170817A multimessenger arrival** | $\lvert c_{GW}-c_{EM}\rvert / c$ | **ONE direction, ONE event.** Corpus-carried magnitude: $\sim10^{-15}$ ([`port-register`](../manuscript/ave-kb/common/port-register.md)-adjacent; `deep-space-band-map_derivation.md`:207 verbatim: *"consistent with GW170817 (`c_GW = c_EM` to `10⁻¹⁵`)"*). **A single-direction bound cannot see a sky pattern; it fixes ONE point on it.** But a `10 %` anisotropy would have to vanish to `10^{-15}` at that one sky position — a coincidence at the $10^{-14}$ level. This is the class that makes a $\rho^\ast$-riding shear channel look immediately hard. | corpus-carried |
| **O2** | **Multi-event GW speed / sky-pattern regression** (the untested axis the tracker names) | $c_{GW}(\hat n)$ decomposed on cubic harmonics against fixed axes | **THIS IS THE MATCHED OBSERVABLE.** Requires ≥2 well-localized multimessenger events, or a population-level timing analysis. | `[requires-external-retrieval]` — how many multimessenger events exist post-O4 and what the joint bound is |
| **O3** | **SME gravity-sector coefficients** (Kostelecký–Mewes GW framework) | direction-dependent (anisotropic) $d=4$ GW-speed coefficients, expanded in spherical harmonics | **DIRECTLY the sky pattern.** The corpus already knows this basis exists and owes a mapping — [`vol4/claim-quality.md`](../manuscript/ave-kb/vol4/claim-quality.md):733, verbatim: *"Map the parity-odd $k$-linear term onto the explicit SME operator basis and show which Kostelecký coefficient it feeds"*. A cubic $A\neq1$ anisotropy feeds the **parity-EVEN** anisotropic coefficients — a different operator set from that owed campaign. | `[requires-external-retrieval]` for values; the basis is corpus-acknowledged |
| **O4** | **Inter-detector timing residuals** (H/L/V/KAGRA triangulation vs EM counterpart position) | consistency of the GW-derived sky position with the optical one | Weak per-event, but **exists today for every localized event**; a direction-dependent $c_{GW}$ biases triangulation systematically. | `[requires-external-retrieval]` |
| **O5** | **GW polarization-splitting / birefringence bounds** (the §1.4 second observable) | $\lvert c_{T1}-c_{T2}\rvert/c$ at a given $\hat n$ | LVK tests-of-GR already publish GW-birefringence constraints. **This is the matched observable for the shear-splitting axis and the tracker does not name it.** | `[requires-external-retrieval]` |
| **O6** | **Optical cavity / Michelson-Morley class** | $\delta c_{EM}(\hat n)/c$ | Corpus-carried: SME cavity bounds $\sim10^{-19}$–$10^{-20}$ ([`preferred-frame-and-emergent-lorentz.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md):22). **Load-bearing under F-A5:** if the photon is the transverse-$u$ branch, THESE bounds already constrain the elastic anisotropy at $10^{-19}$ — far tighter than any GW bound, and they would rule out $\rho^\ast$ for the photon branch outright. | corpus-carried |
| **O7** | **Pulsar-timing-array / nanohertz band** | low-frequency $c_{GW}$ anisotropy | different band, same axes; a genuinely independent frequency lever | `[requires-external-retrieval]` |

★ **The feasibility verdict for Axis 1(b) falls out of O6, not O2.** If the photon rides the same
rank-4 tensor (F-A5), then the *tightest existing constraint on the vacuum's Zener anisotropy is
already an optical-cavity bound at $10^{-19}$–$10^{-20}$*, not a GW bound. That is `~18` OOM below
the $\rho^\ast$ value of `10 %`. **The discriminating work is therefore NOT "go measure a GW sky
pattern" — it is "answer W1", and the answer is already heavily constrained by existing optical
data.** This is a cheap-and-decisive scoping outcome and it inverts the tracker's implied plan.

### §1.9 — (c) The bench-frame caveat, quoted verbatim as required

[`research/2026-07-28_subc-kubc-bracket_result.md`](2026-07-28_subc-kubc-bracket_result.md):327,
verbatim and complete:

> **★BENCH-FRAME CAVEAT (2026-07-28 leak-audit fold — Grant [sic]: "fold").** `[100]` is the
> **bench's** launch direction because the simulation grid made it convenient — an **engineering
> choice**, not a derived one. The **physical** discriminator (a compression wave meeting a
> star-scale composite) has its propagation direction set by **source geometry relative to the
> cosmically-fixed lattice axes** — generically off-axis, with mode conversion at oblique
> incidence. So the three-way question below is the **bench-consistency** form; the physical-scenario
> form needs the direction-resolved Christoffel treatment or a **derived source-direction average** —
> explicitly **NOT** a VRH/polycrystal average: the vacuum is a **single crystal**; there are no
> grains to average over, and "average over grain orientations" and "average over propagation
> directions of a fixed crystal" are different objects.

**Consequence carried forward:** no step of this scoping uses a VRH average, and §1.5 flags that the
corpus's canonical channel-speed ratios do.

### §1.10 — (d) The calculation needed to go from $C_{ijkl}$ to a sky pattern, and its feasibility

The caveat names the required object: *"the direction-resolved Christoffel treatment."* Concretely:

1. **Christoffel (Kelvin–Christoffel) eigenproblem.** For unit propagation direction $\hat n$,
   build $\Gamma_{ik}(\hat n) = C_{ijkl}\,\hat n_j\,\hat n_l$ (a real symmetric $3\times3$); its
   three eigenvalues are $\rho c^2$ for the one quasi-longitudinal and two quasi-transverse
   branches, its eigenvectors are the polarizations. Sweep $\hat n$ over the sphere ⇒ the full
   slowness surface ⇒ the sky pattern.
2. **Project onto cubic harmonics** to get the observable decomposition (the $\ell=4$ cubic harmonic
   is the leading anisotropic term for a cubic medium), which is what an SME-style sky regression
   consumes.
3. **Fix the lattice-axis orientation on the sky.** The corpus identifies the lattice rest frame
   with the CMB rest frame ([`preferred-frame-and-emergent-lorentz.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md):16)
   — but that fixes the **frame**, not the **axes**. The three cubic axes' orientation on the sky is
   an **additional unfixed input** (3 Euler angles). Note `:178` already reports a null:
   *"Cluster mean direction vs cubic axes (±x, ±y, ±z) | 95.8°, 133.7°, 44.3° (no alignment)"* — so
   the corpus has *assumed* an axis orientation somewhere in that Gaia analysis without deriving it.
   **This is walk-question W3.**

**Feasibility: TRIVIAL on cost, BLOCKED on inputs.**

| Step | Cost | Status |
|---|---|---|
| Christoffel eigensolve over a dense sky | seconds; **`~30` lines of numpy**; already exercised in Appendix B of this doc | **NOT the bottleneck** |
| The $C_{ijkl}$ input | **already merged** (#506 at $\rho^\ast$; iso-bond row at $\rho=1$) | **available** |
| Which $\rho_{bond}$ (W1) | — | **BLOCKING physics input, unresolved** |
| Lattice-axis sky orientation (W3) | — | **BLOCKING input, never derived** |
| Reconciling $c_{shear}\equiv c$ with a direction-dependent $c_{shear}$ (F-A3) | — | **BLOCKING definition, flagged** |

★ **Feasibility verdict, Axis 1:** the *computation* is essentially free and partly already done; the
lane is blocked entirely on **three physics inputs, all of which are Grant/adjudication questions,
none of which is a compute question.** Firing a build lane before W1/W3 would produce a
precisely-computed sky pattern for an operating point nobody has selected — the #796 band-placement
fault in a new costume.

### §1.11 — Outcome-class bins, Axis 1 (**DRAFT — NOT FROZEN**; every class has a reachable bin)

Per the STANDING DESIGN LESSONS (queue file §21 block, lesson 1: *"Every outcome class needs a
REACHABLE bin"*), each bin below is checked reachable **before** any freeze. These are a sketch for
the future pre-reg, not criteria.

| Bin | Condition | Reachable? | Consequence |
|---|---|---|---|
| **A1-ISOTROPIC** | W1 ⇒ the gravitational-band channel rides $\rho_{bond}=1$ | **YES** — #506 measures $A=1.000$ there, exactly | No anisotropy observable exists. Item 21 **closes negative-by-construction**, and the *real* surviving question becomes the $K<0$ mechanical instability at that point (a different, harder problem). |
| **A1-ANISOTROPIC-EXCLUDED** | W1 ⇒ $\rho^\ast$, and O6/O1 exclude `10 %` | **YES** — the optical-cavity bound is `~18` OOM below | A **live falsification exposure**, not a prediction. Routes to a walk-back lane, not a build lane. Rule 11 applies: this is a clean negative with a named mechanism. |
| **A1-ANISOTROPIC-LIVE** | W1 ⇒ $\rho^\ast$ **and** a sector carve makes the photon isotropic while the GW branch is not | **YES but requires a mechanism** — would need the photon to NOT be the transverse-$u$ branch, i.e. a reversal of the G2 relabel | The only branch on which item 21 is a forward prediction. Then O2/O5 become the matched tests. |
| **A1-UNDERDETERMINED** | W1 unanswerable without new physics; the two operating points are not reconcilable in one medium | **YES** | Escalates the $\rho_{bond}$ fork itself to the frontier, above item 21. Honest and probably the most likely. |
| **A1-DEFINITION-BLOCKED** | F-A3 resolves such that $c_{shear}$ is not a single number, so `c_GW = c_EM` needs restating before any test | **YES** | The Q1-revert bookkeeping and `port-register.md:48` need a direction-resolved restatement first. |

### §1.12 — Consistency-vs-emergence class of every Axis-1 candidate statement

| Candidate statement | Class | Why |
|---|---|---|
| "The vacuum lattice is cubic-anisotropic with $A \neq 1$" | **axiom-manifestation** | Direct consequence of Axiom 1 (a specific crystal) + the bond model. No external value imported; the *number* $A$ falls out of $\rho_{bond}$. |
| "$A = 1.229$ at the $\nu=2/7$ point" | **consistency-check** — and *value-importing* | $\rho^\ast$ is located by $\nu=2/7 \Leftrightarrow K=2G$, which #506 `:159` says is *"K=2G RE-IMPORTED, not an independent crystalline determination"*. The value rides a GR import. Cannot be headlined emergence. |
| "$A = 1.000$ at $\rho_{bond}=1$" | **axiom-manifestation** (Axiom 3) | #516 derives $\rho_{bond}=1$ knob-free from minimum internal reflection. This one is genuinely axiom-forced. |
| "Long-wave GW speed is direction-dependent at `10 %`" | **conditional manifestation**, currently **UNCLASSIFIABLE** | Class is undefined until W1 picks the operating point. Do not tag it. |
| "The anisotropy is a falsifiable AVE-distinct prediction" | **NOT ESTABLISHED** — fails `ave-discrimination-check` as written | Any crystalline-vacuum / emergent-gravity model with a cubic substrate predicts the same structure. The AVE-distinct content would have to be the *specific* $A$ value, which is $K=2G$-imported (row 2). **Do not headline this as a chord.** |
| "The corpus's $\sqrt{10/3}$ ratio rides a VRH average" | **internal-consistency finding** | Not a physics claim; a bookkeeping contradiction between two merged corpus statements. Flag-don't-fix. |

## §2 — AXIS 2: gravitational photoelasticity (the Grant fold)

*(sections below)*

## §3 — Walk questions for Grant

*(sections below)*

## §4 — What this lane did NOT do

*(sections below)*

## Appendix A — skill-selection plan + retro-pass

*(sections below)*

## Appendix B — two-method receipts

*(sections below)*
