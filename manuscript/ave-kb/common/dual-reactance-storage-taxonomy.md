[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "definitional taxonomy disambiguating V_TOROIDAL_HALO = dual-reactance count (X_L + X_C sectors) from the 6 other V-symbols and the 3 distinct '2's; no new physical claim"
path-stable: "referenced from vol2 Ch2 baryon sector (V_TOROIDAL_HALO meaning), constants.py V_TOROIDAL_HALO docstring, and tensors.py compute_toroidal_halo_volume as the canonical reactance-count-vs-volume disambiguation"
-->

# Dual-Reactance Storage Taxonomy: V_TOROIDAL_HALO = 2 is a reactance-sector COUNT, not a volume

This is a **definitional / no-claim** leaf. It introduces no new physical result; it disambiguates a vocabulary collision and a symbol-overload.

The constant `V_TOROIDAL_HALO = 2` ([`constants.py`](../../../src/ave/core/constants.py):770) appears in the baryon mass eigenvalue `x = I_scalar/(1 − V·p_c) + 1`. The corpus historically named it a geometric **"toroidal halo volume"** and "derived" it via a signed-crossing integral. That framing is a **misnomer** (the signed integral evaluates to 0, not 2; the "FEM-verified 2.001 ± 0.003" has no FEM driver — see [`2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) §3). The "2" is the **dual-reactance count**: the node's TWO reactance sectors (Axiom 1: 3 translational-E DOF → capacitive `X_C`; 3 microrotational-B DOF → inductive `X_L`), each one electron-ground-state unit. This is the SAME E/B conjugate pair the photon uses ([`translation-circuit.md`](translation-tables/translation-circuit.md):35).

This leaf fixes three disambiguations the "volume" misnomer obscured: (1) the symbol `V` is overloaded **7×** in the corpus and must not be read as the same quantity across uses; (2) there are **three distinct "2"s** in this neighborhood that must not be fused; (3) the count is **additive** (energy `E_L + E_C`), not a **signed reactance sum** (`X_L + X_C = 0` at resonance).

## The collision — "V" is overloaded 7×

The glyph `V` carries seven distinct meanings across the AVE corpus. Reading
`V_TOROIDAL_HALO` as "a voltage" or "a volume" because the glyph matches another
use is the error this table prevents. (This is the load-bearing reason the
result doc adopts `X_L / X_C` for the reactance sectors rather than `V_L / V_C`:
`V` is too overloaded to carry the reactance-sector meaning unambiguously.)

| # | Symbol | Quantity | Units | Canonical source |
|---|---|---|---|---|
| 1 | `V_yield` (`V_YIELD`) | dielectric yield voltage `√α·V_snap` | V (≈ 43.65 kV) | [`constants.py`](../../../src/ave/core/constants.py):382; INVARIANT-C1 |
| 2 | `V_snap` (`V_SNAP`) | substrate rupture voltage `m_e c²/e` | V (≈ 511 kV) | [`constants.py`](../../../src/ave/core/constants.py):373 |
| 3 | `V_inc` | **incident** wave amplitude (phase-space coordinate) | V | phase-space pair (A46; Clifford-torus / impedance plane) |
| 4 | `V_ref` | **reflected** wave amplitude (phase-space coordinate) | V | phase-space pair (A46; `Γ = V_ref/V_inc`) |
| 5 | `V_DC` | DC bias point on the Ax4 varactor kernel (operating point $A_0 = V_{DC}/V_{yield}$ is a **per-node** ratio) | V | INVARIANT-S2 (PONDER-05's "0.687 at 30 kV" is the quartz material's voltage-coefficient — consistency-class analog of the kernel SHAPE, NOT a vacuum-kernel reading; `vol4/claim-quality.md:51`) |
| 6 | `V_TOROIDAL_HALO` (`𝒱_total`, legacy `V_halo`) | **dual-reactance COUNT** (this leaf) | dimensionless integer (= 2) | [`constants.py`](../../../src/ave/core/constants.py):770; this leaf |
| 7 | gain term `V·p_c` | loop-gain `βA` in the regenerative-feedback eigenvalue | dimensionless | baryon eigenvalue `x = I_scalar/(1 − V·p_c) + 1` |

Symbols 1–2 are **voltages** (energy thresholds). Symbols 3–4 are **phase-space
wave amplitudes** (the impedance-plane / Clifford-torus coordinates per A46;
their ratio is the reflection coefficient `Γ`). Symbol 5 is a **bias point**.
Symbol 6 is a **dimensionless integer count** (the subject of this leaf), and
symbol 7 is that count used as the dimensionless loop-gain multiplier. Only
symbols 6 and 7 are dimensionless; 6 is the only one that is an integer count.

## The three distinct "2"s

Three numerically-coincident 2's live near this result. They are physically
distinct and must NOT be fused. The shared digit is a coincidence, not an
identity.

| # | The "2" | What it is | Numeric form | Canonical source |
|---|---|---|---|---|
| 1 | **V = 2** | **reactance-sector COUNT** — the X_C sector + the X_L sector, each one electron-unit (this leaf) | integer 2 (a count) | [`constants.py`](../../../src/ave/core/constants.py):770; [`2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) §1 |
| 2 | **K/G = 2** | bulk/shear modulus ratio at the EMT trace-reversal operating point → √2 longitudinal/photon speed ratio | ratio 2 (→ √2) | [`../vol1/claim-quality.md`](../vol1/claim-quality.md):1391 (clm-uu1qbo); [`../vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md):32 |
| 3 | **E_L = E_C** | equipartition of the two reactive energy stores at resonance | ratio 1 (equal) | LC resonance equipartition (this leaf) |

> **Coincidence flag.** The numerical coincidence **V = 2 (count) = K/G = 2
> (modulus ratio)** is NOT a derived identity. They reach the integer 2 by
> unrelated routes — a count of reactance channels vs a continuum-elastic
> modulus ratio. Do not write "the reactance count equals the modulus ratio" or
> imply one derives the other. They are flagged here as a coincidence precisely
> so a future reader does not manufacture a false identity from the shared digit
> — the same failure mode that produced the four false "volume" derivations.

> **Downstream-not-driver note.** `K = 2G` is a **downstream consistency**, NOT
> the driver of α/EM. α comes from the Golden Torus geometry (Vol 1 Ch 8); the
> lattice **sits at** `K = 2G` *given* α (`vol1/claim-quality.md:135,145`;
> `zero-parameter-universe.md:32` — "the EMT argument … is a self-consistency
> check, not an independent derivation of α"). Do not write "K=2G drives the EM
> equilibrium."

## The two reactance sectors — X_L / X_C / E_L / E_C

Axiom 1 (INVARIANT-S2) gives the node 6 DOF: 3 translational → E-field origin →
capacitive storage; 3 microrotational → B-field origin → inductive flywheel
([`translation-circuit.md`](translation-tables/translation-circuit.md):35). These
are the two reactance sectors. The substrate IS an LC network and inherits
standard LC reactance algebra verbatim.

| Symbol | Name | Definition | Substrate origin | Sign / sense |
|---|---|---|---|---|
| `X_C` | capacitive reactance | `X_C = 1/(jωC) = −j/(ωC)` | 3 translational-E DOF (dielectric storage) | negative-imaginary |
| `X_L` | inductive reactance | `X_L = jωL` | 3 microrotational-B DOF (inductive flywheel) | positive-imaginary |
| `E_C` | capacitive stored energy | `E_C = ½ C V²` | electric-field energy | positive-definite |
| `E_L` | inductive stored energy | `E_L = ½ L I²` | magnetic-field energy | positive-definite |

**Symbol choice (why X_L / X_C, not V_L / V_C or E_L / E_C for the sectors).**
`X` (reactance) is the EE-native per-sector symbol and avoids the 7× `V`
overload above. `E` collides with the E-field, `E_yield`, and "energy"
generically. So the sectors are named by their **reactance** `X_L / X_C`; the
**additive count** is cleanest stated via the positive-definite stored energies
`E_L`, `E_C` (next section).

## Signed cancellation — why the count is additive, not a signed sum

This is the load-bearing nuance. At resonance the two reactances **cancel**, so
the "2" cannot be a signed reactance sum.

Standard LC algebra (inherited by the substrate per Axiom 1): `Z_L = jωL`,
`Z_C = 1/(jωC) = −j/(ωC)` — because `1/j = −j`, the two reactances have
**opposite sign**. At resonance `ωL = 1/(ωC)`, so:

- `X_L = −X_C`  ⟹  `|X_L| = |X_C|`  ⟹  **signed sum `X_L + X_C = 0`.**

Therefore **V = 2 is the COUNT of the two reactance sectors, NOT a signed sum**
of their reactances (that sum is 0). The additive "2" is cleanest expressed as
the **stored energy**, which is positive-definite in each sector and equal at
resonance (equipartition):

- `E_L = E_C`  (equipartition, the third "2"'s ratio-1 cousin)  ⟹  the count of
  energy-storing reactance sectors is **2**.

In the eigenvalue `x = I_scalar/(1 − V·p_c) + 1`, the term `V·p_c` reads as
"(2 reactance channels) × (per-channel coupling `p_c`)" — a **count of channels
times a per-channel gain**, i.e. the regenerative-feedback loop-gain `βA`. The
integer 2 (not √2) confirms it is a **discrete channel count**, not the RMS of
two unit channels: the proton mass uniquely selects additive-2
(`V=2 → 1836.117 m_e`; `V=1 → 1423.96`; `V=p_c → 1203.43`; CODATA 1836.153 —
see [`2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) §2).

## V_TOROIDAL_HALO = the dual-reactance count

> **`V_TOROIDAL_HALO = 2` is the dual-reactance count** — the number of the
> node's reactance sectors (1 capacitive `X_C` + 1 inductive `X_L`), each one
> electron-ground-state unit, feeding the proton's regenerative self-consistent
> mass loop. It is a **dimensionless integer count**, NOT a geometric volume.

**Why the legacy name is a misnomer (and what it spawned).** The legacy name
"toroidal halo volume" and the legacy symbol `V_halo` / `𝒱_total` invited four
false geometric "derivations" of the number 2 (all unsound; full audit in
[`2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) §3):

1. **`∫∫∫ sgn(det) = 0`, not 2** — a *signed* great-circle intersection integral
   vanishes by antisymmetry (`s_i → s_i + π` flips `det`'s sign); it cannot equal 2.
2. **Geometric-inevitability §V_halo=2 asserts, does not compute** — labels the
   result "computed analytically" but evaluates no integral (and disagrees with
   the constants.py derivation on whether the circles live on S² or S³).
3. **`tensors.py::compute_toroidal_halo_volume()` hardcodes 2.0** — returns a
   literal while its docstring claims an integration "converges perfectly."
4. **"FEM-verified 2.001 ± 0.003" has no FEM** — a 0.05%-precision claim with no
   finite-element driver in the repo.

The reframe to **reactance count** removes the false-derivation surface
entirely: a channel count is not integrated, it is **counted** — there are two
reactance sectors per node by Axiom 1. The value 2.0 is unchanged and remains
mass-confirmed (§2 of the result doc); only the *meaning* (and the fabricated
volume-derivations) changes.

> **Honest residual.** The count-2 is **CLOSED** (forced reactance count,
> mass-confirmed at exactly 2.000). The per-channel coupling `p_c = 8πα` is a
> **RESIDUAL** — canonical-packing-plausible (algebraically exact given α) but
> its identification as the reactance-loop gain is not line-by-line derived. So
> the baryon ladder is **"1-residual Skyrme"** (1 residual: per-channel p_c) vs
> standard Skyrme's 2 baryon-data-tuned params (F_π, e) — **NOT
> "zero-parameter."** The separate parsimony claim "zero *baryon-data-tuned*
> parameters" (inputs are electron-physics-provenanced) stands.

## τ_yield open item — RESOLVED (2026-06-02): STAYS-INHERITED + dual-branch landing

> **RESOLVED (2026-06-02): STAYS-INHERITED.** The yield event is the electric
> (ε-only) branch — single-sector ([`../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78,
> *"only $\varepsilon_{eff} \to 0$ while $\mu_{eff}$ remains intact … the
> dielectric-rupture branch (electric breakdown)"*); the ×2 is the inherited
> $\mathcal{V}_{total}$ count-tag, **not** an $E_C + E_L$ within-event sum. The
> count-2 manifests at the yield scale as the **two mutually-exclusive
> saturation branches** of the same Axiom-4 kernel (electric → $X_C$ →
> $\tau_{yield}$; magnetic → $X_L$ → rest mass, clm-lv3uw1) — the same
> $X_C + X_L$ count as baryon $\mathcal{V} = 2$. **Class B manifestation; no
> empirical discriminator.**

**The adjudicated question** (Grant 2026-06-02) was *which physical event the
yield is* — (A) first-sector breakdown of a pre-existing node-tank, or (B)
nucleation of a new two-sector defect. The substrate walk landed on **(A)** and
**ruled out (B)**: the master equation makes the two branches **mutually
exclusive** (`master-equation.md:81`, *"they differ in which constitutive
parameter saturates first"*); each self-terminates. The defect-nucleation
outcome (B) invokes — the trapped $\Gamma \to -1$ two-sector knot — **IS the
magnetic branch = rest mass** (`master-equation.md:79`, clm-lv3uw1), not
$\tau_{yield}$; (B) mis-assigns the branch. And $\tau_{yield}$'s own outcome
($Z \to \infty$, open-circuit, opaque) is a voltage-antinode / current-node
boundary — capacitive-dominated, itself single-sector. So the yield-event
physics is **single-sector (electric branch)** and does **not** supply an
"$E_C + E_L$ summed at breakdown" justification for the 2. The value 2 itself
was already **CLOSED** (forced reactance count, mass-confirmed — §"V_TOROIDAL_HALO
= the dual-reactance count" above); only the *provenance* of the ×2 in
$\tau_{yield}$ was open, and it resolves to **inherited** (a count-tag naming
*which two-sector node* this is, not physics-forced by the yield event). The
numerical value ($1.04\times 10^{22}$ Pa) stays canonical and mass-confirmed.
The prior "FEM-verified Borromean halo volume" provenance on the $\tau_{yield}$
sites was fabricated and is dropped.

> **🔴 MAGNETIC-BRANCH = SIGN-SELECTOR, NOT CAGE-MECHANISM (2026-06-18, Rule 12 / PR#260 B3-DEGENERATE — paragraph above ("…IS the magnetic branch = rest mass") and the table below PRESERVED unedited; Grant-ratified).** Where this leaf identifies the **Magnetic** branch ($\mu_{eff}\to0$, $\Gamma=-1$) with **rest mass / Fermion confinement**, the "magnetic branch" is the **chirality/spin SIGN-selector** (μ-first $\Rightarrow \Gamma=-1$ vs ε-first $\Rightarrow \Gamma=+1$ are spin-conjugate signs) and is **MUTE on the mass sector** — NOT the cage *mechanism*. The mass-cage is the **A1 longitudinal dilatation** ($Z_{bulk}\to0 \Rightarrow \Gamma_{bulk}=-1$); the magnetic-vs-electric fork is DEGENERATE on the equilibrium observables ($Z=Z_0\sqrt{S}$, $|\Gamma|=1$ both ways), the asymmetry chirality-set not substrate-forced. The $X_C+X_L$ dual-reactance *count* (the load-bearing point of this leaf) is unaffected; only the "magnetic-branch *builds* the mass" reading is demoted, since wiring confinement into the $X_L$/charge-winding sector would break the two-"3"s orthogonality (A1 ⊥ T2, `master-equation.md:20`). Body preserved per Rule-12.

**The landing (the real result): the dual-branch unification.** The count-2
*does* live at the yield scale — as the **two mutually-exclusive saturation
branches of the same Axiom-4 kernel**, which **are** the two reactance sectors:

| Branch | Saturates | $Z$, $\Gamma$, boundary | Reactance sector | Outcome |
|---|---|---|---|---|
| **Electric** (`master-equation.md:78`) | $\varepsilon_{eff} \to 0$ ($\mu$ intact) | $Z \to \infty$, $\Gamma \to +1$, open | **$X_C$** (capacitive / translational-E) | **$\tau_{yield}$** (dielectric breakdown) |
| **Magnetic** (`master-equation.md:79`, clm-lv3uw1) | $\mu_{eff} \to 0$ ($\varepsilon$ intact) | $Z \to 0$, $\Gamma \to -1$, short | **$X_L$** (inductive / microrotational-B) | **rest mass** (Fermion confinement) |

The branch↔sector identification is **canonical, not asserted**: the magnetic
branch is named the **inductive / microrotational-B** sector at
[`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md):464
(*"substrate microrotational sector hits Ax 4 yield on the inductive branch …
magnetic-branch saturation; clm-lv3uw1"*) and `:526`; the electric branch is its
capacitive / translational-E complement. So **each branch literally IS one
reactance sector reaching its Axiom-4 yield** (clm-lv3uw1) → the yield-scale "2"
= the $X_C + X_L$ count = the same count as baryon $\mathcal{V} = 2$
([`../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md)).

> **Shown identity, NOT the forbidden fusion.** Tying the yield-scale "2" to the
> $X_C + X_L$ count is a **derived identity** (each branch *is* one reactance
> sector at its Ax-4 yield, clm-lv3uw1), not a manufactured coincidence. It must
> still be held apart from the other "three distinct 2's" above (§"The three
> distinct '2's"): this is the **reactance-sector count**, NOT $K/G = 2$
> (modulus ratio) and NOT the $E_L = E_C$ equipartition ratio-1. The chord it
> lands: the dual-reactance count threads from the baryon (fm) through the two
> saturation branches that split **yield vs mass** — it unifies $\tau_{yield}$
> *and* rest mass, a stronger result than "yield scales with the count" would
> have been.

> **🔴 $X_L$ = the FLYWHEEL (spin/frequency-regulation) sector, NOT the rest-mass store (2026-06-20, Rule 12 — the "magnetic → $X_L$ → rest mass" gloss at ~:164, the §"branch" table row at ~:198, and all bodies above PRESERVED unedited; Grant-ratified mass-sector ruling; EXTENDS the 2026-06-18 PR#260 B3-DEGENERATE banner above).** Where this leaf glosses the **Magnetic** branch ($\mu_{eff}\to0$) inductive sector "$X_L$" as **rest mass**, the **$X_L$ = the inductive FLYWHEEL = the T2 / Cosserat micro-rotation ($\omega$) frequency-regulation (spin) sector** — the local frequency regulator / Park-dq FOC rotating frame, whose mass-gap is the Compton/Larmor *clock* gap, **NOT** the rest-mass store. The **rest mass is the A1 longitudinal DILATATION** (the $X_C$-side / bulk-dilatation depression, $Z_{bulk}\to0$; [`master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20 "A1 dilatation-MASS"), held at $90°$ to T2 by the FOC orthogonal decoupling (**A1 ⊥ T2**; canonical [`helium-symmetric-cavity.md`](../vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md):52-56). The flywheel regulates the *frequency that SETS* the mass (Compton $f = mc^2/\hbar$ → A1 depression depth); mass stays A1.
>
> **V=2 SAFETY (verified, load-bearing).** This re-scope touches the **descriptive label only**, never the **count**. The baryon mass eigenvalue `x = I_scalar/(1 − V·p_c) + 1` reads `V·p_c` as "(**2 reactance channels**) × (per-channel coupling `p_c`)" — a **count of channels** (§"The two reactance sectors", ~:110–116; `V=2 → 1836.117 m_e` vs CODATA 1836.153). Both sectors still exist, each one electron-unit, so **`V = 2` is UNCHANGED**; the eigenvalue depends on the count, not on the "$X_L$ = rest mass" identification. The "unifies $\tau_{yield}$ *and* rest mass" chord above is re-read as "unifies $\tau_{yield}$ (electric/$X_C$-branch yield) *and* the two-sector node that carries the A1 rest mass" — the dual-reactance count still threads from baryon to electron. Body preserved per Rule-12.

**Classification (consistency-vs-emergence, no promotion past canonical
ceiling).** The dual-branch landing is **Class B axiom-manifestation**: the two
branches are already canonical (`master-equation.md:77-81`, clm-lv3uw1); the new
content is the *identification* branch↔sector↔baryon-count, near-definitional
given the sector definitions. **Not** Class 2 emergence; **not** a new empirical
prediction. Observable axis: **Class 4 consistency** — the sector count is not
empirically variable. Resolved 2026-06-02 (`research/2026-06-02_tau-yield-reactance-count.md`
§7); tracked at the τ_yield claim-quality entries
([`../vol1/claim-quality.md`](../vol1/claim-quality.md) clm-8ep2b4;
[`../vol4/claim-quality.md`](../vol4/claim-quality.md) clm-o2shcn). The separate
vol1 open item (whether a proton-provenanced reactance count belongs in a
*macroscopic / cosmological* formula at all) is distinct and remains tracked at
clm-8ep2b4.

## Cross-references

- [`2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) — the result doc: dual-reactance mechanism (§1), mass-discriminator (§2), the four false-volume-derivation audit (§3), honest "1-residual Skyrme" status (§4).
- [`2026-06-02_fabricated-FEM-walkback-and-tau-yield-fork.md`](../../../research/2026-06-02_fabricated-FEM-walkback-and-tau-yield-fork.md) — the fabricated-FEM walk-back + τ_yield Bucket-A finish (Grant 2026-06-02): drops the fabricated "FEM-verified" label on the τ_yield sites, propagates the dual-reactance reframe, and names the yield-scales-with-count open item (§3).
- [`translation-circuit.md`](translation-tables/translation-circuit.md):35 — Axiom-1 E/B conjugate-storage decomposition (3 translational-E → capacitive; 3 microrotational-B → inductive); §4.5 EE Analytical Tool Tracker carries the baryon-self-feedback ↔ regenerative dual-reactance LC loop row; §6 means-test carries the mass-discriminator entry.
- [`self-consistent-mass-oscillator.md`](../vol2/particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md) — the baryon mass eigenvalue (Vol 2 canonical).
- [`../vol1/claim-quality.md`](../vol1/claim-quality.md):1391 — K=2G → √2 longitudinal/photon speed ratio (clm-uu1qbo); the SECOND distinct "2" (do not fuse with V=2).
- [`../vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md):32 — K/G=2 is downstream-of-Golden-Torus consistency, not an α derivation.
- [`constants.py`](../../../src/ave/core/constants.py):770 — `V_TOROIDAL_HALO = 2.0` (docstring reframed to dual-reactance count on `analysis/baryon-v2-reactance-scrub`).
- [`tensors.py`](../../../src/ave/topological/tensors.py):40 — `compute_toroidal_halo_volume()` (docstring reframed: returns the dual-reactance count, not an integration).
