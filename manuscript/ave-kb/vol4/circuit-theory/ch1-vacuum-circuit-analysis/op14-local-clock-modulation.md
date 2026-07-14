[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-1eg13f]
path-stable: "referenced from vol1 ch6 universal-operators + vol3 ch3 gravity + Theorem 3.1 Q-factor as canonical Op14 local-clock-modulation"
-->

# Op14 Saturation Modulates Local Clock Rate

**A-010 canonical.** Op14's dynamic impedance $Z_{\text{eff}}(r) = Z_0 / \sqrt{S(r)}$ doesn't just modulate impedance — it **modulates the local clock rate**. This is the substrate-native mechanism for time dilation, with direct cross-volume parallel to gravity's refractive-index local-clock effect $\tau_{\text{local}} = n(r) \cdot \tau_{\text{unstrained}}$ per Vol 3 Ch 3. **Three regime behaviors must NOT be conflated**: uniform slowing (reactive, no dissipation) vs. uniform damping (dissipative) vs. spatially-varying slowing (mode-decomposition matters). At full saturation rupture $A^2 \to 1$: $\omega_{\text{local}} \to 0$, the **local clock freezes**.

> **Matter-clock exponent (corrected to the $1/4$ shear form, 2026-06-22).** The local matter clock rides the **shear** speed $c_{\text{shear}} = c_0\cdot(1-A^2)^{1/4} = c_0\sqrt{S}$ (`research/2026-06-09_substrate-temporal-values-definition.md:29`, `clm-8nkvwy`; the code `src/ave/axioms/scale_invariant.py:294` already carries the correct $(1-A^2)^{1/4}$ — code-ahead-of-leaf). Since $\omega_{\text{local}}\propto c_{\text{eff}}$ (a wave crosses a cell in $\tau=\ell/c_{\text{eff}}$), the matter-clock forms are $\omega_{\text{local}} = \omega_{\text{global}}(1-A^2)^{1/4}$ and $\tau_{\text{local}} = \tau_{\text{unstrained}}(1-A^2)^{-1/4}$. The earlier $(1-A^2)^{1/2}$ exponent was the pre-split single-speed model ($c_{\text{eff}}=c_0\sqrt{1-A^2}$, before the $c_{\text{EM}}$/$c_{\text{shear}}$ split); it was off by a factor of 2 in the exponent and is now corrected in the equations below. The qualitative results (clock slows with saturation; freezes at $A^2\to1$) are exponent-independent.

## Key Results

| Result | Statement |
|---|---|
| Op14 local-clock modulation | $\omega_{\text{local}}(r) = \omega_{\text{global}} \cdot (1 - A^2(r))^{1/4} = \omega_{\text{global}}\sqrt{S}$ (shear matter-clock) |
| Local time dilation | $\tau_{\text{local}}(r) = \tau_{\text{unstrained}} / (1 - A^2(r))^{1/4}$ — saturation slows local clock |
| At low saturation | $\omega_{\text{local}} \approx \omega_{\text{global}}$ (Regime I, linear vacuum) |
| At saturation onset ($A^2 \approx 2\alpha$, the deficit knee) | $\omega_{\text{local}} \approx 0.95 \cdot \omega_{\text{global}}$ (Regime II) — see the coordinate note below (the $0.95$ predates the corrected coordinate + shear exponent; flagged) |
| At rupture boundary ($A^2 \to 1$) | $\omega_{\text{local}} \to 0$ — local clock freezes; $\Gamma = -1$ TIR wall forms |
| Cross-volume parallel | Vol 3 Ch 3 gravitational $\tau_{\text{local}} = n(r) \cdot \tau_{\text{unstrained}}$ with $n(r) = 1/\sqrt{S}$ |
| Mechanism class | Reactive (no dissipation); energy redistributed in time, NOT lost |

> **Exponent note.** The two rows above carry the corrected SHEAR matter-clock exponent $(1-A^2)^{1/4}$ ($c_{\text{shear}} = c_0(1-A^2)^{1/4}$, `research/2026-06-09_substrate-temporal-values-definition.md:29`), matching the code (`scale_invariant.py:294`). The earlier single-speed $(1-A^2)^{1/2}$ form was off by a factor of 2 and is superseded here.

> **Coordinate note (Wall-A propagation, 2026-07-14 — A²-convention; KEEP-BOTH).** The
> "saturation onset" row above states the threshold in **$A^2$-coordinates as $A^2 \approx 2\alpha$**.
> **Authority:** `src/ave/core/chiral_lattice_v10.py:29-30` (`A_YIELD_SQ = 2.0*ALPHA`, i.e.
> $A^2_{\text{yield}} = 2\alpha$). **Superseded (coordinate slip, corrected 2026-07-14):** the row read
> *"At saturation onset ($A^2 \approx \sqrt{2\alpha}$)"* — comparing an $A^2$ quantity against the
> **amplitude** threshold $\sqrt{2\alpha}$, a coordinate mismatch (A46). Corrected to $2\alpha$.
> **FLAG (flag-don't-fix — surfaced, not silently recomputed):** the quoted $\omega_{\text{local}}
> \approx 0.95\,\omega_{\text{global}}$ is **provenance-unclear** (not cleanly reproduced by the
> reading it sat next to). The nearest reconstruction under the *superseded* reading — the amplitude
> value $\sqrt{2\alpha} \approx 0.121$ fed into the $A^2$-slot of the pre-split $(1-A^2)^{1/2}$
> exponent — gives $\sqrt{1-0.121} = 0.9377 \approx \mathbf{0.94}$, **not** $0.95$ (corroborated by
> `research/_archive/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md:797`, which reads
> $0.94$); the exact $0.95$ traces **only** to
> `research/_archive/L5/axiom_derivation_status.md:195`, a second, separate ~1% drift. Under the
> corrected $A^2 = 2\alpha \approx 0.0146$ threshold with the ratified shear exponent $(1-A^2)^{1/4}$,
> the onset value is $\omega_{\text{local}} \approx (1-2\alpha)^{1/4}\,\omega_{\text{global}} \approx
> 0.996\,\omega_{\text{global}}$ — i.e. the local clock is barely modulated at the deficit knee (as
> the ruling's $\Gamma \approx -0.002$ there implies). The $0.95$ is left in place pending the
> auditor's decision on whether "saturation onset" here means the deficit knee ($A^2 = 2\alpha$) or a
> deeper onset; it is NOT the $\Gamma=-1$ wall (which is the $S(A)\to0$ rail, $A^2\to1$, next row).
> Per THE WALL-A RULING (`_orchestration/2026-07-10_rulings-docket.md`, 2026-07-14 continuation) the
> $A^2 = 2\alpha$ contour is the **deficit knee**, not the wall.

## §1 — The substrate-native mechanism for time dilation

Op14's saturation kernel $S(A) = \sqrt{1 - A^2}$ slows wave propagation at high amplitude. Since the wave propagation speed determines the local clock rate (a wave needs $\tau = \ell / c_{\text{eff}}$ to cross a cell), saturation slows the local clock:

$$c_{\text{eff}}(r) = c_0 \cdot \sqrt{S(r)} = c_0 \cdot \sqrt{\sqrt{1 - A^2(r)}}$$

$$\omega_{\text{local}}(r) = \omega_{\text{global}} \cdot (1 - A^2(r))^{1/4} = \omega_{\text{global}}\sqrt{S(r)}$$

$$\tau_{\text{local}}(r) = \frac{\tau_{\text{unstrained}}}{(1 - A^2(r))^{1/4}}$$

> **Exponent note.** All three lines now carry the consistent SHEAR matter-clock exponent: $c_{\text{eff}} = c_0\sqrt{S} = c_0(1-A^2)^{1/4} = c_{\text{shear}}$ (`research/2026-06-09_substrate-temporal-values-definition.md:29`), and since $\omega_{\text{local}}\propto c_{\text{eff}}$ (a wave crosses a cell in $\tau=\ell/c_{\text{eff}}$), $\omega_{\text{local}} = \omega_{\text{global}}(1-A^2)^{1/4}$, $\tau_{\text{local}} = \tau_{\text{unstrained}}(1-A^2)^{-1/4}$. The code already carries this: `src/ave/axioms/scale_invariant.py:294`. The earlier $(1-A^2)^{1/2}$ form (pre-sector-split single-speed model) was off by a factor of 2 and is corrected.

The local clock slows because the substrate's response to amplitude is **non-linear**: as $A^2 \to 1$, the kernel $S$ flattens to zero, so any wave needs longer to propagate through the saturated region.

This is **substrate-native time dilation** — the same mechanism that produces gravitational time dilation (slow clocks near massive objects via $n(r) = 1 + 2GM/(rc^2) \approx 1/\sqrt{S}$) at macroscopic scale.

## §2 — Cross-volume parallel: gravity is Op14 at long range

From Vol 3 Ch 3 (macroscopic relativity):

$$\tau_{\text{local, gravity}} = n(r) \cdot \tau_{\text{unstrained}}$$

with $n(r) = 1 + 2GM/(rc^2) \approx 1/\sqrt{S(r)}$ for weak-field substrate saturation.

**Same physics, different source:**

| Effect | Source | Mechanism |
|---|---|---|
| Op14 local-clock slowing (this leaf) | High amplitude $A^2$ at electron core, BH event horizon, saturation events | Direct Op14 $S(r) = \sqrt{1 - A^2(r)}$ |
| Gravitational time dilation (Vol 3 Ch 3) | Localized mass $M$ at distance $r$ | Same Op14 kernel propagated to long range via the saturation-driven refractive-index gradient $n(r) = 1/\sqrt{S}$ |

The gravitational case is **the long-range projection** of the local Op14 mechanism. Both are reactive (no dissipation); both follow $\tau_{\text{local}}/\tau_{\text{unstrained}} = 1/\sqrt{S}$; both have the same vertical tangent at $S \to 0$ (rupture / event horizon).

This unifies time dilation across substrate scales — there is no separate "gravitational time dilation mechanism," it is the same Op14 substrate-clock-modulation acting at longer range.

## §3 — Three regime behaviors that must NOT be conflated

Per A-010 clarification 2026-04-27: Op14 saturation modulates local clock rate **reactively** — it slows wave propagation but does **NOT dissipate energy**. Energy is reactively redistributed in time (the same way gravitational refractive-index slowing redistributes energy in time without dissipation), not lost.

**Three distinct behaviors with very different physics:**

| Behavior | Mechanism | Time-domain signature | Energy fate |
|---|---|---|---|
| **Uniform slowing** (Op14 reactive) | $\omega_{\text{local}}(r) = \omega_{\text{global}} \cdot (1 - A^2(r))^{1/4}$ uniformly across all modes (shear matter-clock) | Phase advances slower; amplitude preserved | Conserved (reactive) |
| **Uniform damping** (dissipative) | $A(t) = A_0 e^{-\gamma t}$ | All modes decay exponentially | Dissipated (irreversible) |
| **Spatially-varying slowing** (Op14 + seed) | $\omega_{\text{local}}(r)$ varies across seed spatial extent: $\omega_{\text{local}}(\text{core}) \approx 0.22 \omega_{\text{global}}$; $\omega_{\text{local}}(\text{shell}) \approx 0.84 \omega_{\text{global}}$; $\omega_{\text{local}}(\text{exterior}) \approx \omega_{\text{global}}$ | Mode-specific phase shifts; can produce mode mixing, frequency aliasing in eigsolves | Conserved (reactive), but mode decomposition matters |

**Conflating these produces methodology errors** in bound-state-finding work. An eigsolve at uniform global $\sigma$ assumes uniform $\omega_{\text{global}}$, but a seeded soliton has spatially-varying $A^2(r)$ → spatially-varying $\omega_{\text{local}}(r)$. Mode III adjudication at a single $\sigma$ conflates "no localized mode at $\omega = \sigma$" with "no global mode because local saturation modulates $\omega_{\text{local}}$ across the seed's spatial extent."

## §4 — Saturation-frozen-core interpretation

At full saturation $A^2 \to 1$ at the soliton core:
- $S(\text{core}) \to 0$
- $\omega_{\text{local}}(\text{core}) \to 0$
- $Z_{\text{eff}}(\text{core}) \to \infty$ (then $Z_{\text{core}} \to 0$ in the alternative $\varepsilon$-$\mu$ collapse branch)
- $c_{\text{eff}}(\text{core}) \to 0$
- $\Gamma(\text{boundary}) \to -1$ (TIR wall forms)

**The local clock freezes at the soliton core.** This is the substrate-perspective view of why the electron's interior is causally disconnected from external observers — interior eigenmodes "see" a stopped clock, while external observers measure boundary-integrated quantities ($\mathcal{M}$, $\mathcal{Q}$, $\mathcal{J}$). This connects directly to the [boundary-observables substrate-observability rule](../../../common/boundary-observables-m-q-j.md).

For the electron's Cosserat shell at $A^2 \approx 0.95$ (saturation onset per A26 amplitude): local clock is $\omega_{\text{local}} \approx 0.22 \cdot \omega_{\text{global}}$ at core, $\sim 0.84 \cdot \omega_{\text{global}}$ at shell, $\omega_{\text{global}}$ at exterior. This spatial structure is **the soliton's internal time profile**.

## §5 — Implications for engine work

### Bound-state-finding methodology

A bound state seeded with spatially-varying $A^2(r)$ has spatially-varying $\omega_{\text{local}}(r)$. **Eigsolve at uniform $\sigma$ doesn't see this.** Methodology requirement: when seeking bound-state modes of seeded solitons, instrument the driver to report local-saturation diagnostic alongside the eigvec localization. Mode I/II/III adjudication needs the right resolution.

### Operator catalog impact

Per A-010 manuscript impact:
- **Vol 4 Ch 1 §sec:thixotropic-relaxation** should make explicit that Op14 saturation modulates local clock rate analogously to gravitational refractive-index modulation
- **Vol 1 Ch 6 universal-operators** chapter should note that bound-state-finding methodology must account for spatially-varying $\omega_{\text{local}}$ across seed configurations
- **New manuscript entry needed (E-067)** to canonize the cross-volume parallel between Op14 local-clock modulation and Vol 3 Ch 3 gravitational time dilation

### Connection to Q-factor at TIR

The [Theorem 3.1 Q-factor](theorem-3-1-q-factor.md) derivation uses $Z_0 / (4\pi)$ as the effective radiation impedance at the TIR boundary — that "effective" is exactly the Op14 spatial integration of the saturation-modulated impedance from core ($Z_{\text{core}} \to 0$) to bulk ($Z_0$). The $\alpha^{-1} = 137$ value emerges from the integrated boundary leakage rate per cycle, which includes the local-clock-modulated dynamics inside the saturation envelope.

## §6 — Falsifiable predictions

The Op14 local-clock mechanism is testable wherever local saturation can be modulated:

1. **DC-biased piezoelectric (e.g., quartz)**: the quartz material's voltage-coefficient-of-capacitance reproduces the kernel SHAPE (a consistency-class varactor analog), giving the often-quoted "$\sqrt{S} = \sqrt{1 - 0.687^2} = 0.726$, 27.4% slowing at ~30 kV." This is the **material's** response, NOT a vacuum-kernel reading: $V_{\text{DC}}/V_{\text{yield}}$ is a **per-node** ratio ($A_0 = E_{local}\ell_{node}/V_{YIELD}$), and at 30 kV across real quartz the vacuum per-node $A_0 = 10^{-7}$–$10^{-10}$ → vacuum $c_{eff}$ modulation ~0. The "0.687 at 30 kV" reading conflates apparatus voltage with the per-node ratio (per `vol4/claim-quality.md:51`); a genuine vacuum $c_{eff}$ modulation needs facility fields ($\sim 8\times10^{16}$ V/m). The bench falsifier tests the material's $C(V)$-arc shape, classified consistency-class.
2. **Asymmetric-electrode vacuum-mirror bench** (Vol 4 Ch 11): cross-polarized vacuum birefringence at $\sim 10^{12}$ departure from QED's polynomial Euler-Heisenberg expansion, because Op14's saturation kernel departs from polynomial before it sums to the same Born-Infeld form
3. **Autoresonant rupture** (Vol 4 Ch 15): PLL ring-up to Schwinger-fraction rupture — autoresonant lock condition $\omega_{\text{drive}} = \omega_{\text{local}}(A^2(t))$ as $A^2$ rises tracks the Op14 frequency drop quantitatively
4. **High-field laser bench**: at $A^2 \to 1$ regions, local clock measured via interferometric phase delay against unstrained reference

## Cross-references

- **Canonical manuscript:**
  - Vol 3 Ch 3 (macroscopic relativity) — $\tau_{\text{local}} = n(r) \cdot \tau_{\text{unstrained}}$ gravitational analog
  - Vol 4 Ch 1 §sec:thixotropic-relaxation — Op14 dynamic impedance derivation
  - Vol 1 Ch 6 (universal operators) — Op14 in operator catalog
- **KB cross-cutting:**
  - [Lattice Impedance Decomposition](../../../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) — $Z_{\text{eff}}(r) = Z_0 / \sqrt{S}$ canonical
  - [Theorem 3.1 Q-factor](theorem-3-1-q-factor.md) — TIR-boundary leakage at Op14-modulated impedance
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — Op14 as 26-instance kernel application
  - [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](../../../common/boundary-observables-m-q-j.md) — substrate-observability rule using local-clock-frozen interior
  - [Substrate-Perspective Electron](../../../vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md) — operational view of local-clock-slowing at canonical electron
  - [Photon Identification](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md) — free photon at sub-saturation has $\omega_{\text{local}} \approx \omega_{\text{global}}$ (Regime I); electron formation engages Op14 at $V_{\text{yield}}$
  - [Vol 3 Ch 3 refractive-index-of-gravity leaf](../../../vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md) — gravitational case
