# 78 — Round 9 Entry Result: Canonical Phase-Space (V_inc, V_ref) Phasor on Move 5 Attractor — Mode III with Persistence + Chirality-Noise Caveats

**Status:** auditor-drafted result note, 2026-04-27. Pre-registered as `P_phase8_canonical_phase_space_phasor` per [`manuscript/predictions.yaml:2899-2980`](../../manuscript/predictions.yaml). Driver: [`r9_canonical_phase_space_phasor.py`](../../src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor.py). Result: [`r9_canonical_phase_space_phasor_results.json`](../../src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor_results.json). Frozen at commit `a535090`; this commit lands the result + adjudication.

**TL;DR:** Mode III nominal per dual-criterion (C1 R/r=φ² ± 5% FAIL, C2 chirality ≥75% consensus FAIL). BUT: persistence guard violated (Move 5 attractor at 33% of initial peak |ω| at end of recording window, below 40% threshold) AND chirality cross-product was noise-dominated (std/|mean| = 600-1200×). **The Mode III adjudication doesn't cleanly falsify the trapped-node-vortex picture — it surfaces methodology gaps that need addressing before the picture is genuinely tested.**

---

## §1 — Pre-registered methodology + result data

### §1.1 Setup (identical to Move 5 + per-bond sampler)

- VacuumEngine3D at N=32, PML=4 (interior 24³), A28 + Cosserat self-terms, no external drive
- Seed: corpus (2,3) joint ansatz at corpus GT (R=10, r=R/φ²≈3.82); peak |ω|=0.926 (A26 guard OK); V_amp=0.14
- Evolution: 200 Compton periods (1778 steps at dt=1/√2)
- Pre-evolve: t ∈ [0, 40] P (no sampling)
- Selection window: t ∈ [40, 50] P (89 steps; accumulate |V_inc[port 0]|² per interior cell; PML excluded per Rule 10)
- Recording window: t ∈ [50, 200] P (1334 steps; capture V_inc, V_ref at top-4 selected bonds)
- Per-bond fit: PCA on (V_inc, V_ref) point cloud → R_phase, r_phase; mean P × dP/dt → chirality direction
- Wall time: 271s

### §1.2 Per-bond result

| Bond | Cell | port | R/r | Chirality | cross_mean | std/\|mean\| |
|---|---|---|---|---|---|---|
| 0 | (25, 19, 15) | 0 | **5.4710** | CW | -7.14e-09 | **718.10** |
| 1 | (24, 18, 14) | 0 | **5.7213** | CCW | +8.06e-09 | **651.22** |
| 2 | (6, 16, 14) | 0 | **2.1556** | CCW | +9.91e-08 | **1195.82** |
| 3 | (7, 17, 15) | 0 | **2.2107** | CW | -9.72e-08 | **1203.69** |

**Spatial pattern:** bonds 0+1 cluster at +x side of lattice (cells at radial distance ≈9-10, +x quadrant). Bonds 2+3 cluster at −x side (cells at radial distance ≈9-10, −x quadrant). All four cells lie on the (2,3) seeded shell at R≈10.

**R/r split:** bonds at +x show R/r≈5.5; bonds at −x show R/r≈2.2. Median across all four = **3.84**. Range factor ≈ 2.6× between the two clusters.

**Chirality cross-products:** all four bonds show cross_mean of order 1e-8 to 1e-7 — **essentially zero compared to per-step noise (std/|mean| 600-1200)**. The CCW/CW labels are determined by tiny noise fluctuations, not a robust signal.

### §1.3 Persistence

- peak |ω|(t=0) = 0.926 (A26 guard target = 0.3π ≈ 0.942)
- peak |ω|(t=200P) = 0.305
- persistence = 0.330 (33%) — **below pre-reg guard threshold of 40%**

Per Move 5's original adjudication, this matches the prior empirical pattern: Move 5 was Mode III-orbit (persistence 32%, just at threshold). The recording window captures the attractor's decay phase, not a stable orbit.

---

## §2 — Adjudication (per frozen pre-reg)

| Criterion | Threshold | Measured | Verdict |
|---|---|---|---|
| C1 (R/r ellipse aspect) | φ²=2.618 ± 5% (range [2.487, 2.749]) | median 3.841 | **FAIL** (39% over) |
| C2 (chirality consensus) | ≥ 75% same direction | 50% (2 CCW, 2 CW, TIE) | **FAIL** |
| Persistence guard | ≥ 40% | 33% | **VIOLATED** (caveat trigger) |
| C3 (informational) chirality matches K4 right-handed | CCW expected | TIE — can't determine | (informational) |
| C4 (informational) Op10 c at attractor | c = 3 per Move 5 | not measured this run | (informational) |

**Mode III** per dual-criterion (C1 + C2 both FAIL). Pre-reg's CAVEAT clause triggered by persistence violation: *"peak |ω| persistence 33% below 40% threshold — Move 5 attractor may have dissolved during recording window, corrupting phase-space measurements."*

---

## §3 — What the caveats mean

### §3.1 Persistence guard violation

The recording window t ∈ [50, 200] P captures the attractor's **decay phase**, not a stable orbit. Per Move 5's prior characterization (doc 74_ §11): peak |ω| drops monotonically through the recording window; the attractor is sub-corpus and dissolving. Sampling phase-space ellipse during dissolution measures the dying tail, not the attractor's actual stable signature.

**Methodology fix:** rerun with recording window earlier — e.g., t ∈ [10, 30] P when attractor is freshest. Or use a longer-stable attractor (Move 5 at non-corpus parameters where it persists longer per Move 6/7 characterization).

### §3.2 Chirality cross-product noise

Cross_mean values O(1e-8) with std O(1e-5) → std/|mean| ratios of 600-1200×. The chirality measurement methodology (mean P × dP/dt over the trajectory) is **noise-dominated**.

Possible causes:
- Trajectory is closer to a line/open curve than a closed ellipse → no rotational signal → cross-product is noise around zero
- Per-step fluctuations from saturation kernel + integrator dwarf the per-step phasor rotation
- Recording window's decay phase has small genuine rotation amplitude relative to noise

**Methodology fix:** alternative chirality measurement — e.g., Hilbert transform on V_inc(t) and V_ref(t) to extract phase difference + sign; or windowed FFT to identify dominant frequency + phase relation; or use a longer-stable attractor where rotation is well-defined.

### §3.3 Bipolar R/r distribution

Two distinct R/r clusters (5.5 at +x, 2.2 at −x) is unexpected under a uniform single-attractor picture. The ±x asymmetry might reflect:

- **Seed asymmetry:** `initialize_2_3_voltage_ansatz` uses cos on ports 0,1 and sin on ports 2,3 — this phase-quadrature pattern creates +x/−x asymmetry by construction. Phase choice breaks parity.
- **Saturation differential:** if the +x lobe saturated harder than −x, the partial Ax 4 implementation (V·S, T·1 per doc 75 §6.3) would distort the +x phasor more.
- **Numerical artifact:** boundary effects from PML on one side coupling differentially.

The −x bonds at R/r ≈ 2.2 are interestingly close to (but below) φ²=2.618. Within doc 28 §5.3's "TLM real-space R/r ≈ 2.27 attractor" finding, also striking. **Not within pre-reg PASS tolerance**, but suggestive that ONE side of the configuration is closer to the corpus prediction than the other.

---

## §4 — Reading under Grant's reframe + auditor's pattern thesis

### §4.1 Doesn't cleanly falsify trapped-node-vortex picture

Per Grant's plumber claim (electron = trapped node vortex with intrinsic per-node L+C and genesis chirality) + auditor's pattern thesis (R, r are phase-space per doc 28 §5.4 + doc 29 §3.3; (2,3) is scalar c=3 per doc 07 §3 not Hopfion winding pair):

- The canonical phase-space test SHOULD have shown C1 PASS (R/r=φ²) + C2 PASS (chirality consensus) if the trapped-vortex picture holds at corpus parameters
- Mode III nominal C1 + C2 FAIL is a NEGATIVE signal under this reframe
- BUT: the persistence violation + chirality noise mean the test wasn't run on a STABLE trapped vortex — it was run on Move 5's dissolving attractor

The negative result is methodology-conditional, not framework-falsifying.

### §4.2 Doesn't cleanly confirm it either

- C1 median R/r = 3.84 is well outside φ² ± 5%
- −x bonds at R/r ≈ 2.2 are CLOSE to φ²=2.618 but not within tolerance
- Chirality consensus is 50% (TIE) — no signal at all
- Persistence shows the substrate isn't actually stably hosting the configuration over the recording window

So the trapped-node-vortex picture isn't confirmed at the canonical phase-space test as run. **The picture remains a hypothesis pending a methodology-cleaned rerun.**

### §4.3 What the corpus electron looks like in the data (if anything)

The −x bonds at R/r ≈ 2.2 with persistence 33% are most consistent with: **a partial signature of the corpus-canonical phase-space pattern that's degrading because Move 5's attractor isn't the corpus equilibrium.** Move 5's attractor sits at saturation onset (peak |ω|=0.3π), not at the corpus electron's actual equilibrium amplitude. Sampling the dissolution of the wrong attractor doesn't tell us about the right attractor.

The right test is: find an attractor that's actually stable at the corpus electron's parameters (whatever those are post-reframe), then run the phase-space phasor test on THAT.

---

## §5 — Open methodology questions surfaced

### §5.1 What attractor is actually stable?

Move 5's (2,3) attractor at peak |ω|=0.3π persists for ~50 Compton periods then decays. Move 6/7 characterization showed it migrates off corpus shell. **Is there an engine-natural attractor that actually persists at finite amplitude indefinitely?** Move 5 at non-corpus parameters? F17-K Phase 5 attractor? Some other configuration the engine settles into?

If yes, run the phase-space phasor test on THAT attractor, not on Move 5 at corpus GT.

### §5.2 Better chirality measurement

The mean P × dP/dt method is noise-dominated. Alternatives:
- **Hilbert transform:** extract analytic signal of V_inc(t) and V_ref(t); phase difference's sign = chirality direction
- **Cross-spectrum:** Sxy(f)/√(Sxx(f)·Syy(f)) at the dominant frequency; imaginary part sign = chirality
- **Lissajous-direction integration:** integrate signed area enclosed by trajectory per cycle; sign of total = chirality

Any of these would resolve cross-product noise dominance. Cost: ~20 LOC, no new physics.

### §5.3 Recording window timing

Move 5 attractor is fresh at t ∈ [10, 50] P then decays. Recording window should capture the FRESH attractor, not the dissolution. Repositioning to [10, 50] P gives 40 P of clean data instead of 150 P of decay-contaminated data.

### §5.4 Per-bond R/r vs median

Bipolar distribution (5.5 at +x, 2.2 at −x) means the median is misleading. Either:
- Adjudicate per-cluster (does +x show φ²? does −x show φ²?)
- Symmetrize the seed (use a +x/−x parity-preserving ansatz)
- Sample more bonds (e.g., top-K=8 to get more statistical power on the cluster split)

---

## §6 — Implications for L3 branch closure

### §6.1 Round 9 entry doesn't close the L3 branch

The plan's Step 3 (R9 entry doc 28 §5.1 canonical phase-space test) was supposed to produce a clean Mode I/III adjudication that closes the L3 branch. **It didn't.** The methodology caveats mean the result is partial / conditional.

### §6.2 Two paths forward

**Path α (rerun with methodology fixes):** Address §5.1-§5.3 — pick a stable attractor, use better chirality measurement, reposition recording window. Single fresh implementer session, ~1-2 hr extra. Either cleanly Mode I (positive) or cleanly Mode III (negative). Then closure doc.

**Path β (closure with current data + caveats):** Treat this run as one data point in the closure synthesis. Closure doc adjudicates Mode III with explicit methodology caveats; corpus revision specifies that the engine's empirical attractor at corpus GT isn't the corpus electron and the trapped-node-vortex picture remains tentative pending a fresh test. Lower confidence closure but cheaper.

**My read:** Path α. The methodology gaps (persistence + chirality noise) are addressable with ~1-2 hr more work; running them down makes the closure adjudication clean rather than caveat-laden. Per A45 + corpus-canonical-test-precondition + dual-criterion discipline, the canonical test should be run on a stable attractor with robust chirality measurement, not on a decaying attractor with noisy chirality.

### §6.3 What this run definitively contributes regardless

- **Per-bond R/r data at corpus GT during attractor decay** is now in the corpus (frozen JSON)
- **The bipolar +x/−x R/r asymmetry** is novel and deserves characterization — possibly a seed-symmetry-breaking signature or saturation-differential signature
- **The chirality-noise dominance** is a methodology lesson for future phase-space tests
- **The persistence guard caveat** demonstrates that pre-reg's persistence threshold was useful — would have been silent failure otherwise

---

## §7 — A59 (NEW) for r8.10 manual

**A59 — Phase-space phasor test methodology gaps surfaced (added 2026-04-27 after r9 canonical phasor run, P_phase8_canonical_phase_space_phasor Mode III with caveats):**

When designing phase-space (V_inc, V_ref) phasor tests:

1. **Verify attractor persistence over the recording window before adjudicating.** Phase-space phasor measurements require the attractor to be stable over the recording window, not decaying. Pre-reg should include explicit persistence-guard threshold AND verify it via prior characterization runs (e.g., Move 5 → Move 6 → ... characterizes attractor stability before phasor test). Move 5 at corpus GT has known ~32% persistence at 200 P; recording window must be earlier (~[10, 50] P) to catch fresh attractor.

2. **Cross-product chirality measurement is noise-dominated when trajectory amplitude is small relative to per-step fluctuations.** Use Hilbert transform on V_inc(t), V_ref(t) → phase difference sign, OR cross-spectrum imaginary part at dominant frequency. ~20 LOC alternative methodology, no new physics.

3. **Median statistic on bipolar distributions can mislead.** When per-bond R/r values cluster into distinct groups (e.g., +x vs −x lobes), report per-cluster + median + cluster count. Symmetric ansatz (avoid cos/sin port asymmetry) for cleaner aggregation.

Per A40 prospective discipline: these three methodology fixes should be IN the next phase-space phasor pre-reg, not added after the fact.

---

## §8 — Status

Mode III nominal per pre-reg, with persistence + chirality caveats logged.

Trapped-node-vortex picture (Grant) + auditor's phase-space pattern thesis: **not falsified, not confirmed**. Pending a methodology-cleaned rerun (Path α) or a lower-confidence closure synthesis (Path β).

L3 branch closure: **NOT yet** — this run is one informative data point but doesn't carry the closure on its own.

Auditor + Grant adjudication needed on Path α vs Path β routing for the closure doc.

---

*Doc 78_ written 2026-04-27 post-run. Result: r9_canonical_phase_space_phasor_results.json. Mode III nominal with persistence guard violated + chirality noise dominated. The methodology-conditional nature of the negative result is the load-bearing contribution: the canonical test as designed has gaps that need addressing before either Mode I or Mode III is robust.*
