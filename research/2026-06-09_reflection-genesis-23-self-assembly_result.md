# RESULT — Reflection-genesis: the (2,3) self-assembly (the "3" in the coupled engine)

**Date:** 2026-06-09 · **Lane:** implementer · **Branch:** `analysis/2026-06-09-reflection-genesis-23` (off `analysis/2026-06-09-reactive-entrainment-source`, worktree `AVE-Core-genesis23-wt`)
**Prereg (FROZEN):** `research/2026-06-09_reflection-genesis-23-self-assembly_prereg.md`
**Foundation (REUSED):** verdict II (`research/2026-06-06_saturation-tir-moving-boundary-result.md`, `manuscript/ave-kb/common/historical-precedents.md:28`) — the moving reflective Γ=−1 boundary CONVERTS collapse → confinement; the ω-photon self-traps (loc 0.94 vs 0.26 energy-term), the "2" Cosserat winding forms, charge=helicity confirms. **STANDALONE** result (`CosseratField3D`).
**Driver:** [`src/scripts/vol_1_foundations/reflection_genesis_23_self_assembly.py`](../src/scripts/vol_1_foundations/reflection_genesis_23_self_assembly.py) · **JSON:** `…_results.json` (N=24, 50 steps)
**Engine:** `ave.topological.vacuum_engine.VacuumEngine3D` (COUPLED K4⊗Cosserat) with `use_impedance_boundary`+`couple_v_sector`+`use_lagrangian_emf_coupling` (verdict-II wall ported coupled; KEEP-BOTH, default OFF).

---

## §0 — HEADLINE: not A. Two gaps, each LOCALIZED to a single mechanism. (mechanically C; B/C-boundary)

> **The (2,3) does NOT self-assemble from a photon in the coupled engine — and the run localizes
> the obstruction to TWO precise, independent mechanisms.** The brief's central question ("does the
> '3' = the V-sector U(1) fibre close onto the '2'?") is answered DECISIVELY, with a sharper diagnosis
> than the L3 history had:
>
> **GAP 1 (primary, robust — THE deliverable answer).** A transverse photon **NEVER ENERGIZES the K4
> V-sector at all** — `max|V_inc| = 0` to machine precision, across **every** config tested (soft wall,
> hard wall, explicit, implicit, EMF reciprocal ON and OFF). The longitudinal (V_inc, V_ref) phase-space
> is **UNPOPULATED** — the "3" never enters phase-space, so there is nothing to wind into a (2,3). The
> gap is **not "the winding is wrong"** — it is **"the engine has no transverse→longitudinal (ω→V)
> source channel that bootstraps the V-sector from zero."**
>
> **GAP 2 (secondary — FLAGGED, contradicts the brief's assumption).** The verdict-II clean confinement
> **does NOT port to the coupled engine for a free photon.** There is **no stable confining window**: the
> soft (non-pumping) wall **under-engages** (Γ_min = −0.003, the photon disperses, loc 0.48 < no-wall
> 0.54), and when the wall is driven hard enough to engage (Γ_min = −0.994) it **parametric-pumps**
> (|ω| 3.0 → 1144). The "2" **winding carrier** (c = 2) IS present and charge=helicity + spin-lock
> reproduce, but the **collapse→confinement step itself does not cleanly reproduce coupled** — exactly the
> Option-D §3 narrow window (`2026-06-06_optionD-impose-under-reflective-confinement-result.md`).

**ave-discriminator-before-synthesis / honest-closure (Rule 11).** The driver's **pre-registered**
boolean returns **C** (`2-confirms=False` because the coupled wall under-engages → `held=False`; `3-closes
=False`). I do **not** override that to B by relaxing the confinement criterion (that would be dropping an
adjudication criterion to convert ❌→✅). The honest read: **the verdict-II MECHANISM is standalone-
validated (the representation is not wrong in principle), but its COUPLED PORT has two localized gaps** —
the "3" source (primary) and the stiff-wall confinement window (secondary). **No electron-genesis claim**
(A needs the full signature {(2,3), ℏ/2, α=Q⁻¹, charge=helicity, chirality}; the "3", confinement, α legs
do not close).

**flag-don't-fix (contradiction surfaced, NOT silently resolved).** The brief states *"the '2' should
re-emerge (verdict II)."* The coupled engine **partly contradicts** this: the "2" **winding** re-emerges
(c=2) but the "2" **confinement** does not (no stable window for a free photon). Surfaced for Grant /
auditor — not reframed to match either expectation.

---

## §1 — substrate-native-check + the run (CP8 seed-not-plant, CP9 dynamical, A46 phase-space)

- **CP8 (load-bearing).** Seed = the **generative precursor** — a transverse, Z₀-matched, circularly-
  polarized helical ω-photon (`initialize_gaussian_wavepacket_omega`, `helicity=±1`). **NOT**
  `initialize_electron_2_3_sector` (which PLANTS the `θ=2φ+3ψ` knot). The K4 V-sector starts at
  **identically zero** — the test is whether the coupled channel self-assembles the "3" from the photon.
- **CP9.** Every number is measured from the **dynamically-evolved** fields (K4 `V_inc/V_ref/Φ_link`,
  Cosserat `ω/ω̇`), never a heuristic.
- **phase-space-coordinate-check (A46).** The (2,3) lives in **(V_inc, V_ref) phase-space on the Clifford
  torus** — the **three-layer canonical** (`cosserat_field_3d.py:931`, doc 101_ §9, Grant 2026-04-30):
  *Layer 1 = 0₁ unknot real-space; Layer 2 = SU(2) bundle (Cosserat ω hosts these); **Layer 3 =
  (V_inc, V_ref) (2,3) winding on the Clifford torus — the K4 V-tank, NOT Cosserat ω real-space.*** So
  the "3" is measured in the K4 V-sector phase-space; the Cosserat-ω real-space winding (the "2", `c`) is
  **diagnostic only**.

---

## §2 — the "2": winding carrier re-emerges (c=2); clean confinement does NOT port coupled (GAP 2)

Genesis-amplitude helical ω-photon (peak |ω| = 3.0), wall ON, vs a matched no-wall control (same seed),
N=24, 50 steps. Validity gate passed first (low-A photon: **Γ_min = −3.3×10⁻⁹** matched, **E_f/E_0 =
0.9964**, **max|V_inc| = 0** — V-sector silent).

| run (config) | localization (peak, PML-excl) | |ω|max | Γ_min (wall) | outcome |
|---|---|---|---|---|
| **soft wall** (K=60, implicit, the energize+LOCK config) | 0.968 → **0.482** | 3.00 → 0.98 | **−0.003** | **under-engages** — disperses |
| no-wall control (K=0) | 0.968 → **0.542** | 3.00 → 1.25 | −0.012 | disperses (free photon) |
| **hard wall** (K=400, explicit, verdict-II-exact) | 0.968 → 0.378 | 3.00 → **1144** | **−0.994** | **PARAMETRIC-PUMPS** |
| — energy-term (verdict II, standalone) | 0.967 → 0.256 | → 2.2×10⁵ | — | collapse (reference) |
| — moving wall (verdict II, **STANDALONE**) | 0.967 → **0.938** | → 3.9 | soft-mod | **held (the foundation)** |

**Reading.** In the COUPLED engine there is **no stable confining window** for a free photon: the soft
wall (the only non-pumping config) **under-engages** (Γ ≈ 0, holds *less* than the no-wall control), and
the hard wall (the engaged Γ = −0.994 short) **parametric-pumps** to |ω| = 1144 — the §6 stiff-wall
instability verdict-II flagged, **not tamed** in the coupled+free-photon case (Option-D §3 corroborated).
**The "2" WINDING carrier IS present** (Cosserat ω real-space c = **2**, §3); **the clean collapse→
confinement does NOT cleanly reproduce coupled** (GAP 2). max|V_inc| = 0 in **every** row — the K4 sector
never lights up.

---

## §3 — THE "3": does (V_inc, V_ref) close onto the "2" in phase-space? — **NO; the V-sector is EMPTY** (GAP 1)

The load-bearing A46 measurement, in matching coordinates, on the evolved soft-wall run:

| quantity | value | reading |
|---|---|---|
| **max\|V_inc\|** (K4 V-sector "3") | **0.000** | the V-sector is **identically zero** |
| **max\|Φ_link\|** (the U(1) fibre flux) | **0.000** | no fibre flux assembles |
| V_sq_sum (V-sector energy) | 0.000 | zero |
| (V_inc, V_ref) phase-space amplitude | 0.000 | **UNPOPULATED** |
| (V_inc) winding (w_tor, w_pol) | (0, 0) | undefined (no amplitude) |
| **phase-space populated?** | **False** | the "3" never enters phase-space |
| the "2" (Cosserat ω real-space, DIAGNOSTIC) | c = **2** | the toroidal winding carrier |

> **The "3" does not close — because it is never energized.** A transverse helical photon seeds the
> Cosserat ω-sector; the K4 V-sector ("3") starts at zero and **stays at zero to machine precision**.
> There is **no (V_inc, V_ref) trajectory** to trace a (2,3) Clifford winding. The headline is not "the
> winding is wrong" — it is **"the longitudinal phase-space is empty."**

**The mechanism, named precisely (the localized gap).** In the coupled `step()` (`k4_cosserat_coupling.py:709`),
the only ω→V channels are:
1. **Op14 z_local (the shared front, `_update_z_local_total`):** the Cosserat curvature modulates the K4
   bond impedance `z_local = √(S_μ/S_ε)` — **multiplicative on the scattering** of an *existing* V; `0`
   voltage in → `0` voltage out. It cannot SOURCE V.
2. **The reciprocal Lagrangian-EMF channel (`use_lagrangian_emf_coupling`, `_compute_emf_per_port:703`):**
   `EMF[port] = +2·V_inc[port]·∂L_c/∂V_sq`, applied as `V_inc += EMF·dt` — **proportional to V_inc itself**;
   it can amplify a nonzero V-sector but **cannot bootstrap one from zero**.

Empirically confirmed: max|V_inc| = 0 at step 0 AND at the end, **identically for EMF OFF and ON**. **The
engine has NO transverse→longitudinal (ω→V) source term that bootstraps the V-sector from zero.** That is
the entire "3" gap, in one sentence.

---

## §4 — charge = helicity — the sign-flip CARRIER reproduces

Seed +h vs −h (wall ON); integrated Beltrami helicity `H_bel = Σ ω·(∇×ω)`:

| seed | H_bel | localization |
|---|---|---|
| +h | **−78.4** | → 0.482 |
| −h | **+81.0** | → 0.500 |

The helicity **sign flips with the seed** (sign_flips = **True**) — the corpus `e⁻ (LH) / e⁺ (RH)`
charge=helicity carrier (matches verdict II §5). (`both_confine = False` only because the soft wall
under-engages — GAP 2, not a charge=helicity failure: the sign-flip IS the signature.)

---

## §5 — chirality: κ_chiral=1.2α parity-odd selection — present but SUB-THRESHOLD at the stable wall

The chirality bias in the shared front (`cosserat_field_3d.py:577-578`):
`A²_μ = (1+κ_chiral·h)·A²_μ_base`, `A²_ε = (1−κ_chiral·h)·A²_ε_base`. The helicity sign h biases which
side (μ vs ε) saturates first.

| seed | wall Γ_min | μ-short fraction |
|---|---|---|
| +h | −0.003 | 0.000 |
| −h | −0.004 | 0.000 |

The Γ_min differs by helicity sign (−0.003 vs −0.004 → the bias is **directionally present**) but the
soft wall barely engages, so the selection is **sub-threshold** (definite_selection = **False** at this
config; it registered at the tighter N=16 box, −0.029 vs −0.033). **The κ_chiral parity-odd bias is real
in the kernel, but at the only non-pumping wall it is too weak to cleanly select** — gated on GAP 2.

---

## §6 — spin/L: energized + LOCKED, NOT pumped — the discriminator is CLEAN ✅

Reactance pair recorded every step (A-Rule 10: ω C-state AND ω̇ L-state). LOCK run vs the hard-wall PUMP
control:

| run | |ω|max (C-state) | |L| range | verdict |
|---|---|---|---|---|
| **LOCK** (A=3.0, soft wall) | 1.26 → **2.63** | [4.49, 25.1] | **bounded — LOCKED** ✅ |
| PUMP control (A=6.0, hard wall) | 4.89 → **331.95** | — | **detonates — PUMPED** (→C) |

The spin is **energized and bounded (LOCKED)** at the stable config while the hard wall **secular-pumps**
(the wrong model). **The recurring secular-pump bug is avoided in the LOCK regime** — the energize+lock
discrimination (reactive-entrainment §2, the gyroscope) reproduces cleanly. (Note: the LOCK config that
avoids the pump is the SAME soft config that under-engages the wall — the two requirements, *confine* and
*don't-pump*, are not simultaneously satisfiable here. That tension IS GAP 2.)

---

## §7 — α from the leak — BLOCKED (needs the "3" Golden-Torus)

| quantity | value |
|---|---|
| wall Γ_min (soft) | −0.003 |
| T²_residual = 1 − Γ² (Op17) | 1.000 (nearly transparent soft short) |
| Golden-Torus α⁻¹ = 4π³+π²+π (target) | **137.0363** (`constants.py:204`) |

> **α⁻¹ is BLOCKED, not measurable here (honest).** The canonical α = the Γ=−1 leak with **Q = α⁻¹ =
> 4π³+π²+π** is a property of the **(2,3) Golden-Torus geometry** (R=φ/2, r=(φ−1)/2, R·r=1/4,
> `constants.py:200-204`) realized in **(V_inc, V_ref) phase-space**. With the "3" not closing there is
> **no Golden-Torus** — the bare soft ω-wall's residual leak (T²≈1) is **not** the electron's α-leak.
> **No α claim.** The leak SWEEP (Γ_min vs amplitude, figure 5) shows the wall engages soft→hard with
> amplitude (Γ −0.003 at A=0.5 → −0.99 at A≥4), and that the hard Γ=−1 short is the parametric-pump
> regime (→ C) — i.e. the engagement *exists* but only in the pumping regime.

---

## §8 — gap-localization diagnostic: GIVEN energy, does the wall WIND the V-sector to (2,3)? — NO

To separate the **source-question** (does the "3" get energized?) from the **topology-question** (given
energy, does the shared wall wind it to (2,3)?), a small K4 V-sector partner (a V-photon precursor scaled
to the engine's natural V_SNAP — NOT the (2,3) knot, transverse-winding structure) is co-seeded with the
photon, EMF channel ON:

| quantity | value | reading |
|---|---|---|
| V-partner seed max\|V_inc\| | 0.116 → end **0.086** | the V-sector, once energized, **persists/confines** (survives=True) under the shared wall |
| (V_inc) phase-space winding (w_tor, w_pol) | (0, 0), rel=0 | does NOT organize into (2,3) |
| closes (2,3)? | **False** | the wall confines but does NOT WIND |

> **Both halves of the gap localized.** (a) **Source-question:** the transverse photon does NOT energize
> the V-sector (§3) — the dominant, load-bearing gap. (b) **Topology-question:** even when the V-sector is
> *externally* energized, the shared Γ=−1 wall **holds** it (0.116→0.086, survives) but does **not**
> organize it into a (2,3) phase-space winding — the wall is a *confiner*, not a *winder*. The κ_chiral
> coupling enters only the saturation GEOMETRY (the shared front), never as a transverse→longitudinal
> converter nor a (2,3)-imposing torque. **The "3" needs a NEW coupled-channel primitive, not a re-tuning.**

---

## §9 — A/B/C verdict + DERIVED / VERIFIED / BLOCKED + the localized gaps

**ave-discriminator-before-synthesis (the hypothesis was the "3"-closes; the run decided):**

| signature leg | result | status |
|---|---|---|
| "2" winding carrier (Cosserat ω c=2) | present | ✅ re-emerges |
| charge = helicity (sign flips) | +h −78.4 / −h +81.0 | ✅ CARRIER reproduces |
| spin: energized + LOCKED vs pumped | LOCK bounded (2.6), PUMP detonates (332) | ✅ CLEAN discriminator |
| **"2" clean collapse→confinement (COUPLED)** | soft under-engages / hard pumps | ❌ **GAP 2** (does not port) |
| chirality: definite handedness (μ vs ε) | directionally present, sub-threshold | ◑ gated on GAP 2 |
| **"3": (V_inc,V_ref) (2,3) phase-space closure** | **V-sector ≡ 0, phase-space empty** | ❌ **GAP 1** (primary) |
| **α = Q⁻¹ (Golden-Torus 4π³+π²+π)** | needs the "3" → no Golden-Torus | ⛔ BLOCKED |

**VERDICT — mechanically C (pre-registered boolean); adjudicated as a two-gap localization at the B/C
boundary.** The verdict-II MECHANISM is standalone-validated (the representation is not wrong in
principle), and the "2" winding carrier + charge=helicity + spin energize-lock-vs-pump reproduce — but the
coupled-engine clean confinement does not (GAP 2) and the "3" never energizes (GAP 1). **No genesis claim.**

### DERIVED (this run)
- **GAP 1 — the "3" is a MISSING SOURCE CHANNEL, not a failed winding.** A transverse ω-photon leaves the
  K4 V-sector identically at zero (max|V_inc| = 0, machine precision) across all configs, because every
  ω→V channel is either geometric-multiplicative (`z_local`, 0→0) or `∝ V_inc` (the EMF reciprocal, cannot
  bootstrap from zero). The longitudinal (V_inc,V_ref) phase-space is **unpopulated** — the (2,3) has
  nothing to wind. **This is the precise, single-mechanism localization the L3 problem needed.**
- **GAP 2 — the coupled-engine wall has no stable confining window for a free photon:** soft → under-
  engages (Γ=−0.003, no confinement); hard → parametric-pumps (Γ=−0.994, |ω|→1144). The verdict-II clean
  confinement (loc 0.94, standalone) does NOT port coupled — the §6 stiff-wall integrator instability,
  Option-D §3 corroborated. The two requirements (confine AND don't-pump) are not simultaneously satisfiable.
- The partial positives that **localize** (not refute): the "2" winding carrier (c=2), charge=helicity
  (sign flips), and the spin energize-LOCK vs PUMP discriminator (bounded 2.6 vs detonating 332).

### VERIFIED (verify-before-cite — every cite greped/opened this session)
- verdict II: `research/2026-06-06_saturation-tir-moving-boundary-result.md` (loc 0.94 vs 0.26, "2"
  forms, charge=helicity) + `historical-precedents.md:28`. ✓
- Option-D narrow window: `research/2026-06-06_optionD-impose-under-reflective-confinement-result.md`
  (§3: soft sub-threshold below, hard parametric-pumps above; sector-coupling worsens). ✓
- the three-layer canonical: `cosserat_field_3d.py:931,1083` (Layer 3 = (V_inc,V_ref) (2,3) on the
  Clifford torus, NOT Cosserat ω real-space). ✓
- κ_chiral = 1.2α: `cosserat_field_3d.py:110,126` (`KAPPA_CHIRAL_ELECTRON = α·κ̃(2,3)`, κ̃=pq/(p+q)=1.2);
  the chirality bias `A²_μ=(1+κ_chiral·h)·…` at `cosserat_field_3d.py:577-578`. ✓
- Golden-Torus α⁻¹ = 4π³+π²+π = `ALPHA_COLD_INV` (`constants.py:204`); R,r,R·r (`:200-202`). ✓
- clm-fr3mos (photon = electron's same ω-wave): `photon-identification.md`. ✓
- the EMF source `∝ V_inc`: `k4_cosserat_coupling.py:703` (`emf = +2·V_inc·∂L/∂V_sq`); the coupled step
  channels: `k4_cosserat_coupling.py:709-751`. ✓
- **NOT cited:** the retracted 1.009 (per the prereg guard). ✓ absent.

### BLOCKED / NOT CLAIMED (honest ceiling)
- **The "3" (V-sector U(1) fibre) does NOT close** — no electron-genesis claim. The full signature
  {(2,3), ℏ/2, α=Q⁻¹, charge=helicity, chirality} is incomplete: the (2,3), confinement, and α legs are absent.
- **α⁻¹ = 4π³+π²+π is BLOCKED** — a Golden-Torus phase-space property that requires the "3" to close.
- The spin magnitude `ℏ/2` is **canonical input, not derived** (the conserved quantization that would
  derive ½ requires the (2,3) in phase-space — which does not close).
- **The coupled-engine "2" confinement is itself a localized gap (GAP 2)** — verdict-II clean confinement
  is standalone-validated only; it does not port to the coupled+free-photon case.

### The localized gaps — for the orchestrator / Grant (flag-don't-fix; do NOT draft the fix)
1. **GAP 1 (primary) — a missing TRANSVERSE→LONGITUDINAL (ω→V) SOURCE primitive.** The engine couples the
   sectors only through the saturation GEOMETRY (the shared front) and a `∝ V_inc` EMF reciprocal — neither
   bootstraps the V-sector from a transverse photon. Closing the "3" needs a coupled-channel term that
   converts confined transverse ω-energy into longitudinal V-sector amplitude (the chiral half-twist acting
   as a *source*, not a geometry modulation). **Substrate-physics question (is such a conversion canonical?
   — the Heaviside-deleted longitudinal scalar RE-ENGAGING) — surfaced for Grant + the corpus.** Per A44
   (missing-axiom-vs-engine-bug): plausibly an engine-completeness gap (the ω→V source is absent from the
   coupled step), to be adjudicated against Ax 1-4 before any new primitive is drafted. **I do not draft it.**
2. **GAP 2 (secondary) — the coupled stiff-wall has no stable confining window.** The §6 moving-hard-wall
   integrator instability (verdict II) is not tamed in the coupled+free-photon case. Either an implicit/
   symplectic-with-amplitude-dependent-stiffness integrator OR a different engagement protocol (the photon
   never self-focuses hard enough to engage the soft wall before it disperses) is needed. **Flagged; the
   brief's assumption "the '2' should re-emerge" holds for the WINDING (c=2) but NOT the confinement.**

### consistency-vs-emergence classification
- The "2" winding carrier, charge=helicity, spin-lock-vs-pump are **MANIFESTATION / CONSISTENCY** class
  (verdict-II structure re-instantiated). Not emergence of a new number.
- The "3" / α are the **EMERGENCE** legs that would have made this genesis — and they **do not close**.
  No emergence is headlined (ave-evidence-framing-discipline). No genesis claim.

### Figures (savefig, clickable)
1. [FIG 1 — phase-space (V_inc,V_ref) winding: does the "3" close?](../src/scripts/vol_1_foundations/genesis23_fig1_phase_space_winding.png)
2. [FIG 2 — localization (self-trap vs energy-term control)](../src/scripts/vol_1_foundations/genesis23_fig2_localization.png)
3. [FIG 3 — charge=helicity + chirality selection](../src/scripts/vol_1_foundations/genesis23_fig3_charge_chirality.png)
4. [FIG 4 — spin/L conservation (energized + locked, not pumped)](../src/scripts/vol_1_foundations/genesis23_fig4_spin_lock.png)
5. [FIG 5 — α-from-leak (Γ engagement vs A; Golden-Torus α⁻¹ target)](../src/scripts/vol_1_foundations/genesis23_fig5_alpha_leak.png)

### Skills fired
`substrate-native-check` (CP8 seed-precursor-not-plant, CP9 dynamical, §1) · `phase-space-coordinate-check`
(A46 — the (2,3) measured in (V_inc,V_ref), the three-layer canonical, §3) · `ave-canonical-leaf-pull`
(photon-id, (2,q) ladder, Golden-Torus α, κ_chiral, charge=helicity) · `ave-canonical-source` (κ_chiral=1.2α,
V_SNAP/V_YIELD, Z₀, ℓ_node, ALPHA_COLD_INV — zero new free params, asserted at run start) ·
`ave-resonant-amplification-check` (spin energized+LOCKED not pumped; the hard-wall secular-pump reproduced
as the → C control, §6) · `ave-discriminator-before-synthesis` (the "3"-closes was the HYPOTHESIS; the run
decided, §9) · `ave-discrimination-check` (the V≡0 finding is AVE-engine-specific) · `ave-evidence-framing-
discipline` (no genesis claim; α/emergence not headlined; mechanically-C not softened to B) ·
`ave-driver-script-honesty` (every number measured from the evolved field; PROXY/COORDINATE/BLOCKED inline) ·
`consistency-vs-emergence` (the "2" legs manifestation; the "3"/α emergence — do not close) ·
`verify-before-cite` (every cite greped; retracted 1.009 absent) · `flag-don't-fix` (the ω→V missing-source
gap AND the brief-assumption contradiction on confinement surfaced for Grant, not silently resolved).

### Reproduce
```bash
PYTHONPATH=src ./.venv/bin/python \
  src/scripts/vol_1_foundations/reflection_genesis_23_self_assembly.py
# → JSON + 5 PNGs in src/scripts/vol_1_foundations/   (env: GEN23_N, GEN23_STEPS override geometry)
```

### Canonical cross-refs
- `research/2026-06-06_saturation-tir-moving-boundary-result.md` (verdict II — the "2", STANDALONE, REUSED)
- `research/2026-06-06_optionD-impose-under-reflective-confinement-result.md` (the IMPOSE+DRIVE prior, verdict III; GAP 2 narrow-window precedent)
- `research/2026-06-09_reactive-entrainment-source_result.md` (spin energized+locked, the gyroscope)
- `manuscript/ave-kb/common/historical-precedents.md:28` (the localized "3" gap, verdict II)
- `src/ave/topological/cosserat_field_3d.py:931` (three-layer canonical — Layer 3 phase-space)
- `src/ave/topological/k4_cosserat_coupling.py:703,709` (the EMF `∝V_inc` channel + the coupled step)
- `src/ave/core/constants.py:200-204` (Golden-Torus R,r,R·r + α⁻¹=4π³+π²+π)
