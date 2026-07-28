# Continuum radial-acoustic solver — STAGE 1 FROZEN pre-registration (INSTRUMENT CERTIFICATION ONLY; banks no physics verdict)

**Date:** 2026-07-28
**Class:** INSTRUMENT-CERTIFICATION pre-registration (research-doc; **forms derived, values dimensionless/geometric; mints no `clm-`/`def-`; propagates to no KB/tex leaf; banks NO physics verdict**). This is COMMIT 1 — the pre-registration ALONE, frozen and pushed before any solver code (the #761/#767/#770/#775/#782/#792 frozen-first discipline).
**Charter:** `research/2026-07-21_continuum-radial-solver_CHARTER.md` (merged #789). The charter is the contract; this prereg operationalizes its §5 requirements into pass/fail gates for **stage 1 only**.
**Result-doc pointer requirement (machine-checkable frozen-provenance convention, gate LIVE since 2026-07-22).** The result doc that resolves this certification MUST carry a machine-readable pointer line `Prereg-file: research/2026-07-28_continuum-radial-solver-stage1_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file (`manuscript/ave-kb/tools/verify-frozen-provenance.py`). Every frozen criterion below is written as an inline-code `` `quoted token` `` for exactly that byte-match.
**Provenance:** Grant ruled the charter's §0 open decisions 2026-07-28 (verbatim `[sic]`: *"D2: disclosed, D3: follow rec, D4: do it, D5: do the rec"*). **D1 REMAINS HELD** — Grant is walking the sector-crossed `c²`; stage 1 is therefore built and certified **D1-INDEPENDENT** (§10).
**Lane fences:** DERIVATION / instrument lane only. Engine `src/ave` **BYTE-UNTOUCHED** (imports read-only; the whole instrument lives in `research/drivers/`). **No** `manuscript/` or `manuscript/ave-kb/` `.tex`/`.md` leaf edits; **no** port-register edit; **no** falsification-ledger edit; **no** charter edit — regardless of outcome. Consequences ROUTED to Grant / the auditor lane only.

> **FREEZE STATEMENT.** This document freezes: (i) the stage-1 scope carve — what certification IS and what it explicitly is NOT (§1); (ii) the ruled formulation + the orthotropic radial channel + the two solvers (§2); (iii) the stage-1 import-ledger delta on top of the charter's I1–I10 (§3); (iv) the D5 measured-profile input path + its disclosed gap (§4); (v) the NINE validation gates G1–G9 with FROZEN NUMERIC TOLERANCES (§5); (vi) the FOUR gate-fireability self-tests FT-1…FT-4, each of which MUST FIRE (§6); (vii) the R6 artifact controls adapted to the continuum (§7); (viii) the EXHAUSTIVE outcome classes with a reachability argument for each (§8); (ix) the mutual-satisfiability proof of the frozen requirements (§9 — the Protocol-E lesson); (x) the symbolic-`c²` discipline + the R2 two-term separable reporting contract (§10); (xi) the ledger tags + the owed-follow-ons fence (§11). Nothing below §11 is a result. **The certification verdict may cite ONLY the frozen criteria's outputs, read from the shipped `continuum_radial_solver_stage1_results.json` via the deterministic driver — NO prose-string conclusions (the #770 lesson).**

---

## §0 — The RULINGS consumed + REGIME / SECTOR / PHASE-STATE header + the substrate-native walk

**★THE RULINGS (Grant, 2026-07-28, verbatim `[sic]`: `"D2: disclosed, D3: follow rec, D4: do it, D5: do the rec"`), stage-1 reading:**

| # | Charter question | Ruling | How stage 1 consumes it |
|---|---|---|---|
| **D1** | which sector's `c²` divides `E_trapped` (`c_P` / `c_S` / `c_EM`) | **HELD — Grant is walking it** | stage 1 is built + certified **D1-INDEPENDENT**: no gate consumes a `c²` choice; the trapped-energy column is carried SYMBOLICALLY with its `c²` label exposed (§10). No default (`c_light`, or an unlabeled `c`) is admissible — R8. |
| **D2** | import `β` as a disclosed scan, or hold it symbolic | **DISCLOSED SWEEP** — `β ∈ {0, 1, 3}` per the #782 companion | every trapped-energy output is a FAMILY over the frozen sweep, never a single number; the magnitude stays OPEN (`clm-m5swh9`). |
| **D3** | solver formulation | **the charter's recommendation: T1 (a) + (c)** | frequency-domain **transfer-matrix PRIMARY** (no CFL floor at `k·r_core ≪ 1`) **+ analytic matched-asymptotics BACKSTOP** (§2). Time-domain FDTD (T1 (b)) is NOT built. |
| **D4** | run stage 1 pre-walk, or wait | **BUILD NOW** | certification on **profile-independent** gates; **stage 1 banks NO physics verdict** and every output says so (§1, §8). |
| **D5** | the vessel-state remap evaluation input | **feed the MEASURED profile** (#796) | the R1 orthotropic profile is built from the numbers shipped in `research/drivers/vessel_state_rve_results.json`, read programmatically — never retyped from prose (§4). |

**SECTOR.** **A1 — dilatation / compression** (the bulk `∇·u` channel, the P-branch). The instrument's channel is the spherically-symmetric (`n = 0`, monopole) radial displacement `u_r(r)`. **Sector-ownership discipline (do NOT cross-wire):** A1 owns compression/mass/dilatation; T2 owns shear; the `(2,3)` Cosserat winding owns charge/spin. The trapped-energy inertia the charter's I5 import loads is T2/swing-class energy sitting in the A1 budget — `A1 ⊥ T2` is LIVE and unresolved (D1); stage 1 therefore **does not evaluate that term at any numeric `c²`** (§10).

**MODE.** Classical, **lossless-reactive** continuum (Ax3 — no `Re(Z)` dissipative term). Linear, time-harmonic, small-displacement. A single cage / graded shell, spherically symmetric, embedded in the cold uncaged medium.

**REGIME (the point of the lane).** Deep-quasistatic `k·r_core ≪ 1`, below the fundamental cage cavity resonance `k·r_core = π` — the regime the lattice cannot reach (`research/2026-07-20_deep-rail-kscaling_derivation.md` §2). The frequency-domain formulation has **no CFL floor**, so the band bottom is set by matrix conditioning, not by a time step (§9).

**PHASE-STATE (stage 1).** Certification runs on **profile-INDEPENDENT** limits (§5) plus a **DEMONSTRATION** pass on the D5-measured grown vessel-state profile (§4). Stage 1 asserts nothing about the vessel-state physics.

**SUBSTRATE-NATIVE WALK (`substrate-native-check`, fired BEFORE any solver code — this section was written before the first line of the driver).**
1. **K4 / srs connectivity.** This instrument is a CONTINUUM instrument by charter construction — it is NOT a lattice stencil and must not pretend to be one. Its cold-medium constitutive inputs are taken from the **srs-z3 lattice measurement** (`c_P`, `c_S`, I2) rather than from any continuum-Helmholtz convention, and the isotropic reference is cross-checked against the canonical `ν_Hill = 2/7` (`ave.core.constants.N_NU`, imported — never hard-coded). Frozen disclosure: `the continuum radial channel is a CONTINUUM representation whose constitutive inputs are lattice-measured; it is not a discretization of the srs stencil and carries no K4 connectivity claim`.
2. **Cosserat / channel basis.** The radial channel is the TRACEFUL (dilatational, A1) channel. The DEVIATORIC (T2) channel enters only through the shear modulus inside the layer moduli; no independent shear observable is claimed. The `n ≥ 1` (dipole and higher) channels are **NOT hosted** — see the load-bearing scope statement in §1.
3. **Op14 saturation.** The cage is a STATIC constitutive grade `S(A) → 0` toward the rail on a graded shell — the same near-yield-shell surrogate as #770/#782/#792. Op14 is NOT run dynamically; the kernel knee is not hosted. Frozen disclosure: `Op14 saturation enters as a static constitutive grade S(A); the kernel-knee marginality is NOT hosted`.
4. **Phase-space vs real-space (A46).** Every verdict-class observable is a DIMENSIONLESS RATIO against a dimensionless argument: `r_Z = Z_bulk,eff/Z_0` (impedance plane), `rho_N(k·r_core)` (radiated-power ratio vs a dimensionless argument), and the gate residuals are relative. No real-space Cartesian read is compared against a phase-space prediction. **α-CLEAN** (the α-circularity lesson: any chord must be a dimensionless ratio).
5. **Checkpoint 8 (emergence / hosting) — FALLBACK, disclosed.** A self-bound saturated soliton is INFEASIBLE here as on the lattice (`research/2026-07-21_beta-tracking-feasibility_scoping.md` §3 absence-3). The cage is an IMPOSED graded profile. Frozen disclosure: `grade-frame: Eulerian, imposed (not self-bound); the instrument hosts no field-generated co-moving grade`.
6. **Checkpoint 10 (boundary-not-bulk).** The cage is a bounded graded shell — a boundary/topological object, not a bulk force (#403/#404).

**PRE-TEST PHYSICS CHECK (`pre-test-physics-check`; Rule 16 — ONE plumber-physical question surfaced to Grant BEFORE the design locks, not after).** *Grant — plumber-physically: this instrument drives a cage from the inside and reads what leaks out. But a "source" in a plumbing sense is two different fittings, and they give different answers to the shielding question. A **prescribed-DISPLACEMENT** source is a rigid piston: it moves the same volume per cycle no matter how soft the shell around it is, so a very compliant shell just gets pumped and still passes some flow outward. A **prescribed-TRACTION** source is a constant-pressure port: against a very compliant shell it does a lot of stroke and very little work on the far medium. On the lattice the drive was a compression pulse into a fixed geometry — neither fitting exactly. **The question: which fitting is the constituent soliton — a fixed-stroke pump (displacement) or a fixed-pressure port (traction)?** Stage 1 does NOT pick: it freezes BOTH as a reported axis (§5 G-list, §7 (v)) and shows the certification is invariant across them. The physics choice is routed to you; it becomes verdict-controlling only at stage 2.* Surfaced at design time.

**CONSISTENCY-VS-EMERGENCE TAG (`consistency-vs-emergence`).** Every stage-1 number is **CONSISTENCY-class** (the instrument reproducing known analytic limits) or **ENGINEERING-class** (numerics). Nothing here is manifestation- or emergence-class, because stage 1 banks no physics verdict. Frozen tag: `stage-1 outputs are CONSISTENCY-class (analytic-limit reproduction) or ENGINEERING-class (numerics); no manifestation- or emergence-class claim is made`.

---

## §1 — WHAT STAGE 1 CERTIFIES AND WHAT IT EXPLICITLY DOES NOT (the fence, frozen)

**Stage 1 CERTIFIES (instrument-class statements only):**
- **S1 — the radial-channel machinery is correct against analytic limits.** The layer assembly, the static (Lamé) limit, the orthotropic layer, the outgoing-radiation matching, and the lossless-reactive bookkeeping reproduce closed-form results to the §5 tolerances.
- **S2 — the deep-quasistatic band is REACHABLE and its floor is stated.** The certified band in `k·r_core` is measured, not assumed, and the mechanism that sets its bottom (matrix conditioning, NOT a CFL floor) is reported.
- **S3 — the gates are FIREABLE.** Each gate is shown to FAIL on a deliberately mis-specified input (§6), so a PASS carries information.
- **S4 — the instrument ACCEPTS the R1 orthotropic (hoop-stiff / radial-soft) profile and the D5-measured numbers,** and produces the R2-separable outputs in the frozen reporting format (§10).

**Stage 1 does NOT settle (stated plainly so the certification is not over-read):**
- **X1 — it does NOT derive `β`.** Unchanged from the charter: that needs self-bound soliton dynamics. Stage 1 PROPAGATES the D2 disclosed sweep.
- **X2 — it does NOT adjudicate the import's truth,** and — stage-1-specific — **it does not touch D1**: no `c²` is chosen, so no trapped-energy magnitude is evaluated.
- **X3 — it does NOT settle ensemble aggregation** (`N > 1`), unchanged from the charter.
- **X4 (stage-1 specific) — it banks NO physics verdict of ANY class.** Not `p`, not `r_Z`, not the vessel-state question. Every physics-shaped number in the stage-1 outputs is an INSTRUMENT-LIVENESS demonstration and is labelled `DEMONSTRATION — no verdict banked`.
- **★X5 (stage-1 specific, LOAD-BEARING — surfaced, not silently reconciled).** **The `n = 0` spherically-symmetric channel this charter specifies cannot host either of the two objects that the charter's C1 and C2 name, and this is a property of the channel, not of the implementation:**
  - the charter's **C1** frozen form F2 (`ρ_N ∝ (k·r_core)²`, `p = 2`) is derived in `deep-rail-kscaling_derivation.md` §1 explicitly for a source **DISPLACED from centre** ("a source displaced from center by `~r_core` leaks its leading uncancelled multipole with amplitude `∝ (k·r_core)`") — a **dipole (`n = 1`)** statement. A strictly spherically-symmetric instrument has no `n = 1` channel;
  - the charter's **C2** term-(i) **structural added-mass** ("a soft/pressure-release inclusion trends DOWN, bubble-like") is the long-wavelength **effective-DENSITY** correction, which in an effective-medium expansion is carried by the **dipole (`n = 1`)** scattering coefficient; the `n = 0` monopole coefficient carries the effective COMPRESSIBILITY (`K_eff`), not `ρ_eff`.
  **Frozen consequence:** stage 1 certifies the `n = 0` machinery and states that **C1's `p = 2` test and C2's term-(i) require an `n = 1` (coupled P–S) radial channel that stage 1 does NOT build.** This is surfaced to Grant / the auditor lane as a charter-scope finding (flag-don't-fix); the charter's §2 object is NOT reframed here, and no stage-1 output is presented as testing F2. Frozen disclosure carried by every stage-1 output: `n=0 monopole channel only; the n=1 dipole channel (F2 displaced-source p, and the structural added-mass term of rho_eff) is NOT built in stage 1`.

**What the `n = 0` channel DOES deliver (stated so the scope limit is not read as emptiness):** the **centred-source** shielding ratio `rho_N(k·r_core)` — the perfect-centring limit of the cage's compression shielding, which is the `n = 0` half of the derivation's own two readings (`deep-rail-kscaling_derivation.md` §1 Step 1, spherical-cavity reading) — plus the static-compliance ratio that sets its deep-quasistatic value. Stage 1 reports it as liveness, not as a verdict.

---

## §2 — THE INSTRUMENT (D3 = charter recommendation: transfer-matrix PRIMARY + matched-asymptotics BACKSTOP)

**The radial channel (derived, not imported).** For spherically-symmetric radial motion `u = u_r(r) ê_r` in a **spherically-orthotropic** linear-elastic medium (transversely isotropic about `r̂` — exactly the R1 shape: a radial modulus and a hoop modulus, both functions of `r`), with
`σ_rr = C_rr u' + 2 C_rθ u/r` and `σ_θθ = C_rθ u' + (C_θθ + C_θφ) u/r`,
the radial equation of motion `σ_rr' + (2/r)(σ_rr − σ_θθ) + ρ ω² u = 0` reduces to
`u'' + (2/r) u' − (β²/r²) u + (ρ ω²/C_rr) u = 0`, with `β² ≡ 2(C_θθ + C_θφ − C_rθ)/C_rr`.
Frozen consequences (both `[derived]`):
- **Dynamic layer solution:** `u(r) = r^(−1/2) [A J_ν(k r) + B Y_ν(k r)]`, `ν = sqrt(β² + 1/4)`, `k = ω sqrt(ρ/C_rr)`. The isotropic case gives `β² = 2`, `ν = 3/2` — the ordinary spherical-Bessel `j_1`/`y_1` pair.
- **Static layer solution (ω = 0):** `u(r) = A r^s1 + B r^s2`, `s = (−1 ± sqrt(1 + 4β²))/2`. The isotropic case gives `s = +1, −2` — the textbook Lamé pair, whose decaying branch has `∇·u ≡ 0`.

**SOLVER 1 (PRIMARY) — frequency-domain transfer matrix.** The profile is discretized into homogeneous concentric shells; each shell's `2×2` state map on `y = (u, σ_rr)` is `T = M(r_b) M(r_a)^(−1)` built from the exact analytic basis above (**column-normalized before inversion** — the frozen conditioning measure, §9); the layer maps compose to a global `T`. Outgoing radiation is imposed by the exact analytic exterior solution (`H_ν^(1)`) at a matching radius `R_match` inside the homogeneous exterior — so there is **no absorbing boundary, no sponge, and no truncation error from the far field** (the continuum answer to R6-ii). Frozen: `the exterior beyond R_match is represented by the exact analytic outgoing solution; no sponge, no absorbing layer, no far-field truncation`.

**SOLVER 2 (BACKSTOP) — analytic matched-asymptotics.** In the deep-quasistatic limit the interior is the STATIC problem and the exterior is a radiating monopole; matching the static decaying mode `B/r²` onto the small-argument outgoing solution gives `radiated power ∝ k⁴ |B|²`, hence the frozen closed form
`rho_N(k·r_core → 0) = |B_caged / B_uncaged|²` — **a `k`-INDEPENDENT limit** obtained from the STATIC solve alone, with the `k` dependence cancelling in the ratio. This is the backstop for R5 and the instrument of record BELOW the transfer matrix's conditioning floor (§9).

**Why `research/drivers/` and not `src/ave/` (the discipline question, answered).** The engine tree is the certified regime-organized platform (`manuscript/ave-kb/common/engine-capability-map.md` §2); this is a **single-lane instrument** for one research question, with a continuum representation that is deliberately NOT a discretization of the srs stencil (§0 walk item 1). Promoting it into `src/ave/` would place a continuum-Helmholtz-shaped operator inside the substrate engine tree, where later readers would reasonably assume it carries the engine's K4/Cosserat guarantees — it does not. It therefore ships as a lane driver alongside `rve_aggregation_bench.py` / `vessel_state_rve.py`, importing `ave.core.constants` read-only. Frozen: `engine src/ave BYTE-UNTOUCHED; the instrument lives entirely in research/drivers/ and imports ave.core.* read-only`.

---

## §3 — IMPORT-LEDGER DELTA (on top of the charter §3 I1–I10; substrate-first-for-numbers)

The charter's I1–I10 stand unchanged. Stage 1 adds:

| # | Input | Class | Source / anchor |
|---|---|---|---|
| **I11** | Cold-medium speeds `c_P`, `c_S` **read programmatically** from the shipped #796 JSON (`spectral_cold.cP`, `spectral_cold.cS`) | **LATTICE-MEASURED** (= charter I2, now with a machine-read path) | `research/drivers/vessel_state_rve_results.json` |
| **I12** | The isotropic cold reference `ρ_0 ≡ 1`, `C_rr,0 = ρ_0 c_P²`, `G_0 = ρ_0 c_S²`, `K_0 = C_rr,0 − 4G_0/3` | **DERIVED from I11** (unit choice `ρ_0 = 1`, `r_core = 1` — dimensionless by construction) | this lane; all observables are ratios so the unit choice cancels |
| **I13** | `ν_Hill = 2/7` consistency read (`ave.core.constants.N_NU`) | **`[canon]` — imported, read-only, CONSISTENCY-check use only** | `src/ave/core/constants.py` |
| **I14** | The D5 grown-vessel orthotropic gains `hoop_gain`, `radial_gain`, read programmatically from the #796 JSON | **LATTICE-MEASURED (scalars) × `[canon]`-FORM remap** | §4 |
| **I15** | Solver numerics: layer count `n_shell`, layer allocation rule, `R_match`, `r_s`, shell width `W`, band sampling | **ENGINEERING CHOICE — tagged, frozen in §5** | this lane |
| **I16** | The D2 disclosed sweep `β ∈ {0, 1, 3}` | **DISCLOSED SCAN (Grant D2)** — magnitude OPEN | `clm-m5swh9`; #782 companion |
| **I17** | The sector-crossed `c²` | **OPEN — HELD by Grant (D1); carried SYMBOLICALLY, never evaluated** | `clm-m5swh9`; §10 |

**R8 audit rule (frozen).** `every number the solver consumes appears on the charter §3 ledger or the §3 delta with its tag; no SM/GR convention default (in particular no c_light and no unlabeled c) enters anywhere`.

---

## §4 — THE D5 PROFILE INPUT (measured, machine-read) + its DISCLOSED GAP

**Ruled input (D5).** The R1 orthotropic profile is built from the **grown** vessel state measured by the #796 bench, read programmatically from `research/drivers/vessel_state_rve_results.json` — never retyped from prose. The two gains entering the shell layers are:
- `radial_gain ≡ verdict.fixed_budget_headline.min_kse / provenance.constants.k_s_KS0` — the radial-bond softening at its extremum;
- `hoop_gain ≡ 1 + provenance.constants.k_a_RHO_STAR · verdict.fixed_budget_headline.peak_A / provenance.constants.k_s_KS0` — the hoop stiffening at its extremum, via the `[canon]`-form remap `k_shear,eff = k_s + T/ℓ`, `T/ℓ = k_a·ε` (`axiom-register.md:193`).

Frozen: `the D5 profile gains are computed from the shipped vessel_state_rve_results.json fields (min_kse, peak_A, k_a_RHO_STAR, k_s_KS0) at driver runtime; no vessel-state number is retyped from prose`.

**★THE DISCLOSED GAP (flag-don't-fix — surfaced, not papered over).** D5 says "feed the measured profile". **The #796 bench did not ship a resolved radial profile `ε(r)`.** What it shipped is (a) two SCALAR extrema (`peak_A`, `min_kse`) and (b) a C-V shell reconstruction that its own result doc grades **corroborative-only** — the `K(ε_bias)` curve is "nearly FLAT … a total variation of `0.059 %`", so the reconstructed POSITION/WIDTH/ASYMMETRY "reads the tiny residual monotonic slope's off-centre-ness, not a resolved depletion-edge shell feature" (`research/2026-07-22_vessel-state-rve_result.md` §—C-V). **Stage 1 therefore builds a profile whose EXTREMA are measured and whose radial SHAPE is an engineering choice** (the frozen quadratic grade of §5), and says so in every output. Frozen disclosure: `the D5 vessel-state EXTREMA are lattice-measured; the radial SHAPE between them is an ENGINEERING CHOICE — #796 shipped no resolved radial profile, and its C-V shell reconstruction is corroborative-only by its own grading`.

**★THE MIXED-PROVENANCE CARRY (cited as #796 requires).** #796's own ledger correction states that its `r_Z = 0.5436` is `[derived]` in its `K` factor and `[assumption]` in its `ρ` factor — "a MIXED-provenance number, and it must be cited as such downstream (notably by the continuum-radial-solver lane, #789 D5/R1)". Frozen: `any stage-1 output that carries the #796 r_Z cites it as MIXED-provenance (K derived, rho assumed at rho_eff/rho_0 = 1); the #796 rho half is UNRESOLVED and stage 1 does not repair it`.

---

## §5 — THE FROZEN VALIDATION GATES (G1–G9), with numeric tolerances

**Frozen instrument geometry + numerics (I15, ENGINEERING, tagged).** `r_core = 1`, source surface `r_s = 0.30`, graded-shell width `W = 0.30` (grade band `r ∈ [0.70, 1.00]`), grade law `S(t) = 1 + (S_rail − 1)·t²` with `t = (r − 0.70)/0.30`, baseline `S_rail = 1e-3`, layer allocation **log-uniform in `S`** (equal ratio of adjacent layer moduli), `n_shell = 256`, `R_match = 4·r_core`, exterior annulus `r ∈ [1, R_match]` in 8 uniform layers. Deterministic: no RNG anywhere in the instrument.

**Frozen observables (KEEP-BOTH — the charter/#775 convention conflict is preserved, not resolved by fiat).** The charter's R5(b) asks for `ρ_N → 0` in the uniform-medium null, while #775's `ρ_N` is a caged/uncaged POWER RATIO whose no-scatterer value is `1` (its measured band is `0.26–2.90`, and a no-cage arm is `1` by construction). Rather than redefine either in place, stage 1 freezes **both**, and reports both everywhere:
- `rho_N ≡ P_rad(caged)/P_rad(uncaged) at matched source amplitude` — the #775-convention ratio; uniform-null value `1`.
- `rho_S ≡ |rho_N − 1|` — the scattered RESIDUAL; uniform-null value `0`, which is the charter's R5(b) reading.
Frozen: `the uniform-medium NULL is read on BOTH conventions: rho_N -> 1 and rho_S -> 0; neither convention is redefined in place (KEEP-BOTH)`.

| Gate | What it certifies | FROZEN criterion |
|---|---|---|
| **G1** | **Lamé exterior `∇·u = 0` static limit** (charter R5(a); the #782-confirmed gate) — a graded shell pressurized in an INFINITE medium has a pure-deviatoric exterior tail | `lame_ratio ≡ max over r in {1.5, 2.5, 3.5} of |div u|(r) / |div u|(0.5) <= 1e-10` AND the multi-radius agreement `max|Δ div u| / mean(div u) <= 0.25 across the three exterior radii` (the #782 frozen shell-agreement tolerance, inherited) |
| **G2** | **Uniform-medium NULL** (charter R5(b)) — cage moduli set equal to the matrix ⇒ no scatterer | `at zero contrast: |rho_N - 1| <= 1e-12 AND rho_S <= 1e-12 AND |r_Z - 1| <= 1e-12`, evaluated at `k·r_core ∈ {1e-3, 0.3}` |
| **G3** | **Orthotropic→isotropic reduction** — the orthotropic layer at unit gains must reproduce the isotropic layer exactly (R1's representation is not an approximation) | `|B_ortho(hoop=1,radial=1) - B_iso| / |B_iso| <= 1e-12` |
| **G4** | **Transfer-matrix ↔ matched-asymptotics agreement** (D3's (a)+(c) cross-check; the two-of-three build) | `|rho_N_TM(k·r_core) - rho_N_MA| / rho_N_MA <= 1e-6 for every k·r_core <= 1e-3 in the frozen band` |
| **G5** | **Ax3 lossless-reactive discipline** (charter R7) — no smuggled friction; work in = power radiated | `|P_in - P_rad| / |P_in| <= 1e-10` at `k·r_core = 0.3` AND the assembled transfer matrix is real: `max|Im T| / max|Re T| <= 1e-14` |
| **G6** | **Layer-refinement convergence** (I15 numerics) | `|rho_N(2·n_shell) - rho_N(n_shell)| / rho_N(n_shell) <= 1e-3 at the frozen n_shell = 256`, on BOTH the isotropic and the D5 orthotropic profile |
| **G7** | **Drive-amplitude independence** (charter R6-i) | `rho_N invariant across source amplitude 1e-6 ... 1e+6 to <= 1e-12 relative`. **Disclosed:** in a linear frequency-domain solver this is STRUCTURALLY exact, so a PASS is a wiring check, not evidence of physical linearity — labelled as such (§7 (i)). |
| **G8** | **Matching-radius / outer-boundary independence** (charter R6-ii) | `rho_N invariant across R_match/r_core in {2, 4, 8, 16} to <= 1e-9 relative` |
| **G9** | **Band + conditioning** (declares the certified band rather than assuming it) | `cond(system matrix) <= 1e12 at every sampled k·r_core in the certified band k·r_core in [1e-8, 4]`, sampled at `k·r_core ∈ {1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 1e-1, 0.3, 1.0, 3.0, 4.0}` |

**Source-fitting axis (the pre-test-physics-check, frozen as an axis not a value).** G1–G9 are evaluated for BOTH `src ∈ {displacement, traction}`; a gate PASSES only if it passes for both. Frozen: `every gate is evaluated for both source fittings (prescribed displacement and prescribed traction) and passes only if it passes for both`.

---

## §6 — THE GATE-FIREABILITY SELF-TESTS (FT-1…FT-4) — each MUST FIRE

**The rule (frozen).** A gate that cannot fail is not a gate. Each self-test feeds a **deliberately mis-specified** input that the corresponding gate MUST reject; if any self-test fails to fire, the certification is **NOT-CERTIFIED (VOID)** regardless of how many gates passed (§8). The self-tests are shipped in the same JSON as the gates.

| # | Targets | Deliberate mis-specification | FROZEN firing criterion |
|---|---|---|---|
| **FT-1** | **G1** (Lamé) | a profile whose grade does NOT terminate at the cage contour — the exterior carries a residual power-law modulus grade `(r/r_core)^(−q)` with `q = 0.10`; and, separately, an exterior mistakenly carrying the cage's orthotropy (`hoop = 1.02`, `radial = 0.99`) | `both mis-specified profiles MUST return lame_ratio >= 1e-3` (i.e. `>= 1e7 ×` the G1 pass tolerance) |
| **FT-2** | **G2** (null) — the **structural-null lens**: proves `rho_S` is a LIVE observable, not identically zero by construction | a tiny but nonzero cage contrast `S_rail = 0.99` | `the contrast case MUST return rho_S >= 1e-5 at k·r_core = 1e-3` |
| **FT-3** | **G5** (Ax3) | an ABSORBING shell — a complex modulus with `Im/Re = 1e-3` (a smuggled friction, exactly what R7 forbids) | `the absorbing case MUST return |P_in - P_rad|/|P_in| >= 1e-2` |
| **FT-4** | **G4** (TM↔MA) — proves the agreement is a real, breakable agreement rather than two evaluations of one code path | evaluate the SAME comparison at `k·r_core = 3.0`, i.e. ABOVE the quasistatic validity of the backstop | `the out-of-regime comparison MUST return |rho_N_TM - rho_N_MA|/rho_N_MA >= 1e-1` |

Frozen: `gate_fireability_selftest_pass = FT-1 AND FT-2 AND FT-3 AND FT-4 all FIRE at their frozen thresholds`.

---

## §7 — R6 ARTIFACT CONTROLS, adapted to the continuum (frozen)

- **(i) Drive-amplitude independence** → **G7**, with the honesty caveat frozen in: `G7 is STRUCTURALLY exact in a linear frequency-domain solver; it certifies wiring, not physical linearity, and is reported as such`. (The lattice prototype's failure of the analogous gate, `beta-tracking-feasibility_scoping.md` §6 gate-i, was a NONLINEAR-settling artifact that cannot arise here — so the control is retained as a wiring check and explicitly demoted as evidence.)
- **(ii) Outer-boundary / reflection control** → **G8**, plus the structural statement that the exterior is analytic beyond `R_match` (§2) — there is no sponge to fail.
- **(iii) Resonance control** → **G9** declares the band, and every reported sub-resonant quantity is restricted to `k·r_core <= 1e-3` where **G4** holds; the resonant region `k·r_core ≳ 1` is reported but never used for a power-law read. Frozen: `no exponent or quasistatic quantity is read above k·r_core = 1e-3; the resonant band is reported as characterization only`.
- **(iv) Grade-FRAME disclosure** → frozen string, carried in every output: `grade-frame: Eulerian, imposed (not self-bound); the instrument hosts no field-generated co-moving grade`.
- **(v) Source-fitting disclosure** (new, from the §0 pre-test-physics-check) → frozen string: `source fitting reported on BOTH axes (prescribed displacement / prescribed traction); the physical fitting is Grant-routed and not picked here`.
- **(vi) Determinism** → `two independent full driver runs produce an identical results digest (SHA-256 over the results object minus timing fields)`.

---

## §8 — OUTCOME CLASSES (exhaustive; every class REACHABLE)

The stage-1 verdict is a CERTIFICATION class, not a physics bin. Three classes, exhaustive by construction:

- **CLASS A — CERTIFIED.** `all of G1..G9 PASS on both source fittings AND gate_fireability_selftest_pass = True`. ⇒ The instrument is certified over the measured band, for the `n = 0` channel, with the §1 X-fence attached.
- **CLASS B — CERTIFIED-SCOPED.** `all of G1..G9 PASS and gate_fireability_selftest_pass = True, but at least one gate passes only over a REDUCED band or a REDUCED profile class`. ⇒ certification stands with the reduction stated explicitly in the result headline (e.g. a narrower certified `k·r_core` band, or one source fitting only).
- **CLASS C — NOT-CERTIFIED (VOID).** `any of G1..G9 FAILS, OR any of FT-1..FT-4 fails to fire`. ⇒ no stage-2 build proceeds on this instrument; the failure is reported with its numbers and routed. **A gate that cannot fail voids the certification exactly as hard as a gate that fails** (the fireability rule).

**Reachability argument (frozen — every outcome class has a REACHABLE bin).** CLASS C is reachable and is DEMONSTRATED reachable by FT-1…FT-4 themselves: each self-test is an actual run of the actual gate on an input that lands it in CLASS C, so the failing bin is exercised in every certification run, not merely postulated. CLASS B is reachable because the band edges (G9) and the source-fitting axis are measured, not assumed — a conditioning failure at the band bottom or a one-fitting-only pass lands CLASS B without any criterion being dropped. CLASS A is reachable because the scouted margins on every gate exceed the frozen tolerance by `≥ 4` orders of magnitude (§9). No outcome requires a criterion to be relaxed after the fact (Rule 11: `no adjudication criterion may be dropped or relaxed post-hoc to convert a FAIL to a PASS`).

**★Stage-1 no-verdict fence (frozen, mandatory in every output).** `stage 1 banks NO physics verdict; every physics-shaped number in these outputs is an INSTRUMENT-LIVENESS DEMONSTRATION and is labelled DEMONSTRATION — no verdict banked`.

---

## §9 — MUTUAL-SATISFIABILITY OF THE FROZEN REQUIREMENTS (the Protocol-E lesson, applied BEFORE the freeze)

The #796 lane's root-cause finding was a **frozen-precondition conflict caught only at integrator time**: its frozen §4 required `k·r_core ≪ 1` while its frozen box sizes forced `k·r_core ≈ 2–4` — "the frozen box sizes and the frozen long-λ precondition are mutually unsatisfiable" (`research/2026-07-22_vessel-state-rve_result.md`). This section checks the stage-1 frozen set BEFORE the freeze. The checks below were run on an **uncommitted scratch prototype** (disclosed; no physics observable was scouted — only feasibility and tolerance headroom).

1. **Deep-quasistatic reach vs the solver formulation.** The frequency-domain transfer matrix has **no CFL floor**, so `k·r_core ≪ 1` is not in tension with anything. **Satisfiable.**
2. **G4's overlap band is NON-EMPTY.** G4 requires a band where the transfer matrix is well-conditioned AND the matched-asymptotics leading order is accurate. TM conditioning stays `≤ 1e12` down to `k·r_core = 1e-8`; the MA leading order is accurate to `≤ 1e-6` up to `k·r_core = 1e-3` (its error grows as `(k·r_core)²`). **Overlap = `[1e-8, 1e-3]`, five decades. Satisfiable.**
3. **The band top (G9, `k·r_core = 4 > π`) does not conflict with G4,** because G4 is required only for `k·r_core ≤ 1e-3`; above it, FT-4 requires the two solvers to DISAGREE. The two requirements are on disjoint sub-bands. **Satisfiable, and jointly informative.**
4. **G1 (static, `ω = 0`) and G4/G5/G9 (dynamic) share one layer stack and one assembly path,** so a single frozen profile serves both without a second discretization. **Satisfiable.**
5. **G8's `R_match` sweep stays in the homogeneous exterior:** the grade terminates at `r_core = 1` and the smallest swept `R_match` is `2·r_core`. **Satisfiable.**
6. **G6's refinement to `2·n_shell = 512` at every band point on two profiles and two source fittings is a linear-algebra cost of `O(10³)` `2×2` products per solve.** Scouted total battery runtime is well under the frozen budget. Frozen: `total certification-battery runtime <= 600 s on the reference machine; a longer run is disclosed, not silently accepted`.
7. **★THE ONE REQUIREMENT DELIBERATELY NOT FROZEN, and why (the honest limit).** A requirement that the **transfer matrix** reach the physical constituent regime `k·r_core ~ 1e-25` (`deep-rail-kscaling_derivation.md` §2 table) would be **UNSATISFIABLE in double precision**: the two basis solutions differ in magnitude by `~ x^(−2ν) = x^(−3)`, i.e. `~1e75` at `x ~ 1e-25`, far beyond float64. It is therefore **not frozen as a transfer-matrix requirement**. Frozen instead: `below k·r_core = 1e-8 the matched-asymptotics backstop is the instrument of record; it is k-independent in that limit and is certified against the transfer matrix in the overlap band [1e-8, 1e-3]`. This is precisely why D3's ruling is (a)+(c) and not (a) alone.

---

## §10 — THE SYMBOLIC `c²` DISCIPLINE (D1 HELD) + the R2 two-term separable reporting contract

**R2 (frozen reporting contract).** Every `ρ_eff` output is reported as **two named columns, never pre-summed**:
- **term (i) — STRUCTURAL added-mass.** In the `n = 0` channel at leading order in the long-wave limit, the structural effective density is the volume average; for a pure STIFFNESS grade at uniform substrate inertia this is `rho_eff_structural/rho_0 = 1` exactly — the same anchor #782/#796 carry. **The dynamic (dipole) part of this term is the `n = 1` object stage 1 does not build (§1 X5), so the column ships as `1` with the flag `structural dipole term NOT BUILT (n=1 channel absent in stage 1)`.**
- **term (ii) — TRAPPED-ENERGY loading (the charter's I5 import).** Reported as `beta·phi` over the D2 disclosed sweep `β ∈ {0, 1, 3}`, with the frozen symbolic label carried in the column header and in the JSON: `beta = (u_trapped · P) / (rho_0 · c_x^2) — c_x SYMBOLIC, D1 HELD; no c^2 evaluated`.

**★How the symbolic `c²` threads through the outputs without any choice leaking in (frozen).** The import is `ρ_contribution = E_trapped/c_x² · (participation)`, so the trapped-energy column depends on `c_x` **only through the factor `1/c_x²`**. Two consequences, both frozen:
- **(a) The D2 sweep and the D1 choice lie on the SAME axis.** `β` as defined above is the PRODUCT of a magnitude and `1/c_x²`; a different sector choice does not add a new degree of freedom, it relabels which member of the disclosed `β`-family is the physical one. Hence **the D2 disclosed sweep makes stage 1 D1-independent by construction**, and stage 1's outputs are a family, not a false-precision number.
- **(b) The LEVER LENGTH of the D1 choice is reported as a pure dimensionless ratio** — the candidate-swap factor `(c_i/c_j)²` computed from the LATTICE-MEASURED speeds (I11), with **no candidate designated**: swapping the divisor between the two lattice-measured candidates rescales `β` by `(c_P/c_S)² `, a number the instrument reports, and the third candidate `c_EM` is carried as an UNEVALUATED symbol because no lattice-measured value for it is on the ledger. Frozen: `the c^2 dependence is reported as the dimensionless candidate-swap ratio (c_i/c_j)^2 from the lattice-measured speeds, with NO candidate designated and c_EM carried as an unevaluated symbol`.

**R4 (frozen).** `r_Z = sqrt((K_eff/K_0)·(rho_eff/rho_0))` is ASSEMBLED, not re-measured: the `K_eff/K_0` factor is the lattice input I1 and `r_Z must NOT recompute or perturb K_eff/K_0`. Stage 1 reports `r_Z` only as a two-term FAMILY over the D2 sweep, tagged `DEMONSTRATION — no verdict banked`, and carrying the #796 MIXED-provenance citation of §4.

---

## §11 — LEDGER TAGS + OWED FOLLOW-ONS (fenced; NOT executed here)

**Ledger tags (`consistency-vs-emergence`, frozen).** `lame_ratio`, `rho_N`, `rho_S`, `r_Z`, the gate residuals and the conditioning numbers are `[derived]` dimensionless ratios, **CONSISTENCY-class** (analytic-limit reproduction). `c_P`, `c_S` are `[lattice-measured]` (I11). The D5 gains are `[lattice-measured]` scalars × a `[canon]`-form remap; the radial SHAPE is `[engineering-choice]` (§4). `ν_Hill = 2/7` is `[canon]`, read-only. `β` is a `[disclosed-scan]` with an OPEN magnitude (`clm-m5swh9`). `c_x²` is `[OPEN — HELD]` and never evaluated. The E=mc² trapped-energy inertia law is `[TAGGED IMPORT — NOT DERIVED]` (charter I5) and is never promoted to derived. `α`-CLEAN. **No emergence-class claim; no manifestation-class claim; no physics verdict.**

**Owed follow-ons (fenced; NOT executed here — Rule 12, the slot is NOT refilled with an assertion).**
1. **The `n = 1` (coupled P–S) radial channel** — required by the charter's C1 (`p = 2`, displaced source) and C2 term-(i) (structural added-mass). Surfaced in §1 X5; a stage-2 build with its own prereg, or a charter amendment if Grant rescopes. **Not drafted here** (the auditor lane lands charter-level changes).
2. **D1** — the sector-crossed `c²`, HELD by Grant. Until it lands, no trapped-energy magnitude is evaluated anywhere in this lane.
3. **A resolved radial `ε(r)` for the vessel state** — #796 shipped extrema, not a profile (§4). Whether one is obtainable is #796's OWED-2 territory, routed to Grant, not this lane's.
4. **The charter's §4 scope tension** (single-core `p` vs star-scale aggregation) stands unchanged and unadjudicated; stage 1 touches neither side.

---

> **Pre-registration provenance.** Stage-1 prereg for the merged charter `research/2026-07-21_continuum-radial-solver_CHARTER.md` (#789), authored after Grant ruled its §0 decisions 2026-07-28 (verbatim `[sic]`: `"D2: disclosed, D3: follow rec, D4: do it, D5: do the rec"`), with **D1 HELD**. This is COMMIT 1 — the prereg ALONE, frozen and pushed before any solver code. Companion inputs cited by path (cite-don't-duplicate): the charter §0/§3/§4/§5/§6; `research/2026-07-20_deep-rail-kscaling_derivation.md` §1/§2 (F2, the regime gap, the displaced-source reading); `research/2026-07-21_beta-tracking-feasibility_scoping.md` §3/§4/§6; `research/2026-07-21_rve-aggregation-bench_prereg-FROZEN.md` §1/§3/§4 (the `r_Z` discriminator, the KUBC extraction, the Lamé gate); `research/2026-07-22_vessel-state-rve_result.md` + `research/drivers/vessel_state_rve_results.json` (the D5 measured profile, its MIXED-provenance `r_Z`, and the Protocol-E mutual-satisfiability lesson); `manuscript/ave-kb/common/relative-offset-principle.md` (`clm-hu1jjw` direction / `clm-m5swh9` open magnitude). Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; port-register / falsification-ledger untouched regardless of outcome. **Banks no physics verdict.** Companion: the docket fragment `_orchestration/docket-entries/2026-07-28-continuum-radial-solver-stage1.md`.

