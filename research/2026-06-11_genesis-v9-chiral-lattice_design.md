# Genesis v9 — Chiral Trivalent Lattice + Two Smokes (Phase-0 Design)

**Branch:** `analysis/2026-06-11-genesis-v9-chiral-lattice` (off `origin/main` @ `f6ffd98d`)
**Lane:** implementer. **Phase:** PHASE-0 (scaffold + smokes only — NO genesis run).
**Status:** DESIGN-OF-RECORD for the scaffold. The Phase-1 pre-registration is a separate
DRAFT (`2026-06-11_genesis-v9-phase1-prereg_DRAFT.md`) — returned, **not frozen**. Grant freezes.

This document does four things, in order:
0. surfaces the **load-bearing adjudication flag** (v9 re-opens an adjudicated canon resolution);
1. walks `substrate-native-check` end-to-end **before** any engine code (all checkpoints written out);
2. specifies the lattice (positions + adjacency + parameter mapping, both enantiomorphs + control);
3. defines the two smokes and the phased plan;
4. records the design rationale + a citation ledger (canon / external-math / session-record split).

---

## 0. ADJUDICATION FLAG (flag-don't-fix) — v9 re-opens the 2026-06-07 lattice-net resolution-of-record

**This is surfaced for Grant, not resolved here. Phase-1 MUST NOT be frozen until this is adjudicated.**

The v9 premise is a **chiral trivalent (degree-3) lattice**. Canon at `origin/main` carries a
**resolution-of-record that settled against exactly this object.** Both texts are quoted verbatim so
the conflict is visible without reframing either side.

**Canon resolution (the side v9 challenges)** —
`_orchestration/2026-06-07_lattice-net-resolution.md`:
> "**Resolution: z=4 diamond.** It is the net the framework actually computes on. … The z=3 'srs'
> leaves are **unbacked numerology — the outliers.**" (Conclusion 1)
> "Chirality = a `k_χ` Cosserat order-parameter on the diamond — `Fd-3m` (supergroup) + chiral
> decoration = `I4₁32`. … The cold lattice is achiral; chirality is **excited**." (Conclusion 3)
> "**Engine action:** none … **Do NOT rebuild on z=3 srs** (would invalidate the α + Lorentz chains)."

**Canon Axiom 1 (the still-unpropagated self-contradiction the walk-back queue names)** —
`manuscript/common_equations/eq_axiom_1.tex:20`:
> "a **chiral Laves K4 Cosserat crystal** … governed by the right-handed `I4_1 32` chiral space
> group, with **4-fold K4 nearest-neighbor connectivity** at each node."

The Laves/`I4₁32` name implies degree-3 (Sunada srs); the stated connectivity is degree-4 (diamond).
The same file's k4-tlm leaf still asserts "the lattice is permanently bipartite and therefore natively
chiral" (`k4-tlm-simulator.md`, validation section), a line the unmerged z4-walk-back branch
(`origin/analysis/2026-06-08-vacuum-z4-coordination-walkback @ 28026bed`) drops as a non-sequitur.
**`origin/main` therefore simultaneously carries both readings.** The walk-back is UNMERGED with its
naming gate held for Grant.

**What this means for v9 (the two honest framings, Grant picks one):**
- **(A) Deliberate challenge.** v9 is a falsification test of the resolution-of-record's claim that the
  z=3 srs net is "unbacked numerology." If Smoke B (optical activity, signed per enantiomorph, zero on
  control) fires on the trivalent net, that is positive structural evidence the srs reading carries
  physics the diamond cannot inject — and the resolution's α/Lorentz-chain-invalidation warning becomes
  the explicit cost to weigh. This is the framing the scout recommends and the one this scaffold is built
  to serve.
- **(B) Reconcile with excited-decoration.** v9's chiral net is treated as a *model of* the excited
  `k_χ` decoration's geometric content, not a replacement substrate — in which case the trivalent net is
  a diagnostic instrument, the α/Lorentz chains stay on diamond, and nothing is "rebuilt on z=3."

The scaffold below is **neutral to that call**: it builds and validates the trivalent net and runs the
smokes either way. What is gated on Grant is whether a *passing* Smoke B is read as (A) evidence to
migrate the substrate or (B) evidence about the decoration. **Per the challenge-canonical-negative
discipline, this scaffold does not cite canon as straightforwardly "trivalent-chiral" — canon's computed
object is degree-4 achiral diamond, and the trivalent claims are the flagged outlier leaves.**

---

## 1. `substrate-native-check` walk (done BEFORE engine code)

Walked at design time per Operating Principle 1. Every checkpoint written out. The point of the walk is
to keep SM/QED defaults (Lagrangian, gradient-descent, continuum-Helmholtz, energy-basin) from leaking
into the scaffold by default.

### CP — Sector
The two smokes live in two different substrate sectors, and the scaffold keeps them separate:
- **Smoke A** (scalar dispersion / energy conservation) is the **translational / capacitive E-sector** —
  one scalar `V_inc` per port, the canonical sub-saturation TLM wave (`k4-tlm-simulator.md:36-42`).
- **Smoke B** (optical activity) is the **trace-free transverse-EM sector** — the polarization 2-vector
  in the plane perpendicular to propagation. Per Axiom 1 the transverse EM field is the trace-free
  transverse part of the 6-DOF node (`eq_axiom_1.tex:20`: "trace-free transverse EM wave propagation").
- **Chirality itself** lives where canon says it lives: per FLAG A of
  `research/2026-06-07_2ndshell-screw-holonomy-result.md:77`, bare diamond positions are achiral and the
  `I4₁32` handedness is "necessarily a Cosserat-frame decoration." v9's move is to test whether putting
  the handedness into the **bare trivalent connectivity** (srs, genuinely chiral as positions) reproduces
  that same transverse holonomy *geometrically* — i.e. without the injected one-parameter
  `κ_chiral = α·pq/(p+q)` coupling that `origin/main` currently uses
  (`src/ave/topological/cosserat_field_3d.py:115,131,522-523`).

### CP — Objective (NOT Lagrangian / gradient-descent / energy-basin)
The dynamics is **scatter + connect** (impedance/wave time-stepping), per the canonical TLM loop
(`k4-tlm-simulator.md:36-40`): `V_ref = S·V_inc` at each node, then transfer to the opposing port of the
neighbour. There is **no action functional, no descent on an energy basin, no Helmholtz continuum
solve.** Smoke B's Phase-0 observable is the **writhe (helicity) of the lattice's shortest closed
circuits** — a frame-free geometric pseudoscalar (the chiral-antenna *source* of gyrotropy), not a
minimization. The dynamical polarization-rotation it sources (frame parallel-transport / full vector-TLM)
is the **Phase-1** deliverable — the substrate-native locus of optical activity named but never executed
in canon (`k4-tlm-simulator.md:32`: "geometric transverse polarization rotations emerge natively"). See
§3 for the empirical record of why the parallel-transport probe is Phase-1, not Phase-0.

### CP — Coordinates (A46 phase-space-vs-real-space)
- Lattice **geometry** is built and validated in **real-space Cartesian** (node positions, bond vectors).
  This is correct: the geometric keepers (degree, girth, bond angle, chirality) ARE real-space claims.
- Smoke B's **observable** is a **reflection-odd pseudoscalar** (ring writhe / circuit helicity), measured
  in its own chirality coordinate — **not** a real-space lattice-Cartesian field component. The corpus
  claim about optical activity is a handedness (rotation of the polarization *plane*,
  `k4-tlm-simulator.md:32`), and a pseudoscalar source is the matching-coordinate (A46) measurement of a
  handedness. Recorded as the mean ring-writhe. (Phase-1's `Δθ_pol / L` polarization-plane angle is the
  downstream dynamical observable in the same chirality coordinate.)

### CP — K4 (the name-disambiguation crux)
"K4" is overloaded in canon (resolution-of-record Conclusion 4: "an ambiguous name — Sunada's K4-*graph*
(4 vertices, degree-3) vs 4-*coordination*"). The scaffold is explicit:
- **engine "K4" = diamond, degree-4** (`k4_tlm.py:101-119`, ports `(+1,+1,+1),(+1,-1,-1),(-1,+1,-1),
  (-1,-1,+1)`, achiral bare positions) — used as the **achiral control**.
- **v9 "K4" = Sunada srs / (10,3)-a Laves net, degree-3** — the chiral object under test. Its geometric
  properties (trivalent, 120° balanced bonds, girth-10, `I4₁32`/`I4₃32` enantiomorph pair) are
  **external mathematics** (source class: Sunada, "Crystals that nature might miss creating," *Notices
  AMS* 2008; RCSR `srs` net; Wells (10,3)-a). They are **not asserted from canon** — they are
  **constructed and verified in the scaffold's own keepers** (§2, §3). Canon's only contact with these
  properties is the open-question FLAG A.

### CP — Cosserat (where chirality enters)
Phase-0 carries **no Cosserat micro-rotation field** — the chirality is in the bare srs connectivity, by
design (that is the v9 hypothesis being tested). The transverse frame transported in Smoke B is the
**EM polarization frame**, transported by the bond geometry, not a separate Cosserat DOF. This keeps
Phase-0 a clean test of "does geometry alone do it?" The full 6-DOF micropolar node (Cosserat sector) is
**Phase-1 scope**.

### CP — Op14 (saturation)
Phase-0 is **linear sub-saturation** (`A ≪ 1`): the K4-TLM regime per A-027
(`k4-tlm-simulator.md:12`). Op14 non-linear impedance saturation is **OFF**. Therefore the empirical-
driver corollary on **local-clock modulation** (`ω_local(r) = ω_global·√(1−A²(r))`) is **out of scope for
Phase-0** and is flagged as a Phase-1 genesis concern (when `A → 1`). No eigsolve at global σ is performed
in Phase-0.

### CP9 — heuristic-vs-dynamical
Both smokes are **dynamical**: Smoke A time-steps the scatter+connect loop and measures a propagating
wavefront + a conserved energy sum; Smoke B transports an actual launched packet's polarization frame
along the net. Neither is a heuristic score on a static configuration. The geometric keepers (girth,
chirality) are structural assertions on the built net, run as executable graph algorithms — they FIND the
shortest rings and assert the size, they do not assert "10" by fiat.

### CP10 — boundary-not-bulk-rendering + PML cell exclusion
Smoke A's energy-conservation keeper runs **closed** (no PML) so the conserved quantity is exact (orthogonal
scatter ⇒ `Σ|V_inc|²` invariant to machine epsilon). Any field-density extraction in the driver filters
PML cells (`pml_thickness ≤ idx ≤ N − pml_thickness − 1`) before `argpartition`, and samples at energy-
density peaks (top-K `|V|²`), not at a centroid — per A-Rule 10. (Phase-0 smokes do not need top-K
extraction, but the driver scaffolding records the convention so Phase-1 inherits it.)

### Walk verdict
Sector-clean, objective-native (scatter+connect, no descent), coordinate-correct (A46), name-
disambiguated (diamond=control, srs=under-test), saturation-off (Op14 deferred), dynamical (CP9),
boundary-honest (CP10). **The single non-native risk is the name-collision adjudication in §0 — surfaced,
not silently resolved.**

---

## 2. Lattice spec

Implemented in `src/ave/core/chiral_lattice.py`. Three nets, one builder, one CONNECT convention.

### 2.1 The srs (Laves / Sunada-K4 / (10,3)-a) net — node positions

**EXTERNAL MATHEMATICS (source class: Sunada 2008 / RCSR `srs` / Wells (10,3)-a), verified-in-scaffold.**
The conventional cubic cell (`I4₁32`, #214, Wyckoff `8a`) holds 8 nodes. Fractional coordinates
(native / right-handed enantiomorph), confirmed by the scaffold keepers:

```
rotation set:       (1/8,1/8,1/8) (3/8,5/8,7/8) (7/8,3/8,5/8) (5/8,7/8,3/8)
body-centred (+½):  (5/8,5/8,5/8) (7/8,1/8,3/8) (3/8,7/8,1/8) (1/8,3/8,7/8)
```

Nearest-neighbour bond length `= √2 / 4` in cell units; each node bonds to exactly 3 others.
**The mirror enantiomorph (`I4₃32`, srs-c / (10,3)-a left-handed)** is the improper image `x → −x`
(mod 1). These two are NOT superimposable by any proper rotation + translation (verified: §3 keeper).

**These properties are asserted by keepers, never by fiat:**
| property | value | keeper |
|---|---|---|
| coordination (degree) | **3** (every interior node) | `test_srs_is_trivalent` |
| bond angles at a node | **120°, 120°, 120°** (balanced: Σ edge-unit-vectors = 0) | `test_srs_bonds_120_balanced` |
| girth (shortest ring) | **10** (BFS-found, asserted, not assumed) | `test_srs_girth_is_ten` |
| self-symmetry point group | **432** (24 proper, 0 improper ⇒ chiral) | `test_srs_chiral_point_group_432` |
| native ↔ mirror | proper:0 / improper:24 (enantiomorph pair) | `test_enantiomorph_pair_is_improper` |

(Scaffold scratch-validation already run: degree-3 uniform, 120.0°/120.0°/120.0° balanced, girth 10 at
both L=4 and L=6 supercells under PBC, self-symmetry proper=24 improper=0, native→mirror proper=0
improper=24. The keepers re-run these as the committed gates.)

### 2.2 The achiral control net — diamond (engine-canonical, degree-4)
The control is the canonical **diamond / engine-"K4"** net (`k4_tlm.py:101-119`): A = all-even coords,
B = all-odd, ports `(±1,±1,±1)` with even sign-count, achiral bare positions (point group `Fd-3m`,
inversion-symmetric). Smoke B MUST read ~0 rotation here — the control proves the rotation comes from
chirality, not from the transport machinery. The diamond is the *resolution-of-record's computed object*,
so the control is canon's own substrate.

### 2.3 Adjacency / the CONNECT map (derived, not borrowed from cubic code)
For each node `u`, the builder emits an ordered port list `ports[u] = [(v, p_v), …]` where `p_v` is the
index, on neighbour `v`, of the reverse edge `v→u`. CONNECT is the universal TLM rule, geometry-agnostic:
```
V_inc[v, p_v]   (next step)  =  V_ref[u, p_u]   (this step)        for each directed edge u→v
```
This is the canonical CONNECT ("Port i on node A connects to Port i on neighbour B; no reciprocity
mapping needed," `k4_tlm.py:117-118`) generalised to a non-bipartite valence-3 net by storing the
explicit reverse-port index per edge. **No cubic stencil is reused** — adjacency is built from the
verified srs geometry by minimum-image NN search, then the reverse-port index is resolved per edge.

### 2.4 The trivalent scatter matrix — DERIVED from Op5 (new instantiation, flagged)
Canon's executable TLM definition is **Op5** (canonical, `operators.md:45`):
`[S] = (I + [Y]/Y₀)⁻¹·(I − [Y]/Y₀)`, instantiated in canon **only** at the 4-port diamond junction
`S_ij = ½ − δ_ij` (`k4_tlm.py:64-93`, `k4-tlm-simulator.md:24-32`). A 3-port trivalent S-matrix exists
nowhere in canon, so it is **derived from Op5's shunt-junction reduction** — the identical physics that
gives the 4-port, taken at n=3:

> Shunt node, `n` equal-admittance (`Y₀`) ports meeting at a common node voltage `V`. Total port voltage
> `V_i = V_i^inc + V_i^ref = V` (common, shunt). Current into node from port `i`: `I_i = Y₀(V_i^inc −
> V_i^ref)`. KCL `ΣI_i = 0` ⇒ `V = (2/n)·Σ_j V_j^inc`, hence `V_i^ref = V − V_i^inc`, i.e.
> **`S_ij = 2/n − δ_ij`.** At n=4 this is `½ − δ_ij` (recovers canon exactly). At n=3:
> **`S_ij = ⅔ − δ_ij`**, i.e. `S = (2/3)J − I` (J = all-ones 3×3).

`S = (2/3)J − I` is symmetric with `S² = (4/9)J² − (4/3)J + I = (4/3)J − (4/3)J + I = I` (using J²=3J), so
**`SᵀS = I` exactly, eigenvalues ±1** — unitary, energy-conserving, same class as the 4-port. **This is a
derivation-not-in-canon: canon supplies only the n=4 case; the n=3 case follows from the identical Op5
shunt-KCL reduction and is tagged as a new instantiation, executed and unitarity-checked by
`test_trivalent_scatter_unitary` (the n=4 reduction is checked against the canonical `½ − δ_ij` in the
same keeper as a cross-anchor).**

### 2.5 Parameter mapping (from `constants.py`, per `ave-canonical-source`)
All physical scale comes from `src/ave/core/constants.py` — **no hand-set numbers**:
| quantity | source | value |
|---|---|---|
| node pitch `ℓ_node` | `constants.L_NODE` (= ħ/mₑc) | 3.8616×10⁻¹³ m |
| bond admittance `Y₀ = 1/Z₀` | `constants.Z_0` (= √(μ₀/ε₀)) | Z₀ ≈ 376.73 Ω |
| wave speed anchor `c₀` | `constants.C_0` with TLM `c₀ = dx/(dt√2)` | per `k4-tlm-simulator.md:42` |
| `μ₀`, `ε₀` | `constants.MU_0`, `constants.EPSILON_0` | LC bond reactances |

Bond `L`, `C` follow from `Z₀ = √(L/C)` and `c₀ = 1/√(LC)` per node-pitch; the srs cell-to-Cartesian
scale uses `a_cell = k·ℓ_node` with `k` set so the NN bond length equals one canonical bond (`√2/4·a_cell
= ℓ_node` ⇒ `a_cell = 2√2·ℓ_node`). This is an **engineering choice of the supercell scale**, tagged as
such (it sets units, not physics); the dimensionless smoke invariants are scale-free.

---

## 3. The two smokes (the phase's empirical heart)

Both implemented as executable keepers (`src/tests/test_chiral_lattice_smokes.py`) + a fuller battery
driver (`src/scripts/vol_1_foundations/chiral_lattice_optical_activity.py`, `__main__`).

### Smoke A — CONSISTENCY GATE ("the lattice change must not break the physics that already worked")
**Claim under test:** an achiral observable on the chiral srs net matches the diamond-engine baseline
within tolerance. Measured on **dimensionless, scale-free invariants** (the honest match — absolute c
differs by a known geometric factor between z=3 and z=4, so the gate is on invariants, not on the raw
speed):
1. **Scatter unitarity:** `max|SᵀS − I| ≤ 1e-12` on the trivalent `S = ⅔J − I` (canon diamond baseline:
   `2.2e-16`, `k4-tlm-simulator.md:50`). Tol relaxed to 1e-12 only as a float guard; expected ~1e-16.
2. **Eigenvalues on the unit circle:** all `|λ_i| = 1.000 ± 1e-12` (canon baseline: all `|λ|=1.000`).
3. **Closed-system energy conservation:** time-step the srs scatter+connect closed (no PML); assert
   `Σ|V_inc|²` constant to `≤ 1e-10` relative drift over ≥ 200 steps (canon baseline: monotone under
   boundary absorption; closed ⇒ exactly conserved). **This is the load-bearing "didn't break it" gate.**
4. **Small-k dispersion is linear + isotropic:** launch a low-k scalar packet along the three cubic axes;
   assert the measured front speed is **axis-isotropic** to `≤ 5%` and **linear in k** at small k (the
   achiral-physics-preserved signature). Records the srs front speed for the Phase-1 calibration.

**PASS criterion (Smoke A):** all four hold. If any fails, the trivalent scatter/connect is broken and
Phase-1 is blocked regardless of Smoke B.

### Smoke B — OPTICAL-ACTIVITY SMOKE (the discriminating heart)
**Claim under test (canon names it, never executed — `k4-tlm-simulator.md:32`; AVE-HOPF
`open_questions.md:31` names the missing derivation chain):** a chiral lattice is optically active, **with
opposite signs on the two enantiomorphs and zero on the achiral control.**

**Phase-0 observable (substrate-native, robust): the writhe (helicity) of the lattice's shortest closed
circuits.** Optical activity (gyrotropy) is *sourced* by the net helicity of a medium's closed circuits —
the chiral-antenna / wire-loop mechanism (the `k4-tlm-simulator` wire-loop resonance section; the
canonical `(2,3)`-knot helicity picture). The srs net's shortest rings are the 10-membered circuits;
their **writhe** is a reflection-ODD, frame-free, **box-independent** pseudoscalar. It is the
**necessary-condition source term** for optical rotation: a medium whose shortest circuits carry net
helicity is gyrotropic, and the sign of the helicity sets the sign of the rotation.

> **Why not parallel transport of a launched packet (the obvious first design).** That WAS the first
> Phase-0 mechanism drafted (Bishop-transport a transverse polarization along a screw-axis ray, measure
> `Δθ_pol/L`). Run early per Rule 10, it was found **non-converged at Phase-0**: a discrete scalar walk
> through a finite periodic supercell *wanders*, the net along-axis displacement is non-monotonic, and the
> measured rate is sensitive to box size and step count (it even sign-flipped between `L=6` and `L=8`).
> The clean machine-epsilon numbers it sometimes produced were `(L, nsteps)` artifacts. **Honest scope
> call:** a converged dynamical polarization-rotation requires the full **vector-TLM** (transverse
> 2-component field on the ports), which is **Phase-1**. Phase-0 measures the robust geometric **source**
> (writhe), not the dynamical rotation. Writhe is independent of traversal direction (the Gauss double
> integral is unchanged under curve reversal) and odd under mirror, so ring writhes sum coherently with no
> orientation convention and vanish identically for a centrosymmetric (achiral) net.

- **Measurement:** mean ring-writhe over the distinct shortest rings, for native srs / mirror srs /
  diamond control. Reported as a pseudoscalar (A46: a chirality observable, measured in its own
  reflection-odd coordinate, not a real-space field amplitude).
- **PASS criterion (Smoke B):**
  - the chiral net carries **nonzero** ring helicity (`|writhe| > 1e-3`);
  - native and mirror have **opposite sign** and **equal magnitude** (`|w_R + w_L| ≤ 1e-2·|w_R|`) —
    canon independently predicts sign-odd / magnitude-even between enantiomorphs
    (`cosmic-axes-and-frames-glossary.md:63-67`: "Mirror-image freeze-in … identical magnitude …
    identical physics");
  - the achiral diamond control writhe is **≤ 5%** of the chiral magnitude (a pseudoscalar of a
    centrosymmetric net vanishes identically).
- **EMPIRICAL RESULT (this scaffold, committed driver + keeper):** srs-right `−4.0867e-02`,
  srs-left `+4.0867e-02` (exact sign-flip, per-ring spread ~1e-9), diamond control `0.0` exactly; and
  box-independent (identical at `L=4,6,8`). **Smoke B PASSES** — the chiral geometry carries signed
  helicity into its shortest circuits, with the enantiomorph sign-flip and the achiral-control null.
  *This is positive necessary-condition evidence for the lattice-chirality hypothesis* (subject to the §0
  adjudication on what a pass licenses — substrate migration vs decoration-model).
- **FAIL reading (honest closure, Rule 11):** had the trivalent net shown zero / unsigned circuit
  helicity, the hypothesis would take a **structural hit** — report the clean negative, name the mechanism
  (geometry alone does not carry the handedness), do not rescue. (It did not fail; recorded for symmetry.)

### What Phase-0 does NOT claim
Phase-0 does **not** quantify a rotatory-dispersion constant, does **not** compare to `α·pq/(p+q)` (that
is the injected-coupling number, the very thing v9 is trying to escape), and does **not** run a genesis /
bound-state soliton. It tests the **necessary geometric condition** and arms (or disarms) Phase-1.

---

## 4. Phased plan

**Phase-0 (this scaffold) — DELIVERED:**
- `chiral_lattice.py`: srs builder (both enantiomorphs) + diamond control + trivalent Op5 scatter +
  CONNECT map + `constants.py` parameter mapping.
- Geometric keepers (degree-3, 120°-balanced, girth-10, chiral-432, enantiomorph-improper) — each a real
  algorithm that FINDS and asserts.
- Smoke A (consistency gate) + Smoke B (optical-activity necessary-condition), executable, CI-scale.
- Battery driver for the full Smoke B sweep.
- Phase-1 prereg **DRAFT** (separate file, NOT frozen).
- `make verify` green per commit.

**Phase-1 (genesis) — PREREG-GATED, NOT in this phase:**
- Frozen only after (a) Grant adjudicates §0, and (b) Smoke B fires (else Phase-1 is disarmed and the
  branch closes on the clean negative).
- Full dynamical **vector-TLM** on the srs net (transverse 2-component field carried on ports, not just
  parallel transport); Op14 saturation ON for bound-state genesis (local-clock modulation re-enters
  scope — `ω_local(r) = ω_global·√(1−A²(r))`).
- **Controls (Phase-1):** the enantiomorph pair (sign-flip discriminator) + the diamond achiral control
  (zero-rotation discriminator). The enantiomorph pair is the primary discriminator: any artifact that is
  achiral (transport mis-scaling, numerical bias) is common-mode and cancels in the native−mirror
  difference.
- The genesis target (does a stable chiral soliton nucleate natively on the srs net without the injected
  `κ_chiral`?) is the Phase-1 question — out of scope for Phase-0.

**Kill conditions (honest closure):**
- Smoke A fails ⇒ trivalent scatter/connect is broken ⇒ fix-or-close before any Smoke B reading is
  trusted.
- Smoke B null (no signed holonomy, control already ~0) ⇒ lattice-chirality hypothesis falsified at the
  geometric-necessary-condition level ⇒ close branch, record mechanism, do not rescue.

---

## 5. Design rationale

**The chiral-mirror hypothesis.** AVE's chirality at `origin/main` is **injected by hand**: a one-
parameter coupling `κ_chiral = α·pq/(p+q)` (`cosserat_field_3d.py:115,131,522-523`), with `α` hardcoded,
applied as `A2_mu = (1+κ·h)·A2_mu`, `A2_eps = (1−κ·h)·A2_eps`. Canon's own scope caveat concedes this
"does not provide independent numerical verification of α-emergence" (`k4-tlm-simulator.md:75`). The v9
hypothesis: **handedness should be structural — a property of the lattice you build, not a knob you
turn.** A genuinely chiral bare net (srs) is the cleanest possible test: if optical activity falls out of
the geometry alone (signed per enantiomorph, zero on the achiral diamond), the handedness is *real and
structural*; if it does not, the injected-coupling status quo is, for now, the honest description.

**The grid-chirality engine gap (named at three levels in canon, not virgin):**
- cubic-vs-K4: `cem-methods-survey.md:66,103` ("forcing a chiral topology onto a flat, rectilinear grid";
  "Correcting the TLM topology from cubic to K4 would yield a native AVE vacuum simulator").
- degree-4-engine-vs-degree-3-Laves: FLAG A (`2026-06-07_2ndshell-screw-holonomy-result.md:77`).
- fully adjudicated against z=3: the 2026-06-07 resolution-of-record (§0).

**The optical-activity derivation chain is the genuinely virgin piece.** AVE-HOPF names it missing:
`open_questions.md:31` ("Without a derivation chain (K4 geometry → optical activity → wire-coupling form),
the prediction is hard to extend or critique"); `13_l3_chirality_review.tex:24` (the χ construction "makes
no claim about … polarization rotation"). Smoke B is the first executed test of that chain.

**Prior-art honesty (session-record, NOT canon).** A 4-port K4-crystal graft already SMOKE-FAILED on an
unmerged branch (`analysis/2026-06-09-crystal-k4-graft @ 09bb22d1`, SMOKE-3 real-space/phase-space
incoherence) — that failure was on the degree-4 graft, NOT a trivalent net, and informs why v9's Smoke B
is coordinate-disciplined (A46) and measured in polarization coordinates from the start.

---

## 6. Citation ledger (provenance discipline)

**CANON (verified file:line, `origin/main` @ f6ffd98d):**
`eq_axiom_1.tex:20` · `operators.md:45` (Op5) · `k4_tlm.py:64-93,101-119,117-118,211-217` ·
`k4-tlm-simulator.md:12,24-42,50-58,75` · `_orchestration/2026-06-07_lattice-net-resolution.md` ·
`research/2026-06-07_2ndshell-screw-holonomy-result.md:18,77` ·
`cosserat_field_3d.py:115,131,522-523` · `cem-methods-survey.md:66,103` ·
`cosmic-axes-and-frames-glossary.md:63-67` · `constants.py:96-98,133,239` · AVE-HOPF
`open_questions.md:31`, `13_l3_chirality_review.tex:24`.

**EXTERNAL MATHEMATICS (requires-verification; verified-in-scaffold by keepers, source class named):**
srs / (10,3)-a / Laves / Sunada-K4 net properties — trivalent, 120° balanced bonds, girth-10,
`I4₁32`/`I4₃32` enantiomorph pair, `8a` Wyckoff coordinates. Source class: Sunada, "Crystals that nature
might miss creating," *Notices AMS* 55(2) 2008; RCSR `srs`; Wells, *Three-Dimensional Nets and
Polyhedra*. **Asserted only via executable keepers, never from canon.**

**SESSION-RECORD (NOT canon — branch/orchestration state):** the v9 chiral-trivalent premise and its
adjudication status; the z4-walk-back branch `28026bed` (UNMERGED); the k4-graft smoke-fail `09bb22d1`
(UNMERGED); the injected-`κ_chiral` motivation. Cited as session-record, not as framework decision.

