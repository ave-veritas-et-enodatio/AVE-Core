[↑ Ch.12 Falsifiable Predictions](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-k4d4ph]
-->

## The K4 Bloch Dispersion and the $(q\,\ell_{node})^4$ Photon-Anisotropy Chord

The continuum photon rides the K4 / diamond-cubic substrate lattice without locking to its nodes
(weak-C; the photon is the LC-ladder long-wavelength regime, sub-saturation, $Z_0$-matched). Diagonalizing
the per-cell K4 Bloch **dynamical matrix** $D(\mathbf k)$ across the Brillouin zone shows that the lattice's
**first** directional anisotropy is the cubic harmonic $\Xi(\hat q)=\hat q_x^4+\hat q_y^4+\hat q_z^4$,
appearing at order $(q\,\ell_{node})^4$ — **quartic, not quadratic**, symmetry-protected by the diamond-cubic
($Fd\bar 3m$) point group. A random (non-cubic) bond set breaks this protection: its first anisotropic
invariant is the **quadratic** $\Sigma_b(\hat q\cdot\hat d_b)^2$, so its anisotropy is $O(k^2)$. The
quartic FORM is therefore K4-specific, not generic. This is the surviving forward prediction the weak-C
reconciliation kept ([`binary-kill-switches.md`](binary-kill-switches.md):17, gate `wejkhvnfb`).

> **Consistency-vs-emergence tag.** This leaf is **CONSISTENCY / FORM-class**. The **FORM** — that the
> first cubic-symmetric angular invariant of the K4/diamond bond set is the QUARTIC cubic harmonic, and that
> a random lattice breaks this to quadratic — is the AVE-distinct **CHORD**: it is demonstrated node-up by a
> from-geometry eigensolve and reproduces under an independent from-scratch verifier to $\sim10^{-15}$. The
> **MAGNITUDE** (the coefficient $\kappa_\gamma=1/24$, the physical birefringence $\delta\approx 2.2\times10^{-22}$
> at optical $q\ell_{node}$) is an **ECHO** — it is a lattice-geometry number sitting $\sim$2–3 OOM below current
> LIV / vacuum-birefringence bounds, so this dispersion test is **NOT near-term bankable**. The bankable
> QED-discriminator stays the **E-route birefringence COEFFICIENT** (🔴 CORRECTED 2026-07-03:
> $7.5\pi/\alpha^2\approx4.42\times10^5\times$ QED; was $7.5/\alpha^3\approx1.93\times10^7$ before the
> QED-normalization fix — see `vacuum-birefringence-e4.md` banner;
> [clm-pp3qwf](../../claim-quality.md), [`vacuum-birefringence-e4.md`](vacuum-birefringence-e4.md)).
> The **temporal cutoff value** $\omega_C=c_0/\ell_{node}$ ($\hbar\omega_C=m_ec^2=511$ keV) is likewise an
> **ECHO** — peer-with-QED, both import $m_e$ — and is a **DISTINCT mechanism** from this spatial quartic
> (see §4). No new dimensionful constant is minted: $c_0,Z_0,\ell_{node},\omega_C$ are all imported by SYMBOL
> from [`constants.py`](../../../../../src/ave/core/constants.py) (`C_0`, `Z_0`, `L_NODE`, `OMEGA_C`).

> **Derivation provenance.** The eigensolve construction, the closed-form bond-moment identities, the
> matter-vs-photon contrast, the random control, and the QED-symmetric-standard verdict are derived in
> [`research/2026-06-22_k4-bloch-dispersion-quartic_result.md`](../../../../../research/2026-06-22_k4-bloch-dispersion-quartic_result.md)
> (FORK-2 resolution). The driver is
> [`src/scripts/vol_4_engineering/k4_bloch_dispersion.py`](../../../../../src/scripts/vol_4_engineering/k4_bloch_dispersion.py);
> figures by [`k4_bloch_dispersion_figures.py`](../../../../../src/scripts/vol_4_engineering/k4_bloch_dispersion_figures.py).

## §1 — The K4 Bloch dynamical matrix

The substrate is the diamond two-sublattice $(A,B)$ structure of `k4_tlm.py`: each $A$ connects to four $B$
neighbours along the tetrahedral bond directions $\hat d_n=\tfrac{1}{\sqrt3}(\pm1,\pm1,\pm1)$ with an even
number of minus signs (`k4_tlm.port_shifts`). The EM-translation Bloch dynamical matrix is the
**general-force-constant** bond-spring sum

$$
\Phi_b = k_a\,\hat d_b\otimes\hat d_b + k_s\,(\mathbf I - \hat d_b\otimes\hat d_b), \qquad
D_{AB}(\mathbf k) = -\tfrac1m\sum_b \Phi_b\, e^{\,i\,\mathbf k\cdot(\boldsymbol\tau_B+\mathbf R_b)}
$$

with axial $k_a$ and transverse/shear $k_s$ the discrete sampling of the continuous $(\mu+\kappa,\,\beta+\gamma)$
constitutive tensor. This is the **substrate-native** stencil (the RANK-2 bond tensor), **not** a Cartesian
6-point Laplacian (which would fake an $O(k^2)$ anisotropy — the disabled-flag discretization bug the RANK-2
lesson warns against). A pure central-force model ($k_s=0$) would carry soft transverse-acoustic branches;
the general-force-constant tensor restores all three linear acoustic branches.

> **VALIDATE-ON-KNOWN (gate).** The small-$|k|$ acoustic branch of the $6\times6$ Bloch matrix recovers
> $\omega=c_0|k|$ — $c_0$ to rel-err $2.2\times10^{-16}$, $Z_0$ to rel-err $0$. At the isotropic-bond point
> $k_s=k_a$ the acoustic-speed spread across $\langle100\rangle,\langle110\rangle,\langle111\rangle,\langle210\rangle$
> is $0$ (machine precision) — this is the **emergent-Lorentz isotropy point** of the K4 lattice, genuinely
> node-up. If this gate fails the model is wrong and the driver HALTs.

## §2 — The quartic chord (the bond-moment identities)

The angular structure is carried by the bond moments $\Sigma_b(\hat q\cdot\hat d_b)^n$. The node-up facts
(no assertion — verified to machine precision by the driver and an independent from-scratch eigensolve):

> **[Resultbox]** *The first cubic anisotropy is QUARTIC*
>
> $$
> \Sigma_b(\hat q\cdot\hat d_b)^2 = \tfrac43 \;\;\text{(ISOTROPIC, spread }6.7\times10^{-16}\text{)},
> \qquad
> \Sigma_b(\hat q\cdot\hat d_b)^4 = -\tfrac89\,(\hat q_x^4+\hat q_y^4+\hat q_z^4) + \tfrac43
> \;\;\text{(verified to }1.3\times10^{-15}\text{)}.
> $$

The **2nd** bond moment carries **no** angular dependence; the **4th** moment is the pure cubic harmonic. So
the continuum (unlocked) photon, which inherits the lattice point-group symmetry but carries **no** zone-edge
$(q\ell_{node})^2$ term, has its **first** directional anisotropy at $(q\ell_{node})^4$:

$$
\frac{\omega^2(\mathbf k)}{c^2|\mathbf k|^2} = 1 + \kappa_\gamma\,\Xi(\hat q)\,(k\ell_{node})^4,
\qquad \kappa_\gamma=\tfrac1{24},\qquad \Xi(\hat q)=\hat q_x^4+\hat q_y^4+\hat q_z^4-\tfrac35.
$$

$\Xi$ is **sign-changing**: $\Xi[100]=+0.400$, $\Xi[111]=-0.267$ — a genuine cubic (four-fold-in-plane)
birefringence, not an isotropic shift. The driver reports a directional-anisotropy log-log slope of $4.00$ for
the photon dispersion — but this is the **hardcoded form's** slope, **conditional on weak-C**; the genuine
chiral-srs eigensolve MEASURES slope $1.9999$ (see the demotion caveat immediately below).

> 🟡 **DEMOTED — LOAD-BEARING CAVEAT (P1b genuine chiral-srs eigensolve, 2026-06-24; flag-don't-fix).** The
> reported photon slope $=4.0$ is **NOT** an independent eigenvalue measurement. The driver's
> `photon_omega_sq_over_c2k2` (and the canonical
> [`vacuum_node_circuit.photon_birefringence`](../../../../../src/ave/core/vacuum_node_circuit.py)) **hardcode**
> the form $1+\kappa_\gamma\,\Xi\,(k\ell)^4$. The **genuine 24×24 chiral-srs Bloch eigensolve** — substrate-native
> rank-2 bond tensor $\Phi_b=k_a\,\hat d\otimes\hat d+k_s(\mathbf I-\hat d\otimes\hat d)$ on the lattice's OWN z=3
> srs bonds (Wyckoff-8a, $I4_132$), NOT a Cartesian Laplacian
> (driver `src/scripts/vol_4_engineering/srs_bloch_dispersion.py` + result JSON
> `_output/srs_bloch_dispersion.json` — **now on `main` @ commit `19a31836`** "P1b.3: the band-edge dispersion gate — genuine srs eigensolve gives SLOPE-2"; the earlier "on branch `engine/p1b-modes-live`, not yet on main" cite is STALE, corrected 2026-07-03 per the verdict-exposure sweep) —
> **MEASURES** band-edge anisotropy slope $=\mathbf{1.9999}$
> ($a_2=+0.056$ **dominant** over $a_4=-0.0017$, for **BOTH** enantiomorphs; cross-checked by the raw
> $[100]$–$[111]$ speed-diff ratio $=4.0=O(k^2)$, and the fit returns $4.0$ on a synthetic quartic so slope-2 is a
> genuine measurement, not a fit floor). This **confirms** the prior from-scratch $6\times6$ k4_tlm result: the
> genuine lattice carries the isotropic $O(k^2)$ zone-edge term that the unlocked photon is **ASSERTED** (not
> derived here) to lack. So the eigensolve gives the **GENERIC slope-2 band-edge term**; the distinctive
> $(q\ell_{node})^4$ EM-dispersion tell is **CONDITIONAL on the UNPROVEN weak-C no-zone-edge theorem**
> ([`binary-kill-switches.md`](binary-kill-switches.md):17, gate `wejkhvnfb`, Grant-confirmed 2026-06-14, **OPEN**) —
> the slope-4 is a **re-statement of the inserted exponent**, not a from-eigensolve derivation of quartic-ness. This
> is a **DEMOTION, not a refutation**: the distinctive quartic could RETURN if weak-C is proven (the photon must be
> shown to decouple from the zone-edge $O(k^2)$ quadratic). What the eigensolve **does** establish node-up is the
> matter-vs-photon CONTRAST, the bond-moment identities of §2, **and** the small-$k$ emergent-Lorentz ISOTROPY
> ($c(k\to0)=1/\sqrt3$, cross-axis speed-spread $=0$) — so this is **band-edge anisotropy, NOT a low-$k$ Lorentz
> violation**; the small-$k$ isotropy SURVIVES. The rigorous proof that the continuum limit is exact ($\delta=0$,
> $\omega=ck$) **remains OPEN on the same weak-C lever** — the genuine eigensolve has $\max|\omega^2/c^2k^2-1|=10^{-3}$
> at $k\ell=0.08$, so $\delta=0$ is NOT exact at the lattice level
> ([`binary-kill-switches.md`](binary-kill-switches.md):19).

## §3 — The matter contrast and the random control

A **matter** carrier IS lattice-locked, so it keeps the zone-edge $(q\ell_{node})^2$ term; its anisotropy
appears at $O(k^2)$ (log-log slope $2.0$). A **random** (non-cubic) bond set has no point-group protection:
its first anisotropic invariant is the quadratic $\Sigma_b(\hat q\cdot\hat d)^2$ (direction-dependent,
spread $0.80$ across directions), so its anisotropy is $O(k^2)$ (slope $2.0$). The K4 photon's anisotropy
being pushed to $O(k^4)$ — while both the matter carrier and the random-lattice photon sit at $O(k^2)$ — is
the discriminating signature that the quartic is **K4-symmetry-protected**, not generic.

| Carrier / lattice | first anisotropic invariant | anisotropy order | slope |
|---|---|---|---|
| **K4 photon** (unlocked, cubic) | $\Sigma_b(\hat q\cdot\hat d)^4$ (cubic harmonic) | $(q\ell)^4$ | $4.0$ **conditional on weak-C** (genuine eigensolve gives $2.0$ — see the §2 demotion caveat) |
| K4 matter (lattice-locked) | zone-edge $(q\ell)^2$ | $(q\ell)^2$ | $2.0$ |
| random photon (control) | $\Sigma_b(\hat q\cdot\hat d)^2$ (anisotropic) | $(q\ell)^2$ | $2.0$ |

The genuine 24×24 chiral-srs eigensolve (P1b, 2026-06-24) MEASURES the **K4 photon** row at slope $1.9999$ — i.e.
the photon's band-edge anisotropy is GENERIC $(q\ell)^2$ at the lattice level. The $(q\ell)^4$ slope holds ONLY if
the unproven weak-C theorem (the photon decouples from the zone-edge $O(k^2)$ quadratic, gate `wejkhvnfb`) is
established; until then the "$4.0$" in the table is a re-stated inserted exponent, not a from-eigensolve number.

## §4 — Temporal cutoff vs spatial zone-edge (DISTINCT mechanisms)

The TEMPORAL pair-production cutoff $\omega_C = c_0/\ell_{node}$ ($k=1/\ell_{node}$, symbol `OMEGA_C`) and the
SPATIAL Brillouin zone-edge ($k=\pi/\ell_{node}$) are **distinct** mechanisms with ratio exactly $\pi$:

$$
\hbar\omega_C = \hbar c_0/\ell_{node} = m_e c^2 = 511\text{ keV},\qquad
\frac{k_{zone\text{-}edge}}{k_{cutoff}} = \pi.
$$

The cutoff **value** (511 keV) is an ECHO (imports $m_e$, peer-with-QED). The spatial quartic of §2 is a
**separate** geometric prediction; the two must not be conflated.

> **The temporal cutoff is face (1) of the single substrate scale.** $\hbar\omega_C=m_e c^2$ is one of five
> algebraic faces of AVE's single imported lattice scale ($m_e$ via $\ell_{node}\equiv\hbar/(m_e c)$) — see
> [`single-substrate-scale.md`](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/single-substrate-scale.md)
> (`clm-sw5oao`). That leaf records the honest scope (frame-checked 2026-06-22, `claim_survives = false`): the
> multi-face web is a **one-import ECONOMY** (one dial vs the SM's $\sim$19+) plus a **same-substrate-event
> explanatory ONTOLOGY**, **NOT** a prediction and **NOT** an AVE-distinct chord. $\hbar\omega_C=m_e c^2$ is true
> **by the definition of $\ell_{node}$** (constants.py `OMEGA_C` comment), so it is definitional-by-construction,
> peer-with-QED (QED equally ties the Compton length and Schwinger field to $m_e$). It must **not** be framed as
> "structural unification the SM lacks." The AVE-distinct content of *this* leaf is the **spatial quartic FORM**
> of §2 (geometry, node-up to $10^{-15}$), which is a **distinct mechanism** from this temporal value-echo. The
> open scale-from-substrate theorem (gate `wejkhvnfb`, §6) is the SAME lever that would un-condition both the
> cutoff-as-echo and the photon slope-4.

## §5 — Figures

- [`k4_bloch_dispersion_bands`](../../../../../manuscript/vol_4_engineering/figures/k4_bloch_dispersion_bands.pdf)
  — $\omega(k)$ along $\langle100\rangle\to\langle110\rangle\to\langle111\rangle\to\langle210\rangle$: six K4
  mechanical bands + photon branch + light-line $\omega=c|k|$, with cutoff and zone-edge marked.
- [`k4_bloch_anisotropy_polar`](../../../../../manuscript/vol_4_engineering/figures/k4_bloch_anisotropy_polar.pdf)
  — polar $[\omega/(c|k|)-1]$ vs direction: the QUARTIC four-fold K4 clover vs the random-control's QUADRATIC
  two-fold pattern.
- [`k4_bloch_k2_k4_fit`](../../../../../manuscript/vol_4_engineering/figures/k4_bloch_k2_k4_fit.pdf)
  — $a_2(k\ell)^2+a_4(k\ell)^4$ fit + residuals; photon $a_2\approx0$ (no zone-edge), $a_4=\kappa_\gamma\Xi[100]$.
- [`k4_bloch_bz_surface`](../../../../../manuscript/vol_4_engineering/figures/k4_bloch_bz_surface.pdf)
  — heatmap + 3D surface of the anisotropy over the inscribed BZ disk; the sign-changing cubic harmonic.
- [`k4_bloch_anisotropy_sweep.gif`](../../../../../manuscript/vol_4_engineering/figures/k4_bloch_anisotropy_sweep.gif)
  — animation of the polar anisotropy as $|k|$ sweeps $\Gamma\to$ zone-edge.

## §6 — Falsification scope

- **FALSIFIES this leaf:** an independent demonstration that the diamond-cubic bond set's first cubic angular
  invariant is **not** quartic (i.e. that $\Sigma_b(\hat q\cdot\hat d)^2$ is direction-dependent on K4), or that
  a random lattice retains the quartic protection. Neither holds (verified to $10^{-15}$).
- **DOES NOT bear on** the weak-C no-zone-edge premise itself — that is carried separately as a regime-grounded,
  GRB-corroborated PREDICTION ([`binary-kill-switches.md`](binary-kill-switches.md):17), not derived here.
- **NOT a near-term experimental falsifier:** the physical magnitude is $\sim$2–3 OOM below current bounds. The
  bankable QED-discriminator is the E-route birefringence COEFFICIENT (clm-pp3qwf), a separate test.

---

> **Quality, depends-on, and solidity for `clm-k4d4ph` live in the volume claim register**
> ([`../../claim-quality.md`](../../claim-quality.md)).
