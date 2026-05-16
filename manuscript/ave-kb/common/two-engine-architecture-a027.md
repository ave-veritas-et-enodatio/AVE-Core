[↑ Common Resources](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1, vol4, vol5 as canonical two-engine architecture reference -->

# A-027 Two-Engine Architecture: K4-TLM + Master Equation FDTD

The AVE substrate has **two disjoint operating regimes** requiring two specialized engines. This is canonical architecture (A-027 per L5 derivation status, doc 113 §3.2): pre-2026-05-14's single-engine approach (K4-TLM for everything) is superseded.

## The two engines

| Engine | Source | Regime | Status |
|---|---|---|---|
| **K4-TLM** | `src/ave/core/k4_tlm.py` | Sub-saturation bench regime ($A \ll 1$; linear + weakly nonlinear up to $V_{\text{yield}}$ onset) | Canonical for sub-saturation |
| **Master Equation FDTD** | `src/ave/core/master_equation_fdtd.py` | Bound-state regime ($A \to 1$; saturation kernel + $c_{\text{eff}}(V)$ modulation; breathing soliton solutions) | Canonical for bound-state; v14 Mode I PASS validated |

## Why two engines

**K4-TLM** implements the discrete K4 lattice with bond-by-bond impedance updates. It has $Z(V)$ modulation (saturation-bounded characteristic impedance via Axiom 4) but **lacks $c_{\text{eff}}(V)$** — the wave speed does not slow at the saturation core. Without wave-speed modulation, the engine cannot trap waves into a localized bound state; propagating modes simply propagate.

**Master Equation FDTD** implements the substrate's non-linear d'Alembertian:
$$\nabla^2 V - \mu_0 \varepsilon_0 \sqrt{1 - (V/V_{\text{yield}})^2}\, \partial_t^2 V = 0$$
which has both $Z(V)$ and $c_{\text{eff}}(V) = c_0 \sqrt{S(A)}$ modulation. This is the canonical bound-state engine; waves slow at the saturation core and localize into stable breathing solitons.

## Validation: v14 Mode I PASS (doc 113)

The Master Equation FDTD engine produces a stable breathing bound state at the Vol 1 Ch 8 Golden Torus geometry with:
- **4/4 strict on the breathing-soliton criterion** ($V_{\text{peak}}$ mean > 0.2; FWHM stable; $n(r)$ gradient measurable; long-term stability)
- Shell $\Gamma \approx -1$ TIR (total internal reflection) structure
- Saturation-onset amplitude (peak $|\omega| \approx 0.3\pi$)

The K4-TLM engine at the same geometry showed Mode III on the bound-state criterion — wave propagation without localization, exactly as the engine-architecture analysis predicted.

## What was superseded

The pre-2026-05-14 framework attempted to use K4-TLM as the universal engine, including bound-state simulations. The "Mode III at Vol 1 Ch 8 Golden Torus" result was originally framed as a framework failure; per doc 113 §3.2, it is instead an **engine-architecture mismatch** — K4-TLM is the wrong tool for bound-state work, not a failed validation of the framework.

This is a meta-lesson recorded in the corpus: empirical results need engine-architecture context. The Vol 1 Ch 8 α derivation, the Vol 2 Ch 6 electroweak derivations, and the Vol 3 Ch 4 cosmology framing all rest on substrate physics that requires the bound-state regime; Master Equation FDTD is the canonical engine for verifying them computationally.

## Implications for simulation workstreams

| Workstream | Engine | Rationale |
|---|---|---|
| Bench / sub-saturation linear validation (IM3, IP3, etc.) | K4-TLM | $A \ll 1$ regime |
| IVIM bench tree-level discrimination | K4-TLM | Linear bench regime |
| Bound-state soliton verification (electron, baryon, breathing) | Master Equation FDTD | $A \to 1$ regime; localization required |
| Pair production (Schwinger, autoresonant) | Master Equation FDTD | $A \to 1$ kernel boundary crossing |
| Cosserat field-component simulations | `cosserat_field_3d.py` (validated standalone) | Mode-specific factor-of-4 mass-gap |

## Status

**Canonical (closed).** A-027 entry in L5 axiom_derivation_status; doc 113 §3.2 architectural statement; v14 Mode I PASS empirical validation. Future bound-state simulations should use Master Equation FDTD by default; K4-TLM for sub-saturation bench-style work. Cross-references that mention "K4-TLM bound-state" need to be updated to reference Master Equation FDTD.

## Cross-references

- **Canonical engine implementations:**
  - `src/ave/core/k4_tlm.py` — K4-TLM canonical engine (sub-saturation)
  - `src/ave/core/master_equation_fdtd.py` — Master Equation FDTD canonical engine (bound-state)
  - `src/ave/topological/cosserat_field_3d.py` — Cosserat field implementation (validated standalone, factor-of-4 mass gap)
- **Canonical manuscript anchors:**
  - Common Foreword §"The Synthesis: The Unifying Master Equation" — Master Equation as the dielectric specialization of Axiom 4's universal saturation kernel
  - [Backmatter Ch 4 Physics Engine Architecture](../../backmatter/04_physics_engine_architecture.tex) — engine architecture canonical
- **Related KB leafs:**
  - [Q-G47 Substrate-Scale Cosserat Closure](q-g47-substrate-scale-cosserat-closure.md) — Cosserat substrate-scale work uses cosserat_field_3d.py
  - [Solver Toolchain](solver-toolchain.md) — universal regime-boundary eigenvalue method (engine-agnostic)
  - [Mathematical Closure](mathematical-closure.md) — DAG proof + engine cross-references
