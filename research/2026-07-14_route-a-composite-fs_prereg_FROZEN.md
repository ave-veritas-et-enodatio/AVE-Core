# ROUTE A — THE COMPOSITE FADDEEV-SKYRME NEUTRON BUILD — FROZEN PRE-REGISTRATION

**Date:** 2026-07-14 · **Lane:** implementer — corpus TBD-pin completion (the one new capability: the threaded-electron term in the FS energy integral).
**Brief (binding):** Grant GO 2026-07-14 — build ROUTE A, the corpus's own named completion route
(`neutron-identification.md:36`/`:77` TBD-pin: *"derive 1.293 MeV from FS solver applied to threaded
`0₁`-in-`6₂³` composite topology … Same shape as proton mass eigenvalue derivation but with the
additional threaded-electron constraint adding to the FS energy integral"*; `:54`: *"compute the FS
energy of the `6₂³ ∪ 0₁` composite minus the FS energy of the bare `6₂³`, in units of m_e c²"*). This
resurrects the n–p mass-split discriminator (the `2026-07-13_np-mass-split-gate` bin-(iv) second shot)
AND measures the split's δ_th-loading in one build (the ablation).
**Branch:** `derivation/route-a-composite-fs` · **PR:** opens `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` (only Grant merges).

**FREEZE-BY-PUSH.** This prereg lands as its OWN commit, PUSHED to origin, BEFORE any solver / driver /
result / test code exists in the tree. The freeze margin is the gap between this push and the first code
push — auditable from the GitHub push timestamps. No bin, tolerance, target, hard rail, C1–C5 choice, or
verdict-consequence in this document is edited after the first composite computation runs (Rule 11).

---

## THE ONE-SENTENCE BUILD

Build the composite Faddeev–Skyrme instrument the corpus TBD-pin names — the threaded-`0₁` term added to
the proton's own FS energy integral — value-blind, and read off (a) the n–p split `Δm = E_FS(composite) −
E_FS(bare)` in m_e units, sign included, and (b) the split's δ_th-loading via the warm-vs-cold κ_FS ablation.

---

## SECTOR HEADER (declared before any substrate claim)

- **MODE:** derivation-from-canon — extend the *existing* canonical proton FS instrument
  (`faddeev_skyrme.py` `TopologicalHamiltonian1D`) with the one new capability the TBD-pin specifies:
  the threaded-electron constraint inside the FS energy integral. **NOT engine-fire** (no time-domain
  K4/Cosserat step). The composite is a static rest-mass eigenvalue, same class as the proton.
- **REGIME:** cold lattice, baryon sector. Static rest-mass eigenvalues; no dynamics. The proton is the
  self-consistent FS feedback eigenvalue at cinquefoil crossing number `c=5` (`constants.py` proton
  chain `_X_CORE`/`PROTON_ELECTRON_RATIO`, reproduced live); the neutron is the *composite* — the same
  `6₂³` cage with a `0₁` unknot threaded through its central void.
- **PHASE-STATE:** bound topological solitons. The split is a **rest-energy difference** between two
  bound configurations (composite cage vs bare cage), plus (Reading X) the threaded electron rest mass.
- **SECTOR:** **A1 (dilatation / mass).** The split is an A1 rest-energy question (elastic strain of the
  stretched cage + threaded-electron rest mass), **NOT** a charge-sector question. Charge = Cosserat
  `(2,3)` winding (untouched); the threaded electron's `−1` cancels the proton's `+1` for net-zero
  (`neutron-identification.md:24`). A1 ⊥ charge respected; the split is not cross-wired to the charge
  cancellation. **Both cage twists contribute +1 m_e of inductive mass each** (mass is positive-definite
  regardless of twist sign — `self-consistent-mass-oscillator.md:54`).

**Phase-space coordinate check (A46):** the measured quantity is the **dimensionless rest-mass difference
in m_e units** — both the corpus target (`+2.531 m_e`) and every computed quantity live in that same real,
dimensionless coordinate. This is A1 rest-energy, **not** a phase-space (V_inc, V_ref) φ² claim; no
real-space-vs-phase-space mismatch is possible. The solver's integration coordinate `r` and the threading
displacement `d` are in the solver's **dimensionless ℓ_node Nyquist-gradient-cutoff unit** (per
`faddeev_skyrme.py:15-23`, the 2026-06-08 dimensional-provenance relabel), **NOT a real-space length** —
consistent with `r_opt = κ_FS/c` being a dimensionless coupling-budget ratio, not a confinement radius.

**Consistency-vs-emergence tag:** a *computable* split from the composite FS instrument, with **no
neutron-CODATA input** (the neutron mass is not read anywhere in the chain — it appears only as the
adjudication anchor `M_N_MEV_TARGET`, `constants.py:1138`, *"no framework derivation has yet been adopted
for the neutron mass"*), is an **emergence-class** attempt on the split's FORM. BUT: the absolute
magnitude rides α (via `p_c = 8πα` in the eigenvalue denominator) and δ_th (via `κ_FS`), so a magnitude
match is at most **consistency/manifestation-class** (same class as the proton m_p/m_e). **The δ_th
ablation is the δ_th statement** — a warm-only bin-(i) pass does NOT certify δ_th (see interpretation-care).

---

## THE FROZEN CHAIN (quoted with receipts — the ONLY chain permitted)

### A. The canonical proton eigenvalue chain (reproduced live, no refit)

```
_X_CORE               = I_SCALAR_1D / (1.0 - V_TOROIDAL_HALO * P_C)     # constants.py proton chain
PROTON_ELECTRON_RATIO = _X_CORE + 1.0                                   #  → 1836.1170402290593
```

Frozen consumed constants (HEAD literals @ base `240d59d8` — the no-refit reference set; any run-time
deviation is a finding):

| Constant | Value | Receipt |
|---|---|---|
| `I_SCALAR_1D` | `1161.9870305252678` | `constants.py:941` (FS scalar trace, `c=5`, warm κ_FS) |
| `V_TOROIDAL_HALO` | `2.0` | `constants.py:982` (dual-reactance count) |
| `P_C` | `8πα` ≈ `0.18340247377893987` | `constants.py` (`P_C` def) |
| `ALPHA` | `7.2973525693e-3` | `constants.py` (imported CODATA) |
| `KAPPA_FS_COLD` | `8π` ≈ `25.132741228718345` | `constants.py:832` |
| `DELTA_THERMAL` | `1/(14π²)` ≈ `0.0072372` | `constants.py:924` (the δ_th under audit) |
| `KAPPA_FS` | `KAPPA_FS_COLD·(1−δ_th)` ≈ `24.95084986518475` | `constants.py:927` |
| `PROTON_ELECTRON_RATIO` | `1836.1170402290593` | `constants.py` (proton chain) |

**δ_th enters via `KAPPA_FS` → the FS solver.** The FS solver `solve_scalar_trace(c=5)` at `κ=KAPPA_FS`
reproduces `I_SCALAR_1D = 1161.987…` (verified live); at `κ=KAPPA_FS_COLD` (cold 8π) it gives `1170.586…`
(the +0.74% δ_th shift). This is the ablation handle.

### B. The canonical neutron construction (`neutron-identification.md`; `proton-neutron-mass-split.md`)

- `neutron-identification.md:13`: `n = 6₂³ ∪ 0₁` — a proton Borromean cage with an electron `0₁` unknot
  threaded through its central structural void.
- `neutron-identification.md:25`: *"Ax1 forbids any flux tube from shrinking below transverse thickness
  1 ℓ_node, so threading an electron tube into the proton's core forces the Borromean rings to stretch
  outward — the elastic tension of this stretch is the Δm c² = 1.293 MeV mass **surplus**."*
- `neutron-identification.md:54`: *"compute the FS energy of the `6₂³ ∪ 0₁` composite minus the FS energy
  of the bare `6₂³`, in units of m_e c²."* — with the `ℓ_node`-radial-expansion premise 🔴 FLAGGED as
  *"not established."*
- `neutron-identification.md:77`: *"Same shape as proton mass eigenvalue derivation but with the
  additional threaded-electron constraint **adding to the FS energy integral**."*
- **Canonical fact frozen:** the neutron is explicitly **NOT a `(2,q)` ladder entry**
  (`neutron-identification.md:23`) — so the split is NOT an even-`c` `BARYON_LADDER` lookup; it is the
  composite `E_comp − E_bare` the TBD-pin names.

---

## THE SUBSTRATE-NATIVE WALK (fired before any solver code — the rendering is CANON-FORCED, not invented)

The one new capability is "the threaded-electron constraint adding to the FS energy integral." Three
physically-distinct renderings of "threading forces the rings to stretch" were walked against the bare
`c=5` solver (established/public values only — NOT the composite answer):

| Candidate rendering | 1D realization | sign of `E_comp − E_bare` | verdict |
|---|---|---|---|
| **(a) inner-core exclusion** | integrate cage profile on `[d, ∞)` (void vacated) | **NEGATIVE** (removes positive integrand near core) | ❌ ruled out by `:25` "mass **surplus**" |
| **(b) confinement stretch** | raise `r_opt` above `r_opt_max = κ/c` | **NEGATIVE** (E decreases monotonically with `r_opt`; no interior minimum, the functional is scale-free) | ❌ wrong sign |
| **(c) profile-shift-outward** | hold core `φ=π` on `[0,d]` (occupied by the threaded tube), wind `φ = π/(1+((r−d)/r_opt)ⁿ)` on `[d,∞)`; same functional, same `c=5` confinement | **POSITIVE** (the spherical `4πr²` measure weights the displaced winding shell more) | ✅ the **only** survivor |

**Checkpoint 10 (boundary-not-bulk):** rendering (c) is a **boundary condition** — the threaded tube is
an inner wall at `r=d` where `φ(d)=π`; the cage winds from that wall outward. NOT a bulk confining
potential `U_conf(r)` (which would be singular and detonate). ✅
**Checkpoint 1-3:** objective is the *existing* FS energy functional minimization (the canonical proton
instrument), not a new Lagrangian; A1 sector; the threading is a boundary displacement, not a bulk force. ✅
**Checkpoint 4:** measured in the matched dimensionless m_e coordinate; `r`, `d` in ℓ_node cutoff units
(not lengths). ✅

**The rendering is CANON-FORCED:** the corpus's own positive-surplus mechanism (`:25`) rules out (a) and
(b); only (c) survives, and it simultaneously satisfies `:77` ("same shape … adding to the FS energy
integral") and `:54` ("composite minus bare, in m_e units"). It is not a free choice.

---

## THE C1–C5 CHOICE LEDGER (the n–p gate's five enumerated missing choices — NOW MADE, justified from canon or tagged ENGINEERING-CHOICE)

| # | The missing choice (n–p gate) | ROUTE A choice | Justification |
|---|---|---|---|
| **C1** | FS field ansatz for the threaded `0₁` inside the `6₂³` cage | **Profile-shift-outward (c)**: cage `φ(r)=π` for `r≤d`, `φ(r)=π/(1+((r−d)/r_opt)ⁿ)` for `r>d`; same FS functional; confinement `r_opt ≤ κ_FS/5` unchanged (proton stays a proton). | **CANON-FORCED** — the only rendering consistent with `:25` positive surplus; satisfies `:77` "same shape … adding to the FS energy integral". The held-core `φ=π` on `[0,d]` (the tube's fully-wound core) is a modelling **ENGINEERING-CHOICE**, disclosed. |
| **C2** | threading-lock / boundary coupling energy term | **Folded into the boundary displacement — NO separate term.** The threading-lock energy IS the elastic FS-energy increase from the displacement. | **ENGINEERING-CHOICE (minimal, non-mint)** — `:25` attributes the whole surplus to a *single* "elastic-expansion tension" mechanism; adding a separate lock-coupling constant would be a MINT. The minimal choice adds nothing. |
| **C3** | Borromean cage elastic stiffness + radial-expansion magnitude `d` | Stiffness = **the FS functional's own tension** (no new constant). Displacement **`d = 1.0 ℓ_node`** (Ax1 transverse-thickness floor). | `d=1.0` from **Ax1** (no tube below 1 ℓ_node thick, `:25`; `:54` "expand by ℓ_node radially"). `:54` FLAGS this premise "not established" → a **disclosed `d`-sweep** `{0.5, 1.0, 1.5, 2.0} ℓ_node` is reported for robustness, with `d=1.0` the **frozen primary**. The sweep is characterization, **NOT** a selection mechanism (value-blind rail 4). |
| **C4** | mass-accounting: rest-mass-additive (X) vs absorbed (Y) | **Report BOTH.** Reading X: `Δm = [I_comp(d)−I_bare]/(1−V·p_c) + 1.000 m_e`. Reading Y: `Δm = [I_comp(d)−I_bare]/(1−V·p_c)` (whole surplus elastic). | **DISCLOSED FORK** (`proton-neutron-mass-split.md:10` leaves it open; np-gate flagged flag-don't-fix). Both readings' splits reported; bin assigned under both. Not a tuning choice. |
| **C5** | whether δ_th softens the composite's coupling | **RESOLVED EMPIRICALLY by the ablation** — run the whole split at BOTH warm `κ_FS=8π(1−δ_th)` AND cold `κ_FS=8π`; the **difference of the two splits** = the split's δ_th-loading. | Substrate adjudicates the FORK (`:77` FS-route δ_th-carrying vs `:54` linear-elastic δ_th-free) — no fiat. The ablation IS the C5 measurement. |

---

## THE SPLIT (the frozen computation)

Via the canonical eigenvalue map (the neutron cage is still a self-consistent FS oscillator — the same
`/(1−V·p_c)` regenerative feedback the proton uses):

```
m_p           = I_bare        / (1 − V·p_c) + 1                 # bare proton (reproduced live)
m_n(cage)     = I_comp(d)     / (1 − V·p_c) + 1                 # same +1 proton twist
Reading X:  Δm = [I_comp(d) − I_bare] / (1 − V·p_c) + 1.000     # + threaded 0₁ rest mass
Reading Y:  Δm = [I_comp(d) − I_bare] / (1 − V·p_c)             # whole surplus = elastic
```

where `I_bare = solve_scalar_trace(c=5; κ)` and `I_comp(d) = ` the shift-outward composite energy at
displacement `d`, same `(r_opt, n)` minimization, same `κ`. **DISCLOSED ALTERNATIVE** (reported, not
primary): the without-feedback elastic `[I_comp(d) − I_bare]` (linear-response, outside the loop) — a
sub-choice that changes the elastic term by the `1/(1−V·p_c) ≈ 1.58×` factor but (pre-registered
expectation) does not change the bin.

---

## THE δ_th ABLATION (frozen — its own observable, reported separately from the split)

**Every configuration runs at BOTH `κ_FS = 8π(1−δ_th)` (warm) AND `κ_FS = 8π` (cold).** The frozen
observable is **the difference of the two SPLITS** (not the two masses):

```
δ_th-loading of the split ≡ Δm(warm) − Δm(cold)
```

This is the resurrected δ_th second shot on the R3/R7/R10/R12 provenance findings — it measures how much
of the *split* rides δ_th, empirically resolving the C5 FORK. **Reported as its own frozen number**, under
both Reading X and Reading Y, at the primary `d=1.0`. A bin-(i) magnitude pass at warm-only does NOT
certify δ_th; **the ablation number is the δ_th statement.**

---

## THE FROZEN BINS (pre-named; consequences frozen verbatim)

**Target (named from CODATA anchors — band-NAMING only, NOT a derivation input):**
`Δm_target = (M_N_MEV_TARGET − M_P_MEV_CODATA) / (m_e c²) = (939.565420 − 938.272088)/0.51099895 = +2.531 m_e`
(`constants.py:1137-1138`). `2×` band (same sign): `|Δm| ∈ [1.266, 5.062] m_e`.

- **(i) STRUCTURE-SIGNAL.** The composite FS instrument produces a computable split with **correct sign
  (Δm > 0, neutron heavier) AND `|Δm|` within 2× of `2.531 m_e`** (`Δm ∈ [+1.266, +5.062] m_e`), at the
  frozen primary `d=1.0`, warm κ_FS. *Consequence:* the corpus's own composite-FS instrument reproduces
  the split's sign and scale — the tuning hypothesis is made **strictly harder to hold** (NOT: refuted;
  see interpretation-care). The δ_th-loading is then reported as its own separate statement.

- **(ii) WRONG-SIGN.** The composite FS produces `Δm < 0` (proton heavier). *Consequence, frozen verbatim
  from the n–p gate's bin (ii):* **"the ppm precision of the m_p/m_e chain is confirmed a proton-specific
  coincidence — a δ_th tuned to land the proton on CODATA has no reason to produce the correct sign of a
  difference measurement, and it did not. This corroborates the epic-§40 Δ(1232) +2.35% miss
  ('proton-specific tightness = COINCIDENCE')."**

- **(iii) RIGHT-SIGN-WRONG-MAGNITUDE (>2×).** Correct sign (Δm > 0) but `|Δm|` outside the 2× band
  (`< 1.266` or `> 5.062 m_e`), at the frozen primary `d=1.0`, warm κ_FS. *Consequence:* **partial** —
  the composite FS instrument carries the SIGN (canon-forced positive, matching observation) but not the
  SCALE; the 1D-radial proxy for a 3D linking over- or under-predicts the elastic tension. The SIGN and
  the δ_th-LOADING remain the load-bearing observables; the absolute magnitude is instrument-dependent.

- **(iv) BUILD-INSUFFICIENT.** The threading constraint **cannot be expressed in the 1D solver without
  choices BEYOND C1–C5.** *Consequence:* an honest build gap — if, after making C1–C5, a further
  non-enumerable choice is required to emit a number (e.g. the 3D linking has no faithful 1D-radial
  proxy at all), the deliverable is a **verbatim enumeration of the residual choice(s)** and STOP. This
  bin fires only if the build genuinely cannot proceed on C1–C5 alone.

**DISCLOSED LEANING (open to the substrate adjudicating otherwise):** from the substrate-native walk
(rendering (c) at the Ax1-floor `d=1.0`, mapped through `/(1−V·p_c)`), my pre-run leaning is **bin (iii)
RIGHT-SIGN-WRONG-MAGNITUDE** — the sign is canon-forced positive, and the shift-outward elastic term at
the Ax1 thickness floor is expected to *over*-predict the 2× band (the 1D radial spherical measure is a
coarse proxy for the true 3D linking geometry). I freeze the bins and let the composite computation
confirm; if it lands in-band (bin i) or wrong-sign (bin ii), I report that instead — the substrate
adjudicates.

---

## HARD RAILS (binding — value-blind)

1. **No new parameters minted.** Zero constants beyond frozen set A + `M_E` (the `0₁` unknot = 1 m_e) +
   the threading displacement `d` (an Ax1-floor geometric input, `d=1.0 ℓ_node`, not a fitted constant).
   No separate threading-lock coupling constant (C2 folds it into the elastic term).
2. **No refit.** Every consumed constant is imported LIVE from `ave.core.constants`; the driver diffs each
   against an independent frozen HEAD JSON sidecar and aborts on any mismatch (incl. `DELTA_THERMAL` /
   `KAPPA_FS_COLD`, the ablation's focal constants).
3. **No non-enumerated choice.** If the build needs a choice beyond C1–C5 → **bin (iv), enumerate, STOP.**
   No silent choice-making.
4. **Never seed from `1836`, `1.293`, `2.53`, `2.531`, `2.532`, `939.565`, or the CODATA proton ratio**
   inside the computation. These appear ONLY as adjudication-band names (target) and CODATA anchors —
   never as inputs the computation reads. **The displacement `d` and the rendering are NOT tuned to hit
   the target**; `d=1.0` is fixed from Ax1 before the split is computed. The `d`-sweep is disclosed
   characterization, never a selection mechanism.
5. **δ_th ablation runs BOTH κ configurations** for every reported split; a config that emits a single-κ
   split as "the ablation" is a plant the ablation-bypass gate catches.
6. **Freeze-by-push** — this prereg is its own pushed commit before any code.
7. **DO-NOT-MERGE** — PR opens `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`; only Grant merges. No
   derived neutron-mass symbol is canonized into `ave.core.constants` (that is a corpus-state change
   requiring Grant adjudication); Route A lives as a standalone driver, so the n–p gate's live
   corpus-state detector remains clean **by design** (see coordination note).

---

## INTERPRETATION-CARE (frozen BEFORE the run — what each bin does and does NOT establish for δ_th)

- **A bin-(i) magnitude pass at warm-only does NOT certify δ_th's provenance.** It does not convert the
  pre-git-minted, once-re-tuned, single-site δ_th (audit findings R3/R7/R10/R12) into a first-principles
  constant. **The ablation number — `Δm(warm) − Δm(cold)` — is the δ_th statement**, not the warm split.
  A large δ_th-loading means the split's ppm-scale digits ride δ_th (the coincidence reading's exposure);
  a small loading means the split is δ_th-robust (the linear-elastic-route reading). Either way, the
  *level* provenance (the proton m_p/m_e) is untouched; a chord on the difference does not de-tune the level.
- **A bin-(ii)/(iii)/(iv) does NOT falsify the +0.74% bare-topology emergence result.** That result
  (cold `κ_FS=8π` → `1849.70 (+0.7377%)` from integers + imported α) stands independently of δ_th AND of
  the neutron construction. Route A speaks only to the split; nothing about the bare-topology result is touched.
- **The absolute magnitude is the LEAST robust observable.** The 1D radial FS functional is a coarse
  spherically-symmetric proxy for the composite's true 3D linking geometry (the `0₁` threading the cage's
  void is a 3D topological relation the 1D hedgehog cannot fully represent). The **SIGN** (canon-forced
  positive) and the **δ_th-LOADING** (the ablation) are the load-bearing observables; a magnitude miss
  (bin iii) is expected and is a statement about the instrument's coarseness, not a physics falsification
  of the composite ontology.
- **Flag (surfaced, not resolved) — the `/(1−V·p_c)` feedback question.** Whether the elastic surplus
  rides the full regenerative mass-feedback loop (primary reading, `×1.58`) or is a linear-response
  perturbation outside it is a genuine framing fork. It is NOT load-bearing for the bin under the pre-run
  leaning (both sub-readings over-predict the 2× band), so it is surfaced as a flag to Grant/auditor
  rather than blocking the async build; both are reported.

---

## THE INSTRUMENT (what the driver computes — no-refit, fireable)

1. **No-refit reproduction (positive control that CAN fail):** re-derive `PROTON_ELECTRON_RATIO` live and
   assert `= 1836.1170402290593`; assert `solve_scalar_trace(c=5; KAPPA_FS) = I_SCALAR_1D`; diff every
   consumed constant against the frozen HEAD JSON sidecar; abort on any mismatch.
2. **Composite FS leg (the new capability):** compute `I_comp(d)` via the shift-outward rendering (C1) at
   `d=1.0` (C3), same `(r_opt, n)` minimization as the bare solve, at BOTH warm and cold κ_FS (ablation).
3. **Split leg:** emit `Δm` under Reading X and Reading Y (C4), warm and cold, mapped through
   `/(1−V·p_c)`; report the without-feedback alternative separately.
4. **Ablation leg:** emit `Δm(warm) − Δm(cold)` (the δ_th-loading), both readings, at `d=1.0`.
5. **`d`-sweep leg (disclosed robustness):** emit `Δm` at `d ∈ {0.5, 1.0, 1.5, 2.0}` — characterization only.
6. **Bin classifier:** assign the frozen bin from `Δm(warm, d=1.0)` under both readings.
7. **Plant gates (must fire):**
   - a **refit plant** (mutate a consumed constant) trips the no-refit abort;
   - a **seed plant** (inject `1.293`/`2.531`/`939.565`/proton-ratio as a computation input) trips the seed guard;
   - an **ablation-bypass plant** (report a split without both κ configurations) trips the ablation gate;
   - a **d-refit plant** (change the frozen primary `d` away from the Ax1-floor `1.0`) trips a primary-d guard.

---

## COORDINATION — the n–p gate's corpus-state detector (`test_np_mass_split_gate.py`)

The n–p gate wired a detector (`corpus_has_derived_neutron_mass`) and a test
(`test_detector_fires_if_derived_neutron_mass_appears`) designed to **announce exactly this event** — the
moment Route A resurrects the second shot. Per the RESULT doc (`2026-07-13_np-mass-split-gate_RESULT.md:100`,
Route A charter): Route A IS the δ_th second shot the detector was built to flag. **Coordination (this
build):** Route A is a **standalone driver** (`route_a_composite_fs.py`), DO-NOT-MERGE, value-blind; it does
**NOT** canonize a `NEUTRON_ELECTRON_RATIO`/`M_N_MEV_AVE` into `ave.core.constants` (canonization is a
corpus-state change requiring Grant adjudication). So the live detector remains clean **by design** — the
n–p gate's `magnitude_computability_leg` does not raise. The n–p gate test file gets a **dated note**
(2026-07-14) recording that Route A now exists as the derivation the detector was designed to announce, and
that canonization (which would flip the detector) awaits Grant adjudication of Route A's result.

---

## SKILL-SELECTION PLAN (60-sec, pre-workstream)

APPLIED: **substrate-native-check** (the rendering walk above — three candidates against the bare solver;
(c) canon-forced by the positive-surplus requirement; boundary-not-bulk CP10; A1 sector; matched
dimensionless coordinate), **pre-test-physics-check** (the load-bearing framing question — the
`/(1−V·p_c)` feedback fork — surfaced as a flag; the rendering fork resolved by corpus-search per Step 2:
`:25`/`:77`/`:54` force rendering (c)), **ave-prereg** (this doc, freeze-by-push), **verify-before-cite**
(every quote grep-confirmed at base `240d59d8`; constants at file:line), **phase-space-coordinate-check**
(A1 rest-energy in the matched m_e coordinate — no φ² mismatch), **consistency-vs-emergence** (form =
emergence-attempt, magnitude = consistency; the ablation is the δ_th statement — tagged), **ave-canonical-
source** (constants consumed live, diffed against HEAD), **flag-don't-fix** (the feedback fork + the C4
mass-accounting fork surfaced, not resolved). NOT-fired: engine/loop-gap skills (no engine-fire);
Checkpoint-8 emergence-hosting (this is a static eigenvalue, not an autonomous-hosting test).
