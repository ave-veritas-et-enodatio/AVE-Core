# Two-band / k·p kinematics of the K4 carrier sector — RESULT

**Date:** 2026-08-05 · **Branch:** `research/two-band-kinematics` · **SVA pilot case 4**
**Pre-registration (frozen ALONE, before any code):**
[`2026-08-05_two-band-kinematics_prereg-FROZEN.md`](2026-08-05_two-band-kinematics_prereg-FROZEN.md)
at commit `f5ddd995805d724e9e4edb769f384a6517eef1e9`.
**Driver:** [`src/scripts/vol_1_foundations/two_band_kp_kinematics.py`](../src/scripts/vol_1_foundations/two_band_kp_kinematics.py)
**Shipped artifact:** [`research/drivers/two_band_kp_kinematics_results.json`](drivers/two_band_kp_kinematics_results.json)
(deterministic double-run digest `7d55f51139cc65e92082de1ef95605651f9870810c6e8de72decd20d1a27b135`).

---

## 0. Verdict, one screen

> **BIN: `FORM-REPRODUCED-V-MISMATCH`.**
>
> The relativistic massive form **is** reproduced exactly and isotropically on the carrier
> (Cosserat micro-rotation) sector: $\omega^2(k) = \omega_0^2 + v^2k^2 + O(k^4)$ with
> $\omega_0^2 = m^2 = 4G_c/I_\omega$. The carrier limiting velocity **is not** the EM-channel
> speed, and the mismatch is **structural, not numerical**: the carrier splits into TWO
> limiting velocities whose difference is exactly the gap-opening modulus,
> $$v^2_\perp - v^2_\parallel \;=\; \frac{G_c}{\rho} \;=\; \frac{I_\omega}{4\rho}\,m^2 .$$
> A single carrier limiting velocity therefore requires $G_c = 0$ — i.e. **no gap**. No choice
> of positive moduli gives a massive carrier one limiting speed, let alone $c_{EM}$.
>
> At the engine's placeholder moduli: $v_\parallel/c_{EM} = `1.4142135623730951`$ (=$\sqrt2$,
> multiplicity 2) and $v_\perp/c_{EM} = `1.7320508075688772`$ (=$\sqrt3$, multiplicity 4),
> against a frozen tolerance of `1e-09`. Reported plainly, not softened.
>
> **Read alongside §6, which materially qualifies how far this travels:** on this lattice the
> relativistic form's *validity window closes before its own relativistic regime opens*
> ($k_{\text{break}}/k_{\text{rel}} = `0.38729833462076746`$ and `0.42426406871200073`), and
> the full-BZ carrier group velocity never exceeds $c_{EM}$
> (max $|\nabla_k\omega| = `0.6116704022406638`$ vs $c_{EM} = 1$). The mismatch is in the
> **low-energy effective theory's invariant speed**, not in an observed superluminal transport.

**Separate axis — VALUE-PROVENANCE: `FACTOR DERIVED / VALUE IMPORTED`** (§1; frozen in the
prereg before any computation).

---

## 1. VALUE-PROVENANCE (STEP 0) — settled pre-derivation, quarantined from the form

Re-located per the brief: the gap statement has line-shifted off `trampoline-framework.md:188`
(now the microrotation EOM) to **`manuscript/ave-kb/common/trampoline-framework.md:192`**,
verbatim *"**Mass gap in the rotation sector:** $m_\omega^2 = 4 G_c / I_\omega$ where $G_c$ is
the Cosserat couple-stress modulus. Period $T = 2\pi/\omega_m = \pi$ in natural units."*
Pure line-shift, correct-when-written. Canonical home: `cosserat-mass-gap.md` (`clm-jz0xaw`).

| component | verdict | receipt |
|---|---|---|
| the factor **4** | **DERIVED** — $2$ (antisymmetric-pair $\Sigma_{ij}$ doubling) $\times\,2$ (Lagrangian→EOM Hessian) | `cosserat-mass-gap.md`:61 |
| $G_c$, $I_\omega$ | **ENG-CHOICE placeholder** | `cosserat_field_3d.py`:12 *"Moduli pinning (natural units, ell_node = 1): G = G_c = gamma = rho_vac = 1"*; `:954` *"phase-I placeholder"*. **No `constants.py` symbol exists for either.** |
| $\omega_m = 2$ | forced by that placeholder choice, not by the substrate | $2\sqrt{G_c/I_\omega}$ |
| the MeV scale | **IMPORTED from CODATA $m_e$** | `cosserat-mass-gap.md`:143 *"the substrate parameters $\rho, I_\omega, G_c$ **calibrated to** $\ell_{node} = \hbar/(m_ec)$"*; :151 *"placeholders … rather than measured-from-substrate"* |

**No MeV value for the gap exists anywhere in the corpus** — the "~1 MeV" is an inference from
$\hbar\omega_m = 2\hbar c_0/\ell_{node} = 2\,m_ec^2 = 1.022$ MeV. Another instance of the
corpus's own FORM-deriving / VALUE-importing meta-finding. **Quarantined:** no gate and no bin
in this lane reads the MeV value; the whole derivation runs in dimensionless modulus ratios.

---

## 2. The two-band structure — what it actually is (and is not)

At $k=0$ both gradient symbols vanish identically ($G^{self}_j = -\tfrac14\sum_\ell p_\ell^j = 0$
and $G^{cross}_j(0) = \tfrac14\sum_\ell p_\ell^j = 0$), so $D(0)$ is **exactly diagonal**
(off-diagonal max `0.0`, G3):

- **6 eigenvalues at `0`** — pure translational $u$ character (off-character weight `0.0`).
- **6 eigenvalues at `4.0`** $= m^2 = 4G_c/I_\omega$ — pure micro-rotational $\omega$ character.

> **The gap is SECTOR-based, not sublattice-based.** The two-band split is $u$-manifold vs
> $\omega$-manifold, opened by the **ON-SITE** micropolar term $-\epsilon_{ijk}\omega_k$. The
> K4/diamond bipartite doubling supplies a **degenerate partner inside each manifold**, not the
> gap: the tetrahedral gradient is a first-moment operator with $\sum_\ell p_\ell = 0$, so it
> does not penalise a uniform A↔B offset and the translational optical branch is **not** gapped
> at $\Gamma$. This is **not** the graphene/staggered-on-site two-band picture, and the brief's
> "K4 bipartite two-band" framing should be read as sector-two-band. `GAP-SECTOR-MISMATCH` does
> **not** fire (the gap used is the Cosserat sector's own gap); `NO-TWO-BAND-STRUCTURE` does
> **not** fire (a genuine gapped two-manifold structure exists and is exhibited).

The interband coupling is genuinely $O(k)$ (`D1_interband_nonzero` true in every direction), so
this is a real k·p problem and not a decoupled-block calculation.

---

## 3. The k·p result — exact closed forms, general moduli

Second-order degenerate perturbation theory on $D(k) = D_0 + D_1 + D_2 + O(k^3)$:

$$\lambda^{(\omega)}(k) = m^2 + P_\omega D_2 P_\omega + \tfrac{1}{m^2}P_\omega D_1 P_u D_1 P_\omega + O(k^4),\qquad
\lambda^{(u)}(k) = P_u D_2 P_u - \tfrac{1}{m^2}P_u D_1 P_\omega D_1 P_u + O(k^4).$$

| manifold | branch | multiplicity | $v^2$ (exact, all moduli) | $v/c_{EM}$ at placeholders |
|---|---|---|---|---|
| **$\omega$ — CARRIER** | $\boldsymbol\omega \parallel \mathbf k$ (twist) | 2 | $\dfrac{2\gamma}{I_\omega}$ | `1.4142135623730951` |
| **$\omega$ — CARRIER** | $\boldsymbol\omega \perp \mathbf k$ | 4 | $\dfrac{2\gamma}{I_\omega} + \dfrac{G_c}{\rho}$ | `1.7320508075688772` |
| $u$ — translational | transverse (**the photon**) | 4 | $\dfrac{G}{\rho} \;=\; c_{EM}^2$ | `1.0` |
| $u$ — translational | longitudinal (P-wave) | 2 | $\dfrac{10G}{3\rho}$ | `1.8257418583505538` |

Derived by exact `eigenvals()` on the high-symmetry axis and then **verified as an exact
characteristic-polynomial identity** in all five sampled directions
(`100`, `110`, `111`, `210`, `321`) — so the $O(k^2)$ dispersion is **isotropic**, and the form
$E(k)^2=(E_g/2)^2+(\hbar v k)^2$ holds per branch with no $O(k)$ term and no $O(k^2)$ anisotropy.

**Two structural readings that are the actual content of this lane:**

1. **The photon's $c_{EM}$ is protected, and the protection is a k·p cancellation.** The direct
   micropolar stiffness contributes $(G+G_c)/\rho$ to the transverse-$u$ branch, and the level
   repulsion from the gapped $\omega$ manifold subtracts **exactly** $G_c/\rho$. The result
   $v^2 = G/\rho$ is identically $c_{EM}^2$ for **all** moduli — the classic long-wave reduction
   of a micropolar medium to Cauchy elasticity, here obtained as the $O(k^2)$ k·p term. The
   substrate does deliver *one* branch at exactly $c_{EM}$, for free, robustly.
2. **The same modulus that opens the gap splits the carrier's velocity.**
   $v^2_\perp - v^2_\parallel = G_c/\rho = (I_\omega/4\rho)\,m^2$. Gap $\Rightarrow$ split;
   no gap $\Rightarrow$ no split (G6, measured across $G_c \in \{1, 10^{-2}, 10^{-4}, 0\}$: the
   splitting tracks $G_c/\rho$ to `1.000000260376055`, `0.009999997357956758`,
   `9.999750051448153e-05`, `0.0`). Therefore:

| target | condition | verdict |
|---|---|---|
| $v_\parallel = c_{EM}$ | $2\gamma/I_\omega = G/\rho$ | attainable by tuning |
| $v_\perp = c_{EM}$ | $2\gamma/I_\omega + G_c/\rho = G/\rho$ | attainable by tuning |
| **both** | $G_c = 0$ | **the gap closes — no massive carrier** |
| transverse-$u$ $=c_{EM}$ | none | **identically true, all moduli** |

**This is the kill-condition-class statement, stated plainly:** in this operator a *massive*
carrier cannot have a single limiting velocity, and cannot have $c_{EM}$ as its limiting
velocity, for any positive moduli. Not a placeholder artifact.

---

## 4. Full-dispersion verification (D4 / G5) + numerical conditioning (G8)

$R(k) = |\lambda_{exact} - (\lambda_0 + v^2k^2)|/k^4$ computed at `mpmath` 60 dps on the exact
$D(k)$, five directions × five decades. The $k^4$ coefficients converge to exact rationals:

| branch | $k^4$ coefficient at $k=10^{-6}$, $[100]$ | closed form |
|---|---|---|
| transverse $u$ (photon) | `-0.08333333333358056` | $-1/12$ |
| longitudinal $u$ (P-wave) | `-1.111111111110963` | $-10/9$ |
| carrier $\boldsymbol\omega\parallel\mathbf k$ | `-0.6666666666665778` | $-2/3$ |
| carrier $\boldsymbol\omega\perp\mathbf k$ | `-1.249999999999575` | $-5/4$ |

Worst successive-decade ratio deviation over $k = 10^{-4}\!\to\!10^{-6}$:
`3.4914552138332056e-08` (criterion `< 1e-6`) — **G5 PASS**.

**NUMERICAL-CONDITIONING receipt (G8).** The float64 shadow run of the *same* extraction
diverges from the mp result by up to `2931237005.988395` at $k \le 10^{-4}$ — i.e. the float64
$k^4$ coefficient is pure noise nine orders of magnitude wide. A float64-only lane would have
reported that noise as the $k^4$ term. Two further conditioning defects were found **at
integrator time** (Rule 10) and are recorded because they are the same class:

- **exact-rational $v^2$ is mandatory.** Using `float(10/3)` in the subtraction injects a
  $1.5\times10^{-16}$ error into $v^2$ which, divided by $k^4$, lands as a $3\times10^{-3}$
  error in the $k^4$ coefficient at $k=10^{-6}$ — and *grows* as $k$ shrinks.
- **exact direction normalisation is mandatory.** A float64 unit vector carries $\sim10^{-16}$
  relative error, entering as $\delta(k^2)v^2/k^4 \sim 4\times10^{-4}$, again growing as
  $1/k^2$. The axis direction $[100]$ hid this because its components are exactly
  representable; every non-axis direction showed a *diverging* residual until the normalisation
  was moved into mp.

---

## 5. Gate / self-test table (UNRUN ≠ PASSED)

| # | gate | run | result | pass |
|---|---|---|---|---|
| G1 | independent rebuild == canonical `dynamical_matrix_two_sublattice` | RUN | matrix diff `0.0`, eig diff `0.0` over 5 random $k$ | **PASS** |
| G1b | B-reference sign is a unitary gauge, not a physics choice | RUN | different matrix, eig diff `0.0` | **PASS** |
| G2 | negative control — PR #392 V1–V4 | RUN | $c_{EM}$ rel-err `3.0387404814646857e-09`; $c_R(G_c{=}0)=\sqrt2$ rel-err `1.6666666935449825e-09`; $m^2=4$ rel-err `0.0`; 6 gapless | **PASS** |
| G3 | $D(0)$ two-band block structure | RUN | off-diag `0.0`; 6 at 0, 6 at $m^2$; off-character weight `0.0` | **PASS** |
| G4 | Hermitian, real non-negative $\omega^2$ (lossless) | RUN | $\max|D-D^\dagger|$ `0.0`; min $\omega^2$ over BZ `0.001788197079800313` | **PASS** |
| G5 | k·p vs exact dispersion, mp 60 dps | RUN | worst ratio deviation `3.4914552138332056e-08` | **PASS** |
| G6 | negative control $G_c\to0$ | RUN | gap `0.0`, splitting `0.0`, all carrier branches at `1.9999999933333334` | **PASS** |
| **G7a** | **srs z=3 as pre-registered** | **RUN** | **`BLOCKED-STRUCTURAL`** — see §7 | **not passed; blocked** |
| G7b | connectivity-independence (disclosed substitute) | RUN | identical closed forms on z=6 cubic, z=8 bcc, anisotropic z=4 | **PASS** |
| G8 | float64 conditioning receipt | RUN | divergence `2931237005.988395` | **PASS (receipt)** |
| — | deterministic double-run digest | RUN | `7d55f51139cc65e92082de1ef95605651f9870810c6e8de72decd20d1a27b135` twice | **PASS** |

---

## 6. What materially qualifies the verdict — the validity window

The relativistic form names an **asymptotic** velocity, attained only where
$\hbar v k \gg E_g/2$. Ask whether that regime lies inside the expansion's own validity.
$k_{\text{rel}}$ is where $v^2k^2 = \omega_0^2$; $k_{\text{break}}$ is where the $k^4$ term
reaches 10% of the $k^2$ term:

| carrier branch | $v/c_{EM}$ | $k_{\text{rel}}$ | $k_{\text{break}}$ | ratio | relativistic regime inside validity? |
|---|---|---|---|---|---|
| $\boldsymbol\omega\parallel\mathbf k$ | `1.4142135623730951` | `1.4142135623730951` | `0.5477225575052026` | `0.38729833462076746` | **NO** |
| $\boldsymbol\omega\perp\mathbf k$ | `1.7320508075688772` | `1.1547005383792515` | `0.489897948556719` | `0.42426406871200073` | **NO** |

**The lattice bends the band over before the carrier reaches the regime in which $v$ would
become its group velocity.** Consistent with that, the full-BZ scan (400 seeded pseudo-random
$k$, central differences) reads the carrier manifold's largest $|\nabla_k\omega|$ as
`0.6116704022406638`, **below** $c_{EM}=1$, while the translational manifold reaches
`1.763402725591625` (approaching the P-wave $\sqrt{10/3}$).

So the honest statement of the mismatch is: **the low-energy effective theory of the carrier is
not Lorentz-invariant with $c_{EM}$ as its invariant speed** — its invariant speeds are
$\sqrt{2\gamma/I_\omega}$ and $\sqrt{2\gamma/I_\omega + G_c/\rho}$, and they differ from each
other. It is **not** a claim of observed superluminal energy transport, and it does **not** by
itself fire LC-1's kill (which requires an energy-carrying *inter-event* channel at $\neq c$;
this lane does not establish that the carrier branch is such a channel).

**Root cause of the missing window, stated for the record:** with $\ell_{node} \equiv
\hbar/(m_ec)$, the carrier's rest frequency sits at $\omega_0 = 2$ in units of $c_0/\ell_{node}$
— a large fraction of the $\omega$-manifold's own bandwidth. There is no scale separation
between the carrier's Compton scale and the lattice cutoff **by construction of the
$\ell_{node}$ identification**, so no lattice regularisation of this family can have a wide
relativistic window. This is a structural consequence of the corpus's own length calibration,
surfaced here, not adjudicated.

---

## 7. FLAGS (verbatim, flag-don't-fix — none of these are silently resolved)

**FLAG-1 — a factor-2 tension in the gap's relativistic reading (carried from the prereg).**
Under the relativistic reading the branch bottom is the REST frequency ($\hbar\omega_0 = E_g/2$)
and the $\pm\omega$ interband splitting is $E_g = 2\hbar\omega_0$. With the placeholder moduli
$\omega_0 = \omega_m = 2\omega_C$, giving $E_g = 4\,m_ec^2 = 2.044$ MeV — **not** the 1.022 MeV
that the Zitterbewegung / pair-threshold identification wants. To land $E_g = 2m_ec^2$ the
branch bottom must be $\omega_C$, i.e. $G_c/I_\omega = 1/4$, not 1. Either the placeholder is
off by 4 in $G_c/I_\omega$, or $\omega_m$ is being read as the FULL gap rather than the branch
bottom, or the two "2"s (A-008's frame-vs-field double cover, `trampoline-framework.md`:226-227,
and the Klein-Gordon $\pm$ splitting) are being double-counted. **Not adjudicated; no gate
depends on it.**

**FLAG-2 — the dispatch brief's dispersion-model instruction contradicts the corpus for this
sector.** The brief directs use of the arccos / coined-quantum-walk map and states the
graph-Laplacian map is canon-REJECTED. The corpus scopes that adjudication to the **scalar**
channel. Verbatim, `srs-band-structure.md`:88-89: *"because the scalar arccos map does **NOT**
cleanly generalize to the vector channel (3 acoustic branches, 2 distinct speeds $c_P\neq c_S$,
anisotropic per-site self-block ⇒ no single $\omega_{\text{link}}$)."* The canonical vector /
Cosserat band model in the corpus is the elastic dynamical-matrix eigenproblem, used by
`srs_vector_band_survey.py` and by the CI-gated `cosserat_band_structure_two_sublattice.py`.
**Resolution taken and declared:** this lane uses the canonical Cosserat dynamical-matrix
operator, because it is the adjudicated model *of the sector that owns the gap* and because the
arccos map has no micropolar DOF to gap at all. The brief's instruction is flagged as
scope-overreach, not followed, and not reframed.

**FLAG-3 — the canonical Cosserat operator runs on the z=4 diamond CONTROL net, not the
ratified z=3 srs production carrier.** `cosserat_band_structure_two_sublattice.py`:77-84 uses
the four tetrahedral even-parity ports (diamond, $z=4$). The corpus labels that net the
**control**: `src/ave/core/chiral_lattice.py`:240 verbatim *"Canonical diamond (engine-'K4',
degree-4, achiral) **control** net"*, against `:231` `carrier="srs-z3",  # the D1-ratified
production carrier (Axiom-1's object)` and `lattice-model-register.md`:24. So the sector's own
canonical mass gap and band structure live on the **control** connectivity. Surfaced, not
resolved.

**G7a — the pre-registered srs re-run is `BLOCKED-STRUCTURAL`, and the blocker is measured.**
The engine's tetrahedral gradient is a **least-squares** gradient; it exists only where the
per-site bond tensor $M = \sum_b \hat d_b\otimes\hat d_b$ is invertible. Measured at every srs
site: eigenvalues `[-0.0, 1.5, 1.5]`, **rank `2`** (trigonal-planar coordination puts the
out-of-plane gradient in the null space).
Diamond control: `[1.333333333333, 1.333333333333, 1.333333333333]`, rank `3`.
So the engine's Cosserat energy functional **cannot be transferred
to the ratified z=3 carrier** without a new bond-based constitutive model. That model was NOT
silently substituted; G7a is reported BLOCKED.

**Disclosed pre-reg deviation — G7b substituted for G7a.** Instead of the blocked srs run, the
lane demonstrates **connectivity-independence** of the $O(k^2)$ result: the identical exact
closed forms are recovered on a $z=6$ simple-cubic stencil, a $z=8$ bcc stencil, and a
deliberately anisotropic $z=4$ stencil. The reason this is the right substitute is analytic:
the least-squares gradient symbol satisfies $M^{-1}\sum_b d_b\,(i\,\mathbf k\cdot d_b) = i\mathbf
k$ **exactly** for any full-rank centro-symmetric bond set, so the whole $O(k^2)$ k·p is a
property of the **continuum** micropolar functional, not of the connectivity. **FLAG-3 therefore
does not move this lane's $O(k^2)$ verdict** — but it is not thereby discharged for anything
else (band tops, zone-edge structure, chirality, and any $O(k^4)$ statement all remain
connectivity-dependent, and the $k^4$ coefficients reported in §4 ARE diamond-specific).

---

## 8. Documented consequence — Zitterbewegung (mints nothing, adjudicates nothing)

For a real second-order-in-time field the branch pair is $\pm\omega$, so a superposition
straddling the gap beats at the interband frequency $E_g/\hbar = 2\omega_0$. In lattice units
$\omega_0 = `2.0`$ and $E_g/\hbar = `4.0`$. Under the $\ell_{node}\equiv\hbar/(m_ec)$
calibration that is $2\omega_m = 4\omega_C$, and FLAG-1's factor-2 tension rides directly on
this identification: the Dirac Zitterbewegung frequency is $2\omega_C$, which this operator
reaches only if the branch bottom is $\omega_C$, i.e. $G_c/I_\omega = 1/4$.

The $m^*$ identity $m^* = E_g/(2v^2)$ was **declared tautological in the prereg** (algebraically
forced by $\omega^2 = \omega_0^2 + v^2k^2$) and is confirmed as a numerics check with residual
`0.0` on both carrier branches. It is **not** counted as evidence.

Cross-reference: [`2026-08-04_electron-ontology-walk_framing-note.md`](2026-08-04_electron-ontology-walk_framing-note.md)
— this lane **feeds** its §3 "Mass"/"Spin" rows and its §7 E1 routing and **adjudicates none of
them**. In particular this lane says nothing about the electron's rest-mass value, and per the
corpus's own Rule-12 re-scope (`cosserat-mass-gap.md`:149) the $\omega$-gap is the **flywheel
clock gap**, not the rest-mass store.

## 9. Classification + fence

**Emergence-class FORM-derivation at PEER-WITH-SM strength. NOT a chord.** The Dirac equation
postulates the same form; Wilsonian universality says any gapped two-band lattice reproduces it
near the gap. The only content that could have come out differently is the **number** $v/c_{EM}$
— and it did. Symmetric-standard note: the SM does not derive $v = c$ either, it builds it in;
so the mismatch is informative and an equality would have been peer, not superior.

**This lane does NOT license:** any statement about the electron's rest-mass value; any claim
that the $\omega$-branch *is* the electron; any Zitterbewegung claim; any $O(k^4)$ or band-top
statement on the ratified z=3 carrier; and any firing of LC-1's arc-level kill.

---

> **⚑ ORCHESTRATOR REVIEW BLOCK (Tier-2 verify processed, 2026-08-05; body above preserved per
> Rule 12).** The independent audit CONFIRMED the headline identity (re-derived symbolically from
> the canonical energy functional, general moduli; hidden-O(k) and symmetry-degeneracy attacks
> failed), the cancellation mechanism (exact), FLAG-2's operator choice, and FLAG-3's rank-2 srs
> computation (analytically forced: coplanar 3-coordination). Corrections applied:
>
> 1. **The 0.612 figure is retracted as a point value.** The driver's 400-point scan is a LOWER
>    bound; the audit's denser scan measured ≥ 0.6133. Both KB sites now state the bound and the
>    method; the < c_EM conclusion is unaffected.
> 2. **The scale-separation attribution is softened:** "no scale separation because
>    ℓ_node ≡ ħ/(m_ec)" holds only under the ADDITIONAL identification gap = Compton
>    (G_c/I_ω = 1/4 reopens the window with ℓ_node untouched) — which is exactly FLAG-1's open
>    item, not a settled premise.
> 3. **FLAG-1 corrected and sharpened:** resolutions (b) and (c) are the same operation (two
>    distinct resolutions, not three). NEW WITNESS the lane missed: `trampoline-framework.md:224`
>    heads the cited lines "**A-008 resolution canonical** (Grant adjudication 2026-04-27)" —
>    "the factor of 2 IS the half-cover" (frame m_Cosserat = 2 vs field ω_C = m_e = 1). A dated
>    canonical ruling on this factor was presented as an open candidate. → Grant: does A-008
>    close FLAG-1, and is E_g = ħω_m or 2ħω_m?
> 4. **The VALUE-PROVENANCE absence claim is RETRACTED:** "no MeV gap value exists anywhere in
>    the corpus" was a single-method grep false-negative — the audit's second method found ≥ 9
>    tracked sites carrying ω_m ~ 1 MeV, including this landing's own leaf (:718) and
>    load-bearing uses (the B-mode freeze ratio behind clm-hp7nlm). The placeholder findings
>    (no constants.py symbols; engine pinning) STAND. Lesson re-banked: absence claims require a
>    second method — now mandated in dispatch briefs.
> 5. **The centrosymmetric justification is corrected:** TETRA_OFFSETS is NOT centrosymmetric;
>    the O(k²) connectivity-independence holds because the least-squares gradient's asymmetric
>    piece enters the eigenvalues only at O(k³) — the result stands, the stated reason did not
>    cover the primary case.
> 6. **Checker-scope gap routed:** the number-check gates only this result doc; the KB landing
>    and claim card numerals are ungated. Routed as a follow-on (extend the scan surface), and
>    the KB numerals were hand-reconciled in this repair pass.
> 7. The scope-interpretation audit found **NO LEAK**: V-MISMATCH binds the linear microrotation
>    branches on the diamond control net only; the canonical electron (nonlinear self-trapped
>    soliton) is not bound by it, and no text conflates them.
