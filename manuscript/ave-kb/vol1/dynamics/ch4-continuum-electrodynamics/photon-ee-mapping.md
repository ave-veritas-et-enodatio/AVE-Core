[↑ Ch.4 Continuum Electrodynamics](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "consolidation / translation leaf — the photon's pending EE-mapping leaf that translation-circuit.md (the I/Q quadrature E↔B row) flags as 'consolidating canonical leaf pending'. Distinguishes free-photon (T2-only, Gamma=0, no core) from self-trapped-electron (Gamma=-1 Local Bubble); maps carrier x envelope, E~(V_inc+V_ref) / B~(V_inc-V_ref)/Z, I/Q quadrature <-> (V_inc,V_ref), V<->Phi_link linear LC slosh. Originates no new derivation: photon identity owned by photon-identification.md (clm-3npynp/i4p11y/fr3mos), Gamma=-1 magnetic-branch core by master-equation.md (clm-lv3uw1), EE rows by translation-circuit.md (clm-eemap1). Classified consistency/translation per consistency-vs-emergence — NOT an emergence test. Created per ave-ee-first-mapping Step 6."
-->

# Photon EE Mapping — Free Photon ($Z_0$, $\Gamma=0$) vs Self-Trapped Electron ($\Gamma=-1$)

This leaf is the photon's consolidating EE-mapping leaf — the one the [circuit translation table](../../../common/translation-tables/translation-circuit.md) I/Q-quadrature E↔B row (line 173) flags as **"consolidating canonical leaf pending."** It distinguishes the **free photon** (single-sector $T_2$, matched at $Z_0$, $\Gamma=0$, no core) from the **self-trapped electron** (the same wave at Axiom-4 saturation: $\Gamma=-1$ Local Bubble), and maps the photon's internal EE structure — carrier × envelope, the linear $E$↔$B$ as an I/Q quadrature on the bond's forward/backward voltage waves, and the $V\leftrightarrow\Phi_{link}$ linear LC slosh.

## §1 — Scope and classification

> **[Resultbox]** *Classification — consistency / translation (NOT emergence)*
>
> Per `consistency-vs-emergence`: every mapping here is a **consistency / translation identification** between a substrate primitive (canonical elsewhere) and its EE component. NONE of it is an emergence test or a new derivation. This leaf carries `no-claim:` frontmatter and references its owning claims by cross-link. In particular, the **$R\!\cdot\!r=\tfrac14$ phasor-radius question is Class-B** (the substrate does not independently select it) and is explicitly NOT presented here as derived (§5).

The owning canonical content:

> → Primary: [Photon Identification (T₂-only Cosserat ω)](photon-identification.md) — the free-photon = single-sector $T_2$ identification ($u=0$, $\omega\neq0$, $\Delta\phi\ll\alpha$, $Z=Z_0$, $\Gamma=0$) and the electron = self-trapped photon at $V_{\text{yield}}$ (clm-3npynp, clm-i4p11y, clm-fr3mos).
> → Primary: [Master Equation](master-equation.md) — the two mutually-exclusive Axiom-4 saturation branches: electric ($\varepsilon_{eff}\to0$, $Z\to\infty$, $\Gamma\to+1$ open) vs magnetic ($\mu_{eff}\to0$, $Z\to0$, $\Gamma\to-1$ short); the electron is the magnetic / short branch (clm-lv3uw1, lines 78–79).
> ↗ See also: [Circuit Translation Table](../../../common/translation-tables/translation-circuit.md) §4 / §4.5 — the I/Q quadrature E↔B row (line 173) this leaf consolidates; the $\Gamma=-1$ short-circuit row (line 115); the shorted $\lambda/4$ resonator (line 240) (clm-eemap1).
> ↗ See also: [Double-Slit EE / Glossary Mapping](../ch3-quantum-signal-dynamics/double-slit-ee-mapping.md) — the double-slit companion (the electron-as-particle navigating its ponderomotive wake).

## §2 — Free photon vs self-trapped electron (the load-bearing distinction)

## §2 — Free photon vs self-trapped electron (the load-bearing distinction)

The free photon and the electron are **two amplitude phases of the same underlying object** — a $T_2$-only transverse Cosserat-microrotation wave — parameterized only by whether Axiom-4 self-saturation has engaged ([photon-identification.md](photon-identification.md):11, §4.0). The EE distinction is sharp:

| Property | **Free photon** | **Self-trapped electron** |
|---|---|---|
| Substrate sector | $T_2$ only — $u=0$, $\omega\neq0$ | $T_2$ only — same wave, at saturation amplitude |
| Amplitude | sub-saturation, $\Delta\phi\ll\alpha$ | at-yield, $\Delta\phi\to\alpha$ ($V\to V_{\text{yield}}=\sqrt{\alpha}\,V_{\text{snap}}\approx43.65$ kV) |
| Saturation branch | none (linear regime) | **magnetic**: $\mu_{eff}\to0$ |
| Local impedance $Z$ | $Z_0\approx376.7\,\Omega$ — **matched** | $Z=\sqrt{\mu_{eff}/\varepsilon_0}\to0$ |
| Reflection $\Gamma$ | $\Gamma=0$ (matched) | $\Gamma=-1$ (**short-circuit**, total internal reflection) |
| Core / bubble | **NO core, NO bubble** | **YES** — $\Gamma=-1$ self-created $0\,\Omega$ "Local Bubble", $c_{local}\to0$ |
| EE component | matched lossless transmission line | **shorted $\lambda/4$ resonator** (gate-(b) CLOSED 2026-06-04) |
| Rest mass | none (massless) | trapped reactive energy of the shorted resonator |

**Anchors:** free photon = [photon-identification.md](photon-identification.md):11,24 (✓-VERIFIED canonical); electron = self-trapped photon = [photon-identification.md](photon-identification.md):11; $\Gamma=-1$ magnetic-branch short = [master-equation.md](master-equation.md):78–79 (clm-lv3uw1) + [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):115; Local Bubble = [resonant-lc-solitons.md](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):50 + [zero-impedance-boundary.md](../ch3-quantum-signal-dynamics/zero-impedance-boundary.md):51; shorted $\lambda/4$ resonator = [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):240.

> **[Resultbox]** *The two mutually-exclusive Axiom-4 branches (do not conflate)*
>
> At saturation the substrate divides into two symmetries that differ in which constitutive parameter collapses first:
> - **Magnetic branch** (the electron): $\mathbf{B}$ saturates $\mu_{eff}\to0$ first → $Z\to0$ → $\Gamma\to-1$ (**short-circuit**) → trapped topological knot → rest mass. This is the matter core.
> - **Electric branch** (dielectric rupture): $\varepsilon_{eff}\to0$ while $\mu_{eff}$ intact → $Z\to\infty$ → $\Gamma\to+1$ (**open-circuit**) → electromagnetically opaque / evanescent.
>
> Both governed by the same kernel $S(A)=\sqrt{1-(A/A_{yield})^2}$. The electron is the **magnetic / short / $\Gamma=-1$** branch. ([master-equation.md](master-equation.md):78–79, clm-lv3uw1.)

**Distinctness guards** (carry into any downstream use):
- The electron's "bubble" is bubble-LIKE (self-confined matter core) — it is **NOT** the free photon (which is matched, $\Gamma=0$, coreless), and **NOT** a sonoluminescence cavitation bubble (saturated Rayleigh-Plesset inertia, a different mechanism — [sonoluminescence-derivation.md](../../../vol3/applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md):25–27).
- The **dual-sector "helical photon"** ($u\neq0$ AND $\omega\neq0$) is **RETRACTED** as empirically wrong ([photon-identification.md](photon-identification.md):93, "Doc 107 correction"). The canonical photon is single-sector ($T_2$ only). Do not reintroduce it.

## §3 — Carrier × envelope

## §4 — The photon's own E↔B: I/Q quadrature ↔ (V_inc, V_ref), V ↔ Φ_link

## §5 — Honest-status flags
