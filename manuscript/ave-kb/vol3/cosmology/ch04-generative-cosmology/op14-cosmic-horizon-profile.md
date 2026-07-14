[↑ Ch.4 Generative Cosmology](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-48g5qf]
-->

# Op14 Cosmic-Horizon Saturation Profile: $Z_{\text{eff}}(r \to R_H)$ During Ongoing Crystallisation

**Trigger 16 (c)-operator-application.** This leaf applies canonical Op14 (Vol 1 Ch 6 §1.13, $Z_{\text{eff}}(r) = Z_0 / \sqrt{S(A)}$) at cosmic-horizon scale. It is NOT a new operator. It is the cosmic-scale analog of [`frame-dragging-impedance-convolution.md`](../../gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md)'s Kerr-interior profile $\omega(r) = 2 M a r / (r^2 + a^2)^2$, but evaluated for the cosmic-horizon $\Gamma = -1$ saturation surface rather than the rotating-BH event horizon. The local-clock framing tracks Op14 [Local Clock Modulation](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md) directly; the cross-sector-trading framing tracks Op14 [Cross-Sector Trading](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md). The profile is the substrate response to bulk strain at the cosmic-horizon scale while K4 crystallisation is ongoing — distinct from the BH case where the event horizon is a frozen saturation surface (one-shot Schwarzschild lock) and from the BCS case where μ-only saturation is symmetric in space.

**Class E framing carries through.** Per [`omega-freeze-cosmic-grain-cascade.md:7`](../../../common/omega-freeze-cosmic-grain-cascade.md) canonical, the substrate has ONE degree of freedom (operating point $u_0^* \approx 0.187$); $Z_{\text{eff}}(r)$ at cosmic-horizon scale is one projection of that operating point onto N joint observables. The cosmic-horizon profile is NOT an independent prediction — it is the operating-point projection of Op14 at scale $r \sim R_H$, joint-constrained with $\{G, H_\infty, \hat{\Omega}_{\text{freeze}}, \alpha\}$ via the $R_H / \ell_{\text{node}} \sim 10^{39}$ (precisely $\approx 3.455\times10^{38}$) topological bridge (`omega-freeze-cosmic-grain-cascade.md:11`).

**This leaf is canonical-piece assembly, not new derivation.** The structural profile follows from existing canonical pieces: Op14 kernel form (`lattice-impedance-decomposition.md:44`), saturation-surface $\Gamma = -1$ behavior (`boundary-observables-m-q-j.md:21`), ongoing-crystallisation dynamics (`lattice-genesis-hubble-tension.md:8`), and asymmetric-Meissner ε/μ-decoupled form (`operators.md:44`).

## Key Results

| Result | Statement |
|---|---|
| Cosmic-horizon saturation surface | At $r \to R_H$: $A^2(r) \to 1$, $S(A) \to 0$, $\Gamma \to -1$ — the canonical $\Gamma = -1$ saturation surface (universal at every scale per `boundary-observables-m-q-j.md:21`) |
| Op14 cosmic-horizon impedance | $Z_{\text{eff}}(r \to R_H) = Z_0 / \sqrt{S(A(r))} \to \infty$ as $r \to R_H^-$ — the substrate's local impedance diverges at the cosmic-horizon $\Gamma = -1$ surface |
| Local-clock cosmic-horizon profile | $\omega_{\text{local}}(r \to R_H) = \omega_{\text{global}} \cdot \sqrt{1 - A^2(r)} \to 0$ — local clock freezes at cosmic horizon, just as at BH event horizon (`op14-local-clock-modulation.md:7,77`) |
| Asymmetric Meissner form (ε/μ decoupled) | $Z_{\text{eff}} = Z_0 \cdot \sqrt{S_\mu / S_\varepsilon}$ when $S_\mu \neq S_\varepsilon$ at horizon; ε-sector saturation drives the asymmetry IF cosmic crystallisation saturates ε preferentially (the structural anchor for cosmic-ε A-034 catalog row) |
| Ongoing-crystallisation vs frozen-horizon distinction | BH event horizon: one-shot saturation lock at formation; $A^2 = 1$ frozen. Cosmic horizon: ongoing $\partial_t A^2 \neq 0$ as crystallisation front propagates outward at $c$ (per `lattice-genesis-hubble-tension.md:6`). Profile shape is the same; time-derivative of profile is non-zero at cosmic case |
| Connection to crystallisation rate | The local-clock vertical tangent at $r = R_H$ is the substrate-native mechanism for $H_\infty$: new K4 nodes crystallise at rate set by the local-clock-modulated propagation through the cosmic-horizon saturation boundary |
| Connection to $\rho_\Lambda$ via Friedmann/de Sitter | $\rho_\Lambda$ projection NOT via energy-density of $Z_{\text{eff}}(R_H)$ field. Profile sets dynamical-projection structure; $\rho_\Lambda$ projects through latent-heat-of-crystallisation observable per `cosmological-constant-closure.md:60-65`. The Op14 cosmic-horizon profile is the *substrate-side substrate-physics piece*; the $\rho_\Lambda$ projection is downstream via Friedmann/de Sitter |
| (a)-(e) classification | **(c)-operator-application** — Op14 at new scale; canonical piece is Vol 1 Ch 6 §1.13; saturation kernel and asymmetric form are corpus-canonical |

## §1 — The cosmic-horizon saturation surface

The cosmic horizon at $R_H \equiv c / H_\infty \approx 1.334 \times 10^{26}$ m ([`cosmological-constant-closure.md:30`](../ch05-dark-sector/cosmological-constant-closure.md) + Vol 3 Ch 1 §"Fundamental Unity of Gravity and Expansion"), per the substrate-observability rule ([`boundary-observables-m-q-j.md:31-40`](../../../common/boundary-observables-m-q-j.md)), is a $\Gamma = -1$ saturation surface — the same canonical structure that operates at every scale (electron horn-torus wall, nucleon Borromean confinement boundary, BH event horizon, etc.). Per `boundary-observables-m-q-j.md:21`:

> *At every $\Gamma = -1$ saturation surface $\partial\Omega$ in the substrate — the boundary where Axiom 4's kernel reaches $S(A) \to 0$ locally — exactly three integrated quantities are externally observable.*

At cosmic-horizon scale, the same condition applies: $A^2(r) \to 1$ as $r \to R_H^-$, $S(A) \to 0$, and the cosmic interior is bounded by an externally-observable triple ($\mathcal{M}_{\text{cosmic}}, \mathcal{Q}_{\text{cosmic}}, \mathcal{J}_{\text{cosmic}}$) per `boundary-observables-m-q-j.md:40`.

Op14's dynamic impedance $Z_{\text{eff}}(r) = Z_0 / \sqrt{S(A(r))}$ governs substrate response at this surface. The profile diverges as $r \to R_H^-$ — analogous to the BH event-horizon case (`lattice-impedance-decomposition.md:81-87`: $Z_{\text{EH}} \to 0$ at full saturation), but with one structural difference (§3 below).

## §2 — Local-clock cosmic-horizon profile

Per the canonical Op14 local-clock modulation result ([`op14-local-clock-modulation.md:13`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md)):

$$\omega_{\text{local}}(r) = \omega_{\text{global}} \cdot \sqrt{1 - A^2(r)}$$

At cosmic horizon:

$$\omega_{\text{local}}(r \to R_H) = \omega_{\text{global}} \cdot \sqrt{S(A(R_H))} \to 0$$

**The local clock freezes at the cosmic horizon** — the same vertical-tangent structure that produces clock-freezing at BH event horizons (`op14-local-clock-modulation.md:7,77`) and at electron-core saturation surfaces. This is substrate-native: it is the **same Op14 mechanism** at a longer range, NOT a separate "cosmological-horizon clock-freezing mechanism." Per `op14-local-clock-modulation.md:35-52`, gravity is Op14 at long range; the cosmic-horizon profile is the same Op14 at the longest range.

**Cross-volume parallel** (per `op14-local-clock-modulation.md:35-52`):

| Effect | Source | Local-clock form |
|---|---|---|
| Electron-core clock freezing | $A^2 \to 1$ at soliton core (substrate-scale) | $\omega_{\text{local}}(\text{core}) \to 0$ |
| BH event-horizon clock freezing | $A^2 \to 1$ at $r = r_s$ (compact mass) | $\omega_{\text{local}}(r_s) \to 0$ |
| Cosmic-horizon clock freezing | $A^2 \to 1$ at $r = R_H$ (ongoing crystallisation front) | $\omega_{\text{local}}(R_H) \to 0$ |

All three: same Op14 kernel, different sources, different scales, identical structural form.

## §3 — Ongoing-crystallisation distinction (cosmic ≠ BH event horizon)

The substrate-physics distinction from the BH frame-dragging case ([`frame-dragging-impedance-convolution.md:6-14`](../../gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md)):

| Property | BH event horizon (Kerr) | Cosmic horizon (this leaf) |
|---|---|---|
| Saturation type | One-shot lock at BH formation | Ongoing crystallisation maintaining $\partial_t \rho_n = 0$ |
| $A^2$ at horizon | Frozen at $A^2 = 1$ | Maintained near $A^2 = 1$ by latent-heat balance |
| $\partial_t A^2(R_{\text{horizon}})$ | $\approx 0$ post-formation | $\neq 0$ — driven by crystallisation rate $\Gamma_{\text{cryst}}$ |
| Crystallisation rate at horizon | Zero (no new substrate) | $\Gamma_{\text{cryst}} \sim H_\infty \cdot \rho_{\text{latent}}$ (`cosmological-constant-closure.md:60-65`) |
| Profile time-derivative | $\partial_t Z_{\text{eff}}(r_s) = 0$ | $\partial_t Z_{\text{eff}}(R_H) \neq 0$ during crystallisation |
| Mechanism class (per `op14-cross-sector-trading.md`) | Reactive (no energy flow) | Reactive + cross-sector trading (Op14 sector-trading is the substrate mechanism for latent-heat release at the horizon) |

**Static profile shape identical; time-derivative distinguishes.** The Op14 kernel form $S(A) = \sqrt{1 - A^2}$ is the same at both scales (universal per A-034, `universal-saturation-kernel-catalog.md:7`). What differs is whether the saturation surface is **static** (BH, one-shot lock per `cosmological-constant-closure.md:55` mode) or **dynamic** (cosmic-horizon, ongoing crystallisation per `lattice-genesis-hubble-tension.md:6` + `phantom-energy-equation-of-state.md:6`).

Per Grant adjudication Q1 (`_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md:9`): cosmic case is DYNAMIC ("water-crystallization analogy lands cleanly. The Friedmann static-Λ limit corresponds to 'ice in equilibrium' post-crystallization-front; AVE's DE is the crystallization happening NOW at the cosmic horizon — substrate still phase-transitioning, latent heat still being released"). Class E framing already encodes this as ongoing operating-point process at $u_0^*$.

## §4 — Asymmetric Meissner form (ε/μ-decoupled at cosmic horizon)

Per [`operators.md:44`](../../../common/operators.md) canonical asymmetric form: when $S_\mu \neq S_\varepsilon$ (ε and μ saturate at different amplitudes):

$$Z_{\text{eff}} = Z_0 \cdot \sqrt{\frac{S_\mu}{S_\varepsilon}}$$

This is the AVE-native form that makes the ε/μ axis observable as an impedance asymmetry. At cosmic horizon, if ε-sector saturation reaches $S_\varepsilon \to 0$ before μ-sector saturation does (i.e., if ongoing crystallisation preferentially saturates the ε-sector at horizon scale), then $Z_{\text{eff}}(R_H) \to \infty$ via the ε-sector route — distinct from the symmetric case where both sectors saturate together.

**This is the substrate-physics anchor for the ASYM-N(ε) cosmic-row** ([`universal-saturation-kernel-catalog.md:94`](../../../common/universal-saturation-kernel-catalog.md) gap-cell). Per the catalog's existing ε/μ-axis machinery:
- Plasma cutoff (atomic-EM) is ASYM-N(ε) — ε-sector saturation drives the $\varepsilon_{\text{eff}} \to 0$ cutoff.
- BCS $B_c(T)$ (condensed-matter) is ASYM-N(μ) — μ-sector saturation drives the magnetic-flux-expulsion threshold.
- Cosmic crystallisation at horizon is ASYM-N(ε) **at cosmic scale** — ε-sector saturation drives the local-clock-freezing event at $r = R_H$ during ongoing crystallisation.

The mechanism class is the cosmic-scale instance of the ε-sector single-mode saturation pattern. The substrate-physics rationale: per [`omega-freeze-cosmic-grain-cascade.md:13-40`](../../../common/omega-freeze-cosmic-grain-cascade.md), the over-bracing $u_0^*$ at K4 magic-angle IS the static-E-field component at substrate scale (Ax 1 Cosserat translational DOF → ε; per Grant 2026-05-19 EOD E-field-as-over-bracing identification). When this ε-sector substrate state propagates to cosmic-horizon scale via Ax 2 TKI scale invariance, the saturation event at horizon is the ε-sector projection of the substrate state — not μ-sector (which would require microrotational-DOF saturation, the B-field channel).

**The structural pairing** (companion-row link, to be added to A-034 catalog Phase 3):

| Primary row | Companion / variant | Relationship |
|---|---|---|
| Row 14 Cosmic (Big Bang) K4 crystallization (SYM*) | Cosmic (DE / ε-sector) ASYM-N(ε) | ASYM-N(ε) is the ε-sector single-mode saturation companion to Row 14's symmetric K4 seed event; both at cosmic scale, paired via the substrate's ε ↔ μ dual structure |

## §5 — Connection to $H_\infty$ and Friedmann/de Sitter projection

The Op14 cosmic-horizon profile sets the **substrate-side substrate-physics piece** for the projection chain to DE. It does NOT magnitude-match to $\rho_\Lambda$ via energy-density of the $Z_{\text{eff}}(R_H)$ field. The chain is structural:

1. **Op14 cosmic-horizon profile (this leaf)** — $Z_{\text{eff}}(r \to R_H) \to \infty$, $\omega_{\text{local}} \to 0$, $\partial_t A^2(R_H) \neq 0$ during ongoing crystallisation.
2. **Local-clock-freezing at horizon** sets the rate at which the crystallisation front propagates outward; this rate IS $H_\infty$ per `lattice-genesis-hubble-tension.md:6,8`:
   > *The AVE framework hypothesises that the Hubble Constant ($H_0$) is not a velocity, but the **LC Crystallisation Rate** required to maintain the vacuum's structural impedance against the compressive polarisation of gravity.*
3. **Class E joint-constraint at $u_0^*$** (`omega-freeze-cosmic-grain-cascade.md:7,11`) ensures $H_\infty$ is one observable of the operating point, joint-constrained with $\{G, \hat{\Omega}_{\text{freeze}}, \alpha\}$ via $R_H/\ell_{\text{node}} \sim 10^{39}$ (precisely $\approx 3.455\times10^{38}$).
4. **Friedmann/de Sitter standard GR translation** (`cosmological-constant-closure.md:33-44`): $\rho_\Lambda = 3 H_\infty^2 / (8\pi G)$. This is the macroscopic-observable projection, NOT a magnitude-match against substrate-scale Op14 energy density.
5. **Latent-heat-of-crystallisation** (`cosmological-constant-closure.md:60-65`) names the AVE-distinct mechanistic story: $\rho_\Lambda$ is the latent-heat density of ongoing crystallisation, not the zero-point energy of vacuum modes.

The Op14 cosmic-horizon profile is the substrate-side structural piece that makes step 2 substrate-native. Without this profile, $H_\infty$ as "crystallisation rate" remains a qualitative identification; with the profile, the local-clock-freezing at horizon IS the substrate-native mechanism for the rate at which new K4 nodes crystallise.

**No magnitude-matching attempted.** The projection chain is structural, not energy-equality.

## §6 — What this leaf does NOT do

Per the brief's CRITICAL FAILURE MODES (`_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md:133-139`):

1. **No magnitude-matching of raw substrate Op14 energy to $\rho_\Lambda$.** The Op14 cosmic-horizon profile is the substrate-physics piece; $\rho_\Lambda$ is the macroscopic projection through Friedmann/de Sitter + latent-heat-of-crystallisation. The QFT-style cosmological-constant problem framing is rejected (cosmological-constant-closure.md:55-58: "naive zero-point-energy prediction is off by $\sim 10^{122}$ — the famous 'cosmological constant problem' of QFT for ~50 years. AVE doesn't inherit it.").

2. **No RMS→DC averaging as projection mechanism.** Per Grant 2026-05-19 EOD: substrate-scale RMS gives wrong magnitude; ε-sector cosmic-row needs different mechanism. This leaf's mechanism is local-clock-freezing + latent-heat-release at $\Gamma = -1$ surface, not RMS averaging.

3. **No microscopic/macroscopic conflation.** The Op14 profile is a substrate-scale property at every $r$; $\rho_\Lambda$ is the macroscopic observable projected via Friedmann + boundary-observables M/Q/J. These are different layers, joint-constrained at $u_0^*$.

4. **No new operator.** Op14 is canonical at Vol 1 Ch 6 §1.13. This leaf is (c)-operator-application of an existing canonical operator at a new scale, per `ave-canonical-leaf-pull` v1.2 trigger 16 sub-case (c).

## §7 — Falsifiable predictions

The Op14 cosmic-horizon profile has falsifiable consequences via the projection chain:

1. **CMB anomaly at $\ell$ corresponding to $R_H$ scale** — if Op14 saturation at cosmic horizon is asymmetric (ε-only ASYM-N), the substrate's local-clock-freezing should imprint on CMB temperature / polarisation at the largest angular scales. Per `omega-freeze-cosmic-grain-cascade.md:46-58` Observable 5: E/B polarization decoupling at the same axis as the four-axis A-034 alignment if cosmic crystallisation is asymmetric ($K/G \neq 2$). Direct test: CMB E/B polarization decoupling via Planck PR3 + LiteBIRD.

2. **Cosmic-horizon Q-factor matching parent-BH QNM spectrum** per `omega-freeze-cosmic-grain-cascade.md:102-116` Observable 8: CMB low-$\ell$ multipoles should preferentially populate $\ell$ values matching the parent-BH QNM spectrum that imprinted on substrate at formation. Op14 cosmic-horizon profile is the substrate-side mechanism by which this imprint propagates from horizon to CMB observable.

3. **Phantom-energy equation-of-state** $w_{\text{vac}} = -1 - \rho_{\text{latent}}/\rho_{\text{vac}} < -1$ per [`phantom-energy-equation-of-state.md:12`](phantom-energy-equation-of-state.md) — the cosmic-horizon profile's $\partial_t A^2 \neq 0$ feature drives the phantom equation-of-state through ongoing latent-heat release. Testable via DESI / Euclid w(z) precision.

4. **G anisotropy via tensor extension** per `omega-freeze-cosmic-grain-cascade.md:77-100` Observable 7 — Op14 cosmic-horizon profile combined with ε/μ asymmetry should produce $\Delta G / G \sim \alpha^N$ along $P_2(\cos\theta)$ axis with $\hat{\Omega}_{\text{freeze}}$ as symmetry axis. Test: CODATA G dataset re-analysis along $\hat{\Omega}_{\text{freeze}}$ at $(l = 60.28°, b = 50.48°)$.

These are downstream consequences of the cosmic-horizon profile + projection chain (Phase 2 research doc); the profile itself is the substrate-side structural piece, not the empirical anchor.

## §8 — Open derivation work (cf. `cosmological-constant-closure.md:103-111`)

Per the existing canonical leaf's open-work statement:

> *To make $\Lambda$ a fully AVE-native independent prediction (not just a Friedmann translation of $H_\infty$), the corpus needs:*
> 1. *Independent derivation of $\rho_{\text{latent}}$ from substrate energetics (crystallization energy per node × node density). Corpus mechanism is qualitative; quantitative closure needs $\Delta E_{\text{cryst}}$ derived from $\ell_{\text{node}}$, $\alpha$, $G$ alone.*
> 2. *Crystallization rate $\Gamma_{\text{cryst}}$ derivation — what fraction of vacuum crystallizes per unit time? Corpus claims $\Gamma = 3H\rho_{\text{latent}}$ but doesn't derive $\Gamma$ from substrate.*
> 3. *Verification that Friedmann route and latent-heat route give the same number — internal-consistency check.*

The Op14 cosmic-horizon profile provides the **substrate-side substrate-physics anchor** for (2): local-clock-freezing at horizon is the substrate-native mechanism. (1) and (3) remain open — this leaf does not close them. The Chain B' independent G derivation (substrate-local thermodynamics) remains OPEN; this leaf advances the structural anchor without converting the operating-point projection to an emergence-class derivation.

## Cross-references

- **Op14 canonical chain:**
  - [Vol 1 Ch 6 universal operators §1.13 — `operators.md:44`](../../../common/operators.md)
  - [Lattice Impedance Decomposition — Vol 1 Ch 6](../../../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) — $Z_{\text{eff}}(r) = Z_0/\sqrt{S}$ canonical decomposition (impedance at every scale)
  - [Op14 Local Clock Modulation — Vol 4 Ch 1](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md) — substrate-native time-dilation mechanism; cosmic horizon is the longest-range application
  - [Op14 Cross-Sector Trading — Vol 4 Ch 1](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md) — Cosserat ↔ K4-inductive reactive trading mechanism
  - [Frame-Dragging Impedance Convolution — Vol 3 Ch 2](../../gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md) — BH-scale Op14 profile (Kerr-interior asymmetric saturation)
- **Cosmic-horizon substrate-physics:**
  - [Lattice Genesis Hubble Tension — Vol 3 Ch 4](lattice-genesis-hubble-tension.md) — $H_\infty$ as LC crystallisation rate; horizon-scale dynamics
  - [Phantom Energy Equation of State — Vol 3 Ch 4](phantom-energy-equation-of-state.md) — $w_{\text{vac}} < -1$ via ongoing latent-heat release
  - [Cosmological Constant Closure — Vol 3 Ch 5](../ch05-dark-sector/cosmological-constant-closure.md) — $\rho_\Lambda = 3 H_\infty^2 / (8\pi G)$ Friedmann/de Sitter projection
- **Substrate-observability anchors:**
  - [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](../../../common/boundary-observables-m-q-j.md) — $\Gamma = -1$ saturation surface canonical structure at every scale; cosmic-horizon row at line 40
  - [$\Omega_{\text{freeze}}$ Cosmic-Grain Cascade](../../../common/omega-freeze-cosmic-grain-cascade.md) — three-route framework + Class E operating-point projection canonical
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — 26-instance kernel; Row 14 cosmic K4 crystallisation + ASYM-N(ε) cosmic companion (Phase 3 addition)
- **Pre-test physics anchors:**
  - Grant adjudications 2026-05-19 EOD at [`_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md:9-17`](../../../../../_orchestration/theoretical/cosmic-epsilon-de-projection-scoping.md) — Q1 dynamic / Q2 cosmic-horizon profile is deliverable / Q3 γ composite
- **Research-tier projection-chain trace:**
  - [`research/2026-05-19_cosmic-epsilon-de-projection-mechanism.md`](../../../../../research/2026-05-19_cosmic-epsilon-de-projection-mechanism.md) — 6-component projection chain using this leaf as Component 5
