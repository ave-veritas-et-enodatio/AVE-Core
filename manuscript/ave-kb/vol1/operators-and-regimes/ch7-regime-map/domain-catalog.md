[↑ Ch.7 Regime Map](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-b2anl4, clm-82dxbj]
path-stable: "referenced from vol1 as sec:domain_catalog"
-->

## Section 7.2: Domain Control Parameter Catalog
<!-- claim-quality: clm-82dxbj -->

Each domain has a unique physical interpretation of the amplitude $A$ and the critical threshold $A_c$. In every case, $A_c$ is **derived from the four axioms**---it is never a fitted or empirical parameter.

> ↗ See also: [Temporal Saturation Regime Classifier](../../../common/temporal-saturation-regime-classifier.md) — companion leaf introducing the orthogonal temporal axis (lossless / cyclic / lossy) on top of the Regime I-IV spatial-instantaneous classification per this catalog. Maps additional field domains (semiconductor, plasma, MHD, nonlinear optics, cavity QED, tribology, polymer dynamics, magnonics, etc.) to the AVE regime framework.

<!-- claim-quality: clm-b2anl4 (regime classification applied per-domain throughout this catalog) -->
### Electromagnetic (Dielectric)

| | |
|---|---|
| Amplitude $A$ | Applied voltage $V$ |
| Critical $A_c$ | $V_{yield} = \sqrt{\alpha} \cdot V_{snap} = \sqrt{\alpha} \cdot m_e c^2/e \approx 43.65$ kV |
| Control parameter | $r = V / V_{yield}$ |

**Regime locations:**
- Lab capacitor (1 kV): $r = 0.023$ --- Regime I
- HV Capacitor @ 30 kV: $r = 0.687$ --- Regime II
- HV Capacitor @ 43 kV: $r = 0.985$ --- Regime III
- Schwinger pair production: $r = 1.0$ --- Regime IV boundary

### Electromagnetic (Field Strength)

| | |
|---|---|
| Amplitude $A$ | Local electric field $E$ |
| Critical $A_c$ | $E_{yield} = V_{yield}/\ell_{node} \approx 1.13 \times 10^{17}$ V/m |
| Control parameter | $r = E / E_{yield}$ |

At the lattice scale, even extreme laboratory fields ($10^6$ V/m) correspond to $r \sim 10^{-11}$, deep in Regime I. The Schwinger critical field ($E_S = m_e^2 c^3/(e\hbar) \approx 1.32 \times 10^{18}$ V/m) corresponds to $r = E_S/E_{yield} = V_{snap}/V_{yield} = 1/\sqrt{\alpha} \approx 11.7$, deep in Regime IV.

### Gravitational

| | |
|---|---|
| Amplitude $A$ | Principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ |
| Critical $A_c$ | Unitary strain = 1 |
| Control parameter | $r = \varepsilon_{11}$ |

The factor of 7 arises from the 7 compliance modes of the K4/SRS lattice ($\nu_{vac} = 2/7$). **Regime locations:**
- Solar surface: $\varepsilon_{11} = 1.486 \times 10^{-5}$ --- Regime I
- White dwarf (Sirius B): $\varepsilon_{11} \approx 1.81 \times 10^{-3}$ --- Regime I
- Neutron star (1.4 $M_\odot$, $R = 10$ km): $\varepsilon_{11} \approx 1.46$ --- Regime IV
- Black hole at $r_s = 2GM/c^2$: $\varepsilon_{11} = 7/2 = 3.5$ --- Regime IV

> **Correction (2026-08-01 — factor-7 residual; flagged by two independent audits).** The solar-surface row previously read $\varepsilon_{11} = 2.1 \times 10^{-6}$, which is exactly $GM_\odot/(c^2R_\odot) = 2.123 \times 10^{-6}$ — the **un-multiplied Newtonian potential**, a factor of 7 low against this leaf's own $\varepsilon_{11} = 7GM/(c^2r)$ definition above. Recomputed on canonical constants ($G$, $c$, $M_\odot$ from [`constants.py`](../../../../../src/ave/core/constants.py); $R_\odot = 6.957\times10^{8}$ m, IAU nominal): $7GM_\odot/(c^2R_\odot) = 1.486\times10^{-5}$. This is a **residual of the 2026-05-17 factor-7 cleanup** logged at [`claim-quality-closure-roadmap.md`](../../../claim-quality-closure-roadmap.md) (row C11-MACH-ZEHNDER, commit `d48f75d`) — that pass corrected the driver, the C11 source leaf, `eq_gravity_derived.tex` and the matrix, but did not reach this catalog. The neighbouring neutron-star ($7 \times 0.2068 = 1.4475 \approx 1.46$) and black-hole ($7/2 = 3.5$) rows already carried the 7 and are unchanged; so does the companion red-giant row in [`stellar-regime-classification.md`](../../../vol3/applied-physics/ch07-stellar-interiors/stellar-regime-classification.md) ($7 \times 1.062\times10^{-7} = 7.43\times10^{-7} \approx 7\times10^{-7}$). **Not corrected here — routed:** the white-dwarf row states no $M$ or $R$, so it is not decidable from *this* file alone — but the corpus carries a decider, and **two KB leaves disagree by exactly 7 on the same body.** [`white-dwarf-gravitational-predictions.md`](../../../vol3/gravity/ch20-white-dwarf-predictions/white-dwarf-gravitational-predictions.md) tabulates Sirius B at $M = 1.018\,M_\odot$, $R = 5800$ km under this same $\varepsilon_{11} = 7GM/(c^2R)$ definition and prints $1.81\times10^{-3}$ — the **with-7** value at those stated parameters ($7GM/(c^2R) = 1.8148\times10^{-3}$). The $3\times10^{-4}$ in the row above is the **un-7'd** $GM/(c^2R) = 2.59\times10^{-4}$ at the same parameters — which is also the **measured gravitational redshift**, the observable its vol3 companion table's *Physical consequence* column cites. The two leaves are therefore tabulating *different quantities*, not different roundings. Adjudication routed, not resolved here.

> **Resolution (2026-08-02 — Grant ruling D8, verbatim [sic]: *"2. correct plus note"*). The white-dwarf row is CORRECTED to the with-7 strain; the displaced number is NOT deleted, because it is a different observable and it is named as such below.** This discharges the *"Not corrected here — routed"* disposition in the 2026-08-01 note immediately above, whose text is **preserved unedited per Rule 12** — that audit's diagnosis (two leaves tabulating different quantities on the same body) was right, and this ruling picks the arm.
> **(a) The corrected value.** At the Sirius B parameters the corpus's own decider tabulates — $M = 1.018\,M_\odot$, $R = 5800$ km, [`white-dwarf-gravitational-predictions.md`](../../../vol3/gravity/ch20-white-dwarf-predictions/white-dwarf-gravitational-predictions.md)`:32` — this leaf's own definition $\varepsilon_{11} = 7GM/(c^2 r)$ (the Amplitude row above) gives, on canonical constants ($G$, $c$, $M_\odot = 1.989\times10^{30}$ kg from [`constants.py`](../../../../../src/ave/core/constants.py)):
> $$\varepsilon_{11} = \frac{7GM}{c^2R} = 1.8148\times10^{-3} \;\rightarrow\; 1.81\times10^{-3}$$
> which **byte-matches the value that companion leaf already carried**, so the two leaves now agree instead of disagreeing by exactly the factor under audit. The body is named in the row because the number is body-specific, not a generic white-dwarf order of magnitude: the same companion table runs $6.58\times10^{-4}$ (40 Eridani B) to $1.81\times10^{-3}$ (Sirius B).
> **(b) THE NOTE — the displaced $3\times10^{-4}$ was never a rounding of the strain; it is a DIFFERENT OBSERVABLE, and it is the one the consequence column actually cites.** The un-7'd $GM/(c^2R) = 2.59\times10^{-4}$ at the same parameters (which $3\times10^{-4}$ is the one-significant-figure round of) is the **measured gravitational redshift** $z$ — not the principal radial strain. Receipt that this is the observable and not a bookkeeping coincidence: $c\,GM/(c^2R) = 77.72$ km/s, and the exact-Schwarzschild redshift at the same $M$, $R$ is $77.75$ km/s — **exactly the $v_{\text{GR}} = 77.75$ km/s** the companion leaf's Sirius B resultbox quotes against the $80.65 \pm 0.77$ km/s spectroscopic measurement. So the *Physical consequence* column's *"Gravitational redshift $\sim 10^{-4}$"* in [`stellar-regime-classification.md`](../../../vol3/applied-physics/ch07-stellar-interiors/stellar-regime-classification.md)`:18` is **correct and unchanged** — it was always describing the redshift, which is the un-7'd potential; only the $\varepsilon_{11}$ *column* was filing that number under the strain. **The 7 is the difference between the two quantities, not a correction to either:** the strain carries the 7 compliance modes ($\nu_{vac} = 2/7$), the redshift does not. Both numbers are right for their own quantity; only the filing was wrong. **Do not swap them back.**
> **(c) Mirrors corrected in the same pass** (value-only, following the 2026-08-01 solar-row precedent, which likewise noted in the KB and edited values in the `.tex`): [`stellar-regime-classification.md`](../../../vol3/applied-physics/ch07-stellar-interiors/stellar-regime-classification.md)`:18` (+ condensed note), `vol_1_foundations/chapters/07_regime_map.tex`, `vol_3_macroscopic/chapters/07_stellar_interiors.tex`, `vol_9_vacuum_datasheet/chapters/14_phase_diagrams.tex`. **Code sites are NOT touched and stay ROUTED:** the driver's own white-dwarf entry still reads the un-7'd value — `src/ave/core/regime_map.py:524`, `("White dwarf", 3.0e-4, 1.0, "strain")`, verified at this commit — and the three-convention mix around it is explicitly **outside this ruling's scope**. Surfaced here so the doc/code divergence is on the record rather than silently opened by this correction.

*The neutron star result demands attention.* A 1.4 $M_\odot$ star at $R = 10$ km has $\varepsilon_{11} = 1.46 > 1$, placing it in Regime IV (ruptured topology). This is the AVE analog of the Buchdahl limit: no static configuration can have $r < 9GM/4c^2$ (where $\varepsilon_{11} > 63/36 = 1.75$). In AVE, the saturation boundary defines an absolute limit on gravitational compactness --- the lattice topology cannot support strain beyond unity.

> **[Examplebox]** *Evaluating the Gravitational Regime of a Black Hole*
>
> **Problem:** Calculate the dimensionless control parameter $r$ for the gravitational strain at the Event Horizon ($r_s = 2GM/c^2$) of a black hole, and determine its operating regime.
>
> **Solution:** In the gravitational domain, the amplitude $A$ is the principal radial strain $\varepsilon_{11} = 7GM/(c^2 R_{radial})$, where the factor of 7 arises from the 7 compliance modes of the K4 lattice. The critical capacity of the lattice is unitary strain ($A_c = 1$).
> At the Schwarzschild radius $R_{radial} = r_s = 2GM/c^2$:
>
> $$
> r = \frac{A}{A_c} = \frac{7GM/(c^2 \cdot (2GM/c^2))}{1} = \frac{7}{2} = 3.5
> $$
>
> Because $r = 3.5 \ge 1.0$, the local spatial metric has structurally failed. The LC network at the event horizon is in **Regime IV (Ruptured)**, meaning topological coherence is destroyed and local scalar $c_{eff} = 0$.

### BCS / Superconducting

| | |
|---|---|
| Amplitude $A$ | Temperature $T$ (or magnetic field $B$) |
| Critical $A_c$ | $T_c$ (or $B_{c0}$) |
| Control parameter | $r = T/T_c$ |

The BCS relation $B_c(T) = B_{c0}\sqrt{1 - (T/T_c)^2}$ IS the AVE saturation operator, with $A = T$ and $A_c = T_c$. Below $T_c$: superconducting ($S > 0$, Meissner effect active). At $T_c$: normal state ($S = 0$, topology destroyed).

### Magnetic

| | |
|---|---|
| Amplitude $A$ | Applied magnetic field $B$ |
| Critical $A_c$ | $B_{snap} = m_e^2 c^2/(e\hbar) \approx 1.89 \times 10^9$ T |
| Control parameter | $r = B / B_{snap}$ |

Lab magnets ($\sim$10 T) have $r \sim 10^{-8}$ (Regime I). A magnetar surface field ($\sim 10^{10}$ T) has $r \sim 5$ (Regime IV). At $B_{snap}$, the vacuum permeability $\mu_{eff}$ reaches zero --- the vacuum becomes a perfect diamagnet (the Meissner effect of the vacuum itself).

### Nuclear

| | |
|---|---|
| Amplitude $A$ | $d_{sat}/r_{sep}$ (confinement ratio) |
| Critical $A_c$ | 1 (Pauli wall) |
| Control parameter | $r = d_{sat}/r_{sep}$ |

When $r_{sep} > d_{sat}$: $r < 1$, the interaction potential $U(r) = -(K/r)(1 - 2\Gamma^2)$ is attractive (Regime I--III). When $r_{sep} \leq d_{sat}$: $r \geq 1$, $\Gamma \to 1$, the potential becomes repulsive --- this is Pauli exclusion from first principles.

### Gravitational Waves

| | |
|---|---|
| Amplitude $A$ | GW strain $h$ |
| Critical $A_c$ | $h_{yield} = \sqrt{\alpha} \approx 0.0854$ |
| Control parameter | $r = h / \sqrt{\alpha}$ |

LIGO detections ($h \sim 10^{-21}$) correspond to $r \sim 10^{-20}$ --- the most deeply linear measurement in physics. A neutron star merger at the surface ($h \sim 0.01$) reaches $r = 0.117 < \sqrt{2\alpha} = 0.121$ --- still in Regime I. The correction $\Delta S = 0.007 < \alpha$ is sub-$\alpha$ and unresolvable. A strong merger at $h \sim 0.02$ ($r = 0.23$) enters Regime II.

### Galactic Rotation

| | |
|---|---|
| Amplitude $A$ | Newtonian gravitational acceleration $g_N$ |
| Critical $A_c$ | $a_0 \approx 1.2 \times 10^{-10}$ m/s$^2$ |
| Control parameter | $r = g_N / a_0$ |

*Note:* The galactic domain uses the **same** universal operator as every other domain: $S(r \to 1)$ means medium compliance $\to 0$. What differs is the *observational consequence*: in EM, $\varepsilon \to 0$ produces pair production (dramatic). In gravity, $G_{shear} \to 0$ produces an event horizon (dramatic). In the galactic domain, $\eta \to 0$ means the lattice drag *vanishes*, leaving simple Newtonian gravity (unspectacular).

The "dark matter problem" **IS** the Regime III$\to$IV phase transition. At $r = g_N/a_0 \approx 1$, the lattice mutual inductance undergoes the same phase transition as every other domain. "Dark matter" is the drag that exists on the Regime I--III side of this boundary. Inner-galaxy stars at $g_N \gg a_0$ ($r \gg 1$) are in Regime IV: the lattice is fully saturated, drag is zero, orbits are Keplerian. Outer-galaxy stars at $g_N \ll a_0$ ($r \ll 1$) are in Regime I: the lattice is unsaturated, full drag produces $g_{eff} \to \sqrt{g_N \cdot a_0}$ (flat rotation curves).

---
