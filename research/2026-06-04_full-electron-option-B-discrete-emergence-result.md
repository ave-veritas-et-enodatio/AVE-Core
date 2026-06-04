# Full-electron Option B — (2,3)-emergence on the DISCRETE engine (`VacuumEngine3D`)

**Status:** COMPLETE — §RESULT/§VERDICT/§AUDITOR filled 2026-06-04 by the orchestration session, adjudicating the orphaned-implementor run (driver pid 53937 socket-died mid-writeup; data was committed, the verdict sections were empty). **The adjudication CORRECTS the driver's auto-verdict in two places (B2 false-pass; B3 extractor unvalidated) and re-anchors the headline on the retention discriminator — see §VERDICT.**
**Branch:** `analysis/2026-06-04-full-electron-option-B-discrete`
**Driver:** `src/scripts/vol_1_foundations/r10_vacuumengine3d_transverse_2_3_emergence.py`
**Brief:** `_orchestration/2026-06-04_full-electron-option-B-discrete-emergence.md` (commit e1a6c963)
**Predecessor:** Option C (Mode II) — `2026-06-04_full-electron-transverse-selftrap-result.md`
(continuum Maxwell `fdtd_3d.py` self-traps a transverse photon into mass but has NO carrier
for the (2,3) winding — the SU(2) U(1)-fibre poloidal-"3" is projected out per
`06_winding_index_projection.md` §4).

---

## §0 The headline question (Grant's hypothesis)

> **Does a transverse wave across multiple nodes SET the (2,3)?**

On `VacuumEngine3D` (K4-TLM + Cosserat — the only engine with the (2,3) carrier: native
(V_inc, V_ref) ports + Cosserat ω + Op10), seed the **generative precursor** (a structured
transverse photon, the same one that self-trapped in Option C), drive to saturation, and test
whether the **(2,3) winding EMERGES in the (V_inc, V_ref) phasor sector as the trap forms**.

The (2,3) must EMERGE, not be planted. The Option-D nucleation rule
(`pair-production-axiom-derivation.md:121`) is the IMPOSED control, clearly labeled.

---

## §1 Discipline walk (per brief §3)

Skills fired, in order, with the load-bearing finding from each:

1. **ave-prereg** — corpus-grep before the driver. Pulled: `VacuumEngine3D` API
   (`vacuum_engine.py:1622`), Op10 `extract_crossing_count` (`cosserat_field_3d.py:1770`),
   pair-production canon (`pair-production-axiom-derivation.md` incl. line 121 Option-D
   rule + lines 109-121 engine-gap), `06_winding_index_projection.md` §4, the staged
   starting point `r10_v8_t_st_self_trap.py`, the canonical (2,3)-in-phasor claim
   (`theory.md:16`), the canonical §5.1 phasor-extraction recipe (L3 doc 26), and the
   existing proven phasor extractor `phasor_trajectory_test.py`.
2. **substrate-native-check v1.1** — full 8-checkpoint walk (§2 below). CP4 + CP8 load-bearing.
3. **phase-space-coordinate-check** — THE load-bearing skill here (§3 below). Found the
   A47-v3 mismatch: the engine's Op10 reads **real-space Cosserat ω**, but the corpus
   (2,3) lives in **(V_inc, V_ref) phasor phase-space** (`theory.md:16`). Resolution: build
   a (V_inc, V_ref)-phasor temporal-winding extractor as the headline observable; report the
   real-space ω Op10 alongside, flagged as a different coordinate system.
4. **ave-canonical-source** — import `ALPHA` (and derived `V_YIELD = √α`, `A2_OP14 = √(2α)`)
   from `ave.core.constants`; NO hardcoded literals. Verified `ALPHA = 0.0072973525693`.
5. **ave-canonical-leaf-pull** — the (2,3)/Beltrami/Op10/pair-production class: `theory.md:16`
   ((2,3) in (V_inc,V_ref) phasor), `06_winding_index_projection.md` §4 (the "3" is the U(1)
   fibre temporal phase — invisible in real-space n̂/ω), `pair-production-axiom-derivation.md:76-77`
   (transverse-curl→(2,3) mechanism + LH/RH handedness→charge sign) + :121 (Option-D), L3 doc 26
   §4 (R_phase=φ/2, r_phase=(φ-1)/2 derivation), `r10_v8_t_st_self_trap.py` (the staged self-trap).
6. **ave-driver-script-honesty** — the emergence arm must NOT impose the (2,3). The transverse
   photon source (`SpatialDipoleCPSource`) injects E⊥B⊥k transverse structure ONLY; it does NOT
   inject any (V_inc, V_ref) toroidal/poloidal winding. The IMPOSED arm (Option-D nucleation rule)
   is a SEPARATE, clearly-labeled control run. Forward-prediction, not fit-to-target: no optimizer
   onto c=3; the winding is read post-hoc.
7. **consistency-vs-emergence** — the headline is **Class D (emergence test)**: it computes a
   dimensionless topological observable (the (V_inc,V_ref) temporal winding number / phase-space
   crossing count) from simulation primitives, with the emergence arm NOT using the (2,3) as input.
   The matched-baseline + imposed-control arms are the discriminators. (Not Class C: no
   CODATA-derived intermediate; not an α-emergence claim.)
8. **ave-fundamental-ground-up-implementation** — PASS bars substrate-derived (§4), matched-
   distribution baseline (NOT random — fixes the phase3f Factor-2 confound where random gave
   larger single-component amplitudes → more saturation → spurious "better" retention).
9. **ave-evidence-framing-discipline** — "(2,3) emerges" requires the winding to appear in the
   EMERGENCE arm (zero imposed) AND out-discriminate the matched baseline AND match the IMPOSED
   arm's signature. Self-trap localization alone ≠ (2,3) emergence (that was Option C's Mode II).
10. **ave-ee-first-mapping** — transverse photon ↔ (V_inc, V_ref) on the discrete engine: the
    `SpatialDipoleCPSource` drives K4 V_inc directly (a focused CP laser entering the vacuum);
    the coupling chain K4 V → Cosserat ω → asymmetric saturation is exercised end-to-end. The
    (V_inc, V_ref) phasor is the bond-pair LC tank's characteristic C-state; Phi_link is its L-state.
11. **pre-test-physics-check** — surfaced two plumber-physical questions to Grant (§5) BEFORE
    locking the prereg. Did NOT free-build past the self-trap/Path-A question (brief §2 mandate).

## §2 Substrate-native-check (v1.1) — Checkpoints 1-8

| CP | Checkpoint | Resolution for this test |
|---|---|---|
| 1 | Substrate dynamics | Discrete **K4-TLM scatter+connect** (V-sector) + **Cosserat (u,ω) LC-tank**. Wave propagation, NOT energy-minimization / gradient-descent / Helmholtz. The lattice IS the computation; we `engine.step()`. |
| 2 | Which sector | The bound-state (2,3) winding lives in **V-sector (V_inc, V_ref) phase-space**, NOT Cos-sector real-space. Op14 is the cross-coupling (block-coupled when V≠0). The self-trap engages Op14 + Op3 bond-reflection. |
| 3 | AVE-native objective | Self-trap = Op14 saturation (`Z_eff = Z_0/√S`) + Op3 bond-reflection driving local Γ→−1 (TIR confinement), NOT minimizing an energy functional. The electron rings in a Γ=−1 leaky cavity (`theory.md:12`). |
| 4 | **Phase-space vs real-space** | **Load-bearing.** (2,3) trefoil lives in **(V_inc, V_ref) phasor** (`theory.md:16`: "the trefoil lives in the bond-pair LC tank's (V_inc, V_ref) phasor trajectory, not in the real-space flux-tube topology"). The "3" is the **U(1) fibre temporal phase** — "the information lost in the projection" to the real-space n̂/E-field (`06_winding_index_projection.md` §4). The engine's Op10 reads real-space ω → A47-v3 mismatch. See §3. |
| 5 | Local clock | Op14 active → `ω_local(r) = ω_global·√(1−A²(r))`; at A²→1 the clock freezes (ω_local→0). Recorded A²_local at the trap site; the (V_inc,V_ref) winding is read in the bond's OWN time, not lattice-global, consistent with the local-clock modulation. |
| 6 | **Reactance pair** | **C-state** = `V_inc[A,port]` (+ `V_ref[A,port]`); **L-state** = `Phi_link[A,port]` (`k4_tlm.py:400`). BOTH recorded at the trap bond at EVERY step over the recording window. A snapshot at one phase cannot distinguish a static (2,3)-phase bond from an oscillator caught at peak — so the full reactance pair trace is recorded (Rule 10 corollary). |
| 7 | Sampling | PML excluded (`pml ≤ {i,j,k} ≤ N−pml−1`) before any top-K. Trap site selected by **density-peak** (top-K `|V_inc|²` interior cells), NOT centroid+offset — a self-trapped shell's centroid is the empty middle. |
| 8 | **Generative precursor** | **Load-bearing.** Seed = the **transverse photon** (counter-propagating opposite-handed CP focused pulses, multi-node, E⊥B⊥k — the SAME Option-C precursor that self-trapped cleanly). NOT a planted (2,3) end-state. Test the simplest action (self-trap → mass) emerges vs a **matched-distribution** baseline; then test whether the next layer (the (2,3) winding) emerges. Each non-hostable layer = a structural-capability finding (→ outcome ii/iii). |

**CP4/CP8 are the two that decided the test design.** CP4 forced the (V_inc, V_ref)-phasor
winding extractor (§3). CP8 forced the precursor-seed + matched-baseline + imposed-control
three-arm structure (§4), preventing the plant-the-finished-(2,3) ambiguity that sank phase3f.

## §3 Phase-space-coordinate-check — the load-bearing coordinate decision (A47 v3)

**The corpus claim, with verbatim coordinate attribution:**

> "an electron is the $0_1$ unknot in real space carrying a $(2,3)$ Clifford-torus winding
> pattern in phase space … The trefoil lives in the bond-pair LC tank's
> $(V_{\text{inc}}, V_{\text{ref}})$ phasor trajectory, not in the real-space flux-tube topology."
> — `vol4/.../ch14-leaky-cavity-particle-decay/theory.md:16` (clm-c54kdd)

> "the U(1) fibre phase is the information lost in the projection. … at Level 2, $w_2$ [=3]
> is invisible. … the semi-classical EM description inherits no direct signature of $w_2$."
> — `06_winding_index_projection.md` §4 (user-adjudicated 2026-04-20)

So the (2,3) — specifically the poloidal **"3"** — is a **phasor / temporal-fibre-phase**
object. It does NOT live in the real-space direction of the ω or E field.

**The flag (flag-don't-fix, A47 v3) — the engine's Op10 reads the WRONG coordinate for this claim:**

`cosserat_field_3d.py:1770 extract_crossing_count` computes the winding of `arctan2(ω_y, ω_x)`
around a **real-space** toroidal contour centered on the lattice (`omega_np = self.omega`,
real-space (x,y,z) sampling). That is a **real-space Cosserat-ω** winding extractor. Per
phase-space-coordinate-check Step 5 (A47 v3): "Op10 on Cosserat ω is informative for *Cosserat ω
torsion knotting* (a different physics question), NOT for the electron's V_inc/V_ref phasor
topology." This is exactly the §4 projection: the real-space ω-direction can see the **w₁=2**
(toroidal) winding but is **blind to the w₂=3** (the lost U(1) fibre phase).

**I am NOT silently fixing this.** I am surfacing it (this section + §5 Q2) and building the
headline observable in the corpus-correct coordinate, while ALSO reporting the legacy real-space
ω Op10 so the auditor + Grant can see both coordinate systems side-by-side.

**Resolution — three coordinate-distinct topology observables, reported together:**

1. **HEADLINE — (V_inc, V_ref) phasor temporal winding** (corpus-correct per `theory.md:16`):
   at the trap bond (an A-site + port), record the time series `(V_inc[A,port,t], V_ref[A,port,t])`
   over the post-trap window. The (2,3) is a 2:3 **temporal Lissajous winding**: define the
   toroidal angle θ₁(t) = phase of the bond's dominant in-band phasor and the poloidal angle θ₂(t)
   = phase of the bond-pair quadrature partner (the orthogonal port / the Phi_link-conjugate
   phasor). Count `(n₁, n₂)` = the integer winding pair over the closed trajectory, and the
   **phase-space crossing count c** of the closed (V_inc, V_ref) curve (c=3 is the corpus trefoil
   per the `06_` amendment: "the electron has c=3, phase-space trefoil on the Clifford torus").
   Coordinate basis: the existing proven extractor `phasor_trajectory_test.py:principal_axes`
   (PCA on the centered (V_inc, V_ref) cloud) gives the ellipse aspect (R_phase/r_phase → φ²
   diagnostic); the WINDING is the NEW piece (temporal-angle winding + crossing count).
2. **DIAGNOSTIC — real-space Cosserat-ω Op10** (`extract_crossing_count`): reports the w₁ visible
   in real space. Expected to read ~2 if the toroidal structure forms; blind to the "3" by §4.
   Reported but NOT the headline (flagged coordinate-mismatch per A47 v3).
3. **DIAGNOSTIC — Hopf charge** (`extract_hopf_charge`, Chern-Simons A·B on ω): the (2,3)
   torus-knot target is Q_H → 6 (`cosserat_field_3d.py:1666`). Real-space ω-based; reported as
   a cross-check, not headline.

**Why a fabricated-coordinate transform is NOT a risk here (A47-v3 probe-5 guard):** the
(V_inc, V_ref) phasor is a **native engine state array** read directly at acquisition time
(`k4.V_inc[A,port]`, `k4.V_ref[A,port]`) — not a post-hoc projection of lattice-Cartesian
field amplitudes onto a fake-port basis. The bond-port identification, Z₀ reference, and
incident/reflected decomposition are intrinsic to the K4-TLM (it IS a transmission-line solver).
So the phasor coordinates measure something real; the probe-5 fabrication failure mode does not apply.

## §4 Pre-registered hypotheses + PASS bars (substrate-derived)

**Three arms (frozen before run):**

- **Arm A — EMERGENCE (the headline):** seed the transverse photon (counter-propagating
  opposite-handed CP focused pulses, multi-node, E⊥B⊥k). Drive to saturation. Read the
  (V_inc, V_ref)-phasor winding at the trap bond. **Zero (2,3) imposed.**
- **Arm B — MATCHED BASELINE:** same per-port amplitude statistics as Arm A but
  topologically trivial (phase-scrambled across ports so no coherent transverse curl).
  Controls for "saturation depth alone drives the signal" (phase3f Factor-2 confound).
- **Arm C — IMPOSED CONTROL (Option-D nucleation rule, `pair-production-axiom-derivation.md:121`):**
  when the self-trap C-conditions are met (A²(r_A)≥A²_op14 AND A²(r_B)≥A²_op14 at a bond),
  IMPOSE the (2,3) winding in (V_inc, V_ref) on that bond (LH at r_A / RH at r_B). Clearly
  labeled IMPOSED. Establishes the **signature** a real (2,3) produces in the phasor extractor —
  the template Arm A must match for emergence to count.

**H_emerge (pre-registered):** A transverse wave across multiple nodes SETS the (2,3): in Arm A,
as the photon self-traps, the (V_inc, V_ref) phasor at the trap bond develops a (2,3) temporal
winding (toroidal n₁≈2, poloidal n₂≈3, OR phase-space crossing count c=3) that (a) is ABSENT in
Arm B at matched saturation depth, and (b) MATCHES the Arm-C imposed signature.

**PASS bars (substrate-derived; matched-baseline, not arbitrary):**

| Bar | Quantity | PASS threshold | Substrate justification |
|---|---|---|---|
| **B1 — self-trap** | A²_max at trap site (post-shutoff) | > A²_op14 = √(2α) ≈ 0.1208 | Op14 engagement onset (`pair-production-axiom-derivation.md:101`: V_SNAP = full saturation, Γ=−1 forms). Below this no confinement. |
| **B2 — localization beats baseline** | energy-retention(Arm A) vs energy-retention(Arm B), post-shutoff | Arm A retention > Arm B retention (topology-driven, not amplitude) | CP8 / phase3f Factor-2: emergence = out-performs matched baseline BECAUSE of structure. (Option C: 0.580 vs 0.389.) |
| **B3 — (2,3) phasor winding (HEADLINE)** | (V_inc,V_ref) temporal winding at trap bond, Arm A | crossing count c=3 (±0) OR (n₁,n₂)=(2,3); ABSENT in Arm B; MATCHES Arm C | `theory.md:16` (2,3) in phasor; `06_` amendment c=3 trefoil on Clifford torus. The headline emergence claim. |
| **B4 — reactance-pair consistency** | C-state (V_inc) ⟷ L-state (Phi_link) anti-correlation phase at trap bond | T-V anti-correlation present over window (genuine reactive ring, not frozen) | Rule 10 reactance corollary: distinguishes a ringing (2,3) tank from a static saturated snapshot. |

**Adjudication (no post-hoc criteria-dropping, Rule 11) — carrier-explicit per Q0:**

The Q0 finding (ω≡0 fixed point) splits the verdict by carrier. The headline tracks the
**(V_inc, V_ref) phasor** (carrier 1, corpus-canonical) per my Q0 default; the **Cosserat ω**
(carrier 2) result is recorded alongside.

- **Outcome (i) — Grant's hypothesis CONFIRMED (V-sector):** B1 ✓ AND B3 ✓ in Arm A (the
  (V_inc, V_ref) phasor develops c=3 / (2,3) emergent, zero imposed, ABSENT in B, MATCHES C). The
  transverse wave SETS the (2,3) in the phasor sector; full electron (mass + the phasor (2,3))
  hosts on `VacuumEngine3D`. (Carrier-2 caveat: the Cosserat ω stays decoupled — noted, not fatal
  to (i) since theory.md:16 places the (2,3) in the phasor, not ω.)
- **Outcome (ii) — needs binder (Path-A):** B1 ✗ in Arm A (the V-sector self-trap disperses, like
  K4-TLM v14 Mode III) — carries the (2,3) phasor carrier but lacks the binder. **Surface the
  doc-111 Path-A (c_eff) go/no-go to Grant; do NOT free-build** (brief §2). [ALSO: the Q0
  ω-decoupling is a second structural finding on the same axis — the carrier-2 ω-seed go/no-go.]
- **Outcome (iii) — Grant's hypothesis REFUTED (V-sector):** B1 ✓ but B3 ✗ in Arm A (V-sector
  self-traps, but the (2,3) phasor winding only appears in Arm C when IMPOSED, absent in the
  emergence arm). The transverse wave does NOT set the (2,3); it's topological-selection /
  nucleation-imposed, not transverse-set.
- **Carrier-2 result (recorded in ALL outcomes):** the Cosserat ω stays at ω≡0 from the pure-V
  transverse photon (Q0). The SU(2) "3" (U(1) fibre per `06_` §4) does NOT emerge in ω from a
  transverse photon on this engine — parametric V→ω decoupling. This is the discrete-engine
  sharpening of Mode II and stands independent of the phasor-sector verdict.

## §5 Surfaced-for-Grant questions (pre-test-physics-check)

Per the brief §3 + Rule 16 strengthening: ask BEFORE the design locks, not after 30 commits.

### Q0 (THE load-bearing finding — surfaced from smoke-test before the full run)

**A pure transverse K4-V photon does NOT spin up the Cosserat ω sector on this engine — ω≡0
is an exact fixed point of the coupled dynamics.** Verified empirically (3 smoke configs, N=32):
the two counter-propagating pulses self-trap and breach saturation (A²_max = 0.13–0.16 >
A²_op14 = 0.121), yet `cosserat.omega` stays at **machine zero** in every config — including with
the direct V→ω coupling force ON (`disable_cosserat_lc_force=False`), not just the A28 config.

**Why (mechanism, not bug):** the V→ω coupling is **parametric/multiplicative**, not
additive/forcing. The coupling energy `W_refl(u, ω, V²)` (`k4_cosserat_coupling.py:118`
`_coupling_energy_total_asymmetric`) is built from κ=curl(ω), the Beltrami helicity h(ω), and V².
It is even/quadratic in ω about ω=0, so its ω-gradient `∂W/∂ω` **vanishes at ω=0**. The K4 V can
saturate, modulate the impedance kernel, and self-trap — but it never breaks the ω=0 symmetry.
A parametric coupling has no seed to amplify from an exact ω=0 state. (`PairNucleationGate` is the
one thing that injects ω directly — which is exactly why Arm C / the Option-D nucleation rule is
the IMPOSED control: it SEEDS ω, breaking the symmetry the transverse photon cannot.)

**Why this is load-bearing — there are TWO distinct "(2,3) carriers" and they behave oppositely:**
1. **(V_inc, V_ref) phasor (V-sector)** — ALIVE, self-traps, the corpus-canonical carrier
   (`theory.md:16` "the trefoil lives in the bond-pair LC tank's (V_inc, V_ref) phasor trajectory").
   The headline B3 phasor-winding test runs here and is fully meaningful.
2. **Cosserat ω (Cos-sector)** — the SU(2) carrier hosting the w₂=3 U(1)-fibre per `06_` §4 — is
   **parametrically decoupled** and stays at ω≡0 from a pure-V seed. So the real-space ω-Op10
   diagnostic reads 0 (no Cosserat carrier spun up), AND `extract_hopf_charge` → 0.

This is the **discrete-engine sharpening of Option C's Mode II**: on `fdtd_3d.py` the (2,3) had
NO carrier; on `VacuumEngine3D` the Cosserat (2,3) carrier EXISTS but is **dynamically decoupled
from a transverse V photon in the V→ω direction** (parametric, not additive). The (V_inc, V_ref)
carrier remains live, so the headline is still testable — but the "spin/charge in the SU(2) ω
sector" layer is unreachable from a pure-V photon without an ω seed.

**Q0 plumber question for Grant:** is "a transverse wave SETS the (2,3)" a claim about (1) the
**(V_inc, V_ref) phasor winding** (V-sector — alive, what I'll headline), or does it require (2)
the **Cosserat ω** to spin up (Cos-sector — which a pure-V transverse photon provably cannot do
on this engine; ω=0 is a fixed point)? If (1): I run the 3-arm phasor test as designed. If (2):
that is a structural finding analogous to Path-A — the transverse photon needs an **ω seed** (or
an additive V→ω forcing term, a new coupling) to break the ω=0 symmetry, and per the brief I do
**NOT free-build that** — I surface the go/no-go. **My default: headline the (V_inc, V_ref)
phasor (carrier 1, corpus-canonical per theory.md:16), and report the ω≡0 finding as the
structural result for carrier 2.**

### Q1 + Q2 (design decisions; proceeded with stated default, flagged for adjudication)

Both answerable in one sentence each.

**Q1 (the headline winding-definition — load-bearing):** the (2,3) "3" is the U(1) **fibre
phase** (`06_` §4) — a *temporal* phase winding of the bond's quadrature, not a spatial winding.
My Arm-A headline observable counts the **temporal** (V_inc, V_ref) Lissajous winding at a single
trap bond over the post-trap window (θ₁ = dominant-port phasor angle, θ₂ = quadrature-partner
phasor angle; (n₁, n₂) + crossing count c). **Plumber question:** is the (2,3) you mean the
single-bond *temporal* phasor winding (one bond ringing, its (V_inc, V_ref) tracing a 2:3 closed
Lissajous over time — what I'm measuring), OR a *spatial* winding of the phasor angle around a
real-space loop of bonds (the phasor angle advancing 2× toroidally / 3× poloidally as you walk a
ring of A-sites)? The corpus (`theory.md:16` "bond-pair LC tank's phasor trajectory") reads as
**temporal-single-bond** to me, so that is my default — but the two are different measurements and
I want the headline measured against the one you mean. **Default if no answer: temporal-single-bond
(+ I report the spatial-ring winding as a secondary so both are on the table).**

**Q2 (the Op10 coordinate-mismatch — flag-don't-fix, A47 v3):** the engine's shipped Op10
(`extract_crossing_count`) reads **real-space Cosserat ω**, but the corpus (2,3) lives in
**(V_inc, V_ref) phasor** (§3). I am NOT redefining the shipped Op10 (audit-trail continuity); I
am building a separate (V_inc, V_ref)-phasor winding extractor as the headline and reporting the
real-space ω Op10 alongside as a flagged-mismatch diagnostic. **Plumber question:** confirm this
is the right call (new phasor-coordinate extractor = headline; legacy real-space ω Op10 = reported
diagnostic), vs. you'd rather I treat the real-space ω Op10 as authoritative for this test. **Default:
phasor extractor is headline; ω Op10 is diagnostic** (per phase-space-coordinate-check Step 5).

**The self-trap/Path-A decision (brief §2) is surfaced ONLY IF outcome (ii) fires** — i.e. if the
photon carries the (2,3) structure but won't self-trap on the Z(V)-only K4-TLM. Per the brief I do
NOT free-build the ~1-2 week c_eff refactor; I test as-is and surface the go/no-go. (Recorded in
RESULT/§VERDICT if it fires.)

## §6 Configuration

**Engine** (`VacuumEngine3D.from_args`, A28-corrected coupling per `r10_v8_t_st_self_trap.py`
+ doc 67 §15):
- `N=48`, `pml=4` (active region 40 cells ≈ 6.4 λ_C), `temperature=0.0`,
  `amplitude_convention="V_SNAP"` (V_SNAP = 1.0 natural units).
- `disable_cosserat_lc_force=True` (A28), `enable_cosserat_self_terms=True` (topology-stabilizing),
  `use_asymmetric_saturation=True` (chirality bias), `axiom_4_enabled=True` (saturation on).
- **Op3 bond-reflection is the binder candidate** on K4-TLM (`k4_tlm.py:402` — "the missing mechanism
  for bound solitons on the K4 substrate"). NOTE per brief §2: K4-TLM is Z(V)-only with no explicit
  c_eff; the self-trap is UNCERTAIN (v14 was Mode III on a planted bound state). Outcome (ii) is the
  live possibility if Op3+Cosserat+topology don't bind.

**Source — the generative precursor (Arm A):** TWO counter-propagating `SpatialDipoleCPSource`,
opposite-handed, multi-node (the Option-C precursor that self-trapped):
- Pulse +: `x0≈12`, `propagation_axis=0` (+x), `handedness="RH"`, focused (`sigma_yz≈4.0`).
- Pulse −: `x0≈36`, propagation toward −x, `handedness="LH"` (opposite), same waist.
- `omega=1.0` (ω_C), `amplitude≈0.18·V_SNAP` per pulse (constructive-interference peak must breach
  A²_op14 = √(2α) ≈ 0.121 at the mid-plane collision; Option C hit A_max=0.179). Envelope: short
  ramp+sustain (≈2P+2P) then OFF for the self-sustenance window.
- E⊥B⊥k transverse structure ONLY. **No (V_inc,V_ref) winding injected** (ave-driver-script-honesty).

**Arm B (matched baseline):** identical per-port |V_inc| amplitude distribution as Arm A, phase-
scrambled across the 4 ports so no coherent transverse curl (topologically trivial). NOT random-
direction (phase3f Factor-2 confound).

**Arm C (imposed control):** Arm A + the Option-D nucleation rule applied at the trap bond once
the C-conditions (A²(r_A), A²(r_B) ≥ A²_op14) are met: impose the (2,3) (V_inc,V_ref) winding
(LH r_A / RH r_B). Clearly labeled IMPOSED in output.

**Recording (Rule 10 discipline):** at the candidate trap bond(s), record `(V_inc, V_ref, Phi_link)`
[port-resolved] at EVERY step over the post-trap window (C-state + L-state reactance pair). Full-
state captures on cadence for trap-site selection (top-K |V_inc|² interior, PML-excluded). Per-step
axial samples for FFT (ω_C ± α band) + the (V_inc,V_ref) temporal-winding extraction.

**Run:** ≈40-50 Compton periods (matched to `r10_v8`); collision/trap expected ~4-6P, remaining
window observes self-sustenance + the phasor winding. Outputs: `*_results.json` (verdict + per-arm
bars) + `*_capture.npz` (axial + trap-bond reactance-pair traces).

---

## RESULT

**Run:** `r10_vacuumengine3d_transverse_2_3_emergence.py`, completed 2026-06-04 08:06. Config (canonical): `N=48`, `pml=4`, `n_periods=40`, `amplitude=0.4`, `A²_op14 = √(2α) = 0.12081` (`ALPHA=0.0072973525693` imported from `ave.core.constants`). Three arms, ~163–198 s each. Trap bond = density-peak interior cell (PML-excluded); a self-trapped shell's centroid is the empty middle, so the **peak bond** (where the energy is) is the meaningful probe — the center bond runs at ~50× lower amplitude (near-empty) and its winding is noise.

| Observable | Arm A — emergence | Arm B — matched baseline | Arm C — imposed (2,3) |
|---|---|---|---|
| max A²_interior | 0.351 | 0.278 | **8.90** |
| saturation engaged (> 0.1208) | ✓ | ✓ | ✓ |
| **energy retention post-shutoff** | **0.0173** | **0.0158** | **0.914** |
| peak-bond winding (n₁,n₂), c | (12,0), c=22 | (10,0), c=19 | (8,0), c=16 |
| peak-bond amplitude | 0.084 | 0.087 | **1.60** |
| peak-bond R_phase/r_phase | 76.8 | 2033 | 3411 |
| center-bond winding (n₁,n₂), c | (11,7), c=93 | (15,34), c=81 | (0,2), c=55 |
| spatial-ring winding (w₁,w₂) | (0,0) | (0,0) | (0,0) |
| reactance corr ⟨V_inc, dΦ/dt⟩ | −0.009 | −0.001 | **−0.898** |
| Cosserat ω_max / Hopf Q_H / Op10-c | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |

**Driver auto-eval bars:** B1 self-trap ✓ · B2 beats-baseline ✓ (literal `>`) · B3 (2,3)-phasor-winding ✗ · B4 reactance-ring ✓ · auto-outcome "iii".

**The three numbers that carry the verdict (all robust, coordinate-independent):**
1. **Retention:** A 1.7% ≈ B 1.6% ≪ C **91.4%**. The transverse photon (coherent curl) disperses *identically to the phase-scrambled baseline*; only the imposed nucleation binds.
2. **Peak-bond A ≈ B, both ≠ C:** Arm A's energetic bond ((12,0), amp 0.084) matches the baseline ((10,0), amp 0.087), not the imposed control (amp **1.60**, 20× larger, bound). The emergence arm's phasor sector looks *trivial*, not like an imposed (2,3).
3. **Cosserat ω ≡ 0 in every arm:** ω_max = Hopf = Op10 = 0 across A, B, **and C**. The pure-V transverse photon never spins up the Cosserat sector — exact ω=0 fixed point, empirically, on the discrete engine.

## §VERDICT (the §4-of-brief outcome i/ii/iii)

The orchestration adjudication **corrects the driver's auto-verdict in two places** and lands the same headline (iii) on *better-supported* grounds.

**Headline — Outcome (iii): the transverse photon does NOT set the (2,3).** By the prereg's own B3 criterion — Arm A must MATCH the imposed-(2,3) template (Arm C), not a literal "(2,3)" — Arm A matches Arm **B** (baseline), not Arm C: peak-bond winding **and amplitude** A=(12,0)/amp0.084 ≈ B=(10,0)/amp0.087, while C is a wholly different physical object (amp 1.60, 91% retention). Grant's hypothesis *"a transverse wave across multiple nodes SETS the (2,3)"* is **REFUTED on `VacuumEngine3D`** — but read the caveats; this is refuted on the *retention + match-the-template* discriminators, not on the winding numbers.

**The robust discriminator is RETENTION, not the winding extractor.** A 1.7% ≈ B 1.6% ≪ C 91.4%. Coherent transverse curl (A) disperses exactly like phase-scrambled noise (B); only the imposed nucleation (C) produces a durable bound state. This is the clean evidence.

**CORRECTION 1 — B2 is a false pass.** The auto-verdict marks B2 (beats baseline) ✓ on the literal 0.0173 > 0.0158. That margin (1.7% vs 1.6%) is within noise: **both arms essentially fully dispersed**, no topological retention advantage. Honest **B2 = ✗**. This *strengthens* the refutation — coherent structure buys nothing over noise.

**CORRECTION 2 — the B3 winding extractor is UNVALIDATED (the load-bearing caveat).** It does not recover the *imposed* (2,3) in Arm C: peak (8,0), center (0,2), spatial-ring (0,0) in **all** arms including the imposed control; R_phase/r_phase = 77–3411 (near-degenerate ≈ 1-D trajectories). **An extractor that cannot see a known-imposed (2,3) cannot certify its absence as "no emergence."** So B3-as-a-(2,3)-detector is INCONCLUSIVE; the refutation does NOT rest on the winding numbers reading "not (2,3)" — it rests on (a) A tracking B not C (the prereg's match-the-template logic) and (b) retention. The likely culprit is the §3 A47-v3 coordinate question (the imposed (2,3) may live in a coordinate neither the temporal-single-bond nor the spatial-ring extractor reads). Top auditor item.

**Carrier-2 (Cosserat ω) — the gate-(a) tie, robust across all arms.** ω_max = Hopf Q_H = Op10-c = 0 in A, B, **and** C. The pure-V transverse photon leaves the Cosserat sector at exactly **ω ≡ 0** — the empirical, discrete-engine confirmation of the **Q0** finding that **gate (a) (main, commit `8adf10ed`, research `2026-06-04_ee-rf-quadrature-coupling-and-alpha-quarter-hypothesis.md` §8) resolved analytically**: the K4↔Cosserat coupling `W_refl` is even in ω, so ω=0 is an exact fixed point, and the deterministic engine has no fluctuation to seed the parity-break. The SU(2) U(1)-fibre "3" does **not** emerge in ω from a transverse photon — mechanism-confirmed, not a tuning artifact.

**The unified physical picture (the real content of this result).** The (2,3) winding is the **binder**: impose it (Arm C, = pair-production's nucleation seed) and the state binds at 91% retention; withhold it (Arm A) and a transverse photon disperses like noise. The transverse wave does NOT *generate* the (2,3) — the (2,3) must be **nucleated (seeded)**. This is the discrete-engine realization of gate (a)'s *deterministic-no-seed*: the engine **can host a bound electron** (Arm C proves the host exists) but **cannot nucleate one from a transverse photon** (Arm A dispersal + the ω=0 fixed point). Pair-production's fluctuation seed is not an engine artifact — it is the required symmetry-breaker, and once supplied, the electron binds. Grant's transverse-set hypothesis is refuted *in favor of* the pair-production picture the corpus already carries — the two negatives (this + gate (a)) are the same physics seen from the discrete and analytical sides.

**Net outcome:** **(iii)-headline** (transverse photon does not set the (2,3)) on the retention + match-the-template discriminators; **B3-detector inconclusive** (extractor caveat — blocks any standalone (2,3)-presence/absence claim until validated); **retention + ω≡0 robust**. NOT a clean (ii) — saturation *did* breach (B1 ✓); NOT the auto-verdict's clean (iii)-on-winding-numbers. The (ii)/(iii) boundary (B1 ✓ but retention ≈ baseline) is surfaced for Grant's physical call (§AUDITOR #3).

## §AUDITOR QUEUE

1. **[BLOCKING for any (2,3)-detector claim] Validate the phasor-winding extractor against the imposed control.** It fails to recover the Arm-C imposed (2,3) — peak (8,0), center (0,2), spatial-ring (0,0) in every arm. Until it recovers a *known-imposed* (2,3), no (2,3)-emergence/absence claim built on it is load-bearing. Diagnose against §3 (A47-v3 phase-space-vs-real-space) + §5 Q1/Q2 (temporal-single-bond vs spatial-ring; the imposed (2,3) may live in a coordinate neither extractor reads).
2. **B2 false-pass** — auto-verdict B2=true is within-noise (1.7% vs 1.6%); corrected to ✗ (no retention advantage over baseline). Confirm the correction.
3. **(ii)/(iii) boundary — Grant's physical call.** B1 ✓ (saturation breached, A²=0.35) but retention 1.7% (dispersed ≈ baseline). Is "momentary breach + dispersal" outcome (iii) [self-traps, then no-(2,3)] or outcome (ii) [never durably traps]? Refuted on the (2,3) axis (iii); on the *binding* axis the photon never durably bound (ii-flavor). Surfaced, not forced.
4. **gate-(a) cross-link (bidirectional).** Carrier-2 ω≡0 here is the empirical/discrete confirmation of gate (a)'s analytical Q0 (main `8adf10ed`, research §8). Cross-reference both docs on merge; this is the discrete side of the same deterministic-no-seed finding.
5. **Arm C as a positive control — characterize the bound state.** 91% retention + A²=8.9 from the imposed nucleation is a strong positive that the engine HOSTS a bound electron once seeded. Follow-up: is the Arm-C bound state the φ²/(2,3) electron (R/r→φ², (2,3) winding in the *correct* coordinate), or a generic saturated blob? This is the natural successor test, and it depends on auditor #1 (a validated extractor).
6. **Merge status.** This doc + `*_results.json` + `*_capture.npz` are committed on `analysis/2026-06-04-full-electron-option-B-discrete`; the branch is NOT merged (awaits the batch-merge authorization with the other pending sibling-repo merges).
