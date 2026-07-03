# FROZEN PRE-REG — Writhe arc STAGE (a): the linear-channel |F|-ratio campaign

**Status:** FROZEN. Committed BEFORE the campaign driver (Chern-arc discipline).
**Grant ruling (2026-07-03, verbatim):** *"A full, and C"* — (A-full) the parity-odd SIGN chord observable with all baked-ins, AND (C) the magnitude-R formally booked as a named blocker (not silently dropped).
**Charter:** [`_orchestration/2026-07-02_writhe-force-ratio-build-brief.md`](../_orchestration/2026-07-02_writhe-force-ratio-build-brief.md) (steps 1–5).
**Built on:** Gate-0 (MERGED, PR #465) — [`2026-07-03_writhe-gate0-pair-feasibility_result.md`](2026-07-03_writhe-gate0-pair-feasibility_result.md) (STABLE-IN-A-WINDOW).
**Scope:** STAGE (a) = the linear ω-overlap channel in the buckle-OFF S1 host (`CrystalGraftV4`). Stage (b) (the κ_chiral saturation channel in the JAX `CosseratField3D`) is the pre-committed FINAL roll — a SEPARATE arc, defined in §9, fired only under the §8 bin condition.
**Classification (`consistency-vs-emergence`):** the parity-odd SIGN chord-candidate is an EMERGENCE-class claim IF it survives all gates; the Coulomb-recovery alternative is CONSISTENCY-class. Tagged per-bin (§8). No promotion past what the run shows.

---

## 0. Sector header + regime declaration

- **SECTOR.** T2 / Cosserat micro-rotation ω-sector; charge = Beltrami helicity on the ω-grade (S1 axiom chain). The pair force is a T2-sector momentum-flux interaction read through the ω-field stress tensor.
- **HOST / REGIME.** The S1 isolated-knot host (`_build_isolated_knot`: `CrystalGraftV4`, buckle OFF, photon OFF, lock ON, κ̃=6/5 α-clean). Reused verbatim from Gate-0. **The κ_chiral saturation-bias term is NOT active in this host** (buckle OFF) — handedness here is the seed-geometry winding SIGN evolving under the LINEAR ω wave equation `a_ω = c_ω²∇²ω − ω_gap²ω` (`crystal_graft_v4.py:240-243`). This is the LINEAR channel by construction.
- **PHASE-STATE.** Seeded quasi-stationary breathing (2,3) knots, evolved under the engine's real `step()`. Cold parity-even inter-knot medium.

### 0.1 Coordinate declaration (`phase-space-coordinate-check`, A46)
The (2,3) winding label is PHASE-SPACE (ω-tank LC quadrature + toroidal ω-polarization). The pair separation d and the force are REAL-SPACE (lattice-Cartesian x). The winding is read per-knot in its native phase-space coords (roll-to-center); the force is read in real-space x. Never cross-compared.

---

## 1. The measurement domain (frozen)

- **Separations d ∈ {34, 38, 44} cells** = {1.55, 1.73, 2.00}·L_core (L_core = 2R = 22). All THREE are Gate-0-STABLE under the full stability criteria: d=34/44 in the Gate-0 result; **d=38 verified STABLE this session** (RR, all 8 winding reads (2,3), E retained 95.0%, sep drift 0.0, alias 0.25 ≤ 0.34). Three separations give the separation-scaling check the charter requires (§5).
- **Configs:** RR, LL, RL, LR (the four handedness combinations) + null controls: single knot (the self-stress baseline, subtracted from every pair) and — cheap — knot+unknot (a winding vs a null-ω sphere) as a "one source is inert" control.
- **Handedness encoding:** the enantiomorph (R vs L) is the z-reflection mirror of the seed (`writhe_gate0_pair_feasibility._single_knot_fields(mirror=…)`), which inverts the poloidal winding sign. VERIFIED (Gate-0): the winding magnitude read stays (2,3) for both R and L; the SIGN is the handedness.
- **Window:** warmup 50, recording 200–300 steps (the Gate-0-certified window; the sign is a time-mean over the window). Cadence per §4.

---

## 2. THE CHORD-CANDIDATE OBSERVABLE (A-full): the parity-odd interaction SIGN

### 2.1 Force definition (operational, frozen BEFORE running)

The substrate-native force between the two knots is the **Maxwell field-stress-tensor normal stress** of the ω vector field, integrated over the mid-plane between them:

- **Stress density:** `T^{xx}_ω(x) = Σ_c (∂_x ω_c)(∂_x ω_c) − ½ Σ_c |∇ω_c|²` — the xx-component (normal stress on the x-plane) of the ω-field momentum-flux tensor. `∂_x ω` central difference; `|∇ω|²` the full gradient magnitude. (This is the SPATIAL stress T^{xx}, distinct from Gate-0's momentum-DENSITY flux T^{0x}=(∂_tω)(∂_xω); the force between objects is the spatial stress integrated over the separating surface — the standard field-theory force definition.)
- **Plane integral:** `F_raw(plane) = Σ_{interior, mid-plane} T^{xx}_ω` — the x-force on the RIGHT knot, PML-excluded (Rule 10), face-centered (mean of the two planes adjacent to XC).
- **Self-subtraction (mandatory):** `F_int = F_raw[pair] − F_raw[knot-A alone] − F_raw[knot-B alone]`, each evolved under the same host for the same window. The raw stress is dominated by each knot's own self-stress; the INTERACTION is the residue. Self-subtraction is REQUIRED (prototype: raw F is ~10× the interaction and the self-stress must come off).
- **Sign convention (frozen):** `F_int > 0 ⇒ REPULSIVE` (pushes the right knot further from the left knot, +x); `F_int < 0 ⇒ ATTRACTIVE`. This is fixed by the geometry (right knot at XC+d/2, +x points away from the left knot).

### 2.2 The chord observable = the SIGN of F_int, required plane-invariant

The chord-candidate is the **parity-odd interaction SIGN**: co-handed (RR, LL) vs anti-handed (RL, LR). **NOT** the magnitude ratio (that is the §3 named blocker). The sign is required to be **plane-invariant** (the same sign across the plane-position sweep, §4).

### 2.3 Pre-registered expectation (prototype provenance — stated as the expectation, NOT the verdict)

From this session's prototypes (self-subtracted, plane XC+0, d=34; scratchpad `proto_signtable.py`, throwaway):
- **QUANTIZED (2,3):** co (RR) = **+7.27e-3 REPULSIVE**; anti (RL) = **−1.28e-3 ATTRACTIVE**.
- The sign was consistent across all integration planes tried (XC±0/±1/±3): RR always +, RL always − (`proto_force.py`).

**Pre-registered expectation:** the quantized winding pair does **co-REPEL / anti-ATTRACT**, which **INVERTS the classical current-loop rule** (co-directed circulations attract). This inversion is the pre-registered chord-candidate signature. The campaign TESTS it at full window, all four configs, all three separations, with the invariance gates (§4) and the two baselines (§5) — it does NOT assume it.

---

## 3. THE MAGNITUDE-R NAMED BLOCKER (Grant's C — formally booked)

**`R = |F|_co / |F|_anti` is ILL-DEFINED at current engine capability.** Formally booked here as a named blocker, with two DERIVED reasons (not a debugging failure — a structural fact):

1. **Knot overlap at stable separations ⇒ no plane-conservative integral exists between them.** At the Gate-0 stable window (d = 34–44 = 1.5–2.0·L_core) the two knots' ω-fields overlap in the mid-region (Gate-0: mid ω amp 2e-2 at d=34). The mid-region is therefore NOT source-free, so the stress-integral is not plane-conservative: the interaction magnitude varies ~10× across integration planes (prototype `proto_force.py`: R = 2.73 at plane XC+0 vs 0.98 at XC±3). A magnitude ratio read at any single plane is knob-riding.
2. **Yukawa screening ⇒ no source-free far-field zone carries signal.** The ω field is gapped (`a_ω = c_ω²∇²ω − ω_gap²ω`), so the pair force is Yukawa-class short-range with range ξ = c_ω/ω_gap = **0.548 cells** (sub-lattice). Prototype `proto_range.py`: the self-subtracted |F| falls **F(34)/F(44) ≈ 2.6×10⁵ (co), 5.1×10⁵ (anti)** over 10 cells, exponential-fit decay length λ ≈ 0.8 cells (≈ ξ). By d=44 the force is 3×10⁻⁸ (machine-noise). There is NO source-free far-field surface with nonzero signal — the conservative far-field magnitude extraction (option B) is structurally dead. R itself drifts with d (3.51 → 4.82 → 6.86 at 34/38/44) as the signal sinks into noise.

**Transparency requirement:** the magnitude data (F_int per config, R per separation) is STILL REPORTED in the result — tagged **knob-riding / blocked**. The register §2.4 "dimensionless ratio" objective gets this honest status change explicitly (§8, result-doc + register note): the magnitude-ratio target is ill-defined in the linear channel at current engine capability.

---

## 4. Invariance gates (VCA-R19; the sign is the subject)

The SIGN must survive every knob. A sign that flips under a knob is not a forced observable.

- **(G-plane) Plane-position sweep:** F_int sign read at integration planes across the full valid mid-region (at minimum XC, XC±1, XC±3, and the widest planes still between the tube surfaces). **Forced ⇒ the SIGN is identical at every plane** for each config. (Prototype: RR always +, RL always − across XC±0/±1/±3 — the expectation.) A sign flip across planes ⇒ ILL-DEFINED (§8 blocker).
- **(G-window) Window/centroid knob sweep:** F_int sign under window lengths {150, 250, 350} and the two centroid-tracking params (half-region split position ±1 cell). Sign must not flip; the magnitude spread is reported but is the §3 blocker, NOT a sign gate.
- **(G-α) α→2α invariance:** the sign path is α-clean (host κ̃=6/5 literal, no α import). To confirm the sign is α-free, perturb any α-derived quantity that could enter (none should) and require the sign unchanged. Since the host imports no α on this path, this is a confirm-clean check; report `|dF_int/F_int|` under an α→2α perturbation of the (unused) α and require the sign invariant (expected: exactly unchanged, α does not enter).
- **(G-enantiomorph) Enantiomorph-consistency guard (at the SIGN level):** the co-handed sign from RR must equal the co-handed sign from LL, AND the anti-handed sign from RL must equal that from LR. Formally: sign(F_int[RR]) = sign(F_int[LL]) and sign(F_int[RL]) = sign(F_int[LR]). A mismatch = RED FLAG, no verdict (surface to Grant, do not resolve). (Prototype at magnitude level: RR=LL and RL=LR exactly — Gate-0/campaign expectation.)

---

## 5. TWO classical baselines, co-computed (the discrimination legs)

The load-bearing knives: a handedness-dependent sign EXISTING is not AVE-distinct unless the quantized winding differs from classical baselines. Both baselines run through the IDENTICAL self-subtracted extraction (§2.1).

### 5.1 Baseline (i) — unquantized classical circulation (current-loop / vortex knife)
A smooth toroidal ω circulation of matched geometry with p=q=1 (no integer winding), handedness = a sign (`proto_signtable.py` construction). **Validate-on-known (baseline's own):** coaxial CO-directed circulations (current-loop / solenoid class) must ATTRACT, counter-directed REPEL. Prototype: co (++) = **−9.11e-2 ATTRACTIVE**, anti (+−) = **+1.21e-1 REPULSIVE** — reproduces the current-loop rule. The knife: does the QUANTIZED sign structure MATCH this classical one? Prototype: quantized is co-REPEL/anti-ATTRACT — the **OPPOSITE** of classical ⇒ DISCRIMINATES. This is the pre-registered expectation; the campaign confirms it at full window.

### 5.2 Baseline (ii) — achiral charge-like source (Coulomb-recovery knife) [NEW per Grant's 1c-ii]
An achiral radial "hedgehog" ω source (curl-free, no helicity, static ω_prev=ω) — a monopole/scalar-charge class analog on the same ω machinery. Since a radial field has NO handedness, the z-mirror "co vs anti" is physically a no-op. **Expectation (Coulomb recovery):** co = anti (no parity-odd distinction). Prototype `proto_charge.py`: co = anti = +8.93e-5 (identical, both repulsive), `|co−anti|/max = 0.000`. The knife: the achiral charge pair produces NO parity-odd sign flip ⇒ the sign observable's parity-oddness is genuinely sourced by the winding handedness, not by mere geometry/charge. This is the Coulomb-recovery-vs-AVE-distinct control.

**Numerical-construction justification (per Grant's "justify the choice"):** both baselines are constructed numerically on the same host (not analytical statements) because the same self-subtracted lattice extraction must be applied to all three field classes for a like-for-like comparison — an analytical mediator statement would not share the lattice's discretization and self-stress structure, breaking the comparison. The achiral hedgehog is the cleanest charge-class analog in the ω-sector (the knots live in ω, so a V-sector scalar monopole would be a different sector; the ω-radial hedgehog keeps the sector fixed and removes only the handedness).

---

## 6. ω_gap PROVENANCE ROW (G4 ledger) — is the Yukawa range a prediction or an artifact?

**VERDICT: ω_gap is a HOST KNOB, not a substrate-derived constant. The Yukawa range is an artifact-SCALE (lattice units), NOT a physical prediction.**

- `omega_gap = 1.0` is a **default parameter** of the host (`crystal_graft_v2.py:65`, default 1.0; set literally in the S1 `_CFG`, `s1_winding_conservation_gate.py:55`). It is described as "ω_0 mass-gap = the ω tank's OWN inductive restoring" (`crystal_graft_v2.py:77`) but its VALUE (1.0) is a lattice-unit host choice, NOT imported from `ave.core.constants`.
- The canonical substrate mass-gap `OMEGA_C = C_0/L_NODE` (ℏ·OMEGA_C = m_e c², `constants.py:294`) EXISTS but is NOT what the host uses. The host's ω_gap=1.0 is in dimensionless lattice units with no mapping to OMEGA_C established on this path.
- **Consequence:** the Yukawa range ξ = c_ω/ω_gap = 0.548 cells is set by two host knobs (c_ω, ω_gap=1.0), so its physical value is undetermined — the short-range/screened character is a robust QUALITATIVE fact (a gapped field gives a Yukawa force), but the RANGE MAGNITUDE (0.548 cells) is not a substrate prediction. This is stated plainly in the result and register note: "the winding pair force is short-range/Yukawa (a gapped-field consequence, qualitatively robust); the range magnitude rides a host knob (ω_gap=1.0 lattice), not a canonical constant — so no bench-scale range is predicted from the linear channel."

---

## 7. Configs, order, driver plan

- **Order (frozen):** (1) validate-on-known: single (2,3) knot reads (2,3) in the campaign setup (gate everything). (2) The four configs RR/LL/RL/LR × three separations {34,38,44}, self-subtracted F_int, at the plane sweep. (3) The two baselines (i)+(ii) at matched geometry. (4) The invariance gates (§4). (5) Bin (§8).
- **Driver:** `src/scripts/vol_4_engineering/writhe_campaign_linear_channel.py`, importing the shared Gate-0 machinery from `writhe_gate0_pair_feasibility` (seed, roll, per-knot read, interior mask). Canonical constants only; every printed number computed in-run (`ave-driver-script-honesty`). Heavy evolves routed to the engine_sim lane.
- **Result doc:** `research/2026-07-03_writhe-campaign-linear-channel_result.md` (committed-verdict gates, Gate-0/Chern pattern).

---

## 8. FROZEN BINS

Exactly one fires. Committed here; not redefinable post-hoc.

1. **[PARITY-ODD SIGN CHORD-CANDIDATE]** — the charge-like baseline (ii) does NOT reproduce co-repel/anti-attract (it has no parity-odd distinction), AND the sign is plane-invariant (G-plane), AND enantiomorph-consistent (G-enantiomorph), AND the knob gates pass (G-window, G-α), AND the quantized sign is distinct from the classical circulation baseline (i). → **EMERGENCE-class parity-odd SIGN chord-candidate.** Mint the `clm-`; register §2.4 upgrade UNBUILT→DERIVED-SIGN-CHORD-CANDIDATE **with the honest bench-reachability note** (sub-nuclear/artifact-scale Yukawa range ⇒ expect a FORM result, likely NOT bench-reachable; the prior-art mapping onto torsion-balance/Eöt-Wash spin-dependent-force bound classes goes in the RESULT, auditor-marked). The magnitude-R remains the §3 named blocker.
2. **[COULOMB-RECOVERY, CONSISTENCY-class]** — the charge-like baseline (ii) DOES reproduce the same sign pattern as the quantized pair (i.e. the sign is not parity-sourced but geometry/charge-sourced). → **CONSISTENCY-class:** book honestly as the engine-derived interaction leg of Axiom-2 (like-windings repel/attract with the engine-computed sign — the coupling-class content Cleave lacked). Mint the consistency claim; **NOT a chord.**
3. **[ILL-DEFINED / named blocker]** — the sign fails plane-invariance (G-plane) OR the enantiomorph guard (G-enantiomorph) fails. → named blocker, no verdict; record the specific failing gate.
4. **[STAGE-(b) SUCCESSOR fires]** — the sign books classically-degenerate (bin 2) with NO AVE-distinct residue anywhere in the linear channel. → the pre-committed FINAL roll is the κ_chiral / saturation channel (§9). This is the ONLY escape; no other rescue.

---

## 9. STAGE-(b) successor definition (pre-committed FINAL roll)

**Fires ONLY under §8 bin 4** (linear channel books classically-degenerate with no AVE-distinct residue). Stage (b) = the **κ_chiral saturation-bias channel** in the JAX `CosseratField3D` engine:

- The parity-odd coupling `_reflection_density_asymmetric` (`A²_μ = (1 + κ_chiral·h_local)·A²_μ_base`) lives at **`src/ave/topological/cosserat_field_3d.py:554`** (NOT `src/ave/core/…` — the charter's path is corrected; see the charter's 2026-07-03 correction note). This term is **NOT active in the linear-channel S1 host `CrystalGraftV4`** (buckle OFF), which is exactly why the linear channel is parity-even-at-the-coupling and the sign (if any) comes only from seed geometry.
- Stage (b) would seed the pair in the saturation engine (walls at yield) where κ_chiral is live, and re-run the sign observable. It is a SEPARATE arc (separate prereg, separate branch), not this campaign. It is the pre-committed second-and-FINAL roll; no further escapes are authorized.

---

## 10. What the campaign does NOT establish

- **NO magnitude-R claim** (§3 named blocker — ill-defined at current engine capability).
- **NO bench-reachability claim** without the artifact-scale caveat (§6: the Yukawa range rides a host knob).
- The parity-odd SIGN, if it books as a chord-candidate, is a FORM result (a sign, a direction) — not a quantitative number. The register upgrade is DERIVED-SIGN-CHORD-CANDIDATE, not "a forced number."
- All results are on the linear buckle-OFF host; stage (b) says nothing until fired.
