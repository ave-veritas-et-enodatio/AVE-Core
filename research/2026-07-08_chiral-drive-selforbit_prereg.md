# Chiral-drive self-orbit — does a CURL-type chiral bias drive a persistent, LOSSLESS self-orbit of the (2,3) loop?

**Status:** **FROZEN PRE-REG.** Frozen BEFORE any result exists (timestamp-ordered: this commit precedes the run commit).
**Date:** 2026-07-08 · **Branch:** `analysis/chiral-drive-selforbit` · **Base SHA:** `5219a0b0aa0e12b10d5a6838c56b383892b9d35b`
**Class:** MECHANISM test (does chirality-as-curl drive a lossless self-orbit that *behaves like* rest mass). **NOT** a derivation of m_e. Q=137 stays EMPTY. mass=A1 (PR#260) UNTOUCHED.
**Module:** `src/ave/solvers/chiral_drive_selforbit.py` · **Test:** `src/tests/test_chiral_drive_selforbit.py` · **Driver:** `src/scripts/vol_2_particle_physics/chiral_drive_selforbit_run.py` · **Results:** `results/chiral_drive_selforbit_results.json`

---

## §0 THE PHYSICAL PICTURE (Grant-walked, Task #22 — TEST it, do not re-litigate)

Rest mass = the energy of a persistent, **LOSSLESS** self-orbit of the (2,3) loop, driven by a
**CURL-type chiral inter-node bias** — a rotational EMF / trapped flux threaded through the loop.
Analogy: a cyclotron orbit. A background "magnetic" flux forces a charged loop into a closed
circulation at a flux-set rate, doing ZERO net work (conservative); the loop energy reorganizes
into a persistent circulation. Chirality supplies the curl. Rate should be ω_C-like; the orbit
energy is the mass analogue; the DC-averaged inter-node mismatch is the network readout.

**Substrate-native encoding (the discriminator's whole content):**
- a **curl** bias = a nonzero plaquette/loop flux (Peierls link phases whose loop sum ∮ ≠ 0);
- a **gradient** bias = a pure gauge (∮ = 0, a node-potential difference).
This is the Aharonov–Bohm / persistent-current-in-a-ring distinction — established physics that a
flux drives a persistent lossless current while a pure gauge cannot.

**Corpus grounding (grep-verified this session, base SHA `5219a0b0`):**
- Chirality = srs / I4₁32 handedness sign `h∈{+1,−1,0}` (`crystal_engine.py:41`). The per-cell
  chiral converter is a CONSERVATIVE velocity-space rotation by θ_χ = κ̃·h·g_front
  (`crystal_engine.py` docstring). Coupling κ̃ = 6/5 = pq/(p+q) is the (2,3) topology, α-free.
- A chirality phase **θ_χ = 2π·ν_vac** (ν_vac = 2/7, α-free) and a **gauge-invariant loop flux
  `3χθ_χ` — explicitly Aharonov–Bohm-like** — are ALREADY established in
  `research/2026-06-20_node-circulator-coupling.md:116` (the 3-port ring recovers a real chirality
  flux the 2-port cannot carry). **That result also found the non-reciprocity MAGNITUDE is IMPOSED
  (echo), because the cubic-FDTD chiral-crystal engine AVERAGES CHIRALITY OUT**
  (`device-circuit-models.md:163`; node-circulator §4 VERDICT: IMPOSED-AT-MAGNITUDE). So: chirality
  supplies a genuine loop curl at the ring level, but the coarse lattice does not hand us its net
  magnitude — a NET flux must be imposed.
- The just-closed electron-lock arc (`research/2026-07-08_electron-lock-arc_CLOSE.md`) — five
  negative loci — **LACKED a chiral drive entirely** (grep-verified: `electron_lock_barrier.py`
  contains no chiral/flux/curl/Peierls term; "chiral" appears only in the α-leak GUARD). This test
  asks whether the chiral CURL flux is the missing ingredient those loci never had.

## §1 THE ASSEMBLY (frozen)

Smallest LOSSLESS (unitary) node-network that supports a (2,3) loop and a threadable loop flux: a
tight-binding node **ring of N nodes embedded on the (2,3) torus knot**. State `ψ ∈ ℂ^N` — the LC
analytic amplitude per node (`ψ = q + i·p`: Re = C-state/displacement/voltage, Im = L-state/
momentum/flux-linkage; the reactance pair, recorded at every step). Nearest-neighbour loop coupling
`t`. This is the phase-space (LC-quadrature) amplitude; the circulation is read as the winding of
`arg(ψ)` around the loop — the SAME phase-space charge="3"=LC-quadrature coordinate the corpus uses
(node-circulator §1, A46-compliant), NOT a real-space Cartesian moment.

Hermitian generator (⇒ evolution is EXACTLY unitary, no damping is representable):

    H[ψ]_n = −t (e^{+iθ_n} ψ_{n+1} + e^{−iθ_{n−1}} ψ_{n−1}) + ε_n ψ_n
    ε_n    = ω_0 · √(1 − (|ψ_n|/A_y)²)     (Op14/Ax4 saturation kernel = local clock; OPTIONAL)

- **θ_n = the Peierls link phase** (the curl/gauge bias). The loop flux is the gauge-invariant
  Wilson loop **Φ ≡ ∮θ = Σ_n θ_n around the physical (2,3) node ring** — genuinely ON the native
  loop (the ring's one independent 1-cycle), NOT a Cartesian coordinate square (avoids the
  "positive-control-mislocated-on-Cartesian" failure class). A ring is the MINIMAL system whose only
  gauge-invariant content is exactly this one flux — no confound.
- **Saturation ε_n**: the substrate √(1−A²) local-clock modulation. Real diagonal ⇒ H Hermitian ⇒
  unitary preserved. Set A_y→∞ (OFF, linear) for the CLEAN discriminator; ON for the A1/robustness arm.
- **Integrator:** Crank–Nicolson / Cayley `ψ_{n+1}=(I−iHΔt/2)(I+iHΔt/2)^{-1}ψ_n`. The Cayley
  transform of a Hermitian H is UNITARY BY CONSTRUCTION (norm exact to machine precision; energy
  exact for linear H). For saturation-ON, H is evaluated at the midpoint density (one Picard
  corrector). **No damping term exists in the scheme** — a circulation that needed dissipation could
  not appear here (Ax3-lossless HARD gate).

**Seeds (static, NON-circulating — the (2,3) loop at rest):**
- **SEED-B (primary, emergence):** a localized REAL raised-cosine bump on the loop. Real ⇒ zero net
  circulation at Φ=0; NOT an eigenstate ⇒ circulation must genuinely BUILD under the flux (DC-averaged).
- **SEED-A (exact anchor):** the uniform REAL k=0 mode (flux-off ground state). Zero circulation at
  Φ=0; under flux carries the exact persistent current 2t·sinΦ (constant-in-time eigenstate).

**Bias configurations (equal per-link magnitude |Φ/N| — only ∮ differs):**
- **CURL:** θ_n = Φ/N ∀n → ∮ = Φ ≠ 0 (a genuine flux; cannot be gauged away).
- **GRADIENT:** θ_n = (Φ/N)·(−1)^n → ∮ = 0 (a pure gauge = discrete gradient of a sawtooth χ_n;
  same per-link magnitude). Verified pure-gauge: χ_n = −(Φ/2N)(−1)^n reproduces it.

## §2 THE ARMS (frozen BEFORE the run)

1. **CURL (the mechanism).** SEED-B static; turn on the curl flux (∮=Φ≠0). Does a PERSISTENT
   circulation EMERGE (steady node-to-node self-orbit)? Measure the DC-averaged net circulation
   ⟨C⟩ over the recording window and sweep Φ ∈ {0, …, ≲π}. **Rate law:** is the circulation rate set
   by the flux, ⟨C⟩ ≈ 2t·sinΦ (∝ Φ for small Φ, like ω_cyclotron ∝ B)? SEED-A gives the exact anchor.
   *Anti-tautology:* circulation must EMERGE from the static (C=0-at-Φ=0) seed; we do NOT plant a
   spinning loop.
2. **GRADIENT control (kill-or-confirm).** SEED-B static; pure-gauge bias (∮=0) of EQUAL per-link
   magnitude. Its DC circulation MUST be ≈ 0. If the gradient ALSO drives a persistent circulation,
   the mechanism is WRONG.
3. **CONSERVATIVE check.** Report H-drift `max_t|⟨H⟩(t)−⟨H⟩(0)|/|⟨H⟩(0)|` and norm-drift for the
   curl run. Lossless (small drift) required; a circulation needing dissipation ⇒ NOT-LOSSLESS.
4. **MASS OBSERVABLE.** DC-averaged inter-node mismatch `M` = time-mean of the mean normalized bond
   current (the ∮/node-potential asymmetry the network reads). Does the circulation ENERGY
   `E_circ(Φ) = ⟨H⟩_DC(Φ) − ⟨H⟩_DC(0)` track `M` via a definite law? Pre-registered expectation
   (kinetic-from-circulation): **E_circ ∝ M²** (momentum²-like). Report the fitted exponent + R².
   **Bias-off (Φ=0) → M=0 and E_circ=0 (liveness).**
5. **A1 sourcing (secondary, saturation-ON).** Does the curl circulation produce a localized A1
   dilatation (trapped bulk = persistent local |ψ_n|² concentration)? Measure DC density localization
   (participation-ratio / peak) under curl vs bias-off. If yes, the mechanism sits BEHIND mass=A1
   (reconciles with canon #260) rather than competing. Tagged PROXY (density concentration ≠ the A1
   scalar grade proper).

## §3 VERDICT ROUTING (pre-registered; the substrate routes it)

- **[CHIRAL-DRIVE-VIABLE]** — curl drives a persistent LOSSLESS circulation (Arm 1 + Arm 3) AND the
  gradient control does NOT (Arm 2 null) AND the DC-mismatch tracks the circulation energy (Arm 4).
  ⇒ mechanism plausible; worth proposing a full arc.
- **[DISCRIMINATOR-FAILS]** — the gradient ALSO drives it, OR the curl does not. ⇒ mechanism wrong.
- **[NOT-LOSSLESS]** — the circulation requires dissipation / is not conservative (H-drift large or
  it decays without a drive). ⇒ contradicts Ax3.
- **[NO-SOLITON]** — the (2,3) loop excitation disperses / no stable loop survives the window.

## §4 ANTI-TAUTOLOGY + DISCIPLINE GATES (report every one HONESTLY — do NOT smooth a threshold to force a bin)

- **EMERGENT-not-PLANTED:** verify the seed carries C≈0 at Φ=0 (both seeds). The circulation appears
  ONLY under the flux. We do not plant a rotating state (a spinning loop trivially persists on a
  lossless substrate; that would be vacuous).
- **BIAS-OFF NULL (liveness):** Φ=0 ⇒ ⟨C⟩≈0 AND M≈0. If nonzero at Φ=0, the observable is broken ⇒ HALT.
- **GRADIENT CONTROL:** ∮=0, equal per-link magnitude ⇒ must be null (Arm 2). This is the kill-test.
- **CONSERVATIVE:** H-drift and norm-drift small; the scheme carries NO damping term (Cayley-unitary).
- **PHASE-SPACE COORDINATE (A46):** circulation read as winding of `arg(ψ)` on the LC quadrature, on
  the native loop — matching coordinates; ∮ computed around the PHYSICAL ring, not a Cartesian square.
- **α-CLEAN:** the verdict observables are pure `arg()`/current ratios; no ALPHA/Q_TANK/m_e/V_SNAP on
  the verdict path. Constants (NU_VAC, OMEGA_C) enter ONLY as off-path scale anchors.

## §5 HONEST SCOPE + ANTI-OVERCLAIM (critical — decided BEFORE the run)

- **This targets the MECHANISM, not a value.** Do NOT tune the flux to hit ω_C or m_e and call it a
  mass derivation. The VALUE is a calibration (ECHO) unless the chirality magnitude is INDEPENDENTLY
  forced. Corpus already says it is NOT: θ_χ = 2π·ν_vac has ν_vac = 2/7 = **GR-imported** (K=2G,
  `constants.py:381` — a one-parameter family, not lattice-forced), and node-circulator §4 found the
  chiral magnitude IMPOSED because the engine averages chirality out. **Expectation: the ω_C-rate
  flux is a FREE / IMPORTED knob, not forced.** We will report this explicitly.
- **The discriminator is partly EXPECTED-MATH.** On a ring it is a mathematical fact that a pure
  gauge cannot drive a gauge-invariant current while a flux can (like the charge-quantization gate's
  "topological invariance is expected math"). The AVE-content being tested is NOT "AB physics works"
  (it does, trivially) but: (a) that such a self-orbit can be genuinely **LOSSLESS** (Ax3-compatible —
  not a priori guaranteed), (b) the DC-mismatch **mass-observable law** E_circ∝M² (a definite network
  readout), (c) that the (2,3) loop **supports it stably** (the NO-SOLITON check), and (d) the
  connection that chirality→curl is corpus-established (node-circulator), so this is the drive the
  electron-lock loci lacked. The chord potential lives in the MECHANISM + the observable, NOT the value.
- **No self-formation.** We SEED the (2,3) loop and evolve it; the barred self-formation slot stays barred.

**Pre-test physics check (surfaced to Grant, pre-design):** *is a single-ring Wilson-loop flux a
faithful stand-in for "chirality threads the (2,3) loop", or does the (2,3) knot's Seifert-surface
structure carry flux the single 1-cycle misses?* Frozen decision: the ring's one independent 1-cycle
IS the complete gauge-invariant curl content of a loop; the plaquette-resolved (2D torus-surface)
generalization is named OUT-OF-SCOPE future work, not smuggled into this minimal test.
