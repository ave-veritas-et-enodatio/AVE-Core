# The cold-Q pole derivation **v2.1** — FROZEN pre-registration (compactified-spectral instrument; same four bins; corner-, edge- and conditioning-certified)

**Date:** 2026-08-03
**Class:** DERIVATION pre-registration (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger — regardless of outcome**). Committed **ALONE** and pushed **before any driver code and before any number exists**.
**Result-doc pointer requirement.** The result doc that resolves these bins MUST carry `Prereg-file: research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file (`manuscript/ave-kb/tools/verify-frozen-provenance.py`).
**Provenance:** Grant's GO on the cold-Q successor, 2026-08-03, verbatim `[sic]`: `"Go on cold-Q"`.
**Written against** `origin/main` = `583d43dd`.

## ★ SUPERSESSION NOTE (2026-08-03) — what this document supersedes, and why

This document **supersedes `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` (commit `00724432`, pushed 2026-08-03)**, which remains **byte-untouched as the record**. This is **pre-measurement prereg repair via versioned supersede**: the v2 prereg was frozen and pushed, a review of it identified gate-coverage holes, and **no driver code was written and no number was produced under v2** — so nothing is being retuned in light of a result. Rule 11 governs post-result retuning; there is no result. The v2 file is not edited, not relaxed, and not deleted; it is superseded by a new version number with its own verification chain, exactly as #845 was superseded by v2.

**This document is SELF-CONTAINED.** It restates the full lane rather than incorporating v2 by reference, so the frozen document stands alone.

**The four defects in v2 that forced the supersede — all of them coverage holes, none of them a relaxation:**

1. **No left-edge bound and no conditioning certification.** v2 identified — but did not bound or gate — its **own** low-`Ω` mechanism: at the outflow point the relation is `4iΩ·ψ_η + [2Ω²(1+4λ) − 4ℓ(ℓ+1)]·ψ = 0`, so as `Ω → 0` the `ψ_η` coefficient weakens and that row's information content degrades. v2 froze a rectangle whose left edge was inherited from v1 with **no justification from v2's own mechanism**. **v2.1 derives the bound (§4.6) and freezes a conditioning-monitor gate (C10).**
2. **No graded-representation accuracy certification at the rectangle's corners and edges.** v2's C1 certified the **zero-grade** operator; C4 certified **consistency** over the rectangle. Neither is an accuracy certification of the **graded** representation at the corners. **v2.1 adds C9.**
3. **Control-box coverage stopped short of the physics rectangle's high-`|Ω|` corner.** v2's control box reached `|Ω| ≈ 7.2`; the frozen physics rectangle reaches `|Ω| = 15.65`. **v2.1 extends the closed-form control ladder to `ℓ = 18` (reach `|Ω| = 17.67`), which covers it with an EXACT reference (§5, C1).**
4. **No count-vs-box-WIDTH scaling sub-gate at fixed content.** v2's FT-D tested three different boxes with three different expected counts, which is not the same test. **v2.1 folds a nested width family into C4 and FT-D.**

**Two carry-over corrections are made AT SOURCE in this document (they are NOT repeated from v2):** the characterisation of #845's FT-5 artifact (§2.4) and the attribution of the `x_sat`-generalized advance identity (§2.5).

> **FREEZE STATEMENT.** This document freezes: (i) the sector/regime/phase-state/coordinate header and the substrate-native walk (§0); (ii) the scope carve (§1); (iii) the inherited ratified physics plus the compactified formulation this lane discretizes, **independently verified as operator algebra** (§2); (iv) the complete import ledger (§3); (v) **THE METHOD, chosen and stated before any number exists, with its candidate evaluation, its engineering-choice tag, and the DERIVED resolution and conditioning bounds** (§4); (vi) the ELEVEN certification gates C1–C11 with FROZEN NUMERIC TOLERANCES (§5); (vii) the TEN gate-fireability self-tests FT-A…FT-J, each of which MUST FIRE (§6); (viii) the physics OUTCOME BINS, exhaustive and reachable, with the same precedence and the same boundary numbers as v1 and v2 (§7); (ix) what transfers from #845 and from v2 and what must be re-earned (§8); (x) the mutual-satisfiability check run BEFORE the freeze and its full disclosure (§9); (xi) the flags raised AT FREEZE TIME (§10); (xii) ledger tags + owed follow-ons (§11). **The verdict may cite ONLY the frozen criteria's outputs, read from the shipped `coldq_pole_v2_results.json` via the deterministic driver — NO prose-string conclusions (the #770 lesson).**

---

## §0 — SECTOR / REGIME / PHASE-STATE / COORDS header, declared BEFORE any physics word

**Restated fresh for this lane. The framing is RATIFIED and is not re-litigated here** (it is v1's §0, re-walked rather than copied-by-reference, because a successor that inherits a header without re-walking it inherits the header's blind spots too).

- **MODE.** Cold (`a_* = 0`, Schwarzschild-limit) post-merger remnant ringing down. The object is the fundamental `ℓ = 2` quasinormal resonance of the saturation cavity, and its radial overtone ladder.
- **SECTOR.** The **observable** is a **transverse shear (T2)** oscillation. The **bias field** that builds the cavity is the **A1 radial dilatation** `ε_11 = 7GM/(c²r)`. Orthogonal grades, **not cross-wired**: the A1 strain is the DC operating point that sets the constitutive profile; the T2 shear mode is the small-signal AC riding on it. Receipt for `ε_11` **being** the Axiom-4 amplitude `A`: [`common/vocabulary-register.md:309`](../manuscript/ave-kb/common/vocabulary-register.md), verbatim *"the A1-dilatation **radial "strain"** that IS the Axiom-4 saturation **amplitude $A$**"*.
- **REGIME.** Far field (`r ≫ r_sat`) = **Regime I** — linear, lossless, reactive; a legal radiating port. The graded exterior `r > r_sat` = Regime I with a spatially varying modulus (Op14 grade). The wall `r = r_sat` = the **Regime III→IV** soft-mode terminus, `G_shear → 0`. The interior `r < r_sat` = **Regime IV**, where shear cannot propagate at all and which is therefore **not part of the computational domain** — the domain is `[r_sat, ∞)`, and that is a physics statement, not a truncation.
- **PHASE-STATE.** Op14 ON throughout the graded exterior as a **static constitutive grade** (the DC bias is time-independent; the ringdown is the small-signal response). `A = 1` exactly at `r_sat = 7GM/c²`; `Γ_shear = −1` there.
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the **dimensionless-eigenvalue register** (`ω_R M_g`, `ω_I M_g`, `Q`) that AVE and GR share — no phase-space/real-space mismatch. This lane solves for the **complex pole** directly, so what it returns *is* the pole-`Q` that the GR comparator is; **no port→pole transfer is performed, needed, or assumed.**
- **The eigenfunction's own coordinate.** The radial localization observable (BIN-3) is read in **real-space radius normalized to `r_sat`** and compared only against real-space radii. It is **not** compared against `r_eff = 49M_g/9`, which is a **spectral marker (a cutoff radius), not a place**.

### Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code)

1. **K4 / srs connectivity.** This is a **CONTINUUM** instrument. Frozen disclosure: `the radial channel is a CONTINUUM representation of the shear constitutive law; it is not a discretization of the srs stencil and carries no K4 connectivity claim`. What it consumes from the lattice is the **constitutive law only**: the Ax-4 kernel and the Op16 shear-speed projection.
2. **Cosserat / channel basis.** The mode solved for is the **toroidal (odd-parity / axial) branch**, whose displacement field is **exactly divergence-free**, so the Lamé `λ` (bulk/A1) modulus drops out of the equations of motion **identically** rather than by assumption. Frozen: `the toroidal (odd-parity) branch is exactly divergence-free, so the bulk modulus drops out identically and there is no linear P-SV conversion partner; the single-channel classification is structural in this branch`.
3. **Op14 saturation.** Enters as the **static constitutive grade** `S(A) = sqrt(1 - A²)` with `A(r) = r_sat/r`, projected into shear by Op16. Frozen: `Op14 enters as a static constitutive grade S(A); the A -> 1 terminus is handled by an exact change of variable, not by a numerical cutoff or a regularized floor`.
4. **★ The substrate-native reading of the compactification, and it is not decoration.** This lane's compactified radial coordinate is `A = r_sat/r` — **the Axiom-4 saturation amplitude itself**. The computational domain is `A ∈ (0, 1]`: `A = 1` IS the wall, `A = 0` IS infinity. The instrument therefore does not *impose* a coordinate on the medium; it **adopts the medium's own order parameter as the coordinate.** Frozen: `the compactified radial coordinate is the Axiom-4 saturation amplitude A = r_sat/r itself, so A = 1 is the wall and A = 0 is infinity; the instrument adopts the medium's own order parameter as its coordinate rather than imposing a lattice-Cartesian one`.
5. **Phase-space vs real-space (A46).** Every verdict-class observable is a **dimensionless ratio**: `ω M_g`, `Q`, `r_peak/r_sat`, and the overtone ratios. **α-CLEAN** — `α` appears nowhere in the chain.
6. **Checkpoint: boundary-not-bulk.** The resonator is a **boundary/graded-shell** object, not a bulk-force object — consistent with the #403/#404 localization ruling. The loss is a **radiative port at infinity** (Ax-3-licensed), and there is **no** `Re{Z}` anywhere in the medium. C7 tests exactly that.
7. **Checkpoint: what the substrate does NOT supply.** The angular index `ℓ = 2` is **not** derived here; it is the quadrupole selection the corpus carries for the GW channel. Stated so it is not mistaken for an output.

### Pre-test physics check (`pre-test-physics-check`, Rule 16 — ONE plumber question surfaced to Grant BEFORE the design locks)

> **Grant — plumber-physically, and this is a DIFFERENT question from v1's.** v1 asked *where* the mode sits (rim vs ramp) and handed it to the substrate. That question is still live and BIN-3 still measures it. The question **this** design cannot answer for itself is about the far end of the pipe. v1 tried to read the standing-wave ratio at a finite distance down the line and back out the reflected wave — and that failed exactly the way it fails on a real bench when the line is lossy and you probe too far out: the incident term swamps the reflected one and you are measuring your own noise floor. **v2 does not probe at a finite distance at all. It changes variables so that "infinitely far down the line" is a single point on the grid, and the outgoing-wave behaviour is divided out ANALYTICALLY before any number is computed.** The physical content of that move: the line's far end is treated as a *matched termination that has already been solved in closed form*, and the solver only ever handles the slowly-varying envelope riding on it. **What I need from you if you disagree:** this presumes that the only thing at the far end is the cold Regime-I lattice acting as a clean radiating port with `Z → Z_0` — no far-field structure, no second reflection, no cosmological horizon term. If the substrate has *anything* out there that reflects, the analytic factor I divide out is the wrong one and every number in this lane is wrong in the same direction. **This lane does not test that assumption; it inherits it from the frozen canonical input set (I7), and it says so.**

### Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE results — and it is not uniform across the bins

Written in units of `r_sat`, the problem has **no free parameter at all**: the profile is `A = r_sat/r`; the kernel is `S = sqrt(1 - A²)`; the speed is `c_shear = c₀·sqrt(S)`; the inertia is the cold `ρ₀`. Therefore `Ω ≡ ω·r_sat/c₀` is a **pure number** fixed by the profile SHAPE, the Ax-4 kernel, and `ℓ`.

| output | rides `r_sat`'s coefficient `7`? | class |
|---|---|---|
| `ω_R M_g` (BIN-1) | **YES** — `ω_R M_g = Re(Ω)/x_sat` with `x_sat = 7` | **VALUE-CONSISTENCY.** The `7` is the `1/7` trace-reversed bulk projection, which takes `ν_vac = 2/7` as **input** ([`one-seventh-impedance-projection.md:18`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md): *"the $1/7$ boundary is a projection of a GR-imported ratio, not a first-principles lattice output"*). **May NOT be headlined as value-level emergence.** |
| **`Q = ω_R/(2\|ω_I\|)` (BIN-2)** | **NO — it cancels exactly** | **`ν_vac`-FREE, therefore EMERGENCE-CAPABLE at value level.** `Q = Re(Ω)/(2\|Im(Ω)\|)`; the `x_sat` conversion divides out identically. |
| `r_peak/r_sat` (BIN-3) | **NO** | `ν_vac`-free ratio; **FORM-class** statement about where the mode lives. |
| overtone ratios (BIN-4) | **NO** | `ν_vac`-free ratios. |

Frozen tag: `Q, the localization ratio and the overtone ratios are exactly nu_vac-free (the r_sat scale divides out identically); omega_R*M_g is NOT and is VALUE-CONSISTENCY class because the 7 in r_sat = 7GM/c^2 is the 1/7 projection of the GR-imported nu_vac = 2/7`.

> **★ AN HONESTY UPGRADE OVER v1, STATED BEFORE THE RUN.** In v1 the `ν_vac`-cancellation gate (its G8) was a *numerical* test of a *structural* fact, and it failed at `1e-9` while confirming the fact to eight significant figures. **In v2's formulation the cancellation is EXACT BY CONSTRUCTION and cannot be otherwise:** the compactified coordinate is `A = r_sat/r` and the eigenvalue variable is `Ω = ω r_sat`, so `r_sat` appears nowhere else in the discretized operator. A gate that cannot fail is not a gate. C5 is therefore frozen as a check on the **implementation's arithmetic fidelity** to a structural identity — the driver builds the coefficient functions through an arithmetic path that carries `r_sat` explicitly, so different `x_sat` produce different floating-point intermediates — and its **fireability is demonstrated by FT-E**, which injects an `x_sat`-dependent profile perturbation and requires the gate to fire. **The structural exactness is disclosed here, in advance, rather than presented afterwards as a result.**

---

## §1 — WHAT THIS LANE COMPUTES, AND WHAT IT EXPLICITLY DOES NOT

**COMPUTES.** The complex quasinormal eigenvalues `ω M_g` of the `ℓ = 2` **toroidal shear** mode of the canonical graded saturation profile, with a traction-free (`Z_shear → 0`, `Γ_shear = −1`) inner terminus at `r_sat` and an outgoing-radiation condition at infinity; and from them `ω_R M_g`, `Q = ω_R/(2|ω_I|)`, the eigenfunction's radial localization, and the overtone ladder.

**DOES NOT:**
- **X1 — does NOT derive `ℓ = 2`.** The quadrupole selection is an input.
- **X2 — does NOT derive `ν_vac`, `K = 2G`, or the `7` in `r_sat`.** Their value provenance is GR-IMPORT, closed by PR #261/#506 and untouched here.
- **X3 — does NOT touch the spin (`a_* > 0`) mapping.** This is the `a_* = 0` anchor only.
- **X4 — does NOT compute a port-`Q`, a radiation resistance, or a Chu/Collin–Rothschild stored-energy `Q`.**
- **X5 — does NOT adjudicate #814 FORK-12** (is killing the `Q ∝ ℓ` scaling a win or a falsifier?). Grant has not answered it. The `ℓ`-ladder **is** computed and **is** reported, explicitly as `DIAGNOSTIC — no bin, no verdict; FORK-12 is unanswered and this lane does not adjudicate it`.
- **X6 — does NOT run FORK-3(b)** (`ρ_eff = ρ₀/S³` as the shear-wave inertia).
- **X7 — does NOT import, confirm, refute, or re-adjudicate any #845 number.** #845 is `NOT-ADJUDICATED prior-lane data`.
- **X8 — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry**, whatever the outcome.

---

---

## §2 — THE PHYSICS (inherited, ratified, NOT re-derived) AND THE COMPACTIFIED FORM THIS LANE DISCRETIZES

### §2.1 Inherited unchanged from the ratified v1 framing — stated, not re-derived

The BH ringdown as a **transmission line**: series `L = ρ`, shunt `C = 1/G(A)`; the DC strain profile `A(r) = 7GM/c²r` grades it; the wall is `Z_shear → 0`, a **SHORT** at `r_sat`; the exterior is the graded taper; and `Q` is read as **the pole of the spin-2-weighted input impedance**, not from a port formula. **Zero free inputs.** The **spin-2 weighting is kept** — v1 measured it load-bearing (its FT-6: the spin-1 `ℓ(ℓ+1)` substitution broke its energy gate by `0.21729`). The **advance identity** is restated in §2.5.

The shear channel is a linear, lossless-reactive elastic continuum with a radially graded shear modulus and the cold inertia:

- `ρ(r) = ρ₀` — the cold lattice inertia;
- `G_shear(r) = ρ₀ c_shear(r)²` with `c_shear = c₀·sqrt(S)` — **Op16, CANONICAL** ([`common/operators.md:56`](../manuscript/ave-kb/common/operators.md), row `Op16 | Universal Wave Speed | $c_{shear} = c_0\cdot\sqrt{S}$`), reinforced verbatim at [`saturating-modulus-and-backreaction.md:60`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md): *"**SHEAR softens:** $c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection,"*
- `S(A) = (1 - A²)^{1/2}` and `A = ε_11/ε_yield` with `ε_yield = 1` — **Ax 4**, verbatim from the same leaf at `:51`–`:52`: *"\qquad A=\varepsilon_{11}/\varepsilon_{\text{yield}}\ (\varepsilon_{\text{yield}}=1),"* and *"\qquad D(A)=\frac{1}{S(A)},\qquad S(A)=(1-A^2)^{1/2}."*
- `ε_11 = 7GM/(c²r)` — [`temporal-spatial-lattice-decomposition.md:14`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md), verbatim *"The principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ compresses the lattice asymmetrically."*
- the SHORT — [`vol3/claim-quality.md:123`](../manuscript/ave-kb/vol3/claim-quality.md), verbatim *"a solid$\to$liquid free surface ($G_{shear} \to 0$) is exactly a $Z_{shear} \to 0$ short"*; and `r_sat` at `:121`, verbatim *"the **shear/bulk** rupture boundary is deeper, at $r_{sat} = 7GM/c^2 = 3.5\,r_s$ where the radial strain $\varepsilon_{11} = 1$"*.

The **toroidal (odd-parity)** radial system, inherited unchanged, in the displacement scalar `W(r)` and its conjugate traction `T(r) ≡ μ(r)·(W′ − W/r)` with `μ ≡ G_shear`:

```
(1/r³)·d/dr[ r³ μ (W′ − W/r) ] + [ ρω² − (ℓ−1)(ℓ+2)·μ/r² ]·W = 0
```

equivalently, after expansion and division by `μ` (with `g ≡ μ′/μ`, and using `2 + (ℓ−1)(ℓ+2) = ℓ(ℓ+1)`):

```
W″ + (2/r + g)·W′ + [ ω²ρ/μ − ℓ(ℓ+1)/r² − g/r ]·W = 0
```

with the spin-2 stored-energy weighting `(ℓ−1)(ℓ+2)` (NOT the spin-1 `ℓ(ℓ+1)`):

```
E_strain(r) ∝ μ(r)·[ |W′ − W/r|² + (ℓ−1)(ℓ+2)·|W|²/r² ]·r²
E_kin(r)    ∝ ρ(r)·|ω|²·|W|²·r²
```

Frozen: `the radial system is the toroidal (odd-parity, exactly divergence-free) branch of the shear-channel continuum equations; the impedance relation T = mu(W' - W/r) and the (l-1)(l+2) stored-energy weighting are the spin-2 ones and no spin-1 vector-multipole impedance is imported anywhere in this lane`.

### §2.2 The compactified, outgoing-factored form (DERIVED HERE — this is what v2 actually discretizes)

Set `c₀ = ρ₀ = G₀ = 1`. Adopt the **Axiom-4 amplitude as the radial coordinate**, `A ≡ r_sat/r ∈ (0, 1]`, so `μ = S = sqrt(1 − A²)`, `A = 1` is the wall and `A = 0` is infinity. Define the scale-free eigenvalue `Ω ≡ ω·r_sat/c₀`.

**Step 1 — factor out the outgoing wave ANALYTICALLY.** Write

```
W = A · exp( i Ω (1/A + λ A) ) · ψ(A)
```

with `λ` a frozen **hyperboloidal gauge parameter** (§4.4). The factor `A·exp(iΩ/A)` is exactly the `e^{iωr}/r` outgoing spherical behaviour; `exp(iΩλA)` is entire and changes nothing physical. **Every exponentially large or small quantity in the problem lives in this closed-form prefactor and is never represented numerically.** At `λ = 0` the equation for `ψ` is

```
A² ψ_AA + [ −2iΩ + 2A + A²ĝ ] ψ_A + [ Ω²/(S(1+S)) − iΩĝ − ℓ(ℓ+1) + 2Aĝ ] ψ = 0 ,   ĝ ≡ (dμ/dA)/μ = −A/(1−A²)
```

(the `ω²ρ/μ` term is written as `Ω²/(S(1+S))` after the exact identity `(1/S − 1)/A² = 1/(S(1+S))`, which removes the apparent `0/0` at `A = 0` **in closed form rather than numerically**). The general `λ` form is obtained by `ψ_{λ=0} = e^{iΩλA}ψ_λ`.

**Step 2 — the outgoing condition is built into the equation, not imposed.** At `A = 0` the coefficient of `ψ_AA` vanishes to **second order** while the coefficient of `ψ_A` is `−2iΩ ≠ 0`. The point is an **outflow boundary**: collocating the equation there supplies the relation `−2iΩ ψ_A(0) − ℓ(ℓ+1) ψ(0) + (grade terms) = 0` **automatically**, and the ingoing solution — which behaves as `e^{−2iΩ/A}`, an essential singularity — is **not in the analytic function space at all**. Frozen: `no radiation boundary condition is imposed at infinity; the outgoing branch is the analytic branch of the compactified equation and the ingoing branch carries an essential singularity that is not in the discretization's function space, so no far-field matching, no asymptotic series and no subdominant-coefficient extraction occurs anywhere in this lane`.

**Step 3 — the wall terminus, exactly.** Near `A = 1` the modulus vanishes as `μ ∝ (r−r_sat)^{1/2}` and the indicial exponents are `s = 0` (traction-free) and `s = 1/2`. Substitute

```
A = 1 − η² ,   η ∈ [0, 1]   (η = 0 is the wall, η = 1 is infinity)
```

Under this exact substitution the two branches become `η⁰` and `η¹`, the `1/η³` terms cancel **identically** against the modulus-gradient term, and `η = 0` becomes an **ordinary regular point** of the transformed equation. Writing the transformed equation as `𝒜(η)ψ_ηη + ℬ(η,Ω)ψ_η + 𝒞(η,Ω)ψ = 0` with `𝒜 = (1−η²)²`, the traction is `T ∝ μ(W_A − …)` and evaluates at the wall to `T(0) ∝ ψ_η(0)`, so

```
the traction-free (Z_shear → 0, Γ_shear = −1) condition is EXACTLY   dψ/dη |_{η=0} = 0
```

Frozen: `the wall is reached exactly via the A = 1 - eta^2 substitution, which makes eta = 0 an ordinary regular point of the transformed equation; the canonical traction-free SHORT is exactly the single linear condition dpsi/deta = 0 at eta = 0, with no offset, no series start, no regularized modulus floor and no shooting`.

### §2.3 What is NOT the same as the spin-1 problem

The **impedance relation** is `T = μ(W′ − W/r)` — *not* `Z_ℓ ∝ h_ℓ′/h_ℓ`. The extra `−W/r` term is the tensor-rank content and it is what makes the wall condition genuinely different from the spin-1 one; likewise the stored-energy weighting carries `(ℓ−1)(ℓ+2)`, not `ℓ(ℓ+1)`. Both are gated (C6) and both are shown load-bearing by mutation (FT-F).

### §2.4 The zero-grade closed-form control (the entry ticket's reference) — CORRECTED CHARACTERISATION

With `μ ≡ G₀` (zero grade) but the **same** traction-free wall at `r_sat` and the **same** outgoing condition, the `ψ`-equation collapses to

```
A² ψ_AA + (2A − 2iΩ) ψ_A − ℓ(ℓ+1) ψ = 0 ,   wall condition  (iΩ − 2)ψ(1) − ψ_A(1) = 0
```

whose solutions are **exactly polynomials of degree `ℓ`** — so a spectral discretization of order `n ≥ ℓ+1` represents them **without error**. Equivalently, with `u(x) ≡ x^{ℓ+1} h_ℓ^{(1)}(x) e^{−ix}` (a polynomial of degree `ℓ`, `x ≡ Ω`), the wall condition is the polynomial

```
i x u + x u′ − (ℓ+2) u = 0        of degree exactly ℓ+1, hence exactly ℓ+1 roots
```

**This is the object #845's FT-5 failed on**, returning a winding of `15.000` for `ℓ = 1, 2, 3` alike where the closed-form counts are `1`, `1`, `2`.

> **★ CORRECTED CHARACTERISATION OF THAT ARTIFACT — this replaces the "optical length" reading, at source.** The v2 prereg (and #845's own result doc) described the `15.000` as **the optical length `2R_match − a`**, i.e. as a *fixed signature*. **That reading is superseded.** The concurrent #845 audit refines it to a **PHASE-RATE artifact**: on the noise-dominated stretch of the contour the objective's phase advances at a rate `d(arg N)/dω_R ≈ 2R_match − a`, so the winding is approximately `rate · Δω_R / 2π` — i.e. it is a **BOX-WIDTH COINCIDENCE, not a constant.** The distinction is load-bearing for gate design: a fixed signature could be tested for by looking for the number `15`, whereas a phase-rate artifact scales with the box and can only be excluded by a **count-vs-box-width scaling test at fixed content**, which is why v2.1 folds that family into C4 and FT-D. Frozen: `the #845 FT-5 artifact is a PHASE-RATE artifact whose winding scales as rate times box width over 2 pi and is NOT a fixed optical-length signature; no gate in this lane tests for the number 15 or for any inherited constant, and the artifact class is excluded instead by a count-versus-box-width scaling family at closed-form-known content`. **Disclosure: this lane CITES the audit's refinement; it did not re-derive it, and NO v2.1 gate depends on it being correct.**

**Control ladder coverage (DERIVED, §4.6).** The closed-form ladder is available at every `ℓ`, and its `|Ω|` reach grows with `ℓ`. The frozen control set is `ℓ ∈ {1, 2, 3, 6, 10, 14, 18}`, whose reach **covers the frozen physics rectangle's `|Ω|` span with an exact reference at both ends** — closing v2's defect 3.

### §2.5 The advance identity (restated, frozen) — CORRECTED ATTRIBUTION

```
k₀ r_sat = x_sat · ω_R M_g
```

Frozen: `k_0*r_sat = x_sat * omega_R M_g identically, so the 9/7-above-cutoff test IS the omega_R versus 18/49 comparison re-expressed and is NOT an independent axis`. It is restated **before any number exists**, exactly so that a `k₀r_sat` result and an `ω_R` result cannot afterwards be presented as two corroborating findings. They are one.

> **★ CORRECTED ATTRIBUTION, made at source.** The `x_sat`-generalized form above is **THIS LANE'S OWN frozen criterion**, minted here. It is **NOT** inherited from #845. What #845 froze is the **literal-7 specialisation**, at `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md:284`, verbatim: *"k₀ r_sat = ℓ(1+ν_vac) = 18/7 = 2.5714`, and `k₀ r_sat = 7·ω_R M_g` identically"*. **Byte-verification receipt: a grep of the #845 prereg for the `x_sat`-generalized form returns `0` matches.** The v2 prereg listed the generalized identity under its §8 "TRANSFERS … from #845", which was imprecise; **that imprecision is corrected here rather than carried forward.** The generalisation matters because C5 varies `x_sat ∈ {5, 7, 11}`, where the literal `7` would be false.

### §2.6 ★ INDEPENDENT VERIFICATION OF THE η-FORM COEFFICIENTS (new in v2.1; leak-free)

The load-bearing algebra of this lane is the transformation of the `A`-form equation into the `η`-form actually discretized. That transformation is verified **as an operator identity**, on arbitrary analytic test functions, without solving anything:

```
𝓛_η[ψ](η)  ≡  𝒜(η)ψ_ηη + ℬ(η,Ω)ψ_η + 𝒞(η,Ω)ψ      must equal      4η² · 𝓛_A[ψ](A) ,   A = 1 − η²
```

for **every** `ψ`, hence in particular for test functions that are no solution of anything. This is a pure-algebra check: **it produces no eigenvalue, no solution and no physics observable**, and it is therefore run before the freeze (§9 item 1). It is promoted to a **mandatory gate, C11.** Frozen: `the eta-form coefficients are verified as an OPERATOR IDENTITY against the A-form composed with the chain rule, evaluated on arbitrary analytic test functions that solve nothing, so the verification produces no eigenvalue and no physics observable`.

---

## §3 — IMPORT LEDGER (every number the solver consumes, tagged; `substrate-first-for-numbers`)

| # | Input | Value / form | Class | Source |
|---|---|---|---|---|
| **I1** | Saturation-wall radius | `r_sat = 7GM/c² = 7 M_g`, i.e. `x_sat = 7` | **`[canon]`** — form-derived, **VALUE rides the GR-imported `ν_vac`** | `vol3/claim-quality.md:121`; `temporal-spatial-lattice-decomposition.md:14`; provenance at `one-seventh-impedance-projection.md:18` |
| **I2** | Saturation amplitude profile | `A(r) = ε_11/ε_yield = r_sat/r`, `ε_yield = 1` | **`[canon]`** | `saturating-modulus-and-backreaction.md:51`; `vocabulary-register.md:309` |
| **I3** | Ax-4 kernel | `S(A) = (1 − A²)^{1/2}` | **`[canon]` — Axiom 4** | `saturating-modulus-and-backreaction.md:52` |
| **I4** | Shear-speed projection | `c_shear = c₀·S^{1/2}` (Op16) | **`[canon]`** | `common/operators.md:56`; `saturating-modulus-and-backreaction.md:60` |
| **I5** | Shear-wave inertia | `ρ(r) = ρ₀` (cold lattice inertia) | **`[canon, FORK-3 leading reading]`** — the naming gap at `vol3/claim-quality.md:122` is #814 CF-7, **routed not repaired** | `vol3/claim-quality.md:122`, `:124` |
| **I6** | Inner boundary condition | traction-free, `T(r_sat) = 0` (`Z_shear → 0`, `Γ_shear = −1`) | **`[canon]`** | `vol3/claim-quality.md:123` |
| **I7** | Outer boundary condition | outgoing radiation into the cold matched lattice; **no far-field structure, no second reflection** | **`[canon]` — Regime-I radiative port, Ax-3-licensed. ASSUMED, NOT TESTED — see the §0 plumber question** | §0 REGIME header |
| **I8** | Angular index | `ℓ = 2` (quadrupole) | **`[canon, INPUT not derived]`** | §1 X1 |
| **I9** | Unit choice | `M_g = 1`, `c₀ = 1`, `ρ₀ = 1`, hence `G₀ = 1` | **`[dimensionless by construction]`** | this lane |
| **I10** | `ν_vac = 2/7` | imported **read-only** from `ave.core.constants.N_NU`; used ONLY to form the `r_eff = r_sat/(1+ν_vac)` comparator and the `r★` turning-point comparator | **`[canon]` — VALUE GR-IMPORTED (PR #261/#506)** | `src/ave/core/constants.py:397` |
| **I11** | GR cold comparator | `ω_R M = 0.37367`, `ω_I M = 0.08896` at `a_* = 0`, read **programmatically** from the frozen `KERR_QNM` dict | **`[GR-IMPORTED comparator — the frozen C-comparator, inherited unchanged from v1]`** | `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51` |
| **I12** | GR overtone real parts | `ω_R M (ℓ=2, n=1) = 0.346711`, `(ℓ=2, n=2) = 0.301053`, read **programmatically** from the in-repo `SCHW_OMEGA_R` dict | **`[GR-IMPORTED comparator]`** | `research/2026-07-20_ringdown-systematics_checks.py:72-73` |
| **I13** | GR overtone imaginary part | `ω_I M (ℓ=2, n=1) = 0.273915` | **`[GR-IMPORTED comparator — EXTERNAL, no in-repo carrier]`** — Berti–Cardoso–Will Schwarzschild `s=2` living-review table; **disclosed, not hidden** | external |
| **I14** | Standing AVE shortcut | `ω_R M_g = 18/49`, `Q = ℓ = 2`, `r_eff = 49M_g/9`, `r★/r_sat = 1.2247` | **`[corpus comparators — the objects under test]`** | `vol3/claim-quality.md:198`; `vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md`; #814 CF-9 |
| **I15** | Solver numerics | Chebyshev order `n`, gauge `λ`, contour sampling, mp precision `dps`, seed grid, dedupe radius | **`[ENGINEERING CHOICE — tagged, frozen in §4/§5]`** | this lane |

**R8 audit rule (frozen).** `every number the solver consumes appears on this ledger with its tag; no SM/GR convention default enters anywhere, and in particular no spin-1 vector-multipole impedance, no Chu/Collin-Rothschild stored-energy weighting, and no Regge-Wheeler or Zerilli potential is used as an input`.

---

---

## §4 — THE METHOD, chosen and stated BEFORE any number exists

### §4.1 The requirement the successor must meet

#845's diagnosis names the disease precisely: **on the real radial axis, with `Im ω < 0`, the outgoing solution is the DOMINANT one, so the quasinormal condition asks for a SUBDOMINANT coefficient to vanish, and a relative integration error `δ` manufactures a spurious ingoing amplitude of order `δ·exp(2|Im ω| R_match)`.** Compounding it, the far-field expansion in `1/r` is **asymptotic, not convergent**, so "more terms is better" is false. **Any successor that still evaluates a solution at a finite real radius and extracts a subdominant coefficient there inherits both diseases regardless of how carefully it is gated.** The requirement is therefore structural: *no exponentially large or small quantity may be represented numerically anywhere in the chain.*

### §4.2 Candidate evaluation (three candidates, evaluated before choosing)

| candidate | how it would cure the disease | why it is / is not chosen as PRIMARY |
|---|---|---|
| **(a) Exterior complex rotation / complex scaling** — integrate along `r = r_sat + e^{iθ}s` so the outgoing solution decays along the rotated ray, with two-sided shooting and a Wronskian condition | Inverts the dominance: each leg integrates its own dominant solution and the seed error at the far end is damped as `exp(−2|p|Δs)` instead of amplified | **NOT chosen.** It cures the conditioning but keeps two structural liabilities: (1) the rotated ray is only valid in the wedge `\|ω_I\|/ω_R < tan θ`, so the frozen search rectangle's low-`ω_R` corner (`ω_R M_g = 0.02`, `\|ω_I\| M_g = 1.00`, ratio `50`) would demand `θ > 88.9°` and **the argument-principle contour would have to traverse a region where the method is invalid** — the exact structural defect that made #845's winding untrustworthy, merely relocated; (2) it still needs an approximate seed at a finite `s_max`. **Retained as the frozen cross-check family, not as primary** |
| **(b) ★ Compactified (hyperboloidal) spectral discretization with the outgoing condition built into the basis** | The outgoing wave is divided out **in closed form** before discretization; infinity becomes **one grid point**; the ingoing branch carries an essential singularity `e^{−2iΩ/A}` and is **not in the polynomial function space at all**. There is no matching radius, no series truncation, no subdominant extraction, and **no exponentially large or small number is ever formed** | **CHOSEN AS PRIMARY.** It removes the disease by construction rather than by conditioning improvement, it is uniformly valid over the whole frozen rectangle (no wedge), and it makes the zero-grade control **exactly representable** (the control solution is a polynomial of degree `ℓ`), which turns #845's fatal self-test into a gate with essentially unlimited headroom |
| **(c) Integral-equation / log-derivative (Riccati) formulation** | Propagating `T/W` removes the overall exponential scale | **NOT chosen.** The Riccati variable passes through poles wherever `W` vanishes, requiring re-initialisation logic whose placement is a tuning knob — a new free parameter in a lane whose entire point is zero free inputs |

### §4.3 THE PRIMARY METHOD (frozen)

Frozen: `the PRIMARY method is a compactified hyperboloidal Chebyshev spectral discretization in the Axiom-4 amplitude coordinate A = r_sat/r with the outgoing wave divided out in closed form, the traction-free SHORT imposed exactly as dpsi/deta = 0 at eta = 0, no boundary condition imposed at infinity, root extraction by extended-precision determinant polish, and pole counting by an argument-principle winding of the determinant phase; there is no matching radius, no asymptotic series, no shooting and no subdominant-coefficient extraction anywhere in the chain`.

**ENGINEERING-CHOICE TAG (`substrate-first-for-numbers`), stated explicitly.** Frozen: `the method is NUMERICS and is tagged ENGINEERING CHOICE; the medium, the profile, the kernel, the wall condition and the radiative port are CANON; no physical content of any kind is derived from the choice of discretization, and the gauge parameter lambda, the Chebyshev order n, the extended-precision dps and the contour sampling are engineering knobs whose only permitted role is to be varied and shown not to move the answer`.

### §4.4 Frozen numerics (every parameter fixed here)

- **Radial coordinate:** `A = r_sat/r`, `A = 1 − η²`, `η ∈ [0,1]` on Chebyshev–Gauss–Lobatto nodes.
- **Chebyshev order:** primary `n = 48`; independence set `n ∈ {48, 56, 64}`; reported convergence sweep `n ∈ {24, 32, 40, 48, 56, 64}`. **Justified in §4.6, not asserted.**
- **Hyperboloidal gauge:** primary `λ = 0`; independence set `λ ∈ {−0.25, 0.0, +0.25}`.
- **Extended precision:** `dps = 50` for every root polish and for the closed-form control roots; deterministic complex secant on `det M(Ω)` by mpmath LU, seeded from the double-precision linearized-pencil spectrum, terminating at `|Δ| ≤ 1e-38·|Ω|` or 60 iterations. **No RNG anywhere; no adaptivity; fully deterministic.**
- **Physics search rectangle (identical to v1's and v2's, so the bins stay comparable):** `ω_R M_g ∈ [0.02, 2.00]` × `|ω_I| M_g ∈ [1e-3, 1.00]`. **The left edge is NOT inherited on faith — it is certified against this lane's own mechanism in §4.6 and gated by C10.**
- **Zero-grade control box (identical to #845's own FT-5 box, so C1 is literally the test that killed v1):** `Re Ω ∈ [0.05, 6.0]` × `−Im Ω ∈ [0.02, 4.0]`, run at `ℓ ∈ {1, 2, 3}`.
- **★ Zero-grade control HIGH-|Ω| box (new in v2.1, closing defect 3):** `Re Ω ∈ [0.02, 20.0]` × `−Im Ω ∈ [0.02, 10.0]`, run at `ℓ ∈ {6, 10, 14, 18}`.
- **★ Count-vs-box-WIDTH family (new in v2.1, closing defect 4):** on the zero-grade control at `ℓ = 6`, the nested boxes `Re Ω ∈ [0.02, W]` × `−Im Ω ∈ [0.02, 8.0]` for `W ∈ {0.5, 1.0, 2.0, 4.0, 8.0, 16.0}`, with the closed-form content of each computed at run time.
- **★ C9 probe points (new in v2.1, closing defect 2):** the 4 corners, the 4 edge midpoints and the centre of the frozen physics rectangle — 9 frozen points.
- **★ C10 monitor points (new in v2.1, closing defect 1):** the 9 C9 probes plus 64 points sampled deterministically at equal parameter spacing around the frozen rectangle's boundary.
- **Contour sampling:** `{200, 400, 800}` points per rectangle side; winding read as the unwrapped phase of the **LU sign** of `det M(Ω)` (never a product of pivots, and never a sum of principal pivot logarithms — see §9 item 6).
- **Root dedupe radius:** `1e-6` relative.
- **Physical-vs-artifact criterion, frozen in advance:** `a located root is PHYSICAL only if it is present at every n in {48, 56, 64} within 1e-6 relative; roots failing this are reported as DISCRETIZATION ARTIFACTS and are excluded from every bin`.
- **C9 normalization rule, frozen deterministically:** `the C9 probe solves M_n(Omega) psi = b with b the all-ones vector, then normalizes psi by psi at eta = 0, falling back to the component of largest modulus if |psi(eta=0)| < 1e-13 times the infinity norm; convergence is measured on a frozen common grid of 200 equispaced eta by Chebyshev interpolation`.
- **Closed-cavity control (C6/C7/FT-F/FT-G):** traction-free at BOTH `r_sat` and an outer wall at `R_wall = 8 r_sat`, mapped by `r = r_sat + (R_wall − r_sat)ζ²`; Chebyshev order `n = 64`.
- **Runtime:** frozen `total battery runtime <= 3600 s on the reference machine; a longer run is disclosed, not silently accepted`. The budget is **not** an adjudication criterion.

### §4.5 Why `research/drivers/` and not `src/ave/`

Frozen: `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`.

### §4.6 ★ DERIVED BOUNDS (new in v2.1) — the left edge, the resolution, and the control reach

**All three numbers below are derived from the profile and the operator, before any eigenvalue exists. None is asserted and none is inherited.**

**(a) The left-edge bound, derived from THIS lane's own mechanism.** At the outflow point `η = 1` (`A = 0`) the leading coefficient `𝒜` vanishes and the collocated equation reduces to

```
4iΩ · ψ_η(1)  +  [ 2Ω²(1+4λ) − 4ℓ(ℓ+1) ] · ψ(1)  =  0
```

Define the **outflow-row balance ratio**

```
ρ_out(Ω) ≡ |𝒞(1)| / |ℬ(1)| = | 2Ω²(1+4λ) − 4ℓ(ℓ+1) | / (4|Ω|)     →   ℓ(ℓ+1)/|Ω|   as Ω → 0
```

After row equilibration the `ψ_η` coefficient in that row carries relative weight `1/ρ_out`, so it is resolved only to `≈ 10^(−dps)·ρ_out`. Requiring that to stay below the C3 target of `1e-12` gives the **derived left-edge bound**

```
|Ω|_min  ≥  ℓ(ℓ+1) · 10^(12 − dps)   =   6 × 10^(−38)   at ℓ = 2, dps = 50
```

The frozen rectangle's actual minimum is `|Ω|_min = 0.1402` (at `ω_R M_g = 0.02`, `|ω_I| M_g = 1e-3`, `x_sat = 7`). **The bound is cleared by 36 orders of magnitude.** Frozen: `the low-Omega outflow-row mechanism is REAL but NON-BINDING at the frozen rectangle: the derived bound |Omega|_min >= ell(ell+1)*10^(12-dps) equals 6e-38 at dps = 50 while the rectangle's actual |Omega|_min is 0.1402, a margin of 36 orders of magnitude; the left edge therefore does NOT move, and the mechanism is certified by the C10 conditioning monitor rather than by truncating the rectangle`. **This is stated as a derivation with a margin, not as an absence of a problem** — and C10 measures `ρ_out` across the whole rectangle rather than trusting the algebra.

**(b) The resolution requirement, derived from the profile's phase budget.** The factored envelope `ψ` carries the accumulated phase difference between the graded and ungraded light-travel times,

```
δ̂ ≡ (1/r_sat) ∫_{r_sat}^{∞} ( c₀/c_shear − 1 ) dr  =  ∫₀¹ ( (1−A²)^(−1/4) − 1 ) A^(−2) dA
```

which is a **property of the canonical profile alone** — no solution enters. Its value is `δ̂ = 0.4009298826`. The maximum envelope phase content over the frozen rectangle is therefore

```
Φ_max = |Ω|_max · δ̂ = 15.6525 × 0.4009298826 = 6.2755 rad   (≈ 2π: at most ONE oscillation across the whole domain)
```

An oscillatory content of `Φ` needs `n ≳ Φ/2` Chebyshev modes, i.e. `≈ 3.1` here; the binding requirement is instead the **analytic structure of the coefficient functions**, whose measured Chebyshev tail reaches `5.3e-16` by `n = 40` (§9 item 7). Frozen: `the frozen order set n in {48, 56, 64} is DERIVED, not asserted: the envelope's maximum phase content over the frozen rectangle is 6.2755 radians requiring about 3 modes, and the coefficient functions' own Chebyshev tail reaches 5.3e-16 by n = 40, so the frozen set clears both requirements and C9 measures the resulting graded-representation convergence directly at the rectangle's corners`.

**(c) The control reach, derived from the closed-form ladder.** The zero-grade control's closed-form roots have `|Ω|` reach growing with `ℓ`: `1.73` (`ℓ=1`), `2.45` (`ℓ=2`), `3.31` (`ℓ=3`), `6.09` (`ℓ=6`), `9.91` (`ℓ=10`), `13.78` (`ℓ=14`), `17.67` (`ℓ=18`). The frozen physics rectangle spans `|Ω| ∈ [0.1402, 15.6525]`. Frozen: `the frozen control ladder ell in {1, 2, 3, 6, 10, 14, 18} reaches |Omega| = 17.67, which COVERS the frozen physics rectangle's |Omega| span of 0.1402 to 15.6525 with an exact closed-form reference at both ends; v2's control box stopped at |Omega| = 7.2 and left the high corner uncovered`.

---

## §5 — THE FROZEN CERTIFICATION GATES (C1–C11), with numeric tolerances

**Every tolerance below is at least as strict as the corresponding v1 gate, and identical to or stricter than v2's. C9, C10 and C11 are NEW and add requirements; nothing is removed and nothing is loosened.**

| Gate | What it certifies | v1 / v2 analog | FROZEN criterion |
|---|---|---|---|
| **C1 ★** | **ZERO-GRADE CLOSED-FORM CONTROL — the entry ticket**, now covering the physics rectangle's full `\|Ω\|` span | v1 FT-5(b), which returned `15.000`; v2 C1, which stopped at `\|Ω\| = 7.2` | `on the zero-grade control, for ell in {1,2,3} over the frozen control box and for ell in {6,10,14,18} over the frozen high-Omega box, the number of located roots inside the box equals the closed-form root count computed at run time from the degree-(ell+1) polynomial, the located roots match the closed-form roots to <= 1e-20 absolute, and the argument-principle winding over the same box equals that same count exactly to <= 1e-3` |
| **C2** | **Hyperboloidal-gauge independence** | v1 G4 (`1e-8`, FAILED at `1.2377e-04`) | `\|Omega(lambda) - Omega(lambda')\| / \|Omega\| <= 1e-12 for every pair in lambda in {-0.25, 0.0, +0.25} at the primary n` |
| **C3** | **Resolution convergence** | v1 G5 (`1e-8`, FAILED at `1.9488e-05`) | `\|Omega(n) - Omega(n')\| / \|Omega\| <= 1e-12 for every pair in n in {48, 56, 64}` |
| **C4 ★** | **Argument-principle count consistency in the compactified frame, PLUS count-vs-box-WIDTH scaling at closed-form-known content** | v1 G7 (FAILED: winding `28` vs `34`); v2 C4, which lacked the width family | `the argument-principle winding over the frozen physics rectangle is within 1e-3 of an integer, is identical at contour sampling 200, 400 and 800 per side, and equals the number of distinct located roots inside that rectangle; AND over the frozen nested width family the winding equals the run-time closed-form content of EVERY box to <= 1e-3, so the count is NOT proportional to box width` |
| **C5** | **`nu_vac`-cancellation, MEASURED** | v1 G8 (`1e-9`, FAILED at `1.1058e-08`) | `Q, r_peak/r_sat and the overtone ratios are invariant to <= 1e-9 relative across x_sat in {5, 7, 11}, while omega_R*M_g scales as 1/x_sat to <= 1e-9 relative` |
| **C6** | **Spin-2 energy-functional consistency AND spin-2-vs-spin-1 discrimination** | v1 G2 (`1e-9`, PASSED) + v1 FT-6 | `the residual of the Euler-Lagrange identity built from the frozen spin-2 (ell-1)(ell+2) energy weighting, evaluated on the converged closed-cavity eigenfunction, is <= 1e-9 relative, AND substituting the spin-1 ell(ell+1) weighting into the same quotient breaks that agreement by >= 1e-3 relative` |
| **C7** | **Ax-3 lossless-reactive discipline** | v1 G6 (`1e-10`, PASSED at `0.0`) | `every eigenvalue of the CLOSED (doubly traction-free) cavity has \|Im omega\| / \|omega\| <= 1e-10` |
| **C8** | **Determinism** | v1 G9 | `two independent full driver runs produce an identical results digest (SHA-256 over the results object minus timing fields)` |
| **C9 ★ NEW** | **GRADED-representation accuracy at the rectangle's CORNERS, EDGE MIDPOINTS and CENTRE** — the hole v2 left, closed by resolution doubling rather than by a closed form (none exists for the graded operator) | none | `at each of the 9 frozen probe points of the physics rectangle, the normalized graded solution of M_n(Omega) psi = b converges under resolution doubling with max over probes of the infinity-norm difference between n = 32 and n = 64 <= 1e-10, measured on the frozen common evaluation grid` |
| **C10 ★ NEW** | **OUTFLOW-ROW CONDITIONING MONITOR across the rectangle** — certifies the boundary row rather than trusting the derived bound | none | `at every frozen C10 monitor point the measured outflow-row balance ratio rho_out = \|C(1)\|/\|B(1)\| satisfies rho_out * 10^(-dps) <= 1e-15, and the measured maximum rho_out over the frozen rectangle and gauge set is reported against the derived left-edge bound` |
| **C11 ★ NEW** | **Operator-identity verification of the η-form against the A-form** — the load-bearing algebra, checked as algebra | none | `the eta-form operator agrees with 4*eta^2 times the A-form operator to <= 1e-13 relative on the frozen set of arbitrary analytic test functions, over lambda in {-0.25, 0.0, +0.25}, ell in {2,3} and Omega spanning the frozen rectangle` |

**Certification classes (exhaustive).**
- **`SOLVER-CERTIFIED`** — `all of C1..C11 PASS and all of FT-A..FT-J FIRE`.
- **`SOLVER-CERTIFIED-SCOPED`** — `all gates pass and all self-tests fire, but at least one gate passes only over a REDUCED parameter set, stated explicitly in the result headline`.
- **`SOLVER-NOT-CERTIFIED`** — `any of C1..C11 FAILS, OR any of FT-A..FT-J fails to fire`. **A gate that cannot fail voids the certification exactly as hard as a gate that fails.** Under this class **no physics bin is adjudicated** (§7 precedence).

**Rule-11 fence on the method itself, frozen and binding.** `no gate, tolerance, frozen numeric parameter or method element in sections 4 and 5 may be changed after any gate result is seen; if this instrument fails certification the lane reports SOLVER-NOT-CERTIFIED and routes to its own successor with a new version number, exactly as #845 routed to v2 and v2 routed to v2.1`.

---

## §6 — GATE-FIREABILITY SELF-TESTS (FT-A…FT-J) — each MUST FIRE

**The rule (frozen).** `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is SOLVER-NOT-CERTIFIED regardless of how many gates passed`.

| # | Targets | Deliberate mis-specification | FROZEN firing criterion |
|---|---|---|---|
| **FT-A** | **C1** | perturb the wall-boundary-condition row by `1e-9` relative | `the corrupted operator MUST move the zero-grade control roots by >= 1e-15 absolute` |
| **FT-B** | **C2** | apply the hyperboloidal gauge `λ` to the interior coefficients but NOT to the wall-BC row — a realistic implementation bug | `the half-applied gauge MUST break C2 by >= 1e-12 relative` |
| **FT-C** | **C3** | run at `n = 8`, far below the resolution derived in §4.6(b) | `the under-resolved order MUST deviate from the n = 64 result by >= 1e-6 relative` |
| **FT-D ★** | **C4** | (a) a sub-rectangle containing no located root; (b) the zero-grade control box, count known in closed form; (c) a sub-rectangle containing exactly the fundamental; **(d) NEW — the nested width family, where the closed-form content SATURATES while the width keeps doubling** | `case (a) MUST return winding 0 to <= 1e-3, case (b) MUST return the closed-form root count for ell in {1,2,3}, case (c) MUST return 1 to <= 1e-3, and case (d) MUST return a count that stays equal to the run-time closed-form content while the box width spans a factor of 32, so a count proportional to box width MUST be excluded` |
| **FT-E** | **C5** — v1's OWN real first-run bug, weaponised | inject an `x_sat`-dependent profile perturbation `A -> A*(1 + 1e-6*(x_sat - 7)/7)` | `the x_sat-dependent perturbation MUST make the C5 spread exceed 1e-9` |
| **FT-F** | **C6 / the spin-2 discipline** — TWO independent discriminators | (i) spin-1 `ℓ(ℓ+1)` weighting in the Rayleigh quotient; (ii) the spin-1 wall condition `W'(r_sat) = 0` in place of the spin-2 `T(r_sat) = 0` | `(i) the spin-1 weighting MUST break the Rayleigh identity by >= 1e-3 relative, AND (ii) the spin-1 wall condition MUST move the fundamental Omega by >= 1e-2 relative` |
| **FT-G** | **C7** (Ax-3) | smuggled loss `Im(mu)/Re(mu) = 1e-3` | `the lossy closed cavity MUST return \|Im omega\|/\|omega\| >= 1e-5` |
| **FT-H ★ NEW** | **C10** | (a) evaluate the monitor at `Ω = 1e-36`, deep below the derived left-edge bound; (b) zero the outflow row's `ℬ(1)` coefficient — a plausible bug (forgetting the gauge term, or mis-evaluating at `η = 1`) | `case (a) MUST report rho_out * 10^(-dps) > 1e-15, and case (b) MUST drive rho_out non-finite or above 1e30, so the monitor detects both the physical degeneracy it exists for and a realistic implementation error` |
| **FT-I ★ NEW** | **C9** | run the graded probe at `n = 8 -> 16`, grossly under the derived requirement | `the under-resolved graded probe MUST exceed the C9 tolerance by returning a resolution-doubling difference >= 1e-10` |
| **FT-J ★ NEW** | **C11** | corrupt one `η`-form coefficient by `1e-12` relative | `the corrupted coefficient MUST break the operator identity by >= 1e-13 relative` |

---

## §7 — THE FROZEN PHYSICS BINS (identical to v1's and v2's; exhaustive; every bin REACHABLE; precedence stated)

**Rule-11 fence, stated up front and binding.** `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the solver returns is banked`. There is **no free parameter to tune** — that is the point of the lane.

**PRECEDENCE (frozen, evaluated in this order, identical to v1's).** `BIN-F-SOLVER` > `BIN-F-PROFILE` > `BIN-F-NOPOLE` > `BIN-1/2/3/4`. If an earlier bin fires, the later ones are reported as `N/A — not adjudicated` and **no verdict language is used about them.**

### Honest-failure bins (each reachable, each with a disposition)

| bin | condition | disposition |
|---|---|---|
| **`BIN-F-SOLVER`** | `any of C1..C11 FAILS or any of FT-A..FT-J fails to fire` | **SOLVER-NOT-CERTIFIED.** No physics bin adjudicated; the failing gate's numbers are reported; the lane returns the instrument failure as its result. No claim, no walk-back, no solidity change, **and no retune** — it routes to its own successor with a new version number. |
| **`BIN-F-PROFILE`** | `the canonical input set of section 3 is found to be internally inconsistent at solve time (two canonical statements that cannot both hold on the domain)` | **flag-don't-fix.** Both file paths + verbatim content surfaced to Grant and the auditor lane; **neither side reframed to match the other**; no bin adjudicated. |
| **`BIN-F-NOPOLE`** | `the certified solver returns argument-principle count 0 over the frozen rectangle` | **A decisive, clean negative and a GOOD outcome.** It would say the canonical graded profile with the canonical Ax-4 kernel, the canonical Op16 projection and the canonical SHORT supports **no `ℓ = 2` quasinormal resonance at all** in a band that comfortably brackets both GR and the standing corpus value — falsifying the standing ringdown chain at the level of *existence*, not of value. Banked as such; branch closed. |

### BIN-1 — the real part `ω_R M_g`

`D_omega ≡ omega_R_derived / omega_R_GR − 1`, with `omega_R_GR = 0.37367` read programmatically from the frozen `KERR_QNM[0.00]` row (I11).

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-1-MATCH`** | `abs(D_omega) < 0.03` |
| **`BIN-1-NEAR`** | `0.03 <= abs(D_omega) < 0.10` |
| **`BIN-1-MISS`** | `abs(D_omega) >= 0.10` |

Reported alongside, **not a separate class**: `D_omega_shortcut ≡ omega_R_derived/(18/49) − 1`, the deviation from the standing corpus shortcut `18/49 = 0.36735`; and the sign of both. **Class line (mandatory in the result headline):** `BIN-1 is VALUE-CONSISTENCY class, not emergence: omega_R*M_g carries the GR-imported nu_vac through the 7 in r_sat`.

### BIN-2 — the quality factor `Q` (★ the emergence-capable axis)

`Q_derived ≡ omega_R/(2*abs(omega_I))`; `Q_GR ≡ omega_R_GR/(2*omega_I_GR)` computed from the same frozen row; `D_Q ≡ Q_derived/Q_GR − 1`.

> **⚑ FLAG-1 — TWO comparator values for `Q_GR` exist in the corpus, and this lane freezes the SAME one v1 froze rather than adjusting.** The generating table `KERR_QNM[0.00] = (0.37367, 0.08896)` gives `Q_GR = 2.1002135791366907`. The **rounded KB-prose** pair `0.3737`/`0.0890` (`vol3/claim-quality.md:199`, `vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md:18`) gives `Q_GR = 2.0994`, the value carried at `research/2026-07-30_qlaw-derivation_scoping.md:401`. **These are the same underlying table at different precision (agreement to 3 s.f.; the gap is `0.0008`, i.e. `0.04%` — two orders below BIN-2's tightest boundary, so it cannot flip any bin.)** The frozen source did not move, so the programmatic value is used and the discrepancy is **surfaced, not silently adopted or silently ignored.** **★ FALSIFICATION RECORDED (flag-don't-fix): a review of the v2 prereg asserted that *nothing in the corpus reads 2.0994*. That assertion is FALSE.** Verified three independent ways (`grep -Fn`, full-tree `grep -rIn`, python line-index): `research/2026-07-30_qlaw-derivation_scoping.md:401` reads verbatim *"$3.2\%$") → $Q_{GR}(0) = 2.0994$, cold deficit $-4.74\%$. Agrees with the frozen table to 3 s.f."*, with its derivation from the rounded prose pair at `:398`–`:402`. **The v2 prereg's FLAG-1 was correct and is carried forward unchanged in substance; the review finding is the thing that needs correcting, and it is surfaced here rather than reframed.** Frozen: `Q_GR is computed programmatically from KERR_QNM[0.00] = (0.37367, 0.08896) and equals 2.1002135791366907; the rounded KB-prose value 2.0994 is the same table at 3 significant figures and is reported alongside, and the 0.04 percent gap between them is two orders below the tightest BIN-2 boundary and cannot flip any bin`.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-2-MATCH`** | `abs(D_Q) < 0.03` |
| **`BIN-2-NEAR`** | `0.03 <= abs(D_Q) < 0.10` |
| **`BIN-2-MISS`** | `abs(D_Q) >= 0.10` |

**And the three-way discriminator, frozen separately** (the axis that decides whether the substrate prefers GR's value or the corpus's `2π`-convention `Q = ℓ = 2`):

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-2-CLOSER-GR`** | `abs(Q_derived - Q_GR) < abs(Q_derived - 2.0)` |
| **`BIN-2-CLOSER-CONVENTION`** | `abs(Q_derived - 2.0) < abs(Q_derived - Q_GR)` |
| **`BIN-2-EQUIDISTANT`** | `abs(abs(Q_derived - Q_GR) - abs(Q_derived - 2.0)) <= 1e-6` |

**Class line (mandatory in the result headline):** `BIN-2 is the nu_vac-FREE axis: Q = Re(Omega)/(2*abs(Im(Omega))) contains no r_sat scale, so the GR-imported 7 cancels exactly`.

### BIN-3 — where the mode actually lives (FORK-1, handed to the substrate)

> **★ IDENTITY NOTE, frozen BEFORE results.** The "9/7-above-cutoff" statement is **not an independent axis** (§2.5). `r_eff = r_sat/(1+ν_vac) = 49M_g/9` with the cutoff identity `k r_eff = ℓ` gives `k₀ r_sat = ℓ(1+ν_vac) = 18/7 = 2.5714`, and `k₀ r_sat = x_sat·ω_R M_g` identically — so testing `k₀r_sat` against `18/7` **is** testing `ω_R M_g` against `18/49`. Reported as `k0_r_sat` with the tag `IDENTITY — not independent of BIN-1's shortcut comparison`.

Frozen observable: `u ≡ r_peak/r_sat`, where `r_peak` maximizes the frozen spin-2 mode-energy density `E(r) = rho|omega|^2|W|^2 r^2 + mu(|W' - W/r|^2 + (ell-1)(ell+2)|W|^2/r^2) r^2` over the frozen window `r/r_sat in [1.0, 2.0]`. A second, independent measure `u_kin` uses the kinetic term alone.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-3-RIM`** | `1.00 <= u <= 1.10` — the mode hugs the wall; the rim-ring reading |
| **`BIN-3-RAMP`** | `1.10 < u <= 1.50` — the mode sits in the stiffness ramp. Sub-flag `BIN-3-RAMP-TURNING-POINT` if additionally `abs(u - 1.2247) <= 0.05` |
| **`BIN-3-OUTER`** | `u > 1.50` — neither standing picture locates the mode |
| **`BIN-3-MONOTONE`** | `the energy density has no interior maximum in the frozen window (the maximum sits at an endpoint)` — localization is not a well-posed observable for this mode; the endpoint is reported |
| **`BIN-3-DISCORDANT`** | `abs(u - u_kin) > 0.10` — the two frozen measures disagree; both are reported and no localization verdict is banked |

**The `(1+ν_vac)` verdict rides on BIN-1's shortcut companion, stated in advance:** `if BIN-1's derived omega_R*M_g deviates from 18/49 by more than 3 percent, the standing chain's r_eff = r_sat/(1+nu_vac) assertion is FALSIFIED as a derivation of the eigenfrequency, and that is a GOOD outcome recorded as such`.

### BIN-4 — the overtone ladder

Poles are ordered by increasing `|ω_I|`; the fundamental is `n = 0`; **only roots satisfying the frozen PHYSICAL criterion of §4.4 are eligible.** `R_I ≡ abs(omega_I_n1)/abs(omega_I_n0)`, GR value `0.273915/0.088962` (I13, EXTERNAL comparator, tagged). `R_R ≡ omega_R_n1/omega_R_n0`, GR value `0.346711/0.373672` read programmatically from the in-repo `SCHW_OMEGA_R` (I12).

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-4-NONE`** | `exactly one physical pole is located in the frozen rectangle` |
| **`BIN-4-LADDER-MATCH`** | `at least two physical poles AND abs(R_I/R_I_GR - 1) < 0.10 AND abs(R_R/R_R_GR - 1) < 0.10` |
| **`BIN-4-LADDER-DIFFERENT`** | `at least two physical poles AND at least one of the two ratios is outside 10 percent` |

### Reachability audit (frozen — every outcome class has a reachable bin)

- `BIN-F-SOLVER` is reachable **and is demonstrated reachable every run**: FT-A…FT-G each drive an actual gate into its failing state.
- `BIN-F-PROFILE` is reachable: the canonical set carries live tensions this lane touches (#814 CF-7's unnamed `ρ` at `vol3/claim-quality.md:122`).
- `BIN-F-NOPOLE` is reachable: the argument principle over a **finite** rectangle returns an honest integer, which can be `0`.
- `BIN-1/2/3/4` sub-bins are each reachable because each is an interval or a strict comparison on a continuously-valued measured quantity, and the intervals **partition** their axis with no gaps and no overlaps. `BIN-3-MONOTONE` and `BIN-3-DISCORDANT` exist precisely so that "the question is ill-posed for this mode" has a bin.
- **No outcome requires a criterion to be relaxed after the fact.**

### Mutual satisfiability of the bins

1. **BIN-1 and BIN-2 are independent axes and can disagree.** Both bin sets are stated without any consistency requirement between them.
2. **`BIN-2-MATCH ⇒ BIN-2-CLOSER-GR`** (3% of `2.10021` is `0.063` while `|2.10021 − 2.000| = 0.10021`), and that implication is **stated deliberately**: the discriminator is informative exactly in the `NEAR`/`MISS` region, which is where the standing tension lives.
3. **BIN-3 does not presuppose a localized mode.**
4. **BIN-4 does not presuppose more than one pole.**
5. **The domain and the comparator are compatible.** The frozen rectangle brackets both `0.3737` and `0.3673` by more than a factor of `5` on each side and brackets `Q ∈ [0.01, 1000]`. There is no frozen precondition that excludes the values the lane is trying to measure.

---

---

## §8 — WHAT TRANSFERS FROM #845 AND FROM v2, AND WHAT MUST BE RE-EARNED

**TRANSFERS FROM #845 (framing and discipline, cited not copied):**
- the **ratified physics framing** — the transmission-line reading, the graded profile, the SHORT at `r_sat`, the radiative port, the spin-2 channel, `Q` as a pole. **#845's failure was of its *instrument*, not of its *physics statement*;**
- the **shape** of the certification battery — frozen gates with numeric tolerances, self-tests that must FIRE, a determinism digest, an exhaustive outcome-class table with a reachability argument;
- the **frozen-first commit order**;
- the **four bins and their boundary numbers**, re-derived from the same canonical sources and found unchanged;
- the **measured fact that the spin-2 weighting is load-bearing** — as a *motivation* to keep the spin-2 form, **not** as a number this lane may lean on;
- the **literal-7 advance identity** `k₀ r_sat = 7·ω_R M_g` at `#845 prereg:284`. **The `x_sat`-generalized form used here is NOT #845's and is minted in §2.5 as this lane's own frozen criterion — see the corrected attribution there.**

**TRANSFERS FROM v2 (`research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md`, commit `00724432`):** the method choice and its candidate evaluation, the compactified formulation, the import ledger, the bins, and gates C1–C8 at their frozen tolerances. **v2 produced no number and no result; nothing empirical transfers because nothing empirical exists.**

**DOES NOT TRANSFER — must be re-earned, and is (gate in brackets):**
- **the certification.** #845 is `SOLVER-NOT-CERTIFIED`; v2 was never run. [C1–C11]
- **every number.** No pole, no `Q`, no `Omega`, no localization ratio, no overtone, no sensitivity from #845 enters this lane as an input, a seed, a target, a tolerance or a comparator. **All of them are `NOT-ADJUDICATED prior-lane data`.**
- **the far-field treatment.** #845 matched to a truncated asymptotic series at a finite real radius. v2.1 has **no matching radius at all**. [C1, C2, C4, C9]
- **the pole-counting instrument.** [C1, C4, FT-D]
- **v2's coverage.** The four holes named in the supersession note are re-earned by C9, C10, C11 and C4's width family, not assumed away.

Frozen: `no gate, tolerance, certification class or measured number is inherited from PR #845; the physics framing and the bin boundaries transfer, the instrument and the certification do not, and every gate in section 5 is re-earned on this discretization`.

---

## §9 — MUTUAL SATISFIABILITY OF THE FROZEN REQUIREMENTS (checked BEFORE the freeze; fully disclosed)

Run on an **uncommitted scratch prototype** before this document was frozen.

> **★ DISCLOSURE, stated so it is auditable. Only MACHINERY, PROFILE PROPERTIES and the ZERO-GRADE CLOSED-FORM CONTROL were exercised. No graded-profile eigenvalue and no graded-profile solve was computed, estimated, seeded or looked at before these bins and gates were frozen.** The graded operator was exercised **only** to (i) confirm its coefficient functions are finite and spectrally resolved, and (ii) verify the `η`-form against the `A`-form **as an operator identity on test functions that solve nothing**. Neither produces an eigenvalue.

1. **★ The load-bearing algebra is verified as ALGEBRA (C11's pre-check).** `𝓛_η[ψ]` agrees with `4η²·𝓛_A[ψ]` to a worst relative deviation of `1.401e-15` across `λ ∈ {0, ±0.25}`, `ℓ ∈ {2,3}`, `Ω ∈ {0.9−0.3i, 2.5−1.1i, 14.0−6.0i}` and five `η` values spanning `[0,1]`, on arbitrary analytic test functions. **C11's `1e-13` therefore has two orders of headroom. Satisfiable, and it produced no physics observable.**
2. **The discretization is EXACT, not merely accurate.** Substituting the closed-form zero-grade eigenfunction into the assembled discrete operator at the closed-form eigenvalue returns a residual of `≤ 8.6e-16` in the infinity norm for `ℓ ∈ {1,2,3}` at `n = 16`. **This tests the SOLUTION REPRESENTATION, not a coefficient's expansion. Satisfiable.**
3. **The wall terminus is reached exactly and removes a parameter rather than adding one.** `A = 1 − η²` makes `η = 0` an ordinary regular point and the traction-free SHORT becomes the single exact condition `ψ_η(0) = 0`. **No offset, no series start, no floor. Satisfiable.**
4. **★ C1's headroom is enormous, and this is the gate that killed v1.** With `dps = 50` the determinant polish converged to the closed-form root to the full accuracy of the double-precision reference (`1.9e-15`, i.e. the *reference's* error, not the polish's); recomputing the reference in extended precision removes that floor entirely. **C1's `1e-20` has ≥ 25 orders of headroom over what v1's method could reach on the same problem. Satisfiable, and strict rather than generous.**
5. **★ The winding returns the closed-form count EXACTLY, which is precisely what v1 could not do.** On the frozen control box the winding read from the unwrapped phase of the LU sign of `det M(Ω)` returned `1.00000`, `1.00000`, `2.00000` for `ℓ = 1, 2, 3` — **identical at 200, 400 and 800 contour points per side** — and a deliberately pole-free box returned `0.000000`. **v1's same test returned `15.000` for all three `ℓ`. Satisfiable; C1/FT-D are live rather than tautological.**
6. **A naive determinant-by-log-pivots implementation FAILS this test, and that failure was found and fixed BEFORE the freeze.** Summing principal logarithms of the LU pivots gives a phase that jumps across branch cuts and returned windings of `8`, `27`, `30` on the same boxes. The frozen implementation therefore specifies the **LU sign** route explicitly (§4.4). **Disclosed so the frozen numeric specification is understood as load-bearing, not incidental.**
7. **The graded coefficient functions are finite and analytic on the grid.** At `n = 24/40/60` the assembled `𝒜`, `ℬ`, `𝒞` contain zero non-finite entries and the Chebyshev coefficient tail of `𝒞` falls to `5.3e-16` by `n = 40`. **This is a property of the COEFFICIENTS, not of any solution, and is labeled as such** (the v1 trap, named and quarantined). **C3's and C9's order sets sit well past it. Satisfiable.**
8. **★ C4's width family is live and discriminating, and it was exercised.** On the zero-grade control at `ℓ = 6, n = 32`, the nested boxes `W ∈ {0.5, 1.0, 2.0, 4.0, 8.0, 16.0}` returned windings `0, 0, 1, 2, 3, 3` (magnitudes) against run-time closed-form contents `0, 0, 1, 2, 3, 3`. **The content SATURATES at 3 while the width doubles from 8 to 16, and the family spans a factor of 32 in width — so a count proportional to box width is decisively excluded. Satisfiable, and it is exactly the artifact class §2.4 describes.**
9. **★ C10's monitor is comfortably satisfiable and its bound is derived, not assumed.** The measured maximum `ρ_out` over the frozen rectangle and the full gauge set is `42.803672`, so `ρ_out·10^(−dps) = 4.28e-49` against C10's `1e-15` — **34 orders of headroom** — while the derived left-edge bound `6e-38` is cleared by the rectangle's actual `|Ω|_min = 0.1402` by 36 orders. **FT-H supplies the fireability, since a gate with 34 orders of headroom would otherwise be dead.**
10. **★ The C9 tolerance is justified by derivation rather than by scouting.** The graded probe itself was **deliberately not run before the freeze** (it is a graded solve). Its tolerance is instead derived from three independently measured facts: the operator identity holds to `1.4e-15` (item 1), the coefficient tail reaches `5.3e-16` by `n = 40` (item 7), and the maximum envelope phase content over the whole rectangle is `6.2755` radians requiring `≈ 3` modes (§4.6(b)). **C9's `1e-10` at `n = 32 → 64` follows from those with margin. Stated as a derivation with its risk disclosed: if the graded solve nonetheless fails C9, that is an honest SOLVER-NOT-CERTIFIED and routes to a successor — it will NOT be retuned.**
11. **C2 and C3 probe genuinely different knobs.** `λ` changes the analytic prefactor and therefore every coefficient function *and* the wall-BC row; `n` changes only the resolution. FT-B's half-applied gauge shows C2 is sensitive to exactly the coupling a real bug would break. **Jointly informative.**
12. **C5 is a structural identity checked as an arithmetic-fidelity gate, and FT-E supplies its fireability** (§0). **Disclosed in advance.**
13. **Runtime.** The dominant costs are the mp determinant polish (`≈ 0.1 s` at `n = 32`, `≈ 0.8 s` at `n = 64` per evaluation), the double-precision winding contours, and C9's `2 × 9` graded solves. The frozen `3600 s` budget has headroom.

---

## §10 — FLAGS RAISED AT FREEZE TIME (flag-don't-fix; surfaced, not resolved)

1. **⚑ FLAG-1 — the two `Q_GR` comparator values, AND the falsified absence claim.** Fully stated in BIN-2. The programmatic `2.1002135791366907` is frozen (v1's choice, unchanged); the rounded-prose `2.0994` is reported alongside; the gap is `0.04%`, two orders below the tightest bin boundary. **A review assertion that nothing in the corpus reads `2.0994` is falsified by three independent methods at `research/2026-07-30_qlaw-derivation_scoping.md:401`.** Routed to the auditor lane as a corpus-precision question, **not repaired here**.
2. **⚑ FLAG-2 — this lane DECLINES to gate on #845's `0.21729` spin-1 break, deliberately.** Frozen: `the #845 FT-6 value 0.21729 is NOT-ADJUDICATED prior-lane data produced by a SOLVER-NOT-CERTIFIED instrument and therefore may not gate this lane; the spin-2-vs-spin-1 discrimination is gated instead on its OWN frozen thresholds (C6 and FT-F), and the comparison against 0.21729 is REPORTED as cross-lane corroboration with no gating power`. Two structural reasons: (a) an uncertified instrument's diagnostic cannot certify its successor; (b) the two lanes evaluate the Rayleigh quotient on **different objects**, so numerical agreement is **not expected** and requiring it would be a false gate firing on a difference of setup rather than of physics. **The discrimination itself is mandatory and gating; only the specific inherited number is not.**
3. **⚑ FLAG-3 — I7 is assumed, not tested.** The radiative port at infinity with no far-field structure and no second reflection is a **frozen canonical input**, and this lane's entire method divides out the corresponding analytic factor. If the substrate carries any far-field reflector, every number in this lane is wrong in the same direction. **Surfaced in the §0 plumber question; not tested here; routed.**
4. **⚑ FLAG-4 — #814 CF-7's naming gap stands, untouched.** `vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` and never names which `ρ`. This lane consumes the leading reading (`ρ₀`, I5) as a frozen input and does **not** repair the leaf.
5. **⚑ FLAG-5 — the `15.000` characterisation is corrected at source, and the correction is CITED not re-derived.** §2.4 replaces the "optical length" reading with the phase-rate reading supplied by the concurrent #845 audit. **This lane did not re-derive that refinement and no v2.1 gate depends on it**; the artifact class is excluded empirically by C4's width family instead. Routed so the #845 result doc's own §2.2 wording can be corrected by its lane, not by this one.

---

## §11 — LEDGER TAGS + OWED FOLLOW-ONS (fenced; NOT executed here)

**Ledger tags (`consistency-vs-emergence`, frozen).** `omega_R*M_g` is `[derived]` but **VALUE-CONSISTENCY** class (rides the GR-imported `7`). `Q`, `r_peak/r_sat` and the overtone ratios are `[derived]` and `ν_vac`-**FREE**, hence **emergence-capable at value level**. The GR numbers are `[GR-IMPORTED comparators]` (I11–I13), one of which (I13) has **no in-repo carrier** and is disclosed as external. `ν_vac = 2/7` is `[canon]`, read-only, value GR-imported. Gate residuals, Chebyshev orders, gauge parameters and precisions are `[engineering]`. **`α`-CLEAN. No manifestation-class claim. No claim of any kind is minted.**

**Owed follow-ons (fenced; Rule 12 — the slot is NOT refilled with an assertion):**
1. **The spheroidal (even-parity / P–SV-coupled) branch.** Toroidal only here. A stage-2 build with its own prereg.
2. **FORK-3's naming gap** (FLAG-4). Routed to the auditor lane.
3. **FORK-9's formal half** — whether Op6's phase-matching condition applies to a graded shear cavity with a `Γ = −1` inner wall.
4. **FORK-12** — the win-or-falsifier question must be answered by Grant **before** any `ℓ`-ladder verdict is banked.
5. **The exterior-complex-rotation cross-check (§4.2 candidate (a))** as an independent second instrument. Not built here; a genuine independent confirmation would need it.
6. **FLAG-3's far-field assumption** — a test that the Regime-I port really is reflectionless at the scales that matter.
7. **FLAG-5's routing** — the `#845` result doc's optical-length wording, corrected by its own lane.

---

> **Pre-registration provenance.** Frozen pre-registration for the cold-Q pole derivation **v2.1** authorized by Grant on 2026-08-03, verbatim `[sic]`: `"Go on cold-Q"`. Written against `origin/main` = `583d43dd`. Committed **ALONE** and pushed before any driver code and before any number existed. **Supersedes** `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` (commit `00724432`), which remains **byte-untouched as the record** — pre-measurement versioned supersede, no result existed. **Predecessor lane (KEEP-BOTH, unmodified):** `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` and `..._result.md` (PR #845, `SOLVER-NOT-CERTIFIED`, all four bins `N/A`). Companion inputs cited by path: `research/2026-07-30_qlaw-derivation_scoping.md`; `research/2026-07-31_qlaw-framing-challenge_walk.md`; `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51`; `research/2026-07-20_ringdown-systematics_checks.py:72-73`. Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched regardless of outcome. Companion: the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-pole-v2.md`.
