# Smith-annulus computation lane — research-doc DRAFT (repaired 2026-08-24)

**Status: WALK-grade-under-test. Nothing here is canon; nothing here is a chord claim.**
Prereg-light: expectations were frozen in `2026-08-24_smith-annulus_expectations_FROZEN.md` BEFORE the first
script run (that file is the receipt and is untouched; §2 below is a CONDENSATION of
it, not a copy). Scripts: `drivers/smith_annulus_comp.py`; raw numbers: `drivers/smith_annulus_results.json`.
This revision is the post-adversarial-verify repair pass (3 lenses, 17 findings);
the repair ledger is §9.

**Model-scope banner (binding, added at repair):** every T1 number in this draft is
computed in the **ISOLATED-JUNCTION reading** — far arms terminated as matched
semi-infinite lines. That is an S-matrix reference convention, not the in-lattice
steady state; its own receipt says so: *"Same junction, two terminations."*
(`research/2026-07-10_x38-s11-bore-selection_derivation.md:23` — X37 embeds the
junction in the periodic lattice/Bloch, X38 terminates in matched lines). The
in-lattice reading is computed in §3.2b and it materially changes the physical
register (§3.3, §4). STUCK-POINT #6.

**Context anomaly, logged first:** the dispatch's open item
`2026-08-24-smith-annulus-tube-ratio-pin.md` does not exist in the AVE-Core
checkout (`_orchestration/open-items/` listed; two grep methods; matching all three
pull-phase lanes' independent findings). This lane executed from the dispatch spec +
Grant's verbatim directives alone. STUCK-POINT #1.

**Standing-item pointer (PARKED — named per the park, minting nothing):** the
adjacent open item `_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md`
is **Grant-PARKED** (status: PARKED, opened 2026-08-18): the Smith-chart-ontology
canonization ("Γ disk = ℂP¹ …, one chart per sector" as ontology) is parked, and its
stated re-open condition is *"an engine lane actually wants the dual-sector Smith
chart as a live instrument."* This WALK lane USES the Γ-disk as a working
coordinate plane, which is at least adjacent to that condition — **flagged for
Grant; un-parking is Grant's alone. Nothing in this draft canonizes, extends, or
adjudicates any Smith-chart ontology; every chart statement below is either the
already-canonical practical layer (`cvr-reflection-smith.md`, which the park item
itself lists as NOT parked) or plain circuit arithmetic.**

Grant's dispatch directives (verbatim, frozen 2026-08-24):

> Q1: "run the comp, but we should think through eigenvalues/modes, and what the
> transduction is from phase to real space is, and give the biquarternion network
> equations a glancing view"
> Q2: "we should think through the ideal case, and what's physically or logically
> justified under AVE alone as a non ideal correction"
> Q3: "the lock must depend on the vacuums uniforms impedance, and how that couples
> to the lattices backreaction?"

## 1. Regime declaration (binding)

- **MODE/REGIME/PHASE-STATE:** small-signal AC on a cold, sub-yield,
  lossless-reactive lattice (Axiom 3): uniform Z₀ on every bond, *"perfectly matched
  everywhere; reflection coefficient $\Gamma = 0$ at every bond"* (photon-identification.md:113).
  Amplitude grading enters ONLY through the canonical kernel, the *"universal
  quarter-arc kernel"* S(A)=√(1−A²) (ave-kb/CLAUDE.md:73), via the trajectory
  `replaced by the canonical $Z_0\sqrt{S}$ trajectory` (resonant-lc-solitons.md:41),
  same object in the master-equation status note `$Z=Z_0\sqrt{S}$, $|\Gamma|=1$ both ways`
  (master-equation.md:106 — that line is the 🔴 B3-DEGENERATE/sign-selector banner;
  status carried: the magnetic-vs-electric fork is a chirality sign-selector, not the
  cage mechanism).
- **k·ℓ regime declaration (added at repair):** the T1 sweep spans θ = k·ℓ ∈ (0,π).
  Canon scopes the bare −1/3 event by wavenumber ON THE SAME LINE as the counting
  fact: it is "homogenized away for in-band collective carriers"
  (manuscript/ave-kb/common/translation-tables/translation-circuit.md:189, the T4-fork-close clause; σ≈0.12 of the incoherent
  limit, resolving only near the band edge, "crosses $1/9$ at $k\cdot\ell\approx1.85$",
  with "band edge not independently located (probe reached $k\cdot\ell\le0.83$)").
  So: θ ≲ 0.83 is the canon-validated in-band regime where the bare floor is NOT the
  operative steady-state reflection; θ ≈ 1.85 is where canon says it resolves; the
  n=1 comb at θ = π sits ABOVE that crossing and beyond the validated probe range.
  Every §3 number carries this scoping. This is also how the two baseline receipts
  coexist: photon-identification's Γ=0-everywhere cold lattice and the bare-vertex
  −1/3 are reconciled BY the k·ℓ homogenization, not by this lane.
- **Coordinates:** phase-space throughout. Every T1–T3 object lives in the Γ-plane
  (reflection-coefficient disk) — the SAME plane as the mark's `trefoil_gamma`,
  radial profile `rho = (R + r * np.cos(TUBE_SENSE * 3.0 * t)) / (R + r)`
  (smith_sim.py:59-68 — **cross-repo receipt: this file lives in the
  `the-electron-plumber` repo at `animations/smith_sim.py`, NOT in AVE-Core**).
  No real-space quantity appears before §6 (T4a).
- **SECTOR DECLARATION (chart ownership):** the graded Γ(A) here is built from the
  Z₀√S→0 trajectory, so the chart's radial coordinate is the **A1-longitudinal tank
  sector's Γ** (short wall, Γ→−1); the transverse-T2 rupture (Z→∞, Γ→+1) is a
  distinct impedance "belonging on its **own** Smith chart" per the dual-sector
  reading, "one chart per sector" (cvr-reflection-smith.md:80; sector split
  Grant-ratified 2026-06-15, "differing only in boundary phase" — ave-kb/CLAUDE.md:73).
  The −1/3 junction floor is "a COUNTING fact" on whichever channel has uniform Z₀
  (manuscript/ave-kb/common/translation-tables/translation-circuit.md:189) — sector-agnostic in form; used here on the A1 chart.
  The mark's chart is generic; no silent A1/T2 cross-wiring occurs below.
  **Chart-declaration scope (corrected at repair):** this declaration fixes which
  wall SIGN is the physically-relevant one on this chart (Γ→−1). It does NOT
  adjudicate the FORM J/B side-assignment fork — see §3.4 H1.
- **Coordinate fence (do-not-weld):** the mark's (R=2, r=1) parametrize the Γ-disk
  radial profile ρ(t)=(R+r·cos3t)/(R+r). The Golden-Torus (R=φ/2, r=(φ−1)/2,
  R·r=1/4) are (V_inc,V_ref) phasor-ellipse semi-axes (Q-EMBED step-c:36,55).
  **Different objects in different coordinates.** The mark's own comment says the
  same: "Tube ratio is a MARK geometry, not an electron-body claim" (smith_sim.py:16-17).
  Nothing below welds them; §3.4 states what the comp actually pins.

## 2. FROZEN EXPECTATIONS (condensed; the standalone file is the receipt)

**Receipt-integrity correction (2026-08-24 repair):** the prior revision of this
draft claimed this section was *"byte-identical"* to `2026-08-24_smith-annulus_expectations_FROZEN.md`. That
was FALSE — the section was always a ~2.2k-char condensation of the ~6.5k-char
frozen file. The claim is withdrawn; what follows is an honest condensation, with
the frozen file quoted verbatim (fenced) where load-bearing. The frozen file itself
is untouched, before and after this repair.

**Frozen-prior defect, flagged (not silently corrected):** frozen E6, under the
header "Ranking at onset expected:", lists drive/back-reaction (item 3, "≲1e-18")
ABOVE the thermal floor (item 4, "≈ 5e-11") — the frozen prior mis-ranked those two
by ~8 orders of magnitude against its own quoted numbers. The previous draft
revision silently re-ordered them in §4; this revision states it: **a frozen
expectation was internally inconsistent, and §4's corrected ranking places thermal
(row 4) above drive/back-reaction (row 5), inverting the frozen prior's item
order.** (Every individual magnitude in the frozen file is numerically fine; only
the list order was wrong.)

Model, verbatim from the frozen file:

```
One srs bond = lossless Z₀ line, delay θ = ωℓ_node/c. Each end terminates on a
z=3 shunt junction whose other two bonds are matched semi-infinite Z₀ lines
(x38-s11 derivation:15,46), so each end presents Z₀/2 and the end reflection
seen from inside the bond is Γ_end = (½−1)/(½+1) = −1/3, which must equal
scatter_matrix(3)[0,0] = 2/3 − 1 = −1/3 (chiral_lattice.py:81-102).
```

Graded end reflection, two candidate forms, verbatim from the frozen file
(side-assignment tagged UNDERIVED-CHOICE there and here):

```
- FORM J (junction/far-side graded): load = √S·Z₀/2 against cold bond reference
  Z₀ → Γ_J(A) = (√S/2 − 1)/(√S/2 + 1).
- FORM B (bond graded, cold junction): bond reference Z₀√S against load Z₀/2
  → Γ_B(A) = (1/2 − √S)/(1/2 + √S).
```

Expectations, condensed: **E1 (H1)** endpoints |Γ|=(1/3,1) exact for both forms,
wall sign form-dependent (J:−1, B:+1). **E2** composite from an exterior line:
−1/2 at DC; min 1/5 at θ=π/2; below 1/3 in a finite band; never 0; unitary.
**E3** poles θ_n = nπ + j·ln9/2, Q_n = nπ/ln9 ≈ 1.430n; SWR 2; graded
Q(A)→∞ at yield *(that →∞ is corrected at repair — §3.3 (Q ≤ 428.9n) and §4 row 3: the canonical wall
leak caps it)*. **E4 (H2)** annulus [1/3,1] = monotone image of |Γ_J(A)|; FAILS
for FORM B (chart-centre crossing at A=√15/4). **E5 (H3)** endpoints reproduced,
shape not; endpoints alone pin ρ_min=1/3 ⇒ R/r=2; amplitude laws N1/N2 both
UNDERIVED-CHOICE. **E6 (T2)** near cold |Γ_J|≈1/3+A²/9; item order defective as
flagged above. **E7 (T3)** first-order ε₁₁ detuning DELAY-ONLY (δω/ω=−ν_vac·ε₁₁,
ν_vac=2/7, Op19, UNDERIVED-EXTENSION); impedance detuning second order; floor
immune to symmetric bias *(that immunity claim is REPAIRED in §5 — it conflated
two different symmetric operations; one is exact at all orders, the other moves
the floor at O(ε²))*.

## 3. T1 results (all numbers from `drivers/smith_annulus_results.json`, regenerated by the repaired script)

### 3.1 End-reflection check

`scatter_matrix(3)[0,0] = −1/3` (the engine's shunt-KCL scatter,
`S_ij = 2/n - delta_ij`, chiral_lattice.py:81-102) and the impedance route (Z₀/2
load) agree to machine precision. Scope: this is the bare-vertex counting fact in
the isolated-junction reference convention (§ banner); its in-lattice standing is
§3.2b.

### 3.2 Composite two-junction reflection vs frequency — the matching-section answer

**Within the isolated-junction model: YES, the locked one-bond spacing produces
composite |Γ| below 1/3 over a wide band.**

- DC limit |Γ|=1/2 (the two junctions merge into an effective z=4 node: 2/4−1=−1/2 ✓).
- Minimum |Γ| = **0.2000 at θ = π/2** (quarter-wave: the ℓ_node bond transforms the
  far junction's Z₀/2 into 2Z₀; paralleled with the near junction's own Z₀ arm →
  Z_par=(2/3)Z₀ → Γ=−1/5). E2 exact.
- Below-1/3 band, **root-found** (bisection on |Γ(θ)|=1/3 to 1e-14, replacing the
  prior grid-sampled edges whose trailing digits were spurious):
  **θ ∈ (0.8410686705679, 2.3005239830219)** — 46.46% of the (0,π) band, centred on
  quarter-wave; the two edges sum to π to 6e-15 (exactly symmetric about π/2, which
  the grid-sampled values had masked). Never reaches 0.
- Full 4-external-port S-matrix unitary to **6.7e-16 across the ENTIRE 20001-point
  sweep** (repaired: the prior draft checked 3 spot frequencies and reported the
  property unqualified; it is now checked at every θ used for the band claim).
  Axiom-3 lossless honest.

So within this model the fixed ℓ_node spacing is a matching section near its
quarter-wave frequency: two locked z=3 junctions reflect LESS than one. **Physical
register, scoped:** this composite interference is itself a same-lattice mechanism
of exactly the kind §3.2b shows the full lattice supplies — it is bookkeeping about
the isolated-junction convention, not a steady-state lattice prediction.

### 3.2b In-lattice embedding (added at repair) — what the lattice actually presents

The matched-arm termination deletes the lattice's band structure. Closing the SAME
model class self-consistently (identical Z₀ bonds + z=3 shunt junctions, loop-free
Bethe-tree closure; `drivers/smith_annulus_results.json` block `embedding`), the branch impedance obeys
`j*t*z^2 + z - 2*j*t = 0` (t = tanθ), end load = z/2:

- **In-band the end reflection is BELOW the floor:** |Γ_end| = 3−2√2 ≈ **0.1716**
  at θ=π/2 (analytic, matches numeric to 1e-15).
- **Purely reactive stopband:** |Γ_end| = 1 for θ < 0.3398 and θ > 2.8018 (the
  Bloch load goes reactive; no propagating band to leak into).
- **|Γ_end| is within 5% of 1/3 on only ~3.4% of (0,π).** The −1/3 floor is a
  reference-convention number, not the lattice's steady-state end reflection at
  essentially any frequency.
- **At the comb frequency θ = π the tree termination degenerates to a SHORT:**
  shell-depth recursion gives |Γ_end| = 0.333, 0.600, 0.778, 0.882, 0.939, 0.969 →
  1 (depths 1–6 → ∞). Half-wave-invisible bonds pile the junctions up coherently.
- Direction agrees with canon's own in-band measurement: the per-vertex 1/9 is
  "homogenized away for in-band collective carriers" (manuscript/ave-kb/common/translation-tables/translation-circuit.md:189,
  σ≈0.12 of the incoherent limit — same-line clause the prior revision omitted).
  The srs net's loops soften the tree idealization; an engine run on the actual srs
  net would arbitrate (STUCK-POINT #6).

### 3.3 Eigenvalues/modes (Grant Q1) — TRUNCATION-ARTIFACT-SCOPED at repair

Within the isolated-junction truncation, poles of the composite sit at
θ_n = nπ + j·ln9/2 (Newton, perturbed seeds, machine-exact), i.e. ω_n = nπ·c/ℓ_node
with Q_n = nπ/ln9 = 1.4298·n, SWR 2 on the bond, ends at 0.50 of the antinode.

**These are artifacts of the shell-1 truncation, not lattice modes.** The repair
evidence (§3.2b): at the very frequency θ=π where the comb is quoted, the embedded
lattice presents a SHORT (|Γ_end|→1), so the embedded bond at its own comb is a
leak-free cold trapped mode, NOT the "grossly leaky resonator, Q₁≈1.43, a shoulder
in the continuum" the prior revision described — that Q is maximally wrong exactly
at the frequency it was quoted for. In-band, the tree end-reflection is ~0.17–0.21,
below the floor. Additionally the n=1 comb at k·ℓ=π sits above canon's band-edge
crossing (≈1.85) and beyond the validated probe range (k·ℓ≤0.83)
(manuscript/ave-kb/common/translation-tables/translation-circuit.md:189, "band edge not independently located (probe reached $k\cdot\ell\le0.83$)").
The prior revision's narrative "the confinement Q is entirely a wall effect, all of
it arriving in the last few percent of amplitude" is WITHDRAWN — in the embedded
picture the lattice's band structure supplies confinement at the comb with no
Axiom-4 wall engaged at all.

**Graded Q within the truncation (bookkeeping only):** Q(A)/n = 1.4330 at A=√α,
1.558 at A=0.5, 4.13 at A=0.99. The prior "→∞ as A→A_y (TIR closes the leak)" is
corrected twice over: (i) it is truncation-scoped as above; (ii) even at the wall
canon caps it — the wall reflectivity is `|\Gamma|^2 = 1 - \alpha`
(cvr-reflection-smith.md:38), giving Q ≤ nπ/(−ln(1−α)) ≈ **428.9·n, finite**, with
the leak "falls short of unity by exactly the fine-structure constant"
(cvr-reflection-smith.md:73). The Γ→−1 TIR self-creation statement itself is
canonical ("Γ \to −1 TIR cavity self-creates", photon-identification.md:140) — what
is corrected is the exact-unity reading of it.

### 3.4 Graded Γ(A) — H1/H2/H3 verdicts

**H1 — PASS (magnitudes exact); wall-sign framing CORRECTED at repair.**
Both forms give |Γ| endpoints (1/3, 1) to machine precision. FORM J walls at Γ=−1;
FORM B at Γ=+1. The prior revision identified these two signs with canon's two rim
points at ave-kb/CLAUDE.md:73 (*"differing only in boundary phase"*). **That
identification was FALSE:** the ave-kb/CLAUDE.md:73 rim pair (*"the two sectors' impedances"*) is the SECTOR pair — A1 tank
Z→0 (Γ=−1) vs transverse-T2 wave impedance √(μ/ε)→∞ (Γ=+1 rupture), two different
impedance OBJECTS. FORM B is not that object: its +1 arises because the collapsing
bond is used as REFERENCE (Γ=(Z_L−Z_ref)/(Z_L+Z_ref)→+1 as Z_ref→0), with nothing
diverging. Both J and B are A1-trajectory objects; the A1/T2 sector split
adjudicates neither. Likewise the prior "Choosing the A1 chart declared in §1
selects FORM J" was CIRCULAR (the chart declaration presupposes the −1 wall) and
contradicted the lane's own stuck point; withdrawn. **The side-assignment fork
stands fully open as STUCK-POINT #2.**

**H2 — PASS for FORM J only, RE-HEADLINED at repair: the annulus is the medium's
response map, not any orbit the electron takes.**
|Γ_J(A)| is monotone onto [1/3, 1] — as a MAP, A ↦ Γ. FORM B is not (chart-centre
crossing |Γ|→3e-6 at A=√15/4=0.96825, a real matched event; exits the annulus).
But canon pins the standing electron's A1 amplitude FIXED at the operating point:
"the electron's A1 mass core operates at strain" A=√α, "sub-saturated ($S(\sqrt\alpha)=\sqrt{1-\alpha}\approx0.996$)"
(vocabulary-register.md:757, def-vyvsn1); "the confining $\Gamma=-1$ wall is supplied by the *transverse* $T_2$ self-trap at $V_{yield}$, not by any A1-varactor divergence" (nonlinear-vacuum-capacitance.md:36);
*"the $S\to0$ varactor runaway
never fires on the mass channel"* (pair-production-axiom-derivation.md:103). On this
chart the electron sits at |Γ_J(√α)| = 0.334147 — **0.12% into the [1/3,1] annulus,
99.9% short of the outer edge — and does not sweep.** So H2's PASS means: the
annulus is the image of the response map Γ_J over the HYPOTHETICAL amplitude range
[0,A_y]; no canon statement makes any physical amplitude execute that swing, and
def-vyvsn1 pins the one physical A1 operating point near the inner edge. A→A_y=1
on this kernel normalization means V→V_snap (Schwinger/pair-nucleation), not a
standing-electron trajectory.

**Lumped-step caveat on ALL intermediate-A quantities (added at repair):** FORM J
and FORM B are both zero-length STEP discontinuities, and there is a third,
unexplored option: a spatial TAPER (the physical grading is an amplitude FIELD over
many cells, and a lossless taper's reflection is frequency-dependent and suppressed
relative to the equivalent step). Every intermediate-A number in this draft — the
A²/9 coefficient, hence the §4 width entries and the §5 differential-bias split —
is a lumped-step-family artifact; only the endpoints are profile-robust (A=0 →
bare vertex; A→A_y → |Γ|→1 for any profile reaching Z→0, up to the α-leak). FORM J
as implemented also grades the ENTIRE semi-infinite far arms uniformly, which no
localized winding can do — an infinite-extent saturation, in tension with the
localization framing of STUCK-POINT #2 itself. Folded into STUCK-POINT #2.

**H3 — ENDPOINTS-ONLY, decisively.**
Against the mark's ρ(t)=(2+cos3t)/3: both natural amplitude laws reproduce the
endpoints exactly but miss the shape badly — max deviation 0.433 (N1) / 0.375
(N2), harmonic distortion **72% / 54%** vs the mark's exact 0% (vs the frozen
prior's "several-percent" expectation — the prior was wrong by an order of
magnitude, reported as such). The inverse A_req(t) that WOULD reproduce the mark
exists (sweeps [0,1]) but resembles neither natural law (max dev 0.65/0.40, corr
0.77/0.89) and is not a recognizable simple form.

**What endpoints-only pins — SOFTENED at repair.** ρ_min = (R−r)/(R+r) = 1/3 ⇒
R/r = 2 in the mark's parametrization, matching the mark's (R=2, r=1). But the
prior claim "pinned by the two impedance facts alone … with zero freedom"
over-counted: in the mark's own family the outer tangency ρ_max=1 is enforced by
the /(R+r) normalization BY CONSTRUCTION — the mark's code says so:
"/(R+r) always hits the rim." (smith_sim.py:23) — so the family has ONE free ratio
and the single physics input ρ_min=1/3 does all the pinning; the Axiom-4-rim "fact"
is consumed by the mark's normalization convention. And R=2r was a design INPUT of
the mark (*"R=2r and R+r=1 so the vertical shadow of the torus curve is the flat
trefoil touching the rim"*, smith_sim.py:15-16), so this is a consistency identity
against a chosen mark parameter, not an independent recovery. The 1/3 itself
inherits the §3.2b scoping (bare-vertex, matched-reference convention). Per the §1
fence this pins the **Γ-disk annulus ratio**, NOT the Golden-Torus phasor-ellipse
R/r — different object; no weld.

## 4. T2 — ideal case + AVE-only non-ideal corrections (Grant Q2) — RE-RANKED at repair

**Ideal case, scoped:** cold lattice, exact uniformity, isolated-junction reading.
The inner edge |Γ|=1/3 is the bare-vertex counting event, *"immune to symmetric
transformation"* (manuscript/ave-kb/common/translation-tables/translation-circuit.md:189) — AND, same line, *"homogenized away
for in-band collective carriers"* in the embedded steady state. The outer edge is
NOT exactly |Γ|=1: canon's wall reflectivity is `|\Gamma|^2 = 1 - \alpha`
(cvr-reflection-smith.md:38). So even the "ideal" annulus edges carry AVE-canonical
structure: [1/3 (convention-scoped), √(1−α) ≈ 0.99634].

Width sources justified under AVE alone (closed form near cold: |Γ_J| ≈ 1/3 + A²/9;
all intermediate-A entries carry the §3.4 lumped-step caveat):

| # | Source | Mechanism + receipt | δ\|Γ\| scale |
|---|--------|--------------------|-----------|
| 0 | **Surrounding-lattice loading (inner edge)** — ADDED at repair | the embedded end reflection differs from −1/3 by O(0.1–0.5) across the band (§3.2b Bethe numbers: 0.17 in-band, 1 in stopband/at comb); the largest AVE-native correction, previously omitted while its own mechanism (§3.2 composite interference, min 0.2) was being measured | **O(0.1–0.5)** — dominant; termination-model-dependent (STUCK-POINT #6) |
| 1 | **Outer-edge radiative α-leak** — ADDED at repair | wall reflectivity "falls short of unity by exactly the fine-structure constant" (cvr-reflection-smith.md:73); outer edge sits at √(1−α), offset 1−√(1−α) = 3.655e-3 ≈ α/2. **Status-carry:** the leaf tags this Class-B "value-level echo" (cvr-reflection-smith.md:80) — echo-class, admissible by the same standard as row 2 — AND carries the Ruling-12 contour tag (cvr-reflection-smith.md:49-55): √(1−α)=0.996345 is the *"STORAGE clock"*, near-colliding with the response clock (1−2α)^(1/4)=0.996331 (Δ=1.4e-5); *"the rate alone cannot discriminate the contour — always carry the tag"* | **α/2 ≈ 3.66e-3** — dominant among edge-local widths; 4.5× row 2 |
| 2 | **Saturation operating-point offset (inner edge)** | electron A1 core at A=√α, "BOTH are **CALIBRATION, not derived**" (vocabulary-register.md:753, def-vyvsn1) ⇒ inner edge sits at \|Γ(√α)\|, not 1/3 | α/9 ≈ 8.1e-4 (numeric 8.14e-4) — echo-class |
| 3 | **Radiative loading (frequency width)** | 1/Q leak through the ends; Δω/ω = ln9/(nπ) ≈ 0.70/n in the truncation — but §3.3: comb/Q are truncation artifacts, and the wall-closed ceiling is Q ≈ 428.9n (α-leak), not ∞ | 0.70/n → α/(nπ) ≈ 2.3e-3/n (floor, = 1/Q at the wall-closed ceiling), an ω-width not a \|Γ\|-width |
| 4 | **Thermal floor at T_CMB** | equipartition k_B·T_CMB against the m_ec² bond quantum: A_th=2.14e-5 (estimator UNDERIVED-CHOICE, STUCK-POINT #3) | A_th²/9 ≈ 5.1e-11 |
| 5 | **Drive / back-reaction** | ε₁₁ into the kernel `A = clip(|ε₁₁|, 0, 1)` (backreaction.py:16) — but see §5: for a UNIFORM long-wavelength strain the floor is ratio-invariant at ALL orders; the physical width is set by ∇ε₁₁ across one node, many orders below ε₁₁²/9. The ε₁₁²/9 figure presupposes the FORM-J side-assignment (UNDERIVED-EXTENSION tag, §5) | ≪ ε₁₁²/9 ≈ 2.2e-19 (mechanism corrected at repair) |

**Ranking at onset (corrected): #0 ≫ #1 ≫ #2 ≫ #4 ≫ #5, with #3 orthogonal (an
ω-width).** The prior revision ranked #2 (α/9) "dominant" — that stood only by
omitting the outer-edge α-leak (4.5× larger, sitting ~10 lines from a receipt the
lane already had open) and the surrounding-lattice loading (~100–500× larger, the
very mechanism its own §3.2 was measuring). This ranking also FLAGS the frozen-E6
order defect (§2). The dominant physical annulus-edge widths are the embedding
term and the OUTER-edge α-leak, not the inner-edge operating-point offset; note
rows 1 and 2 are both echo-class (imported-α inheritance), so no width here is a
new prediction.

## 5. T3 — the lock, uniform impedance, back-reaction (Grant Q3) — REPAIRED

Grant's hypothesis, verbatim: *"the lock must depend on the vacuums uniforms
impedance, and how that couples to the lattices backreaction?"*

**Structure of the lock.** The two-junction phase lock = (i) both ends present
exactly Z₀/2 because every arm is at uniform Z₀ ("perfectly matched everywhere",
photon-identification.md:113), giving equal Γ=−1/3 with equal phase π; (ii) equal
bond delay ℓ_node/c. **So yes — within the model, the lock depends on the vacuum's
uniform impedance exactly as the hypothesis says: uniformity is what makes the
floor a pure counting fact** (scoped per §3.2b to the isolated-junction reading).

**How back-reaction couples (first-pass analytics; every coupling route tagged):**

- **First order in ε₁₁: DELAY ONLY.** The only canon coupling linear in ε₁₁ is
  refractive: `n(r) = 1 + (ν_vac) · ε₁₁(r)` with ν_vac = 2/7 (gravity/__init__.py:45;
  Op19, "how slow is propagation?" — universal_operators.py:1088). Bond delay
  θ → θ(1+ν_vac ε₁₁), so the comb detunes as δω_n/ω_n = −(2/7)·ε₁₁.
  **TAG: UNDERIVED-EXTENSION** (regime transplant, gravity sector → bond lock).
- **Impedance route, tag SYMMETRIZED at repair:** feeding ε₁₁ into the junction
  reflection kernel via `A = clip(|ε₁₁|, 0, 1)` (backreaction.py:16) is the SAME
  regime-transplant class — that docstring defines a Stage-3 gravitational
  fixed-point construct, not a junction-reflection statement. The prior revision
  tagged only the Op19 route and left this one receipt-direct; both now carry
  **UNDERIVED-EXTENSION**. δZ/Z = −ε₁₁²/4 (second order; no linear Z(ε₁₁) exists in
  canon — pull absence, verified two ways).
- **Symmetric bias, CORRECTED (this replaces the prior contradictory pair of
  claims).** Three distinct cases, now all computed in `drivers/smith_annulus_results.json` T3_lock:
  1. **UNIFORM grading (every arm, reference bond included, scales to Z₀√S):**
     Γ_end = −1/3 **EXACTLY, at ALL orders** (computed at A = 0.1/0.5/0.9/0.999;
     max deviation 5.6e-17). This is the corpus's actual *"immune to symmetric
     transformation"* statement (manuscript/ave-kb/common/translation-tables/translation-circuit.md:189) — a uniform impedance
     scale factor cancels in Γ=(2−z)/z. The prior claim of first-order-only protection was an
     UNDERSELL of this case.
  2. **SYMMETRIC END bias under FORM J (both junction sides graded equally, bond
     held cold):** the floor MOVES at O(ε²): |Γ₁Γ₂| = (1/9)(1+2ε²/3); computed at
     ε=1e-3: 0.11111118519 vs cold 1/9 (matches prediction to 5e-14). The prior
     sentence "Only a DIFFERENTIAL end-to-end bias breaks the floor" was FALSE in
     the lane's own model — it was contradicted by the formula two lines below it.
     Holding the bond cold while grading the junctions is an implicit
     bond-vs-junction DIFFERENTIAL, so this whole case presupposes the
     STUCK-POINT-2 side-assignment.
  3. **DIFFERENTIAL end bias (ε₁≠ε₂):** additionally SPLITS the inner edge by
     (ε₁²−ε₂²)/9; numeric check at ε₁=1e-3, ε₂=0: product 0.111111148148 vs
     predicted, agree to 1e-13; Q/n 1.4298004 → 1.4298007.
  The former drivers/smith_annulus_results.json field `floor_immune_to_symmetric_bias: true` was a
  HARDCODED literal (reconcile-don't-declare violation); it is REPLACED by the
  computed fields `floor_invariant_under_UNIFORM_grading_all_orders` (computed
  true, dev 5.6e-17) and `symmetric_END_bias_form_J.moves_floor` (computed true).
- **Physical consequence for T2 row 5:** a long-wavelength gravitational ε₁₁ is
  uniform across a bond and its junctions — case 1, ratio-invariant at all orders —
  so the physical back-reaction |Γ|-width is set by the ∇ε₁₁ DIFFERENTIAL across
  one node, many orders below ε₁₁²/9. (Ranking unaffected; mechanism corrected.)
- **Sanity: two-way back-reaction exists in-engine** (backreaction.py solves the
  saturating-modulus fixed point), but the lock-detuning formulas here are
  first-pass analytics, not verified in-engine (STUCK-POINT #4).

## 6. T4a — transduction, phase → real space (Grant Q1)

What canon provides for mapping the Γ-plane annulus to real-space observables —
three routes, and only three (all from pull receipts):

1. **TKI dictionary (Axiom 2):** charge as *"a discrete geometric dislocation (a
   localised phase twist)"* with ξ_topo ≡ e/ℓ_node (axiom-definitions.md:21-28);
   the translation `L = \xi^{-2} m`, C=ξ²κ, Z=ξ⁻²η (xi-topo-traceability.md:133).
   This maps IMPEDANCES, not chart geometry: it says what Z₀ and Z₀√S are
   mechanically; it does not transport the annulus's shape anywhere.
2. **Envelope law — quotient map stated explicitly (repaired):** the primer's
   phasor plane is the I/Q (d-q) plane — its axes are the E-quadrature and
   B-quadrature of one bond's real-space node DOFs (electron-plumbing-primer:24,41-43).
   The annulus does NOT live there: it lives in the Γ-disk, the QUOTIENT of the
   (V_inc, V_ref) pair — Γ = V_ref/V_inc, a ratio of the I/Q phasors, one Möbius
   projection downstream of the plane the primer receipt describes. With that map
   stated: |Γ| is a ratio of real wave amplitudes, and only the time-averaged
   ENVELOPE of the orbit survives projection to a real-space observable
   (electron-plumbing-primer:46).
3. **M/Q/J boundary law:** at a Γ=−1 surface exactly three integrated quantities
   are externally observable; "interior eigenmode wavelengths, microrotation
   profiles, soliton topology ... are invisible" (boundary-observables:20,37).
   The winding projects out ONLY as the integer Link, charge FORM-derived as
   `Q = \mathrm{Link}(\partial\Omega, F) \in \mathbb{Z}` (electron-identification.md:108).

**Honest negative (unchanged, it survived verification):** canon provides NO map
that carries the annulus's radial PROFILE into any real-space observable. Under
M/Q/J the entire interior trace is invisible; what survives is the wall's
existence (→ M), the integer winding (→ Q), and time-averaged envelope strain
(→ far field). The annulus INTERIOR is phase-space bookkeeping. This is also why
H3's endpoints-only verdict is not a loss: the endpoints are the two features
canon lets project out.

## 7. T4b — biquaternion glancing view (Grant Q1)

The map, from the receipts: the biquaternion block is coupling-layer NOTATION only
(leaf:5 no-claim; doctrine §F:263-277 — cores never evolve a biquaternion field, no
eigenproblem is expressed in it; the 2026-06-27 integration epic is SUPERSEDED).
**Status-carry:** the leaf itself is 🔴 DEMOTED 2026-08-11 (R40-B1 — the
three-propagating-channels framing; Z_bulk and H_couple rows NEEDS-RE-DERIVATION
under R40-B2a); nothing below load-bears on the demoted rows. Its one load-bearing
structural fact: **|Γ|=1 ⟺ N(q)=0** — the lossless-reactive wall is the algebra's
null cone (leaf:80,225), which exists only because the complex norm is not
positive-definite (result-doc:91). Γ itself is a PSL(2,ℂ) Möbius/spinor action
(leaf:79; result-doc:276).

**Judgment (glancing, no derivation):** the §3.3 mode problem is NOT naturally
biquaternionic — a scalar round-trip condition, standard non-Hermitian linear
algebra, and canon fences exactly this (leaf:45). What the algebra says about the
annulus: the OUTER edge is algebra-native (the null cone — and note the physical
outer edge sits at √(1−α), just inside the null cone, per §4 row 1). The INNER
edge is not — 1/3 is a z=3 counting fact; the algebra generates no integers or
π-powers (G1–G3 FAIL, result-doc:13; π-powers come from Golden-Torus geometry,
result-doc:351). **The biquaternion gives the annulus its rim, not its floor.**
Standing fences honored: nothing here cites the block toward Q=1/α (FORBIDDEN,
leaf:267) or α (G2 FAIL).

## 8. Stuck points

1. **Open item absent:** `2026-08-24-smith-annulus-tube-ratio-pin.md` does not
   exist in the checkout; lane ran from the dispatch spec. Needs Grant/orchestrator
   to either commit the item or confirm the spec was the item.
2. **Side-assignment of the grading is underived — now a THREE-way fork (J / B /
   taper):** J sweeps the annulus, B exits through the chart centre at A=√15/4, and
   a spatial TAPER (the physically-localized third option, §3.4) suppresses every
   intermediate-A coefficient the step forms give. Physical walk wanted: does the
   winding's amplitude saturate the junction cell it occupies (J), the bond it
   stands on (B), or a graded profile spanning cells (taper)? Note FORM J as
   implemented grades infinite arms — unphysical under localization.
3. **Thermal-floor estimator:** dispatch named a "Johnson-Nyquist row" receipt not
   among the pulls; T2 row 4 uses plain equipartition against the canonical bond
   quantum instead (minor; same order expected).
4. **T3 lock-detuning formulas are first-pass analytics, not verified in-engine**;
   and BOTH ε₁₁ coupling routes (Op19 delay; kernel-impedance) are
   UNDERIVED-EXTENSION regime transplants.
5. **A(t) amplitude law:** canon has no amplitude-swing statement (Q-EMBED
   absence); H3's candidates are UNDERIVED-CHOICE; ENDPOINTS-ONLY is robust across
   both, but no shape claim of any kind should leave this lane.
6. **Termination/embedding choice (added at repair):** isolated-junction (matched
   arms) vs in-lattice (Bloch/Bethe) readings give qualitatively different end
   reflections (§3.2b); the corpus's X37-Bloch reading + the PR#669 homogenization
   are the in-corpus adjudicators; an engine run on the actual srs net (loops
   included) would arbitrate. Until then every −1/3-floor statement in this lane is
   convention-scoped.
7. **Chart-as-instrument vs PARKED CP1 item (added at repair):** this lane's use of
   the Γ-disk as a working instrument is adjacent to the parked item's re-open
   condition (§ header). Grant's call; nothing minted here.

## 9. Repair ledger (2026-08-24 — 17 findings, 3 lenses; every finding dispositioned)

| Lens | Finding (severity) | Disposition |
|---|---|---|
| vphys-1 (MAJOR) | Z₀/2 = isolated-junction reading; comb/Q/band = truncation-scoped | FIXED: model-scope banner; §3.2b Bethe-tree computed block in script+results; §3.2/§3.3 rescoped; STUCK-POINT #6 |
| vphys-2 (MAJOR) | outer edge \|Γ\|²=1−α omitted; ranking inverted; Q→∞ false | FIXED: §4 row 1 + re-rank; §3.3 Q ceiling 428.9n; Class-B echo status carried |
| vphys-3 (MAJOR) | J/B not the single choice — taper third option; A²/9 lumped-step artifact; H1 "chart selects J" overreach | FIXED: §3.4 lumped-step caveat; SP#2 three-way; H1 withdrawal |
| vphys-4 (MINOR) | ε₁₁→γ_J transplant untagged (asymmetric vs Op19 tag) | FIXED: §5 both routes UNDERIVED-EXTENSION; SP#4 |
| vphys-5 (MINOR) | PARKED CP1 item uncited; smith_sim.py cross-repo bare; "zero freedom" register | FIXED: park pointer §header + SP#7; cross-repo naming §1; §3.4 H3 softened |
| vcanon-1 (MAJOR) | same-line homogenization clause omitted; no k·ℓ regime declared | FIXED: §1 k·ℓ declaration; clause quoted at every floor statement (§3.2b, §4) |
| vcanon-2 (MAJOR) | comb/Q maximally wrong at own frequency; T2 omitted O(0.1–0.5) lattice term; R52-class band-edge scoping | FIXED: §3.3 truncation-artifact scoping w/ shell numbers; §4 row 0 |
| vcanon-3 (MAJOR) | H2 "image of the amplitude swing" vs electron FIXED at √α | FIXED: §3.4 H2 re-headlined (response map, not orbit; 0.12% into annulus) |
| vcanon-4 (MAJOR) | false "byte-identical" claim; frozen-E6 mis-rank silently corrected | FIXED: §2 honest condensation + fenced verbatim quotes + explicit frozen-defect flag; frozen file untouched |
| vcanon-5 (MAJOR) | ave-kb/CLAUDE.md:73 sector-pair misidentified with J/B; circular H1 | FIXED: §3.4 H1 corrected (reference-collapse ≠ T2 rupture; both forms A1 objects) |
| vcanon-6 (MAJOR) | symmetric-bias immunity mis-scoped both directions; self-contradiction | FIXED: §5 three-case restructure; uniform = all-orders invariant (computed); symmetric-end moves floor (computed) |
| vcanon-7 (MINOR) | tube-ratio pin over-counted (normalization consumes rim fact) | FIXED: §3.4 H3 (one free ratio; ρ_min does the pinning; design-input caveat) |
| vcanon-8 (MINOR) | unitarity claimed unqualified, checked at 3 θ | FIXED: script checks all 20001 sweep points (6.7e-16) |
| vcanon-9 (MINOR) | I/Q-plane receipt transferred to Γ-disk without the quotient map | FIXED: §6 route 2 states Γ = V_ref/V_inc projection explicitly |
| vnum-1 (MINOR) | `floor_immune_to_symmetric_bias` hardcoded True + false in-model | FIXED: replaced by computed fields (uniform-grading dev 5.6e-17; symmetric-end product computed); §5 |
| vnum-2 (MINOR) | byte-identical + E6 ordering (dup of vcanon-4) | FIXED with vcanon-4 |
| vnum-3 (MINOR) | band edges grid-sampled, spurious digits | FIXED: bisection to 1e-14; edges sum to π to 6e-15; JSON field renamed `below_one_third_band_theta_rootfound` |

No-change items within the findings: the frozen file's own E6 ordering defect is
NOT edited (the file is frozen; the fix is the dated flag in §2, per
vacated-cite/frozen-text discipline). All other finding content produced edits.

