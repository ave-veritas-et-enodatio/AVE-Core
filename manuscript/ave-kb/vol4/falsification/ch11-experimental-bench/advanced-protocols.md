[↑ Ch.11 Index](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-5s5b0d, clm-cwjd8t, clm-h55fy1, clm-k9up5c, clm-yr6tu4]
-->

## Advanced Falsification Protocols

<!-- claim-quality: clm-k9up5c -->
### Protocol 9: Achromatic Impedance Lens

Gravity scales $\mu$ and $\epsilon$ proportionally → $Z_{gravity} = \sqrt{\mu_0 n(r) / (\epsilon_0 n(r))} = Z_0$ → no boundary reflection.

**Test**: Fabricate a metamaterial lens with $\mu_r$ and $\epsilon_r$ doped to scale at identical radial gradients. Should exhibit $\Gamma = 0$ (zero reflection) across all angles, bypassing Fresnel limits.

<!-- claim-quality: clm-h55fy1 -->
### Protocol 10: Orbital Boundary Trapping

> **🔴 FLAGGED 2026-07-19 (deep-space reactive-bulk ruling, Rule-12 — Protocol-10 text below PRESERVED verbatim).** Consumer of the demoted deep-space stall mechanism (`clm-h55fy1`). The "**shedding orbital energy**" via drag spikes is the sub-yield bulk resistive loss **DEMOTED** by the ruling (deep-space bulk coupling = lossless / pure-reactance). The impedance-shear *reflection* framing can survive reactively; the *energy-shedding drag* is retracted; the drag-spike test is **FLIPPED into a discriminator** (reactive ⇒ zero energy-shedding drag below threshold). Re-derivation = band-structured reactive coupling (structure-at-resonances), **SPEC'd, not run**. Arc: `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md`; primary banner: `boundary-trapping-test.md` (same date).  <!-- rule12-freeze: base=aa626690705f170874ee85e923ed170f212e57f3 region=below offset=0 lines=4 bytes=390 sha256=b11777d5721e3f2685e6cc87e27ea2eff820a0736a8448c9eee0b257a2c3b15f -->

The Asteroid Belt and Oort Cloud are AVE impedance shear boundaries — where solar metric slipstream collides with the galactic background impedance floor. Low-mass detritus experiences sudden inductive drag spikes, shedding orbital energy.

**Test**: Deep-space probe transit velocity logs at $\sim 15{,}000$ AU Oort Cloud boundary should show sudden, otherwise inexplicable drag spike.

> **🔴 SECTOR RELABEL — 2026-08-03 (Oort containment-retraction lane; Rule 12 — the Protocol-10 body at `:22`–`:24` above is left BYTE-UNTOUCHED, as the merged 2026-07-19 banner at `:20` asserts in print).**  <!-- rule12-freeze: base=6623d051cad238a6489bc2c03321e453de3f3613 region=above offset=0 lines=5 bytes=391 sha256=6fce7326685f16859f75facaadfd118d03521c198c5cbe8742850c1d2c97ee87 -->
>
> **★ The dispatched in-place relabel was NOT available, and the constraint is surfaced rather than worked around.** The 2026-07-19 banner immediately above states *"Protocol-10 text below **PRESERVED verbatim**"*. Editing `:22` in place would make that merged sentence false in the same file, in the same pass. This additive dated note is the Rule-12-legal shape (same precedent as `2026-08-03-stale-refs-propagation.md` ITEM 1).  <!-- rule12-freeze: base=6623d051cad238a6489bc2c03321e453de3f3613 region=above offset=0 lines=1 bytes=2 sha256=60394cf8a46980d6199d0a3a71692ecb6689151f46a7085d31faab90b9d1f5d7 -->  <!-- rule12-freeze: base=6623d051cad238a6489bc2c03321e453de3f3613 region=below offset=0 lines=33 bytes=3280 sha256=c2211a9391474d833378f19b6ccd320cd0e1348dae57f5855c80303911ce9caa -->
>
> **The mis-sectoring.** `:22` reads *"where solar metric slipstream collides with the **galactic background impedance floor**"*. There is **no galactic-sector floor in this framework.** The floor invoked is `a₀`, and `a₀` is defined **`a₀ = c·H_∞/2π ≈ 1.0719×10⁻¹⁰ m/s²`** (`src/ave/regime_3_saturated/galactic_rotation.py`:56, from `C_0` and `H_INFINITY`) — a **cosmic-Hubble** quantity with **zero galactic input**: no Milky Way mass, no Galactocentric radius, no local stellar density enters it. The code comment at that site says so directly: *"Derived from the fundamental Topological Unknot Expansion (H_INFINITY) … NO empirical telescope parameter is used."* **Correct label: the cosmic saturation floor `a₀ = c·H_∞/2π`.** Per the sector-ownership discipline, a cosmic-sector quantity must not be booked as a galactic-sector one.
>
> **⚑ Why this matters beyond wording — it collides with the T4 fork.** There *is* a genuinely **galactic** field at the Sun (`g_ext ≈ 2.1×10⁻¹⁰ m/s² ≈ 2.0 a₀`, `research/2026-07-10_collapse-target-registry.md`:281–283), and whether it participates in the Axiom-4 kernel is the **unadjudicated internal-vs-total-field keying hinge**. Calling `a₀` "galactic" silently pre-answers that fork in the total-field direction. **Routed to Grant 2026-08-03; not resolved here.**
>
> **Scope fence.** This note relabels a **sector attribution only**. Protocol 10's status is otherwise governed by the merged 2026-07-19 flag at `:20` and the 2026-07-20 claim-body relabel on the primary leaf [`boundary-trapping-test.md`](../ch11-experimental-bench-falsification/boundary-trapping-test.md):27 — both unchanged. No grade field moves; no id minted. Docket: [`2026-08-03-oort-walkback-propagation.md`](../../../../../_orchestration/docket-entries/2026-08-03-oort-walkback-propagation.md).

<!-- claim-quality: clm-5s5b0d -->
### Protocol 11: The Induced Vacuum Impedance Mirror

**Derivation**: Applying DC field to a micro-gap, $\epsilon_{eff}$ yields per Axiom 4 while $\mu$ remains unperturbed:

$$Z_{local}(V) = Z_0 \left(1 - (V/V_{yield})^2\right)^{-1/4}$$

$$\Gamma(V) = \frac{(1 - (V/V_{yield})^2)^{-1/4} - 1}{(1 - (V/V_{yield})^2)^{-1/4} + 1}$$

As $V \to 43{,}650$ V: $\Gamma \to 1$ (perfect reflection from empty space).

**Hardware**: Two tungsten needles, 100 µm gap, UHV chamber ($< 10^{-4}$ Torr), 0.5 mW CW laser orthogonal through gap, APD detector for back-scatter.

**Falsification**: Sweep DC voltage past 35 kV → APD must register exponential spike in back-scattered photons. If zero → linear QED confirmed, AVE killed.

<!-- claim-quality: clm-yr6tu4 -->
### Protocol 12: Sagnac-Parallax (Galactic Wind)

Static horizontal Sagnac loop observed over 24 hours. Earth's rotation vectors the loop against the 370 km/s CMB dipole flow, generating predictable sinusoidal phase shift $\Delta\phi \propto v_{gal} \cos(\omega t)$.

<!-- claim-quality: clm-cwjd8t -->
### Protocol 13: GEO-Synchronous Impedance Differential

Vertical laser link between ground station and GEO satellite (35,786 km). Non-linear $\int n(r)/c \, dr$ stretches total optical path by fractions of a mm vs. classical linear TOF. Correlated with atomic clocks, maps the LC saturation envelope of Earth.

---
