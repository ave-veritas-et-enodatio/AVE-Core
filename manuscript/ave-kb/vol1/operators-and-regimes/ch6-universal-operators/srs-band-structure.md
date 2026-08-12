[↑ Ch.6 Universal Operators](index.md)
<!-- claim-quality: clm-bnd5rq -->

<!-- kb-frontmatter
kind: leaf
claims: [clm-bnd5rq]
path-stable: "the canonical srs vacuum-net linear band-structure survey — scalar 4-band top π√3 ω_C, vector 12-band top BRACKET [5.441,17.011] ω_C, NO internal gap either channel"
-->

# srs Vacuum-Net Linear Band Structure — scalar top $\pi\sqrt3\,\omega_C$, vector top BRACKET, NO internal gap

> **What this leaf is (class + scope, load-bearing honesty).** The canonical characterization of the
> **chiral srs vacuum net's own linear band structure** ($I4_132$, $z=3$, 4-site BCC primitive cell) in both
> the **scalar** channel (4 bands) and the **vector / Cosserat-translational** channel (12 bands). It is a
> **CONSISTENCY / characterization** result (a measurement of the substrate's linear dispersion by generic
> power-network eigenvalue math), **NOT a falsification and NOT an emergence claim**. It consolidates the two
> merged surveys — scalar (#604) and vector (#607) — into one canonical band-structure leaf and records the
> **load-bearing methods fact** those surveys established: the substrate-native band model is the
> **transmission-line arccos** (coined-quantum-walk) map, not the graph-Laplacian $\omega=\sqrt\lambda$.
>
> Provenance (survey drivers + result docs, merged): scalar
> [`src/scripts/vol_1_foundations/srs_band_survey.py`](../../../../../src/scripts/vol_1_foundations/srs_band_survey.py)
> / `research/2026-07-09_srs-band-survey_result.md`; vector
> [`src/scripts/vol_1_foundations/srs_vector_band_survey.py`](../../../../../src/scripts/vol_1_foundations/srs_vector_band_survey.py)
> / `research/2026-07-09_srs-vector-band-survey_result.md`.

## §1 — Scalar channel: band top $\pi\sqrt3\,\omega_C$ at H, NO internal gap
<!-- claim-quality: clm-bnd5rq -->

The scalar Bloch survey of the 4-site primitive cell resolves the global band top and the gap inventory:

> **[Resultbox]** *Scalar band top (closed form)*
>
> $$
> \omega_{\text{top}}^{\text{scalar}} = \pi\sqrt3\,\omega_C = 5.4414\,\omega_C = 2.781\ \text{MeV},
> \qquad\text{at the }H\text{ point }(2\pi/a)(1,0,0)\ (\mu=-3,\ \lambda=6).
> $$
> Bands: $\omega_n(\mathbf k)=\omega_{\text{link}}\arccos(\mu_n(\mathbf k)/3)$, $\omega_{\text{link}}=\sqrt3\,\omega_C$,
> $\mu_n$ = eigenvalues of the $4\times4$ Bloch adjacency. Closed form $\pi/\texttt{ANALYTIC\_NETWORK\_FACTOR}$.

- **GAP INVENTORY (complete): NO full stop-band.** The four scalar bands form a single connected manifold
  $0\to5.441\,\omega_C$ (all adjacent envelopes overlap: band0↔1, band1↔2, band2↔3). "No internal gap" is a
  first-class result. Band envelopes ($\omega_C$): 0 [0, 2.132]; 1 [1.655, 3.309]; 2 [2.132, 3.787];
  3 [3.309, **5.441**]. $\Gamma$: one acoustic branch ($\omega=0$) + a **triply-degenerate optical multiplet at
  $3.3093\,\omega_C = \sqrt3\arccos(-1/3)$**.
- Gates PASS: (i) acoustic velocity factor $1/\sqrt3$ to $3\times10^{-9}$, isotropic; (ii) $\lambda_{\max}=6.000000$
  vs direct `build_srs_net`; (iii) 4 bands $\forall\mathbf k$, both enantiomorphs identical to $10^{-9}$.

## §2 — MODEL ADJUDICATION (the load-bearing methods fact): arccos TL map is substrate-native

The naive **graph-Laplacian** band model $\omega=\sqrt\lambda$ (the model the task brief and the x29 review's
quick methods sketched) **FAILS the frozen $1/\sqrt3$ velocity gate** — it gives $1/\sqrt2$, a genuine geometric
fact (the srs acoustic Laplacian curvature is $C=1/2$, not $1/3$) but the $\omega\to0$ *lumped* limit only, **not**
the substrate-native vacuum. The substrate-native srs vacuum is a **distributed LC transmission-line network**
(the Op5 scatter+connect TLM, `chiral_lattice_dynamics.py`, which measures $0.5778\approx1/\sqrt3$ on
`build_srs_net`); its dispersion is the **coined-quantum-walk / transmission-line arccos map**
$\omega=\omega_{\text{link}}\arccos(\mu/3)$, which recovers the canonical $1/\sqrt3$ exactly.

| model | operator | srs velocity factor | srs band top |
|---|---|---|---|
| **lumped** (graph-Laplacian / tight-binding) | $\omega=\sqrt\lambda$, $\lambda=\text{eig}(3I-A)$ | $1/\sqrt2=0.7071$ ✗ | $\sqrt{12}=3.464\,\omega_C$ |
| **distributed** (transmission-line / TLM) | $\omega=\omega_{\text{link}}\arccos(\mu/3)$ | $1/\sqrt3=0.5774$ ✓ | $\pi\sqrt3=5.441\,\omega_C$ |

**Gate (i) is not decorative — it SELECTS the model.** This is the load-bearing methods fact of the whole
survey: the arccos TL map, not $\omega=\sqrt\lambda$, is the substrate-native band model, and it fixes the
$\omega_C$ normalization. The prior "$\approx3.3$–$3.5\,\omega_C$" band-top estimate (x29 superband note) was the
$\Gamma$-optical / [001]-zone-edge fold $\arccos(-1/3)\cdot\sqrt3=3.309$, **not** the global maximum (at $H$).

> **ω-vs-k discipline (do NOT conflate — cross-check).** The $\pi\sqrt3=5.441\,\omega_C$ here is a **frequency**
> band top ($\omega$-space, at $H$). It is a **distinct quantity** from the k-space Nyquist **wavevector** edge
> recorded at [`boundary-observables-m-q-j.md`](../../../common/boundary-observables-m-q-j.md) (clm-3bwhad,
> $\sqrt2\,\pi/\ell_{\text{node}}\approx4.44$ on the srs axis; $\sqrt3\,\pi/\ell_{\text{node}}\approx5.44$ cubic
> control) — that is a $k_{\max}$ in $1/\text{length}$. The numeric coincidence $\sqrt3\,\pi\approx5.44$ appears
> in both (cubic-control wavevector edge AND scalar frequency band top) but they are different axes. The
> corresponding $\omega$ cutoff of the k-space zone edge is $\pi\cdot\omega_{\text{link}}$ (first Bragg /
> half-wave-line resonance), physical, **not** a temporal-Nyquist artifact.

## §3 — Vector / Cosserat-translational channel: 12 bands, NO gap, band top BRACKETED

The 12-band vector survey (4 sites × 3 DOF, rank-2 bond tensor $\Phi_b=k_a\hat d\otimes\hat d+k_s(\mathbf I-\hat
d\otimes\hat d)$ at the canonical bond ratio $\rho^*=9.77337$, DERIVED from $\nu_{\text{Hill}}=$`N_NU`$=2/7$):

> **[Resultbox]** *Vector band top — BRACKET (single-scale vs stiffness-lifted PENDING Grant)*
>
> $$
> \omega_{\text{top}}^{\text{vector}} \in [\,5.441,\ 17.011\,]\,\omega_C = [\,2.781,\ 8.693\,]\ \text{MeV}.
> $$
> because the scalar arccos map does **NOT** cleanly generalize to the vector channel (3 acoustic branches,
> 2 distinct speeds $c_P\neq c_S$, anisotropic per-site self-block ⇒ no single $\omega_{\text{link}}$). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**

| estimate | value ($\omega_C$) | value (MeV) | basis |
|---|---|---|---|
| normalized-arccos (substrate-native, **LOWER**) | 5.4414 | 2.781 | $\tilde\lambda_{\max}=2.0000$ (srs bipartite) ⇒ $\pi\sqrt3$ for ANY $\rho$ — normalization divides out the stiffness that should lift the top |
| P-wave-scaled | 9.9346 | 5.078 | $\pi\sqrt3\cdot\sqrt{10/3}$ (macroscopic P/S factor) 🔴 **[DEMOTED 2026-08-11 — R40-B1; note at EOF]** |
| lumped-calibrated | 12.4060 | 6.340 | $\pi\sqrt3\cdot\sqrt{\lambda_{\max}(D)/6}$ (elastic $\sqrt{\text{eig}}$, computed) |
| raw-link ($\sqrt{\rho^*}$, loosest **UPPER**) | 17.0111 | 8.693 | $\pi\sqrt3\cdot\sqrt{\rho^*}$ (raw stiffness link-speed cutoff) |

- **NO full stop-band (both maps).** All 11 adjacent band-pair envelopes overlap; the 12-band manifold is
  fully connected $0\to\text{top}$. The $k_a\gg k_s$ split did NOT open a full internal gap.
- **⚠ single-scale vs stiffness-lifted is PENDING Grant (do NOT resolve).** Under the normalized-TLM map the
  top is pinned at $\pi\sqrt3\,\omega_C$ by $\ell_{\text{node}}+c_0$ alone (a striking "one-scale vacuum"
  reading); under per-channel link speeds the stiff longitudinal channel lifts the Bragg cutoff to
  $\pi\sqrt3\cdot\sqrt{\rho^*}$. Grant's ruling sets the fork-A floor (5.441 vs ~17); it does **NOT** change the
  band SHAPE, the velocity table (§4), or the gap inventory. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**
- Gates PASS: 12 bands $\forall\mathbf k$; scalar reduction exact ($2.7\times10^{-15}$, top 5.4414);
  $\nu_{\text{Hill}}=0.285714$, $K/G=2.0000$, Zener $A=1.2293$; enantiomorphs identical ($1.9\times10^{-8}$,
  the 12×12 roundoff floor, Rule-7 post-hoc relaxation $1\text{e-}9\to1\text{e-}6$ disclosed); $\rho^*$ imported.

## §4 — Per-branch velocity map: which $\sqrt{}$-factor is which (deliverable c)

Three $\sqrt{}$-factors are in play; they are **distinct objects** and the survey resolves which is which:

| factor | value | what it is | longitudinal? |
|---|---|---|---|
| **$\sqrt3$** | 1.7321 | **network / coordination projection** $c_{\text{link}}\to c_0$ (D=3 isotropic average over $z=3$); the emergent light-speed factor. Multiplies **ALL** branches equally — an overall scale, **NOT a channel/polarization selector**. | **NO — universal network factor** |
| **$\sqrt{10/3}$** | 1.8257 | **P-wave (LONGITUDINAL)** speed ratio $c_P/c_S$ at the **VRH (Voigt-Reuss-Hill) average ONLY**: $(K+4G/3)/G=10/3$. A **K=2G RE-EXPRESSION** (GR-imported, PR #261), **NOT lattice-emergent** — no single lattice direction gives $10/3$; only the VRH average does. | YES — longitudinal branch factor 🔴 **[DEMOTED 2026-08-11 — R40-B1; note at EOF]** |
| **$\sqrt2$** | 1.4142 | **A1-scalar BULK-SOUND** `V_LONG`$=\sqrt{2G/\rho}$, the pure-dilatation A1 port mode that DROPS the $4G/3$ shear term — a **scalar-sector** object **imported from `constants.py:770`**, **NOT a Bloch branch** of this translational problem (not lattice-computed here). | NO — different sector (A1 dilatation) |
| **$1$** | 1.0000 | **S / transverse (shear)** branch $=c_S=c_0$ — the **light-like PROXY** (velocity factor $1/\sqrt3$ vs $c_{\text{link}}$). ⚠ PROXY: the true photon is the **T2 Cosserat MICROROTATION**, a **named follow-on** not surveyed at this Cauchy-translational level. | transverse |

Direction-resolved $c_P/c_S$ (the Zener $A=1.23$ anisotropy, direction-real, lattice-computed): **[100] 1.71,
[110] 1.85, [111] 1.90**. Only the Hill average recovers the clean $\sqrt{10/3}$; the per-direction spread IS
the material anisotropy. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**

## §5 — Consumers

- **(a) FORK-A tone floor (γγ carrier = T2 / vector-sector).** Conservative (stiffness-lifted) floor $=17.01\,
  \omega_C$; recommended $\omega_a\approx18.51\,\omega_C$, $\omega_b\approx17.51\,\omega_C$ (both clear 17.01,
  difference $1.0\,\omega_C$ in-band). The scalar-provisional $5.94/6.94\,\omega_C$ (#604 §3a) is **NOT
  vector-safe** — it sits below even the P-wave-scaled 9.93 and the lumped-computed 12.41. If Grant rules the
  top is single-scale, the floor drops to the scalar $5.94/6.94$.
- **(b) pair-channel / propagating-mode coexistence window (CONDITIONAL).** Pair threshold $2\omega_C=1.022\, 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
  \text{MeV}$ opens **below** the band top ⇒ propagating lattice modes **coexist** with the pair channel. Scalar
  window $[1.022, 2.781]\,\text{MeV}$; under the stiffness-lifted vector reading it widens to $[1.022, \text{up
  to } 8.693]\,\text{MeV}$ — or stays $[1.022, 2.781]\,\text{MeV}$ under the single-scale reading. ⚠ Conditional,
  pending Grant's single-scale-vs-stiffness-lifted ruling.
- **(c) gap-breather.** NO full internal gap (either channel) ⇒ **gap-PINNED** (intrinsic-gap-breather) carrier
  candidates are **UNAVAILABLE** in both the scalar and vector srs channels. **⚠ scoping:** this kills
  GAP-PINNED modes ONLY; the **above-band mobile breather** (freq > the true top, in the semi-infinite gap
  above the connected manifold) is **NOT falsified** and remains the live carrier-fork branch. The carrier-fork
  gate must not read no-internal-gap as killing the above-band breather.

## §6 — Consistency-vs-emergence + solidity

**CONSISTENCY / characterization.** $\omega_C=c_0/\ell_{\text{node}}$ is an **IDENTITY** (`OMEGA_C`,
[`constants.py`](../../../../../src/ave/core/constants.py):294); $1/\sqrt3$ is a **Class-B geometric
MANIFESTATION** (`ANALYTIC_NETWORK_FACTOR`, `chiral_lattice_dynamics.py`:48); $\nu=2/7$ is **GR-imported**
(`N_NU`/`NU_VAC`, K=2G, PR #261/#506); $\sqrt{10/3}$ is a **manifestation of K=2G**. Every gate is **COMPUTED**
vs an independently-derived canonical number (velocity factor vs the imported symbol; $\lambda_{\max}$ vs the
direct `build_srs_net`; scalar reduction vs the scalar survey; $\nu_{\text{Hill}}$ vs the validated 8-site
Born-Huang). **No $\alpha$/`Q_TANK` on any verdict path; no CODATA; forward computation only.** This is a
characterization of the substrate's own linear dispersion, not a chord and not an emergence.

> **Adjudication flag carried (does not block the survey verdict).** The $\omega_C$ **scale label** adopts **R2**
> ($c_0=$ the long-wavelength acoustic-branch velocity $=c_{\text{link}}/\sqrt3$, so $\omega_C=c_0/\ell_{\text{node}}
> =511$ keV; the microscopic link speed $c_{\text{link}}=\sqrt3\,c_0$ is sub-lattice, unobservable). Under R1
> (calling $c_{\text{link}}=c_0$) every $\omega_C$ band label divides by $\sqrt3$ (top $\to\pi=3.142\,\omega_C$).
> Only the scale LABEL changes under R1, not the k-space band SHAPE or the gap inventory. Flagged for adjudication.

> **Quality, depends-on, and solidity for `clm-bnd5rq` live in the volume claim register**
> ([`../../claim-quality.md`](../../claim-quality.md)).

## Cross-references

- [`../../../vol2/quantum-orbitals/ch07-quantum-mechanics/brillouin-zone-uv-cutoff.md`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/brillouin-zone-uv-cutoff.md) (clm-1wmyx3) — the band-limited lattice propagator + the SPATIAL $k_{\max}=\pi/\ell_{\text{node}}$ loop bound; the temporal/spatial distinct-cutoff discipline. This survey supplies the **temporal $\omega(k)$ band structure** that leaf's spatial loop-integral bound is the k-space companion to.
- [`../../../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md`](../../../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md) (clm-k4d4ph) — the $(q\ell_{\text{node}})^4$ photon-anisotropy FORM + the same 24×24 chiral-srs Bloch eigensolve; §4 there is the temporal-cutoff-vs-spatial-zone-edge discipline this survey extends.
- [`../../../common/boundary-observables-m-q-j.md`](../../../common/boundary-observables-m-q-j.md) (clm-3bwhad) — the k-space Nyquist **wavevector** edge ($\sqrt2\,\pi/\ell_{\text{node}}$ srs, $\sqrt3\,\pi/\ell_{\text{node}}$ cubic control), the $\omega$-vs-k companion (§2 discipline note).
- [`../../../common/lattice-model-register.md`](../../../common/lattice-model-register.md) — the srs-embedding column that owns the Brillouin zone / band edge / dispersion $\omega(k)$; its frequency-fence entry cites this leaf.
- [`../../../vol4/falsification/ch12-falsifiable-predictions/vacuum-photon-photon-channel.md`](../../../vol4/falsification/ch12-falsifiable-predictions/vacuum-photon-photon-channel.md) (clm-gg4wmx) — the γγ / FORK-A consumer whose tone floor gates on the §5(a) vector-safe placement.

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:94`** — *"P-wave-scaled | 9.9346 | 5.078 | $\pi\sqrt3\cdot\sqrt{10/3}$ (macroscopic P/S factor)"*
  Stamped in place at `:94`.
  **Why it dies (audited row rationale, verbatim):** Band-top estimate obtained by scaling with the P-wave propagation factor; with no propagating longitudinal branch the estimate has no referent.
- **`:102`** — *"under per-channel link speeds the stiff longitudinal channel lifts the Bragg cutoff to $\pi\sqrt3\cdot\sqrt{\rho^*}$"*
  Stamped in place at `:104`.
  **Why it dies (audited row rationale, verbatim):** The stiffness-lifted arm of the PENDING-Grant single-scale-vs-stiffness-lifted fork requires the longitudinal channel to be a propagating channel with a Bragg cutoff; carve voids that arm — FLAG: this is a fork-adjudication implication, route to the lane, do not resolve by leaf edit.
- **`:116`** — *"**P-wave (LONGITUDINAL)** speed ratio $c_P/c_S$ at the **VRH (Voigt-Reuss-Hill) average ONLY**: $(K+4G/3)/G=10/3$"*
  Stamped in place at `:116`.
  **Why it dies (audited row rationale, verbatim):** Prereg-named site: the sqrt(10/3) as a longitudinal-branch speed ratio has no referent under the carve; the row's own 'K=2G RE-EXPRESSION, NOT lattice-emergent' provenance survives as static-import bookkeeping.
- **`:120`** — *"Direction-resolved $c_P/c_S$ (the Zener $A=1.23$ anisotropy, direction-real, lattice-computed): **[100] 1.71, [110] 1.85, [111] 1.90**"*
  Stamped in place at `:122`.
  **Why it dies (audited row rationale, verbatim):** Lattice-computed directional propagation anisotropy of the P branch — a per-direction physical transit-speed claim; no branch, no anisotropy of it.

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).

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

- **`:89`** — stamped at `:89`. *(family: band-structure-longitudinal)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  the scalar arccos map does **NOT** cleanly generalize to the vector channel (3 acoustic branches, 2 distinct speeds $c_P\neq c_S$
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Vector-channel characterization counts the longitudinal acoustic branch as spectrum content (c_P as a branch speed); transverse/shear content survives — band-top bracket and branch census owed a recount with the compression branch constraint-removed.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:131`** — stamped at `:131`. *(family: band-structure-longitudinal)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  Pair threshold $2\omega_C=1.022\,\text{MeV}$ opens **below** the band top ⇒ propagating lattice modes **coexist** with the pair channel
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Coexistence-window consumer: the window survives for surviving (transverse / signal-channel) modes but its width under the stiffness-lifted reading counts longitudinal members; recount owed (also conditional on the same fork as :102).
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

