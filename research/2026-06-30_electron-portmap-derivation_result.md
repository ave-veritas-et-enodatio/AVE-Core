# RESULT — Electron Port-Coupling Network: does a self-braced standing electron BIND?

**Date:** 2026-06-30 · **Lane:** implementer · **Branch:** `analysis/electron-portmap-derivation`
(worktree `/private/tmp/electron-portmap`, off `origin/main` @ `778823e9`).
**Prereg (frozen FIRST):** [`2026-06-30_electron-portmap-derivation_prereg_FROZEN.md`](2026-06-30_electron-portmap-derivation_prereg_FROZEN.md)
(frozen commit `a6c03c72`). Adjudication criteria §5 followed exactly; none dropped (Rule 11).
**Type:** DERIVATION / ANALYSIS. **NO simulation.** Self-consistency of the symbolic chain only.
**Class (consistency-vs-emergence):** **C — CONSISTENCY** throughout (the mechanism, if it binds,
is a FORM-chord peer-with-SM; the SIZE is a scale tied to imported `L_NODE`; `R·r=¼` is a Class-B
input; α appears only through the flagged echo channels). NOT Class-D emergence.

---

## 0. HEADLINE (the four deliverable answers, one line each)

> **INWARD-LEG SIGN: COMPRESSIVE (inward).** The rectified time-average of the μ→A1 back-reaction
> lowers the effective bulk compliance stiffness at the amplitude peak (`C_eff=C_0/S` softens, the
> ponderomotive index `n_grav=S^(−1/2)` rises), and the self-consistent index gradient lenses the
> envelope into itself. `⟨F_A1⟩` is inward. (V1 holds.) **DERIVED, not assumed** — see §2, incl.
> the honest caveat that the SAME `S→0` limit makes the varactor a runaway (positive feedback),
> which is exactly why a brace is REQUIRED and why its steepness is the whole question.
>
> **BRACE: the winding DC-circulation angular-momentum reactive pressure `∝ L_w²/(m r³)`, backstopped
> by the topological ropelength hard-wall at `r → r_floor ~ (1/2π)·(perimeter floor)`.** Candidate (c)
> saturation-stiffening is NOT an independent brace — it is the SAME `S→0` that drives the pull
> (it cannot both pull and brace at the same sign). Candidate (a) IS present (the (2,3) winding
> carries a nonzero DC circulation `L_w`, and centrifugal-reactive pressure scales `r^{−3}`, steeper
> than the pull). Candidate (b) is a HARD floor, not a smooth brace. **Derived which is present: (a)
> smooth + (b) hard-wall; (c) disqualified as a brace.**
>
> **EQUILIBRIUM: `r* ~ L_NODE` (Compton scale) — order-consistent, NOT independently derived.**
> The `r^{−3}` brace vs the pull crosses at a scale set by `L_w` and the envelope stiffness; both
> are tied to the imported `L_NODE=ℏ/(m_e c)` and the `R·r=¼` Class-B input. Scale-consistent (V5),
> but this is calibration-consistency, NOT a derivation of the size.
>
> **STABILITY VERDICT: see §5 — and it is NOT a clean pass.** The `r^{−3}` centrifugal brace vs a
> `~r^{−1}`-or-shallower ponderomotive pull WOULD give a stable well (`dF_net/dr>0`) — BUT the
> saturation varactor introduces a competing positive-feedback branch (the `S→0` runaway) whose
> `r`-derivative can overwhelm the brace in the deep-saturation core. The honest reading is a
> **CONDITIONAL / FORK verdict**, stated precisely in §5.

**One-paragraph plain reading.** The electron picture DOES assemble as a real reactive port network
with a genuine inward pull and a genuine reactive (lossless) outward brace — so it is NOT an
immediate NO (the naive "there's no brace at all → implosion" failure does not occur; a brace IS
present, and it is reactive, not the forbidden dissipative crutch). BUT the same nonlinearity that
supplies the pull (the `S→0` varactor runaway) is a positive feedback whose steepness competes with
the brace's steepness, and at the symbolic level the winner depends on an un-adjudicated
grade/exponent input. So the deliverable is a **self-braced network that binds IF the centrifugal
`r^{−3}` brace out-steepens the saturation runaway at the core** — a condition that is plausible but
NOT closed symbolically, and that must be decided by the greenlit sim measuring the two `r`-slopes.
This is reported as **FORK-FOR-GRANT / CONDITIONAL-BIND**, not a manufactured PASS.

---

## 1. THE PORT NETWORK (reuse the 3-channel graded-impedance structure; pose the STABILITY question)

### 1.1 Ports (native Cosserat, NOT Cartesian)

Reusing the canonical three-channel graded-vacuum-impedance network
(`resonant-lc-solitons.md`:120–124; the coupled-eigensolve H-structure,
`coupled_eigensolve.py`), with the ROLE labels the engine-reroute Resultbox fixed:

| Port | Sector | Reactance kind | Impedance | Bias rail | State variable(s) | Role |
|---|---|---|---|---|---|---|
| **P_A1** | A1 dilatation = MASS envelope | **Capacitive** (varactor `C_eff=C_0/S`) | `Z_bulk=ρc_bulk` | `A→1` (`V_snap` core) | strain `A=|V|/V_yield`; conjugate momentum `π_V` | the compressive mass "3" |
| **P_μ (DC)** | Cosserat (2,3) winding = CHARGE | **Inductive**, static circulation | `Z_shear=ρc_shear` | `V_yield` self-trap | `Link(∂Ω,F)=−1`; DC circulation `L_w` | static topological charge boundary (no real power) |
| **P_μ (AC)** | Cosserat (2,3) winding = the ringing | **Inductive**, oscillating | `Z_shear` | — | `b_ω` amplitude; `ω_dot` (the L-state) | the AC circulation that gets RECTIFIED |
| **P_Γ** | Γ=−1 wall = TERMINATION | reflective (Op17-bounded BC) | `Z_core=Z_0√S→0` | at the `S→0` shell | `Γ = (Z_core−Z_0)/(Z_core+Z_0) → −1` | the self-woven perfect mirror |
| **P_EM** | radiative carrier port | matched, `Z_0` | `Z_0=376.7Ω` | — | far-field coupling | the α-leak CARRIER (NOT in the binding loop; work-exchanging) |
| **P_ε** | T2 transverse permittivity | capacitive `ε_eff=ε_0 S` | `Z_wave=√(μ/ε)→∞` | rupture read | transverse polarization | enters ONLY as the wall's dual (sign-selector), see §1.4 |

**Sector-ownership discipline (memory: A1⊥T2 cross-wiring watch).** Mass = A1 (P_A1). Charge =
Cosserat winding (P_μ). μ-sign = the wall's chirality selector. These are NEVER cross-wired. The
binding loop we analyze is **P_A1 ↔ P_μ(AC/DC), terminated by P_Γ**. P_EM is the radiative carrier
(work-exchanging, α-leak) — it sits OUTSIDE the reactive binding loop and is the reason the electron
has a finite loaded Q but does NOT decay (`resonant-lc-solitons.md`:92,100–104). P_ε is the wall's
capacitive-vs-inductive dual (wall-fork H3, `resonant-lc-solitons.md`:108); it is a SIGN selector,
not an independent binding DOF.

### 1.2 The couplings (the graph edges)

```
                          P_EM (Z_0, radiative CARRIER — OUTSIDE the binding loop, α-leak)
                            :  (loaded-Q coupling only; no net binding force)
                            :
   ┌─────────────────────── P_Γ (Γ=−1 wall) ───────────────────────┐
   │  reflective BC: Z_core=Z_0√S → 0 as A→1 (self-woven mirror)    │
   │                                                                │
   │   ┌──────────────┐   κ_couple = S(A)-front-gated   ┌────────┐  │
   │   │   P_A1        │◄───────── mutual  ────────────►│  P_μ    │  │
   │   │ MASS envelope │   (varactor C_eff=C_0/S;        │ CHARGE  │  │
   │   │  capacitive   │    ponderomotive n_grav=S^-1/2) │inductive│  │
   │   │  C_eff=C_0/S  │                                 │ DC: L_w │  │
   │   └──────────────┘                                 │ AC: b_ω │  │
   │          ▲                                          └────────┘  │
   │          │ rectified DC compression (§2)  centrifugal r^-3 (§3) │
   └──────────┴─────────────────────────────────────────────────────┘
```

Two coupling edges carry the binding physics:

1. **μ(AC) → A1 back-reaction (the INWARD leg, §2).** The AC winding circulation, run through the
   saturation nonlinearity, has a nonzero DC time-average that acts on the A1 envelope. Coupling is
   the S(A)-front-gated mutual term (the `coupled_cage_winding` front gate; `κ_chiral=α·κ̃(2,3)`,
   `research/2026-06-09_...:52`). This is a **ponderomotive / parametric** coupling — the fast AC
   drives a slow DC envelope force.
2. **A1 → μ(DC) reaction (the BRACE leg, §3).** Compressing the A1 envelope (shrinking `r`) forces
   the DC circulation `L_w` into a smaller loop; conservation of the winding integer + circulation
   raises the reactive centrifugal pressure `∝ L_w²/(m r³)`. This is the outward push.

### 1.3 Losslessness — CONFIRMED via Tellegen (not asserted)

**Tellegen's theorem:** for ANY network obeying Kirchhoff's laws (KCL at nodes, KVL around loops),
`Σ_branches V_k · I_k* = 0` — a topological identity independent of the branch constitutive laws.
Split into real + imaginary: the real part is `Σ Re(V_k I_k*) = total dissipated power`.

Every branch in the binding loop (P_A1, P_μ-DC, P_μ-AC, P_Γ) is a **purely reactive** element:
- P_A1: `C_eff=C_0/S` — an ideal (lossless) nonlinear capacitor. `Z = 1/(jωC_eff)` is purely
  imaginary.
- P_μ: `Z_shear=ρc_shear` mechanical reactance; the DC circulation is a persistent current in a
  lossless inductor; the (2,3) `Link` is a STATIC topological constraint carrying NO real power
  (`resonant-lc-solitons.md`:124, "lossless-REACTIVE constraint carrying no real power").
- P_Γ: `Γ=−1` is a UNIT-modulus reflection — `|Γ|²=1`, zero power transmitted across the wall
  (`resonant-lc-solitons.md`:52, "100% ... reflects internally").

With every binding-loop branch impedance purely imaginary, `Re(V_k I_k*) = 0` for each, so
`Σ Re(V_k I_k*) = 0` — **the network dissipates zero real power.** Losslessness FALLS OUT of the
all-reactive port assignment via Tellegen; it is not an added assumption. **This is the guard that
disqualifies the #83 artifact:** the retracted "stable loop" bought its localization with a
viscosity term `e^{−η dt M}`, which is a REAL-part (dissipative) branch — it would show up as
`Σ Re(V_k I_k*) = −η·(…) ≠ 0`, violating Tellegen for a lossless substrate (Axiom 3). Our binding
loop has NO such branch: the ONLY real-power port is P_EM, and P_EM is explicitly OUTSIDE the binding
loop (it is the radiative carrier / loaded-Q coupling, not a binding force). **Losslessness of the
binding loop: CONFIRMED. (V4 holds.)**
