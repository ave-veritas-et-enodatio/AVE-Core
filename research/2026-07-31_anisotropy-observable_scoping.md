# The anisotropy observable — FEASIBILITY SCOPING (two axes): GW-band sky pattern + gravitational photoelasticity

> **★ SCOPE FENCE, STATED FIRST AND BINDING ON EVERY LINE BELOW.** This lane is **SCOPING, not
> derivation and not measurement.** No solver was run. No engine file was touched. No corpus file
> was modified. **No claim was minted, no solidity was changed, no magnitude is asserted without a
> named derivation-path, and the outcome bins in §1.11 / §2.8 are explicitly NOT FROZEN** — freezing
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

**Grant's picture, taken as canon for this axis** (his words, verbatim `[sic]`): *"isn't gravity just
macroscopic static strain including e and b field? so vacuum birefringence? if AVE is right?"*
Restated in substrate-native terms: **gravity is a macroscopic static DC strain of the lattice,
sourced by all stored energy including field energy; a probe photon crossing that strain gradient is
a wave crossing a pre-stressed medium; pre-stressed media are generically photoelastic; therefore —
does the gravitational strain field split the two polarizations?**

### §2.1 — (a) Where canon states the SYM claim, and its derived-vs-asserted grade

**The canonical leaf is [`graded-network-response.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/graded-network-response.md)
§2** (the achromatic leaf is its SYM limit, and the leaf says so at `:157`). The load-bearing table,
`:145`–`:148`, verbatim:

> | Loading | $S_\varepsilon(x),S_\mu(x)$ | $Z(x)=Z_0\sqrt{S_\mu/S_\varepsilon}$ | Index | Boundary |
> |---|---|---|---|---|
> | **SYM co-grade** (gravity-class; internal $\mathbf E$ **and** $\mathbf B$) | $S(x),\,S(x)$ | $Z_0$ **invariant** | $n=1/\sqrt{S}$, $\delta n\approx+\tfrac14 A^2$ | $\Gamma=0$ **reflectionless** |
> | **ASYM** (static-$\mathbf E$; $\partial\mathbf B/\partial t=0\Rightarrow S_\mu=1$) | $S(x),\,1$ | $Z_0(1-A^2)^{-1/4}$ **varies** | $\delta n\approx-\tfrac14 A^2$ | $\Gamma\ne0$ **reflective** |

**Derived-vs-asserted, graded honestly and per-link:**

| Link in the SYM chain | Grade | Evidence |
|---|---|---|
| Given $S_\varepsilon=S_\mu=S$, then $Z\equiv Z_0$ and $\Gamma=0$ | **DERIVED** (algebraic identity) | `graded-network-response.md`:337 verbatim: *"SYM $\Rightarrow Z=Z_0$ reflectionless, $\delta n\approx+\tfrac14 A^2$ \| **DERIVED** \| impedance ratio cancellation"*. The register's rationale for `clm-07kd5v` says the same (`vol3/claim-quality.md`:94: *"an exact algebraic identity given symmetric scaling"*). |
| That gravity IS the SYM loading (both sectors driven) | **ASSERTED / structurally-argued, NOT node-up derived** | [`achromatic-impedance-matching.md`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md):15 states it as a premise: *"the geometric polarization of the LC network scales its dual reactive components symmetrically"* — no derivation in the leaf. INVARIANT-S2 (`manuscript/ave-kb/CLAUDE.md`:75) grounds it on the driving picture (*"realized when both sectors are driven, e.g. a mass-soliton carrying internal $\mathbf E$ and $\mathbf B$"*), which is a physical argument, not a node-up measurement. The **Axiom-3 parent derivation exists only for the ELASTIC sibling** ($k_s=k_a$, #516) and the EM half is stated as its sibling by analogy (`achromatic-impedance-matching.md`:33). |
| That SYM $\Rightarrow$ polarization-blind | **ASSERTED**, and §2.3 shows the corpus's own machinery does not obviously give it | see §2.3 |
| Solidity of the whole | `clm-07kd5v` **solidity 0.55**, `use as input only, don't build deeper` (`vol3/claim-quality.md`:93) | verbatim |

**★ F-B1 — a stale verify-before-cite false-negative that under-grades this carve (flag, do not fix).**
[`research/2026-07-13_registers-walk_framing.md`](2026-07-13_registers-walk_framing.md):147 records,
verbatim: *"⚠ **Cite correction (verify-before-cite).** The walk pointed this carve at `CLAUDE.md:75`;
that line did **not** verify — `CLAUDE.md:75` is the repo's *Pure-AVE-corpus rule* text, not the
SYM/ASYM physics carve. So the carve is recorded here as **chat-record framing** … **pending a
canonical carve leaf.**"* **That correction resolved against the wrong file.** The repo-root
`CLAUDE.md:75` is indeed the pure-corpus rule — but the SYM/ASYM carve **is canonical**, at
**`manuscript/ave-kb/CLAUDE.md`:75** (INVARIANT-S2, the W6 clarification 2026-06-05), and
`graded-network-response.md`:137 cites exactly that path. So the SYM/ASYM carve is **not**
chat-record-pending-a-leaf; it is INVARIANT-level canon plus a canonical leaf. Surfaced for the
auditor lane; nothing edited here.

### §2.2 — The gravitational forcing chain, IF the loading is exactly symmetric

The corpus supplies a mechanism, not just an assertion — and it is worth stating because it is the
strongest form of the polarization-blindness case. Merged **#519**
([`research/2026-07-04_saturated-elastic-tensor_result.md`](2026-07-04_saturated-elastic-tensor_result.md):16–18)
computes the DC-biased small-signal Cauchy tensor, verbatim:

> *"the saturated **small-signal** Cauchy elastic tensor — computed by the Born-Huang method of long
> waves on the **SATURATED** bond tensor `Φ_b(A) = k_{a,0}·S(A_axial)·d̂⊗d̂ +
> k_{s,0}·S(A_shear)·(I−d̂⊗d̂)`, i.e. the differential stiffnesses at the DC bias point — is the
> **COLD tensor with ρ → ρ_eff = ρ_cold·(S_axial/S_shear)**, exactly."*

★ **The forcing chain falls straight out of that identity.** The whole bias-dependence enters through
the single ratio $S_{axial}/S_{shear}$. **A perfectly symmetric bias has $S_{axial}=S_{shear}$ ⇒
$\rho_{eff}=\rho_{cold}$ ⇒ the small-signal tensor is UNCHANGED ⇒ zero induced birefringence, at any
bias depth.** That is a genuine forcing statement, in this model, on already-merged machinery — the
polarization-blindness of SYM lensing is not merely asserted, it has a lattice-level mechanism.
**Class: CONSISTENCY / axiom-manifestation, model-bounded.** It is exactly as strong as the premise
"the gravitational bias loads the two bond channels equally," which is §2.3's residual.

### §2.3 — (b) The sharp residual: three independent reasons the polarization-blindness is NOT automatic

**★ F-B2 — the corpus's own flagship falsifier derives a POLARIZATION-SPLITTING tensor from the SAME
scalar kernel.** [`vacuum-birefringence-e4.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md):95,
verbatim:

> *"Under a linearly-polarized pump, the AVE vacuum is **uniaxial** (optic axis $\parallel$ the pump).
> The probe-response tensor is $\varepsilon_{ij}=\varepsilon\,\delta_{ij}+2\varepsilon' E_{0i}E_{0j}$
> (the exact differential of the scalar Axiom-4 kernel $S=\sqrt{1-(E/E_{yield})^2}$, optic axis
> $\parallel \hat E_0$; DERIVED, OQ-1 Step 1)."*

So **the scalar Axiom-4 kernel does NOT produce a scalar response once the bias has a DIRECTION.**
Differentiating $S(|{\bf E}|)$ with respect to a directed bias yields a rank-2 **uniaxial** tensor
with optic axis along the bias. The cross-polarization-isotropy statement the SYM side leans on —
`graded-network-response.md`:271, verbatim: *"the cross-polarization **isotropy** — the kernel keys
off $|E|$ so $\Gamma_\parallel=\Gamma_\perp$"* — is a statement about the **normal-incidence boundary
reflection coefficient**, a different observable from the **propagation index tensor**. **Two merged
canonical leaves, one scalar kernel, opposite polarization verdicts, because one treats the bias as a
magnitude and the other as a vector. Surfaced with both cites; not reframed; not resolved here.**

**★ F-B3 — the gravitational bias state is intrinsically UNIAXIAL, at BOTH scales the corpus measures.**
Photoelastic response is **rank-4** ($\delta(\varepsilon^{-1})_{ij}=p_{ijkl}\,\epsilon_{kl}$), so —
exactly as in §1.2 — cubic symmetry does **not** force it isotropic: a cubic $p_{ijkl}$ has three
independent constants ($p_{11},p_{12},p_{44}$), and a **uniaxial** strain drives a birefringence
proportional to $(p_{11}-p_{12})$ or $p_{44}$ depending on the axis. It vanishes only if the strain
itself is **hydrostatic**. The corpus says it is not:

| Scale | Strain state | Cite |
|---|---|---|
| **Far field / weak** | $A = \varepsilon_{11} = 7GM/(c^2 r)$ — a **strain-tensor component**, not a scalar; the radial and tangential strains of a spherical field differ (this is the same content as the corpus's own temporal-vs-spatial index split, $n_{temporal}=1+(2/7)\varepsilon_{11}$ vs $n_{spatial}=1+(9/7)\varepsilon_{11}$) | [`vol3/claim-quality.md`](../manuscript/ave-kb/vol3/claim-quality.md):42,:45 |
| **Vessel / near** | explicitly orientation-split: **hoop-stiffen / radial-soften**, `k_{shear,eff}` anisotropic by bond orientation | [`research/2026-07-21_boundary-strain-amplitude_result.md`](2026-07-21_boundary-strain-amplitude_result.md):96 (R6), verbatim: *"the shell is a **pressure vessel (hoop tension + radial compression)** and `k_{shear,eff}` is **anisotropic**: hoop bonds STIFFEN, radial bonds SOFTEN"* |

★ **In #519's own variables, an orientation-split bias is precisely $S_{axial}\neq S_{shear}$ — the
one thing that moves $\rho_{eff}$, and $\rho_{eff}$ is the parameter that sets the Zener anisotropy
(§1.3).** So the SYM forcing chain of §2.2 and the #779 R6 vessel state **pull in opposite
directions**, on merged corpus numbers, and nothing in the corpus reconciles them. **This is the
sharp residual the fold was asked to find.**

**★ F-B4 — the corpus has NO photoelastic coupling anywhere, verified two ways.** `grep -rniE` and
`git grep -niE` over `*.md` / `*.tex` / `*.py` for
`photoelast|photo-elast|stress-optic|elasto-optic|piezo-optic|Pockels tensor` return **0 hits by both
methods** (Appendix B receipt 3). The framework has never named, derived, measured or bounded a
$p_{ijkl}$. **That is the honest state: the polarization-blindness of gravitational lensing is a
standing forward statement with no coupling calculation behind it, in either direction.**

**★ Related LIVE flag, already on the books — do NOT re-mint it.** The $n_{eff}$ sign/direction
overload ($\sqrt S$ EM-transverse vs $1/\sqrt S$ gravitational) is **already a tracked open item**:
[`engine-capability-map.md`](../manuscript/ave-kb/common/engine-capability-map.md):130 and
[`vol9/ch17-engine-requirements/index.md`](../manuscript/ave-kb/vol9/ch17-engine-requirements/index.md):32
item **(13a)**, *"LIVE (KB-owner decision)"*, flagged in code at `master_equation_fdtd.py:178-180` and
`crystal_engine.py:433-435`. Any Axis-2 magnitude work inherits it, because the sign of the induced
$\delta n$ per polarization rides exactly that convention. **Cited as already-live; not re-raised as
a new finding.**

### §2.4 — (c) EM protection of the UNSTRAINED lattice: what is measured, and what the measurement can and cannot support

| Statement | Status | Cite |
|---|---|---|
| Cold lattice has **no birefringence**: the two transverse photon branches are DEGENERATE, $\max\lvert\omega_{T1}-\omega_{T2}\rvert = 1.7\times10^{-14}$, *"for every direction including the low-symmetry [110]/[210]"* | **MEASURED node-up** (#515) | [`research/2026-07-04_lorentz-on-srs_result.md`](2026-07-04_lorentz-on-srs_result.md):27–29,:127 |
| Cold $c(k\to0)$ direction-independent, cross-direction spread extrapolated to $k=0$ = **0.0** | **MEASURED node-up** (#515) | ibid. `:24`–`:25`,`:125`–`:126` |
| srs point group **432** is non-centrosymmetric and PERMITS $k$-linear gyrotropy (**optical activity**) that centrosymmetric diamond $m\bar3m$ forbids | **MEASURED node-up in two sectors** (#508 mechanical, #515 photon), parity-odd, diamond-null | [`chiral-mechanical-gyrotropy.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/chiral-mechanical-gyrotropy.md):54–55; [`vol4/claim-quality.md`](../manuscript/ave-kb/vol4/claim-quality.md):710,:713 |
| Its magnitude is $\mathcal{O}(k\ell_{node})$-suppressed: $\delta_{chiral}\approx1.7\times10^{-9}\cdot(q\ell_{node})$, i.e. $1.7\times10^{-9}$ at 633 nm, $\sim$**11 OOM below** SME cavity bounds | **MEASURED; ECHO-class, explicitly NOT a near-term falsifier** | [`vol4/claim-quality.md`](../manuscript/ave-kb/vol4/claim-quality.md):716 |

**★ The honest carve required by the brief — "verify each symmetry claim against the corpus's actual
EM implementation."** The answer is the same one Axis 1 reached at F-A5, and it constrains what §2.4
can be used for:

- The corpus's long-wave EM response does **NOT** reduce to an independent rank-2 $\varepsilon$
  tensor at the lattice level. `port-register.md`:47 makes the photon **the transverse-$u$ branch**
  (*"photon $=$ transverse-$u$, not micro-$\omega$"*), whose $k\to0$ speeds are eigenvalues of the
  **rank-4** $C_{ijkl}$. The rank-2 $\varepsilon,\mu$ description is the **continuum projection** of
  that, not an independent structure.
- Consequently **"cubic symmetry forces $\varepsilon$ isotropic" is a true statement about a rank-2
  object that the lattice does not independently carry**, and the #515 degeneracy measurement was
  taken at $\rho_{bond}=1$, where the rank-4 tensor is isotropic anyway ($A=1.000$).
- **What survives untouched:** every #515 number, and the structural statement that **432 admits
  optical activity at order $k\ell_{node}$** (a point-group fact, magnitude honestly wavelength-
  suppressed, already ECHO-graded). **What does not survive as written:** "the unstrained lattice is
  EM-protected *by rank-2 cubic symmetry*." On the corpus's own G2 relabel the protection is
  **operating-point** protection (Axiom-3-forced $\rho_{bond}=1$), which is a different — and
  arguably stronger, because derived — claim, but it is not the one usually stated.

### §2.5 — (d) Why the gravitational (SYM) and pumped-E (ASYM) predictions DIFFER — stated so neither null can be misread as killing the other

This is the single most important framing output of Axis 2, because the two channels are near-neighbours
in vocabulary and antipodal in physics.

| | **Gravitational photoelasticity (Axis 2)** | **Flagship E-route falsifier (`clm-pp3qwf`)** |
|---|---|---|
| **Loading class** | **SYM** — both $\varepsilon$ and $\mu$ grades co-scale | **ASYM** — $\varepsilon$-only |
| **Why** | the source carries internal $\mathbf E$ **and** $\mathbf B$ (mass-soliton / symmetric bulk strain), INVARIANT-S2 W6 | a static/DC $\mathbf E$ has $\partial\mathbf B/\partial t=0$, so $I_{vac}=0$, so $S_\mu=1$ is **forced, not assumed** (`graded-network-response.md`:161–163) |
| **Kernel argument** | strain amplitude $A=\varepsilon_{11}=7GM/c^2r$ | $A=E/E_{yield}$ (the $V$-keyed varactor) |
| **Impedance** | $Z\equiv Z_0$ **invariant** ⇒ $\Gamma=0$ | $Z=Z_0(1-A^2)^{-1/4}$ **varies** ⇒ $\Gamma\ne0$ |
| **Index sign** | $\delta n\approx+\tfrac14A^2$ (light **slows**) | $\delta n\approx-\tfrac14A^2$ |
| **Predicted birefringence** | **ZERO** (the standing forward statement) | $\delta n_{bir}\approx-\tfrac12A^2$, ratio $3.75\pi/\alpha^2\approx2.2\times10^5$ over instantaneous Euler-Heisenberg |
| **Amplitude at its own bench** | $A\sim10^{-9}$ at the solar limb | $A^2\sim5.9\times10^{-7}$ at HIBEF demonstrated pump |
| **Kill-shape** | *"any confirmed **polarization-dependence** or **reflection component** in gravitational lensing kills the symmetric carve outright"* — [`research/2026-07-13_registers-walk_framing.md`](2026-07-13_registers-walk_framing.md):160, verbatim; recorded in the docket at [`_orchestration/2026-07-10_rulings-docket.md`](../_orchestration/2026-07-10_rulings-docket.md):463 | a QED-sized differential coefficient falsifies AVE; an AVE-sized one falsifies QED |

> ### ★ THE NON-CONFUSION STATEMENT (write this into any pre-reg on either channel)
>
> **A gravitational-lensing polarization NULL does not corroborate the flagship, and does not kill it.**
> A null there is the SYM carve's **own** prediction (§2.2), on a **different loading symmetry**, a
> **different kernel argument**, and an amplitude $\sim10^{-9}$ versus the flagship's
> $\sim7.7\times10^{-4}$ in $A$.
>
> **Conversely, a HIBEF null does not rescue the SYM carve** and a HIBEF detection does not imply
> gravitational birefringence: the ASYM channel is $\varepsilon$-only *because* $\partial{\bf B}/\partial t=0$,
> which is a property of the drive, not of the vacuum.
>
> **The one thing that WOULD couple them** is a demonstration that the gravitational bias is not
> exactly symmetric (F-B3). Then gravity acquires a small ASYM component and the two channels share
> a mechanism. **That is the physics question, and it is open.**

### §2.6 — Observational constraint classes for a gravitational polarization signature

Same discipline as §1.8: classes enumerated, magnitudes tagged `[requires-external-retrieval]`, no
bound invented. All of these are **already-existing-data** classes — none needs a new facility.

| # | Class | Signature it would carry | Why it is the matched observable |
|---|---|---|---|
| **P1** | **Strong-lensed quasar / radio-source polarimetry** (multiple images of one source through one deflector) | differential polarization-angle or ellipticity **between images** at different impact parameters | The source polarization cancels in the image-to-image difference — the cleanest differential form. Radio-loud lenses have high intrinsic polarization and precise angle measurement. **Best class.** |
| **P2** | **Solar-limb polarimetry** | tangential/radial polarization pattern in light grazing the Sun | Largest well-characterized nearby $\varepsilon_{11}$; the F-B3 predicted axis is **radial**, giving a tangential/radial split with a known geometry |
| **P3** | **Pulsar polarization through the Galactic potential** | secular polarization-angle drift correlated with potential gradient, not with rotation measure | Pulsars are strongly polarized with stable angle profiles; separable from Faraday rotation by its **non-$\lambda^2$** frequency dependence |
| **P4** | **CMB polarization** | large-angle E/B pattern correlated with the lensing potential | Sensitive but confusion-limited; note the corpus's own §2.4 optical activity is a **rotation** (parity-odd), while photoelasticity is a **linear birefringence** (parity-even) — different CMB signatures, must not be merged |
| **P5** | **Black-hole / neutron-star X-ray polarimetry (IXPE-class)** | polarization-angle rotation with photon ring / strong-field impact parameter | Deepest available $\varepsilon_{11}$; but the strong-field regime brings the corpus's own $r_{sat}=3.5r_s$ saturation boundary into play — **regime-check first** |
| **P6** | **Shapiro-delay polarization dependence** | polarization-dependent arrival time for a grazing signal | A pure-timing form of the same effect; VLBI/pulsar-timing data already exist |

**All six are `[requires-external-retrieval]` on magnitudes.** ★ **But the honest feasibility read is
that the class matters less than the coupling**: with $p_{ijkl}$ entirely absent from the corpus
(F-B4), no bound-comparison is possible yet in either direction. **The gating work is the coupling
calculation, not the observation survey.**

### §2.7 — Feasibility of the coupling calculation (the actual gate)

★ **HIGH feasibility. The two photoelastic channels are already named and one is already built.**

| Channel | Mechanism | Corpus status | Cost to compute |
|---|---|---|---|
| **(i) Spring-softening** | bias softens the two bond springs by their per-channel $S(A)$ ⇒ $\rho_{eff}=\rho_{cold}(S_{axial}/S_{shear})$ ⇒ new $C_{ijkl}$ ⇒ new branch speeds per polarization | **BUILT + MERGED** (#519 `saturated_elastic_tensor.py`) | **A parameter sweep, not a new solver.** Feed an *orientation-split* $(S_{axial},S_{shear})$ instead of a symmetric one, re-run the existing Born-Huang extraction, read $\Delta c$ between the two transverse branches. |
| **(ii) Geometric / pre-stress stiffness** | $k_{shear,eff}=k_s+T/\ell$, the #779 remap; explicitly orientation-split (hoop vs radial) | **BUILT** in the vessel-state driver (#796 live geometric term); **NOT** connected to any optical read | Moderate — needs the pre-stressed lattice's transverse branches, i.e. #515's eigensolve on #796's stressed configuration |
| **(iii) Bias-induced geometry relaxation** | node positions / bond directions relax off the cold geometry | **NAMED AND OPEN** — #519 `:29`–`:30` verbatim: *"**(b) bias-induced geometry change** … Both are **OUT OF SCOPE here and remain OPEN**"* | Higher; needs a relaxation solve |

**Feasibility verdict, Axis 2:** channel (i) is a **cheap, decisive first cut on already-merged
machinery** and it directly tests F-B3 — feed a symmetric bias, confirm the §2.2 forcing chain
returns exactly zero splitting (a known-positive gate); then feed the #779 hoop/radial split and read
whether the splitting is nonzero and at what order in $A$. **That is the whole discriminator, and it
is a driver-extension, not a new engine.** ★ **Blocking inputs are the same three as Axis 1 plus one
new one:** the $\rho_{bond}$ operating point (W1), the $n_{eff}$ convention (item 13a), the SYM-vs-
orientation-split question for the *gravitational* bias specifically (**W4**), and the F-B2
magnitude-vs-vector reading of the kernel (**W5**).

### §2.8 — Outcome-class bins, Axis 2 (**DRAFT — NOT FROZEN**; every class has a reachable bin)

| Bin | Condition | Reachable? | Consequence |
|---|---|---|---|
| **A2-BLIND-FORCED** | channel (i) returns exactly zero splitting for a symmetric bias **and** W4 rules the gravitational bias symmetric | **YES** — #519's $\rho_{eff}=\rho_{cold}(S_{ax}/S_{sh})$ identity makes the zero exact, not numerical | The SYM carve's polarization-blindness is **upgraded asserted → derived**. **Consistency-class** (a $\mu_r=\varepsilon_r$ metamaterial does the same, `graded-network-response.md`:324) — **not** a chord. Real gain: the standing kill-shape gets a mechanism. |
| **A2-RESIDUAL-BELOW-BOUND** | splitting nonzero but $\propto A^2$ with an $\mathcal{O}(1)$ coefficient ⇒ $\sim10^{-18}$ at the solar limb | **YES** | A forward prediction that is **honest and un-testable**; bank as ECHO/consistency, do **not** headline. Same shape as the §2.4 optical-activity result. |
| **A2-RESIDUAL-TESTABLE** | splitting $\propto A$ (first order) rather than $A^2$ ⇒ $\sim10^{-9}$ at the limb | **YES** — first order is what a genuine rank-4 photoelastic coupling to a **linear** strain gives; $A^2$ would require the linear term to cancel | **The interesting branch.** P1/P2 become live tests and the lane earns a pre-reg. ⚠ Note this bin is reachable *precisely because* photoelasticity is linear in strain while the kernel's index shift is quadratic in amplitude — **the two are not the same expansion**, which is why the bin is not a rescue. |
| **A2-KILLED** | splitting large enough that existing lensing polarimetry already excludes it | **YES** | The SYM carve dies on its own recorded kill-shape (`registers-walk_framing.md`:160). Rule 11: bank the negative, name the mechanism, close. |
| **A2-COUPLING-BLOCKED** | channel (i) cannot represent the gravitational bias at all (e.g. it needs (iii), the relaxation term) | **YES** | ARTIFACT, not falsification, per regime discipline. Routes to a bigger build with a stated ceiling. |
| **A2-DEGENERATE** | W4 unanswerable — "is gravitational strain hydrostatic or uniaxial?" is not settled by the corpus | **YES, and likely** | Escalates F-B3 to Grant. This is the honest default and it costs nothing to reach. |

### §2.9 — Consistency-vs-emergence class of every Axis-2 candidate statement

| Candidate statement | Class | Why |
|---|---|---|
| "SYM co-grading ⇒ $Z\equiv Z_0$ ⇒ $\Gamma=0$" | **definitional-identity** | Algebraic cancellation, given the premise. `graded-network-response.md`:337 grades it DERIVED; the content is in the premise, not the algebra. |
| "Gravity is the SYM loading" | **consistency-check**, premise-grade | Physically argued from the mass-soliton's internal $\mathbf E$&$\mathbf B$; not node-up derived. |
| "Gravitational lensing is polarization-blind" | **consistency-check** (currently), **candidate axiom-manifestation** if channel (i) closes it | Consistent with all data; no coupling calculation behind it either way (F-B4). |
| "SYM ⇒ reflectionless achromatic lens is AVE-distinct" | **NOT AVE-distinct as a mechanism-existence claim** | The corpus already says so: `graded-network-response.md`:324, verbatim — *"a co-doped $\mu_r=\varepsilon_r$ metamaterial also gives $\Gamma=0$; the AVE-distinct content is which physical drive … realizes it"*. `ave-discrimination-check` PASSES only on the drive-identification, not on the $\Gamma=0$. |
| "A nonzero gravitational photoelastic splitting would be an AVE chord" | **would be genuinely AVE-distinct in FORM** | GR predicts **exactly zero** — the spacetime metric couples to both polarizations identically at leading order; a nonzero splitting is a presence/absence divergence of the same clean shape as `clm-fofwr1`'s parity chord. **But its magnitude would be an $A$-echo** (rides $GM/c^2r$, an imported scale), so headline the FORM only. |
| "The $n_{eff}$ direction convention" | **NOT a physics statement** — a live notation adjudication | Already tracked as item (13a). |

## §3 — Walk questions for Grant (one per load-bearing assumption; asked BEFORE design, per the Rule-16 strengthening)

These are the `pre-test-physics-check` output. **Nothing fires until W1 and W6 are answered** —
those two decide whether either axis exists. Each is stated as a plumber-physical question with the
options that are actually on the table; none is rhetorical and none has a pre-picked answer.

**W1 — Which bond-stiffness operating point does the gravitational-band channel sit at?** The corpus
carries two, and they give opposite answers to item 21. At $\rho_{bond}=k_a/k_s=1$ the lattice is
**Zener-isotropic exactly** ($A=1.000$) and there is no anisotropy observable at all — but the bulk
modulus is **negative** there ($K=-0.0589$), i.e. the medium would collapse under hydrostatic
pressure. At $\rho^\ast=9.7734$ the medium is mechanically stable and $\nu=2/7$, but $A=1.229$ and
the shear branch is `10 %` direction-dependent. Plumber form: *is the vacuum one medium sitting at one
stiffness ratio, or is the "photon operating point" a different thing from the "matter operating
point" in a way that a real material can actually do?* Options on the table: **(a)** one medium at
$\rho^\ast$ — then Axis 1 is a live falsification exposure, probably already excluded by optical
cavities; **(b)** one medium at $\rho_{bond}=1$ — then item 21 closes negative-by-construction and
the $K<0$ instability becomes the frontier question instead; **(c)** genuinely two operating points
(some carve makes the photon see $\rho=1$ and matter see $\rho^\ast$) — then the carve itself is
what needs deriving, and it is a bigger and more interesting object than item 21; **(d)** the
question is malformed because $\rho_{bond}$ is not a single global number.

**W2 — Is `c_shear = c` a statement about ONE direction, or an averaged number?** `port-register.md`:48
canonizes $c_{shear}=c$ and the band-map derives $\sqrt2$ and $\sqrt{10/3}$ inter-channel ratios
"from $K=2G$" — but $K$ and $G$ are the **two** constants of an isotropic solid and this medium has
**three**, so a Voigt/Reuss/Hill choice is buried in there (#506 `:147`). The same corpus's leak-audit
ruling forbids exactly that average on a single crystal. Plumber form: *when we say the GW travels at
`c`, do we mean along a lattice axis, along the body diagonal, or "on average" — and if the last one,
average over what, given there are no grains?* Options: **(a)** it is a direction-resolved statement
and one direction must be named; **(b)** it is a source-direction average and that average must be
derived, not VRH-borrowed; **(c)** at the true operating point $A=1$ so the question dissolves (this
is W1 option (b) again); **(d)** the ratios are FORM-only and were never meant to carry a direction.

**W3 — Where are the cubic axes on the sky?** The corpus fixes the lattice **rest frame** to the CMB
rest frame, but a frame is 3 numbers and an orientation is 3 more. No corpus statement derives the
axis orientation — yet `preferred-frame-and-emergent-lorentz.md`:178 already reports a null against
"cubic axes (±x, ±y, ±z)", which means an orientation was assumed somewhere. Plumber form: *when the
vacuum crystallized at recombination, what picked which way the crystal axes point, and is that even
a well-posed question for a single cosmic-scale crystal?* Options: **(a)** derivable from the freeze
process; **(b)** an initial condition, i.e. 3 free parameters any sky-pattern test must fit; **(c)**
not a single global orientation at all (domains — which would reintroduce grains and change the
whole leak-audit ruling); **(d)** already fixed somewhere and this lane failed to find it.

**W4 — Is the gravitational strain state hydrostatic or uniaxial?** This is the Axis-2 crux and it is
squarely a plumber question. A pressure vessel has hoop tension and radial compression — different
signs on different bond orientations. A hydrostatic squeeze has the same strain in every direction.
The corpus says gravity is "symmetric bulk strain" (INVARIANT-S2) in one place and "hoop-stiffen /
radial-soften" (#779 R6) in another. Plumber form: *sitting inside one lattice cell a solar radius
from the Sun — is the cell being squeezed equally from all sides, or squeezed radially and stretched
tangentially?* Options: **(a)** hydrostatic ⇒ $S_{axial}=S_{shear}$ ⇒ zero photoelastic splitting,
exactly (§2.2 forcing chain closes); **(b)** uniaxial-radial ⇒ nonzero splitting, magnitude to be
computed; **(c)** hydrostatic in the far field and uniaxial only near the yield boundary — a
regime-split answer; **(d)** the $A_1$/$T_2$ decomposition already answers this and the two
statements are about different sectors, in which case the reconciliation is bookkeeping not physics.

**W5 — Does the Axiom-4 kernel see the bias as a MAGNITUDE or as a VECTOR?** The corpus does both.
`graded-network-response.md`:271 leans on *"the kernel keys off $\lvert E\rvert$"* to get
polarization-blindness; `vacuum-birefringence-e4.md`:95 differentiates the same kernel with respect to
a **directed** $E_0$ and gets a **uniaxial** tensor — and calls that DERIVED. Plumber form: *when a
cell is biased, does it get uniformly softer, or does it get softer along the bias direction and stay
stiff across it?* Options: **(a)** magnitude — then the flagship's uniaxial tensor needs re-deriving;
**(b)** vector — then SYM polarization-blindness needs re-deriving; **(c)** both, because the two
sites are describing different objects (the boundary $\Gamma$ vs the propagation index) and the
apparent conflict is a category error; **(d)** it depends on which bond channel is loaded, which
routes back to W4.

**W6 — Is the photon really the transverse-$u$ acoustic branch?** `port-register.md`:47 says yes (the
G2 relabel: *"photon $=$ transverse-$u$, not micro-$\omega$"*). If yes, then the photon's speed is an
eigenvalue of the same rank-4 $C_{ijkl}$ as the GW shear branch, and (i) the emergent-Lorentz isotropy
is operating-point protection rather than rank-2 symmetry protection, and (ii) existing optical-cavity
anisotropy bounds at $10^{-19}$ already constrain the vacuum's Zener number ~18 OOM below the
$\rho^\ast$ value. Plumber form: *is light a shear wave in this medium, or is it a genuinely separate
electromagnetic mode that only shares a speed?* Options: **(a)** yes, one branch — then W1 is
essentially already answered by optical-cavity data and the answer is $\rho_{bond}=1$; **(b)** no,
separate sectors — then the G2 relabel needs revisiting and the rank-2 protection returns; **(c)**
the same branch at long wavelength but distinguishable near the zone edge.

**W7 — Does "SYM = both sectors driven" mean equal $S$ per FIELD sector ($\varepsilon$ vs $\mu$) or
equal $S$ per BOND channel (axial vs shear)?** The two are not the same statement and the whole
Axis-2 forcing chain rides on which one is meant: #519's identity is
$\rho_{eff}=\rho_{cold}(S_{axial}/S_{shear})$ — a **bond-channel** ratio — while INVARIANT-S2's SYM
condition is $S_\varepsilon=S_\mu$, a **field-sector** condition. Plumber form: *"both sectors
loaded" — is that the cap and the inductor, or the stretch-spring and the shear-spring?* Options:
**(a)** field sectors, and the bond-channel mapping is a separate open question; **(b)** bond
channels, and $S_\varepsilon=S_\mu$ follows; **(c)** they are the same thing under TKI and the
identification is already canon somewhere this lane did not find.

**W8 — Priority: does either axis get fired at all?** ★ The honest read from this scoping is that
**item 21 is not an independent frontier item.** Axis 1 collapses onto W1/W6, and if W6 answers
"one branch" then existing optical-cavity data has already constrained the object ~18 OOM tighter
than any GW measurement could. Axis 2 is the axis with genuine untouched content (F-B4: zero
photoelastic coupling anywhere in the corpus) and a cheap first cut on merged machinery. Options:
**(a)** fire Axis 2 channel-(i) only, as a small driver extension, after W4/W5/W7; **(b)** fire
neither, and instead route the $\rho_{bond}$ two-operating-point fork (W1/W6) as its own frontier item
above item 21 — this lane's recommendation if only one thing moves; **(c)** fire the Axis-1
Christoffel sky-pattern anyway as a cheap consistency artefact, accepting that its output is
conditional on an unpicked operating point; **(d)** park both and record item 21 as **subsumed** by
the $\rho_{bond}$ fork.

## §4 — What this lane did NOT do (non-goals, fenced)

- **Did not run a solver.** No driver executed, no engine file touched, `src/ave` byte-untouched.
  The only computation is the Appendix-B Christoffel cross-check, which is a scratch verification of
  an already-shipped table and produces no new physics.
- **Did not mint a claim, a `clm-`/`def-`/`sup-` node, or a solidity.** No `claim-quality.md` edited.
- **Did not freeze bins.** §1.11 and §2.8 are drafts with a reachability audit; a pre-reg freezes.
- **Did not resolve any contradiction it found.** F-A3, F-A4, F-A5, F-B1, F-B2, F-B3 are all
  surfaced with both file paths and verbatim content, neither side reframed to match the other.
  **Flag-don't-fix.**
- **Did not walk anything back.** #802's anisotropy block is already `SUPPLEMENTARY…NOT_FROZEN` and
  enters no frozen read, so F-A4 needs no retraction — only a warning to future consumers. #515's
  measurements stand exactly as measured; F-A5 narrows an *interpretation*, not a number.
- **Did not invent an external bound.** Every observational magnitude in §1.8 and §2.6 is either a
  corpus read with a cite or tagged `[requires-external-retrieval]`, per the standing rule at
  [`research/2026-06-11_alpha-hand-of-god-framing.md`](2026-06-11_alpha-hand-of-god-framing.md):255.
- **Did not draft the auditor's manual entry, a KB leaf, or a manuscript edit.** The findings are
  surfaced; the auditor lane lands them.
- **Did not re-mint the `n_eff` overload** — cited as already-live item (13a).
- **Did not draft an Axiom-5 candidate.** Nothing here diagnoses a missing axiom; every finding is
  either an engine/corpus consistency question or a Grant-adjudicable physics fork.
- **Did not pick a side on W1–W8.** W8 carries a stated *recommendation* (route the $\rho_{bond}$
  fork above item 21), explicitly labelled as a recommendation, not a decision.

---

## Appendix A — skill-selection plan + retro-pass

### A.1 — The 60-second plan, written BEFORE work started

| Skill / discipline | Why planned | Fired? |
|---|---|---|
| `ave-prereg` (corpus-grep-first) | Both axes smell like they may already exist somewhere in a merged lane; grep before deriving | ✅ **and it paid the whole lane** — the grep found #506's direction-resolved slope table (F-A1) and #519's saturated tensor (§2.2), which is why nothing needed deriving |
| `verify-before-cite` | Every finding is a file:line claim against merged corpus; stale beliefs do not carry | ✅ continuously — caught two of my own draft cites (`:124`→`:125`, `:199`→`:197`) **and** caught F-B1, a stale cite-correction in the corpus itself |
| `substrate-native-check` (K4 / Cosserat / Op14 / phase-space-vs-real-space) | Mandatory before any solver-shaped thinking | ✅ — fired as the §0 sector header before any standard-physics word; it is what forced the rank-2/rank-4 carve (§1.2) rather than reaching for a continuum-Helmholtz picture |
| `phase-space-coordinate-check` (A46) | Corpus claim is directional real-space; must not compare against a phase-space object | ✅ — §0 row 4; both axes matched, no mismatch found |
| `consistency-vs-emergence` | Brief requires a class per candidate statement | ✅ — §1.12 and §2.9, per-statement |
| `ave-discrimination-check` | Anything smelling AVE-distinct must face the SM counterfactual | ✅ — killed the "anisotropy = AVE-distinct falsifiable prediction" framing (§1.12 last-but-one row) and confirmed the corpus's own `:324` verdict that $\Gamma=0$ is metamaterial-reproducible |
| sector-ownership (A1 ⊥ T2 cross-wiring watch) | The tracker title says "P-speed" but the GW channel is shear | ✅ — §0 note + §1.4 finding 1; corrected the sector without silently rewriting the tracker |
| regime / phase-state discipline | A null where the effect cannot exist is an artifact | ✅ — §0 row 5; used in bin A2-COUPLING-BLOCKED |
| `pre-test-physics-check` | Rule-16 strengthening: ask BEFORE design | ✅ — §3, eight questions, asked before any pre-reg exists |
| pure-AVE-corpus rule | Every tracked file must be pure physics | ✅ — §A.3 receipt |
| grep-completeness two-method | My `**` globs and `$…$` patterns silently false-negative | ✅ — the F-B4 absence claim is checked by two independent methods (Appendix B receipt 3) |

### A.2 — Retro-pass on applied-set drift (run before commit, per the standing discipline)

**Three skills fired that were NOT in the plan, and one planned item was deliberately NOT fired:**

- **`ave-canonical-leaf-pull` — fired, unplanned.** Both axes are propagation-speed problems, which
  is an explicit trigger. Pulled: `port-register.md` (the four-channel table), the band-map
  derivation, `cosserat-mass-gap.md` via the port-register's two-method receipt line,
  `achromatic-impedance-matching.md`, `graded-network-response.md`. **This is what surfaced F-A3**
  (the VRH provenance of the canonical channel ratios) — a finding the planned set would have missed.
- **`ave-mechanism-claims-discipline` — fired, unplanned.** §2.2 is a mechanism statement (the
  $\rho_{eff}$ forcing chain). It is headlined with its class (CONSISTENCY / model-bounded) and its
  premise-dependence, not as a bare mechanism win.
- **`ave-evidence-framing-discipline` — fired, unplanned.** Applied to the §1.4 magnitudes: they are
  labelled *arithmetic on merged numbers, conditional on W1*, not "AVE predicts 10 % GW anisotropy."
- **`ave-reproduction-gate` — deliberately NOT fired, disclosed.** The gate would re-run #506's and
  #519's drivers on the current engine before load-bearing their numbers. This lane load-bears them
  only for *scoping direction*, does not bank any of them, and is engine-untouched by charter. ★ **A
  pre-reg that fires on the back of this doc MUST run the reproduction gate on #506's `C_ij` before
  banding anything on them** — recorded here so the omission is a disclosed scope choice, not an
  oversight.

### A.3 — Pure-AVE-corpus receipt

Deliverable, docket fragment and every commit message in this lane carry **pure physics only** — no
non-physics external context of any kind appears in any tracked file. All rationale is stated in
substrate-physics terms. Checked two ways (pattern scan over the tracked deliverables, and a scan of
the lane's commit messages); both clean.

---

## Appendix B — two-method receipts

**Receipt 1 — the #506 slope table IS the exact cubic Christoffel solution of the #506 $C_{ij}$
(method 1 = shipped table read; method 2 = independent eigensolve).** Feeding
$C_{11},C_{12},C_{44} = 0.7279, 0.3232, 0.2488$ (the $\rho^\ast$ row,
[`2026-07-04_srs-elastic-tensor_result.md`](2026-07-04_srs-elastic-tensor_result.md):132) into
$\Gamma_{ik}(\hat n)=C_{ijkl}\hat n_j\hat n_l$ and diagonalizing:

| Direction | Christoffel eigenvalues (method 2) | shipped table (method 1) | max abs diff |
|---|---|---|---|
| `[100]` | `0.24880, 0.24880, 0.72790` | `0.24876, 0.24876, 0.72786` | `4.0e-05` |
| `[110]` | `0.20235, 0.24880, 0.77435` | `0.20235, 0.24876, 0.77426` | `9.0e-05` |
| `[111]` | `0.21783, 0.21783, 0.78983` | `0.21782, 0.21782, 0.78973` | `1.03e-04` |

Residuals are at the 4-decimal precision of the $C_{ij}$ as printed in the source table — i.e. the
agreement is **exact to the available input precision**. ★ **Consequence for §1.10: the
"direction-resolved Christoffel treatment" the merged caveat names is not new work — the symmetry
directions are already solved, and the full sky sweep is a `~30`-line extension.**

**Receipt 2 — the two Zener definitions in play agree.** #802 uses $A = C_{44}/C'$ with
$C'=(C_{11}-C_{12})/2$; #506 uses $A = 2C_{44}/(C_{11}-C_{12})$. These are algebraically identical.
Evaluated on the $\rho^\ast$ row: $C' = (0.7279-0.3232)/2 = 0.20235$, $A = 0.2488/0.20235 =
1.229553$, against #506's shipped `1.229` — agreement to the shipped precision. **Cross-method bonus:
$C'$ computed this way equals the shipped `[110]` T(low) slope `0.20235` exactly**, which is the
textbook cubic identity $\rho c^2_{[110],T\perp} = C'$ — a third, independent confirmation that the
table and the tensor are the same object.

**Receipt 3 — the photoelasticity absence (F-B4), two independent methods.**

| Method | Command | Hits |
|---|---|---|
| filesystem walk | `grep -rniE "photoelast\|photo-elast\|stress-optic\|stress optic\|elasto-optic\|elastooptic\|piezo-optic\|Pockels tensor" . --include="*.md" --include="*.tex" --include="*.py"` | **0** |
| git index | `git grep -niE "photoelast\|stress.optic\|elasto.optic\|piezo.optic" -- '*.md' '*.tex' '*.py'` | **0** |

Two methods, two zeroes. The absence claim is safe. *(This is the grep-completeness discipline
applied deliberately: a single-pattern `grep` returning zero is exactly the false-negative shape
that has bitten before.)*

**Receipt 4 — every file:line cite in this document was re-read at ship time**, not carried from
session context. Three draft cites were wrong and were corrected before commit
(`srs-elastic-tensor_result.md:124`→`:125`, `:199`→`:197`–`:198`,
`graded-network-response.md:160`→`:161`). ★ **The same check found F-B1** — a cite-correction in the
corpus that itself resolved against the wrong `CLAUDE.md`.

**Receipt 5 — the two operating-point numbers, cross-read.** $\rho_{bond}=1$ giving $A=1.000$ is read
BOTH from #506's table row (`:125`, Zener column `1.000`) AND from #506's prose (`:197`–`:198`, *"At
the iso-bond point (ρ=1) all directions collapse to 0.17678 (A=1, but K<0 unstable)"*) AND
independently from #516's minimiser landing at $\rho^\ast=0.99999999$ with $\Gamma_{min}=1.5\times10^{-8}$
(`2026-07-04_parent-condition-match-forces-balance_result.md`:24,:119). Three sites, one number.

---

> **Lane mechanics.** Self-isolated throwaway worktree off `origin/main` @ `512e1ef4`; branch
> `research/anisotropy-observable-scoping`; skeleton-first incremental commits (one section per
> commit). Engine `src/ave` byte-untouched; zero corpus files modified; the only new files are this
> document and its docket fragment. PR opened `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.
