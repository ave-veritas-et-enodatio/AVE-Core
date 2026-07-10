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
> 2 distinct speeds $c_P\neq c_S$, anisotropic per-site self-block ⇒ no single $\omega_{\text{link}}$).

| estimate | value ($\omega_C$) | value (MeV) | basis |
|---|---|---|---|
| normalized-arccos (substrate-native, **LOWER**) | 5.4414 | 2.781 | $\tilde\lambda_{\max}=2.0000$ (srs bipartite) ⇒ $\pi\sqrt3$ for ANY $\rho$ — normalization divides out the stiffness that should lift the top |
| P-wave-scaled | 9.9346 | 5.078 | $\pi\sqrt3\cdot\sqrt{10/3}$ (macroscopic P/S factor) |
| lumped-calibrated | 12.4060 | 6.340 | $\pi\sqrt3\cdot\sqrt{\lambda_{\max}(D)/6}$ (elastic $\sqrt{\text{eig}}$, computed) |
| raw-link ($\sqrt{\rho^*}$, loosest **UPPER**) | 17.0111 | 8.693 | $\pi\sqrt3\cdot\sqrt{\rho^*}$ (raw stiffness link-speed cutoff) |

- **NO full stop-band (both maps).** All 11 adjacent band-pair envelopes overlap; the 12-band manifold is
  fully connected $0\to\text{top}$. The $k_a\gg k_s$ split did NOT open a full internal gap.
- **⚠ single-scale vs stiffness-lifted is PENDING Grant (do NOT resolve).** Under the normalized-TLM map the
  top is pinned at $\pi\sqrt3\,\omega_C$ by $\ell_{\text{node}}+c_0$ alone (a striking "one-scale vacuum"
  reading); under per-channel link speeds the stiff longitudinal channel lifts the Bragg cutoff to
  $\pi\sqrt3\cdot\sqrt{\rho^*}$. Grant's ruling sets the fork-A floor (5.441 vs ~17); it does **NOT** change the
  band SHAPE, the velocity table (§4), or the gap inventory.
- Gates PASS: 12 bands $\forall\mathbf k$; scalar reduction exact ($2.7\times10^{-15}$, top 5.4414);
  $\nu_{\text{Hill}}=0.285714$, $K/G=2.0000$, Zener $A=1.2293$; enantiomorphs identical ($1.9\times10^{-8}$,
  the 12×12 roundoff floor, Rule-7 post-hoc relaxation $1\text{e-}9\to1\text{e-}6$ disclosed); $\rho^*$ imported.

## §4 — Per-branch velocity map: which $\sqrt{}$-factor is which (deliverable c)

Three $\sqrt{}$-factors are in play; they are **distinct objects** and the survey resolves which is which:

| factor | value | what it is | longitudinal? |
|---|---|---|---|
| **$\sqrt3$** | 1.7321 | **network / coordination projection** $c_{\text{link}}\to c_0$ (D=3 isotropic average over $z=3$); the emergent light-speed factor. Multiplies **ALL** branches equally — an overall scale, **NOT a channel/polarization selector**. | **NO — universal network factor** |
| **$\sqrt{10/3}$** | 1.8257 | **P-wave (LONGITUDINAL)** speed ratio $c_P/c_S$ at the **VRH (Voigt-Reuss-Hill) average ONLY**: $(K+4G/3)/G=10/3$. A **K=2G RE-EXPRESSION** (GR-imported, PR #261), **NOT lattice-emergent** — no single lattice direction gives $10/3$; only the VRH average does. | YES — longitudinal branch factor |
| **$\sqrt2$** | 1.4142 | **A1-scalar BULK-SOUND** `V_LONG`$=\sqrt{2G/\rho}$, the pure-dilatation A1 port mode that DROPS the $4G/3$ shear term — a **scalar-sector** object **imported from `constants.py:770`**, **NOT a Bloch branch** of this translational problem (not lattice-computed here). | NO — different sector (A1 dilatation) |
| **$1$** | 1.0000 | **S / transverse (shear)** branch $=c_S=c_0$ — the **light-like PROXY** (velocity factor $1/\sqrt3$ vs $c_{\text{link}}$). ⚠ PROXY: the true photon is the **T2 Cosserat MICROROTATION**, a **named follow-on** not surveyed at this Cauchy-translational level. | transverse |

Direction-resolved $c_P/c_S$ (the Zener $A=1.23$ anisotropy, direction-real, lattice-computed): **[100] 1.71,
[110] 1.85, [111] 1.90**. Only the Hill average recovers the clean $\sqrt{10/3}$; the per-direction spread IS
the material anisotropy.

## §5 — Consumers

- **(a) FORK-A tone floor (γγ carrier = T2 / vector-sector).** Conservative (stiffness-lifted) floor $=17.01\,
  \omega_C$; recommended $\omega_a\approx18.51\,\omega_C$, $\omega_b\approx17.51\,\omega_C$ (both clear 17.01,
  difference $1.0\,\omega_C$ in-band). The scalar-provisional $5.94/6.94\,\omega_C$ (#604 §3a) is **NOT
  vector-safe** — it sits below even the P-wave-scaled 9.93 and the lumped-computed 12.41. If Grant rules the
  top is single-scale, the floor drops to the scalar $5.94/6.94$.
- **(b) pair-channel / propagating-mode coexistence window (CONDITIONAL).** Pair threshold $2\omega_C=1.022\,
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
