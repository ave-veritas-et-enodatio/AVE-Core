[↑ Ch.1 — Topological Matter](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-hvb7q3]
path-stable: "referenced from electron-identification (framing #9) + electron-bound-resonator-coverage + vol4 resonant-lc-solitons as the Class-C hollow-vortex binding-structure leaf"
-->

# The Electron as a HOLLOW VORTEX — Class-C Binding-Structure Picture

**This leaf is CANONICALIZATION of a verified Class-C result, NOT new physics.** It documents
the *structural* picture of what the electron IS — a self-consistent **hollow vortex** — and
carries, prominently and load-bearing, the honesty demotions an independent verify applied to
it. The picture is a **FORM-consistency** description (AVE DESCRIBES the electron as one
self-consistent object), **NOT a chord** (it does not PREDICT the electron): exactly the
corpus meta-finding that AVE forces FORMS and imports VALUES
([`form-deriving-value-importing.md`](../../../common/form-deriving-value-importing.md)).

> **SCOPE FENCE (read first).** Two SEPARATE statements, do not conflate:
> - **EXISTENCE / CONFINEMENT (SOLID, already canon on main).** The electron's A1 mass is held by
>   the T2/charge **$\Gamma=-1$ self-trap wall at $V_{\text{yield}}$** — an *independent*, sim-surviving
>   binder ([`../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):127,:134,:136;
>   `def-vyvsn1` = T2, Grant-ruled 2026-06-30). This leaf **cross-links** that; it does NOT re-derive it.
>   The electron's EXISTENCE does not depend on the hollow-vortex picture below.
> - **BINDING-STRUCTURE (this leaf, Class-C consistency).** The hollow-vortex open/close balance is a
>   *self-consistent structural description* of the same object, banked Class-C — with three honesty
>   caveats (§3) that an independent verify made load-bearing. It is a SOFT positive, not a discriminator.
> - **IDENTITY vs ENVELOPE (D3 coexist, 2026-07-09).** The cavity this leaf describes is a **near-core
>   yield-ENVELOPE** description — the ~$\ell_{\text{node}}$ region where the medium's saturation
>   response lives (cavitation-bubble sense: *where the medium gave up*, not the inside of the
>   propeller). It answers *"how does the medium respond near the core?"*. It does **NOT** store the
>   electron's identity: charge sign and the winding integers are **topological boundary data**
>   (Burgers/Frank-analog INPUTs to the surrounding elasticity), not a spatial map read out of the
>   cavity interior. Two questions, two radii — the ENVELOPE (this leaf, Class-C) and the IDENTITY
>   (boundary data, [electron-identification.md](electron-identification.md)) COEXIST without
>   contradiction; neither demotes the other, and describing the envelope's constitution never
>   promotes this leaf to a chord (§3.3).

## §1 — What the electron IS (the Class-C FORM, genuine + earned)

The electron is a self-consistent **hollow vortex**: a **cavitated core** drilled and held open by
the $(2,3)$ Cosserat circulation, closed by the surface tension of the void↔vacuum boundary.

| element | statement | substrate source |
|---|---|---|
| **cavitated core** | the incompressible melted-vacuum EOS floor $\bar\rho_{\text{cav}} = -1/\varphi$, reachable by circulation | `cavitation_flow.py:64` (`RHO_CAV = -1/PHI`); [`../../../research/2026-06-11_bubble-physics-completion.md`](../../../../../research/2026-06-11_bubble-physics-completion.md):22 |
| **the drill (opener)** | the $(2,3)$ Cosserat circulation $\Gamma$ drills the void; outward hoop/line-tension pressure $\propto \Gamma^2/R^3$ | the winding integer + cavitation-Mach swirl (§2 below) |
| **the closer** | surface tension $\sigma/R$ (inward) of the diffuse void↔vacuum boundary | $\sigma = 3\sqrt6/10 - \sqrt{30}/10 \approx 0.18712$ (§2) |
| **equilibrium** | $R^* = \Gamma/\sqrt\sigma \approx 1.6\,\ell_{\text{node}}$ (electron / reduced-Compton scale) | §2, Model-1 headline |

**Incompressible-cavity balance, NOT a bulk-compression soliton.** The vacuum's *melted* state is
incompressible, so the bulk-K compression restoring term is **DELETED** from the free-body diagram.
The void wall sees only the outward circulation push and the inward Laplace $\sigma/R$. This is a
**cavity** balance (Laplace-vs-circulation), not an energy-basin soliton (SM/QED energy-minimization
default does NOT apply here — substrate-native-check CP2/CP10).

**Equilibrium radius.** Balancing the $R^{-3}$ opener against the $R^{-1}$ closer:
$$
\rho_0\,\Gamma^2\,\ell_{\text{node}}/R^{*3} = \sigma/R^*
\;\Rightarrow\;
R^{*2} = \rho_0\,\Gamma^2\,\ell_{\text{node}}/\sigma
\;\Rightarrow\;
R^* = \Gamma\sqrt{\rho_0\,\ell_{\text{node}}/\sigma}
\;\xrightarrow[\rho_0=\ell_{\text{node}}=1]{}\;
R^* = \Gamma/\sqrt\sigma .
$$
With $\Gamma_{\text{drill}} \approx 0.775$ and $\sigma \approx 0.18712$ (engine units), the headline is
$R^*/\ell_{\text{node}} \approx 1.34$–$1.85$ (mid $\approx 1.6$); the robust self-consistent band
across opener-law and modulus choices is $[0.59, 3.58]$ (§2.3).

## §2 — The two ingredients (σ and Γ), honestly provenanced

### 2.1 σ — the void↔vacuum interface tension (IMPORT-BY-IDENTITY, see §3.1)

$$
\sigma = c_\sigma \cdot K \cdot \ell_c \cdot (\Delta\bar\rho)^2,\qquad c_\sigma = \tfrac13\ (\text{tanh-kink, DERIVED}),
$$
with $K = 2G = 0.6$, $\ell_c = \sqrt6\,\ell_{\text{node}}$, $(\Delta\bar\rho)^2 = 1/\varphi^2$:
$$
\sigma = \tfrac13\cdot 0.6 \cdot \sqrt6 \cdot \tfrac1{\varphi^2}
= \tfrac{3\sqrt6}{10} - \tfrac{\sqrt{30}}{10} = 0.18712\ \rho_0 c_0^2 \cdot \ell_{\text{node}}.
$$
The $c_\sigma = 1/3$ tanh-kink prefactor is **genuinely derived** (sympy integrates the square-gradient
functional; the literal string "0.187" is never typed into the integrand). **But the VALUE is inherited
by interface-identity** — see §3.1 — because the three inputs ($\Delta\bar\rho = 1/\varphi$,
$\ell_c = \sqrt6$, $K = 2G$) are imported wholesale from the #190 shell interface
([`../../../research/2026-06-11_bubble-physics-completion.md`](../../../../../research/2026-06-11_bubble-physics-completion.md):54-67),
which already produced $\sigma \approx 0.187$.

### 2.2 Γ — the $(2,3)$ winding's conserved Kelvin circulation (DERIVED, provenance-clipped)

$$
\Gamma = n\cdot(\text{contour} = \ell_{\text{node}})\cdot(M_{\text{edge}}^*\cdot c_0),\qquad
\Gamma_{\text{drill}}\ (n{=}1) = 0.75\text{–}0.80\ (\text{mid }0.775)\ \text{engine units}.
$$
Three substrate-native inputs: the winding integer $n$ (the $(2,3)$: $w_{\text{tor}}=2$, $|\text{Link}|=1$);
the ropelength contour ($2\pi\cdot(\ell_{\text{node}}/2\pi) = \ell_{\text{node}}$ exactly); and the swirl speed
fixed at the cavitation-onset edge Mach $M_{\text{edge}}^* \approx 0.75$–$0.80$. **Provenance clip
(§3):** the $M_{\text{edge}}^*$ source is CLIP-demoted — only the *reach* (that $\bar\rho_{\text{cav}}$ is
REACHABLE by circulation, a smooth reversible crossing) is load-bearing, not any FLASH/LOCK verdict.

> **Homonym guard.** This $\Gamma = \oint u\cdot dl$ is the **Kelvin circulation** ($L^2/T$), NOT the Smith
> reflection coefficient $\Gamma = V_{\text{ref}}/V_{\text{inc}}$ (which is the $-1$ of the confining wall),
> and NOT the genesis-v5 seed value $\Gamma=80.75$. Do not cross-wire the two $\Gamma$'s.

### 2.3 R* — the equilibrium, and the opener-law fork (flag-don't-fix)

The opener pressure admits three models; two are self-consistent with the fixed-Mach Γ (Model 2 re-floats
the swirl as $\Gamma/(2\pi R)$, contradicting the fixed $M_{\text{edge}}^*$ premise — REJECTED). The two
self-consistent models (Model 1 filament-hoop $R^* = \Gamma/\sqrt\sigma$; Model 3 fixed-Mach Bernoulli
$R^* = 2\sigma/(\rho_0 M_{\text{edge}}^{*2})$, which is $n$-independent) bracket
$R^*/\ell_{\text{node}} \in [0.59, 3.58]$ — all $O(1)$, all inside the frozen $[0.1, 10]$ band. Which
opener law the dynamics realize is the first thing a forward $R^*$-vs-drive sim (§4) would resolve.

## §3 — THE HONEST SCOPING (the verify's demotions — load-bearing, do NOT overclaim)

These three caveats are the reason this leaf is banked Class-C consistency and NOT headlined as a chord.
They are the independent verify's demotions and must travel with the picture.

### 3.1 σ = 0.18712 is IMPORT-BY-IDENTITY, not from-scratch

The cavity void↔vacuum boundary **IS** the same $\Delta\bar\rho = 1/\varphi$ / $\ell_c = \sqrt6$ / $K = 2G$
bulk-density step already derived at
[`../../../research/2026-06-11_bubble-physics-completion.md`](../../../../../research/2026-06-11_bubble-physics-completion.md):54-67
(the #190 shell $\sigma$). Same interface described twice → $\sigma$ coincides **BY CONSTRUCTION, not
by discovery**. Feeding a shell's own inputs into a (correct) prefactor and recovering the shell's own
output is an **identity, not a corroborating coincidence**. The earned content of §2.1 is (a) the
$c_\sigma = 1/3$ tanh-kink prefactor derivation, and (b) the *structural* recognition that the
hollow-vortex closer is the #190 interface — NOT an independent second determination of 0.187.
$\sigma$ carries the #190 CANDIDATE-class ceiling (tanh-CH scaling across a non-double-well EOS;
$K$-vs-$M$ modulus $\sim 1.7\times$ spread).

### 3.2 R*/ℓ_node ≈ 1.6 is DIMENSIONALLY FORCED (a consistency check, not a discriminating test)

$R^*/\ell_{\text{node}} = n\cdot M_{\text{edge}}/\sqrt\sigma$ is a **product of three $O(1)$ dimensionless
numbers**, and $\ell_{\text{node}}$ is the theory's **ONLY** length scale — so the ratio could NOT have
landed at $10^3$ or $10^{-3}$. With $M_{\text{edge}} < 1$ (subsonic cap) and $\sigma \sim O(0.1)$, the
ratio is algebraically pinned to $O(1)$; **the gate could not have returned DEAD for any physical
$\sigma, \Gamma > 0$.** A test that cannot fail is not discriminating. The only content that is *not*
forced is the specific coefficient ($\approx 1.6$, band $0.59$–$3.58$), and even that rides the
$\sigma$/$\Gamma$/opener ranges. Passing the $[0.1, 10]$ band was never in doubt.

### 3.3 The binding is FORM-CONSISTENCY, NOT a chord (Class-C)

AVE **DESCRIBES** the electron as one self-consistent hollow-vortex object; it does **NOT PREDICT** it.
$R^*/\ell_{\text{node}}$ is dimensionless, but $\ell_{\text{node}} = \hbar/(m_e c)$ is CODATA-derived
(through $m_e$), so the $O(1)$ landing is a **consistency check** that the mechanism is self-consistent
at electron scale — NOT an independent prediction of the electron scale, and NOT an AVE-distinct chord.
This is another FORM-derived / VALUE-imported instance
([`form-deriving-value-importing.md`](../../../common/form-deriving-value-importing.md)). **Do NOT write
"binds / confirmed / derived-from-scratch / discriminating"** of this picture.

## §4 — The 5-attempt existence-side trail (unification does NOT yield a chord)

The session tried five routes to turn the electron's *existence* into a chord. All either failed, do not
exist, or are soft/tautological. The single mechanism across them: at the T2 operating point $A = \sqrt\alpha$
the varactor sits in the linear corner of the saturation kernel, so the nonlinear pull/brace contest has
no dynamic range.

| # | route | verdict | key mechanism |
|---|---|---|---|
| 1 | front-freeze | **FALSIFIED** | Mode-III disperse (Cartesian-grid artifact) |
| 2 | static eigensolve | **DOES-NOT-EXIST** (#415/#417) | coupled eigenmode absent; orbit carries carrier ratio not the (2,3) |
| 3 | bind-sim (self-braced) | **INCONCLUSIVE** | varactor pull flat to $<1\%$ at $A=\sqrt\alpha$ ($S$-range 0.35%); `p` flips with grid — [`../../../research/2026-06-30_electron-bind-sim_result.md`](../../../../../research/2026-06-30_electron-bind-sim_result.md) |
| 4 | co-compress unifier | **TAUTOLOGY → Class-C** | measured Derrick exponents re-read the seed-pinned fixed-charge convention; no failure route in-window — `research/2026-07-01_electron-unifier-cocompress_result.md` (on sibling PR; cite-by-path) |
| 5 | hollow-vortex σ-gate (this) | **SOFT-CONSISTENCY** | σ-identity + R* dimensionally forced (§3) — `research/2026-07-01_hollow-vortex-sigma-gate_result.md` (on sibling PR; cite-by-path) |

## §5 — The forward R*-vs-drive prediction (the ONLY chord-locus)

The chord, if any, lives **ONLY** in a **FORWARD $R^*$-vs-drive prediction** — $R^*$ as a function of the
drive amplitude (edge Mach / circulation), the one place a nontrivial functional dependence the algebra
alone does not pin could live. It is a **different / future experiment**, NOT realized here. It requires:

- **its OWN frozen prereg** with a **pre-registered discriminating observable** (NOT the $O(1)$ landing,
  which is forced per §3.2); and
- **the positive-$c^2$-floor integrator fixed or replaced first** — the current
  `cavitation_flow.py:159-163` floors $c^2$ strictly positive
  (`c_bulk2 = max(raw, c2_floor·c0²)`, `c2_floor = 1e-3 > 0`), so the void cannot go tensile in the
  integrated dynamics and a held void renders as reversible compliance, not a held void.

No stability sim seeded at $R \approx 1.6\,\ell_{\text{node}}$ advances the claim: it would either
reproduce the analytic $R^*$ (the seed-pinned PR#443 trap) or produce a positive-$c^2$-floor artifact.
This is the open forward handle, noted as NOT realized.

## Cross-references

- **Existence / confinement (the independent binder — SOLID, cross-linked not re-derived):**
  [`../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):127,:134,:136
  (the $\Gamma=-1$ T2/charge wall at $V_{\text{yield}}$; A1 mass sub-saturated at $A=\sqrt\alpha$ inside it)
- **The T2 wall grade ruling:** [`def-vyvsn1`](../../../common/vocabulary-register.md) (= T2, Grant 2026-06-30);
  [`pair-production-axiom-derivation.md`](pair-production-axiom-derivation.md):102 (T2 self-trap horn);
  [`../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md):16 (A1 varactor re-keyed to $V_{\text{snap}}$)
- **Canonical electron identification (the object this leaf structurally describes):**
  [electron-identification.md](electron-identification.md) (4-property def; $0_1$ unknot + $(2,3)$ + $\Gamma=-1$ + T2 core)
- **Coverage matrix (where this row lives in the honest A/B/C buckets):**
  [electron-bound-resonator-coverage.md](electron-bound-resonator-coverage.md)
- **The σ interface source (#190 shell):**
  [`../../../research/2026-06-11_bubble-physics-completion.md`](../../../../../research/2026-06-11_bubble-physics-completion.md):36-89
- **The FORM-derives / VALUE-imports meta-finding:**
  [`form-deriving-value-importing.md`](../../../common/form-deriving-value-importing.md)
- **Research trail (Class-C adjudication docs):**
  [`../../../research/2026-06-30_electron-portmap-derivation_result.md`](../../../../../research/2026-06-30_electron-portmap-derivation_result.md) (port-map + self-braced FBD, BINDS-under-T2 then sim-caveated),
  [`../../../research/2026-06-30_electron-bind-sim_result.md`](../../../../../research/2026-06-30_electron-bind-sim_result.md) (INCONCLUSIVE);
  and (on sibling PRs, cite-by-path — not yet in this worktree):
  `research/2026-07-01_electron-unifier-cocompress_result.md` (tautology → Class-C),
  `research/2026-07-01_hollow-vortex-sigma-gate_result.md` (this — soft-consistency, σ-identity, R*≈1.6)
