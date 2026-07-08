# Electron-lock RECONNECTION-BARRIER test — does GENUINE confinement rescue the (2,3) winding from being a carrier-ratio ECHO?

**Status:** **FROZEN PRE-REG.** SHA-pin before the run. Frozen BEFORE any result exists (timestamp-ordered: this commit precedes the run commit).
**Date:** 2026-07-08
**Class:** CONSISTENCY (confirms/denies whether *confinement installs a topological energy barrier* that rescues the charge-winding; NOT a novel-value chord). Q=137 stays EMPTY. mass=A1 (PR#260) UNTOUCHED. charge = Link(∂Ω,F) ∈ ℤ (static topology) UNTOUCHED.
**Module:** `src/ave/solvers/electron_lock_barrier.py` · **Test:** `src/tests/test_electron_lock_barrier.py` · **Results:** `results/electron_lock_barrier_results.json`
**Reuse (Rule 14):** `coupled_cage_winding.step()` (the conservative UNITARY S3 evolver, `coupled_cage_winding.py:394`), `seed_A1_sech`/`seed_winding` (the electron seed), `front_gate` (the α-free R_II=4/7 saturation-front gate), `compute_Q_link` (the real-space winding reader). New code = the moving-Γ=−1 reactive confinement wall (Hermitian on-site potential), the phase-space + real-space winding readers, the 4 arms, the barrier homotopy, the discipline gates.

---

## §0 SCOPE-LOCK (the load-bearing distinctions)

- **This is the LAST SWING.** Both loci already read AGAINST Reading B (grep-confirmed):
  - REAL-SPACE winding HOLDS but is INERT (`research/2026-06-24_engine-s1-winding-dof_result.md:25`); the same arc's S3 is DISPERSE-FALSIFIED (`research/2026-06-24_engine-s3-cavity-pinning_result.md:4,50` — "even with the winding demonstrably conserved, the coupling does not pin the core").
  - PHASE-SPACE winding reads the LC CARRIER RATIO, not topology (#417 BREAK, `research/2026-06-24_engine-phase-space-winding_result.md:29`): the CARRIER-RATIO DETUNING sweep found the "(2,3)" tracks ω_b:ω_s CONTINUOUSLY (1:1→0.93, 2:3→0.65, 3:2→1.54, 1:2→0.48). A topological integer CANNOT slide; a carrier ratio does exactly that.
  - Production `rigid_template` mode CANNOT unwind (frozen ê_w, conserved BY CONSTRUCTION, `coupled_cage_winding.py:158,240`); a "held" there is a data-structure artifact.
- **The ONE un-run version is the BARRIER.** Every prior run measured whether a LABEL stayed constant; NONE measured whether there is an ENERGY BARRIER against a REAL reconnection. Pre-test physics (walked with Grant): *"a knot holds because untying it COSTS energy, losslessly — not because a bookkeeping integer is conserved."*
- **RECONNECTION-CAPABLE, never FROZEN.** The physical arm evolves the FREE `dispersive_vector` director (ω = a_w ∈ C³) so unwinding is physically POSSIBLE. `rigid_template` (frozen ê_w) is used ONLY as a PROTECTED-reachable bin-liveness control — never as the physical hold-claim.
- **CONSERVATIVE, never PUMPED.** The generator H is Hermitian ⇒ `step()` (Crank–Nicolson/Cayley) is EXACTLY UNITARY ⇒ joint energy conserved to GMRES tol. NO external drive. NO damping. A hold bought by damping is the top trap (Ax3-lossless: "no damping fakes a pin").
- **α-clean / phase-only.** The phase-space observable is a pure `arg()`. No ALPHA/Q_TANK/V_SNAP/KAPPA_CHIRAL_ELECTRON on the verdict path. An AST firewall asserts no α/m_e NAME token in any verdict-path function.
- **SEED, never FORM.** We seed the already-placed electron and evolve it. The barred self-formation slot stays BARRED.

## §1 THE ASSEMBLY (frozen)

Evolve a reconnection-capable (dispersive_vector) director WITH a moving-Γ=−1 confinement wall ON, under the UNITARY evolver, and read the winding in PHASE-SPACE (Clifford torus) AND real-space.

- **Spine:** `CoupledCageWinding`, `winding_mode="dispersive_vector"`, `winding_on=True` (the A1↔ω coupling live), `seed_A1_sech(0.60, radius=6.0)` + `seed_winding` (canonical (2,3), R=7, r=2.3), N=24, pml=4, dt=0.066.
- **Wall:** `ConfinedCageWinding` — a HERMITIAN reactive on-site potential `U_conf(x) = clamp_strength·g(x)` on the ω-block diagonal, `g` a MOVING saturation-front weight ∈[0,1]. This is the UNITARY-scheme faithful analog of `cosserat_field_3d.py:1920`'s reactive `V_clamp = ½K·relu(−Γ)·|ω|²` (`use_impedance_boundary`) — a LOSSLESS, energy-STORING reflective short keyed on the moving front. Real diagonal ⇒ H Hermitian ⇒ CN exactly UNITARY.
  - **BC-not-bulk (stated):** the wall is the Op17-bounded moving-front reactive confinement, NOT the singular bulk `_reflection_density` term (`cosserat_field_3d.py:441`, the genesis-24 detonation, CP10). Default `wall_form="omega_front"` = `front_gate(|ω|/ω_yield)`, a reflective SHELL at the ω-sector saturation front (the μ-side short locus where the ω-photon focuses).
  - **⚑ HONEST FLAG:** the literal `CosseratField3D.use_impedance_boundary` is a velocity-Verlet clamp on the JAX Cosserat u/ω with a Meissner (S_μ,S_ε) Γ=−1; the scalar unitary spine does not carry the μ/ε split, and the velocity-Verlet hard-clamp CANNOT pass the "energy-conserving (unitary)" HARD gate (its own docstring reports ~1e4–1e5× runaway at default dt). On the spine the wall is the reactive V_clamp analog keyed on the |ω|-front proxy. The correspondence is the V_clamp term; the μ/ε provenance is replaced — stated, not smoothed.
- **Readers:**
  - PHASE-SPACE (Clifford torus): toroidal `φ(t) = arg(Σ_x a_A1)` (counts "2"), poloidal `ψ(t) = arg(Σ_x ê_w·a_w)` (the ω-sector global phase along the winding template, counts "3"). Pure args ⇒ α-free.
  - REAL-SPACE: `compute_Q_link(Re(a_w), R, r)` — the reconnection observable; `Q_link_raw` (fractional) exposes partial/mid-slip winding.

## §2 THE FOUR ARMS (frozen BEFORE the run)

1. **LIVENESS / CONTROL** — dispersive_vector, `wall_form="off"`, `winding_on=False`, zero drive. MUST unwind/disperse (real-space `Q_link_raw` decays away from the seed integer). Proves the reconnection channel is OPEN. If it does NOT unwind ⇒ the test is VACUOUS ⇒ HALT.
2. **TEST (hold?)** — dispersive_vector, wall ON (`omega_front`), `winding_on=True`, zero drive, tuned to (2,3). Does the real-space (2,3) HOLD (vs Arm 1)? Does the phase-space read it?
3. **DETUNING KILL-GATE (DECISIVE)** — wall ON, sweep carrier ratio ω_b:ω_s over {1:1, 2:3, 3:2, 1:2} plus the (2,3) reference. Phase-space `ratio = (toroidal net turns)/(poloidal net turns)`. Does `ratio` TRACK ω_b/ω_s continuously (ECHO, #417 signature) or stay PINNED at a constant (TOPOLOGICAL)? This gate decides the effort.
4. **BARRIER** — the energy cost to force a partial unwind. Adiabatic homotopy θ_λ = (1−λ)·(2φ+3ψ), λ∈[0,1] (λ=0 fully wound → λ=1 unwound). At each λ compute the confinement Hamiltonian `H_conf(λ) = E_grad(ω_λ) + V_clamp(ω_λ)` (elastic gradient energy via the native L_D + the reactive wall storage). `barrier = max_λ [H_conf(λ) − H_conf(0)]`. `budget` = the zero-drive fluctuation of `H_conf` over the free Arm-2 evolution (range). `barrier > budget` ⇒ lossless topological protection.

## §3 VERDICT ROUTING (pre-registered; the substrate routes it)

- **[PROTECTED]** — Arm 3 detuning-INVARIANT (ratio pinned) AND Arm 4 barrier>budget AND Arm 2 holds (real-space integer stable vs Arm 1). ⇒ Reading B REAL: confinement rescues the topology; the electron holds because untying costs energy; lossless. Chord-worthy.
- **[ECHO]** — Arm 3 detuning-TRACKS. ⇒ #417 confirmed on a harder test; confinement does NOT rescue; the phase-space "(2,3)" is the carrier ratio; Reading B closes negative.
- **[NOT-PROTECTED]** — Arm 2 disperses like Arm 1 (and Arm 4 barrier≤budget). ⇒ confinement protects neither mass core nor winding; Reading B closes negative.

The phase-space (Clifford) locus is where the KB says the electron IS (`ave-kb/CLAUDE.md:22`); ECHO there is the headline route. If the real-space and phase-space loci DISAGREE (e.g. real-space holds with barrier but phase-space tracks), that is a FINDING to SURFACE (flag-don't-fix), not to reconcile by fiat.

## §4 ANTI-TAUTOLOGY + DISCIPLINE GATES (report every one HONESTLY — do NOT smooth a threshold to force a bin)

- **Arm 1 liveness:** channel demonstrably open (it unwinds) — else HALT (vacuous).
- **Energy conservation:** joint-norm H-drift < 1e-5 across EVERY arm — else numerical leak, not physics. Report the number for each arm.
- **Firewall:** AST-scan the verdict-path functions (phase-space reader, detuning-classify, barrier-measure, verdict) for any `ALPHA`/`M_E`/`m_e` NAME token — must be ABSENT.
- **Scale-invariance:** verdict identical at datasheet V_yield=1.0 and at 2×V_yield (the α-echo magnitude in V_yield must NOT reach the verdict).
- **BC-not-bulk:** confirm the confinement path is the Op17-bounded moving-front reactive wall (the V_clamp analog), NOT the singular bulk `_reflection_density` term. State which is wired.
- **Phase-space locus:** winding read on the Clifford torus (phase-space), not only real-space. State the reader.
- **Bin-liveness:** show each verdict bin is REACHABLE via synthetic/control configs (PROTECTED via rigid_template hold + synthetic pinned+barrier; ECHO via the dispersive detuning sweep; NOT-PROTECTED via wall-off dispersal) so the negative is informative, not a dead branch.
- **Detuning-gate can-fire:** show the gate CAN report "tracks" (feed it the frozen-template/uncoupled config #417 showed tracks) AND CAN report "pinned" (a synthetic phase-locked config).

## §5 MAKE-OR-BREAK (pre-stated)

- **PROTECTED:** all three of {detuning-invariant, barrier>budget, real-space hold-vs-Arm1} — confinement installs a lossless topological barrier; Reading B survives the last swing.
- **ECHO / NOT-PROTECTED:** the detuning tracks (ECHO) or the winding disperses with no barrier (NOT-PROTECTED) — the effort closes NEGATIVE. Per Rule 12 this RETRACTS to "confinement does not install a reconnection barrier" — it does NOT walk back charge = Link(∂Ω,F) (static topology, independently grounded) nor mass=A1 (#260).
- **INCONCLUSIVE (Rule 11):** the reconnection channel does not open (Arm 1 fails ⇒ vacuous), OR an energy leak (H-drift ≥ 1e-5) — report, re-scope; do NOT rescue a clean negative into INCONCLUSIVE.

**Honest closure (Rule 11):** a confirmed ECHO is a REAL result. Do NOT hunt for a PROTECTED pass. If the pre-registered predictions fail and a single mechanism explains all failures, record the falsification and close the branch.
