# EM-sector saturation keying — ROUND 2 — the WORKED-CELL keying derivation — PRE-REGISTRATION [FROZEN]

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/em-keying-round2-worked-cell`
**Class:** DERIVATION of the EM-sector constitutive keying variable (derive-or-kill). No claim minted
until the derivation + the SEVEN frozen constraint evaluations complete (six falsifiers + the new
slow-drive/quasi-static boundary item).

**Round 1 is MERGED as [CONSTRAINT-KILLED]** (`research/2026-07-05_em-saturation-keying-functional_RESULT.md`,
PR #542). This round-2 arc is the forward pointer's execution — a NEW derivation, NOT a patch (Rule 12).

## 0. GATES ON (verify-before-cite; grepped live at worktree HEAD `fc6a2379`)

- **Round-1 RESULT + retraction ledger** `research/2026-07-05_em-saturation-keying-functional_RESULT.md`:
  the boxed LOCAL-Poynting functional `S_E=√(1−𝒯)`, `𝒯=(E/E_c)²·[H/(E/Z_0)]`, is [CONSTRAINT-KILLED] on
  the physical atom (CRITICAL-1: proton-dipole H(r) makes the LOCAL pointwise E×H nonzero everywhere;
  overshoot 1278× the 2.3 µeV CREMA window). CRITICAL-2: the aliasing boost story is refuted.
- **Round-1 FROZEN prereg** `research/2026-07-05_em-saturation-keying-functional_prereg_FROZEN.md`:
  the six frozen falsifiers §4; the piece-(a) secular-averaging §A; the T-POYNT/T-BEAT/T-CIRC sub-bins §2b.
- **Standing falsifier (consumed by import, NOT reimplemented):**
  `src/tests/test_em_saturation_keying_functional.py::test_muonic_physical_H_CONSTRAINT_KILLED` +
  `test_physical_atomic_H_is_nonzero_local_poynting`; the physical-H machinery
  `src/scripts/verify/em_saturation_keying_constraints.py` (`H_atomic`, `constraint_1_muonic`); the #539
  bracket-integral `src/scripts/verify/problem3_muonic_lamb_shift.py` (`rho_2s`,`rho_2p`,`_norm`,`A_MU`,`K`,
  `WINDOW_ueV_primary`).
- **The keyed-argument duality (the microfoundation)** `manuscript/ave-kb/vol4/circuit-theory/
  ch1-vacuum-circuit-analysis/node-up-small-large-signal.md`:§1 (LC tank `L=µ₀ℓ`, `C=ε₀ℓ`,
  `ω_C=1/√(LC)=c/ℓ`), :118 (ε-varactor keys on VOLTAGE `A_V=V/V_yield~E`, a *potential/amplitude*
  variable), :119-123 (µ-inductor keys on CIRCULATION `A_I=I/I_max∝∮H·dℓ`, a *rate/flux* variable; static
  B → no dI/dt → A_I=0 → transparent), :125-129 (A46: `A_V`,`A_I` are PHASE-SPACE/reactance coords, NOT
  real-space field magnitudes), :217-221 (R2: "a static E is a real operating-point bias for the V-keyed
  varactor — it loads ε and shifts n"; R3: static B loads nothing, δn_µ=0 EXACTLY).
- **Route C (B-sector dual, MERGED)** `.../relativistic-inductor.md`:15,18; `.../pvlas-static-b-verdict.md`
  (clm-pvlas1); `I_max=ξ_topo·c=124.384 A` (`constants.py`).
- **The cross-sector MECHANISM precedent (cited for the CLASS only; NO number crosses the EM/mechanical
  seam)** `research/2026-07-05_pilot-field-comoving-companion_result.md`: a launched traveling wavetrain
  PASSES energy through matched cells (momentum conserved on the closed ring, Σp_long≈8e-16); the 2nd-order
  mean it deposits is a BUILT response, not an instantaneous deposit — "traveling waves pass energy through
  matched cells without depositing; held bows press on their cage." MECHANICAL sector (translational-u
  elastic, both k_a/k_s capacitive); NOT the ε/µ photon pair.
- The Letter `papers/2026_birefringence_letter/main.tex` (v2).

---

## 0.1 ORCHESTRATOR PHYSICAL-PICTURE CORRECTION (recorded VERBATIM before the freeze; Grant's walk)

The orchestrator relayed a Grant-walked correction to the candidate BEFORE this prereg was frozen. It
is recorded here verbatim; it binds the derivation. It changes the candidate materially — the briefed
net-flux candidate is DEGENERATE and dies on the first derivation line; the surviving candidate is the
WORKED-CELL variable.

> **THE NET-FLUX CANDIDATE AS BRIEFED IS DEGENERATE.** By Poynting's theorem, the closed-surface net
> flux through a cell equals dU_cell/dt, which is ZERO for every steady state — the atom's
> hidden-momentum loop AND the steady pump beam alike (power in one face = power out the other). So
> net-closed-surface keying would blind the pump and kill Table I: it cannot be the engagement variable.
> Verify this degeneracy explicitly as your first derivation step (it is a one-line Poynting identity) —
> it eliminates the briefed candidate honestly rather than silently.
>
> **THE SURVIVING PHYSICAL CANDIDATE (Grant's walk; derive-or-kill, do not assume):** the cell responds
> to being WORKED, not held and not passed-through — the keying variable is the CYCLIC DRIVE AMPLITUDE at
> the cell (the amplitude of the time-VARYING field content; the energy sloshing between the cell's C and
> L per cycle). Executioner behavior to DERIVE: bare Coulomb — fields constant at the cell, nothing
> moves, blind; hidden-momentum circulation — flux passes through but the fields at the cell are STATIC
> in time, nothing moves, blind (the round-1 killer dissolves with no net-vs-local machinery); pump —
> cell driven at ω amplitude A, engaged, coefficient vs the Letter's −½A² computed honestly; boosted
> uniform static — constant at a lattice cell, blind, lattice-frame-anchored for free; standing wave —
> cells ARE cyclically worked (consistent with the Letter's own pump mechanism and node-up's ¼A²; the
> matter/radiation split lives in the MECHANICAL channel per merged canon — state the sector split, do
> not re-litigate it).
>
> **REQUIREMENT 1 UNCHANGED IN SPIRIT:** derive from the cell's own equations WHAT the loading variable
> is — if the network dynamics force the cyclic-working variable, that is the derived answer; if they
> force something else, follow the substrate. The physical-H atom falsifier, the six constraint-
> falsifiers, the open norm fork, and all round-1 lessons stand exactly as briefed.
>
> **ONE NEW HONEST ITEM for your constraint table: the slow-drive limit.** "Worked" needs its
> quasi-static boundary stated (a field re-aimed over seconds does not ring a 10⁻²¹-s cell). State what,
> if anything, experimentally constrains the E-sector's middle band between DC and optical; if nothing
> does, say so plainly (an unconstrained crossover is a declared open scale, not a free parameter to hide).

---

## 0.2 SECTOR HEADER (mandatory)

- **Which sector?** The EM channel: the vacuum LC tank's ε-grade (VARACTOR, transverse-T2 permittivity)
  and µ-grade (relativistic INDUCTOR, Cosserat-B). The ε/µ EM sector.
- **NOT the mechanical Q-point sector.** The bond-strain / ρ_eff / transverse-tangent-stiffness canon
  (pilot-field `..._pilot-field-comoving-companion_result.md`; matter-stiffening #518; channel-resolved
  #524) is a DIFFERENT sector (translational-elastic bond springs). It supplies a cross-sector MECHANISM
  precedent (traveling wave passes energy through; held field presses on its cage) — cited for the CLASS
  only; NO number crosses the EM/mechanical seam. **The matter/radiation stiffening split lives in the
  MECHANICAL DC channel per merged canon (#529/#531/#518) — this arc does NOT re-litigate it; the "hum is
  not the stiffening carrier" is stated as a sector fact, not re-derived here.**
- **Cold vs saturated?** Deep-cold vacuum, small-signal about a large-signal operating point set by the
  drive (pump `A²~6e-7`; muon static field `A²~0.025`). DOF the engine carries: the FDTD ε/µ reactances,
  the Axiom-4 kernel `S(A)=√(1−A²)`, the node clock `ω_C=c/ℓ_node`.
- **Homonym guard.** "A²" is overloaded: (i) Axiom-4 kernel argument (a phase-space reactance coordinate,
  A46), (ii) the Letter's `(E/E_c)²` field-amplitude ratio, (iii) mechanical bond strain, (iv) the ROUND-1
  transport content `𝒯`. This round's derived keying variable is a FIFTH object — the WORKED content
  `𝒲` (the amplitude of the TIME-VARYING field content at a cell) — named `𝒲` throughout, its relation
  to each "A²" stated explicitly. The two candidate MEASURES of `𝒲` are named `𝒲_var` (AC-variance) and
  `𝒲_beat` (temporal-gradient / T-BEAT).
- **Phase-space coordinate discipline (A46).** `A_V`,`A_I` are phase-space/reactance coordinates. The
  WORKED variable is a real-space, per-cell TIME-DOMAIN quantity; its map into the kernel engagement
  coordinate (the phase-space arc) is DERIVED and stated explicitly. The physical-H falsifier is itself a
  real-space local-in-time claim (is the field at the cell time-varying?), so it is A46-clean.

## 0.3 PRE-TEST PHYSICS CHECK — the plumber question (fired; recorded; fork converted to computable)

Fired `pre-test-physics-check` (trigger 1 pre-reg freeze; trigger 6 draft-moment; trigger 8 dispatch
ontology — the candidate's noun changed from "net transport" to "worked"; trigger 9 fork-to-computable;
trigger 10 null-verdict liveness — the atom-blind verdict is a NULL that needs a positive control). The
top-level ontology ("worked, not held, not passed-through") is Grant-supplied and recorded §0.1. The
residual fork the candidate itself leaves OPEN is converted to a COMPUTABLE DISCRIMINATOR, not pressed
for fiat (trigger 9; Grant's demonstrated preference (b) — "engine tells us, not fiat"):

> **Plumber question (surfaced, recorded):** Of the two measures of "the cell is being worked" that both
> vanish for a held field and are both nonzero for a wave — the AC-VARIANCE of the field content
> `𝒲_var = ⟨E²⟩−⟨E⟩²` (frequency-INDEPENDENT; the amplitude of what sloshes) versus the TEMPORAL-GRADIENT
> content `𝒲_beat = ⟨(∂_tE)²⟩/ω_C²` (frequency-SUPPRESSED by `(ω/ω_C)²`; the rate of sloshing) — which one
> does the LC cell's own energy-exchange equation load on? They agree up to a kinematic `ω²` factor for a
> co-moving wave (`𝒲_beat = (ω/ω_C)²·𝒲_var`) but give OPPOSITE Table-I fates: `𝒲_var` engages the pump
> fully (Table I survives); `𝒲_beat` collapses the pump by `(ω_pump/ω_C)² ≈ 9×10⁻¹²`. Round 1 eliminated
> `𝒲_beat` (as "T-BEAT") BY TABLE-I SURVIVAL — a constraint-selection the round-1 retraction flagged as
> not-a-derivation. This round DERIVES which measure the cell's equation forces, and lets the substrate
> adjudicate; NEITHER is selected against Table I.

The freeze protects the derivation regardless of the fork's resolution. Both measures are carried as
frozen sub-bins `[WORKED-VAR]` / `[WORKED-BEAT]`; the routed one is whichever the cell equation forces.

---

## 1. THE DERIVATION (the five round-1 requirements + the new slow-drive item; every step sympy)

### STEP 0 (mandatory FIRST line) — kill the briefed net-flux candidate by the Poynting identity

Show, by the one-line Poynting identity, that the closed-surface net flux through a cell equals
`−dU_cell/dt`, whose time-average is ZERO for ANY steady state — so the briefed net-flux candidate blinds
the STEADY PUMP as well as the atom and kills Table I. This ELIMINATES the briefed candidate BY
DERIVATION (not by selection). sympy: `∮_∂V S·dA = ∫∇·(E×H) = −∫∂_t u`; for `E=E₀cos(ωt)` at a cell,
`⟨∂_t u⟩_cycle = 0`. (Prereg-time dimensional/analytic check done: `⟨dU/dt⟩=0` confirmed; `𝒲_var=E₀²/2`,
`𝒲_beat=(ω/ω_C)²E₀²/2`, `𝒲_beat=ω²·𝒲_var`.)

### STEP 1 (REQUIREMENT 1) — DERIVE the loading variable from the cell's own equations (NOT select it)

The honest route (round-1 requirement 1, unchanged in spirit): work the energy bookkeeping of a single
LC cell. `U_cell = ½C V² + ½L I²`; the varactor keys on `A_V=V/V_yield` (node-up:118, the VOLTAGE — a
potential/amplitude variable), the inductor on `A_I=I/I_max` (node-up:119, the CURRENT/circulation). The
question requirement 1 forces: what physically drives the varactor toward its rail —
- **(H1) the stored-energy EXCURSION** the cell undergoes per cycle (the AC-variance `𝒲_var` of the
  reactive-energy sloshing between C and L — Grant's "energy sloshing between C and L per cycle"), OR
- **(H2) the temporal-gradient content** `𝒲_beat` (the RATE of change, the round-1 T-BEAT), OR
- **(H3) the held amplitude** `A_V=|E|` (the corpus R2 canon, node-up:217 — the round-1 [C-EXCLUDED] key), OR
- something else the substrate forces.

Derive it from the LC energy-exchange equation, sympy, TWO independent code paths (a symbolic LC-cycle
energy ledger; a numpy time-domain cell driven at ω, reading what its kernel-argument excursion integrates
to). If the derivation lands on `𝒲_var` → the candidate is derived AND Table I survives. If it lands on
`𝒲_beat` → follow the substrate and report the Table-I collapse honestly (the pump-suppression is then a
real prediction, banded against the slow-drive item §4-7). If it lands on `𝒲=A_V` (held amplitude) → the
round-1 [C-EXCLUDED] failure recurs and we route [CONSTRAINT-KILLED] again. **No selection against Table
I; the cell equation decides.** The load-bearing distinction from the corpus R2 canon (which says the
varactor loads on the HELD voltage amplitude, node-up:217) is surfaced as the load-bearing tension §1.1.

### STEP 2 (REQUIREMENT 2) — the physical-H atom falsifier STANDS, must pass BY DERIVATION

Evaluate the DERIVED `𝒲`-keyed functional on the REAL atomic configuration (proton dipole H(r) + the
static Coulomb E(r), the round-1 machinery consumed by import). **The derived readout is a TIME-DOMAIN
quantity: is the field at the cell varying in TIME?** For the atom, the proton-dipole field and the
Coulomb field are BOTH STATIC IN TIME (a permanent moment, a fixed charge) — so `∂_t E = 0` and
`⟨E²⟩−⟨E⟩² = 0` at every cell, IDENTICALLY, for BOTH `𝒲_var` and `𝒲_beat`. **The atom is blind with NO
net-vs-local machinery: it is blind because its fields are static in TIME, not because a divergence
theorem cancels a circulation.** This is the round-1 killer dissolving cleanly — show the identity
(`𝒲(static-in-time)=0`) through the SAME #539 bracket-integral pipeline that routed round-1 [C-EXCLUDED]
and CRITICAL-1, and show the level shift `δ[ΔE]=0` EXACTLY, under the 2.3 µeV CREMA window. **Positive
control (null-verdict liveness, trigger 10):** feed the IDENTICAL pipeline a TIME-VARYING field (an
optical-band drive at the cell) and show `δ[ΔE]≠0`, proving the zero is physics (static-in-time → not
worked), not a bookkeeping zero for any field.

### STEP 3 (REQUIREMENT 3) — pump engagement recomputed under the DERIVED keying

Net worked-content through a cell for the BIREF pump-probe geometry (a focused traveling optical pulse):
the cell IS cyclically worked at the pump ω. Compute the engagement coefficient vs the Letter's `−½A²`,
honestly banded, under BOTH sub-bins:
- `[WORKED-VAR]`: `𝒲_var = ½(E/E_c)²` (frequency-independent) → engages FULLY → Table I survives (the
  same value the Letter uses, up to the peak-vs-cycle-average factor 2 convention flagged round-1).
- `[WORKED-BEAT]`: `𝒲_beat = ½(ω/ω_C)²(E/E_c)²` → suppressed by `(ω_pump/ω_C)²≈9.2×10⁻¹²` → Table I
  collapses by that factor (the pump birefringence is then predicted ~10¹¹× BELOW the Letter — a stark,
  honestly-banded consequence stated, not hidden).
The Table-I consequence is stated under the OPEN norm fork (BOTH arms, no crowning — the round-1
tautology lesson: NORM-YIELD's "Table I unchanged" is a tautology of its own definition).

### STEP 4 (REQUIREMENT 4) — the norm fork carried OPEN

No "substrate-consistent" preference for NORM-YIELD vs NORM-CLOCK without a derivation that forces it. Both
`c_𝒲=1` (NORM-YIELD) and `c_𝒲=1/(4π)` (NORM-CLOCK) reported; the coefficient rides the node-power
normalization. (Moot if the derivation lands [WORKED-BEAT] — the `(ω/ω_C)²` collapse dwarfs the `4π`.)

### STEP 5 (REQUIREMENT 5) — NO constraint-selected eliminations

Every alternative invariant is eliminated BY DERIVATION or carried as an OPEN alternative. The knife is
armed on ALL the frozen falsifiers as VISIBLE TARGETS (muon window, Table-I anchored values, PVLAS/BMV/
DeLLight bounds, the boost). The AC-variance-vs-T-BEAT fork is decided by the cell equation, NOT by
Table-I survival.

### 1.1 THE LOAD-BEARING TENSION THIS DERIVATION MUST ADJUDICATE (flag-don't-fix)

The corpus R2 canon (node-up:217, verbatim): *"A static E is a real operating-point bias for the V-keyed
varactor — it loads ε and shifts n"* — i.e. the ε-varactor loads on the HELD voltage amplitude `A_V=|E|`.
This is the SAME held-amplitude key that #539 routed [C-EXCLUDED] at atomic scales and that CRITICAL-1
confirmed overshoots by 10³×. Grant's WORKED candidate says the varactor loads on the CYCLIC (time-varying)
content, NOT the held amplitude — which CONTRADICTS node-up:217 for a static field. **This prereg does NOT
silently pick a side.** It derives the loading variable from the cell equation and lets the result
adjudicate:
- If the derived `𝒲` is time-varying-keyed AND clears muonic-H AND fires on the pump → the corpus R2
  "static E loads ε on |E|" statement is SUPERSEDED (surfaced to the auditor lane; the KB leaf is the
  auditor's to land, KEEP-BOTH candidate: a WORKED-keyed R2′ alongside the legacy amplitude-keyed R2).
- If the derived `𝒲` cannot be made time-varying-keyed from the cell equation → the keying enters only as
  an assigned postulate; ledger the cost ([SELECTED-NOT-DERIVED] or [CONSTRAINT-KILLED]).

## 2. THE DUAL S_B (Route C, MERGED — consumed, not re-derived)

`S_B=√(1−A_I²)`, `A_I=|∮H·dℓ|_norm/I_max`, `I_max=ξ_topo·c=124.384 A`. Static B → ∇×H=0 → I_cell=0 →
A_I=0 → S_B=1 (transparent, clm-pvlas1). **The B-side is ALREADY worked-consistent:** the µ-inductor keys
on CIRCULATION induced by `∂_tB` (node-up:119-123, Lenz) — a static B is not worked (no dI/dt), exactly as
a static E is not worked. So the E-side WORKED candidate makes the E and B sides DUALS under the same
"worked = time-varying content engages, held is blind" structure. Demonstrate the duality (both blind for
static, both keyed for time-varying), OR report its failure. **Blocker-B lesson (VCA-R01):** the worked
variable must be a bounded cycle-averaged envelope quantity, NOT a pointwise ratio that diverges at
zero-crossings — `𝒲_var`,`𝒲_beat` are both cycle-averaged and bounded (checked).

## 3. FROZEN CONSTANTS (verify-before-cite, live @ worktree HEAD `fc6a2379`)

- `ω_C = c/ℓ_node = 7.76344071105011e20 rad/s`; `ℏω_C = m_ec² = 8.187105776823886e-14 J` (ratio 1.0 exact).
- `ℓ_node = 3.8615926772e-13 m`; `E_c = E_YIELD = √α·E_crit = 1.1304105713e17 V/m`.
- `I_max = ξ_topo·c = 124.3840330669 A`; `Z_0 = 376.730… Ω = 1/(cε₀)`.
- `ω_pump(1.55 eV)/ω_C = 3.0332743e-6` → `(ω_pump/ω_C)² = 9.20e-12` (the T-BEAT pump-suppression factor).
- `ω_probe(10 keV)/ω_C = 0.0195695`.
- Muon: `m_µ/m_e = 206.7682830` (CODATA 2018, EXTERNAL); `a_µ = 284.75 fm` (#539); proton moment
  `µ_p=2.7928473446 µ_N` (CODATA 2018, EXTERNAL).
- CREMA window: `202.3706(23) meV`; 1σ = 2.3 µeV (primary), 10 µeV (loose).

## 4. THE SEVEN FROZEN CONSTRAINT FALSIFIERS (knife armed on ALL; NO parameter chosen to satisfy them)

The DERIVED functional (with its DERIVED coefficient, not tuned) is EVALUATED against each. Bands. Each is
a NAMED VISIBLE TARGET with its bound + provenance (the constraint-falsifier pattern, ave-prereg
2026-07-05 amendment).

1. **MUONIC-H** — bound: `|δ[ΔE]| < 2.3 µeV` (CREMA 2010, Pohl et al., primary 1σ; 10 µeV loose).
   Provenance: `problem3_muonic_lamb_shift.py` WINDOW_ueV_primary. Evaluate the DERIVED `𝒲`-keyed
   functional on the PHYSICAL atom (proton dipole H(r) + Coulomb E(r), BOTH static-in-time) via the #539
   bracket integral. `𝒲=0` for a static-in-time field (both measures) ⟹ `δ[ΔE]=0` EXACTLY. **Must pass BY
   DERIVATION** (the identity `𝒲(∂_t=0)=0`). The round-1 [CONSTRAINT-KILLED] recurs ONLY if the derived
   `𝒲` is somehow nonzero for a static-in-time field — checked.
2. **THE PUMP / TABLE I** — bound: the Letter's `δn_bir=−½A²`, `A²(pump)=5.9e-7` (1e21 W/cm², BIREF@HIBEF).
   Provenance: `main.tex` Table I; round-1 `constraint_2_pump`. Report the DERIVED coefficient vs `−½A²`
   under BOTH sub-bins (`[WORKED-VAR]`: ×1; `[WORKED-BEAT]`: ×`(ω/ω_C)²`) and BOTH norm arms. Table-I
   consequence stated under the open fork, NO crowning.
3. **PVLAS** — bound: `δn ≲ 5e-23` (Ejlli 2020, 2.5 T rotating ~Hz). Provenance: `pvlas-static-b-verdict.md`
   clm-pvlas1; round-1 `constraint_3_4_magnetic`. Evaluate S_B (Route C, computed A_I from physical dB/dt,
   NOT a hardcoded zero). A quasi-static B → A_I→0 → δn_µ≈0. Report the computed number.
4. **BMV** — bound: `δn ≲ 5e-22` (Cadène/BMV, ms pulse, large ∂B/∂t). Provenance: same leaf. Same S_B path.
5. **DELLIGHT** — bound: Sagnac common-mode sensitivity (Robertson 2021). Provenance: round-1
   `constraint_5_dellight`. Derived `𝒲`-keyed common-mode `δn_iso≈−¼𝒲` at a focused propagating pump
   (worked) — report vs the Letter's `−¼A²`, under the open fork (the NORM-YIELD match is tautological).
6. **BOOST** — bound: motional `E=vB` at CMB boost (`v=370 km/s`, 2.5 T → `A²≈6.7e-23`, matches the
   Letter ~7e-23, `main.tex:305-312`). Provenance: round-1 `constraint_6_boost`. **State plainly as the
   frame's role, NOT a covariance claim:** the functional is LATTICE-FRAME-ANCHORED (the theory's declared
   preferred frame). A boosted UNIFORM static field is CONSTANT at a lattice cell → `∂_t E=0` at the cell
   → `𝒲=0` → blind, lattice-frame-anchored FOR FREE (no aliasing story needed — CRITICAL-2's aliasing
   refutation is thereby MOOT, replaced by the clean "constant-at-a-cell → not worked" statement). A
   boosted observer sees transformed observables; the vacuum response does not re-key.
7. **[NEW] SLOW-DRIVE / QUASI-STATIC BOUNDARY** — bound: to be STATED, not fit. "Worked" needs its
   quasi-static limit stated: a field re-aimed over seconds does not ring a `T_C=2π/ω_C≈8×10⁻²¹ s` cell.
   Compute the crossover: `𝒲_var` is frequency-independent (any nonzero ω engages) — but the SMALL-SIGNAL
   kernel deficit is `~𝒲` and the DERIVED coefficient may carry an `(ω/ω_C)` factor from the cell response
   time. State what constrains the E-sector MIDDLE band between DC (muon/PVLAS static) and optical (pump):
   if NO experiment constrains the sub-optical worked-E band, say so PLAINLY — a declared OPEN SCALE, not
   a free parameter. Enumerate the known anchors (DC: muon static, PVLAS static-B; optical: HIBEF pump) and
   the GAP between them; name any facility (RF, THz, static-field-with-AC-modulation) that would probe it.

## 5. BINS (FROZEN verbatim; routed with no post-hoc criterion drops, Rule 11)

- **[NET-TRANSPORT-DERIVED]** — RETIRED at STEP 0: the net-transport (closed-surface flux) candidate is
  DEGENERATE (Poynting: `⟨net flux⟩=−⟨dU/dt⟩=0` for every steady state — blinds the pump too). This bin
  cannot be routed positively; it is retained only as the record of the briefed candidate's honest death.
  (Referential-integrity note, ave-prereg Step 3.6: no falsifier routes INTO this bin as a positive; the
  net-flux path is eliminated at STEP 0, upstream of the falsifier table.)
- **[WORKED-DERIVED]** — the cell's energy-exchange equation FORCES the worked variable (AC-variance
  `𝒲_var` OR temporal-gradient `𝒲_beat`, whichever the equation forces); the physical-H atom passes BY
  DERIVATION (static-in-time → `𝒲=0`); all seven falsifiers pass/banded by derivation; Table-I consequence
  quantified under the open norm fork AND the open `𝒲_var`/`𝒲_beat` sub-fork if it is not resolved.
  - sub-bin `[WORKED-VAR]`: the equation forces `𝒲_var` (frequency-independent, Table I survives).
  - sub-bin `[WORKED-BEAT]`: the equation forces `𝒲_beat` (frequency-suppressed, Table I collapses by
    `(ω/ω_C)²`; the pump-suppression is a REAL banded prediction, not a failure to hide).
- **[SELECTED-NOT-DERIVED]** — worked-keying passes every constraint but the cell equation cannot FORCE it
  over the alternatives (`𝒲_var` vs `𝒲_beat` vs held-`A_V`) ⟹ it enters as a POSTULATE. **Ledger both
  costs separately:** (i) for the STANDALONE LETTER (which postulates its kernel anyway) a scoping
  postulate is admissible Keith-Outcome-B structure; (ii) for the AVE CORPUS it is an imported keying
  awaiting derivation — state both ledgers.
- **[CONSTRAINT-KILLED]** — the derived/candidate functional FAILS a falsifier (e.g. the derived `𝒲` is
  nonzero for a static-in-time atom, recurring round-1's kill; or the pump collapses AND that is falsified
  by a middle-band bound) ⟹ round 2 dies honestly; name the single mechanism; report what a round 3 needs.
  Do NOT refill the slot (Rule 12).
- **[UNDERDETERMINED]** — name the missing structure (e.g. the slow-drive crossover coefficient is
  unconstrained and no experiment bounds the middle band ⟹ the E-sector worked band is a declared open
  scale).

**Knife (armed):** ½/¼ derived-only (the Letter's −½/−¼ are DERIVED kernel coefficients; any NEW ½/¼ in
MY coefficient must be sympy-traced); ω_C/9-class thresholds (the #539 `9·ℓ_node` muonic floor is a
computed defeat-scale, not to be reproduced coincidentally); 2/7, 9.7734, √8 (mechanical-Q-point sector
numbers — must NOT appear in the EM coefficient; a cross-wire flag if they do). Any constraint satisfied
SUSPICIOUSLY EXACTLY (`δ[ΔE]=0` to machine precision) is CHECKED for structural degeneracy via the live
positive control (a time-varying field gives nonzero — the null-verdict-liveness check, trigger 10). The
`𝒲_var`-vs-`𝒲_beat` fork is decided by the cell equation, NOT by Table-I survival (the round-1 lesson).

## 6. DISCIPLINE STACK

Prereg FROZEN before results (this doc; the orchestrator correction + Grant's walk verbatim §0.1);
skeleton-first then one section per commit; sympy on every analytical step; independent code paths for
numerics (derive-then-confirm, ReconcileGate with can-fire-proven on REAL paths, derived tolerances); NO
self-verifying controls; gate the CONSUMED observable (pre-test Trigger 9: the control measures the
variable the mechanism consumes — here `∂_t E` at the cell, NOT a proxy); consume merged machinery by
import (#539 evaluator, Route C constants, the Axiom-4 kernel); magnitudes as bands; quote-audit;
homonym guard (§0.2 "A²"/`𝒲`); sector split (§0.2); pure-corpus; `make verify` green; tests split (fast
core + engine_sim) INCLUDING the standing physical-H falsifier consuming MY `𝒲` functional; prereg-vs-code
fidelity — any FORCED deviation gets its erratum banner AT the moment it is forced (ave-prereg 2026-07-05
amendment (a)); PR titled with the routed bin, `[REVIEW: pending-orchestrator]`, NO SELF-MERGE.

## 7. DIMENSIONAL / MAGNITUDE PRE-CHECK (ave-prereg Step 3.5 — done at freeze)

- `𝒲_var(wave) = ⟨E²⟩−⟨E⟩² = E₀²/2` (sympy-confirmed at freeze). Dimensionless in `(E/E_c)²` units:
  `𝒲_var = ½(E/E_c)²`. Frequency-INDEPENDENT.
- `𝒲_beat(wave) = ⟨(∂_tE)²⟩/ω_C² = ½(ω/ω_C)²(E/E_c)²` (sympy-confirmed). `𝒲_beat = ω²·𝒲_var` (in field
  units), i.e. `𝒲_beat/𝒲_var = (ω/ω_C)²`. At the pump `(ω_pump/ω_C)² = 9.20×10⁻¹²`.
- `⟨∂_t u⟩_cycle = 0` (sympy-confirmed) ⟹ the net-flux candidate is degenerate (STEP 0). No dimensional
  surprise: net flux `~ dU/dt`, cyclic-average zero for any steady state.
- The pump Table-I consequence bands: `[WORKED-VAR]` → ×1 (unchanged); `[WORKED-BEAT]` → ×`9.2×10⁻¹²` on
  δn (or ×`(9.2e-12)²` on P_flip). These two bands are frozen as the discriminating outcomes.

---
**FROZEN.** Any change below this line after the first result commit is an ERRATA BANNER ONLY (the body is
a record). The freeze act is this commit; the derivation fires on it.
