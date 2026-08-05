# The cold-Q AXIAL family under RHO-B — FROZEN pre-registration (**FORK-3(b) in the certified axial instrument class; discharges v2.4 §7 FLAG-4**)

**Date:** 2026-08-04
**Class:** DERIVATION pre-registration (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger — regardless of outcome**). Committed **ALONE** and pushed **before any driver code and before any number produced by this instrument exists**.
**Result-doc pointer requirement.** The result doc that resolves these bins MUST carry `Prereg-file: research/2026-08-04_coldq-axial-rhob_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file.
**Provenance:** Grant's ruling of 2026-08-04 — the fork v2.4 fenced at `X6` is owed an **AXIAL** run before the `BIN-1`/`BIN-2` misses are read as profile falsification. The polar lane ran FORK-3(b) once, in an **UNCERTIFIED coupled** instrument that found no root on any configuration and adjudicated nothing; the **certified-axial** debt named by v2.4's own §7 FLAG-4 is still unpaid. **This lane pays it.**
**Written against** `origin/main` = `10213df3`.

---

## §P — WHAT THIS LANE IS, IN ONE PARAGRAPH, AND WHAT IT IS NOT

The `ℓ = 2` toroidal shear pole of the graded saturation cavity has been located and **certified** once, by v2.4, under the inertia reading **RHO-A** (`ρ(r) = ρ_bulk`, the cold lattice inertia). That certified root **misses** GR on both axes. v2.4's own §7 FLAG-4 records that a second canonical inertia reading exists — **RHO-B**, `ρ_eff = ρ_bulk/S³` — that it was fenced off by `X6`, never run, and **would move the eigenvalue**. **This lane runs it, in the axial class, with a wall row derived from the RHO-B branch rather than imported from RHO-A.**

**It is NOT** a re-certification of v2.4, **NOT** an adjudication of FLAG-W (the bulk-sign contradiction — this lane is SHEAR-channel only and the axial family never touches the bulk line), **NOT** a repair of any KB leaf, and **NOT** a claim about which inertia canon means. It is one fork, run once, gated, and reported.

### §P.1 Predecessor state, in order — and the blob pins that make "byte-untouched" checkable

| lane | artifact | state |
|---|---|---|
| **v2.4** (MERGED) | `research/2026-08-03_coldq-pole-v2.4-root_prereg-FROZEN.md`, `..._result.md`, `research/drivers/coldq_pole_v2p4_root.py`, `..._results.json` | **`ROOT-CERTIFIED`** under RHO-A. `BIN-1-MISS`, `BIN-2-MISS`, `BIN-3-MONOTONE`. **FORK-3(b) fenced at `X6`; FLAG-4 routes it as owed.** |
| **polar family** (PR #869, OPEN, DO-NOT-MERGE) | `research/2026-08-03_coldq-polar-family_*`, `research/drivers/coldq_polar_family*` | **`SOLVER-NOT-CERTIFIED`**; `BIN-PF-NOROOT` on all three configurations including `CFG-SOFT-B` (RHO-B). **Adjudicated nothing.** Its `BIN-PF-WALLSING` was **never evaluated** — the indicial analysis is in its UNRUN set. |

**Predecessor fence, frozen.** `every predecessor file named in section P.1 is BYTE-UNTOUCHED by this lane and the claim is discharged by an empty git diff --stat against the freeze base on each of them; research/drivers/coldq_pole_v2p4_root.py is IMPORTED READ-ONLY as a comparison object for the negative control and is neither edited nor re-executed as a battery`.

**Lane fence, frozen.** `this lane is SHEAR-CHANNEL ONLY; it computes no bulk modulus, no dilatational speed, no polar/spheroidal branch and no coupled system, so it CANNOT and DOES NOT adjudicate FLAG-W; the section 9 appendix is a DERIVED-CONSEQUENCE FLAG for the core session's FLAG-W walk and repairs nothing, edits no leaf, and prefers no branch`.

---

## §0 — SECTOR / MODE / REGIME / PHASE-STATE / COORDS header, declared BEFORE any physics word

**Re-walked fresh.** The walk reaches v2.4's conclusions on five checkpoints and **departs from them on two**, and the departures are the content of this lane.

- **MODE.** DC operating-point **eigenproblem**, shear channel. Cold (`a_* = 0`, Schwarzschild-limit) remnant ringing down. The object is **one** quasinormal resonance of the saturation cavity — the `ℓ = 2` **toroidal** shear mode — and **not** its ladder.
- **SECTOR.** The observable is a **transverse shear (T2)** oscillation. The bias field that builds the cavity is the **A1 radial dilatation** `ε_11 = 7GM/(c²r)`. Orthogonal grades, **not cross-wired**: A1 sets the DC constitutive profile; T2 is the small-signal AC riding on it. **RHO-B changes the T2 channel's series-`L` (inertia), not its sector.**
- **REGIME.** Sub-yield lossless-reactive. Far field (`r ≫ r_sat`) = Regime I. The graded exterior `r > r_sat` = Regime I with a spatially varying modulus **and, under RHO-B, a spatially varying inertia**. The interior `r < r_sat` = Regime IV, **not part of the computational domain**; the domain is `[r_sat, ∞)`.
- **★ THE WALL, RESTATED FOR THIS LANE.** Under RHO-A the wall `r = r_sat` is the `S → 0` level set reached at **FINITE** optical distance. **Under RHO-B it is the same level set reached at INFINITE optical distance** (§2.4). That is a regime statement, it is derived, and it is the single most important difference this lane carries.
- **PHASE-STATE.** Cold lattice. Op14 ON throughout the graded exterior as a **static constitutive grade** (the DC bias is time-independent; the ringdown is the small-signal response). `A = 1` exactly at `r_sat = 7GM/c²`.
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the **dimensionless-eigenvalue register** (`ω_R M_g`, `Q`) that AVE and GR share — no phase-space/real-space mismatch. This lane solves for the **complex pole** directly, so what it returns *is* the pole-`Q` the GR comparator is; **no port→pole transfer is performed, needed or assumed.**
- **★ ARTIFACT-CLASS DISCIPLINE, declared in advance.** Frozen: `a null in which the mode CANNOT exist under the frozen construction is an ARTIFACT-class finding and is classified as such, not as a falsification of the profile; specifically, a no-root outcome traceable to the instrument's function space failing to contain the RHO-B endpoint behaviour is ARTIFACT-class, and this document is required to say so in its headline rather than in a footnote`.

### Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code)

1. **K4 / srs connectivity.** **CONTINUUM** instrument. Frozen: `the radial channel is a CONTINUUM representation of the shear constitutive law; it is not a discretization of the srs stencil and carries no K4 connectivity claim`. What it consumes from the lattice is the **constitutive law only**: the Ax-4 kernel, the shear-modulus grading, and the inertia grading under test.
2. **Cosserat / channel basis.** The mode is on the **toroidal (odd-parity / axial) branch**, whose displacement field is **exactly divergence-free**, so the Lamé `λ_L` (bulk/A1) modulus drops out of the equations of motion **identically** rather than by assumption. Frozen: `the toroidal (odd-parity) branch is exactly divergence-free, so the bulk modulus drops out identically and there is no linear P-SV conversion partner; this is why the RHO-B fork can be run in the axial class WITHOUT touching the FLAG-W bulk contradiction, and it is the mechanical reason this lane can adjudicate where the polar lane could not`. **The Cosserat microrotational channel is not built** (§1.3 Y5).
3. **Op14 saturation.** Enters as the **static constitutive grade** `S(A) = sqrt(1 − A²)` with `A(r) = r_sat/r`. **Under RHO-B it enters a SECOND time, in the inertia**, as `ρ_eff = ρ_bulk/S³`. Frozen: `Op14 enters the shear modulus as a static constitutive grade mu = G_vac*S and, under RHO-B ONLY, a second time in the inertia as rho_eff = rho_bulk/S^3; the A -> 1 terminus is handled by an exact change of variable plus an exact Frobenius factoring, never by a numerical cutoff or a regularized floor`.
4. **★ The compactification is the medium's own order parameter.** The radial coordinate is `A = r_sat/r` — the Axiom-4 saturation amplitude itself; `A = 1` IS the wall, `A = 0` IS infinity. Frozen: `the compactified radial coordinate is the Axiom-4 saturation amplitude A = r_sat/r itself, so A = 1 is the wall and A = 0 is infinity; the instrument adopts the medium's own order parameter as its coordinate rather than imposing a lattice-Cartesian one`.
5. **Phase-space vs real-space (A46).** Every verdict-class observable is a **dimensionless ratio**: `ω_R M_g`, `Q`. **α-CLEAN** — `α` appears nowhere in the chain.
6. **Checkpoint: boundary-not-bulk.** The resonator is a **boundary/graded-shell** object, consistent with the #403/#404 localization ruling. The loss is a **radiative port at infinity** (Ax-3-licensed), and there is **no** `Re{Z}` anywhere in the medium. **G10 tests exactly that, on the certified eigenfunction's own operator.**
7. **★ NEW CHECKPOINT, forced by this lane: is `ρ_eff = ρ_bulk/S³` a MODULUS statement or an INERTIA statement, and does it belong in the series-`L`?** It is an **inertia** statement and it belongs in the series-`L`, and that is the whole content of FORK-3(b). Canon writes the shear impedance as `Z_shear = ρ_bulk c_shear` with a **constant** `ρ_bulk` ([`vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md:21`](../manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md)) **and, three bullets apart in one leaf**, asserts `ρ_eff → ∞` at the same wall ([`vol3/claim-quality.md:122`](../manuscript/ave-kb/vol3/claim-quality.md) and `:124`). **Both cannot be the series-`L` of the same line.** This lane runs the second reading and reports what it does; it does **not** decide which canon means (§10 FLAG-R).
8. **★ NEW CHECKPOINT: is the RHO-A wall row transferable?** **NO, and the derivation is §2.5.** Frozen: `the RHO-A traction-free SHORT row dpsi/deta = 0 at eta = 0 is a condition at an ORDINARY point of the RHO-A transformed equation and has NO RHO-B analogue, because eta = 0 is a REGULAR SINGULAR point of the RHO-B transformed equation; importing it would impose a Neumann condition at a singular point where the solution's derivative generically diverges, and this lane rejects it BY DERIVATION and exercises it only as a self-test mutation`.

### Pre-test physics check (`pre-test-physics-check`, Rule 16 — ONE plumber question surfaced to Grant BEFORE the design locks)

> **Grant — this is a NEW question and it is the one RHO-B creates. It is not v2.4's BIN-3 question and it is not the polar lane's FLAG-W question.**
>
> Under RHO-A my cavity is a **shorted stub**: the taper runs from the cold lattice down to `Z = 0` at `r_sat`, and the short sits at a **finite** electrical length — a wave launched inward hits it and comes back. Under RHO-B the same taper's characteristic impedance `Z = sqrt(Gρ) = ρ₀c₀/S` runs the **other way — to infinity** — and the phase velocity `c = c₀S²` collapses fast enough that the **electrical length to the wall becomes infinite**. `∫dr/c` diverges logarithmically. **A wave launched inward never arrives.**
>
> So in plumber terms I no longer have a shorted stub with a taper on it. I have a lossless line that keeps getting slower and heavier without end, and the "termination" is a place no signal reaches in finite time. **My question is: is that still a cavity?**
>
> - **(a) Yes, and it is the better cavity.** Infinite electrical length with nothing coming back is *structurally the same boundary a black-hole horizon presents* — energy goes in and does not return, with no dissipation anywhere in the medium. Ax 3 already licenses exactly this at the other end (the radiative port at infinity). If that is the right reading, the inner condition is **purely ingoing**, and RHO-B does not merely move the pole — **it converts the AVE saturation wall from a reflector into a horizon-analogue**, and the corpus's *"echoes are predicted"* line ([`vol3/claim-quality.md:123`](../manuscript/ave-kb/vol3/claim-quality.md)) would be an RHO-A statement, not a substrate statement.
> - **(b) No — the mode is trapped by the impedance GRADIENT, not by a reflector.** On this reading the only physical inner condition is **boundedness/finite energy**, the resonance is a graded-taper trapping rather than a stub resonance, and the word "reflect" should be retired from the RHO-B branch entirely.
>
> **I am not choosing between them by preference.** Both are derivable rows at the same regular singular point and I have frozen them as **CO-PRIMARY** (§2.5, §4.3). What I need from you is the plumber's call on whether **(a)** is the honest reading of an infinite-electrical-length lossless termination — because if it is, then the interesting number in this lane is not `Q` versus GR, it is **whether an AVE wall that behaves like a horizon produces a GR-like `Q`**, and that is a different question from the one v2.4 asked.
>
> **Carried forward unchanged and NOT re-asked:** v2.4's FLAG-5 (a substrate-derived low-frequency cutoff) and its BIN-3 localization question. `BIN-B-4` stays `N/A BY CONSTRUCTION`; no localization observable is computed in this lane at all (§1.3 Y6).

### Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE any result

Written in units of `r_sat`, the RHO-B problem has **no free parameter at all**: the profile is `A = r_sat/r`; the kernel is `S = sqrt(1 − A²)`; the modulus is `μ = G_vac S`; the inertia is `ρ_bulk/S³`. Therefore `Ω ≡ ω·r_sat/c₀` is a **pure number** fixed by the profile SHAPE, the two Ax-4 gradings, and `ℓ`.

| output | rides `r_sat`'s coefficient `7`? | class |
|---|---|---|
| `ω_R M_g` (`BIN-B-1`) | **YES** — `ω_R M_g = Re(Ω)/x_sat` | **VALUE-CONSISTENCY.** The `7` is the `1/7` trace-reversed bulk projection, which takes `ν_vac = 2/7` as **input** ([`one-seventh-impedance-projection.md:18`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md)). **May NOT be headlined as value-level emergence.** |
| **`Q = ω_R/(2\|ω_I\|)` (`BIN-B-2`)** | **NO — it cancels exactly** | **`ν_vac`-FREE, therefore EMERGENCE-CAPABLE at value level.** |
| the RHO-B/RHO-A shift (`BIN-B-3`) | **NO** — a ratio of two `Ω`s | **FORM-class.** A statement about which inertia grading the cavity's spectrum prefers, not a value-level substrate claim. |
| the wall's indicial exponents `σ±` | **NO** | **FORM-class, and DERIVED.** `σ± = (1 ± sqrt(1 − 4Ω²))/2` is an exact consequence of the RHO-B grading and contains no imported number. |

Frozen tag: `Q and the RHO-B/RHO-A shift ratio are exactly nu_vac-free (the r_sat scale divides out identically); omega_R*M_g is NOT and is VALUE-CONSISTENCY class because the 7 in r_sat = 7GM/c^2 is the 1/7 projection of the GR-imported nu_vac = 2/7`.

> **★ WHAT A CERTIFIED RHO-B ROOT WOULD AND WOULD NOT MEAN, written before the run.** A `ROOT-CERTIFIED` verdict is a statement about an **instrument**: *this discretization's eigenvalue at this location is a property of the continuous problem and not of the discretization*. It does **not** say the substrate rings there, and it does **not** say RHO-B is the right inertia. **Additionally and specific to this lane:** because the RHO-B wall row is **CO-PRIMARY across two derived branches** (§2.5), a certification on one branch certifies **that branch's** eigenvalue and nothing about the other.

---

## §1 — THE TARGET AND THE EXPLICIT NON-CLAIMS

### §1.1 The target

**Locate and certify the `ℓ = 2` toroidal shear pole of the graded saturation cavity under the RHO-B inertia grading `ρ_eff = ρ_bulk/S³`, in the axial (toroidal) instrument class, with a wall row DERIVED from the RHO-B branch — and report where the pole lands against (i) v2.4's certified RHO-A root and (ii) the frozen GR comparators, both read PROGRAMMATICALLY from in-repo artifacts.**

**Seed provenance.** The search is seeded from **v2.4's certified root, read programmatically from the shipped in-repo JSON** — not transcribed. Frozen: `the RHO-B search is seeded from v2.4's certified RHO-A root read PROGRAMMATICALLY from research/drivers/coldq_pole_v2p4_root_results.json; the seed selects WHICH pencil eigenvalue is polished and enters no gate, no tolerance, no comparator and no bin as a value; a second, independent seed sweep over the frozen physical-quadrant seed grid of section 4.6 is also run and its result is reported whether or not it agrees`.

**Certification means: ALL gates of §5 PASS and ALL fireability self-tests of §6 FIRE, per configuration.** There is no partial certification: `ROOT-CERTIFIED` or `ROOT-NOT-CERTIFIED`, **stated separately for each configuration of §4.3**.

### §1.2 The non-claims, written in advance and binding

- **NO winding, argument principle, or contour integral is computed anywhere in this lane.** Frozen: `no argument-principle winding, no contour integral and no region count is computed anywhere in this lane; the pole-counting instrument the PR #854 audit impeached is not used, not repaired and not relied on`.
- **NO completeness claim, no "the only mode", no mode count, no overtone ladder.** `BIN-B-4` is `N/A BY CONSTRUCTION`, stated in advance.
- **NO claim that RHO-B is the correct inertia.** Frozen: `this lane runs FORK-3(b); it does not adjudicate FORK-3, does not prefer RHO-B over RHO-A, and a root located under RHO-B is evidence about the RHO-B branch of the fork and about nothing else`.
- **NO retroactive pass or fail for v2.4.** Frozen: `whatever this lane measures, v2.4 stands ROOT-CERTIFIED on the RHO-A operator it gated; a RHO-B result neither certifies, rescues, re-scores nor reverses it, and the negative control of section 5 G-NC is a REGRESSION CONTROL on this lane's own transcription, not a re-certification of v2.4`.
- **NO adjudication of FLAG-W.** Frozen per §P's lane fence.

### §1.3 What this lane additionally does NOT do

- **Y1 — does NOT derive `ℓ = 2`.** Quadrupole selection is an input.
- **Y2 — does NOT derive `ν_vac`, `K = 2G`, or the `7` in `r_sat`.** GR-IMPORT, closed by PR #261/#506, untouched.
- **Y3 — does NOT touch the spin (`a_* > 0`) mapping.**
- **Y4 — does NOT compute a port-`Q`, a radiation resistance, or a Chu/Collin–Rothschild stored-energy `Q`.**
- **Y5 — does NOT build the Cosserat microrotational channel**, and every statement here is conditional on it not participating at `ℓ = 2` in the cold limit.
- **Y6 — does NOT compute any localization observable.** v2.4's `BIN-3` axis is **not re-measured, not widened and not re-defined**; it is simply absent, because v2.4 landed it in `BIN-3-MONOTONE` and its plumber question is still owed.
- **Y7 — does NOT build the polar / spheroidal branch, and does NOT re-run, repair, or re-score the polar lane.**
- **Y8 — does NOT derive, assume, sketch or gesture at a low-frequency cutoff.**
- **Y9 — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry**, whatever the outcome.
- **Y10 — does NOT run the `c`-PRIMARY reading of RHO-B** (§2.2), which is fenced by derivation and disclosed rather than silently dropped.
- **Y11 — does NOT edit `Makefile` recipes belonging to any other lane**; it appends its own target only.

---

## §2 — THE RHO-B PHYSICS, DERIVED HERE — AND THE WALL ROW, WHICH IS THE WHOLE POINT

### §2.1 The inherited radial system, restated so the RHO-B entry point is visible

The toroidal (odd-parity) radial system, in `W(r)` with conjugate traction `T(r) ≡ μ(r)·(W′ − W/r)`, `μ ≡ G_shear`:

```
W'' + (2/r + g) W' + [ w^2 rho/mu - l(l+1)/r^2 - g/r ] W = 0 ,   g = mu'/mu
```

**`ρ` enters this equation at exactly ONE place: the combination `ρ/μ`.** Nowhere else. Frozen: `the inertia enters the toroidal radial system at exactly one place, the combination rho/mu in the omega^2 coefficient, so FORK-3(b) is a ONE-COEFFICIENT change to the certified axial operator and every other coefficient — the 2/r term, the modulus log-derivative g, the centrifugal term and the -g/r term — is byte-identical between RHO-A and RHO-B`.

This is derived, not asserted: with `T = μ(W′ − W/r)` and `T′ = [(ℓ−1)(ℓ+2)μ/r² − ρω²]W − 3T/r`, eliminating `T` gives the displayed second-order form, and `ρ` appears only in `T′`'s inertia term.

### §2.2 ★ WHICH RHO-B — the `μ`-primary reading is FROZEN, and the `c`-primary reading is fenced by derivation, not by preference

Canon supplies **three** statements that cannot all survive an inertia grading:

| # | statement | leaf, verified two-method at this freeze |
|---|---|---|
| **(i)** | `S(A) = (1 − A²)^{1/2}`, `A = ε_11/ε_yield`, `ε_yield = 1` | [`saturating-modulus-and-backreaction.md:51`–`:52`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md) |
| **(ii)** | *"**SHEAR softens:** $c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection"* | same leaf, **`:60`** |
| **(iii)** | *"a solid$\to$liquid free surface ($G_{shear} \to 0$) is exactly a $Z_{shear} \to 0$ short"* | [`vol3/claim-quality.md:123`](../manuscript/ave-kb/vol3/claim-quality.md) |

Under RHO-A the three are consistent: `μ = ρ₀c₀²S = G_vac S` (so `G_shear → 0` ✓) and `c = sqrt(μ/ρ₀) = c₀√S` (so (ii) ✓). **Under RHO-B they are not**, and a choice must be made and disclosed:

- **`μ`-PRIMARY (FROZEN, RUN).** Hold the **modulus** grading `μ = G_vac·S`. Then `c_shear = sqrt(μ/ρ_eff) = c₀·S²`, so **(ii)'s `√S` projection is superseded** but **(iii)'s `G_shear → 0` is preserved**.
- **`c`-PRIMARY (FENCED, NOT RUN — `Y10`).** Hold **Op16's speed** `c_shear = c₀√S`. Then `μ = ρ_eff c² = G_vac/S²`, which **diverges** at the wall — **contradicting (iii) verbatim**, and contradicting the `SHEAR softens` half of the leaf's own per-channel **sign-lock** (`:56`, *"The per-channel **sign-lock** (INVARIANT-S2) keeps the three channels physically distinct"*).

**The `μ`-primary reading is chosen because Op16's `√S` is itself DERIVED under `ρ = ρ₀`** — `c = sqrt(G_vac S/ρ₀) = c₀√S` — so it is a **consequence** of RHO-A rather than an independent axiom, whereas `G_shear → 0` is asserted directly at `:123` and is the load-bearing content of the shear-melt picture. **Holding the derived consequence fixed while varying its own premise would be circular.**

Frozen: `RHO-B is run in the MU-PRIMARY reading: the modulus grading mu = G_vac*S is held and the shear speed becomes c_shear = c_0*S^2, superseding Op16's sqrt(S) projection which is itself a CONSEQUENCE of rho = rho_0 rather than an independent axiom; the c-PRIMARY reading (hold c_shear = c_0*sqrt(S), giving mu = G_vac/S^2 which DIVERGES) is fenced and NOT run because it contradicts vol3/claim-quality.md:123's G_shear -> 0 verbatim and the per-channel sign-lock at saturating-modulus-and-backreaction.md:56; the choice is disclosed here, is a FORK not a fact, and is routed as FLAG-MU`.

**Independent confirmation that the frozen reading reproduces the polar lane's derivation.** The polar lane froze, at `research/2026-08-03_coldq-polar-family_prereg-FROZEN.md:336` @ `d9015e38`: *"under RHO-B the shear speed becomes `c_shear = sqrt(μ/ρ) = c₀ S²` rather than `c₀ sqrt(S)`"*. **Re-derived here independently and agreeing:** `sqrt(μ/ρ_eff) = sqrt(G_vac S · S³/ρ_bulk) = c₀ S²`. **Agreement is recorded as a cross-lane consistency check on a DERIVATION, not as corroboration of any measured value** — that lane measured nothing.

### §2.3 The operator change, in closed form

Set `c₀ = ρ_bulk = G_vac = 1`; `A ≡ r_sat/r ∈ (0,1]`, `Ω ≡ ω·r_sat/c₀`, `μ = S`, and factor the outgoing wave out analytically with v2.4's **unchanged** factoring `W = A·exp(iΩ(1/A + λA))·ψ`. Then the ONLY changed coefficient is the `Ω²` one:

```
RHO-A :  Om^2 / ( S (1 + S) )              [ = (1/S  - 1)/A^2 ]
RHO-B :  Om^2 ( 1 + S^2 ) / S^4            [ = (1/S^4 - 1)/A^2 ]
```

**Derivation, in two lines.** The `ω²ρ/μ·r²` term contributes `Ω²/(A²)·(ρ/μ)`; the outgoing factoring subtracts the cold-exterior plane wave's `Ω²/A²`. So the net coefficient is `Ω²(ρ/μ − 1)/A²`. With `ρ/μ = 1/S` this is `Ω²(1−S)/(A²S) = Ω²/(S(1+S))` since `A² = 1−S²`. With `ρ/μ = 1/S⁴` it is `Ω²(1−S⁴)/(A²S⁴) = Ω²(1+S²)/S⁴` since `1−S⁴ = A²(1+S²)`. **The first line reproduces v2.4's shipped coefficient exactly, which is the algebraic negative control on this derivation and is gated as `G0`.**

**Far field, and why the port survives unchanged.** `ρ_eff/ρ₀ = S^{-3} = (1−A²)^{-3/2} = 1 + (3/2)A² + O(A⁴)`, and `ρ/μ = S^{-4} = 1 + 2A² + O(A⁴)`. **`O(A²) = O(1/r²)`: no `1/r` term.** So the graded exterior remains a **SHORT-RANGE** perturbation of a homogeneous medium, produces no logarithmic phase, and produces no reflection at any polynomial order in `1/(kr)`.

Frozen: `under RHO-B the modulus-and-inertia deviation from the cold values is O(1/r^2) with no 1/r term exactly as under RHO-A, so the reflectionless Regime-I port at infinity is DERIVED for RHO-B by the same argument the polar lane derived it by, the outgoing factoring exp(i*Om/A) is exact to all polynomial orders, and NO boundary condition is imposed at infinity; the ingoing branch carries an essential singularity that is not in the discretization's function space`.

### §2.4 ★ THE WALL, UNDER RHO-B — impedance, optical distance, and the indicial analysis

Everything below is evaluated on the exact change of variable `A = 1 − η²`, under which `S² = 1 − A² = η²(2 − η²)`, `S = η·u`, `u = sqrt(2 − η²) → sqrt(2)`.

**(a) The wall IMPEDANCE flips sign of divergence — computed two ways.**

```
Z_shear = sqrt(mu * rho)  = sqrt( S * S^-3 )      = 1/S   -> INFINITY
Z_shear = rho * c_shear   = S^-3 * S^2            = 1/S   -> INFINITY
```

against RHO-A's `sqrt(S·1) = sqrt(S) → 0`. **The two constructions agree exactly.** Frozen: `under RHO-B the shear wall impedance Z_shear = sqrt(mu*rho) = rho*c_shear = 1/S DIVERGES at the wall, computed two ways in agreement, where under RHO-A it VANISHES; the naive local-interface reading of that divergence is Gamma_shear = +1 (an OPEN) in place of RHO-A's Gamma_shear = -1 (a SHORT), and this lane records that reading and then REJECTS it as the wall row in favour of the graded-medium derivation of part (c), because there is no interface at r_sat — the medium's own impedance diverges continuously`.

**(b) The wall moves to INFINITE optical distance.** With `c_shear = S²` and `dr ≈ 2η dη` near the wall,

```
RHO-A :  int dr/c = int 2 eta d(eta) / (sqrt(2) eta^(1/2))  ~  int eta^(1/2) d(eta)   FINITE
RHO-B :  int dr/c = int 2 eta d(eta) / (2 eta^2)            =  int d(eta)/eta         LOG-DIVERGENT
```

Frozen: `under RHO-B the saturation wall sits at INFINITE optical distance — the travel-time integral int dr/c_shear diverges logarithmically at eta = 0 — where under RHO-A it sits at finite optical distance; a wave launched inward under RHO-B never arrives, so there is no reflection event at the wall and the RHO-A reflection-coefficient vocabulary does not apply to the RHO-B branch`.

**(c) `η = 0` becomes a REGULAR SINGULAR POINT, and the indicial equation is exact.** Multiplying the `A`-form by `4η²` exactly as v2.4 does (`𝓛_η ≡ 4η²·𝓛_A`) and writing `𝒜ψ_ηη + ℬψ_η + 𝒞ψ = 0`:

```
A_coef = A^2                                   -> 1        at eta = 0
B_coef = (A^2/eta)(-1 + 2A/u^2) + 4i*Om*eta*(1 - lam*A^2) - 4*A*eta   -> O(eta)
C_coef = 4 Om^2 (1 + eta^2 u^2)/(eta^2 u^4) + 4i*Om*A/u^2 - 8 A^2/u^2 + O(eta^2)
       -> Om^2/eta^2 + 2i*Om - 4 + O(eta)
```

`ℬ`'s apparent `1/η` cancels identically (`−1 + 2A/u² = −η²/2 + O(η⁴)`), which is the same cancellation that makes `η = 0` **ordinary** for RHO-A. **What is new is `𝒞`'s double pole.** Hence `η·p(η) → 0` and `η²·q(η) → Ω²`, so `η = 0` is a **regular singular point** and the indicial equation is exactly

```
sigma (sigma - 1) + Om^2 = 0    =>    sigma_pm = ( 1 +- sqrt(1 - 4 Om^2) ) / 2
```

with the **principal** branch of the square root (so `Re sqrt ≥ 0` and `Re σ₊ ≥ Re σ₋`). **Under RHO-A the same construction gives `𝒞 → 2iΩ − 4` and `η = 0` is an ordinary point with no indicial equation at all.**

Frozen: `under RHO-B eta = 0 is a REGULAR SINGULAR point of the transformed equation with the exact indicial equation sigma*(sigma-1) + Om^2 = 0 and exponents sigma_pm = (1 +- sqrt(1 - 4*Om^2))/2 on the principal branch; under RHO-A the same eta = 0 is an ORDINARY point; this order change is the DERIVED consequence the polar lane pre-registered as reachable and this lane computes it rather than assuming it`.

**(d) The three near-wall consequences, each derived and each gated.**

```
finite energy       int rho |W|^2 r^2 dr ~ int eta^(2 Re sigma - 2) d(eta)   converges iff Re sigma > 1/2
traction T          T = mu (W' - W/r) ~ (sigma/sqrt(2)) eta^(sigma - 1)      vanishes iff Re sigma > 1
Frobenius regularity  the two exponents must not differ by a positive integer, else a log term enters
```

**Read them together and the RHO-A wall row is dead.** Because `Re σ₊ + Re σ₋ = 1`, at most one exponent can have `Re σ > 1`. So `T(r_sat) = 0` cannot be an independent *condition* under RHO-B: on one branch it holds automatically and on the other it is unsatisfiable. **A traction-free row is either vacuous or contradictory. There is no third possibility, and this is a theorem of the indicial equation, not a numerical observation.**

### §2.5 ★ THE RHO-B WALL ROW — DERIVED, CO-PRIMARY IN TWO BRANCHES, AND ITS DISAGREEMENT WITH RHO-A STATED IN FULL

Two rows are derivable at the regular singular point, they correspond to the two physical readings the §0 plumber question puts to Grant, and **neither is preferred**:

| | **ROW-BOUND** | **ROW-IN** | **ROW-SHORT (RHO-A's)** |
|---|---|---|---|
| exponent retained | `σ₊` (larger `Re`) | `σ₋` (smaller `Re`) | — |
| physical content | finite energy / limit-point; the mode is trapped by the impedance **gradient** | purely **ingoing** at the wall; nothing returns from an infinite-electrical-length termination — the Ax-3-licensed mirror of the port at infinity | traction-free free surface at a **finite**-distance interface |
| status under RHO-B | **DERIVED, CO-PRIMARY** | **DERIVED, CO-PRIMARY** | **REJECTED BY DERIVATION** (§2.4(d)) |
| how it is imposed | Frobenius factoring `ψ = η^{σ₊}φ`, then `dφ/dη\|₀ = 0` | Frobenius factoring `ψ = η^{σ₋}φ`, then `dφ/dη\|₀ = 0` | `dψ/dη\|₀ = 0` |

**The Frobenius row is DERIVED, not assumed, and it is the same row for both branches.** Substituting `ψ = η^σφ` into `𝒜ψ_ηη + ℬψ_η + 𝒞ψ = 0`, multiplying by `η²` and then dividing by `η`, and taking `η → 0`:

```
eta*A_coef*phi_etaeta + (2*A_coef*sigma + B_coef*eta)*phi_eta
    + [ (A_coef*sigma*(sigma-1) + eta^2*C_coef)/eta + B_coef*sigma ] * phi = 0
```

At `η = 0`: `𝒜 = 1`; `ℬ = O(η)` so `ℬσ → 0`; and `𝒜σ(σ−1) + η²𝒞 → σ(σ−1) + Ω² = 0` **by the indicial equation**, with **no `O(η)` term** (both `𝒜` and `η²𝒞` are even in `η` at leading orders), so the bracket `→ 0`. The surviving row is `2σ·φ_η(0) = 0`, i.e.

```
dphi/deta |_{eta = 0} = 0        for sigma != 0
```

**which is exactly the `a₁ = 0` statement of the Frobenius recursion, i.e. an ANALYTICITY constraint, not a boundary condition.** Frozen: `the RHO-B wall row is dphi/deta = 0 at eta = 0 in the Frobenius-factored variable phi = eta^(-sigma) psi, derived from the eta-multiplied equation's limit using only the indicial identity sigma*(sigma-1) + Om^2 = 0; it is the a_1 = 0 analyticity constraint of the Frobenius recursion and NOT a traction condition, and it is IDENTICAL in form for both branches, with the branch selection carried by which sigma is factored out and by function-space membership`.

**★ THE DISAGREEMENT WITH RHO-A, STATED EXPLICITLY AS THE BRIEF REQUIRES.**

| axis | RHO-A (v2.4, certified) | RHO-B (this lane, derived) |
|---|---|---|
| `η = 0` classification | **ordinary point** | **regular singular point** |
| wall impedance `Z = sqrt(μρ)` | `sqrt(S) → 0` — a **SHORT** | `1/S → ∞` — diverges |
| naive interface `Γ_shear` | `−1` | `+1` |
| optical distance to the wall | **finite** | **infinite** |
| wall row | `dψ/dη\|₀ = 0` (traction-free) | `dφ/dη\|₀ = 0` on `φ = η^{−σ}ψ` (Frobenius analyticity) |
| is the row a boundary condition? | **yes** — it selects one of two regular solutions | **no** — it is an analyticity constraint; the physical selection is the choice of `σ` |
| corpus statement it honours | `vol3/claim-quality.md:123`, `Z_shear → 0` short, *"echoes are predicted"* | **none — it contradicts `:123` at the wall** |

Frozen: `the RHO-B wall row DISAGREES with the RHO-A row in kind and not only in value: RHO-A's is a boundary condition at an ordinary point selecting one of two regular solutions, RHO-B's is an analyticity constraint at a regular singular point whose physical content is carried by the branch exponent; the RHO-B impedance divergence contradicts vol3/claim-quality.md:123's Z_shear -> 0 short verbatim, that contradiction is SURFACED and not repaired, and no leaf is edited by this lane`.

> **⚑ FLAG-CANON, raised at freeze and NOT adjudicated.** [`vol3/claim-quality.md:122`](../manuscript/ave-kb/vol3/claim-quality.md) writes `$Z_{shear} = \rho\,c_{shear} \to 0 \Rightarrow \Gamma_{shear} = -1$` with an **unnamed** `ρ` (the #814 CF-7 gap), and **`:124` of the same bullet list** writes *"$\rho_{eff} \to \infty$ as $\varepsilon_{11} \to 1$"*. **Substituting the leaf's own `:124` density into the leaf's own `:122` impedance formula inverts `:122`'s conclusion from `Γ_shear = −1` to `Γ_shear = +1`.** Both lines verified two-method at this freeze. **This lane surfaces the tension with both line numbers and both verbatim quotes, repairs neither, and prefers neither.** It is routed to Grant and the auditor lane as `FLAG-CANON` (§10).

### §2.6 What is imposable in this instrument class, disclosed BEFORE the run

**ROW-BOUND is cleanly imposable.** Factoring `η^{σ₊}` sends the other branch to `η^{σ₋−σ₊} = η^{−Δ}` with `Re Δ > 0` — **unbounded**, hence excluded by a polynomial function space exactly as the ingoing branch at infinity is excluded by the essential singularity there. `φ` is then analytic on `[0,1]` (the exponents are non-resonant generically) and **Chebyshev convergence is spectral.**

**ROW-IN is only ALGEBRAICALLY clean, and that is disclosed in advance rather than discovered.** Factoring `η^{σ₋}` sends the other branch to `η^{+Δ}`, which **vanishes** at `η = 0` and is therefore *not* excluded by boundedness. It is `C^k` with `k = floor(Re Δ)` and infinitely oscillatory (`η^{ReΔ}e^{i ImΔ ln η}`), so a polynomial basis represents it with **algebraic** error `~ n^{−(2ReΔ+1)}` rather than excluding it. Frozen: `ROW-IN's branch selection is imposed by function-space membership only to ALGEBRAIC accuracy, because the rejected branch behaves as eta^(+Delta) with Re Delta > 0 and is approximable rather than excluded; this is disclosed BEFORE the run, ROW-IN's convergence gate is frozen at an algebraic tolerance derived in section 4.5 rather than at ROW-BOUND's spectral one, and a ROW-IN certification may NOT be presented as equal in strength to a ROW-BOUND one`.

**A THIRD, UNFACTORED instrument is run as the seeding path and as an independent check on ROW-BOUND.** Discretizing `ψ` directly with the row `ψ(0) = 0` — which is the `η²`-multiplied equation evaluated at `η = 0`, since `η²𝒞 → Ω²` and `Ω ≠ 0` — keeps the operator a **quadratic matrix pencil** in `Ω`, so v2.4's double-precision companion-linearization seeding path and its isolation measurement carry over unchanged. Frozen: `the unfactored instrument's wall row psi(0) = 0 is DERIVED as the eta = 0 limit of the eta^2-multiplied equation given Om != 0, it is the discrete surrogate for retaining the sigma_+ branch, its convergence is ALGEBRAIC because eta^(sigma_+) is not analytic, and its role is (i) to supply the quadratic pencil the seeding and isolation gates need and (ii) to be an independent check on the Frobenius instrument's ROW-BOUND root`.

---

## §3 — IMPORT LEDGER (every number the instrument consumes, tagged; `substrate-first-for-numbers`)

| # | Input | Value / form | Class | Source (verified two-method at this freeze) |
|---|---|---|---|---|
| **K1** | Saturation-wall radius | `r_sat = 7GM/c² = 7 M_g`, `x_sat = 7` | **`[canon]`** — form-derived, **VALUE rides the GR-imported `ν_vac`** | `vol3/claim-quality.md:121`; provenance `one-seventh-impedance-projection.md:18` |
| **K2** | Saturation amplitude profile | `A(r) = ε_11/ε_yield = r_sat/r`, `ε_yield = 1` | **`[canon]`** | `saturating-modulus-and-backreaction.md:51` |
| **K3** | Ax-4 kernel | `S(A) = (1 − A²)^{1/2}` | **`[canon]` — Axiom 4** | `saturating-modulus-and-backreaction.md:52` |
| **K4** | Shear modulus grading | `μ(r) = G_vac·S` | **`[canon, μ-PRIMARY reading FROZEN in §2.2]`** | `saturating-modulus-and-backreaction.md:60`; `vol3/claim-quality.md:123` |
| **K5 ★** | **Shear-wave inertia — THE FORK UNDER TEST** | `ρ_eff = ρ_bulk/S³` (**RHO-B**, FORK-3(b)) | **`[canon, UNDER-DETERMINED grading — the object of this lane]`** | `saturating-modulus-and-backreaction.md:73`, verbatim *"$\rho_{\text{eff}}=\rho_0/S_{\text{topo}}^3$ with $S_{\text{topo}}=\sqrt{1-\varepsilon_{11}^2}\to0$"*; `interior-singularity-resolution.md:19`–`:21`; `vol3/claim-quality.md:124` |
| **K6** | Inertia, control branch | `ρ(r) = ρ_bulk` (**RHO-A**) | **`[canon, v2.4's I5]`** — consumed by the NEGATIVE CONTROL only | `vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md:21`; `vol3/claim-quality.md:122` |
| **K7 ★** | Wall condition | **DERIVED here per branch** (§2.5): `dφ/dη\|₀ = 0` on `φ = η^{−σ}ψ`, `σ ∈ {σ₊, σ₋}` | **`[DERIVED from the RHO-B indicial analysis; NOT imported from RHO-A]`** | §2.4, §2.5 |
| **K8** | Outer boundary condition | outgoing radiation into the cold matched lattice | **`[canon]` — Regime-I radiative port, Ax-3-licensed. DERIVED from the RHO-B profile in §2.3, not assumed** | §2.3 |
| **K9** | Angular index | `ℓ = 2` (quadrupole) | **`[canon, INPUT not derived]`** | §1.3 Y1 |
| **K10** | Unit choice | `M_g = 1`, `c₀ = 1`, `ρ_bulk = 1`, `G_vac = 1` | **`[dimensionless by construction]`** | this lane |
| **K11** | `ν_vac = 2/7` | imported **read-only** from `ave.core.constants.N_NU`; reported only as context | **`[canon]` — VALUE GR-IMPORTED (PR #261/#506)** | `src/ave/core/constants.py:397` |
| **K12** | GR cold comparator | `ω_R M`, `ω_I M` at `a_* = 0`, read **PROGRAMMATICALLY** from the frozen `KERR_QNM` dict | **`[GR-IMPORTED comparator — the frozen C-comparator, unchanged from v1/v2.1/v2.2/v2.4]`** | `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51` |
| **K13 ★** | **The certified RHO-A axial root** | `Ω_A`, `ω_R M_g(A)`, `Q(A)` — read **PROGRAMMATICALLY** from the merged in-repo JSON, never transcribed | **`[IN-REPO CERTIFIED PRIOR-LANE RESULT — the seed, the `BIN-B-P3` comparator and the `G-NC(b)` target]`** | `research/drivers/coldq_pole_v2p4_root_results.json` |
| **K14** | Prior-lane discretization artifact | `Ω_art`, read **PROGRAMMATICALLY** from the read-only-imported v2.4 driver's frozen constant | **`[PRIOR-LANE FIREABILITY TARGET — FT-5 only]`** | `research/drivers/coldq_pole_v2p4_root.py` module constant |
| **K15** | Corpus `Q` convention | `Q = ℓ = 2` | **`[corpus comparator — the object under test]`** | `vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md`; #814 CF-9 |
| **K16** | Instrument numerics | Chebyshev order `n`, gauge `λ`, mp `dps`, polish tolerance/cap, dedupe radius, `R_iso`, the convergence-law floors, the `n`-stability threshold | **`[ENGINEERING CHOICE — tagged, frozen in §4]`** | this lane |

**R8 audit rule (frozen).** `every number the instrument consumes appears on this ledger with its tag; no SM/GR convention default enters anywhere, and in particular no spin-1 vector-multipole impedance, no Chu/Collin-Rothschild stored-energy weighting, no Regge-Wheeler and no Zerilli potential is used as an input, a seed, a comparator or a check`.

**★ Ledger discipline note, stated at freeze.** `K13` is a **certified** in-repo value and is nonetheless used **only** as a seed, as the `G-NC(b)` regression target and as the `BIN-B-P3` comparator — **never as a tolerance and never as a band**. `K14` is produced by an instrument that banked it as an ARTIFACT and is used only as a self-test target. Frozen: `no gate tolerance, no convergence-law floor and no bin boundary in this lane is set from any prior-lane MEASURED value; the bin boundaries are byte-identical to v2.4's frozen ones and the tolerances are derived in section 4.5 from the arithmetic of the method, from the derived endpoint regularity class, or carried unchanged from v2.4 with the carry named`.

---

## §4 — THE METHOD AND ITS FROZEN NUMERICS

### §4.1 The method (frozen)

Frozen: `the method is a compactified hyperboloidal Chebyshev spectral discretization in the Axiom-4 amplitude coordinate A = r_sat/r under A = 1 - eta^2, with the outgoing wave divided out in closed form, the RHO-B wall handled by an EXACT Frobenius factoring psi = eta^sigma phi whose exponent solves the derived indicial equation sigma*(sigma-1) + Om^2 = 0, the derived row dphi/deta = 0 imposed exactly at eta = 0, no boundary condition imposed at infinity, root extraction by extended-precision determinant polish, and eigenfunction extraction by extended-precision inverse iteration; there is no matching radius, no asymptotic series, no shooting, no subdominant-coefficient extraction, no regularized modulus floor and NO ARGUMENT-PRINCIPLE WINDING anywhere in the chain`.

**ENGINEERING-CHOICE TAG.** Frozen: `the discretization is NUMERICS and is tagged ENGINEERING CHOICE; the medium, the profile, the Ax-4 kernel, the two gradings, the derived wall rows and the radiative port are CANON or DERIVED; no physical content of any kind is derived from the choice of discretization, and the gauge lambda, the Chebyshev order n, the mp dps, the polish tolerance, the isolation radius and the convergence-law floors are engineering knobs whose only permitted role is to be varied and shown not to move the answer`.

**★ THE ONE STRUCTURAL DEPARTURE FROM v2.4, DISCLOSED.** Because `σ(Ω)` is transcendental in `Ω`, the Frobenius operator is **NOT a polynomial matrix pencil** and cannot be companion-linearized. Frozen: `the Frobenius-factored operator is transcendental in Om and admits no companion linearization, so seeding and the isolation measurement are performed on the UNFACTORED quadratic pencil (CFG-BOUND-POLY) and the Frobenius configurations are polished by mp secant from that seed; this is disclosed as a real reduction in what the isolation gate covers — G5 certifies isolation for the POLY instrument only and NO isolation claim of any kind is made for the Frobenius configurations`.

### §4.2 Frozen numerics (every parameter fixed here, before any code)

```
N_PRIMARY        = 48
N_LADDER         = (32, 48, 64, 80)      full ladder: G4(b), G5, FT-5
N_LADDER_CERT    = (32, 48, 64)          certification ladder, measured against N_REF
N_REF            = 80
LAMBDA_PRIMARY   = 0.0
LAMBDA_SET       = (-0.25, 0.0, +0.25)
DPS              = 50
DPS_HIGH         = 80
DPS_FT4          = 20
POLISH_TOL_EXP   = 38
POLISH_ITERS     = 60
INVIT_ROUNDS     = 4
DEDUPE_REL       = 1e-6
R_ISO            = 0.5
X_SAT            = 7.0
X_SAT_SET        = (5.0, 7.0, 11.0)
ELL              = 2
N_UNDER          = 8                     under-resolved order, FT-2 / FT-4(b)
OMEGA_FTW        = 0.5                   FT-W's degenerate trial exponent point
NSTABLE_REL      = 1e-3                  the seed-sweep n-stability threshold
RESONANCE_GUARD  = 1e-3                  G-W(iv) Frobenius non-resonance margin
RUNTIME_BUDGET_S = 7200.0
```

Frozen: `no gate, tolerance, band, frozen numeric parameter, bin boundary or method element in sections 4, 5, 6 and 7 may be changed after any gate result is seen; if a configuration fails certification this lane reports ROOT-NOT-CERTIFIED for that configuration, adjudicates NO physics bin for it, and routes to a successor with a new version number`.

### §4.3 The configuration matrix — frozen, with the roles named in advance

| tag | inertia | wall row | role |
|---|---|---|---|
| **`CFG-A-CONTROL`** | RHO-A | `dψ/dη\|₀ = 0` (v2.4's) | **NEGATIVE CONTROL ONLY.** No physics bin. Must reproduce v2.4's certified root or the lane STOPS. |
| **`CFG-BOUND-FROB`** | RHO-B | Frobenius `σ₊`, `dφ/dη\|₀ = 0` | **CO-PRIMARY** |
| **`CFG-IN-FROB`** | RHO-B | Frobenius `σ₋`, `dφ/dη\|₀ = 0` | **CO-PRIMARY** (algebraic-accuracy only, §2.6) |
| **`CFG-BOUND-POLY`** | RHO-B | `ψ(0) = 0` | **SEEDING + INDEPENDENT CROSS-CHECK** of `CFG-BOUND-FROB`. No independent bin. |

Frozen: `the two derived RHO-B wall branches are CO-PRIMARY and neither is preferred; if CFG-BOUND-FROB and CFG-IN-FROB return different verdicts on any bin, that bin is reported as BRANCH-DEPENDENT, both verdicts are printed, and the bin is routed to Grant as an open adjudication rather than collapsed to one number`.

**★ THE STOP RULE, frozen, and it is unconditional.** Frozen: `if the negative control CFG-A-CONTROL fails either limb of G-NC, this lane STOPS, produces NO RHO-B number of any kind, reports the failure with both values, and adjudicates nothing; a RHO-B measurement produced by an instrument that cannot reproduce the certified RHO-A root is worthless and this lane will not produce one`.

### §4.4 The seed rule and the independent seed sweep — frozen BEFORE any run

1. **Primary seed:** v2.4's certified root, read programmatically (`K13`). The `CFG-BOUND-POLY` pencil eigenvalue **nearest** that seed is polished; the Frobenius configurations are then polished from the POLY result.
2. **Independent sweep:** ALL `CFG-BOUND-POLY` pencil eigenvalues in the physical quadrant (`Re Ω > 0`, `Im Ω < 0`) with `|Ω| ≤ 8`, deduped at `DEDUPE_REL`, filtered to those **`n`-stable** between `n = 48` and `n = 80` at `NSTABLE_REL`, ordered by decreasing `Re/(2|Im|)`, top **five** reported.

Frozen: `the seed-selection rule and the independent physical-quadrant sweep are frozen here before any code exists; the sweep's output is REPORTED whether or not it agrees with the primary seed's root, it makes NO completeness claim and NO mode count, and if the sweep's top candidate differs from the primary-seeded root the result doc prints both and says so`.

### §4.5 ★ WHERE EVERY TOLERANCE COMES FROM — derived, with ZERO pre-freeze computation on this instrument

> **★ DISCLOSURE.** **This lane ran NOTHING before this document was frozen.** No operator was assembled, no eigenvalue computed, estimated, seeded or looked at. The only arithmetic performed before the freeze is the **symbolic** algebra of §2 — the coefficient transformation, the indicial equation, and the Frobenius row — all of which is reproduced by the driver and machine-checked. **The risk is disclosed and accepted:** a tolerance derived rather than scouted can be wrong, and if it is, the gate FAILS and the configuration is reported `ROOT-NOT-CERTIFIED`. **It will not be retuned.**

| gate | tolerance | derivation |
|---|---|---|
| **G-NC(a)** | `1e-40` | both operators are built in mp at `dps = 50` from the same closed forms; the arithmetic floor is `~1e-50`; `1e-40` sits ten orders above it |
| **G-NC(b)** | `1e-30` | both polishes terminate at `1e-38` relative and the shipped root is a 40-digit mp string; `1e-30` sits eight orders above the achievable agreement |
| **G0** | `1e-13` | the `𝓛_η ≡ 4η²𝓛_A` identity in double-precision probe arithmetic; v2.4 measured `1.0385e-15` on the RHO-A limb of the identical identity, and `1e-13` sits ~2 orders above the worst prior evidence on the same construction |
| **G-IND** | `1e-30` | `\|σ(σ−1) + Ω²\|` evaluated in mp from the polished root; both inputs carry `~1e-38` relative accuracy; `1e-30` is eight orders above |
| **G-FROB** | ratio `≤ 1e-9` | the derived bracket vanishes **linearly** in `η`, so evaluating at `η = 1e-5` and `η = 1e-15` must give a ratio `≤ 1e-10` exactly; `1e-9` carries one order of headroom against mp rounding |
| **G-W** | booleans + `RESONANCE_GUARD = 1e-3` | all four limbs are exact inequalities on the derived exponents; the resonance guard is an **engineering choice** sized so that a Frobenius log term (which enters only at integer exponent difference) cannot be within `1e-3` of the measured `Δ` unnoticed |
| **G1** | `1e-20` | carried unchanged from v2.4, where it was derived from the `1e-38` polish termination and `50`-digit mp against an `O(n⁴)` conditioning; v2.4 measured `4.7268e-50` |
| **G2** `CFG-BOUND-FROB` | `1e-10` | **carried unchanged from v2.4's G2.** `φ` is analytic on `[0,1]` under the `σ₊` factoring (§2.6), so the same spectral class applies and the same tolerance is honest |
| **G2** `CFG-IN-FROB`, `CFG-BOUND-POLY` | `1e-3` | **DERIVED FROM THE ENDPOINT REGULARITY CLASS, AND DISCLOSED AS LOOSE.** Both carry a non-analytic `η^{ρ}` endpoint, so the error decays **algebraically** as `n^{−(2ρ+1)}`. At the certification ladder's coarsest rung `n = 32` with the frozen floor `p = 1.0`, the worst admissible separation is `O(1/32) ≈ 3e-2`; `1e-3` is therefore a **stricter** requirement than the frozen law floor guarantees, chosen so the gate can genuinely fail |
| **G2c** law floors | `p ≥ 1.0` (algebraic configs), `c ≥ 1.0` (spectral config), `max\|resid\| ≤ 0.60` | the floors are **existence-of-decay** thresholds, not rate targets: `p ≥ 1.0` is the weakest genuine algebraic decay and `c ≥ 1.0` is the polar lane's own in-repo-derived non-convergence floor; the residual floor is v2.4's `0.40` widened to `0.60` because a three-rung fit of a two-parameter law has one degree of freedom, and the widening is an **engineering choice**, tagged |
| **G3** | `1e-10` (spectral), `1e-3` (algebraic) | `λ` enters only `O(η²)` terms of `𝒞` and therefore **cannot** change `σ` (§2.4(c)); the gauge-independence residual is bounded by the same convergence class as G2 |
| **G4(a)** | `1e-25` | carried unchanged from v2.4: the polish terminates at `1e-38` relative, so `dps 50` vs `80` cannot differ by more than `~1e-38`; `1e-25` is 13 orders above |
| **G4(b)** | `1e-6` | carried unchanged from v2.4: the double-precision-operator floor was measured there at `1.7559e-08` over the same ladder |
| **G5** | `R_iso = 0.5`, count `== 1` | carried unchanged from v2.4, whose four receipts are **recomputed by this driver** relative to **this lane's** located root and shipped, not asserted |
| **G8** | `1e-9` | carried unchanged from v1/v2.1/v2.2/v2.4. `r_sat` enters the discretized operator only through `A = r_sat/r` and `Ω = ω r_sat`, so the cancellation is structural and the gate measures the arithmetic path — which is why **FT-8 is mandatory** |
| **G10(a)/(b)** | `1e-40` / `1e-20` | (a) the RHO-B `Ω²`-coefficient `4(1+S²)/(η²u⁴)` is **manifestly real**, exactly as RHO-A's `4η/(u(1+S))` is, so the reality structure is unchanged and the tolerance catches a structural transcription error; (b) both mirror-pair members are polished to `1e-38` relative independently |
| **G-AGREE** | `1e-3` | **DISCLOSED AS LOOSE AND DERIVED.** It compares an algebraically-convergent instrument (`CFG-BOUND-POLY`) to a spectrally-convergent one (`CFG-BOUND-FROB`); the honest bound is the algebraic instrument's own convergence class, i.e. G2's `1e-3` |

### §4.6 Determinism, and the G9 successor instruction

Frozen: `this driver emits NO pass field for G9; it ships the run digest and the note only, the certification tally cannot read a G9 pass flag because none exists, and G9's verdict is obtained solely by the external two-run diff recorded in the result doc` — executing the successor instruction v2.4's own merged result doc routed and the polar lane honoured.

---

## §5 — THE GATES (frozen; an UNRUN gate is NOT a passed gate)

**Frozen:** `a gate that was never run cannot be counted as passed; the shipped results object MUST record a _certification_scope block naming every gate as RUN or UNRUN, and the result doc MUST print the UNRUN set explicitly; the certification tally counts only RUN gates and any UNRUN gate makes the affected configuration ROOT-NOT-CERTIFIED`.

| gate | what it certifies | frozen tolerance | configurations |
|---|---|---|---|
| **G-NC(a)** ★ | **NEGATIVE CONTROL, operator level** — this lane's RHO-A mp operator entry-by-entry against v2.4's `graded_matrices_mp`, imported read-only | `1e-40` | `CFG-A-CONTROL` |
| **G-NC(b)** ★ | **NEGATIVE CONTROL, root level** — this lane's RHO-A polished root against v2.4's shipped certified mp root | `1e-30` | `CFG-A-CONTROL` |
| **G0** | operator-transcription identity `𝓛_η ≡ 4η²·𝓛_A` for the RHO-B coefficients, on a frozen analytic probe; **the RHO-A limb of the same identity is evaluated in the same call and must reproduce v2.4's coefficient exactly** | `1e-13` | all |
| **G-IND** ★ | the derived indicial identity `σ(σ−1) + Ω² = 0` at the located root, in mp | `1e-30` | RHO-B |
| **G-FROB** ★ | the derived Frobenius row: the bracket of §2.5 vanishes **linearly** in `η`, measured at `η ∈ {1e-5, 1e-15}` in mp | ratio `≤ 1e-9` | RHO-B |
| **G-W** ★ | the wall classification at the located root: **(i)** `Re σ₊ > 1/2`; **(ii)** `Re σ₋ ≤ 1/2`; **(iii)** `Re(σ₊ − σ₋) > 0`; **(iv)** `min_k \|(σ₊−σ₋) − k\| > RESONANCE_GUARD` over integers `1 ≤ k ≤ 20`. **All four must hold.** The traction exponent `Re σ − 1` is REPORTED for both branches, not gated | booleans | RHO-B |
| **G1** | residual of the certified eigenfunction at the certified root (mp) | `1e-20` | all |
| **G2** | `n`-independence over `N_LADDER_CERT` against `N_REF` | `1e-10` spectral / `1e-3` algebraic | all |
| **G2c** ★ | the convergence LAW, **law-matched to the derived endpoint class**: root-exponential `E(n)=C·exp(−c√n)` for `CFG-BOUND-FROB`; power-law `E(n)=C·n^{−p}` for the two algebraic configurations | `c ≥ 1.0` / `p ≥ 1.0`, and `max\|resid\| ≤ 0.60` | all |
| **G3** | hyperboloidal-gauge independence over `LAMBDA_SET` | `1e-10` spectral / `1e-3` algebraic | all |
| **G4** | (a) `dps 50` vs `80`; (b) double pencil vs mp at every rung of `N_LADDER` | `1e-25` / `1e-6` | `CFG-BOUND-POLY`, `CFG-A-CONTROL` |
| **G5** | **ISOLATION** — pencil-eigenvalue count within `R_iso` of the located root, full ladder, with the four `R_iso` receipts recomputed and shipped | exactly `1` | `CFG-BOUND-POLY`, `CFG-A-CONTROL` |
| **G8** | `x_sat` cancellation at the root, mp end-to-end, over `X_SAT_SET` | `1e-9` | all |
| **G10** | Ax-3: (a) operator reality structure; (b) conjugate-mirror symmetry `Ω ↦ −conj(Ω)` | `1e-40` / `1e-20` | all |
| **G-AGREE** ★ | **TWO-INSTRUMENT AGREEMENT on ROW-BOUND** — `CFG-BOUND-POLY` against `CFG-BOUND-FROB`; genuinely different-in-kind at the endpoint (one approximates the branch, the other resolves it exactly) | `1e-3` | ROW-BOUND pair |

**Frozen scope of G-AGREE:** `G-AGREE is a two-instrument agreement on the ROW-BOUND branch ONLY; there is NO second instrument for ROW-IN, no agreement gate exists for it, and no ROW-IN number in this lane carries cross-instrument corroboration of any kind`.

---

## §6 — THE FIREABILITY SELF-TESTS (each MUST fire; a gate that cannot fail is not a gate)

| self-test | mutation | targets | frozen firing threshold |
|---|---|---|---|
| **FT-NC** ★ | flip the inertia switch to RHO-B inside the negative control | G-NC(b) | `≥ 1e-30` |
| **FT-0** | corrupt `𝒞`'s `Ω`-free part by `1e-12` | G0 | `≥ 1e-13` |
| **FT-1** | evaluate the residual at `Ω*(1 + 1e-10)` | G1 | `≥ 1e-20` |
| **FT-2** | under-resolved `n = N_UNDER` | G2 | `≥ 1e-3` |
| **FT-2c** | stagnation: add `1e-12` to every non-reference rung's separation | G2c | fitted law parameter must fall **below** its frozen floor |
| **FT-3** | correctly-specified half-applied gauge (`λ` applied to the factoring but not to the coefficients) | G3 | `≥ 1e-3` |
| **FT-4** | (a) `dps = DPS_FT4`; (b) double pencil at `n = N_UNDER` vs mp at `N_PRIMARY` | G4 | `≥ 1e-25` / `≥ 1e-6` |
| **FT-5** | isolation pointed at the v2.1-banked artifact `Ω_art` (`K14`, read programmatically) | G5 | count `≠ 1` at ≥ 1 order |
| **FT-8** | `x_sat`-dependent profile perturbation | G8 | `≥ 1e-9` |
| **FT-10** | smuggled `Im(μ)/Re(μ) = 1e-3` | G10 | `≥ 1e-6` |
| **FT-W** ★ | evaluate the wall classifier at the degenerate trial point `Ω = OMEGA_FTW = 0.5`, where `sqrt(1 − 4Ω²) = 0` exactly | G-W | limbs **(iii)** and **(iv)** must both FAIL |
| **FT-SHORT** ★★ | **impose the RHO-A traction-free row `dψ/dη\|₀ = 0` on the RHO-B operator** — the row §2.4(d) rejects by derivation | the wall row itself | the located root must differ from the `CFG-BOUND-POLY` root by `≥ 1e-2` relative |

**FT-SHORT is the load-bearing self-test of this lane and it is written as one.** Frozen: `FT-SHORT exists to demonstrate that the RHO-B wall row is LOAD-BEARING rather than cosmetic: if imposing the rejected RHO-A traction-free row on the RHO-B operator moved the root by less than 1e-2 relative, then the wall-row derivation of section 2.5 would be doing no work and this lane's central claim — that RHO-B changes the wall in KIND and not only in value — would be unsupported by its own instrument; that outcome is pre-registered as a FAILURE TO FIRE and would make every RHO-B configuration ROOT-NOT-CERTIFIED`.

**Ordering rule, frozen:** `each gate's self-test is executed and recorded in the same block, BEFORE the gate's own measurement is read`.

---

## §7 — THE OUTCOME CLASSES (frozen; exhaustive; each reachable)

**PRECEDENCE (frozen, evaluated in this order, PER CONFIGURATION).** `BIN-B-N` > `BIN-B-W` > `BIN-B-S` > `BIN-B-P1 / BIN-B-P2 / BIN-B-P3`. If an earlier bin fires, the later ones are reported `N/A — not adjudicated` and **no verdict language is used about them**. `BIN-B-4` is `N/A BY CONSTRUCTION` at every precedence level.

### §7.1 The honest-failure bins

| bin | condition | disposition |
|---|---|---|
| **`BIN-B-N`** | `no root is located for that configuration, or no located root is n-stable between n = 48 and n = 80 at NSTABLE_REL` | **A clean negative.** Classified **ARTIFACT-class** if the shipped diagnostics trace it to the instrument's function space (§0), **PHYSICS-class** only if they do not. Both readings are printed and the classification is stated. No physics bin adjudicated. |
| **`BIN-B-W`** ★ | `the wall classification G-W fails at the located root — the RHO-B wall admits no uniquely selectable branch (resonant exponents, or a degenerate/limit-circle classification)` | **An HONEST RESULT, not an instrument failure.** This is the axial instantiation of the polar lane's pre-registered `BIN-PF-WALLSING`. It would say the RHO-B wall does not determine a boundary condition, which is a statement about the RHO-B grading. Routed to Grant; no physics bin adjudicated. |
| **`BIN-B-S`** | `any RUN gate FAILS, or any self-test fails to fire, or any gate is UNRUN, for that configuration` | **`ROOT-NOT-CERTIFIED`** for that configuration. Numbers reported; no physics bin adjudicated; no retune; routes to a successor with a new version number. |
| **`BIN-B-STOP`** | `the negative control CFG-A-CONTROL fails G-NC` | **THE LANE STOPS.** No RHO-B number is produced at all (§4.3 stop rule). |

### §7.2 `BIN-B-P1` — the real part `ω_R M_g` (boundaries byte-identical to v2.4 §7.2)

`D_omega ≡ omega_R_derived / omega_R_GR − 1`, `omega_R_GR` read programmatically (`K12`).

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-B-P1-MATCH`** | `abs(D_omega) < 0.03` |
| **`BIN-B-P1-NEAR`** | `0.03 <= abs(D_omega) < 0.10` |
| **`BIN-B-P1-MISS`** | `abs(D_omega) >= 0.10` |

**Class line (mandatory in the result headline):** `BIN-B-P1 is VALUE-CONSISTENCY class, not emergence: omega_R*M_g carries the GR-imported nu_vac through the 7 in r_sat`.

### §7.3 `BIN-B-P2` — the quality factor `Q` (★ the `ν_vac`-free, emergence-capable axis)

`Q_derived ≡ Re(Ω)/(2·abs(Im(Ω)))`; `Q_GR` formed programmatically from the `K12` pair; `D_Q ≡ Q_derived/Q_GR − 1`.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-B-P2-MATCH`** | `abs(D_Q) < 0.03` |
| **`BIN-B-P2-NEAR`** | `0.03 <= abs(D_Q) < 0.10` |
| **`BIN-B-P2-MISS`** | `abs(D_Q) >= 0.10` |

Three-way discriminator, frozen separately and byte-identical to v2.4 §7.3:

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-B-P2-CLOSER-GR`** | `abs(Q_derived - Q_GR) < abs(Q_derived - 2.0)` |
| **`BIN-B-P2-CLOSER-CONVENTION`** | `abs(Q_derived - 2.0) < abs(Q_derived - Q_GR)` |
| **`BIN-B-P2-EQUIDISTANT`** | `abs(abs(Q_derived - Q_GR) - abs(Q_derived - 2.0)) <= 1e-6` |

**Class line (mandatory in the result headline):** `BIN-B-P2 is the nu_vac-FREE axis: Q = Re(Omega)/(2*abs(Im(Omega))) contains no r_sat scale, so the GR-imported 7 cancels exactly`.

### §7.4 ★ `BIN-B-P3` — THE FORK DISCRIMINATOR, which is what this lane exists to produce

**Does FORK-3(b) move the `ℓ = 2` pole toward GR, away from it, or nowhere?** Both `D`s are computed from the SAME programmatic comparators for both inertia readings, with the RHO-A values read from `K13`.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-B-P3-RESCUE-BOTH`** | `abs(D_omega_B) < abs(D_omega_A)` **and** `abs(D_Q_B) < abs(D_Q_A)` |
| **`BIN-B-P3-RESCUE-PARTIAL`** | exactly one of the two strict inequalities holds |
| **`BIN-B-P3-WORSE-BOTH`** | `abs(D_omega_B) > abs(D_omega_A)` **and** `abs(D_Q_B) > abs(D_Q_A)` |
| **`BIN-B-P3-NEUTRAL`** | `abs(abs(D_omega_B) - abs(D_omega_A)) <= 1e-6` **and** `abs(abs(D_Q_B) - abs(D_Q_A)) <= 1e-6` |

**And the decisive sub-flag, frozen:** `BIN-B-P3-RESCUE-DECISIVE fires if and only if BIN-B-P3-RESCUE-BOTH fires AND both abs(D_omega_B) < 0.10 and abs(D_Q_B) < 0.10, i.e. FORK-3(b) converts BOTH of v2.4's misses into non-misses; anything short of that is NOT a rescue of the v2.4 result and the result doc may not describe it as one`.

**And the reciprocal statement, frozen so a negative is read as a negative:** `if BIN-B-P3 lands WORSE-BOTH or NEUTRAL, then FORK-3(b) is NOT the explanation of v2.4's BIN-1/BIN-2 misses, v2.4's FLAG-4 debt is DISCHARGED by this lane, and the misses stand against the profile with one fewer escape route; that is a GOOD outcome and is recorded as such rather than as a disappointment`.

### §7.5 `BIN-B-4` — `N/A BY CONSTRUCTION`

Frozen: `BIN-B-4 is N/A BY CONSTRUCTION in this lane and is not adjudicated at any precedence level including a full gate pass; no overtone, no ladder, no mode count and no completeness statement is computed, and the deferral is an open instrument-scope question awaiting a substrate-derived low-frequency cutoff, not a failure of this lane`.

### §7.6 Reachability audit (frozen)

- `BIN-B-STOP` is reachable: the negative control either reproduces the certified root at `1e-30` or it does not.
- `BIN-B-N` is reachable: the polar lane's RHO-B configuration returned exactly this outcome in a different instrument class.
- `BIN-B-W` is reachable: `G-W`'s four limbs are exact inequalities on `Ω`, and **FT-W demonstrates reachability every run** by exhibiting an `Ω` at which two of them fail.
- `BIN-B-S` is reachable and is **demonstrated reachable every run**: every self-test drives an actual gate into its failing state.
- `BIN-B-P1/P2/P3` sub-bins are each reachable because each is an interval or a strict comparison on a continuously-valued measured quantity, and the intervals **partition** their axis with no gaps and no overlaps.
- **No outcome requires a criterion to be relaxed after the fact.**

### §7.7 ★ PREDICTABILITY DISCLOSURE — what this lane does and does not know in advance

**This lane knows the DERIVED structure in advance and says so here: the wall's order changes, the impedance's divergence flips sign, and the optical distance becomes infinite. All three are theorems of §2 and none of them is a measurement.** What this lane does **not** know in advance is **where the pole lands**, whether a pole exists at all under either derived row, or which way `BIN-B-P3` falls. Frozen: `the derived wall statements of section 2 are theorems available before the run and may NOT be presented in the result doc as discoveries of the instrument; the located root, its bin verdicts and the BIN-B-P3 direction are genuinely unknown at this freeze and are the only outputs this lane may present as measurements`.

---

## §8 — WHAT TRANSFERS, AND WHAT MUST BE RE-EARNED

**TRANSFERS (cited, not silently absorbed):** the ratified physics framing (transmission-line reading, graded profile, radiative port, spin-2 channel, `Q` as a pole); the compactified formulation and its exact `A = 1 − η²` substitution, **as algebra re-verified by G0 every run**; the **shape** of the certification battery; the frozen-first commit order; the **bin boundaries** of `BIN-B-P1`/`BIN-B-P2`, byte-identical to v2.4's; the number-check architecture with all six of the polar lane's frozen fixes.

**DOES NOT TRANSFER — must be re-earned (gate in brackets):**
- **the certification.** v2.4 is certified on the RHO-A operator. Every gate is re-run here on this file, per configuration. [all]
- **★ the WALL ROW.** Explicitly NOT inherited. Derived from the RHO-B indicial analysis (§2.5) and demonstrated load-bearing. [G-IND, G-FROB, G-W, FT-SHORT]
- **the shear-speed projection.** Op16's `√S` is superseded on the RHO-B branch by derivation (§2.2). [G0]
- **implementation independence.** Frozen: `this lane carries over v2.4's Chebyshev, mp-LU, polish and inverse-iteration machinery by copy-with-attribution so that the OPERATOR and the WALL ROW are the only variables; it is NOT an independent reimplementation, it claims no reimplementation independence from v2.4, and G-AGREE's two instruments differ in their ENDPOINT TREATMENT and in nothing else`.
- **any completeness statement.** Not re-earned; out of scope.

Frozen: `no gate, tolerance, certification class or measured number is inherited as PASSED from any predecessor lane; the physics framing, the compactified algebra, the bin boundaries and the numerical machinery transfer, the certification does not, and every gate in section 5 is re-earned on this file per configuration`.

---

## §9 — ★ THE DERIVED-CONSEQUENCE APPENDIX (specified HERE, before the run; FLAG OUTPUT ONLY)

The result doc MUST carry an appendix computing, **symbolically and numerically**, the wall behaviour of `Z = sqrt(K·ρ)` and `c = sqrt(K/ρ)` under **both** inertia readings for **both** canon-available bulk-modulus branches, on the frozen grid `S → 0`:

| branch | `K(S)` | canon source |
|---|---|---|
| **BRANCH-STIFF** | `K = 2G_vac/S` (the `D = 1/S` stiffening branch) | `saturating-modulus-and-backreaction.md:59`, verbatim *"**BULK stiffens:** $D=1/S\to\infty$ at $A\to1$ (the modulus goes rigid, halting the collapse)."* |
| **BRANCH-SOFT** | `K = 2G_vac·S` (the `K = 2G`-tracking branch) | `bulk-impedance-at-saturation-boundary.md:31`, verbatim *"$c_{bulk} \to 0$ (bulk dilatational speed vanishes at snap / rupture)"* with `Z_bulk = ρ_bulk c_bulk → 0`; `K = 2G` provenance PR #261 |

**Frozen appendix rules, all four binding:**

1. **It is FLAG OUTPUT ONLY.** Frozen: `the section 9 appendix repairs nothing, edits no KB leaf, mints no claim, prefers no FLAG-W branch and adjudicates nothing; it exists to feed the core session's FLAG-W walk with a derived arithmetic consequence and its every row is a two-line algebraic substitution that any reader can check`.
2. **It is SHEAR-lane-fenced.** Frozen: `this lane computes no bulk eigenvalue, no polar mode and no coupled system; the appendix is an IMPEDANCE-SIGN computation on canon's own formulas and is not a solve`.
3. **It must print the RHO-A row beside the RHO-B row** for every branch, so the reader sees which conclusions are RHO-A-conditional.
4. **It must name, with line numbers and verbatim quotes, every canon line whose stated conclusion the substitution inverts** — and must state explicitly that no leaf is edited.

**Frozen deliverable:** `the appendix ships a four-row table (two bulk branches x two inertia readings) giving the wall limits of K, rho, c = sqrt(K/rho) and Z = sqrt(K*rho) as exact powers of S, together with the corresponding SHEAR-channel row, and it states in one sentence per row whether the wall VENTS (Z -> 0), JAMS (Z -> infinity) or is INDETERMINATE`.

---

## §10 — FLAG-DON'T-FIX: what is raised at freeze and routed, not resolved

1. **★ `FLAG-CANON` — routed to Grant and the auditor lane.** `vol3/claim-quality.md:122` and `:124` are three bullets apart in one leaf; substituting the second's `ρ_eff → ∞` into the first's `Z_shear = ρ c_shear` inverts the first's `Γ_shear = −1` conclusion. **Both lines verified two-method at this freeze. Neither is repaired. Neither is preferred.** (§2.5.)
2. **★ `FLAG-MU` — the `μ`-primary vs `c`-primary fork inside RHO-B** (§2.2). A choice was forced, it was made by derivation, and the rejected reading is named with the reason. **Routed as an open fork, not presented as settled.**
3. **★ `FLAG-ROWCLASS` — `ROW-IN` is only algebraically imposable in this instrument class** (§2.6). The successor requirement is named: an instrument whose function space **excludes** rather than approximates the `η^{+Δ}` branch — the same exterior-complex-scaling build the polar lane's §6 item 2 and v2.4's FLAG-10 both route. **One build discharges three routings.**
4. **`FLAG-3` carried forward.** The reflectionless Regime-I port is derived **for this profile** (§2.3); a far-field reflector introduced by physics outside the profile is untouched.
5. **`FLAG-5` carried forward, unresolved** — the substrate-derived low-frequency cutoff. `BIN-B-4` stays `N/A BY CONSTRUCTION`.
6. **`FLAG-W` NOT TOUCHED.** Under a live Grant walk in the core session. This lane's §9 appendix is input to that walk and is not a contribution to its adjudication.
7. **v2.4's `BIN-3` plumber question is still owed and is NOT re-asked, NOT answered, and NOT re-measured** (`Y6`).

---

## §11 — VALIDATION REQUIREMENTS (frozen)

- **Determinism.** Two full driver runs; digests must match; shipped objects byte-identical apart from `_runtime_sec`. **G9 emits no `pass` field** (§4.6).
- **The gating number check.** Frozen: `this lane's gating number check implements, from the first commit: (i) a MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, machine-enforced at BOTH the configuration end and the document end; (ii) PER-SITE rather than global dedup, so every occurrence of a numeral is checked and the reported counts describe SITES; (iii) LIST-VALUED REGISTRATION, so a bracketed count vector is matched elementwise against a shipped JSON list rather than decomposed into single-digit tokens; (iv) a NEWLINE-EXCLUDING token pattern, so a fenced code block cannot be consumed as one span and invert back-tick pairing for the remainder of the document; (v) a COMPLETENESS GUARD making any registered key the document never exercises a hard configuration FAIL; and (vi) a DIGEST CLASSIFIER, so run digests are checked against the shipped JSON as tokens in their own class rather than skipped by a numeral regex that never matched them`.
- **Mutation receipt.** The number check must be demonstrated to FAIL on a single-digit drift of at least two distinct registered numerals in the result doc, and the receipts recorded in the docket fragment.
- **Engine fence.** Frozen: `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`.
- **Predecessor fence.** Per §P: empty `git diff --stat` on every predecessor file.
- **Scope, unchanged:** `ℓ = 2` is an input; `ν_vac`, `K = 2G` and the `7` in `r_sat` are GR-imported and untouched; spin is out of scope; the Cosserat microrotational channel is not built; the polar branch is not built; **no completeness or overtone statement of any kind is made.**

---

> **Freeze provenance.** This document is COMMIT 1 of the lane, committed **ALONE** and pushed **before any driver code exists and before any number produced by this instrument exists**. It mints no `clm-`/`def-`, propagates to no KB or manuscript leaf, changes no solidity and edits no falsification ledger, **regardless of outcome**. Predecessor files are byte-untouched; `research/drivers/coldq_pole_v2p4_root.py` is imported read-only as a comparison object.
