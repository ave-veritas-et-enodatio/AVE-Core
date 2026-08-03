# The cold-Q pole **v2.4** — FROZEN pre-registration (**ROOT certification; model-derived gates; supersedes v2.3 PRE-MEASUREMENT**)

**Date:** 2026-08-03
**Class:** DERIVATION pre-registration (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger — regardless of outcome**). Committed **ALONE** and pushed **before any driver code and before any number produced by this instrument exists**.
**Result-doc pointer requirement.** The result doc that resolves these bins MUST carry `Prereg-file: research/2026-08-03_coldq-pole-v2.4-root_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file (`manuscript/ave-kb/tools/verify-frozen-provenance.py`).
**Provenance:** Grant's standing ruling of 2026-08-03 — **certify the located root, not the rectangle** — carried forward unchanged.
**Written against** `origin/main` = `184db4b6`.

---

## ★ SUPERSESSION NOTE (2026-08-03) — v2.3 is superseded PRE-MEASUREMENT, and v2.3's file is BYTE-UNTOUCHED

### §S.1 What came before, in order

| lane | prereg (path @ commit) | outcome |
|---|---|---|
| **v1 / PR #845** (MERGED, `052ccbba`) | `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` | `SOLVER-NOT-CERTIFIED`. Real-axis asymptotic far-field matching; killed by an asymptotic `1/r` series plus an `exp(2\|Im ω\| R_match)`-ill-conditioned subdominant-coefficient extraction. All four bins `N/A`. |
| **v2** | `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` @ `00724432` | Frozen ALONE; **superseded PRE-MEASUREMENT** by v2.1. No driver, no number. **BYTE-UNTOUCHED, and never given a retraction header** — the supersession record lived entirely in v2.1's note. |
| **v2.1** | `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` @ `7d8fe484` | Frozen ALONE. Battery `bdcfa678`. `SOLVER-NOT-CERTIFIED`. **BYTE-UNTOUCHED.** |
| **v2.2** | `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` @ `f15a6e4d`; result `..._result.md` @ `982c4c9b` | **`ROOT-NOT-CERTIFIED` on exactly one gate, G2** (`1.2496816388248957e-10` vs frozen `1e-10`). Ten of eleven gates PASSED, eleven of eleven self-tests FIRED. **BYTE-UNTOUCHED.** |
| **v2.3** | `research/2026-08-03_coldq-pole-v2.3-root_prereg-FROZEN.md` @ **`3e2c0c1c`** (2026-08-03T07:23:37-07:00) | Frozen ALONE and pushed. **NO driver was ever executed and NO number produced by that instrument exists.** Superseded **PRE-MEASUREMENT** by this document. **BYTE-UNTOUCHED and given NO retraction header**, following the v2→v2.1 shape exactly. |

### §S.2 ★ WHY v2.3 IS SUPERSEDED — the eight-condition compliance table, reproduced as the auditable rationale

v2.3 was frozen at `3e2c0c1c` and pushed before an adversarial review of the v2.2 lane reported. When that review's findings arrived, the v2.3 lane audited **its own frozen document** against them and found it non-compliant on five of eight conditions and partially non-compliant on two more. **That audit is the rationale for this supersede and is reproduced here in full so the reasoning is auditable without any other document open:**

| # | condition | v2.3's frozen text @ `3e2c0c1c` | verdict |
|---|---|---|---|
| 1 | the convergence law is **root-exponential**, `E(n) ≈ C·exp(−c√n)`; the word "geometric" is wrong | v2.3 froze a gate literally named **`GEOMETRIC-CONVERGENCE SHAPE`** (its §5 table) testing a **constant ratio floor**, while quoting `1544.6 / 690.97 / 403.39` — **monotonically declining ratios** — in the same document | **NON-COMPLIANT.** A frozen criterion contradicted by a receipt quoted inside the same frozen file — the exact failure class this arc exists to repair |
| 2 | G2's tolerance derived from the convergence model | v2.3 derived it from a triangle-inequality bound on prior measurements (`1.6181e-13`, `618×` inside `1e-10`) | **NON-COMPLIANT** (though v2.2's digit-count defect was **not** inherited) |
| 3 | rung derivation + true citation sites | rung `n ≥ 40` correctly derived; primary-source location verified twice; **but v2.3:63 asserted v2.2 cites the receipt in "its §6 FT-2 non-vacuity column, *and its §9 G0 row*"** — the second clause is FALSE: v2.2's §9 G0 row cites v2.1's C11 `8.9716e-16`, not the coefficient tail | **PARTIAL — one inherited mis-location** |
| 4 | checker scope + the inherited FT-8 arithmetic | v2.3:516 froze `±1.43e-06` as the FT-8 perturbation magnitude. **The true values are `-2.857143e-07` and `+5.714286e-07`** (`1e-6·(x_sat−7)/7` at `x_sat = 5, 11`) | **NON-COMPLIANT — a false numeral inside a frozen document** |
| 5 | FT-7 must be a **differently-coded equivalent** spec | v2.3 froze v2.2's identical-code-path null, expected `0.0` — which measures determinism, not discriminator honesty | **NON-COMPLIANT** |
| 6 | mp strings per ladder rung | not required by v2.3's freeze | fixable without a criterion change |
| 7 | framing of the code relationship | v2.3's §2.3 **already** froze the honest version (carry-over, **not** independent reimplementation; G6 adds **no** new independence; agreement is a regression check) — **but FLAG-10 endorsed v2.2's own "independent transcription sharing no line of code" framing** | **COMPLIANT except the FLAG-10 endorsement** |
| 8 | the Makefile contact | v2.3's FLAG-12 called it an **"append-only textual contact"** | **NON-COMPLIANT characterization — it is a real two-line conflict** |

**Two things v2.3 did NOT inherit, recorded so the supersede is not read as a blanket condemnation:** it never cited `0a7dec1f`, and it never used a digit-count characterization to derive a tolerance. Both defects were consciously avoided.

**Why a versioned supersede and not an edit.** **Zero numbers exist from the v2.3 instrument** — its driver was written but never executed. This is therefore a clean **pre-measurement** supersede, governed by the same rule that took v2 to v2.1: the superseded prereg keeps its bytes, receives **no** retraction header, and the entire supersession record lives **here**. Frozen: `v2.3 (research/2026-08-03_coldq-pole-v2.3-root_prereg-FROZEN.md @ 3e2c0c1c) is superseded PRE-MEASUREMENT, with zero numbers produced by its instrument; its file is BYTE-UNTOUCHED and carries no retraction header, exactly as v2's prereg was left when v2.1 superseded it, and this section is the whole supersession record`.

### §S.3 ★ THE CONVERGENCE LAW, DERIVED HERE FROM AN IN-REPO BLOB — and the provenance problem with the relayed audit numbers, surfaced rather than smoothed

**This lane was instructed to derive the rung placement from a 12-rung measurement attributed to the adversarial review of PR #856 (a FAIL/PASS boundary between `n = 32` and `n = 36`; monotone decay over thirteen orders out to `n = 112`). Before citing that receipt this lane went looking for it, and could not find it.**

Checked at freeze time, all returning empty or unchanged:

```
gh pr view 856 --json comments      -> no comments
gh pr view 856 --json reviews       -> no reviews
gh api .../pulls/856/comments       -> no inline review comments
gh api .../issues/856/comments      -> no issue comments
git log origin/research/coldq-pole-v2p2   -> tip still 982c4c9b (unchanged since 07:00:07)
git branch -r                        -> no branch carrying an audit of #856
```

Frozen: `the 12-rung sweep attributed to the PR #856 review (the n = 32 / n = 36 FAIL-PASS boundary and the monotone decay to n = 112) is ORCHESTRATOR-RELAYED and was NOT independently verifiable in the repository record at this freeze; PR #856 carried no comments, no reviews and no inline review comments, and its branch tip was unchanged; it is therefore used ONLY as corroboration and NO gate, tolerance, ladder rung or bin in this lane depends on it`.

**So the model, its parameter band, and the ladder placement are derived HERE, from evidence this lane verified itself.** The primary evidence is an **in-repo blob**: the v2.2 shipped results object at commit `982c4c9b`, whose `diagnostics.spectral_convergence` block carries the per-rung errors at full double precision — not the 5-significant-figure table the v2.2 result doc printed:

```
research/drivers/coldq_pole_v2p2_root_results.json @ 982c4c9b
  diagnostics.spectral_convergence.reference_n = 96
  e(32) = 1.2496816369074884e-10
  e(48) = 8.090599741070316e-14
  e(64) = 1.1708996452296386e-16
  e(80) = 2.9026479440283196e-19
  e(96) = 0.0   (reference)
```

**The law.** A Chebyshev spectral discretization of a problem carrying an endpoint singularity converges **root-exponentially**, `E(n) = C·exp(−c·sqrt(n))`, not at a constant ratio per rung. **The declining ratios v2.2 published are the signature of exactly that law**, and v2.2's own label for them was wrong. Taking logs of the blob values above, pairwise:

```
c(32->48) = ln(e(32)/e(48)) / (sqrt(48)-sqrt(32)) = 5.775382
c(48->64) = ln(e(48)/e(64)) / (sqrt(64)-sqrt(48)) = 6.100131
c(64->80) = ln(e(64)/e(80)) / (sqrt(80)-sqrt(64)) = 6.354001
```

**A constant-ratio law would require these three to be a declining sequence of ratios and a NON-constant `c`; a root-exponential law requires a near-constant `c`. The measurement gives a near-constant `c`.** That is the discriminating computation, it is done here on an in-repo blob, and it does **not** depend on the relayed audit.

**Corroboration, both directions, stated as corroboration and not as the derivation:**
- the relayed audit's band `c ∈ 5.4 … 6.6` **contains all three** values computed above — an independent-source agreement, tagged per the frozen disclosure;
- the **verified** v2.1 receipt at **`research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:489`** (§9 item 7) @ `7d8fe484`, located by two methods (`git show … | grep -n` and `git show … | awk 'NR==489'`), verbatim: *"the Chebyshev coefficient tail of `𝒞` falls to `5.3e-16` by `n = 40`"* — a **coefficient-representation** statement that independently places the same floor under the ladder. It is restated by that lane at `:308`.

**★ THE OUT-OF-SAMPLE TEST, which is what actually places the ladder.** Fit `ln e(n) = ln C − c·sqrt(n)` by ordinary least squares on the **certification rungs only**, `n ∈ {48, 64, 80}`:

```
fitted c   = 6.216374
fitted lnC = 12.962558          (C = 4.261549e+05)
residuals in ln e:  -0.039741, +0.084849, -0.045108      max |residual| = 0.084849
```

Extrapolate that fit — which never saw `n = 32` — **out of sample** to `n = 32`:

```
predicted e(32) = 2.277976e-10        measured e(32) = 1.249682e-10      pred/meas = 1.8228
```

**The model, fitted only on rungs at or above 48, predicts that `n = 32` cannot pass a `1e-10` gate — and the measurement agrees.** The ladder's lower rung is therefore placed by a **law that this lane fitted and tested out of sample**, not by the outcome it produces and not by a relayed characterization. Frozen: `the G2 certification ladder's lower rung is placed by the root-exponential convergence law E(n) = C*exp(-c*sqrt(n)) fitted on rungs n in {48, 64, 80} of the in-repo blob research/drivers/coldq_pole_v2p2_root_results.json @ 982c4c9b, whose out-of-sample extrapolation predicts e(32) = 2.277976e-10 against a measured 1.249682e-10, both above the frozen 1e-10; the v2.1 coefficient-tail receipt at research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:489 @ 7d8fe484 corroborates the same floor from the coefficient side, and the orchestrator-relayed PR #856 sweep corroborates the c band without being depended on`.

### §S.4 ★ THE CHANGES, stated precisely and exhaustively (relative to v2.2, the last lane that produced a number)

**CHANGED — one gate specification:**
> **G2's certification ladder becomes `n ∈ {48, 64, 80, 96}` at the SAME frozen `1e-10` tolerance**, whose value is now **derived from the convergence model** (§4.4(d)) rather than inherited.

**ADDED — one supplementary gate and one self-test, both built on the ROOT-EXPONENTIAL model:**
> **G2b** — the convergence-law gate: fit `ln e(n) = ln C − c·sqrt(n)` on the certification rungs; gate on **(i)** the fit residual and **(ii)** the fitted `c` lying inside a frozen band. **FT-2b** — a stagnation mutation that drives the fitted `c` out of band.

**REPAIRED — five inherited defects, each named in §S.2:** the convergence-law framing (condition 1); the tolerance derivation (2); the citation mis-location (3); the FT-8 non-vacuity arithmetic (4); FT-7's identical-code-path null (5). **Plus** mp strings per rung (6), the FLAG-10 framing (7) and the FLAG-12 characterization (8).

**RETAINED, NOT DELETED — the `n = 32` rung, in three roles:** a **gated** rung of `G4(b)`, `G5`, `FT-5(a)` and `FT-5(b)`, which sweep the **full** ladder `{32, 48, 64, 80, 96}` unchanged; a **mandatory non-gated diagnostic row** of G2; and a **pre-registered expectation** (§9). **No measurement is hidden.**

**UNCHANGED — everything else,** restated self-contained below: the target and seed; the non-claims; the physics; the operator; the import ledger; `R_iso = 0.5` and its four receipts; G0, G1, G3–G10 and their tolerances; FT-0, FT-1, FT-2, FT-3, FT-4, FT-5, FT-6, FT-8, FT-9, FT-10; **every BIN-1/2/3 boundary**; the FLAG-1 window; the precedence order; `BIN-4 = N/A BY CONSTRUCTION`.

**★ Vocabulary fence, frozen.** Frozen: `the word "geometric" describes no convergence law in this lane and appears only inside dated quotations of superseded text; the law is ROOT-EXPONENTIAL, E(n) = C*exp(-c*sqrt(n))`.

### §S.5 ★ KILL-SWITCH DISCLOSURE, restated for this lane

The adversarial review of PR #856 had **still not landed a receipt in the repository record** at this freeze (§S.3). Its relayed findings **corroborate** this lane and are **not depended on** by any gate. Frozen: `no gate, tolerance, ladder rung or bin in this lane depends on the orchestrator-relayed PR #856 findings; if a receipt lands in the repository and CONTRADICTS the root-exponential fit derived in section S.3 from the in-repo blob at 982c4c9b, this lane HALTS at its next commit boundary, reports state, and any certification it has produced is VOID`.

---
## §0 — SECTOR / REGIME / PHASE-STATE / COORDS header, declared BEFORE any physics word

**Re-walked fresh, not incorporated by reference.** A successor that inherits a header without re-walking it inherits the header's blind spots too. The walk below reaches the same conclusions v2.2's did — **which is the expected outcome, because this lane changes a discretization parameter and not one line of physics** — and that agreement is stated as a result of the walk, not assumed before it.

- **MODE.** Cold (`a_* = 0`, Schwarzschild-limit) post-merger remnant ringing down. The object is **one** quasinormal resonance of the saturation cavity — the `ℓ = 2` toroidal shear mode located by v1, v2.1 and v2.2 — and **not** its ladder.
- **SECTOR.** The **observable** is a **transverse shear (T2)** oscillation. The **bias field** that builds the cavity is the **A1 radial dilatation** `ε_11 = 7GM/(c²r)`. Orthogonal grades, **not cross-wired**: the A1 strain is the DC operating point that sets the constitutive profile; the T2 shear mode is the small-signal AC riding on it. Receipt for `ε_11` **being** the Axiom-4 amplitude `A`: [`common/vocabulary-register.md:309`](../manuscript/ave-kb/common/vocabulary-register.md), verbatim *"the A1-dilatation **radial "strain"** that IS the Axiom-4 saturation **amplitude $A$**"*.
- **REGIME.** Far field (`r ≫ r_sat`) = **Regime I** — linear, lossless, reactive; a legal radiating port. The graded exterior `r > r_sat` = Regime I with a spatially varying modulus (Op14 grade). The wall `r = r_sat` = the **Regime III→IV** soft-mode terminus, `G_shear → 0`. The interior `r < r_sat` = **Regime IV**, where shear cannot propagate at all and which is therefore **not part of the computational domain** — the domain is `[r_sat, ∞)`, and that is a physics statement, not a truncation.
- **PHASE-STATE.** Op14 ON throughout the graded exterior as a **static constitutive grade** (the DC bias is time-independent; the ringdown is the small-signal response). `A = 1` exactly at `r_sat = 7GM/c²`; `Γ_shear = −1` there.
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the **dimensionless-eigenvalue register** (`ω_R M_g`, `ω_I M_g`, `Q`) that AVE and GR share — no phase-space/real-space mismatch. This lane solves for the **complex pole** directly, so what it returns *is* the pole-`Q` that the GR comparator is; **no port→pole transfer is performed, needed, or assumed.**
- **The eigenfunction's own coordinate.** The radial localization observable (BIN-3) is read in **real-space radius normalized to `r_sat`** and compared only against real-space radii. It is **not** compared against `r_eff = 49M_g/9`, which is a **spectral marker (a cutoff radius), not a place**.

### Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of numerical code)

1. **K4 / srs connectivity.** This is a **CONTINUUM** instrument. Frozen disclosure: `the radial channel is a CONTINUUM representation of the shear constitutive law; it is not a discretization of the srs stencil and carries no K4 connectivity claim`. What it consumes from the lattice is the **constitutive law only**: the Ax-4 kernel and the Op16 shear-speed projection.
2. **Cosserat / channel basis.** The mode certified is on the **toroidal (odd-parity / axial) branch**, whose displacement field is **exactly divergence-free**, so the Lamé `λ` (bulk/A1) modulus drops out of the equations of motion **identically** rather than by assumption. Frozen: `the toroidal (odd-parity) branch is exactly divergence-free, so the bulk modulus drops out identically and there is no linear P-SV conversion partner; the single-channel classification is structural in this branch`.
3. **Op14 saturation.** Enters as the **static constitutive grade** `S(A) = sqrt(1 - A²)` with `A(r) = r_sat/r`, projected into shear by Op16. Frozen: `Op14 enters as a static constitutive grade S(A); the A -> 1 terminus is handled by an exact change of variable, not by a numerical cutoff or a regularized floor`.
4. **★ The compactification is the medium's own order parameter, and that is what makes the ROOT-LOCAL gates meaningful.** The radial coordinate is `A = r_sat/r` — the Axiom-4 saturation amplitude itself; `A = 1` IS the wall, `A = 0` IS infinity. Frozen: `the compactified radial coordinate is the Axiom-4 saturation amplitude A = r_sat/r itself, so A = 1 is the wall and A = 0 is infinity; the instrument adopts the medium's own order parameter as its coordinate rather than imposing a lattice-Cartesian one`. **Root-local consequence, stated in advance:** because `r_sat` appears in the discretized operator *only* through this coordinate and through `Ω = ω r_sat`, a root-local `x_sat`-invariance measurement (G8) is a check on the arithmetic path, not on the physics — the physics cancellation is structural. It is gated anyway, in mp, because v2.1's version of this measurement was corrupted by a `complex` cast (PR #854 audit WARN 7).
5. **Phase-space vs real-space (A46).** Every verdict-class observable is a **dimensionless ratio**: `ω M_g`, `Q`, `r_peak/r_sat`. **α-CLEAN** — `α` appears nowhere in the chain.
6. **Checkpoint: boundary-not-bulk.** The resonator is a **boundary/graded-shell** object, not a bulk-force object — consistent with the #403/#404 localization ruling. The loss is a **radiative port at infinity** (Ax-3-licensed), and there is **no** `Re{Z}` anywhere in the medium. **G10 tests exactly that, and it tests it ON THE CERTIFIED EIGENFUNCTION'S OWN OPERATOR** rather than on a separate closed cavity.
7. **Checkpoint: what the substrate does NOT supply.** The angular index `ℓ = 2` is **not** derived here; it is the quadrupole selection the corpus carries for the GW channel. **And the substrate does not here supply a low-frequency cutoff either, which is exactly why no completeness claim is made.** Stated so neither is mistaken for an output.
8. **★ NEW CHECKPOINT, forced by this lane's one change: is the Chebyshev order a physics knob or an engineering knob?** It is an **engineering knob**, and the check is that nothing physical depends on it: `n` enters the medium nowhere — not the profile `A = r_sat/r`, not the kernel `S = sqrt(1 − A²)`, not the Op16 projection, not the `Γ = −1` wall, not the port. It enters **only** the representation of the coefficient functions on the grid. Frozen: `the Chebyshev order n is an ENGINEERING knob that enters the representation and enters the medium nowhere; changing which orders a convergence gate is measured over changes no physical content, and the only thing it can legitimately change is whether the gate is measuring the root or measuring the basis`. **This is the checkpoint that licenses the ladder change as a numerics repair rather than a physics retune — and it is also the checkpoint that would forbid changing `x_sat`, `ℓ`, the kernel or the wall condition, none of which this lane touches.** **Corollary, and it is why G2b can exist at all:** because `n` is purely representational, the way the error decays in `n` is a property of the *representation* and of the operator's *analytic structure* — an endpoint singularity gives `E(n) = C·exp(−c·sqrt(n))` — and is therefore a legitimate object for a gate to test **without** that gate making any physical claim.

### Pre-test physics check (`pre-test-physics-check`, Rule 16 — ONE plumber question surfaced to Grant BEFORE the design locks)

> **Grant — this is a NEW question, and it is the one this lane creates rather than the one v2.2 asked.** v2.2's question was about the *bottom* of the sweep (the low-frequency cutoff) and it is still open, still deferred, and restated unchanged in FLAG-5. **My question is about where the energy sits, because this lane is the first in the arc that can actually reach BIN-3 and land a verdict on it.**
>
> Here is what the uncertified prior run saw. I walk outward from the wall at `r = r_sat` and integrate the mode's stored energy density. It does **not** peak anywhere inside my window — it keeps climbing all the way to `r/r_sat = 2.0`, which is just where I stopped looking. The wall itself holds about `4 %` of the window's maximum. **In plumber terms: I've got a shorted stub with a taper on it, I'm looking for the belly of the standing wave, and I can't find one — the amplitude just keeps growing as I walk away from the short.**
>
> Two readings, and I cannot tell them apart from inside the numerics:
> - **(a) It's real.** The cavity genuinely stores its energy far out on the taper, the "rim ring" picture is wrong, and `r_eff` is a spectral marker with no place attached to it.
> - **(b) It's the leak, not the mode.** Any leaky resonator's eigenfunction grows like `exp(|ω_I| r)` on the way out — that's the outgoing wave that left earlier, arriving with more amplitude because the thing was ringing harder back then. **On that reading "where does the mode live" is the wrong question for a radiating cavity, and any answer I compute is a statement about my window's right-hand edge.**
>
> **What I need from you is the plumber's call on whether (b) is simply what a leaky resonator does** — because if it is, `BIN-3-MONOTONE` is the honest verdict and the localization axis should be retired from this arc rather than re-measured with a wider window. I have **pre-registered `BIN-3-MONOTONE` as a reachable bin** (§7.4) precisely so this can land in a pre-registered slot instead of in prose after the fact. **I am not widening the window to hunt for a peak, and I am not re-defining the observable.** The window stays `[1.0, 2.0]`, byte-identical to v1/v2.1/v2.2.
>
> **Carried forward unchanged and NOT re-asked:** v2.2's deferred question — a **substrate-derived low-frequency cutoff** for the graded shear cavity, without which no completeness or overtone statement is honest. `BIN-4` stays `N/A BY CONSTRUCTION` for as long as that takes.

### Consistency-vs-emergence tag (`consistency-vs-emergence`), computed BEFORE any result — and it is not uniform across the bins

Written in units of `r_sat`, the problem has **no free parameter at all**: the profile is `A = r_sat/r`; the kernel is `S = sqrt(1 - A²)`; the speed is `c_shear = c₀·sqrt(S)`; the inertia is the cold `ρ₀`. Therefore `Ω ≡ ω·r_sat/c₀` is a **pure number** fixed by the profile SHAPE, the Ax-4 kernel, and `ℓ`.

| output | rides `r_sat`'s coefficient `7`? | class |
|---|---|---|
| `ω_R M_g` (BIN-1) | **YES** — `ω_R M_g = Re(Ω)/x_sat` with `x_sat = 7` | **VALUE-CONSISTENCY.** The `7` is the `1/7` trace-reversed bulk projection, which takes `ν_vac = 2/7` as **input** ([`one-seventh-impedance-projection.md:18`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md): *"the $1/7$ boundary is a projection of a GR-imported ratio, not a first-principles lattice output"*). **May NOT be headlined as value-level emergence.** |
| **`Q = ω_R/(2\|ω_I\|)` (BIN-2)** | **NO — it cancels exactly** | **`ν_vac`-FREE, therefore EMERGENCE-CAPABLE at value level.** `Q = Re(Ω)/(2\|Im(Ω)\|)`; the `x_sat` conversion divides out identically. |
| `r_peak/r_sat` (BIN-3) | **NO** | `ν_vac`-free ratio; **FORM-class** statement about where the mode lives. |
| the existence + location of the root itself | **the LOCATION rides it; the SHAPE does not** | The certified object is `Ω`, a pure number. Its projection into `ω M_g` is what carries the imported `7`. |

Frozen tag: `Q and the localization ratio are exactly nu_vac-free (the r_sat scale divides out identically); omega_R*M_g is NOT and is VALUE-CONSISTENCY class because the 7 in r_sat = 7GM/c^2 is the 1/7 projection of the GR-imported nu_vac = 2/7`.

> **★ WHAT A CERTIFIED ROOT WOULD AND WOULD NOT MEAN, written before the run.** A `ROOT-CERTIFIED` verdict is a statement about an **instrument**, not about the world: it says *this discretization's eigenvalue at this location is a property of the continuous problem and not of the discretization*. It does **not** say the substrate rings there — that additional step needs the canonical input set of §3 to be right, and I7 in particular is **assumed, not tested** (FLAG-3). And it says **nothing whatever** about what else the substrate does or does not do at other frequencies (§1's non-claim). **Additionally, and specific to this lane:** a `ROOT-CERTIFIED` verdict here would be earned on a ladder that **excludes** `n = 32` from one gate on the strength of a fitted convergence law, and any reader is entitled to the `n = 32` number and to the law's own out-of-sample prediction for it — which is why both are reported (§5, §9).

---

## §1 — THE TARGET, AND THE EXPLICIT NON-CLAIM

### §1.1 The target

**Certification of the SINGLE located root of the graded spin-2 hyperboloidal problem near**

```
Omega_0  =  1.8536552108408788 - 1.0072567831433188 i
```

**Seed provenance.** That value is transcribed from the v2.1 shipped results object, `research/drivers/coldq_pole_v2_results.json`, at commit `bdcfa678` (branch `research/coldq-pole-v2`, PR #854, **OPEN, DO-NOT-MERGE — the file is not on `origin/main`, which is why it is transcribed rather than read**). It is the same seed v2.2 used, unchanged. It is carried in the driver as a named frozen constant with that citation in a comment.

Frozen: `the frozen seed Omega_0 = 1.8536552108408788 - 1.0072567831433188i is a SEED ONLY: at each order the polish is seeded from the double-precision linearized-pencil eigenvalue NEAREST the frozen seed, so the seed selects WHICH pencil eigenvalue is polished and enters no gate, no tolerance, no comparator and no bin as a value`.

**Certification means: ALL root-local gates G0..G10 (including G2b) of §5 PASS and ALL fireability self-tests FT-0..FT-10 (including FT-2b) of §6 FIRE.** There is no partial certification and no scoped certification in this lane: `ROOT-CERTIFIED` or `ROOT-NOT-CERTIFIED`.

### §1.2 The non-claim, written in advance and binding

> **This lane asserts the existence and location of THIS root; it asserts NOTHING about the absence or presence of other modes.**

Frozen: `this lane asserts the existence and location of THIS root; it asserts NOTHING about the absence or presence of other modes`.

Operationally, and each of these is a **prohibition on this lane's own result doc**:

- **NO winding, argument principle, or contour integral is computed over any rectangle, box or region, anywhere in this lane.** Frozen: `no argument-principle winding, no contour integral and no region count is computed anywhere in this lane; the pole-counting instrument the PR #854 audit impeached is not used, not repaired and not relied on`.
- **NO completeness claim, no "the only mode", no "no overtones", no mode count, no ladder.** `BIN-4` is `N/A BY CONSTRUCTION` (§7), stated **in advance**, and that status is **not** an outcome of any measurement.
- **NO claim that the certified root is the FUNDAMENTAL.** It is *a* root. Whether it is the least-damped, the lowest, or the physically-selected one is **not adjudicated here**.
- **The pseudo-spectrum the PR #854 audit found is not re-measured, not characterised, and not explained here.** G5 measures only whether it comes within a frozen radius of the certified root.
- **★ NEW, and binding on this lane specifically: a certification here is NOT a retroactive pass for v2.2.** Frozen: `a ROOT-CERTIFIED verdict in this lane does not certify, rescue, re-score or reverse v2.2, which stands ROOT-NOT-CERTIFIED on the ladder it froze, and does not revive v2.3, which is superseded pre-measurement; and it does not establish that the n = 32 rung was harmless, only that the fitted convergence law places it below the order at which the representation is converged`.

### §1.3 What this lane additionally does NOT do

- **X1 — does NOT derive `ℓ = 2`.** The quadrupole selection is an input.
- **X2 — does NOT derive `ν_vac`, `K = 2G`, or the `7` in `r_sat`.** Their value provenance is GR-IMPORT, closed by PR #261/#506 and untouched here.
- **X3 — does NOT touch the spin (`a_* > 0`) mapping.** This is the `a_* = 0` anchor only.
- **X4 — does NOT compute a port-`Q`, a radiation resistance, or a Chu/Collin–Rothschild stored-energy `Q`.**
- **X5 — does NOT adjudicate #814 FORK-12.** No `ℓ`-ladder is computed in this lane at all.
- **X6 — does NOT run FORK-3(b)** (`ρ_eff = ρ₀/S³` as the shear-wave inertia).
- **X7 — does NOT certify, rescue, re-adjudicate or repair PR #845, PR #854, PR #856, or the superseded v2.3 freeze.** All remain as they stand. **G6's two-instrument agreement is a check on THIS lane's transcription, not a certification of any predecessor** — see FLAG-2 in §10.
- **X8 — does NOT derive, assume, sketch or gesture at a low-frequency cutoff.** Deferred, with Grant's input owed first (§0).
- **X9 — does NOT land any claim, solidity change, KB row, manuscript edit or ledger entry**, whatever the outcome.
- **X10 — NEW: does NOT widen, move or re-define the BIN-3 localization window, and does NOT re-tune any bin boundary.** Every boundary in §7 is byte-identical to v2.2's, which were byte-identical to v2.1's and v2's and v1's.

---
## §2 — THE PHYSICS (inherited, ratified, NOT re-derived) AND THE OPERATOR THIS LANE CARRIES OVER

### §2.1 Inherited unchanged from the ratified v1/v2.1/v2.2 framing — stated, not re-derived

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

### §2.3 ★ THE CARRY-OVER DISCLOSURE — this lane is NOT an independent third reimplementation, and that changes what G6 buys

**This is the single most important honesty statement in this document and it is written before any code exists.**

v2.2's §2.3 froze an **independent reimplementation** disclosure and argued that G6 was therefore a live check on a fresh transcription. **This lane does something different, deliberately, and the difference is disclosed rather than glossed:**

Frozen: `the v2.4 instrument CARRIES OVER v2.2's method into this lane's own file research/drivers/coldq_pole_v2p4_root.py by copy-with-attribution, so that the ONLY differences between the two batteries are the gate specifications of section S.4; it is NOT an independent third reimplementation, and this lane may not claim reimplementation independence from v2.2`.

**Lineage disclosure, stated rather than left to be discovered.** The v2.3 lane wrote a driver at `research/drivers/coldq_pole_v2p3_root.py` and **never executed it** — no results object, no digest, no number of any kind was produced by it, and it was never committed. Its file is adapted here under the new version number. Frozen: `the v2.4 driver is adapted from the UNCOMMITTED and NEVER-EXECUTED v2.3 driver, which produced no results object, no digest and no number; the adaptation is therefore pre-measurement and carries no contamination, and this lineage is disclosed rather than presented as a fresh authorship`.

**Why carry over rather than reimplement a third time.** The scientific question this lane exists to answer is *"does the certification change when the defective gate specifications are repaired?"* A fresh third transcription would answer a **different** question — *"does a third instrument agree?"* — and would confound the two: any change in the gate table could then be the ladder **or** the new transcription. **Carrying the method over unchanged makes the gate-specification changes the only variable.** That is a controlled comparison, and it is chosen for that reason.

**The four consequences, each stated as a limit on what this lane may claim:**

1. **G6 no longer demonstrates independence from v2.2.** It still gates this lane's file against v1's **different-in-kind** instrument (real-axis asymptotic matching, sharing no formulation with this one), and FT-6 still demonstrates it catches a coefficient corruption. **But a G6 pass here is not evidence that two independent implementations agree — v2.2 already established what it established, and this lane adds nothing to it.** Frozen: `G6 in this lane gates THIS file's transcription against v1's different-in-kind instrument and adds NO new implementation-independence beyond what v2.2 already reported; a G6 pass here may not be presented as a second independent confirmation`.
2. **Numerical agreement with v2.2 is EXPECTED, not corroborative.** Every unchanged gate should reproduce v2.2's number, and where it does that is a **regression check**, not a confirmation. Frozen: `agreement between this lane's unchanged gates and v2.2's is a REGRESSION CHECK on the carry-over and is not independent corroboration of any value`.
3. **A DISagreement on an unchanged gate is a defect, and it is reported as one.** If any unchanged gate's measured value differs from v2.2's published value by more than its own reporting precision, that is a carry-over error or a platform difference, and the result doc must surface it with both numbers. Frozen: `if any gate this lane did not change measures differently from the value v2.2 published, the result doc reports BOTH numbers and treats the difference as a defect to be surfaced, not as a new measurement`.
4. **Attribution is at the transcription site.** Every routine and every algebraic form carried over carries a comment naming its source file and lane. `research/drivers/coldq_pole_v2p2_root.py` and `research/drivers/coldq_pole_v2.py` are **neither imported nor edited nor executed** by this lane; they belong to PR #856 and PR #854 respectively and are byte-untouched here.

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
| **I7** | Outer boundary condition | outgoing radiation into the cold matched lattice; **no far-field structure, no second reflection** | **`[canon]` — Regime-I radiative port, Ax-3-licensed. ASSUMED, NOT TESTED — see FLAG-3** | §0 REGIME header |
| **I8** | Angular index | `ℓ = 2` (quadrupole) | **`[canon, INPUT not derived]`** | §1.3 X1 |
| **I9** | Unit choice | `M_g = 1`, `c₀ = 1`, `ρ₀ = 1`, hence `G₀ = 1` | **`[dimensionless by construction]`** | this lane |
| **I10** | `ν_vac = 2/7` | imported **read-only** from `ave.core.constants.N_NU`; used ONLY to form the `r_eff = r_sat/(1+ν_vac)` comparator reported alongside BIN-1 | **`[canon]` — VALUE GR-IMPORTED (PR #261/#506)** | `src/ave/core/constants.py:397` |
| **I11** | GR cold comparator | `ω_R M = 0.37367`, `ω_I M = 0.08896` at `a_* = 0`, read **programmatically** from the frozen `KERR_QNM` dict | **`[GR-IMPORTED comparator — the frozen C-comparator, inherited unchanged from v1, v2.1 and v2.2]`** | `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51` |
| **I12** | GR `ℓ=2` overtone real parts | `ω_R M (2,0) = 0.373672`, `(2,1) = 0.346711`, read **programmatically** from the in-repo `SCHW_OMEGA_R` dict | **`[GR-IMPORTED comparator]` — used ONLY to derive the G5 isolation radius's upper constraint (§4.3); enters no bin** | `research/2026-07-20_ringdown-systematics_checks.py:69`, `:72` |
| **I13** | GR `ℓ=2` overtone imaginary parts | `ω_I M (2,0) = 0.088962` from the in-repo `SCHW_OMEGA_I` dict; `ω_I M (2,1) = 0.273915` with in-repo carrier `research/drivers/coldq_pole_derivation.py:106` (merged with PR #845) | **`[GR-IMPORTED comparator]` — same restricted use as I12; enters no bin** | `research/2026-07-20_ringdown-systematics_checks.py:133`; `research/drivers/coldq_pole_derivation.py:106` |
| **I14** | Standing AVE comparators | `ω_R M_g = 18/49`, `Q = ℓ = 2`, `r_eff = 49M_g/9` | **`[corpus comparators — the objects under test]`** | `vol3/claim-quality.md:198`; `vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md`; #814 CF-9 |
| **I15** | Prior-lane root, v2.1 | `Ω_0 = 1.8536552108408788 − 1.0072567831433188i` | **`[PRIOR-LANE SEED — selects which pencil eigenvalue is polished; enters no gate, tolerance, comparator or bin]`** | `research/drivers/coldq_pole_v2_results.json` @ `bdcfa678` |
| **I16** | Prior-lane root, v1 | `Ω_v1 = x_sat·(omega_R_M − i·omega_I_M)` reconstructed **programmatically** from the shipped v1 JSON row `x_sat = 7.0` | **`[PRIOR-LANE COMPARATOR — G6 only; NOT-ADJUDICATED prior-lane data, gates THIS lane's transcription and certifies nothing about #845]`** | `research/drivers/coldq_pole_derivation_results.json:505`, `:509`, `:510`, `:512` |
| **I17** | Prior-lane discretization artifact | `Ω_art = 0.30587571217415294 − 2.4674822214282157i`, banked by v2.1's own frozen physical-vs-artifact criterion | **`[PRIOR-LANE FIREABILITY TARGET — FT-5 and the G2b artifact diagnostic only]`** | `research/drivers/coldq_pole_v2_results.json` @ `bdcfa678` |
| **I18** | Prior-lane contaminated-edge probe | `Ω_edge = 0.1400 − 3.5035i`, one of v2.1's own frozen C9 probe points, measured there at `3.658e+00` | **`[PRIOR-LANE FIREABILITY TARGET — FT-5 only]`** | v2.1 result doc §3.2 probe table @ `bdcfa678` |
| **I19** | Instrument numerics | Chebyshev order `n`, gauge `λ`, mp precision `dps`, polish tolerance and iteration cap, dedupe radius, isolation radius `R_iso`, **the G2b ratio floor** | **`[ENGINEERING CHOICE — tagged, frozen in §4]`** | this lane |
| **I20 ★** | **Prior-lane coefficient-resolution receipt** | the Chebyshev coefficient tail of `𝒞` falls to `5.3e-16` by `n = 40` | **`[PRIOR-LANE MEASURED RECEIPT — used ONLY to place G2's certification-ladder lower rung; enters no tolerance, no comparator and no bin]`** | `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:489` (§9 item 7) @ `7d8fe484`, restated at `:308` |
| **I21 ★** | **Prior-lane per-rung convergence errors, FULL PRECISION** | `e(32) = 1.2496816369074884e-10`, `e(48) = 8.090599741070316e-14`, `e(64) = 1.1708996452296386e-16`, `e(80) = 2.9026479440283196e-19` against the `n = 96` reference | **`[PRIOR-LANE MEASURED DIAGNOSTIC, read from an IN-REPO BLOB — used ONLY to fit the convergence law of §4.4 and to place the ladder rung; enters no bin. Produced by a ROOT-NOT-CERTIFIED instrument, so it is used to fit a LAW and to set bands with headroom, never as a value]`** | `research/drivers/coldq_pole_v2p2_root_results.json` @ `982c4c9b`, key `diagnostics.spectral_convergence` |
| **I22 ★** | **Orchestrator-relayed review findings** | a 12-rung sweep with a FAIL/PASS boundary between `n = 32` and `n = 36`, monotone decay to `n = 112`, and a band `c ∈ 5.4 … 6.6` | **`[ORCHESTRATOR-RELAYED, NOT INDEPENDENTLY VERIFIABLE IN THE REPOSITORY AT THIS FREEZE — corroboration only; NO gate, tolerance, ladder rung or bin depends on it]`** | §S.3; PR #856 carried no comments, no reviews and no inline review comments at freeze, and its branch tip was unchanged at `982c4c9b` |

**R8 audit rule (frozen).** `every number the instrument consumes appears on this ledger with its tag; no SM/GR convention default enters anywhere, and in particular no spin-1 vector-multipole impedance, no Chu/Collin-Rothschild stored-energy weighting, and no Regge-Wheeler or Zerilli potential is used as an input`.

**★ Ledger discipline note on I20, I21 and I22, stated at freeze.** All three are numbers produced outside this lane by instruments that are **not certified**, and I22 could not even be located in the repository record. **None is used as a value.** I20 places a ladder rung **above** the resolution it reports. I21 is used to **fit a law** whose out-of-sample prediction is then tested, and to set **bands with headroom** — never to set a target. I22 is **corroboration only**. Frozen: `I20, I21 and I22 are used ONLY to place a ladder rung above a measured resolution, to fit the convergence law and set its bands with headroom, and to corroborate; none enters a bin, a comparator or a tolerance as a value, none is depended on by any gate in the case of I22, and a certification in this lane certifies no predecessor`.

---
## §4 — THE METHOD AND ITS FROZEN NUMERICS

### §4.1 The method (frozen, unchanged)

Frozen: `the method is a compactified hyperboloidal Chebyshev spectral discretization in the Axiom-4 amplitude coordinate A = r_sat/r with the outgoing wave divided out in closed form, the traction-free SHORT imposed exactly as dpsi/deta = 0 at eta = 0, no boundary condition imposed at infinity, root extraction by extended-precision determinant polish seeded from the double-precision linearized pencil, and eigenfunction extraction by extended-precision inverse iteration; there is no matching radius, no asymptotic series, no shooting, no subdominant-coefficient extraction and NO ARGUMENT-PRINCIPLE WINDING anywhere in the chain`.

**ENGINEERING-CHOICE TAG (`substrate-first-for-numbers`).** Frozen: `the method is NUMERICS and is tagged ENGINEERING CHOICE; the medium, the profile, the kernel, the wall condition and the radiative port are CANON; no physical content of any kind is derived from the choice of discretization, and the gauge parameter lambda, the Chebyshev order n, the extended-precision dps, the polish tolerance, the isolation radius and the convergence-law bands are engineering knobs whose only permitted role is to be varied and shown not to move the answer, or to be justified from measured evidence and frozen`.

### §4.2 Frozen numerics (every parameter fixed here, before any code)

- **Radial coordinate:** `A = r_sat/r`, `A = 1 − η²`, `η ∈ [0,1]` on Chebyshev–Gauss–Lobatto nodes.
- **Primary Chebyshev order:** `n = 48`.
- **FULL frozen ladder** (unchanged; swept by G4(b), G5, FT-5(a), FT-5(b), and by G2's diagnostic row): `n ∈ {32, 48, 64, 80, 96}`.
- **G2 CERTIFICATION ladder:** `n ∈ {48, 64, 80, 96}`.
- **Hyperboloidal gauge:** primary `λ = 0`; frozen set `λ ∈ {−0.25, 0.0, +0.25}`.
- **Extended precision:** primary `dps = 50`; high-precision cross-check `dps = 80`.
- **Polish:** deterministic complex secant on `det M(Ω)` by mp LU with partial pivoting, seeded from the double-precision linearized-pencil eigenvalue nearest the frozen seed, terminating at `|Δ| ≤ 1e-38·|Ω|` or `60` iterations. **No RNG; no adaptivity; fully deterministic.**
- **Eigenfunction:** `4` rounds of mp inverse iteration on the row-equilibrated `M(Ω*)`, from the deterministic all-ones vector, infinity-normalized after each round.
- **Row equilibration:** each row of `(M0, M1, M2)` divided by that row's max modulus across the three matrices.
- **Dedupe radius:** `1e-6` relative.
- **`x_sat` set (G8):** `{5, 7, 11}`, mp end-to-end with **no** `complex` cast on the path from the polished root to the reported spread.
- **Localization window (BIN-3):** `r/r_sat ∈ [1.0, 2.0]`, `401` points. **Byte-identical to v1/v2.1/v2.2; not widened.**
- **★ Convergence law:** `E(n) = C·exp(−c·sqrt(n))`. **Frozen `c` band:** `[4.4, 7.6]`. **Frozen fit-residual floor:** `0.40` (max `|residual|` in `ln e`). Both derived in §4.4.
- **★ mp reporting:** Frozen: `the shipped results object carries Omega_re_mp and Omega_im_mp as 40-digit mp STRINGS for EVERY rung of the FULL ladder, for every gauge, for every dps and for every x_sat, so that no reported separation depends on a double-precision cast of the root`.
- **Runtime:** frozen `total battery runtime <= 3600 s on the reference machine; a longer run is disclosed, not silently accepted`. **Not** an adjudication criterion.
- **Engine fence:** Frozen: `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`.

### §4.3 THE G5 ISOLATION RADIUS — carried over unchanged, with its four receipts

> **DISCLOSURE.** Every number here is arithmetic on already-published prior-lane values (the v1 and v2.1 shipped JSONs and the frozen GR comparators I11–I13), reproduced by the driver.

`R_iso` is the exclusion-annulus radius around the certified root inside which no other eigenvalue of the discretization's spectrum may sit, at any order of the FULL ladder. Bounded ABOVE by physics (must not forbid a genuine overtone) and BELOW by numerics (must exceed the dedupe radius).

```
Om_GR(n=0) = 7*(0.373672 - 0.088962i) = 2.615704 - 0.622734i        [I12, I13]
Om_GR(n=1) = 7*(0.346711 - 0.273915i) = 2.426977 - 1.917405i        [I12, I13]
|Om_GR(n=0) - Om_GR(n=1)| = 1.3083542634814167
|Omega_0 - Omega_art|     = 2.127881506829584                        [I15, I17]
|Omega_0|                 = 2.1096454365285577
```

**FROZEN CHOICE:** `R_iso = 0.5` (absolute, in `Ω` units; ENGINEERING CHOICE, tagged).

| receipt | value | reading |
|---|---|---|
| `1.3083542634814167 / R_iso` | `2.6167085269628334` | a genuine overtone at GR-like `ℓ=2` spacing sits **2.62×** outside the annulus and does **not** trip the gate |
| `2.127881506829584 / R_iso` | `4.255763013659168` | the nearest other prior-lane located object sits **4.26×** outside |
| `R_iso / \|Ω_0\|` | `0.23700665113790634` | a **23.7 %** relative exclusion zone |
| `R_iso / (1e-6·\|Ω_0\|)` | `237006.65113790636` | **2.37e5 ×** the dedupe radius — not a restatement of dedupe |

Frozen: `the isolation radius is R_iso = 0.5 absolute in Omega units, chosen as an ENGINEERING CHOICE bounded ABOVE by the GR ell=2 fundamental-to-first-overtone spacing of 1.3083542634814167 in the same units and by the 2.127881506829584 distance to the nearest other root in the v2.1 shipped data, and bounded BELOW by the 1e-6 relative dedupe radius; it is frozen once, is not adjusted after any measurement, and if it fires the lane reports ROOT-NOT-CERTIFIED`.

Frozen: `G5 counts the eigenvalues of the double-precision linearized quadratic pencil of the SAME operator at the SAME order, deduped at the frozen 1e-6 relative radius, that lie within R_iso of the polished root at that order; the count must be EXACTLY ONE at every order of the FULL frozen ladder n in {32, 48, 64, 80, 96}, INCLUDING n = 32`.

### §4.4 ★ THE CONVERGENCE LAW AND EVERYTHING DERIVED FROM IT

> **DISCLOSURE.** Every number in this subsection is arithmetic on the in-repo blob `research/drivers/coldq_pole_v2p2_root_results.json` @ `982c4c9b` (I21) and on the verified v2.1 receipt (I20). **No v2.4 instrument was built, run or consulted, and no eigenvalue of the v2.4 operator existed when this document was frozen.** The arithmetic is reproduced by the driver and reported in the result doc, where it is machine-checked (§4.5).

#### (a) The law, and why a constant-ratio test is the wrong instrument

A Chebyshev spectral discretization of a problem carrying an endpoint singularity converges **root-exponentially**:

```
E(n)  =  C * exp( -c * sqrt(n) )
```

Under this law the successive-error ratio between adjacent rungs is `exp(c·(sqrt(n_{k+1}) − sqrt(n_k)))`, which **declines** as `n` rises because `sqrt` grows more slowly. **A test that demands a constant ratio floor is testing the wrong law, and a test that reads the declining ratios as evidence of a defect is misreading its own instrument.** Frozen: `the convergence law of this instrument is ROOT-EXPONENTIAL, E(n) = C*exp(-c*sqrt(n)); the successive-error ratio therefore DECLINES with n by construction, and a declining ratio sequence is the law's signature rather than evidence of any defect`.

#### (b) The fit, on the certification rungs only

From I21, with the `n = 96` reference, fitting `ln e(n) = ln C − c·sqrt(n)` by ordinary least squares over `n ∈ {48, 64, 80}`:

```
fitted c    = 6.216374
fitted lnC  = 12.962558               (C = 4.261549e+05)
residuals   = -0.039741, +0.084849, -0.045108          max|residual| = 0.084849
```

The three pairwise estimates, which a constant-`c` law requires to be near-constant, are:

```
c(32->48) = 5.775382      c(48->64) = 6.100131      c(64->80) = 6.354001
```

#### (c) The two frozen bands, with their headroom stated

**The `c` band.** Evidence: this lane's own fit `6.216374`; the pairwise span `5.775382 … 6.354001`; and the orchestrator-relayed band `5.4 … 6.6` (I22, corroboration only). Their **union** is `[5.4, 6.6]`. The band is frozen as that union **widened by `±1.0` in `c`**:

```
FROZEN c band  =  [4.4, 7.6]
```

**What `±1.0` in `c` means physically, so the headroom is not a bare number:** at the tightest rung pair `48 → 64`, `sqrt(64) − sqrt(48) = 1.0717968`, so a `±1.0` shift in `c` is a factor `exp(1.0717968) = 2.9206` in the successive-error ratio. **The band tolerates the instrument converging about three times faster or three times slower per rung-pair than every piece of evidence says it does.**

**The fit-residual floor.** The worst residual measured on the prior-lane blob is `0.084849`. Frozen:

```
FROZEN residual floor  =  0.40      (max |residual| in ln e)
```

which is `4.7143×` above the worst measured residual — i.e. the gate tolerates a rung sitting a factor `exp(0.40) = 1.4918` off the fitted law before it fires.

Frozen: `G2b fits ln e(n) = lnC - c*sqrt(n) by ordinary least squares over the G2 certification rungs n in {48, 64, 80} with e(n) the relative separation of Omega_star(n, 0.0, 7.0, 50) from Omega_star(96, 0.0, 7.0, 50), and requires BOTH that the maximum absolute residual in ln e is <= 0.40 AND that the fitted c lies in the frozen band [4.4, 7.6]; the band is the union of this lane's own fit range and the relayed range, widened by plus/minus 1.0 in c, and the residual floor sits 4.7143 times above the worst residual measured on the in-repo blob at 982c4c9b`.

#### (d) ★ G2's TOLERANCE, DERIVED FROM THE MODEL AT `n = 48`

**This is the derivation v2.3 lacked.** Anchor the law at the **finest certification rung** `n = 80` — the most converged, hence the least model-dependent anchor — and extrapolate **back** to `n = 48` at the **worst case the frozen band permits**. Larger `c` back-extrapolates to a larger `e(48)`, so the worst case is the band's **upper** edge:

```
sqrt(80) - sqrt(48) = 2.0160687
e_pred(48) = e(80) * exp(c * 2.0160687)
     c = 4.400000  ->  2.066766e-15        (band lower edge)
     c = 6.216374  ->  8.047286e-14        (the fit; measured e(48) = 8.090599741070316e-14)
     c = 7.600000  ->  1.309506e-12        (band upper edge -- THE WORST CASE)
```

The max pairwise separation over the certification ladder is bounded by `e(48)·(1 + exp(−c·(sqrt(64) − sqrt(48))))`, giving a worst case of `1.309885e-12`. Therefore:

```
G2 tolerance = 1e-10        =  76.3426 x  the model's worst-case prediction
```

**The tolerance value is UNCHANGED from v1/v2.1/v2.2 — it is not retuned — but it is now DERIVED rather than inherited:** it sits `76.3×` above the largest max-pairwise separation the frozen convergence band permits at the ladder's lowest rung. Frozen: `G2's tolerance is 1e-10, UNCHANGED in value from every predecessor lane and DERIVED here rather than inherited: anchoring the root-exponential law at the finest certification rung n = 80 and extrapolating back to n = 48 at the frozen band's upper edge c = 7.6 gives a worst-case max pairwise separation of 1.309885e-12 over the certification ladder, and 1e-10 sits 76.3426 times above it`.

#### (e) ★ WHERE THE LADDER'S LOWEST RUNG COMES FROM — an OUT-OF-SAMPLE prediction, not a preference

The fit of §4.4(b) **never saw `n = 32`**. Extrapolated out of sample:

```
predicted e(32) = exp(12.962558 - 6.216374*sqrt(32)) = 2.277976e-10
measured  e(32) =                                       1.249682e-10          [I21]
pred / meas = 1.8228                     BOTH exceed the frozen 1e-10
```

**The law says `n = 32` cannot pass a `1e-10` gate, and it says so from rungs that exclude `n = 32`.** The measurement agrees, at `1.82×` of the prediction — ordinary agreement for a one-rung extrapolation of an exponential law. **The ladder's lower rung is therefore placed by a law that was fitted elsewhere and tested here, not by the outcome it produces.**

Corroborated independently from the coefficient side by I20 (`5.3e-16` by `n = 40`, `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md:489` @ `7d8fe484`), and by the relayed I22 boundary between `n = 32` and `n = 36` — **neither of which any gate depends on.**

Frozen: `the G2 certification ladder is n in {48, 64, 80, 96}; its lowest rung is placed by the out-of-sample prediction of the root-exponential law fitted on rungs {48, 64, 80}, which predicts e(32) = 2.277976e-10 against a measured 1.249682e-10 with both above the frozen 1e-10 tolerance, corroborated by the v2.1 coefficient-tail receipt at n = 40 and by the orchestrator-relayed n = 32 / n = 36 boundary`.

#### (f) The `n = 32` rung is RETAINED, in three roles

Frozen: `the n = 32 rung is RETAINED in three roles: (i) as a GATED rung of G4(b), G5, FT-5(a) and FT-5(b), which sweep the FULL frozen ladder n in {32, 48, 64, 80, 96} unchanged; (ii) as a REPORTED, NON-GATED DIAGNOSTIC row of G2 shipping the n = 32 root as mp strings, its relative separation from every certification rung, the max pairwise separation over the full five-rung ladder, AND the fitted law's own out-of-sample prediction for e(32) beside the measured value; (iii) as a pre-registered expectation whose failure to appear would itself be reported; NO measurement is hidden and the diagnostic row is mandatory in the result doc's gate table`.

**Why this is not "leaving the bad rung out".** `n = 32` remains **gated** by four other measurements. It is removed from the one gate whose semantics require an asymptotically-resolved representation, on the strength of a law fitted without it and tested against it. **A reader who disagrees can read the diagnostic row and apply v2.2's criterion themselves; the number and the prediction are both there.**

#### (g) The artifact diagnostic — PRE-REGISTERED, explicitly NOT a gate

The same fit routine is additionally pointed at the v2.1-banked discretization artifact `Ω_art` (I17) over the certification ladder and its `c`, residual and per-rung errors are shipped. Frozen: `the artifact-centred convergence fit is a PRE-REGISTERED, NON-GATING DIAGNOSTIC; it is shipped and reported, it enters no gate and no bin, and no certification outcome depends on it`.

### §4.5 ★ THE GATING NUMBER CHECK — the #854 routed fixes, plus a NARROWED scope claim, all disclosed pre-measurement

The PR #854 docket fragment routed two checker defects to its successor rather than changing gating logic after a result — verbatim, from `_orchestration/docket-entries/2026-08-03-coldq-pole-v2.md:22` @ `53bdd90f`:

> **"ROUTED TO THE v2.2 CHECKER AS A NAMED SUCCESSOR ITEM, NOT CHANGED HERE:** a **minimum significant-digit floor (≈`3`) below which a token must be allow-listed rather than matched**, and **per-site rather than global dedup**."

**This lane implements them, plus a third fix, BEFORE its own result exists** — the only time gating logic may honestly be changed. Frozen: `this lane's gating number check implements (i) a MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, machine-enforced, below which a numeral token may NOT be registered against the shipped JSON and MUST be allow-listed with a stated reason; (ii) PER-SITE rather than global dedup, so every occurrence of a numeral is checked and the reported counts describe SITES rather than distinct tokens; and (iii) LIST-VALUED REGISTRATION, so that a bracketed count vector such as the G5 isolation counts or the FT-5 artifact counts is registered against the shipped JSON list as a whole rather than decomposed into single-digit tokens that the significant-digits floor would force onto the allow-list`.

**★ SCOPE, NARROWED DELIBERATELY AND STATED AS A CHOICE.** The checker scans the **result doc only**. Frozen: `the gating number check scans the RESULT DOC only; the arithmetic of sections 4.3 and 4.4 of this prereg is reproduced by the driver and reported in the result doc, where it IS machine-checked, and no claim is made anywhere in this lane that the prereg itself is machine-checked`. **The alternative — extending the checker to scan this prereg — was considered and rejected: it would put gating logic in front of a document containing quoted superseded text and dated quotations of other lanes' numerals, where a false FAIL is more likely than a caught defect.** The choice and its reason are recorded here rather than left implicit.

---
## §5 — THE ROOT-LOCAL CERTIFICATION GATES (G0–G10, plus G2b), with FROZEN numeric tolerances

**Every gate is ROOT-LOCAL: a measurement on the root, on its eigenfunction, or on the discrete spectrum in a frozen neighbourhood of it. No gate integrates, counts or winds over a region.**

**Definitions, frozen.**
`Omega_star(n, lam, x_sat, dps)` = the mp-polished root at that setting, seeded from the double-precision linearized-pencil eigenvalue nearest the frozen seed `Ω_0`.
**The CERTIFIED ROOT** = `Omega_star(48, 0.0, 7.0, 50)`.
**The CERTIFIED EIGENFUNCTION** = `4` rounds of mp inverse iteration on the row-equilibrated `M(Omega_star(48, 0.0, 7.0, 50))` at `dps = 50`, from the all-ones vector, infinity-normalized each round.
**The FULL frozen ladder** = `n ∈ {32, 48, 64, 80, 96}`. **The G2 CERTIFICATION ladder** = `n ∈ {48, 64, 80, 96}`.
**`e(n)`** = the relative separation of `Omega_star(n, 0.0, 7.0, 50)` from `Omega_star(96, 0.0, 7.0, 50)`, computed **in mp** and cast to float only at report time.

| Gate | What it certifies | FROZEN criterion |
|---|---|---|
| **G0** | operator-transcription identity | `the eta-form operator agrees with 4*eta^2 times the A-form operator to <= 1e-13 relative on the frozen set of arbitrary analytic test functions, over lambda in {-0.25, 0, +0.25}, ell in {2, 3} and Omega in {0.9-0.3i, 2.5-1.1i, 14.0-6.0i}` |
| **G1** | residual of the certified eigenfunction at the certified root | `the infinity-norm residual max_i \|(M(Omega_star) psi)_i\| / max_i \|psi_i\| of the CERTIFIED EIGENFUNCTION on the row-equilibrated mp operator at dps = 50 is <= 1e-20` |
| **G2 ★** | **`n`-INDEPENDENCE across the CERTIFICATION ladder**, at a MODEL-DERIVED tolerance | `the maximum pairwise relative separation of Omega_star(n, 0.0, 7.0, 50) over the G2 certification ladder n in {48, 64, 80, 96} is <= 1e-10` |
| **G2b ★** | **the CONVERGENCE LAW itself** — root-exponential, with both parameters gated | `G2b fits ln e(n) = lnC - c*sqrt(n) by ordinary least squares over the G2 certification rungs n in {48, 64, 80} with e(n) the relative separation of Omega_star(n, 0.0, 7.0, 50) from Omega_star(96, 0.0, 7.0, 50), and requires BOTH that the maximum absolute residual in ln e is <= 0.40 AND that the fitted c lies in the frozen band [4.4, 7.6]` |
| **G3** | hyperboloidal-gauge independence | `the maximum pairwise relative separation of Omega_star(48, lam, 7.0, 50) over lam in {-0.25, 0.0, +0.25} is <= 1e-12` |
| **G4** | precision and arithmetic-path independence | `(a) \|Omega_star(48, 0, 7, 80) - Omega_star(48, 0, 7, 50)\| / \|Omega_star(48, 0, 7, 50)\| <= 1e-25, AND (b) at every order of the FULL frozen ladder n in {32, 48, 64, 80, 96} the double-precision linearized-pencil eigenvalue nearest the frozen seed agrees with the mp-polished root at that order to <= 1e-6 relative` |
| **G5 ★** | **ISOLATION** from the discretization's pseudo-spectrum | `G5 counts the eigenvalues of the double-precision linearized quadratic pencil of the SAME operator at the SAME order, deduped at the frozen 1e-6 relative radius, that lie within R_iso of the polished root at that order; the count must be EXACTLY ONE at every order of the FULL frozen ladder n in {32, 48, 64, 80, 96}, INCLUDING n = 32` |
| **G6** | two-instrument agreement vs v1's different-in-kind instrument | `the certified root agrees with the v1 root reconstructed programmatically from research/drivers/coldq_pole_derivation_results.json row x_sat = 7.0 as x_sat*(omega_R_M - i*omega_I_M) to <= 1e-5 relative` |
| **G7** | spin-2-vs-spin-1 discrimination AT THE ROOT | `(a) replacing the spin-2 traction-free wall row by the spin-1 wall condition W'(r_sat) = 0 MOVES the root by >= 1e-3 relative, AND (b) replacing the spin-2 (ell-1)(ell+2) angular weighting by the spin-1 ell(ell+1) weighting in the mode-energy functional evaluated on the CERTIFIED EIGENFUNCTION changes the window-integrated strain-to-kinetic energy ratio by >= 1e-3 relative` |
| **G8** | `nu_vac` cancellation AT THE ROOT, mp end-to-end | `across x_sat in {5, 7, 11} the mp-computed relative spreads of Q = Re(Omega)/(2*abs(Im(Omega))) and of abs(Omega) are each <= 1e-9, and omega_R*M_g = Re(Omega)/x_sat scales as 1/x_sat to <= 1e-9 relative; no value on the path from the polished root to these spreads is cast to a double-precision complex` |
| **G9** | determinism | `two independent full driver runs produce an identical results digest (SHA-256 over the results object minus timing fields)` |
| **G10** | Ax-3 reality / passivity on the certified eigenfunction's own operator | `(a) the row-equilibrated mp operator at n = 48 and every lam in {-0.25, 0.0, +0.25} has max\|Im M0\|/max\|M0\|, max\|Im M2\|/max\|M2\| and max\|Re M1\|/max\|M1\| each <= 1e-40, AND (b) the conjugate-mirror root polished from the seed -conj(Omega_star) satisfies \|Omega_mirror + conj(Omega_star)\| / \|Omega_star\| <= 1e-20` |

### The mandatory NON-GATED diagnostic row

Frozen: `the n = 32 rung is reported as a NON-GATED DIAGNOSTIC row of G2, shipping its polished root as mp strings, its relative separation from every rung of the certification ladder, the maximum pairwise relative separation over the FULL five-rung ladder, and the G2b-fitted law's own OUT-OF-SAMPLE prediction for e(32) printed beside the measured e(32); the result doc MUST print this row in its gate table, and the certification outcome does NOT depend on it`.

### Why G10(b) is the Ax-3 statement and not decoration

With a **real, lossless** constitutive law the `η`-form matrices satisfy `M0, M2` real and `M1` purely imaginary, so `conj(M(−conj(Ω))) = M(Ω)` **identically** and the spectrum is symmetric under `Ω → −conj(Ω)`. That symmetry is the frequency-domain form of *"the medium stores and does not dissipate; all the loss is the radiative port"*. **Smuggling any `Im(μ) ≠ 0` puts an imaginary part into `M2` and breaks it.** G10(a) checks the matrix structure; G10(b) the consequence on the certified root. FT-10 breaks both with one mutation.

### Certification classes (exhaustive, frozen)

- **`ROOT-CERTIFIED`** — `all of G0, G1, G2, G2b, G3, G4, G5, G6, G7, G8, G9 and G10 PASS and all of FT-0, FT-1, FT-2, FT-2b, FT-3, FT-4, FT-5, FT-6, FT-7, FT-8, FT-9 and FT-10 FIRE`.
- **`ROOT-NOT-CERTIFIED`** — `any gate FAILS, OR any self-test fails to fire`. **A gate that cannot fail voids the certification exactly as hard as a gate that fails.** No physics bin is adjudicated (§7 precedence).

Frozen: `this lane has exactly two certification classes, ROOT-CERTIFIED and ROOT-NOT-CERTIFIED; there is no scoped, partial or provisional certification, and a gate that passes only over a reduced parameter set is a FAIL`.

**Rule-11 fence, frozen and binding.** Frozen: `no gate, tolerance, band, frozen numeric parameter or method element in sections 4 and 5 may be changed after any gate result is seen; if this instrument fails certification the lane reports ROOT-NOT-CERTIFIED and routes to its own successor with a new version number`.

**★ THE FENCE'S SHARPEST EDGE, written for this lane specifically.** This lane exists because a predecessor's gate spec was wrong twice — once in its ladder and once in its convergence law. Frozen: `if G2 fails on the certification ladder, or if G2b's residual or fitted c falls outside its frozen bands, the ladder is NOT changed again, no rung is added or removed, the bands are NOT widened, and the lane reports ROOT-NOT-CERTIFIED; a third gate-spec repair in the same arc would be parameter selection under a frozen fence and is forbidden here in advance`.

---

## §6 — GATE-FIREABILITY SELF-TESTS (FT-0 … FT-10, plus FT-2b) — each MUST FIRE

**The rule (frozen).** Frozen: `a gate that cannot fail is not a gate; if any self-test fails to fire, the certification is ROOT-NOT-CERTIFIED regardless of how many gates passed`.

**The ordering rule (frozen).** Frozen: `every self-test is executed and recorded BEFORE its target gate's own measurement is read in the results object, and each self-test's mutation is shown here to be NON-VACUOUS against the object it mutates by an algebraic argument stated at freeze time, not by running`.

| # | Targets | Deliberate mis-specification | FROZEN firing criterion | Why the mutation is NON-VACUOUS (algebra, at freeze) |
|---|---|---|---|---|
| **FT-0** | **G0** | corrupt the `𝒞₀` coefficient by `1e-12` relative | `the corrupted eta-form coefficient MUST break the operator identity by >= 1e-13 relative` | `𝒞₀ = −4ℓ(ℓ+1)η² − 8A²/(2−η²)` is `O(1)` on the interior nodes and appears with unit weight in `𝓛_η`, so a `1e-12` relative corruption is a `~1e-12` relative change in the identity's residual — one order above the gate |
| **FT-1** | **G1** | evaluate the residual of the CERTIFIED EIGENFUNCTION on `M(Omega_star·(1 + 1e-10))` | `the off-root residual MUST be >= 1e-15` | the residual is `≈ σ_min(M(Ω))` and `dσ_min/dΩ` is `O(1)` for a simple root, so a `2.1e-10` absolute displacement gives an `O(1e-10)` residual — five orders above the threshold |
| **FT-2** | **G2** | add `n = 8`, far below every rung of either ladder | `the under-resolved order MUST deviate from Omega_star(48, 0, 7, 50) by >= 1e-6 relative` | at `n = 8` the basis cannot represent the coefficient functions (I20: the tail only reaches `5.3e-16` by `n = 40`); v2.1's FT-C and v2.2's FT-2 each measured `4.4038e-04` for exactly this mutation |
| **FT-2b ★** | **G2b** | **STAGNATION:** add a constant `1e-12` to `Omega_star(n)` at every NON-reference rung of the certification ladder (the `n = 96` reference untouched), then refit | `the stagnation mutation MUST drive the fitted c BELOW the frozen band's lower edge of 4.4` | from I21 the true absolute rung displacements are `1.706830e-13`, `2.470183e-16`, `6.123558e-19` (`e(n)·\|Ω\|`), **every one below the injected `1e-12`**, the tightest margin being `5.858×` at `n = 48`. So every mutated `e(n)` collapses to `≈ 1e-12/\|Ω\|`; the `48→64` ratio is bounded in `[0.8291, 1.1710]` for **any** phase alignment, giving an implied `c ∈ [−0.1748, +0.1473]` — **at least `4.25` below the band's lower edge.** The fit cannot land in band. It is a POST-SOLVE perturbation of recorded values, the same class as FT-9, and that class is disclosed rather than implied |
| **FT-3** | **G3** | a **correctly-specified half-applied gauge**: carry `λ` into `ℬ₁` and `𝒞₁` but OMIT the `λ` terms from `𝒞₂` | `the gauge-omission mutation MUST make the G3 pairwise spread exceed 1e-6` | the omitted terms are `8η²λ − 4η²λ²A²`, which at `λ = +0.25` equal `2η² − 0.0625·4η²A²`, an `O(1)` quantity at `η → 1` — not a no-op, and not the logical negation of G3 |
| **FT-4** | **G4** | (a) run the mp operator at `dps = 20`; (b) build the double pencil at `n = 8` while the mp root is at `n = 48` | `(a) the dps = 20 root MUST differ from the dps = 50 root by >= 1e-25 relative, AND (b) the mismatched-order cross-check MUST exceed 1e-6 relative` | (a) `dps = 20` truncates every entry at `~1e-20` relative and the equilibrated operator's conditioning at `n = 48` is `O(n⁴) ≈ 5e6`, so the root moves by `~1e-14`; (b) `n = 8` is FT-2's under-resolution |
| **FT-5 ★** | **G5** | the identical isolation measurement centred on **(a)** the v2.1-banked artifact `Ω_art` (I17) and **(b)** the v2.1 C9 probe `Ω_edge = 0.1400 − 3.5035i` (I18), over the FULL ladder | `case (a) MUST return a count different from exactly one at at least one order of the FULL frozen ladder, OR a polished n-drift above the G2 tolerance at those orders; AND case (b) MUST return a count different from exactly one at at least one order of the FULL frozen ladder` | (a) `Ω_art` is banked by v2.1's OWN frozen physical-vs-artifact criterion as absent at some `n` in `{48, 56, 64}`, so it cannot be both isolated and `n`-stable across a ladder containing three of those orders; **the OR is deliberate and which branch fails is reported, not chosen.** (b) `Ω_edge` sits where the #854 review measured a migrating spectrum whose in-box count runs `2 → 9` over `n = 32 → 80` |
| **FT-6** | **G6** | corrupt `𝒞₀` by `1e-3` relative and compare THAT root against the v1 comparator | `the corrupted-operator root MUST disagree with the v1 comparator by >= 1e-5 relative` | a `1e-3` relative change in an `O(1)` coefficient moves the eigenvalue by `O(1e-3)` relative — two orders above G6's tolerance |
| **FT-7 ★** | **G7** | **REVERSE fireability, by a DIFFERENTLY-CODED EQUIVALENT SPECIFICATION (not the identical code path):** (a) impose the spin-2 wall row using the **closed-form CGL corner entry** for the endpoint derivative instead of the negative-sum diagonal; (b) evaluate the spin-2 energy ratio with the angular weight written as `ell**2 + ell - 2` and the strain terms summed in **reversed association order** | `both differences between the differently-coded equivalent specification and the primary one MUST be below 1e-3; and if either returns EXACTLY 0.0 the result doc MUST record that the two code paths collapsed and that the intended arithmetic separation did not materialise` | **This is the repair of the inherited defect.** The negative-sum diagonal and the closed-form corner entry are **analytically identical** and differ only by floating-point round-off, so the mutation is a genuine second implementation of the same mathematical condition rather than a re-run of the first: it exercises a distinct rounding path while the null space of the row is unchanged. Same for the reversed-association energy sum. **Expected magnitude `~1e-16 … 1e-13`, i.e. arithmetic noise — NOT the exact `0.0` an identical code path returns by construction, which is why the exact-zero outcome is made reportable rather than silently passing** |
| **FT-8** | **G8** | inject the `x_sat`-dependent profile perturbation `A -> A*(1 + 1e-6*(x_sat - 7)/7)` | `the x_sat-dependent perturbation MUST make the G8 spread exceed 1e-9` | **arithmetic CORRECTED from the inherited value.** The perturbation is identically zero at `x_sat = 7` and equals `1e-6*(x_sat-7)/7`, i.e. **`-2.857143e-07` at `x_sat = 5` and `+5.714286e-07` at `x_sat = 11`** — *not* the `±1.43e-06` v2.2 and v2.3 both carried. It breaks the scale invariance the gate measures without touching the primary run; v2.1's FT-E and v2.2's FT-8 each measured `6.0137e-07` for exactly this mutation, which is `602×` above the `1e-9` threshold |
| **FT-9** | **G9** | perturb one recorded gate value by `1e-15` relative in a COPY of the results object and re-digest | `the perturbed copy MUST produce a different digest` | SHA-256 over the serialized object; the demonstration is that the digest covers the gate payload rather than a header |
| **FT-10** | **G10** | smuggle loss `Im(mu)/Re(mu) = 1e-3` into the modulus | `(a) the lossy operator MUST return max\|Im M2\|/max\|M2\| >= 1e-6, AND (b) the lossy conjugate-mirror residual MUST be >= 1e-5` | a constant complex factor on `μ` leaves `ĝ = μ′/μ` and the wall condition unchanged and changes ONLY `𝒞₂`'s first term, giving `Im 𝒞₂/Re 𝒞₂ ≈ −1e-3`; the conjugate-mirror proof of §5 requires `M2` real, so it breaks at the same order |

---
## §7 — THE FROZEN PHYSICS BINS — adjudicated IFF ALL GATES PASS

**Every boundary in this section is byte-identical to v2.3's (`3e2c0c1c` §7) and to v2.2's (`f15a6e4d` §7), which was byte-identical to v2.1's (`7d8fe484` §7), which inherited them from v2 (`00724432`) and v1. Not one is re-derived, adjusted, widened or narrowed here — across five successive freezes.**

**Rule-11 fence, stated up front and binding.** Frozen: `no adjudication criterion below may be dropped, widened or re-defined after any result is seen; no input in the section 3 ledger may be retuned; whatever the instrument returns is banked`. There is **no free parameter to tune** — that is the point of the lane.

**PRECEDENCE (frozen, evaluated in this order).** `BIN-F-NOROOT` > `BIN-F-ROOT` > `BIN-F-PROFILE` > `BIN-1/2/3`. If an earlier bin fires, the later ones are reported as `N/A — not adjudicated` and **no verdict language is used about them.** `BIN-4` is `N/A BY CONSTRUCTION` **at every precedence level, including a full pass** (§7.5).

### §7.1 Honest-failure bins (each reachable, each with a disposition)

| bin | condition | disposition |
|---|---|---|
| **`BIN-F-NOROOT`** | `the double-precision linearized pencil at n = 48 has no eigenvalue within R_iso of the frozen seed, or the mp polish from that seed fails to converge` | **A clean negative and a GOOD outcome.** It would say the object v1, v2.1 and v2.2 all located is not present in this carry-over of the same formulation — which would be a decisive statement about the carry-over. Banked as such; no bin adjudicated; routed to Grant and the auditor lane. |
| **`BIN-F-ROOT`** | `any gate FAILS or any self-test fails to fire` | **`ROOT-NOT-CERTIFIED`.** No physics bin adjudicated; the failing gate's numbers are reported; the lane returns the instrument failure as its result. No claim, no walk-back, no solidity change, **and no retune** — it routes to its own successor with a new version number. |
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

> **⚑ FLAG-1 CARRIED FORWARD UNCHANGED, and the discriminator's robustness to BOTH corpus values is frozen HERE rather than argued afterwards.** Two `Q_GR` values exist in the corpus: the programmatic `2.1002135791366907` from `KERR_QNM[0.00] = (0.37367, 0.08896)`, and the rounded-prose `2.099438202247191` from the pair `0.3737`/`0.0890`, carried verbatim at `research/2026-07-30_qlaw-derivation_scoping.md:401`. **Both are the same table at different precision.** The frozen source does not move — the programmatic value is used, exactly as v1, v2.1 and v2.2 used it — and the robustness is stated as a *criterion*, not as a *reassurance*:
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

**The ill-posed sub-bin is PRESERVED, deliberately.** Frozen: `BIN-3-MONOTONE and BIN-3-DISCORDANT are preserved unchanged from v1, v2.1, v2.2 and v2.3 so that an ill-posed or discordant localization reading lands in a pre-registered bin rather than in prose`.

### §7.5 BIN-4 — `N/A BY CONSTRUCTION`, declared in advance

Frozen: `BIN-4 is N/A BY CONSTRUCTION in this lane and is not adjudicated at any precedence level including a full gate pass; no overtone, no ladder, no mode count and no completeness statement is computed, and the deferral is an open instrument-scope question awaiting a substrate-derived low-frequency cutoff, not a failure of this lane`.

**This is a scoped non-claim, and the result doc is required to present it as one.** It is not `BIN-4-NONE` — that sub-bin asserted *"exactly one physical pole is located in the frozen rectangle"*, which is a **counting claim over a region** and is exactly what the PR #854 review impeached and what §1.2 forbids. **`BIN-4-NONE`, `BIN-4-LADDER-MATCH` and `BIN-4-LADDER-DIFFERENT` are all unreachable in this lane by construction, and that is disclosed here rather than discovered later.**

### §7.6 Reachability audit (frozen)

- `BIN-F-ROOT` is reachable **and is demonstrated reachable every run**: every self-test drives an actual gate into its failing state (FT-7 by the reverse construction, stated as such).
- `BIN-F-NOROOT` is reachable: the pencil at `n = 48` either has an eigenvalue within `R_iso` of the seed or it does not.
- `BIN-F-PROFILE` is reachable: the canonical set carries live tensions this lane touches (#814 CF-7's unnamed `ρ` at `vol3/claim-quality.md:122`).
- `BIN-1/2/3` sub-bins are each reachable because each is an interval or a strict comparison on a continuously-valued measured quantity, and the intervals **partition** their axis with no gaps and no overlaps.
- `BIN-4`'s sub-bins are **deliberately unreachable**, disclosed in §7.5.
- **No outcome requires a criterion to be relaxed after the fact.**

### §7.7 ★ PREDICTABILITY DISCLOSURE — stated in advance so no bin outcome can later be presented as a blind prediction

**This lane knows, in advance and to several digits, where every bin will land if the gates pass — and says so here rather than after.**

v2.2 shipped these `NOT-ADJUDICATED` diagnostics at the same root, under a `ROOT-NOT-CERTIFIED` instrument (its result doc §5.1–§5.2, @ `982c4c9b`): `Ω = 1.8536552108408788 − 1.0072567831433188i`, `ω_R M_g = 0.2648078872629827`, `Q = 0.9201502744197102`, `u_energy = u_kinetic = 2.0000000000000004` with `interior_max = false`. **Anyone can compute where those fall in §7.2–§7.4, and this lane carries the same instrument, so it expects the same numbers.**

Frozen: `this lane's contribution is CERTIFICATION of an already-published prior-lane number under a repaired gate specification, not the discovery of a new one; the bin outcomes are predictable in advance from the v2.2 NOT-ADJUDICATED diagnostics and that predictability is disclosed here, so no bin outcome may be presented as a blind prediction and no headline may imply surprise`.

**And the honest reading of what that leaves.** The value of an adjudicated bin here is **not** that the number is new. It is that the number is produced by an instrument whose root-local behaviour has been gated end-to-end, so the bin verdict is a statement about the graded cavity rather than about an uncertified discretization. **That is a real difference and it is also a modest one, and both halves of that sentence belong in the result doc.**

---

## §8 — WHAT TRANSFERS, AND WHAT MUST BE RE-EARNED

**TRANSFERS (cited, not silently absorbed):**
- the **ratified physics framing** — the transmission-line reading, the graded profile, the SHORT at `r_sat`, the radiative port, the spin-2 channel, `Q` as a pole;
- the **compactified formulation** and its exact wall substitution, **as algebra re-verified by G0 every run**;
- the **shape** of the certification battery — frozen gates with numeric tolerances, self-tests that must FIRE, a determinism digest, an exhaustive outcome-class table with a reachability argument;
- the **frozen-first commit order**;
- the **bin boundaries**, byte-identical (§7);
- the **`x_sat`-generalized advance identity** `k₀ r_sat = x_sat · ω_R M_g`, minted in the v2.1 prereg §2.5 and cited as that lane's;
- **★ and, new in this lane and disclosed as such: the INSTRUMENT ITSELF, carried over from v2.2 by copy-with-attribution (§2.3).**

**DOES NOT TRANSFER — must be re-earned, and is (gate in brackets):**
- **the certification.** #845, #854 and #856 are all uncertified. Every gate is re-run on this file. [G0–G10, G2b]
- **v2.2's G2 result.** It stands as v2.2 banked it, on v2.2's ladder. This lane's G2 is a **different measurement on a different ladder at a model-derived tolerance** and does not overwrite it. [G2]
- **v2.3's gate specifications.** Superseded pre-measurement; **nothing of v2.3 is inherited as passed, because v2.3 measured nothing.** [all]
- **the pole-counting instrument.** Not re-earned; **not used at all** (§1.2).
- **any completeness statement.** Not re-earned; **abandoned as out of scope** (§7.5).
- **implementation independence.** **Explicitly NOT transferred and explicitly NOT claimed** (§2.3).

Frozen: `no gate, tolerance, certification class or measured number is inherited as PASSED from PR #845, PR #854, PR #856 or the superseded v2.3 freeze; the physics framing, the compactified algebra, the bin boundaries and the instrument's method transfer, the certification does not, and every gate in section 5 is re-earned on this file`.

---

## §9 — SATISFIABILITY OF THE FROZEN REQUIREMENTS — DERIVED, WITH ZERO PRE-FREEZE COMPUTATION

> **★ DISCLOSURE.** **This lane ran NOTHING before this document was frozen.** No operator was assembled, no eigenvalue computed, estimated, seeded or looked at. The only arithmetic performed before the freeze is that of §4.3, §4.4 and §7.3 — elementary arithmetic and a three-point least-squares fit on **already-published prior-lane values read from an in-repo blob** — reproduced by the driver and reported in the result doc, where it is machine-checked.
>
> **The risk is disclosed and accepted:** a band derived rather than scouted can be wrong, and if it is, the gate FAILS and this lane reports `ROOT-NOT-CERTIFIED`. **It will not be retuned.**

| gate | tolerance | where it comes from |
|---|---|---|
| **G0** `1e-13` | v2.1's C11 measured `8.9716e-16` and v2.2's G0 measured `1.0385e-15` on the same identity; `1e-13` sits ~2 orders above the worst prior evidence |
| **G1** `1e-20` | the polish terminates at `1e-38·\|Ω\|`, mp carries `50` digits, the equilibrated operator's conditioning at `n = 48` is `O(n⁴) ≈ 5.3e6`, so the achievable residual floor is `~1e-40`; `1e-20` is frozen 20 orders above. v2.2 measured `4.7268e-50` |
| **G2 ★** `1e-10` | **MODEL-DERIVED (§4.4(d)), value unchanged from every predecessor.** Anchoring `E(n) = C·exp(−c·sqrt(n))` at the finest certification rung and extrapolating to `n = 48` at the band's upper edge `c = 7.6` gives a worst-case max pairwise separation of `1.309885e-12`; `1e-10` sits `76.3426×` above it |
| **G2b ★** residual `<= 0.40`; `c ∈ [4.4, 7.6]` | **§4.4(c).** The residual floor is `4.7143×` above the worst residual measured on the in-repo blob (`0.084849`); the `c` band is the union of this lane's fit range and the relayed range, widened by `±1.0`, which is a factor `2.9206` of ratio tolerance at the tightest rung pair |
| **G3** `1e-12` | v2.1's C2 measured `3.3268e-14` and v2.2's G3 `3.3323e-14` on the identical gauge set at the identical primary order; ~1.5 orders of measured margin |
| **G4(a)** `1e-25` | the polish's termination is `1e-38` relative, so `dps = 50` and `dps = 80` cannot differ by more than `~1e-38`; `1e-25` is 13 orders above. v2.2 measured `5.2778e-47` |
| **G4(b)** `1e-6` | v2.1's B1 disclosure measured the double-precision-operator floor at `2.73e-10 … 8.67e-08`; v2.2 measured `1.7559e-08` over the same full ladder including `n = 32`. `1e-6` is about one order above the worst measured floor |
| **G5** `R_iso = 0.5`, count `== 1` | §4.3, four receipts — two upper constraints from physics, two lower from the instrument's own frozen numerics. v2.2 measured `[1, 1, 1, 1, 1]` on the full ladder |
| **G6** `1e-5` | the observed cross-lane agreement is `6.803232e-07`; `1e-5` carries ~1.2 orders of headroom, so a rounding-level difference passes while a transcription error (FT-6 shows `O(1e-3)`) does not |
| **G7** `1e-3` | v2.1's FT-F(ii) and v2.2's G7(a) each measured the spin-1 wall condition moving the fundamental by `0.28424`; `1e-3` is ~2.5 orders below the measured effect |
| **G8** `1e-9` | v1's, v2.1's and v2.2's frozen tolerance, unchanged. v2.2's mp end-to-end measurement is `1.8619e-46`, ~37 orders inside the gate — which is why **FT-8 is mandatory**: without it the gate would be dead |
| **G9** identical digest | determinism has no tolerance |
| **G10(a)** `1e-40` | exact zeros in mp by the structure argued in §5; the tolerance catches a structural transcription error, and **FT-10 supplies the fireability a zero-valued gate would otherwise lack** |
| **G10(b)** `1e-20` | both mirror-pair members are polished to `1e-38` relative independently, so the symmetry residual is bounded by `~1e-38`; `1e-20` is 18 orders above. v2.2 measured `9.2731e-47` |

**★ THE PRE-REGISTERED EXPECTATIONS, written so that a surprise is visible as a surprise.** Because this lane carries v2.2's instrument over, it expects — and states here, before running — that:

1. **the certified root reproduces** `1.8536552108408788 − 1.0072567831433188i`;
2. **G2 measures `≈ 8.09e-14`** over the certification ladder (the `48 ↔ 96` pair dominates), comfortably inside `1e-10`;
3. **G2b's fitted `c` lands near `6.2`** with a max residual near `0.085`, both inside their bands;
4. **the `n = 32` NON-GATED diagnostic reads `≈ 1.2497e-10`**, i.e. reproduces v2.2's failing G2 number, against the law's out-of-sample prediction of `2.277976e-10`;
5. **every unchanged gate reproduces v2.2's published value** at the precision v2.2 published it;
6. **FT-7's differently-coded equivalent returns `~1e-16 … 1e-13`, not exactly `0.0`.**

Frozen: `these six expectations are stated BEFORE the run so that agreement is recorded as a REGRESSION CHECK and any disagreement is recorded as a DEFECT and surfaced with both numbers; no expectation is a gate, none may be used to adjust a measurement, and a disagreement is reported rather than reconciled`.

**Runtime.** v2.2's battery ran `256.15 s` and `254.41 s` inside the frozen `3600 s`. This lane adds a three-point least-squares fit on already-polished roots, one post-solve mutation, one differently-coded wall row and one artifact fit — all negligible against the mp determinant polish. A longer run is **disclosed, not silently accepted**.

**Mutual satisfiability of the gates (no gate contradicts another).**
1. **G2 and G2b probe different things and can disagree.** G2 asks whether the spread is small; G2b asks whether it obeys the law. **A ladder stagnating at a small constant offset passes G2 and fails G2b — which is exactly the configuration FT-2b constructs.**
2. **G2b's two halves probe different things and can disagree.** The residual half asks whether the rungs lie on *a* root-exponential line; the `c` half asks whether that line has the *right slope*. A well-fitted line at the wrong slope passes the first and fails the second.
3. **G2 and G5 can disagree.** G2 asks whether the root moves with `n`; G5 whether anything else moves *toward* it. FT-5(a) is built on that independence.
4. **G3 and G4 probe genuinely different knobs.** `λ` changes the analytic prefactor and every coefficient function; `dps` changes only the arithmetic.
5. **G6 does not presuppose G2.** A carry-over could be `n`-stable at the wrong place; G6 is the gate that would catch it, and FT-6 demonstrates it would.
6. **G7 and G10 are orthogonal.** G7 mutates the tensor rank; G10 the losslessness.
7. **G8 does not presuppose G1.** `x_sat`-invariance is a statement about the arithmetic path; the residual about the solution.
8. **No gate's PASS condition is another gate's FAIL condition.** Checked explicitly for the new pair: **FT-2b's firing condition (fitted `c` below `4.4` under a stagnation mutation) is not G2b's failure condition (fitted `c` outside `[4.4, 7.6]` unmutated) — they are measured on different value sets, one mutated and one not.**

---

## §10 — FLAGS RAISED AT FREEZE TIME (flag-don't-fix; surfaced, not resolved)

1. **⚑ FLAG-1 — the two `Q_GR` comparator values.** Fully stated in §7.3 with the robustness condition frozen as a criterion. The programmatic `2.1002135791366907` is frozen; the rounded-prose `2.099438202247191` at `research/2026-07-30_qlaw-derivation_scoping.md:401` is reported alongside. **Routed to the auditor lane; not repaired here.**
2. **⚑ FLAG-2 — this lane DOES gate on a prior-lane number (G6), and the direction of inference is fixed in advance.** Frozen: `G6 gates THIS lane's transcription against a prior-lane comparator and certifies NOTHING about PR #845, which remains SOLVER-NOT-CERTIFIED; a G6 pass may not be reported as corroboration of #845, and no #845 number enters any bin, any other gate, or any comparator in this lane`.
3. **⚑ FLAG-3 — I7 is assumed, not tested.** The reflectionless Regime-I port at infinity is a frozen canonical input and this lane's entire method divides out the corresponding analytic factor. If the substrate carries any far-field reflector, every number here is wrong in the same direction — **including the certified root.** Not tested; routed. **A `ROOT-CERTIFIED` verdict does not touch this flag.**
4. **⚑ FLAG-4 — #814 CF-7's naming gap stands, untouched.** `vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` and never names which `ρ`. This lane consumes the leading reading (`ρ₀`, I5) and does **not** repair the leaf.
5. **⚑ FLAG-5 — the completeness question is OPEN.** The open item is: **derive a substrate low-frequency cutoff for the graded shear cavity.** Routed to Grant (§0) and to a successor; **not attempted, not sketched, not assumed.**
6. **⚑ FLAG-6 — v2.1's I13 provenance is stale; the correction is recorded, not propagated.** Since PR #845 merged, `ω_I M (ℓ=2, n=1) = 0.273915` has an in-repo carrier at `research/drivers/coldq_pole_derivation.py:106`. **The v2.1 prereg is frozen and byte-untouched.**
7. **⚑ FLAG-9 CARRIED FORWARD, UNRESOLVED — v1's `0.28430` is a CLAMPED-wall mutation, not the spin-1 one.** v1's FT-2 is `W(r_sat) = 0` (the `Γ = +1` alternative of #814 FORK-3(b)), verbatim at `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md:229`; the spin-1 condition is a different row. v2.1's result-doc §5.4 places them in one row labelled *"spin-1 / clamped wall shift"*. **That row compares two different mutations.** Surfaced, not resolved; both other lanes' files byte-untouched.
8. **★ ⚑ FLAG-10 — RESTATED: this lane claims NO implementation independence, and it also does not vouch for v2.2's.** §2.3 states this lane's own position in full: a carried-over instrument cannot corroborate itself. **And this lane does not endorse v2.2's "independent transcription sharing no line of code" framing either** — v2.2 transcribed from v2.1's driver with attribution markers at the transcription sites, which is a **weaker** form of independence than that phrase suggests, and this lane makes no claim about how much weaker. Frozen: `this lane claims no implementation independence for itself and makes NO claim about the degree of independence of any predecessor; the only genuinely different-in-kind instrument in this arc is v1's real-axis asymptotic matching, and it appears here solely as G6's comparator`. **The exterior-complex-rotation cross-check remains the genuinely independent third instrument, and it is not built here (§11).**
9. **★ ⚑ FLAG-11 — the relayed-review provenance gap, and it is the flag this lane most wants a reader to see.** The 12-rung sweep this lane was directed to cite **could not be located in the repository record** at freeze (§S.3: no PR comments, no reviews, no inline review comments, branch tip unchanged). **Rather than cite an unverifiable receipt, this lane derived the convergence law itself from an in-repo blob and demoted the relayed findings to corroboration that no gate depends on.** Frozen: `where an instruction to cite a receipt could not be satisfied by verification, this lane derived the needed quantity from a source it could verify and recorded the gap rather than citing the receipt; the relayed findings are tagged ORCHESTRATOR-RELAYED throughout and no gate depends on them`. **If the receipt lands and contradicts §S.3's fit, the halt clause of §S.5 fires.**
10. **★ ⚑ FLAG-12 — RESTATED HONESTLY: the Makefile contact is a REAL TWO-LINE CONFLICT, not an append-only merge.** v2.3 called it "append-only textual contact"; **that was wrong.** The `.PHONY` list and the `verify:` prerequisite list are **single lines** that this lane, PR #854 and PR #856 all modify — and a single line modified by two branches is a **textual conflict** under a server-side merge, not an auto-resolved append. Frozen: `the Makefile contact with PR #854 and PR #856 is a REAL two-line conflict on the .PHONY line and the verify: prerequisite line, is NOT append-only, and is NOT auto-resolved by any merge driver on the server side; the mitigation is that this lane's number check is wired as its OWN target so no recipe body is shared, and this branch is REBASED ONTO THE CURRENT origin/main IMMEDIATELY BEFORE THE PR IS OPENED so the conflict surface is measured against a fresh tip and disclosed in the PR body`. **Every `research/` and `_orchestration/` file in this lane is new and shared with no open branch.**

---

## §11 — LEDGER TAGS + OWED FOLLOW-ONS (fenced; NOT executed here)

**Ledger tags (`consistency-vs-emergence`, frozen).** `omega_R*M_g` is `[derived]` but **VALUE-CONSISTENCY** class (rides the GR-imported `7`). `Q` and `r_peak/r_sat` are `[derived]` and `ν_vac`-**FREE**, hence **emergence-capable at value level**. The GR numbers are `[GR-IMPORTED comparators]` (I11–I13). `ν_vac = 2/7` is `[canon]`, read-only, value GR-imported. Chebyshev orders, gauge parameters, precisions, the polish tolerance, `R_iso`, the `c` band and the residual floor are `[engineering]`. The v1, v2.1 and v2.2 numbers are `[PRIOR-LANE]`; the relayed sweep is `[ORCHESTRATOR-RELAYED, UNVERIFIED]`. None is a bin input. **`α`-CLEAN. No manifestation-class claim. No claim of any kind is minted.**

**Owed follow-ons (fenced; Rule 12 — the slot is NOT refilled with an assertion):**
1. **★ The substrate low-frequency cutoff** for the graded shear cavity — the prerequisite for any completeness or overtone claim. Grant's input first (§0), then its own prereg. **Not sketched here.**
2. **★ The BIN-3 question of §0** — whether a leaky resonator's outward-growing eigenfunction makes "where does the mode live" ill-posed. Grant's plumber call owed; **the window is not widened in the meantime.**
3. **★ The relayed-review receipt** — if the PR #856 review's 12-rung sweep exists, it should land in the repository record so a successor can cite it rather than relay it. **Routed to the orchestrator, not to physics.**
4. **The spheroidal (even-parity / P–SV-coupled) branch.** Toroidal only here.
5. **FORK-3's naming gap** (FLAG-4). Routed to the auditor lane.
6. **FORK-9's formal half** — whether Op6's phase-matching condition applies to a graded shear cavity with a `Γ = −1` inner wall.
7. **FORK-12** — untouched; no `ℓ`-ladder is computed at all.
8. **FLAG-3's far-field assumption** — a test that the Regime-I port really is reflectionless at the scales that matter.
9. **The exterior-complex-rotation cross-check** as a genuinely independent third instrument. **Not built here, and FLAG-10 makes it more owed than it was, not less.**

---

> **Pre-registration provenance.** Frozen pre-registration for the cold-Q pole **v2.4 ROOT certification**, under Grant's standing 2026-08-03 ruling *certify the located root, not the rectangle*. Written against `origin/main` = `184db4b6`. Committed **ALONE** and pushed before any driver code and before any number produced by this instrument existed. **Supersedes `research/2026-08-03_coldq-pole-v2.3-root_prereg-FROZEN.md` @ `3e2c0c1c` PRE-MEASUREMENT** — that instrument produced zero numbers, its file is **BYTE-UNTOUCHED and carries no retraction header**, and §S.2 is the whole supersession record, exactly as v2's prereg was left when v2.1 superseded it. **THE CHANGES** are §S.4: G2's certification ladder `n ∈ {48, 64, 80, 96}` at a **model-derived** `1e-10`; **G2b** rebuilt on the root-exponential law `E(n) = C·exp(−c·sqrt(n))` with both parameters gated; **FT-2b** rebuilt as a stagnation mutation; **FT-7** rebuilt as a differently-coded equivalent specification; **FT-8**'s non-vacuity arithmetic corrected to `−2.857143e-07` / `+5.714286e-07`; mp strings per rung; the checker's three fixes and its narrowed scope; and FLAG-10 and FLAG-12 restated. **Predecessor lanes, all unmodified and byte-untouched by this lane:** `research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md` and `..._result.md` (PR #845, MERGED at `052ccbba`); `research/2026-08-03_coldq-pole-v2_prereg-FROZEN.md` (`00724432`); `research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md` (`7d8fe484`) and its result doc (PR #854); `research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md` (`f15a6e4d`) and `research/2026-08-03_coldq-pole-v2.2-root_result.md` (`982c4c9b`) and their driver (PR #856); `research/2026-08-03_coldq-pole-v2.3-root_prereg-FROZEN.md` (`3e2c0c1c`). Companion inputs cited by path: `research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51`; `research/2026-07-20_ringdown-systematics_checks.py:69`, `:72`, `:133`; `research/2026-07-30_qlaw-derivation_scoping.md:401`; `research/drivers/coldq_pole_derivation_results.json:505`, `:509`, `:510`, `:512`; `research/drivers/coldq_pole_derivation.py:106`; `src/ave/core/constants.py:397`; `_orchestration/docket-entries/2026-08-03-coldq-pole-v2.md:20`, `:22` @ `53bdd90f`. Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched regardless of outcome. Companion: the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-v2p4-root.md`.
