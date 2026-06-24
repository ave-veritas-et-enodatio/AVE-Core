# Phase-space coupling-winding — RESULT: the (2,3) does NOT live as a conserved closed time-orbit in the A1↔ω coupling either; the orbit carries the CARRIER ratio, not the charge winding

**Status:** **RESULT (committed).** Two-stage dynamical phase-space orbit run per the frozen pre-reg.
**Date:** 2026-06-24
**Pre-reg:** `research/2026-06-24_engine-phase-space-winding_prereg.md` (commit 0d2b53e4) — followed exactly (all 4 forks Grant-ruled).
**Module:** `src/ave/solvers/phase_space_winding.py` · **Test:** `src/tests/test_phase_space_winding.py` (3 reader-tier + 7 `engine_sim`, all pass).
**Class:** CONSISTENCY (confirms/denies a *canonical home* for the charge-winding; the integer source is adopted-by-geometry, NOT a novel chord). Q=137 stays EMPTY. mass=A1 (PR#260) UNTOUCHED.
**Reuse (Rule 14):** `coupled_cage_winding.step()` (the conservative unitary S3 evolver), `_build_seeded_sim`/`seed_A1_sech`/`seed_winding` (the electron seed), #415's `_assemble_H` SA eigenvectors (Stage A). New code = the φ_rel phase-orbit winding reader (two methods), the energy ledger, the validate-on-known harness.

---

## 0. HEADLINE

> **VERDICT: BREAK.** Seeding the already-formed electron (A1 sech mass + (2,3) winding template) at the
> **V_yield transverse front** and evolving it **conservatively** (Crank–Nicolson/Cayley, unitary, joint
> energy conserved to **2.2×10⁻¹⁰**) over **600 steps (≈6 carrier periods)**, the inter-grade phase-space
> orbit **DOES close and DOES resolve** (period 526 steps, Nyquist OK, closure_quality 0.16) — and it reads
> **(p,q) = (−5,−5)** by **both** independent methods (unwrap-count AND circulation integral agree exactly).
> **(5,5) reduces to (1,1)** — a **carrier-lock** orbit, **NOT** the topological **(2,3)** (which requires
> gcd=1, both ≥2). The two sector global phases lock at the **carrier frequency ratio ω_b:ω_s** — 1:1 at the
> canonical resonant point ω_b=ω_s=1.0. **The (2,3) does NOT live as a conserved closed time-orbit in the
> conservative coupling.** The phase-space dynamical locus tests **NEGATIVE** — deepening the #415 real-space
> negative (the (2,3) is now null in **both** loci).

**The test is CLEAN; the answer is NO.** Every supporting gate holds:
- **Stage A PASS-the-gate**: φ_rel is a non-degenerate definable coordinate (eigenstate |cross|>0; under the conservative step φ_rel **moves**, E drift 4.6×10⁻¹³). Stage A did **not** kill the test (it is not gauge-collapsed). It **did** confirm a stationary eigenstate hosts only a **static** angle — the eigensolve's blind spot, and exactly why a dynamical Stage B was required.
- **Validate-on-known ALL PASS**: positive control (planted (2,3) → reads (2,3), two methods agree), null control (static→(0,0), (1,1)-Lissajous→(1,1); neither false-positives as (2,3)), pumped control (conservative run conserves to 5×10⁻¹¹, deliberately-pumped run trips the bleed gate — the conservative **guard is live**).
- **Energy ledger PASS**: joint norm conserved to 2.2×10⁻¹⁰ (no pumping) **AND** the sectors slosh hard (a1 relative swing 1.26, ≈47% of the total energy moves A1↔ω over the orbit). The pre-reg's PASS *signature* — "energy sloshes between sectors WHILE the integer stays put" — is present, **except the integer that stays put is (1,1), not (2,3).**
- **F4 two-reads-agree PASS** — *but honestly downgraded* (post-audit): unwrap and circulation return the identical pair (within 10⁻¹⁵), **but the two are algebraically the SAME wrapped-increment estimator** (they agree *by construction*, near-zero added assurance). The genuinely-independent, **load-bearing discriminator is the carrier-ratio detuning** (below): the winding ratio tracks ω_b:ω_s continuously (1:1→0.93, 2:3→0.65, 3:2→1.54, 1:2→0.48), which a topology-protected charge could NOT do — *that* is the proof the integer is the oscillator carrier ratio, not a topological charge. F4 is not load-bearing here; the detuning is.
- **α-clean PASS**: every read is a pure `arg()`; no Ω/A*-weighting; κ̃=6/5 host; Q=137 empty; the import-guard triad asserts no α-carrier reached the module.

**The single failing bin is `is_2_3` — the only thing in question — and it fails decisively.**

---

## 1. THE MECHANISM (named — single-mechanism honest closure, Rule 11)

The two Clifford-torus angles are the **global phases of the two coupled LC sectors**:
toroidal φ(t) = arg(Σ a_A1) (mass sector, "2"), poloidal ψ(t) = arg(Σ b_ω) (charge sector, "3").
Under the unitary evolution these global phases **precess at their carrier frequencies ω_b and ω_s.**
So the winding ratio of the phase-space orbit is set by **ω_b:ω_s, the carrier ratio** — an **oscillator
(Lissajous-of-the-carriers) artifact** — NOT by a topological (2,3) that would be carrier-independent.

**Direct confirmation (mechanism test):** detuning the carriers to ω_b:ω_s = 2:3 makes the global phases
wind **2:3** (measured ratio 0.644 vs the carrier ratio 0.667). The "winding" *follows the carriers*. At the
canonical resonant operating point ω_b=ω_s=1.0 — the point where a genuine (2,3) charge winding ought to
appear **independent of the carriers** — the phases lock **1:1**. The (2,3) the seed carries is a **geometric
Clifford-torus embedding of the seeded template** (a static phase texture, adopted-by-geometry), **not a
dynamically-generated conserved time-orbit** of the coupled evolution.

This is the deeper negative the pre-reg §4 named as a BREAK form: *"no commensurate (2,3) appears / a
different integer."* Both obtain — the integer is (1,1)-class and it is the carrier ratio, not (2,3).

---

## 2. WHAT THIS RETRACTS — AND WHAT IT DOES NOT (Rule 12 substitution-not-retraction)

**Retracts (per Rule 12 — preserve body, demote scope):** the open possibility, left after #415, that the
charge-winding has a *phase-space* coupling home that the real-space eigensolve missed. The proper
phase-space, dynamical, V_yield-front version of gate d has now been run and is **NEGATIVE**. Combined with
#415, the (2,3) is null in **both** loci tested:
- #415: real-space + static eigenstate + V_snap core → (2,3) bled out of the bound mode.
- this: phase-space + dynamical orbit + V_yield front → orbit carries the carrier ratio, not (2,3).

The corpus line to update: the eigensolve result's "⚠ SCOPE" caveat
(`research/2026-06-24_engine-coupled-eigensolve_result.md:25-35`) flagged the phase-space coupling-locus
re-test as *UNTESTED / scoped separately*. **It is now tested — NEGATIVE.** (Auditor lands the manual/KB
entry; this doc surfaces the finding.)

**Does NOT retract (independently grounded):**
- **charge = Link(∂Ω, F)** — the structural charge-quantization gate (`charge_quantization.py`,
  `charge_quantization_gate` → PASS) reads the (2,3) as a **real-space field-line linking integer**, planted
  and topologically protected (invariant under continuous deformation, jumps on unwind). That is a **separate
  coordinate** (real-space ω field-line topology) from the **phase-space time-orbit** tested here. This result
  does **not** touch it. The charge is still exactly quantized, finite, no-renormalization.
- **mass = A1** (PR#260) — untouched. The A1 mass sector seeds, evolves, and slosh-exchanges as designed.
- **The (2,3) as a geometric Clifford-torus / golden-torus embedding** — the seeded template's static phase
  texture **is** a (2,3) (validate-on-known confirms the reader sees it where it is planted). What is null is
  the claim that this (2,3) re-emerges as a **conserved closed dynamical time-orbit of the A1↔ω coupling.**

**Substitution-not-retraction discipline:** no new hypothesis is refilled into the now-tested-negative slot.
The phase-space-coupling-home hypothesis is retracted-by-scope; any successor (e.g. a *non-resonant* or
*nonlinearly-locked* winding mechanism) is a **new pre-reg with its own verification chain**, not a refill here.

---

## 3. THE NUMBERS (N=24, R=7, r=2.3, a1_radius=6 [WIDE, front reaches torus], 600 steps, dt=0.066)

| Read | Value | Pass? |
|---|---|---|
| Stage-A coordinate_definable | True (eig |cross|>0, φ_rel moves, E drift 4.6e-13) | gate clears |
| Stage-A stopped_here | False (not gauge-collapsed) | proceed to B |
| winding (p,q) [unwrap] | (−4.95, −5.05) → (−5,−5) | — |
| winding (p,q) [circulation] | (−4.95, −5.05) → (−5,−5) | — |
| two_reads_agree (F4) | True (|Δ|<1e-15) | ✓ |
| **is_2_3** | **False** — (5,5)=(1,1)-class, NOT (2,3) | **✗ (the make-or-break)** |
| period_steps / nyquist_ok | 526 / True | resolved (not Nyquist-limited) |
| closure_quality | 0.16 (orbit closes) | resolved |
| joint-energy max rel drift | 2.2e-10 | conserved ✓ |
| sector-exchange amplitude | 0.469 (≈47% sloshes A1↔ω) | sloshes ✓ |
| positive control (2,3)→read | (2,3), two methods agree | ✓ |
| null control (static / (1,1)) | reads (0,0) / (1,1) | rejects (2,3) ✓ |
| pumped control guard_is_live | conservative conserves; pumped trips | ✓ |
| α on verdict path | none (pure args; guard triad asserts) | clean ✓ |

**Mechanism cross-check:** ω_b:ω_s = 2:3 detune → measured winding ratio 0.644 (carrier ratio 0.667). The
winding tracks the carriers.

---

## 4. HONEST FLAGS / CAVEATS

1. **Seeded, not self-formed.** The electron is PLANTED (`seed_A1_sech` + `seed_winding`); the self-formation
   slot stays BARRED. This tests an *existing* electron's coupling dynamics — it does not, and cannot, speak
   to formation. (Same scope as #415 and the charge-quantization gate.)
2. **Resonant operating point.** ω_b=ω_s=1.0 is the canonical "1:1 resonant tank" of F2 (the pre-reg's own
   ruling: a 1:1 resonant tank with an *internal* 2:3 quadrature winding — NOT a 2:3 inter-tank frequency
   lock). The result is that the *global-phase* orbit on this resonant tank locks 1:1; the *internal* 2:3
   quadrature winding (the seeded template's static texture) does not promote to a dynamical orbit integer.
   The held-back 2:3 inter-tank frequency-lock (pre-reg F2, "emergence-burdened, re-opens a closed
   q-selection negative") was NOT tested and is NOT claimed.
3. **Orbit closure is window-dependent.** The orbit is in general **quasi-periodic** (incommensurate carrier +
   sloshing modulation); it closes cleanly only when the recording window lands near a return (N=24/600:
   closure_quality 0.16; N=20/500: 0.65 — does not close in-window). The *integer it reads is (1,1)-class in
   both cases* — the BREAK is robust to this; only the "closes cleanly" bookkeeping is window-sensitive. The
   driver's INCONCLUSIVE bin is reserved for the case where the orbit *neither* resolves *nor* closes; here it
   resolves (Nyquist OK) and reads a wrong-but-definite integer ⇒ BREAK, not INCONCLUSIVE (we do not rescue a
   clean negative).
4. **φ_rel vs (φ,ψ).** The headline F1 observable φ_rel = arg(Σ a_A1·conj b_ω) tracks φ−ψ; over the orbit it
   winds only −0.38 turns (the carriers nearly cancel in the difference at resonance) — i.e. φ_rel is a slow
   beat coordinate, the (φ,ψ) pair carries the read integer. Both are pure args; neither carries a (2,3).
5. **Q_H=p·q NOT adopted (F4).** The verdict rests on the two field reads agreeing, not on the helicity
   product formula. (The direct helicity integral's ~18% caveat from `charge_quantization.py` is not on this
   path.)
6. **CONSISTENCY-class, not a chord.** A PASS would have confirmed a canonical phase-space *home* for the
   charge-winding (adopted-by-geometry), NOT a novel α-free chord. The BREAK is a legitimate deeper negative,
   not a chord falsification. The AVE-distinct chord lives in the forward predictions (the bench), untouched
   here.

---

## 5. REPRODUCE

```
cd /tmp/pswind && PYTHONPATH=/tmp/pswind/src \
  /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \
  -m ave.solvers.phase_space_winding
```

or the full test gate:

```
cd /tmp/pswind && PYTHONPATH=/tmp/pswind/src \
  /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \
  -m pytest src/tests/test_phase_space_winding.py -m engine_sim -q
```
