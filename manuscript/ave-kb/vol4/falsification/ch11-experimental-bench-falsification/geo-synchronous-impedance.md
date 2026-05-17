[↑ Ch.11: Experimental Bench Falsification](../index.md)
<!-- leaf: verbatim -->

## Protocol 12: GEO-Synchronous Impedance Differential — AVE = GR Shapiro at $O(GM/c^2r)$, corroborative-null

> **Scope correction (2026-05-16 audit):** This protocol was originally framed as a forward prediction of an AVE-extra TOF stretch beyond standard GR Shapiro on a ground-to-GEO laser link. Audit found that AVE's gravitational refractive index $n(r) = 1 + 2GM/c^2 r$ (per [`../../../vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md` line 11](../../../vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md)) is **mathematically identical to the spatial transverse trace of the Gordon optical metric** used in standard GR Shapiro derivation. Both AVE and GR compute the same $\int n(r)/c \, dr$ integral and obtain the same TOF. **There is no AVE-distinct prediction at $O(GM/c^2 r)$.** Full reconciliation at [`../../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md).

### Mechanism

Axiom 1 bounds gravity as a macroscopic spherically symmetric impedance gradient ($\Delta Z_0$). As physical altitude increases, the ambient gravitational strain relaxes, decreasing the effective dielectric load on the LC matrix. This means the effective phase velocity $c_{eff}(r) = c_0/n(r)$ is statistically faster in deep space than on the Earth's surface.

By establishing a vertical laser telecommunications link between a terrestrial ground station and a GEO satellite ($h = 35{,}786$ km), an explicit measurable Time-of-Flight (TOF) anomaly would form IF AVE's $n(r)$ differed from GR's $n(r)$. The classical linear spatial distance $d$ yields a standard TOF of $\sim 119$ ms, with a Shapiro delay correction of order $2GM_\oplus/c^3 \cdot \ln(r_{GEO}/r_\oplus)$ on top.

### Why AVE = GR at $O(GM/c^2 r)$

**AVE's gravitational refractive index is structurally identical to GR's:** per Vol 3 derivation, $n(r) = 1 + (2/7)(7GM/c^2 r) = 1 + 2GM/c^2 r$. The factor 7 from the K4 Poisson ratio $\nu_{vac} = 2/7$ cancels the factor 2/7 from the AVE-modified strain coupling, recovering exactly the GR $2GM/c^2 r$ Schwarzschild form. The leaf [`refractive-index-of-gravity.md` line 14](../../../vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md) explicitly states this is "mathematically identical to the spatial transverse trace of the Gordon optical metric."

**The TOF integral $\int n(r)/c \, dr$ is therefore the same function** in AVE and GR. Standard GR Shapiro delay arises from precisely this integral; AVE's TOF prediction at this order IS standard GR Shapiro.

### The only AVE-distinct piece is cubic-symmetry-suppressed

Per Vol 3 condensed-matter [`discrete-lattice-entropy-constant.md` line 58](../../../vol3/condensed-matter/ch11-thermodynamics/discrete-lattice-entropy-constant.md): "If $n(r)$ is non-linear across the bond ($d^2 n/dr^2 \neq 0$), the 'effective impedance' for bond transmission differs from the naive $Z_0$ value by a **higher-order correction**" — this is a discrete-lattice $(q\ell_{node})^n$ effect.

Per the cohesive narrative [`preferred-frame-and-emergent-lorentz.md` §2-4](../../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md), discrete-lattice anisotropic corrections at optical wavelength $\lambda \sim 1$ μm are suppressed by $(q\ell_{node})^4 \approx 10^{-22}$ via K4 cubic ($Fd\bar{3}m$) symmetry averaging. The AVE-distinct contribution to a GEO laser TOF would therefore be $\sim 10^{-22} \times d_{GEO} \approx 4 \times 10^{-15}$ m — far below any current or near-term laser-ranging precision.

### Corroborative-null status

AVE predicts the same Shapiro TOF as GR at $O(GM/c^2 r)$. Existing laser-ranging archives (LRO, GRACE-FO, ILRS) that confirm GR Shapiro to current precision **corroborate AVE** by construction. The protocol retires from "forward prediction" status to "corroborative-null status" — no new measurement can discriminate AVE from GR via this geometry at observable precision.

### What WOULD constitute a falsification

The cubic-suppressed $(q\ell_{node})^4 \sim 10^{-22}$ residual would only become detectable at sub-$\ell_{node}$ probe wavelengths, where cubic-symmetry averaging breaks down. The surviving Trans-Planckian preferred-frame test in the AVE matrix is GRB Trans-Planckian dispersion (matrix row C7-GRB-DISPERSION) per [`../ch12-falsifiable-predictions/binary-kill-switches.md`](../ch12-falsifiable-predictions/binary-kill-switches.md). Optical-wavelength vertical-impedance-integration tests cannot reach the precision required to discriminate $10^{-22}$ from $0$; this protocol class is observationally exhausted by existing GR Shapiro confirmations.

### Note on the "16.7 mm" figure

Prior matrix and appendix revisions cited a "16.7 mm" TOF stretch. This number does not appear in the current source leaf or any companion derivation chain. The source leaf states "fractions of a millimeter" (a 16,700× discrepancy). The 16.7 mm figure was an asserted matrix entry without derivation backing; **per audit, it is retracted** because the underlying AVE = GR identity at $O(GM/c^2 r)$ predicts no AVE-extra term at this order.

---
