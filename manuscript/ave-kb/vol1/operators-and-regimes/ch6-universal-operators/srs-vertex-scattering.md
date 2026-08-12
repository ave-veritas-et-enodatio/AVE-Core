[↑ Ch.6 Universal Operators](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-v3port, clm-bore2x]
path-stable: "the canonical srs z=3 vertex scattering result — bare Γ=(2−z)/z=−1/3, the lossless-reciprocal 3-port floor |S₁₁|≥1/3 (Pozar-class theorem confirmed at the vertex), the non-reciprocal circulator escape (PENDING-GRANT), and the two-axis Op6 bore verdict (broadband f*=0 unique; single-frequency {0, f_touch} degenerate)"
-->

# srs $z=3$ Vertex Scattering — the reciprocal 3-port reflection floor $|S_{11}|\ge 1/3$, the circulator escape, the two-axis bore verdict

> **What this leaf is (class + scope, load-bearing honesty).** The canonical characterization of
> **reflection at the chiral srs vacuum-net vertex** ($I4_132$, coordination $z=3$): the bare-junction
> counting reflection $\Gamma=(2-z)/z=-1/3$, the **classic matched-lossless-reciprocal-3-port theorem**
> (Pozar §7.1 class) $|S_{11}|\ge 1/3$ **ATTRIBUTED as known microwave-network theory, confirmed at the
> vertex** (provable — not a new derivation), its **sole escape class = non-reciprocity** (the circulator
> witness — PENDING-GRANT), and the **two-axis Op6 bore verdict** (the band-integrated comparator uniquely
> selects the point junction; the frozen single-frequency objective is exactly degenerate on a half-wave-
> invisible bore family). It is a **CONSISTENCY / characterization** result on the reflection axis (the
> theorem confirmation) plus a **derived FORM within the disclosed leading-order lumped reciprocal model
> class** (the bore verdict) — **NOT a falsification and NOT an emergence claim**.
>
> **SECTOR HEADER.** MODE = linear small-signal (S-parameters). REGIME = cold, sub-yield, lossless
> (reactive-only; Axiom 3 — reflection is **reactive back-scatter / redistribution**, never dissipation).
> SECTOR = bare-bond network primitive, **scalar / compression channel**; the vertex 3-port is scoped to the 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
> **lossless reciprocal class** throughout (the one escape is non-reciprocity, §3). Vector/torsion channels
> scoped out (§5).
>
> Provenance (drivers + result docs, merged; verify-before-cite every number against them): the vertex 3-port
> floor + two-axis bore verdict `research/2026-07-10_x38-s11-bore-selection_result.md` (repaired two-axis
> state authoritative) + the junction-parasitic extraction `research/2026-07-10_x37-junction-parasitics_result.md`
> (repaired, incl. C8) + the #620 correction (the reciprocal-class evanescent-stub escape is theorem-dead).
> Modules: [`src/ave/core/junction_scattering.py`](../../../../../src/ave/core/junction_scattering.py) (S₁₁) +
> [`src/ave/core/junction_parasitics.py`](../../../../../src/ave/core/junction_parasitics.py) (the lumped
> loaded-band solve).

## §1 — The bare-junction counting reflection $\Gamma=(2-z)/z=-1/3$
<!-- claim-quality: clm-v3port -->

A wave travelling down one srs bond arrives at the $z=3$ vertex and sees the **other two bonds in parallel**,
a load impedance $Z_0/2$. The transmission-line reflection coefficient (Op3, `reflection-coefficient.md`
`clm-gdd70j`) is then a **pure counting fact**:

> **[Resultbox]** *Bare vertex reflection ($z$-regular junction)*
>
> $$
> \Gamma = S_{11} = \frac{Z_0/(z-1) - Z_0}{Z_0/(z-1) + Z_0} = \frac{2-z}{z}, \qquad
> \Gamma\big|_{z=3} = -\tfrac13, \qquad |\Gamma|^2 = \tfrac19 .
> $$

- **One bond feeding two.** $\Gamma=(2-z)/z$ is a counting fact of the coordination number alone — **immune
  to any symmetric transformation** of the vertex. The memoryless junction **reactively back-scatters /
  redistributes** $|\Gamma|^2 = 1/9$ of the incident power (Axiom 3 — lossless; **not** a "loss") and is
  therefore **NOT matched**.
- **Recovered two ways.** Analytic `bare_junction_s11(3) = -0.3333…`; the loaded S₁₁ path recovers
  $|S_{11}| = 1/3$ as $f\to0$ to `0.0e+00` relative error (X38 gate G-B).
- **The L-match is a network fact, refuted at the vertex.** The ideal two-element L-match ($Q=\sqrt{Z_{hi}/Z_{lo}-1}
  = \sqrt{2-1} = 1$) nulls $|S_{11}|\to0$ for the correct step-orientation — **confirmed as a network fact**.
  But the substrate's parasitic geometry is the **opposite (step-DOWN) orientation** (accumulator on the low-Z
  node), and $C_{3v}$ **forbids a privileged one-arm shunt**, so the L-match dip below $1/3$ is **REFUTED at
  the physical vertex** (§2).

## §2 — The reciprocal 3-port floor $|S_{11}|\ge 1/3$ (Pozar-class theorem, confirmed at the vertex)
<!-- claim-quality: clm-v3port -->

The srs vertex is a **symmetric lossless reciprocal 3-port**. The classic **matched-lossless-reciprocal-3-port
theorem** of microwave network theory (Pozar §7.1 class) states: *a lossless, reciprocal, matched 3-port is
impossible; for the symmetric $C_3$ case the reflection is floored at $|\Gamma|\ge 1/3$.* This is **known
theory, confirmed at the srs vertex** (provable — it **strengthens**, it does not originate, the bound):

> **[Resultbox]** *The exact perfect-square identity (X38 §2, sympy)*
>
> $$
> |S_{11}(\theta;f)|^2 - \tfrac19
> = \frac{8t^2\,\bigl(s_C\,s_L^2\,t^2 + s_C - 3s_L\bigr)^2}{[\,\cdots\,]}, \qquad t = f\theta ,
> $$
> a **perfect square** $\Rightarrow |S_{11}|\ge 1/3$ for **all** $\theta,f$ and all shape factors $s_L,s_C>0$,
> with equality at $\theta\to0$ **and** on the half-wave-invisible locus $t^2=(3s_L-s_C)/(s_C s_L^2)$.

- **No bore of the lossless-reciprocal class beats the floor.** $\min_\theta |S_{11}|^2 = 1/9$ for every $f$
  — the Op6 reflectionless target ($\lambda_{\min}\to0$) is **UNREACHABLE by any bore of the lossless
  reciprocal class**. The floor is an intrinsic $z=3$ **reactive back-scatter / redistribution**, the
  structural price of branching in a lossless reciprocal vertex.
- **Attribution (not new).** This is the classic Pozar-class three-port theorem confirmed at the vertex, **not
  a new structural fact** (X38 correction C5/R5). Its provability at the srs geometry is the strengthening.

## §3 — The sole escape: non-reciprocity (circulator witness — PENDING-GRANT)
<!-- claim-quality: clm-v3port -->

Matched lossless $C_3$-symmetric 3-ports **do exist** — but **only non-reciprocally**. The ideal circulator is
the witness:

$$
S_{\text{circ}} = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix},
\qquad \text{unitary, } C_3\text{-symmetric, } S_{11}=0, \text{ non-reciprocal.}
$$

- **The reciprocal-class escape is theorem-dead (#620).** Any lossless **+** reciprocal **+** $C_3$ network of
  **any** internal complexity — stubs, finite junction volumes, resonant shunt branches — obeys the theorem.
  The evanescent-mode-stub escape hatch named in earlier X37/X38 drafts is **provably dead across the entire
  lossless reciprocal $C_3$ vertex class** (X37 correction C8, landed as PR #620).
- **The one surviving escape class = non-reciprocity.** A gyrotropic / circulator vertex is the **sole**
  remaining way a junction could route around the floor.
- **T-breaking bias — named, NOT asserted (PENDING-GRANT).** Axiom-1's srs chirality (right-handed $I4_132$,
  `axiom-definitions.md`) is **parity (P)-breaking**, but a circulator **additionally** requires a
  **time-reversal (T)-breaking** bias. Candidate: the frozen-bias sector $u_0^{*}/\Omega_{\text{freeze}}$.
  Whether the vacuum supplies such a T-breaker at the vertex (a circulator-like matched, chirality-sorting
  junction) or the vertex is a genuine reciprocal $1/9$ back-scatterer is a **PENDING-GRANT** walk question —
  **asserted nowhere here** (flag-don't-fix).

## §4 — The two-axis Op6 bore verdict (broadband unique $f^{*}=0$; single-frequency degenerate)
<!-- claim-quality: clm-bore2x -->

Applying canon's own selection operator — **Universal Operator #6**, $\lambda_{\min}(S^\dagger S)\to0$
([`eigenvalue-target.md`](eigenvalue-target.md) `clm-gdd70j`) — at the vertex **as a CANDIDATE selector**
(per canon's own honest-scope note, the S₁₁ landscape is FLAT in $R\!\cdot\!r$ and Op6 did **NOT** select the
trefoil $R\!\cdot\!r=1/4$; X38 C6/R6). The vertex bore is a junction extent $d=f\,\ell_{\text{node}}$ carrying
a shunt accumulator $C_j=s_C\varepsilon_0 d$ + a series throat $L_j=s_L\mu_0 d$ (the X37 leading-order lumped
equivalent). The verdict is **TWO-AXIS**:

| Op6 objective | selection | branch |
|---|---|---|
| **band-integrated comparator** $\langle|S_{11}|^2\rangle$ | **uniquely $f^{*}=0$** (point junction) at **every** swept $(s_L,s_C)\in[0.3,3]^2$ | **(ii)** |
| **frozen-primary single-frequency** $|S_{11}(\pi;f)|^2$ | **EXACTLY degenerate** $\{0,\ f_{\text{touch}}=\sqrt2/\pi\approx0.450\}$ (`obj1@touch − 1/9 = −4.2e-17`, machine zero) | **(iv)** |

- **The half-wave-invisible bore family.** The single-frequency degeneracy is the finite extent
  $f_{\text{touch}}=\sqrt{3s_L-s_C}/(\pi\,s_L\sqrt{s_C})$ at which the junction section is **half-wave at the
  probe tone** and thus impedance-transparent **there** — a genuine second global minimum touching the $1/9$
  floor (a perfect-square identity, §2), **not** a near-miss. The trick is **single-tone only**: broadband
  matching washes it out, so the band-integrated comparator still prefers **no bore**. (**Transcription note:**
  the source doc's ASCII rendering `√(3s_L−s_C)/(π√s_C·s_L)` is ambiguous in the denominator grouping; the
  **governing form** is the canonical module `junction_scattering.py:192` / the exact locus
  $t^2=(3s_L-s_C)/(s_C s_L^2)$ at $t=f\theta,\ \theta=\pi$, i.e. $s_L$ sits **outside** the root:
  $f_{\text{touch}}=\sqrt{3s_L-s_C}/(\pi\,s_L\sqrt{s_C})$. Checks: $(1,1)\to\sqrt2/\pi=0.45016$;
  $(s_L,s_C)=(2,3)\to 1/(2\pi)=0.15915$ — the value this leaf's §4 branch-(i) locus asserts.)
- **The broadband-selected ceiling.** On the broadband axis the operator wants the point junction, so the X37
  walk ceiling $\pi\sqrt3\,\omega_C = 5.4414\,\omega_C$ ($g(0)$) is the **broadband-selected** ceiling; the
  X37 finite-extent floor drops to $g(0.5)=3.7304\,\omega_C$ at $s=1$ (extent swing 31.4% of $\pi\sqrt3$,
  branch (iii) there — the junction *magnitude* is extent-dominated / sector-ownership-gated).
- **Branch (i) UNADJUDICATED on the $(2,3)$ locus (PENDING-GRANT).** At swept cell $(s_L,s_C)=(2,3)$,
  $f_{\text{touch}}=1/(2\pi)$ **EXACTLY**, inside $f_{\text{crit}}\approx0.184$ — an exact obj-1 co-minimum
  **ON** the tube-radius (branch-i) mark in the self-consistent regime. A formula locus (s-cell-dependent),
  **neither asserted as branch (i) nor dismissed** — PENDING-GRANT.
- **Framing.** "**Demonstrated (entailed by the model class), not adjudicated**" (X38 R7) — the substrate is
  not being said to "decide." Scoped to the **leading-order lumped reciprocal class** (X37's repaired scope:
  the circuit FORM is a **disclosed modeling choice**; passivity of the positive two-element form gives the
  low-pass / floored-reflection class — it is **not** a from-geometry derivation of $s_L,s_C$).

## §5 — Consistency-vs-emergence + solidity

- **`clm-v3port` (the floor) — CONSISTENCY / characterization.** $\Gamma=(2-z)/z=-1/3$ is a **pure counting
  fact** (dimensionless; the S₁₁ module imports **no** physical scale — $\mu_0/\varepsilon_0/\ell_{\text{node}}$
  cancel). $|S_{11}|\ge1/3$ is **attributed known microwave-network theory** (Pozar §7.1 class), **confirmed**
  (provably) at the srs vertex — a strengthening of a known bound, **not** an emergence claim. The circulator
  escape is a **scoped open fork** (§3, PENDING-GRANT) — **no claim asserted**.
- **`clm-bore2x` (the two-axis bore verdict) — derived FORM within the disclosed model class.** The selected
  $f^{*}$ is **derived-geometric** (a pure number; no scale imported); the **SCALE** $\omega_C=c/\ell_{\text{node}}$
  is a **dimensional-forced identity** appearing only as the reporting unit. No emergent-scale headline (the
  broadband branch is $f^{*}=0$). "Demonstrated, not adjudicated"; branch (i) PENDING-GRANT.
- **No $\alpha$ / `Q_TANK` on any verdict path; no CODATA; forward computation only.** Every X38 gate consumes
  a COMPUTED quantity with a firing tolerance (planted-violation proofs, incl. the G-B parasitics-disabled
  sabotage); 26 X38 tests + 24 X37 tests pass, `make verify` green in both source lanes.

> **Quality, depends-on, and solidity for `clm-v3port` and `clm-bore2x` live in the volume claim register**
> ([`../../claim-quality.md`](../../claim-quality.md)).

## Cross-references

- [`eigenvalue-target.md`](eigenvalue-target.md) (clm-gdd70j) — Universal Operator #6 ($\lambda_{\min}(S^\dagger S)\to0$),
  the selection operator applied at the vertex in §4 **as a candidate selector** (it did not select the trefoil
  $R\!\cdot\!r$; honest-scope note).
- [`reflection-coefficient.md`](reflection-coefficient.md) (clm-gdd70j) — the Op3 two-port $\Gamma=(Z_2-Z_1)/(Z_2+Z_1)$
  that §1 extends to the $z$-regular junction $\Gamma=(2-z)/z$.
- [`srs-band-structure.md`](srs-band-structure.md) (clm-bnd5rq) — the scalar band top $\pi\sqrt3\,\omega_C=5.4414\,\omega_C$
  that is the point-junction (broadband-selected) walk ceiling of §4; the extent-dominated $g(0.5)$ floor is
  the X37 junction-parasitic companion.
- [`../../../common/translation-tables/translation-circuit.md`](../../../common/translation-tables/translation-circuit.md)
  (clm-eemap1) — the EE tool→operator tracker; the vertex reciprocal 3-port floor / circulator alternative row
  lives in §4.5(b) (Impedance & transmission family).
- `research/2026-07-13_srs-vertex-ksweep-backscatter_RESULT.md` — the **collective-mode / in-band
  homogenization complement** to this leaf's bare single-vertex $|\Gamma|^2 = 1/9$ floor (§1–§2). The
  per-vertex $\Gamma=-1/3$ is a **real reactive event** but is **homogenized away for in-band collective
  carriers** ($\sigma\approx0.12$ of the incoherent limit) and **resolves only near the band edge** (crosses
  $1/9$ at $k\cdot\ell\approx1.85$); adjudicates docket **T4** at **CONSISTENCY / peer-with-SM** (bin (i)
  HOMOGENIZATION-SPLIT, PR #669, 2026-07-13; band edge not independently located — probe reached
  $k\cdot\ell\le0.83$). Cross-ref only — **no new claim minted here.**

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../../../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../../../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is reproduced from the banked audit and is
**content-verified at HEAD (markup-reduced, not byte-identical)**; it is never reworded.

**Rows carried in this file.**

- **`:24`** — stamped at `:24`. *(family: compression-channel-scoping; banked `uncertain`)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  SECTOR = bare-bond network primitive, **scalar / compression channel**; the vertex 3-port is scoped to the **lossless reciprocal class**
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  UNCERTAIN: the |S11|>=1/3 reflection floor is channel-agnostic network theory (reflection = surviving class) and survives for any surviving channel; but the sector header scopes the travelling bond waves to the COMPRESSION channel — if read literally that carrier is the removed branch. Conflicts with srs-band-structure treating the same scalar channel's acoustic branch as the emergent light speed (1/sqrt(3)); sector-label adjudication owed, not a leaf edit.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

