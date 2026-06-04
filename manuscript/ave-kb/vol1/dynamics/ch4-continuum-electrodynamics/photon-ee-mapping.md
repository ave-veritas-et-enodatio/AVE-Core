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

The free photon's wave-packet structure decomposes (informally, as a visualization / engineering convenience — not a separate substrate axiom) into a **carrier × envelope**:

- **Carrier** — the oscillation frequency $\omega$ of the $T_2$ microrotation wave. In the empty-space propagation baseline the carrier is a visualization choice ($\lambda_{eff}=10\,dx$), **not** matched to Compton or any SM scale (`photon_propagation.py`:74).
- **Envelope** — a Gaussian amplitude modulation in time (and, for a beam, transversely in space), giving a bandwidth-limited pulse (`photon_propagation.py`:77; `animate_vacuum_phonon_3d.py`:63, "A 'photon': Gaussian envelope × sinusoidal carrier frequency").

EE reading: a standard RF carrier under a pulse envelope. This is descriptive packaging of the matched-$Z_0$ transmission-line wave (§2); it adds no saturation physics ($\Delta\phi\ll\alpha$ throughout).

## §4 — The photon's own E↔B: I/Q quadrature ↔ (V_inc, V_ref), V ↔ Φ_link

This is the section the [circuit translation table](../../../common/translation-tables/translation-circuit.md):173 flags as the pending consolidating leaf. The content (gate-(a) PASSED 2026-06-04 as a **description of what the engine factually does**, read from code):

**The photon's $E$↔$B$ is a LINEAR I/Q quadrature on the bond's forward/backward voltage waves — internal to the K4 sector.** On each transmission-line bond, the incident and reflected voltage waves $(V_{inc}, V_{ref})$ ARE the photon's own in-phase / quadrature components:

$$E \sim (V_{inc} + V_{ref}), \qquad B \sim \frac{V_{inc} - V_{ref}}{Z}$$

locked together by the line impedance $Z$. This is a **linear** $E$↔$B$ coupling **internal to the K4 sector** (the bond's forward/backward voltage waves) — distinct from the *parametric* K4↔Cosserat bridge (which is where photon→matter-spin lives, §4.1 below). Equivalently, the $V\leftrightarrow\Phi_{link}$ linear LC slosh: voltage (capacitive, the $E$-like in-phase part) trades with flux-linkage $\Phi_{link}$ (inductive, the $B$-like quadrature part) every cycle, a lossless reactive exchange at $Z_0$.

> **[Resultbox]** *The photon's quadrature, in EE terms*
>
> $E \sim (V_{inc}+V_{ref})$ (in-phase, capacitive), $B \sim (V_{inc}-V_{ref})/Z$ (quadrature, inductive), locked by the line impedance. The photon's $E$ and $B$ both live in the K4 sector as the two quadratures of one matched-line wave. This is a **linear** $E$↔$B$, NOT the parametric K4↔Cosserat pair-production coupling.

**Anchors (verbatim, ✓-VERIFIED):** [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):173 ("the bond's incident/reflected voltage waves ARE the photon's own quadrature: $E\sim(V_{inc}+V_{ref})$, $B\sim(V_{inc}-V_{ref})/Z$ — a LINEAR $E$↔$B$ internal to the K4 sector"; code-confirmed `k4_tlm.py`:192-206, 340, 400; gate (a) 2026-06-04) and :233 ("(I) Intra-K4, the photon's own E↔B — LINEAR, PRESENT: `V_inc/V_ref ↔ Φ_link` ... E ~ (V_inc+V_ref), B ~ (V_inc−V_ref)/Z, locked by the line impedance").

### §4.1 — Distinguished from the parametric photon→matter bridge (do not conflate)

There are **two distinct "magnetic" DOFs and two distinct $E$↔$B$ couplings** — the load-bearing disambiguation from gate (a):

- **(I) Intra-K4, the photon's own $E$↔$B$ — LINEAR, PRESENT** (this section §4): $V_{inc}/V_{ref}\leftrightarrow\Phi_{link}$ via TLM scatter+connect. This is where the photon's quadrature (and the $R\!\cdot\!r$ phasor) lives.
- **(II) K4↔Cosserat bridge, photon → matter spin — PARAMETRIC, CANONICAL:** $V^2$ modulates the saturation varactor in $W_{refl}$ ($A^2_\varepsilon \supset V^2/V_{SNAP}^2$); it does **not** torque $\omega$. The coupling is **even in $\omega$**, so $\omega=0$ is an exact fixed point — a parametric pump that **cannot** seed the $\omega$-idler from zero (**Q0**). This IS the canonical **pair-production** coupling (matter spin from a *seeded* $\Gamma\to-1$ rupture), NOT a missing additive forcing term: a linear $V\to\omega$ term would manufacture spin below threshold (wrong physics).

The intra-K4 linear $E$↔$B$ (I) is the photon; the K4↔Cosserat parametric bridge (II) is photon→matter. Conflating them is the error gate (a) corrected. (Anchor: [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):232–238.)

## §5 — Honest-status flags

Carried verbatim per `ave-evidence-framing-discipline`:

- **This leaf is consistency / translation, not emergence.** Every mapping is an identification of already-canonical content (§1); `no-claim:` frontmatter; no new derivation.

- **$R\!\cdot\!r=\tfrac14$ is NOT canonical — Class-B, contradicts honest-α.** The substrate does **not** independently select $R\!\cdot\!r=\tfrac14$ ([translation-circuit.md](../../../common/translation-tables/translation-circuit.md):230, "the substrate does NOT independently select R·r=1/4"; `clm-0ktpcn`, Class-B, CHALLENGE-CLOSED 2026-06-04). The I/Q quadrature of §4 is where the $R\!\cdot\!r$ phasor *lives*, but the $\tfrac14$ value is a **named identification the substrate does not derive** — do NOT present §4 as deriving it.

- **The $E$↔$B$ row (translation-circuit.md:173) was ⚠ partial, "consolidating leaf PENDING" — THIS leaf is that pending leaf.** On landing, the §4.5(b) Impedance & transmission I/Q row's pending-note should point here.

- **Soliton self-lock / autoresonance at $\Gamma=-1$ is underived** (✗ GAP, [translation-circuit.md](../../../common/translation-tables/translation-circuit.md):202,217). The electron's stable confinement at the $\Gamma=-1$ boundary is asserted from the saturation mechanism; the autoresonance / self-lock that would keep it locked is a plausible-but-underived candidate (the only autoresonant-PLL leaf is invalidated for using the wrong yield threshold).

- **The shorted $\lambda/4$ resonator map is a DESCRIPTION (gate-(b) CLOSED 2026-06-04), not a $\tfrac14$ derivation.** It describes the electron's trapped-reactive-energy structure (a shorted $\lambda/4$ resonator = a half-Γ-lap on the Smith chart); it does **not** derive $R\!\cdot\!r=\tfrac14$ ([translation-circuit.md](../../../common/translation-tables/translation-circuit.md):240).

- **Helical-photon ($u\neq0$ AND $\omega\neq0$) RETRACTED** ([photon-identification.md](photon-identification.md):93). Canonical photon is single-sector ($T_2$ only). Legacy "helical soliton" scripts use the superseded framing.

> **⚠ Surfaced status drift (flag-don't-fix, for auditor adjudication).** The translation-circuit.md:173 I/Q row's note still reads that "the $R{\cdot}r=1/4$ phasor-radius question that lives in this sector is a *separate*, **gate-(b)-pending** claim", whereas the (e)-section rows at :240–241 record gate (b) as **RUN and CLOSED 2026-06-04** (R·r=¼ "CHALLENGE-CLOSED 2026-06-04, Class B hardened"). The two statements are about the same claim at different points in the same file; the :240–241 closure is the later, authoritative state. This leaf adopts the **Class-B / gate-(b)-CLOSED** status (R·r=¼ not derived) and surfaces the :173 "gate-(b)-pending" phrasing as **stale wording to reconcile**, not a live open question. Do not silently rewrite :173 — the auditor adjudicates whether to update its phrasing when this leaf lands.
