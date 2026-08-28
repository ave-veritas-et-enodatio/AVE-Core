# AUDIT RECORD — asking the Machian-boundary question from AVE first principles, and auditing the KB's answer under the same lens (2026-08-28)

**Status: AUDIT RESULT, FLAG-DON'T-FIX. Nothing here is a ruling, and nothing
in the corpus was edited.** Fifteen repairs were identified and withheld; they
are recorded unadjudicated in §9 so they are auditable rather than silent. The
adjudication routing item is
[`_orchestration/open-items/2026-08-28-machian-form-half-adjudication.md`](../_orchestration/open-items/2026-08-28-machian-form-half-adjudication.md).

**Provenance.** Grant, verbatim (2026-08-28): *"how many nodes are in the
universe? big G is the machian boundary in AVE right? what does that mean
here"*, then — after an orchestrator walk that got the sign of its own
argument wrong — *"ask the question from ave first principles and audit any
claims from the KB under the same critical first principles lense"*.

**The order was the instruction.** Derive what Axioms 1–4 permit **first**,
writing the answer down before opening a cosmology leaf; only then check canon
against it. Starting from canon's formula and testing it for internal
consistency is how a back-solved quantity passes an audit. Lane M1 recorded a
pre-canon derivation to a scratch file with a scored prediction before its
first KB read; that receipt is quoted in §10.

**Scope note, stated up front so the finding is not over-read.** The *value*
of `G` was never at issue and is not in dispute here. Canon states its own
back-solve, unprompted, in at least four shipped places (§6). GR measures `G`
and derives it from nothing; a calibrated coupling is peer, not defect. **What
this audit tests is the mechanism story layered on top of that honest value
label** — the claim that `G` *is* the input impedance of a cosmic transmission
line terminated at the Hubble horizon. That story had never been audited.

---

## §0 — What the audit found, in one page

1. **The headline closure is `x = x`.** `ξ = 4π(R_H/ℓ_node)α⁻²` and
   `ξ ≡ ħc/(7Gm_e²)` are the same expression. `sympy` returns **identically
   zero** for their difference. The operative code computes `H_∞` **from
   CODATA `G`** (`constants.py:755`), so the arrow runs `G → H_∞ → R_H`, the
   exact inverse of the Machian story. The agreement cannot fail, is not a
   check, and carries no content. §2.
2. **Axioms 1–4 supply no outer termination**, and a causal horizon is not an
   impedance discontinuity at all — `Γ = 0` there, because the medium does not
   change. §1.
3. **No termination of any kind produces a coupling linear in cell count.**
   Open and short give purely reactive impedances *periodic* in length; matched
   gives `Z₀` with no length in it. Linear-in-`N` is the DC lumped-ladder
   result — the circuit in which the termination does no work. §1, §4.
4. **The linear count comes from a dropped spherical Jacobian.** Canon's
   integral omits `r'²`. The 3D elliptic operator canon actually ships is
   inner-cutoff dominated: `R_H` enters the near-field coupling at
   `ℓ_node/R_H = 2.894e-39`. It cannot supply a *factor* of `3.456e38`. §1, §3.
5. **The `Γ` cell for the cosmic wall is empty**, its anchor contains no
   termination language by two methods, and the same table asserts two
   incompatible circuits one line apart. §4.
6. **`H_∞` is booked both as today's `H` and as the de Sitter asymptote.**
   Those are exactly the two `Ġ/G` branches. The live branch is excluded by
   LLR at **3393×**; the asymptote branch turns the advertised `0.7%` into
   `+24.4%`. Exactly one survives; canon currently holds both. §5.
7. **The honest verb is EXPRESSED** — a change of variables into substrate
   currency, and a good one. *Derived* was never claimed. **Explained is the
   new casualty.** §6.
8. **One live lead nobody built**: canon asserts a crystallisation front
   propagating at `c` (radius `ct`, numerically horizon-like) and never
   connects it to `R_H = c/H_∞`. §8.

---

## §1 — What the axioms give, derived before any canon read

### Q1/Q2 — nothing bounds the lattice

Axiom 1, verbatim (`manuscript/common_equations/eq_axiom_1.tex:37`):

> "The physical vacuum IS a **chiral Laves K4 Cosserat crystal** — a 3D
> crystallized substrate of nodes at pitch $\ell_{node}$, governed by the
> right-handed $I4_1 32$ chiral space group, with **3-fold ($z=3$) chiral srs
> … nearest-neighbor connectivity**"

That is a connectivity, a pitch, a handedness, and six DOF per node. **It is
not an extent.** A space group is by construction the symmetry group of an
unbounded periodic pattern and contains a translation subgroup of infinite
order; a finite crystal has a point group plus a finite translation set, not a
space group. Axiom 1 has no last row. `:49` adds the only numerical scales the
axiom carries — `Z_0` and `ℓ_node` — both **local line properties**.

Axioms 2–4 add nothing global. Grepping all four axiom files for
`boundar|horizon|infinit|extent|terminat|Gamma` returns three substantive hits:

- `eq_axiom_3.tex:29` — the substrate minimizes `|Γ|²` "at every **internal**
  impedance boundary". The word is *internal*, and the axiom **disfavors**
  reflective boundaries rather than creating one.
- `eq_axiom_4.tex:24` — the BH event horizon at `ε₁₁(r) = 1`.
- `eq_axiom_4.tex:59` — "event horizon = dielectric rupture / perfect shear
  reflector".

**Both Ax4 horizons are keyed on local strain reaching yield.** They are
genuine material boundaries — the medium's constitutive parameters really do
change there — and they live at *high* strain, next to mass. The cosmological
far field is the `A → 0`, `S → 1` limit: the most linear, most homogeneous
region the framework has. **The only material-change mechanism in the axiom set
places its discontinuities at the opposite end of the line from `R_H`.**

Canon states the gap itself, in the ratified source law
(`eq_axiom_5.tex:132`): *"S has no energy→flux map, **G's kappa has no axiom
preimage**, Q is definitional-or-canon."*

### Q3 ★ — a causal limit is not a material boundary

Axiom 3 defines the reflection coefficient (`eq_axiom_3.tex:32`):

```
Γ = (Z₂ − Z₁)/(Z₂ + Z₁)
```

`Z` is a property of **the medium**. The axioms supply exactly two mechanisms
that change a constitutive parameter: Ax4 saturation (`ε_eff = ε₀S(A)`,
`μ_eff = μ₀S(A)` — keyed on **local** strain) and Ax1's crystallized/ruptured
two-phase seam. Both read the node's local state.

A causal horizon reads no local state. It is an integral over light cones —
*which signals reach whom* — and this lattice carries no field that says "a
signal from here arrives." At `R_H`: `ε₀` unchanged, `μ₀` unchanged, `ℓ_node`
unchanged, `z = 3` unchanged. Therefore `Z₂ = Z₁` identically and **`Γ = 0`**.

This is stronger than the "energy leaves and never returns, so it looks
matched" framing the dispatch supplied. **There is no load.** The line
continues into more identical line. The dispatch's framing reaches the right
answer through the weaker door, and the weaker door is worth naming because it
would have left room for an effective-load rebuttal that the substrate does not
in fact permit.

### ★ The result that survives even if you grant canon its wall

| Termination | What it requires of the substrate | `Z_in` | Verdict |
|---|---|---|---|
| **OPEN**, `Γ=+1` | The lattice **stops** — a free surface with dangling bonds | `−jZ₀ cot(βl)` — reactive, **periodic** in `l` | Ax1's space group supplies no last row; Ax3 maximally disfavors it |
| **SHORT**, `Γ=−1` | A different medium — `G_shear→0`, the Ax4 "perfect shear reflector" | `+jZ₀ tan(βl)` — reactive, **periodic** in `l` | REAL in this substrate, but keyed on `A→A_yield`, i.e. at `r_sat`. **Interior.** |
| **MATCHED**, `Γ=0` | Nothing. The medium continues. | `Z₀` — **length-independent** | What a causal limit actually is |

**None of the three is linear in `l`.** Open and short are purely reactive and
periodic with period `λ/2` — they cannot set a real static stiffness at all,
and they run to zero or infinity, not to `N`. Matched has no length in it.
**There is no termination — not one of the three — whose input impedance is
proportional to the number of cells.** Granting a cosmic `Γ = −1` does not
rescue `ξ ∝ R_H`; it gives `jZ₀tan(βl)`.

The one circuit that *does* give impedance linear in `N` is the **lumped series
ladder at DC**: `N` electrically-short cell reactances in cascade,
`Z = N·z + Z_load`, linear in `N` **regardless of the load** — i.e. with the
termination doing no work whatsoever. In that circuit `R_H` is not a boundary
condition. **It is where you stopped counting.**

### Q4 — what selects a radial count over a volume count? Nothing.

Two independent ways to see it.

**(a) The measure.** Canon's integral (verbatim,
`optical-refraction-gravity.md:61`) is `∫₀^{R_H/ℓ} ∮(dΩ/α²) dr'`. The spherical
volume element is `r'² dr' dΩ`. **There is no `r'²`.** With it you get
`(4π/3)N³ = 4.13e115`, a factor `N²/3 ≈ 4e76` different. Dropping the Jacobian
is the single step that converts the 3D problem into a 1D one, and it is argued
nowhere in the leaf.

**(b) The operator's own answer.** The bias law canon ships
(`eq_axiom_5.tex:74-79`) is 3D elliptic: `−∇·[κ D(A) ∇ε₁₁] = 4π T₀₀`. Its
point-source response is

```
∫_a^R dr/(4πr²) = (1/4π)(1/a − 1/R)
```

which **converges**. The outer boundary enters as `ℓ_node/R_H = 2.894e-39`. A
boundary at `R_H` can perturb the near-field coupling by three parts in `10³⁹`.
**It cannot supply a factor of `R_H/ℓ_node = 3.456e38`. The exponent's sign is
inverted relative to what the formula needs.**

---

## §2 — The headline closure is `x = x`

**Orchestrator-verified directly at `a3f4fef7`.** The three lines that matter,
read from `src/ave/core/constants.py`:

```python
:650   XI_MACHIAN: float = HBAR * C_0 / (7.0 * G * M_E**2)
:755   H_INFINITY: float = (28.0 * pi * M_E**3 * C_0 * G) / (HBAR**2 * ALPHA**2)
:758   R_HUBBLE:   float = C_0 / H_INFINITY
```

**`H_∞` is computed from CODATA `G`.** Therefore `R_H ∝ 1/G`, and
`4π(R_H/ℓ_node)α⁻²` is `ħc/(7Gm_e²)` rewritten. By hand, with
`ℓ_node = ħ/(m_e c)`:

```
R_H/ℓ_node = (c/H_∞)·(m_e c/ħ) = m_e c² /(ħ H_∞) = c α² ħ /(28π m_e² G)
× 4π α⁻²   = 4π · cħ/(28π m_e² G) = ħc/(7 m_e² G) = ξ        ∎
```

Symbolic receipt (run this session):

```
sympy.simplify( 4π(R_H/ℓ)/α²  −  ħc/(7·G·m_e²) )  =  0
```

**Identically zero.** Not "agrees to fifteen digits." The Machian identity
**cannot fail**, is not a coincidence, is not a check, and carries no
predictive content. The arrow in the operative code runs `G → H_∞ → R_H` — the
exact inverse of the Machian story, in which the horizon is supposed to set the
coupling.

The tell that was available and missed: a **seven-digit** agreement between `G`
and a Hubble rate that is measured to roughly **1%**.

Canon grades this correctly where it grades it at all. `clm-1klgo2`'s registry
rationale calls the Dirac-LNH and Planck-mass results *"pure algebraic
identities by substitution … carrying zero predictive content. Classification:
identity."* `clm-dsb560` — *"their mutual convergence is **guaranteed by
construction** and is *not* a test."*

**The same holds for the other advertised closures** (lane-reported,
orchestrator spot-checked): `(κ/T_EM)/ξ = 1.0000000000000002`, so
`T_max,g = ξ T_EM = c⁴/7G` is one relation written two ways. And
`1/(7ξ) = G m_e²/(ħc) = α_G` to sixteen digits — the quantity christened the
"Machian dilution factor" at `four-entropy-distinction.md:85` is the electron
gravitational coupling constant under a new name.

---

## §3 — What canon's derivation actually is

The entire forward argument is three sentences and one line of math
(`optical-refraction-gravity.md:54,:56,:61`):

- `:54` — "the effective differential solid angle is modified by the
  cross-sectional porosity ($\Phi_A \equiv \alpha^2$)" — **a `≡`. An
  identification.**
- `:56` — "Integrating the dimensionless radial distance ($r/\ell_{node}$) out
  to the topological horizon $R_H$ over this effective porous solid angle"
- `:61` — `ξ = ∫₀^{R_H/ℓ} ∮(dΩ/α²) dr' = 4π(R_H/ℓ)α⁻²`

**No `Γ`. No reflection. No termination. No impedance discontinuity appears
anywhere in that derivation.** The leaf's only "impedance" hits are the `1/7`
projection and the local `Z = √(μ/ε)` refraction picture.

And the integrand is a **constant**. An integral of a constant is the constant
times the measure. **The "integral" is the product `4π · N · α⁻²` rewritten in
integral notation.** It adds zero content over writing the product — while
supplying, through the choice of measure, the one substantive and unargued step
(§1 Q4).

---

## §4 — The termination story: an empty `Γ`, a dead anchor, and two circuits

The termination language lives entirely in the **translation and taxonomy
layer downstream**, never in the derivation.

### (i) The `Γ` that is not there

`wall-taxonomy.md:164` sets its own column rule: *"`Γ` is the reflection
condition **for that channel only**."* Rows 1–6 and 8 each carry an actual
reflection condition (`−1 short`; `±1`; `−1 from below`; `band edge, v_g→0`;
`gapped branch`; `evanescent below cutoff`; "the **ANTI-wall** — a match, not a
mirror").

**Row 7's `Γ` cell (`wall-taxonomy.md:174`) reads: "far-end **termination** of
the cosmic line."** That is the noun restated. **The leaf whose entire job is to
assign `Γ` per wall names the cosmic termination and never assigns one.**

**Credit where the row earns it**, since this is the sharpest finding and the
row should not be quoted without it: row 7 carries its own inline warning —
*"⚠ **Class:** $G$ is **MIXED — derived-FORM, calibration-fitted-VALUE**;
$\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ embeds $R_H$ and is back-solved from
the empirical $G$. **Not** an independent first-principles determination."*
**The row states the back-solve in the same cell that makes the
input-impedance claim.** The finding is not that canon hides the calibration —
it is that the derived-FORM half it explicitly preserves is the half with the
empty `Γ`.

Row 7 also declares channel = **"all"**, violating the same leaf's mandatory
rule at `:160`: *"Before asserting a wall anywhere: name (i) the **channel**,
(ii) the **axis**, and (iii) the **phase-state**. A claim missing any of the
three is not yet a claim about a wall."*

### (ii) The anchor is empty

Row 7 and `translation-circuit.md:134/:522/:603` all cite
`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md`. Absence check
run **two methods** on that 234-line file — per-token `grep -c`, and an
independent whitespace-flattened Python substring pass that defeats line-wrap
false-negatives. **Both return zero** for `terminat`, `input impedance`,
`transmission line`, `transmission-line`, `R_H`, `reflection`.

What the anchor actually says (`:31`): `ξ` is *"the **cosmic-boundary Sagnac
integration constant**."* That is a **third** description, inconsistent with
both "porosity radial integral" and "input impedance at a termination." Three
pointers, no `Γ`, and the destination describes a different object.

*(Also stale: row 7's second pointer reads "the §6 means-test row at :450".
§6 of `translation-circuit.md` starts at `:501` and the means-test row is at
`:522`; `:450` is a fluid-dynamics subsection heading.)*

### (iii) Two incompatible circuits, one line apart

`translation-circuit.md:134`:

> "| **Machian $G$** | **Distributed transmission-line input impedance at
> Hubble-horizon termination** |"

`translation-circuit.md:135`:

> "| **$R_H/\ell_{node} \sim 10^{39}$** … | Number of **lumped substrate
> cells** along cosmic-scale distributed TL |"

**A lumped-cell count, stated out loud in the same table that calls the result
an input impedance.** Those are the two circuits of §1: the count is the DC
series-ladder reading, the input impedance is the termination reading. Canon
runs both. Only the ladder gives linear-in-`N`, and in the ladder the
termination does nothing.

Reinforced at `vocabulary-register.md:327`: *"`R_H/ell_node` — **NOT a ξ**, a
factor inside ξ_M. Cosmic cell-count ≈ 3.46e38."*

### (iv) `Γ = −1` asserted at `R_H`, against Ax4's own default

`op14-cosmic-horizon-profile.md:20` — *"At $r \to R_H$: $A^2(r) \to 1$,
$S(A) \to 0$, $\Gamma \to -1$"*. But `eq_axiom_4.tex:28` classifies the
**vacuum** as SYM (*"ε and μ saturate together, vacuum K=2G"*), and Ax4's own
table row `:41` reads *"$Z$ (symmetric) | $\sqrt{\mu/\varepsilon} = Z_0$ |
**invariant** | Impedance preserved"* — i.e. `Γ = 0`, the §1 answer.

To reach `Γ = −1` the leaf re-classes the cosmic vacuum as **ASYM-N(ε)** on an
explicit unresolved conditional, `:84`: *"**if** ε-sector saturation reaches
$S_ε \to 0$ before μ-sector saturation does"* — restated as an IF again at
`:23`. And it collides head-on with clause Q (`eq_axiom_5.tex:84`), where the
sourceless substrate sits at *"$\varepsilon_{11} = 0$ away from defects"* — the
**opposite end of the same saturation kernel**, asserted of the same substrate
at the same large `r`.

Neither leaf declares its sector, so the collision is **not adjudicable from
the text** — which is itself the finding, per `wall-taxonomy.md:160`. Marked
UNDERDETERMINED; picking a sector to dissolve it is the cross-wiring failure
mode. It changes nothing about the headline: `Γ = −1` still gives
`jZ₀tan(βl)`, still not linear in `l`.

The leaf self-scopes: `:14` *"**canonical-piece assembly, not new
derivation**"*, `:12` *"**NOT an independent prediction**."* Owning claim
`clm-48g5qf`, solidity **0.45**, build-band **input-only**.

### (v) A correction to lane M3, recorded

M3 offered `four-entropy-distinction.md:20` (*"Γ_horizon = 0 … no EM mismatch
at horizon"*) as corroboration that canon computes `Γ = 0` at the cosmic
horizon. **It does not.** That row's anchors are "Vol 3 Ch 15:19-29 + Ch
21:114" — black-hole orbitals and BH interior. It is the **BH** saturation
surface, not `R_H`.

What it *does* show is worth more: at a wall that is a **genuine material
boundary**, canon computes `Γ_shear = −1`, `Γ_bulk = −1`, **`Γ_EM = 0`** — the
EM channel is matched even at a real wall. **Row 7 claims channel "all" at a
boundary that is not material at all.**

---

## §5 ★ — `H_∞` is booked both ways, and exactly one reading survives

### The prediction

`G = ħc/(7ξm_e²)`, `ξ ∝ R_H`, `R_H = c/H` ⟹ **`G ∝ H`** ⟹
`Ġ/G = Ḣ/H = −(1+q)H` **exactly**. This corrects the standing corpus figure,
which used `|Ġ/G| ~ H₀` and omitted the `(1+q)` factor:

```
Planck18 (H₀=67.4, Ω_m=0.315):  q₀ = −0.5275, (1+q₀) = 0.4725
                                 Ġ/G = −3.2569e-11 /yr
SH0ES    (H₀=73.04):             Ġ/G = −3.5295e-11 /yr
```

A signed number with an explicit `q` dependence, not an order of magnitude.

### The bounds

| Probe | Bound (/yr) | Exclusion |
|---|---|---|
| LLR Biskupek+ 2021, 1σ (primary-fetched, arXiv:2012.12032) | 9.6e-15 | **3393×** |
| LLR 2021, 2σ | 1.92e-14 | 1696× |
| Corpus frozen book value | 1.5e-13 | 217× |
| LLR Hofmann+ 2010 | 3.8e-13 | 86× |
| BBN, Copi+ 2004 | ~3.5e-13 | 93× |
| Pulsar J1713+0747, Zhu+ 2019 | 9.0e-13 | 36× |

**Running-`H` reading: EXCLUDED** by ≥1.5 orders of magnitude across **three
independent probe classes**. Symmetric standard, applied honestly: GR/ΛCDM
predicts `Ġ = 0` and passes trivially, so this is a genuine and unique strain
on the live-keyed reading, not a consensus-bias artifact.

**Fixed de Sitter `H_∞` reading: `Ġ/G = 0` exactly.** Passes everything, on
GR's footing.

### The vise

**Booking A — `H_∞` is today's `H`.** `consistency-manifest.yaml` P23,
orchestrator-verified verbatim:

```yaml
predicted_value: 2.246561628172611e-18
predicted_unit: "s⁻¹ (engine native); ≈ 69.32 km/s/Mpc after × 3.086e19"
observed_value: 69.8
observed_source: "TRGB (late-universe), km/s/Mpc"
error_percent: 0.7
axioms_used: [1, 2, 3, 4]
public_in_readme: true
```

TRGB is a `z≈0` measurement of `H₀`. No asymptote correction is applied.
Reinforced at `optical-refraction-gravity.md:121`, which reads `1/H_∞` as
14.1 Gyr against the 13.8 Gyr age — a **present-epoch** Hubble time; the ΛCDM
asymptotic Hubble time is ~17.5 Gyr — and says it "lies between the modern
Hubble Tension bounds."

**Booking B — `H_∞` is the de Sitter asymptote.** `vol3/claim-quality.md:984`
— `ρ_Λ = 9.03e-27 kg/m³`, *"within a factor 1.54 of the Planck-2018
measurement (**exact in the de Sitter asymptote**)"*. Its own rationale `:1004`
attributes the residual: *"honestly attributed to $\Omega_\Lambda = 0.685 < 1$
(**de Sitter asymptote vs current epoch**)"*.

**Quantified.** `ρ_Λ(AVE) = 3H_∞²/(8πG) = 9.0264e-27`; Planck18
`ρ_Λ = 5.8355e-27`; **ratio 1.5468**, factorising exactly as
`(H_∞/H₀)²/Ω_Λ = 1.0591 × 1.4605`. **The `1/Ω_Λ = 1.4605` piece IS the
asymptote-vs-today conflation — 94% of the residual canon advertises as its
`ρ_Λ` accuracy.**

*(Lane disagreement recorded: M2 got 1.5468, M4 got 1.5374; the synthesizer's
recomputation reproduces M2. Immaterial — both reconstruct canon's "1.54".)*

**These cannot both hold.** Take booking B seriously and P23's comparison
moves: `H_∞ = 69.32` must be scored against the ΛCDM asymptote
`H₀√Ω_Λ = 55.74`, not TRGB 69.8. **The 0.7% becomes +24.4%.** Equivalently,
`H_∞ = 69.32` as a genuine asymptote demands a present-day `H₀ = 83.8`
km/s/Mpc — 14.7% above SH0ES, outside every `H₀` measurement in the tension.
And canon's own stated history ("early matter-dominated deceleration",
`:121`) requires `H_∞ ≤ H₀`, while 69.32 **exceeds** Planck's 67.4.

**The two readings ARE the two `Ġ` branches.** Reading A gives
`Ġ/G = −3.26e-11/yr`, excluded 36×–3393×. Reading B gives `Ġ/G = 0` and
forfeits the `H_∞` headline. Canon currently holds both.

### Does canon confront it? Yes in `research/`. No in `manuscript/`.

A 2026-07-11 lane does this work and does it well:
`research/2026-07-11_astro-adjudicator-sweep_result.md` §A6 books the bounds;
`research/2026-07-11_keying-register-walk_framing.md` §5 lays out three
branches (LIVE / FOSSIL / ATTRACTOR) and names the debt verbatim — *"This
derivation is *owed*, not done."*
`_orchestration/2026-07-10_rulings-docket.md:253` carries it as **BOOKED,
PENDING-GRANT**.

**It never reached canon.** `grep -rln 'naive-live'` over the worktree returns
**exactly 7 files** — three under `research/`, four under `_orchestration/`,
**none under `manuscript/`**. The KB's single `Ġ` reference is
`relational-cancellation-identity.md:318`, in a section titled "Deliberate
exclusions," declaring it out of scope and OWED.

**And the same docket table squeezes from both sides, six lines apart.** Row
G-WHEN: *"LEANS LIVE (retrieval-limited)"* on a direct `a₀(z)` fit. Row G-Ġ:
LIVE excluded 2–3.5 OOM. The escape that satisfies both —
"flatness-protected-live", where the Machian form self-cancels to `Ġ = 0` — is
the item canon itself logs as **underived**. Neither row names the other.

---

## §6 — What survives, and the credit canon has earned

**The honest verb is EXPRESSED.**

AVE **re-expresses** `G` in substrate units: `G = c⁴/(7 ξ T_EM)`, where
`T_EM = m_e c²/ℓ_node` is a real substrate quantity and `ξ` is a dimensionless
number **fixed by `G`**. That is a change of variables, and a good one — it
puts Newton's constant in the same currency as the electron's tension and the
lattice pitch, and it makes the `1/7` trace-reversed projection load-bearing
and checkable. **Nothing in this audit touches the `1/7` projection; it was
not audited and may stand on its own.**

What does not survive:

- **DERIVED** — never claimed. Canon says the back-solve first and unprompted:
  `optical-refraction-gravity.md:52`, `:73`, `constants.py:638`,
  `eq_axiom_5.tex:132`. Not contested by this audit.
- **EXPLAINED** — **no, and this is the new part.** The mechanism story on top
  of the honest value label — *"`G` is the input impedance of a cosmic
  transmission line terminated at the Hubble horizon"* — **had never been
  audited**, and it does not survive Axioms 1–4. The lattice has no far end; a
  causal limit is not an impedance discontinuity; no termination gives a
  coupling linear in cell count; and the 3D elliptic operator canon ships is
  inner-cutoff dominated by 39 orders of magnitude. **The `Γ` cell for row 7 is
  empty because there is nothing to put in it.**
- **IMPORTED** — yes, at value. `G` is CODATA. Canon labels it Class E,
  intentional.

### The symmetric standard, applied both ways

GR measures `G` and derives it from nothing. **A measured coupling is peer, not
defect. AVE is not in trouble for calibrating `G`** — and is in a strictly
better position than GR on the honesty axis, because it says so, in shipped
text, unprompted, in several places.

### Credit, re-verified at `a3f4fef7`

- The 🔴 form-vs-value banner appears at both `optical-refraction-gravity.md:52`
  and `gravitational-coupling-constant.md:10`.
- `constants.py:638-649` declares the circularity **in the operative code**,
  names Chain B′ as the open path, and points at the leaf where it is
  self-stated.
- `clm-1klgo2`'s registry rationale calls its own Dirac-LNH and Planck-mass
  results *"pure algebraic identities … carrying zero predictive content."*
- `clm-dsb560` — *"their mutual convergence is guaranteed by construction and
  is not a test."*
- `clm-nhlo1e` grades the porosity mechanism **0.30, "do not build on, rework
  needed", "Asserted mechanism."**
- `optical-refraction-gravity.md:121` carries a **self-caught overclaim
  repair**: *"(Scope-corrected 2026-06-14: $G$ was previously omitted from this
  'parameter-free' headline … `G` is a third, interlocked input — not an absent
  one.)"*
- The `vol_0` dead-pointer note (`01_theoretical_stress_tests.tex:55-70`) is a
  model of the discipline: it establishes the dead cite **two-method**, quotes
  the KB's contradicting grade verbatim, repairs the pointer, and **explicitly
  refuses** to fix the derivation-grade words — *"FLAG-DON'T-FIX (recorded, NOT
  adjudicated in this pass)."*
- The 2026-05-19 Chain B′ sweep (10 repos, 3 branches, archive) is real
  negative work: *"`XI_MACHIAN` literally inverts the closed-form using CODATA
  G because ξ cannot be evaluated from substrate primitives."*
- **`wall-taxonomy.md:174` states the back-solve inside the very row that makes
  the input-impedance claim** — *"⚠ Class: $G$ is MIXED — derived-FORM,
  calibration-fitted-VALUE … Not an independent first-principles
  determination."*
- **P23's own `notes` field is scrupulous** — it names all five CODATA inputs
  **including `G`**, states the Class-C circularity explicitly ("structurally
  tied to G via the R_H ≡ c/H∞ substitution"), and warns against exactly the
  misreading the public surface invites: *"percent-error averaging across the
  joint observables is meaningful only as ONE data-point about u_0*'s value,
  not N independent successes."*

### ★ Where the honesty stops — a narrower finding than the lanes framed it

**Correction to the synthesizer, made by the orchestrator on direct read.** The
synthesizer listed manifest P23 among "where the honesty stops." That is wrong
about the `notes` field, which is one of the most careful passages in the
corpus (above). **The failure is narrower and worse-placed: the honest content
is in prose, and the machine-readable fields and public surface carry none of
it.**

| Source (honest) | Surface (not) |
|---|---|
| P23 `notes` — names `G` as a CODATA input, states the circularity, warns against counting it as an independent success | Same record's structured fields: `error_percent: 0.7`, `axioms_used: [1, 2, 3, 4]`, `public_in_readme: true`. `axioms_used` is **machine-readable** and asserts an axiom preimage that `eq_axiom_5.tex:132` says does not exist. |
| `clm-wx5324` solidity 0.55, **input-only**; rationale "structurally circular" | `README.md:238` — `\| 23 \| H∞ (Hubble asymptote) \| 0.7% vs TRGB \| ✅ Sits between Planck (67.4) and SH0ES (73) \|`, in a numbered prediction table, **no qualifier**. `LIVING_REFERENCE.md:300` identical. |
| `vol3/claim-quality.md:281` — *"Close the $H_\infty$ dependency so $a_0$ is not downstream of a consistency proof"* | `LIVING_REFERENCE.md:397` — *"This is **NOT a free parameter**"* |
| `10_open_problems.tex:437` — *"structurally an algebraic identity rearrangement … not an independent emergence-class prediction"* | Same file `:11` objectivebox — *"**Resolve the Hubble Tension**"*; `:290` figure caption — *"derived from lattice constants, **zero free parameters**"* |
| `clm-nhlo1e` 0.30 "do not build on"; "not a derivation" | `holographic-paradox.md:12`, `backmatter/01_appendices.tex:75`, `appendices-overview.md:46` — all three still say `Φ_A ≡ α²` **"derived in Chapter 4"**, a pointer canon itself already ruled dead at the fourth site |

**The one-line version.** AVE's ledger for `G` contains exactly one empirical
number — `H_∞ = 69.32` scored against an observed `H` — and that number
consumes three CODATA inputs `{m_e, α, G}` and is read against two mutually
exclusive definitions of what `H_∞` means. The `ξ` integral is not a
derivation; it is a product in integral clothing with the spherical measure
dropped. **Objectiveboxes, figure captions, README rows, and one
machine-readable manifest field are where the honesty stops.**

---

## §7 — The `ξ` factor ledger, and collateral findings

`ξ = 4π (R_H/ℓ_node) α⁻²`. Numbers recomputed from `constants.py` at
`a3f4fef7`:

```
XI_MACHIAN        8.154833696927648e+43     (= ħc/(7·G·m_e²), constants.py:650)
4π·N·α⁻²          8.154833696927643e+43     ratio 0.9999999999999994
N = R_H/ℓ_node    3.455698972907774e+38
R_HUBBLE          1.3344501848536242e+26 m  (= c/H_INFINITY, :758)
H_INFINITY        2.246561628172611e-18 s⁻¹ = 69.3216 km/s/Mpc  (:755, ∝ G)
κ = c⁴/(7G)       1.7289365204831522e+43 N
(κ/T_EM)/XI       1.0000000000000002
```

| Factor | Status | Provenance |
|---|---|---|
| **`4π`** | **ASSEMBLED — and it reaches no observable** | It is the real solid angle `∮dΩ`. But the bias law it feeds carries a **declared** `4π` source convention (`eq_axiom_5.tex:103-111`, per `gordon-optical-metric.md:25`). Since `κ = ξ·T_EM` identically, substituting `ξ` into `−∇·[κD∇ε₁₁] = 4πT₀₀` **cancels the two `4π`s exactly.** The `4π` inside `ξ` has no independent empirical consequence in the gravity sector; it is a bookkeeping split between `ξ` and `R_H`. Honest status: **unconstrained**, neither derived nor wrong. |
| **`R_H/ℓ_node`** | **ASSEMBLED — the Jacobian omission is the whole of it** | Canon's own gloss calls it a count, twice (`translation-circuit.md:135`, `vocabulary-register.md:327`). Linear-in-`N` is the DC series-ladder result, not any termination's `Z_in`. No leaf surfaced argues `R¹` over `R²` or `R³`. Canon's own mass observable is explicitly **3D volume** (`boundary-observables-m-q-j.md:19`), and canon's *other* use of the same porosity factor forces `R²`. |
| **`α⁻²` (via `Φ_A ≡ α²`)** | **ASSERTED — and canon has already ruled the cited pointer DEAD** | The `≡` at `:54` is canon's own; the square is not argued. Three sites still say it was "derived in Chapter 4" (`backmatter/01_appendices.tex:75`, `holographic-paradox.md:12`, `appendices-overview.md:46`). Canon's own 2026-08-02 repair note (`vol_0/01_theoretical_stress_tests.tex:55-70`) establishes **two-method** that this is a dead pointer, that the ONE place `Φ_A` enters is the assertion site itself, and records `clm-nhlo1e`, **solidity 0.30**. Unit problem: `constants.py:477` defines `p_c = 8πα` as a **volumetric** packing fraction — squaring a volume fraction is not how one obtains an areal one. And one porosity factor is used to force two incompatible powers: `R¹` here, `R²` at `holographic-paradox.md:12` ("projected onto the 2D bounding surface area of the causal horizon"). |
| **Which Hubble** | **IMPORTED, and read BOTH WAYS** | `H_INFINITY` is computed **from CODATA `G`** (`constants.py:755`). Not measured, not fitted, not free. See §2 and §5. |

### Collateral findings (lane-reported, synthesizer-recomputed)

1. **An arithmetic error in a downstream build.**
   `four-entropy-distinction.md:20` and `:85` both print
   `4 log 2/(7ξ) ≈ 2.8e-44`. Computed: `4·ln2/(7ξ) = 4.857e-45`. The stated
   number is exactly `16/(7ξ) = 2.8029e-44`; stated/computed = **5.77**. **Two
   sites**, so not a single typo. Owning claim `clm-4o0f0h`, solidity 0.55,
   input-only.
2. **A symbol collision, verified directly.** `T_max,g` is two objects.
   `gordon-optical-metric.md:20` — `T_max,g = ξ T_EM = c⁴/7G` ≈ **1.73e43 N**.
   `electron-unknot.md:17` — *"the scale-invariant baseline topological tension
   $T_{max,g} = \hbar/c$"* ≈ **3.52e-43 kg·m**. Different dimensions, ~86 OOM
   apart, same glyph. `xi-topo-traceability.md` exists specifically to
   de-collide `ξ` and registers nothing for `T_max,g`.
3. **Displayed algebra off by `c²`.** `electron-unknot.md:25` states
   `C_loop = (ħ/c)/(m_e c²) = ħ/(m_e c)`. Computed:
   `(ħ/c)/(m_e c²) = ħ/(m_e c³) = 4.30e-30 m`, not `3.86e-13 m` — **17 OOM**.
   The quoted *result* is right; the displayed algebra is not. Mirrored
   verbatim at `01_topological_matter.tex:116`.

---

## §8 ★ — The one live lead nobody built

**Corrected on orchestrator re-read before commit.** The lanes reported that
canon asserts a crystallisation front *"propagates outward at `c`"* (citing
`lattice-genesis-hubble-tension.md:6`) and **never connects it to
`R_H = c/H_∞`**. **That second half is false as stated**, and the correction
matters more than the original claim.

`op14-cosmic-horizon-profile.md` Key-Results table, "Connection to
crystallisation rate", verbatim:

> "The local-clock vertical tangent at $r = R_H$ **is the substrate-native
> mechanism for $H_\infty$**: new K4 nodes crystallise at rate set by the
> local-clock-modulated propagation through the cosmic-horizon saturation
> boundary"

**Canon does assert the connection.** What it does not do is derive it — and
the assertion runs in **the presupposing direction**: it locates a mechanism
*at* `r = R_H`, taking the radius as given, rather than deriving a front radius
and finding it equals `c/H_∞`. The two ingredients a real derivation needs are
both present in the same leaf — a front propagating at `c` (radius `ct`) and
`R_H ≡ c/H_∞` — and **the step between them is not taken anywhere the sweeps
reached**. The leaf self-scopes accordingly: `:12` *"NOT an independent
prediction"*, `:14` *"canonical-piece assembly, not new derivation."*

**That step is the one place a real derivation might exist that no sweep
surfaced.**
A crystallisation front IS a material boundary in the Ax1 sense: the
crystallized/ruptured two-phase seam, one of exactly two mechanisms the axioms
give for changing a constitutive parameter (§1 Q3). It would carry a genuine
`Γ`. If a front radius is derivably `≈ R_H`, the coincidence becomes
**structural** rather than a conflation, and row 7 gets a real wall — though it
would still have to clear the linear-in-`N` problem of §1, which no termination
solves.

All four lanes stopped short of building the argument, correctly: **building it
IS the withheld repair.**

Note where it points — canon's own declared open item: Chain B′, *"substrate-
local thermodynamic balance for `G` that does NOT route through `R_H`"*
(`constants.py:645-649`, `claim-quality-closure-roadmap.md:38`).

---

## §9 — The fifteen withheld repairs, unadjudicated

**None of these is a recommendation.** They are the temptations, recorded so
they are auditable rather than silent. Nothing in the corpus was edited.

### Held back as edits

1. **Fill in row 7's `Γ`, move it beside row 8 as an anti-wall, or strike it.**
   Refused on canon's own governing rule, `wall-taxonomy.md §10.3`:
   *"**Computed, not chosen.** The authority for a wall's $\Gamma$ phase is the
   branch-derived indicial wall row of a **certified instrument**. Hand-setting
   a sign is an import (the hand-set-perihelion pattern)."* **No cosmic
   instrument exists.** Choosing the sign to dissolve the contradiction would
   be exactly the import §10.3 names. *(Canon also carries an adjacent OPEN
   question at §2.2: "should cold below-cutoff terminations be in a table
   called walls at all?")*
2. Re-score P23 against the ΛCDM asymptote (`+24.4%`), or strip
   `axioms_used: [1,2,3,4]`, or strip `error_percent`.
3. Qualifier text for `README.md:238` / `LIVING_REFERENCE.md:300` / `:397`.
4. Correct `2.8e-44 → 4.86e-45` at the two `four-entropy-distinction.md` sites.
5. Sweep the Vol-2 Ch-10 objectivebox and figure caption — the 2026-05-19
   walk-back landed in the body and missed both.
6. Repair the remaining three "derived in Chapter 4" sites.
7. Correct the docket's exclusion multiples (190×–7600× → 86×–3393×). Refused:
   that row is a **frozen PENDING-GRANT record**, and editing frozen text in
   place is the vacated-cite failure mode. A dated surface-note is the only
   admissible form.
8. Propagate the `Ġ` bounds into the four KB gravity leaves. Refused: the row
   is PENDING-GRANT, and propagating an unruled recommendation makes it look
   ruled.

### Held back as physics calls that are Grant's, not an auditor's

9. ★ **The Jacobian repair is a demolition, not a tune-up.** Restoring `r'²`
   and putting the solid angle in the denominator gives a **convergent**
   accumulation with **no `R_H` in it at all** — which makes `G` a purely
   **local** substrate quantity and simultaneously vacates, as a set: the
   Dirac-LNH derivation, `m_P = m_e√(7ξ)`, `R_H/ℓ = α²/(28πα_G)`, the `H_∞`
   consistency proof, and the `ρ_Λ` closure. **Every one of those is a
   rearrangement of the same relation** (§2). That is a call about what the
   gravity sector *is*. It points where canon's own open item already points:
   Chain B′.
10. **A relabel that saves the arithmetic and drops the story:** stop calling
    `ξ` an input impedance and call it what the integral computes — a radial
    shell-count with equal per-shell weight. Taxonomy relabel, not physics;
    whether the "derived-FORM" half survives it is Grant's call.
11. **The sector call on `clm-48g5qf`.** Neither `op14-cosmic-horizon-profile.md`
    nor clause Q declares which `A` is meant (A1 dilatation? shear? the
    crystallisation order parameter?). Picking one dissolves the collision —
    and inventing the declaration is the cross-wiring failure mode. Flagged
    UNDERDETERMINED.
12. **`op14:20` (`Γ→−1`) vs `:21` (`Z_eff→∞`, an OPEN).**
    `lattice-impedance-decomposition.md:176` offers a two-stage-ramp
    reconciliation, but the leaf never says which stage `R_H` is.
13. **Nobody constructed an alternative forward derivation of `G`.** That is
    Chain B′, canon's declared open problem; inventing one here is the
    "explains-away reconstructs a closed path" failure mode.
14. **The crystallisation-front connection** (§8) — the highest-value next
    read, and the one place a real derivation might live.
15. **Residual empirical content, if any.** Once the definitional loop is
    removed, does `28πm_e³cG/(ħ²α²)` landing inside the measured `H₀` band
    carry anything, or is it the 1937 Eddington–Dirac large-number coincidence
    with a chosen prefactor? **Canon takes the *static* reading of the LNH —
    exactly the branch that avoids the `Ġ` prediction — without saying it is
    doing so.** Dirac's own hypothesis was the *dynamic* reading, and the
    dynamic reading is what the `Ġ` bounds killed. The Brans–Dicke / LNH
    lineage amendment was flagged three times on 2026-07-11 and never landed:
    `grep 'brans'` over `manuscript/` returns **0 files**.

---

## §10 — Method, blind spots, and the receipts

**Structure.** Four independent lanes (M1 what-terminates, M2 `ξ`-factors,
M3 KB-audit, M4 `Ġ/G`) run in parallel with a FLAG-DON'T-FIX charter, then a
synthesizer that **did not take the lanes on trust** — it created its own
detached worktree at `a3f4fef7`, re-read ~25 load-bearing cites, and recomputed
every number from `src/ave/core/constants.py` in-process.

**Order-of-work receipt (lane M1).** M1 read only `eq_axiom_1..4.tex` verbatim,
wrote its first-principles answer to a scratch file (107 lines, **including a
recorded prediction so it could be scored**), and only then opened a cosmology
leaf. This is the discipline the instruction asked for and it is why §1 is not
a rationalisation of §3.

**Absence checks** were run **two methods** throughout: per-token `grep -c`
**and** an independent whitespace-flattened Python substring pass over whole
files, which defeats the line-wrap false-negative that has fired repeatedly in
this corpus.

**What the synthesizer corrected in the lanes.** (a) M3's `Γ_horizon = 0`
corroboration is about the **BH** horizon, not `R_H` (§4 v). (b) M2 and M4
disagreed on the `ρ_Λ` ratio (1.5468 vs 1.5374); recomputation gives 1.5468 and
the disagreement is immaterial. (c) Row 7's second pointer
(`translation-circuit.md:450`) is stale — §6 begins at `:501`. (d) Canon's own
`vol_0` note independently confirms M2's `Φ_A` dead-pointer finding, two-method
— stronger evidence than M2 had.

**What the orchestrator corrected in the synthesizer.** The synthesizer listed
manifest P23 among "where the honesty stops." On direct read the P23 `notes`
field is scrupulous; the failure is that the honest content is in prose while
the **machine-readable** fields and the public README row carry none of it
(§6).

### ★ Blind spots, stated as limits rather than coverage

- **No corpus-wide sweep was run by the synthesizer.** Every enumeration in
  this document is either a lane's — carrying that lane's declared blind spots
  — or one of two targeted absence checks.
- **Declared lane blind spots, carried forward:** M1 did not read all ~320
  files its two sweeps hit; its "no derivation of a cosmic termination exists"
  is scoped to the surfaced sites plus the leaves those cite, and a derivation
  phrased without any of `{terminat*, Gamma, input impedance, transmission
  line, R_H, Hubble, Machian, horizon}` would not have been caught. M3's
  claim-regex **provably missed `clm-dsb560`**; its flattened sweep found 236
  files and read ~18. **M2 left ~45 `src/` and `research/_archive/` `Φ_A` hits
  unread — including two whose names are exactly where a real adjudication of
  the squared form would live: `119_alpha_squared_universal_operator_
  adjudication.md` and `121_plumber_challenge_to_doc120.md`.**
- **Not searched at all:** sibling repos under `AVE-staging/`, git history,
  unmerged branches, PDFs, `.py` docstrings.
- **No "the only", "no leaf", "every", or "none" claim is made about the
  corpus.** Where this document says something is absent, it is absent **from
  the specific file named, under the specific patterns run, by two methods**,
  and it says which.

### The load-bearing premise most worth hitting

§1's composition rule in Q4 — "radial shells in series, angular elements in
parallel" — is a **spreading-impedance intuition shaped by conduction**,
applied to a substrate Axiom 3 insists is lossless-reactive
(`eq_axiom_3.tex:24`). **If that mapping is wrong, the convergence argument
goes with it.** The Q3 result (`Γ = 0` at a causal limit) does **not** depend on
it, and neither does §2.

---

## §11 — The orchestrator's own failed walk, recorded

Between dispatching the lanes and receiving them, the orchestrator proposed in
chat that `ξ` has the shape of a **sphere self-capacitance** — `C = 4πεR`,
linear in `R` — so that the `4π` and the linear cell count both fall out of one
standard electrostatic result and neither is a fitted factor. It was tagged
un-audited at the time. **It is wrong, and it fails on the same step that kills
canon's version.**

A spherical capacitor's capacitance is set by the **inner** radius, not the
outer one:

```
C(a,b)/(4πε) = 1/(1/a − 1/b)        a = ℓ_node, b = R_H
             = 3.861592677242833e-13 m      ← exactly a
C(a,∞)/(4πε) = 3.861592677242833e-13 m
C(a,b)/C(a,∞) = 1.00000000000000000000
outer radius enters as a/b = 2.894e-39
```

`C_horizon/C_node → 1`, not `3.456e38`. **The same `2.894e-39` that §1 Q4
derives from the elliptic operator** — it is the same convergence, reached from
the capacitance side.

It fails a second, independent way: one cannot use `4πεR` for the sphere and
`εℓ` for the node and keep the leftover `4π`. Both normalizations must match,
and then the `4π` cancels.

**The linearity in the walk was real; it was attached to the wrong radius.**
`4πεR` is linear in the radius of the *conductor*, and in this geometry the
conductor is the node.

**Recorded because it is the same class of error the audit found in canon** —
an attractive circuit picture whose dimensional bookkeeping was never worked —
and because the chat-walk-claims-are-un-audited-claims rule fired exactly as
written: it was flagged un-audited, and it died within the hour.

---

## §12 — What this record does NOT establish

- It does **not** show `G` is wrong, mis-valued, or in tension with any
  measurement. `G` is CODATA and nothing here touches its value.
- It does **not** audit the `1/7` trace-reversed projection, which is
  load-bearing elsewhere and may stand on its own.
- It does **not** adjudicate the sector question on `clm-48g5qf`
  (UNDERDETERMINED, §9 item 11).
- It does **not** rule on whether the crystallisation-front connection (§8)
  exists. That is the recommended next read, not a finding.
- It does **not** propose a replacement derivation of `G`. Chain B′ is canon's
  declared open problem and inventing a route here is the failure mode named at
  §9 item 13.
- **It does not claim corpus-wide completeness on anything.** See §10.
