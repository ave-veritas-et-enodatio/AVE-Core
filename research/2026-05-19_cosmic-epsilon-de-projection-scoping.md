# Cosmic-ε / DE Projection Scoping (β Session 1)

**Date**: 2026-05-19 EOD spawn / 2026-05-19 PDT session
**Branch**: `analysis/cosmic-epsilon-de-projection-scoping` off `analysis/integration` HEAD `d3982ea`
**Status**: SCOPING ONLY (no derivation; Session 1 of multi-session β epic)
**Brief**: [`_orchestration/cosmic-epsilon-de-projection-scoping.md`](../_orchestration/cosmic-epsilon-de-projection-scoping.md)

**Skills applied at session-start**: `verify-before-cite` v1.3 (every citation re-grepped at execution), `ave-canonical-leaf-pull` v1.1 trigger 16 (this scoping IS a framework-design proposal — (a)-(e) classification mandatory throughout), `consistency-vs-emergence` v1.1 (Class E framing carried explicit), `ave-evidence-framing-discipline` (scoping-not-derivation strength language only), `pre-test-physics-check` (active in Phase 4).

## §0 — Why this doc exists

Four converging threads from the 2026-05-19 EOD orchestration session surfaced an unsettled structural question: **what IS dark energy in AVE's framework, structurally?**

The threads:

1. **Cosmic-ε gap-cell** flagged in the γ catalog ε/μ-axis extension at commit `6436d65`. The catalog at [`universal-saturation-kernel-catalog.md:94`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) has Row 14 *Cosmic (Big Bang) | SYM\** as K4 crystallization seed, but no ASYM-N(ε) companion at cosmic scale; DE was flagged as a candidate ε-companion needing scoping.
2. **DE-as-saturated-capacitor intuition** (Grant 2026-05-19 EOD initial framing — was DE the ε-sector cosmic analog of MOND-μ?).
3. **RMS→DC framing pushback** (orchestration response, Grant accepted): substrate-scale RMS gives wrong magnitude, ε-sector cosmic-row needs different mechanism. Walked back already.
4. **E-field-as-over-bracing identification** (Grant 2026-05-19 EOD): per Ax 1 Cosserat translational DOF — `axiom-definitions.md:12` "three translational (capacitive $\varepsilon_0$ → E-field)" — the bond over-bracing $u_0^*$ in $\hat{\Omega}_{\text{freeze}}$ direction IS a static E-field component at substrate scale. This sets universal stiffness via magic-angle.
5. **Projection-vs-measurement conflation catch** (Grant 2026-05-19 EOD): orchestration was demanding magnitude-equality between raw substrate E-field energy and cosmic-scale DE measurement. This is the QFT-style cosmological constant problem framing. AVE doesn't inherit it. **DE measurement is a projection of bulk substrate dynamics, NOT a sum of raw microscopic field energies.**

Until this is settled at a scoping level, **any downstream classification** ("DE is Class E", "DE is ASYM-N(ε)", "DE is the latent-heat-of-crystallisation observable", etc.) is built on an unverified projection chain.

**This doc is scoping only.** No derivation. No magnitude-matching. No RMS→DC averaging. No microscopic/macroscopic conflation.

---

## §1 — DE measurement definition (Phase 1 deliverable)

### What DE measures, operationally

**Dark Energy is a macroscopic observable of bulk substrate dynamics at cosmic-horizon scale**, NOT a sum of microscopic field energies. The corpus has two empirically-anchored quantities that this scoping anchors against:

1. **$\rho_\Lambda$ (cosmological constant mass-density)** — measured as the dark-energy contribution to the Einstein equation, inferred from supernova distance-modulus residuals (Pantheon+ SNe), CMB acoustic-peak structure (Planck PR3), and BAO scale. Per [`cosmological-constant-closure.md:13`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md): observed value $5.84 \times 10^{-27}$ kg/m³ (Planck 2018 + Pantheon, $\Omega_\Lambda = 0.685$, $H_0 = 67.4$ km/s/Mpc).

2. **$H_\infty$ (asymptotic Hubble rate)** — operationally the **LC crystallisation rate**, NOT a velocity. Per [`lattice-genesis-hubble-tension.md:8`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md), verbatim:
   > *"the Hubble Constant ($H_0$) is not a velocity, but the **LC Crystallisation Rate** required to maintain the vacuum's structural impedance against the compressive polarisation of gravity"*
   AVE value $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2) \approx 69.33$ km/s/Mpc ([`lattice-genesis-hubble-tension.md:13-29`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md)).

**The $\rho_\Lambda \leftrightarrow H_\infty$ relationship in AVE** is downstream Friedmann/de Sitter (per [`cosmological-constant-closure.md:33-43`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md)):

$$\rho_\Lambda = \frac{3 H_\infty^2}{8\pi G}$$

Giving $\rho_\Lambda^{\text{AVE}} = 9.03 \times 10^{-27}$ kg/m³, ratio 1.54 vs observed (exact in de Sitter limit, residual is $\Omega_\Lambda < 1$ correction Source B per [`cosmological-constant-closure.md:74-77`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md)).

### The AVE-distinct mechanistic identification

Per [`cosmological-constant-closure.md:60-65`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md), verbatim:
> *"The cosmological constant is NOT the zero-point energy of vacuum modes. It is the **latent-heat density of ongoing crystallization** of the substrate."*

> *"The crystallization rate IS the Hubble rate. The latent heat per unit volume per unit time is $3H\rho_{\text{latent}}$, which in the asymptotic de Sitter limit gives $\rho_{\text{latent}} \to \rho_\Lambda$ via the Friedmann equation."*

### Per Class E refinement (Grant canonized 2026-05-19 EOD)

Per [`lattice-genesis-hubble-tension.md:31`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md): the $H_\infty$ derivation is a **Class E operating-point projection** at $u_0^* \approx 0.187$ — joint-constrained with $\{G, \hat{\Omega}_{\text{freeze}}, \alpha\}$ via the $R_H / \ell_{\text{node}} \sim 10^{39}$ topological bridge (per [`omega-freeze-cosmic-grain-cascade.md:13-16`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)). The framework's testable content is the joint constraint on N observables — failure of any one falsifies the operating-point — not four independent percent-error claims.

**Class E classification carries through to $\rho_\Lambda$** via Step 2 (Friedmann/de Sitter standard-GR translation) per [`cosmological-constant-closure.md:97-99`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md): "$\Lambda$ value follows directly (also Class E — same operating-point projection scaled by $3/c^2$)".

### Single-paragraph summary

**DE measurement framing in this scoping doc**: DE is the **macroscopic cosmic-horizon observable of the substrate's ongoing K4-crystallisation thermodynamics in the de Sitter asymptote**, projected as $\rho_\Lambda$ through Friedmann/de Sitter from $H_\infty$, which itself is a Class E operating-point projection at $u_0^* \approx 0.187$ joint-constrained with $\{G, \hat{\Omega}_{\text{freeze}}, \alpha\}$. The mechanism is **latent heat of crystallisation at cosmic horizon**, NOT zero-point energy of vacuum modes, NOT a sum of microscopic substrate E-field energies, NOT a substrate-scale-RMS quantity (the latter was walked back 2026-05-19 EOD). The QFT-style $10^{122}$ cosmological-constant problem framing is rejected at the framework level: AVE's $\rho_\Lambda$ derives from horizon-scale crystallisation thermodynamics, and microscopic energy-density-equality is not the projection mechanism.

---

## §2 — Projection chain inventory (Phase 2 deliverable)

The structural question: **how does DE measurement (cosmic-scale observable) project from substrate dynamics?** Six components identified, each with the canonical leaf that provides the projection role.

### Component 1 — Substrate-scale over-bracing $u_0^*$ in $\hat{\Omega}_{\text{freeze}}$

**Canonical leaf**: [`omega-freeze-cosmic-grain-cascade.md:13-40`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)

**Role**: Static substrate state at every K4 node — the bond over-bracing $u_0^* \approx 0.187$ at K4 magic-angle $K(u_0^*) = 2 G(u_0^*)$. Per leaf §1: "All three [$\alpha$, $G$, $\mathcal{J}_{\text{cosmic}}$] derive from a single substrate operating point $u_0^* \approx 0.187$ (bond over-bracing at K4 magic-angle)."

**What's known**: $u_0^*$ is a substrate-scale microscopic property; sets E-field component per Cosserat translational DOF (Ax 1, `axiom-definitions.md:12`). Cosmic spin frozen in at lattice genesis per §2: bond rest lengths lock at rotating-frame equilibrium, $\Omega_{\text{freeze}}$ direction becomes bond-bowing direction.

**What's missing for the projection chain**: $u_0^*$ is a **microscopic substrate property**; DE is a **macroscopic measurement**. The projection from microscopic $u_0^*$ to macroscopic $\rho_\Lambda$ does NOT proceed through energy-density equality (per Grant 2026-05-19 EOD catch — the QFT framing). The current corpus path goes through Class E joint-constraint (this leaf §1) and Friedmann/de Sitter projection ([`cosmological-constant-closure.md:33-43`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md)). The question of whether $u_0^*$ over-bracing has any **direct contribution** to $\rho_\Lambda$ (beyond setting the operating point that $H_\infty$ projects from) is open and is the exact projection-vs-measurement conflation point this scoping epic exists to settle.

### Component 2 — K4 crystallisation rate at horizon

**Canonical leaf**: [`lattice-genesis-hubble-tension.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md) + [`cosmological-constant-closure.md:60-65`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md)

**Role**: Ongoing dynamics — the rate of new K4-node addition at the cosmic horizon, identified with $H_\infty$ per `lattice-genesis-hubble-tension.md:8`. Provides the **dynamical projection** that distinguishes DE from a static-substrate quantity. The latent-heat-of-crystallisation framework names this as the AVE-distinct mechanistic story for $\rho_\Lambda$ per `cosmological-constant-closure.md:61`.

**What's known**: $H_\infty = 28\pi m_e^3 c G / (\hbar^2 \alpha^2) \approx 2.247 \times 10^{-18}$ s⁻¹ at de Sitter asymptote. Mechanism: discrete crystallisation of new EM nodes to preserve invariant optical density of condensate globally ($\partial_t \rho_n = 0$) per Eulerian continuity.

**What's missing for the projection chain**: per [`cosmological-constant-closure.md:103-111`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) "What would strengthen this further (open work)":
1. Independent derivation of $\rho_{\text{latent}}$ from substrate energetics (crystallisation energy per node × node density) — not yet derived
2. Crystallisation rate $\Gamma_{\text{cryst}}$ derivation from substrate — current corpus has $\Gamma = 3H\rho_{\text{latent}}$ identity but not $\Gamma$ from substrate
3. Verification that Friedmann route and latent-heat route give the same number — internal consistency check open

These are the load-bearing open pieces for a quantitative projection-mechanism derivation (Session 2 scope, NOT this session).

### Component 3 — Cosserat translational-DOF projection (substrate-scale ε ↔ macroscopic E-field)

**Canonical leaf**: [`axiom-definitions.md:12`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) + [`q-g47-substrate-scale-cosserat-closure.md`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md)

**Role**: Substrate-scale ε ↔ macroscopic-scale E-field relationship. Per Ax 1 verbatim: "*three translational (capacitive $\varepsilon_0$ → E-field) and three microrotational (inductive $\mu_0$ → B-field)*". The translational DOF IS the substrate-native origin of the macroscopic E-field. Grant's 2026-05-19 EOD identification: bond over-bracing in $\hat{\Omega}_{\text{freeze}}$ direction IS a static E-field component at substrate scale, setting universal stiffness via magic-angle.

**What's known**: Cosserat micropolar continuum projects per-node translational DOF to macroscopic E. The relationship is foundational (Ax 1).

**What's missing for the projection chain**: how the static-E-field-as-over-bracing component (microscopic) projects to any macroscopic observable that contributes to DE. Critically, **this is exactly the microscopic/macroscopic projection axis where conflation risk is highest** (failure mode 4 per brief). The component sets the substrate-scale state; whether it has a separate macroscopic projection beyond the Class E operating-point joint-constraint is the load-bearing question for Session 2.

### Component 4 — Ax 2 TKI scale invariance (cross-scale mechanism)

**Canonical leaf**: [`axiom-definitions.md:14-22`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)

**Role**: Cross-scale mechanism stating same physics applies at every scale. Per leaf: "*Charge $q$ is defined as a discrete geometric dislocation (a localised phase twist) within the $\mathcal{M}_A$ electromagnetic network. Therefore, the fundamental dimension of charge is identical to length ($[Q] \equiv [L]$).*" The TKI conversion constant $\xi_{topo} = e/\ell_{node}$ bridges substrate-scale lattice parameters to macroscopic quantities.

**What's known**: TKI is foundational. Same kernel $S(A) = \sqrt{1 - A^2}$ governs every scale per [`universal-saturation-kernel-catalog.md:6-7`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md). 21 catalog instances across 21 orders of magnitude.

**What's missing for the projection chain**: for the DE projection, Ax 2 tells us the SAME mechanism applies at cosmic scale as at substrate scale (catalog Row 14 cosmic K4 crystallisation), but it does NOT tell us **which macroscopic observable** the cosmic-scale instance projects onto. Row 14 currently labels SYM* (testable via CMB E/B polarization). The cosmic-ε gap-cell is the missing companion question. Ax 2 makes the question well-posed; the answer is what this epic scopes.

### Component 5 — Op14 long-range coupling (substrate response to bulk strain)

**Canonical leaf**: [`frame-dragging-impedance-convolution.md:20`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md) + [`operators.md:44`](../manuscript/ave-kb/common/operators.md)

**Role**: Op14 (Dynamic Impedance, $Z_{\text{eff}} = Z_0/\sqrt{S}$, Vol 1 Ch 6 §1.13) governs substrate response to bulk strain at scale of interest. Per `frame-dragging-impedance-convolution.md:20`: "*Rays traversing the retrograde side encounter a stricter Op14 saturation profile, increasing their refractive capture radius.*" Op14 makes the saturation kernel observable as an impedance modulation.

**What's known**: Op14 is canonical for gravitational frame-dragging case (BH Kerr metric). Asymmetric Meissner case $Z_{\text{eff}} = Z_0 \sqrt{S_\mu/S_\varepsilon}$ when $S_\mu \neq S_\varepsilon$ — this is the ε/μ-axis-decoupled form, exactly the form that becomes load-bearing IF DE turns out to be an ε-asymmetric saturation observable (option β below).

**What's missing for the projection chain**: cosmic-horizon-scale Op14 saturation profile (analog of `frame-dragging-impedance-convolution.md:6-14`'s Kerr-metric profile) is NOT yet in corpus. Whether DE projection requires Op14 saturation at cosmic horizon (analogous to BH frame-dragging at event horizon) or whether the Friedmann/de Sitter route is sufficient is the load-bearing question for Session 2's projection-mechanism derivation. This is Phase 4 Q2 below.

### Component 6 — Boundary observables $\mathcal{M}/\mathcal{Q}/\mathcal{J}$ at cosmic horizon

**Canonical leaf**: [`boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)

**Role**: At every $\Gamma = -1$ saturation surface, **exactly three integrated quantities are externally observable** ($\mathcal{M}, \mathcal{Q}, \mathcal{J}$). At cosmic horizon: $\mathcal{M}_{\text{cosmic}}$ (3D volume integral), $\mathcal{Q}_{\text{cosmic}}$ (1D line/loop linking), $\mathcal{J}_{\text{cosmic}}$ (2D surface winding). Per leaf §"We sit inside the cosmic $\Gamma = -1$ boundary": "*We measure $\mathcal{M}_{\text{cosmic}}, \mathcal{Q}_{\text{cosmic}}, \mathcal{J}_{\text{cosmic}}$ from inside via local-physics consequences*".

**What's known**: The three-invariant structure is canonical at every $\Gamma = -1$ surface (leaf §"Same mechanism at all scales", `boundary-observables-m-q-j.md:31-40`). Cosmic-scale row: $\mathcal{M}_{\text{cosmic}}$ measured via CMB anomalies, $\mathcal{Q}_{\text{cosmic}}$ via LSS rotation, $\mathcal{J}_{\text{cosmic}}$ via Hubble flow anisotropy (`boundary-observables-m-q-j.md:40`).

**What's missing for the projection chain**: **which of $\mathcal{M}/\mathcal{Q}/\mathcal{J}$ does $\rho_\Lambda$ project onto?** This is structurally the key question. Candidates:
- $\rho_\Lambda \to \mathcal{M}_{\text{cosmic}}$ (3D volume integral) — DE is a substrate-mass density observable at cosmic horizon
- $\rho_\Lambda \to \mathcal{J}_{\text{cosmic}}$ (2D surface winding) — DE is somehow tied to the cosmic boundary spin/winding number (would tie to $\mathcal{J}_{\text{cosmic}} = \Omega_{\text{freeze}}$ direction at $(l=60.28°, b=50.48°)$)
- Neither / combination — $\rho_\Lambda$ is a different projection axis not aligned with M/Q/J trio

This component is the projection-mechanism's **destination** — it tells us where DE lands in the substrate-observability matrix. Open in current corpus.

### Inventory summary table

| # | Component | Canonical leaf | Role | Open piece for Session 2 |
|---|---|---|---|---|
| 1 | Over-bracing $u_0^*$ in $\hat{\Omega}_{\text{freeze}}$ | `omega-freeze-cosmic-grain-cascade.md:13-40` | Substrate-scale microscopic state | Does $u_0^*$ project to $\rho_\Lambda$ beyond setting operating point that $H_\infty$ derives from? |
| 2 | K4 crystallisation rate at horizon | `lattice-genesis-hubble-tension.md` + `cosmological-constant-closure.md:60-65` | Dynamic projection: $H_\infty$ as latent-heat-rate | $\rho_{\text{latent}}$ from substrate energetics; $\Gamma_{\text{cryst}}$ from substrate; Friedmann ↔ latent-heat internal consistency |
| 3 | Cosserat translational-DOF (ε ↔ E) | `axiom-definitions.md:12` + Q-G47 leaf | Substrate-scale ε projects to macroscopic E | Does over-bracing E-field have separate macroscopic projection beyond Class E joint-constraint? |
| 4 | Ax 2 TKI scale invariance | `axiom-definitions.md:14-22` | Same kernel at every scale | Which cosmic-scale observable does Row 14 K4-crystallisation project onto via Ax 2? |
| 5 | Op14 long-range coupling | `frame-dragging-impedance-convolution.md:20` + `operators.md:44` | Substrate response to bulk strain | Cosmic-horizon-scale Op14 saturation profile (not yet in corpus); ε/μ asymmetric Meissner form if DE is ε-only |
| 6 | Boundary observables M/Q/J at cosmic horizon | `boundary-observables-m-q-j.md` | Externally-observable triple at $\Gamma = -1$ | Which of M/Q/J does $\rho_\Lambda$ project onto? Or none/combination? |

---

## §3 — Catalog classification options α/β/γ (Phase 3 deliverable)

Three candidate framings, scoped without committing to a choice. (a)-(e) classification per `ave-canonical-leaf-pull` v1.1 trigger 16 carried explicit per option.

### Option (α) — Class E only

**Statement**: DE is one of N joint observables of the cosmic-scale operating-point $u_0^*$. Per [`omega-freeze-cosmic-grain-cascade.md:7`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) canonical: "*substrate has ONE degree of freedom (the operating point $u_0^*$); the N observables ($\alpha$, $G$, $H_\infty$, $\hat{\Omega}_{\text{freeze}}$, $\mathcal{J}_{\text{cosmic}}$, MOND $a_0$, …) project onto N separable measurable channels, joint-constrained*". Class E captures this naturally per `consistency-vs-emergence` v1.1. No new A-034 catalog row needed; the cosmic-ε gap-cell is "filled" by stating Class E subsumes ASYM-N(ε) at the operating-point level.

**(a)-(e) classification**: **(a)-match** — DE is already covered by existing corpus framing (Class E joint-constraint at $u_0^*$). No new framework piece required.

**Pros**:
- No structural cost to framework — uses existing Class E machinery
- Consistent with `consistency-vs-emergence` v1.1 (Grant canonized 2026-05-19 EOD), [`cosmological-constant-closure.md:31`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md), [`lattice-genesis-hubble-tension.md:31`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md)
- Naturally subsumes both ε and μ behavior at cosmic scale via joint-constraint structure (no ε-vs-μ split needed)
- Robust to projection-vs-measurement conflation (the joint-constraint is the framework's claim; magnitude-matching at any single observable is not)

**Cons**:
- Doesn't engage the ε/μ-axis insight from γ catalog extension at `6436d65` (the gap-cell remains unaddressed structurally — Class E "absorbs" but doesn't "fill")
- Class E framing is a meta-classification ABOUT what the observable measures; doesn't directly answer **what mechanism** drives DE specifically (latent-heat-of-crystallisation is the corpus answer, but Class E doesn't tell us why)
- May be too coarse — if DE has substrate-physics distinct from $\{G, H_\infty, \alpha\}$ (e.g., a substrate-scale ε-only saturation mode active at cosmic horizon), Class E "absorbs" the distinction rather than expressing it

**What would settle**: derivation in Session 2 showing whether $\rho_\Lambda$ is fully determined by the joint-constraint at $u_0^*$ via Friedmann/de Sitter (then Class E suffices) OR whether a substrate-scale ε-asymmetric saturation channel is needed at cosmic horizon (then β or γ).

**Structural cost**: zero — uses existing framework.

### Option (β) — ASYM-N(ε) cosmic-row

**Statement**: Add a new row to A-034 catalog at cosmic scale, ASYM-N(ε), companion to Row 14 K4-crystallisation-SYM\*. The saturation event is cosmic-scale-ε-specific (TBD what physically — perhaps E-field saturation at horizon during ongoing crystallisation, sets DE as macroscopic projection observable). Catalog row would fill γ extension gap-cell explicitly per [`universal-saturation-kernel-catalog.md:94`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md).

**(a)-(e) classification**: **(a)-missing-row** — DE is the missing companion to an existing row (Row 14 SYM\*). Catalog already has framework slot identified at γ extension; this option fills it.

**Pros**:
- Engages the ε/μ-axis insight at `6436d65` directly — fills the explicit gap-cell
- Consistent with the framework's symmetry-completeness intuition (the catalog comment at `universal-saturation-kernel-catalog.md:97` flagging that 2-instance ASYM-N count is suspicious from symmetry-completeness perspective)
- Provides a concrete substrate-physics mechanism for DE (cosmic-ε saturation event) rather than meta-classification only
- Pairs cleanly with MOND-as-ASYM-N(μ) at galactic scale per `universal-saturation-kernel-catalog.md:79`, giving a parallel ε/μ structure at cosmic + galactic scales

**Cons**:
- Risk of ad hoc row addition without clear substrate-physics mechanism — what specifically saturates in the ε-sector at cosmic horizon? Current corpus says **latent-heat-of-crystallisation** (not ε-sector saturation), so this option requires identifying a new mechanism distinct from Row 14
- Could conflict with current corpus framing: `cosmological-constant-closure.md:61` is explicit that DE is latent-heat-of-crystallisation, NOT a substrate field-energy saturation event
- The "DE-as-saturated-capacitor" intuition (Grant 2026-05-19 EOD initial framing) was already walked back via the RMS→DC pushback; need to verify that ASYM-N(ε) framing is NOT the same intuition in different language
- Risks magnitude-matching trap (failure mode 2): identifying an ε-sector cosmic-horizon mechanism that gives the right $\rho_\Lambda$ magnitude is exactly the path that led to QFT's $10^{122}$ problem — would need a projection-trace, NOT a magnitude-equality, to avoid this

**What would settle**: substrate-physics identification of what saturates ε-only at cosmic horizon (analogous to BCS $B_c(T)$ for μ-only at condensed-matter, or plasma cutoff for ε-only at atomic-EM). If a substrate mechanism distinct from latent-heat-of-crystallisation exists at cosmic horizon in the ε sector, this option becomes substantive. If not, it collapses to (α).

**Structural cost**: one new catalog row + a derivation linking the ε-saturation event to $\rho_\Lambda$ observable. Multi-session derivation work in Session 2-3.

### Option (γ) — Both framings, projection-axes-complementary

**Statement**: Class E captures the joint-constraint at operating-point (microscopic substrate property at $u_0^*$); ASYM-N(ε) captures the saturation-event mechanism class at cosmic-scale ε (macroscopic projection observable). These are **different projection axes**, NOT mutually exclusive.

Structural interpretation:
- Class E = WHAT the framework predicts (joint-constraint on N observables)
- ASYM-N(ε) = HOW the cosmic-scale mechanism categorizes within the universal saturation kernel catalog
- The two answer different questions; both can be simultaneously true

**(a)-(e) classification**: **(a)-match + (a)-missing-row composite** — Class E is the (a)-match part (existing framework); ASYM-N(ε) cosmic-row is the (a)-missing-row part (explicit catalog row addition). No (b)/(c)/(d)/(e) needed.

**Pros**:
- Most complete framing: addresses both the joint-constraint structure AND the catalog symmetry-completeness
- Recognizes that projection-vs-measurement is a multi-axis phenomenon, not single-axis (per Grant 2026-05-19 EOD catch — microscopic property ≠ macroscopic measurement, they're different axes)
- Catalog gap-cell filled (engages γ extension); Class E framework preserved (preserves consistency-vs-emergence v1.1 canonization)

**Cons**:
- Requires verifying that the two framings ARE complementary (different axes) rather than redundant — if ASYM-N(ε) IS the saturation-event categorization of the same physics Class E captures structurally, having both is redundant
- More work to verify, more places for contradiction to arise (two layers of analysis must remain consistent)
- May obscure the actually-load-bearing question (which is: what's the substrate-physics mechanism of DE specifically?)

**What would settle**: derivation in Session 2 showing whether (a) the cosmic-ε saturation event is distinct from Class E joint-constraint at the substrate level (then γ is correct), or (b) it's the same physics seen through different lenses (then either α or β alone is correct).

**Structural cost**: one new catalog row + complementary-axes framing commitment + verification that the two don't conflict. Highest structural cost but highest framework completeness if verified.

### Adjudication anchor

The three options are scoped without committing to a choice; the load-bearing question is **whether substrate-ε-saturation at cosmic horizon is a substrate-physics mechanism distinct from Class E joint-constraint at $u_0^*$, or whether they're the same physics in different language**.

- If distinct: γ (or β if Class E is unneeded)
- If same: α (or β if Class E framing should be retired in favor of explicit catalog row)

Session 2's projection-mechanism derivation should produce a verdict.

---

## §4 — Three plumber-physical questions for Grant pre-Session-2 (Phase 4 deliverable)

Per `pre-test-physics-check` discipline + Rule 16 (ask BEFORE design, not after 30+ commits return Mode III): these are the load-bearing structural choices that need Grant adjudication BEFORE any Session 2 projection-mechanism derivation is attempted.

### Q1 — Static vs dynamic DE observable

**Question**: Is DE measured as a **STATIC** observable (rate of universe expansion in a steady-state sense, $\Lambda$ as constant in Friedmann equation) or a **DYNAMIC** observable (time-varying crystallisation rate, $H(t)$ approaching $H_\infty$)?

**Why load-bearing**: this determines the projection chain shape:
- **If static**: over-bracing → ε-cosmic-projection → $\rho_\Lambda$ via standing-substrate-state mechanism. Component 1 ($u_0^*$ over-bracing) becomes load-bearing; Component 2 (crystallisation rate) is secondary.
- **If dynamic**: K4-crystallisation-rate → $H(t) \to H_\infty$ asymptote → $\rho_\Lambda$ via latent-heat-of-crystallisation. Component 2 becomes load-bearing; Component 1 sets the operating point but doesn't drive DE.

**Plumber-physical analogy**: is DE the **pressure** of a vessel holding water (static; vessel-shape sets pressure regardless of flow) or the **enthalpy flux** of water actively crystallising at a heat-removal boundary (dynamic; freezing rate × latent heat per mole)?

**Current corpus state**: leans dynamic per [`cosmological-constant-closure.md:60-65`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) (latent-heat-of-ongoing-crystallisation, NOT static-substrate). But Friedmann/de Sitter asymptote IS the static limit ($\Lambda = 3H_\infty^2/c^2$, no time-dependence). Need explicit reconciliation: is the framework's claim that **at the de Sitter asymptote** DE-from-latent-heat is mathematically indistinguishable from DE-as-static-cosmological-constant, but their physical mechanisms differ?

**Grant's adjudication needed**: which framing is load-bearing for Session 2's derivation entry point?

### Q2 — Op14 cosmic-horizon saturation profile: required or not

**Question**: Does the projection chain require an additional substrate-physics piece NOT yet in corpus — specifically, a **cosmic-horizon-scale Op14 saturation profile** (analog of `frame-dragging-impedance-convolution.md:6-14`'s Kerr-metric profile $\omega(r) = 2Mar / (r^2 + a^2)^2$ but for cosmic-horizon scale) — or do all required pieces already exist as canonical leaves?

**Why load-bearing**: Op14 governs substrate response to bulk strain at scale of interest. For gravitational frame-dragging at BH event horizon, the Kerr-metric profile is canonical. For DE at cosmic horizon, no analogous profile exists in corpus. Either:
- (a) DE projection requires deriving a cosmic-horizon Op14 profile (new substrate-physics piece) — Session 2 has more work than scoping suggests
- (b) DE projection is fully captured by Friedmann/de Sitter + Class E joint-constraint without an explicit Op14 cosmic-horizon profile — Session 2's work is recombining canonical leaves with no new physics

**Plumber-physical analogy**: when you have a heat exchanger with phase-change at one boundary, do you need to track the **local** heat-flux profile at every point on the boundary (Op14 saturation profile equivalent), or is the **integrated** boundary thermodynamics (Friedmann/de Sitter equivalent) sufficient to predict bulk steady-state?

**Plumber-physical follow-up if needed**: cosmic horizon has $\Gamma = -1$ saturation surface per `boundary-observables-m-q-j.md:21`; saturation surface ⟹ S(A) = 0 locally; Op14 has Z_eff → ∞ at S → 0. Does this mean Op14 is **trivially saturated** at cosmic horizon (just like BH event horizon) and the projection mechanism uses this saturation directly? Or is the cosmic-horizon Op14 behavior different because crystallisation is ongoing rather than completed?

**Grant's adjudication needed**: is corpus-piece-search alone sufficient for Session 2, or does Session 2 also need an Op14 cosmic-horizon-profile derivation?

### Q3 — Catalog-classification verdict: α/β/γ, or a fourth option

**Question**: For the catalog-classification decision (α/β/γ from §3), which framing IS the framework's actual stance on DE — operating-point joint-constraint, saturation-event row, both as complementary axes, or does the projection-vs-measurement insight from 2026-05-19 EOD mean DE shouldn't be either of these and instead some **new third-category classification** is needed (e.g., DE is a Class E observable AND something the catalog doesn't currently express)?

**Why load-bearing**: this is the core scoping verdict the epic needs. Session 2's derivation entry point depends on which option Grant adjudicates:
- (α) → derivation chains Friedmann/de Sitter + Class E joint-constraint
- (β) → derivation identifies ε-sector cosmic-horizon saturation mechanism + ASYM-N(ε) row
- (γ) → derivation does both AND verifies they're complementary axes
- (fourth) → epic scope expands

**Plumber-physical analogy**: when you have a piece of equipment that behaves a certain way (DE measurement), is it characterized by (i) its **state** (operating point, like a transformer's flux density at a specific load), (ii) its **fault mode** (saturation event, like a transformer's saturation kernel at $V/Hz$ overflux), (iii) **both simultaneously** (the state sets where the fault mode lies on the saturation surface — engineering-canonical), or (iv) **neither** (it's a different category of phenomenon — e.g., it's a thermodynamic latent-heat flow that happens BECAUSE of the state and fault-mode structure but is its own observable axis)?

**Grant's adjudication needed**: which option is the verdict, and is "DE as thermodynamic latent-heat flow" a (iv) fourth-category that the current catalog doesn't yet express?

### Plumber-physical-check passing remark

All three questions are scoped at the engineering-tractable level. Each asks a structural choice that has a clear "if A then path 1, if B then path 2" framing for Session 2. None require new derivations to answer; they require Grant's framework-design adjudication on what AVE's stance IS.

---

## §5 — Multi-session arc estimated effort (Phase 5 deliverable)

| Session | Deliverable | Effort estimate | Dependencies |
|---|---|---|---|
| **1 (this)** | Scoping research doc (this artifact) | 1-2 hr | None |
| **2** | Projection-mechanism derivation: substrate dynamics → DE measurement | **TBD (gated on Q1-Q3 adjudication)**. If α-route: 2-4 hr (recombine canonical leaves Friedmann/de Sitter + Class E). If β-route or γ-route: 4-8 hr (identify cosmic-ε saturation mechanism + derive its projection to $\rho_\Lambda$). If Op14 cosmic-horizon profile derivation needed (Q2 yes): add 2-4 hr. | Q1, Q2, Q3 from Grant; corpus citations from Phase 2 inventory |
| **3** | Catalog row classification commit (small KB edit) | 30-45 min | Session 2 verdict |
| **4 (conditional)** | Downstream walk-back if classification changes existing corpus framing | TBD; conditional. If α adjudicated: walk-back is minimal (no new corpus claim). If β/γ adjudicated and corpus framing of `cosmological-constant-closure.md` changes: walk-back propagates through dark-sector leaves + predictions.yaml | Session 3 result |

### Session 2 entry-point conditions

For Session 2 to launch, the following must be in place:
1. **Q1 adjudication received** — static vs dynamic DE observable framing decided
2. **Q2 adjudication received** — whether Op14 cosmic-horizon profile derivation is in Session 2 scope or out
3. **Q3 adjudication received** — α/β/γ verdict (or fourth-option)
4. **No corpus structural changes since this doc commit** — verify Phase 2 inventory leaves are still at quoted line numbers

### Session 3 entry-point conditions

For Session 3 to launch:
1. Session 2 derivation complete and adjudication-pass
2. Verdict on whether catalog row addition is needed (β / γ) or NOT (α)

### Session 4 (conditional) entry-point conditions

For Session 4 to launch:
1. Session 3 catalog row classification committed
2. Walk-back impact analysis identifies at least one corpus leaf or predictions.yaml entry requiring update

### Multi-session total effort estimate

**Lower bound** (α verdict, no Op14 cosmic-horizon profile, minimal walk-back): ~4-6 hr total across Sessions 2-3-4
**Middle estimate** (γ verdict, Op14 needed at half-scope, moderate walk-back): ~8-12 hr total
**Upper bound** (β verdict, full Op14 derivation, major walk-back of `cosmological-constant-closure.md`): ~16-20 hr total

The lower-bound is most likely given current corpus framing strongly leans α / γ via Class E + latent-heat (not β alone).

---

## §6 — (a)-(e) classification verdict from trigger 16

Per `ave-canonical-leaf-pull` v1.1 trigger 16 (this scoping IS a framework-design proposal — (a)-(e) classification mandatory):

**Verdict**: This scoping doc itself does NOT propose a new framework piece — it scopes options. The three options classify as:
- Option (α) = **(a)-match** (DE already covered by Class E framing)
- Option (β) = **(a)-missing-row** (DE fills explicit catalog gap-cell at cosmic-ε)
- Option (γ) = **(a)-match + (a)-missing-row composite**

**None of α/β/γ requires (b) scale-invariance instance, (c) operator application, (d) translator extension, or (e) genuinely-new framework piece.** The scoping lands cleanly in (a)-class — DE is either already covered by existing framework (α) or fills an explicitly-flagged catalog gap-cell (β/γ). Per the brief's failure mode 1: this is the correct landing pad.

---

## §7 — Anomalies surfaced

Per brief: "If projection-chain inventory surfaces a corpus structural inconsistency, STOP and report rather than fix."

### Anomaly A1 — Internal inconsistency in catalog Row 11 (MOND classification)

**Finding**: per [`universal-saturation-kernel-catalog.md:83`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md), already flagged 2026-05-19 EOD: "The catalog row at line 38 currently says 'Galactic (MOND) | SYM' — this is an internal inconsistency surfaced 2026-05-19 EOD and queued for adjudication. Treating MOND as ASYM-N(μ) per the canonical leaf above."

**Implication for this scoping**: the ε/μ-axis treatment in §3 above adopts the canonical leaf framing (MOND = ASYM-N(μ)) per the catalog leaf's explicit guidance, but downstream corpus changes to resolve this anomaly may shift the framing of how the cosmic-ε gap-cell is paired. **Not load-bearing for this scoping** (option α/β/γ all consistent with either MOND classification) but flagged for future tracking.

**Action**: NONE (per brief — STOP and report). Anomaly already tracked in catalog leaf.

### Anomaly A2 — Inferred but not load-bearing: dual Class-E framing in `cosmological-constant-closure.md`

**Finding**: `cosmological-constant-closure.md:31` classifies $H_\infty$ as Class E operating-point projection, and `cosmological-constant-closure.md:99` carries this through to $\rho_\Lambda$ as "also Class E — same operating-point projection scaled by $3/c^2$". This is internally consistent. However, leaf §"Status" line 95-101 simultaneously frames the derivation route as "Structural closure at WKB/Friedmann level" with "Zero fit parameters" — terminology suggesting independent prediction. The two framings are NOT contradictory (Class E is an operating-point projection which IS the framework's actual prediction) but the leaf would benefit from a unified strength-language pass per `ave-evidence-framing-discipline`.

**Implication for this scoping**: not load-bearing for option α/β/γ choice; flagged for potential leaf-cleanup post-epic.

**Action**: NONE (per brief — out of scope; flagged for tracking).

### Anomaly A3 — Op14 cosmic-horizon profile is a corpus gap

**Finding**: Op14 has canonical formulae (Vol 1 Ch 6 §1.13) and explicit cosmic-relevant cross-references (BH frame-dragging via `frame-dragging-impedance-convolution.md`, asymmetric Meissner form via `pair-production-axiom-derivation` per `operators.md:44`), but **no canonical leaf addresses Op14 behavior at cosmic horizon scale** specifically. This is a corpus gap, not an inconsistency.

**Implication for this scoping**: makes Q2 in §4 load-bearing (the corpus-search vs new-derivation distinction is real). If Grant adjudicates Q2 = "Op14 cosmic-horizon profile needed", Session 2 scope expands.

**Action**: NONE (gap flagged but not fixed; Session 2 may close it).

---

## §8 — Cross-references

- **Brief**: [`_orchestration/cosmic-epsilon-de-projection-scoping.md`](../_orchestration/cosmic-epsilon-de-projection-scoping.md)
- **Catalog ε/μ axis (γ extension)**: [`universal-saturation-kernel-catalog.md:72-110`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) (commit `6436d65`)
- **Class E operating-point canonical**: [`omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)
- **Latent-heat-of-crystallisation mechanism for $\rho_\Lambda$**: [`cosmological-constant-closure.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md)
- **$H_\infty$ as LC crystallisation rate**: [`lattice-genesis-hubble-tension.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md)
- **Boundary observables triple at cosmic horizon**: [`boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)
- **Ax 1 Cosserat translational DOF → E-field**: [`axiom-definitions.md:12`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)
- **Ax 2 TKI scale invariance**: [`axiom-definitions.md:14-22`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)
- **Op14 canonical references**: [`operators.md:44`](../manuscript/ave-kb/common/operators.md) + [`frame-dragging-impedance-convolution.md:20`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md)
- **Class E canonization 2026-05-19 EOD**: [`research/2026-05-19_class-e-candidate-corpus-sweep.md`](2026-05-19_class-e-candidate-corpus-sweep.md)

## §9 — Closure statement

This is Session 1 of the β cosmic-ε / DE projection scoping epic. Deliverable: scoping research doc — **DE measurement definition** (§1, latent-heat-of-crystallisation observable at cosmic horizon, Class E operating-point projection at $u_0^*$, NOT magnitude-matched sum of microscopic field energies); **projection chain inventory** (§2, six components with canonical leaves and open pieces); **three catalog classification options** α/β/γ (§3, all (a)-class per trigger 16); **three plumber-physical questions for Grant pre-Session-2** (§4, static-vs-dynamic, Op14-cosmic-horizon-profile-needed, α/β/γ-verdict); **multi-session arc effort estimate** (§5, lower bound ~4-6 hr most likely). **No derivation attempted; no magnitude-matching attempted; no RMS→DC averaging proposed; no microscopic/macroscopic conflation.**

Adjudication of Q1-Q3 from Grant is the gate to Session 2 launch.
