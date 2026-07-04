[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.1 General Description and Features

Chapter 1 of the Vol 9 datasheet establishes the substrate identity (the substrate — natural 3D chiral Laves K4 Cosserat crystal), enumerates the load-bearing structural features (intrinsic LC oscillators at each node; bond transmission lines; Cosserat micropolar 6 DOF/node = 3E + 3B; Axiom 4 saturation kernel; $\Gamma$ boundary semantics; saturable yield + breakdown thresholds; $\xi_{topo}$ topological transduction), defines the spec-table column convention used in subsequent chapters, and establishes the epistemic position: the substrate is natural, engineering observation characterizes its limits, AVE substrate-physics derives the mechanism.

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitives are introduced; the content consolidates the canonical axiom statements (CLAUDE.md INVARIANT-S2) and the EE-as-substrate-native META framework (canonical leaf `common/translation-tables/translation-circuit.md` §2, `clm-eemap1`) into datasheet General-Description-and-Features format.

## The vacuum as a component (opening narrative)

The General Description opens with the component-identity statement (consistency-class; every clause traces to merged canon):

- **A chiral crystal of LC resonators.** The medium is the `srs` net ($z=3$, $I4_132$; ratified production carrier per D1, Grant 2026-07-03, [`_orchestration/index.md`](../../../../_orchestration/index.md)); every node is a lossless LC resonator with 6 DOF (3 translational-capacitive $\to \mathbf E$; 3 microrotational-inductive $\to \mathbf B$; Axiom 1) plus a per-node operating point (the saturation state $A$, a DC bias on the node's own nonlinearity — *not* a 7th spatial DOF). $Z_0=\sqrt{\mu_0/\varepsilon_0}\approx377\,\Omega$ (`constants.py` `Z_0`) is the network characteristic impedance.
- **z=3 vs the 4-port (reconciliation).** The physical connectivity is $z=3$ (three nearest-neighbour bonds). The "K4 4-port" $A_1\oplus T_2$ irrep decomposition (ch3/ch11) is the abstract $T_d$ scattering-amplitude decomposition of the K4-TLM scatter matrix ($\dim 4 = 1+3$), *not* a physical bond count — the documented "K4" three-way overload (axiom-named chiral Laves K4 = degree-3 srs; engine "K4" = degree-4 diamond instrument; rotation group $K_4$). The $z=3$ net and the abstract 4-port are separate referents, not a contradiction (ch3 disambiguation).
- **Transparency (governing law).** Axiom 3 minimizes $|\Gamma|^2$ at every internal boundary ([`axiom-register.md`](../../common/axiom-register.md) `axiom-3`); a matched line ($\Gamma=0$) neither reflects nor stores net bias, so light (pure AC on the ground state) crosses without a trace. The stronger chain *min-reflection $\Rightarrow$ bond-stiffness balance ($k_s=k_a$) $\Rightarrow$ isotropy + distortionless* ("one condition, three protections") is now **derived** on the srs-$z=3$ net: minimizing $\Gamma_{\mathrm{internal}}(\rho_{\mathrm{bond}}{=}k_a/k_s)$ lands knob-free on $\rho_{\mathrm{bond}}{=}1$ to machine precision, where match / isotropy / distortionlessness / Zener-$A{=}1$ co-locate — Axiom 3 IS the parent (`research/2026-07-04_parent-condition-match-forces-balance_result.md`, **[MECHANISM-DERIVED]**). **Grade note:** merged research result; canonical KB-leaf + claim-id propagation is a gated follow-on, so it is stated as a derived verdict, not yet a canonized claim.
- **Absolute-maximum ratings.** The Axiom-4 kernel $S(A)=\sqrt{1-A^2}$ has $p=2$ **shape-derived** (the lossless bond-LC L2 energy invariant forces the quarter-arc; `research/2026-07-02_axiom4-forced_result.md`, CONDITIONALLY-FORCED; count stays 4). $V_{yield}=\sqrt\alpha V_{snap}\approx43.65$ kV (T2 wall) and $V_{snap}=m_ec^2/e\approx511$ kV (A1 completion; `def-vyvsn1`) are the max ratings.
- **Matter = standing-wave state.** The electron is a phase-winding knot self-trapped at its yield wall by TIR ($\Gamma=-1$, lossless); mass = the trap's stored energy; spin/moment = its circulation; charge = a topological `Link` integer the lattice forces (winding-quantized, globally neutral), field strength a $\xi_{topo}$ calibration, static Coulomb field **locally unsourced** (four-lock no-go cascade at derivation grade, `clm-nogo4l`, [`the-sourced-charge-no-go-cascade.md`](../../common/the-sourced-charge-no-go-cascade.md)).
- **Honesty ledger.** Structure derived, scales imported ($\alpha$, $m_e$, $G$ — as every framework imports them; [`form-deriving-value-importing.md`](../../common/form-deriving-value-importing.md)). The one pre-registered measurable divergence: the electric response saturates at **tree level** (classical constitutive saturation, not a loop effect) — the vacuum-birefringence falsifier, whose discriminator is the field-**independent coefficient** ratio, NOT an $E^4$-vs-$E^2$ exponent (both are $E^2$-leading; the "$E^4$" framing was retracted as a $\sqrt\varepsilon$ conflation, `clm-pp3qwf`).

The matter-stiffening / state-diagram content is deliberately EXCLUDED (arc still computing — not canon).

## Primary canonical sources

| Source | Content |
|---|---|
| CLAUDE.md INVARIANT-S2 (Axioms 1–4) | Substrate identity; 6 DOF/node decomposition; saturation kernel; minimum-reflection principle |
| Vol 1 Ch 1 (`vol_1_foundations/chapters/01_fundamental_axioms.tex`) | Canonical chapter-form derivation of the four axioms |
| `common/translation-tables/translation-circuit.md` §2 (`clm-eemap1`) | EE-as-substrate-native META framework; minimal-DOF substrate-electrical-network claim |
| `vol4/claim-quality.md` `clm-i9l284` | $\xi_{topo} = e/\ell_{node}$ topological conversion constant |
| `vol4/claim-quality.md` `clm-0vxzfu` | $V_{yield}$ / $V_{snap}$ two-threshold distinction (load-bearing reading hazard) |

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/01_general_description.tex` (canonical Vol 9 chapter file)

---
