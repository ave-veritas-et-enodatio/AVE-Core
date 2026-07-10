# DERIVATION — X36: why the shared node LC tank PINS every channel at the node rate (and why it is TIGHTER than the walk)

**Date:** 2026-07-09 · **Branch:** `analysis/x36-node-bottleneck` · Companion to the
[prereg](2026-07-09_x36-node-bottleneck_prereg_FROZEN.md) and [result](2026-07-09_x36-node-bottleneck_result.md).

This note derives the node-tank dispersion law from the junction physics (NOT tuned) and shows algebraically WHY the
channel-shared shunt tank pins the ceiling at the node resonance ω_C for every channel — the D-I discriminator's
Branch P. Every step is verified numerically by the driver
([`x36_node_bottleneck.py`](../src/scripts/vol_1_foundations/x36_node_bottleneck.py), gates G1–G6).

---

## 1. The node tank, from shunt KCL + losslessness (NOT assumed)

Axiom 1's node is an **intrinsic LC oscillator** — a shunt resonator across the channel junction, resonance
ω_C = c₀/ℓ_node (`OMEGA_C`; `CLAUDE.md:70`, `translation-circuit.md:97`). The 6 DOF/node are 3 translational (E →
**capacitive** store) + 3 microrotational (B → **inductive** flywheel); the node's translational response IS the tank
capacitance. Because **every channel transacts through the same node hardware** (a channel-shared shunt admittance),
the tank presents each of the D translational channels the SAME scalar reactive load — an isotropic reactance × I_D.

The bond network is the X33 continuum dynamical matrix D(k) (rank-2 bond tensors Φ_b = k_a d̂⊗d̂ + k_s(I−d̂⊗d̂)); the
node's total low-frequency inertia m is fixed by the X33 acoustic velocities. A **passive, lossless** shunt resonator
that (a) preserves rigid translation (no on-site restoring force at k=0 ⇒ acoustic branch survives) and (b)
resonates at ω_C is a mass-in-mass store: a fraction η of the node inertia (μ_tank = η m) coupled through a
reactance γ_tank = μ_tank ω_C² to the bond-attached host (m_h = (1−η)m). Eliminating the internal coordinate gives
the **frequency-dependent effective dynamical mass** the bonds see:

    m_eff(ω) = (1−η)·m  +  η·m·ω_C² / (ω_C² − ω²).                                              (1)

The √(shunt) normalization and the mass-in-mass topology are **forced** by shunt KCL + losslessness — they are not a
convenient choice (same logic as the X33 coin's forced √Y symmetrization, applied now to the node reactance instead
of the bond scatter). The coupled dispersion is, per D-eigenvalue λ_b(k) (the isotropic tank commutes with D, so
D's eigenvectors are unchanged — verified by the G4 band count and the literal augmented (u,q) eigensolve):

    eig(D(k)) = ω² · m_eff(ω).                                                                  (2)

**η = 1 is the Axiom-1-pure reading** ("the node IS the tank": the translational storage is entirely the tank
capacitance, no bond-rigid bypass inertia). Alternatives are flagged (prereg §2a): η < 1 (a bypass ⇒ Branch M), a
parallel-LC band-pass shunt (⇒ Branch L), and the microphysical Cosserat translational-C ⊗ rotational-L tank (the
deep model, of which (1) is the translational-sector reduction).

## 2. The pin locus — the reciprocal bottleneck law (η = 1, driver verdict + G2)

At η = 1, m_h = 0, m_eff(ω) = m ω_C²/(ω_C² − ω²), and (2) with m absorbed into the ω_C-unit continuum eigenvalue
Λ_b = (R·√λ_b)² (R = √2 the fixed elastic→ω_C conversion) collapses to

    **1/ω²(k)  =  1/Λ_b(k)  +  1/ω_C².**                                                        (3)

This is the **series-reactance / bottleneck law**: the node tank and the bond network act like two reactances IN
SERIES limiting the frequency; **the SLOWER of {bond network, node tank} binds.** Consequences (all confirmed
numerically):

- **λ_b → ∞ (stiff channel, any ρ*):** ω → ω_C. The stiff channel's would-be high band is capped at the node rate.
  **The stiffness is locked OUT of the ceiling** — exactly as the coin's ±1 eigenvalues locked it out in X33, now via
  the node reactance rather than the bond scatter.
- Driver: node-tank top(ρ*) = **0.9608 → 0.9921 → 0.9992 → 0.99992 ω_C** for ρ* ∈ {1, 9.77, 100, 1000}, **lift ratio
  1.041×** (Branch P: < 1.3). The ceiling **converges to ω_C = 1 exactly** (= m_e c² = 0.511 MeV) as ρ* → ∞.

## 3. The tank DECOUPLES at ω→0 — acoustic velocity unchanged (driver G1)

At low k, Λ_b → 0, so 1/ω² = 1/Λ_b + 1/ω_C² ≈ 1/Λ_b ⇒ ω → √Λ_b, **independent of ω_C**. The node tank contributes
nothing at DC (the m_h = 0, μ_tank co-moving store rides rigidly ⇒ m_eff(0) = m). The acoustic velocities are the
X33 velocities (G1: node-tank/bare-continuum low-k slope ratio = 1 to 5.7e-9). This is why a solver that only checks
long-wave velocities cannot see the tank — the pin-vs-lift split is a **zone-EDGE** phenomenon, exactly as the X33
walk-vs-continuum split was.

## 4. The tank-removed control recovers X33's lifting continuum (driver G2)

ω_C → ∞ ⇒ 1/ω² = 1/Λ_b ⇒ ω = √Λ_b = the bare X33 continuum. Driver G2: the ω_C→∞ node-tank top equals the bare
continuum top to 0.0e+00 relative error, lift ratio 22.4× — X33's LIFTING continuum recovered exactly (the honest
control: the effect is the tank, not a broken pipeline).

## 5. The η < 1 gap structure — a D-INDEPENDENT node stop-band (driver G6)

For 0 < η < 1, (1)+(2) give a quadratic per λ_b: `(1−η) x² − (ω_C² + Λ_b) x + Λ_b ω_C² = 0`, x = ω² ⇒ TWO branches:

- **lower (pinned):** top → ω_C as Λ_b → ∞ (the shared acoustic manifold, capped at the node rate),
- **upper (lifting):** bottom = ω_C/√(1−η) at Λ_b → 0; top ≈ √(Λ_b,max/(1−η)) LIFTS with ρ* (the stiff channel
  pokes through),
- **node-resonance stop-band [ω_C, ω_C/√(1−η)]** — **D-INDEPENDENT** (a pure node property; driver G6:
  edge_err < 1e-6, D-independence to two Λ differing 1000× < 1e-6). This is a **new spectral feature** (prereg §3).

At η → 1 the gap top → ∞ (no upper branch, single pinned manifold — Branch P); at η → 0 the gap closes and the
single band lifts (Branch L / bare continuum). **η is the physical fork parameter** (M-family interpolating P↔L).

## 6. Why the node tank does NOT reproduce the walk — and the #604 tension (prereg §6, surface to Grant)

Both the node tank and the X33 bond-tick walk **PIN**, but by DIFFERENT mechanisms and at DIFFERENT ceilings:

| clock | mechanism | ceiling | in MeV |
|---|---|---|---|
| **node tank** (X36) | node LC resonance ω_C = c₀/ℓ_node | **~1 ω_C** (= m_e c²) | **0.511** |
| **bond tick** (X33 walk) | one bond per tick, Nyquist π·ω_link | **π√3 ω_C** | **2.781** |

The laws differ (rational (3) vs ω_link·arccos), so even the band **shape** differs — the node tank is **NOT** the
walk. And the node tank is **TIGHTER by π√3** (the node resonance sits a factor π√3 below the per-bond Nyquist,
because ω_C = c₀/ℓ_node while ω_link = √3 ω_C and the tick adds another π). **Flag (Grant adjudication, do not
silently reconcile):** IF the node tank is a series bottleneck at ω_C, the vector band tops at the **node rate m_e
c²**, BELOW and in **TENSION** with #604's time-stepped bond-tick top π√3 ω_C = 2.78 MeV — because the #604
scatter+connect engine uses a **memoryless node** (a frequency-independent Householder coin, no LC tank) and thus
OMITS the tank, over-reading the ceiling by π√3. Which clock binds — node-tank (tighter, ~1 ω_C) or bond-tick (#604,
π√3 ω_C) — is the plumber question of prereg §1, surfaced to Grant.

## 7. Consequence: the D-I discriminator resolves to Branch P

The channel-shared node tank **derives effective synchrony** from Axiom-1's node resonance with **NO tick
postulate**: the continuous (Hamiltonian, tickless) network WITH explicit node tanks pins the coupled ceiling at the
node rate for every channel (Λ_b → ∞ ⇒ ω → ω_C ∀ b). Axiom-1's continuous LC language and the walk map's operational
success are reconciled — **the bond-tick walk is the discrete-tick shadow of the continuous node-tank bottleneck**;
both pin, and the node tank is the binding (tighter) clock. The X33 in-engine-undecidable fork **collapses under the
Axiom-1 η=1 node**, replaced by a sharper, corpus-anchorable question: does the node tank resonate at the base node
rate ω_C (Branch P at m_e c², §6 tension with #604) or the bond-tick rate π√3 ω_C (reproduces the walk)?
