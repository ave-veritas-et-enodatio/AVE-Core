[↑ Ch.15 Black Hole Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-395gps]
-->

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

Zero free parameters, zero borrowed results. **This cold Schwarzschild eigenvalue
SURVIVES the 2026-07-20 correction below** — it is the genuine, single-point, zero-free-parameter
result of this section ($-1.7\%$ vs Kerr). (Per the FORM/VALUE carve, $\nu_{vac}=2/7$'s VALUE is
GR-imported via $K=2G$, PR #261; FORM-derived only.)

> **🔴 SUPERSEDED (2026-07-20, kerr-table-canon-correction lane, upstream of PR #772) — the
> spinning-remnant "match" below is a FRAME ARTIFACT.**
>
> Everything in the "Kerr-Corrected Ringdown", "Kerr Quality Factor", Phase-4, and Phase-5
> subsections that reports sub-percent agreement with LIGO (the banked $-0.45\%$ mean $\omega_R$,
> $-0.47\%$ mean $\tau$, "FULL PASS", "covers entire LIGO BBH catalog at GR-class precision") is
> **retracted as a compensating-error artifact**. Two independent defects:
> 1. The GR Kerr QNM reference table (`ligo_ringdown_driver.py`) was **wrong at spin** by
>    $-9.4\%$ to $-26.8\%$ (a*=0.70–0.95); corrected 2026-07-20 (qnm + BCW-2006, three-source).
> 2. The comparison used **source-frame** final masses against **detector-frame** observed
>    frequencies; since $f\propto 1/M$, the $\approx 9\%$ mass gap inflated the prediction by
>    $\approx 9\%$, cancelling a genuine $\approx -10\%$ below-Kerr deficit into a spurious "match".
>
> **Honest state (frame-independent dimensionless eigenvalue ratio, depends only on spin a\*):
> AVE-v2 sits $-9.5\%$ mean BELOW true Kerr** at the catalog spins (GW150914 $-9.2\%$, GW170104
> $-8.6\%$, GW151226 $-10.8\%$), growing with spin ($-12.6\%$ at a*=0.80, $-20\%$ at 0.95) —
> **$-9.53\%$ under the banked v2 $x_{sat}(a_*)$ spin mapping; mapping-conditional.** The
> detector-frame frequency check confirms GW150914 at $-10.1\%$ (true Kerr at detector-frame mass
> reproduces the observed 251 Hz to $-1.0\%$; AVE-v2 gives 226 Hz). Re-run + provenance:
> [`research/2026-07-20_kerr-table-correction_result.md`](../../../../../research/2026-07-20_kerr-table-correction_result.md)
> + [`_rerun.py`](../../../../../research/2026-07-20_kerr-table-correction_rerun.py). The v2 FORMULA
> below is unchanged (it is still AVE's spinning prediction); only its "matches LIGO" validation is retracted.
>
> **★ Mapping-conditional — the v1↔v2 fork REOPENS (routed to Grant).** The $-9.53\%$ is
> conditional on the **retained v2** mapping. On the same frozen C-1 comparator the **retired v1**
> mapping sits **+2.63% mean** vs corrected Kerr — *inside* the frozen `MATCH-SURVIVES |D̄| < 3%`
> band — and its 2026-05-18 retirement for v2 rode the same corrupt table + frame mixing (see the
> 🔴 CORRECTION under "Kerr-Corrected Ringdown" below). v1 is **not re-banked** here; the
> re-adjudication is Grant's. Fork-reopen note:
> [`…_result.md`](../../../../../research/2026-07-20_kerr-table-correction_result.md) § FORK-REOPEN.

> **🟩 GRANT RULING — the reopened fork is RULED (2026-07-21, Ruling B1; body above preserved per
> Rule 12).** Grant, verbatim `[sic]`: *"ruling 1 proceed with your rec, ruling 2 walk back now."*
> Ruling 1 = option **B1** on the reopened v1↔v2 spin-mapping fork (evidence brief:
> [`research/2026-07-20_v1-spin-mapping-adjudication_result.md`](../../../../../research/2026-07-20_v1-spin-mapping-adjudication_result.md),
> the corrected-τ MIXED verdict + mirror-split package; upstream MATCH-ARTIFACT re-adjudication
> [`…_kerr-table-correction_result.md`](../../../../../research/2026-07-20_kerr-table-correction_result.md)).
>
> - **v1 RE-SELECTED as the standing $\omega_R$ spin-mapping phenomenology.** $x_{sat,v1} = 7\,r_{ph}^+/3M$
>   (entire-cavity-compliant; $\omega_R M_g = \ell(1+\nu_{vac})/x_{sat,v1}$) is the standing Kerr $\omega_R$
>   mapping, replacing v2. On the frozen C-1 dimensionless comparator v1 sits **+2.63% mean** on the
>   primary catalog (a\*=0.64/0.67/0.74 → +2.24/+2.50/+3.17%; *inside* the `|D̄| < 3%` MATCH band) and
>   **+3.36% mean** on the secondary higher-spin set (marginal, 3–5%; overshoot grows monotonically with
>   spin). **Grade UNCHANGED: solidity 0.55, build_status "use as input only", disclosed-phenomenological**
>   — the mapping-conditional + phenomenological-photon-sphere-shift riders are RETAINED (v1 is the
>   *simpler* phenomenology, single-component; it is NOT more first-principles-derived than v2 — both are
>   disclosed phenomenological per clm-395gps). This is a **consistency-class** spinning match, NOT a
>   zero-free-parameter benchmark; the only zero-parameter content remains the cold $18/49$ eigenvalue.
> - **v2 preserved verbatim as superseded.** The v2 Resultbox + all v2 text below stay per Rule 12. Note
>   the **mirror-image split**: under the committed Model-B $\tau$ chain, v2 gives $\bar D_Q = +2.12\%$
>   (τ-*matches*), but v2's $\omega_R$ *fails* at −9.53% — v2 near-matches τ only by compensating ω_R/ω_I
>   errors. **No mapping matches on both axes.**
> - **τ STATE BANKED — OPEN NEAR-MISS TENSION (not a match, not a kill).** v1's *actual* corpus τ model
>   is the spin-refined $\omega_I = (\omega_R - m\Omega)/(2\ell)$ at $r_\Omega = r_{ph}\sqrt{1+\nu_{vac}}$
>   with **$\Omega$ corpus-pinned** (Ch.2 frame-dragging Resultbox $\omega(r) = 2Mar/(r^2+a^2)^2$,
>   clm-rd9cjm at $r_\Omega$; the chain regenerates the asserted KB τ = 3.5/2.7/1.2 ms to rounding). Against
>   corrected-Kerr Q it gives **$\bar D_Q = -5.44\%$** (Resultbox form) / **$-4.57\%$** (exact-equatorial-ZAMO
>   variant — sensitivity flagged): an **OPEN τ near-miss tension**, outside the frozen band but far from the
>   cold-model failure. Phase-5's `−0.47%` τ "match" and "outperforms GR" stay RETRACTED (2026-07-20 banners
>   below). The τ tension is the **named next ringdown work** (why −5.4%: the $r_\Omega$ / $\nu_{vac}$ factor
>   / mapping — a queued Q-law derivation, not a closed result).
> - **Q-LAW COMMITMENT.** The **spin story is the mΩ law** $\omega_I = (\omega_R - m\Omega)/(2\ell)$ (above);
>   the topological **$Q = \ell$ (cold flat-Q) is scoped to the a\*=0 anchor** — the $\Omega \to 0$ limit of
>   the mΩ law (`qnm-quality-factor.md`). The flat $Q = \ell = 2$ reading would fail at $-38\%$ at catalog
>   spins (corrected-Kerr Q rises 3.07→3.49); the mΩ law is what carries the spin dependence.
>
> Superseded routing note: the "re-adjudication is Grant's / v1 not re-banked" text above (2026-07-20) is
> now DISCHARGED — this ruling IS that re-adjudication. v1 re-bank + this Q-law scope + the near-extremal
> 54/49 forward promotion land per Ruling B1.

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

**Superseded v1 formula** (pre-2026-05-18, ~~over-predicted spin correction by ~13% mean~~ — **that diagnosis is RETRACTED 2026-07-20; see the correction note below**): $f_{ring}(a_*) = f_{ring}(0) \cdot r_{ph,\text{Schw}}/r_{ph}^+(a_*)$. Treated entire cavity as compliant (no rigid skeleton fraction); diagnosed via Phase-2 LIGO ringdown comparison at [`research/ligo-ringdown-driver-design.md`](../../../../../research/ligo-ringdown-driver-design.md) §7 and refined per Grant adjudication 2026-05-18 (Option A, Cosserat Poisson-ratio back-reaction).

> **🔴 CORRECTION (2026-07-20, kerr-table-canon-correction lane, upstream of PR #772) — the "v1 over-predicted ~13% mean" diagnosis above is itself the FRAME-MIXED ARTIFACT.** The "~13%" figure (verbatim `design doc §8.2:288 "Mean AVE-v1-vs-LIGO: +12.98%"`) is v1 frequency at **source-frame** mass vs **detector-frame** `f_obs`, reproducible only against the corrupt Kerr table — **not** a dimensionless comparison to true Kerr. Against **corrected** Kerr on the frozen **C-1 dimensionless comparator**, the retired v1 mapping ($x_{sat,v1}=7\,r_{ph}^+/3M$, entire cavity compliant) sits at **+2.24%/+2.50%/+3.17%** at a\*=0.64/0.67/0.74 (**mean +2.63%**) — *inside* the prereg's frozen `MATCH-SURVIVES |D̄| < 3%` band — while the retained v2 sits at **−9.53%** (MATCH-ARTIFACT), and v1 outperforms v2 at every catalog spin. The Option-A adjudication that retired v1 for v2 rode this same artifact. **★ The v1↔v2 spin-mapping fork therefore REOPENS — routed to Grant (substrate-adjudicates-forks); v1 is NOT re-banked here** (it was never under this prereg's frozen bins). Provenance + fork-reopen note: [`research/2026-07-20_kerr-table-correction_result.md`](../../../../../research/2026-07-20_kerr-table-correction_result.md) § FORK-REOPEN.

### Kerr Quality Factor

For a spinning remnant, the continuous topological strain gradient convolutes asymmetrically with the QNM mode, reducing the effective radiation rate. The decay rate is obtained from the non-reciprocal phase shift:

$$
\omega_I = \frac{\omega_R - m\,\Omega}{2\,\ell}, \qquad r_\Omega = r_{ph}(a_*) \cdot \sqrt{1 + \nu_\mathrm{vac}}
$$

where $\Omega$ is the asymmetric impedance convolution rate (formerly interpreted as Lense-Thirring angular velocity) at the Poisson-augmented photon sphere $r_\Omega$. The quality factor $Q = \omega_R / (2\omega_I)$ increases with spin ~~matching GR to sub-2% for $a_* = 0.3\textrm{--}0.8$~~ (**"sub-2%" RETRACTED 2026-07-20** — that figure was computed against the corrupt $\omega_R$/$\omega_I$ tables + source-frame masses; see the 🔴 banner above).

Comparison against three LIGO detections, including both frequency and decay time.
**⚠ The table below is the SUPERSEDED frame-mixed artifact (2026-05-18)** — its
$f_\mathrm{AVE\text{-}v2}$ used source-frame $M_{final}$ against detector-frame $f_\mathrm{obs}$;
preserved verbatim as the record of the banked claim. Honest detector-frame / dimensionless
numbers are in the 🔴 supersession banner above ($-9.5\%$ mean, not $-2.0\%$/$-1.2\%$/$+1.9\%$):

| **Event** | $M_{final}$ | $a_*$ | $f_\mathrm{AVE\text{-}v2}$ | $f_\mathrm{obs}$ | $\Delta f$ (v2) | $f_\mathrm{AVE\text{-}v1}$ (superseded) | $\Delta f$ (v1) |
|---|---|---|---|---|---|---|---|
| GW150914 | 62.0 $M_\odot$ | 0.67 | **246.0 Hz** | 251 Hz | **-2.0%** | 278 Hz | +10.6% |
| GW170104 | 48.7 $M_\odot$ | 0.64 | **308.2 Hz** | 312 Hz | **-1.2%** | 345 Hz | +10.5% |
| GW151226 | 20.8 $M_\odot$ | 0.74 | **764.0 Hz** | 750 Hz | **+1.9%** | 884 Hz | +17.9% |

**🔴 SUPERSEDED banked claim (2026-05-18), preserved verbatim:** *"v2 refined formula
(2026-05-18): mean -0.45%, max 2.0% per event — within GR Kerr QNM precision band (mean +0.34%
per Berti+Cardoso+Will 2006 Leaver-method). v1 simplified formula (superseded) over-predicted by
~13% mean per event; failure mode was treating entire cavity as compliant. All from zero free
parameters."* — **RETRACTED 2026-07-20:** both the $-0.45\%$ and the "+0.34% GR reference" rested
on (1) a Kerr QNM table wrong at spin by up to $-27\%$ and (2) source-vs-detector frame mixing.
Honest v2-vs-Kerr: $-9.5\%$ mean (dimensionless, spin-only), growing with spin. The cold a*=0
eigenvalue ($18/49$, $-1.7\%$) is the only surviving zero-free-parameter result.

**🔴 SUPERSEDED banked claim (2026-05-18), preserved verbatim:** *"Phase 5 decay-time τ
refinement (2026-05-18, lattice-Q preservation): mean -0.47% across same 3 events — v2 outperforms
standard GR Kerr QNM (-6.94% mean). Mechanism: K4 lattice impedance sets damping-rate Q (rigid
Cosserat skeleton property), so Q is invariant across v1/v2 cavity-radius refinements. Cavity-radius
shift v1 → v2 propagates inversely into τ via $\tau_{v2} = \tau_{v1} \cdot (\omega_{R,v1} /
\omega_{R,v2})$, taking v2 τ to match LIGO obs at GR-class precision. Per-event: GW150914 τ_v2 = 3.95
ms (-1.2% vs LIGO 4.0 ms); GW170104 τ_v2 = 3.02 ms (+0.7% vs LIGO 3.0 ms); GW151226 τ_v2 = 1.39 ms
(-0.8% vs LIGO 1.4 ms). Full C1-BH-RING test closed: both ω_R AND τ now match LIGO at <1% mean
precision per event from zero free parameters."* — **RETRACTED 2026-07-20:** the τ chain rides the
same source-frame masses AND a separately-corrupt $\omega_I$ table (high by $+11\%$/$+26\%$ at
a*=0.90/0.95); the $-0.47\%$ "match" and the "outperforms GR ($-6.94\%$)" contrast do not survive
the frame + $\omega_I$-table correction. C1-BH-RING is NOT closed; a full frame-corrected τ re-run
is a flagged follow-on.

**🔴 SUPERSEDED banked claim (2026-05-18), preserved verbatim:** *"Phase 4 spin sweep validation
(2026-05-18): v2 reproduces GR Kerr QNM curve across the full observed LIGO BBH spin range. 9 of 11
swept spin values (a* ∈ {0.0, 0.1, ..., 0.95}) PASS at |dev| < 3% vs GR Berti reference. Divergence
onset a* ≥ 0.90 (near-extremal regime, currently unattested in LIGO catalog). Mass-independence
confirmed at 7× range: GW190521 (M = 142 M⊙, IMBH-class) matches at -0.25% per v2; GW170729 (a* =
0.81, higher than Phase-3 max) matches at +1.77%. v2 covers entire currently-detected LIGO BBH
catalog at GR-class precision. Near-extremal regime (a* > 0.90) deferrable to Option B (full
spheroidal cavity) when LIGO detects such an event."* — **RETRACTED 2026-07-20:** the entire spin
sweep was run against the corrupt Kerr table; against corrected Kerr, v2 sits $-8.6\%$ to $-20\%$
BELOW true Kerr across a*=0.6–0.95 (the "<3% PASS" and the near-extremal "positive excess" both
invert — cf. PR #772 findings 0/5). No PASS survives; v2 is a definite below-Kerr forward
prediction, not a catalog-covering GR-class match.

Live-fire validation: [`src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py`](../../../../../src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py) implements v1, v2, GR Berti reference, Phase-3 LIGO-event comparison, Phase-4 spin sweep + extended LIGO events. Phase 3 + 4 results in [`research/ligo-ringdown-driver-design.md`](../../../../../research/ligo-ringdown-driver-design.md) §8-9.

---
