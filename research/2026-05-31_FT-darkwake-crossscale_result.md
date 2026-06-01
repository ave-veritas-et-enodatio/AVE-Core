# FT-Dark-Wake-Cross-Scale Result — Is the g-2 A₂ wake the same τ_zx object as PONDER thrust?

**Date**: 2026-05-31
**Branch**: `analysis/ft-darkwake-crossscale-derivation` (worktree `AVE-Core-dwxs-wt`, off `main`)
**Status**: RESULT (analytical / dimensional). Executes the frozen prereg `research/2026-05-31_FT-darkwake-crossscale_prereg.md` (committed on sibling branch `analysis/forward-pred-darkwake-coldfusion-preregs`).
**Type**: ANALYTICAL (symbolic + dimensional). No large simulation.

## §0 — Outcome (TL;DR)

**OUTCOME C — different objects, shared name. Honest negative.**

The g-2 two-loop dark wake `τ_zx(t) = −dV²/dt|_{t−1/ω_C}` and the PONDER thrust dark wake `τ_zx(r,t) = ρ_Op14·Z_vac·∇|E|²·δ(backward pulse at c₀)` are **structurally distinct objects that share the τ_zx name**. The §4 dimensional bridge `∂_t = −c₀∂_z` is **illegitimate as applied**, for two independent reasons, either of which is sufficient:

1. **Coordinate-system mismatch (the load-bearing failure).** The g-2 τ_zx lives in the **(2,3) Clifford-torus PHASE space**: its "t" is the *trefoil phasor phase* (an internal angular coordinate, `arg` of `cos(2ω_C t)` / `sin(3ω_C t)`), and `(S_d − S_q)` is a d-axis-vs-q-axis phasor asymmetry. There is **no z-coordinate and no spatial propagation** in the g-2 object. The thrust τ_zx lives in **REAL space**: ∇|E|² is a lab-frame spatial gradient over the physical array and the δ-function propagates along a real lab-frame z at c₀. The wave relation `∂_t = −c₀∂_z` is a **real-space d'Alembert relation** that presupposes exactly the lab-frame (z, t) the g-2 object does not possess. There is no z in the g-2 object for `∂_z` to act on.

2. **Dimensional mismatch (the corroborating failure).** Even granting a *formal* substitution, the g-2-side prefactor is **kinematic** (`c₀·ℓ_node`-class, units m²/s or m³/s) while the thrust-side prefactor is **electrical impedance** (`ρ_Op14·Z_vac`, units Ω = kg·m²·s⁻³·A⁻²). These are different physical dimensions; no single *dimensionless* ρ_Op14 can equate them. Closing the gap requires inserting an *additional* dimensionful transducer (a charge/current scale such as ξ_topo = e/ℓ_node), which is not "one trade efficiency."

The corpus's own §10.2 of the scaling derivation (`2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:129`) flagged the ~12-OOM Compton→100 MHz unit-mapping as OPEN and "the single biggest risk to the same-object claim." This derivation resolves that risk in the **negative direction**: the gap is not a missing conversion factor to be filled, it is a **category boundary** between a phase-space kernel-correlation and a real-space momentum pulse.

**Falsifier status (prereg §6):** Outcome A is falsified — the dimensional reconciliation §4 fails (`c₀·ℓ_node` and `ρ_Op14·Z_vac` cannot be made consistent under any canonical normalization), AND the §10.2 unit-mapping is a coordinate-category gap, not a scale-dependent-ρ_Op14 gap. Both prereg-§6 falsifier branches fire.

**What this retires:** the cross-scale "same dark wake, one ρ_Op14, two observables 12 OOM apart" CHORD framing **for this object pair**. It does NOT retire either τ_zx individually, nor the Op14 mechanism, nor the F·c₀ wake-power result (see §7).

## §1 — Discipline log (skills fired)

| Skill | When | Verdict |
|---|---|---|
| `phase-space-coordinate-check` | FIRST, before algebra (§2) | **FAIL-to-reconcile.** g-2 τ_zx is phase-space (Clifford-torus phasor-phase "t", d/q axes); thrust τ_zx is real-space (lab-frame z, ∇|E|²). The two coordinate systems are not reconcilable under `∂_t=−c₀∂_z`. THE load-bearing check; it alone forces Outcome C. |
| `substrate-native-check` | §2.3 | The two objects are different substrate-native cuts: g-2 = Cosserat phase-space kernel-correlation in the (2,3) trefoil portrait; thrust = real-space K4-TLM longitudinal-shear momentum pulse. Different substrate observables, not one object in two coordinates. |
| `consistency-vs-emergence` | §0, §3 | Class 3 **consistency / structural-identity check** (per prereg §7), NOT an emergence test. It establishes whether two existing predictions share one substrate object. Verdict: they do not. No new measured number is produced or claimed. |
| `ave-evidence-framing-discipline` | throughout | Both τ_zx are analytically-argued, neither numerically closed. The negative (Outcome C) is itself analytical/dimensional — it is a *structural* disqualification (coordinate-category + dimension), which is robust to the numerical-closure status of either object. No overclaim of "thrust validated" or "g-2 validated"; the result is strictly about the OBJECT-IDENTITY question. |
| `ave-canonical-source` | §4 | c₀ = `C_0`, ℓ_node = `L_NODE`, Z_vac = `Z_0`, ρ_Op14 = 0.990 pulled from canonical sources; never hardcoded numerically in the algebra (symbols carried). |
| `verify-before-cite` | §1.1 | All file:line anchors re-grepped on this worktree 2026-05-31 (see §1.1). |

### §1.1 — Citation verification (verify-before-cite, re-grepped 2026-05-31 on `AVE-Core-dwxs-wt`)

- `q-g19a-petermann-saliency-closure.md:28-30` — verbatim: "The Cosserat unknot is a real-space 0₁ unknot whose Clifford-torus phase-space portrait winds (2,3): I_d(t) = cos(2ω_C t), I_q(t) = sin(3ω_C t) … The trefoil lives in *phase space*, not real space; the real-space soliton is the unknot 0₁." ✓
- `q-g19a-petermann-saliency-closure.md:35-37` — verbatim: "Dark wake (retarded back-reaction): τ_zx(t) = −dV²/dt|_{t − τ_retard} with τ_retard = 1/ω_C (one Compton-loop transit time …)." ✓
- `q-g19a` grep for {c_0, propagation, ∇|E|², z-axis, backward, z_back}: **zero matches**. The g-2 τ_zx carries no real-space-propagation vocabulary. ✓
- `2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:137` — verbatim: `τ_zx(r,t) = ρ_Op14 · Z_vac · ∇|E|² · δ(r − r_soliton(t) − c₀(t − t₀)ẑ_back)`. ✓
- `2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:129` — verbatim §10.2-precursor open gap: "Substrate-fundamental rate is electron-Compton-scale; PONDER-01 drives at 100 MHz which is ~12 orders of magnitude slower. The wake-ringing frequency at the measurable scale should be the convolution of substrate-rate × soliton-cycle-rate; needs dedicated derivation." ✓
- `chiral-thrust-derivation.md:95` — verbatim: "A continuous wave of longitudinal shear strain (τ_zx) propagates backward from the thruster into the static continuum, cleanly and formally closing the momentum conservation loop." ✓
- `chiral-thrust-derivation.md` grep for {phase-space, Clifford, d-axis, q-axis, phasor, trefoil}: **zero matches**. The thrust τ_zx carries no phase-space vocabulary. ✓
- `op14-cross-sector-trading.md:9,11` — ρ = −0.990 Pearson anti-correlation, A-012 canonical, over t∈[150P,200P]. ✓
- `src/ave/core/constants.py`: `C_0 = 299_792_458.0` (:95); `Z_0 = √(μ₀/ε₀) ≈ 376.73` (:98); `L_NODE = ℏ/(m_e c) ≈ 3.8616e-13 m` (:234). ✓

## §2 — The phase-space-coordinate-check (THE load-bearing check, done FIRST)

This is the check the prereg flagged as load-bearing and instructed be resolved *before* the algebra. The central question: **do the g-2 τ_zx and the thrust τ_zx live in the same coordinate system at all?** If not, the §4 bridge `∂_t = −c₀∂_z` (a real-space wave relation) is illegitimate regardless of how the prefactor algebra comes out.

### §2.1 — Coordinates of the g-2 τ_zx (PHASE space)

From `q-g19a-petermann-saliency-closure.md:28-37`, the g-2 object is built entirely from:

$$I_d(t) = \cos(2\omega_C t), \qquad I_q(t) = \sin(3\omega_C t), \qquad \tau_{zx}(t) = -\frac{dV^2}{dt}\bigg|_{t-1/\omega_C}$$

with the correlation kernel `⟨(S_d − S_q)·τ_zx⟩` averaged **over one trefoil period**. Reading off the coordinate structure:

- **The "t" is a phasor phase, not lab time.** It appears only as the argument of `cos(2ω_C t)` and `sin(3ω_C t)` — i.e. `ω_C t` is the *angle* swept on the Clifford torus. The leaf is explicit (`:30`): "The trefoil lives in *phase space*, not real space; the real-space soliton is the unknot 0₁." So `t` parameterizes the **internal d/q phasor winding**, an angular coordinate of the (2,3) torus-knot portrait. It is a clock *internal to the electron's own LC tank* (rate ω_C = m_e c²/ℏ), not a lab-frame propagation time.
- **(S_d − S_q) is a phasor-axis asymmetry.** `S_d − S_q = √(1−A_d²) − √(1−A_q²)` is the d-axis-minus-q-axis saturation-kernel difference — a difference between two *axes of the phasor plane*, with no spatial extent.
- **There is no z and no propagation.** The retardation `1/ω_C` is a *phase lag* (one Compton-loop transit as an angle), applied to the *same* internal phasor clock. Nothing propagates through lab space. Grep confirms: zero occurrences of {c₀, propagation, ∇|E|², z-axis, backward} anywhere in the leaf.

**Coordinate verdict for g-2:** a 2-D internal **phase space** (the Clifford torus, coordinates = d-axis and q-axis phasors), with a single internal angular time `ω_C t`. Zero real-space spatial coordinates.

### §2.2 — Coordinates of the thrust τ_zx (REAL space)

From `2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:137` and `chiral-thrust-derivation.md:95`:

$$\tau_{zx}(\vec r, t) = \rho_{Op14}\,Z_{vac}\,\nabla|E|^2\,\delta\!\big(\vec r - \vec r_{soliton}(t) - c_0(t-t_0)\hat z_{back}\big)$$

- **`r` and `z` are lab-frame real space.** ∇|E|² is a gradient of field energy density *over the physical array* — Cartesian lab space (the same space in which the torsion balance, the 10 m parallax baseline, and the strain gauge live, per the thrust leaf's §9 falsifiers).
- **`t` is lab time and the pulse propagates.** The δ-function rides a front at `r_soliton(t) + c₀(t−t₀)ẑ_back` — a real-space wavefront moving backward at c₀ in the lab. This *is* a propagating wave; it has a definite arrival delay `Δt = L/c₀` (`scaling-doc:200`, `chiral-thrust:126`).
- **Grep confirms** zero occurrences of {phase-space, Clifford, d-axis, q-axis, phasor, trefoil} anywhere in the thrust leaf.

**Coordinate verdict for thrust:** 3-D lab-frame **real space** (r) + lab time (t), with genuine c₀-propagation along z.

### §2.3 — Are the two coordinate systems reconcilable? (substrate-native-check)

**No.** The substrate-native reading makes the disjointness sharp rather than incidental:

| Aspect | g-2 τ_zx | thrust τ_zx |
|---|---|---|
| Substrate cut | Cosserat (2,3) **phase-space** trefoil portrait | K4-TLM **real-space** longitudinal shear |
| "Time" coordinate | internal phasor angle ω_C t (Clifford torus) | lab-frame propagation time t |
| Spatial coordinate | **none** (no z) | lab-frame r, backward z at c₀ |
| The field it correlates | (S_d − S_q): d-vs-q phasor-axis asymmetry | ∇|E|²: lab-frame energy-density gradient |
| Physical role | back-reaction **kernel** in a phase-averaged correlation | propagating **momentum/stress pulse** (Newton-3) |
| Dimension | [V²/time] (correlation integrand) | [Ω·(V/m)²/m] = real-space stress |
| Propagation? | no — a phase-lagged correlation | yes — a c₀ wavefront with Δt = L/c₀ |

The two share exactly one thing: the string "τ_zx". They share **no coordinate, no propagation structure, and no physical dimension**. The vocabulary-disjointness is not an accident of how the two leaves were written — it is the substrate-native signature that the **(2,3) phase-space d/q-kernel correlation** (g-2) and the **real-space Op14 momentum pulse** (thrust) are two different substrate observables, exactly as prereg Outcome C anticipated.

**`∂_t = −c₀∂_z` requires a real-space (z, t).** The relation is the d'Alembert characteristic for a wave traveling at c₀ along a real spatial axis z. To apply it to the g-2 object you would need (a) a real-space z along which the g-2 τ_zx propagates, and (b) the g-2 "t" to be the matching lab propagation time. The g-2 object has **neither**: its "t" is an internal phasor angle and there is no z. So `∂_z` has nothing to act on, and `∂_t` is a derivative with respect to a phasor phase, not a propagation time. **The bridge cannot be applied without first inventing the very real-space coordinates the g-2 object lacks** — which is precisely the coordinate-substitution the prereg warned would be illegitimate (`phase-space-coordinate-check`: "Real-space lattice-Cartesian measurements compared against phase-space φ² predictions are uninformative"; A46).

**Coordinate-check verdict: FAIL-to-reconcile. The two τ_zx do not live in the same coordinate system. This alone forces Outcome C.** The §3-§4 dimensional algebra below corroborates the same verdict from an independent direction.

## §3 — The §4 bridge, carried symbolically (corroborating, independent of §2)

The prereg §4 instructed: *if reconcilable*, carry out the dimensional reconciliation. §2 already returns NOT reconcilable. For completeness and as an independent corroboration, I carry the algebra anyway — granting (counterfactually) that one could write a real-space z for the g-2 object — and show the prefactors **also** fail to reconcile on dimensional grounds. Two independent failures, either sufficient.

Canonical symbols (pulled, never hardcoded): c₀ = `C_0`, ℓ_node = `L_NODE`, Z_vac = `Z_0`, ρ_Op14 = 0.990 (`op14-cross-sector-trading.md` A-012).

### §3.1 — The substitution as the prereg wrote it

Prereg §4: under `∂_t = −c₀∂_z` for a backward c₀ pulse, with `V ≈ E·ℓ_node`,

$$\frac{dV^2}{dt} = -c_0\frac{dV^2}{dz} \overset{\text{prereg}}{\sim} c_0\,\ell_{node}\,\nabla|E|^2,$$

giving the claimed identification

$$\underbrace{c_0\,\ell_{node}}_{\text{g-2 side}} \overset{?}{\leftrightarrow} \underbrace{\rho_{Op14}\,Z_{vac}}_{\text{thrust side}}.$$

### §3.2 — Power-counting correction (flag, not load-bearing)

`V ≈ E·ℓ_node` ⟹ `V² ≈ E²·ℓ_node²`. Therefore

$$\frac{dV^2}{dz} \approx \ell_{node}^2\,\frac{d(E^2)}{dz} = \ell_{node}^2\,(\nabla|E|^2)_z \;\Rightarrow\; \frac{dV^2}{dt} = -c_0\frac{dV^2}{dz} \approx -c_0\,\ell_{node}^2\,\nabla|E|^2.$$

The g-2-side prefactor is therefore **`c₀·ℓ_node²`** (two powers of ℓ_node), not `c₀·ℓ_node` as prereg §4 wrote (one power) — the prereg substituted `V ~ E·ℓ_node` for V² in one place while needing two powers for V². I FLAG this per flag-don't-fix; it does not rescue Outcome A — it makes the dimensional gap *worse*, not better (see §4). I carry both forms below so the conclusion is robust to which power is intended.

### §3.3 — Dimensional table

| Quantity | Symbolic form | SI dimension | SI value (canonical) |
|---|---|---|---|
| g-2 prefactor (prereg, 1×ℓ) | `c₀·ℓ_node` | m·s⁻¹ · m = **m²·s⁻¹** | (2.998e8)(3.862e-13) ≈ **1.158e-4 m²/s** |
| g-2 prefactor (corrected, 2×ℓ) | `c₀·ℓ_node²` | m·s⁻¹ · m² = **m³·s⁻¹** | (2.998e8)(3.862e-13)² ≈ **4.47e-17 m³/s** |
| thrust prefactor | `ρ_Op14·Z_vac` | dimensionless · Ω = **Ω = kg·m²·s⁻³·A⁻²** | (0.990)(376.73) ≈ **373.0 Ω** |

## §4 — Why the prefactors cannot reconcile under one ρ_Op14

The g-2-side prefactor is **kinematic** (m²/s or m³/s — a velocity×length or velocity×area). The thrust-side prefactor is **electrical impedance** (Ω). These are **different physical dimensions**. No purely *dimensionless* factor — and ρ_Op14 = 0.990 is dimensionless by construction (a Pearson trade-efficiency) — can map m²/s onto Ω. The identification `c₀·ℓ_node ↔ ρ_Op14·Z_vac` is **dimensionally ill-posed**.

To force a bridge one must insert an *additional dimensionful transducer*. The substrate-canonical candidate is ξ_topo = e/ℓ_node (the Axiom-2 electromechanical transduction constant, C/m), and/or a current/charge scale. For instance Z_vac (Ω = V·A⁻¹) carries A⁻² in SI base units; converting it to a kinematic m²/s requires multiplying by a (charge)²/(mass) factor — i.e. by something like `e²/(ε₀ m_e c)`-class quantities. Whatever combination one chooses:

- it is **not** "one trade efficiency ρ_Op14" — it is a *new, separate* dimensionful conversion (a charge↔kinematics transducer), exactly the thing the prereg's single-ρ_Op14 hypothesis (prereg §1, §2.5) asserted was *unnecessary*;
- it would have to be *fitted or separately derived*, and would carry the full ~12-OOM Compton-to-bench mismatch the §10.2 gap already flags — but now as a *dimension*-bridging factor, which no scaling-of-ρ_Op14 can supply.

**Therefore the prereg §6 falsifier fires on its first branch**: the dimensional reconciliation §4 fails — `c₀·ℓ_node` (or `c₀·ℓ_node²`) and `ρ_Op14·Z_vac` cannot be made consistent under any canonical normalization that preserves "one dimensionless ρ_Op14." The §10.2 open unit-mapping is therefore NOT a missing scalar conversion (which would still admit Outcome A or B); it is a **coordinate-and-dimension category boundary** (Outcome C).

### §4.1 — Root cause, stated cleanly

The dimensional mismatch in §4 is a *symptom* of the §2 coordinate mismatch. The g-2 τ_zx = −dV²/dt is a **time-domain correlation integrand** with dimension [V²/time], living inside a phase-averaged dimensionless kernel `(2/πα)⟨(S_d−S_q)·τ_zx⟩` that *outputs a pure number A₂*. The thrust τ_zx = ρ_Op14·Z_vac·∇|E|² is a **real-space stress field** (confirmed by `∫τ_zx dA = F·Z_vac/ρ_Op14`, units N — `scaling-doc:154`). A dimensionless-number-producing phasor kernel and a real-space stress field are not the same object in two coordinate systems; they are two different objects. The dimensional algebra and the coordinate check are two views of the **same** structural fact.

## §5 — Outcome classification (prereg §5)

**OUTCOME C.** Mapping the three pre-registered outcomes against the result:

- **Outcome A (CHORD — same object):** REJECTED. Requires the two forms to reconcile under `∂_t=−c₀∂_z` with one ρ_Op14. The bridge is illegitimate (§2 coordinate-category) and the prefactors are dimensionally irreconcilable under one dimensionless ρ_Op14 (§4). No relation R(A₂, F-coeff, ρ_Op14, N_boundary) exists to be derived.
- **Outcome B (same mechanism, not one coefficient):** REJECTED as stated. Outcome B presumes *both* run on Op14 desaturation but with an extra α-order phase-space weighting at the loop scale only — i.e. a *common mechanism, different coefficient*. The result is stronger than B: the g-2 object is not a real-space Op14 momentum pulse *at all* (it is a phase-space d/q-kernel correlation), so it is not "the same Op14 desaturation mechanism viewed with an extra weighting." The shared-mechanism premise of B is not established. (See §5.1 for the one genuine shared substrate primitive, which is weaker than B and does not lift to B.)
- **Outcome C (different objects, shared name):** **SELECTED.** The g-2 τ_zx (retarded kernel back-reaction, phase-space d/q) and the thrust τ_zx (real-space Op14 momentum pulse) are structurally distinct; the dimensional bridge fails. The cross-scale "same dark wake" framing is a **naming coincidence** for this object pair. Honest negative.

### §5.1 — The one genuine shared primitive (and why it is not Outcome B)

There IS a real substrate kinship, and naming it precisely is what keeps this an honest-C rather than an overclaimed-C: **both objects ultimately trace to the Axiom-4 saturation kernel S(A)=√(1−A²)** — the g-2 via `(S_d − S_q)` (kernel asymmetry across phasor axes) and the thrust via the Jensen-rectification deficit `δ = 1 − ⟨S(E)⟩` (`chiral-thrust-derivation.md:22-28,48`) feeding ∇|E|². That is a **shared axiom**, not a shared *object* and not even a shared *mechanism-instance*:

- The g-2 uses S(A) as a **phasor-axis difference inside a phase-averaged correlation** that outputs a dimensionless A₂.
- The thrust uses S(E) as a **time-averaged real-space rectification deficit** that outputs a DC lattice stress.

Same kernel function, two structurally different *uses* (phase-space correlation vs real-space rectification), with two different *outputs* (pure number vs stress field). A shared axiom is the floor of any AVE pair and does not constitute "one dark-wake object" (Outcome A) or even "one Op14 desaturation mechanism with an extra weighting" (Outcome B). It is correctly Outcome C with a named common ancestor.

## §6 — No relation R, no bench cross-check (prereg §4-step-4)

Because Outcome A is rejected, prereg execution-steps 4 (derive R) and 5 (specify which bench measurement pins the same ρ_Op14 that A₂ pins) **do not apply** — there is no shared ρ_Op14 to pin. For the record, what Outcome A would have *required* (and which is now known not to exist):

- a single dimensionless ρ_Op14 appearing in *both* the A₂ kernel and the thrust coefficient. The thrust coefficient does carry ρ_Op14 = 0.990 (`scaling-doc:137`); the A₂ kernel `(2/πα)⟨(S_d−S_q)τ_zx⟩` carries **no ρ_Op14 at all** — it carries the d/q split (δ = −3α/2) and the 1/π² form factor (`q-g19a:47-48,82`). There is no slot in A₂ for the Op14 trade efficiency, which is itself direct evidence that A₂ is not an Op14-momentum-pulse observable.
- Consequently the prereg-§8 hoped-for pairing — "electron g-2 (0.1 ppb) and a bench torsion-balance + stereo-parallax become two independent windows on the same ρ_Op14" — **does not hold**. The torsion-balance F·c₀ + stereo-parallax (`chiral-thrust:119-128`) measurements pin the *thrust* ρ_Op14; the electron g-2 pins δ = −3α/2 and the d/q energy split. **Different substrate quantities. No cross-scale invariant links them.**

This is the prereg-§8 chord-vs-echo question answered in the negative *for this object pair*: there is no 12-OOM cross-scale invariant here. (It does not bear either way on other AVE cross-scale invariants; it is a single-pair negative.)

## §7 — What is preserved (anti-overclaim, ave-walk-back scope)

Outcome C retires exactly one thing and **nothing more**. Per `ave-evidence-framing-discipline` + prereg §7 anti-overclaim guards, the scope of this negative is:

**Retired (this object pair only):**
- The claim that the g-2 A₂ wake and the PONDER thrust wake are *the same substrate object* connected by `∂_t=−c₀∂_z` with one shared ρ_Op14. (The prereg §0/§1 same-object target.)
- The "one substrate quantity, two falsifiable observables 12 OOM apart" CHORD framing **for {A₂, thrust}**.

**NOT retired (untouched by this result):**
- The g-2 A₂ = (2/πα)⟨(S_d−S_q)τ_zx⟩ = −0.3416 (+4% forward) result itself. Its derivation is internal to the phase-space trefoil and does not depend on any thrust connection. (Still analytically-argued, numerical-closure-pending per `q-g19a:110`.)
- The thrust τ_zx = ρ_Op14·Z_vac·∇|E|², P_wake = F·c₀, and ρ_Op14 = 0.990 results. Their derivation is internal to the real-space Op14-scaling argument and does not depend on any g-2 connection. (Still analytically-argued, numerical-closure-pending per `scaling-doc:219-233`.)
- The Op14 cross-sector-trading mechanism (A-012, ρ = −0.990). Canonical and unaffected.
- The shared Axiom-4 kernel S(A) ancestry (§5.1).

**Explicitly NOT claimed:** that AVE thrust is validated; that AVE g-2 is validated; that the dark-wake concept is wrong in general. The result is narrowly that **these two named-τ_zx are not one object**.

**§10.2 update for the scaling doc (flag for the auditor lane to land):** the scaling-doc §10.2 open item ("trade-frequency unit-mapping, ~12 OOM Compton→100 MHz") should be annotated that the *cross-scale-to-g-2* direction of that mapping is now resolved in the negative: the g-2 τ_zx is a phase-space object in a different coordinate system, so the §10.2 gap is not bridged by any frequency-convolution to the g-2 side — it remains open only as the *within-thrust* (substrate-rate → soliton-cycle-rate) real-space question, which this result does not touch. I surface this; the auditor lane lands the annotation (lane discipline — I do not edit the sibling-branch frozen prereg or the scaling doc's canonical status here).

## §8 — Cross-references

- Frozen prereg: `research/2026-05-31_FT-darkwake-crossscale_prereg.md` (sibling branch `analysis/forward-pred-darkwake-coldfusion-preregs`)
- g-2 leaf: `manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md` (clm-v2sg8z) — phase-space (2,3) trefoil, τ_zx = −dV²/dt at 1/ω_C
- thrust scaling derivation: `research/2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md` — ρ_Op14=0.990, P_wake=F·c₀, §10.2 open unit-mapping (:129)
- thrust leaf: `manuscript/ave-kb/vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md` (clm-7tynm2) — real-space τ_zx, Dark Wake momentum conservation, stereo-parallax
- Op14: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md` (clm-p2tp9i, A-012) — ρ=−0.990
- constants: `src/ave/core/constants.py` — C_0 (:95), Z_0 (:98), L_NODE (:234)
