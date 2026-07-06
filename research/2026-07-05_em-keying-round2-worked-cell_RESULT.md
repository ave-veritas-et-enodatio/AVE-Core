# EM keying ROUND 2 — the WORKED-CELL keying derivation — RESULT

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/em-keying-round2-worked-cell`
**FROZEN prereg (gated on):** `research/2026-07-05_em-keying-round2-worked-cell_prereg_FROZEN.md`
(freeze commit `e4312c43`, committed before any result — git ordering = freeze proof).
**Drivers (two independent files, sympy + numpy, ReconcileGate, live positive controls):**
- `src/scripts/verify/em_keying_round2_derivation.py` — STEP 0 (net-flux kill) + STEP 1 (worked variable).
- `src/scripts/verify/em_keying_round2_constraints.py` — the seven frozen falsifiers (reuses #539).
**Tests:** `src/tests/test_em_keying_round2_worked_cell.py` (17 fast-core gating + 2 engine_sim: the standing
selected-variance falsifier + the mean-square counterfactual consistency anchor).

## ROUTED BIN: **[SELECTED-NOT-DERIVED]** (sector-split) — the WORKED functional PASSES every falsifier and dissolves the round-1 killer, but the cell equation does NOT fully FORCE the E-side keying over the corpus R2 canon.

> **The sector split (the load-bearing finding):**
> - **B-side (µ-inductor): [WORKED-DERIVED].** Worked-keying is CANON-DERIVED — Lenz forces `A_I` to
>   respond only to `∂_tB`; a static B is not worked → `A_I=0` → `S_µ=1` analytically exact
>   (`node-up-small-large-signal.md`:364, "DERIVED analytically exact").
> - **E-side (ε-varactor): [SELECTED-NOT-DERIVED].** The cell energy ledger FORCES the AC content to
>   engage (frequency-independent), but it does NOT force the DC baseline to be EXCLUDED — the mean
>   kernel deficit `⟨1−S(A_V)⟩` tracks the MEAN-SQUARE (DC-included, `held-DC deficit = 0.046 ≠ 0`),
>   which is the round-1 [C-EXCLUDED] amplitude key. DC-exclusion (variance-keying, blind to a held DC E)
>   requires a NEW ε-side Lenz-dual mechanism the corpus does NOT supply, and it CONTRADICTS the corpus
>   R2 canon (`node-up`:118 "A DC bias is a real operating point"; :217 "a static E … loads ε"). #539
>   [C-EXCLUDED] is empirical evidence the DC-included E-key is falsified at atomic scales.

## WHAT SURVIVES / WHAT IS KILLED

- **The briefed NET-FLUX candidate is DEGENERATE — KILLED at STEP 0 (Grant's orchestrator catch,
  reproduced by sympy).** By Poynting's theorem the closed-surface net flux through a cell equals
  `−dU_cell/dt`, whose cycle-average is ZERO for ANY steady state — the STEADY PUMP as much as the atom's
  steady hidden-momentum loop. `⟨net flux⟩_cycle = −⟨∂_t u⟩_cycle = 0` (sympy). So net-flux keying would
  blind the pump and kill Table I. Eliminated BY DERIVATION, not by selection.
- **The round-1 killer (CRITICAL-1) DISSOLVES — with NO net-vs-local machinery.** Round 1 keyed on the
  LOCAL pointwise `E×H`, which is nonzero for the atom's static proton-dipole H(r) (the 1278× overshoot).
  The WORKED functional keys on the TIME-VARIANCE of the field at the cell. The atom's fields (Coulomb E,
  proton-dipole H) are BOTH STATIC IN TIME → `W = Var_t(E) = 0` IDENTICALLY → `S_E=1` → `δ[ΔE]=0` EXACTLY,
  under the 2.3 µeV CREMA window. **The atom is blind because its fields are static in TIME, not because a
  divergence theorem cancels a circulation** — a cleaner, more robust kill of the round-1 killer than the
  briefed net-flux route (which never worked). Null-verdict liveness (trigger 10): the IDENTICAL pipeline
  fed a TIME-VARYING drive returns `+6.87×10³ µeV` (nonzero) — the zero is physics, not bookkeeping.
- **The boost is lattice-frame-anchored FOR FREE — CRITICAL-2 is MOOT.** A boosted UNIFORM static field
  is CONSTANT at a lattice cell → `Var_t(E)=0` → `W=0` → BLIND. No aliasing story needed (the round-1
  CRITICAL-2 aliasing refutation is moot). Stated plainly as the frame's role, NOT a covariance claim: the
  functional is lattice-frame-anchored by the theory's declared preferred frame; a boosted observer sees
  transformed observables, the vacuum response does not re-key.

## THE FUNCTIONAL (amplitude-CLASS DERIVED; variance MEMBER SELECTED)

$$
\boxed{\; S_E[E(\cdot)] \;=\; \sqrt{1 - c_{\mathcal W}\,\mathcal W}, \qquad
\underbrace{\mathcal W}_{\text{amplitude class: DERIVED}} \;=\;
\underbrace{\mathcal W_{\rm var} \;=\; \frac{\operatorname{Var}_t\big(E\big)}{E_c^2}}_{\text{variance member: SELECTED}}
\;=\; \tfrac12\Big(\tfrac{E_0}{E_c}\Big)^2 \ \text{(for a wave)}, \quad 0 \ \text{(static in time)} \;}
$$

The AMPLITUDE CLASS (over the rate — kills `𝒲_beat`) is **DERIVED** from the LC ledger with NO Table-I
reference (§STEP 1). Within the class `{𝒲_var, 𝒲_ms}` the ledger CANNOT discriminate (identical for
every zero-mean wave); the variance member `𝒲_var` is **SELECTED**, not derived — the only
discriminating input is a held DC, where the kernel deficit tracks the MEAN-SQUARE (§crux, :104-107).

- The keying variable is the TIME-VARIANCE of the field at the cell. STATIC-IN-TIME (bare Coulomb,
  hidden-momentum circulation, boosted uniform static) → `𝒲=0` → BLIND. Cyclically WORKED (pump, standing
  wave) → `𝒲=½(E/E_c)²` → engaged.
- **Sub-bin fork (frozen, decided by STEP 1 at CLASS level only):** `[WORKED-VAR]` (AC-variance,
  frequency-INDEPENDENT) vs `[WORKED-BEAT]` (temporal-gradient `⟨(∂_tE)²⟩/ω_C²`, frequency-SUPPRESSED by
  `(ω/ω_C)²`). STEP 1 DERIVES the AMPLITUDE CLASS (kills `[WORKED-BEAT]`) by the frequency-independence
  of the reactive-energy swing amplitude — NOT by Table-I survival (the round-1 constraint-selection
  lesson). Within the amplitude class, `[WORKED-VAR]` is SELECTED (not derived): the ledger cannot
  discriminate `𝒲_var` from the mean-square `𝒲_ms`; the held-DC input picks mean-square (§crux).
- `c_𝒲` rides the norm fork (§ FORK, carried OPEN): `c_𝒲=1` (NORM-YIELD) or `1/(4π)` (NORM-CLOCK).
- **S_B dual (Route C, consumed by import):** `S_B=√(1−A_I²)`, `A_I=|∮H·dℓ|_norm/I_max`,
  `I_max=124.384 A`. The B-side is ALREADY worked-consistent (Lenz: static B not worked).

## THE DERIVATION CHAIN (STEP 0 sympy; STEP 1 = canon premise + cosine identity; ReconcileGate can-fire proven)

**STEP 0 — net-flux degenerate.** `∮_∂V S·dA = ∫∇·(E×H) = −∫∂_t u`; for `E=E₀cos(ωt)` at a cell,
`⟨∂_t u⟩_cycle = 0` (sympy). Net flux zero for the steady pump too → briefed candidate killed.

**STEP 1 (REQUIREMENT 1) — the loading variable.** The load-bearing content of STEP 1 is the CANON
PREMISE (the kernel keys on the instantaneous `A_V` at the cell; `node-up`:118) PLUS the cosine identity
`Var(E₀cos ωt)=E₀²/2`. From these the AMPLITUDE-CLASS excursion (`¼CV₀²` swing for `V(t)=V₀cos(ωt)`) is
**frequency-INDEPENDENT** below resonance, so the amplitude class is forced over the rate `𝒲_beat`
(freq-suppressed). Evidence:
- PATH A (sympy, the algebraic identity): `Var(E₀cos ωt) = E₀²/2` (freq-independent); `⟨(∂_tE)²⟩/ω_C² =
  (ω/ω_C)²·E₀²/2` (freq-suppressed); `𝒲_beat = (ω/ω_C)²·𝒲_var`.
- PATH B (numpy time-domain — an ILLUSTRATION of the imposed parametrization, NOT independent physics):
  PATH B imposes `E(t)=E₀cos(ωt)` at fixed `E₀` and reads `U_C` from the instantaneous field only (no
  inductor current, no cell ODE), so its ω-independence is a property of the imposed cosine and it CANNOT
  fail. Rows reported only in the quasi-static band `ω/ω_C ≪ 1` the driver declares valid (the `ω/ω_C=1`
  resonance row is DROPPED — beyond quasi-static validity the instantaneous-`U_C` proxy is invalid).
- Independent kernel-deficit route (SHIPPED ARTIFACT, `kernel_deficit_omega_sweep`): the mean kernel
  deficit `⟨1−S(A_V(t))⟩` is IDENTICAL (`0.02289467`, spread `~1e-17`) across `ω/ω_C ∈ {1e-3, 1e-2, 0.1,
  0.5}` (tracks `⟨A_V²⟩/2`, amplitude, NOT `(ω/ω_C)²`, rate).
- **ReconcileGate:** proves the NUMERIC-vs-SYMBOLIC agreement of the ONE variance identity `Var(cos)=½`
  (PATH A symbolic `𝒲_var=½` vs PATH B numpy), `max_rel=0`, `can_fire_proven=True` — a numeric-symbolic
  cross-check of the identity, NOT an independent-physics reconciliation.

**→ LEVEL 1 (DERIVED): the ledger forces the AC-EXCURSION AMPLITUDE CLASS, not the rate (`𝒲_beat`
killed) — DERIVED, with NO reference to Table I. LEVEL 2 (SELECTED): within the amplitude class
`{𝒲_var, 𝒲_ms}` the ledger CANNOT discriminate (identical for every zero-mean wave); the variance
member `𝒲_var` is SELECTED — the held-DC discriminating input picks the mean-square (§crux).**

**STEP 1 CRUX (the load-bearing split, flag-don't-fix).** "AC-excursion amplitude" has two readings that
differ by the DC baseline: the VARIANCE `⟨A_V²⟩−⟨A_V⟩²` (blind to held DC) or the MEAN-SQUARE `⟨A_V²⟩`
(DC-included). **The mean kernel deficit the varactor integrates is `~⟨A_V²⟩/2 = MEAN-SQUARE` at leading
order** — NONZERO for a held DC field (`1−S(0.3)=0.046`). So the kernel-deficit route forces the
MEAN-SQUARE (the round-1 [C-EXCLUDED] key), NOT the variance. For the E-varactor to be worked-keyed (blind
to a held DC E) needs the DC baseline EXCLUDED — which the cell ledger does NOT force and which
CONTRADICTS the corpus R2 canon (verbatim):
> `node-up-small-large-signal.md`:118: *"A DC bias is a real operating point."* ; :217: *"A static $\mathbf E$
> is a real operating-point bias for the $V$-keyed varactor — it loads"* ε ; :40: *"analogous to DC bias on a
> semiconductor varactor"*.

The Lenz DC-blindness that WOULD force worked-keying is the µ-INDUCTOR's property (keyed on `∮H·dℓ` via
`∂_tB`; `tau-relax-derivation.md`:93-97, `node-up`:119-123) — there is **no corpus ε-side Lenz-dual** (a
displacement-current DC-blindness for the varactor). So:
- **B-side:** worked-keying CANON-DERIVED (Lenz). `[WORKED-DERIVED]`.
- **E-side:** worked-keying SELECTED — the ledger forces AC-engagement but not DC-EXCLUSION.
  `[SELECTED-NOT-DERIVED]`.

## THE SEVEN FROZEN CONSTRAINTS (evaluated as-derived; bands; knife armed on all)

| # | constraint | bound + provenance | derived WORKED result | verdict |
|---|---|---|---|---|
| 1 | **MUONIC-H** (physical H(r)) | `<2.3 µeV` CREMA (Pohl 2010) | atom fields STATIC IN TIME → `𝒲_var=0` → `δ[ΔE]=0` EXACTLY; liveness (time-varying drive) = `+6.87e3 µeV` | **PASS under the SELECTED variance keying** (`𝒲_var`: static-in-time → `𝒲=0` exactly). Under the ledger-forced MEAN-SQUARE reading (§crux, :104-107) the muon RE-KILLS the E-key at ~4 OOM: `+1.36e4 µeV` @ `r_cut=1.0·a_µ` (`−2.25e6` @ 0.5a, `+1.93e4` @ 2a) vs the 2.3 µeV CREMA window — reproducing #539 [C-EXCLUDED] |
| 2 | **THE PUMP / Table I** | Letter `−½A²`, `A²=5.9e-7` | `[WORKED-VAR]`: `−½A²` (×1, Table I UNCHANGED, NORM-YIELD tautology); `[WORKED-BEAT]`: `×(ω/ω_C)²=9.2e-12` (~10¹¹ below, Table I COLLAPSES) | class resolved (amplitude over rate) by STEP 1 → BEAT collapses; VAR **selected** within class. The ×1 pump row (VAR/NORM-YIELD) therefore inherits E-side **[SELECTED]** status — as the headline verdict already carries |
| 3 | **PVLAS** (2.5 T ~Hz) | `δn≲5e-23` (Ejlli 2020) | S_B computed `A_I=3.1e-27` → `δn_µ≈0` | consistent (Route C dual) |
| 4 | **BMV** (ms pulse) | `δn≲5e-22` (Cadène) | S_B computed `A_I=1.2e-25` → `δn_µ≈0` | consistent |
| 5 | **DELLIGHT** (Sagnac) | Letter `−¼A²` | `[WORKED-VAR/NORM-YIELD]` = `−¼A²` (tautological, fork open) | consistent |
| 6 | **BOOST** | `A²≈6.7e-23` (v=370km/s, 2.5T) | boosted uniform static = CONSTANT at a lattice cell → `𝒲=0` → BLIND, lattice-frame-anchored (not covariance) | **PASS structurally** (CRITICAL-2 moot) |
| 7 | **[NEW] SLOW-DRIVE** | — | sub-optical time-varying-E middle band (RF/THz, `ω/ω_C~1e-11…1e-8`) has NO facility bound | **OPEN SCALE** (declared, not a free parameter) |

**Constraint 7 (the new honest item).** `𝒲_var` is frequency-INDEPENDENT for any `ω≪ω_C`, so "worked"
engages ANY nonzero AC — the freq-independence extends to arbitrarily slow AC in principle; only true DC
(`ω=0`, permanently held) is blind. The known anchors bracket the gap: the muon probes true-static-E (DC,
R2 held); PVLAS/BMV probe the B-side (static-B, R3, transparent); HIBEF probes the optical pump (worked).
**The MIDDLE E-band (sub-optical time-varying E: RF ~1 GHz → THz) has NO facility bound** — a DECLARED
OPEN SCALE, not a free parameter. A future facility driving a time-varying E in this band that reads NO
birefringence would FALSIFY the freq-independence. Named candidate: high-rep-rate RF/THz
vacuum-birefringence with an AC (not DC) E drive.

## THE COEFFICIENT-NORMALIZATION FORK (carried OPEN — no tautological crowning)

`c_𝒲=1` (NORM-YIELD, Table I unchanged) or `c_𝒲=1/(4π)` (NORM-CLOCK). **NORM-YIELD's "Table I unchanged"
is a TAUTOLOGY** of its definition (NORM-YIELD is DEFINED as the flux that reaches 1 at `E=E_c`), stripped
of any "substrate-consistent" crowning — the round-1 lesson. The fork is FULLY OPEN; the substrate does
not force one over the other. (The geometric factors `1/(4π)`, `1/(8π)` are the `√(8π)` family, CONSISTENCY-
class; the sector-guard test confirms they are NONE of the mechanical Q-point numbers 2/7, 9.7734, √8.)

## THE TWO LEDGERS (frozen [SELECTED-NOT-DERIVED] bin — both costs stated separately)

Per the frozen bin: worked-keying passes every constraint but the E-side is not forced ⟹ it enters as a
POSTULATE for the E-sector. Ledger both costs:
- **(i) For the STANDALONE LETTER** (which postulates its `S(A)=√(1−A²)` kernel anyway): a scoping
  postulate "the E-varactor keys on the AC (worked) content of the field, blind to a held DC E" is
  **admissible Keith-Outcome-B structure** — the Letter already postulates its kernel; one more scoping
  postulate (the keying variable) is within the standalone-Letter's declared postulate budget. The Letter's
  pump-probe is a PROPAGATING wave (worked), so Table I is unchanged under `[WORKED-VAR/NORM-YIELD]`, and
  the muonic-H falsifier PASSES under the Letter's postulated variance kernel (the SELECTED `𝒲_var`
  member; static-in-time → `𝒲=0`). NOTE this PASS is CONDITIONAL on the variance member: under the
  ledger-forced mean-square reading (§crux, :104-107) the muon re-kills the E-key at ~4 OOM (reproducing
  #539); the variance member is SELECTED, not derived. For the Letter, POSTULATING the variance kernel
  is a clean, admissible scoping choice that resolves the round-1 contradiction.
- **(ii) For the AVE CORPUS**: it is an **imported keying awaiting derivation**. The corpus R2 canon says
  the ε-varactor loads on the held DC amplitude (node-up:118,:217); the worked postulate CONTRADICTS this.
  The cost is a NEW ε-side DC-blindness mechanism (a Lenz-dual for displacement current) that must be
  DERIVED before the worked E-keying is corpus-canon. Until then, the corpus carries the tension:
  #539 [C-EXCLUDED] (empirical, DC-included E-key fails at atomic scales) vs R2 (DC-included E-key is
  canon) — the worked postulate resolves it, but by importing an underived keying.

## WHAT A ROUND 3 WOULD NEED (per the frozen [SELECTED-NOT-DERIVED] cost ledger)

Derive the ε-side DC-blindness mechanism from the substrate: is there a displacement-current Lenz-dual
that makes the varactor blind to a held DC E (the exact dual of the µ-inductor's `∂_tB` Lenz blindness)?
If yes, the E-side worked-keying becomes `[WORKED-DERIVED]` and the corpus R2 canon is superseded (KEEP-BOTH
R2′). If no such mechanism exists, the E-varactor genuinely loads on the held DC and the birefringence
E-route is scale-bounded (the muon [C-EXCLUDED] stands, the worked resolution fails for the corpus).

## KNIFE CHECKS (armed)

- **½/¼ derived-only:** the `−½`/`−¼` are the Letter's DERIVED kernel coefficients; MY factors are `1`,
  `1/(4π)`, `1/(8π)` (`√(8π)` family), not new `½`/`¼`. The `𝒲_var=½(E/E_c)²` `½` is the sympy variance
  of a cosine (`Var(cos)=½`), declared-derived, not a tell.
- **ω_C/9-class thresholds:** the physical-H PASSES at `𝒲=0` (static-in-time), NOT at a cutoff — the #539
  `9·ℓ_node` defeat-scale is not reproduced (no cutoff needed).
- **2/7, 9.7734, √8:** sector-guard test PASS (EM worked coefficient is none of these).
- **Suspiciously-exact:** the muon `δ[ΔE]=0` to machine precision is CHECKED for structural degeneracy via
  the live positive control (a time-varying field gives `+6.87e3 µeV`) — the zero is physics (static in
  time → not worked), not a bookkeeping zero for any field.

## PREREG-VS-CODE FIDELITY (ave-prereg 2026-07-05 amendment (a); every FORCED deviation gets its erratum)

Diffed each frozen declaration against the code as shipped:
- STEP 0 / STEP 1 / seven falsifiers / norm-fork-open / boost-lattice-anchored / slow-drive-open-scale —
  all implemented as frozen. ✓
- **ONE FORCED DEVIATION (erratum, disclosed at the moment forced):** the frozen bins §5 anticipated a
  single overall `[WORKED-DERIVED]` if the cell equation forced the worked variable. The derivation FORCED
  a **SECTOR SPLIT** — B-side `[WORKED-DERIVED]` (Lenz canon), E-side `[SELECTED-NOT-DERIVED]` (DC-exclusion
  not forced, contradicts corpus R2). This is WITHIN the frozen bin set (the prereg §1.1 explicitly
  anticipated the `[SELECTED-NOT-DERIVED]` branch: "if the derived 𝒲 cannot be made time-varying-keyed from
  the cell equation → the keying enters only as an assigned postulate"), but the SECTOR-SPLIT nature (B
  derived, E selected — not a uniform verdict) is a refinement the frozen §5 did not spell out. Recorded as
  an erratum here; the routed bin is `[SELECTED-NOT-DERIVED]` (the E-side, the load-bearing sector for the
  Letter + muonic falsifier), with the B-side `[WORKED-DERIVED]` stated alongside.

## SECTOR HEADER + HOMONYM GUARD (honored)

- **EM channel** (ε-varactor / µ-inductor). **NOT the mechanical Q-point sector.** The pilot-field /
  matter-stiffening / channel-resolved results supply a cross-sector MECHANISM precedent (traveling wave
  passes energy through matched cells; held field presses on its cage) — cited for the CLASS only; NO
  number crosses the seam. The matter/radiation stiffening split lives in the MECHANICAL DC channel per
  merged canon (#529/#531/#518); NOT re-litigated here.
- **"A²"/`𝒲` homonym** resolved: (i) Axiom-4 kernel arg, (ii) Letter `(E/E_c)²`, (iii) mechanical bond
  strain, (iv) round-1 transport `𝒯`, (v) MY worked content `𝒲` (`𝒲_var` / `𝒲_beat`) — named distinctly.

## DISCIPLINE

- **Rule 11 honest closure:** no post-hoc criterion drops; the E-side is honestly `[SELECTED-NOT-DERIVED]`,
  not converted to `[WORKED-DERIVED]` by asserting the missing ε-side mechanism. One mechanism (worked =
  time-varying-content engages, static-in-time is blind) explains all the executioner behaviors; the E-side
  DC-exclusion is the one piece the cell ledger does not force — reported, not rescued.
- **Rule 12 substitution-not-retraction:** round 1's [CONSTRAINT-KILLED] is preserved (git); this is a NEW
  derivation with a new prereg + verification chain, NOT a refill of the round-1 slot. The missing ε-side
  Lenz-dual is a NEW round-3 question, not a rescue of round 2.
- **flag-don't-fix:** the corpus R2 (node-up:118,:217, DC-included E-key) vs the worked candidate
  (DC-blind) vs #539 [C-EXCLUDED] (DC-included E-key falsified at atomic scales) contradiction is surfaced
  with verbatim citations; NOT silently reconciled. The corpus edit is the auditor's to land (§ CORPUS).
- **substrate-adjudicates-forks:** the AC-engagement is substrate-forced (the LC ledger); the DC-exclusion
  fork is reported OPEN (needs the ε-side mechanism); the norm fork is reported OPEN. None ruled by fiat.
- **gate the consumed observable (pre-test Trigger 9):** the control measures `Var_t(E)` — the variable the
  mechanism consumes — NOT a proxy. Static-in-time → `𝒲=0`; time-varying → `𝒲>0` (test-asserted).
- **verify-before-cite:** every constant live-derived vs `ave.core.constants` @ worktree HEAD `fc6a2379`;
  muon mass + proton moment declared external CODATA; #539 machinery + Route C reused by import.
- Numeric + symbolic code paths per piece + ReconcileGate (can-fire proven on real paths, derived
  tolerance — it proves the numeric-vs-symbolic agreement of the variance identity, NOT independent
  physics; PATH B imposes the parametrization and cannot fail) + live positive controls; `make verify`
  green; 17 fast-core + 2 engine_sim (selected-variance standing falsifier + mean-square counterfactual
  consistency anchor) all pass.

## CORPUS-STATE UPDATE (surfaced to the auditor lane — NOT landed here)

The auditor lane lands these; I surface the empirical finding:
1. **`node-up-small-large-signal.md`:118,:217 / `pvlas-static-b-verdict.md`** — the R2 statement "a static
   E is a real operating-point bias for the V-keyed varactor — it loads ε" is in TENSION with (a) #539
   [C-EXCLUDED] (the DC-included E-key overshoots CREMA 4-7 OOM at atomic scales) and (b) the worked
   candidate (which needs the DC EXCLUDED). **This is a GENUINE EM-sector conflict, NOT a homonym**
   (adversarial-review adjudication): `node-up`:117-118 pins the statement to the ε-grade / transverse-T2
   permittivity channel — the SAME channel the worked E-key would re-key — so the DC-included vs DC-blind
   readings collide in one sector. **KEEP-BOTH candidate:** the worked-keyed R2′ (E-varactor keys
   on the AC/worked content, blind to held DC E) is admissible for the Letter but needs a NEW ε-side
   Lenz-dual DC-blindness mechanism before it is corpus-canon. Do NOT redefine-in-place; add R2′ alongside
   the legacy amplitude-keyed R2 with the missing-mechanism flag. **(Grant adjudicates the resolution;
   surfaced here, NOT resolved — flag-don't-fix.)**
2. **The missing ε-side Lenz-dual (round-3 question)** — the µ-inductor's `∂_tB` Lenz DC-blindness
   (node-up:364, canon-exact) has NO ε-side dual in the corpus. Whether a displacement-current DC-blindness
   for the varactor can be DERIVED is the load-bearing round-3 question. Surfaced for Grant / the auditor.
