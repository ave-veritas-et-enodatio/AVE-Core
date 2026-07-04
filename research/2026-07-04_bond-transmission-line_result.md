# GAP-2 — the bond as a TRANSMISSION LINE (ABCD identity + periodically-loaded Bloch)

**Date:** 2026-07-04
**Branch:** `analysis/gap2-bond-transmission-line` (off `origin/main`)
**Commissioned:** GAP-2, the deferred vol-9 build. The vol-9 remediation arc
(merged PR #519) deferred this because it consumes the Ax3 matched-line theorem —
now MERGED CANON with canonical leaf
[`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md)
(claim `clm-mfb2ax`; Ax3 forces $k_s=k_a$ knob-free; MATCH/BALANCE/HEAVISIDE = one
parent condition at $\rho_{bond}=1$).
**Driver:** [`src/scripts/vol_4_engineering/bond_transmission_line.py`](../src/scripts/vol_4_engineering/bond_transmission_line.py)
**Test:** [`src/tests/test_bond_transmission_line.py`](../src/tests/test_bond_transmission_line.py) (8 pass)
**Consumes (by SYMBOL):** `L_CELL`, `C_CELL`, `Z_0`, `L_NODE`, `OMEGA_C` (via
`C_0`), `MU_0`, `EPSILON_0` from `src/ave/core/constants.py` (the #519-minted
per-node reactive pair).
**Cross-checks against:** the on-engine srs Bloch eigensolve
[`src/scripts/vol_4_engineering/srs_bloch_dispersion.py`](../src/scripts/vol_4_engineering/srs_bloch_dispersion.py)
(`acoustic_omega`, the genuine 24×24 chiral-srs dynamical matrix).

---

## SECTOR HEADER (declared before any substrate statement)

- **SECTOR:** EM-transverse / translational-**capacitive** face (the $\varepsilon$–$\mu$
  photon port). This is the transverse light-cone bond. It is **NOT** the
  T2/Cosserat charge sector and **NOT** the A1 bulk-mass store — no charge/spin
  content is wired here.
- **REGIME:** COLD lattice, $S(A)=1$ ($A=0$). No Op14 saturation load. The
  loaded/biased line is the concurrent SPICE phase-1 arc's domain
  ([`research/2026-07-04_spice-phase1-ladder_result.md`](2026-07-04_spice-phase1-ladder_result.md)),
  not touched here.
- **PHASE-STATE:** lossless-reactive (Axiom 3, no loss term). At the $\rho_{bond}=1$
  photon operating point the medium is $K<0$ (mechanically unstable per
  `clm-mfb2ax` §3) — a lossless-reactive **photon** point, NOT a stable static
  solid. This driver reads only the transverse dispersion; it does not read
  mechanical stability.

## Classification (do NOT lift)

**CONSISTENCY class throughout.** This work re-expresses the already-canonical
per-node LC pair ($L_{CELL}=\mu_0\ell_{node}$, $C_{CELL}=\varepsilon_0\ell_{node}$;
#519) and the LC-ladder sine-law dispersion (`clm-gvn4r1` §1) as a distributed
transmission-line (ABCD) treatment, and re-expresses the Ax3 $\Gamma=0$ point
(`clm-mfb2ax`) as a matched-line. It originates **no** new dimensionful constant
and makes **no** emergence claim: $Z_0$, $c_0$ are validate-on-known anchors;
$\alpha$, $m_e$ are not touched. The only potentially-adjudicable output is the
TL-vs-Bloch zone-edge comparison (below) — and it **agrees with** the existing
weak-C zone-edge flag rather than conflicting with it.

---

## §1 — THE CORE IDENTITY: the bond IS a lossless transmission line

Each K4/srs bond is a lossless TL segment of length $\ell_{node}$ carrying
per-length $\mu_0$, $\varepsilon_0$. Its lumped totals over one span are exactly
the #519 constants, and the derived TL parameters follow (all machine-exact):

| TL quantity | Form | Identity checked | rel-err |
|---|---|---|---|
| series inductance | $L_{CELL}=\mu_0\ell_{node}$ | `L_CELL` vs $\mu_0\ell_{node}$ | $0$ |
| shunt capacitance | $C_{CELL}=\varepsilon_0\ell_{node}$ | `C_CELL` vs $\varepsilon_0\ell_{node}$ | $2.2\times10^{-16}$ |
| characteristic impedance | $Z_0=\sqrt{L_{CELL}/C_{CELL}}=\sqrt{\mu_0/\varepsilon_0}$ | vs `Z_0` | $1.1\times10^{-16}$ |
| one-bond delay | $\tau=\sqrt{L_{CELL}C_{CELL}}=\ell_{node}/c_0$ | vs $\ell_{node}/c_0$ | $0$ |

**The ABCD matrices.** The distributed bond has the exact lossless-line ABCD
(electrical length $\theta=\beta\ell=\omega\tau$):

$$
\mathrm{ABCD}_{line}(\theta) = \begin{bmatrix} \cos\theta & jZ_0\sin\theta \\ j\sin\theta/Z_0 & \cos\theta \end{bmatrix},
\qquad \det = 1,\ A=D\ \text{(unimodular, reciprocal)}.
$$

The #519 **lumped** node model is a single series-$L$ / shunt-$C$ section:

$$
\mathrm{ABCD}_{lump}(\theta) = \begin{bmatrix} 1 & j\omega L \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ j\omega C & 1 \end{bmatrix} = \begin{bmatrix} 1-\theta^2 & j\theta Z_0 \\ j\theta/Z_0 & 1 \end{bmatrix}
$$

(using $\omega L=\theta Z_0$, $\omega C=\theta/Z_0$).

**Where they diverge — the lumped node is the $\omega\tau\ll1$ limit of the line.**
The off-diagonal (impedance/admittance) entries agree to $O(\theta^3)$. The
diagonal entries first diverge at $O(\theta^2)$:

$$
A_{lump}-A_{line} = (1-\theta^2)-\cos\theta = -\tfrac12\theta^2 + O(\theta^4),
\qquad
D_{lump}-D_{line} = 1-\cos\theta = +\tfrac12\theta^2 + O(\theta^4).
$$

Measured (finite-difference at $\theta=10^{-3}$): $A$-coeff $= -0.5000$,
$D$-coeff $= +0.5000$ — the analytic $\mp\tfrac12$. So the lumped LC node is the
**low-frequency ($\omega\tau\ll1$) limit** of the distributed bond TL; the first
correction is $O(\theta^2)=O((\omega\ell_{node}/c_0)^2)$, i.e. the $\omega\tau\sim1$
regime is where the lumped picture breaks.

## §2 — THE PERIODIC-CELL LINE: Bloch condition $\cos(q\ell)=\mathrm{tr(ABCD)}/2$

The lattice is a periodic chain of identical cells, one cell per bond. *Single
consistent ontology (no double-booked $C$):* $C_{CELL}=\varepsilon_0\ell_{node}$
IS the bond segment's own shunt capacitance (§1) — there is no separate node
admittance to add on top; the "loading" is the periodic cell structure itself
(the repeated series-$L$/shunt-$C$ unit), not an extra lumped node hung on a bare
line. The standard Bloch/Floquet condition on the cell ABCD is
$\cos(q\ell_{eff}) = (A+D)/2 = \mathrm{tr(ABCD)}/2$. For the lumped-node cell
($A=1-\theta^2$, $D=1$):

$$
\frac{A+D}{2} = 1-\tfrac12\theta^2 = \cos(q\ell_{node})
\;\Rightarrow\; \theta^2 = 2(1-\cos q\ell_{node}) = 4\sin^2\!\tfrac{q\ell_{node}}{2}
\;\Rightarrow\; \omega(q) = \frac{2c_0}{\ell_{node}}\left|\sin\tfrac{q\ell_{node}}{2}\right|.
$$

This **recovers the canonical LC-ladder sine-law** (`clm-gvn4r1` §1 resultbox,
`z0-derivation.md`) from the ABCD trace — the periodically-loaded-line reading of
the same dispersion. $\omega_{max}=2c_0/\ell_{node}=2\,\omega_C$; at $q\ell=\pi/2$,
$\omega/\omega_{max}=1/\sqrt2$; at the 1D-chain edge $q\ell=\pi$, $\omega/\omega_{max}=1$
(all checked).

### TL-vs-engine-Bloch CROSS-CHECK (the positive control)

**Coordinate match** (phase-space-coordinate-check): both bands are measured in
the **same** k-space variable $k\ell=|k|\cdot\ell_{node}$ (real-space Brillouin
phase per bond). Coordinate-matched — the srs corpus claim is $q$-space
dispersion and so is the TL. Not a phase-space-vs-real-space mismatch.

**Substrate-native scope** (the RANK-2 stencil guard): the 1D TL carries a
**scalar** (direction-independent) dispersion by construction. The srs eigensolve
carries the full **RANK-2** $\Phi_b=k_a\hat d\otimes\hat d+k_s(\mathbf I-\hat d\otimes\hat d)$
tensor on the $z=3$ bonds, so it also carries the direction-dependent zone-edge
anisotropy. We therefore cross-check the scalar 1D TL band against the srs
**directional-mean** acoustic speed, and separately **report** the srs directional
spread (the rank-2 anisotropy the scalar TL cannot host — reported, not forced
onto the TL; forcing it would be the Cartesian-Laplacian disabled-flag error the
srs driver warns against).

Both bands share the same small-$k$ slope (srs $c_{srs}=0.7071$ in bond-length
units, bond length $=1.0\,\ell_{node}$). The **first Brillouin zone edge** along
[100] is at $k\ell=\pi\,\ell_{node}/a\approx1.11$ (srs cubic primitive cell edge
$a=2\sqrt2\,\ell_{node}$) — a **different** zone from the 1D monatomic chain's
$k\ell=\pi$ edge:

The two comparison bands: the **lumped-node-cell** Bloch band (the $\omega\tau\ll1$
face, the sine-law) and — for honest scope — the **truly-distributed** matched-cell
linear band $\omega=c_0 q$ (dispersionless).

| $k\ell$ | $\omega_{lumpcell}$ | $\omega_{srs}$(mean) | $|lumpcell/Bloch-1|$ | $|linear/Bloch-1|$ | srs aniso spread | zone |
|---|---|---|---|---|---|---|
| 0.010 | 0.0071 | 0.0071 | $6.4\times10^{-6}$ | $2.2\times10^{-6}$ | $2.8\times10^{-6}$ | 1st BZ |
| 0.100 | 0.0707 | 0.0707 | $5.9\times10^{-5}$ | $3.6\times10^{-4}$ | $2.8\times10^{-4}$ | 1st BZ |
| 0.200 | 0.1412 | 0.1412 | $2.1\times10^{-4}$ | $1.5\times10^{-3}$ | $1.1\times10^{-3}$ | 1st BZ |
| 0.400 | 0.2810 | 0.2812 | $7.7\times10^{-4}$ | $5.9\times10^{-3}$ | $4.5\times10^{-3}$ | 1st BZ |
| 0.600 | 0.4179 | 0.4185 | $1.5\times10^{-3}$ | $1.4\times10^{-2}$ | $1.0\times10^{-2}$ | 1st BZ |
| 0.800 | 0.5507 | 0.5517 | $1.8\times10^{-3}$ | $2.5\times10^{-2}$ | $1.8\times10^{-2}$ | 1st BZ |
| 1.000 | 0.6780 | 0.6785 | $7.8\times10^{-4}$ | $4.2\times10^{-2}$ | $3.3\times10^{-2}$ | 1st BZ |
| 1.110 | 0.7452 | 0.7444 | $1.0\times10^{-3}$ | $5.4\times10^{-2}$ | $4.6\times10^{-2}$ | 1st BZ edge |
| 1.500 | 0.9640 | 0.7632 | $2.6\times10^{-1}$ | $3.9\times10^{-1}$ | $5.8\times10^{-1}$ | **folded** |
| 2.500 | 1.3421 | 0.5681 | $1.4\times10^{0}$ | $2.1\times10^{0}$ | $1.2\times10^{0}$ | **folded** |
| 2.985 | 1.4098 | 0.4767 | $2.0\times10^{0}$ | $3.4\times10^{0}$ | $1.2\times10^{0}$ | **folded** |

**Reading:**
- **Small $k\ell$ (the photon point):** the **lumped-node-cell** band and srs-Bloch
  agree to $6.4\times10^{-6}$ (at $k\ell=0.01$). **Positive control PASSES.**
- **Through the first BZ** ($k\ell<1.11$): the lumped-node-cell band tracks the srs
  directional-mean to worst $1.8\times10^{-3}$ (at $k\ell=0.8$).
- **Honest scope — lumped-vs-lumped, not distributed-vs-lumped.** The srs engine is
  itself a discrete mass-spring dynamical matrix (a generalized lumped sine-law),
  so the agreement above validates the **lumped-node-cell** band; it does NOT
  adjudicate distributed-vs-lumped bond microphysics. A **truly-distributed**
  matched-segment cell would give the **linear** band $\omega=c_0 q$
  (dispersionless — a matched line has no band-folding), deviating from srs by
  $2.5\times10^{-2}$ ($k\ell=0.8$) / $5.4\times10^{-2}$ (BZ edge) — 14–52× the
  lumped-cell headline (the $|linear/Bloch-1|$ column above). Both cells are
  legitimate readings of the SAME bond constants.
- **The srs anisotropy spread** grows monotonically $2.8\times10^{-6}\to4.6\times10^{-2}$
  across the first-BZ window — this is the **rank-2 direction-dependent zone-edge
  term** the scalar 1D TL cannot carry. It reproduces the existing engine finding:
  a nonzero $O(k^2)$ direction-dependent zone-edge dispersion.
- **Past the first BZ** ($k\ell\gtrsim1.5$, rows marked *folded*): the 1D
  monatomic-chain edge ($k\ell=\pi$) sits inside the srs's **folded higher bands**,
  so a scalar-band comparison there is comparing **different Brillouin zones**, not
  a physics discrepancy. Not counted as agreement.

## §3 — THE MATCHED-LINE READING of `clm-mfb2ax` (CONSISTENCY re-expression)

At $\rho_{bond}=1$ the internal-boundary $\Gamma$ vanishes (Ax3, `clm-mfb2ax`). In
TL language this is a **matched line**: a cascade of bond TL segments each at the
same cold $Z_0$ presents **no** impedance step at any internal node join, so
$\Gamma_{internal}=(Z_0-Z_0)/(Z_0+Z_0)=0$ at every bond. A matched line adds **no**
reflection and **no** mismatch-dispersion — this is the **Heaviside distortionless
line** condition. Driver: matched cascade $\Gamma_{internal}=4.6\times10^{-18}$
(=0); a deliberately mismatched internal bond ($Z=1.5Z_0$) reflects
$|\Gamma|=0.20$ (the reading genuinely sees a mismatch — it is not a blind zero).

> This is a **CONSISTENCY re-expression** of `clm-mfb2ax`, **NOT** a new claim. The
> Ax3 forcing of $\rho_{bond}=1$ and hence $\Gamma=0$ is the canonical result; the
> TL "matched line" is its transmission-line-native statement.

**$K<0$ honest flag (carried).** $\rho_{bond}=1$ is the lossless-reactive **photon**
operating point ($K<0$, mechanically unstable per `clm-mfb2ax` §3), NOT a stable
static solid; the matter locus is a different $\rho^\ast\approx9.77$ (GR-imported,
PR #506/#261/#521). The matched-line reading applies to the photon transverse
port only.

---

## Flags surfaced (flag-don't-fix)

**No conflict with canon.** The TL-vs-Bloch cross-check does **not** change any
zone-edge statement currently in canon. It **agrees with** the existing on-engine
finding (`srs_bloch_dispersion.py`, `clm-gvn4r1` §1.1 SCOPE GUARD, gate
`wejkhvnfb` OPEN):

- The srs eigensolve carries a nonzero direction-dependent $O(k^2)$ zone-edge term
  (my srs-anisotropy-spread column, growing to $4.6\times10^{-2}$ at the first-BZ
  edge). This is the **slope-2 $a_2$ zone-edge** that DEMOTED the $(q\ell)^4$ photon
  horn to conditional-on-weak-C. My scalar 1D TL cannot host it by construction —
  which is *why* it is a scalar isotropic band. **No new tension; the existing
  flag is re-confirmed from the TL side.**
- The continuum-exact $\delta=0$ (no-LIV) theorem remains **OPEN** (gate
  `wejkhvnfb`); this driver does not close it and does not bear on it.

## Discipline ledger

| Element | Status | Basis |
|---|---|---|
| $L_{CELL},C_{CELL}$ ARE the TL totals; $Z_0,\tau$ derived | CONSISTENCY (machine-exact) | identities, #519 constants |
| lossless-line ABCD vs lumped-LC ABCD; $O(\theta^2)$ divergence $\mp\tfrac12$ | DERIVED | standard TL ABCD; measured coeffs |
| lumped node = $\omega\tau\ll1$ limit of the distributed bond | DERIVED | the $O(\theta^2)$ first divergence |
| $\cos(q\ell)=\mathrm{tr(ABCD)}/2\Rightarrow$ sine-law | DERIVED (re-grounds `clm-gvn4r1` §1) | ABCD-trace Bloch condition |
| TL small-$k$ = srs eigensolve to $6\times10^{-6}$ | VALIDATE-ON-KNOWN (positive control) | cross-check vs `acoustic_omega` |
| TL scalar = srs dir-mean to $1.8\times10^{-3}$ across 1st BZ | VALIDATE-ON-KNOWN | cross-check |
| srs rank-2 anisotropy the scalar TL cannot host | REPORTED (re-confirms weak-C flag) | srs-aniso column; `wejkhvnfb` OPEN |
| matched-line $\Gamma_{internal}=0$ at $\rho_{bond}=1$ | CONSISTENCY re-expression of `clm-mfb2ax` | matched cascade |
| $K<0$ photon-point-not-static-solid | HONEST FLAG (carried) | `clm-mfb2ax` §3 |

**Bonus SPICE rung — SUBSUMED, not re-built.** The optional SPICE LTRA/LC-ladder
dispersion rung is already landed and merged by the concurrent SPICE phase-1 arc
([`2026-07-04_spice-phase1-ladder_result.md`](2026-07-04_spice-phase1-ladder_result.md),
Vol 9 Ch 13 §"Lattice dispersion (.AC, cold ladder)": a 40-cell LC ladder in
`ngspice-46` recovers $\omega(k)=2\omega_0|\sin(ka/2)|$ to median rel-err
$1.9\times10^{-3}$). That is the same sine-law this leaf's ABCD-trace Bloch
condition derives, cross-checked in a real SPICE engine. This driver cites it
rather than duplicating it (per the bonus-rung instruction: skip if the deliverable
is met without it).
