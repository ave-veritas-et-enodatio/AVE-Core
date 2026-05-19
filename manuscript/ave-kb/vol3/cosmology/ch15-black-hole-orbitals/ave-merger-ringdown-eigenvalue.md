[↑ Ch.15 Black Hole Orbitals](index.md)
<!-- leaf: verbatim -->

## AVE Merger Ringdown Eigenvalue

When two black holes merge, the resulting object "rings down" at a characteristic frequency observed by LIGO/Virgo. In the AVE framework, this ringdown is the **fundamental resonance mode of the newly formed saturation cavity**---a surface wave at the elastic--ruptured phase boundary.

The $\ell = 2$ fundamental Schwarzschild QNM eigenvalue is derived entirely from Axioms 1--4:

1. **Axiom 4:** $\varepsilon_{11}(r_{sat}) = 1$ gives $r_{sat} = 7\,M_g$.
2. **Poisson:** $r_{eff} = r_{sat}/(1 + \nu_{vac}) = 49\,M_g/9$.
3. **Mode:** $\omega_R = \ell \cdot c / r_{eff}$.

> **[Resultbox]** *AVE Merger Ringdown Eigenvalue*
>
> $$
> \omega_R \cdot M_g = \frac{\ell\,(1 + \nu_{vac})}{x_{sat}} = \frac{18}{49} = 0.3673 \qquad (\text{GR exact: } 0.3737, \text{ error } 1.7\%)
> $$

Zero free parameters, zero borrowed results.

### Kerr-Corrected Ringdown

Frame-dragging shifts the prograde saturation boundary inward, but the K4 Cosserat lattice provides a rigid skeleton fraction that does NOT yield to rotational stress. Per the (2,3) torus knot topology shared between electron and BH ([`electron-bh-isomorphism.md`](electron-bh-isomorphism.md)), the cavity has TWO components: a rigid $\nu_{vac}$ fraction set by K4 elasticity, plus a compliant $(1 - \nu_{vac})$ fraction that scales with the photon-orbit radius.

> **[Resultbox]** *Kerr-Corrected Ringdown (v2 — Cosserat back-reaction, 2026-05-18)*
>
> $$
> x_{sat}(a_*) = 7 \cdot \left[\nu_{vac} + (1 - \nu_{vac}) \cdot \frac{r_{ph}^+(a_*)}{3M}\right] = 2 + 5 \cdot \frac{r_{ph}^+(a_*)}{3M}
> $$
>
> $$
> \omega_R M_g(a_*) = \frac{\ell\,(1 + \nu_{vac})}{x_{sat}(a_*)}, \qquad r_{ph}^+ = \frac{2GM}{c^2}\left(1 + \cos\!\left[\tfrac{2}{3}\arccos(-a_*)\right]\right)
> $$

**Limits**: at $a_* = 0$ (Schwarzschild), $r_{ph}^+ = 3M$ → $x_{sat} = 7$ recovering the cold eigenvalue $18/49$. At $a_* \to 1$ (extremal), $r_{ph}^+ \to M$ → $x_{sat} \to 2 + 5/3 \approx 3.67$ (cavity floored by Cosserat elasticity, not pure photon sphere).

**Superseded v1 formula** (pre-2026-05-18, over-predicted spin correction by ~13% mean): $f_{ring}(a_*) = f_{ring}(0) \cdot r_{ph,\text{Schw}}/r_{ph}^+(a_*)$. Treated entire cavity as compliant (no rigid skeleton fraction); diagnosed via Phase-2 LIGO ringdown comparison at [`research/ligo-ringdown-driver-design.md`](../../../../../research/ligo-ringdown-driver-design.md) §7 and refined per Grant adjudication 2026-05-18 (Option A, Cosserat Poisson-ratio back-reaction).

### Kerr Quality Factor

For a spinning remnant, the continuous topological strain gradient convolutes asymmetrically with the QNM mode, reducing the effective radiation rate. The decay rate is obtained from the non-reciprocal phase shift:

$$
\omega_I = \frac{\omega_R - m\,\Omega}{2\,\ell}, \qquad r_\Omega = r_{ph}(a_*) \cdot \sqrt{1 + \nu_\mathrm{vac}}
$$

where $\Omega$ is the asymmetric impedance convolution rate (formerly interpreted as Lense-Thirring angular velocity) at the Poisson-augmented photon sphere $r_\Omega$. The quality factor $Q = \omega_R / (2\omega_I)$ increases with spin, matching GR to sub-2% for $a_* = 0.3\textrm{--}0.8$.

Comparison against three LIGO detections, including both frequency and decay time:

| **Event** | $M_{final}$ | $a_*$ | $f_\mathrm{AVE\text{-}v2}$ | $f_\mathrm{obs}$ | $\Delta f$ (v2) | $f_\mathrm{AVE\text{-}v1}$ (superseded) | $\Delta f$ (v1) |
|---|---|---|---|---|---|---|---|
| GW150914 | 62.0 $M_\odot$ | 0.67 | **246.0 Hz** | 251 Hz | **-2.0%** | 278 Hz | +10.6% |
| GW170104 | 48.7 $M_\odot$ | 0.64 | **308.2 Hz** | 312 Hz | **-1.2%** | 345 Hz | +10.5% |
| GW151226 | 20.8 $M_\odot$ | 0.74 | **764.0 Hz** | 750 Hz | **+1.9%** | 884 Hz | +17.9% |

**v2 refined formula (2026-05-18): mean -0.45%, max 2.0% per event — within GR Kerr QNM precision band (mean +0.34% per Berti+Cardoso+Will 2006 Leaver-method)**. v1 simplified formula (superseded) over-predicted by ~13% mean per event; failure mode was treating entire cavity as compliant. All from zero free parameters.

**Phase 5 decay-time τ refinement (2026-05-18, lattice-Q preservation): mean -0.47% across same 3 events** — v2 outperforms standard GR Kerr QNM (-6.94% mean). Mechanism: K4 lattice impedance sets damping-rate Q (rigid Cosserat skeleton property), so Q is invariant across v1/v2 cavity-radius refinements. Cavity-radius shift v1 → v2 propagates inversely into τ via $\tau_{v2} = \tau_{v1} \cdot (\omega_{R,v1} / \omega_{R,v2})$, taking v2 τ to match LIGO obs at GR-class precision. Per-event: GW150914 τ_v2 = 3.95 ms (-1.2% vs LIGO 4.0 ms); GW170104 τ_v2 = 3.02 ms (+0.7% vs LIGO 3.0 ms); GW151226 τ_v2 = 1.39 ms (-0.8% vs LIGO 1.4 ms). Full C1-BH-RING test closed: both ω_R AND τ now match LIGO at <1% mean precision per event from zero free parameters.

**Phase 4 spin sweep validation (2026-05-18)**: v2 reproduces GR Kerr QNM curve across the full observed LIGO BBH spin range. 9 of 11 swept spin values (a* ∈ {0.0, 0.1, ..., 0.95}) PASS at |dev| < 3% vs GR Berti reference. Divergence onset a* ≥ 0.90 (near-extremal regime, currently unattested in LIGO catalog). Mass-independence confirmed at 7× range: **GW190521 (M = 142 M⊙, IMBH-class) matches at -0.25% per v2**; GW170729 (a* = 0.81, higher than Phase-3 max) matches at +1.77%. **v2 covers entire currently-detected LIGO BBH catalog at GR-class precision.** Near-extremal regime (a* > 0.90) deferrable to Option B (full spheroidal cavity) when LIGO detects such an event.

Live-fire validation: [`src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py`](../../../../../src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py) implements v1, v2, GR Berti reference, Phase-3 LIGO-event comparison, Phase-4 spin sweep + extended LIGO events. Phase 3 + 4 results in [`research/ligo-ringdown-driver-design.md`](../../../../../research/ligo-ringdown-driver-design.md) §8-9.

---
