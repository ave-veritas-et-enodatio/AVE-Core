# DERIVATION — X36: the series-anti-resonant node-shunt FORM, and why the ceiling = the installed anchor (a characterization, not a first-principles pin)

**Date:** 2026-07-09 · **Branch:** `analysis/x36-node-bottleneck` · Companion to the
[prereg](2026-07-09_x36-node-bottleneck_prereg_FROZEN.md) and [result](2026-07-09_x36-node-bottleneck_result.md).

> **⚠ DEMOTION (2026-07-09, post PR #613 adversarial review, 17/17 CONFIRMED).** This note was written to derive
> "WHY the node tank PINS at ω_C from first principles". That framing is **withdrawn**. What is actually derived is
> the reciprocal **FORM** `1/ω² = 1/Λ + 1/ω_C²` **conditional on a series anti-resonant (mass-in-mass) topology**
> — the standard locally-resonant-metamaterial anti-resonance law. It is **NOT forced** by shunt KCL + losslessness:
> the prereg itself (`prereg_FROZEN.md:85`) lists an equally passive/lossless/KCL-consistent **parallel-LC
> band-pass** shunt that does the opposite (transparent at ω_C → Branch L). The topology choice, the η=1 partition,
> and the anchor frequency are **un-derived modelling inputs**, and the ceiling equals **whatever anchor is
> installed** (result §2 placement probe). Read this note as a characterization of the chosen model; the demoted
> sentences are marked inline. Superseded verdict sentences are preserved in the result doc's correction banner
> (KEEP-BOTH).

This note gives the node-tank dispersion law **for the series-anti-resonant topology** and shows algebraically that,
**given that topology, η=1, and an anchor at ω_C**, the ceiling sits at ω_C for every channel. Every step is verified
numerically by the driver
([`x36_node_bottleneck.py`](../src/scripts/vol_1_foundations/x36_node_bottleneck.py), gates G1–G6; note G2/G6 are
self-comparisons repaired in COMMIT 2).

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

~~The √(shunt) normalization and the mass-in-mass topology are **forced** by shunt KCL + losslessness~~ **[DEMOTED,
CRITICAL-1] — the mass-in-mass (series anti-resonant) topology is a modelling CHOICE, not forced.** Shunt KCL +
losslessness are satisfied *equally* by a **parallel-LC band-pass** shunt (`prereg_FROZEN.md:85`), which is
transparent at ω_C and does NOT pin (→ Branch L). The series-notch form below is therefore local to that choice; it
is the P-vs-L selector, not a consequence. Given the series-notch topology, the coupled dispersion is, per
D-eigenvalue λ_b(k) (the isotropic tank commutes with D, so
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

## 6. The node-tank ceiling vs the walk — the tension REDUCES to the un-derived anchor (prereg §6, surface to Grant)

At anchor ω_C the node-tank ceiling and the bond-tick walk ceiling differ by π√3:

| clock | mechanism | ceiling | in MeV |
|---|---|---|---|
| **node tank** (X36, anchored at ω_C) | series notch at the INSTALLED anchor | ~1 ω_C | 0.511 (= the anchor identity, calib-in/calib-out) |
| **bond tick** (X33 walk) | one bond per tick, Nyquist π·ω_link | π√3 ω_C | 2.781 |

The laws differ (rational (3) vs ω_link·arccos), so the band **shape** differs. But ~~the node tank is TIGHTER by
π√3 … the vector band tops at the node rate m_e c², in TENSION with #604~~ **[DEMOTED, CRITICAL-2]** — the ceiling is
NOT a derived rate: the placement probe (result §2) shows a tank anchored at **π√3·ω_C reproduces the walk's ceiling
(5.428 ≈ 5.441)**. So the "which clock binds" question is the **un-derived choice of anchor/topology**, not a physical
contradiction between the #604 memoryless-node engine and X36. The two engines install **different node models**;
their ceilings are not directly comparable. Surfaced to Grant as the 3-axis question (result §6), **not** a
cross-engine conflict. ℏω_C ≡ m_e c² is a calibration identity (`OMEGA_C`), so a ceiling landing at ω_C is
calibration-in, calibration-out — not an emergence-class prediction.

## 7. Consequence: the D-I discriminator is NOT resolved — the fork is SHARPENED (demoted from "Branch P")

~~The channel-shared node tank derives effective synchrony … the bond-tick walk is the discrete-tick shadow of the
continuous node-tank bottleneck … the X33 in-engine-undecidable fork collapses under the Axiom-1 η=1 node.~~
**[DEMOTED, MAJOR-4 / MAJOR-14/15].** The "discrete-tick shadow" narrative is **contradicted by the branch's own**
`reproduces_walk = False` (ratio 0.182 at anchor ω_C) — the node tank does not reproduce the walk unless it is
*installed* at π√3·ω_C. And the fork does **not collapse**: X36 shows the continuous engine returns whatever node
model is installed (topology × η × anchor), so — **contra MAJOR-14/15** — it does **not** decide the fork and Axiom 1
does **not** fix the three load-bearing choices (channel-shared single scalar shunt, tank-freq = ω_C, η = 1). X33's
in-engine-undecidable ruling **STANDS and is REINFORCED**. The genuine output is the **3-axis question** (result §6):
node-shunt topology (series-notch vs parallel-band-pass) × η partition × anchor frequency — **PENDING-GRANT-WALK.**
What survives as derived content is the anti-resonance **FORM** `1/ω² = 1/Λ + 1/ω_C²` conditional on the series
topology (a standard locally-resonant-metamaterial law), the placement probe, and the η-singularity map.
