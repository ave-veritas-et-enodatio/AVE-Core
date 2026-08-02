# The cold-Q pole derivation — FROZEN pre-registration (zero-free-input spin-2 ringdown eigenvalue)

**Date:** 2026-08-02
**Class:** DERIVATION pre-registration (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger — regardless of outcome**). This is COMMIT 1 — the pre-registration **ALONE**, frozen and pushed **before any driver code** (the #761/#767/#770/#775/#782/#792/#801 frozen-first discipline).
**Result-doc pointer requirement (machine-checkable frozen-provenance convention, gate LIVE since 2026-07-22).** The result doc that resolves these bins MUST carry a machine-readable pointer line `Prereg-file: research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file (`manuscript/ave-kb/tools/verify-frozen-provenance.py`). Every frozen criterion below is written as an inline-code `` `quoted token` `` for exactly that byte-match.
**Provenance:** Grant's GO on the cold-Q derivation, 2026-08-02, verbatim `[sic]`: `"6, GO"` — issued after the full framing-challenge walk. Upstream, in order: [`research/2026-07-30_qlaw-derivation_scoping.md`](2026-07-30_qlaw-derivation_scoping.md) (#808, routes R1–R6, findings F1–F9, walk questions Q1–Q8, DRAFT bins) and [`research/2026-07-31_qlaw-framing-challenge_walk.md`](2026-07-31_qlaw-framing-challenge_walk.md) (#814, CF-1…CF-16, elements E1–E15, FORK-1…FORK-12, the R7 route proposal and its spin-1-vs-spin-2 prerequisite). **This document freezes what #814 proposed and did not execute.**
**Written against** `origin/main` = `ac165cf2`.
**Lane fences:** DERIVATION lane only. Engine `src/ave` **BYTE-UNTOUCHED** (imports read-only; the whole instrument lives in `research/drivers/`). **No** `manuscript/` or `manuscript/ave-kb/` edit of any kind. **No** `_orchestration/` edit except this lane's own docket fragment. **No** `translation-circuit.md` row landed (the #814 §2.7 non-landing stands until the derivation validates a row, and landing is the auditor lane's move, not this one's). Consequences — including a falsified `(1+ν_vac)`, a broken `Q = ℓ` anchor, or a corpus inconsistency discovered mid-solve — are **ROUTED, not repaired.**

> **FREEZE STATEMENT.** This document freezes: (i) the sector/regime/phase-state/coordinate header and the substrate-native walk (§0); (ii) the scope carve — what is computed and what is explicitly NOT (§1); (iii) **the derived spin-2 (toroidal / odd-parity) radial equation, derived here from the shear-channel continuum equations and NOT imported from the spin-1 vector-multipole impedance** (§2); (iv) the complete import ledger, every entry tagged (§3); (v) the instrument — the regular-at-the-wall substitution, the asymptotic outgoing series, the argument-principle pole count, and every numeric parameter (§4); (vi) the EIGHT solver-certification gates G1–G8 with FROZEN NUMERIC TOLERANCES (§5); (vii) the FIVE gate-fireability self-tests FT-1…FT-5, each of which MUST FIRE (§6); (viii) **the physics OUTCOME BINS, exhaustive, every bin reachable, with a precedence order and a mutual-satisfiability argument** (§7); (ix) what transfers from the #801 certified continuum radial solver and what must be re-earned (§8); (x) the mutual-satisfiability check run BEFORE the freeze and its disclosure (§9); (xi) which #814 forks are consumed, which are fenced, and which are dissolved by construction (§10); (xii) ledger tags + owed follow-ons (§11). **The verdict may cite ONLY the frozen criteria's outputs, read from the shipped `coldq_pole_derivation_results.json` via the deterministic driver — NO prose-string conclusions (the #770 lesson).**

---

## §0 — SECTOR / REGIME / PHASE-STATE / COORDS header, declared BEFORE any physics word

- **MODE.** Cold (`a_* = 0`, Schwarzschild-limit) post-merger remnant ringing down. The object is the fundamental `ℓ = 2` quasinormal resonance of the saturation cavity, and its radial overtone ladder.
- **SECTOR.** The **observable** is a **transverse shear (T2)** oscillation. The **bias field** that builds the cavity is the **A1 radial dilatation** `ε_11 = 7GM/(c²r)`. These are orthogonal grades and are **not** cross-wired here: the A1 strain is the DC operating point that sets the constitutive profile; the T2 shear mode is the small-signal AC riding on it. Receipt for `ε_11` **being** the Axiom-4 amplitude `A`: [`common/vocabulary-register.md:309`](../manuscript/ave-kb/common/vocabulary-register.md), verbatim *"$\varepsilon_{11} = 7GM/(c^2 r)$ … the A1-dilatation radial 'strain' that IS the Axiom-4 saturation amplitude $A$"*.
- **REGIME.** Far field (`r ≫ r_sat`) = **Regime I** — linear, lossless, reactive; a legal radiating port. The graded exterior `r > r_sat` = Regime I with a spatially varying modulus (Op14 grade). The wall `r = r_sat` = the **Regime III→IV** soft-mode terminus, `G_shear → 0`. The interior `r < r_sat` = **Regime IV**, where shear cannot propagate at all and which is therefore **not part of the computational domain** — the domain is `[r_sat, ∞)`, and that is a physics statement, not a truncation.
- **PHASE-STATE.** Op14 ON throughout the graded exterior as a **static constitutive grade** (the DC bias is time-independent; the ringdown is the small-signal response). `A = 1` exactly at `r_sat = 7GM/c²`; `Γ_shear = −1` there.
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the **dimensionless-eigenvalue register** (`ω_R M_g`, `ω_I M_g`, `Q`) that AVE and GR share — no phase-space/real-space mismatch. **#814's CF-14 caveat (port-`Q` vs pole-`Q`) is DISSOLVED by construction here, not managed:** this lane solves for the **complex pole** directly, so what it returns *is* the pole-`Q` that the GR comparator is, and **no port→pole transfer is performed, needed, or assumed.** See §10 FORK-10.
- **The eigenfunction's own coordinate.** The radial localization observable (BIN-3) is read in **real-space radius normalized to `r_sat`** and is compared only against real-space radii (`r_sat`, the #814 turning point `r★`). It is **not** compared against `r_eff = 49M_g/9`, which #814's corrected reading establishes is a **spectral marker (a cutoff radius), not a place** — see the IDENTITY note in BIN-3.

### Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code — this section was written before the driver existed)

1. **K4 / srs connectivity.** This is a **CONTINUUM** instrument and must not pretend otherwise. It is **not** a discretization of the srs stencil and carries **no** K4 connectivity claim. What it consumes from the lattice is the **constitutive law only**: the Ax-4 kernel and the Op16 shear-speed projection. Frozen disclosure: `the radial channel is a CONTINUUM representation of the shear constitutive law; it is not a discretization of the srs stencil and carries no K4 connectivity claim`.
2. **Cosserat / channel basis — and this is where the spin-2 discipline bites.** The Cosserat micro-rotation and the A1 dilatation are **both excluded from the observable** by the choice of channel: the mode solved for is the **toroidal (odd-parity / axial) branch**, whose displacement field is **exactly divergence-free**, so the Lamé `λ` (bulk/A1) modulus drops out of the equations of motion **identically** rather than by assumption. This is the substrate-native answer to #814's **A2 open half** and **CF-15**: linear P↔SV interface conversion is a **spheroidal-branch** process; the toroidal branch has **no** compressional partner to convert into at a spherically symmetric interface, so the single-channel classification is *structural* in this branch, not asserted. Frozen: `the toroidal (odd-parity) branch is exactly divergence-free, so the bulk modulus drops out identically and there is no linear P-SV conversion partner; the single-channel classification is structural in this branch`.
3. **Op14 saturation.** Enters as the **static constitutive grade** `S(A) = sqrt(1 - A²)` with `A(r) = r_sat/r`, projected into shear by Op16. The kernel knee is **not** run dynamically and the marginal (`A → 1`) point is handled by an exact change of variable, not by a cutoff. Frozen: `Op14 enters as a static constitutive grade S(A); the A -> 1 terminus is handled by an exact change of variable, not by a numerical cutoff or a regularized floor`.
4. **Phase-space vs real-space (A46).** Every verdict-class observable is a **dimensionless ratio**: `ω M_g` (dimensionless eigenvalue), `Q` (ratio of two frequencies), `r_peak/r_sat` (ratio of two radii), and the overtone ratios. **α-CLEAN** — `α` appears nowhere in the chain.
5. **Checkpoint: boundary-not-bulk.** The resonator is a **boundary/graded-shell** object, not a bulk-force object — consistent with the #403/#404 localization ruling. The loss is a **radiative port at infinity** (Ax-3-licensed), and there is **no** `Re{Z}` anywhere in the medium. G6 tests exactly that.
6. **Checkpoint: what the substrate does NOT supply.** The angular index `ℓ = 2` is **not** derived here; it is the quadrupole selection the corpus carries for the GW channel. Stated so it is not mistaken for an output.

### Pre-test physics check (`pre-test-physics-check`, Rule 16 — ONE plumber question surfaced to Grant BEFORE the design locks)

> **Grant — plumber-physically.** The wall at `r_sat` is a free surface: the shear stiffness there is exactly zero, so the pipe wall offers **no** sideways resistance and the fluid at that face can slosh freely. Everything outward of it is a **stiffness ramp** climbing to full vacuum stiffness over about half a wavelength. The question this design cannot answer for itself: **when you stand at that free face and shake it sideways at `ℓ = 2`, is the thing that rings the *face* (a rim, a bell) or the *ramp* (a horn)?** The design does **not** pick — it computes the eigenfunction and **reports where the mode actually sits** (BIN-3, four reachable sub-bins including "there is no interior maximum, so 'where it sits' is not a well-posed question for this mode"). That is #814's FORK-1 handed to the substrate rather than to either of us. **What I need from you, if you disagree with the framing:** the design fixes the free face as a *zero-traction* boundary — a **motion antinode, force node**. If the frozen infalling matter is part of the pipe wall rather than the water in the pipe (#814 FORK-3(b)), that face is instead **clamped** and the whole standing-wave pattern shifts a quarter wavelength. This lane does **not** run FORK-3(b), because the brief's own canonical input list fixes the SHORT (`Z_shear → 0`) termination — see §10 FORK-3. The clamped case is nevertheless run as a **self-test** (FT-2) and its pole is **reported as a diagnostic**, so if you rule the other way the number is already on the record.

### Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE results — and it is not uniform across the bins

The whole problem, written in units of `r_sat`, has **no free parameter at all**: the profile is `A = r_sat/r`, i.e. `A = 1/(r/r_sat)`; the kernel is `S = sqrt(1 - A²)`; the speed is `c_shear = c₀·sqrt(S)`; the inertia is the cold `ρ₀`. Therefore the eigenvalue in the natural scale-free variable,

`Ω ≡ ω · r_sat / c₀`,

is a **pure number** fixed by the profile SHAPE, the Ax-4 kernel, and `ℓ` — **and by nothing else.** The consequences are asymmetric and must be stated in advance:

| output | rides `r_sat`'s coefficient `7`? | class |
|---|---|---|
| `ω_R M_g` (BIN-1) | **YES** — `ω_R M_g = Re(Ω)/x_sat` with `x_sat = 7` | **VALUE-CONSISTENCY.** The `7` is the `1/7` trace-reversed bulk projection, which takes `ν_vac = 2/7` as **input** ([`one-seventh-impedance-projection.md:18`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md): *"the $1/7$ boundary is a projection of a GR-imported ratio, not a first-principles lattice output"*). **May NOT be headlined as value-level emergence.** |
| **`Q = ω_R/(2\|ω_I\|)` (BIN-2)** | **NO — it cancels exactly** | **`ν_vac`-FREE, therefore EMERGENCE-CAPABLE at value level.** `Q = Re(Ω)/(2\|Im(Ω)\|)`; the `x_sat` conversion divides out identically. This is the object #808 §2.1 says the lane must find: *"dimensionlessness is cheap; cancellation is the actual requirement"* — and here the cancellation is **structural (exact), not numerical.** |
| `r_peak/r_sat` (BIN-3) | **NO** | `ν_vac`-free ratio; **FORM-class** statement about where the mode lives. |
| overtone ratios (BIN-4) | **NO** | `ν_vac`-free ratios. |

Frozen tag: `Q, the localization ratio and the overtone ratios are exactly nu_vac-free (the r_sat scale divides out identically); omega_R*M_g is NOT and is VALUE-CONSISTENCY class because the 7 in r_sat = 7GM/c^2 is the 1/7 projection of the GR-imported nu_vac = 2/7`.

**The `ν_vac → 0` sensitivity #808 §2.1 requires per candidate ratio is therefore discharged ANALYTICALLY rather than numerically for `Q`:** `Q` does not contain `x_sat` at all, so setting `ν_vac → 0` (equivalently `x_sat → ∞`) leaves `Q` **exactly unchanged**. The driver nonetheless **measures** this by re-running the whole chain at `x_sat ∈ {5, 7, 11}` and checking `Q` is invariant to `<= 1e-9` — that is gate **G8**, and it is the machine version of the argument (`reconcile-don't-declare`).

---

## §1 — WHAT THIS LANE COMPUTES, AND WHAT IT EXPLICITLY DOES NOT

**COMPUTES.** The complex quasinormal eigenvalues `ω M_g` of the `ℓ = 2` **toroidal shear** mode of the canonical graded saturation profile, with a traction-free (`Z_shear → 0`, `Γ_shear = −1`) inner terminus at `r_sat` and an outgoing-radiation condition at infinity; and from them `ω_R M_g`, `Q = ω_R/(2|ω_I|)`, the eigenfunction's radial localization, and the overtone ladder.

**DOES NOT:**
- **X1 — does NOT derive `ℓ = 2`.** The quadrupole selection is an input (§0 walk item 6).
- **X2 — does NOT derive `ν_vac`, `K = 2G`, or the `7` in `r_sat`.** Their value provenance is GR-IMPORT, closed by PR #261/#506 and untouched here.
- **X3 — does NOT touch the spin (`a_* > 0`) mapping.** The `r_Ω`/`√(1+ν_vac)` factor, the `Ω` form fork (#808 F2), and the v1/v2 mapping are **out of scope**; this is the `a_* = 0` anchor only. Per #808 F8 that is where `87.7%` of the banked `−5.44%` catalog deficit already lives.
- **X4 — does NOT compute a port-`Q`, a radiation resistance, or a Chu/Collin–Rothschild stored-energy `Q`.** Those are the spin-1 estimators of #814's FORK-11. This lane computes the **pole** and therefore does not have to choose among them (§10).
- **X5 — does NOT adjudicate #814 FORK-12** (is killing the `Q ∝ ℓ` scaling a win or a falsifier?). Grant has not answered it. The `ℓ`-ladder **is** computed and **is** reported, explicitly as `DIAGNOSTIC — no bin, no verdict; FORK-12 is unanswered and this lane does not adjudicate it`. Adjudicating it after seeing the ladder is exactly the post-hoc move Rule 11 forbids.
- **X6 — does NOT run FORK-3(b)** (`ρ_eff = ρ₀/S³` as the shear-wave inertia). Reason and routing in §10.
- **X7 — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry**, whatever the outcome.

---

## §2 — THE DERIVED SPIN-2 RADIAL EQUATION (the #814 R7 prerequisite, discharged here)

**The prerequisite, verbatim from #814 CF-8:** *"`Z_ℓ(x) = jη h_ℓ′(x)/h_ℓ(x)` is the **SPIN-1 vector-multipole impedance** … The GW observable is a **SPIN-2 tensor multipole** … **Therefore: 'derive the spin-2 spherical-mode impedance; do not import the spin-1 one' is an explicit R7 prerequisite.**"* What follows is that derivation. **No spin-1 impedance is imported anywhere in this lane.**

### §2.1 The continuum equations the corpus carries

The shear channel is a linear, lossless-reactive elastic continuum with a radially graded shear modulus and the cold inertia:

- `ρ(r) = ρ₀` — the cold lattice inertia (FORK-3 leading reading (c)/(a); §10);
- `G_shear(r) = ρ₀ c_shear(r)²` with `c_shear = c₀·sqrt(S)` — **Op16, CANONICAL** ([`common/operators.md:56`](../manuscript/ave-kb/common/operators.md), row `Op16 | Universal Wave Speed | c_shear = c_0·sqrt(S) | CANONICAL`), reinforced verbatim at [`saturating-modulus-and-backreaction.md:60`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md): *"**SHEAR softens:** $c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection, NOT a second kernel."*
- `S(A) = (1 - A²)^{1/2}` and `A = ε_11/ε_yield` with `ε_yield = 1` — **Ax 4**, verbatim from the same leaf's Resultbox at `:51-52`: `A=\varepsilon_{11}/\varepsilon_{\text{yield}}\ (\varepsilon_{\text{yield}}=1)`, `S(A)=(1-A^2)^{1/2}`.
- `ε_11 = 7GM/(c²r)` — [`temporal-spatial-lattice-decomposition.md:14`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md), clm-rd9cjm.

Hence `G_shear(r) = G₀·S(r)`, `G₀ ≡ ρ₀c₀²`, and `Z_shear(r) = ρ₀ c_shear(r) = Z_{sh,0}·sqrt(S) → 0` at `r_sat` — which is the canonical SHORT: [`vol3/claim-quality.md:123`](../manuscript/ave-kb/vol3/claim-quality.md), verbatim *"a solid$\to$liquid free surface ($G_{shear} \to 0$) is exactly a $Z_{shear} \to 0$ short"*.

### §2.2 The toroidal (odd-parity) branch, and why it is the honest spin-2 channel

Take the displacement field in the **toroidal** vector-spherical-harmonic basis,

`u(r,θ,φ,t) = W(r) · T_{ℓm}(θ,φ) · e^{−iωt}`, `T_{ℓm} ≡ ∇ × (r̂ r Y_{ℓm})`,

which is **purely tangential and exactly divergence-free**, `∇·u ≡ 0`. Two consequences, both load-bearing:

1. **The Lamé/bulk modulus drops out identically.** The stress is `σ = λ(∇·u)I + 2μ ε` with `∇·u ≡ 0`, so only the shear modulus `μ ≡ G_shear` survives. The A1 sector is not "assumed negligible" — it is **absent**. This is the structural form of the A1 ⊥ T2 discipline.
2. **This is the branch that is isospectral with the GR comparator at `a_* = 0`.** In GR the `ℓ = 2` QNM has an odd-parity (Regge–Wheeler / axial) and an even-parity (Zerilli / polar) sector, and at zero spin they are **isospectral** (Chandrasekhar's identity), so `ω M_g = 0.373672 − 0.088962i` is the eigenvalue of **both**. The toroidal elastic branch is the direct analogue of the odd-parity sector. Comparing the derived toroidal eigenvalue against the frozen `a_* = 0` comparator is therefore legitimate **and the parity choice costs nothing at zero spin**. *(Stated as the reason the comparison is admissible, not as a claim that AVE reproduces GR's parity structure — see §7 BIN-1's class line.)*

### §2.3 The radial system (derived, `[derived]`)

Substituting the toroidal ansatz into `ρ ∂_t²u = ∇·σ` and projecting onto `T_{ℓm}` gives the two-component first-order system in the displacement scalar `W(r)` and its conjugate traction `T(r) ≡ μ(r)·(W′ − W/r)`:

```
W′ = W/r + T/μ
T′ = −3T/r + [ (ℓ−1)(ℓ+2)·μ/r² − ρω² ]·W
```

equivalently the single second-order self-adjoint form

```
(1/r³)·d/dr[ r³ μ (W′ − W/r) ] + [ ρω² − (ℓ−1)(ℓ+2)·μ/r² ]·W = 0
```

**Two internal consistency checks of this derivation, both frozen as gates rather than asserted:**

- **Homogeneous reduction.** With `μ, ρ` constant the system reduces to `W″ + (2/r)W′ + [k² − ℓ(ℓ+1)/r²]W = 0`, `k² = ρω²/μ` — the spherical-Bessel equation, using `2 + (ℓ−1)(ℓ+2) = ℓ(ℓ+1)`. So the **radial functions are the same spherical Hankel functions as the spin-1 problem**, exactly as #814's F10 caution says they must be. Gate **G1** measures this to machine precision.
- **What is NOT the same as spin-1, and this is the whole point.** The **impedance relation** is `T = μ(W′ − W/r)` — *not* `Z_ℓ ∝ h_ℓ′/h_ℓ`. The extra `−W/r` term is the tensor-rank content, and it is what makes the traction-free condition at the wall a genuinely different boundary condition from the spin-1 one. Likewise the **stored-energy weighting** carries `(ℓ−1)(ℓ+2)`, not `ℓ(ℓ+1)`:
  ```
  E_strain(r) ∝ μ(r)·[ |W′ − W/r|² + (ℓ−1)(ℓ+2)·|W|²/r² ]·r²
  E_kin(r)    ∝ ρ(r)·|ω|²·|W|²·r²
  ```
  which is the Euler–Lagrange partner of the radial equation above (checked by re-deriving the equation from the energy functional; **gate G2** below is the numerical form of that check). **This weighting is used for BIN-3 and is NOT the spin-1 Chu/Collin–Rothschild weighting.**

Frozen: `the radial system is the toroidal (odd-parity, exactly divergence-free) branch derived from the shear-channel continuum equations; the radial functions coincide with spherical Hankel functions in the homogeneous limit but the impedance relation T = mu(W' - W/r) and the (l-1)(l+2) stored-energy weighting are the spin-2 ones and no spin-1 vector-multipole impedance is imported anywhere in this lane`.

### §2.4 The two boundary conditions, both canonical, neither tuned

- **Inner, at `r = r_sat`: traction-free.** `T(r_sat) = 0`. This *is* `Z_shear → 0`, `Γ_shear = −1`, the canonical SHORT (`vol3/claim-quality.md:123`). It is a **force node / motion antinode** — the free surface of #814's PART-3 Step 0.
  **Why the terminus is a regular point and not a numerical problem.** Near the wall `1 − A² = (r−r_sat)(r+r_sat)/r²`, so with `x ≡ r − r_sat`, `S ∝ x^{1/2}` and `μ ∝ x^{1/2}`. The indicial exponents of the radial equation at `x = 0` are `s = 0` and `s = 1/2`; the `s = 0` branch has `T(0) = 0` and the `s = 1/2` branch has `T(0) ≠ 0`, so **the traction-free condition selects exactly one branch**. Under the exact substitution `x = σ²` the two-component system becomes **analytic at `σ = 0`** and the initial condition is exactly `(W, T) = (1, 0)` at `σ = 0` — no series start, no offset, no regularized floor. §4 states this as an implementation, §5 G3 measures it.
- **Outer, `r → ∞`: outgoing radiation only.** The far medium is the cold Regime-I lattice (`S → 1`, `μ → G₀`, `c → c₀`) — a matched line, a legal radiating port. **This is the ONLY loss in the ledger**, which is #814's CF-11 taken at face value: the wall is lossless and contributes nothing to `Q`.
  **The far field is NOT free space, and that is not a detail.** `μ(r) = sqrt(1 − r_sat²/r²) = 1 − r_sat²/(2r²) + O(r^{−4})`, so the grade contributes a `1/r²` tail that is the **same order as the centrifugal term** — the effective angular barrier is shifted by `ω²r_sat²/2`, an `O(1)` change at `ℓ = 2`. Truncating the profile at any finite radius and matching to plain spherical Hankel functions would therefore commit an `O(ω r_sat²/R)` phase error. The instrument matches instead to an **exact asymptotic outgoing series generated from the actual `μ(r)`, `ρ(r)`** (§4.2), and gates its `R_match`- and order-independence (G4, G5).

---

## §3 — IMPORT LEDGER (every number the solver consumes, tagged; `substrate-first-for-numbers`)

| # | Input | Value / form | Class | Source |
|---|---|---|---|---|
| **I1** | Saturation-wall radius | `r_sat = 7GM/c² = 7 M_g`, i.e. `x_sat = 7` | **`[canon]`** — form-derived, **VALUE rides the GR-imported `ν_vac`** | `vol3/claim-quality.md:121`; `temporal-spatial-lattice-decomposition.md:14`; the `1/7` projection provenance at `one-seventh-impedance-projection.md:18` |
| **I2** | Saturation amplitude profile | `A(r) = ε_11/ε_yield = r_sat/r`, `ε_yield = 1` | **`[canon]`** | `saturating-modulus-and-backreaction.md:51`; `vocabulary-register.md:309` |
| **I3** | Ax-4 kernel | `S(A) = (1 − A²)^{1/2}` | **`[canon]` — Axiom 4** | `saturating-modulus-and-backreaction.md:52` |
| **I4** | Shear-speed projection | `c_shear = c₀·S^{1/2}` (Op16) | **`[canon]`** | `common/operators.md:56`; `saturating-modulus-and-backreaction.md:60` |
| **I5** | Shear-wave inertia | `ρ(r) = ρ₀` (cold lattice inertia) | **`[canon, FORK-3 leading reading]`** — `ρ_eff = ρ₀/S³` is scoped to **collapsing matter** at three canonical sites, not to the lattice's own shear inertia | `interior-singularity-resolution.md:14,:23`; `vol3/claim-quality.md:124`; the naming gap at `vol3/claim-quality.md:122` is #814 CF-7, **routed not repaired** |
| **I6** | Inner boundary condition | traction-free, `T(r_sat) = 0` (`Z_shear → 0`, `Γ_shear = −1`) | **`[canon]`** | `vol3/claim-quality.md:123` |
| **I7** | Outer boundary condition | outgoing radiation into the cold matched lattice | **`[canon]` — Regime-I radiative port, Ax-3-licensed** | §0 REGIME header; the RADIATIVE-PORT carve at `vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md` |
| **I8** | Angular index | `ℓ = 2` (quadrupole) | **`[canon, INPUT not derived]`** | §1 X1 |
| **I9** | Unit choice | `M_g = 1`, `c₀ = 1`, `ρ₀ = 1`, hence `G₀ = 1` | **`[dimensionless by construction]`** — every observable is a ratio, so the unit choice cancels | this lane |
| **I10** | `ν_vac = 2/7` | imported **read-only** from `ave.core.constants.N_NU`; used ONLY to form the `r_eff = r_sat/(1+ν_vac)` comparator and the `r★` turning-point comparator | **`[canon]` — VALUE GR-IMPORTED (PR #261/#506)** | `src/ave/core/constants.py:397` |
| **I11** | GR cold comparator | `ω_R M = 0.37367`, `ω_I M = 0.08896` at `a_* = 0`, read **programmatically** from the frozen `KERR_QNM` dict | **`[GR-IMPORTED comparator — the frozen C-comparator, inherited unchanged]`** | `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51` (`[branch @ 7aaec46c]`) |
| **I12** | GR overtone real parts | `ω_R M (ℓ=2, n=1) = 0.346711`, `(ℓ=2, n=2) = 0.301053`, read **programmatically** from the in-repo `SCHW_OMEGA_R` dict | **`[GR-IMPORTED comparator]`** | `research/2026-07-20_ringdown-systematics_checks.py:68-73` |
| **I13** | GR overtone imaginary part | `ω_I M (ℓ=2, n=1) = 0.273915` | **`[GR-IMPORTED comparator — EXTERNAL, no in-repo carrier]`** — Berti–Cardoso–Will Schwarzschild `s=2` living-review table. Frozen here so it is fixed before results; its lack of an in-repo carrier is **disclosed, not hidden** | external |
| **I14** | Standing AVE shortcut | `ω_R M_g = 18/49`, `Q = ℓ = 2`, `r_eff = 49M_g/9`, `r★/r_sat = 1.2247` | **`[corpus comparators — the objects under test]`** | `vol3/claim-quality.md:198`; `qnm-quality-factor.md`; `regime-eigenvalue-method.md:52`; #814 CF-9 |
| **I15** | Solver numerics | `n_steps`, `R_match`, series order `N`, contour sampling, root-polish iterations, scan grid | **`[ENGINEERING CHOICE — tagged, frozen in §4/§5]`** | this lane |

**R8 audit rule (frozen).** `every number the solver consumes appears on this ledger with its tag; no SM/GR convention default enters anywhere, and in particular no spin-1 vector-multipole impedance, no Chu/Collin-Rothschild stored-energy weighting, and no Regge-Wheeler or Zerilli potential is used as an input`.

---

## §4 — THE INSTRUMENT (frozen; every numeric parameter fixed here)

### §4.1 Regular-at-the-wall integration

Substitute `r = r_sat + σ²` (so `x = σ²`, `μ = σ·m̂(σ)` with `m̂(σ) = sqrt(2r_sat + σ²)/(r_sat + σ²)` **analytic and nonzero at `σ = 0`**). The system becomes

```
dW/dσ = 2σ·W/r + 2·T/m̂(σ)
dT/dσ = 2σ·[ −3T/r + (ℓ−1)(ℓ+2)·μ W/r² − ρω²W ]
```

— analytic at `σ = 0`, integrated from **exactly** `(W, T) = (1, 0)` at `σ = 0` (the traction-free branch) out to `σ_match = sqrt(R_match − r_sat)`. Integrator: **fixed-step classical RK4**, vectorized over the complex-`ω` grid, **no RNG, no adaptivity, fully deterministic**. Frozen: `the wall is reached exactly via the r = r_sat + sigma^2 substitution, which makes the two-component system analytic at sigma = 0; the initial condition is exactly (W,T) = (1,0) and no offset, series start, or regularized modulus floor is used`.

The `S^{1/4}` counterfactual (§10 FORK-2) uses `r = r_sat + σ⁴` instead, which is the corresponding analytic substitution for `μ ∝ x^{1/4}`.

### §4.2 The exact asymptotic outgoing solution (no free-space truncation)

Write `W_out(r) = e^{iωr}·Σ_{n≥1} c_n r^{−n}` and generate `c_n` by the exact recursion obtained from the radial equation in `z = 1/r`, using the truncated Taylor series of the **actual** `μ(z)` and `ρ(z)`. With `α(z) ≡ 2iω + 2z + g`, `β(z) ≡ ω²(ρ/μ − 1) − ℓ(ℓ+1)z² − gz + iω(2z + g)`, `g ≡ μ′/μ`, matching the coefficient of `z^m` gives, for `m ≥ 3`,

```
c_{m−1} = −[ (m−2)(m−1)c_{m−2} − Σ_{n=1}^{m−2} n c_n α_{m−n−1} + Σ_{n=1}^{m−2} c_n β_{m−n} ] / ( 2iω(2−m) )
```

with `c_1 = 1`. The **ingoing** solution is the same object at `ω → −ω` (the equation depends on `ω` only through `ω²` and the explicit `e^{±iωr}`). At zero grade the recursion **terminates at `n = ℓ+1` and reproduces `h_ℓ^{(1)}(ωr)` exactly** — that is gate **G1**.

The QNM condition is then that the **ingoing** amplitude vanish at `R_match`:

```
N(ω) ≡ W_num·T_out − T_num·W_out  = 0        (analytic in ω; its zeros ARE the poles)
```

with `T_out = μ(W_out′ − W_out/r)` built from the same spin-2 impedance relation.

### §4.3 Frozen numerics

`R_match = 40 M_g` (primary), `series order N = 20`, `n_steps = 16000` for the scan and `n_steps = 64000` for the polish, scan grid `ω_R M_g ∈ [0.02, 2.00]` × `|ω_I| M_g ∈ [1e-3, 1.00]` sampled `181 × 91` uniformly, complex-secant (Muller) polish to `|Δω|/|ω| <= 1e-12` or 60 iterations, argument-principle contour on the same rectangle sampled at `4096` points per full traverse. Independence sets for the gates: `R_match ∈ {25, 40, 60}`, `N ∈ {12, 20, 28}`, `n_steps ∈ {16000, 32000, 64000}`, contour sampling `{2048, 4096, 8192}`.

### §4.4 Why `research/drivers/` and not `src/ave/`

Same discipline as #801 §2: this is a **single-lane continuum instrument**, deliberately not a discretization of the srs stencil (§0 walk item 1). Promoting it into the engine tree would place a continuum operator where later readers would reasonably assume the engine's K4/Cosserat guarantees apply. It ships as a lane driver importing `ave.core.constants` **read-only**. Frozen: `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`.

---

## §5 — THE FROZEN SOLVER-CERTIFICATION GATES (G1–G8), with numeric tolerances

| Gate | What it certifies | FROZEN criterion |
|---|---|---|
| **G1** | **Asymptotic series ↔ spherical Hankel at zero grade.** The spin-2 far-field solution must reduce to the exact `h_ℓ^{(1)}` at zero grade — the check that the radial functions are right before any grade is switched on | `at zero grade the outgoing series log-derivative matches the exact spherical-Hankel log-derivative to <= 1e-12 relative, for every (ell, omega, R) in the frozen check set {ell in 1,2,3} x {0.4, 0.4-0.09i, 1.3-0.4i} x {12, 25, 40}` |
| **G2** | **Energy functional ↔ radial equation consistency** — the `(ℓ−1)(ℓ+2)` stored-energy weighting of §2.3 must be the Euler–Lagrange partner of the integrated equation, measured numerically on the derived eigenfunction | `the residual of the Euler-Lagrange identity built from the frozen spin-2 energy weighting, evaluated on the converged eigenfunction over the frozen radial sample set, is <= 1e-9 relative` |
| **G3** | **Wall-terminus regularity + step convergence.** The `σ`-substituted system integrates from the wall with no offset parameter | `\|omega(n_steps=64000) - omega(n_steps=16000)\| / \|omega\| <= 1e-8 for the fundamental pole on the primary branch` |
| **G4** | **Matching-radius independence** (the far-field-tail control) | `\|omega(R_match) - omega(R_match')\| / \|omega\| <= 1e-8 for every pair in R_match in {25, 40, 60}` |
| **G5** | **Series-order independence** | `\|omega(N) - omega(N')\| / \|omega\| <= 1e-8 for every pair in N in {12, 20, 28}` |
| **G6** | **Ax-3 lossless-reactive discipline.** No `Re{Z}` is smuggled anywhere: close the system (traction-free at BOTH `r_sat` and an outer wall at `R_match`) and the eigenvalues must be **REAL** — the only loss in the open problem is the radiative port | `every eigenvalue of the CLOSED (doubly traction-free) cavity has \|Im omega\| / \|omega\| <= 1e-10, and the assembled real-omega transfer of the open problem carries max\|Im(coefficient)\| = 0 exactly` |
| **G7** | **Pole count is proven, not assumed.** The argument-principle count over the frozen rectangle must equal the number of distinct located roots, and must be invariant under contour refinement | `the argument-principle winding count over the frozen rectangle is an integer to <= 1e-3, is identical at contour sampling 2048, 4096 and 8192, and equals the number of distinct poles located by the frozen polisher` |
| **G8** | **`ν_vac`-cancellation, MEASURED** (the #808 §2.1 requirement, reconciled not declared) | `Q, r_peak/r_sat and the overtone ratios are invariant to <= 1e-9 relative across x_sat in {5, 7, 11}, while omega_R*M_g scales as 1/x_sat to <= 1e-9 relative` |
| **G9** | **Determinism** | `two independent full driver runs produce an identical results digest (SHA-256 over the results object minus timing fields)` |

**Certification classes (exhaustive).**
- **`SOLVER-CERTIFIED`** — `all of G1..G9 PASS and all of FT-1..FT-5 FIRE`.
- **`SOLVER-CERTIFIED-SCOPED`** — `all gates pass and all self-tests fire, but at least one gate passes only over a REDUCED parameter set, stated explicitly in the result headline`.
- **`SOLVER-NOT-CERTIFIED`** — `any of G1..G9 FAILS, OR any of FT-1..FT-5 fails to fire`. **A gate that cannot fail voids the certification exactly as hard as a gate that fails.** Under this class **no physics bin is adjudicated** (§7 precedence).

---

## §6 — GATE-FIREABILITY SELF-TESTS (FT-1…FT-5) — each MUST FIRE

**The rule (frozen).** `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is SOLVER-NOT-CERTIFIED regardless of how many gates passed`.

| # | Targets | Deliberate mis-specification | FROZEN firing criterion |
|---|---|---|---|
| **FT-1** | **G1** | perturb one asymptotic-recursion coefficient by `1e-9` relative | `the corrupted recursion MUST return a G1 log-derivative mismatch >= 1e-11` |
| **FT-2** | **G3 / the physics of the inner BC** — proves the canonical SHORT is **load-bearing** and not decoration | replace the traction-free inner condition by a **clamped** one (`W(r_sat) = 0`, the `Γ = +1` open/clamped alternative of #814 FORK-3(b)/CF-13) | `the clamped-wall fundamental pole MUST differ from the traction-free one by >= 1e-2 relative in \|omega\|` |
| **FT-3** | **G6** (Ax-3) | give the shear modulus a smuggled loss term, `Im(mu)/Re(mu) = 1e-3` | `the lossy closed cavity MUST return \|Im omega\|/\|omega\| >= 1e-5` |
| **FT-4** | **G4 / G5** — proves the far-field matching is a real agreement, not two evaluations of one code path | match at `R_match = 8 M_g`, i.e. **deep inside the grade**, where the asymptotic series is not valid | `the out-of-regime match MUST return \|omega(R=8) - omega(R=40)\|/\|omega\| >= 1e-3` |
| **FT-5** | **G7** — proves the winding count is a live measurement | run the argument principle on (a) a sub-rectangle constructed to exclude every located pole, and (b) the analytically-solvable zero-grade problem whose root count is known in closed form (`ℓ+1` roots, from the degree-`(ℓ+1)` polynomial `i x u + x u′ − (ℓ+2)u` with `u ≡ x^{ℓ+1}h_ℓ e^{−ix}`) | `case (a) MUST return count 0 and case (b) MUST return count equal to the closed-form root count for ell in {1,2,3}` |

---

## §7 — THE FROZEN PHYSICS BINS (exhaustive; every bin REACHABLE; precedence stated)

**Rule-11 fence, stated up front and binding.** `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the solver returns is banked`. The comparator is the frozen `a_* = 0` C-comparator inherited unchanged from #774/#808. There is **no free parameter to tune** — that is the point of the lane.

**PRECEDENCE (frozen, evaluated in this order).** `BIN-F-SOLVER` > `BIN-F-PROFILE` > `BIN-F-NOPOLE` > `BIN-1/2/3/4`. If an earlier bin fires, the later ones are reported as `N/A — not adjudicated` and **no verdict language is used about them.**

### Honest-failure bins (each reachable, each with a disposition)

| bin | condition | disposition |
|---|---|---|
| **`BIN-F-SOLVER`** | `any of G1..G9 FAILS or any of FT-1..FT-5 fails to fire` | **SOLVER-NOT-CERTIFIED.** No physics bin adjudicated; the failing gate's numbers are reported; the lane returns the instrument failure as its result. No claim, no walk-back, no solidity change. |
| **`BIN-F-PROFILE`** | `the canonical input set of section 3 is found to be internally inconsistent at solve time (two canonical statements that cannot both hold on the domain)` | **flag-don't-fix.** Both file paths + verbatim content surfaced to Grant and the auditor lane; **neither side reframed to match the other**; no bin adjudicated. This is #808's bin (e) instantiated. |
| **`BIN-F-NOPOLE`** | `the certified solver returns argument-principle count 0 over the frozen rectangle` | **A decisive, clean negative and a GOOD outcome.** It would say: the canonical graded profile, with the canonical Ax-4 kernel, the canonical Op16 shear projection and the canonical SHORT termination, supports **no `ℓ = 2` quasinormal resonance at all** in a band that comfortably brackets both GR and the standing corpus value — which falsifies the standing ringdown chain at the level of *existence*, not of value. Banked as such; branch closed. |

### BIN-1 — the real part `ω_R M_g`

`D_omega ≡ omega_R_derived / omega_R_GR − 1`, with `omega_R_GR = 0.37367` read programmatically from the frozen `KERR_QNM[0.00]` row (I11).

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-1-MATCH`** | `abs(D_omega) < 0.03` |
| **`BIN-1-NEAR`** | `0.03 <= abs(D_omega) < 0.10` |
| **`BIN-1-MISS`** | `abs(D_omega) >= 0.10` |

Reported alongside, **not a separate class**: `D_omega_shortcut ≡ omega_R_derived/(18/49) − 1`, the deviation from the standing corpus shortcut `18/49 = 0.36735`; and the sign of both. **Class line (mandatory in the result headline):** `BIN-1 is VALUE-CONSISTENCY class, not emergence: omega_R*M_g carries the GR-imported nu_vac through the 7 in r_sat`.

### BIN-2 — the quality factor `Q` (★ the emergence-capable axis)

`Q_derived ≡ omega_R/(2*abs(omega_I))`; `Q_GR ≡ omega_R_GR/(2*omega_I_GR)` computed from the same frozen row (`= 0.37367/(2·0.08896)`); `D_Q ≡ Q_derived/Q_GR − 1`.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-2-MATCH`** | `abs(D_Q) < 0.03` |
| **`BIN-2-NEAR`** | `0.03 <= abs(D_Q) < 0.10` |
| **`BIN-2-MISS`** | `abs(D_Q) >= 0.10` |

**And the three-way discriminator, frozen separately** (this is the axis that decides whether the substrate prefers GR's `2.10021` or the corpus's `2π`-convention `Q = ℓ = 2`):

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-2-CLOSER-GR`** | `abs(Q_derived - Q_GR) < abs(Q_derived - 2.0)` |
| **`BIN-2-CLOSER-CONVENTION`** | `abs(Q_derived - 2.0) < abs(Q_derived - Q_GR)` |
| **`BIN-2-EQUIDISTANT`** | `abs(abs(Q_derived - Q_GR) - abs(Q_derived - 2.0)) <= 1e-6` |

**Class line (mandatory in the result headline):** `BIN-2 is the nu_vac-FREE axis: Q = Re(Omega)/(2*abs(Im(Omega))) contains no r_sat scale, so the GR-imported 7 cancels exactly; G8 measures the cancellation rather than asserting it`.

### BIN-3 — where the mode actually lives (FORK-1, handed to the substrate)

> **★ IDENTITY NOTE, frozen BEFORE results so it cannot be discovered afterwards.** The "9/7-above-cutoff" statement is **not an independent axis**. `r_eff = r_sat/(1+ν_vac) = 49M_g/9` and the cutoff identity `k r_eff = ℓ` (#814 CF-8) together give `k₀ r_sat = ℓ(1+ν_vac) = 18/7 = 2.5714`, and `k₀ r_sat = 7·ω_R M_g` identically — so testing `k₀r_sat` against `18/7` **is** testing `ω_R M_g` against `18/49`, which is BIN-1's companion number. It is reported as `k0_r_sat` with the tag `IDENTITY — not independent of BIN-1's shortcut comparison`. **The genuinely independent localization content is the eigenfunction's own radial profile, which the standing chain never computes**, and that is what BIN-3 adjudicates.

Frozen observable: `u ≡ r_peak/r_sat`, where `r_peak` maximizes the frozen spin-2 mode-energy density `E(r) = rho|omega|^2|W|^2 r^2 + mu(|W' - W/r|^2 + (ell-1)(ell+2)|W|^2/r^2) r^2` over the frozen window `r/r_sat in [1.0, 2.0]`. A second, independent measure `u_kin` uses the kinetic term alone.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-3-RIM`** | `1.00 <= u <= 1.10` — the mode hugs the wall; supports the rim-ring reading (#814 FORK-1(a)) |
| **`BIN-3-RAMP`** | `1.10 < u <= 1.50` — the mode sits in the stiffness ramp; supports the graded-shell / curvature-leaking reading (#814 FORK-1(d)). Sub-flag `BIN-3-RAMP-TURNING-POINT` if additionally `abs(u - 1.2247) <= 0.05` (the #814 CF-9 turning point) |
| **`BIN-3-OUTER`** | `u > 1.50` — neither standing picture locates the mode |
| **`BIN-3-MONOTONE`** | `the energy density has no interior maximum in the frozen window (the maximum sits at an endpoint)` — localization is not a well-posed observable for this mode; the endpoint is reported |
| **`BIN-3-DISCORDANT`** | `abs(u - u_kin) > 0.10` — the two frozen measures disagree; both are reported and no localization verdict is banked |

**The `(1+ν_vac)` verdict rides on BIN-1's shortcut companion, and it is stated in advance:** `if BIN-1's derived omega_R*M_g deviates from 18/49 by more than 3 percent, the standing chain's r_eff = r_sat/(1+nu_vac) assertion is FALSIFIED as a derivation of the eigenfrequency, and that is a GOOD outcome recorded as such` — #808 F1 already grades the factor unproven *and* un-fitted; a derivation that does not reproduce it retires it rather than patching it.

### BIN-4 — the overtone ladder

Poles are ordered by increasing `|ω_I|`; the fundamental is `n = 0`. `R_I ≡ abs(omega_I_n1)/abs(omega_I_n0)`, GR value `0.273915/0.088962` (I13, EXTERNAL comparator, tagged). `R_R ≡ omega_R_n1/omega_R_n0`, GR value `0.346711/0.373672` read programmatically from the in-repo `SCHW_OMEGA_R` (I12).

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-4-NONE`** | `exactly one pole is located in the frozen rectangle` |
| **`BIN-4-LADDER-MATCH`** | `at least two poles AND abs(R_I/R_I_GR - 1) < 0.10 AND abs(R_R/R_R_GR - 1) < 0.10` |
| **`BIN-4-LADDER-DIFFERENT`** | `at least two poles AND at least one of the two ratios is outside 10 percent` |

### Reachability audit (frozen — every outcome class has a reachable bin)

- `BIN-F-SOLVER` is reachable **and is demonstrated reachable every run**: FT-1…FT-5 each drive an actual gate into its failing state, so the failing bin is exercised, not postulated.
- `BIN-F-PROFILE` is reachable: the canonical set already carries two live tensions this lane touches (#814 CF-7's unnamed `ρ` at `vol3/claim-quality.md:122`, and #808 F9's two saturation-amplitude conventions); either surfacing as an on-domain contradiction lands here.
- `BIN-F-NOPOLE` is reachable: the frozen rectangle is a **finite** region and the argument principle returns an honest integer, which can be `0`.
- `BIN-1/2/3/4` sub-bins are each reachable because each is an interval or a strict comparison on a continuously-valued measured quantity, and the intervals **partition** their axis with no gaps and no overlaps. `BIN-3-MONOTONE` and `BIN-3-DISCORDANT` exist precisely so that "the question is ill-posed for this mode" has a bin rather than forcing a false choice.
- **No outcome requires a criterion to be relaxed after the fact.**

### Mutual satisfiability of the bins (the Protocol-E lesson applied to the BINS, not just the gates)

1. **BIN-1 and BIN-2 are independent axes and can disagree.** `ω_R` and `Q` are separate coordinates of one pole; landing one and missing the other is admissible and is exactly the #808 §1.3 sign structure (`ω_R` over, `Q` under) that the lane exists to explain. Both bin sets are therefore stated without any consistency requirement between them.
2. **BIN-2's two frozen sub-bin families are jointly satisfiable.** `BIN-2-MATCH` and `BIN-2-CLOSER-CONVENTION` can co-occur (`Q` within 3% of `2.10021` while nearer to `2.000` is impossible — 3% of 2.10021 is 0.063 and `|2.10021−2.000| = 0.10021`, so `BIN-2-MATCH ⇒ BIN-2-CLOSER-GR`), and that implication is **stated deliberately**: the discriminator is informative exactly in the `NEAR`/`MISS` region, which is where the standing tension lives.
3. **BIN-3 does not presuppose a localized mode**, so a delocalized or monotone eigenfunction does not break the bin set.
4. **BIN-4 does not presuppose more than one pole**, so a single-resonance spectrum is a bin, not a failure.
5. **The domain and the comparator are compatible.** The domain `[r_sat, ∞)` and the frozen rectangle `ω_R M_g ∈ [0.02, 2.00]` bracket both the GR value `0.3737` and the corpus shortcut `0.3673` by more than a factor of `5` on the low side and `5` on the high side, and bracket `Q ∈ [0.01, 1000]`. There is no frozen precondition that excludes the values the lane is trying to measure — the #796 failure mode is checked for and absent.

---

## §8 — WHAT TRANSFERS FROM THE #801 CERTIFIED SOLVER, AND WHAT MUST BE RE-EARNED

#801 (`research/drivers/continuum_radial_solver.py`, class `A_CERTIFIED`) is the nearest certified instrument in the corpus. Its own thesis is that **gates are re-earned per problem**, and that thesis is applied to it here.

**TRANSFERS (architecture and discipline, cited not copied):**
- the **shape** of the certification battery — frozen gates with numeric tolerances, plus self-tests that must FIRE, plus a determinism digest, plus an exhaustive outcome-class table with a reachability argument;
- the **frozen-first commit order** (prereg alone, pushed, before any driver code);
- the **exact-analytic-exterior discipline** — no sponge, no absorbing layer, no far-field truncation. #801 imposes it with an analytic `H_ν^{(1)}` at a matching radius; this lane needs the stronger version (§2.4) because the grade has a `1/r²` tail that #801's problem does not have;
- the **programmatic-number-check** pattern (#801/#802) — every numeral in the result doc registered against the shipped JSON;
- the **`research/drivers/` placement rationale** (§4.4).

**DOES NOT TRANSFER — must be re-earned, and is (gate in brackets):**
- **the channel.** #801 is the `n = 0` **monopole A1/dilatation** channel; this lane is the `ℓ = 2` **toroidal T2/shear** channel. Different sector, different equation, different modulus. Nothing about #801's certification says anything about this equation. [G1, G2]
- **the eigenproblem class.** #801 solves a **driven, real-frequency scattering** problem. This lane solves a **complex-eigenvalue (quasinormal)** problem — a different mathematical object with a different failure mode (exponentially growing eigenfunctions, non-normalizable states, ill-conditioned subdominant-coefficient extraction). [G3, G4, G5, G7]
- **the singular terminus.** #801's grade terminates at a finite modulus ratio (`S_rail = 1e-3`); this lane's modulus goes to **exactly zero** at a regular singular point of the ODE. That is handled by an exact substitution and must be certified as such. [G3, FT-2]
- **the far-field tail.** #801 matches inside a **homogeneous** exterior; this lane's exterior is never homogeneous (§2.4). [G4, G5, FT-4]
- **the loss ledger.** #801's Ax-3 gate is a driven power balance; this lane's is the reality of the **closed-cavity spectrum**. [G6, FT-3]
- **`A_CERTIFIED` itself.** This lane's class is `SOLVER-CERTIFIED` / `-SCOPED` / `-NOT-CERTIFIED` as defined in §5. It is **not** #801's class and does not inherit it.

Frozen: `no gate, tolerance or certification class is inherited from PR #801; the architecture and the discipline transfer, the certification does not, and every gate in section 5 is re-earned on this equation`.

---

## §9 — MUTUAL SATISFIABILITY OF THE FROZEN REQUIREMENTS (checked BEFORE the freeze; disclosed)

Run on an **uncommitted scratch prototype** before this document was frozen. **Disclosure, stated so it is auditable: only MACHINERY was checked. No physics observable was scouted — no complex root-find was executed on the graded profile, `N(ω)` was never evaluated on a complex grid, and the location of no pole was computed, estimated or looked at before these bins were frozen.** The forward solve was exercised at a single **real** `ω = 1.0`, chosen because a real `ω` cannot be a QNM of a radiating system and therefore carries no information about the answer.

1. **The wall terminus is reachable exactly.** The `σ²` substitution renders the system analytic at `σ = 0`; the prototype integrates from exactly `(1, 0)` with no offset. **Satisfiable — and it removes a frozen parameter (`x₀`) rather than adding one.**
2. **The asymptotic recursion is correct and machine-accurate.** At zero grade it reproduced the spherical-Hankel log-derivative to `≤ 7e-15` for `ℓ ∈ {1,2,3}`, at real and complex `ω`, at `R ∈ {12, 25, 40}`. **G1's `1e-12` tolerance therefore has ≥ 2 orders of headroom. Satisfiable.**
3. **Step convergence is 4th-order and reaches the G3 tolerance inside the runtime budget.** Relative change per doubling fell `3.0e-8 → 1.9e-9 → 1.2e-10 → 7.6e-12`. **G3's `1e-8` is met at `n_steps = 16000`; the polish at `64000` has ~3 orders of headroom. Satisfiable.**
4. **The `μ`, `ρ` Taylor expansions converge at every frozen `R_match`.** At `N = 20` the truncated `μ(z)` matched the closed form to `≤ 2.2e-16` at `R = 25, 40, 60`; at `N = 12` the worst case was `2.0e-11` at `R = 25`. **G5's independence set spans a regime where the low order is measurably worse, so G5 is a live gate rather than a tautology. Satisfiable and informative.**
5. **G4's `R_match` sweep and FT-4's out-of-regime match are on disjoint sub-domains** (`R ∈ {25,40,60}` all outside the grade's working region; `R = 8` inside it), so the two requirements cannot conflict. **Satisfiable and jointly informative.**
6. **FT-5(b) is non-vacuous by a structural argument, not by evaluation.** At zero grade the traction-free condition reduces to `i x u + x u′ − (ℓ+2)u = 0` with `u ≡ x^{ℓ+1}h_ℓ(x)e^{−ix}` a polynomial of degree `ℓ`, so the condition is a polynomial of degree exactly `ℓ+1` and has exactly `ℓ+1` roots. The closed-form count is therefore known **without computing any root**, which is why FT-5(b) could be frozen without scouting.
7. **Runtime.** A single vectorized forward solve at `n_steps = 16000` over the full `181 × 91` scan grid is one integration pass. Frozen: `total battery runtime <= 900 s on the reference machine; a longer run is disclosed, not silently accepted`.
8. **★ The one requirement deliberately NOT frozen, and why (the honest limit).** A requirement that the ingoing coefficient be extracted at **arbitrarily large** `R_match` would be **unsatisfiable in double precision**: with `Im ω < 0` the outgoing solution is the *dominant* one, so the subdominant ingoing coefficient is contaminated at relative order `e^{2|Im ω|R}` times the integration error. It is therefore **not** frozen as an "arbitrarily large `R`" requirement; it is frozen as **independence over the finite set `R_match ∈ {25, 40, 60}`** (G4), where at `|ω_I| ≲ 0.3` the contamination factor stays below `10^{8}·`(integration error `≲1e-12`) `= 1e-4` of the *ingoing* amplitude — well inside G4's tolerance on `ω`. Stated so that a later reader does not mistake the finite set for laziness.

---

## §10 — WHICH #814 FORKS THIS LANE CONSUMES, FENCES, OR DISSOLVES

| fork | this lane's handling |
|---|---|
| **FORK-1** (bell vs horn — where does the mode live?) | **HANDED TO THE SUBSTRATE.** BIN-3 computes the eigenfunction and reports where it sits, with a bin for "ill-posed". Not picked by fiat. |
| **FORK-2** (which constitutive branch; is `S^{1/4}` admissible?) | **KEEP-BOTH, as #814 instructs.** `√S` (Op16, CANONICAL) is **PRIMARY**; the Family-E `S^{1/4}` counterfactual is **run and reported** as a frozen sensitivity with its own `ω`, `Q` and localization numbers, and is **not** adjudicated (Grant has not ruled). Frozen: `the S^{1/4} counterfactual is reported as a sensitivity, never as the primary result, and no bin is adjudicated on it`. |
| **FORK-3** (which `ρ`?) | **(a)/(c) CONSUMED as the input**, because the brief's own canonical input set fixes `Z_shear = ρ·c_shear → 0 ⇒ SHORT` (`vol3/claim-quality.md:123`), which **is** the cold-`ρ₀` branch. **(b) NOT RUN** — it gives `Z ∝ S^{−5/2} → ∞`, an OPEN/clamped terminus that **contradicts a frozen canonical input**; running it would be running a different problem. The naming gap at `vol3/claim-quality.md:122` (canon writes `Z_shear = ρ c_shear` and never says which `ρ`) is **surfaced and routed, not repaired**. Its pole is nevertheless reported as a diagnostic via FT-2's clamped-wall run, so the sensitivity is on the record. |
| **FORK-4** (is `9/7` the `(1+ν)` factor's job, or coincidence?) | **ANSWERED BY MEASUREMENT, and the identity that makes the question answerable is frozen first** (BIN-3's IDENTITY NOTE). The derivation either reproduces `k₀r_sat = 18/7` or it does not. |
| **FORK-5** (disposal of transmitted shear) | **STRUCTURALLY MOOT IN THIS BRANCH.** The toroidal branch is exactly divergence-free and has no compressional partner at a spherically symmetric interface, so linear P↔SV conversion is absent by construction (§0 walk item 2). This does **not** settle the fork for the spheroidal branch, and this lane does not claim it does — **routed, with the branch limitation stated.** |
| **FORK-6** (which echo cavity?) | **OUT OF SCOPE.** No echo delay is computed and none is claimed. The banked corpus echo prediction is untouched. |
| **FORK-7** (vessel anisotropy) | **OUT OF SCOPE** — the profile is isotropic-in-shear by the canonical input set; the R6 vessel-state transplant is untested and stays untested. |
| **FORK-8** (spin as Doppler vs circulator) | **OUT OF SCOPE** — `a_* = 0`. |
| **FORK-9** (does Op6's radial phase-matching apply?) | **PARTIALLY ANSWERED, empirically rather than formally.** BIN-4 measures whether the graded shear cavity has a radial-overtone ladder at all. It does **not** derive Op6's `∫k dr + φ_Γ = n_r π` condition for this cavity — that remains open and is **routed**. |
| **FORK-10** (port-`Q` → pole-`Q` transfer) | **DISSOLVED BY CONSTRUCTION.** This lane computes the complex pole directly. There is no port calculation and therefore no transfer, no single-pole approximation, and no error bar on a transfer that is never made. Frozen: `no port-Q is computed and no port-to-pole transfer is performed; the reported Q is the pole-Q that the GR comparator is`. |
| **FORK-11** (which radiation-`Q` estimator is the substrate's?) | **DISSOLVED BY THE SAME MOVE.** Both estimators in dispute (`Q_Z` and Chu/Collin–Rothschild) are **spin-1** approximations to a pole-`Q`; this lane computes the spin-2 pole-`Q` itself, so neither estimator is used and the `50%` spread does not enter. The disagreement recorded in #814 §1.3 is **neither adopted nor resolved** — it is bypassed, and that is stated rather than presented as an adjudication. |
| **FORK-12** (is killing the `Q ∝ ℓ` scaling a win or a falsifier?) | **NOT ADJUDICATED — Grant has not answered it.** The `ℓ`-ladder is computed for `ℓ ∈ {2,3,4,5}` and reported with the frozen tag `DIAGNOSTIC — no bin, no verdict; FORK-12 is unanswered and this lane does not adjudicate it`. Answering it after seeing the ladder is the post-hoc move Rule 11 forbids. |

**#808 Q8 (is the cold anchor in scope?)** — Grant's `"6, GO"` authorizes this derivation, whose entire object **is** the cold anchor. The lane therefore proceeds on the reading that the cold anchor is in scope **for measurement**; it remains out of scope for *repair* — a result that disagrees with `Q = ℓ` is **routed to Grant as a flag**, not applied as a fix. Frozen: `a derived cold Q that disagrees with the B1-ratified Q = ell anchor is routed to Grant as a flag; no solidity, ruling or leaf is changed by this lane`.

---

## §11 — LEDGER TAGS + OWED FOLLOW-ONS (fenced; NOT executed here)

**Ledger tags (`consistency-vs-emergence`, frozen).** `omega_R*M_g` is `[derived]` but **VALUE-CONSISTENCY** class (rides the GR-imported `7`). `Q`, `r_peak/r_sat` and the overtone ratios are `[derived]` and `ν_vac`-**FREE**, hence **emergence-capable at value level** — subject to G8 measuring the cancellation. The GR numbers are `[GR-IMPORTED comparators]` (I11–I13), one of which (I13) has **no in-repo carrier** and is disclosed as external. `ν_vac = 2/7` is `[canon]`, read-only, value GR-imported. Gate residuals and conditioning numbers are `[engineering]`. **`α`-CLEAN. No manifestation-class claim. No claim of any kind is minted.**

**Owed follow-ons (fenced; Rule 12 — the slot is NOT refilled with an assertion):**
1. **The spheroidal (even-parity / P–SV-coupled) branch.** This lane builds the toroidal branch only. #814's CF-15/FORK-5 disposal question lives in the spheroidal branch and is **not** answered here. A stage-2 build with its own prereg.
2. **FORK-3's naming gap** — canon must say which `ρ` enters `Z_shear = ρ c_shear` at `vol3/claim-quality.md:122`. Surfaced, routed to the auditor lane.
3. **FORK-9's formal half** — whether Op6's phase-matching condition, written for the atomic cavity, applies to a graded shear cavity with a `Γ = −1` inner wall. BIN-4 measures the ladder; it does not derive the condition.
4. **FORK-12** — the win-or-falsifier question must be answered by Grant **before** any `ℓ`-ladder verdict is banked.
5. **The two #814 candidate `translation-circuit.md` rows** stay unlanded; landing is the auditor lane's move and only if this derivation validates them.

---

> **Pre-registration provenance.** Frozen pre-registration for the cold-Q pole derivation authorized by Grant on 2026-08-02, verbatim `[sic]`: `"6, GO"`, after the framing-challenge walk merged as PR #814. Written against `origin/main` = `ac165cf2`. This is COMMIT 1 — the prereg **ALONE**, frozen and pushed before any driver code. Companion inputs cited by path (cite-don't-duplicate): `research/2026-07-30_qlaw-derivation_scoping.md` §1.5/§2.0/§2.1/§2.3/§3/§4; `research/2026-07-31_qlaw-framing-challenge_walk.md` §0/§1.1/§1.4/§1.5/§1.7/§2.2/§2.4/§3/§4; `research/2026-07-28_continuum-radial-solver-stage1_prereg-FROZEN.md` §5/§6/§8/§9 (the battery architecture, re-earned not inherited); `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51` (the frozen `a_*=0` comparator); `research/2026-07-20_ringdown-systematics_checks.py:68-73` (the in-repo overtone real parts). Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched regardless of outcome. Companion: the docket fragment `_orchestration/docket-entries/2026-08-02-coldq-pole.md`.
