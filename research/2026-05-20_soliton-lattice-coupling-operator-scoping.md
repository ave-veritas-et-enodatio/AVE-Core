# Soliton-Lattice Coupling Operator — Session 1 Scoping Research Doc

**Date:** 2026-05-20 (session spans 2026-05-19 EOD → 2026-05-20 early; landed under 2026-05-20 per UTC)
**Branch:** `analysis/soliton-lattice-coupling-operator-scoping` off `analysis/integration` at `0f3fd52`
**Originating epic:** [`_orchestration/soliton-lattice-coupling-operator.md`](../_orchestration/soliton-lattice-coupling-operator.md) (Session 1 of multi-session arc)
**Predecessor cascade:** SDSS DR17 merge `9f976e0` → operator-output reframing of three-observable triangle 2026-05-19 EOD; epic spawned at `0f3fd52`

---

## 0. Scope discipline (load-bearing for this session)

**This is a scoping research doc.** It produces:

1. A structural definition sketch of $\hat{\mathcal{O}}_{\text{soliton}}$ (NOT a derivation of its functional form)
2. A corpus building-block inventory of the 8 pieces queued for integration in Session 2
3. A list of substrate-physics derivation prereqs that must close BEFORE Session 2 can produce an integrated operator
4. A list of testable predictions (16 solar-system axis data points + galactic + LSS targets) the operator must reproduce
5. A multi-session arc outline (Sessions 2-5 with effort + branch-points)

**No derivation in this session.** Any functional form, parameter prediction, or numerical claim about the operator's output is out-of-scope and is queued for Session 2.

This doc is research-tier (no manuscript / KB modifications). The corpus building-block summaries in Phase 2 cite from canonical leaves but do not modify them.

---

## 1. Phase 1 — Operator structural definition (sketch only)

### 1.1 What the operator maps

$\hat{\mathcal{O}}_{\text{soliton}}$ maps the substrate's cosmically-frozen rotational direction $\hat{\Omega}_{\text{freeze}}$, modulated by a bound-soliton's structural parameters $(M_s, \omega_s, \mathcal{M}_s, \text{topology})$, onto an externally-observable axis $\hat{n}_{\text{observable}}$ for that soliton:

$$\hat{\mathcal{O}}_{\text{soliton}}\bigl(\hat{\Omega}_{\text{freeze}}; \, M_s, \omega_s, \mathcal{M}_s, \text{topology}\bigr) \to \hat{n}_{\text{observable}}$$

### 1.2 Inputs

| Input | Type | Source |
|---|---|---|
| $\hat{\Omega}_{\text{freeze}}$ | Direction (unit vector on $S^2$) | Substrate-frozen at cosmic genesis per [`omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md):26,37 + Vol 3 Ch 4 lines 408-416; Planck PR3 SMICA pin at $(l = 60.28°, b = 50.48°)$, $\sigma = 0.92°$ per [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md:17`](2026-05-19_c5-cmb-axis-executable-observer-result.md). |
| $M_s$ | Soliton integrated strain ($\mathcal{M}$ projection) | $\mathcal{M}$ boundary observable per [`boundary-observables-m-q-j.md:13`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) — volume integral of $(n(\mathbf{r}) - 1)$ over the soliton's $\Gamma = -1$ enclosure. |
| $\omega_s$ | Soliton rotation rate | Internal angular frequency of the bound soliton; for planets this is the spin-rate (period in hours per Phase 4 table). |
| $\mathcal{M}_s$ | Soliton magnetic moment ($\mathcal{J}$ projection) | $\mathcal{J}$ boundary observable per [`boundary-observables-m-q-j.md:15`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) — surface winding number, which projects to magnetic moment for planetary-class solitons. |
| topology | Discrete invariants | Per Axiom 2 (TKI): $(2,q)$ torus-knot family + Burgers-vector chirality (right-handed vs left-handed per $I4_1 32$ ground state); for planets this maps to internal-structure class (rocky / metallic-H gas-giant / icy-mantle gas-giant). |

### 1.3 Output

$\hat{n}_{\text{observable}}$ — the externally measurable axis for the soliton-class. For planetary-class solitons, this is realized as a **pair** of axes:

- $\hat{n}_{\text{spin}}$ — the spin-axis (mechanical-rotation direction)
- $\hat{n}_{\text{mag}}$ — the magnetic-dipole axis

The operator must explain BOTH axes (16 data points = 8 planets × {spin, magnetic}), and specifically the relative tilt between them. The relative tilt is the operator's load-bearing forward-prediction channel; aligned-spin-and-magnetic (e.g., Saturn <1°) vs gross-misaligned (Uranus 59°, Neptune 47°) is the discriminator.

For galactic-class solitons, $\hat{n}_{\text{observable}}$ is the rotation axis (galactic disk normal); SDSS DR17 LSS data gives the coherent direction at $(l = 129°, b = 79°)$, $\sigma = 6.83°$ per [`research/2026-05-19_c5-sdss-spin-orientation-result.md:21`](2026-05-19_c5-sdss-spin-orientation-result.md).

### 1.4 Structural form sketch

The functional form is conjectured (Session 2 derives) to factor as a rotation acting on $\hat{\Omega}_{\text{freeze}}$:

$$\hat{n}_{\text{obs}} = R\bigl(\theta(M_s, \omega_s, \mathcal{M}_s, \text{topology})\bigr) \cdot \hat{\Omega}_{\text{freeze}}$$

where $R \in SO(3)$ is a rotation parameterized by an angle $\theta$ that depends on the soliton's structural parameters. Special cases that the structural form must accommodate:

- **Aligned regime** ($\theta \to 0$): $\hat{n}_{\text{obs}} \to \hat{\Omega}_{\text{freeze}}$ (e.g., Saturn-class — minimal mag-spin tilt; in galactic limit, this would give SDSS LSS axis aligned with CMB axis-of-evil at the same direction, which is FALSIFIED at 5.33σ per SDSS DR17, so galactic-class is decisively NOT in this regime).
- **Anti-aligned regime** ($\theta \to \pi$): $\hat{n}_{\text{obs}} \to -\hat{\Omega}_{\text{freeze}}$ (Venus retrograde candidate; Venus spin obliquity = 177.4°).
- **Resonance regime** ($\theta \to 90°$ class): $\hat{n}_{\text{obs}}$ orthogonal-class to $\hat{\Omega}_{\text{freeze}}$ (Uranus 98° obliquity, Uranus 59° mag tilt, Neptune 47° mag tilt — both ice-giants).

This sketch is structural only. The derivation of $\theta(M_s, \omega_s, \mathcal{M}_s, \text{topology})$ is Session 2's load-bearing deliverable.

### 1.5 Symmetry constraints (must be respected by Session 2 derivation)

| Symmetry | Constraint | Source |
|---|---|---|
| Chirality (parity) | The substrate ground state is right-handed $I4_1 32$ per Axiom 1; left-handed solutions exist as $\Gamma = -1$-boundary topologically allowed mirror configurations. The operator should give symmetric output under $\hat{\Omega}_{\text{freeze}} \to -\hat{\Omega}_{\text{freeze}}$ modulo chirality-induced asymmetry. | Axiom 1 + [`omega-freeze-cosmic-grain-cascade.md:37`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) |
| Time-reversal | Substrate rotation (frame-dragging) is asymmetric under T-reversal per Op14 prograde-vs-retrograde Op14-saturation asymmetry. Operator must inherit this asymmetry. | [`frame-dragging-impedance-convolution.md:20`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md) |
| Scale | Per Axiom 2 (TKI: $[Q] \equiv [L]$), the operator should admit a scale-parameter ($M_s$ in appropriate units) that interpolates between electron-class (no spin axis except in spinor sense), planetary-class (16 axis data points), and galactic-class (SDSS DR17). | Axiom 2 + [`boundary-observables-m-q-j.md:33`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) (same mechanism at all scales). |

### 1.6 Class E classification (per `consistency-vs-emergence` v1.1)

The operator-output observables ($\hat{n}_{\text{spin}}^{(\text{planet})}$, $\hat{n}_{\text{mag}}^{(\text{planet})}$, $\hat{n}_{\text{galactic}}$) are **Class E — operating-point projection**. The single underlying substrate parameter is $\hat{\Omega}_{\text{freeze}}$ (with $u_0^* \approx 0.187$ jointly setting it); the N observable axes project from that single direction through the operator. Per the canonical Class E framing at [`omega-freeze-cosmic-grain-cascade.md:7`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md):

> falsification of any one kills the operating-point and therefore the entire substrate model

Specifically: if even ONE of the 16 planetary axis data points can be shown to be inconsistent with the operator's prediction (with the operator running off a single $\hat{\Omega}_{\text{freeze}}$ direction), the framework's joint constraint is broken. This is the load-bearing falsification surface for Session 3.

---

## 2. Phase 2 — Corpus building-block inventory (8 pieces)

For each building block: file:line, 1-paragraph contribution-to-the-operator summary, what's still missing for Session 2 integration.

### 2.1 Op14 asymmetric saturation profile (frame-dragging, rotating mass)

**File:** [`manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md:20`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md)

**Verbatim mechanism (line 20):**
> Rays traversing the retrograde side encounter a stricter Op14 saturation profile, increasing their refractive capture radius. Conversely, rays on the prograde side propagate through a mechanically relaxed tensor, allowing them to graze closer to the horizon before capture. This differential refractive trap flattens the shadow boundary on the prograde side, producing the characteristic "D-shape" predicted by the Kerr metric without continuous manifolds.

**Contribution to the operator:** This is the substrate-level mechanism by which a rotating mass IMPRINTS a directional asymmetry on the surrounding substrate impedance. A bound soliton with spin $\omega_s$ in the substrate's $\hat{\Omega}_{\text{freeze}}$ reference frame experiences differential Op14 saturation on the prograde vs retrograde face. This asymmetry is the substrate-physics origin of the rotation $R(\theta)$ in the operator's structural form sketch (§1.4). The angular dependence at the Kerr cosmic instance — $\omega(r) = 2Mar/(r^2 + a^2)^2$ (line 11) — provides the prototype scaling law.

**Still missing for integrated operator:** (i) The scaling of $\theta$ on $(M_s, \omega_s)$ — line 20 establishes prograde/retrograde asymmetry exists but does not quantify the alignment angle the soliton SETTLES INTO under this asymmetric saturation. (ii) The transformation of this asymmetric saturation from substrate-rest frame to soliton-body frame is not derived. (iii) The result is currently stated for the EXTERIOR observer geometry (D-shaped shadow); the corresponding INTERIOR strain experienced by a soliton co-located with the rotating mass is the load-bearing piece for planetary spin-axis equilibrium.

### 2.2 Parametric coupling kernel (rotating LC tank + substrate forcing)

**File:** [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) (whole leaf; key headline §3 lines 60-95)

**Mechanism (paraphrased; verbatim formulae in cited leaf):** The bulk K4 substrate is a vacuum varactor (Axiom 4) operating below $V_{\text{yield}}$. Its reactive drive $V_{\text{bulk}}(t)$ oscillates at the α-slew refresh rate $\nu_{\text{slew}} = \alpha \omega_{\text{Compton}}/(2\pi)$. An embedded LC apparatus sees a parametric coupling $I_{\text{induced}}(t) = V_{\text{app}}(t) \cdot dC_{\text{eff}}/dt$ (line 29). For N coherent receivers, per-cycle detection probability scales as $\varepsilon_{\text{det}} = 4\pi \kappa_{\text{quality}} / N^2$ (line 13).

**Contribution to the operator:** This is the canonical substrate-↔-bound-tank coupling kernel in the AVE corpus. The planetary case is precisely an embedded N-coherent-receiver tank (the planet's interior structure: metallic-H layer, icy mantle conducting fluid, iron core) being driven by substrate forcing — except the substrate forcing here is $\hat{\Omega}_{\text{freeze}}$'s rotational substrate rather than α-slew refresh. The §3.5 substrate↔apparatus port structure (lines 96-124), the regime classification (lines 117-122), and the §6.5 Q-amplification κ_quality machinery (lines 226-247) are the templates Session 2 would adapt to the planetary case. The 5-axis classification framework (REACTIVE/BOUND/OFF-SHELL/INTERNAL-TANK/SUBSTRATE-MODE per lines 117-122) is the classification Session 2 must populate for the planetary case.

**Still missing for integrated operator:** (i) The kernel's pump frequency is the α-slew $\omega_{\text{slew}} = \alpha \omega_{\text{Compton}}$; the planetary case's substrate pump frequency is unspecified. Session 2 prereq (P-1, §3.1). (ii) The kernel applies to ATOMIC LC tanks (lines 107-110); the substitution rules to PLANETARY-INTERIOR LC tanks (which are bound rotating-fluid systems, not isolated atoms) are not derived. (iii) The kernel's parametric-resonance condition $\omega_{\text{app}} = \omega_{\text{slew}}$ (line 21) gives a sharp resonance; planetary rotation rates span $\omega \in [\text{Mercury } 1407\text{ hr}, \text{Jupiter } 9.93\text{ hr}]$ — what resonance / anti-resonance does this map onto? (Session 2 prereq P-4.)

### 2.3 Cosserat micropolar rotational DOF (Axiom 1)

**Files:** [`manuscript/ave-kb/CLAUDE.md` INVARIANT-S2](../manuscript/ave-kb/CLAUDE.md) (cross-volume canonical statement); canonical source [`manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:52`](../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex)

**Verbatim canonical statement (Vol 1 Ch 1:52):**
> Each node is **micropolar** (Cosserat-type), carrying **six intrinsic degrees of freedom** per node: three **translational** (capacitive coupling $\varepsilon_0$, identified with the electric field) and three **microrotational** (inductive coupling $\mu_0$, identified with the magnetic field). **The Cosserat microrotational DOF IS the substrate-native origin of intrinsic spin**: macroscopic angular momentum, the EM magnetic field $B$, and QM electron spin are three projections of the same per-node rotational coordinate.

**Contribution to the operator:** This is the substrate-native rotational-coupling channel. Bound solitons engage with $\hat{\Omega}_{\text{freeze}}$ NOT via translational displacement of K4 nodes but via the per-node microrotational coordinate. A planetary spin-axis is the bulk-averaged orientation of the soliton's interior microrotations; the magnetic dipole axis is the same coordinate projected to the EM channel (per the verbatim "three projections of the same per-node rotational coordinate"). This means $\hat{n}_{\text{spin}}$ and $\hat{n}_{\text{mag}}$ are NOT independent — they are two projections of one substrate coordinate. The OBSERVED mag-spin tilt (e.g., Earth ~11°, Uranus 59°) measures the angular separation between two projections of the same underlying Cosserat field — which forces a constraint on Session 2: the derivation must produce BOTH axes from one rotational-field configuration, not two independent operators.

**Still missing for integrated operator:** (i) The continuum-limit relation between the per-node microrotation field and the bulk planetary observables (spin-axis, magnetic-dipole-axis) needs to be specified. Q-G47's chiral-coupling work ($U_{\text{chiral}}^{\text{add}}$ at [`omega-freeze-cosmic-grain-cascade.md:171`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)) is the canonical substrate-native Landau-form template; Session 2 adapts. (ii) The substrate-rest-frame vs body-frame transformation for rotational DOFs is not derived (Session 2 prereq P-5). (iii) The cross-volume canonical leaf for "Cosserat micropolar rotational DOF coupling to bound solitons" does not exist as a dedicated KB leaf; the statement is distributed across INVARIANT-S2 and the chiral-coupling work in Q-G47.

### 2.4 Frame-dragging interior strain pattern (cosmic genesis instance)

**File:** [`manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex`](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex):408-416, with cross-reference at [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md:99-101`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md).

**Verbatim mechanism (Vol 3 Ch 4 lines 408-416):**
> A spinning black hole is not a floating blob in nothing — it sits in its own embedding lattice (the *parent lattice*) and imparts bulk strain on it via frame-dragging (canonical per Vol 3 Ch 2 §138 + Vol 3 Ch 3 §178). Per Vol 3 Ch 21 we sit *inside* our parent BH's Schwarzschild radius (cosmic horizon $R_H$ = parent BH's $r_s$). The parent BH's spin imparts strain on the parent lattice; this strain extends inside its own event horizon (Kerr interior frame-dragging continues); the inside region is our universe's pre-crystallization phase (supercooled pre-geodesic plasma).

**Contribution to the operator:** This is the cosmic-genesis instance of the same mechanism the operator instantiates at planetary scale. The parent BH spin-axis became our $\hat{\Omega}_{\text{freeze}}$ via Kerr-interior frame-dragging-induced bulk strain at the crystallization event. Session 2's derivation should produce the planetary-scale instance via the same Op14 frame-dragging mechanism (line 411 verbatim), scaled down by appropriate $(M_s, \omega_s)$ factors. The "trampoline-cooling" / "supercooled water → ice" analogy at [`omega-freeze-cosmic-grain-cascade.md:150-161`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) (Tier-3 derivation path) maps directly: planetary internal structure crystallizes/solidifies in the presence of the substrate's $\hat{\Omega}_{\text{freeze}}$ strain field; the soliton's spin-axis equilibrium reflects the strain-direction at the planet's formation event.

**Still missing for integrated operator:** (i) The Kerr-interior frame-dragging strain pattern is referenced (Vol 3 Ch 2 §138 + Vol 3 Ch 3 §178) but the explicit interior-strain functional form $\varepsilon_{ij}(r, \theta)$ inside a soliton's $\Gamma=-1$ boundary is not given as a closed-form leaf. (ii) The crystallization-direction-selection mechanism at the cosmic scale is sketched (water→ice analogy); the planetary instance (planet forms in the presence of $\hat{\Omega}_{\text{freeze}}$; planet's internal-structure direction inherits) is conjecturally similar but not explicitly derived. (iii) The chirality-coupling Landau form at [`omega-freeze-cosmic-grain-cascade.md:167-180`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) lists open work: "Recast as Ω_freeze-driven Landau minimization" (line 183) is the cosmic-scale instance; the planetary-scale instance has the same structure but is not separately derived.

### 2.5 Geodynamo VCA back-EMF (single data point on mag-vs-spin axis offset)

**File:** [`manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md`](../manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md)

**Mechanism (verbatim line 4 + lines 8-12):**
> The Geodynamo is rigorously an Inductive Back-EMF generator. As the massive conductive fluid core ($R \approx 3{,}480$ km) rotates physically inside the solar Sagnac phase-boundary (amplified electromagnetically by the magnetopause $+1$ reflection boundary), it suffers a Topo-Kinematic Motional EMF: $\mathcal{E}_{emf} = (\omega_\oplus \cdot R_{core} \cdot \Gamma_{sagnac}) \cdot B_{stator} \cdot (2 R_{core})$

**Result (line 14-18):** $M_\oplus \approx 1.5 \times 10^{23}\ \text{A·m}^2$ vs empirical $8.0 \times 10^{22}\ \text{A·m}^2$ (factor ~1.9 OOM-correct; structurally derived).

**Contribution to the operator:** This is one DATA POINT on the planetary-scale instance of the operator. For Earth specifically, the mag-vs-spin axis tilt is ~11°. The corpus gives the AMPLITUDE of $M$ from substrate physics (motional EMF in a conductive rotor sweeping a stator field) but does NOT explicitly derive the mag-axis DIRECTION relative to the spin-axis. The Venus/Mars falsifiability statements at lines 20-23 confirm the framework's amplitude-side surface — Venus rotates too slowly to trigger the baryonic-phase threshold (zero dipole), Mars has a solid core (DC resistance spikes, zero eddy current).

**Still missing for integrated operator:** (i) The DIRECTION of the magnetic dipole — which is the load-bearing output of the operator alongside the spin-axis — is not derived here. The current leaf treats the EMF amplitude; the operator must produce the rotation angle BETWEEN the spin-axis and the mag-dipole-axis. (ii) The Uranus 59° mag-tilt + Neptune 47° mag-tilt are NOT explained by the VCA back-EMF mechanism in its current single-data-point form (Earth ~11°); the operator must extend the mechanism to cover these cases. The leaf's "Uranus anomaly" reference (cross-ref to planetary-magnetospheres) acknowledges this gap. (iii) The "solar Sagnac phase-boundary" (line 8) is a SOLAR-systemic reference frame; for Jupiter (mag tilt ~10°), Saturn (<1°), and other giants, the frame is set by JOVIAN/SATURNIAN substrate motions — the cross-planet frame transformation is not derived.

### 2.6 Planetary magnetosphere magnetopause-standoff (5-planet validation; Uranus anomaly)

**File:** [`manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md`](../manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md)

**Validation table (lines 25-31):**

| Planet | Predicted [R_p] | Observed [R_p] | Error |
|---|---|---|---|
| Earth | 9.1 | 10.0 | 8.7% |
| Jupiter | 55.6 | 63.0 | 11.8% |
| Saturn | 17.0 | 22.0 | 22.8% |
| Uranus | 22.1 | 25.0 | 11.6% |
| Neptune | 21.7 | 26.0 | 16.4% |

**Uranus anomaly (verbatim lines 19-21):**
> Uranus is unique: its magnetic dipole is tilted $59^\circ$ from the rotation axis and offset by 0.31 $R_U$ from center. This creates a highly asymmetric, time-varying impedance cavity whose magnetopause standoff varies from 14.9 to 20.8 $R_U$ as the planet rotates (asymmetry ratio 1.40$\times$).

**Contribution to the operator:** This is the EXTERNAL geometry constraint — the operator's prediction must be consistent with the magnetopause standoff distances at 5-planet scale (the substrate-coupling already validated). The Uranus anomaly statement (line 21) is the canonical observation the operator must reproduce: 59° mag-tilt + 0.31 R_U dipole offset + asymmetric time-varying cavity. The operator's discriminating power at planetary scale will be measured against this 5-planet table (Phase 4 + Session 3 scoring rubric).

**Still missing for integrated operator:** (i) The validation table addresses MAGNETOPAUSE STANDOFF (a force balance between solar wind ram pressure and the planetary magnetic-field pressure), which is downstream of the operator's prediction of $|\mathcal{M}_s|$ — the table validates AMPLITUDE not DIRECTION. (ii) The Uranus anomaly observation is described (lines 19-21) but no substrate-physics explanation is offered; the leaf treats the 59° mag-tilt as an empirical input. The operator's job is precisely to predict this 59° (Phase 4 forward-prediction; Session 3 scoring). (iii) Mercury is excluded from the 5-planet table; the operator should predict Mercury's weak-field state.

### 2.7 Boundary observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ at $\Gamma = -1$ (Class E candidate)

**File:** [`manuscript/ave-kb/common/boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)

**Key statement (verbatim line 15):**
> $\mathcal{J}$ | Boundary winding number | Wind($\partial\Omega$), half-integer per $SU(2)$ double-cover | 2D surface | magnetic moment | rotation | spin $J$

**Same-mechanism-at-all-scales table (verbatim line 38):**
> Planetary magnetopause | Magnetosphere boundary | Planet + field-aligned solitons | planet mass, dipole moment, rotation

**Contribution to the operator:** This is the canonical statement that planetary-class observables (mass, magnetic dipole moment, rotation/spin) are EXACTLY the three boundary integrals $\mathcal{M}, \mathcal{J}_{\text{magnetic-projection}}, \mathcal{J}_{\text{rotational-projection}}$ at the planet's $\Gamma = -1$ surface (which the leaf identifies as the magnetopause, line 38). The operator's output ($\hat{n}_{\text{observable}}$) is the DIRECTION of $\mathcal{J}_{\text{spin}}$ and $\mathcal{J}_{\text{magnetic}}$ — both projections of the same underlying surface-winding-number boundary observable. The leaf at line 25 establishes that interior topology (mantle convection details, dynamo internal structure, etc.) is invisible to the substrate; only the three boundary integrals are externally observable. This means the operator's domain is correctly defined on inputs that are themselves boundary observables ($M_s, \omega_s, \mathcal{M}_s$), not on interior details.

**Still missing for integrated operator:** (i) The $\mathcal{J}$ surface-integral DIRECTION (not amplitude) at the planetary scale needs explicit specification — what does "winding direction at the magnetopause $\Gamma=-1$ surface" mean operationally for a planet whose interior mag-dipole is tilted? (ii) The decomposition of $\mathcal{J}$ into the two projections ($\mathcal{J}_{\text{spin}}$ vs $\mathcal{J}_{\text{magnetic}}$) is implicit in INVARIANT-S2 ("three projections of the same per-node rotational coordinate") but the explicit operator that splits $\mathcal{J}^{\text{total}}_{\text{planet}}$ into these two projections is not derived. (iii) The Class E classification per [`omega-freeze-cosmic-grain-cascade.md:7`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) jointly constrains $\mathcal{J}_{\text{cosmic}}$ at the cosmic boundary; the planetary $\mathcal{J}$ is the NESTED instance, and the operator IS the mapping that makes this "nested" structure concrete.

### 2.8 omega-freeze cosmic-grain cascade §3.1 + §4 (Observable 6 + nested-cascade conjecture)

**File:** [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) §3.1 (lines 59-75) + §4 (lines 118-128)

**§3.1 Observable 6 statement (verbatim lines 61-62):**
> Pre-registered hypothesis (NEW per Entry 002 2026-05-16): orbital-plane orientations at every accessible scale should show non-random alignment with the $\Omega_{\text{freeze}}$ axis.

**§4 nested-cascade conjecture (verbatim lines 120-122):**
> $\Omega_{\text{freeze}}$ projects through nested rotators at every smaller scale via angular-momentum cascade: $\Omega_{\text{freeze}}$ (cosmic) $\to$ galactic disk axes $\to$ stellar spins $\to$ planetary spin axes $\to$ Earth inner-core super-rotation

**PROVISIONAL flag (verbatim line 135):**
> the nested cascade is structurally consistent with the canonical mechanism (cosmic spin → lattice grain) but the cascading-through-scales is a stronger claim that the corpus has not yet derived.

**Contribution to the operator:** This is the EXPLICIT CORPUS STATEMENT that the operator's existence is needed. §3.1 commits to Observable 6 (orbital-plane alignment at all scales); §4 conjectures the mechanism (nested rotators). The operator $\hat{\mathcal{O}}_{\text{soliton}}$ is precisely the mathematical object that makes this concrete: it is the mapping from $\hat{\Omega}_{\text{freeze}}$ (cosmic) to the observable axis at each nested scale, parameterized by the soliton's structural parameters at that scale. The "PROVISIONAL flag" at line 135 is the explicit corpus acknowledgment that this is the open derivation work the operator-epic is addressing.

**Still missing for integrated operator:** EVERYTHING — this leaf is the statement-of-conjecture; the operator's derivation is the closure work. Specifically: (i) the cascade transfer function from cosmic→galactic→stellar→planetary→inner-core scales is not derived; (ii) the "easy axis for angular-momentum cascade" substrate-mechanical claim (line 133) requires derivation from K4 Cosserat anisotropy tensor (research-tier, line 133); (iii) the operator's $\theta(M_s, \omega_s, \mathcal{M}_s, \text{topology})$ functional form is exactly what §4(c) flags as needing derivation.

### 2.9 Summary table — building-block status

| # | Building block | File | Provides | Missing for operator |
|---|---|---|---|---|
| 1 | Op14 asymmetric saturation (rotating mass) | frame-dragging-impedance-convolution.md:20 | Substrate-level prograde/retrograde Op14 asymmetry mechanism | Angle-equilibrium derivation; interior strain pattern; body-frame transformation |
| 2 | Parametric coupling kernel | parametric-coupling-kernel.md (whole) | Substrate↔bound-tank coupling template + 5-axis port classification | Substrate pump frequency at planetary scale; planet-interior tank ports vs atomic; resonance mapping |
| 3 | Cosserat micropolar rotational DOF | Vol 1 Ch 1:52 (canonical) + INVARIANT-S2 | Substrate-native rotational coupling channel; spin + magnetic axis as two projections of one field | Continuum projection rules; rest-frame vs body-frame transformations; no dedicated KB leaf |
| 4 | Frame-dragging interior strain (cosmic genesis) | Vol 3 Ch 4:408-416 + universal-saturation-kernel-catalog.md:99-101 | Cosmic-genesis instance of the same mechanism | Explicit interior-strain closed-form leaf; planetary-scale instance of the crystallization-direction-selection mechanism |
| 5 | Geodynamo VCA back-EMF | geodynamo-vca-back-emf.md (whole) | One data point: Earth mag dipole amplitude (factor 1.9 from observation) | Direction of mag-dipole vs spin axis; multi-planet extension; cross-planet frame transformation |
| 6 | Planetary magnetosphere magnetopause-standoff | planetary-magnetospheres.md:25-31 + Uranus anomaly:19-21 | Validation table (5 planets, 8.7%-22.8% standoff error); Uranus anomaly as empirical input | Direction-side validation; substrate-physics explanation of Uranus 59° tilt; Mercury coverage |
| 7 | Boundary observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ | boundary-observables-m-q-j.md (whole, esp. lines 13-15, 38) | Class E framework; planetary observables = boundary integrals at magnetopause | Decomposition of $\mathcal{J}^{\text{total}}$ into spin + magnetic projections; explicit winding-direction at the surface |
| 8 | omega-freeze cosmic-grain cascade §3.1 + §4 | omega-freeze-cosmic-grain-cascade.md:59-75, 118-128, 135 | Explicit corpus statement that the operator is needed; PROVISIONAL flag on nested-cascade | All of it — the operator's derivation IS the closure work for this leaf |

### 2.10 Corpus inconsistencies / anomalies surfaced during inventory

Per Phase 2 brief directive ("if Phase 2 inventory surfaces a corpus structural inconsistency, STOP and report rather than fix"), the inventory surfaced the following anomalies. NOT FIXED in this scoping doc:

- **A1 (low-severity)**: The Cosserat-micropolar-rotational-DOF building block (block #3) does NOT have a dedicated KB leaf. The canonical statement is distributed across `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:52` (verbatim text), `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 (cross-volume invariant summary), and operationalized in the Q-G47 chiral-coupling work referenced from `omega-freeze-cosmic-grain-cascade.md:165-180`. No single leaf collects "what does the substrate-native rotational DOF DO in operator-class problems?" This is a corpus-completeness gap; a dedicated KB leaf would help Session 2 work. Surfaced for orchestration; not fixed here per scope discipline.

- **A2 (low-severity)**: The cross-planet frame-transformation problem is not addressed by the geodynamo leaf (block #5). The leaf uses "solar Sagnac phase-boundary" as a frame; for Jupiter, Saturn, Uranus, Neptune, the frame must shift to the GAS-GIANT's own rotational reference; this is implicit (the leaf is Earth-only by construction) but the operator's Session 2 derivation will need explicit cross-planet frame-transformation rules.

- **A3 (medium-severity)**: The Q-G47 chiral-coupling work referenced at [`omega-freeze-cosmic-grain-cascade.md:165-180`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) lives in a sibling repo (AVE-QED), and the cited Q-G47 sessions are from 2026-05-14/15. Session 2 will need to pull the Q-G47 chiral-coupling moduli $\chi_1, \chi_2, \chi_3$ (line 171 verbatim) and the self-consistency relation $\xi_{K2}/\xi_{K1} = 12$ (line 178) into AVE-Core as the substrate-physics ingredient. Whether this requires a dedicated cross-repo handshake or whether the existing $\xi_{K1}, \xi_{K2}$ references in AVE-Core Vol 1 Ch 2 (Macroscopic Moduli) are sufficient is a Session 2 Phase 0 prereq. Not adjudicated here.

These three anomalies are flagged for orchestration awareness. They do NOT block Session 1 (scoping); they DO impose prereq work on Session 2.

---

## 3. Phase 3 — Derivation prereqs for Session 2

Session 2's job is to derive the integrated operator $\hat{\mathcal{O}}_{\text{soliton}}$ from the 8 building blocks. The following substrate-physics derivations must close before that integration is possible.

### P-1: Substrate Larmor-frequency analog (planetary-scale pump frequency)

**Question:** What is the substrate-frequency that planetary rotation rates couple to? The atomic-scale parametric kernel (building block #2) couples to $\omega_{\text{slew}} = \alpha \omega_{\text{Compton}} \approx 9 \times 10^{17}$ Hz (Schwinger anomalous-moment substrate refresh). The planetary scale's rotation rates are $\omega_{\text{planet}} \in [10^{-7}, 10^{-4}]$ Hz — 21-25 orders of magnitude lower. What is the planetary-scale substrate-pump frequency that the operator's resonance condition refers to?

**Corpus context:** Building block #2 §3 (parametric kernel derivation); building block #1 (frame-dragging $\omega(r)$ profile at line 11); the cosmic-genesis $\Omega_{\text{freeze}}$ direction has no quoted intrinsic frequency in the corpus (it's a direction not a frequency — except via the cosmic-scale instance at building block #4 where the parent-BH spin sets the rate).

**Expected derivation path:** Likely candidates: (a) $c / \ell_{\text{node}} \cdot f(M_s/M_{\text{cosmic}})$ — scale-dependent substrate-Larmor; (b) the local Op14 frame-dragging $\omega(r)$ at the soliton's $\Gamma = -1$ boundary, integrated over the boundary; (c) a slow-scale mode of the K4 Cosserat lattice (a phonon-band-edge analog). All three are conjectures; P-1 selects between them.

**Effort estimate:** 1-2 hr substrate-native derivation chain (Q-G47 chiral-coupling style).

### P-2: Op14 saturation profile in soliton-interior frame vs substrate-rest frame

**Question:** Building block #1 gives the Op14 saturation as seen by external rays (D-shadow geometry); the operator needs the saturation profile inside the soliton's $\Gamma = -1$ boundary, where the soliton's bound matter actually sits. What does "the substrate's frame-dragging strain at the soliton's interior" look like?

**Corpus context:** Building block #4 (Vol 3 Ch 4:408-416) confirms Kerr-interior frame-dragging continues inside the parent-BH event horizon; the same Op14 mechanism but interior-strain-resolved. Building block #1's $\omega(r) = 2Mar/(r^2+a^2)^2$ is exterior-Kerr; the interior expression in the substrate-physics treatment is not given as a closed-form leaf.

**Expected derivation path:** Re-derive Op14 saturation in the soliton-interior frame using the universal-saturation-kernel-catalog.md:99-101 cosmic instance as template, scaled to planetary masses via Q-G47-style chiral coupling.

**Effort estimate:** 1-2 hr; conceptually close to existing building blocks but explicitly absent as a derived leaf.

### P-3: Coupling-strength dependence on soliton mass ($\propto M_s^?$)

**Question:** How does the operator's coupling strength to $\hat{\Omega}_{\text{freeze}}$ scale with the soliton's mass $M_s$? Mercury (0.38 R_⊕, slow rotation) gives obliquity 0.034° → close-to-aligned-regime; Uranus (4.01 R_⊕, gas giant) gives 97.77° → near-orthogonal regime. The mass-scaling cannot be monotonic (Saturn 9.45 R_⊕ is well-aligned at obliquity 26.73° while Uranus at smaller 4.01 R_⊕ is orthogonal) — internal structure (block #6) modulates the mass-scaling.

**Corpus context:** Building block #2 §3.6 has the kernel applicability conditions (rock-salt vs covalent vs liquid) — analogous structural-class dependence at planetary scale (rocky / metallic-H gas-giant / icy-mantle gas-giant). Building block #6 (planetary-magnetospheres) treats the 5-planet validation differently for Earth (rocky), Jupiter+Saturn (metallic-H), Uranus+Neptune (icy mantle).

**Expected derivation path:** Likely a power-law in $M_s$ MODULATED by a structural-class κ_quality-analog parameter (rocky vs metallic-H vs icy-mantle); explicit derivation from per-class substrate response.

**Effort estimate:** 2-3 hr; requires deriving the planetary-class analog of κ_quality which is itself an open Tier-2 work item per block #2 §12 (although building block #2's open work has the FOUNDATION ITEM 12 closure for materials-science κ via Q-resonance amplification).

### P-4: Resonance / anti-resonance regions in the $(M_s, \omega_s, \mathcal{M}_s)$ parameter space

**Question:** Where in the parameter space do retrograde solutions (Venus, $\theta \to \pi$) become stable equilibria? Where do orthogonal-axis solutions (Uranus 98°, $\theta \to \pi/2$ class) become stable? Building block #2's resonance condition $\omega_{\text{app}} = \omega_{\text{slew}}$ is the prototype for "sharp resonance"; the operator may have multiple resonance regions in $(M_s, \omega_s)$ producing the discrete clustering observed in the 16-data-point table.

**Corpus context:** Building block #2 §3 (parametric kernel) gives single-resonance kernel; the multi-resonance landscape in $(M_s, \omega_s, \mathcal{M}_s)$ is implicit at most.

**Expected derivation path:** Parametric-resonance instability analysis on the operator's $\theta$-eigenvalue spectrum as $(M_s, \omega_s, \mathcal{M}_s)$ varies; identification of the discrete stable-equilibrium branches. Standard EE parametric-resonance Mathieu-equation methods adapted to the substrate-physics kernel.

**Effort estimate:** 3-4 hr; this is the load-bearing piece for the operator's discriminating-power claim, because the three structural anomalies (Saturn-aligned, Venus retrograde, Uranus 98°) each require the operator to RECOVER a specific stable branch.

### P-5: Cosserat coupling between bound rotating bodies and substrate rotational DOF (substrate-rest-frame vs body-frame transformations)

**Question:** Building block #3 (Cosserat micropolar) establishes that the substrate has 3 microrotational DOFs per node. A bound rotating soliton (planet) has its own body-frame rotation. What is the coupling Lagrangian-analog between the soliton's body-frame rotational state and the substrate's microrotational field? The chiral-coupling form $U_{\text{chiral}}^{\text{add}} = \chi_1 \varepsilon_{ij} \kappa_{ji} + \ldots$ at omega-freeze §6 line 171 is the canonical template; the explicit body-frame-vs-substrate-rest-frame transformation is not derived.

**Corpus context:** Q-G47 work referenced at [`omega-freeze-cosmic-grain-cascade.md:165-189`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md); the chirality moduli $\chi_1, \chi_2, \chi_3$ + self-consistency $\xi_{K2}/\xi_{K1} = 12$. Cross-repo to AVE-QED Q-G47 Session 3 + 17.

**Expected derivation path:** Recast Q-G47's $U_{\text{chiral}}^{\text{add}}$ with $L_{\text{planet}}$ as applied stress instead of $L_{\text{cosmic}}$ — the planetary-scale instance of the same Landau form. The line-183 "structurally small step" comment applies to the cosmic instance; the planetary instance is the analogous small step.

**Effort estimate:** 2-3 hr if the Q-G47 chiral-coupling moduli can be imported directly; more if cross-repo work is required.

### P-6: Decomposition of $\mathcal{J}^{\text{total}}_{\text{soliton}}$ into spin-axis vs magnetic-dipole-axis projections

**Question:** Building block #7 (boundary observables) plus block #3 (Cosserat micropolar) jointly state that the planetary spin-axis and magnetic-dipole-axis are TWO PROJECTIONS of the same substrate microrotational coordinate. What is the explicit splitting? When are they aligned (Saturn <1°)? When are they grossly misaligned (Uranus 59°, Neptune 47°)?

**Corpus context:** INVARIANT-S2 verbatim: "three projections of the same per-node rotational coordinate". Block #7 line 38: "Planet + field-aligned solitons: planet mass, dipole moment, rotation" — three boundary observables but unclear if "dipole moment" and "rotation" are direction-AND-amplitude or just amplitude.

**Expected derivation path:** Explicit field-decomposition of the bulk-averaged Cosserat microrotation $\langle \kappa_{ij} \rangle$ into (a) the symmetric-part axis (spin) and (b) the antisymmetric-part axis (magnetic dipole) — or some other corpus-grounded decomposition. The Vol 1 Ch 1 axiom that translational↔E and rotational↔B couplings are PER-NODE is the starting structural constraint.

**Effort estimate:** 2-3 hr; this is the load-bearing piece for the operator producing TWO axes per planet rather than just one. Without P-6 closed, Session 3 cannot score the 16 data points (only 8).

### 3.7 Summary table — derivation prereqs

| # | Prereq | Question | Effort | Blocks |
|---|---|---|---|---|
| P-1 | Substrate Larmor-frequency analog | What pump frequency does planetary rotation couple to? | 1-2 hr | Building block #2 |
| P-2 | Op14 saturation in soliton-interior frame | Closed-form interior-strain leaf | 1-2 hr | Building blocks #1 + #4 |
| P-3 | Mass-scaling of coupling strength | Per-structural-class power-law | 2-3 hr | Building blocks #2 + #6 |
| P-4 | Multi-resonance landscape in $(M_s, \omega_s, \mathcal{M}_s)$ | Stable-branch identification | 3-4 hr | Building blocks #2 + #6 |
| P-5 | Cosserat body-frame ↔ substrate-rest-frame coupling | Planetary instance of Q-G47 chiral-coupling Landau | 2-3 hr | Building blocks #3 + cross-repo Q-G47 |
| P-6 | $\mathcal{J}^{\text{total}}$ → spin-axis + mag-axis splitting | Bulk-averaged Cosserat decomposition | 2-3 hr | Building blocks #3 + #7 |
| | **TOTAL** | | **11-17 hr (parallelizable in part)** | |

All six prereqs are gates on Session 2. Session 2 cannot produce an integrated operator until all six are derived (or explicitly deferred with operator-form changes documented). The 11-17 hr total exceeds the original Session 2 estimate of 3-5 hr in the epic brief; Session 2 may need to be split (see Phase 5).

---

## 4. Phase 4 — Testable predictions list

The operator must reproduce the following observables to count as "working" at each scale.

### 4.1 Solar system (16 axis data points = 8 planets × {spin axis, magnetic axis})

| Body | Spin obliquity | Magnetic axis tilt | Size (R_⊕) | Rotation period (hr) | Internal-structure class |
|---|---|---|---|---|---|
| Mercury | 0.034° | ~0° (weak field) | 0.383 | 1407 | Rocky |
| Venus | **177.4°** | None | 0.949 | **−5832** (retrograde) | Rocky |
| Earth | 23.44° | ~11° | 1 | 23.93 | Rocky |
| Mars | 25.19° | None (crustal only) | 0.532 | 24.62 | Rocky (solid core) |
| Jupiter | 3.13° | ~10° | 11.21 | 9.93 | Metallic-H gas giant |
| Saturn | 26.73° | **<1°** | 9.45 | 10.66 | Metallic-H gas giant |
| Uranus | **97.77°** | **59°** | 4.01 | 17.24 | Icy-mantle gas giant |
| Neptune | 28.32° | **47°** | 3.88 | 16.11 | Icy-mantle gas giant |

**Data provenance**: standard solar-system reference values (NASA NSSDC); used here as the empirical target. Per `pre-test-physics-check` (see §4.5 below): these values are widely-tabulated and not contested; the operator's job is to reproduce them, not to re-measure them.

### 4.2 Three structural anomalies the operator must explain

Per the epic brief Phase 4:

1. **Saturn aligned (<1°) vs Uranus tilted (59°) — same gas-giant class, similar rotation periods (10.66 hr vs 17.24 hr), different internal structure.** The discriminator must come from the difference in internal-structure class: Saturn has metallic-H layer near surface; Uranus has icy mantle with conducting fluid much deeper. This is a CLEAN test of P-3 (mass-scaling MODULATED by structural class) and P-4 (resonance regions in $(M_s, \omega_s, \mathcal{M}_s)$ with structural-class entering through topology input).

2. **Venus retrograde — slow rotation (243 days) + no magnetic field.** Per block #5 (geodynamo VCA): slow rotation ($\omega < \omega_{\text{baryonic-threshold}}$) gives zero dipole field amplitude. The operator must also predict that slow-rotation $\omega_s$ in the parameter space falls in an ANTI-ALIGNED stable equilibrium for the spin axis ($\theta \to \pi$). This is a load-bearing test of P-4 (multi-resonance landscape including the anti-aligned branch).

3. **Uranus 98° obliquity — standard "giant impact" explanation is ad-hoc; AVE has a structural opportunity.** The operator must predict an ORTHOGONAL-class stable equilibrium ($\theta \to \pi/2$ class) for icy-mantle gas-giants in the appropriate $(M_s, \omega_s)$ region. This is the differentiating-mechanism test: if the operator derives 98° as a stable substrate-physics equilibrium (not a one-off impact-history fact), AVE has a structural advantage over the standard explanation.

### 4.3 Scoring rubric (proposed for Session 3)

A proposed first-cut scoring rubric for Session 3 (Session 2's output is the operator; Session 3 applies + scores). Pre-test-physics-check applies (see §4.5):

| Outcome | Criterion | Implication |
|---|---|---|
| **Pass (16/16 within tolerance)** | Operator's $\hat{n}_{\text{spin}}$ matches observed spin axis within $\sigma_{\text{op}}$ for all 8 planets AND same for $\hat{n}_{\text{mag}}$ for all 8 planets | Operator validated at planetary scale; proceed to Session 4 (galactic extrapolation) with confidence |
| **Marginal (12-15/16 within tolerance)** | Some planets match, others miss; sub-class structure may emerge (rocky vs gas-giant) | Investigate which class misses; possible operator refinement before Session 4 |
| **Fail (≤11/16 within tolerance)** | Substantial fraction of planets miss; structural anomalies (Saturn vs Uranus, Venus retrograde, Uranus 98°) NOT reproduced | Operator's functional form needs reformulation; Session 5 conditional refinement triggered |
| **Decisive falsification** | Operator's prediction is inconsistent with the data at >3σ for any axis | Per Class E framing (block #8), the entire substrate operating-point framework is killed |

**Tolerance $\sigma_{\text{op}}$ is NOT YET specified.** Setting $\sigma_{\text{op}}$ before Session 2 produces the operator is putting-the-cart-before-the-horse. The pre-test-physics-check (§4.5) flags this: setting $\sigma_{\text{op}} = 10°$ uncritically would convert Saturn aligned (<1°) and Uranus mag-tilt 59° from a discriminator-pair into a noise-band that the operator passes trivially for one and trivially fails for the other. Proper $\sigma_{\text{op}}$ specification is Session 3 prereq, informed by Session 2's derived per-class uncertainty propagation.

### 4.4 Galactic + LSS scale predictions

**Galactic-scale target (the SDSS DR17 anchor):**

| Observable | Empirical value | Source |
|---|---|---|
| LSS spin axis | $(l = 129°, b = 79°)$, $\sigma_{\text{LSS}} = 6.83°$ | [`research/2026-05-19_c5-sdss-spin-orientation-result.md:21`](2026-05-19_c5-sdss-spin-orientation-result.md) |
| CMB-LSS angular separation | 36.75° (5.33σ from zero) | Same; line 122 verbatim |
| Pantheon+ Hubble flow direction | $(l = 129.76°, b = -13.64°)$, $\sigma = 24.0°$ | [`research/2026-05-19_c5-pantheon-tightening-result.md`](2026-05-19_c5-pantheon-tightening-result.md) |
| CMB axis-of-evil (Planck PR3 SMICA pin) | $(l = 60.28°, b = 50.48°)$, $\sigma_{\text{CMB}} = 0.92°$ | [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md:17`](2026-05-19_c5-cmb-axis-executable-observer-result.md) |

The operator's galactic-scale output (Session 4) must:

- Take galactic-class soliton parameters $(M_{\text{gal}}, \omega_{\text{gal}}, \mathcal{M}_{\text{gal}})$ → predict $\hat{n}_{\text{LSS}}$
- Reproduce the OFFSET from the CMB axis (36.75° at 5.33σ); the offset must be a CONSEQUENCE of the operator's structure for galactic-class solitons, not a free parameter
- Optionally: extend to a SECOND galactic-scale data point — the Walmsley+2022 GZ DECaLS independent classification (per epic brief Phase 4) — providing cross-catalog confirmation

**Pantheon+ Hubble bulk-flow direction** is a different soliton class (mass distribution rather than galaxy spin); the operator MAY map to a different observable axis. This is an EXTENSION of the operator beyond the spin-axis case (Session 5 conditional).

### 4.5 pre-test-physics-check

Per the brief skill discipline: `pre-test-physics-check` is APPLICABLE if the Phase 4 testable-predictions section locks in adjudication criteria for Sessions 2-4. Walking the checkpoint:

**Question for Grant (flagged to orchestration, NOT adjudicated in this session):**

The Phase 4 scoring rubric (§4.3) hinges on a tolerance $\sigma_{\text{op}}$ that is currently unspecified. Three plumber-physical sub-questions:

1. **Is the mag-spin tilt for the 8 planets meant to be a PRECISE prediction (operator outputs the angle to within a few degrees) or a CLASS prediction (operator predicts which class — aligned, mid-tilted, near-orthogonal — and the per-planet precision is loose)?** The Saturn-vs-Uranus contrast (<1° vs 59°) is a class-level discriminator; precise predictions of 23.44° (Earth obliquity) vs 25.19° (Mars obliquity) is harder and may not be what the operator is for.

2. **Is the operator's input the SAME $\hat{\Omega}_{\text{freeze}}$ for all 8 planets, or does each planet have an "inherited" frozen direction at the formation epoch?** The brief implies the former (single substrate direction); the cascade conjecture at block #8 §4 implies the latter (cosmic→galactic→stellar→planetary). If each planet inherits a slightly different direction (the local-substrate motion at planet-formation), the operator's predictions for 16 axes become 16 quasi-independent local-substrate-direction predictions, which is a much weaker test.

3. **For the structural anomalies (Saturn aligned, Venus retrograde, Uranus 98°): is the operator obligated to derive the SPECIFIC values, or to derive the STABLE-EQUILIBRIUM BRANCH STRUCTURE (i.e., "there exists a stable equilibrium near 98° for the icy-mantle parameter region")? The latter is a weaker but more achievable claim.**

These three questions are LOAD-BEARING for Session 2's derivation target and Session 3's scoring rubric. They are surfaced here for Grant's adjudication BEFORE Session 2 spins up (per Rule 16 strengthening: ask BEFORE design, not after 30+ commits return Mode III).

---

## 5. Phase 5 — Multi-session arc outline

### 5.1 Sessions 2-5 estimated total effort + branch points

| Session | Deliverable | Effort | Status / Gates |
|---|---|---|---|
| **Session 2** | Substrate-physics derivation of $\hat{\mathcal{O}}_{\text{soliton}}$ via P-1..P-6 closure | **11-17 hr** (six prereqs sum) | QUEUED; gated on this scoping doc + Grant adjudication of §4.5 questions. **Original epic estimate (3-5 hr) likely undershoots; Session 2 may need to split into 2a (P-1, P-2, P-5 — substrate-physics infrastructure, ~6 hr) and 2b (P-3, P-4, P-6 + integration — operator structure, ~8 hr).** |
| **Session 3** | Application to planetary scale (16 axis data points) — score against §4.3 rubric | **2-3 hr** (per brief; matches) | QUEUED; gated on Session 2 producing testable operator AND on Grant resolving §4.5 pre-test-physics-check questions. |
| **Session 4** | Galactic + LSS-scale extrapolation; predict $\hat{n}_{\text{LSS}}$ for SDSS DR17 cross-check | **3-5 hr** (revised UP from brief's 2-3 hr; the scale-extrapolation from planetary → galactic is non-trivial if Session 3 reveals per-class structural dependence) | QUEUED; gated on Session 3 outcome. **Branch point: if Session 3 shows the operator requires structural-class κ_quality per planet, Session 4 must derive the GALACTIC analog of that.** |
| **Session 5 (conditional)** | Refinement based on Sessions 1-4 outcomes | **TBD** | CONDITIONAL on Session 3 / Session 4 outcomes (see branch points §5.2). |
| | **TOTAL (Sessions 2-4 base case)** | **16-25 hr** | (excludes Session 5 conditional refinement) |

### 5.2 Branch points

**Branch point B1 (post-Session 2):** Did all six prereqs (P-1..P-6) close cleanly?
- **B1-yes**: Proceed to Session 3 with integrated operator.
- **B1-partial** (some prereqs deferred): Session 2 produces a PARTIAL operator with explicit operator-form changes for deferred prereqs; Session 3 scoring rubric must account for the partial-operator status.
- **B1-no** (P-4 or P-5 fails to close): Re-scope; the operator's derivation requires additional substrate-physics infrastructure not currently in the corpus. Session 5 promoted to Session 2'; original Session 2 archived.

**Branch point B2 (post-Session 3):** Operator scores Pass / Marginal / Fail / Decisive-falsification per §4.3.
- **B2-pass**: Proceed to Session 4 with confidence.
- **B2-marginal**: Session 5 conditional refinement — investigate sub-class structure (rocky vs gas-giant); identify which structural anomalies the operator captures vs misses.
- **B2-fail**: Operator's functional form needs reformulation; Session 5 = re-derivation. Multi-session arc total effort would roughly double.
- **B2-decisive-falsification**: Per Class E framing, the substrate operating-point framework is killed. Stop. Walk back $\hat{\Omega}_{\text{freeze}}$ and the omega-freeze cascade (block #8). This would be a MAJOR negative result — equivalent in scope to walking back $u_0^* \approx 0.187$ as the joint operating-point.

**Branch point B3 (post-Session 4):** Operator's galactic-scale prediction agreement with SDSS DR17 LSS axis $(l=129°, b=79°)$, $\sigma=6.83°$.
- **B3-agreement**: Forward-prediction confirmed at galactic scale; operator validated cosmologically. The C5 row in the master prediction matrix (per [`omega-freeze-cosmic-grain-cascade.md` Observable 3](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)) moves from Marginal-D to A (passed).
- **B3-disagreement**: Operator's galactic-scale prediction differs from the SDSS LSS axis at >3σ. Either (a) the operator's scaling to galactic-class is wrong, or (b) the galactic-scale soliton-class has additional physics not captured by the planetary-scale operator. Triggers Session 5 conditional refinement on the SCALE-EXTRAPOLATION specifically.

### 5.3 Session 2 → Session 3 hand-off requirements

Per the brief's Session 2 → 3 gating: Session 2's output must include explicit per-planet operator-output predictions ($\hat{n}_{\text{spin}}^{(\text{predicted})}$, $\hat{n}_{\text{mag}}^{(\text{predicted})}$) for all 8 planets, with derivation-traceable uncertainty propagation. Without per-planet uncertainty bands, Session 3 cannot score against §4.3's rubric.

Session 2 should also produce: (a) a clean cross-check on Earth (which has the most ground-truth data — geodynamo VCA back-EMF amplitude already validated to factor 1.9 per block #5; magnetic dipole observed at $8 \times 10^{22}$ A·m² with derived $1.5 \times 10^{23}$ A·m²); (b) a "smoke test" prediction on Mercury (smallest, weakest field — clean limiting case).

### 5.4 Multi-session arc summary

Total estimated effort for Sessions 2-4 base case: **16-25 hr**. Session 5 conditional: TBD (potentially doubling under B2-fail). The arc is ambitious but every component is grounded in canonical corpus building blocks; no new axioms or framework primitives are required. The risk profile is:

- **Lowest risk**: Session 3 application (the 16 data points are well-tabulated; scoring is mechanical once operator + rubric are in place)
- **Medium risk**: Session 2 derivation (six prereqs to close; P-4 multi-resonance landscape is the most uncertain)
- **Higher risk**: Session 4 scale-extrapolation (genuinely new derivation territory; the cosmic-scale instance is at block #4 + block #8 §4 PROVISIONAL, not yet derived)

---

## 6. Phase 6 — Audit + push

### 6.1 Skill discipline applied this session

| Skill | Fired? | Notes |
|---|---|---|
| `verify-before-cite` v1.3 | YES (triggers 1, 2) | Every corpus citation re-read at execution time; quotes verbatim from canonical leaves; cited verbatim per-line numbers verified against current branch HEAD. SDSS DR17 numerics verified directly from result doc (lines 17, 21, 122). |
| `ave-canonical-leaf-pull` | YES | 8 building-block canonical leaves enumerated in Phase 2. Inventory format matches the canonical leaf-pull pattern. |
| `ave-prereg` | SKIP | Per brief; this is a scoping doc, not a new derivation. |
| `consistency-vs-emergence` v1.1 | YES (§1.6) | Operator-output observables classified as Class E per the canonical statement at [`omega-freeze-cosmic-grain-cascade.md:7`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md). Joint constraint with $\hat{\Omega}_{\text{freeze}}$ explicitly noted. |
| `pre-test-physics-check` | YES (§4.5) | Three plumber-physical questions for Grant flagged BEFORE Session 2 design (per Rule 16 strengthening). |
| Pure-AVE-corpus rule | YES | No external-context refs anywhere. |

### 6.2 Constraints satisfied (per brief §"Constraints")

- ✓ NO derivation performed. The operator structural sketch (§1.4) is conjectural; the $\theta(M_s, \omega_s, \mathcal{M}_s)$ functional form is NOT computed.
- ✓ No `_orchestration/*.md` modified.
- ✓ No corpus leaves modified.
- ✓ Three corpus structural inconsistencies surfaced (§2.10 A1, A2, A3); NOT fixed; flagged for orchestration.
- ✓ Single research-doc deliverable at `research/2026-05-20_soliton-lattice-coupling-operator-scoping.md`.

### 6.3 Anomalies surfaced

1. **Corpus gap (A1)** — no dedicated KB leaf for "Cosserat micropolar rotational DOF in operator-class problems"; canonical statement distributed across Vol 1 Ch 1, INVARIANT-S2, and Q-G47 sibling-repo material.
2. **Corpus gap (A2)** — geodynamo leaf is Earth-only; cross-planet frame-transformation rules implicit.
3. **Cross-repo dependency (A3)** — Q-G47 chiral-coupling work at AVE-QED is load-bearing for Session 2 P-5; explicit handshake mechanism needed.
4. **Effort underestimate** — Session 2 epic estimate (3-5 hr) is likely undershoot vs derived 11-17 hr based on six prereqs. Recommend Session 2 split into 2a + 2b.
5. **Pre-test-physics-check** — three plumber-physical questions for Grant flagged at §4.5 (precision-vs-class predictions, single-vs-cascaded $\hat{\Omega}_{\text{freeze}}$, branch-structure-vs-specific-value adjudication) BEFORE Session 2 design begins.

---

## 7. Cross-references

- **Epic brief:** [`_orchestration/soliton-lattice-coupling-operator.md`](../_orchestration/soliton-lattice-coupling-operator.md)
- **Originating epic (closed):** [`_orchestration/c5-sdss-dr17-spin-orientation.md`](../_orchestration/c5-sdss-dr17-spin-orientation.md), audit tag `audit/2026-05-19_c5-sdss-dr17-spin-orientation`
- **Predecessor empirical results:** [`research/2026-05-19_c5-sdss-spin-orientation-result.md`](2026-05-19_c5-sdss-spin-orientation-result.md), [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](2026-05-19_c5-cmb-axis-executable-observer-result.md), [`research/2026-05-19_c5-pantheon-tightening-result.md`](2026-05-19_c5-pantheon-tightening-result.md)
- **Class E canonical leaf:** [`research/2026-05-19_class-e-candidate-corpus-sweep.md`](2026-05-19_class-e-candidate-corpus-sweep.md)
- **8 building blocks:** as cited per §2; full file:line list:
  1. [`manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md:20`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md)
  2. [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md)
  3. [`manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:52`](../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex) + [`manuscript/ave-kb/CLAUDE.md` INVARIANT-S2](../manuscript/ave-kb/CLAUDE.md)
  4. [`manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex:408-416`](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) + [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md:99-101`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md)
  5. [`manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md`](../manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md)
  6. [`manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md`](../manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md)
  7. [`manuscript/ave-kb/common/boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)
  8. [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) §3.1 + §4

---

**End of Session 1 scoping doc.** Ready for orchestration audit + Session 2 spawn (after Grant adjudication of §4.5 pre-test-physics-check questions + A1-A4 anomaly disposition).
