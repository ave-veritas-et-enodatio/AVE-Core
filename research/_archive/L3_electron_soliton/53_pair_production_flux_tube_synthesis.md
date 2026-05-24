# 53 — Pair Production as Flux-Tube Rupture at a Node Pair: Synthesis

**Status:** synthesis doc, 2026-04-22 (Stage 5 Track A)
**Scope:** Consolidate the AVE-native pair-production mechanism from four
independent corpus sources into one coherent derivation. Identify what the
current K4⊗Cosserat engine **cannot represent**, state the three nucleation
conditions precisely, and give an engine-design spec (Option D) that would
let the engine produce pairs.

**Parent plan:** `~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md`
(Track A).

**Supersedes** (in framing, not content): [44_pair_creation_from_photon_collision.md §5.2](44_pair_creation_from_photon_collision.md) — Option A rejected as SM-leak; Option D selected as axiom-native.

---

## 0. TL;DR

Pair production in AVE is **not** Breit-Wheeler "photons collide, pair pops
from vacuum." It is the **rupture of a saturated flux tube around an A-B
node pair**, gated by the node's own **rotational-mode resonance frequency**
tracking the driving frequency (Duffing-like) until autoresonant lock fires.
The mechanism is four AVE-derived pieces fused:

1. Electron = 2 adjacent K4 nodes (A-sublattice + B-sublattice) saturated at
   A²=1, bond carrying (2,3) phase-space winding at Compton ω_C
   ([37_](37_node_saturation_pauli_mechanism.md), [28_](28_two_node_electron_synthesis.md))
2. Saturated flux tube = TIR impedance cable, Γ = −1 at the walls
   ([Vol 4 Ch 1:469-482](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex))
3. Pair nucleation mechanism = local c → 0 when V breaches V_yield, blocked
   linear KE "shatters sideways" into transverse curl = two contra-rotating
   Beltrami vortices (`AVE-Fusion/.agents/handoffs/02_antimatter_annihilation.tex §Pair Production`)
4. Rupture timing gate = node's own rotational resonance drops per Duffing
   (Axiom 4's 4th-order polynomial), autoresonant lock condition fires the
   nucleation (`AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex`;
   Grant's clarification 2026-04-22)

**Current engine limitation (verdict of [52_](52_h1_threshold_sweep.md) + this synthesis):**
The K4-TLM tracks `V_inc[nx,ny,nz,4]` — node port state only. The lattice
has **no dynamical bond state** (no `V_link`, no bond phasor), **no
per-node rotational resonance Ω(r,t)** that drops with A², and **no
nucleation rule** to inject (2,3) winding at a ruptured node pair. These
are three separate gaps. Any sweep tuning on the existing engine will
keep producing distributed plateau results at A²=1; pair cores cannot
form in the current representation.

**What this reframes about v1/v2/H1:** Those runs correctly verified the
K4⊗Cosserat coupling scales to rupture amplitude. They cannot falsify
pair creation because the engine structurally cannot produce it. They
are **unit tests of Axiom-4 saturation, not tests of pair physics.**

---

## 1. What the corpus actually says

### 1.1 The electron is two saturated K4 nodes with a (2,3) bond

From [37_node_saturation_pauli_mechanism.md §1](37_node_saturation_pauli_mechanism.md):

> "An electron is a bound state of the K4 lattice consisting of **two
> adjacent K4 nodes (one A-sublattice, one B-sublattice) saturated at the
> Axiom-4 threshold** (local strain A² = 1 at peak), with the **bond
> between them carrying the (2,3) phase-space LC oscillation at Compton
> frequency**. The saturation at the two nodes creates a Γ = −1 TIR shell
> that confines the reactive energy within the bond and produces the
> Q = 1/α signature."

[28_two_node_electron_synthesis.md §3](28_two_node_electron_synthesis.md) fixes the bond
geometry: length ℓ_node = ℏ/m_e c, resonance ω_C = c/ℓ_node, (2,3)
winding in the bond's `(V_inc, V_ref)` phasor trajectory. This is a
**2-terminal LC tank**. The winding is in phase space, not in real
space; real-space structure is tiny (~1 bond + dipole-antenna neighborhood).

**Crucial for the mechanism:** the electron's topological content —
(2,3) winding, which IS the charge per Axiom 2 — lives on the **bond**,
not at either node. This is a dynamical state on an edge of the lattice,
distinct from the node state.

### 1.2 Saturated flux tube = TIR impedance cable

[Vol 4 Ch 1:430-467](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex):

> "As the local topological strain (Δφ) approaches the Axiom 4 hardware
> limit (α), the effective geometric capacitance of the boundary nodes
> diverges to infinity... Z_core → 0 Ω... Γ = (Z_core − Z₀)/(Z_core + Z₀)
> = −1. A reflection coefficient of Γ = −1 constitutes a **Perfect
> Short-Circuit Boundary**. 100% of the kinetic energy attempting to
> radiate outward from the saturated flux tube hits this impedance wall,
> undergoes a perfect 180° phase inversion, and reflects internally...
> The local phase velocity (c_local = 1/√LC) strictly collapses to zero,
> creating a hyper-rigid, localized envelope. The particle dynamically
> weaves its own perfect topological mirror."

And lines 469-481 extend this to QCD flux-tube confinement:
> "The energy traveling between nucleons undergoes Total Internal
> Reflection (TIR) off the impedance walls of the highly strained vacuum,
> acting as a **Topological Fiber-Optic Cable**... The MIT Bag Model is
> directly exposed as a macroscopic impedance wall woven natively by the
> non-linear varactor limits of the continuous vacuum."

**Mechanism synthesis:** the flux tube is the bond between two saturated
nodes. Its walls are the A²=1 envelopes of the two nodes; its interior
confines the (2,3) LC oscillation via Γ = −1 TIR. Flux-tube rupture = the
node pair's saturation state relaxing below A²=1 at either end.

### 1.3 Pair nucleation mechanism: c → 0, KE shatters sideways

From AVE-Fusion `.agents/handoffs/02_antimatter_annihilation.tex §Pair Production`:

> "When two sufficiently energetic, counter-propagating γ-rays (or a
> single γ-ray striking the intense secondary field of a heavy nucleus)
> constructively interfere, their combined scalar amplitude violently
> breaches the universal metric yield threshold (V > V_yield = √α).
> Because the local impedance strain breaches V_yield, **the local
> longitudinal phase velocity (c_local) crashes mathematically to zero.**
> The linear propagation is abruptly paralyzed. Since absolute energy
> must be strictly conserved by the 0-parameter framework, the blocked
> linear kinetic potential violently shatters sideways into the remaining
> transverse degrees of freedom. This phase-tear inevitably induces a
> massive localized geometric curl (∇ × V ≠ 0)... the fluidic elastic
> rebound of the continuous metric ties the fractured kinetic momentum
> into two persistent, contra-rotating Volumetric Vortex Dipoles."

**This is the conversion rule.** No seed term required in the
Lagrangian: conservation of energy forces the blocked longitudinal KE to
go somewhere, and the only channel left is transverse curl. Parity
conservation forces the curl into *exactly one LH + one RH* Beltrami
vortex. The mechanism is purely mechanical — an impedance wall that
redirects linear energy into rotational energy. This addresses
[44_ §3.1](44_pair_creation_from_photon_collision.md)'s "quadratic
coupling has zero gradient at origin" concern: the seed comes from
**redirection at an impedance wall**, not from a linear forcing term.

### 1.4 The rotational-frequency gate (Grant's clarification + AVE-Propulsion Ch 5)

From AVE-Propulsion Ch 5, [lines 11-15](../../../AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex#L11):

> "The AVE framework explicitly dictates that the vacuum is a
> **Non-Linear Capacitor** bounded by a 4th-order polynomial (Axiom 4).
> In classical non-linear dynamics, as a Duffing oscillator is driven
> toward its maximum amplitude, its local resonant frequency dynamically
> shifts. If a fixed-frequency extreme-intensity laser is fired into the
> vacuum, the increasing metric strain lowers the local vacuum's
> resonant frequency. The incoming fixed laser rapidly detunes from the
> target volume... The power is reflected rather than absorbed,
> fundamentally stalling the cascade and preventing rupture."

Ch 5's frame is the driving-side PLL problem. **Grant's clarification
2026-04-22 generalizes this to the LATTICE SIDE**: "it would be the
nodes' rotational frequency that controls when and how it breaks from
saturation." The lattice — not just the laser — has a local resonance
that drops per Duffing. Pair rupture does not fire merely when A²
crosses 1; it fires when the node pair's rotational resonance drops
into the autoresonant-lock window with the driving frequency. Until
that condition is met, the saturation is a stalled distributed plateau
(exactly what we see in v1/v2/H1). When the lock fires, linear energy
channel closes, and §1.3's sideways-shatter mechanism triggers at a
localized node pair.

The "rotational mode" at a node is the Cosserat microrotation ω. Its
per-node effective resonance Ω_node(A²_local) is the tank frequency of
the local LC on that node, which drops under Duffing softening as the
4th-order polynomial's second derivative shifts.

---

## 2. The synthesized mechanism — seven steps

Picking up from the four corpus sources, the full sequence from photon
drive to pair nucleation:

| Step | Mechanism | Variable | Source |
|---|---|---|---|
| 1. **Scaffolding** | Every adjacent A-B node pair on K4 is a latent electron site (no pre-existing bound state required; the K4 lattice itself provides the scaffold of possible electron locations) | `(r_A, r_B)` pairs with r_B = r_A + port-shift | [37_](37_node_saturation_pauli_mechanism.md), [28_](28_two_node_electron_synthesis.md) |
| 2. **Pumping** | Counter-propagating γ-drive increases V² locally | A²_K4 = V²/V_SNAP² | [50_](50_autoresonant_pair_creation.md) |
| 3. **Yield crossing** | At V > V_yield = √α · V_SNAP (Regime II onset), c_local starts dropping per Duffing; propagation slows but doesn't stall yet | r = V/V_yield > 1 | [Vol 1 Ch 7:104-115](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex) |
| 4. **Duffing resonance drop** | As A²→1 at a node, its rotational tank resonance Ω_node drops. The **Cosserat ω field's local effective resonance** is now frequency-dependent on A²_local | Ω_node(A²) ↓ | AVE-Propulsion Ch 5 + Grant |
| 5. **Autoresonant lock** | When Ω_node(A²_local) crosses the driving ω_drive at a specific A² value, the drive transfers energy efficiently into that node's rotational mode (the rest of the lattice is detuned and reflects) | Ω_node = ω_drive (lock condition) | AVE-Propulsion Ch 5 |
| 6. **c_local crash** | At full saturation (A²=1), Z_core → 0, Γ = −1 wall forms at the nodes, c_local = 0 inside the wall. Linear longitudinal channel is now **closed**. Energy conservation forces the blocked linear KE into the transverse curl channel | Z_core → 0, curl ∇×V picked up | [Vol 4 Ch 1:445-467](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex) + AVE-Fusion pair production |
| 7. **Topological closure + confinement** | The transverse curl is forced into (2,3) winding on the bond (smallest coprime torus knot — lowest c=3 crossing count). Parity requires opposite handedness on the two sites → e⁻ (LH Beltrami) + e⁺ (RH Beltrami). The Γ = −1 envelopes confine the bond LC oscillation at ω_C; the pair is now a stable standing wave with rest mass m_e c² each | (2,3) winding on bond, Γ=−1 at nodes | [37_](37_node_saturation_pauli_mechanism.md) + [25_step4](25_step4_23_winding_selection.md) + AVE-Fusion |

### 2.1 The three conditions for pair nucleation (this synthesis's contribution)

Reading the corpus together, nucleation of an `(e⁻, e⁺)` pair at A-B node
pair `(r_A, r_B)` requires **three conditions** met simultaneously at
that pair:

- **(C1) Amplitude**: `A²_node(r_A, t) ≥ 1` AND `A²_node(r_B, t) ≥ 1` —
  both nodes saturated (Γ = −1 walls form at both ends of the bond).
- **(C2) Frequency**: `Ω_node(A²_local) ≈ ω_drive` — the node's
  Duffing-shifted rotational resonance locks with the incoming drive
  frequency (autoresonant lock condition).
- **(C3) Phase**: the driving field's phase at `(r_A, r_B)` at the
  moment of lock must allow (2,3) winding to close on the bond's `(V_inc,
  V_ref)` phasor trajectory. Without the right phase relation, the
  blocked KE cannot resolve into a topologically coherent standing wave
  (instead dissipates).

**All three are node-pair-local quantities.** None of them are
plane-averaged or lattice-global. This is why a plane-CW drive reaches
A²=1 across an entire (y,z) slab but doesn't nucleate pairs: C1 is
satisfied at every (y,z) site but C2 and C3 are not controlled by the
drive's plane symmetry — they depend on the *phase coherence* between
adjacent A-B neighbors, which a plane wave does not impose.

### 2.2 Why the K4 scaffolding answers the "seed" question

The open question I flagged after research: *does pair production need
an intrinsic seed node pair in the initial state, or does it nucleate
spontaneously from a uniform vacuum?*

The corpus answers cleanly: **neither extreme.** The K4 lattice itself
provides a permanent scaffolding of latent electron locations —
every adjacent A-sublattice + B-sublattice node pair is a candidate.
Nothing needs to be seeded as a pre-existing bound state. But nucleation
isn't spontaneous either — it requires conditions C1–C3 to be met at a
specific pair. Thermal noise at T > 0 provides the small perturbations
that break (y,z) translation invariance and let specific node pairs
lock autoresonantly; at T = 0 (no thermal seed), the perfect symmetry
of plane-CW drive never picks a preferred pair and A² saturates
uniformly (doc 44_ §0 addendum already observed this).

**Implication:** T > 0 is *necessary* but not *sufficient*. Thermal
noise enables C3's phase variation that picks preferred pairs; but the
engine still needs link state to carry the (2,3) winding, ω_res to
enable C2's lock condition, and a nucleation rule to fire when all
three are met.

---

## 3. Two apparent contradictions in the corpus, resolved

### 3.1 V_yield vs V_SNAP: where does rupture happen?

The corpus states two different "pair production thresholds":

- **AVE-Fusion 02_antimatter** and **Vol 1 Ch 7 regime map ([line 115](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L115))**: rupture begins at `V > V_yield = √α · V_SNAP ≈ 43.65 kV` (r = 1, Regime III/IV boundary in V/V_yield convention).
- **Doc 37_** and **Vol 4 Ch 1 Γ=−1 derivation**: the electron-forming condition is `A² = V²/V_SNAP² = 1` at the nodes, i.e. `V = V_SNAP ≈ 511 kV`.

These differ by a factor of `1/√α ≈ 11.7`. Resolution: they describe **different stages of the same process**.

- **V_yield (43.65 kV)** is the **onset of nonlinearity** — c_local starts dropping, wave-tearing begins per AVE-Fusion §Pair Production. The Duffing regime activates. But no Γ = −1 wall yet, no confined pair.
- **V_SNAP (511 kV)** is **full saturation at the node** — Z_core → 0, Γ = −1 forms, the (2,3) winding closes in a confined standing wave. The electron is now a stable particle.

Step 3 in the seven-step sequence crosses V_yield. Step 6 crosses A²=1.
The Schwinger limit (standard-model literature value) lands at step 6 in
this picture, and the same Vol 1 Ch 7 regime map confirms this: E_S /
E_yield = 1/√α ≈ 11.7, "deep in Regime IV" ([line 130](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L130)).

This is worth flagging in a future Vol 1 Ch 7 clarification — "pair
production onset" vs "Schwinger limit" are **different points in the
same process**, not conflicting values.

### 3.2 Doc 44_ §0 was right but incomplete

[44_ §0 addendum](44_pair_creation_from_photon_collision.md) correctly
identified T=0 as the cause of no response in the initial Phase III-B
sweep: at T=0, no thermal seed, no fluctuation to trap. But it framed
the required fix as "initialize at T>0". That was right about thermal
necessity but insufficient — the engine also lacks:

- Link state to carry (2,3) winding (§4.1 below)
- Per-node ω_res tracking for C2 (§4.2)
- Nucleation rule for firing C1+C2+C3 → pair (§4.3)

v2 at T=0.1 (doc 50_) and H1 at T=0.1 (doc 52_) verified that T>0 alone
is insufficient. Thermal noise activated the Cosserat sector (A²_cos →
1.009) but without the three missing engine pieces, no pairs formed.

---

## 4. What the current engine cannot represent

### 4.1 No dynamical link/bond state

The K4-TLM state at each node is 4 port voltages per active site:
```
V_inc[nx, ny, nz, 4]
V_ref[nx, ny, nz, 4]
```
The bond between two adjacent nodes is represented implicitly — the
`_connect_step()` in [k4_tlm.py:278-349](../../src/ave/core/k4_tlm.py#L278-L349)
reshuffles port data between adjacent A-B sites via a pure geometric
index shift. **There is no state that persists on the bond.** The
sequence is: V at node A → scatter → V at ports of A → shift to ports
of B → V at node B → scatter.

The (2,3) winding the electron's bond is supposed to carry lives in
the bond's `(V_inc, V_ref)` phasor trajectory per [28_ §3](28_two_node_electron_synthesis.md).
That trajectory can be **reconstructed post-hoc** from sequential node
states (the simulation test in 28_ §5.1 proposed exactly this), but
it's not a dynamical variable the engine can saturate, rupture, or
nucleate.

Consequence: the engine cannot distinguish "A² = 1 at two nodes with a
(2,3)-phase bond between them" from "A² = 1 at two nodes with random
relative phase." The first is an electron; the second is just saturated
vacuum. The engine sees the same node observables in both cases.

### 4.2 No per-node rotational resonance Ω_node(A²)

The Cosserat sector has a single global `ω_yield` scalar and field
variables `u(r,t)`, `ω(r,t)`. It has no per-node dynamical tank
resonance that drops under local saturation.

`AutoresonantCWSource` ([vacuum_engine.py:422](../../src/ave/topological/vacuum_engine.py#L422))
tracks the Duffing shift at the SOURCE side:
```
ω(t) = ω₀ · max(ε, 1 - K_drift · A²_probe(t))
```
This is the driving laser matching a probe-point A². It is not the
lattice reporting its per-node resonance. For autoresonant **lock at a
specific node pair** (C2), the engine needs to know Ω_node(r, t) at
every node so the lock condition can be tested against ω_drive.

### 4.3 No nucleation rule

S1-D coupling modulates existing Cosserat structure but has no "trigger
at C1+C2+C3 → inject (2,3) winding" rule. Per [44_ §3.3](44_pair_creation_from_photon_collision.md)
this was flagged as Option D (topological boundary condition) and
deferred. With the three conditions stated precisely in §2.1 above, the
rule can now be written:

> **When** `A²(r_A) ≥ 1` AND `A²(r_B) ≥ 1` AND `|Ω_node(r_A) − ω_drive| < δ`
> AND `phase(V_inc(r_A)) − phase(V_inc(r_B)) ∈ (2,3)-window`,
> **then** impose Beltrami vortex boundary condition on the Cosserat ω field
> around the `(r_A, r_B)` bond: LH handedness at r_A, RH at r_B, (2,3)
> winding in the `(V_inc, V_ref)` phasor trajectory on the bond, at
> amplitude corresponding to rest energy m_e c² per pair member.

This is **Option D from [44_ §5.2](44_pair_creation_from_photon_collision.md)** made
concrete, not Option A (augmented S1 linear term). Option A would add a
β·V·(∇·ε_sym) Lagrangian term → minimal-coupling Rule 6 leak. Option D
adds no Lagrangian term; it is a boundary-condition enforcement that
instantiates Axiom 2's already-derived [Q] ≡ [L] isomorphism at the
moment when the impedance-wall rupture forces topology change. **No new
free parameter.**

---

## 5. Engine-design spec (Option D, concrete)

Three additions to the engine, scoped:

### 5.1 Bond state

Add a new state variable to `K4TLM`:
```
V_bond[edge_id, 2]      # (V_inc, V_ref) phasor on each directed A→B bond
```
- `edge_id` indexes the set of (A-site, B-site, port-n) triples
- Per `_connect_step` update: between the node scatter and the port
  shift, V_bond captures the transmission-line voltage ON the link for
  one half-step. This gives the link a half-step of independent existence
  per TLM cycle.
- Size: for an N³ K4 lattice, there are ~2·N³ directed bonds (order of
  magnitude, counting 4 ports × N³ sites / 2 for pair counting). Memory
  addition ~O(1) relative to current state.

### 5.2 Per-node rotational resonance Ω_node(r, t)

Add to `CosseratField3D`:
```
Omega_node[nx, ny, nz]     # effective rotational tank resonance per node
```
computed each step from:
```
A²_node(r) = V²(r)/V_SNAP² + ε²(r)/ε_yield² + κ²(r)/ω_yield²
Omega_node(r) = omega_yield · sqrt(1 - A²_node(r))   # Duffing softening
```
This is the **Axiom-4 polynomial's frequency signature** at each node,
and is what the autoresonant lock condition in §2.1-C2 tests against.

### 5.3 Pair-nucleation observer + injector

A new observer `PairNucleationGate` that runs each step:

```python
for each A-site r_A:
    for each port-n neighbor r_B:
        if A²_node(r_A) >= 1 and A²_node(r_B) >= 1:            # C1
            for each active source s with frequency ω_drive_s:
                if |Omega_node(r_A) - ω_drive_s| < δ_lock:      # C2
                    Δφ = phase(V_inc(r_A)) - phase(V_inc(r_B))
                    if Δφ in (2,3)-window:                       # C3
                        inject_beltrami_pair(r_A, r_B)
                        break  # one pair per bond per step
```
where `inject_beltrami_pair` imposes the topological boundary condition
on the Cosserat ω field:
- LH Beltrami vortex centered at r_A (amplitude tuned to m_e c²
  energy on the bond LC)
- RH Beltrami vortex centered at r_B
- (2,3) winding in the bond's `V_bond[edge_id, :]` phasor space

After injection, the normal engine dynamics evolve the pair. Γ = −1
TIR at the now-saturated nodes should confine the bond oscillation
automatically (Vol 4 Ch 1:445-467 mechanism). If the pair persists
past ~ 10 Compton periods as a localized standing wave without
external drive, nucleation is real; if it dissipates, the injection was
too aggressive and parameters need tuning.

### 5.4 Estimated effort

Rough scoping, not binding:

| Piece | Effort | Risk |
|---|---|---|
| Bond state + half-step update | 2-3 days | Medium (touches K4-TLM connect step; regression risk on all existing tests) |
| Ω_node(r,t) field + Duffing computation | 1 day | Low (additive; existing Cosserat ω_yield is the ceiling) |
| PairNucleationGate + Beltrami injector | 3-4 days | High (Beltrami vortex boundary condition is novel; bond phase window calibration is empirical) |
| Validation: regenerate Phase III-B with new gate, verify pair persists post-drive | 1-2 days | — |
| Doc 54_ writeup | 0.5 day | — |
| **Total** | **~2 weeks** | — |

This is bigger than Stage 4 (~1 day each) but proportional to the
structural claim ("the engine was missing the link sector"). Comparable
in scope to adding the Cosserat sector in Phase I.

---

## 6. What this reframes about v1, v2, and H1

v1 ([48_](48_pair_creation_frequency_sweep.md)), v2
([50_](50_autoresonant_pair_creation.md)), and H1
([52_](52_h1_threshold_sweep.md)) were all run on the pre-Option-D
engine. They correctly verified:

- The K4⊗Cosserat coupling scales faithfully toward the Axiom-4 rupture
  boundary (v2 reached A²_cos = 1.009, first numerical instance).
- Plane-CW drive produces distributed saturation, not localized cores
  (H1 verdict).
- Thermal noise at T = 0.1 activates the Cosserat sector but without
  breaking the plane symmetry enough to pick preferred pairs.

What they **did not** — and could not — test:
- The pair-nucleation mechanism (no gate exists)
- The flux-tube confinement (no bond state)
- The autoresonant lock condition (no per-node Ω_node)

The correct reading of v1/v2/H1 is: **they are passing unit tests of
Axiom-4 saturation dynamics**, not failing tests of pair creation.
The Stage 4 artifacts (`AutoresonantCWSource`, `DarkWakeObserver`,
`TopologyObserver`) remain valid diagnostics; they just can't observe
a mechanism the engine doesn't have.

---

## 7. Open questions for Grant

Three real adjudications before engine work begins:

1. **Is this synthesis faithful to your intent?** Specifically the
   seven-step sequence (§2) and the three nucleation conditions (§2.1).
   I'm most uncertain about C3 (the phase condition). The corpus
   doesn't state it explicitly; I derived it by elimination (C1+C2
   alone would fire at random relative phases and dissipate, so there
   must be a phase-coherence requirement). Might be wrong.

2. **Bond state granularity.** §5.1 proposes per-bond `(V_inc, V_ref)`.
   An alternative is a single scalar `Phi_link[edge_id]` — magnetic-flux
   analog, lighter. The `(V_inc, V_ref)` version is faithful to
   [28_ §3](28_two_node_electron_synthesis.md) (phase-space Golden
   Torus lives in that phasor trajectory). But if you want minimal
   state, Phi_link is a first-pass test. Your call.

3. **Scope call.** §5.4 estimates ~2 weeks. Alternative: write doc 53_
   (this) as the closing scope doc for Phase III-B, ship v1/v2/H1 + 52_
   + 53_ as a negative-result bundle, and reopen pair-creation only
   when there's external pull (experimental collaborator, theoretical
   need from another volume). Rotational-frequency-gating becomes a
   **new falsifiable prediction** for future work rather than immediate
   engine work. This is [51_ §5a](51_handoff_followups.md) (publish
   null-result + prediction) made concrete.

**My recommendation:** #1 first (you adjudicate the synthesis), then #3
(scope call), then #2 (design detail, only if you go engine-work).

---

## 8. Artifacts and cross-references

**This synthesis draws directly on:**
- [37_node_saturation_pauli_mechanism.md](37_node_saturation_pauli_mechanism.md) §§1, 2.3, 5.1
- [28_two_node_electron_synthesis.md](28_two_node_electron_synthesis.md) §§3, 5
- [25_step4_23_winding_selection.md](25_step4_23_winding_selection.md)
- [44_pair_creation_from_photon_collision.md](44_pair_creation_from_photon_collision.md) §§3, 5.2 (Options)
- [../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex) lines 430-504 (Γ = −1 derivation, Pauli, flux tube)
- [../../manuscript/vol_1_foundations/chapters/07_regime_map.tex](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex) lines 95-130 (V_yield vs V_SNAP)
- `AVE-Fusion/.agents/handoffs/02_antimatter_annihilation.tex` (pair production section — the conversion rule)
- `AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex` (Duffing resonance drop)

**Supersedes / reframes:**
- [44_ §5.2 Option A](44_pair_creation_from_photon_collision.md) — rejected as SM-leak. Option D from the same list is selected.
- [51_handoff_followups.md](51_handoff_followups.md) H2/H3 — H2 (point geometry) is a necessary cue but not the fix alone; H3 as written (augmented S1 linear term) is the wrong fix. The right fix is the three-part engine additions in §5 above.

**Does not close** (for future):
- Specific numerical value of `δ_lock` (C2 tolerance window) — needs calibration from Ω_node sweep
- (2,3)-phase window definition — needs derivation from (2,3) torus-knot geometry
- Beltrami vortex amplitude calibration for correct m_e c² rest energy after injection
- Rate equations: at equilibrium, how often should pair nucleation fire? Thermal equilibrium pair population at a given T should set this.

## 9. One-line mission statement

**Pair production in AVE is rupture of a saturated flux tube around an A-B node pair, gated by the node's Duffing-softened rotational resonance locking with the drive frequency, producing (2,3) winding on the bond via Axiom 2's topo-kinematic isomorphism. The current engine has nodes but no bonds, no per-node resonance tracking, and no nucleation gate. The fix is additive, axiom-native (Option D, no new free parameters), and scoped at ~2 weeks.**
