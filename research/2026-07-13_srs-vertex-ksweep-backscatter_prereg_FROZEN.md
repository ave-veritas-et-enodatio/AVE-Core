# PREREG (FROZEN) — srs vertex k-sweep backscatter driver (carrier-wave frame)

**Date:** 2026-07-13 · **Class:** satellite-session driver run (self-contained forward test).
**Role:** adjudicate the srs per-vertex Γ=−1/3 ontology fork (docket **T4** / the srs 1/9
real-vs-idealization fork; `manuscript/ave-kb/common/program-arc-map.md:306`) that A-class cascade
drainage's "primitive unit" language load-bears on.
**Handoff:** [`_orchestration/2026-07-13_srs-vertex-ksweep-handoff.md`](../_orchestration/2026-07-13_srs-vertex-ksweep-handoff.md).

**This document is frozen and pushed BEFORE the driver runs** (freeze-by-push rail). The production
config, metrics, three-way classifier, and sabotage-detection gates below are committed in advance;
the run adjudicates against them without further tuning.

---

## Sector header (mandatory)

- **MODE:** linear wavepacket propagation on the srs scalar-TLM lattice — a **carrier /
  homogenization property of the network**, NOT a saturation test.
- **REGIME:** cold lattice, **KERNEL OFF** — no Op14 saturation. The one-step operator is the pure
  combinatorial scatter+connect (`scalar_tlm_step`), which is **orthogonal ⇒ lossless to machine
  precision** (Axiom 3: the −1/3 is **reactive back-scatter / redistribution, never dissipation**).
- **PHASE-STATE:** freely propagating Bloch/wavepacket content, sub-yield throughout (amplitudes are
  linear; the step is amplitude-independent).
- **SECTOR:** bare-bond network primitive, **scalar / compression channel** (matches the canonical
  leaf `srs-vertex-scattering.md` sector header). Vector/torsion/chiral channels scoped OUT (the
  optical-activity SO(2) twist is irrelevant to backscatter magnitude and is not engaged).

---

## Mission

Adjudicate the **srs per-vertex Γ = −1/3 ontology fork** — *is the per-vertex mismatched-tee
reflection physically expressed for propagating collective (Bloch) modes, or is it homogenized away?*

Method: launch **forward wavepackets** on the srs lattice across a **k-sweep**; measure the
**backscatter fraction R vs k·ℓ_node**, KERNEL OFF (linear lattice).

## The arithmetic (per-vertex tee — stated, not re-derived)

Each **z = 3 vertex is a three-way tee**. A wave down one bond sees the **other two in parallel**
(Z₀/2), so the bare junction reflects **Γ = (2 − z)/z = −1/3** — a **COUNTING fact**, one bond
feeding two, immune to symmetric transformation. Power split: **|Γ|² = 1/9 reflected**, **4/9 + 4/9
transmitted**. This is **LOSSLESS reactive back-scatter** — **Axiom 3 is never threatened**
(matched-lossless-reciprocal-3-port theorem, |S₁₁| ≥ 1/3 floor). The **fork is whether the
per-vertex event is physically expressed for a carrier**, not whether it costs energy (it never
does). Canonical: `manuscript/ave-kb/common/translation-tables/translation-circuit.md:180`;
`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-vertex-scattering.md` §1
(`clm-v3port`; X38/X37, PR #619/#616/#620). **The per-vertex 1/9 is confirmed here as an
arithmetic identity (see meter-validation P3 below) — it is NOT what this test adjudicates.** This
test adjudicates the *collective-mode expression* of that per-vertex event.

---

## Frozen bins (three-way)

- **(i) HOMOGENIZATION-SPLIT** — *Grant's leaned frame; carrier-wave picture.* Backscatter **falls
  toward zero at long wavelength** (k·ℓ_node → 0) and **rises toward the per-vertex scale near the
  band edge**. Physical reading: **in-band collective Bloch modes never see a tee** — the periodic
  lattice's eigenmodes already diagonalize the vertex scattering; only content that cannot be carried
  collectively (near the band edge) resolves the individual junction.
- **(ii) REAL-AT-ALL-K** — localized/collective packets **scatter at the per-vertex scale
  (|Γ|² ≈ 1/9) at every k**; the tee is physically expressed independent of wavelength.
- **(iii) NULL-EVERYWHERE** — backscatter **consistent with zero at all k** (including the band
  edge); the lumped junction **never physically resolves** (−1/3 a bookkeeping idealization only).

### Standard-physics parity note (stated for honesty, NOT to prejudge)

For **any** correct linear periodic lattice, bin (i) is the *expected* outcome: a periodic medium is
transparent to long-wavelength carriers (the vertex scattering is diagonalized into the band
structure) and reflective at band edges/gaps — this is the ordinary "why crystals are transparent"
physics, and the SM/condensed-matter counterfactual gives the same. **Bin (ii) is the *incoherent*
limit** (disorder / single-site injection, where coherent forward cancellation is destroyed);
**bin (iii) would signal a broken measurement.** The test's real deliverables are therefore: (a)
**confirm** the homogenization-split *quantitatively* and locate/characterize the **band-edge rise**
(the muon-Q-relevant quantity); (b) **demonstrate** — via a disorder positive-control — that bin (ii)
is the incoherent limit and the meter is not blind; (c) rule the pristine lattice is not in (iii).
Per `ave-discrimination-check`: this result is **peer-with-SM consistency physics on the reflection
axis**, not an AVE-distinct chord. Its value is the *quantitative* band-edge characterization that
downstream muon-Q work load-bears on.

---

## Platform + rails (binding)

- **Platform firewall: loop-gap / srs platform ONLY.** srs scalar-TLM via
  `ave.core.chiral_lattice.build_srs_net` + `scalar_tlm_step` + `scatter_matrix`. **No
  `NativeCageIMEX` / cage / VacuumEngine3D work** — this is a linear srs-network property.
- **KERNEL OFF** — the combinatorial `scalar_tlm_step` carries no Op14 saturation term; verified
  lossless (gate G1). This is NOT the loop-gap genesis harness and does NOT create a new
  `chiral_lattice_v{N}` (per `ave-loop-gap-harness-discipline`: no version treadmill — a fresh
  linear-network measurement reusing the frozen v9 scaffold's graph + scatter primitives).
- **Freeze-by-push** — this prereg is its own commit, pushed before the driver runs.
- **Sabotage plants act on EVOLVED observables** — see §Sabotage; every plant corrupts the evolved
  backscatter field, not a post-hoc reduction.
- **DO-NOT-MERGE** — PR opens `[DO-NOT-MERGE]`; only Grant merges.

---

## Measurement design

### Substrate + why the time-domain observable (substrate-native-check)

The srs scalar-TLM one-step operator `M = CONNECT ∘ blockdiag(S)`, `S = (2/n)J − I` with `n=3`
(→ the −1/3 tee), is **real-orthogonal**. Consequences that fix the design:

1. **KERNEL OFF ⇒ exactly lossless** (`Σ|V|²` conserved to machine ε): confirmed, drift ~3×10⁻¹⁴
   over 400 steps (meter-validation P2).
2. **On a pristine periodic lattice, an in-band Bloch eigenmode never backscatters** (it is an
   eigenmode of M — pure phase rotation). The −1/3 is diagonalized into the bands. **Backscatter is
   therefore a property of a *localized* (finite-width) forward packet** whose k-content overlaps the
   band edge — the physically relevant probe (a bound particle like the muon is spatially localized,
   ∴ its k-content is broad). This is exactly the handoff's "launch wavepackets" measurement.
3. **An eigenmode-population ("backward-eigenmode fraction") observable is REJECTED** — momentum W
   does not commute with M, and ±k modes are frequency-degenerate, so the forward/backward split is
   basis-ambiguous within each degenerate eigenspace (empirically confirmed: Schur-orthonormalized
   R_eig is non-monotone garbage). The **conserved, well-defined observable is the time-domain
   backward-moving energy fraction** of an evolved forward launch.

### Observable (frozen)

Per (node u, port p), the stored incident pulse's **axial velocity** is
`w[u,p] = −bond_unit[u][p]·ẑ` (it arrived travelling from neighbour → u). With `ẑ = axis 2`:

- `E_fwd(V) = Σ V[u,p]² · relu(+w[u,p])`, `E_bak(V) = Σ V[u,p]² · relu(−w[u,p])`
- `b(t) = E_bak / (E_fwd + E_bak)` = instantaneous backward-moving energy fraction.

**Forward launch** at central wavevector k: Gaussian envelope `exp(−½((z−z₀)/σ)²)`,
`σ = width_frac·box`, `z₀ =` 12th-percentile of z; amplitude `env·cos(k·z)·relu(w)` seeded on
**forward ports only** (`w>0`) ⇒ net +z current `J_z(0)>0`, `b(0)=0` (meter-validation P1).

**Frozen estimator** `R(k) = mean_t b(t)` over the window `t ∈ [t_burn, ⌊t_transit⌋]`,
`t_burn = 15` (skip the broadband launch spike), `t_transit = box / (1/√3)` (one axial transit at
the long-wavelength network velocity `ANALYTIC_NETWORK_FACTOR = 1/√3`). Robustness companions
reported (not classifier inputs): `median_t b` over the same window, and the same over
`[t_burn, ⌊2.5·t_transit⌋]`.

### Constants (ave-canonical-source)

Imported from `ave.core.constants`: `L_NODE`, `Z_0`, `C_0`. **ℓ_node = 1.0** in the driver's
position units (`a_cell = 2√2` ⇒ NN bond length = 1.0000, verified; NN bond ≡ node pitch L_NODE per
`build_srs_net` docstring). Therefore **k·ℓ_node = k · (NN bond length) = k** in these units. A
`verify_constants()` cross-check runs before any output.

### Frozen production config

| Param | Value |
|---|---|
| Lattice | `build_srs_net(L, "right")`, scalar TLM, KERNEL OFF |
| Primary box | **L = 16** (N = 32 768 nodes) |
| Convergence boxes | L = 12, L = 20 (reported; not classifier inputs) |
| k·ℓ_node sweep | **18 points, linspace(0.15, 3.00)** (0 < k·ℓ ≤ π zone-boundary) |
| width_frac | **0.09** |
| Steps | `⌈3·t_transit⌉` per k |
| Disorder control | lossless random ±1 sign on fraction **p_dis = 0.5** of directed edges, **rng seed 12345**; same launch/estimator, all k |
| Enantiomorph gate | repeat sweep on `build_srs_net(L, "left")` |
| Band-structure x-check | `network_velocity_factor` / `measure_dispersion` → v_g(k), band edge |

### Frozen metrics

- `R_LW` = mean R over k·ℓ ∈ **[0.15, 0.50]** (long-wavelength window)
- `R_BE` = mean R over k·ℓ ∈ **[2.00, 3.00]** (band-edge window)
- `R_dis` = mean disorder-control R over **all** k (incoherent-limit anchor; expect ≈ 0.5)
- `Γ² = 1/9 = 0.11111` (per-vertex scale)
- `ρ = R_BE / R_LW` (band-edge rise), `σ = R_LW / R_dis` (long-λ suppression vs incoherent limit)
- Spearman rank-corr `s_rank` of R vs k over the sweep (monotone-rise test)

### Frozen three-way classifier

- **(i) HOMOGENIZATION-SPLIT** iff **ALL**:
  (i.a) `σ = R_LW/R_dis ≤ 0.35` (long-λ backscatter strongly suppressed vs the incoherent limit);
  (i.b) `ρ = R_BE/R_LW ≥ 2.0` (rises toward the per-vertex scale near the band edge);
  (i.c) `R_BE ≥ 0.5·Γ² = 0.0556` (band-edge backscatter reaches ≥ half the bare-tee scale — the tee
        resolves);
  (i.d) `R_dis ≥ 2·R_LW` (meter-not-blind: the incoherent lattice backscatters where the pristine
        one does not).
- **(ii) REAL-AT-ALL-K** iff `σ > 0.35` **AND** `ρ < 2.0` **AND** `R_LW ≥ 0.5·Γ²` (per-vertex
  reflection expressed even at long wavelength, roughly flat).
- **(iii) NULL-EVERYWHERE** iff `R_BE < 0.5·Γ²` **AND** `R_LW < 0.5·Γ²` (negligible even at the band
  edge). Sub-clause: if additionally `R_dis < 0.15` the meter is blind ⇒ **INDETERMINATE**, not (iii).
- else **INDETERMINATE / MIXED** — reported verbatim, no forcing.

Thresholds are physics-anchored round numbers (`σ≤0.35` = "below a third of incoherent"; `ρ≥2` =
"at least doubles"; `R_BE≥½·per-vertex`), chosen with margin so the classification is not knife-edge.

---

## Sabotage plants (act on EVOLVED observables) + detection gates

Each plant corrupts the **evolved field** (not a post-hoc reduction). The frozen gates below must
catch them; the driver runs each plant and asserts the corresponding gate trips.

| Plant | Evolved-field corruption | Fakes | Caught by |
|---|---|---|---|
| **A — kill-backward** | zero all backward-moving port energy each step (project onto forward ports) | bin (iii) | **G1** (lossy → drift ≫ ε) |
| **B — inject-source** | add a fixed backward-port amplitude each step | bin (ii) floor | **G1** (adds energy → drift ≫ ε) |
| **D — lossless fwd↔bwd mix** | per-step orthogonal rotation (angle θ=0.15) mixing one fwd + one bwd port per node | k-independent (ii)-like floor | **G3** (flat-elevated R fails monotone-rise) + **G2** collapse |

**Frozen detection gates:**
- **G1 — Lossless:** max relative energy drift over the pristine run **< 1×10⁻⁸**. (Catches A, B.)
- **G2 — Meter-not-blind:** `R_dis ≥ 2·R_LW`. (Anchors σ; disorder must out-scatter pristine.)
- **G3 — Band-structure consistency:** R(k) rises monotonically over the upper half of the sweep,
  `s_rank ≥ 0.7`, and the R-rise region overlaps the v_g→0 band-edge region. (Catches D's flat R.)
- **G4 — Enantiomorph symmetry:** `|R_R − R_L| / R < 0.20` per k-band (backscatter magnitude is
  chirality-blind — the counting −1/3 is identical for both hands). (Catches asymmetric corruption.)

The **pristine** production run must pass **G1–G4**; a plant that trips a gate is *detected* (the
test cannot be fooled by an evolved-field corruption without the gate firing).

---

## The sharp edge the resolution must survive (NAMED consistency check, not a result)

The **electron is also node-scale** — it binds at **R\* ≈ 1.6 ℓ_node**
(`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:133`;
**dimensionally-forced / CANDIDATE-class consistency check**, NOT a discriminating test) — **yet its
Q → ∞** (terminal pole, `Q_tank = 4π³+π²+π = α⁻¹`, lossless). So **proximity to node scale cannot
itself price the channel.** The resolution the adjudication must survive: **proximity PRICES the
channel only where an onward mode exists to carry the drained power; topology GATES it.** The
electron sits at a **terminal pole** (no onward mode ⇒ nothing to drain into ⇒ Q→∞); the muon's
content **straddles a region with an onward channel** (candidate origin of its finite loss-Q). **This
is a named consistency check the adjudication must not contradict — it is NOT assumed as a result of
this driver.** A bin-(i) result (band-edge-only backscatter) is *consistent* with it (band-edge = the
"onward channel exists" regime); a bin-(ii) result (per-vertex price at all k) would *tension* it
(the electron's terminal-pole Q→∞ would then need a separate reason it pays no price).

---

## Honest cite-flags (evidence-framing-discipline)

- **"muon content ~0.74-cell radial"** — **Grant's leaned estimate (2026-07-13), NO corpus receipt**
  (searched research/ + ave-kb/). Nearest anchors: muon sub-pitch band `[r_turn, ℓ_node]` dominating
  the overshoot (`research/2026-07-08_p4-forward-voltage-threshold_RESULT.md:115`) and muon ∇A
  gradient scale ~1–2 ℓ_node (`research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md:374`).
  **Carried as a lean, not a fact; this driver does not use or test 0.74.**
- **Q_μ ≈ 3.5×10¹⁷ cycles** (`manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md:14`)
  — the *middle-of-ladder* muon value is **flagged NOT-verified at this HEAD**
  (`research/2026-07-13_registers-walk_framing.md:129`, pending `ww0giq5he`). Carried as a cited lean.
- The **band-edge = muon-Q mechanism** link is a **downstream hypothesis, not adjudicated here**;
  this driver only characterizes R(k) on the bare srs network.

## Meter-validation pilots run BEFORE this freeze (transparency)

Meter-validation (instrument checks, **not** the production R(k) curve) was run to confirm the
observable and set physics-anchored thresholds with margin:
- **P1** forward launch: `J_z(0) > 0`, `b(0) = 0.0000` ✓ (clean traveling launch).
- **P2** lossless: energy drift `3.5×10⁻¹⁴` / 400 steps ✓ (KERNEL OFF confirmed).
- **P3** single-port delta → reflected power `0.1111 = 1/9` exactly ✓ (meter reads the per-vertex scale).
- **P4** pristine backscatter **rises with k** while the disorder control sits flat-high (~0.50) ✓
  (qualitative regime = rising ⇒ leans (i); thresholds set as round fractions, not to these values).
The production run (frozen config above) is what is officially adjudicated.

---

## References (grep-verified anchors — 2026-07-13, worktree base d0037d8f / origin/main 046d883c)

- `manuscript/ave-kb/common/translation-tables/translation-circuit.md:180` — srs z=3 vertex =
  intrinsically mismatched reciprocal 3-port; Γ=(2−z)/z=−1/3 counting fact; |Γ|²=1/9 reactive
  back-scatter (Axiom 3 — reactive, not loss); |S₁₁|≥1/3 floor; circulator escape PENDING-GRANT.
- `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-vertex-scattering.md` §1
  (`clm-v3port`) — canonical bare-vertex characterization (X38/X37, PR #619/#616/#620).
- `manuscript/ave-kb/common/program-arc-map.md:306` — the open T4 fork ("is the 1/9 per-vertex
  reflection a real network event or an idealization a distributed merge smooths out?").
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:133`
  (+ `research/2026-07-01_hollow-vortex-sigma-gate_result.md:312`) — electron binds at R\*≈1.6 ℓ_node
  (dimensionally-forced / CANDIDATE-class consistency check).
- `research/2026-07-08_p4-forward-voltage-threshold_RESULT.md:115` + `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md:374`
  — muon radial-extent nearest anchors (the "~0.74-cell" figure is Grant's unreceipted lean).
- `manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md:14` — Q_μ≈3.5×10¹⁷
  (flagged NOT-verified at this HEAD, `research/2026-07-13_registers-walk_framing.md:129`).
