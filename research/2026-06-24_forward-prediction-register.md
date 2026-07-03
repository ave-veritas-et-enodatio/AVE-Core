# Forward-Prediction Register — AVE-distinct vs SM/QED, derived-vs-echo

**Date:** 2026-06-24
**Class:** research (low canonical-risk consolidation; not a new claim node, not a pre-reg).
**Branch:** `analysis/forward-prediction-register-oa-node`
**Source-map provenance:** all file:line below re-grep-confirmed at HEAD `dc9e1791` this session.
**Lane:** implementer.

---

## 0. THE HARD FACT — read this first

**Nothing in this register is experimentally tested.** Every forward prediction
in the AVE corpus carries `experimental_solidity: None` in the claims index
(`manuscript/ave-kb/.index/claims.jsonl`) — confirmed by direct read: all 299
`clm-` nodes (incl. the new `clm-fofwr1` minted here) carry
`experimental_solidity: null`, and the birefringence/dispersion/GW/baryon
predictions cited here are among them. "Forward prediction" here means
**untested-by-construction**: a DERIVED (or asserted) divergence from SM/QED
that *no experiment has yet confronted*. The solidity numbers quoted (0.80,
0.70, 0.60, …) are **derivation_solidity** — internal derivation rigor — not
empirical confirmation. Do not read any row below as "AVE is empirically
ahead." None of these has been measured.

A second hard fact: the AVE-distinct content is, almost everywhere, the
**FORM** (the shape/structure/parity of the divergence), while the **MAGNITUDE**
is frequently an **α-echo** (a CODATA-α-rooted value the substrate does not
independently select) or sits below current experimental bounds. The honest
register separates these per-prediction.

---

## 1. HEADLINE VERDICT

- **Cleanest near-term make-or-break = E-route vacuum birefringence FORM**
  (`clm-pp3qwf`). The CHORD is that the vacuum saturates *at tree level*
  (O(1) existence) versus QED's α²-loop birefringence — a structural,
  two-sided, field-independent COEFFICIENT divergence reachable at HIBEF-class
  fields. (The magnitude ratio `7.5/α³ ≈ 1.93×10⁷` is itself an α-echo; the
  bankable content is the *existence of the saturation coefficient*, not its
  α-rooted value.)

- **The winding's distinct payoff = the PARITY axis.** S1 (the (2,3) winding as
  a separately-conserved DOF) **PASSED** (2026-06-24, derived-REAL, scoped to
  real-space ω + single-knot conservation). What the winding buys is the
  cleanest possible divergence shape: **parity zero-vs-nonzero**. QED vacuum is
  parity-even ⟹ structurally pinned to exactly zero on any chiral-vacuum
  observable. Two winding-channel observables ride this:
  1. **Field-free optical activity sign-flip** — FORM AVE-distinct and
     live-confirmed (writhe ±0.04087, sign-flips between enantiomorphs, exactly
     0 on achiral diamond). MAGNITUDE **not bankable** (~40 OOM over the cosmic
     bound; continuum mapping OPEN). Minted as `clm-` this session (see §9).
  2. **Writhe co-vs-anti-handed |F| ratio** — **CLOSED → RESOLVED-TO-CONSISTENCY**
     (2026-07-03; was "highest-value unbuilt FORM chord"). Built through Gate-0 +
     the linear-channel campaign: magnitude-R BLOCKED (overlap + Yukawa), SIGN =
     signed-Coulomb under the Ax2 winding=charge mapping (SM-shared, not
     parity-distinct). Did NOT bank as a chord; produced the engine-derived
     Axiom-2 interaction leg instead (`clm-wcoul2`). See §2.4 status history.

- **NOT winding channels:** E-route birefringence (field-INDUCED, even-in-k,
  dielectric saturation) and the (q·ℓ_node)⁴ dispersion (parity-EVEN, achiral
  diamond point group). These are real divergences but they do not test parity.

- **The bankable AVE-distinct list is THINNING (2026-06-24).** The (q·ℓ_node)⁴
  dispersion tell is now **DEMOTED** (derived-chord → CONDITIONAL on the
  unproven weak-C no-zone-edge theorem; the P1b genuine chiral-srs eigensolve
  measures the GENERIC slope-2 band-edge term — §2.2). It joins the other
  demoted/non-bankable forward predictions: **OA sign-flip** (FORM-distinct but
  magnitude NOT bankable, ~40 OOM over the cosmic bound, continuum k→0 OPEN —
  §2.3); **birefringence** (the E⁴-vs-E² exponent framing was RETRACTED — the
  divergence is the E²-leading COEFFICIENT, not an E⁴ tell — §2.1); **GW-echo**
  (consistency-class, retrospective, ~4 ms ringdown-echo claims in tension —
  §2.5). What stays as the cleanest near-term make-or-break is the **E-route
  vacuum-birefringence COEFFICIENT** (`clm-pp3qwf`, existence-of-saturation,
  reachable at HIBEF-class fields) and — once built — the **dimensionless
  co-vs-anti |F| winding-ratio**. The FORM chords survive; the *bankable* ones
  are few.

---

## 2. PER-PREDICTION REGISTER

Each row: **claim** / **SM-QED divergence** / **derivation status** / **falsifier** /
**winding channel?**. Status legend: DERIVED-form = the shape/structure is
node-up derived; ECHO-magnitude = the dimensionful value is CODATA-α-rooted or
imported; ASSERTED = stated, not in-leaf derived; FALSIFIED; consistency-class =
reproduces SM at current sensitivity; corroborated-null = agrees with both data
*and* SM (survival, not divergence).

### 2.1 Vacuum birefringence, E-route — `clm-pp3qwf` (solidity 0.80)

- **Claim.** A static **E** field loads ε only (ε-varactor, V-keyed), giving an
  isotropic common-mode index shift `δn ≈ −¼(E/E_yield)²` and a matched
  differential falsifier `δn_bir = n∥ − n⊥ ≈ −½A²` (uniaxial probe). At
  HIBEF-class fields δn ≈ 2×10⁻⁷ vs QED Euler-Heisenberg ~5×10⁻¹⁴.
  Canonical at `vol4/claim-quality.md:389` (`<!-- id: clm-pp3qwf -->`).
- **SM/QED divergence.** Both AVE and QED are **E²-leading** — the discriminator
  is the **COEFFICIENT**, not the exponent. AVE's vacuum saturates at tree-level
  with an O(1) (un-suppressed) nonlinearity against `E_yield ≈ 1.13×10¹⁷ V/m`;
  QED's Euler-Heisenberg shift is α²-loop-suppressed against
  `E_crit ≈ 1.32×10¹⁸ V/m`. The matched field-independent ratio is
  `δn_AVE/δn_QED = 7.5/α³ ≈ 1.93×10⁷` (`vol4/claim-quality.md:399`).
- **Derivation status.** FORM = **DERIVED genuine chord** (tree-level O(1)
  saturation existence vs α²-loop). MAGNITUDE = **α-ECHO**: the ratio is
  `7.5/α³`, and the yield field itself carries `V_YIELD = √α · V_SNAP` — the √α
  is **inserted by hand** at `src/ave/core/constants.py:460`
  (`V_YIELD: float = np.sqrt(ALPHA) * V_SNAP`). Re-grep CONFIRMS the source map.
  Symmetric-standard note: QED's `a_EH α²` is equally α-rooted, so calling the
  value an echo is peer-mapped, not an AVE-comedown.
- **Falsifier.** Two-sided: a QED-sized coefficient (~10⁶× smaller at the same
  field) falsifies AVE; an AVE-sized coefficient falsifies QED. Field-INDEPENDENT
  (present at all fields), so it does not need a regime-gated exponent change.
- **Winding channel?** **NO.** Field-INDUCED, even-in-k, dielectric saturation
  (parity-even). This is the cleanest *near-term* test but it is **not** a parity
  test.

### 2.2 (q·ℓ_node)⁴ dispersion / birefringence — `clm-k4d4ph` (0.60, DEMOTED) + `clm-yr6tu4` (0.78)

- **Claim.** The K4/diamond-cubic Bloch matrix has its first directional
  anisotropy at order `(q·ℓ_node)⁴` — the cubic harmonic
  `Ξ(q̂) = q̂_x⁴+q̂_y⁴+q̂_z⁴` (sign-changing, Fd-3m-protected). Magnitude
  `δ ≈ 2.2×10⁻²²` at 633 nm. Canonical at `vol4/claim-quality.md:437`
  (`clm-k4d4ph`); group-theory parent `vol1` (`clm-yr6tu4`).
- **SM/QED divergence.** A quartic (not quadratic) first-anisotropy, symmetry-
  protected; a random (non-cubic) bond set would break it to quadratic. Parity-
  EVEN.
- **Derivation status — DEMOTED 2026-06-24 (derived-chord → CONDITIONAL).** The
  bond-moment FORM identities (`Σ_b(q̂·d̂)² = 4/3` isotropic, `Σ_b(q̂·d̂)⁴ =
  −8/9·Ξ + 4/3` anisotropic; reproduced by an independent from-scratch eigensolve
  to ~10⁻¹⁵) are DERIVED and node-up — but the **distinctive (q·ℓ_node)⁴ photon
  EM-dispersion tell is NOT a from-eigensolve result.** The **P1b genuine 24×24
  chiral-srs Bloch eigensolve** (substrate-native rank-2 bond tensor on the z=3
  srs bonds; `src/scripts/vol_4_engineering/srs_bloch_dispersion.py` on branch
  `engine/p1b-modes-live`, cited by path) MEASURES band-edge anisotropy slope
  **1.9999** (`a₂ = +0.056` dominant over `a₄ = −0.0017`, BOTH enantiomorphs;
  raw [100]–[111] speed-diff ratio = 4.0 = O(k²); fit returns 4.0 on a synthetic
  quartic ⟹ slope-2 is a genuine measurement). This CONFIRMS the prior 6×6
  k4_tlm caveat (`vol4/claim-quality.md:448`): the genuine lattice carries the
  isotropic O(k²) zone-edge term, so the eigensolve gives the **GENERIC slope-2**
  band-edge term. The slope-4 is a **re-stated INSERTED exponent**
  (`photon_omega_sq_over_c2k2` / `vacuum_node_circuit.photon_birefringence`
  hardcode the `1+κ_γ Ξ(kℓ)⁴` form). The distinctive quartic survives **ONLY
  conditional on the UNPROVEN weak-C "photon carries no zone-edge (q·ℓ)² term"
  theorem** (gate `wejkhvnfb`, OPEN). δ=0 continuum-exact is also NOT exact
  (max|ω²/c²k²−1| = 1e-3 at kℓ=0.08), OPEN on the same weak-C lever. **DEMOTED,
  not refuted** — the distinctive quartic could RETURN if weak-C is proven. The
  small-k emergent-Lorentz ISOTROPY SURVIVES (c(k→0)=1/√3, cross-axis spread=0):
  this is **band-edge anisotropy, NOT a low-k Lorentz violation**. MAGNITUDE =
  **ECHO** (`κ_γ = 1/24`) ~2–3 OOM **BELOW** current LIV/birefringence bounds
  (`vol4/claim-quality.md:449`) ⟹ **NOT near-term bankable** regardless.
- **Falsifier.** A facility-class observable resolving the `(qℓ_node)⁴`
  anisotropy above the ~2–3 OOM gap; or confirmation it stays beneath (then
  consistency-class). Note the FALSIFIER is now gated twice: the photon must
  carry a quartic-not-quadratic tell (weak-C, unproven) AND the magnitude must
  reach facility class.
- **Winding channel?** **NO.** Parity-EVEN, achiral (diamond point group). Not a
  parity test.

### 2.3 Field-free optical activity — `def-0pt1ac` (engine) + `def-wr1th3` (source); minted `clm-` this session (§9)

- **Claim.** A handed lattice rotates the polarization plane of a transmitted
  transverse wave with a **signed** rate that **flips sign between enantiomorphs**
  and is **exactly zero on the achiral diamond control** — sourced by the
  reflection-odd ring-writhe pseudoscalar (`def-wr1th3`, writhe ±0.04087,
  live-confirmed). The optical-activity response is `def-0pt1ac`
  (`common/vocabulary-register.md:545`).
- **SM/QED divergence.** **Parity ZERO-vs-NONZERO** — the cleanest possible
  divergence. QED vacuum is parity-even ⟹ field-free optical activity is
  *structurally* exactly 0 at any magnitude. AVE's chiral vacuum gives a nonzero
  signed rotation. This is a *qualitative* (presence/absence) divergence, not a
  coefficient comparison.
- **Derivation status.** FORM = **AVE-distinct + live-confirmed** on the parity
  axis (signed / enantiomorph-odd / diamond-null / writhe-sourced / lossless
  reciprocal gyrator — all SOLID, GATE-1 PR#374). MAGNITUDE = **NOT bankable**:
  the engine's `±75.46°/unit` is an **`ETA_ROT_PER_WRITHE = 1.0` engineering
  DECREE** (demoted PR#374, `common/vocabulary-register.md:551`,
  `chiral_lattice_vector.py:27,93`), and the **substrate-DERIVED** bulk g₀
  (Phase-1 EXECUTED, PR#374, OUTCOME A = the 4₁ screw pitch, ∓2.21589 rad /
  lattice-z-unit) converts to ~2.0×10¹² rad/m ≈ **40 OOM OVER** the cosmic
  bound (~4×10⁻²⁹ rad/m). The **k→0 continuum extraction is OPEN**
  (`research/2026-06-23_chiral-vector-tlm-phase1_result.md` §9).
- **Falsifier.** A measured field-free optical rotation that is *exactly zero*
  on a known-chiral configuration (within the lattice-handedness sign
  convention) would challenge the FORM; the magnitude is not yet a falsifier
  (40 OOM over bound + continuum-mapping open).
- **Winding channel?** **YES.** This is the winding/charge channel — the
  parity-axis observable. FORM solid; magnitude not bankable.

### 2.4 Writhe co-vs-anti-handed |F| ratio — Observable-C / "Stage-6": **CLOSED → RESOLVED-TO-CONSISTENCY** (2026-07-03)

> **STATUS HISTORY (edit-in-place, row preserved per KEEP-BOTH — the original UNBUILT framing stays below for provenance):**
> - **2026-06-24 → 2026-07-02:** UNBUILT; "highest-value unbuilt FORM chord."
> - **2026-07-03 (Gate-0, PR #465):** pair-feasibility STABLE-IN-A-WINDOW (d∈{34,44}); the arc proceeds.
> - **2026-07-03 (linear-channel campaign, this PR):** **CLOSED.**
>   - **Magnitude-R objective = BLOCKED** (Grant ruling C): R=|F|_co/|F|_anti is ill-defined at current engine capability — knot-overlap ⇒ no plane-conservative integral (plane spread 4.7–9.5×), + Yukawa screening ⇒ no source-free far-field (|F| falls 2.6e5× over d=34→44; ξ=c_ω/ω_gap≈0.548 cells, and ω_gap is a HOST KNOB so the range is artifact-scale).
>   - **Sign observable = RESOLVED-TO-CONSISTENCY** (Grant ruling α + Coulomb-recovery): the quantized pair does co-REPEL / anti-ATTRACT, which MATCHES signed-Coulomb under Axiom 2's winding=charge mapping — SM-shared, so by the symmetric standard NOT an AVE-distinct parity chord. Minted `clm-wcoul2` (the engine-derived Axiom-2 interaction leg: like windings repel / unlike attract, mediated by the gapped ω rotation sector, electrically not magnetically).
>   - **"Highest-value unbuilt FORM chord" designation = CLOSED** — resolved-to-consistency, **NOT falsified**: the winding-force question produced the Ax2 interaction leg instead of an AVE-distinct chord. Stage-(b) (κ_chiral saturation channel) = MOOT (no classical degeneracy fired the successor).
>   - Cross-ref: `research/2026-07-03_writhe-campaign-linear-channel_result.md` + `manuscript/ave-kb/vol4/claim-quality.md` (`clm-wcoul2`).

**[Below: the original UNBUILT framing, preserved for provenance.]**

- **Claim (proposed, not built).** A pairwise force whose magnitude depends on
  the **RELATIVE handedness** of two winding solitons — a **dimensionless**
  co-handed-vs-anti-handed |F| ratio. Because it is a ratio, it dodges the
  m_e/α-echo magnitude trap entirely.
- **SM/QED divergence.** A handedness-dependent force ratio ≠ 1; QED has no
  parity-odd vacuum force between like objects.
- **Derivation status.** **UNBUILT.** It *follows from* S1's winding-DOF, which
  **PASSED** (2026-06-24, `research/2026-06-24_engine-s1-winding-dof_result.md`:
  "the (2,3) winding is a separately-conserved DOF … upgrades A1-sustains-
  rotation from asserted-CLASS to derived-REAL," scoped to real-space ω +
  single-knot). Needs: a `T⁰ⁱ` momentum-flux observable, near-yield regime, a
  writhe-aware kernel. This is the cleanest forward prediction IF-S1-passed —
  and **S1 passed**.
- **⚠ DISTINCT from the FALSIFIED chiral-THRUST.** Do **NOT** list the thrust as
  live. The chiral rectification / dark-wake thrust is FALSIFIED:
  `research/2026-06-08_rrad-l-rectification_result.md` rectification ratios 0.62
  / 0.31 (chiral) — dominated by ordinary non-chiral common-mode radiation
  pressure; closed-by-derivation in the bulk near-yield regime
  (τ_bulk has no `sign(dρ̄/dt)` memory ⟹ cannot rectify a symmetric cyclic
  drive). The UNBUILT pairwise |F|-asymmetry is a **different** object (a
  static relative-handedness force ratio, not a cyclic-drive rectifier).
- **Falsifier.** Once built: a co-vs-anti |F| ratio of exactly 1 falsifies the
  winding-force chord.
- **Winding channel?** **YES** — and the highest-value unbuilt one.

### 2.5 GW echo / BH ringdown — `clm-rd9cjm` cluster: consistency-class

- **Claim.** Ringdown frequency from `ν_vac = 2/7` (`ω_R M_g = 18/49`).
- **SM/QED (here GR) divergence.** Reproduces GR at current LIGO sensitivity
  (<3% to Kerr for a* < 0.85); divergence only emerges at a* ≥ 0.90 (unobserved).
- **Derivation status.** ω_R DERIVED, but **consistency-class** at current
  sensitivity. The "echo" is **RETROSPECTIVE** — no SHA-pinned forward prereg.
- **Falsifier.** A high-spin (a* ≥ 0.90) ringdown deviating from Kerr; not
  currently reachable.
- **Winding channel?** **NO.**

### 2.6 GRB no-dispersion — C7 / `clm-gw2wgc`: corroborated-null

- **Claim.** No energy-dependent GRB arrival-time dispersion (continuum photon,
  weak-C). `vol4/claim-quality.md` (`clm-gw2wgc`).
- **SM/QED divergence.** **None at the observable** — AVE predicts the NULL,
  which *agrees with both* GRB090510 (31 GeV) + LHAASO 221009A (13 TeV) data
  **and** with SM. This is a **survival**, not a divergence.
- **Derivation status.** **corroborated-null.** Regime-grounded + empirically-
  corroborated; the decoupling theorem (δ = 0 exact, ω = ck) is **OPEN** (not
  derived; asserting it derived would be substitution-not-retraction, A47 v11b).
- **Falsifier.** A measured energy-dependent GRB dispersion would falsify; the
  existing nulls corroborate.
- **Winding channel?** **NO.**

### 2.7 Neutrino parity — C6: disclosed-import null-expected

- **Claim.** Right-handed-neutrino detection falsifies the ⅓ G_vac
  microrotational boundary of the chiral LC bandgap (`clm-gw2wgc` cluster).
- **SM/QED divergence.** A disclosed-IMPORT, **null-EXPECTED** falsifier — not a
  positive divergent prediction. (SM also expects effectively no light
  right-handed neutrino interaction.)
- **Derivation status.** Disclosed-import; tied to a named axiom, not an
  in-leaf derivation.
- **Falsifier.** Detection of a right-handed neutrino.
- **Winding channel?** **NO** (a chiral-bandgap boundary, not the writhe channel).

### 2.8 Torus-knot baryon ladder — C8 / `clm-to41c7` (0.60, "use as input only")

- **Claim.** Baryon masses from a curved torus-knot ladder.
- **SM/QED divergence.** A topological mass ladder vs SM's fitted Yukawas.
- **Derivation status.** **WALKED-BACK to postdiction.** Only the proton bare-
  topology hit + the curved-ladder FORM survive; the (2,21)→3199 entry misses
  the nearest state by **+8.4%**. `build_status: "use as input only"`.
- **Falsifier.** A predicted-but-absent state, or a state mass outside the
  ladder tolerance (the +8.4% miss is the live tension).
- **Winding channel?** Topological (knot winding) but **NOT** the parity/writhe
  channel; and it is a postdiction, not a forward chord.

---

### 2.9 Cleave-01 plate-displacement charge coupling — Ax2 bench: **RETIRED-AS-DISCRIMINATOR** (2026-07-02)

- **Claim (prior).** Mechanically displacing a capacitor plate pumps topological
  charge `Q = ξ_topo·x` (dQ/dx = e/ℓ_node = 414.9 fC/µm), a bench falsifier of
  Axiom 2 (`[Q] ≡ [L]`).
- **Derivation status → NULL-CONFIRMED-FINAL.** The coupling was ASSERTED (a
  `def-tk1xfm` unit-bridge, not a mechanism). A three-angle adversarial derivation
  returned UNDECIDABLE-AT-PAPER with a single surviving candidate — an adiabatic
  Thouless registry pump over the 4₁ screw. Grant ruled (b): the engine
  adjudicates. Both the 2-band
  (`research/2026-07-02_cleave-registry-pump-chern_result.md`) and the faithful
  **N-band** srs occupied-manifold Chern
  (`research/2026-07-02_cleave-registry-pump-chern-nband_result.md`) return
  **C = 0** in BOTH substrate readings (sliding + locked) and BOTH enantiomorphs
  (gapped, grid-converged, validate-on-known PASS). The registry-pump mechanism is
  dead; per Grant's frozen last-roll pre-commitment the coupling question CLOSES.
- **Disposition.** **AVE itself predicts the bench null** — there is no derived
  displacement pump. The bench is **corroborative-null class**: it is NOT a
  chord-confirming forward prediction. It retains one-sided value as a *falsifier*
  (a nonzero gap-independent integer floor surviving a ≥4× gap-sweep would still
  falsify AVE), so it is a **do-not-build-as-a-chord-confirmation** discriminator,
  kept only as a one-sided kill-test.
- **SM/QED divergence.** None at the derived level: both frameworks predict the
  null (SM: no displacement charge; AVE: C=0 pump). The `ξ_topo = e/ℓ_node` slope
  is a VALUE-import (unit-bridge), not an AVE-distinct magnitude.
- **Winding channel?** It probes the T2 winding sector, but the *derived* answer is
  a null — it is not a live winding-channel chord.

---

## 3. WINDING-CHANNEL SUMMARY (what S1 unlocks)

S1 (the (2,3) winding as a separately-conserved DOF) **PASSED** 2026-06-24
(`research/2026-06-24_engine-s1-winding-dof_result.md`, PASS-WITH-FLAGS,
derived-REAL, scoped to real-space ω director-phase + single-knot conservation;
`make verify` PASS). With the winding now a genuine independent DOF, its
distinct prediction is **PARITY** — the cleanest possible divergence axis,
because **QED vacuum is parity-even and therefore structurally pinned to exactly
zero** on any chiral-vacuum observable.

Two winding-channel observables sit on this axis:

| Observable | FORM | MAGNITUDE | Status |
|---|---|---|---|
| Field-free OA sign-flip (§2.3) | AVE-distinct, live-confirmed (signed / enantiomorph-odd / diamond-null) | **NOT bankable** — ~40 OOM over cosmic bound; k→0 continuum OPEN | minted `clm-` (§9) |
| Co-vs-anti |F| ratio (§2.4) | ~~follows from S1's PASS; dimensionless (dodges echo trap)~~ → SIGN = signed-Coulomb (SM-shared, not parity-distinct) | **magnitude-R BLOCKED** (overlap + Yukawa) | **CLOSED → RESOLVED-TO-CONSISTENCY** (2026-07-03; `clm-wcoul2`, Ax2 interaction leg) |

**Not winding channels** (real divergences, but parity-mute): E-route
birefringence (§2.1, field-induced, even-in-k) and the (qℓ_node)⁴ dispersion
(§2.2, parity-even, achiral diamond point group).

**Net for the winding lane (updated 2026-07-03):** the FORM of the parity
divergence is solid on the OA observable (§2.3, still minted, still 40 OOM over
on magnitude). The co-vs-anti |F| ratio (§2.4) is now **CLOSED**: built through
Gate-0 + the linear-channel campaign, its magnitude-R is BLOCKED (overlap +
Yukawa) and its SIGN resolved-to-CONSISTENCY (signed-Coulomb under the Ax2
winding=charge mapping — SM-shared, not parity-distinct). It did NOT bank as a
chord; it produced the engine-derived Axiom-2 interaction leg instead
(`clm-wcoul2`). So the winding lane's chord hope now rests on the OA
observable alone (§2.3); the |F|-ratio path is spent (resolved-to-consistency,
not falsified).

---

## 4. CROSS-REFERENCE NOTE (master matrix is a gated follow-on)

The canonical C1–D5 divergence matrix lives at
`manuscript/ave-kb/common/divergence-test-substrate-map.md`. This register is a
**derived-vs-echo consolidation lens** over a subset of those rows, not a
replacement. A light cross-ref pointer to this register has been added to that
map; **full integration of these derived-vs-echo verdicts into the C1–D5 matrix
is a GATED FOLLOW-ON** (it would rewrite load-bearing matrix rows and must be
adjudicated separately — flag-don't-fix). Do not treat this register as having
superseded any matrix row.

**Flag-don't-fix log (drift from source map on re-grep):** none. All cited
file:line confirmed at HEAD `dc9e1791` — `clm-pp3qwf` body at
`vol4/claim-quality.md:389`, the `7.5/α³` ratio at `:399`, `clm-k4d4ph`
slope-4-asserted at `:448` and ECHO-below-bounds at `:449`, `V_YIELD = √α·V_SNAP`
at `constants.py:460`, `def-0pt1ac` ETA-decree demotion at
`vocabulary-register.md:551`, the OA OUTCOME-A + 40-OOM caveat at
`research/2026-06-23_chiral-vector-tlm-phase1_result.md` §0/§9, S1 PASS at
`research/2026-06-24_engine-s1-winding-dof_result.md`, chiral-thrust FALSIFIED at
`research/2026-06-08_rrad-l-rectification_result.md`. Q=137 slot left EMPTY (no
α re-pose).
