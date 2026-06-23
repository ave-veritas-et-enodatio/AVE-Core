# RESULT — K4 Bloch Dispersion: the $(q\,\ell_{node})^4$ Photon-Anisotropy Chord (FORK-2 resolution)

Canonical leaf: [`manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md)
(claim `clm-k4d4ph`). Driver: `src/scripts/vol_4_engineering/k4_bloch_dispersion.py`. Figures:
`src/scripts/vol_4_engineering/k4_bloch_dispersion_figures.py`. This doc is the research substrate for the
canonicalization; the leaf + claim-register carry the canonical summary.

## 0. TL;DR

The K4 / diamond-cubic Bloch **dynamical matrix** $D(\mathbf k)$, diagonalized across the Brillouin zone,
has its **first** directional anisotropy at order $(q\,\ell_{node})^4$ — the cubic harmonic
$\Xi(\hat q)=\hat q_x^4+\hat q_y^4+\hat q_z^4$ — **quartic, not quadratic**, symmetry-protected by the
diamond-cubic $Fd\bar3m$ point group. A random (non-cubic) bond set breaks this protection to quadratic.
The temporal cutoff $\omega_C=c_0/\ell_{node}$ (511 keV) and this spatial quartic are **distinct mechanisms**.

**Consistency-vs-emergence:** CONSISTENCY / FORM-class. The FORM is the CHORD; the magnitude is an ECHO
($\sim$2–3 OOM below current bounds ⟹ not near-term bankable). The bankable QED-discriminator stays the
E-route birefringence COEFFICIENT (clm-pp3qwf). **FORK-2 resolution:** the $(q\ell_{node})^4$ test is
re-scoped from the "dispersive-$\mu(\omega)$ workstream" pointer to **this Bloch eigensolve**.

## 1. FORK-2 stated

The node-up VCA-R01 resolution ([`research/2026-06-22_node-up-small-large-signal_result.md`](2026-06-22_node-up-small-large-signal_result.md):§6,
[`node-up-small-large-signal.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):205–207)
deferred the $\omega_C$ cutoff and the AVE-distinct $(q\,\ell_{node})^4$ anisotropy to *"a dispersive-$\mu(\omega)$
workstream — the AVE-distinct $(q\cdot\ell_{node})^4$ lattice-dispersion test at the 511 keV scale."*

**FORK-2** is the implementation question that pointer left open: *is the $(q\ell_{node})^4$ test a temporal
ADE-$\mu(\omega)$ FDTD, or a k-space Bloch eigensolve?* A temporal-$\mu$ FDTD on a coarse-grid continuum engine
($dx\gg\ell_{node}$) runs at $\omega/\omega_C\lesssim10^{-6}$ and only ever validates the **null** $\mu=\mu_0$
(it cannot reach the quartic). The directional anisotropy is a **k-space** object — it lives in $D(\mathbf k)$
across the Brillouin zone, not in the time-domain $\mu(\omega)$ response. **FORK-2 resolves to the Bloch
eigensolve**, which is the corpus's own "k-space eigensolve" call. The temporal cutoff $\omega_C$ stays a
*separate* (and already-closed, VCA-R01) mechanism (§4).

## 2. The eigensolve construction (substrate-native)

The lattice is the diamond two-sublattice $(A,B)$ structure of `k4_tlm.py`: $A$ connects to 4 $B$-neighbours
along the tetrahedral bonds $\hat d_n=\tfrac1{\sqrt3}(\pm1,\pm1,\pm1)$, even number of minus signs
(`k4_tlm.port_shifts`). Each bond carries the **general-force-constant** tensor
$\Phi_b=k_a\,\hat d_b\otimes\hat d_b+k_s(\mathbf I-\hat d_b\otimes\hat d_b)$ — the discrete sampling of the
continuous $(\mu+\kappa,\,\beta+\gamma)$ constitutive tensor, i.e. the substrate-native RANK-2 bond stencil,
**not** a Cartesian 6-point Laplacian (which would fake an $O(k^2)$ anisotropy — the disabled-flag
discretization bug the RANK-2 lesson warns against). The $6\times6$ Hermitian Bloch matrix
$D_{AB}(\mathbf k)=-\tfrac1m\sum_b\Phi_b\,e^{i\mathbf k\cdot(\boldsymbol\tau_B+\mathbf R_b)}$ is diagonalized
to $\omega^2(\mathbf k)$; $k_a,k_s,m$ are calibrated out of the speed (validate-on-known); only the FORM
survives in the angular structure.

## 3. The numerics

| Quantity | Value | Status |
|---|---|---|
| **VALIDATE-ON-KNOWN** $c_0$ recovered | rel-err $2.22\times10^{-16}$ | EXACT |
| $Z_0$ recovered | rel-err $0$ | EXACT |
| Acoustic-speed spread across dirs (isotropic-bond pt) | $0$ | emergent-Lorentz isotropy point, node-up |
| $\Sigma_b(\hat q\cdot\hat d_b)^2$ across all dirs | $4/3$, spread $6.7\times10^{-16}$ | ISOTROPIC (2nd moment carries no anisotropy) |
| $\Sigma_b(\hat q\cdot\hat d_b)^4=-\tfrac89\Xi+\tfrac43$ identity | residual $1.3\times10^{-15}$ | first anisotropy enters at 4th moment |
| Cubic harmonic $\Xi$: $[100]$ / $[111]$ | $+0.400$ / $-0.267$ | sign-changing → genuine cubic |
| **Photon** anisotropy log-log slope | $4.000$ | QUARTIC (see §5 caveat) |
| **Matter** (lattice-locked) anisotropy slope | $2.000$ | QUADRATIC (zone-edge) |
| **Random control** anisotropy slope | $2.000$ | QUADRATIC (protection broken) |
| Random $\Sigma_b(\hat q\cdot\hat d)^2$ spread across dirs | $0.796$ | random 2nd moment IS anisotropic |
| $\omega_C$ | $7.763\times10^{20}$ rad/s | $\hbar\omega_C/(m_ec^2)=1.000$ (511 keV) |
| $k_{zone\text{-}edge}/k_{cutoff}$ | $\pi$ (exact) | cutoff vs zone-edge are distinct |

The matter isotropic $a_2$ is fit-window-dependent (driver $-0.0484$, 2.0-norm $2.32$; independent verifier
$-0.0393$, 2.0-norm $1.885$) — both in the $\sim2.0$ family, neither $\sqrt6=2.449$; $a_2$ is **not** a robust
invariant, so the small mismatch is expected. The robust invariant ($\Sigma(\hat q\cdot\hat d)^4=-\tfrac89\Xi+\tfrac43$)
reproduces to $10^{-15}$.

## 4. Temporal cutoff vs spatial zone-edge (distinct mechanisms)

$\omega_C=c_0/\ell_{node}$ ($k=1/\ell_{node}$, symbol `OMEGA_C`) is the TEMPORAL pair-production cutoff;
$\hbar\omega_C=m_ec^2=511$ keV. The SPATIAL Brillouin zone-edge is $k=\pi/\ell_{node}$. Ratio exactly $\pi$.
These are not the same object: the cutoff is a frequency scale (VCA-R01 dispersive-$\mu$ closed it as the
null $\mu=\mu_0$ for FDTD-reachable waves); the quartic is a k-space angular invariant. The 511 keV **value**
is an ECHO (imports $m_e$, peer-with-QED).

## 5. Independent verification + the load-bearing caveat (flag-don't-fix)

An independent from-scratch eigensolve (`/tmp/indep_k4_verify.py`, `/tmp/indep_order_check.py`), built only
from `k4_tlm` tetrahedral bond geometry + standard lattice-dynamics Bloch form + `ave.core.constants` by
SYMBOL (NOT the driver), reproduced **every load-bearing number**: continuum $c$ (rel-err $2.22\times10^{-16}$),
$Z_0$ (rel-err $0$), $\Sigma(\hat q\cdot\hat d)^2=4/3$ (spread $6.7\times10^{-16}$), the quartic identity
($1.3\times10^{-15}$), $\Xi[100]=+0.400$/$\Xi[111]=-0.267$, the random control 2nd-moment per direction
($1.415/1.931/1.135/1.872$, spread $0.796$), the cutoff/zone-edge ratio $=\pi$, and $\omega_C$ with
$\hbar\omega_C/(m_ec^2)=1.0$.

> 🟡 **THE CAVEAT (must be surfaced, not buried).** The driver's reported **photon slope $=4.0$ is NOT an
> independent eigenvalue.** The driver's `photon_omega_sq_over_c2k2` and the canonical
> `vacuum_node_circuit.photon_birefringence` (`src/ave/core/vacuum_node_circuit.py`:302) **hardcode** the form
> $1+\kappa_\gamma\Xi(k\ell)^4$. The independent node-up eigensolve of the actual $6\times6$ dynamical matrix
> gives anisotropy slope $=2.0$, **not** $4.0$, because the genuine lattice carries the isotropic $O(k^2)$
> zone-edge term. The slope-4 depends **entirely** on the weak-C physics ASSERTION that the unlocked continuum
> photon carries no zone-edge $(q\ell)^2$ term (deleting that isotropic $k^2$ piece pushes the first anisotropy
> from $k^2$ to $k^4$). This assertion is **CORPUS-CANONICAL, not the driver's invention**:
> [`binary-kill-switches.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md):17
> (gate `wejkhvnfb`, Grant-confirmed 2026-06-14) states the continuum photon *"carries no zone-edge
> $(q\ell_{node})^2$ dispersion"* and *"retains the $(q\ell_{node})^4$ anisotropy by inheriting the lattice's
> cubic symmetry; that is the surviving forward prediction."* So the quartic is REAL **conditional on a canonical
> weak-C premise**, and the matter/photon CONTRAST is the genuine substrate content. NOT refuted — but the
> slope-4 number is a **re-statement of an inserted exponent**, not a from-eigensolve measurement. The rigorous
> proof that the continuum limit is exact ($\delta=0$) remains OPEN
> ([`binary-kill-switches.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md):19).

I specifically hunted the $\sqrt6$-class zone-edge coefficient slip the prior lane self-corrected and found
NONE: the dispersion coefficients are clean rationals ($4/3$, $-8/9$, $1/24$), all verified to $10^{-15}$; the
only $\sqrt6$ in the vicinity is the **unrelated** Cosserat $\ell_c=\sqrt6\,\ell_{node}$ (`constants.py` symbol
`L_C`), which does not contaminate the dispersion coefficients.

## 6. QED-symmetric-standard verdict

| Axis | AVE | QED | Verdict |
|---|---|---|---|
| Vacuum birefringence FORM | $(q\ell)^4$ cubic-anisotropic (this leaf) | $\alpha^2$-loop, isotropic | **distinct-IN-KIND** (CHORD) |
| 511 keV cutoff value | $\hbar c/\ell_{node}=m_ec^2$ (imports $m_e$) | $m_ec^2$ (imports $m_e$) | **peer / ECHO** |
| Birefringence magnitude | $\delta\approx2.2\times10^{-22}$ (optical $q\ell$) | similar OOM | $\sim$2–3 OOM below bounds |
| Near-term experimental reach | NO (dispersion test) | — | **NOT bankable** |
| Bankable discriminator | E-route COEFFICIENT $7.5/\alpha^3$ (clm-pp3qwf) | $\alpha^2$-loop | separate test, KEPT |

Applying the symmetric standard (the orchestrator and every sub-agent carry SM/QED priors set by
training-volume, so an AVE claim and the matching SM claim must be held to the same bar): the $(q\ell)^4$
cubic form **is** distinct-in-kind from QED's isotropic vacuum birefringence — that is a genuine AVE-distinct
FORM. But the **magnitude** is an echo $\sim$2–3 OOM below current LIV / vacuum-birefringence bounds, so this
dispersion test is **not a near-term falsifier**. This matches what the corpus already says (consistency /
FORM-class). The bankable QED-discriminator remains the E-route birefringence COEFFICIENT (clm-pp3qwf), where
the $\sim10^6\times$ coefficient gap is present at all fields.

## 7. Derived-vs-asserted ledger

| Element | Status | Basis |
|---|---|---|
| Bond geometry $\hat d_n$, two-sublattice Bloch form | **DERIVED** | `k4_tlm.port_shifts` + standard lattice dynamics |
| $\Sigma_b(\hat q\cdot\hat d)^2=4/3$ isotropic | **DERIVED** (node-up, $10^{-15}$) | direct bond-moment sum |
| $\Sigma_b(\hat q\cdot\hat d)^4=-\tfrac89\Xi+\tfrac43$ | **DERIVED** (node-up, $10^{-15}$) | direct bond-moment sum |
| $c_0$, $Z_0$ recovery (validate-on-known) | **DERIVED** (exact) | acoustic-branch small-$k$ slope |
| Random control breaks protection to quadratic | **DERIVED** (node-up) | random 2nd moment spread $0.796$ |
| matter anisotropy $=O(k^2)$, photon $=O(k^4)$ CONTRAST | **DERIVED** | the two carriers' first invariants |
| **Photon slope $=4.0$ of the *physical* photon** | **ASSERTED** (weak-C no-zone-edge, gate `wejkhvnfb`) | corpus-canonical premise, not in-leaf; the genuine eigensolve gives slope $2.0$ |
| $\kappa_\gamma=1/24$ magnitude | **ECHO** (lattice geometry) | matches `vacuum_node_circuit.photon_birefringence` |
| 511 keV cutoff value | **ECHO** (imports $m_e$, peer-QED) | $\hbar\omega_C=m_ec^2$ |

## 8. Corpus defects fixed on the branch (PR#367 follow-through)

Three corpus defects were grep-verified fixed/flagged on `analysis/k4-bloch-dispersion`:

- **B1 (units, 5 sites)** — `1.24e20 rad/s` → `7.76e20 rad/s (f_C ≈ 1.24e20 Hz; ℏω_C = m_ec² = 511 keV)` at
  `fdtd_3d.py`, `fdtd_3d_jax.py`, `test_vca_r01_static_b_mu_keying.py`, the node-up result-doc, and the node-up
  leaf. The relationship is internally consistent ($7.763\times10^{20}/2\pi=1.236\times10^{20}$ Hz).
- **B2 (`OMEGA_C` symbol)** — `constants.py` `OMEGA_C = C_0 / L_NODE` (cited by SYMBOL); $\hbar\,$`OMEGA_C`$=m_ec^2$
  exactly, rel-err $0$. UNITS GUARD comment present.
- **B3 (cite-drift)** — RESOLVED this revision (cite-the-symbol, bundled into #369): the `B_SNAP` cites that used a drifting `constants.py` line number — `2026-06-22_node-up-small-large-signal_result.md`:52, the `ave-analytical-toolkit-index.md` leaf, and Vol-9 ch02/ch10 — now use file-level pointers + the `B_SNAP` symbol. (`B_SNAP` is at `:456` on this branch, `:444` on main — exactly the drift the symbol-cite immunizes against.) Build's claimed source for $\kappa_\gamma$,
  `vacuum_node_circuit.photon_birefringence`, resolves at `src/ave/core/vacuum_node_circuit.py`:302 and its
  $q^4$-scaling test passes — no fabricated cite.

## 9. Residuals carried to Grant

- **B3 line-drift** (`:444`→`:456` for `B_SNAP` in the node-up result-doc) — surfaced; cite-the-symbol fix is
  the standing convention. Not edited from this lane (it is in a different result-doc).
- **The OPEN topological-decoupling theorem** — closing the weak-C no-zone-edge premise from a *derived* theorem
  (currently regime-grounded + GRB-corroborated PREDICTION) would upgrade the photon slope-4 from a re-stated
  exponent to a from-eigensolve result. Not landed.
- **FORK-1 (tracked open fork — Grant directive 2026-06-22).** The **electric-channel free-wave dispersion**
  is unwritten — the corpus derived the magnetic μ-grade's temporal response only. Does the ε-grade cut off
  with frequency like the μ-grade (a low-pass band-fold, the $\varepsilon_{eff}(\omega)$ analog of
  $\mu_{eff}(\omega)=\mu_0\sqrt{1-(\omega/\omega_C)^2}$), or is it a Klein–Gordon-style high-pass? **MOOT for the
  free photon** (which by the weak-C premise carries no zone-edge term at all), so non-blocking here — but it
  **GATES a future bound-resonator model** (where the electric grade IS loaded). Resolution path: extend the
  Bloch eigensolve / per-DOF node circuit to the ε-channel and read off its $\omega$-dependence. Tracked, not
  actioned.

### Provenance

- FORK-2 resolution workflow: canonicalize lane, `analysis/k4-bloch-dispersion` off `origin/main`.
- Independent verifier: `/tmp/indep_k4_verify.py`, `/tmp/indep_order_check.py` (auditor lane, /tmp scratch).
- Driver: `src/scripts/vol_4_engineering/k4_bloch_dispersion.py`; JSON: `_output/k4_bloch_dispersion.json`.
