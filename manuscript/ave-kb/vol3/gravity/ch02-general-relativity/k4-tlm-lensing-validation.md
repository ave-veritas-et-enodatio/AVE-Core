[↑ Ch.2 General Relativity](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-rd9cjm]
path-stable: "referenced from vol4 as sec:k4_tlm_lensing"
-->

---

## K4-TLM Gravitational Lensing Cross-Validation

The preceding sections derive photon deflection analytically---$\delta = 4GM/(bc^2)$---and validate it via Hamiltonian raymarching. We now cross-validate the same physics with the K4-TLM native lattice dynamics simulator (Section sec:k4\_tlm, Vol. 4), which time-evolves electromagnetic waves natively through the pure Diamond lattice vacuum.

### Method

In a true K4-TLM Diamond lattice, the presence of mass is implemented strictly via Op14 continuous saturation. An exceptionally dense coordinate is designated as the mass origin. As incident scalar amplitude $\sum|V|$ grows uncontrollably near this point, Op14 dictates that the local geometry saturates.

This builds a static $Z_{local}$ gradient across the network:

$$
Z_{\text{local}}(r) = \frac{Z_0}{S^{1/2}} = \frac{Z_0}{\sqrt{S}}
$$

> **Register correction (2026-07-14, quarter-power map §Family-E; KEEP-BOTH).**
> Previously stated as $Z_{\text{local}} = Z_0/S^{1/4}$ — the legacy register that
> let the Family-E $S^{1/4}=(1-A^2)^{1/8}$ exponent ride in, un-propagated.
> Corrected to the canonical Op14 register $Z = Z_0/\sqrt{S}$ (`operators.md:54`;
> `cosserat_field_3d.py:425`, `Z_eff = 1/\sqrt{S}`). Prior form preserved here for
> provenance. ⚑ **Downstream flag (auditor):** with $Z_0/\sqrt{S}$, the
> $c_{\text{local}} = c_0\sqrt{Z_0/Z_{\text{local}}}$ relation below yields
> $c_0 S^{1/4}$, which still differs from the canonical shear/lensing slow-down
> $c_{\text{shear}} = c_0\sqrt{S}$. That $c_{\text{local}}$ derivation relation is
> a SEPARATE un-propagated item, NOT silently rewritten here (it touches the
> still-open sign/ontology fork, map §3).

The refractive index operates directly within the explicit 4-port scattering matrices ($S_{ij} = \frac{y_{local}}{2} - \delta_{ij}$), passively slowing the effective wave speed $c_{\text{local}} = c_0 \sqrt{Z_0/Z_{\text{local}}}$.

A photon wavepacket is injected into the lattice, propagating toward the mass defect with a finite impact parameter.

### Results

As the wide photon wavefront encounters the topological saturation gradient, the inner side of the wavefront (closest to the mass) enters the high-impedance zone first. This forces the inner pulse to slow down, while the outer pulse remains traveling at $c_0$ in the free vacuum.

This impedance mismatch organically pivots the entire wavefront downward into the mass defect.

> → Primary: [K4-TLM Simulator](../../../vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md) — outbound sec:k4\_tlm reference (source line 115); vol4 not yet distilled

---
