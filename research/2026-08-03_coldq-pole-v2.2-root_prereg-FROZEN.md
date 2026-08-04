# The cold-Q pole **v2.2** — FROZEN pre-registration (**ROOT certification, not rectangle survey**)

**Date:** 2026-08-03
**Class:** DERIVATION pre-registration (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger — regardless of outcome**). Committed **ALONE** and pushed **before any driver code and before any number produced by this instrument exists**.
**Result-doc pointer requirement.** The result doc that resolves these bins MUST carry `Prereg-file: research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file (`manuscript/ave-kb/tools/verify-frozen-provenance.py`).
**Provenance:** Grant's ruling of 2026-08-03 on the PR #854 audit's Q2 — **certify the located root, not the rectangle.**
**Written against** `origin/main` = `184db4b6`.

---

## ★ SUPERSESSION NOTE (2026-08-03) — full auditable provenance

*(This section exists because the PR #854 audit's finding 10 was that a supersession note without the audit verdict, the findings it rests on and the ruling that narrowed the target is not auditable. It is written to be auditable without any other document open.)*

### What came before, in order

| lane | prereg | outcome |
|---|---|---|
| **v1 / PR #845** (MERGED, `052ccbba`) | `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` | `SOLVER-NOT-CERTIFIED`. Real-axis asymptotic far-field matching; killed by an asymptotic (divergent) `1/r` series plus an `exp(2\|Im ω\| R_match)`-ill-conditioned subdominant-coefficient extraction. All four bins `N/A`. |
| **v2** (commit `00724432`) | `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` | Frozen and pushed ALONE; **superseded pre-measurement** by v2.1. No driver code, no number. **BYTE-UNTOUCHED and not touched by this lane.** |
| **v2.1** (commit `7d8fe484`) | `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` | Frozen and pushed ALONE. Battery run at `bdcfa678`. `SOLVER-NOT-CERTIFIED` (C1, C9 FAIL; FT-B did not fire). All four bins `N/A`. **BYTE-UNTOUCHED and not touched by this lane.** |

Both predecessor preregs live on branch `research/coldq-pole-v2` (PR #854, **OPEN, DO-NOT-MERGE**) and are **not on `origin/main`**. They are cited here **by commit SHA** so the citation resolves regardless of which branch is checked out, and this lane **edits neither, by any byte**.

### The PR #854 adversarial audit (2026-08-03) — verdict and the findings this lane rests on

**Audit verdict: BLOCKED.** The audit did not impeach the located root. It impeached the *rectangle survey* around it. The three findings that matter here, each carried into the repair commits on the #854 branch and quoted from those commit messages (`git log`, the audit trail per house rule):

1. **Finding 1 (repair commit `0a7dec1f`, "R1") — C9's failure is REAL INSTRUMENT DEGRADATION, not a defective gate spec.** Verbatim from the commit body: *"MECHANISM MEASURED: migrating pseudo-spectrum adjacent to Re Omega ~ 0. In-box pencil eigenvalue count grows 2 -> 9 as n goes 32 -> 80; only Omega = 1.853655 - 1.007257i is n-stable. The instrument manufactures discrete spectrum on the rectangle's low-Re-Omega edge."* The v2.1 result doc's forced-vs-homogeneous mechanism was **measured-refuted** (a homogeneous outgoing probe fails the same 6 of 9 probes at the same magnitudes).
2. **Finding 2 (repair commit `d7c9c564`, "R2") — C1's high-`ℓ` failure is the SAME instrument defect, seen over the high-`|Ω|` box.** Verbatim: *"raising n makes it monotonically WORSE: at ell=6 the in-box SPURIOUS zeros grow 4 -> 32 while correctly-seeded TRUE roots drop 2 -> 1"*, and *"the discretization carries spurious in-box zeros over the high-|Omega| box. SAME PHENOMENON CLASS AS R1 -- two gates, one instrument defect."*
3. **Finding 3 (repair commit `ea4b59ee`, "R3") — C4 and C10 are DE-WEIGHTED.** C4's PASS is *"an ACCIDENT OF THE FROZEN ORDER"* (winding `2.0/2.0/2.0` only at `n ≤ 48`; `3/5/3`, `3/4/14`, `12/4/11` at `n = 56/64/80`), and C10 *"MEASURED THE WRONG QUANTITY'S MARGIN"* — its derived left-edge bound is arithmetic-precision, ~37 orders off the binding constraint, which is **spectral**.

Two further audit items are recorded for completeness and are **repaired at source in this lane rather than inherited**: WARN 4 (`6a93131a`) — v2.1's FT-B was doubly structurally vacuous *and* its driver did not implement the frozen mutation; WARN 5/7 (`21981789`) — v2.1's C9 probe pass-count was `3 of 9` not `5 of 9`, and *"the nu_vac cancellation is EXACT, to the last bit"* was **an artifact of a `complex` cast** (`research/drivers/coldq_pole_v2.py:612`), re-measured at `dps = 50` as `Q` spread `4.466e-47`, `|Ω|` spread `1.381e-46`. **This lane keeps `x_sat` invariance in mp end-to-end (G8) precisely so that the same artifact cannot recur.**

### The ruling, and the target narrowing

**Grant, 2026-08-03**, agreeing with the orchestrator recommendation on the audit's Q2: **certify the located root, not the rectangle.**

The narrowing follows the audit's own logic. The audit's mechanism — a migrating, `n`-dependent pseudo-spectrum on the rectangle's low-`Re Ω` edge and spurious in-box zeros over the high-`|Ω|` box — is a statement about **counting over a region**. It says nothing against the one object every measurement in v2.1 agreed on: **`Ω = 1.853655 − 1.007257i` was the only `n`-stable in-box eigenvalue at every order the audit swept (`n = 32 → 80`), and it agrees with v1's different-in-kind instrument to `6.803232e-07` relative.** That object is what this lane certifies, and the survey around it is what this lane **declines to claim**.

**What is DEFERRED, not failed.** Whether other modes exist — overtones, or a lower-frequency fundamental hiding inside the contaminated edge — is an **open instrument-scope question**. Answering it needs a **substrate-derived low-frequency cutoff** to set the counting region's left edge honestly. That derivation is **not attempted here, is not sketched here, and is not this lane's work.** `BIN-4` is therefore `N/A BY CONSTRUCTION`, declared in advance (§7), and that is a **scoped non-claim, not a failure**.

---

## §0 — SECTOR / REGIME / PHASE-STATE / COORDS header, declared BEFORE any physics word

**Re-walked fresh, not incorporated by reference.** A successor that inherits a header without re-walking it inherits the header's blind spots too.

- **MODE.** Cold (`a_* = 0`, Schwarzschild-limit) post-merger remnant ringing down. The object is **one** quasinormal resonance of the saturation cavity — the `ℓ = 2` toroidal shear mode located by v1 and v2.1 — and **not** its ladder.
- **SECTOR.** The **observable** is a **transverse shear (T2)** oscillation. The **bias field** that builds the cavity is the **A1 radial dilatation** `ε_11 = 7GM/(c²r)`. Orthogonal grades, **not cross-wired**: the A1 strain is the DC operating point that sets the constitutive profile; the T2 shear mode is the small-signal AC riding on it. Receipt for `ε_11` **being** the Axiom-4 amplitude `A`: [`common/vocabulary-register.md:309`](../manuscript/ave-kb/common/vocabulary-register.md), verbatim *"the A1-dilatation **radial "strain"** that IS the Axiom-4 saturation **amplitude $A$**"*.
- **REGIME.** Far field (`r ≫ r_sat`) = **Regime I** — linear, lossless, reactive; a legal radiating port. The graded exterior `r > r_sat` = Regime I with a spatially varying modulus (Op14 grade). The wall `r = r_sat` = the **Regime III→IV** soft-mode terminus, `G_shear → 0`. The interior `r < r_sat` = **Regime IV**, where shear cannot propagate at all and which is therefore **not part of the computational domain** — the domain is `[r_sat, ∞)`, and that is a physics statement, not a truncation.
- **PHASE-STATE.** Op14 ON throughout the graded exterior as a **static constitutive grade** (the DC bias is time-independent; the ringdown is the small-signal response). `A = 1` exactly at `r_sat = 7GM/c²`; `Γ_shear = −1` there.
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the **dimensionless-eigenvalue register** (`ω_R M_g`, `ω_I M_g`, `Q`) that AVE and GR share — no phase-space/real-space mismatch. This lane solves for the **complex pole** directly, so what it returns *is* the pole-`Q` that the GR comparator is; **no port→pole transfer is performed, needed, or assumed.**
- **The eigenfunction's own coordinate.** The radial localization observable (BIN-3) is read in **real-space radius normalized to `r_sat`** and compared only against real-space radii. It is **not** compared against `r_eff = 49M_g/9`, which is a **spectral marker (a cutoff radius), not a place**.

### Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code)

1. **K4 / srs connectivity.** This is a **CONTINUUM** instrument. Frozen disclosure: `the radial channel is a CONTINUUM representation of the shear constitutive law; it is not a discretization of the srs stencil and carries no K4 connectivity claim`. What it consumes from the lattice is the **constitutive law only**: the Ax-4 kernel and the Op16 shear-speed projection.
2. **Cosserat / channel basis.** The mode certified is on the **toroidal (odd-parity / axial) branch**, whose displacement field is **exactly divergence-free**, so the Lamé `λ` (bulk/A1) modulus drops out of the equations of motion **identically** rather than by assumption. Frozen: `the toroidal (odd-parity) branch is exactly divergence-free, so the bulk modulus drops out identically and there is no linear P-SV conversion partner; the single-channel classification is structural in this branch`.
3. **Op14 saturation.** Enters as the **static constitutive grade** `S(A) = sqrt(1 - A²)` with `A(r) = r_sat/r`, projected into shear by Op16. Frozen: `Op14 enters as a static constitutive grade S(A); the A -> 1 terminus is handled by an exact change of variable, not by a numerical cutoff or a regularized floor`.
4. **★ The compactification is the medium's own order parameter, and that is what makes the ROOT-LOCAL gates meaningful.** The radial coordinate is `A = r_sat/r` — the Axiom-4 saturation amplitude itself; `A = 1` IS the wall, `A = 0` IS infinity. Frozen: `the compactified radial coordinate is the Axiom-4 saturation amplitude A = r_sat/r itself, so A = 1 is the wall and A = 0 is infinity; the instrument adopts the medium's own order parameter as its coordinate rather than imposing a lattice-Cartesian one`. **Root-local consequence, stated in advance:** because `r_sat` appears in the discretized operator *only* through this coordinate and through `Ω = ω r_sat`, a root-local `x_sat`-invariance measurement (G8) is a check on the arithmetic path, not on the physics — the physics cancellation is structural. It is gated anyway, in mp, because v2.1's version of this measurement was corrupted by a `complex` cast (audit WARN 7).
5. **Phase-space vs real-space (A46).** Every verdict-class observable is a **dimensionless ratio**: `ω M_g`, `Q`, `r_peak/r_sat`. **α-CLEAN** — `α` appears nowhere in the chain.
6. **Checkpoint: boundary-not-bulk.** The resonator is a **boundary/graded-shell** object, not a bulk-force object — consistent with the #403/#404 localization ruling. The loss is a **radiative port at infinity** (Ax-3-licensed), and there is **no** `Re{Z}` anywhere in the medium. **G10 tests exactly that, and it tests it ON THE CERTIFIED EIGENFUNCTION'S OWN OPERATOR** rather than on a separate closed cavity.
7. **Checkpoint: what the substrate does NOT supply.** The angular index `ℓ = 2` is **not** derived here; it is the quadrupole selection the corpus carries for the GW channel. **And — new in this lane and load-bearing — the substrate does not here supply a low-frequency cutoff either, which is exactly why no completeness claim is made.** Stated so neither is mistaken for an output.

### Pre-test physics check (`pre-test-physics-check`, Rule 16 — ONE plumber question surfaced to Grant BEFORE the design locks)

> **Grant — this is a DIFFERENT question from v1's and v2.1's, and it is the one your ruling creates.** You swept a cavity. Down at the bottom of the sweep the analyzer is showing a cloud of junk that moves every time you change the resolution — that is the audit's migrating pseudo-spectrum, and it is my instrument's junk, not the cavity's. Up at `Ω = 1.85 − 1.01i` there is one marker that does **not** move: same place at every resolution from `n = 32` to `n = 80`, and a completely different instrument (v1's asymptotic-matching rig) put its marker within `6.8e-07` of the same spot. Your ruling says: certify that marker, stop claiming the sweep. **This design does exactly that, and here is what it structurally cannot tell you:** whether that marker is the *fundamental*. If the cavity's true lowest shear resonance sits down inside the junk, my instrument would not be able to see it, and nothing in this lane would notice. **What I need from you, when you want the completeness question answered:** a real low-frequency cutoff for the graded shear cavity that comes from the *medium* — a frequency below which the saturation grade cannot support a propagating shear resonance at all — not a number I pick to make the counting region behave. That is a derivation about the substrate, it is deferred, and this lane does not attempt it, sketch it, or assume it. **If you think the cutoff is something you can already name plumber-physically, say so and it becomes a successor lane's target; if not, `BIN-4` stays `N/A` for as long as it takes.**

### Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE any result — and it is not uniform across the bins

Written in units of `r_sat`, the problem has **no free parameter at all**: the profile is `A = r_sat/r`; the kernel is `S = sqrt(1 - A²)`; the speed is `c_shear = c₀·sqrt(S)`; the inertia is the cold `ρ₀`. Therefore `Ω ≡ ω·r_sat/c₀` is a **pure number** fixed by the profile SHAPE, the Ax-4 kernel, and `ℓ`.

| output | rides `r_sat`'s coefficient `7`? | class |
|---|---|---|
| `ω_R M_g` (BIN-1) | **YES** — `ω_R M_g = Re(Ω)/x_sat` with `x_sat = 7` | **VALUE-CONSISTENCY.** The `7` is the `1/7` trace-reversed bulk projection, which takes `ν_vac = 2/7` as **input** ([`one-seventh-impedance-projection.md:18`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md): *"the $1/7$ boundary is a projection of a GR-imported ratio, not a first-principles lattice output"*). **May NOT be headlined as value-level emergence.** |
| **`Q = ω_R/(2\|ω_I\|)` (BIN-2)** | **NO — it cancels exactly** | **`ν_vac`-FREE, therefore EMERGENCE-CAPABLE at value level.** `Q = Re(Ω)/(2\|Im(Ω)\|)`; the `x_sat` conversion divides out identically. |
| `r_peak/r_sat` (BIN-3) | **NO** | `ν_vac`-free ratio; **FORM-class** statement about where the mode lives. |
| the existence + location of the root itself | **the LOCATION rides it; the SHAPE does not** | The certified object is `Ω`, a pure number. Its projection into `ω M_g` is what carries the imported `7`. |

Frozen tag: `Q and the localization ratio are exactly nu_vac-free (the r_sat scale divides out identically); omega_R*M_g is NOT and is VALUE-CONSISTENCY class because the 7 in r_sat = 7GM/c^2 is the 1/7 projection of the GR-imported nu_vac = 2/7`.

> **★ WHAT A CERTIFIED ROOT WOULD AND WOULD NOT MEAN, written before the run.** A `ROOT-CERTIFIED` verdict is a statement about an **instrument**, not about the world: it says *this discretization's eigenvalue at this location is a property of the continuous problem and not of the discretization*. It does **not** say the substrate rings there — that additional step needs the canonical input set of §3 to be right, and I7 in particular is **assumed, not tested** (FLAG-3). And it says **nothing whatever** about what else the substrate does or does not do at other frequencies (§1's non-claim).

---

## §1 — THE TARGET, AND THE EXPLICIT NON-CLAIM

### §1.1 The target

**Certification of the SINGLE located root of the graded spin-2 hyperboloidal problem near**

```
Omega_0  =  1.8536552108408788 - 1.0072567831433188 i
```

**Seed provenance.** That value is transcribed from the v2.1 shipped results object, `research/drivers/coldq_pole_v2_results.json`, at commit `bdcfa678` (branch `research/coldq-pole-v2`, PR #854, **OPEN, DO-NOT-MERGE — the file is not on `origin/main`, which is why it is transcribed rather than read**). It is carried in the driver as a named frozen constant with that citation in a comment.

Frozen: `the frozen seed Omega_0 = 1.8536552108408788 - 1.0072567831433188i is a SEED ONLY: at each order the polish is seeded from the double-precision linearized-pencil eigenvalue NEAREST the frozen seed, so the seed selects WHICH pencil eigenvalue is polished and enters no gate, no tolerance, no comparator and no bin as a value`.

**Certification means: ALL root-local gates G0..G10 of §5 PASS and ALL fireability self-tests FT-0..FT-10 of §6 FIRE.** There is no partial certification and no scoped certification in this lane: `ROOT-CERTIFIED` or `ROOT-NOT-CERTIFIED`.

### §1.2 The non-claim, written in advance and binding

> **This lane asserts the existence and location of THIS root; it asserts NOTHING about the absence or presence of other modes.**

Frozen: `this lane asserts the existence and location of THIS root; it asserts NOTHING about the absence or presence of other modes`.

Operationally, and each of these is a **prohibition on this lane's own result doc**:

- **NO winding, argument principle, or contour integral is computed over any rectangle, box or region, anywhere in this lane.** Frozen: `no argument-principle winding, no contour integral and no region count is computed anywhere in this lane; the pole-counting instrument the PR #854 audit impeached is not used, not repaired and not relied on`.
- **NO completeness claim, no "the only mode", no "no overtones", no mode count, no ladder.** `BIN-4` is `N/A BY CONSTRUCTION` (§7), stated **in advance**, and that status is **not** an outcome of any measurement.
- **NO claim that the certified root is the FUNDAMENTAL.** It is *a* root. Whether it is the least-damped, the lowest, or the physically-selected one is **not adjudicated here**.
- **The pseudo-spectrum the audit found is not re-measured, not characterised, and not explained here.** G5 measures only whether it comes within a frozen radius of the certified root.

### §1.3 What this lane additionally does NOT do

- **X1 — does NOT derive `ℓ = 2`.** The quadrupole selection is an input.
- **X2 — does NOT derive `ν_vac`, `K = 2G`, or the `7` in `r_sat`.** Their value provenance is GR-IMPORT, closed by PR #261/#506 and untouched here.
- **X3 — does NOT touch the spin (`a_* > 0`) mapping.** This is the `a_* = 0` anchor only.
- **X4 — does NOT compute a port-`Q`, a radiation resistance, or a Chu/Collin–Rothschild stored-energy `Q`.**
- **X5 — does NOT adjudicate #814 FORK-12.** No `ℓ`-ladder is computed in this lane at all, so the question does not even arise here.
- **X6 — does NOT run FORK-3(b)** (`ρ_eff = ρ₀/S³` as the shear-wave inertia).
- **X7 — does NOT certify, rescue, re-adjudicate or repair PR #845 or PR #854.** Both remain `SOLVER-NOT-CERTIFIED`. **G6's two-instrument agreement is a check on THIS lane's reimplementation (§5), not a certification of either predecessor** — see the FLAG-2 reconciliation in §10.
- **X8 — does NOT derive, assume, sketch or gesture at a low-frequency cutoff.** Deferred to a successor with Grant's input (§0 plumber question).
- **X9 — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry**, whatever the outcome.

---

## §2 — THE PHYSICS (inherited, ratified, NOT re-derived) AND THE OPERATOR THIS LANE REIMPLEMENTS

### §2.1 Inherited unchanged from the ratified v1/v2.1 framing — stated, not re-derived

The BH ringdown as a **transmission line**: series `L = ρ`, shunt `C = 1/G(A)`; the DC strain profile `A(r) = 7GM/c²r` grades it; the wall is `Z_shear → 0`, a **SHORT** at `r_sat`; the exterior is the graded taper; and `Q` is read as **the pole**, not from a port formula. **Zero free inputs.**

- `ρ(r) = ρ₀` — the cold lattice inertia;
- `G_shear(r) = ρ₀ c_shear(r)²` with `c_shear = c₀·sqrt(S)` — **Op16, CANONICAL** ([`common/operators.md:56`](../manuscript/ave-kb/common/operators.md), row `Op16 | Universal Wave Speed | $c_{shear} = c_0\cdot\sqrt{S}$`), reinforced verbatim at [`saturating-modulus-and-backreaction.md:60`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md): *"**SHEAR softens:** $c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection,"*
- `S(A) = (1 - A²)^{1/2}` and `A = ε_11/ε_yield` with `ε_yield = 1` — **Ax 4**, verbatim from the same leaf at `:51`–`:52`: *"\qquad A=\varepsilon_{11}/\varepsilon_{\text{yield}}\ (\varepsilon_{\text{yield}}=1),"* and *"\qquad D(A)=\frac{1}{S(A)},\qquad S(A)=(1-A^2)^{1/2}."*
- `ε_11 = 7GM/(c²r)` — [`temporal-spatial-lattice-decomposition.md:14`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md), verbatim *"The principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ compresses the lattice asymmetrically."*
- the SHORT — [`vol3/claim-quality.md:123`](../manuscript/ave-kb/vol3/claim-quality.md), verbatim *"a solid$\to$liquid free surface ($G_{shear} \to 0$) is exactly a $Z_{shear} \to 0$ short"*; and `r_sat` at `:121`, verbatim *"the **shear/bulk** rupture boundary is deeper, at $r_{sat} = 7GM/c^2 = 3.5\,r_s$ where the radial strain $\varepsilon_{11} = 1$"*.

The **toroidal (odd-parity)** radial system, inherited unchanged, in `W(r)` with conjugate traction `T(r) ≡ μ(r)·(W′ − W/r)`, `μ ≡ G_shear`:

```
W'' + (2/r + g)*W' + [ w^2 rho/mu - l(l+1)/r^2 - g/r ]*W = 0 ,   g = mu'/mu
```

with the spin-2 stored-energy weighting `(ℓ−1)(ℓ+2)` (NOT the spin-1 `ℓ(ℓ+1)`):

```
E_strain(r) ~ mu(r)*[ |W' - W/r|^2 + (l-1)(l+2)*|W|^2/r^2 ]*r^2
E_kin(r)    ~ rho(r)*|w|^2*|W|^2*r^2
```

Frozen: `the radial system is the toroidal (odd-parity, exactly divergence-free) branch of the shear-channel continuum equations; the impedance relation T = mu(W' - W/r) and the (l-1)(l+2) stored-energy weighting are the spin-2 ones and no spin-1 vector-multipole impedance is imported anywhere in this lane`.

### §2.2 The compactified, outgoing-factored operator (the object this lane discretizes)

Set `c₀ = ρ₀ = G₀ = 1`; `A ≡ r_sat/r ∈ (0, 1]`, so `μ = S = sqrt(1 − A²)`; `Ω ≡ ω·r_sat/c₀`. Factor the outgoing wave out **analytically**,

```
W = A * exp( i Om (1/A + lam A) ) * psi(A)
```

with `λ` a frozen **hyperboloidal gauge parameter**. At `λ = 0`,

```
A^2 psi_AA + [ -2 i Om + 2A + A^2 ghat ] psi_A
           + [ Om^2/(S(1+S)) - i Om ghat - l(l+1) + 2 A ghat ] psi = 0 ,   ghat = -A/(1-A^2)
```

Frozen: `no radiation boundary condition is imposed at infinity; the outgoing branch is the analytic branch of the compactified equation and the ingoing branch carries an essential singularity that is not in the discretization's function space, so no far-field matching, no asymptotic series and no subdominant-coefficient extraction occurs anywhere in this lane`.

The wall terminus is reached exactly by `A = 1 − η²`, `η ∈ [0,1]`, under which `η = 0` is an **ordinary regular point** and the traction-free SHORT is exactly `dψ/dη|_{η=0} = 0`. Frozen: `the wall is reached exactly via the A = 1 - eta^2 substitution, which makes eta = 0 an ordinary regular point of the transformed equation; the canonical traction-free SHORT is exactly the single linear condition dpsi/deta = 0 at eta = 0, with no offset, no series start, no regularized modulus floor and no shooting`.

Writing the `η`-form as `𝒜(η)ψ_ηη + ℬ(η,Ω)ψ_η + 𝒞(η,Ω)ψ = 0`, the discrete operator is the quadratic matrix pencil `M(Ω) = M0 + Ω·M1 + Ω²·M2` on Chebyshev–Gauss–Lobatto nodes, with row `0` replaced by the exact SHORT row.

### §2.3 ★ THE REIMPLEMENTATION DISCLOSURE, and why it makes G6 a live gate

**This lane REIMPLEMENTS the operator, the polish and the eigenfunction extraction in its own driver file** (`research/drivers/coldq_pole_v2p2_root.py`). It does **not** import, edit or execute `research/drivers/coldq_pole_v2.py`, which belongs to the concurrent PR #854 repair lane and is **byte-untouched by this lane**. Where an algebraic form or a routine shape is taken from that file, the v2.2 driver carries an attribution comment naming it.

Frozen: `the v2.2 instrument is an INDEPENDENT REIMPLEMENTATION; research/drivers/coldq_pole_v2.py is neither imported nor edited nor executed by this lane, and every algebraic form transcribed from it carries an attribution comment at the transcription site`.

**Consequence, and it is the reason G6 is not a rubber stamp.** A transcription error in any coefficient of `M0`, `M1`, `M2` or the SHORT row moves the root. **G0** catches it against the `A`-form algebra; **G6** catches it against a *different-in-kind* prior instrument (v1's real-axis asymptotic matching, which shares no line of code and no formulation with this one). Neither gate certifies a predecessor; both certify **this** transcription.

### §2.4 What is NOT the same as the spin-1 problem

The **impedance relation** is `T = μ(W′ − W/r)` — *not* `Z_ℓ ∝ h_ℓ′/h_ℓ`. The extra `−W/r` term is the tensor-rank content and it is what makes the wall condition genuinely different from the spin-1 one; likewise the stored-energy weighting carries `(ℓ−1)(ℓ+2)`, not `ℓ(ℓ+1)`. **G7 measures both differences AT THE CERTIFIED ROOT** — one on the eigenvalue (the wall row), one on the eigenfunction (the energy weighting).

---

## §3 — IMPORT LEDGER (every number the instrument consumes, tagged; `substrate-first-for-numbers`)

| # | Input | Value / form | Class | Source |
|---|---|---|---|---|
| **I1** | Saturation-wall radius | `r_sat = 7GM/c² = 7 M_g`, i.e. `x_sat = 7` | **`[canon]`** — form-derived, **VALUE rides the GR-imported `ν_vac`** | `vol3/claim-quality.md:121`; `temporal-spatial-lattice-decomposition.md:14`; provenance at `one-seventh-impedance-projection.md:18` |
| **I2** | Saturation amplitude profile | `A(r) = ε_11/ε_yield = r_sat/r`, `ε_yield = 1` | **`[canon]`** | `saturating-modulus-and-backreaction.md:51`; `vocabulary-register.md:309` |
| **I3** | Ax-4 kernel | `S(A) = (1 − A²)^{1/2}` | **`[canon]` — Axiom 4** | `saturating-modulus-and-backreaction.md:52` |
| **I4** | Shear-speed projection | `c_shear = c₀·S^{1/2}` (Op16) | **`[canon]`** | `common/operators.md:56`; `saturating-modulus-and-backreaction.md:60` |
| **I5** | Shear-wave inertia | `ρ(r) = ρ₀` (cold lattice inertia) | **`[canon, FORK-3 leading reading]`** — the naming gap at `vol3/claim-quality.md:122` is #814 CF-7, **routed not repaired** | `vol3/claim-quality.md:122` |
| **I6** | Inner boundary condition | traction-free, `T(r_sat) = 0` (`Z_shear → 0`, `Γ_shear = −1`) | **`[canon]`** | `vol3/claim-quality.md:123` |
| **I7** | Outer boundary condition | outgoing radiation into the cold matched lattice; **no far-field structure, no second reflection** | **`[canon]` — Regime-I radiative port, Ax-3-licensed. ASSUMED, NOT TESTED — see the §0 plumber question and FLAG-3** | §0 REGIME header |
| **I8** | Angular index | `ℓ = 2` (quadrupole) | **`[canon, INPUT not derived]`** | §1.3 X1 |
| **I9** | Unit choice | `M_g = 1`, `c₀ = 1`, `ρ₀ = 1`, hence `G₀ = 1` | **`[dimensionless by construction]`** | this lane |
| **I10** | `ν_vac = 2/7` | imported **read-only** from `ave.core.constants.N_NU`; used ONLY to form the `r_eff = r_sat/(1+ν_vac)` comparator reported alongside BIN-1 | **`[canon]` — VALUE GR-IMPORTED (PR #261/#506)** | `src/ave/core/constants.py:397` |
| **I11** | GR cold comparator | `ω_R M = 0.37367`, `ω_I M = 0.08896` at `a_* = 0`, read **programmatically** from the frozen `KERR_QNM` dict | **`[GR-IMPORTED comparator — the frozen C-comparator, inherited unchanged from v1 and v2.1]`** | `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51` |
| **I12** | GR `ℓ=2` overtone real parts | `ω_R M (2,0) = 0.373672`, `(2,1) = 0.346711`, read **programmatically** from the in-repo `SCHW_OMEGA_R` dict | **`[GR-IMPORTED comparator]` — used ONLY to derive the G5 isolation radius's upper constraint (§4.3); enters no bin** | `research/2026-07-20_ringdown-systematics_checks.py:69`, `:72` |
| **I13** | GR `ℓ=2` overtone imaginary parts | `ω_I M (2,0) = 0.088962` from the in-repo `SCHW_OMEGA_I` dict; `ω_I M (2,1) = 0.273915` (Berti–Cardoso–Will living-review table) | **`[GR-IMPORTED comparator]` — same restricted use as I12; enters no bin** | `research/2026-07-20_ringdown-systematics_checks.py:133`; **and — CORRECTING v2.1's disclosure — `0.273915` now DOES have an in-repo carrier, `research/drivers/coldq_pole_derivation.py:106`, merged with PR #845 after v2.1's prereg was frozen** |
| **I14** | Standing AVE comparators | `ω_R M_g = 18/49`, `Q = ℓ = 2`, `r_eff = 49M_g/9` | **`[corpus comparators — the objects under test]`** | `vol3/claim-quality.md:198`; `vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md`; #814 CF-9 |
| **I15** | Prior-lane root, v2.1 | `Ω_0 = 1.8536552108408788 − 1.0072567831433188i` | **`[PRIOR-LANE SEED — selects which pencil eigenvalue is polished; enters no gate, tolerance, comparator or bin]`** | `research/drivers/coldq_pole_v2_results.json` @ `bdcfa678` |
| **I16** | Prior-lane root, v1 | `Ω_v1 = x_sat·(omega_R_M − i·omega_I_M)` reconstructed **programmatically** from the shipped v1 JSON row `x_sat = 7.0` | **`[PRIOR-LANE COMPARATOR — G6 only; NOT-ADJUDICATED prior-lane data, gates THIS lane's transcription and certifies nothing about #845]`** | `research/drivers/coldq_pole_derivation_results.json:505`, `:509`, `:510`, `:512` |
| **I17** | Prior-lane discretization artifact | `Ω_art = 0.30587571217415294 − 2.4674822214282157i`, banked by v2.1's own frozen physical-vs-artifact criterion | **`[PRIOR-LANE FIREABILITY TARGET — FT-5 only]`** | `research/drivers/coldq_pole_v2_results.json` @ `bdcfa678` |
| **I18** | Prior-lane contaminated-edge probe | `Ω_edge = 0.1400 − 3.5035i`, one of v2.1's own frozen C9 probe points, measured there at `3.658e+00` | **`[PRIOR-LANE FIREABILITY TARGET — FT-5 only]`** | v2.1 result doc §3.2 probe table @ `bdcfa678` |
| **I19** | Instrument numerics | Chebyshev order `n`, gauge `λ`, mp precision `dps`, polish tolerance and iteration cap, dedupe radius, isolation radius `R_iso` | **`[ENGINEERING CHOICE — tagged, frozen in §4]`** | this lane |

**R8 audit rule (frozen).** `every number the instrument consumes appears on this ledger with its tag; no SM/GR convention default enters anywhere, and in particular no spin-1 vector-multipole impedance, no Chu/Collin-Rothschild stored-energy weighting, and no Regge-Wheeler or Zerilli potential is used as an input`.

---

## §4 — THE METHOD AND ITS FROZEN NUMERICS

### §4.1 The method (frozen)

Frozen: `the method is a compactified hyperboloidal Chebyshev spectral discretization in the Axiom-4 amplitude coordinate A = r_sat/r with the outgoing wave divided out in closed form, the traction-free SHORT imposed exactly as dpsi/deta = 0 at eta = 0, no boundary condition imposed at infinity, root extraction by extended-precision determinant polish seeded from the double-precision linearized pencil, and eigenfunction extraction by extended-precision inverse iteration; there is no matching radius, no asymptotic series, no shooting, no subdominant-coefficient extraction and NO ARGUMENT-PRINCIPLE WINDING anywhere in the chain`.

**ENGINEERING-CHOICE TAG (`substrate-first-for-numbers`).** Frozen: `the method is NUMERICS and is tagged ENGINEERING CHOICE; the medium, the profile, the kernel, the wall condition and the radiative port are CANON; no physical content of any kind is derived from the choice of discretization, and the gauge parameter lambda, the Chebyshev order n, the extended-precision dps, the polish tolerance and the isolation radius are engineering knobs whose only permitted role is to be varied and shown not to move the answer, or to be justified from prior-lane evidence and frozen`.

### §4.2 Frozen numerics (every parameter fixed here, before any code)

- **Radial coordinate:** `A = r_sat/r`, `A = 1 − η²`, `η ∈ [0,1]` on Chebyshev–Gauss–Lobatto nodes.
- **Primary Chebyshev order:** `n = 48`.
- **Frozen `n`-ladder (G2):** `n ∈ {32, 48, 64, 80, 96}`.
- **Hyperboloidal gauge:** primary `λ = 0`; frozen set `λ ∈ {−0.25, 0.0, +0.25}`.
- **Extended precision:** primary `dps = 50`; high-precision cross-check `dps = 80`.
- **Polish:** deterministic complex secant on `det M(Ω)` computed by mp LU with partial pivoting, seeded from the double-precision linearized-pencil eigenvalue nearest the frozen seed, terminating at `|Δ| ≤ 1e-38·|Ω|` or `60` iterations. **No RNG anywhere; no adaptivity; fully deterministic.**
- **Eigenfunction:** `4` rounds of mp inverse iteration on the row-equilibrated `M(Ω*)`, started from the **deterministic** all-ones vector, normalized in the infinity norm after each round.
- **Row equilibration:** each row of `(M0, M1, M2)` divided by that row's max modulus across the three matrices, so `‖M‖_∞ = O(1)` and the residual G1 measures is scale-free.
- **Dedupe radius:** `1e-6` relative — applied to the pencil spectrum before any count.
- **`x_sat` set (G8):** `{5, 7, 11}`, run in mp end-to-end with **no** `complex` cast anywhere on the path from the polished root to the reported spread.
- **Localization window (BIN-3):** `r/r_sat ∈ [1.0, 2.0]`, `401` equispaced points in the `η` image of that window.
- **Runtime:** frozen `total battery runtime <= 3600 s on the reference machine; a longer run is disclosed, not silently accepted`. The budget is **not** an adjudication criterion.
- **Engine fence:** Frozen: `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`.

### §4.3 ★ THE G5 ISOLATION RADIUS — DERIVED FROM PRIOR-LANE SHIPPED DATA, FROZEN HERE

> **DISCLOSURE, stated so it is auditable.** Every number in this subsection is **arithmetic on already-published prior-lane values** (the v1 and v2.1 shipped JSONs and the frozen GR comparators I11–I13). **No v2.2 instrument was built, run, or consulted to produce any of them, and no eigenvalue of the v2.2 operator existed when this document was frozen.** The arithmetic is reproduced by the driver and registered by the number check, so it is checkable rather than trusted.

`R_iso` is the radius of the exclusion annulus around the certified root inside which **no other eigenvalue of the discretization's spectrum may sit, at any order of the frozen ladder**. It is bounded from ABOVE by physics (the gate must not forbid a genuine neighbouring overtone) and from BELOW by numerics (the gate must be more than a restatement of the dedupe radius).

**(a) Upper constraint — a genuine overtone must NOT trip the gate.** GR's Schwarzschild `ℓ = 2` fundamental and first overtone, converted to this lane's scale-free variable by `Ω = x_sat·ω M` at `x_sat = 7`:

```
Om_GR(n=0) = 7*(0.373672 - 0.088962i) = 2.615704 - 0.622734i        [I12, I13]
Om_GR(n=1) = 7*(0.346711 - 0.273915i) = 2.426977 - 1.917405i        [I12, I13]
|Om_GR(n=0) - Om_GR(n=1)| = 1.3083542634814167
```

**(b) Upper constraint — the nearest OTHER object in the prior-lane data.** The only other root v2.1 located over its rectangle is the artifact `Ω_art` (I17):

```
|Omega_0 - Omega_art| = 2.127881506829584
```

**(c) Lower constraints.** `|Ω_0| = 2.1096454365285577`. The frozen dedupe radius is `1e-6` relative, i.e. `2.1096e-06` absolute; the G2 root-drift tolerance is `1e-10` relative, i.e. `2.1096e-10` absolute.

**FROZEN CHOICE:**

```
R_iso = 0.5      (absolute, in Omega units; ENGINEERING CHOICE, tagged)
```

with the four receipts it is chosen against, all reproduced by the driver:

| receipt | value | reading |
|---|---|---|
| `1.3083542634814167 / R_iso` | `2.6167085269628334` | a genuine overtone at GR-like `ℓ=2` spacing sits **2.62×** outside the annulus and does **not** trip the gate |
| `2.127881506829584 / R_iso` | `4.255763013659168` | the nearest other prior-lane located object sits **4.26×** outside the annulus |
| `R_iso / \|Ω_0\|` | `0.23700665113790634` | the annulus is a **23.7 %** relative exclusion zone — a substantive separation statement, not a hair's breadth |
| `R_iso / (1e-6·\|Ω_0\|)` | `237006.65113790636` | the annulus is **2.37e5 ×** the dedupe radius, so the gate is not a restatement of dedupe |

Frozen: `the isolation radius is R_iso = 0.5 absolute in Omega units, chosen as an ENGINEERING CHOICE bounded ABOVE by the GR ell=2 fundamental-to-first-overtone spacing of 1.3083542634814167 in the same units (so a genuine overtone does not trip the gate) and by the 2.127881506829584 distance to the nearest other root in the v2.1 shipped data, and bounded BELOW by the 1e-6 relative dedupe radius; it is frozen once, is not adjusted after any measurement, and if it fires the lane reports ROOT-NOT-CERTIFIED`.

**What G5 counts (frozen).** Frozen: `G5 counts the eigenvalues of the double-precision linearized quadratic pencil of the SAME operator at the SAME order, deduped at the frozen 1e-6 relative radius, that lie within R_iso of the polished root at that order; the count must be EXACTLY ONE at every order of the frozen ladder n in {32, 48, 64, 80, 96}`.

> **Why the double-precision pencil and not the polished set.** The audit's mechanism is a property of the **discrete spectrum the discretization manufactures** — *"In-box pencil eigenvalue count grows 2 -> 9 as n goes 32 -> 80"* (`0a7dec1f`). Counting the polished set instead would count only what the seeding found, which is the weaker measurement. **G5 therefore measures the same object the audit measured, restricted to a neighbourhood of the root.**

---

## §5 — THE ROOT-LOCAL CERTIFICATION GATES (G0–G10), with FROZEN numeric tolerances

**Every gate below is ROOT-LOCAL: it is a measurement on the root, on its eigenfunction, or on the discrete spectrum in a frozen neighbourhood of it. No gate integrates, counts or winds over a region.**

**Definitions used below, frozen.**
`Omega_star(n, lam, x_sat, dps)` = the mp-polished root at that setting, seeded from the double-precision linearized-pencil eigenvalue nearest the frozen seed `Ω_0`.
**The CERTIFIED ROOT** = `Omega_star(48, 0.0, 7.0, 50)`.
**The CERTIFIED EIGENFUNCTION** = the vector returned by `4` rounds of mp inverse iteration on the row-equilibrated `M(Omega_star(48, 0.0, 7.0, 50))` at `dps = 50`, started from the all-ones vector, infinity-normalized after each round.

| Gate | What it certifies | FROZEN criterion |
|---|---|---|
| **G0** | **Operator-transcription identity** — the reimplemented `η`-form is the `A`-form, as algebra | `the eta-form operator agrees with 4*eta^2 times the A-form operator to <= 1e-13 relative on the frozen set of arbitrary analytic test functions, over lambda in {-0.25, 0, +0.25}, ell in {2, 3} and Omega in {0.9-0.3i, 2.5-1.1i, 14.0-6.0i}` |
| **G1** | **Residual of the certified eigenfunction at the certified root** | `the infinity-norm residual max_i |(M(Omega_star) psi)_i| / max_i |psi_i| of the CERTIFIED EIGENFUNCTION on the row-equilibrated mp operator at dps = 50 is <= 1e-20` |
| **G2** | **`n`-INDEPENDENCE of the root across the frozen ladder** | `the maximum pairwise relative separation of Omega_star(n, 0.0, 7.0, 50) over the frozen ladder n in {32, 48, 64, 80, 96} is <= 1e-10` |
| **G3** | **Hyperboloidal-gauge independence** (the live C2-class gate) | `the maximum pairwise relative separation of Omega_star(48, lam, 7.0, 50) over lam in {-0.25, 0.0, +0.25} is <= 1e-12` |
| **G4** | **Precision and arithmetic-path independence** | `(a) |Omega_star(48, 0, 7, 80) - Omega_star(48, 0, 7, 50)| / |Omega_star(48, 0, 7, 50)| <= 1e-25, AND (b) at every order of the frozen ladder the double-precision linearized-pencil eigenvalue nearest the frozen seed agrees with the mp-polished root at that order to <= 1e-6 relative` |
| **G5 ★** | **ISOLATION — the root is locally separated from the discretization's pseudo-spectrum** | `G5 counts the eigenvalues of the double-precision linearized quadratic pencil of the SAME operator at the SAME order, deduped at the frozen 1e-6 relative radius, that lie within R_iso of the polished root at that order; the count must be EXACTLY ONE at every order of the frozen ladder n in {32, 48, 64, 80, 96}` |
| **G6** | **Two-instrument agreement** — this reimplementation against v1's different-in-kind instrument | `the certified root agrees with the v1 root reconstructed programmatically from research/drivers/coldq_pole_derivation_results.json row x_sat = 7.0 as x_sat*(omega_R_M - i*omega_I_M) to <= 1e-5 relative` |
| **G7** | **Spin-2-vs-spin-1 discrimination AT THE ROOT** — two independent measurements, one on the eigenvalue and one on the eigenfunction | `(a) replacing the spin-2 traction-free wall row by the spin-1 wall condition W'(r_sat) = 0 MOVES the root by >= 1e-3 relative, AND (b) replacing the spin-2 (ell-1)(ell+2) angular weighting by the spin-1 ell(ell+1) weighting in the mode-energy functional evaluated on the CERTIFIED EIGENFUNCTION changes the window-integrated strain-to-kinetic energy ratio by >= 1e-3 relative` |
| **G8** | **`nu_vac` cancellation AT THE ROOT, measured in mp end-to-end** | `across x_sat in {5, 7, 11} the mp-computed relative spreads of Q = Re(Omega)/(2*abs(Im(Omega))) and of abs(Omega) are each <= 1e-9, and omega_R*M_g = Re(Omega)/x_sat scales as 1/x_sat to <= 1e-9 relative; no value on the path from the polished root to these spreads is cast to a double-precision complex` |
| **G9** | **Determinism** | `two independent full driver runs produce an identical results digest (SHA-256 over the results object minus timing fields)` |
| **G10** | **Ax-3 reality / passivity ON the certified eigenfunction's own operator** | `(a) the row-equilibrated mp operator at n = 48 and every lam in {-0.25, 0.0, +0.25} has max|Im M0|/max|M0|, max|Im M2|/max|M2| and max|Re M1|/max|M1| each <= 1e-40, AND (b) the conjugate-mirror root polished from the seed -conj(Omega_star) satisfies |Omega_mirror + conj(Omega_star)| / |Omega_star| <= 1e-20` |

### Why G10(b) is the Ax-3 statement and not decoration

With a **real, lossless** constitutive law the `η`-form matrices satisfy `M0, M2` real and `M1` purely imaginary (`ℬ ∝ 4iη(1 − λA²)`, `𝒞`'s `Ω`-linear part `∝ 4iA/(2−η²)·(…)`), so `conj(M(−conj(Ω))) = M(Ω)` **identically** and the spectrum is symmetric under `Ω → −conj(Ω)`. That symmetry is the frequency-domain form of *"the time-domain equation has real coefficients"* — i.e. of *"the medium stores and does not dissipate; all the loss is the radiative port"*. **Smuggling any `Im(μ) ≠ 0` puts an imaginary part into `M2` and breaks it.** G10(a) checks the matrix structure; G10(b) checks the consequence on the certified root. FT-10 breaks both with one mutation.

### Certification classes (exhaustive, frozen)

- **`ROOT-CERTIFIED`** — `all of G0..G10 PASS and all of FT-0..FT-10 FIRE`.
- **`ROOT-NOT-CERTIFIED`** — `any of G0..G10 FAILS, OR any of FT-0..FT-10 fails to fire`. **A gate that cannot fail voids the certification exactly as hard as a gate that fails.** Under this class **no physics bin is adjudicated** (§7 precedence).

**There is no scoped or partial class in this lane.** Frozen: `this lane has exactly two certification classes, ROOT-CERTIFIED and ROOT-NOT-CERTIFIED; there is no scoped, partial or provisional certification, and a gate that passes only over a reduced parameter set is a FAIL`.

**Rule-11 fence on the method itself, frozen and binding.** Frozen: `no gate, tolerance, frozen numeric parameter or method element in sections 4 and 5 may be changed after any gate result is seen; if this instrument fails certification the lane reports ROOT-NOT-CERTIFIED and routes to its own successor with a new version number, exactly as #845 routed to v2, v2 to v2.1 and v2.1 to v2.2`.

---

## §6 — GATE-FIREABILITY SELF-TESTS (FT-0 … FT-10) — each MUST FIRE, each demonstrated on a MUTATED input BEFORE the real gate is read

**The rule (frozen).** Frozen: `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is ROOT-NOT-CERTIFIED regardless of how many gates passed`.

**The ordering rule (frozen), new in this lane and a direct response to audit WARN 4.** Frozen: `every self-test is executed and recorded BEFORE its target gate's own measurement is read in the results object, and each self-test's mutation is shown here to be NON-VACUOUS against the object it mutates by an algebraic argument stated at freeze time, not by running`.

| # | Targets | Deliberate mis-specification | FROZEN firing criterion | Why the mutation is NON-VACUOUS (algebra, stated at freeze) |
|---|---|---|---|---|
| **FT-0** | **G0** | corrupt the `𝒞₀` coefficient by `1e-12` relative | `the corrupted eta-form coefficient MUST break the operator identity by >= 1e-13 relative` | `𝒞₀ = −4ℓ(ℓ+1)η² − 8A²/(2−η²)` is `O(1)` on the interior nodes and appears with unit weight in `𝓛_η`, so a `1e-12` relative corruption is a `~1e-12` relative change in the identity's residual — one order above the gate |
| **FT-1** | **G1** | evaluate the residual of the CERTIFIED EIGENFUNCTION on `M(Omega_star·(1 + 1e-10))` instead of `M(Omega_star)` | `the off-root residual MUST be >= 1e-15` | the residual is `≈ σ_min(M(Ω))`, and `dσ_min/dΩ` is `O(1)` for a simple root, so a `2.1e-10` absolute displacement produces an `O(1e-10)` residual — five orders above the threshold and ten above the gate |
| **FT-2** | **G2** | add `n = 8`, far below every order of the frozen ladder | `the under-resolved order MUST deviate from Omega_star(48, 0, 7, 50) by >= 1e-6 relative` | at `n = 8` the Chebyshev basis cannot represent the coefficient functions, whose measured tail (v2.1 §9 item 7) only reaches `5.3e-16` by `n = 40`; v2.1's FT-C measured `4.4038e-04` for exactly this mutation |
| **FT-3** | **G3** | **a CORRECTLY-SPECIFIED half-applied gauge**: carry `λ` into `ℬ₁` and `𝒞₁` but OMIT the `λ` terms from `𝒞₂`, i.e. use `𝒞₂ = 4η/(u(1+S))` and drop `+8η²λ − 4η²λ²A²` | `the gauge-omission mutation MUST make the G3 pairwise spread exceed 1e-6` | **the omitted terms are `8η²λ − 4η²λ²A²`, which at `λ = +0.25` equal `2η² − 0.0625·4η²A²`, an `O(1)` quantity at `η → 1` — the mutation is NOT a no-op and NOT the logical negation of G3.** This is the explicit repair of v2.1's FT-B, which was vacuous twice over (audit WARN 4): it withheld `λ` from a wall row that carries no `λ`, and its firing condition was G3's own failure condition |
| **FT-4** | **G4** | (a) run the mp operator at `dps = 20`; (b) build the double-precision pencil at `n = 8` while the mp root is at `n = 48` | `(a) the dps = 20 root MUST differ from the dps = 50 root by >= 1e-25 relative, AND (b) the mismatched-order double-vs-mp cross-check MUST exceed 1e-6 relative` | (a) `dps = 20` truncates every operator entry at `~1e-20` relative and the equilibrated Chebyshev operator's conditioning at `n = 48` is `O(n⁴) ≈ 5e6`, so the root moves by `~1e-14` — eleven orders above the threshold; (b) `n = 8` is the same under-resolution FT-2 uses |
| **FT-5 ★** | **G5** | run the identical isolation measurement centred on **(a)** the v2.1-banked discretization artifact `Ω_art` (I17) and **(b)** the v2.1 C9 probe point `Ω_edge = 0.1400 − 3.5035i` inside the contaminated left edge (I18), instead of on the certified root | `case (a) MUST return a count different from exactly one at at least one order of the frozen ladder, OR a polished n-drift above the G2 tolerance at those orders; AND case (b) MUST return a count different from exactly one at at least one order of the frozen ladder` | (a) `Ω_art` is banked by v2.1's OWN frozen physical-vs-artifact criterion as absent at some `n` in `{48, 56, 64}` within `1e-6` relative, so it cannot be both isolated and `n`-stable across a ladder that contains three of those orders; **the OR is deliberate and is stated in advance: the artifact must fail EITHER isolation OR stability, and which one it fails is reported, not chosen.** (b) `Ω_edge` sits in the region the audit measured as carrying a migrating spectrum whose in-box count runs `2 → 9` over `n = 32 → 80`, so a count of exactly one there at every order would itself contradict `0a7dec1f` |
| **FT-6** | **G6** | corrupt the `𝒞₀` coefficient by `1e-3` relative and compare THAT root against the v1 comparator | `the corrupted-operator root MUST disagree with the v1 comparator by >= 1e-5 relative` | a `1e-3` relative change in an `O(1)` coefficient of the eigenvalue problem moves the eigenvalue by `O(1e-3)` relative — two orders above G6's tolerance. **This is the demonstration that G6 catches a transcription error rather than rubber-stamping a known agreement** |
| **FT-7** | **G7** | **REVERSE fireability (stated as such):** run both discriminators between IDENTICAL specifications — spin-2 wall against spin-2 wall, and spin-2 weighting against spin-2 weighting | `both null-mutation differences MUST be below 1e-3, demonstrating that G7's discriminator does not manufacture a difference between identical specifications` | G7's pass condition is a LARGE difference, so its failure mode is a small one; the correct fireability demonstration is a configuration in which the measurement returns small. Both null mutations are exact identities and must return `0` up to arithmetic |
| **FT-8** | **G8** | inject the `x_sat`-dependent profile perturbation `A -> A*(1 + 1e-6*(x_sat - 7)/7)` | `the x_sat-dependent perturbation MUST make the G8 spread exceed 1e-9` | the perturbation is identically zero at `x_sat = 7` and `±1.43e-06` relative at `x_sat = 5, 11`, so it breaks the scale invariance the gate measures without touching the primary run; v2.1's FT-E measured `6.0137e-07` for exactly this mutation |
| **FT-9** | **G9** | perturb one recorded gate value by `1e-15` relative in a COPY of the results object and re-digest | `the perturbed copy MUST produce a different digest` | SHA-256 over the serialized object; the demonstration is that the digest actually covers the gate payload rather than a header |
| **FT-10** | **G10** | smuggle loss `Im(mu)/Re(mu) = 1e-3` into the modulus, which enters the `η`-form only through the `Ω²ρ/μ` term of `𝒞₂` | `(a) the lossy operator MUST return max|Im M2|/max|M2| >= 1e-6, AND (b) the lossy conjugate-mirror residual MUST be >= 1e-5` | a constant complex factor on `μ` leaves `ĝ = μ′/μ` and the wall condition `ψ_η(0) = 0` unchanged and changes ONLY `𝒞₂`'s first term `4η/(u(1+S)) → 4η/(u(1+S)(1+iδ))`, giving `Im 𝒞₂/Re 𝒞₂ ≈ −δ = −1e-3`; the conjugate-mirror symmetry proof of §5 requires `M2` real, so it breaks at the same order |

---

## §7 — THE FROZEN PHYSICS BINS — adjudicated IFF ALL GATES PASS

**Rule-11 fence, stated up front and binding.** Frozen: `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the instrument returns is banked`. There is **no free parameter to tune** — that is the point of the lane.

**PRECEDENCE (frozen, evaluated in this order).** `BIN-F-NOROOT` > `BIN-F-ROOT` > `BIN-F-PROFILE` > `BIN-1/2/3`. If an earlier bin fires, the later ones are reported as `N/A — not adjudicated` and **no verdict language is used about them.** `BIN-4` is `N/A BY CONSTRUCTION` **at every precedence level, including a full pass** (§7.5).

> **★ THE PRECEDENCE IS REORDERED RELATIVE TO v1/v2.1, DELIBERATELY, AND THE REASON IS STATED IN ADVANCE.** v1 and v2.1 ordered `SOLVER` before `NOPOLE` because their solver gates were region-wide and could be adjudicated without a located root. **Every gate in this lane is root-local, so if no root is located there is nothing for the gates to measure.** `BIN-F-NOROOT` therefore comes first. This is a structural consequence of the target narrowing, not a relaxation: the set of outcomes is unchanged and both failure classes remain reachable.

### §7.1 Honest-failure bins (each reachable, each with a disposition)

| bin | condition | disposition |
|---|---|---|
| **`BIN-F-NOROOT`** | `the double-precision linearized pencil at n = 48 has no eigenvalue within R_iso of the frozen seed, or the mp polish from that seed fails to converge` | **A clean negative and a GOOD outcome.** It would say the object v1 and v2.1 both located is not present in this reimplementation of the same formulation — which would be a decisive statement about at least one of the three instruments. Banked as such; no bin adjudicated; routed to Grant and the auditor lane. |
| **`BIN-F-ROOT`** | `any of G0..G10 FAILS or any of FT-0..FT-10 fails to fire` | **`ROOT-NOT-CERTIFIED`.** No physics bin adjudicated; the failing gate's numbers are reported; the lane returns the instrument failure as its result. No claim, no walk-back, no solidity change, **and no retune** — it routes to its own successor with a new version number. |
| **`BIN-F-PROFILE`** | `the canonical input set of section 3 is found to be internally inconsistent at solve time (two canonical statements that cannot both hold on the domain)` | **flag-don't-fix.** Both file paths + verbatim content surfaced to Grant and the auditor lane; **neither side reframed to match the other**; no bin adjudicated. |

### §7.2 BIN-1 — the real part `ω_R M_g`

`D_omega ≡ omega_R_derived / omega_R_GR − 1`, with `omega_R_GR = 0.37367` read programmatically from the frozen `KERR_QNM[0.00]` row (I11, `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51`).

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-1-MATCH`** | `abs(D_omega) < 0.03` |
| **`BIN-1-NEAR`** | `0.03 <= abs(D_omega) < 0.10` |
| **`BIN-1-MISS`** | `abs(D_omega) >= 0.10` |

Reported alongside, **not a separate class**: `D_omega_shortcut ≡ omega_R_derived/(18/49) − 1`, the deviation from the standing corpus shortcut `18/49 = 0.36735`; and the sign of both. **Class line (mandatory in the result headline):** `BIN-1 is VALUE-CONSISTENCY class, not emergence: omega_R*M_g carries the GR-imported nu_vac through the 7 in r_sat`.

**The `(1+ν_vac)` rider, frozen:** `if BIN-1's derived omega_R*M_g deviates from 18/49 by more than 3 percent, the standing chain's r_eff = r_sat/(1+nu_vac) assertion is FALSIFIED as a derivation of the eigenfrequency, and that is a GOOD outcome recorded as such`.

**The advance identity, restated so two readings of one result cannot be presented as two results.** Frozen: `k_0*r_sat = x_sat * omega_R M_g identically, so the 9/7-above-cutoff test IS the omega_R versus 18/49 comparison re-expressed and is NOT an independent axis`.

### §7.3 BIN-2 — the quality factor `Q` (★ the `ν_vac`-free, emergence-capable axis)

`Q_derived ≡ Re(Omega)/(2*abs(Im(Omega)))`; `Q_GR ≡ 0.37367/(2*0.08896) = 2.1002135791366907` from the same frozen row; `D_Q ≡ Q_derived/Q_GR − 1`.

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

> **⚑ FLAG-1 CARRIED FORWARD UNCHANGED, and the discriminator's robustness to BOTH corpus values is frozen HERE rather than argued afterwards.** Two `Q_GR` values exist in the corpus: the programmatic `2.1002135791366907` from `KERR_QNM[0.00] = (0.37367, 0.08896)`, and the rounded-prose `2.099438202247191` from the pair `0.3737`/`0.0890`, carried verbatim at `research/2026-07-30_qlaw-derivation_scoping.md:401` (*"$3.2\%$") → $Q_{GR}(0) = 2.0994$, cold deficit $-4.74\%$. Agrees with the frozen table to 3 s.f."*). **Both are the same table at different precision.** The frozen source does not move — the programmatic value is used, exactly as v1 and v2.1 used it — and the robustness is stated as a *criterion*, not as a *reassurance*:
>
> - **`abs(D_Q)` bins.** The two comparators differ by `0.0007753768895` — `0.037 %` of `Q_GR`, two orders below `BIN-2-MATCH`'s `0.03` boundary. **No `abs(D_Q)` sub-bin can flip.**
> - **The three-way discriminator.** Its crossover is the midpoint between the comparator and `2.0`: `2.0501067895683455` for the programmatic value and `2.0497191011235955` for the rounded one, a window of width `0.00038768844`. **Only a `Q_derived` landing INSIDE that window could be flipped by the choice of comparator.**
>
> Frozen: `the BIN-2 three-way discriminator is robust to the FLAG-1 comparator ambiguity unless Q_derived lands inside the window between 2.0497191011235955 and 2.0501067895683455; the result doc MUST report whether it does, and if it does the discriminator is reported as AMBIGUOUS rather than adjudicated`.

**Class line (mandatory in the result headline):** `BIN-2 is the nu_vac-FREE axis: Q = Re(Omega)/(2*abs(Im(Omega))) contains no r_sat scale, so the GR-imported 7 cancels exactly`.

### §7.4 BIN-3 — where the mode actually lives (FORK-1, handed to the substrate)

Frozen observable: `u ≡ r_peak/r_sat`, where `r_peak` maximizes the frozen spin-2 mode-energy density `E(r) = rho|omega|^2|W|^2 r^2 + mu(|W' - W/r|^2 + (ell-1)(ell+2)|W|^2/r^2) r^2` over the frozen window `r/r_sat in [1.0, 2.0]`, evaluated on the CERTIFIED EIGENFUNCTION. A second, independent measure `u_kin` uses the kinetic term alone.

| sub-bin | FROZEN criterion |
|---|---|
| **`BIN-3-RIM`** | `1.00 <= u <= 1.10` — the mode hugs the wall; the rim-ring reading |
| **`BIN-3-RAMP`** | `1.10 < u <= 1.50` — the mode sits in the stiffness ramp. Sub-flag `BIN-3-RAMP-TURNING-POINT` if additionally `abs(u - 1.2247) <= 0.05` |
| **`BIN-3-OUTER`** | `u > 1.50` — neither standing picture locates the mode |
| **`BIN-3-MONOTONE`** | `the energy density has no interior maximum in the frozen window (the maximum sits at an endpoint)` — localization is not a well-posed observable for this mode; the endpoint is reported |
| **`BIN-3-DISCORDANT`** | `abs(u - u_kin) > 0.10` — the two frozen measures disagree; both are reported and no localization verdict is banked |

**The ill-posed sub-bin is PRESERVED, deliberately.** `BIN-3-MONOTONE` exists so that *"the localization question is ill-posed for this mode"* has a bin and does not have to be argued for after the fact. Frozen: `BIN-3-MONOTONE and BIN-3-DISCORDANT are preserved unchanged from v1 and v2.1 so that an ill-posed or discordant localization reading lands in a pre-registered bin rather than in prose`.

### §7.5 BIN-4 — `N/A BY CONSTRUCTION`, declared in advance

Frozen: `BIN-4 is N/A BY CONSTRUCTION in this lane and is not adjudicated at any precedence level including a full gate pass; no overtone, no ladder, no mode count and no completeness statement is computed, and the deferral is an open instrument-scope question awaiting a substrate-derived low-frequency cutoff, not a failure of this lane`.

**This is a scoped non-claim, and the result doc is required to present it as one.** It is not `BIN-4-NONE` — that sub-bin asserted *"exactly one physical pole is located in the frozen rectangle"*, which is a **counting claim over a region** and is exactly what the audit impeached and what §1.2 forbids. **`BIN-4-NONE`, `BIN-4-LADDER-MATCH` and `BIN-4-LADDER-DIFFERENT` are all unreachable in this lane by construction, and that is disclosed here rather than discovered later.**

### §7.6 Reachability audit (frozen)

- `BIN-F-ROOT` is reachable **and is demonstrated reachable every run**: FT-0…FT-10 each drive an actual gate into its failing state (FT-7 by the reverse construction, stated as such).
- `BIN-F-NOROOT` is reachable: the pencil at `n = 48` either has an eigenvalue within `R_iso` of the seed or it does not.
- `BIN-F-PROFILE` is reachable: the canonical set carries live tensions this lane touches (#814 CF-7's unnamed `ρ` at `vol3/claim-quality.md:122`).
- `BIN-1/2/3` sub-bins are each reachable because each is an interval or a strict comparison on a continuously-valued measured quantity, and the intervals **partition** their axis with no gaps and no overlaps.
- `BIN-4`'s sub-bins are **deliberately unreachable**, disclosed in §7.5.
- **No outcome requires a criterion to be relaxed after the fact.**

### §7.7 ★ PREDICTABILITY DISCLOSURE — stated in advance so no bin outcome can later be presented as a blind prediction

**The bin boundaries in §7.2–§7.4 are inherited byte-identically from the v2.1 prereg (commit `7d8fe484`, §7), which itself inherited them from v2 (`00724432`) and v1. They were frozen before any number in this arc existed, and this lane does not re-derive, adjust, widen or narrow a single one of them.**

**And this lane knows roughly where they will land.** v2.1 shipped `NOT-ADJUDICATED` diagnostics at `Ω = 1.8536552108408788 − 1.0072567831433188i` — `ω_R M_g = 0.2648078872629827`, `Q = 0.9201502744197103` — under a `SOLVER-NOT-CERTIFIED` instrument. **Anyone can compute where those fall in the bins above.** Disclosing that here, in advance, is the honest handling: the value of this lane is **not** a surprising bin outcome, it is a **certified** bin outcome — the difference between a number produced by an instrument nobody has certified and the same number produced by one whose root-local behaviour has been gated. Frozen: `this lane's contribution is CERTIFICATION of an already-published prior-lane number, not the discovery of a new one; the bin outcomes are predictable from the v2.1 NOT-ADJUDICATED diagnostics and that predictability is disclosed in advance, so no bin outcome may be presented as a blind prediction`.

---

## §8 — WHAT TRANSFERS, AND WHAT MUST BE RE-EARNED

**TRANSFERS (framing and discipline, cited not copied):**
- the **ratified physics framing** — the transmission-line reading, the graded profile, the SHORT at `r_sat`, the radiative port, the spin-2 channel, `Q` as a pole;
- the **compactified formulation** of v2/v2.1 §2.2 and its exact wall substitution, **as algebra to be re-verified by G0, not as a certified implementation**;
- the **shape** of the certification battery — frozen gates with numeric tolerances, self-tests that must FIRE, a determinism digest, an exhaustive outcome-class table with a reachability argument;
- the **frozen-first commit order**;
- the **bin boundaries**, byte-identical (§7.7);
- the **`x_sat`-generalized advance identity** `k₀ r_sat = x_sat · ω_R M_g`, minted in the v2.1 prereg §2.5 and cited here as that lane's, not re-minted.

**DOES NOT TRANSFER — must be re-earned, and is (gate in brackets):**
- **the certification.** #845 and #854 are both `SOLVER-NOT-CERTIFIED`. [G0–G10]
- **the implementation.** Every coefficient, the polish, the eigenfunction extraction and the localization are reimplemented and re-verified. [G0, G6]
- **the pole-counting instrument.** It is not re-earned; **it is not used at all** (§1.2).
- **any completeness statement.** Not re-earned; **abandoned as out of scope** (§7.5).
- **v2.1's `nu_vac`-exactness claim.** The audit showed it was a `complex`-cast artifact; this lane measures it in mp end-to-end and reports whatever mp says. [G8]

Frozen: `no gate, tolerance, certification class or measured number is inherited from PR #845 or PR #854; the physics framing, the compactified algebra and the bin boundaries transfer, the instrument and the certification do not, and every gate in section 5 is re-earned on this reimplementation`.

---

## §9 — SATISFIABILITY OF THE FROZEN REQUIREMENTS — DERIVED, WITH ZERO PRE-FREEZE COMPUTATION

> **★ DISCLOSURE, and it is stricter than v2.1's.** v2.1 ran an uncommitted scratch prototype before its freeze and disclosed it. **This lane ran NOTHING.** No prototype was written, no operator was assembled, no eigenvalue was computed, estimated, seeded or looked at before this document was frozen and pushed. The only arithmetic performed before the freeze is the arithmetic of §4.3 and §7.3, which is **elementary arithmetic on already-published prior-lane values and frozen GR comparators**, is reproduced by the driver, and is machine-checked by the number check. Every tolerance below is therefore justified by **derivation or by prior-lane measured evidence**, never by scouting this instrument.
>
> **The risk of that choice is disclosed and accepted:** a tolerance derived rather than scouted can be wrong, and if it is, the gate FAILS and this lane reports `ROOT-NOT-CERTIFIED`. **It will not be retuned.**

| gate | tolerance | where it comes from |
|---|---|---|
| **G0** `1e-13` | v2.1's C11 measured `8.9716e-16` on the same identity and its pre-freeze prototype measured `1.401e-15`; `1e-13` sits ~2 orders above the worst prior evidence |
| **G1** `1e-20` | the polish terminates at `1e-38·|Ω|`, mp carries `50` digits, and the equilibrated Chebyshev operator's conditioning at `n = 48` is bounded by `O(n⁴) ≈ 5.3e6`, so an achievable residual floor is `~1e-40`. **`1e-20` is frozen 20 orders above that floor** because the inverse-iteration extraction is the least-controlled step in the chain and no prior lane has measured it |
| **G2** `1e-10` | the PR #854 audit measured this root stable to **12 digits** over `n = 32 → 80` (`0a7dec1f`: *"only Omega = 1.853655 - 1.007257i is n-stable"*). **`1e-10` is frozen two orders looser than the measured evidence supports**, as honest headroom for the two orders the audit did not sweep (`n = 96`, and this lane's own reimplementation) |
| **G3** `1e-12` | v2.1's C2 measured `3.3268e-14` on the identical gauge set at the identical primary order; `1e-12` keeps v2.1's own frozen tolerance unchanged, with ~1.5 orders of measured margin |
| **G4(a)** `1e-25` | the polish's own termination is `1e-38` relative, so two runs at `dps = 50` and `dps = 80` cannot differ by more than `~1e-38`; `1e-25` is frozen 13 orders above that |
| **G4(b)** `1e-6` | v2.1's B1 disclosure measured the double-precision-operator floor at `2.73e-10 … 8.67e-08` on the flat control at `n = 32/40`. The graded operator at `n ≤ 96` is more ill-conditioned, so **`1e-6` is frozen about one order above the worst prior-lane measured floor** |
| **G5** `R_iso = 0.5`, count `== 1` | derived in §4.3 from four receipts, two of them upper constraints from physics and two lower constraints from the instrument's own frozen numerics |
| **G6** `1e-5` | the observed cross-lane agreement is `6.803232e-07` (§ supersession note). **`1e-5` is an ENGINEERING CHOICE with ~1.2 orders of deliberate headroom over the observed value**, so that a reimplementation that is *slightly* different in a rounding-level way still passes while a transcription error (FT-6 shows `O(1e-3)`) does not |
| **G7** `1e-3` | v2.1's FT-F(ii) measured the spin-1 wall condition moving the fundamental by `0.28424`, and v1's FT-2 measured `0.28430` for the same substitution — two independent instruments agreeing to `2.1e-04` on a `0.284` effect. **`1e-3` is frozen ~2.5 orders below the twice-measured effect** |
| **G8** `1e-9` | v1's and v2.1's frozen tolerance, unchanged. The audit's mp re-measurement of the same quantity is `4.466e-47` / `1.381e-46`, i.e. ~37 orders inside the gate — which is why **FT-8 is mandatory**: without it this gate would be dead |
| **G9** identical digest | determinism has no tolerance |
| **G10(a)** `1e-40` | the quantities are exact zeros in mp by the structure argued in §5 (`M0`, `M2` real; `M1` purely imaginary); the tolerance exists only to catch a structural transcription error, and **FT-10 supplies the fireability a zero-valued gate would otherwise lack** |
| **G10(b)** `1e-20` | both members of the mirror pair are polished to `1e-38` relative independently, so their symmetry residual is bounded by `~1e-38`; `1e-20` is frozen 18 orders above |

**Runtime.** The dominant cost is the mp determinant polish, `O(n³)` mp operations per evaluation. v2.1 measured `≈ 0.1 s` at `n = 32` and `≈ 0.8 s` at `n = 64`; scaling cubically, `n = 96` is `≈ 2.7 s` per determinant. The frozen ladder, gauge set, precision set, `x_sat` set and eleven mutations total a few hundred determinant evaluations. The frozen `3600 s` budget has headroom; a longer run is **disclosed, not silently accepted**.

**Mutual satisfiability of the gates (no gate contradicts another).**
1. **G2 and G5 probe different things and can disagree.** G2 asks whether the root moves with `n`; G5 asks whether anything else moves *toward* it. FT-5(a) is built on exactly that independence.
2. **G3 and G4 probe genuinely different knobs.** `λ` changes the analytic prefactor and therefore every coefficient function; `dps` changes only the arithmetic. FT-3's `𝒞₂`-omission shows G3 is sensitive to the coupling a real bug would break; FT-4(a) shows G4 is sensitive to arithmetic width.
3. **G6 does not presuppose G2.** A reimplementation could be `n`-stable at the wrong place. G6 is the only gate that would catch that, and FT-6 demonstrates it would.
4. **G7 and G10 are orthogonal.** G7 mutates the tensor rank; G10 mutates the losslessness. Neither mutation touches the other's object.
5. **G8 does not presuppose G1.** `x_sat`-invariance is a statement about the arithmetic path; the residual is a statement about the solution. Both can fail independently.
6. **No gate's PASS condition is another gate's FAIL condition.** Checked explicitly against audit WARN 4's finding that v2.1's FT-B was the logical negation of the gate it guarded: **FT-3's firing condition (`G3 spread ≥ 1e-6` under a mutation) is not G3's failure condition (`G3 spread > 1e-12` unmutated) — they are measured on different operators.**

---

## §10 — FLAGS RAISED AT FREEZE TIME (flag-don't-fix; surfaced, not resolved)

1. **⚑ FLAG-1 — the two `Q_GR` comparator values.** Fully stated in §7.3, with the robustness condition frozen as a criterion rather than argued afterwards. The programmatic `2.1002135791366907` is frozen (v1's and v2.1's choice, unchanged); the rounded-prose `2.099438202247191` at `research/2026-07-30_qlaw-derivation_scoping.md:401` is reported alongside. **Routed to the auditor lane as a corpus-precision question; not repaired here.**
2. **⚑ FLAG-2 — RECONCILED, NOT OVERRIDDEN: this lane DOES gate on a prior-lane number, and the distinction from v2.1's refusal is structural.** v2.1 froze: *"the #845 FT-6 value 0.21729 is NOT-ADJUDICATED prior-lane data produced by a SOLVER-NOT-CERTIFIED instrument and therefore may not gate this lane"*, on two stated grounds: (a) an uncertified instrument's diagnostic cannot certify its successor, and (b) **the two lanes evaluate that quantity on DIFFERENT objects**, so numerical agreement is not expected. **Ground (b) does not hold for the eigenvalue.** v1 and v2.1 compute the eigenvalue of the *same* problem — `ℓ = 2` toroidal, canonical graded profile, `Γ = −1` SHORT at `r_sat`, radiative port, `x_sat = 7` — by two different methods, and they agree to `6.803232e-07`. **Ground (a) is honoured in full and is why G6's direction of inference is fixed in advance:** Frozen: `G6 gates THIS lane's reimplementation against a prior-lane comparator and certifies NOTHING about PR #845, which remains SOLVER-NOT-CERTIFIED; a G6 pass may not be reported as corroboration of #845, and no #845 number enters any bin, any other gate, or any comparator in this lane`.
3. **⚑ FLAG-3 — I7 is assumed, not tested.** The reflectionless Regime-I port at infinity is a **frozen canonical input**, and this lane's entire method divides out the corresponding analytic factor. If the substrate carries any far-field reflector, every number here is wrong in the same direction — **including the certified root.** Surfaced in the §0 plumber question; not tested here; routed. **A `ROOT-CERTIFIED` verdict does not touch this flag.**
4. **⚑ FLAG-4 — #814 CF-7's naming gap stands, untouched.** `vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` and never names which `ρ`. This lane consumes the leading reading (`ρ₀`, I5) as a frozen input and does **not** repair the leaf.
5. **⚑ FLAG-5 — the completeness question is OPEN and this lane makes it harder to forget, not easier.** By declaring `BIN-4` `N/A BY CONSTRUCTION` the lane removes the temptation to read a certified root as a certified spectrum. **The open item is: derive a substrate low-frequency cutoff for the graded shear cavity.** Routed to Grant (§0) and to a successor lane; **not attempted, not sketched, not assumed here.**
6. **⚑ FLAG-6 — v2.1's I13 disclosure is now stale, and the correction is stated rather than propagated.** v2.1's ledger tagged `ω_I M (ℓ=2, n=1) = 0.273915` as *"EXTERNAL, no in-repo carrier"*. Since PR #845 merged (`052ccbba`), an in-repo carrier exists at `research/drivers/coldq_pole_derivation.py:106`. **This lane records the corrected provenance on its own ledger (I13) and does not edit the v2.1 prereg, which is frozen and byte-untouched.**
7. **⚑ FLAG-7 — the Makefile contact with the concurrent #854 branch, disclosed at freeze time.** This lane's gating number check is wired as its **own** target placed away from #854's insertion point, but two single-line list appends (the `.PHONY` list and the `verify:` prerequisite list) are lines the #854 branch also appends to. **This is an append-only textual contact on two lines, is disclosed here before either lane merges, and is for the orchestrator to sequence.** No physics, no gate and no result depends on it.

---

## §11 — LEDGER TAGS + OWED FOLLOW-ONS (fenced; NOT executed here)

**Ledger tags (`consistency-vs-emergence`, frozen).** `omega_R*M_g` is `[derived]` but **VALUE-CONSISTENCY** class (rides the GR-imported `7`). `Q` and `r_peak/r_sat` are `[derived]` and `ν_vac`-**FREE**, hence **emergence-capable at value level**. The GR numbers are `[GR-IMPORTED comparators]` (I11–I13). `ν_vac = 2/7` is `[canon]`, read-only, value GR-imported. Chebyshev orders, gauge parameters, precisions, the polish tolerance and `R_iso` are `[engineering]`. The v1 and v2.1 roots are `[PRIOR-LANE]`, one a seed and one a comparator, neither a bin input. **`α`-CLEAN. No manifestation-class claim. No claim of any kind is minted.**

**Owed follow-ons (fenced; Rule 12 — the slot is NOT refilled with an assertion):**
1. **★ The substrate low-frequency cutoff** for the graded shear cavity — the prerequisite for any completeness or overtone claim. Grant's input first (§0), then its own prereg. **Not sketched here.**
2. **The spheroidal (even-parity / P–SV-coupled) branch.** Toroidal only here.
3. **FORK-3's naming gap** (FLAG-4). Routed to the auditor lane.
4. **FORK-9's formal half** — whether Op6's phase-matching condition applies to a graded shear cavity with a `Γ = −1` inner wall.
5. **FORK-12** — untouched here; no `ℓ`-ladder is computed at all.
6. **FLAG-3's far-field assumption** — a test that the Regime-I port really is reflectionless at the scales that matter.
7. **The exterior-complex-rotation cross-check** as a genuinely independent third instrument. Not built here.

---

> **Pre-registration provenance.** Frozen pre-registration for the cold-Q pole **v2.2 ROOT certification**, authorized by Grant's ruling of 2026-08-03 on the PR #854 audit's Q2 — *certify the located root, not the rectangle*. Written against `origin/main` = `184db4b6`. Committed **ALONE** and pushed before any driver code and before any number produced by this instrument existed. **Predecessor lanes, all unmodified and byte-untouched by this lane:** `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` and `..._result.md` (PR #845, MERGED at `052ccbba`, `SOLVER-NOT-CERTIFIED`); `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` (commit `00724432`); `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` (commit `7d8fe484`) and its result doc (PR #854, OPEN, DO-NOT-MERGE, `SOLVER-NOT-CERTIFIED`). Companion inputs cited by path: `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51`; `research/2026-07-20_ringdown-systematics_checks.py:69`, `:72`, `:133`; `research/2026-07-30_qlaw-derivation_scoping.md:401`; `research/drivers/coldq_pole_derivation_results.json:505`, `:509`, `:510`, `:512`; `research/drivers/coldq_pole_derivation.py:106`; `src/ave/core/constants.py:397`. Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched regardless of outcome. Companion: the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-v2p2-root.md`.
