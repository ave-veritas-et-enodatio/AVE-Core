# The cold-Q **polar family** — FROZEN pre-registration (**the coupled shear–bulk channel network; the isospectrality discriminator**)

**Date:** 2026-08-03
**Lane:** cold-Q MODEL-FIDELITY + POLAR-FAMILY
**Written against:** `origin/main` = `ce65b3b8`
**Class:** DERIVATION pre-registration (**mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` is BYTE-UNTOUCHED; `ave.core.constants` is imported read-only.

> **THIS FILE IS FROZEN AND IS PUSHED ALONE, BEFORE ANY DRIVER CODE EXISTS AND BEFORE ANY NUMBER PRODUCED BY THIS INSTRUMENT EXISTS.** No gate, tolerance, band, frozen numeric parameter, bin boundary or method element below may be changed after any result of this instrument is seen.

---

## §P — PROVENANCE

### §P.1 Grant's ruling, verbatim

> **"2. Proceed"**

*[sic]* — Grant, 2026-08-03, on the option to run the polar solve. That is the whole of the authorising text and it is reproduced without expansion.

### §P.2 The fidelity fork was routed by the merged v2.4 result document itself

The second half of this lane's remit is not a new instruction; it is a routing the merged v2.4 result document already carries. Quoted verbatim from `research/2026-08-03_coldq-pole-v2.4-root_result.md:321` (blob `18a38735324c2dbfb4b242a37089ad1591ec2c61`, on `origin/main`):

> *"**★ FLAG-4 — #814 CF-7's naming gap is untouched, and it is now load-bearing on a falsification.** `manuscript/ave-kb/vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` and never names which `ρ`. This lane consumed the leading reading (`ρ₀`, `I5`). **The prereg's `X6` fences off FORK-3(b)'s alternative `ρ_eff = ρ₀/S³`, which is NOT run here — and which would move the eigenvalue.** Before the `BIN-1`/`BIN-2` misses are read as a falsification of the profile, that fork is owed a run. **Surfaced, not resolved.**"*

and at `:320`:

> *"**★ FLAG-3 stands, and it is now the single biggest threat to the physics reading of this result.** `I7` — the reflectionless Regime-I port at infinity — is a **frozen canonical input, assumed and not tested**, and this lane's entire method divides out the corresponding analytic factor. **If the substrate carries any far-field reflector, the certified root moves and the `29 %`/`56 %` misses are misattributed.** A `ROOT-CERTIFIED` verdict does **not** touch this flag. **Routed as the highest-value follow-on to the negative.**"*

**This lane discharges FLAG-4 and FLAG-3 as derivations (§2.3, §2.4) and runs FORK-3(b) as a frozen, disclosed sensitivity (§4.6).**

### §P.3 The isospectrality insight, and its reasoning

**Grant-ratified framing, stated here as the physics premise of the whole lane.**

In General Relativity the Schwarzschild `ℓ = 2` axial (Regge–Wheeler) and polar (Zerilli) quasinormal spectra are **identical**. That degeneracy is **GR's own theorem** — it follows from the Chandrasekhar–Detweiler transformation relating the two potentials, and it is a property of the Einstein equations, not a property of "any theory of a ringing compact object."

**A medium with SEPARATE channel impedances generically breaks it.** The axial family is a pure **shear-channel** (`T2`) problem: its displacement field is exactly divergence-free, so the bulk modulus drops out identically and the only material function it sees is `μ(r)`. The polar family is the **coupled shear + bulk two-line network**: its displacement field carries both a dilatation and a shear, the two are coupled by the radial gradients of the moduli, and it sees `μ(r)`, `K(r)` and `ρ(r)` together. **Two families that sample different constitutive content have no reason to share a spectrum** unless a special structure forces them to — and in a graded medium with `Z_shear ≠ Z_bulk` there is no such structure.

**Therefore:**

- If the polar family lands **on top of** the axial pole, that is a **nontrivial consistency** — the substrate reproduced a degeneracy it was not obliged to reproduce.
- If the polar family lands **off** the axial pole, AVE predicts a **SPLIT ringdown spectrum where GR predicts degeneracy**. That is a **forward divergent prediction**, in principle observable in ringdown data, and it is a **discriminator, not an escape** from the v2.4 misses. It is stated here, before the run, so that neither outcome can be presented as the one the lane was hoping for.

Frozen: `the axial/polar isospectrality of Schwarzschild is a theorem of GR, not a generic property of a ringing compact object; a medium carrying separate Z_shear and Z_bulk generically splits the two families, so a SPLIT is a forward divergent prediction and a DEGENERACY is a nontrivial consistency, and this lane commits to both readings in advance`.

**Vocabulary discipline (binding on this lane's own prose).** The coupled family is written **"the coupled shear–bulk channel network"**, or "the polar family". The seismological name for the same mathematical object is **not** used anywhere in this lane's tracked files.

### §P.4 Supersession / relationship — this lane SUPERSEDES NOTHING

**This lane EXTENDS the certified v2.4 arc to the second mode family. It does not supersede, revise, re-score, rescue or retract any predecessor.**

Every predecessor frozen file is **BYTE-UNTOUCHED** by this lane and is cited by blob SHA so that the claim is checkable rather than asserted:

| predecessor frozen file | blob SHA (`git hash-object`) at `ce65b3b8` |
|---|---|
| `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` (v1, PR #845 MERGED) | `90a16113a8cfdf255fedeca30d183ce42fc6526e` |
| `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` | `0e34ff98ed21d41eaec07fee06c6638ee2b507bc` |
| `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` | `4fc4faf92eda610971f5814c07de3c084db8f5fc` |
| `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` | `b7a209bd035775e897e8b9a439330e68bdc5e9e9` |
| `research/2026-08-03_coldq-pole-v2.3-root_prereg-FROZEN.md` (superseded PRE-MEASUREMENT) | `33432ac7fd20eb5c4a348c4b2428a799b5f4dd4b` |
| **`research/2026-08-03_coldq-pole-v2.4-root_prereg-FROZEN.md`** (commit `d5b9978b`) | `894be984a41010f6f9629967464300fe023a2f3d` |
| **`research/2026-08-03_coldq-pole-v2.4-root_result.md`** (`ROOT-CERTIFIED`) | `18a38735324c2dbfb4b242a37089ad1591ec2c61` |
| `research/drivers/coldq_pole_v2p4_root.py` | `6758725b10ccec684021e13767fdf29349226973` |
| `research/drivers/coldq_pole_v2p4_root_results.json` | `207f9e7b6a3f3bcfd970f03c36cc51a5dcba2b95` |

Frozen: `this lane EXTENDS the certified v2.4 arc to the second mode family and supersedes, revises, re-scores, rescues and retracts nothing; every predecessor frozen file is byte-untouched and is cited by blob SHA`.

### §P.5 Carry-over disclosure — this instrument is NOT independent of v2.4

Frozen: `the polar instrument CARRIES OVER the v2.4 numerical machinery (Chebyshev-Gauss-Lobatto differentiation in double and in mp, the quadratic-pencil linearization and its seeding path, the mp LU determinant and secant polish, the mp inverse-iteration eigenfunction, the relative-separation-in-mp helper and the root cache) by COPY-WITH-ATTRIBUTION from research/drivers/coldq_pole_v2p4_root.py at blob 6758725b10ccec684021e13767fdf29349226973; it is NOT an independent reimplementation of that machinery, and no agreement between this lane and v2.4 on any shared quantity may be presented as independent corroboration`.

Transcription sites in the driver carry `[xcribe v2.4 ...]` markers. **What is NEW here and is NOT carried over:** the two-field coupled operator, its derivation, the moduli grading, the wall rows, the branch fork, the dilatation diagnostic, and every gate specific to those. **That is where any defect in this lane will live, and the gates are concentrated there.**

---

## §0 — SECTOR / REGIME / PHASE-STATE / COORDS header, declared BEFORE any physics word

**Re-walked fresh for the polar family. It is NOT the axial header with a word changed — the sector line is materially different, and that difference is the entire lane.**

- **MODE.** Cold (`a_* = 0`, Schwarzschild-limit) post-merger remnant ringing down. The object is the `ℓ = 2` **polar** (even-parity) quasinormal resonance of the saturation cavity — **one** resonance of that family, not its ladder.
- **SECTOR — and this is the line that changed.** The observable is a **coupled A1-dilatation + T2-shear** oscillation. The **bias field** that builds the cavity is still the **A1 radial dilatation** `ε_11 = 7GM/(c²r)` (the DC operating point). The **small-signal AC** now rides in **both** grades at once: the polar displacement field carries a non-zero dilatation `Δ = ∇·u` (A1) **and** a non-zero shear (T2), and the two are coupled by the radial gradients of the moduli. **★ SECTOR-OWNERSHIP CHECK (A1 ⊥ T2, no cross-wiring):** the A1 grade owns the **dilatation / mass** channel and its modulus `K`; the T2 grade owns the **shear** channel and its modulus `μ`. This lane does **not** claim that one confines or holds the other. It claims only what the elastodynamic operator forces: a **linear coupling through `dμ/dr` and `dλ/dr`**, which is a constitutive-gradient coupling, not a sector re-assignment. **The DC bias remains pure A1 and remains time-independent.**
- **REGIME.** Far field (`r ≫ r_sat`) = **Regime I** — linear, lossless, reactive; a legal radiating port, now **two** ports (one per channel). The graded exterior `r > r_sat` = Regime I with two spatially varying moduli (Op14 grade). The wall `r = r_sat` = the Regime III→IV terminus. The interior `r < r_sat` = **Regime IV**, outside the computational domain. Domain: `[r_sat, ∞)`.
- **PHASE-STATE.** Op14 ON throughout the graded exterior as a **static constitutive grade**. `A = 1` exactly at `r_sat = 7GM/c²`.
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the **dimensionless-eigenvalue register** (`ω_R M_g`, `ω_I M_g`, `Q`) that AVE and GR share, and the SPLIT observable is a **dimensionless ratio of two eigenvalues computed by the same instrument in the same register**. No phase-space/real-space mismatch; no port→pole transfer.
- **★ NOTATION FENCE, declared because this lane carries two objects that both want the letter `λ`.** The **Lamé first parameter** is written `λ_L`; the **hyperboloidal gauge parameter** — which v2.4 wrote `λ` — is written **`κ`** throughout this lane. In the driver they are `lam_L` and `HGAUGE`. Frozen: `this lane writes the Lame first parameter as lambda_L and the hyperboloidal gauge parameter as kappa; the v2.4 symbol lambda for the gauge is deliberately renamed and no expression in this lane uses the bare symbol lambda`.

### Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code)

1. **K4 / srs connectivity.** CONTINUUM instrument. Frozen: `the radial channel is a CONTINUUM representation of the shear and bulk constitutive laws; it is not a discretization of the srs stencil and carries no K4 connectivity claim`. What it consumes from the lattice is the **constitutive law only**.
2. **★ Cosserat / channel basis — the checkpoint that creates this lane.** v2.4's walk concluded, verbatim from `research/2026-08-03_coldq-pole-v2.4-root_prereg-FROZEN.md:136`: *"the toroidal (odd-parity) branch is exactly divergence-free, so the bulk modulus drops out identically and there is no linear P-SV conversion partner; the single-channel classification is structural in this branch"*. **That sentence is TRUE and it is also a statement of what v2.4 could not see.** The polar branch is **not** divergence-free; the bulk modulus does **not** drop out; the two channels **do** convert into one another at every radius where the moduli have a gradient. This lane builds exactly the object that sentence excluded.
3. **Op14 saturation.** Enters as the static constitutive grade `S(A) = sqrt(1 − A²)`, `A(r) = r_sat/r`, projected into **shear** by Op16 (`c_shear = c₀·sqrt(S)`) and into **bulk** by the `K = 2G` operating point — **and the bulk projection is where canon does not speak with one voice (§2.2, FLAG-W).**
4. **The compactification is the medium's own order parameter.** The radial coordinate is `A = r_sat/r`, the Axiom-4 saturation amplitude itself; `A = 1` IS the wall, `A = 0` IS infinity. Unchanged from v2.4 and re-adopted deliberately.
5. **Phase-space vs real-space (A46).** Every verdict-class observable is a dimensionless ratio: `ω M_g`, `Q`, and the SPLIT. **α-CLEAN** — `α` appears nowhere in the chain.
6. **Boundary-not-bulk.** The resonator is a boundary/graded-shell object. The loss is a radiative port at infinity, Ax-3-licensed, and there is **no `Re{Z}` anywhere in the medium**. G10 tests exactly that, on this lane's own operator.
7. **★ NEW CHECKPOINT — is a two-channel wave operator substrate-native, or is it an imported elasticity default?** It is substrate-native, and the receipt is that AVE's own **three-impedance law** already names the two mechanical channels and gives each its own impedance and its own reflection coefficient at this very boundary ([`common/port-register.md:49`](../manuscript/ave-kb/common/port-register.md), [`vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md`](../manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md)). A wave operator that carried only one of them would be the **imported** object, not the substrate-native one. **What IS imported and is tagged as such: the isotropic-continuum form of the coupling.** The substrate is a chiral Cosserat medium with a microrotational sector; a full Cosserat polar operator would carry a third (rotational-`μ`) channel with its own gapped dispersion. Frozen: `this lane builds the ISOTROPIC two-channel (shear + bulk) continuum operator and explicitly does NOT build the Cosserat microrotational channel; the omission is an approximation of the substrate, it is tagged here rather than discovered later, and any result of this lane is conditional on the microrotational channel not participating at l = 2 in the cold limit`.
8. **★ Checkpoint: what the substrate does NOT supply.** `ℓ = 2` is not derived here. No low-frequency cutoff is derived here. **And the substrate does not here supply the sign of the bulk modulus's response to compressive saturation — that is FLAG-W, and it is the finding of this lane's derivation phase (§2.2).**

### Pre-test physics check (`pre-test-physics-check`, Rule 16 — ONE plumber question surfaced to Grant BEFORE the design locks)

> **Grant — this is the question the derivation threw off, and it is a plumbing question, not a mathematics question.**
>
> I went to canon to find out what the vacuum's **bulk** line does at the saturation wall, because the polar family needs it and the axial family never did. **Canon gives me two opposite answers, in two leaves, both canonical, both about the same surface at `r_sat`.**
>
> - One leaf says the bulk line **opens**: `c_bulk → 0`, `Z_bulk → 0`, `Γ_bulk = −1`. That is a **pressure-release** wall — a free surface, like a pipe venting to atmosphere. The compression wave hits it and bounces with a sign flip.
> - The other leaf says the bulk line **jams**: `D = 1/S → ∞`, the modulus goes rigid, "halting the collapse". That is `Z_bulk → ∞`, `Γ_bulk = +1` — a **rigid** wall, like a pipe dead-ended into a block of steel. The compression wave hits it and bounces with no sign flip.
>
> **In plumber terms: at the saturation radius, does the vacuum's compression line vent, or does it dead-end?** The shear line is not in dispute — it vents (`G_shear → 0`, the solid melts, `Γ_shear = −1`). It is the compression line I cannot settle from the corpus.
>
> **Why I cannot just pick one.** They are not the same wall with two descriptions. They are two different boundary-value problems and they will give two different polar frequencies — possibly one of them no polar mode at all. **And the axial lane could not have caught this**, because the axial mode never touches the bulk line: that is precisely why this fork surfaced now and not four lanes ago.
>
> **What I am doing about it, frozen before any number:** I am **not** picking. I run **both** branches, report **both**, and if they give different bin verdicts the result is reported as **BRANCH-DEPENDENT** and routed to you (§7.5). The contradiction is surfaced with both file paths and both verbatim sentences (§2.2) and is **not repaired** in either leaf by this lane.
>
> **Carried forward unchanged and NOT re-asked:** v2.2's and v2.4's deferred question — a substrate-derived low-frequency cutoff — stays deferred, and `BIN-P4`-class completeness statements stay `N/A BY CONSTRUCTION`.

### Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE any result

Written in units of `r_sat`, the polar problem has **no free parameter**: the profile is `A = r_sat/r`, the kernel is `S = sqrt(1 − A²)`, the shear speed is `c₀·sqrt(S)`, the bulk modulus is fixed by the `K = 2G` operating point on whichever branch is being run, and the inertia is the cold `ρ_bulk`. `Ω ≡ ω·r_sat/c₀` is a **pure number** fixed by the profile shape, the two moduli laws, and `ℓ`.

| output | rides `r_sat`'s coefficient `7`? | class |
|---|---|---|
| `ω_R M_g` (BIN-P1) | **YES** — `ω_R M_g = Re(Ω)/x_sat`, `x_sat = 7` | **VALUE-CONSISTENCY.** The `7` is the `1/7` trace-reversed bulk projection, which takes `ν_vac = 2/7` as **input** ([`one-seventh-impedance-projection.md:18`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md)). **May NOT be headlined as value-level emergence.** |
| **the SPLIT (BIN-P2)** | **NO — it cancels exactly** | **★ `ν_vac`-FREE and the most emergence-capable object in the whole arc.** It is a ratio of two eigenvalues of the SAME cavity computed by the SAME instrument: `r_sat` divides out identically, and so does every instrument-common systematic. **This is the axis where an AVE-distinct forward prediction can live.** |
| `Q` (BIN-P3) | **NO — it cancels exactly** | **`ν_vac`-FREE, emergence-capable at value level.** |
| the existence and location of the polar root | LOCATION rides it; SHAPE does not | the certified object is `Ω`, a pure number |

Frozen: `the SPLIT and Q are exactly nu_vac-free (the r_sat scale divides out identically); omega_R*M_g is NOT and is VALUE-CONSISTENCY class because the 7 in r_sat = 7GM/c^2 is the 1/7 projection of the GR-imported nu_vac = 2/7`.

> **★ WHAT A CERTIFIED POLAR ROOT WOULD AND WOULD NOT MEAN, written before the run.** A `SOLVER-CERTIFIED` verdict is a statement about an **instrument**. It does **not** say the substrate rings there. It says nothing about other modes of either family. **And specific to this lane: a certified polar root on ONE branch of FLAG-W is a certified root of ONE of two candidate media, not of "the AVE vacuum" — because canon has not yet said which medium it means.**

---

## §1 — THE TARGET, AND THE EXPLICIT NON-CLAIM

### §1.1 The target

**The `ℓ = 2` polar (even-parity, coupled shear–bulk) quasinormal pole of the graded saturation cavity, on the canonical profile, with zero free parameters — and its separation from the certified axial pole.**

The axial comparator, cited from the merged v2.4 shipped JSON (`research/drivers/coldq_pole_v2p4_root_results.json`, blob `207f9e7b6a3f3bcfd970f03c36cc51a5dcba2b95`, key `adjudication.omega_R_M_g`; certified root `certified_root.Omega_re_mp` / `Omega_im_mp`):

```
omega_R M_g (axial, certified)  =  0.2648078872629827
Omega       (axial, certified)  =  1.853655210840878848320699157729883961213
                                 - 1.00725678314331889260211374956072904467 i
```

**It is read PROGRAMMATICALLY from that in-repo JSON at run time. Nothing about it is typed into a gate, a tolerance or a bin as a literal.**

### §1.2 The non-claim, written in advance and binding

> **This lane asserts the existence and location of the polar roots it certifies, on the branches it certifies them on. It asserts NOTHING about the absence or presence of other modes in either family, and NOTHING about which branch of FLAG-W the substrate actually is.**

Frozen: `this lane asserts the existence and location of the polar roots it certifies on the branches it certifies them on; it asserts NOTHING about the absence or presence of other modes in either family and NOTHING about which branch of FLAG-W the substrate actually is`.

Operationally, each of these is a prohibition on this lane's own result doc:

- **NO winding, argument principle, or contour integral is computed over any rectangle, box or region, anywhere in this lane.** Frozen: `no argument-principle winding, no contour integral and no region count is computed anywhere in this lane`.
- **NO completeness claim, no "the only polar mode", no overtone, no ladder, no mode count.**
- **NO claim that a certified polar root is the FUNDAMENTAL of its family.**
- **NO retroactive re-scoring of v2.4.** A certification here neither strengthens nor weakens v2.4's `ROOT-CERTIFIED` verdict.
- **NO repair of either FLAG-W leaf.** Both are cited verbatim and left byte-untouched.

### §1.3 What this lane additionally does NOT do

- **Y1** — does NOT derive `ℓ = 2`.
- **Y2** — does NOT derive `ν_vac`, `K = 2G`, or the `7` in `r_sat`. GR-IMPORT, closed by PR #261/#506, untouched.
- **Y3** — does NOT touch the spin (`a_* > 0`) mapping.
- **Y4** — does NOT compute a port-`Q`, a radiation resistance, or a stored-energy `Q`.
- **Y5** — does NOT build the **Cosserat microrotational** channel (§0 walk item 7).
- **Y6** — does NOT adjudicate FLAG-W. It runs both branches and routes.
- **Y7** — does NOT derive, assume, sketch or gesture at a low-frequency cutoff.
- **Y8** — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry, whatever the outcome.
- **Y9** — does NOT widen, move or re-define any bin boundary after any result is seen.
- **Y10** — does NOT compute a GR polar (Zerilli) mode of its own. The GR comparator is the **same** `I11` pair v1/v2.1/v2.2/v2.4 used, read programmatically, and GR's own axial/polar degeneracy is what licenses using one comparator for both families (§P.3).

---

## §2 — THE PHYSICS TASK, DERIVED BEFORE ANY NUMBER

**Everything in this section is derived, or cited verbatim, BEFORE the driver exists. Where canon under-determines an input, the candidates are frozen here and BOTH are run as a disclosed sensitivity — chosen in advance, not selected after seeing a result.**

### §2.1 The coupled polar radial system — DERIVED, not imported

The medium is a radially graded isotropic elastic continuum with Lamé parameters `λ_L(r)`, `μ(r)` and inertia `ρ(r)`. The polar (even-parity) displacement field for a scalar surface harmonic `Y` is

```
u  =  U(r) Y r^  +  V(r) grad_1 Y          (grad_1 = the unit-sphere surface gradient)
```

so the field carries a dilatation `Δ = ∇·u = [U' + (2U − L V)/r] Y` with `L ≡ ℓ(ℓ+1)`. **`Δ ≠ 0` is the whole difference from the axial family.**

The equation of motion is `∇·T + ρω²u = 0` with `T = λ_L Δ I + 2μ e`. For radially varying moduli,

```
∇·T  =  λ_L' Δ r^  +  (λ_L + μ) ∇Δ  +  μ ∇²u  +  2 μ' (e · r^)
```

**Projection onto `Y` and onto `grad_1 Y` gives the coupled radial system. It was derived SYMBOLICALLY (`sympy`), for `ℓ = 2`, `3`, `4` independently, verified `θ`-separable at each `ℓ`, and verified to be EXACTLY AFFINE in `L = ℓ(ℓ+1)` (the three-point affine-interpolation residual is identically `0`).** The derivation is reproduced inside the driver as the `G0(c)` gate and is re-run there rather than trusted:

```
RADIAL  (coefficient of Y):

  (λ_L + 2μ) U''
    + [ λ_L' + 2μ' + 2(λ_L + 2μ)/r ] U'
    + [ ρω² + 2λ_L'/r − (2(λ_L + 2μ) + L μ)/r² ] U
    − [ L (λ_L + μ)/r ] V'
    + [ −L λ_L'/r + L (λ_L + 3μ)/r² ] V
    = 0

TANGENTIAL  (coefficient of grad_1 Y):

  μ V''
    + [ μ' + 2μ/r ] V'
    + [ ρω² − μ'/r − L (λ_L + 2μ)/r² ] V
    + [ (λ_L + μ)/r ] U'
    + [ μ'/r + 2(λ_L + 2μ)/r² ] U
    = 0
```

**Frozen:** `the coupled polar radial system is DERIVED symbolically from the graded-moduli Navier operator, is verified theta-separable at ell = 2, 3 and 4 independently, and is verified EXACTLY affine in L = ell(ell+1) with an identically-zero three-point affine residual; the derivation is re-executed inside the driver as gate G0(c) rather than trusted`.

**Two independent sanity limits, both stated before the run and both gated:**

1. **Fluid limit `μ → 0`.** The tangential equation collapses to `ρω²V = −(λ_L/r)Δ`, i.e. `ρω²V = p/r` with `p = −λ_L Δ` — the horizontal momentum balance of a fluid. **Correct.**
2. **★ Homogeneous limit `λ_L' = μ' = 0`.** The exact solution is the two-potential Bessel pair
   `φ = a·j_ℓ(k_P r)`, `ψ = b·j_ℓ(k_S r)` with `k_P = ω/c_P`, `k_S = ω/c_S`,
   `c_P = sqrt((λ_L+2μ)/ρ)`, `c_S = sqrt(μ/ρ)`, giving
   `U = a·k_P j_ℓ'(k_P r) + b·L j_ℓ(k_S r)/r` and
   `V = a·j_ℓ(k_P r)/r + b·[ j_ℓ(k_S r)/r + k_S j_ℓ'(k_S r) ]`.
   **This is gate `G0(a)`, and it is the strongest check in the battery: any factor error anywhere in the derived system fails it.**

### §2.2 ★ THE CHANNEL IMPEDANCES AND THE MODULI GRADING — AND THE CANON CONTRADICTION (FLAG-W)

#### (a) The shear channel — canon speaks with one voice

```
mu(r) = G_vac · S ,      c_shear = c_0 · sqrt(S) ,      S = sqrt(1 − A²)
```

Op16, CANONICAL, verbatim at [`common/operators.md:56`](../manuscript/ave-kb/common/operators.md) (`Op16 | Universal Wave Speed | $c_{shear} = c_0\cdot\sqrt{S}$`) and reinforced at [`saturating-modulus-and-backreaction.md:60`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md): *"**SHEAR softens:** $c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection,"*. With `ρ = ρ_bulk` this gives `μ = ρ_bulk c_shear² = G_vac S`. **Unchanged from v2.4, and identical on both branches below — which is exactly why the axial lane never met this fork.**

#### (b) ★ THE WAVE OPERATOR'S LONGITUDINAL SPEED IS `sqrt(10/3)·c`, NOT `sqrt(2)·c` — DERIVED, and it CORRECTS the premise this lane was handed

The lane brief specified *"the bulk speed √2c per port-register"*. **That is the port-register's PORT/impedance-mode column, and the port register itself says it is not the propagating far-field speed.** Verbatim, [`common/port-register.md:49`](../manuscript/ave-kb/common/port-register.md), the channel-3 row:

> *"**$\sqrt2\,c$** ($V_{LONG}$; $K=2G$ magic-angle PORT/impedance mode) | **$\sqrt{10/3}\,c \approx 1.83c$** (isotropic-solid P-wave; the $4G/3$ shear term cannot be dropped for a real far-field wave)"*

and at `:56`:

> *"The **PORT/impedance speed $\sqrt2\,c$** ($Z_{bulk}=\rho c_{bulk}$) governs *reflection at a boundary* (saturation wall, TIR) and *reactive near-field storage*"*

Two-method confirmation from the engine, verbatim at `src/ave/core/constants.py:775-781`:

> *"MODE DISTINCTION (KEEP-BOTH; no value change). V_LONG below is the BULK-SOUND speed v_bulk = √(K/ρ) = √(2G/ρ) = √2·c — the A1-scalar/dilatational port-mode (clm-uu1qbo, cosserat-mass-gap.md); **it DROPS the 4G/3 shear term. It is NOT the solid P-wave**: the full compressional (P) wave is c_L = √((K + 4G/3)/ρ) = √(10/3)·c ≈ 1.83c ... The two are distinct physical longitudinal modes, both retained"*

**The derivation is forced and leaves no freedom.** An isotropic elastic wave operator has exactly two speeds, `sqrt(μ/ρ)` and `sqrt((λ_L+2μ)/ρ)`. There is no third. And `λ_L + 2μ = K + 4μ/3`, so at `K = 2μ`,

```
lambda_L + 2 mu  =  2 mu + 4 mu/3  =  (10/3) mu      =>      c_P = sqrt(10/3) · c_shear
```

which reproduces the port register's own `sqrt(10/3)c` **exactly**, at the cold operating point, from the elastic identity. **The `sqrt2·c` is `Z_bulk/ρ`; it enters this lane ONLY through the reflection statement at the wall and NEVER as a propagation speed in the wave operator. Using it in the operator would be an error, not a fork.**

Frozen: `the polar wave operator carries the two isotropic elastic speeds sqrt(mu/rho) and sqrt((lambda_L + 2 mu)/rho); at the K = 2G operating point the second is sqrt(10/3)*c_shear, which reproduces the port register's own far-field longitudinal speed exactly; the sqrt(2)*c PORT/impedance speed is Z_bulk/rho and enters this lane only through the wall reflection statement, never as a propagation speed`.

**Surfaced, not fixed:** the lane brief's `√2c` specification is corrected here by derivation from canon. **This is recorded as a correction to the brief, not as a defect in the port register**, which draws the distinction correctly and in bold.

#### (c) ★ FLAG-W — CANON GIVES TWO OPPOSITE SIGNS FOR THE BULK MODULUS AT THE SAME WALL

**Both sentences below are canonical, both are about the compressive saturation boundary at `r_sat`, and they are opposite.**

**VOICE 1 — the bulk line VENTS.** [`vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md:31-32`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md), verbatim:

> *"- $c_{bulk} \to 0$ (bulk dilatational speed vanishes at snap / rupture)*
> *- Therefore $Z_{bulk} = \rho_{bulk}\,c_{bulk} \to 0$"*

and at `:39-42`:

> *"$\Gamma_{bulk} = \frac{Z_{bulk,2} - Z_{bulk,1}}{Z_{bulk,2} + Z_{bulk,1}} \to -1 \quad \text{as } Z_{bulk} \to 0$ ... The saturated interior is a **bulk-longitudinal perfect reflector** — the sonic-horizon / pressure-release boundary ($p = 0$ at the wall)"*

Reinforced at [`vol3/claim-quality.md`](../manuscript/ave-kb/vol3/claim-quality.md) (the corrected channel-split bullets): *"likewise $Z_{bulk} \to 0 \Rightarrow \Gamma_{bulk} = -1$ at the dielectric rupture"*.

**VOICE 2 — the bulk line JAMS.** [`vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md:57`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md), verbatim:

> *"- **BULK stiffens:** $D=1/S\to\infty$ at $A\to1$ (the modulus goes rigid, halting the collapse)."*

immediately above the `SHEAR softens` line this lane's `μ(r)` is taken from — **the two lines are three lines apart in the same per-channel sign-lock list, and the same leaf calls that list a "sign-lock"**: *"The per-channel **sign-lock** (INVARIANT-S2) keeps the three channels physically distinct"* (`:54`).

**VOICE 3 — a third leaf flags the conflation as a firewall violation.** [`common/engine-capability-map.md:69`](../manuscript/ave-kb/common/engine-capability-map.md), verbatim:

> *"**Underlying firewall — stiffening vs softening.** The A1 dilatation's *own* wall is the **stiffening** branch ($c_{eff}\to\infty$, the BULK-TRAP, `crystal_engine.py:18-20`). The `bulk_rarefaction_sector` / `cavitation_flow` pocket is the **softening** branch ($c_{bulk}\to0$ at ρ̄_cav) — canon flags it *"a FOURTH object — NOT Γ=−1"* ... **Conflating them is the firewall violation.**"*

**Read plainly and without adjudication: Voice 1 assigns the astrophysical compressive wall the SOFTENING behaviour; Voice 2 assigns the compressive `A → 1` limit the STIFFENING behaviour; Voice 3 says the softening branch belongs to RAREFACTION and that conflating the two is a firewall violation. This lane does not resolve that. It runs both.**

Frozen: `canon carries two opposite bulk-modulus signs at the same r_sat wall -- bulk-impedance-at-saturation-boundary.md:31 (c_bulk -> 0, Z_bulk -> 0, Gamma_bulk = -1) and saturating-modulus-and-backreaction.md:57 (D = 1/S -> infinity, the modulus goes rigid) -- with engine-capability-map.md:69 flagging the conflation as a firewall violation; this lane surfaces the contradiction with all three verbatim citations, repairs no leaf, adjudicates nothing, and runs BOTH branches`.

#### (d) The two frozen branches

Both branches share `μ = G_vac S` and both agree exactly at the cold limit `A → 0` (`K → 2G_vac`, `c_P → sqrt(10/3) c₀`). **They differ only under load, which is the whole content of the fork.**

| | **BRANCH-SOFT** (Voice 1) | **BRANCH-STIFF** (Voice 2) |
|---|---|---|
| bulk modulus | `K = 2 μ = 2 G_vac S` | `K = 2 G_vac / S` |
| Lamé `λ_L = K − 2μ/3` | `(4/3) G_vac S` | `2 G_vac/S − (2/3) G_vac S` |
| `λ_L + 2μ` | `(10/3) G_vac S` | `2 G_vac/S + (4/3) G_vac S` |
| `c_P` | `sqrt(10/3) · c₀ sqrt(S)` → `0` | `→ ∞` |
| `Z_bulk` at the wall | `→ 0` | `→ ∞` |
| `Γ_bulk` at the wall | `−1` | `+1` |
| Poisson ratio at the wall | stays `2/7` | `→ 1/2` (incompressible) |
| cold limit `A → 0` | `K = 2G_vac`, `c_P = sqrt(10/3)c₀` | `K = 2G_vac`, `c_P = sqrt(10/3)c₀` |

Frozen: `BRANCH-SOFT sets K = 2*mu = 2*G_vac*S and BRANCH-STIFF sets K = 2*G_vac/S; both carry the identical shear law mu = G_vac*S and both reduce to K = 2*G_vac and c_P = sqrt(10/3)*c_0 at the cold limit A -> 0; neither is preferred and both are run`.

### §2.3 ★ FLAG-4 DISCHARGE — WHICH `ρ` THE SERIES-`L` CARRIES, NAMED FROM CANON

**FLAG-4 has two parts and they have different answers. Conflating them is what left it open.**

#### (a) THE NAMING GAP IS CLOSED — canon does name the density, in a different leaf

`vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` with an unnamed `ρ`; that is the #814 CF-7 gap. **The symbol is named at two other canonical sites, and they agree.**

- [`vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md`](../manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md), the cold-lattice assignments table, verbatim: *"Shear / GW | $Z_{\mathrm{shear}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$"* and *"Bulk-longitudinal | $Z_{\mathrm{bulk}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}$"*.
- `src/ave/core/constants.py:766`, verbatim: *"# 3D continuum shear modulus  G_vac = ρ_bulk · c²"* with `G_VAC: float = RHO_BULK * C_0**2`, and `:781` `V_LONG: float = np.sqrt(2.0 * G_VAC / RHO_BULK)`.

**Two-method receipt, and the answer is unambiguous: canon carries ONE lattice mass density, `ρ_bulk` (`RHO_BULK`), and BOTH channels' series-`L` is that same density.** The subscript "bulk" names the *lattice*, not the *channel* — the shear channel's impedance is written with it explicitly. **The #814 CF-7 naming gap is therefore a gap in ONE leaf, not in canon; it is discharged by citation here and is NOT repaired in that leaf by this lane.**

Frozen: `canon names ONE lattice mass density rho_bulk and assigns it to BOTH channels' series-L, verbatim at vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md (Z_shear = rho_bulk c_shear and Z_bulk = rho_bulk c_bulk) and at src/ave/core/constants.py:766,781; the #814 CF-7 naming gap at vol3/claim-quality.md:122 is discharged by citation and that leaf is byte-untouched by this lane`.

#### (b) THE GRADING IS GENUINELY UNDER-DETERMINED — and BOTH candidates are run

Canon names the symbol but not its radial dependence under load. Two readings exist in-corpus:

- **RHO-A (`ρ(r) = ρ_bulk`, the cold lattice inertia).** The leading reading, v2.4's `I5`, and the one every predecessor lane consumed.
- **RHO-B (`ρ_eff = ρ_bulk / S³`).** FORK-3(b), fenced by v2.4's `X6` and never run. Canonical at [`vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md) via `saturating-modulus-and-backreaction.md:73`, verbatim: *"$\rho_{\text{eff}}=\rho_0/S_{\text{topo}}^3$ with $S_{\text{topo}}=\sqrt{1-\varepsilon_{11}^2}\to0$"*. **Note that `S_topo = sqrt(1 − ε_11²)` is `S(A)` identically, since `A = ε_11`** — so FORK-3(b) is exactly `ρ = ρ_bulk/S³` in this lane's variables.

**Consequence, derived in advance:** under RHO-B the shear speed becomes `c_shear = sqrt(μ/ρ) = c₀ S²` rather than `c₀ sqrt(S)`, which changes the ORDER of the wall's singularity — the `A = 1 − η²` substitution that makes `η = 0` an ordinary point for RHO-A is **not** guaranteed to do so for RHO-B. **That is pre-registered as a reachable outcome, not discovered afterwards:** `BIN-PF-WALLSING` (§7.1) fires if the wall's indicial analysis admits no regular solution, and it is an honest result rather than a failure.

Frozen: `RHO-A is rho(r) = rho_bulk and RHO-B is rho_eff(r) = rho_bulk/S^3 (FORK-3(b), fenced by v2.4's X6 and run here for the first time); under RHO-B the shear speed becomes c_0*S^2 and the wall's singularity order changes, so a no-regular-solution outcome at the wall is PRE-REGISTERED as BIN-PF-WALLSING and is an honest result rather than an instrument failure`.

### §2.4 ★ FLAG-3 DISCHARGE — WHAT THE CANON PROFILE ACTUALLY IMPLIES FOR THE EXTERIOR PORT, PER CHANNEL

**FLAG-3 asked whether the reflectionless Regime-I port is an assumption. For this lane it is DERIVED, per channel, from the profile — and the derivation says something sharper than "assumed".**

The profile is `A = r_sat/r`, so

```
S = sqrt(1 − A²) = 1 − r_sat²/(2r²) + O(r^-4)
```

**Every modulus's deviation from its cold value is `O(1/r²)`. There is NO `1/r` term.** Consequently:

1. **The graded exterior is a SHORT-RANGE perturbation of a homogeneous medium in BOTH channels.** A `1/r²` modulus tail enters the radial wave equation exactly like a shift of the centrifugal term; it produces **no** logarithmic phase (unlike the Schwarzschild tortoise coordinate, whose `1/r` tail does), and it produces **no** reflected wave at any order in `1/r` — the reflection from a smooth short-range tail is beyond all orders in `1/(k r)`. **The `exp(iΩ/A)` plane-wave factoring is therefore EXACT to all polynomial orders, in both channels, and that is a property of the canonical profile rather than an assumption about it.**
2. **The two channels have DIFFERENT far-field speeds, so they have different phase rates.** `k_S r = Ω/A` and `k_P r = Ω/(A·sqrt(10/3)) = sqrt(3/10)·Ω/A`. **This is the structural difference from the axial problem and it is handled explicitly in §2.6.**
3. **The channels DECOUPLE asymptotically.** The coupling terms in §2.1 carry `λ_L'`, `μ'` and `1/r²`; with `μ' = O(1/r³)` the coupling decays faster than the `1/r` wave amplitude. **So a per-channel outgoing condition is legitimate, and the legitimacy is derived rather than assumed.**
4. **BRANCH-STIFF changes NONE of this in the far field.** `K = 2G_vac/S = 2G_vac(1 + r_sat²/(2r²) + …)` — the same `O(1/r²)` short-range form with the opposite sign. **The port is reflectionless on both branches; the branches differ only at the wall.**

Frozen: `the canonical profile's modulus deviation is O(1/r^2) with no 1/r term, so the graded exterior is a SHORT-RANGE perturbation in both channels, produces no logarithmic phase and no reflection at any polynomial order in 1/(k r), and the channels decouple asymptotically because the coupling carries the modulus gradients; the reflectionless Regime-I port is therefore DERIVED from the profile per channel rather than assumed, on BOTH branches`.

**What this discharge does NOT cover, stated plainly:** it covers the port implied by **this profile continued to infinity**. It does not and cannot exclude a far-field reflector introduced by physics outside this profile (a cosmological boundary, a second saturation surface, a Cosserat-channel structure). **FLAG-3 is discharged for the profile, not for the universe**, and the residual is recorded in §9.

### §2.5 THE WALL BOUNDARY CONDITION — DERIVED PER BRANCH, NOT ASSUMED TO SHORT TOGETHER

The two channel-wise reflection statements are **not** assumed to combine. Each is converted into a condition on the computational variable and the conversion is derived.

Near the wall, with `A = 1 − η²`:

```
S² = 1 − A² = η²(2 − η²)  =>  S = η·u ,  u = sqrt(2 − η²) ,  S → sqrt(2)·η
d/dr = (A²/(2 η r_sat)) d/dη          [so a 1/η is generated by every radial derivative]
```

**BRANCH-SOFT.** Every modulus is `∝ S ∝ η`. The two tractions are

```
R  ≡ T_rr  = (λ_L + 2μ) U' + λ_L (2U − L V)/r
S_t ≡ T_rθ = μ (V' − V/r + U/r)
```

With `μ, λ_L, (λ_L+2μ) all ∝ η` and `U' ∝ (1/η)·dU/dη`, the products `(λ_L+2μ)U'` and `μV'` are **finite**, while every un-differentiated term is `O(η) → 0`. Hence, exactly:

```
R(r_sat) = 0     <=>    dU/dη|_{η=0} = 0
S_t(r_sat) = 0   <=>    dV/dη|_{η=0} = 0
```

**This is the exact analogue of the axial case**, where `T = μ(W' − W/r) → 0` reduces to `dW/dη|₀ = 0` — and it is derived here for each channel separately and only then combined. `Γ_shear = −1` gives the second row; `Γ_bulk = −1` (Voice 1) gives the first. **Together they are the vanishing of the FULL traction vector at `r_sat` — a free surface in both channels.** Because the factoring `E = A·exp(iΩ(1/A + κA))` has `dA/dη = −2η = 0` at `η = 0`, both rows carry through to the factored variables unchanged: `du/dη|₀ = 0` and `dv/dη|₀ = 0`.

**BRANCH-STIFF.** `μ ∝ η` still, so the shear row is unchanged: `dv/dη|₀ = 0`. But `λ_L, (λ_L+2μ) ∝ 1/η`, so `R` is finite only if the dilatation vanishes at the wall:

```
Δ(r_sat) = U' + (2U − L V)/r  =  0        [the incompressibility forced by K → ∞]
```

**This is the substrate-native reading of `Γ_bulk = +1` at a GRADED impedance divergence**: the wall is not a second medium with `Z → ∞`, it is a point where the medium's own bulk impedance diverges, so the compressional wave's local wavenumber `k_P = ω/c_P → 0` and the wave is expelled rather than absorbed. **The rigid-wall content is `Δ = 0`, not `U = 0`.** Frozen with an explicit failure slot: the driver computes the indicial exponents at `η = 0` on this branch and reports them; if the wall admits no regular solution the outcome is `BIN-PF-WALLSING`, which is a **pre-registered honest result routing to the wall-BC derivation**, not a defect.

Frozen: `the wall rows are derived per channel and are not assumed to combine; on BRANCH-SOFT the full traction vector vanishes and the rows are exactly du/deta = 0 and dv/deta = 0 at eta = 0; on BRANCH-STIFF the shear row is unchanged and the bulk row is the incompressibility Delta(r_sat) = 0 forced by K -> infinity, whose regularity is computed by an indicial analysis reported by the driver, with BIN-PF-WALLSING pre-registered as the honest outcome if no regular solution exists`.

### §2.6 THE COMPACTIFIED, OUTGOING-FACTORED TWO-FIELD OPERATOR — and the multi-speed disclosure

Set `c₀ = ρ_bulk = G_vac = 1`; `A ≡ r_sat/r ∈ (0,1]`; `Ω ≡ ω·r_sat/c₀`. Factor the outgoing wave out analytically with a **single shared factor**, the SAME one v2.4 uses:

```
(U, V)  =  A · exp( i Ω (1/A + κ A) ) · (u, v)
```

**Why a SINGLE factor and not one per channel — DERIVED, and it is the key structural decision of this instrument.**

The four asymptotic branches behave, as `A → 0` with `Im Ω < 0`, like

| branch | growth | after division by `E_S = exp(iΩ/A)` |
|---|---|---|
| shear-OUT | `exp(\|Im Ω\|/A)` | `O(1)` — **bounded, retained** |
| bulk-OUT | `exp(sqrt(3/10)·\|Im Ω\|/A)` | `exp(−(1 − sqrt(3/10))·\|Im Ω\|/A) → 0` — **bounded, retained** |
| shear-IN | `exp(−\|Im Ω\|/A)` | `exp(−2\|Im Ω\|/A)`… **inverted**: `exp(+2\|Im Ω\|/A)` — **unbounded, excluded** |
| bulk-IN | `exp(−sqrt(3/10)\|Im Ω\|/A)` | `exp(+(1 + sqrt(3/10))\|Im Ω\|/A)` — **unbounded, excluded** |

**So dividing BOTH fields by the SHEAR channel's outgoing factor retains exactly the two-dimensional outgoing subspace and excludes both ingoing branches from the discretization's function space. That is the correct and complete radiation condition, and no boundary condition at infinity is imposed.** The alternative — a per-channel factor — is **wrong** and is rejected by derivation, not by preference: dividing `U` by the bulk factor leaves the shear content of `U` growing like `exp(+(1 − sqrt(3/10))|Im Ω|/A)`, i.e. unbounded.

**★ THE DISCLOSURE THIS BUYS, stated before the run.** The retained bulk-outgoing content is suppressed by `exp(−(1 − sqrt(3/10))·|Im Ω|/A)`, a **beyond-all-orders** factor: smooth at `A = 0` with every derivative vanishing, but not analytic. Two consequences are pre-registered:

1. **The convergence law may carry a floor or a slower-than-axial rate.** `G2b` gates the SHAPE of the law and a decay floor, and does **not** import the axial lane's fitted `c` (§4.5).
2. **★ The instrument could in principle return a mode with negligible dilatation — i.e. a disguised shear mode dressed as a polar one.** This is pre-registered as a **gated** quantity, `G-P` (§5), which measures the certified eigenfunction's dilatation content against a frozen floor. **A polar certification with negligible dilatation content is NOT a polar certification and the gate fails it.**

Frozen: `both fields are divided by the SINGLE shear-channel outgoing factor A*exp(i*Omega*(1/A + kappa*A)); this retains exactly the two-dimensional outgoing subspace and excludes both ingoing branches, a per-channel factoring is rejected by derivation because it leaves the cross-channel content unbounded, and the resulting beyond-all-orders suppression of the bulk-outgoing content by exp(-(1 - sqrt(3/10))*abs(Im Omega)/A) is disclosed in advance with its two pre-registered consequences`.

The wall terminus is reached exactly by `A = 1 − η²`, `η ∈ [0,1]`. Writing the `η`-form of the two-field system as a block operator on Chebyshev–Gauss–Lobatto nodes, the discrete object is a **quadratic matrix pencil** `M(Ω) = M0 + Ω·M1 + Ω²·M2` — quadratic because `ρω²` is the only intrinsically-`Ω²` term and the factoring contributes at most `Ω²` through `(E'/E)²`. **The v2.4 seeding path (double-precision companion linearization → nearest eigenvalue → mp secant polish) therefore carries over unchanged, and no frequency scan, no winding and no contour is needed anywhere.**

---

## §3 — IMPORT LEDGER (every number the instrument consumes, tagged; `substrate-first-for-numbers`)

| # | Input | Value / form | Class | Source |
|---|---|---|---|---|
| **J1** | Saturation-wall radius | `r_sat = 7GM/c² = 7 M_g`, `x_sat = 7` | **`[canon]`** — form-derived, **VALUE rides the GR-imported `ν_vac`** | `vol3/claim-quality.md:121`; provenance `one-seventh-impedance-projection.md:18` |
| **J2** | Saturation amplitude profile | `A(r) = ε_11/ε_yield = r_sat/r`, `ε_yield = 1` | **`[canon]`** | `saturating-modulus-and-backreaction.md:51` |
| **J3** | Ax-4 kernel | `S(A) = (1 − A²)^{1/2}` | **`[canon]` — Axiom 4** | `saturating-modulus-and-backreaction.md:52` |
| **J4** | Shear modulus | `μ(r) = G_vac·S` (Op16, `c_shear = c₀ S^{1/2}`) | **`[canon]`** | `common/operators.md:56`; `saturating-modulus-and-backreaction.md:60` |
| **J5 ★** | Bulk modulus under load | **FORK, both run:** `K = 2G_vac·S` (BRANCH-SOFT) or `K = 2G_vac/S` (BRANCH-STIFF) | **`[canon, CONTRADICTORY — FLAG-W]`** — neither preferred, both run | `bulk-impedance-at-saturation-boundary.md:31`; `saturating-modulus-and-backreaction.md:57`; `engine-capability-map.md:69` |
| **J6** | Cold bulk operating point | `K = 2G_vac`, hence `λ_L + 2μ = (10/3)G_vac` and `c_P = sqrt(10/3)c₀` | **`[canon]` — VALUE GR-IMPORTED via `ν_vac = 2/7` (PR #261/#506)** | `constants.py:775-781`; `common/port-register.md:49` |
| **J7 ★** | Inertia | **FORK, both run:** `ρ = ρ_bulk` (RHO-A) or `ρ_eff = ρ_bulk/S³` (RHO-B, FORK-3(b)) | **`[canon, UNDER-DETERMINED grading — FLAG-4(b)]`** | `three-channel-impedances.md`; `saturating-modulus-and-backreaction.md:73` |
| **J8** | Shear wall condition | `T_rθ(r_sat) = 0` (`Z_shear → 0`, `Γ_shear = −1`) | **`[canon]`** | `vol3/claim-quality.md:123` |
| **J9 ★** | Bulk wall condition | **branch-derived (§2.5):** `T_rr(r_sat) = 0` (SOFT) or `Δ(r_sat) = 0` (STIFF) | **`[DERIVED here from J5 + the graded-impedance limit]`** | §2.5 |
| **J10** | Outer boundary condition | outgoing radiation into the cold matched lattice, per channel | **`[canon]` — Regime-I radiative port, Ax-3-licensed. DERIVED from the profile in §2.4, no longer assumed** | §2.4 |
| **J11** | Angular index | `ℓ = 2` (quadrupole) | **`[canon, INPUT not derived]`** | §1.3 Y1 |
| **J12** | Unit choice | `M_g = 1`, `c₀ = 1`, `ρ_bulk = 1`, `G_vac = 1` | **`[dimensionless by construction]`** | this lane |
| **J13** | `ν_vac = 2/7` | imported read-only from `ave.core.constants.N_NU`; used ONLY to form the reported `r_eff` comparator | **`[canon]` — VALUE GR-IMPORTED** | `src/ave/core/constants.py:397` |
| **J14** | GR cold comparator | `ω_R M = 0.37367`, `ω_I M = 0.08896` at `a_* = 0`, read **programmatically** | **`[GR-IMPORTED comparator — the frozen C-comparator, inherited unchanged from v1/v2.1/v2.2/v2.4]`** | `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51` |
| **J15 ★** | **The certified AXIAL root** | `Ω_axial`, `ω_R M_g (axial)`, `Q_axial` — read **PROGRAMMATICALLY** from the merged in-repo JSON | **`[IN-REPO CERTIFIED PRIOR-LANE RESULT — the BIN-P2 comparator and the G-C(b) reduction target; on `origin/main`, blob-pinned]`** | `research/drivers/coldq_pole_v2p4_root_results.json` @ blob `207f9e7b6a3f3bcfd970f03c36cc51a5dcba2b95` |
| **J16 ★** | **v2.4's measured convergence-law parameters** | the axial lane's fitted `c` and residual, and the two in-repo NON-CONVERGENT `c` values (its artifact fit and its FT-2b stagnation fit) | **`[IN-REPO MEASURED — used ONLY to DERIVE this lane's G2b decay floor with headroom; enters no bin, no comparator and no tolerance as a value]`** | `coldq_pole_v2p4_root_results.json`, keys `gates.G2b`, `diagnostics.artifact_convergence`, `self_tests.FT_2b` |
| **J17** | Instrument numerics | Chebyshev order `n`, gauge `κ`, mp precision, polish tolerance/cap, dedupe radius, isolation radius | **`[ENGINEERING CHOICE — tagged, frozen in §4]`** | this lane |

**R8 audit rule (frozen).** `every number the instrument consumes appears on this ledger with its tag; no SM/GR convention default enters anywhere, and in particular no Regge-Wheeler potential, no Zerilli potential, no Chandrasekhar-Detweiler transformation and no GR polar master equation is used as an input, a seed, a comparator or a check`.

**★ Ledger discipline note on J16, stated at freeze.** v2.4's fitted `c = 6.216374478994577` is **not** imported as a band for this lane. Only the **non-convergent** `c` values are used, and only to place a **floor** with headroom (§4.5). **A different operator has no obligation to share a convergence rate, and importing one would be exactly the I22 defect v2.4's own result doc routed to its successor.**

---

## §4 — THE METHOD AND ITS FROZEN NUMERICS

### §4.1 The method (frozen)

Compactified hyperboloidal Chebyshev spectral discretization of the **two-field** coupled system of §2.1, in the Axiom-4 amplitude coordinate `A = r_sat/r` under `A = 1 − η²`, with the single shared outgoing factor of §2.6 divided out in closed form, the branch-derived wall rows of §2.5 imposed exactly as the two `η = 0` rows, **no** boundary condition imposed at infinity, root extraction by extended-precision determinant polish seeded from the double-precision linearized pencil, and eigenfunction extraction by extended-precision inverse iteration.

**The operator's coefficient functions are built SYMBOLICALLY at run time** from §2.1 + the branch grading + the change of variables + the factoring, then evaluated numerically. Frozen: `the operator coefficients are constructed symbolically at run time from the derived radial system, the branch grading, the change of variables and the factoring, and are then evaluated numerically; no coefficient is hand-transcribed, and the symbolic construction is re-verified by gate G0 rather than trusted`.

### §4.2 Frozen numerics (every parameter fixed here, before any code)

```
N_PRIMARY        = 48                       (per field; the block operator is 2(n+1) square)
N_LADDER         = (32, 48, 64, 80)         full ladder, swept by G4(b), G5, FT-5
N_LADDER_G2      = (48, 64, 80)             the G2 certification ladder
HGAUGE_PRIMARY   = 0.0                      kappa
HGAUGE_SET       = (-0.25, 0.0, +0.25)
DPS              = 50
DPS_HIGH         = 80
DPS_FT4          = 20
POLISH_TOL_EXP   = 38
POLISH_ITERS     = 60
INVIT_ROUNDS     = 4
DEDUPE_REL       = 1e-6
R_ISO            = 0.5                      (derived in §4.4)
X_SAT            = 7.0
X_SAT_SET        = (5.0, 7.0, 11.0)
ELL              = 2
N_UNDER          = 8                        under-resolved order, FT-2 / FT-4(b)
DILATATION_FLOOR = 1e-3                     G-P, derived in §4.7
RUNTIME_BUDGET_S = 7200.0
```

**Why the ladder is `(32, 48, 64, 80)` and the certification ladder is `(48, 64, 80)`.** The block operator is `2(n+1)` square, so the mp determinant cost scales as `(2n)³` — eight times the axial lane's at the same `n`. The top rung is placed at `80` rather than `96` for that reason, and the placement is an **engineering** choice, tagged. `n = 32` is **retained** as a gated rung of `G4(b)`, `G5` and `FT-5`, and as a **mandatory non-gated diagnostic row of G2** — the same treatment v2.4 gave it, for the same reason, and nothing about it is hidden.

Frozen: `no gate, tolerance, band, frozen numeric parameter, bin boundary or method element in sections 4, 5, 6 and 7 may be changed after any gate result is seen; if this instrument fails certification the lane reports SOLVER-NOT-CERTIFIED, does NOT adjudicate any physics bin, and routes to a successor with a new version number`.

### §4.3 The configuration matrix — frozen, with the primary named in advance

| tag | branch | inertia | role |
|---|---|---|---|
| **`CFG-SOFT-A`** | BRANCH-SOFT | RHO-A | **CO-PRIMARY** |
| **`CFG-STIFF-A`** | BRANCH-STIFF | RHO-A | **CO-PRIMARY** |
| `CFG-SOFT-B` | BRANCH-SOFT | RHO-B | frozen SENSITIVITY (FORK-3(b), first run) |

Frozen: `the two FLAG-W branches at RHO-A are CO-PRIMARY and neither is preferred; CFG-SOFT-B is a frozen disclosed sensitivity; the certification gates are run on every configuration that produces a root, and a configuration that fails certification is reported SOLVER-NOT-CERTIFIED for that configuration and has NO physics bin adjudicated`.

**★ CO-PRIMARY consequence, frozen:** `if the two co-primary configurations return different bin verdicts on any bin, that bin is reported as BRANCH-DEPENDENT, both verdicts are printed, and the bin is routed to Grant as an open adjudication rather than collapsed to one number`.

**`CFG-STIFF-B` is deliberately NOT run.** Frozen: `CFG-STIFF-B (BRANCH-STIFF with RHO-B) is NOT run in this lane; it compounds two independent under-determinations, and a result from it could not be attributed to either`.

### §4.4 The G5 isolation radius — carried over unchanged, with its receipts recomputed here

`R_iso = 0.5` is carried from v2.4 unchanged. Its four receipts are **recomputed by the driver and shipped**, not asserted: the GR overtone gap `|Ω_GR(n=0) − Ω_GR(n=1)|` against `R_iso`; `R_iso/|Ω|`; `R_iso/(DEDUPE_REL·|Ω|)`; and the axial-to-polar separation against `R_iso`. **The fourth is new and is this lane's own:** if the polar root sits within `R_iso` of the axial root, the isolation measurement cannot distinguish them and the driver reports that explicitly rather than silently counting two eigenvalues as one.

### §4.5 ★ G2b — the convergence law, with bands DERIVED FROM IN-REPO EVIDENCE ONLY

**The law.** `E(n) = C·exp(−c·sqrt(n))`, fitted as `ln e(n) = lnC − c·sqrt(n)` by ordinary least squares over the certification rungs `{48, 64}` against the `n = 80` reference. Under this law the successive-error ratio **declines with `n` by construction**; the ratios are reported and are **NOT** gated on.

**The two gated quantities, and why the `c`-band is NOT the axial lane's.**

- **residual floor `0.40`.** Carried from v2.4, where it was derived as `4.7143 ×` the worst measured residual on an in-repo blob. Re-used here as a **shape** criterion.
- **decay floor `c ≥ 1.0`, and NO upper edge.** Derived from **in-repo NON-convergent** measurements only: v2.4's shipped `diagnostics.artifact_convergence.c` (a pseudo-pole; the fit does not decay) and `self_tests.FT_2b.c` (the stagnation mutation). The floor `1.0` sits **above both** with headroom, and the driver **computes and ships that headroom ratio** rather than this document asserting it. **No upper edge is frozen**, because §2.6's beyond-all-orders disclosure predicts this operator may converge at a different rate from the axial one and an imported upper edge would gate on a number from a different operator.

Frozen: `G2b fits ln e(n) = lnC - c*sqrt(n) by ordinary least squares over the G2 certification rungs against the finest rung, and requires BOTH that the maximum absolute residual in ln e is <= 0.40 AND that the fitted c is >= 1.0; there is deliberately NO upper edge on c, because the beyond-all-orders disclosure of section 2.6 predicts this operator may converge at a rate the axial operator does not share and an imported upper edge would gate on a number from a different operator; the decay floor 1.0 is derived from the two IN-REPO non-convergent c values shipped by v2.4 and the headroom ratio is computed and shipped by this driver rather than asserted here`.

### §4.6 The FORK-3(b) sensitivity, and what it can and cannot settle

`CFG-SOFT-B` runs `ρ_eff = ρ_bulk/S³` for the first time in the arc. Frozen: `CFG-SOFT-B discharges the RUN half of v2.4's FLAG-4 routing; it does NOT adjudicate which inertia canon means, it does NOT repair the naming leaf, and if it returns a root that root is reported alongside the RHO-A roots as a SENSITIVITY, never substituted for them`.

### §4.7 ★ G-P — the dilatation floor, DERIVED

The gate must separate "a polar mode" from "a shear mode the polar solver happened to find". The measured quantity is the **window-integrated dilatation-to-shear energy ratio** of the certified eigenfunction,

```
D_ratio  =  Integral[ K(r) |Δ|² r² dr ]  /  Integral[ mu(r) ( |V' - V/r + U/r|² + ... ) r² dr ]
```

over the frozen window `r/r_sat ∈ [1.0, 2.0]` (**byte-identical to the axial lane's BIN-3 window, and not widened**). Frozen floor `1e-3`. **Derivation of the floor:** the axial mode has `Δ ≡ 0` **identically and analytically**, so its `D_ratio` is `0` up to round-off, which in `dps = 50` arithmetic is `O(1e-45)`. A floor of `1e-3` therefore sits **42 orders of magnitude** above the analytic zero of the object it must exclude, while being small enough not to prejudge how much dilatation a genuine polar mode carries. **The driver measures the axial instantiation's own `D_ratio` and ships it as the fireability receipt.**

Frozen: `G-P requires the certified polar eigenfunction's window-integrated dilatation-to-shear energy ratio to be >= 1e-3 over the frozen window r/r_sat in [1.0, 2.0]; the floor is derived as sitting far above the analytic zero of the axial mode, whose dilatation vanishes identically, and the axial instantiation's own measured ratio is shipped as the fireability receipt; a polar certification with a dilatation ratio below the floor is NOT a polar certification and the gate fails it`.

### §4.8 ★ THE GATING NUMBER CHECK — every accumulated checker lesson, applied at freeze

Frozen: `this lane's gating number check implements, from the first commit: (i) a MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, machine-enforced at BOTH the configuration end and the document end; (ii) PER-SITE rather than global dedup, so every occurrence of a numeral is checked and the reported counts describe SITES; (iii) LIST-VALUED REGISTRATION, so a bracketed count vector is matched elementwise against a shipped JSON list rather than decomposed into single-digit tokens; (iv) a NEWLINE-EXCLUDING token pattern, so a fenced code block cannot be consumed as one span and invert back-tick pairing for the remainder of the document; (v) a COMPLETENESS GUARD making any registered key the document never exercises a hard configuration FAIL; and (vi) a DIGEST CLASSIFIER, so run digests are checked against the shipped JSON as tokens in their own class rather than skipped by a numeral regex that never matched them`.

Frozen: `the gating number check scans the RESULT DOC only; no claim is made anywhere in this lane that this prereg is machine-checked`.

Frozen: `machine-dependent values -- the runtime seconds -- are NON-REGISTRABLE by configuration guard and are written in the result doc WITHOUT back-ticks, so that an honest re-run on another machine cannot fail the gate`.

### §4.9 The G9 reporting repair, executing a routed successor instruction

v2.4's merged result doc routed an explicit instruction to its successor, verbatim at `research/2026-08-03_coldq-pole-v2.4-root_result.md:334`: *"**The successor's driver MUST NOT EMIT a `pass` field for `G9` at all.** It should ship the digest and the note, and leave the verdict to the external two-run diff, so that the only way to obtain a G9 verdict is to actually perform the comparison."*

Frozen: `this driver emits NO pass field for G9; it ships the digest and the note only, the certification tally cannot read a G9 pass flag because none exists, and G9's verdict is obtained solely by the external two-run diff recorded in the result doc`.

---

## §5 — THE SOLVER-CERTIFICATION GATES, with FROZEN numeric tolerances

**Certification means: ALL gates below PASS and ALL fireability self-tests of §6 FIRE, for the configuration in question.** There is no partial and no scoped certification: per configuration, `SOLVER-CERTIFIED` or `SOLVER-NOT-CERTIFIED`.

| gate | what it certifies | frozen criterion |
|---|---|---|
| **G0(a)** ★ | **the derived system is right** — the un-factored graded system evaluated on the EXACT homogeneous-medium two-potential Bessel solution | max relative residual `≤ 1e-12`, in mp |
| **G0(b)** | the change of variables — the `η`-form operator reproduces the `r`-form operator applied to a manufactured smooth field | `≤ 1e-12` |
| **G0(c)** ★ | the symbolic derivation is re-executed for `ℓ ∈ {2, 3, 4}`, `θ`-separability re-checked, and the affine-in-`L` three-point residual re-checked | separability residual **exactly** `0` and affine residual **exactly** `0` |
| **G1** | residual of the certified eigenvector at the certified root, mp, `dps = 50` | `≤ 1e-20` |
| **G2** | `n`-independence over the certification ladder `{48, 64, 80}` | max pairwise relative separation `≤ 1e-8` |
| **G2b** ★ | the root-exponential convergence law | `max\|resid\| ≤ 0.40` **and** `c ≥ 1.0` (no upper edge — §4.5) |
| **G3** | hyperboloidal-gauge independence, `κ ∈ {−0.25, 0, +0.25}` | `≤ 1e-10` |
| **G4** | (a) precision `dps 50` vs `80`; (b) double pencil vs mp at every FULL-ladder order | `≤ 1e-25` / `≤ 1e-5` |
| **G5** | **ISOLATION** — pencil-eigenvalue count within `R_iso = 0.5` at every FULL-ladder order | exactly `1` |
| **G-C(a)** ★ | **REDUCTION, operator level** — this lane's assembler, instantiated on the toroidal branch, equals v2.4's certified operator entry-wise | `≤ 1e-40`, in mp |
| **G-C(b)** ★ | **REDUCTION, root level** — that instantiation's polished root equals the certified axial root | `≤ 1e-10` relative |
| **G-C(c)** ★ | **COUPLING NON-VACUITY** — with the inter-channel coupling zeroed, the polar root MOVES | `≥ 1e-6` relative |
| **G-P** ★ | **the mode is actually polar** — window-integrated dilatation-to-shear energy ratio | `≥ 1e-3` (§4.7) |
| **G8** | `x_sat` invariance at the root, mp end-to-end, over `x_sat ∈ {5, 7, 11}` | `≤ 1e-9` |
| **G9** | determinism | **EXTERNAL ONLY** — the driver emits NO `pass` field (§4.9) |
| **G10** | Ax-3 (a) operator reality; (b) conjugate-mirror symmetry | `≤ 1e-40` / `≤ 1e-20` |

**★ THE THREE GATES THAT DO NOT EXIST IN v2.4, and what each buys.**

- **`G0(a)`** is the gate that makes a newly-derived operator trustworthy. The axial lane inherited an operator three lanes deep; this lane derived one this morning. **A manufactured-solution identity against the exact Bessel solution of the homogeneous limit is the only check that can catch a factor error in a freshly-derived coupled system, and it is placed first for that reason.**
- **`G-C`** is the reduction control. `G-C(a)` is an **operator-level identity against a certified predecessor**, which is strictly stronger than reproducing a number: it proves the new assembler is the old one plus coupling, entry by entry. Frozen: `G-C(a) imports research/drivers/coldq_pole_v2p4_root.py READ-ONLY as a comparison object; that file is executed as an imported module and is BYTE-UNTOUCHED, and the comparison is an operator identity rather than a value agreement`.
- **`G-P`** is the gate that stops this lane from certifying a shear mode and calling it polar. **Given §2.6's beyond-all-orders disclosure, this is the failure mode this instrument is most exposed to, and it is gated rather than hoped about.**

**★ THERE IS NO `G6` IN THIS LANE, AND THAT IS DISCLOSED RATHER THAN DISGUISED.** v2.4's `G6` gated against v1's different-in-kind instrument. **No second polar instrument exists anywhere in this repository**, so there is nothing to gate against and this lane invents nothing to fill the slot. Frozen: `this lane has NO two-instrument agreement gate because no second polar instrument exists; G-C(b)'s reproduction of the certified axial root is a REGRESSION CONTROL on the shared machinery and is NOT a two-instrument agreement on any polar quantity, and no polar number in this lane carries cross-instrument corroboration of any kind`.

### Certification classes (exhaustive, frozen)

- **`SOLVER-CERTIFIED`** — all gates PASS, all self-tests FIRE, for that configuration. Its physics bins are adjudicated.
- **`SOLVER-NOT-CERTIFIED`** — anything else. **No physics bin is adjudicated for that configuration, at any precedence level.**

Frozen: `a gate that cannot fail is not a gate; if any self-test fails to fire, the configuration is SOLVER-NOT-CERTIFIED regardless of how many gates passed`.

---

## §6 — GATE-FIREABILITY SELF-TESTS — each MUST FIRE

| self-test | targets | mutation | frozen threshold |
|---|---|---|---|
| **FT-0(a)** | G0(a) | the `(λ_L + μ)` coupling coefficient in the tangential equation scaled by `(1 + 1e-9)` | residual `≥ 1e-12` |
| **FT-0(b)** | G0(b) | the chain-rule factor `A²/(2ηr_sat)` replaced by `A²/(2ηr_sat)·(1 + 1e-9)` | `≥ 1e-12` |
| **FT-0(c)** | G0(c) | the derived radial equation's `L`-coefficient perturbed symbolically | affine residual `≠ 0` |
| **FT-1** | G1 | residual evaluated at `Ω*(1 + 1e-10)` | `≥ 1e-15` |
| **FT-2** | G2 | under-resolved order `n = 8` | `≥ 1e-6` |
| **FT-2b** | G2b | STAGNATION: `+1e-12` added to every non-reference rung | fitted `c` must fall **below** `1.0` |
| **FT-3** | G3 | `κ` carried into the first-derivative coefficient but omitted from the `Ω²` coefficient | `≥ 1e-6` |
| **FT-4** | G4 | (a) `dps = 20`; (b) double pencil at `n = 8` vs mp at `n = 48` | `≥ 1e-25` / `≥ 1e-6` |
| **FT-5** | G5 | isolation measured centred on the **axial** root instead of the polar one | count `≠ 1` at ≥ 1 order, **or** the polished root drifts by `> 1e-8` |
| **FT-C** ★ | G-C | the toroidal instantiation built with the **spin-1** `ℓ(ℓ+1)` stored-energy weighting in place of the spin-2 `(ℓ−1)(ℓ+2)` | operator identity `≥ 1e-40` **and** root separation `≥ 1e-3` |
| **FT-P** ★ | G-P | the dilatation ratio measured on the **axial** instantiation, whose dilatation vanishes analytically | measured ratio `< 1e-3`, i.e. the gate would FAIL there |
| **FT-8** | G8 | `A → A·(1 + 1e-6·(x_sat − 7)/7)` | `≥ 1e-9` |
| **FT-9** | G9 | one gate value perturbed `1e-15` in a copy, re-digested | digest must change |
| **FT-10** | G10 | `Im(μ)/Re(μ) = 1e-3` smuggled into the shear modulus | `≥ 1e-6` / `≥ 1e-5` |

**★ `FT-P` is the most important self-test in this battery and it is the one that would be easiest to omit.** It points `G-P` at an object whose dilatation is **analytically zero** and requires the gate to **fail** there. **A dilatation gate that passes on a divergence-free field is measuring round-off, not dilatation.**

Frozen: `each self-test's mutation is executed and recorded in the same block as its gate's own measurement and BEFORE that measurement is read; FT-P points G-P at the axial instantiation, whose dilatation vanishes analytically, and G-P MUST FAIL there or the gate is measuring round-off rather than dilatation`.

---

## §7 — THE FROZEN PHYSICS BINS — adjudicated IFF that configuration is `SOLVER-CERTIFIED`

**Precedence, frozen:** `BIN-PF-NOROOT > BIN-PF-WALLSING > BIN-PF-SOLVER > BIN-PF-PROFILE > BIN-P1 / BIN-P2 / BIN-P3`.

### §7.1 Honest-failure bins (each reachable, each with a disposition)

- **`BIN-PF-NOROOT`** — no pencil eigenvalue within `R_iso` of any seed, or the mp polish fails to converge, at `n = 48`. **Disposition:** reported as the honest outcome that this configuration's cavity has no polar pole in the searched neighbourhood. **This is `BIN-P2-NO-POLAR-MODE` for that configuration.**
- **`BIN-PF-WALLSING`** ★ — the wall's computed indicial analysis admits no regular solution for that configuration (§2.3(b), §2.5). **Disposition:** an honest result routing to the wall-BC derivation, exactly as the brief specified. **NOT an instrument failure.**
- **`BIN-PF-SOLVER`** — any gate FAILS or any self-test does not FIRE. **Disposition:** `SOLVER-NOT-CERTIFIED`; no physics bin adjudicated for that configuration; route to a successor with a new version number.
- **`BIN-PF-PROFILE`** — a canonical-input contradiction is encountered **on the computational domain** that makes the operator ill-defined. **Disposition:** reported and routed. **Note that FLAG-W is NOT this bin** — FLAG-W is handled by running both branches, and it fires nothing.

### §7.2 BIN-P1 — the polar `ω_R M_g` against the frozen GR comparator

`D_omega_P = (ω_R M_g)_polar / (ω_R M)_GR − 1`, with the GR comparator `J14` read programmatically.

| verdict | criterion |
|---|---|
| `BIN-P1-MATCH` | `abs(D_omega_P) < 0.03` |
| `BIN-P1-NEAR` | `0.03 ≤ abs(D_omega_P) < 0.10` |
| `BIN-P1-MISS` | `abs(D_omega_P) ≥ 0.10` |

**Class line (mandatory, frozen):** `BIN-P1 is VALUE-CONSISTENCY class, not emergence: omega_R*M_g carries the GR-imported nu_vac through the 7 in r_sat`.

**Frozen comparator note:** `GR predicts the SAME value for both families, because Schwarzschild axial/polar isospectrality is a theorem of GR; the comparator is therefore the same I11/J14 pair the axial lane used, and using one comparator for both families is licensed by GR's own degeneracy rather than by convenience`.

### §7.3 ★ BIN-P2 — THE SPLIT, the observable this lane exists to produce

**Primary measure (frozen):** `split = abs(Omega_polar − Omega_axial) / abs(Omega_axial)`, complex, computed **in mp**, with `Omega_axial` read programmatically from the merged in-repo JSON (`J15`).
**Secondary measure (frozen, reported, NOT the bin):** `split_real = abs(omega_R_polar − omega_R_axial) / omega_R_axial`.

| verdict | criterion |
|---|---|
| `BIN-P2-DEGENERATE` | `split < 0.01` |
| `BIN-P2-SPLIT` | `0.01 ≤ split ≤ 1.00` |
| `BIN-P2-SPLIT-BEYOND-MENU` | `split > 1.00` |
| `BIN-P2-NO-POLAR-MODE` | `BIN-PF-NOROOT` or `BIN-PF-WALLSING` fired for this configuration |

Frozen: `BIN-P2's frozen band for SPLIT is 1 percent to 100 percent inclusive; a separation exceeding 100 percent lands in BIN-P2-SPLIT-BEYOND-MENU, which is read as a SPLIT for the discrimination note and is flagged as lying outside the frozen band; the token is minted HERE, before any run, so that no verdict string this driver can emit is absent from this menu`.

**Class line (mandatory, frozen):** `BIN-P2 is the nu_vac-FREE axis and is the most emergence-capable object in this arc: it is a ratio of two eigenvalues of the SAME cavity computed by the SAME instrument, so r_sat divides out identically and every instrument-common systematic divides out with it`.

### §7.4 BIN-P3 — the polar `Q`

`Q_polar = Re(Ω)/(2·abs(Im Ω))`; `D_Q_P = Q_polar/Q_GR − 1` with `Q_GR` formed programmatically from the `J14` pair.

| verdict | criterion |
|---|---|
| `BIN-P3-MATCH` | `abs(D_Q_P) < 0.03` |
| `BIN-P3-NEAR` | `0.03 ≤ abs(D_Q_P) < 0.10` |
| `BIN-P3-MISS` | `abs(D_Q_P) ≥ 0.10` |

**Class line (mandatory, frozen):** `BIN-P3 is nu_vac-FREE and emergence-capable at value level: Q contains no r_sat scale, so the GR-imported 7 cancels exactly, and G8 measures that cancellation`.

### §7.5 ★ THE TWO PRE-REGISTERED RIDERS

**RIDER-1 — the isospectrality rider.** Frozen: `if BIN-P2 returns DEGENERATE, the result is recorded as a NONTRIVIAL CONSISTENCY -- a graded two-channel medium with separate Z_shear and Z_bulk reproduced a degeneracy that is a theorem of GR and that nothing in the medium's structure required; if BIN-P2 returns SPLIT or SPLIT-BEYOND-MENU, the result is recorded as a FORWARD DIVERGENT PREDICTION -- AVE predicts a split l = 2 ringdown spectrum where GR predicts one line -- and in BOTH cases the record is made without any claim that the underlying frequencies match observation`.

**RIDER-2 — the FLAG-W load-bearing rider.** Frozen: `if the two co-primary configurations' omega_R*M_g differ by more than 3 percent, the bulk-modulus sign contradiction of FLAG-W is EMPIRICALLY LOAD-BEARING on an observable rather than a documentation inconsistency, and no polar number from this arc may be cited anywhere until Grant adjudicates which branch canon means; if they differ by 3 percent or less, FLAG-W is recorded as observationally weak at l = 2 in the cold limit and remains a documentation contradiction that is still owed a repair`.

### §7.6 BIN-P4 — `N/A BY CONSTRUCTION`, declared in advance

Frozen: `BIN-P4 (overtone ladder, mode count, completeness) is N/A BY CONSTRUCTION in this lane and is not adjudicated at any precedence level including a full gate pass; no overtone, no ladder, no mode count and no completeness statement is computed for either family, and the deferral is an open instrument-scope question awaiting a substrate-derived low-frequency cutoff, not a failure of this lane`.

### §7.7 ★ PREDICTABILITY DISCLOSURE — stated in advance

**Nothing in this lane is a blind prediction and it is not presented as one.** The axial root is known and merged; the GR comparators are known; the derivation of §2 tells me the two families sample different constitutive content and therefore that a split is *expected on structural grounds*. **What is NOT known to me at freeze:** the sign of the split, its magnitude, whether either branch admits a polar root at all, whether `CFG-SOFT-B` has a regular wall, and whether the instrument certifies. Frozen: `the EXPECTATION of a split is stated at freeze as a structural consequence of separate channel impedances; the magnitude, the sign, the branch dependence, the existence of a root on either branch and the certification outcome are all unknown at freeze, and no bin outcome in this lane may be presented as a blind prediction`.

---

## §8 — THE DISCRIMINATION NOTE, FROZEN IN ADVANCE

**Written under `consistency-vs-emergence` and `ave-discrimination-check`, BEFORE any result, so that it is a commitment rather than a rationalization.**

### §8.1 What a SPLIT would and would not establish

**WOULD:** that this chain — canonical graded profile + Ax-4 kernel + Op16 shear projection + a `K = 2G` bulk projection + the branch's wall pair + the derived Regime-I port — produces **two distinct `ℓ = 2` lines where GR produces one.** That is a **forward divergent prediction** and it is where an AVE-distinct chord could live, because it is a **dimensionless ratio** measured by one instrument on one cavity and it survives the `α`-circularity constraint the corpus already ratified.

**WOULD NOT:**
1. **It would not rescue the v2.4 misses.** A polar line that also misses GR's value is still a miss. **A split is a statement about the RELATIONSHIP between two AVE lines; it is not a statement that either sits where GR sits.**
2. **It would not be observable-ready.** Extracting two `ℓ = 2` lines from a ringdown requires signal-to-noise this document makes no claim about, and this lane computes **no** detectability statement.
3. **It would not be branch-free** unless RIDER-2 says so. If FLAG-W is load-bearing, the *size* of the split is a statement about a **choice canon has not made**.
4. **It would not be Cosserat-complete.** The microrotational channel is not built (Y5), and a third channel could split the family further or shift it.

### §8.2 What a DEGENERATE result would and would not establish

**WOULD:** a genuinely nontrivial consistency. Nothing in a two-channel graded medium requires axial/polar degeneracy; if it appears anyway, the medium is carrying more structure than its constitutive laws obviously contain, and **that is a real finding that should be reported as such and investigated, not filed as "no result".**

**WOULD NOT:** it would not be evidence for AVE over GR (both predict degeneracy, so the observable does not discriminate), and it would not repair the v2.4 misses.

### §8.3 What `NO-POLAR-MODE` would and would not establish

**WOULD:** that the branch's wall pair admits no regular polar solution — which is a strong statement about the **wall**, and routes directly to the wall-BC derivation.
**WOULD NOT:** it would not show the cavity has no polar modes anywhere (`BIN-P4` is `N/A BY CONSTRUCTION`), and it would not falsify the profile.

### §8.4 The standing limit that applies to every outcome

**This lane sees at most one mode per family per configuration.** With `BIN-P4` `N/A BY CONSTRUCTION`, no outcome here says anything about the spectrum. Frozen: `every outcome of this lane is conditional on the section 3 input ledger, on the FLAG-W branch chosen, on the Cosserat microrotational channel not participating, and on this lane seeing at most one mode per family; the result document must carry all four conditions together or none of them`.

---

## §9 — FLAGS RAISED AT FREEZE TIME (flag-don't-fix; surfaced, not resolved)

1. **★ FLAG-W — canon carries two opposite bulk-modulus signs at the same wall** (§2.2(c)). Three verbatim citations, three leaves, no repair. **Routed to Grant. This is the finding of the derivation phase.**
2. **★ FLAG-B — the lane brief's `√2c` bulk speed is corrected by derivation** (§2.2(b)). The port register draws the distinction correctly and in bold; the brief consumed the impedance column as a propagation speed. **Recorded as a correction to the brief, not a defect in canon.**
3. **★ FLAG-4(a) DISCHARGED, FLAG-4(b) OPEN** (§2.3). The `ρ` is named — `ρ_bulk`, two-method — and the naming leaf is left byte-untouched. The **grading** is genuinely open and both candidates are run.
4. **★ FLAG-3 DISCHARGED FOR THE PROFILE, NOT FOR THE UNIVERSE** (§2.4). The reflectionless port is derived from the `O(1/r²)` short-range tail. It does not exclude a far-field reflector from physics outside this profile.
5. **⚑ FLAG-COS — the Cosserat microrotational channel is not built** (§0 walk item 7, Y5). Every result is conditional on it not participating at `ℓ = 2` in the cold limit. **Not tested, not sketched, not assumed away — tagged.**
6. **⚑ FLAG-NOG6 — this lane has no two-instrument agreement gate** (§5). No polar number here carries cross-instrument corroboration.
7. **⚑ FLAG-BAO — the beyond-all-orders bulk suppression** (§2.6) is disclosed in advance with its two pre-registered consequences. **If `G-P` fails, this flag is the explanation and the lane says so rather than hunting for another.**
8. **⚑ FLAG-MK — the Makefile contact.** This lane adds a **fifth** cold-Q number-check target. The `.PHONY` line and the `verify:` prerequisite line are shared with any other open cold-Q branch and are a **real two-line conflict**, not an append-only merge. Mitigation, frozen: the number check is wired as its **own** target so no recipe body is shared, and this branch is rebased onto a fresh `origin/main` immediately before the PR. **At freeze, this lane is the only cold-Q lane running.**
9. **⚑ FLAG-5 CARRIED FORWARD, UNRESOLVED** — the substrate-derived low-frequency cutoff. Unchanged from v2.2 and v2.4. `BIN-P4` stays `N/A BY CONSTRUCTION` for as long as that takes.

---

## §10 — WHAT TRANSFERS FROM v2.4, AND WHAT MUST BE RE-EARNED

**TRANSFERS (and is cited, not re-derived):** the profile `A = r_sat/r`; the Ax-4 kernel; the Op16 shear projection; the `Γ_shear = −1` wall; the `A = 1 − η²` substitution; the compactified hyperboloidal framing; the numerical machinery of §P.5; the GR comparators; the `R_iso` value; the `[1.0, 2.0]` window.

**MUST BE RE-EARNED, and is not inherited under any circumstances:**

1. **The operator.** Newly derived; gated by `G0(a)`, `G0(b)`, `G0(c)`.
2. **The wall.** Newly derived per branch; gated by the indicial analysis and by `BIN-PF-WALLSING`.
3. **The port.** Newly derived per channel; §2.4.
4. **The convergence law's parameters.** Not imported from the axial operator; §4.5.
5. **Certification.** v2.4's `ROOT-CERTIFIED` transfers **nothing**. Frozen: `v2.4's ROOT-CERTIFIED verdict certifies the axial instrument on the axial operator and transfers NOTHING to this lane; this instrument is certified or not certified on its own gates, per configuration, and a G-C(b) reproduction of the certified axial root is a regression control on shared machinery and is not a certification of anything polar`.
6. **Any physics reading.** The v2.4 misses are v2.4's. **A polar result neither rescues nor deepens them, and the result document must say so in those words.**

---

> **Freeze provenance.** This file is COMMIT 1 of the lane `research/coldq-polar-family`, pushed **ALONE** before any driver code exists and before any number produced by this instrument exists. Written against `origin/main` = `ce65b3b8`. Predecessor frozen files are byte-untouched and blob-pinned in §P.4. Mints no `clm-`/`def-`; propagates to no leaf; engine `src/ave` byte-untouched; falsification ledger untouched. Companion (written after the run): `research/2026-08-03_coldq-polar-family_result.md` and the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-polar-family.md`.
