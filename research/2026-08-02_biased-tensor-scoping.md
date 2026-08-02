# The DC-biased small-signal tensor at the iso-bond point — W1-RESOLUTION SCOPING + PILOT

**Date:** 2026-08-02 · **Lane:** implementer · **Branch:** `research/biased-tensor-scoping`
**Grade:** **SCOPING + PILOT. Draft bins are NOT FROZEN** — the follow-on prereg freezes them.
**Grant GO (2026-08-02, verbatim `[sic]`):** *"7, GO"* — on the W1-resolution path ratified in the
walk: the vacuum sits at the **energetics-derived iso-bond point** $\rho_{bond}=1$ (knob-free per the
#516 Axiom-3 minimisation), whose bare $K<0$ instability is stabilised by a **DC operating-point
pre-stress** — the pressurized-vessel picture (Grant, verbatim `[sic]`: *"I agree smells like DC op
point"*) — with each band riding the **SMALL-SIGNAL** tensor about that bias.
**Pilot driver:** `src/scripts/vol_1_foundations/biased_tensor_iso_bond_pilot.py`
**Pilot output (tracked):** `research/2026-08-02_biased-tensor-scoping_pilot.json`
**Docket fragment:** `_orchestration/docket-entries/2026-08-02-biased-tensor-scoping.md`

---

## ★ HEADLINE — the pilot moved the question, and it moved it in the direction Grant named

Three results, all computed on the **merged, validated** cold Born-Huang pipeline imported
**unmodified** (`srs_elastic_tensor.py`; no new stencil, no new solver):

1. **A symmetric DC bias provably CANNOT stabilise anything** — and it does not need to. Under
   $S_{axial}=S_{shear}=S$ the tensor is the cold tensor uniformly $S$-scaled (#519 degree-1
   homogeneity), so $K_{acoustic}=S\cdot K_{cold}<0$ for **every** $S>0$ and Zener stays $1.000$ to
   $1.6\times10^{-15}$. **Confirmed numerically over the whole sweep $A_0\in[0,0.999]$.**
2. **An asymmetric bias CAN buy $K>0$, and the pilot prices it:** near the iso-bond point
   $A_{Zener}-1 \simeq (\rho_{eff}-1)/8$ and the transverse-branch fractional speed spread
   $\simeq(\rho_{eff}-1)/16$. Buying $K_{acoustic}>0$ costs $\rho_{eff}\ge2$, i.e. **Zener
   $=1.0889$ and a $4.24\%$ shear-branch speed split.** So the tension the brief asked to map is
   real and exactly quantified — **within the swapped-springs model, isotropy and $K_{acoustic}>0$
   are mutually exclusive.**
3. **★ But the object being stabilised is not what the merged docs say it is.** The Born rank-2
   bond tensor is **not rotationally invariant** unless its shear spring $k_s$ **is** a bond
   pre-tension $\tau=k_s\ell$ (pilot P1: a rigid rotation costs energy $4.000$, exactly
   $\tfrac12 k_s\sum_b|\Omega \mathbf r_b|^2$; it costs $-2\times10^{-17}$ at $k_s=0$). Reading
   $k_s$ that way — which the corpus is **already forced into**, and #526 already found the same
   projector identity from the other direction — the reference state carries an **isotropic
   tension** $\sigma_0=(1/3V)\sum_b k_s\ell_b^2 = 0.176776695$, and at $\rho_{bond}=1$ the **entire**
   acoustic tensor is that pre-stress and nothing else:
   $$C_{11}=C_{44}=-C_{12}=\sigma_0 \quad(\text{agrees to } 1.2\times10^{-9}),$$
   with the second-order (Brugger) elastic tensor **identically zero**. The Birch↔Brugger split
   then gives, **exactly at every $\rho$ probed** (max error $1.1\times10^{-8}$):
   $$\boxed{K_{\text{thermodynamic}}(\rho_{bond}) = (\rho_{bond}-1)\cdot\frac{\sigma_0}{3}}$$
   **⇒ at the iso-bond point the intrinsic bulk modulus is ZERO, not negative.** The published
   $-0.0589$ is exactly $-\sigma_0/3$: the **initial-stress offset**, i.e. the dead-load Birch
   combination of a **pre-tensioned membrane**, not a bulk modulus of the medium. And the phonon
   spectrum is **positive-definite at every wavevector** (P4: $\min\lambda(D(q))=+5.18\times10^{-3}$
   over 2000 seeded $q$; structurally $D(q)=L(q)\otimes I_3$ **exactly**, $\lVert\cdot\rVert=0.00$,
   a positive-semidefinite graph Laplacian).

**Plumber form.** At the iso-bond point the vacuum is not a stiff solid with a broken bulk modulus.
It is a **pre-tensioned membrane / cable net** — a pressure vessel whose wall has no stiffness of
its own, held out by whatever supplies the pressure. Waves on it are taut-membrane waves: exactly
isotropic, exactly non-dispersive at leading order, and **all three polarisations travel at the same
speed**. "K < 0" is what you get if you insist on reading a membrane's wave coefficients as a
solid's bulk modulus. **The stabilisation question is therefore not "what flips the sign of K"; it
is "what supplies and regulates the pressure, and what stiffens the marginal bulk channel at higher
order" — Grant's DC-op-point / pressurized-vessel picture, now with the marginality located
exactly.**

> **Scope fence, stated up front.** This is **SCOPING + PILOT**, not a derivation and not a claim.
> **Zero corpus files modified.** No claim minted, no `clm-`/`def-`/`sup-` node created, no solidity
> changed, no manual landed (the auditor lane lands manuals). The bins in §8 are **NOT FROZEN**.
> Everything below is **within the engine-native BORN rank-2 bond model on the ratified chiral
> srs-z3 carrier** — the three-way Born/Keating/`clm-bjceop` bond-model discrepancy flagged at
> `research/2026-07-04_srs-elastic-tensor_result.md`:247–275 is **INHERITED and still open**, and
> §6 records how much of this survives a different bond model.

---

## §0 — SECTOR DECLARATION (mandatory header, before any standard-physics word)

| Axis | Declaration |
|---|---|
| **Which sector?** | **Translational-$u$ (Cauchy) sector** of the ratified chiral **srs-z3** net (I4₁32, Wyckoff-8a, 8 sublattices × 3 DOF, $z=3$). Both $k_a$ and $k_s$ are translational-$u$ **capacitive** springs — the axial STRETCH and the transverse SHEAR of the *same* bond. **NOT** the $\varepsilon$-vs-$\mu$ photon pair (#519 header, verbatim). Cosserat couple-stress = Stage 2, **not invoked** (it does not enter the $k\to0$ Cauchy slopes, `axiom4-moduli`:24). |
| **Does the engine carry that DOF?** | Yes — `cauchy_bloch_D` / `acoustic_christoffel` on `build_srs_net`, merged and validate-on-known'd at #506 §1 (simple-cubic, diamond-Born-vs-symbolic, isotropy; all PASS). The pilot imports them **unmodified**. |
| **Cold or saturated?** | **Both, and they are separated arms.** P0/P1/P4 are **COLD** (saturation OFF). P2/P3 are **SMALL-SIGNAL about a DC bias**, Op14/Ax4 saturation ON, $S(A)=\sqrt{1-A^2}$ via `ave.axioms.scale_invariant.saturation_factor`. |
| **Mode / regime / phase-state** | Quasi-static long-wave about a DC operating point (varactor picture, INVARIANT-S2). Sub-yield on the interior; $A\to1$ is the yield-wall limit, approached but not claimed. |
| **Coords (A46)** | Operating-point knob $(A_{axial},A_{shear})$ in **phase-space / reactance**; tensor readout $\omega(k)\to C_{ij}\to K,\ A_{Zener}$ in **real-space / spatial-Brillouin**. Each measured in its own matching coordinate. No $\varphi^2$/winding comparison anywhere. A46-clean on both axes. |
| **Class (consistency-vs-emergence)** | **CONSISTENCY** (P0, P2, P3, P4) + **IDENTITY/MECHANISM** (P1 — the pre-stress reading is an algebraic identity of the bond model, not an emergence claim). **EMERGENCE FORBIDDEN for every value here.** $\sigma_0$, $\rho^\ast=9.7734$, $2/7$, $\sqrt{10/3}$, $2$ are **read-off comparison constants the sweeps never fit to**. α enters ONLY through the read-off $A=\sqrt\alpha$ core-amplitude comparison row and is off every verdict path. |

---

## §1 — THE STABILIZATION QUESTION

### §1.1 — First: the object to be stabilised, carved three ways (the load-bearing correction)

The merged corpus carries one number and one word for what is actually **three distinct
statements**. Verbatim, the two sites:

- `research/2026-07-04_srs-elastic-tensor_result.md`:135–137, verbatim `[sic]`:
  *"**K (bulk modulus) is NEGATIVE for ρ < 2** — mechanically unstable (the lattice would collapse
  under hydrostatic pressure). **K = 0 EXACTLY at ρ = 2**"*; and `:144–145`, verbatim `[sic]`:
  *"**The only A = 1 point is ρ = 1**, where **K < 0 (unstable)**"*.
- `research/2026-07-04_parent-condition-match-forces-balance_result.md`:48–53, verbatim `[sic]`:
  *"the match point ρ_bond=1 is mechanically **UNSTABLE** (bulk modulus K<0 …). The photon's
  zero-reflection point is a **lossless-reactive operating point** … NOT a stable static elastic
  solid."*

The pilot separates the three:

| Statement | Object | Value at $\rho_{bond}=1$ | Status |
|---|---|---|---|
| **(i) Dynamical stability** — are all phonon frequencies real? | $\lambda(D(q))$ over the whole BZ | $\min\lambda = +5.183\times10^{-3}$ over 2000 seeded $q$; structurally $D(q)=L(q)\otimes I_3$, a **positive-semidefinite graph Laplacian**, so $\ge 0$ **everywhere** | **STABLE.** No instability at any wavevector. |
| **(ii) Intrinsic bulk stiffness** — the second-order (Brugger) $K$ | $K_{th}=(C_{11}+2C_{12})/3$ on the **stress-free-referred** constants | $K_{th} = 0$ **exactly** (measured $\lvert K_{th}\rvert\le5\times10^{-10}$) | **MARGINAL, not negative.** |
| **(iii) Dead-load hydrostatic response** — the Birch combination the merged docs report | $K_{ac}=(C_{11}+2C_{12})/3$ on the **acoustic (Birch)** constants | $-0.058926 = -\sigma_0/3$ | **NEGATIVE — and it is exactly the initial-stress offset.** |

The relation the pilot verifies is the standard initial-stress split (Birch / Wallace), here derived
directly from the bond model rather than cited: with $\sigma^0_{ij}=\sigma_0\delta_{ij}$ the
reference tension,
$$C^{ac}_{11}=C^{th}_{11}+\sigma_0,\qquad C^{ac}_{12}=C^{th}_{12}-\sigma_0,\qquad
C^{ac}_{44}=C^{th}_{44}+\sigma_0 ,$$
which is the textbook $B_{11}=C_{11}-P,\ B_{12}=C_{12}+P,\ B_{44}=C_{44}-P$ at **$P=-\sigma_0$**
(the reference state is in **TENSION**, not compression). Hence
$K_{ac}=K_{th}-\sigma_0/3$, and the pilot's exact closed form
$K_{th}=(\rho_{bond}-1)\sigma_0/3$ reproduces **every** published K value in #506's table (§2, P1)
including the $K=0$-at-$\rho=2$ "stability floor", which is now identified as the point where
$K_{th}=+\sigma_0/3$ exactly cancels the dead-load offset — **a property of the loading device, not
of the medium.**

> **ρ-CONVENTION GUARD (binding on every number in this document).** Every $\rho$ here is the **srs
> swapped-spring** $\rho = k_a/k_s$ — the convention in which $K_{acoustic}=0$ at $\rho=2$ and
> $K=2G$ at $\rho^\ast\approx9.7734$. It is **not** the moduli-model / buckling $\rho$ (the $z=4$
> Keating convention that puts $K=2G$ at $\rho=2$). The corpus carries this disambiguation
> explicitly at `manuscript/ave-kb/common/axiom-register.md` §"ρ-CONVENTION DISAMBIGUATION",
> verbatim `[sic]`: *"The two ρ's SHARE the symbol across carriers … they are not the same
> coordinate."*

**Why the pre-tension reading is FORCED, not chosen** — *within the Born rank-2 model, and see
FLAG-4 for the competing reading the corpus already carries*. Pilot arm P1(a): an infinitesimal
**rigid rotation** of the net costs harmonic energy $4.000000$ under $\Phi_b=k_a\hat d\hat d+k_s(I-\hat d\hat
d)$ with $k_a=k_s=1$ — exactly $\tfrac12 k_s\sum_b\lvert\Omega \mathbf r_b\rvert^2$ — and costs
$-1.96\times10^{-17}$ (machine zero) at $k_s=0$. **A rotationally invariant force-constant model
must return exactly zero.** The Born rank-2 model therefore is not rotationally invariant *as a
standalone harmonic model*; it becomes invariant precisely when the $k_s(I-P)$ term is read as the
transverse projection of a bond **tension** $\tau=k_s\ell$, whose first-order work against the
second-order shortening $\delta\ell=-\tfrac12\lvert\delta u_\perp\rvert^2/\ell$ cancels it. **There
is one alternative and only one: accept a genuine absolute rotational frame** — which is exactly the
reading the corpus already carries, and which **FLAG-4** puts to Grant rather than resolving. (This
is the same fact Keating's angle-bend model exists to avoid, and it is the missing half of #506's
three-way bond-model flag.) **Independently corroborated:** PR #802 measured the same thing on a
different driver — `research/2026-07-28_subc-kubc-bracket_result.md`:70, verbatim `[sic]`:
*"`E(rigid rotation, 1e-3) = 1.984e-3 > 0`; `born_model_confirmed_rotations_cost_energy = True`"*.

**Corpus cross-check, from the other direction.** #526 (`research/2026-07-04_prestress-tensor_result.md`:29–31)
already found the identical projector identity, verbatim `[sic]`: *"The transverse string-tension
term `(T/ℓ)(I−d̂d̂ᵀ)` has the **SAME PROJECTOR STRUCTURE** as the shear spring `k_s(I−P)`, so the
pre-stressed force-constant matrix is **EXACTLY the cold matrix with a shifted shear spring**
`k_s → k_s + T/ℓ`."* This scoping adds the converse and the forcing: **the cold $k_s$ is itself
already a $T/\ell$**, so #526's $k_s+T/\ell$ is the *total* bond tension over length and its remapped
coordinate $\rho' = S_{ax}/(S_{shear}+T/\ell)$ is exactly $\rho'=k_a\ell/\tau_{total}$. The two
results are **consistent and mutually explanatory** — #526's "family survives, dictionary breaks" is
structural once tension and shear spring are recognised as one slot.

### §1.2 — Candidate map (enumerated honestly, including the ones that fail)

Six candidates. For each: what the #519 identity says the small-signal tensor becomes, and whether
transverse-$u$ isotropy (Zener $=1$) survives.

#### **S1 — Hydrostatic / symmetric DC bias via the Ax4 kernel** ($S_{axial}=S_{shear}=S(A_0)$)

- **What #519's identity says.** $\rho_{eff}=\rho_{cold}\cdot(S_{ax}/S_{sh})=1$ unchanged; the whole
  tensor is the cold tensor **uniformly $S$-scaled** (degree-1 homogeneity, #519 VS2).
- **Does the ratio move?** **No** — exactly, by construction.
- **Does it flip $K$?** **No, on both readings.** $K_{ac}=S\cdot(-\sigma_0/3)<0$ for every $S>0$;
  $K_{th}\equiv0$. Pilot P2 confirms over $A_0\in[0,0.999]$: sign never flips, $\lvert K_{th}\rvert
  \le5.0\times10^{-10}$.
- **Isotropy?** **SURVIVES exactly** — $\lvert A_{Zener}-1\rvert\le1.6\times10^{-15}$,
  $\lvert c_L/c_T-1\rvert\le10^{-9}$, at every bias point.
- **Verdict: CLOSED as a stabilisation route** — but *it is not needed*, because under the §1.1
  carve the medium at $\rho=1$ is marginal, not unstable. What symmetric bias actually does is
  **depressurise the vessel**: $\sigma_0\to S\sigma_0$ (pilot: $0.176777\to0.007904$ at $A_0=0.999$).
  It softens the tension without touching any ratio. That IS the physical content of the SYM row.

#### **S2 — Asymmetric bias** ($S_{axial}\neq S_{shear}$)

- **What #519's identity says.** $\rho_{eff}=S_{ax}/S_{sh}$ moves off 1; the tensor is the cold
  tensor evaluated at $\rho_{eff}$, absolute scale softened.
- **Does it flip $K$?** **Yes**, at a price: $K_{th}>0$ for **any** $\rho_{eff}>1$
  ($K_{th}=(S_{ax}-S_{sh})\sigma_0/3$, verified exactly); $K_{ac}>0$ only for $\rho_{eff}>2$.
- **Isotropy?** **BROKEN, and the pilot prices it** (P3): $A_{Zener}-1\simeq(\rho_{eff}-1)/8$
  (measured slope $0.124990$) and the transverse fractional speed spread
  $\simeq(\rho_{eff}-1)/16$ (measured one-sided secant $0.0625$).
- **The exact trade.** To buy $K_{ac}>0$ you must reach $\rho_{eff}=2$, where **$A_{Zener}=1.08889$
  and the shear branches split by $4.24\%$**. To buy only $K_{th}>0$ the price is infinitesimal —
  but so is the stiffness bought.
- **Verdict: WORKS but is priced in isotropy**, and the price is paid in exactly the observable
  item 21 asks about. This is THE tension the brief asked to map, and §1.3 is its resolution.

#### **S3 — The pre-stress the model is ALREADY carrying (the pressurized vessel)** ★

- **What it is.** Not an added bias: the reference state's own isotropic tension
  $\sigma_0 = (1/3V)\sum_b k_s\ell_b^2$, forced by rotational invariance (§1.1). At $\rho_{bond}=1$
  the acoustic tensor is **nothing but** this: $C_{11}=C_{44}=-C_{12}=\sigma_0$, $C^{th}\equiv0$.
- **Does it flip $K$?** It **relocates** the question. $K_{th}=0$: the medium is **marginal** in the
  bulk channel, so second-order elasticity cannot decide stability — the decision moves to (a) the
  boundary/loading condition and (b) third-order (anharmonic) terms the harmonic Born model does not
  carry.
- **Isotropy?** **SURVIVES exactly, and for a stronger reason than Zener $=1$** (see §1.3).
- **Verdict: the load-bearing candidate.** It is exactly #519's explicitly-OMITTED channel **(a)**
  (`saturated-elastic-tensor_result.md`:27–28, verbatim `[sic]`: *"**(a) initial/residual stress**
  (the bias pre-loads the bonds → a nonzero reference stress that shifts the effective moduli beyond
  spring-softening)"*), and it is Grant's *"DC op point"* read.

#### **S4 — Self-arrest of the $K<0$ mode (spontaneous condensation)**

- **What it would be.** If the bulk channel were genuinely unstable, the unstable mode would grow and
  self-arrest at finite amplitude, generating a spontaneous DC bias.
- **What the pilot says.** **The premise fails at $\rho_{bond}=1$.** There is no quadratic bulk
  instability to condense: $K_{th}=0$ exactly, and the second variation of the elastic energy in the
  dilatation channel vanishes identically. The energy for a homogeneous dilatation $\varepsilon$ is
  $W = 3\sigma_0\varepsilon + 0\cdot\varepsilon^2 + O(\varepsilon^3)$ — **linear**, so the arrest
  amplitude is set entirely by the $O(\varepsilon^3)$ term, i.e. by the **anharmonicity of the bond
  law**, which the harmonic Born force-constant model does not contain.
- **Verdict: NOT COMPUTABLE in this model, and honestly so.** What is needed is named: a bond
  potential $U(\ell)$ with a third derivative, not another sweep of $(k_a,k_s)$. Any estimate of a
  condensation amplitude from the present machinery would be manufactured.

#### **S5 — External boundary / cosmological loading**

- **What it is.** The pre-tension $\sigma_0$ must be balanced by something: a pressure-bearing
  content, or a closed (boundary-free) topology in which the net's tension is self-balanced.
- **Why it is not a side option.** Because $K_{th}=0$, **the boundary condition IS the stability
  criterion.** Under a *dead* hydrostatic load the Birch criterion applies and gives $K_{ac}<0$
  (runaway); under *controlled volume* the medium is neutrally stable at second order; under a
  *pressure-bearing content with its own nonzero bulk modulus*, the composite is stable and the wall
  contributes only tension. These are three different physical vessels and the pilot cannot choose
  among them — **the choice is physics input, i.e. a walk question** (§7 V3).
- **Isotropy?** Unaffected — a hydrostatic boundary load is isotropic by construction.
- **Verdict: the residual, and the real frontier object.** This is where "what pressurises the
  vessel" lives.

#### **S6 — Bias-induced BOND-LENGTH shift (geometry), i.e. #519's OMITTED channel (b)**

- **What it is.** In the pre-tension reading, $k_a$ and $k_s$ are not two independent springs: they
  are $U''(\ell)$ and $U'(\ell)/\ell$ — the **curvature and the slope of ONE bond potential at ONE
  operating length**. So
  $$\rho_{bond}(\ell)=\frac{\ell\,U''(\ell)}{U'(\ell)}=\frac{d\ln U'}{d\ln \ell},$$
  a pure function of the DC operating length. A bias that shifts $\ell$ moves BOTH channels along a
  **one-parameter curve set by the bond law** — it cannot move them independently.
- **★ What $\rho_{bond}=1$ then MEANS.** $\rho=1 \iff U'\propto\ell \iff U\propto\ell^2$: the
  iso-bond point is **the zero-rest-length linear spring**. That is exactly why the dynamical matrix
  factorises as $k\,L(q)\otimes I_3$ (P4) — a zero-rest-length spring net's energy
  $\tfrac{k}{2}\sum_b\lvert \mathbf x_i-\mathbf x_j\rvert^2$ is a scalar quadratic form, blind to
  bond orientation.
- **Does it flip $K$?** It is the only channel that can move $\rho_{bond}$ **without** an ad-hoc
  asymmetric $S$-assignment — so it inherits S2's isotropy price, but with the asymmetry now
  *derived from a bond law* instead of assigned.
- **Verdict: OPEN and the most derivable of the six.** It converts "which $S$-channel does gravity
  load?" into "what is $U(\ell)$, and where does the DC operating point sit on it?"

### §1.3 — The isotropy question, answered more strongly than Zener $=1$

The brief asks whether transverse-$u$ isotropy survives each candidate. The pilot's P4 arm makes the
answer sharper than the Zener number:

**At $\rho_{bond}=1$ the vector elasticity problem collapses to a SCALAR problem.** Measured:
$\lVert D(q) - L(q)\otimes I_3\rVert/\lVert D(q)\rVert = \mathbf{0.00}$ — *bit-exact*, at every
sampled $q$, where $L(q)$ is the ordinary 8×8 scalar graph Laplacian of the srs net. Consequences,
all measured:

- **All three polarisations are degenerate at EVERY $q$ in the zone**, not merely in the long-wave
  limit: worst relative intra-triple spread $2.4\times10^{-15}$ over 2000 seeded $q$ (control at
  $\rho_{bond}=3$: $0.279$ — the instrument sees the difference).
- **$c_L = c_T$ exactly.** Direction-averaged $c_L/c_T = 1.000000000$ at $\rho=1$ (vs $1.8209$ at
  $\rho^\ast=9.7734$).
- **Zener $A=1$ is a SYMMETRY THEOREM here, not a numerical coincidence.** Once the problem is
  scalar, its long-wave coefficient is a **rank-2** tensor $D_{ij}$, and on a cubic net a rank-2
  symmetric tensor is forced $\propto\delta_{ij}$. So $A_{Zener}=1$ and $\Gamma_{internal}=0$ hold
  **exactly, for any cubic bond geometry** — which upgrades #516's knob-free minimiser result
  (`:119–120`, verbatim `[sic]`: *"the minimum is at ρ_bond = 1 (k_s = k_a), knob-free … Γ_min =
  1.54×10⁻⁸ = machine-zero"*) from a numerical minimisation on srs to a **structural theorem**.
- **Internal-strain relaxation contributes exactly zero at $\rho=1$** (affine vs relaxed Christoffel
  agree to $6\times10^{-9}$, the pipeline's finite-difference floor).

**⇒ For S1, S3, S5 (all isotropic loadings) Zener $=1$ survives exactly. For S2 and S6 it does not,
and the pilot gives the slope.** There is no middle: any bias that moves $\rho_{eff}$ off 1 by
$\delta$ buys anisotropy $\delta/8$, immediately.

---

## §2 — THE PILOT (numbers; deterministic, driver-regenerable, shipped JSON)

Driver `src/scripts/vol_1_foundations/biased_tensor_iso_bond_pilot.py`; output
`research/2026-08-02_biased-tensor-scoping_pilot.json` (tracked). Seed `20260802`. Canonical
constants only (`ave.core.constants.ALPHA`, `ave.axioms.scale_invariant.saturation_factor`); the
merged cold pipeline imported unmodified. Console receipt:

```
P0 cold recovery PASS (max dev 3.30e-06)
P1 sigma_0 = 0.176776695; pure-prestress dev 1.18e-09; closed-form K_thermo err 1.12e-08
P1 rigid-rotation energy (Born, k_s=1) = 4.000000 (central-force-only = -1.96e-17)
P2 sign(K_acoustic) ever flips: False; max|K_thermo| 4.97e-10; max|Zener-1| 1.55e-15
P3 dZener/drho at iso-bond = 0.124990; K_acoustic>0 first at rho_eff=2.0
P4 ||D - L(x)I3||/||D|| = 0.00e+00; worst triple spread 2.40e-15 (control rho=3: 0.279);
   min eig D(q) = 5.1827e-03
```

### P0 — cold recovery (positive control, HALT-gated)

Reproduces the merged #506 $\rho=1$ row (`srs-elastic-tensor_result.md`:125, verbatim `[sic]`:
*"| 1.000 | +0.1768 | −0.1768 | +0.1768 | **−0.0589** | 1.000 | (K=0 pole) |"*) to
$3.3\times10^{-6}$ — the residual is the 5-significant-figure rounding of the published literals
(computed $C_{11}=0.176776696$), not a disagreement. Gate $5\times10^{-6}$, disclosed.

### P1 — the pre-stress identity (the load-bearing arm)

| Quantity | Measured | Meaning |
|---|---|---|
| Rigid-rotation harmonic energy, Born $k_a=k_s=1$ | **$4.000000$** | $= \tfrac12 k_s\sum_b\lvert\Omega \mathbf r_b\rvert^2$ exactly ⇒ **not rotationally invariant** as a standalone spring model |
| Same, central-force only ($k_s=0$) | $-1.96\times10^{-17}$ | machine zero ⇒ the violation is entirely the $k_s$ term |
| $\sigma_0=(1/3V)\sum_b k_s\ell_b^2$ (closed form, geometry only) | **$0.176776695$** | $=1/(4\sqrt2)$ on srs ($12$ bonds, $\ell=1$, $a=2\sqrt2$) |
| $\sigma^0_{ij}$ max off-diagonal | $6.9\times10^{-18}$ | the reference stress is **isotropic** (cubic ⇒ $\sigma_0\delta_{ij}$) |
| $\max\lvert(C_{11},C_{12},C_{44})-(\sigma_0,-\sigma_0,\sigma_0)\rvert$ at $\rho=1$ | $1.2\times10^{-9}$ | at $\rho=1$ the acoustic tensor is **pure pre-stress** |
| Internal-relaxation contribution at $\rho=1$ (affine vs relaxed) | $\le6\times10^{-9}$ | relaxation contributes nothing at the iso-bond point |
| $\max\lvert K_{th}-(\rho-1)\sigma_0/3\rvert$ over $\rho\in[0.5,10]$ | $1.1\times10^{-8}$ | the closed form is **exact** |

The Birch↔Brugger split, over the same $\rho$ grid #506 published (every $K_{acoustic}$ column
below reproduces #506's own table):

| $\rho_{bond}$ | $C_{11}$ | $C_{12}$ | $C_{44}$ | $K_{acoustic}$ (#506's "K") | $K_{thermo}$ | $(\rho-1)\sigma_0/3$ | $C_{11}^{th}$ | $C_{44}^{th}$ | Zener |
|---|---|---|---|---|---|---|---|---|---|
| 0.50 | +0.123744 | −0.194454 | +0.147314 | −0.088388 | −0.029463 | −0.029463 | −0.053033 | −0.029463 | 0.9259 |
| **1.00** | **+0.176777** | **−0.176777** | **+0.176777** | **−0.058926** | **$0$** | **$0$** | **$0$** | **$0$** | **1.0000** |
| 1.52 | +0.218440 | −0.151646 | +0.195016 | −0.028284 | +0.030641 | +0.030641 | +0.041663 | +0.018239 | 1.0539 |
| 2.00 | +0.252538 | −0.126269 | +0.206239 | $0$ | +0.058926 | +0.058926 | +0.075761 | +0.029463 | 1.0889 |
| 3.00 | +0.318198 | −0.070711 | +0.220971 | +0.058926 | +0.117851 | +0.117851 | +0.141421 | +0.044194 | 1.1364 |
| 5.00 | +0.441942 | +0.044194 | +0.235702 | +0.176777 | +0.235702 | +0.235702 | +0.265165 | +0.058926 | 1.1852 |
| 9.7734 | +0.727855 | +0.323150 | +0.248756 | **+0.458052** | +0.516978 | +0.516978 | +0.551079 | +0.071980 | 1.2293 |

> **⚑ FLAG (surfaced, NOT fixed) — an arithmetic residual in the merged #506 table.** The published
> $\rho^\ast$ row (`srs-elastic-tensor_result.md`:132) reads
> *"| **9.7734** | +0.7279 | +0.3232 | +0.2488 | +0.4308 | **1.229** | **+0.2857 = 2/7** |"*. That
> row's own $C_{11},C_{12}$ give $K=(0.7279+2\times0.3232)/3 = \mathbf{0.45805}$, not $0.4308$; the
> re-run gives $0.458052$; and the row's own $K/G_{Hill}=2.0000$ requires $0.458052$
> ($G_{Hill}=0.229031$). **Every other row in that table is internally consistent** (checked at
> $\rho = 0.5,\ 1,\ 1.52,\ 2,\ 3,\ 5,\ 5.305,\ 7,\ 10$). This is an isolated transcription residual
> in the K column of one row; **no conclusion in #506 rides on it** ($\nu=2/7$, $K/G=2$, Zener
> $=1.229$ are all unaffected). Routed to the auditor lane; **this lane edits no corpus file.**

### P2 — SYMMETRIC bias sweep (the brief's arm: does symmetric bias change sign(K)?)

$S_{axial}=S_{shear}=S(A_0)=\sqrt{1-A_0^2}$:

| $A_0$ | $S$ | $\rho_{eff}$ | $\sigma_0^{eff}$ | $K_{acoustic}$ | $K_{thermo}$ | Zener $A$ | $c_L/c_T$ | $C_{44}$ (abs) |
|---|---|---|---|---|---|---|---|---|
| 0 | 1.000000 | 1.0000000000 | 0.176777 | −0.0589256 | $-3.9\times10^{-10}$ | 1.0000000000 | 1.000000000 | 0.176777 |
| $\sqrt\alpha$ = 0.085425 | 0.996345 | 1.0000000000 | 0.176131 | −0.0587102 | $-1.6\times10^{-10}$ | 1.0000000000 | 1.000000000 | 0.176131 |
| 0.300 | 0.953939 | 1.0000000000 | 0.168634 | −0.0562114 | $-5.0\times10^{-10}$ | 1.0000000000 | 1.000000000 | 0.168634 |
| 0.500 | 0.866025 | 1.0000000000 | 0.153093 | −0.0510310 | $+4.0\times10^{-10}$ | 1.0000000000 | 1.000000000 | 0.153093 |
| 0.900 | 0.435890 | 1.0000000000 | 0.077055 | −0.0256851 | $-1.5\times10^{-10}$ | 1.0000000000 | 1.000000000 | 0.077055 |
| 0.990 | 0.141067 | 1.0000000000 | 0.024937 | −0.0083125 | $+2.0\times10^{-11}$ | 1.0000000000 | 1.000000000 | 0.024937 |
| 0.999 | 0.044710 | 1.0000000000 | 0.007904 | −0.0026346 | $-2.3\times10^{-11}$ | 1.0000000000 | 1.000000000 | 0.007904 |

**Read:** the sign of $K_{acoustic}$ **never flips** (it cannot: $K_{ac}=S\cdot K_{cold}$,
$S>0$); $K_{thermo}$ is **identically zero** to $5\times10^{-10}$; **Zener stays $1.000$ to
$1.6\times10^{-15}$ and $c_L/c_T$ stays $1.000$**. The *only* thing a symmetric bias changes is the
**pre-tension magnitude** $\sigma_0\to S\sigma_0$ and, with it, every absolute modulus — the
"floppy-near-yield" axis #519 §4 already identified, here re-read as **depressurising the vessel**.

### P3 — ASYMMETRIC bias: the anisotropy price of buying $K>0$

$S_{shear}$ held at the cold value, $S_{axial}$ stiffened (the assignment-mirror is the reflection
about $\rho_{eff}=1$; magnitudes at leading order are assignment-independent):

| $\rho_{eff}$ | $K_{acoustic}$ | $K_{thermo}$ | Zener $A$ | T-branch spread | $c_L/c_T$ |
|---|---|---|---|---|---|
| 1.000000 | −0.058926 | $0$ | 1.0000000 | $2.5\times10^{-8}$ (floor) | 1.000000 |
| 1.000001 | −0.058926 | $+5.9\times10^{-8}$ | 1.0000001 | $7.5\times10^{-8}$ | 1.000000 |
| 1.001 | −0.058867 | +0.000059 | 1.0001250 | $6.25\times10^{-5}$ | 1.000198 |
| 1.010 | −0.058336 | +0.000589 | 1.0012453 | $6.22\times10^{-4}$ | 1.001971 |
| 1.100 | −0.053033 | +0.005893 | 1.0120416 | $5.98\times10^{-3}$ | 1.019068 |
| 1.500 | −0.029463 | +0.029463 | 1.0521739 | $2.54\times10^{-2}$ | 1.084857 |
| **2.000** | **$0$** | +0.058926 | **1.0888889** | **$4.24\times10^{-2}$** | 1.153328 |
| 3.000 | +0.058926 | +0.117851 | 1.1363636 | $6.34\times10^{-2}$ | 1.268322 |
| 9.7734 | +0.458052 | +0.516978 | 1.2293216 | $1.019\times10^{-1}$ | 1.820946 |

**Local slopes at the iso-bond point (the transferable numbers):**
$$\frac{dA_{Zener}}{d\rho_{eff}}\bigg|_{\rho=1} = 0.124990 \;\simeq\; \tfrac18, \qquad
\frac{d(\text{T-spread})}{d\rho_{eff}}\bigg|_{\rho=1} = 0.0625 \;\simeq\; \tfrac1{16}.$$
*(The T-spread is a max-minus-min and is V-shaped through $\rho=1$; a centred difference across the
cusp is meaningless, so the slope is a one-sided secant from the $\rho_{eff}\in(1.0005,1.02)$ rows —
disclosed, and the two secants agree to $0.4\%$.)*

**Thresholds:** $K_{thermo}>0$ at **any** $\rho_{eff}>1$ (price: $A_{Zener}-1=(\rho_{eff}-1)/8$,
arbitrarily small but so is $K$); $K_{acoustic}>0$ only at $\rho_{eff}\ge2$ (price: $A_{Zener}=1.0889$,
$4.24\%$ shear split).

### P4 — Brillouin-zone structure at $\rho_{bond}=1$

| Check | Measured | Control |
|---|---|---|
| $\lVert D(q)-L(q)\otimes I_3\rVert/\lVert D(q)\rVert$ | **$0.00$ (bit-exact)** | — |
| worst relative intra-triple eigenvalue spread, 2000 seeded $q$ | $2.40\times10^{-15}$ | $\rho_{bond}=3$: **$0.279$** |
| $\min\lambda(D(q))$ over the same sample | $+5.183\times10^{-3}$ | — |

The factorisation is exact because $\Phi_b = k(\hat d\hat d + I - \hat d\hat d) = k\,I$ at $\rho=1$;
the 24×24 dynamical matrix is then the 8×8 scalar Laplacian tensored with $I_3$. This is the
**mechanism** behind #516's knob-free $\Gamma_{min}$ and #506's *"all directions collapse to
0.17678"* (`:198`).

---

## §3 — SECTOR KEYING: which bias components each carrier class engages

The brief asks for the SYM/ASYM ↔ INVARIANT-S2 structure and the explicit connection to #813's W7
(*"Does 'SYM = both sectors driven' mean equal $S$ per FIELD sector ($\varepsilon$ vs $\mu$) or equal
$S$ per BOND channel (axial vs shear)?"*, `research/2026-07-31_anisotropy-observable_scoping.md`:1108–1116).

### §3.1 — The bond-channel ↔ carrier-class map, with the pre-tension reading applied

| Bond channel | What it is (pre-tension reading) | Elastic role | Carrier class it restores | Engaged by which bias? |
|---|---|---|---|---|
| **$k_a$ (axial)** | $U''(\ell)$ — the bond's radial **curvature** | supplies the *deviation from pure tension*: $C^{th}\propto(k_a-k_s)$ | **A₁ dilatation / mass** (the bulk-longitudinal channel) | any bias that changes the bond's stiffness at fixed length **or** shifts the operating length |
| **$k_s$ (shear)** | $\tau/\ell = U'(\ell)/\ell$ — the bond's **tension** over its length | supplies the whole isotropic pre-stress $\sigma_0$ | **T₂ transverse** — photon *and* mechanical-shear/GW, which at $\rho=1$ are the **same** triply-degenerate branch (P4) | the same two knobs |

**★ The structural constraint this adds, which the corpus's two-independent-$S$ model does not
carry.** $k_a$ and $k_s$ are not independent springs — they are the **curvature and the slope of one
bond potential at one operating point**. A scalar DC bias that moves the operating length moves both
along a **one-parameter curve fixed by $U(\ell)$**:
$$\rho_{bond}(\ell) = \frac{\ell U''(\ell)}{U'(\ell)} = \frac{d\ln U'}{d\ln\ell}.$$
So "$S_{axial}$ and $S_{shear}$ are two free knobs" is a modelling convenience, **not a substrate
freedom** — and #519's $\rho_{eff}=\rho_{cold}(S_{ax}/S_{sh})$ is a *reparametrisation* of "where on
the bond law does the DC operating point sit."

**And $\rho_{bond}=1 \iff U\propto\ell^2$ (a zero-rest-length spring).** That is the substrate-native
content of the Ax3 match point: the vacuum's bond law is *locally* the one potential whose network
energy is orientation-blind. Everything in §1.3 follows from it.

### §3.2 — SYM / ASYM: the two definitions, and where they can and cannot be identified (W7)

| Reading | Condition | What the pilot says |
|---|---|---|
| **W7(a) — field-sector SYM** ($S_\varepsilon=S_\mu$, INVARIANT-S2) | the EM cap/ind pair is loaded equally ⇒ $Z\equiv Z_0$, $\Gamma=0$ | **Silent.** The Cauchy sector does not carry an $\varepsilon$-vs-$\mu$ split; both $k_a$ and $k_s$ are capacitive-family (#519 header). The pilot cannot see this axis. |
| **W7(b) — bond-channel SYM** ($S_{axial}=S_{shear}$) | $\rho_{eff}=1$ ⇒ tensor uniformly $S$-scaled | **Fully measured (P2).** Zener $=1.000$, $c_L/c_T=1.000$, $\rho_{eff}=1$ exactly, only $\sigma_0$ moves. |
| **W7(c) — they are the same thing under TKI** | — | **NOT supported by anything this lane found.** Under the §3.1 reading, bond-channel SYM means $\delta\ln U'' = \delta\ln(U'/\ell)$, i.e. the bias rescales the *whole bond law* without moving the operating length. That is a statement about the **kernel's action on a bond potential** — a genuinely different object from $S_\varepsilon=S_\mu$. **Identifying them would be an assumption, and no corpus leaf this lane found derives it.** |

**⇒ The W7 answer this pilot supports is (a)-and-(b)-are-distinct**, with a sharpened form of the
missing map: it is not "field sectors → bond channels", it is **"what does the Ax4 kernel do to a
bond potential — rescale it, or move the operating point along it?"** Those two actions have
*different* consequences (rescale ⇒ $\rho_{eff}$ fixed, isotropy exact; move ⇒ $\rho_{eff}$ moves,
isotropy broken at slope $1/8$), and the corpus currently models only the first (#519) while
#526 partially models the second (as an additive $T$).

### §3.3 — Connection to #813's W4 (does a radial gravitational squeeze load the channels unequally?)

#813 W4 (`:1053–1084`) asks exactly the ASYM question in the gravitational sector, and records that
*"**Nothing in the corpus maps the first onto the third**"* (`:1066`). The pilot supplies the missing
**transfer function** for whichever answer W4 gets:

$$\lvert A_{Zener}-1\rvert \simeq \tfrac18\lvert\rho_{eff}-1\rvert, \qquad
\left\lvert\frac{\delta c_T}{c_T}\right\rvert \simeq \tfrac1{16}\lvert\rho_{eff}-1\rvert,$$

and for a **maximally asymmetric** reading (one channel loaded at gravitational amplitude $A$, the
other unloaded, either assignment), $\lvert\rho_{eff}-1\rvert \simeq A^2/2$, hence

$$\left\lvert\frac{\delta c_T}{c_T}\right\rvert \simeq \frac{A^2}{32}.$$

This is **arithmetic on merged numbers, not a prediction** — it is conditional on W4 answering
(b)/(c) and on W6 (is the photon the transverse-$u$ branch). Evaluated at the two corpus amplitudes:

| Bench | $A=\varepsilon_{11}=7GM/(c^2r)$ | $A^2$ | $\lvert\delta c_T/c_T\rvert = A^2/32$ | Note |
|---|---|---|---|---|
| **Solar limb** | $1.486\times10^{-5}$ (`domain-catalog.md`:50) | $2.21\times10^{-10}$ | $\mathbf{6.9\times10^{-12}}$ | accumulated differential retardance through the solar field $\approx \pi b A_b^2/(32\lambda) \approx \mathbf{3.0\times10^{4}}$ waves at $\lambda=500$ nm — light grazing the Sun would be **completely depolarised**, which it is not |
| **Earth surface** | $4.87\times10^{-9}$ (`appendix-experiments.md`:17) | $2.37\times10^{-17}$ | $\mathbf{7.4\times10^{-19}}$ | within ~1 OOM of the optical-cavity anisotropy scale #813 quotes ($\sim10^{-19}$) — **but the optic axis is local vertical, co-rotating with the lab**, so a turntable experiment about a vertical axis sees a **constant offset, not a sidereal modulation**. Applicability is a real-experiment question, tagged `[requires-external-retrieval]`; **no bound is invented here** |

**Read, stated as a bounding argument and not as a verdict:** the solar-limb row is a
~4–5 OOM over-shoot of any plausible polarimetric null, so **the maximally-asymmetric reading of
gravitational bond-channel loading is disfavoured by inspection** — which *argues for* W4 option (a)
("the radial uniaxiality averages out over the cell's bond orientations, $S_{axial}=S_{shear}$"), and
is consistent with the ratified W1 answer. **It does not prove it**: the $A^2/2$ step assumes the
extreme one-channel-only loading, and the honest statement is that the pilot converts W4 from a
qualitative fork into a **quantitatively bounded** one. The cross-check against #813's own
independent estimate is clean: #813 §2.8 banded $\sim8.8\times10^5$ waves *at an $\mathcal{O}(1)$
coefficient*; the pilot's derived coefficient is $1/32$, and $8.8\times10^5/32 = 2.8\times10^4$,
agreeing with the $3.0\times10^4$ above.

---

## §4 — CONSEQUENCES MAP

Per stabilization candidate: what item-21's observables become, and what the $\nu=2/7$ / $K=2G$ chain
inherits. **Surfaced, not landed** — every row is an implementer finding for auditor/Grant
adjudication.

### §4.1 — Item-21's observables

| Candidate | Zener at the operating point | GW polarisation-speed split | Photon birefringence | Item-21 status |
|---|---|---|---|---|
| **S1** symmetric bias | $1.000$ **exactly, at every $q$** | **zero** | **zero** | closes **negative-by-construction**, and for a *stronger* reason than #813 had: not "Zener $=1$ in the long-wave limit" but **exact triple degeneracy at every wavevector** (P4) |
| **S2** asymmetric bias | $1+\delta/8$ | $\delta/16$ fractional | $\delta/16$ fractional (if W6 = one branch) | item 21 becomes a **live, gravitationally-sourced** observable with a derived transfer function — but the solar-limb arithmetic (§3.3) disfavours the maximally-asymmetric reading by 4–5 OOM |
| **S3** pre-stress (already there) | $1.000$ exactly | zero | zero | same as S1 — a *hydrostatic* pre-stress is isotropic by construction |
| **S4** mode condensation | undetermined (needs anharmonic $U$) | undetermined | undetermined | **not computable in a harmonic model** |
| **S5** external/cosmological loading | $1.000$ exactly if hydrostatic; **anisotropic if the cosmological load is not isotropic** | — | — | opens a **new** axis #813 did not consider: a non-hydrostatic boundary load would print a **cosmological-scale** Zener anisotropy with a preferred axis, which is the sky-pattern object of #813 W3 — and it would *derive* the axis orientation instead of assuming it |
| **S6** bond-length shift | $1+\delta/8$ with $\delta$ set by $U(\ell)$ | as S2 | as S2 | converts item 21's magnitude question into a **bond-law** question |

**★ The one genuinely new item-21 lead in this document is the S5 row.** #813 W3 flagged that the
lattice's sky orientation was never derived (and that the one place the corpus appears to fix it is a
galactic-coordinate default, `:1033–1042`). Under S5, an **anisotropic** cosmological boundary load
is the one mechanism in this candidate set that would *supply* a preferred axis rather than assume
one. Not pursued here; recorded as a routed lead.

### §4.2 — What the $\nu=2/7$ / $K=2G$ chain inherits (the sharpest consequence)

At the ratified operating point $\rho_{bond}=1$, the pilot measures:

$$C^{th}_{11}=C^{th}_{12}=C^{th}_{44}=0 \ \Rightarrow\ K_{th}=0,\ G_{th}=0,\qquad
\frac{K_{ac}}{G_{ac}}=\frac{-\sigma_0/3}{\sigma_0}=-\frac13 .$$

**Neither reading is anywhere near $K=2G$.** The thermodynamic ratio is $0/0$ (undefined); the
acoustic ratio is $-1/3$. And $\nu$ is at its pole (#519 `:134` locates the $\nu$-denominator zero
$3K+G=0$ at exactly $\rho_{eff}=1.00000$ — *the iso-bond point*, which is now identifiable as the
pre-stress-only point).

| Site | What it inherits | Grade |
|---|---|---|
| **$\nu_{vac}=2/7 \iff K=2G$** (`vacuum-poisson-ratio.md`, `clm-x19btt`) | The algebraic identity is **untouched**. What changes is that the operating point at which it could hold ($\rho^\ast=9.7734$) is now **not the vacuum's operating point** under the ratified W1 answer. #506 already graded the value **GR-imported**; this pilot sharpens "imported" to **"imported AND not located at the vacuum's own operating point"**. | **SURFACED — status-language sharpening, auditor lands** |
| **The three /7 PPN couplings** (`gravity-ppn-coherence-result.md`) | **UNCHANGED at the number level** — #506's own fallout row already records that the /7 PPN numbers are *"calibrated in independently at the deflection-integral level"* (`:217–218`), `predictions.yaml` P10 `type: consistency_check`. Only the provenance story moves. | **UNCHANGED (bounded)** |
| **`constants.py` `V_LONG=√(2G/ρ)` "From K=2G (EMT)"** | #506 already re-attributed this to GR-imported $K=2G$. This pilot adds: at $\rho_{bond}=1$ **$c_{bulk}=c_{shear}=c$ exactly** (P4 triple degeneracy; $c_L/c_T=1.000000000$), so the $\sqrt2$ separation has **no operating point in the ratified vacuum**. | **SURFACED — see §5 FLAG-1** |
| **Port-register channels 1/2/3 speeds** (`port-register.md`:49) | Same: at $\rho_{bond}=1$ channels 1, 2 and 3 are **one triply-degenerate acoustic branch**. | **SURFACED — see §5 FLAG-1** |
| **#519 `[SAME-TENSOR-POINT]`** | **UNTOUCHED and re-confirmed** — the pilot's P2/P3 reproduce the degree-1 homogeneity and the undeformed $\rho_{eff}$ map exactly. What the pilot adds is *outside* #519's fence (its MODEL-SCOPE channel (a)). | **STRENGTHEN-THE-SCOPE (candidate)** |
| **#526 `[MAP-DEFORMED]` + the $T$-sign axis** | **STRENGTHENED and partly explained** (§1.1). ⚠ **Correction made mid-draft:** #526's $T$-sign fork is **NOT open** — it was resolved channel-keyed and **Grant-ratified**, `manuscript/ave-kb/common/axiom-register.md` §"LOAD-RESPONSE SIGN RULE", verbatim `[sic]`: *"a **transverse pluck** … ⟹ **TENSION** ($T>0$) … an **axial end-load** buckles the strut ⟹ **COMPRESSION** ($T<0$…)… The verdict depends on $\text{sign}(T)$ ALONE … this is Grant's ratified 'it does both depending on interaction.'"* (provenance `research/2026-07-04_bond-force-sign-rule_result.md`, `[SIGN-RULE-DERIVED]`). The pilot's input sits **upstream** of that rule, not inside it: it asks whether the **cold** $k_s$ is *already* a tension before any $T$ is added. If yes, the ratified compression arm has a **hard floor** — $k_s^{total}=k_s+T/\ell$ can reach $0$, at which point the transverse restoring force vanishes, the $L(q)\otimes I_3$ structure is destroyed and the net buckles; #526's "UNCAPPED" track is then capped from below by $\tau_{total}=0$. **Input to a settled rule's domain of validity, not a re-opening of the fork.** | **SURFACED — routed to auditor; the ratified sign rule is untouched** |
| **#516's Ax3 result** | **STRENGTHENED.** The knob-free minimiser at $\rho=1$ is now identifiable as a **symmetry theorem** (§1.3): once $\Phi_b=kI$ the problem is scalar and cubic symmetry forces rank-2 isotropy. Also **#516's honest flag (`:48–53`) is the one that moves**: the match point is *marginal*, not unstable, and the phonon spectrum there is positive-definite. | **STRENGTHEN + honest-flag update (candidate)** |
| **#506's `[ANISOTROPIC-BREAKDOWN]` / `[DIFFERENT-ν]` bins** | **UNTOUCHED.** Those bins are about the $\rho$-family and the GR-import, both reproduced here bit-for-bit. | **UNCHANGED** |

---

## §5 — FLAG-DON'T-FIX (surfaced with both paths + verbatim; nothing reframed, nothing edited)

**FLAG-1 — the inter-channel speed ratios have no operating point at the ratified $\rho_{bond}=1$.**

- Corpus, `manuscript/ave-kb/common/port-register.md`:49, verbatim `[sic]`: channel 3 carries
  *"**$\sqrt2\,c$** ($V_{LONG}$; $K=2G$ magic-angle PORT/impedance mode)"* and
  *"**$\sqrt{10/3}\,c \approx 1.83c$** (isotropic-solid P-wave …)"*, while channels 1 and 2 carry
  $c$ and $c_{shear}=c$.
- Pilot, at $\rho_{bond}=1$: the three acoustic branches are **exactly degenerate at every $q$**
  ($2.4\times10^{-15}$ over 2000 seeded $q$; $D(q)=L(q)\otimes I_3$ bit-exact), and
  direction-averaged $c_L/c_T = 1.000000000$. #506 already reports the long-wave half of this
  (`:198`, verbatim `[sic]`: *"At the iso-bond point (ρ=1) all directions collapse to 0.17678"*).
- **Both statements cannot be true of the same operating point.** Note the corpus is *internally
  consistent about the provenance*: `srs-band-structure.md`:116 already grades $\sqrt{10/3}$ as
  *"a **K=2G RE-EXPRESSION** (GR-imported, PR #261), **NOT lattice-emergent**"*. So this is not a new
  independent contradiction — it is **the same GR-import surfacing in its sharpest form yet**: under
  the ratified W1 answer the imported ratios describe a medium the vacuum is not.
- **Not resolved here.** Two honest paths exist and this lane picks neither: (α) the ratios are
  **matter-regime / loaded-vacuum** constitutive numbers (they hold where $\rho_{eff}\gg1$, i.e. at
  or inside matter) and were mislabelled as vacuum numbers; (β) the ratified $\rho_{bond}=1$ is a
  **photon-sector** operating point and the bulk channel rides a different one — which is #813's W1
  option (c), the "genuinely two operating points" branch, and would need the carve derived.
  **Grant adjudicates.**

**FLAG-2 — "mechanically unstable" is a three-way conflation.** §1.1. The pilot does **not** claim
#506/#516 are wrong about their computed numbers (every one reproduces); it claims the *word* covers
three different statements with three different answers. Verbatim sites quoted at §1.1. **Routed to
the auditor lane; no corpus file edited.**

**FLAG-3 — the #506 $\rho^\ast$-row K entry.** §2 P1 box. Isolated transcription residual; no
conclusion rides on it.

**FLAG-4 — the corpus already MEASURED the rotation-costs-energy fact and reads it the OPPOSITE way.**
*(This flag was rewritten mid-draft: the first version claimed the corpus never addresses rotational
invariance of $\Phi_b$. **That was false and the two-method receipt caught it** — receipt 4, §B.)*

- **Corroboration first.** The pilot's P1(a) number is independently confirmed by a different lane on
  a different driver: `research/2026-07-28_subc-kubc-bracket_result.md`:70 (PR #802, merged),
  verbatim `[sic]`: *"`E(uniform translation) = 0.0` exactly; `E(rigid rotation, 1e-3) = 1.984e-3 >
  0`; `born_model_confirmed_rotations_cost_energy = True`"*. Two independent measurements, same fact.
- **But the corpus reads it as a FEATURE, not a symptom.** `manuscript/ave-kb/common/translation-tables/translation-circuit.md`:360,
  verbatim `[sic]`: *"on the shipped Born bond model rotations **cost energy**, so the actual null
  space is the **3 translations only** … A network reading … would have missed **the Born model's
  absolute-frame rotational stiffness** entirely."* That is a reading in which the substrate
  genuinely has an absolute rotational frame and a rigid rotation genuinely costs energy.
- **The pilot's reading is the other one:** a rigid rotation costing energy is the standard signature
  of a **missing first-order (pre-stress) term**, i.e. that $k_s$ is $\tau/\ell$ and the reference
  state is pre-tensioned. **These are different physics** — absolute rotational stiffness would break
  local rotational invariance (a Cosserat-grade statement about the substrate), whereas the
  pre-tension reading preserves it and buys an initial stress instead.
- **What IS absent, by two methods (receipt 4):** the **Birch / Brugger acoustic-vs-thermodynamic
  elastic-constant split** — `"Brugger"` **0 hits** and `"Birch"` (in the elastic sense) **0 hits**
  in `research/` + `manuscript/ave-kb/` + `src/` on the working tree AND **0 commits** under a
  `git log -S` pickaxe over `origin/main` history (the 13 working-tree `Birch` hits are all
  Birch–Swinnerton-Dyer). And no leaf reads the **cold** $k_s$ as itself a pre-tension: the 11
  `initial-stress` hits are all #526's *added* $T$ slot plus the vessel-state RVE prereg.
- **Not resolved.** Both readings are live; the choice decides whether $K_{ac}<0$ is an initial-stress
  offset (pilot) or a real stiffness statement (corpus). **Grant adjudicates** (§7 V1).

---

## §6 — HOW MUCH OF THIS IS BOND-MODEL-DEPENDENT (honest scope)

| Result | Survives a different bond model? |
|---|---|
| $k_s$ ⇒ pre-tension (rotational invariance) | **Model-specific to Born rank-2** — and that is the point: it is a statement *about* the engine-native model. Keating's angle-bend model is rotationally invariant **without** pre-stress, so under Keating there is no $\sigma_0$ and the $K<0$ has a different (and still unexamined) origin. **This is exactly why #506 §8's open question matters.** |
| $K_{th}=(\rho-1)\sigma_0/3$, $C^{th}\equiv0$ at $\rho=1$ | Born-specific (same reason). |
| $D(q)=L(q)\otimes I_3$ at $\rho_{bond}=1$ | Born-specific, but **geometry-independent**: it holds on *any* net, because $\Phi_b=kI$ is orientation-blind. |
| Zener $=1$ at $\rho=1$ is a symmetry theorem | Follows from the above; Born-specific in the same way. |
| Symmetric bias cannot flip sign($K$) | **Model-independent** — it is degree-1 homogeneity of the long-wave map, which #519 VS2 verified holds for the map's structure, not for a particular $\Phi_b$. |
| The $1/8$ and $1/16$ slopes | Born-specific numbers; the *existence* of a linear anisotropy price at any $\rho\neq1$ is generic. |

---

## §7 — WALK QUESTIONS FOR GRANT (for the follow-on prereg; asked BEFORE design, per the Rule-16 strengthening)

Inline prose with bulleted options; none pre-picked, none rhetorical.

**V1 — Does a rigid rotation of the vacuum cost energy, or does the cold $k_s$ carry a pre-tension?**
This is FLAG-4 and it is the fork everything else in this document hangs from. Two independent
measurements agree that the shipped Born model makes a rigid rotation cost energy (pilot P1(a):
$4.000$; #802 `:70`: $1.984\times10^{-3}$). The corpus reads that as *"the Born model's absolute-frame
rotational stiffness"* (`translation-circuit.md`:360); the pilot reads it as the standard signature of
a missing first-order term, i.e. $k_s=\tau/\ell$ and a pre-tensioned reference state. Plumber form:
*take the whole lattice and turn it, rigidly, by a hair — with nothing else changing. Does that cost
work? If it does, the vacuum knows which way is "un-rotated," which is a big claim. If it doesn't,
then the sideways stiffness we wrote down has to be coming from a pull along the wire.* Options:
**(a)** pre-tension — the vacuum is a taut cable net / soap film, everything in §1.3 holds, and $K<0$
is an initial-stress offset; **(b)** genuine absolute-frame rotational stiffness — the corpus's
reading, in which case the substrate has a preferred rotational frame at the Cauchy grade and
**that** is the headline, not the vessel; **(c)** the Born rank-2 form is a convenient instrument
that was never meant to be rotationally complete, and the physical bond is Keating/3-body (which
routes to V7(b)); **(d)** both, at different grades — a Cosserat micro-rotation stiffness is real and
*separate* from the Cauchy-grade tension, and the two have been conflated in one $k_s$.

*(Note for the walk: this is **upstream** of, and does not re-open, the ratified LOAD-RESPONSE SIGN
RULE — `axiom-register.md`, Grant-ratified, "$T>0$ for a transverse pluck / $T<0$ for an axial
end-load, sign(T) alone." If (a), that rule acquires a hard floor at $k_s+T/\ell=0$.)*

**V2 — What is holding the vessel out?** $K_{th}=0$ means the wall has **no bulk stiffness of its
own**; the tension must be balanced by something. Plumber form: *a soap bubble does not hold its
shape because the film is stiff — it holds it because there is gas inside at a pressure. What is the
gas?* Options: **(a)** a pressure-bearing content with its own nonzero bulk modulus (the corpus has
candidate reservoirs; naming one is a physics call this lane will not make); **(b)** nothing — the
topology is closed and the tension is self-balanced, no external agent required; **(c)** the
anharmonic ($U'''$) term stiffens the bulk channel at finite amplitude and there is no separate
agent; **(d)** the vessel is *not* in equilibrium and the imbalance is the expansion.

**V3 — Which boundary condition is the physical one?** Because $K_{th}=0$, the stability verdict is
**decided entirely by the loading condition** and not by the elastic tensor. Dead hydrostatic load ⇒
$K_{ac}<0$ ⇒ runaway; controlled volume ⇒ neutral at second order; pressure-bearing content ⇒ stable
composite. Plumber form: *when we ask "is the vacuum stable", are we asking about a sample in a
press, a sample in a sealed can, or a sample that is the whole can?* Options: **(a)** dead load;
**(b)** fixed volume; **(c)** self-balanced closed system; **(d)** the question needs a cosmological
answer and belongs upstream of this arc.

**V4 — Does the Ax4 kernel RESCALE the bond law or MOVE the operating point along it?** These have
different consequences (§3.2): rescale ⇒ $\rho_{eff}$ fixed, isotropy exact, only $\sigma_0$ moves
(what #519 models); move ⇒ $\rho_{eff}$ moves, isotropy broken at slope $1/8$ (what #519's MODEL-SCOPE
channel (b) calls out as open). Plumber form: *when a cell is biased, does every spring in it get
uniformly weaker, or do the nodes actually move to a new spacing where the springs read differently?*
Options: **(a)** rescale only; **(b)** operating-point shift only; **(c)** both, with the split set by
the bond law; **(d)** the distinction is not physical because $S(A)$ is defined on amplitude, not
length.

**V5 — Does gravity load the two bond channels equally?** This is #813's W4, now with a transfer
function attached (§3.3): $\lvert\delta c_T/c_T\rvert \simeq A^2/32$ under maximal asymmetry, which
over-shoots solar-limb polarimetry by ~4–5 OOM. Plumber form: *a lattice cell one solar radius from
the Sun — is it squeezed the same from every side, or squeezed radially and stretched tangentially;
and does its stretch-spring feel that differently from its shear-spring?* Options: **(a)** equally
(the radial uniaxiality averages over the cell's bond orientations) ⇒ zero photoelastic splitting,
consistent with the ratified W1; **(b)** unequally but far below maximal, in which case the pilot's
slope makes the residual computable and the prereg should freeze on it; **(c)** unequally at the
maximal rate, in which case the arithmetic already excludes it and that is a **clean closed-negative**
worth banking; **(d)** the real-space radial/tangential split and the bond-channel split are
different objects and the map is the missing derivation (#813 W4 option (c)).

**V6 — Where do the $\sqrt2$ and $\sqrt{10/3}$ channel speeds live, now that they cannot live at
$\rho_{bond}=1$?** FLAG-1. Plumber form: *if empty vacuum carries sound and light at the same speed,
what is the medium in which the compression wave runs $1.83\times$ faster — is that a loaded vacuum,
or is it a different channel we have mis-parented?* Options: **(α)** matter-regime / loaded-vacuum
constitutive numbers, mislabelled as vacuum; **(β)** two genuinely different operating points with a
carve that must be derived (#813 W1 option (c)); **(γ)** the ratios are FORM-only and were never
meant to carry an operating point; **(δ)** the ratified W1 answer needs revisiting *because* of this.

**V7 — Should the follow-on prereg test the model, or the physics?** The pilot's headline is an
**identity of the engine-native Born model**. A prereg could freeze bins on (i) the pre-stress
picture's consequences within the Born model, or (ii) the Born-vs-Keating-vs-`clm-bjceop` fork
itself (#506 §8), which the rotational-invariance finding now makes decidable rather than a matter of
taste. Options: **(a)** (i) — stay inside the ratified carrier and push the vessel picture;
**(b)** (ii) — settle the bond model first, because everything numerical above is conditional on it;
**(c)** both, in that order, with (ii) as a small gate before (i); **(d)** neither — the frontier
object is V2/V3 (what pressurises the vessel), which is a cosmology-sector question and should be
routed there.

---

## §8 — DRAFT OUTCOME BINS (**NOT FROZEN** — scoping-grade; the follow-on prereg freezes them)

Recorded so the follow-on has a starting point, and so that the *reachability* of each is auditable
now (per the standing DESIGN LESSON 1 in #813 `:1181`).

| Bin | Fires if | Reachable? |
|---|---|---|
| **B1 — VESSEL-CONSISTENT** | the pre-stress reading survives a rotationally-invariant re-derivation AND a named balancing agent gives a stable composite | reachable; needs V2 + an anharmonic bond law |
| **B2 — MARGINAL-BUT-UNRESOLVED** | $K_{th}=0$ confirmed, but stability is boundary-condition-dependent and no BC is derivable | **already the pilot's honest standing state** |
| **B3 — BOND-MODEL-ARTIFACT** | a rotationally-invariant model (Keating / `clm-bjceop`) gives $K>0$ at its own iso-bond point with no pre-stress ⇒ the whole $\sigma_0$ story is Born-specific bookkeeping | reachable and cheap (the #506 §8 fork) |
| **B4 — ISOTROPY-PRICED** | the physical vacuum is shown to sit at $\rho_{eff}\neq1$ ⇒ anisotropy at slope $1/8$ becomes a live prediction | reachable via V5; solar-limb arithmetic already bounds it |
| **B5 — TWO-OPERATING-POINTS** | a derived carve puts photon at $\rho=1$ and bulk elsewhere | reachable only with a derivation nobody has |
| **B6 — W1-REVISIT** | FLAG-1 is judged to falsify $\rho_{bond}=1$ as the vacuum point | reachable; would reopen the ratified path |

**Anti-tune ledger.** No parameter was tuned toward any visible target. $\sigma_0$ falls out of
geometry; the $1/8$ and $1/16$ slopes fall out of the sweep; $\rho^\ast=9.7734$, $2/7$, $2$, $2.0$ and
$\sqrt{10/3}$ are read-off comparison constants declared in the driver and **never** inputs. The one
place a number *could* have been steered — the closed form $K_{th}=(\rho-1)\sigma_0/3$ — was
**predicted from the pair-potential expansion before the sweep was run** and then checked, not fitted.

---

## §9 — WHAT THIS LANE DID NOT DO (non-goals, fenced)

- **Did not edit any corpus file.** Zero `manuscript/` changes, zero `_orchestration/` changes beyond
  the new docket fragment, `src/ave` **byte-untouched**.
- **Did not mint a claim, a `def-`, a `clm-`, or change any solidity.** Did not land any manual entry
  (auditor lane).
- **Did not freeze bins.** §8 is draft.
- **Did not resolve** the Born/Keating/`clm-bjceop` fork, #526's $T$-sign fork, W1's FLAG-1 tension,
  W4/W7, or the boundary-condition question. All surfaced.
- **Did not derive any value.** $\sigma_0$ is in engine units ($k_s=\ell=1$); no SI, no CODATA on the
  verdict path, no comparison to a measured constant.
- **Did not invent an observational bound.** The one external comparison (§3.3) is tagged
  `[requires-external-retrieval]`.
- **Did not run a Cosserat / couple-stress arm.** Out of scope at the $k\to0$ Cauchy grade.

---

## Appendix A — skill-selection plan + retro-pass

### A.1 — The 60-second plan, written BEFORE work started

| Skill | Why fired (planned) |
|---|---|
| `verify-before-cite` | every #506/#516/#519/#813 line quoted; stale session beliefs do not carry |
| `substrate-native-check` | K4/Cosserat/Op14/phase-space walk **before** any driver line — the brief scaffolds a solver arm |
| `pre-test-physics-check` | scoping precedes a prereg ⇒ plumber-questions surfaced to Grant BEFORE design (§7) |
| `phase-space-coordinate-check` | the bias knob is phase-space, the tensor readout is real-space; A46 |
| `consistency-vs-emergence` | the pilot touches $\nu=2/7$, $\rho^\ast$, $\sqrt{10/3}$ — all visible targets |
| `ave-canonical-source` | constants from `ave.core.constants` / `ave.axioms.scale_invariant`, never hard-coded |
| `ave-discrimination-check` | before any "AVE-distinct" language on the anisotropy observable |
| Rule-10 empirical-driver discipline | run the pilot early even if imperfect |

### A.2 — Retro-pass on applied-set drift (run before commit)

| Drift | What happened |
|---|---|
| **`verify-before-cite` fired harder than planned, and it changed two conclusions.** | (i) FLAG-4's first draft claimed the corpus never addresses rotational invariance of $\Phi_b$ — **false**; #802 measured it and `translation-circuit.md`:360 canonizes the *opposite* reading. FLAG-4 rewritten, and the finding is stronger for it (a live two-reading fork, plus an independent corroboration of the pilot's own number). (ii) The #526 $T$-sign fork was drafted as "open"; it is **Grant-ratified closed** (`axiom-register.md` LOAD-RESPONSE SIGN RULE). Row and V1 rewritten. |
| **`ave-reproduction-gate` fired unplanned.** | The pilot re-runs #506's published table on the current engine before load-bearing it. It reproduces — except the one K-column cell at `:132` (FLAG-3), banked under this dated note, **not** overwritten upstream. |
| **`ave-discrimination-check` outcome.** | *"The vacuum is a pre-tensioned membrane"* would be an **AVE-internal model statement**, not an AVE-distinct prediction: continuum elasticity has carried the Birch initial-stress split since 1947 and any pre-stressed-lattice treatment reaches the same split. **No AVE-distinct claim is made here.** The one place a distinct FORM could live is §4.1's S5 row (a cosmological-load-sourced Zener axis) — not pursued, and it would owe a magnitude. |
| **`consistency-vs-emergence` outcome.** | Everything here is **CONSISTENCY** or **IDENTITY**. Nothing is emergence-class. $\sigma_0=0.1768$ is an engine-unit geometry sum, not a physical value. |
| **Not fired, and why.** | `ave-canonical-leaf-pull` (no Q-factor/scaling-law/cross-section object); `ave-walk-back` (no matrix row retires — every #506/#516/#519 verdict letter stands); `ave-mechanism-claims-discipline` — *checked and it binds*: the headline is a mechanism claim, so it carries no solidity and is explicitly post-review-gated (§9). |

### A.3 — Pure-AVE-corpus receipt

Three methods over the two new deliverables + the driver + the docket fragment + every commit
message on this branch: **zero** external-context references (no investor/fund/interview/pitch/1517
tokens). Physics-only rationale throughout.

---

## Appendix B — two-method receipts

**Receipt 1 — #506's $\rho=1$ row and its "unstable" wording.**
(M1) `sed -n '125p;135,137p;144,145p;198p'` on `research/2026-07-04_srs-elastic-tensor_result.md`.
(M2) driver re-run reproduces the row to $3.3\times10^{-6}$ (P0). **Both agree.**

**Receipt 2 — #516's $\Gamma_{min}$ / $\rho^\ast$ rows.**
(M1) `grep -n` on `:112`, `:117`, `:119–122`, `:48–53`, `:166`.
(M2) the pilot's independent structural derivation of *why* $\rho=1$ minimises (the $L(q)\otimes I_3$
factorisation ⇒ cubic rank-2 isotropy theorem, P4). **Agree, and M2 explains M1.**

**Receipt 3 — #519's MODEL SCOPE channels (a)/(b).**
(M1) `grep -n "MODEL SCOPE (explicit\|initial/residual stress\|bias-induced geometry change"` →
`:24`, `:27`, `:29`.
(M2) `sed -n '24,34p'` reads the fence in full. **Both agree**: (a) initial/residual stress and
(b) bias-induced geometry change are the two OMITTED channels; this document opens (a) and names (b).

**Receipt 4 — the rotational-invariance / initial-stress literature search (the one that corrected me).**
(M1) working-tree `grep -rniE` over `research/` + `manuscript/ave-kb/` + `src/`: `"rigid rotation"`
and `"rotational invarian"` return **53 hits**, concentrated in the #802 SUBC/KUBC lane and
`translation-circuit.md`; `"Brugger"` **0**; `"Birch"` **13, all Birch–Swinnerton-Dyer**;
`"initial-stress"` **11, all #526 + the vessel-state RVE prereg**.
(M2) `git log -S<term> --oneline origin/main -- research/ manuscript/ src/` (pickaxe, sees content
written-and-later-deleted): `"rotational invariance"` **1**, `"rigid rotation"` **29**,
`"Brugger"` **0**, `"Huang condition"` **0** (control: `"Born-Huang"` in `research/` → **29**, so the
pickaxe is live). **Both methods agree**: the *fact* is in the corpus and canonized with the opposite
reading; the *Birch/Brugger split* is genuinely absent. **The first draft's "zero hits" claim was a
false negative and is retracted in-place at FLAG-4.**

**Receipt 5 — the #506 $\rho^\ast$-row K discrepancy.**
(M1) arithmetic on that row's own published $C_{11},C_{12}$: $(0.7279+2\times0.3232)/3 = 0.45805
\neq 0.4308$.
(M2) driver re-run at $\rho=9.7734$: $K = 0.458052$; and the row's own $K/G_{Hill}=2.0000$ requires
$0.458052$ given $G_{Hill}=0.229031$. **Three-way agreement against the printed cell.** Every other
row in the table checks out.

**Receipt 6 — the port-register speed rows and their own provenance grade.**
(M1) `sed -n '44,52p' manuscript/ave-kb/common/port-register.md` — channel 3 carries $\sqrt2\,c$ /
$\sqrt{10/3}\,c$.
(M2) `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md`:116,
verbatim `[sic]`: *"a **K=2G RE-EXPRESSION** (GR-imported, PR #261), **NOT lattice-emergent**"*.
**Both agree** — which is why FLAG-1 is framed as an import surfacing, not a new contradiction.

**Receipt 7 — the gravitational amplitudes.**
(M1) `manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md`:50 —
*"Solar surface: $\varepsilon_{11} = 1.486\times10^{-5}$"*; `common/appendix-experiments.md`:17 —
*"canonical Earth strain $\varepsilon_{11} = 7GM_\oplus/(c^2R_\oplus)\approx4.87\times10^{-9}$"*.
(M2) #813 `:31` and `:741` carry the same two numbers with the non-confusion discipline attached.
**Both agree.** *(#813's own FLAG that `domain-catalog.md`:50's neighbouring solar row elsewhere reads
factor-7 low is inherited, unresolved, and touched by nothing here.)*

**Receipt 8 — the ρ-convention.**
(M1) `axiom-register.md` §"ρ-CONVENTION DISAMBIGUATION" — the srs swapped-spring ρ vs the
moduli-model ρ.
(M2) the pilot's own table: $K_{acoustic}=0$ at $\rho=2$ and $K/G=2$ at $\rho=9.7734$, i.e. the srs
convention, reproduced. **Both agree**; the guard box in §1.1 states which one is in force.

**Receipt 9 — the #526 sign rule's status.**
(M1) `axiom-register.md` §"LOAD-RESPONSE SIGN RULE" — Grant-ratified, `[SIGN-RULE-DERIVED]`,
provenance `research/2026-07-04_bond-force-sign-rule_result.md`.
(M2) `research/2026-07-04_prestress-tensor_result.md`:55 (the fork as originally posed) + `:282`.
**Both agree the fork is closed**; the draft's "open" framing was corrected (A.2).

---

## Cross-references (verified on this branch at write time)

- Pilot driver: `src/scripts/vol_1_foundations/biased_tensor_iso_bond_pilot.py`
- Pilot output (tracked): `research/2026-08-02_biased-tensor-scoping_pilot.json`
- Cold family / $\rho$-table (#506): `research/2026-07-04_srs-elastic-tensor_result.md`
- Ax3 iso-bond derivation (#516): `research/2026-07-04_parent-condition-match-forces-balance_result.md`
- Saturated small-signal identity + MODEL SCOPE (#519): `research/2026-07-04_saturated-elastic-tensor_result.md`
- Pre-stress arc (#526): `research/2026-07-04_prestress-tensor_result.md`; driver `src/scripts/vol_1_foundations/prestress_elastic_tensor.py`
- Bond-force sign rule (ratified): `research/2026-07-04_bond-force-sign-rule_result.md`; `manuscript/ave-kb/common/axiom-register.md`
- SUBC/KUBC bracket, the independent rotation measurement (#802): `research/2026-07-28_subc-kubc-bracket_result.md`:70
- Anisotropy scoping, W1/W3/W4/W6/W7 (#813): `research/2026-07-31_anisotropy-observable_scoping.md`
- Channel speeds: `manuscript/ave-kb/common/port-register.md`:44–52; `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md`:116
- Gravitational amplitudes: `manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md`:45,50; `manuscript/ave-kb/common/appendix-experiments.md`:17
- Born-model rotation cost, canonized reading: `manuscript/ave-kb/common/translation-tables/translation-circuit.md`:360
- Carrier: `src/ave/core/chiral_lattice.py` `build_srs_net`; kernel `src/ave/axioms/scale_invariant.py`
