> **⚠ LANE ANALYSIS — pre-ruling, headline WITHDRAWN.** The A1 circuit lane's
> original headline ("both scaffold options are mirrors") is withdrawn: the
> swept parameter was a *transmission* coefficient, not a source reflection,
> so its circuit labels named a circuit the code never built. What survives is
> recorded in R58 §2 — the ϖ-projection receipt **cannot fire** (M is real;
> measured 1.6e-12), the solver's "KUBC / voltage-clamped" docstring label is
> wrong (it is a **matched generator**), the multiplicative-vs-additive
> common-mode homonym, and the decision-4 machinery blocker. Nothing here is
> canon.

# LANE A1 — REPAIRED. The scaffold's circuit, re-derived after the verify lane

**Date:** 2026-08-25 · **Supersedes** `ANALYSIS.md` (same directory) on every point below.
**Read-only against** `/Users/grantlindblom/AVE-staging/AVE-Core`. Nothing written into the corpus.
**All numbers in this document were recomputed in this session**, not carried over.
Receipts: `../a1repair/structure.py`, `../a1repair/sweep_corrected.py`,
`../a1repair/commonmode_and_norton.py`, `../a1repair/replicate_R1_R2.py`
(run with `PYTHONPATH=/Users/grantlindblom/AVE-staging/AVE-Core/src`).

---

## §0 — Status line

> **HEADLINE DEMOTED.** The sentence *"both scaffold options are mirrors — ρ=−1 manufactures 10
> poles, ρ=+1 manufactures 24, matched manufactures 0"* is **not established** and is withdrawn.
> The swept parameter was a **transmission** coefficient across the cut, not a source **reflection**
> coefficient, so every circuit noun hung on it (SHORT / OPEN / ideal-V-source / ideal-current-
> source / "two mirrors" / "cavity mode") named a circuit the code never built. The pole counts
> 10 and 24 are also wrong as counts: they were 400-point grid spike counts, and the exact counts
> under the corrected operator are **32** and **60**.
>
> What replaces it is smaller and true: **an absorbing boundary installs no real-axis poles and a
> lossless one installs a full set** — now proved by an exact spectral criterion rather than a
> grid, holding under *both* the mislabelled and the corrected family. That is a theorem about
> lossless-vs-absorbing systems, which the original document already conceded in its own §4.5.
> **It is corroboration, not a crux, and it does not decide decision 1.**
>
> **The lane's real result is elsewhere and it survives intact:** the ϖ (global-phase) common mode
> is *exactly* unobservable, so decision 1's proposed common-mode-projection receipt cannot fire —
> which removes the stated basis for decision 1's fork and settles it on the merits.

---

## §1 — THE KILLER: what the code actually does at a terminated port

### 1.1 Line by line, `harmonic_balance_srs.py`

A `Termination` (`:383-405`) carries three arrays: `ports` (flat directed **incident** slots),
`paired` (`:387-389`, *"the flat SRC port whose V_ref would have CONNECTed into it"*), and
`drive` (the imposed phasors `s_hat`). `make_termination:485` builds `paired` by inverting the
connect map, `dst_to_src`.

Inside `solve_tone` (`:534-613`) — the operative sequence, in order:

1. `mask_T = _term_mask(...)` (`:561`), `mask_F = ~mask_T` (`:562`) — the terminated slots are
   removed from the unknown set.
2. `v_s[term.ports] = term.drive[tone_index]` (`:566-567`) — the incident phasor on each terminated
   slot is **imposed**, state-independently.
3. `b = M_flat(v_s)[mask_F]` (`:571`) — the imposed value is pushed one step into the interior.
4. `matvec` (`:575-579`) assembles `e^{iθ}x − (Mv)` **on `mask_F` only**. The fixed-point equation
   at a terminated slot is never written down.
5. `defect = (eith*v − M_flat(v))[mask_F]` (`:604`) — the residual receipt is also free-slots-only.

**Measured on the shipped fixture** (`build_srs_net(L=2)`, N=64, degree 3, ndof 192, 96 bonds;
32 terminated slots; `structure.py`), at θ=0.6:

| quantity | value |
|---|---|
| `v_T − s_hat` (is the incident wave imposed?) | **0.0** exactly |
| fixed-point defect on FREE slots | 1.84e-15 |
| fixed-point defect on TERMINATED slots | **0.354** — the equation there is discarded, not satisfied |
| arriving wave `(Mv)_T` max abs (discarded) | 0.4189 |
| near-side outgoing `V_ref_T` max abs (radiated into the scaffold, never returned) | 0.4189 |
| imposed drive max abs | 0.300 |

**So, at a terminated port:** the incident wave is **imposed** = `s_hat`; the wave the interior
radiates outward is **swallowed and never returned**; the wave that would have arrived from the far
side is **discarded**. The termination set is closed under pairing (measured:
`all_partners_terminated = True`), so each of the 16 crossing bonds is cut in **both** directions —
a full sever, with an independent matched generator hanging on each stump.

### 1.2 What circuit element that IS, with the S-parameter

Take the port's wave variables in the bond's own reference impedance `Z_b = Z_0·sqrt(S(A_b))`:
`a` = wave travelling **into** the lattice (`= v[t]`), `b` = wave travelling **out of** the lattice
(`= V_ref[t]`). The scaffold sets

```
a = s_hat ,   independent of b            =>    S_source = ∂a/∂b = 0
```

**That is a matched generator: a one-port source whose S-parameter is `Γ_s = 0`, i.e. a wave port
terminated in the reference impedance `Z_s = Z_b = Z_0·sqrt(S(A_b))` with an incident-wave
excitation.** In TLM language it is a modal/wave port with a matched load; in VNA language it is a
port calibrated to `Z_b` — an anechoic boundary that also injects.

**Not** `Z_s = 0`. A `Z_s = 0` ideal voltage source is `Γ_s = −1`, and canon's own KUBC row says so:
`translation-circuit.md:404` `[CANON, verified verbatim at that line]`: *"every boundary node held
by an ideal voltage source on the affine profile"*. Holding the total node voltage means
`a + b = const`, i.e. `a = −b + s` — a different operator from `a = s`. **Surviving finding (i)
stands, and is now proved by exhibiting the KUBC operator and showing it is a different one** (§1.4).

### 1.3 The sweep parameter was a TRANSMISSION coefficient — CONFIRMED

`rho_sweep.py:47-50` sets

```python
out[mask_T] = x[mask_T] - rho*Mx[mask_T]        # i.e.  v_T = rho·(Mv)_T + s_hat
```

Measured identities on the fixture (`structure.py`, exact to 0.0 on a random complex state):

```
(Mv)[t]         == V_ref[paired[t]]     the wave arriving FROM ACROSS the cut
(Mv)[paired[t]] == V_ref[t]             the near side's OWN outgoing wave
```

So the swept coefficient multiplies **the far end's outgoing wave**: `near-incident := rho × far-
outgoing`. That is a **through-transmission gain across the severed bond**. At `rho = ±1` the bond
is still *connected* (with a sign flip at −1) and the only thing removed on `T` is the `e^{iθ}`
factor — it is a defect in the lattice's own equation, not a mirror at a cut. **Verify finding (b)
is CONFIRMED in full.**

A genuine **source reflection** must send the near side's outgoing wave back at it:

```
v_T = Γ·(Mv)[paired] + s_hat       ==      v_T = Γ·V_ref_T + s_hat        (the CROSSED form)
```

The two families **coincide identically at zero** — measured relative difference between the two
solutions at `Γ = ρ = 0`: **0.0 exactly**, both matching the shipped `solve_tone` to **2.11e-15**.
Therefore the original document's §2.2 validation (*"ρ=0 reproduces the shipped solver to 7.3e-15,
and only at ρ=0"*) has **zero discriminating power** over which family is the right generalization.
That defence is withdrawn.

### 1.4 The corrected family is the one canon already names

Substituting `V_ref[t] = w[u] − v[t]` (the shunt-junction node voltage minus the incident wave):

| Γ | terminated equation | reduces to | canon name |
|---|---|---|---|
| **−1** | `v_T + V_ref_T = s` | **`w[u] = s`** — the node voltage is clamped | **KUBC**, `translation-circuit.md:404` |
| **0** | `v_T = s` | incident wave imposed, outgoing absorbed | matched generator — **what ships** |
| **+1** | `v_T − V_ref_T = s` | **port current clamped** | **SUBC**, `translation-circuit.md:196` |

**Measured, not asserted** (`sweep_corrected.py`, θ=0.7): the Γ=−1 node-voltage clamp holds to
**1.11e-16**; the Γ=+1 port-current clamp holds to **6.33e-16**.

This is the reason the corrected family is the right one: its three members are exactly canon's
three named boundary excitations, and the shipped code sits at the middle one. It also means
**no solver change is needed to run the correct sweep** — the crossed operator is assembled from
`apply_M` and `scatter_weights` alone, outside the module. It *would* be needed to ship Γ into
`Termination` (amendment 1).

### 1.5 The corrected sweep, run — and an exact pole count instead of spike counting

Same fixture, same 400 θ ∈ [0.05, π−0.05], same cold linear network (A=0, S=1). "Poles" are no
longer counted as grid spikes: the driven operator is `A(θ) = z·D + K` with `z = e^{iθ}` entering
**linearly and only on free rows**, so its singularities are the finite eigenvalues of the pencil
`(−K, D)`. A real-θ pole is an eigenvalue **on the unit circle**. 160 finite eigenvalues in every
case.

| family | Γ / ρ | median | max | grid spikes (>10× median) | **exact: on unit circle** | **exact: in (0.05, π−0.05)** |
|---|---|---|---|---|---|---|
| — | matched (both families, identical) | 2.076 | 3.282 | 0 | 36 of 160 | **0** |
| straight (**mislabelled**) | −1 | 3.023 | 143.64 | 10 | 160 of 160 | **46** |
| straight (**mislabelled**) | +1 | 1.476 | 102.46 | 24 | 160 of 160 | **46** |
| **crossed (correct)** | **−1 = KUBC** | 2.981 | **414.65** | 8 | 160 of 160 | **32** |
| **crossed (correct)** | **+1 = SUBC** | 1.577 | **185.80** | 23 | 160 of 160 | **60** |

Two things this fixes and one it preserves:

* **The matched "0" is now exact and honestly qualified.** 36 of the 160 eigenvalues *are* on the
  unit circle — measured angles: **exactly 0 and exactly π, nothing else**. Those are the
  self-conjugate tones `ToneSet` already rejects by construction (module header, `:80`). The other
  124 are strictly inside the disk (max |z| = **0.9563**); **none** is outside. So: *the matched
  scaffold installs no pole anywhere in the open tone domain (0,π)* — proved, not sampled.
* **The mirror counts are wrong and are withdrawn.** 10 → 46 (straight), 24 → 46 (straight),
  and under the correct operator 32 (KUBC) and 60 (SUBC). Grid spike counting undercounts by ~4×
  because resonances narrower than the θ-spacing fall between samples.
* **The qualitative conclusion survives both operators:** at `|Γ| = 1` *every* eigenvalue sits on
  the unit circle (max deviation 1.7e-15 … 3.3e-15) — the boundary absorbs nothing, the system is
  closed and lossless, and real-axis resonances are dense. At Γ=0 they retreat inside the disk.

**But that is a theorem, not a discovery.** A lossless system with a non-absorbing boundary has its
spectrum on the unit circle; adding a matched absorber moves it inside. `ANALYSIS.md` §4.5 states
the same fact in its own honest caveat. **The sweep is corroboration. It is demoted from "the whole
argument for the verdict" (original §2.4) to a worked illustration.**

### 1.6 The internal contradiction (verify finding 3) — resolved, not papered over

The straight `ρ=+1` arm and the ADOPTED `I_u` Norton cross-check are the same class of object and
were given opposite verdicts for the same property. **Measured:** straight ρ=+1 has 160/160
eigenvalues on the unit circle; the intact `M` has **192/192** (max deviation from unity
1.15e-14) with **62** angles in the window. Both are closed lossless systems with a full
real-axis pole set.

The correct distinction is not *"has poles"* but *"whose poles"*:

* an **uncut** lattice's unit-circle spectrum is the medium's own cold Bloch band — trivially
  satisfiable, *"you found a plane wave"* (original §4.5, correct);
* a **cut with a mirror on it** manufactures a spectrum that belongs to the cut.

So the ρ=+1 row's rejection reason as written ("it has poles") was wrong; its rejection reason as
corrected is that the crossed Γ=+1 (SUBC) *cut* installs 60 poles the medium does not own. The
Norton row keeps its ADOPT — with the disclosure in §3 attached.

---

## §2 — Decision 1 re-adjudicated: the "NEITHER OPTION AS POSED" verdict was rejecting a strawman

### 2.1 What the source texts actually propose (verified verbatim)

`_orchestration/open-items/2026-08-25-g2-freeze-decisions.md:22-30`, Decision 1 in full:

> *"Source-terminated boundary phasors vs injection-lock. **Orchestrator recommendation, REVISED at
> the 2026-08-25 walk** (the earlier lean was source-terminated alone): solve **source-terminated
> with the common mode explicitly projected out**, injection-lock as the physics-honest
> cross-check, and make the projection a receipt — if projecting out the common mode changes the
> solution, the scaffold was doing illegitimate work."*

`research/2026-08-25_g2-boundary-and-gyromagnetic-walk_RECORD.md` §1, the table, verbatim:

| scaffold | what it imposes | guard-8 status |
|---|---|---|
| source-terminated | absolute port phasors = differential **+** common mode | imposes ϖ unless explicitly quotiented |
| injection-lock | relative phase only | **imposes only the differential, by construction** |

**Grep across all four named source files** (`g2-freeze-decisions.md`,
`2026-08-24_g1-ac-steady-state-walk_RECORD.md`, `2026-08-25_g2-boundary-and-gyromagnetic-walk_RECORD.md`,
`2026-08-24_static-existence-epic.md`) for `zero source impedance|series impedance|ideal AC
voltage|voltage source|Thevenin|Norton`: **zero hits in every file.**

`ANALYSIS.md` §2.1 asserts *"The decision text (and this lane's brief) read source-terminated as
ideal AC voltage sources, Thevenin, zero source impedance."* **That attribution to the decision text
is false.** (No A1 lane brief exists in the corpus, so the "and this lane's brief" half is not
checkable from here; the checkable half is wrong.) **Verify finding (e) is CONFIRMED.**

### 2.2 Worse than a misquote: the sweep varies an axis decision 1 does not fork on

Read the walk table again. Both options are described by **what the drive specifies** —
*absolute port phasors* vs *relative phase only*. Neither row says anything about source
**impedance**. The ρ/Γ sweep varies source impedance. **The two options in decision 1 are not
Γ=−1 and Γ=+1; they are two drive specifications, both of which live at Γ=0.** Rejecting
"both literal readings" rejected two circuits the lane itself introduced.

### 2.3 The ADOPT set is structurally what decision 1 already recommends

| decision 1 | this lane's ADOPT set | relation |
|---|---|---|
| source-terminated, PRIMARY | shipped matched-generator termination, PRIMARY | **same object** |
| injection-lock, cross-check | node-current (Norton) injection, cross-check | same *role*; **not the same object** — see §3.3 |
| the common-mode projection, as a receipt | *(killed — cannot fire)* | **the one real disagreement** |

**So the deliverable is the amendments, not the rejection.** The verdict line is rewritten:

> **DECISION 1 — ENDORSE, with three amendments and one deletion.** Keep source-terminated
> (the shipped matched generator) as PRIMARY and injection-lock as the cross-check, exactly as
> decision 1 says. **Delete the common-mode-projection requirement**: in the ϖ sense the projection
> is a no-op the solve already satisfies at machine precision, and in the additive sense it removes
> real drive. Relabel the scaffold correctly (it is a matched generator at `Γ_s = 0`, not the
> "KUBC / voltage-clamped" class its own docstring names) and normalize the idle criterion.

### 2.4 And the deletion settles decision 1 on the merits

Decision 1's *stated basis* for demanding the projection is guard 8: source-terminated
*"imposes ϖ unless explicitly quotiented."* **It does not.** `M` is real (`a_nodes = 2Yp/ΣYp` is
real-positive at `:324-334`; CONNECT is a permutation at `:492-504`), so `s → e^{iφ}s` implies
`v → e^{iφ}v` exactly, and the envelope reads `|v|`, so the S-field cannot move. **Replicated
independently this session** (`replicate_R1_R2.py`, two-tone self-consistent solve, φ=0.7391):

```
||A' − A||_inf                            = 1.6119e-12
phase spread of v'/v after removing e^{iφ} = 6.189e-11
modulus spread of v'/v                     = 2.956e-11
```

Guard 8 is discharged for free by the reality of `M`. The ϖ objection to source-terminated
evaporates; the two options are equivalent on the axis that motivated the fork. **This — not the
pole sweep — is the lane's answer to decision 1.**

---

## §3 — The `term is None` structural-zero branch (verify finding (d)) — CONFIRMED, amendment fixed

### 3.1 The branch, verbatim

`harmonic_balance_srs.py:805-815`, verbatim at those lines:

> *"SCAFFOLD-ABSENT BRANCH — READ THIS BEFORE QUOTING AN IDLE VERDICT (disclosed 2026-08-25,
> adversarial round 2). When `term is None` there is no scaffold to measure, and this function
> returns LITERAL ZEROS for source_amp / exchange_amp / P_in / P_out — they are structurally
> guaranteed, NOT measurements. On such a call two of idle_verdict's three criteria are satisfied
> by construction and only r_auto carries content, so an 'idle' verdict there is a ONE-observable
> verdict."*

`ANALYSIS.md` and `SCHEMATIC.txt` never mention it. §4.1 presents idle as three observables with no
branch caveat. **CONFIRMED.**

### 3.2 The recommended Norton cross-check walks straight into it — measured

The ADOPTED cross-check is `I_u` injection with the lattice **uncut**. Uncut ⇒ no `Termination` ⇒
`term is None`. Measured (`commonmode_and_norton.py` C3; θ=0.6, dense solve of
`(e^{iθ}I − M)v = c`, `c` = node-current-style additive drive):

```
source_amp = 0.0    exchange_amp = 0.0    P_in = 0.0    P_out = 0.0     (literal, structural)
r_auto     = 0.32517202531675493
||c||/||v|| = 0.32517202531675493         identity gap = 0.0  EXACTLY
idle_verdict -> source_quiet = True, scaffold_untouched = True   (both by construction)
```

So under the Norton scaffold two of the three idle criteria pass **for free**, and the third is the
identity `r_auto ≡ ||c||/||v||`. The original §4.4's celebrated *"agree to 1e-13"* is the LGMRES
tolerance on a tautology — with a dense solve the gap is **exactly 0.0**. It is not evidence of
anything physical. **Its status is demoted from receipt to derivation check.**

Note what does *not* collapse: the surviving observable, `r_auto = ||c||/||v||`, is the **reciprocal
of the driven transfer**, which is precisely the scale-free ratio §4.5 argues for. The Norton
cross-check is not worthless; it is **one-observable**, and it must be declared as such.

### 3.3 Amendment 3, fixed

Original amendment 3 read: *"Freeze `source_amp/norm(v)` (or, under node injection,
`r_auto == norm(c)/norm(v)`) as the criterion."* The parenthetical freezes a tautology as a
criterion. Rewritten:

> **Amendment 3 (revised).** Freeze the **scale-free** idle criterion `source_amp/‖v‖` and
> `exchange_amp/‖v‖` on the terminated scaffold, and book `P_net` as a convergence receipt rather
> than a verdict observable (it is identically zero by losslessness — replicated: `P_in = P_out =
> 2.4577940011`, `P_net = −2.0e-11`). **On the uncut Norton cross-check, state in the prereg that
> the idle verdict is a ONE-observable verdict** (`harmonic_balance_srs.py:805-815`), that the
> surviving observable is `r_auto = ‖c‖/‖v‖` = 1/(driven transfer), and that the remaining verdict
> weight there must be carried by the railing criterion and decision 2's projected M/Q — not by
> `source_amp`, `exchange_amp`, `P_in` or `P_out`, which are structural zeros on that branch.

Also flagged: decision 1's cross-check is **injection-lock** ("relative phase only"), which is a
*drive specification*. The lane silently substituted **node-current Norton injection on an uncut
lattice**, which is a *different object* and the one that triggers the `term is None` branch.
G2 should freeze which of the two it means.

---

## §4 — The common mode (verify finding (c)) — claim corrected, positive control re-scoped

### 4.1 The claim as written is false on this fixture — measured

`ANALYSIS.md` §3.3 and `SCHEMATIC.txt` box S3 assert: *"every boundary port driven with the same
incident voltage = the junction's `+1` eigenvector = the A1 monopole/dilatation drive."*

Measured on the shipped fixture (`commonmode_and_norton.py` C1):

```
terminated slots                 : 32, on 32 DISTINCT nodes
max terminated ports per node    : 1
common-mode energy share of a UNIFORM additive drive : 0.33333333333333337
common-mode energy share of a RANDOM  drive          : 0.33333333333333333
predicted Y_p/ΣY (the §1.2b weight formula)          : 0.33333333333333333
```

**The uniform additive drive is a 1/3-common, 2/3-differential mixture**, exactly as `ANALYSIS.md`'s
own §1.2b weight formula `Γ_vertex = (Y_0/ΣY)(+1) + (1 − Y_0/ΣY)(−1)` predicts. The document
contradicts itself between §1.2b and §3.3, and the figure asserts it harder than the prose
(panel (a) prints *"the COMMON mode (A1 breathing)"*).

Sharper than the verify lane put it: because every terminated node hosts **exactly one** terminated
port, the drive subspace at each node is one-dimensional, so **the 1/3 : 2/3 split is fixed for
every drive this fixture can express** — uniform, ramped or random (measured above: identical to
16 digits). No drive available through this `Termination` is purely common, and none is purely
differential. There are three distinct objects wearing the name here, not two:

| name | object | on this fixture |
|---|---|---|
| **CM-mult (ϖ)** | global phase `s → e^{iφ}s` | gauge; exactly unobservable (§2.4) |
| **CM-add (boundary set)** | uniform additive `s → s + c` across the terminated set | a real drive; **1/3 A1 + 2/3 differential per node** |
| **A1 (port irrep)** | the junction's `+1` eigenvector, per node | **not expressible** by this fixture's drive |

Naming the z=3 vertex's `+1` mode "A1" additionally imports canon's **K4 4-port** decomposition
(`port-register.md:37`, verified verbatim: *"The K4 4-port amplitude space decomposes under $T_d$
as $V_{4\text{-port}} = A_1 \oplus T_2$"*) onto a degree-3 carrier — the same unstated 4→3 mapping
the module itself flags as un-canonical. Keep the "A1-**adjacent**" hedge the module uses at `:146`.

### 4.2 The 23% positive control, re-scoped — and given the matched control it lacked

The 23% number replicates (`replicate_R1_R2.py`: `dA_rel = 0.23398` at `c = 0.10`, baseline
`A_max = 0.54733`). **What it establishes is that an additive shift of the boundary drive moves the
solution — i.e. the drive is not gauge and the receipt can fail.** That is a valid positive control
and it is kept, **renamed**: *additive-drive sensitivity*, not *"A1 mass-sector drive"*.

What it cannot establish is anything about the A1 channel specifically, because the perturbation is
2/3 differential by construction and there is no comparator.

**A control that does isolate A1 is constructible today with the shipped `make_termination`, with
no solver change** — terminate all `z` ports of a set of nodes, so the node's `+1` eigenvector lies
in the drive space. Built and run (`commonmode_and_norton.py` C2; 8 nodes × 3 ports = 24 terminated
slots; two-tone self-consistent solve; both perturbations of **equal norm 0.48990**):

| perturbation | common-mode energy share | `‖ΔA‖_inf / A_max` |
|---|---|---|
| **pure common (the A1 `+1` eigenvector)** | **1.0** | **32.24 %** |
| **pure differential** (`Σ_j Y_j s_j = 0`) | 3.2e-33 | **37.88 %** |

(baseline `A_max = 0.4107`, all three solves converged; this fixture is *not* the crossing-plane
fixture, so 32% is not comparable to the 23% above.)

Two conclusions, and the second is the one that had to be walked back:

1. **A genuine A1 drive does move the S-field — 32%.** So "projecting out the additive common mode
   removes real drive" is **true in kind** and survives, *on a fixture where the A1 mode is
   expressible*.
2. **A1 is not privileged.** An equal-norm differential perturbation moves the S-field *more*
   (37.9% vs 32.2%). The rhetorical claim that projecting out the common mode would *"delete the
   drive on the very sector the solver runs in"* over-reads: it would remove one channel among
   several, and on this measurement not the strongest one. **Demoted from a decisive argument to a
   supporting one.**

The re-scoped P3 for the prereg is therefore two items: the **additive-drive sensitivity** control
(fires, 23%, on the shipped fixture) and, if an A1-specific claim is wanted, the **A1-isolating
fixture with its matched differential comparator** (32.2% vs 37.9%).

---

## §5 — PRESERVED: what the verify lane did not dispute, re-verified here

**(i) The shipped docstring's "KUBC / voltage-clamped" label is wrong for a TLM wave port.**
The phrase is at `harmonic_balance_srs.py:49` (verified verbatim; `ANALYSIS.md` cited `:40-46` —
anchor drift, corrected in §6). Canon defines KUBC at `translation-circuit.md:404` as *"every
boundary node held by an ideal voltage source"* — verified verbatim at that line. **Now proved
constructively rather than argued:** the operator that actually does that is the crossed `Γ = −1`,
which clamps `w[u] = s` to **1.11e-16** (§1.4), and it is a *different operator* from the shipped
`Γ = 0`. `Γ_s = −1` vs `Γ_s = 0`. **Relabel: MATCHED GENERATOR / wave port at `Z_s = Z_b`.**
The module's decline to use the Hill-Huet two-sided bound (`:51-53`) is separately correct and
canon-fenced (`translation-circuit.md:196`, verified verbatim: *"static / DC / single-sign-
susceptance ONLY — for a mixed-reactance AC network $B(\omega)$ is not sign-definite and both
bounds FAIL"*).

**(ii) The ϖ-projection receipt CANNOT FIRE — the strongest surviving result.**
`M` is real ⇒ the solve is exactly equivariant under global phase ⇒ decision 1's proposed receipt
is a tautology. Independently replicated this session: `dA_inf = 1.6119e-12`, phase spread
6.189e-11, modulus spread 2.956e-11 (§2.4). It kills decision 1's recommended receipt outright and,
as §2.4 argues, removes the stated basis for decision 1's fork. **Book ϖ-equivariance as a
REGRESSION TEST on `M` staying real — not as physics evidence about the scaffold.**

**(iii) The multiplicative-vs-additive common-mode homonym, with the canon fence.**
`relational-cancellation-identity.md:63-64` (verified verbatim, the quote spans both lines; the
document cited `:64` alone): *"⚑ **'Common-mode' here is an INFLUENCE class, never the A1 port/irrep
MODE grade** — see the fence in §5.5."* And `:316` (verified verbatim): *"**The A1 port/irrep
COMMON-MODE MODE grade** — 'A1 = common-mode scalar/longitudinal (dilatation, mass)'
(`port-register.md:37`) — is the **physical mass sector**, the opposite disposition from a
self-cancelling influence."* The homonym is real, canon states it, and the lane was right to
separate the two senses. §4.1 above **adds a third** sense that the document collapsed into the
second (boundary-set uniform ≠ per-node `+1` eigenvector).

**(iv) The choke analogy breaks for ϖ.** *"You cannot build a component that blocks a choice of
time origin."* A choke blocks common-mode **current** — a physical channel; ϖ is a phase reference,
not a channel. **This is the load-bearing break-reason and it stands alone** (see §6, finding 8:
the other two stated reasons are withdrawn).

**(v) The decision-4 machinery blocker — VERIFIED, with the anchor corrected.**
Verbatim at `harmonic_balance_srs.py:146-149` (the `* sector` bullet):

> *"SCALAR channel on the srs-z3 carrier (the Class-C lane's), the A1-adjacent longitudinal slot.
> The T2/Cosserat channel is NOT wired in (A1 perpendicular to T2, `master-equation.md:20`); no
> winding observable exists here."*

`ANALYSIS.md` §6(a) cites this as `:157-161` and marks it verbatim; §3.3 cites `:155-160`.
**Both anchors are wrong** — `:157-161` is the `* coordinates` bullet. The **text is accurate**;
only the line anchor drifted. See §6, finding 7.

**Consequence for decision 4, stated precisely.** `g` is a **cross-sector ratio**: magnetic moment
from the T2 winding over angular momentum from the Cosserat microrotation, normalized by an A1
mass. This module carries the A1-adjacent scalar channel **only**, and declares that no winding
observable exists in it. Therefore:

* **`g` cannot be computed by this solver today.** Not "is hard to compute" — the operator has no
  degree of freedom that carries the numerator. **`decision4_blocker_confirmed = true`.**
* A G2 unit test asserting a computed `g` would be **testing a stub**, and freezing `g` as a G2
  *verdict observable* would freeze an observable the instrument cannot read.
* What *is* testable now is unchanged from the original §6(b) and survives: (1) the **anti-leak
  assert** on the same triad the module already guards for ALPHA / Q_TANK / ELECTRON, so a future
  `g` is provably not smuggled in from constants; (2) a **convention-invariance test** on the
  eventual estimator under global phase, `v_norm` rescale, and c-state vs full-tank envelope.
  Both are guards on a future `g`, not measurements of one — label them that way.
* Unblocking `g` requires wiring the T2/Cosserat channel, i.e. a different (or extended) solver.
  That is a build item, not a prereg item.

---

## §6 — The remaining verify findings, each dispositioned

**Finding 3 (MEDIUM, ρ=+1 vs Norton contradiction) — ACCEPTED, fixed in §1.6.**

**Finding 5 (MEDIUM, the drawn varactor) — ACCEPTED IN PART; one sub-claim of the verify lane is
itself wrong.**
*Accepted:* `S` reaches the operator **only** through `a_nodes = 2·Yp/ΣYp` (`:324-334`, read this
session), and `conn` is a fixed permutation (`:492-504`) — so the per-bond transit is exactly one
step at **every** `A`, and there is **no** saturation-induced delay, index or dispersion anywhere in
the operator. Drawing a lumped in-line varactor `C_eff = C_0/S` on a line also labelled
`T_D = ℓ_node/c` implies a delay that changes with `S`, which the code does not have: with `L`
fixed, `C → C_0/S` gives `Z = Z_0√S` but delay `T_0/√S`. The schematic hides a real modelling
commitment (a **stubless unit-delay graded-admittance TLM network**) behind a lumped part.
*Also accepted:* the element row citing `chiral_lattice.py:431-438 (bond_lc)` points at a function
the solver never imports — verified: `bond_lc` exists at exactly those lines, and `grep` for
`bond_lc|L_per|C_per|c0` in `harmonic_balance_srs.py` returns **nothing** (the solver is
dimensionless, `Y0 = 1`). Delete the row or mark it as out-of-path context.
*Rejected:* the verify lane's claim that *"holding the delay fixed requires both, which gives Z
proportional to S, not sqrt(S)"* — that is arithmetic on the wrong pair. With `L → L_0√S` and
`C → C_0/√S`: `Z = √(L/C) = Z_0·√S` ✓ and delay `= √(LC) = √(L_0C_0)` **fixed** ✓. The element set
**is** realizable; the schematic's labels are simply the wrong ones. **Fix = relabel** the bond as a
distributed graded LC line, `L ∝ √S`, `C ∝ 1/√S`, constant one-step delay — not "unrealizable".

**Finding 6 (MEDIUM, regime overreach) — ACCEPTED.**
`rho_sweep.py:28` is `bond_admittance(np.zeros(bt.n_bonds))`: A = 0, S = 1, strictly **linear**.
My corrected sweep (§1.5) is cold too — the pole statement is a **cold-linear** statement. The R3
drive sweep runs *downward* (A_max 0.547 → 0.019), away from the rail. `SCHEMATIC.txt` box S4's
unqualified *"NO POLE ANYWHERE NEAR these tones on this net"* is withdrawn and replaced by:
**"no pole in the open tone window on the COLD LINEAR net; the nonlinear existence question at
A → A_cap is untouched by any measurement in this lane."**

**Finding 7 (MEDIUM, cite drift) — ACCEPTED. Corrected anchors, each re-verified at HEAD:**

| claim | cited as | **actual** |
|---|---|---|
| "KUBC / voltage-clamped boundary-condition CLASS" | `:40-46` | **`:49`** |
| the Hill-Huet decline | `:44-46` | **`:51-53`** |
| "The T2/Cosserat channel is NOT wired in … no winding observable exists here" | `:157-161` / `:155-160` | **`:146-149`** |
| "one step = one bond transit" | `:31-33` | **`:43-44`** |
| `relational-cancellation-identity` common-mode fence | `:64` | **`:63-64`** (quote spans two lines) |

The quoted **text** is accurate in every case; only the anchors drifted. The §6(c) finding against
the four KB leaves is separately **CONFIRMED**: `translation-circuit.md:637` reads *"The substrate's
cold-lattice ideal state is the limit:"* and the g=2-POSITED text is at **`:839`**.

**Finding 8 (LOW, choke break-reasons) — ACCEPTED.** Break-reason (i) ("no two-wire pair") is
equally true of CM-add, for which the same section says the analogy holds, so it cannot be a
CM-mult-specific break. Break-reason (ii) (finite vs infinite CMRR, citing
`relational-cancellation-identity.md:79`, verified verbatim: *"The substrate's CMRR is infinite BY
IDENTITY."*) is a difference of **degree**, and canon draws it as a contrast with a bench
instrument, not as a prohibition. **Reasons (i) and (ii) are withdrawn as break-points; reason
(iii) is the category break and is sufficient alone.**

**Finding 9 (LOW, the replacement receipt is redundant) — ACCEPTED, and it is *more* redundant
under the corrected operator.** In the crossed form the boundary term is `Γ·V_ref_T` — and
`V_ref` at the terminated set is *exactly* what `exchange_amp` already measures
(`harmonic_balance_srs.py:826-830`, `out = V_ref.ravel()[term.paired]`; the terminated set is closed
under pairing, measured §1.1). So *"the interior must be Γ-invariant"* and *"`exchange_amp/‖v‖ →
0`"* are the same statement, and the module already computes the second one for free. The partial
defence (the self-consistent S-field makes the response nonlinear in the boundary term, so they are
not *strictly* equivalent) is real but was never argued in `ANALYSIS.md`. **Amendment 2 is rewritten
in §7 to use the observable that already exists, plus a single Γ=−1 discriminator rather than a
5-point sweep.**

**Finding 10 (LOW, presentation) — ACCEPTED.** `(2−z)/z = −1/3` is **z=3 only** (re-run of
`junction_modes.py`: z=4 cold `S[0,0] = −0.5`, z=4 graded `−0.5705`, z=3 graded `−0.44022`); what
holds in all four cases is the **mixture formula**, which is the real finding. Figure panel (a)
prints the chain as one equality — fix the figure. And `[CANON]` tags on module source/docstring
lines (§3.3, §4.1) violate the document's own grade key (*"quoted from corpus with a receipt"*) —
module source is `[CODE]`, not canon.

---

## §7 — The three amendments, rewritten

1. **Relabel first; ship `Γ` only if it earns its place.** The docstring relabel
   (`harmonic_balance_srs.py:49`) is unconditional and free: the shipped scaffold is a **matched
   generator / TLM wave port, `Γ_s = 0`, `Z_s = Z_b = Z_0√S`**, not the "KUBC / voltage-clamped"
   class. If a source-reflection parameter is added to `Termination`, it **must** be the crossed
   form `v_T = Γ·(Mv)[paired] + s_hat` (equivalently `Γ·V_ref_T`), whose Γ = −1 / 0 / +1 are canon's
   KUBC / matched / SUBC — measured to 1.1e-16 and 6.3e-16 (§1.4). **Do not ship the
   `rho·(Mv)_T` form from `rho_sweep.py`: it is a transmission gain across the cut, and shipping it
   would land the error in AVE-Core.** Both forms reproduce today's solver at zero, so that
   validation cannot be used to justify either.
2. **Use the receipt that already exists.** Replace the ϖ-projection receipt with the scale-free
   **`exchange_amp/‖v‖`** the module already computes, and — if a boundary-load-bearing
   discriminator is wanted — **one** re-solve at the crossed `Γ = −1` (true KUBC), not a 5-point
   sweep at 5× cost. Book ϖ-equivariance as a **regression test** on `M` staying real.
3. **Normalize the idle criterion and disclose the one-observable branch** — as written in §3.3.

Plus one deletion and one addition:

4. **DELETE** decision 1's common-mode-projection requirement (§2.4): a no-op in the ϖ sense,
   a mutilation in the additive sense.
5. **ADD** the positive controls of §4.2 — *additive-drive sensitivity* on the shipped fixture
   (23.4%), and, for any A1-specific claim, the **A1-isolating fixture with its matched
   differential comparator** (32.2% vs 37.9%), which needs no solver change.

---

## §8 — What this lane now claims, and at what strength

| claim | strength |
|---|---|
| The shipped termination is a matched generator, `Γ_s = 0`, and its "KUBC / voltage-clamped" docstring label is wrong | **SOLID** — proved by exhibiting the KUBC operator (node-voltage clamp to 1.1e-16) and showing it is a different one |
| The ϖ-projection receipt cannot fire; guard 8 is discharged by the reality of `M` | **SOLID** — 1.6e-12, replicated twice independently |
| Decision 1 should be ENDORSED with amendments; the "NEITHER OPTION" rejection is withdrawn | **SOLID** — source texts quoted verbatim; zero hits for the attributed language |
| An uncut Norton cross-check gives a ONE-observable idle verdict | **SOLID** — structural zeros measured, identity gap exactly 0.0 |
| The uniform additive drive is 1/3 A1 + 2/3 differential, and a pure A1 drive is not expressible on this fixture | **SOLID** — 0.33333333333333337, max 1 terminated port per node |
| A pure A1 drive moves the S-field (32.2%), but by less than an equal-norm differential one (37.9%) | **MEASURED**, single fixture, cold-started self-consistent solve |
| A matched boundary installs no pole in the open tone window; a lossless one installs a full set | **CORROBORATION of a theorem**, cold-linear only — *not* a crux, and it does not decide decision 1 |
| "10 poles / 24 poles / 0 poles", "two mirrors", ρ as a source reflection coefficient | **WITHDRAWN** |
| `g` is not computable by this solver today | **SOLID** — module's own sector declaration, `:146-149` verbatim |
