# STAGE 0 PREREG — the α-clean spine lock (re-scoped Gate 0)

**Created:** 2026-06-23 · implementer lane · branch `analysis/engine-stage0-alpha-clean-spine`
**Epic:** [`_orchestration/2026-06-23_full-engine-pathway.md`](../_orchestration/2026-06-23_full-engine-pathway.md) Stage 0
**Supersedes:** the original Gate 0 (PR #394 HARD-STOP) which targeted the wrong
host (`CosseratField3D` bakes Q=1/α). This re-scopes onto the α-clean foundation.

**Status:** FROZEN (pre-run). Result doc lands separately.

---

## SUBSTRATE-FIRST SECTOR HEADER (prereg, before any standard word)

- **SECTOR:** the A1 dilatation mass-cage (Γ=−1 confinement wall) on the α-clean
  spine. The α-clean spine = the cold `CrystalEngine` (`crystal_engine.py:51`,
  `converter_on=False` ⇒ A1 SCALAR BULK branch ONLY, no (2,3) micro-rotation
  winding) + the `master_equation_fdtd` c_eff(V) cage kernel
  (`c_eff²=c₀²/S`, `S(A)=√(1−A²)`). The K4 node set is **named** as the single
  shared grid TARGET; the Cartesian-∇²V → K4-graph-Laplacian (z=3) COLLAPSE is
  Stage 3 (the two-grid bridge, the FIRST RECONCILIATION MILESTONE), explicitly
  NOT Stage 0. Stage 0 erects the α-clean foundation + grid scaffold ONLY.
- **REGIME:** cold (the lossless-cage ring-down is a COLD measurement; A≪1 launch
  transient + a posited deep core; no drive pumping the bulk).
- **NO winding/coupling:** `converter_on=False` throughout. The two-"3"s guard
  (`master-equation.md:20`) holds by construction — charge/spin/μ are NEVER read
  off the scalar cage; the winding is never wired into the (V_inc, V_ref) phasor.

## VCA (vacuum-circuit-analysis) FRAMING — MANDATORY (Grant directive)

Frame circuit-native:

- The **Γ=−1 wall = the impedance short** (Z_core→0 as A→1; the α-free
  Z_eff=√S route, `resonant-lc-solitons.md:38`; `crystal_engine.gamma_bulk()`).
  The cage is a *boundary condition* (a reflecting short), NOT a bulk confining
  potential (substrate-native-check CP10 — a bulk well detonates at the wall).
- The resonator **Q is MEASURED by ring-down** — Hilbert-envelope decay,
  `Q = ω₀·τ/2`, `ringdown_Q` (`src/tests/engine_acceptance/_bulk.py:466`).
  NEVER read from a closed form. The α-echo VALUE Q = 4π³+π²+π ≈ 137
  (`ALPHA_COLD_INV`, `constants.py:243`) — equivalently the GEOMETRIC
  golden-torus Q-form 16π³(R·r)+4π²(R·r)+π·d (`cosserat_field_3d.py:2425`,
  =137 at R·r=¼) — IS the contamination this stage exists to EXCLUDE.
- The spine = the **α-free LC network**. The Q-determining mechanical quantities
  are α-free dimensionless ratios (`ν_vac=2/7`, `c_L²/c_T²=10/3`, K=2G), never α.

---

## FULL SKILL DISCIPLINE (Grant directive — all applied)

| Skill | Applied as |
|---|---|
| **ave-prereg** | corpus-grep done (Step 2 below); no prior Stage-0 result doc exists — first build of re-scoped Gate 0. Guard/scrubber/landing-zone primitives ALREADY exist + battle-tested (8 consumers); Stage 0 assembles them onto the spine, does NOT reinvent. |
| **substrate-native-check** | CP1 wave-propagation leapfrog (not Lagrangian/min); CP2 V-sector A1 scalar; CP8 cold posit is consistency-class (NOT an emergence/self-formation test — no precursor-vs-baseline needed at Stage 0); CP10 cage = Γ=−1 boundary short, not bulk well. |
| **phase-space-coordinate-check** | the Q observable is **spectral/time-domain** (Hilbert envelope of ∂_t V, FFT cutoff ω) in real-space — matching the corpus claim (cold-cage ring-down is a time-domain/spectral observable, `_bulk.py:40-44`). NO phase-space φ²/Clifford-torus claim is at issue at Stage 0. Coordinate systems MATCH. |
| **consistency-vs-emergence** | Stage 0 is **CONSISTENCY/foundation, NO chord**. Every check classified below (§ Classification). |
| **ave-canonical-source** | all constants imported from `constants.py`; engine-natural units (c₀=1, V_yield=1) in the dynamical path. ALPHA/Q_TANK/ELECTRON/RHO_BULK NEVER imported into the engine globals (the guard triad asserts this). |
| **vacuum-circuit-analysis (ave-vca-setup-compliance)** | VCA framing above; R01 kernel-arg (the bulk kernel is fed V, its own conjugate C-state — never μ₀|H|); R13 resolution floor (geometric, NOT the 138≈1/α α-echo); R17 mode (the cold-cage Q is a RING-DOWN linewidth, not a time-dilation exponent — no exponent at issue). |

## Step 2 — corpus-grep outcome (ave-prereg)

- **No prior Stage-0 / α-clean-spine result doc** exists (`grep research/`):
  this is the first build of the re-scoped Gate 0.
- **The immune-system primitives already exist + are battle-tested:**
  - guard triad — `graded_vacuum_network.py:111-114` (asserts
    `ALPHA`/`Q_TANK`/`ELECTRON`/`RHO_BULK` NOT in globals at module load).
  - literal scrubber — `charge_quantization.py:104`
    (`_assert_no_alpha_literal_in_code_path`, forbids `'137'`/`'0.00729'` in the
    verdict-determining code path) + the value-echo immunity guard at `:90-94`.
  - landing-zone CI gate — `test_graded_vacuum_network_isolation.py:74`
    (`assert not (117.0 < Q < 157.0)`, "an α-leak would land here").
  - the Q-extractor — `ringdown_Q` (`_bulk.py:466`), α-free by construction
    (reads decay from the COLD dynamics, never Q_TANK / ELECTRON).
  - 8 existing consumers of the guard pattern (fork_b_*, node_scattering,
    vacuum_varactor, charge_quantization, graded_vacuum_network).
- **The contaminated host is confirmed contaminated** (the architecture
  decision): `cosserat_field_3d.py:56` imports `ALPHA`; `:115`
  `kappa_chiral_from_topology(p, q, alpha: float = ALPHA)` (the exact
  default-kwarg leak); `:131` `KAPPA_CHIRAL_ELECTRON = ALPHA * KAPPA_TILDE`;
  `:2425` the geometric golden-torus Q-form (=137 at R·r=¼; the α-echo VALUE
  literal lives at `constants.py:243`). **Stage 0 does NOT import the cosserat
  host into the engine globals.** Its α-free factor `KAPPA_TILDE_ELECTRON=6/5`
  (`:94`) is the only clean piece, and the spine host (`crystal_engine.py`) uses
  its OWN α-free `kappa_tilde=6/5` default — it never imports the cosserat module.

## Step 1.5 — physical picture (5 bullets, no math)

- A saturated A1 dilatation core (a posited deep bulk well, A→1) sits at the
  centre of the lattice; its high-strain shell is a Γ=−1 impedance short
  (Z_core→0): a wave hitting it is totally reflected (a TIR cage).
- A small breathing kick on the wall sets the bound longitudinal mode ringing —
  the cage is an LC resonator, the kick is the initial-condition energy.
- In the **lossless** configuration — the LINEAR regime (A≪1 ⇒ S=1 ⇒ uniform
  c₀, no nonlinear dispersion), seeded as a STANDING-WAVE EIGENMODE of the box,
  with NO absorbing channel (`pml_thickness=0`, energy-conserving reflecting
  boundaries) — the ring-down envelope does NOT decay: the energy stays in the
  standing mode, the cage is a perfect reactive short. Q=∞ — read honestly off
  the flat envelope (`slope≥0 ⇒ τ=∞ ⇒ Q=∞`).
  ⚑ DISTINCTION (load-bearing): a `pml=0` *saturated* (A→1) cage is NOT lossless
  in the time domain — its breathing wavepacket DISPERSES (nonlinear c_eff(V)
  gradient) and reflects off the hard box, dephasing the probe envelope to a
  FINITE Q≈25. That is a finite-grid DEPHASING artifact, NOT dissipation and NOT
  a leak (corpus-named: `test_graded_vacuum_network_isolation.py:16-24`). The
  genuinely-lossless time-domain cage is the LINEAR standing eigenmode.
- In the **radiating** configuration (a finite grid with a PML / open port) the
  breathing mode leaks energy out geometrically; the envelope decays with τ; the
  measured Q is finite (≈30.8) — and decisively NOT 137.
- The α-echo Q=137 can ONLY appear if α is baked into the read. The spine reads
  Q from the cold dynamics with NO α in scope — so 137 cannot appear by
  construction. That absence is the immune-system working.

## Classification (consistency-vs-emergence — Stage 0 is CONSISTENCY, NO chord)

| Check | Class | Rationale |
|---|---|---|
| (a) lossless cage ring-down → **Q=∞** | **Class C consistency** | a lossless reactive resonator with no open port is Hermitian ⇒ no decay ⇒ Q=∞. This is a foundation/consistency property of the engine (the cold cage is a real LC short), NOT an emergence chord. Q is MEASURED off the flat envelope, not asserted. |
| (b) guard triad fires at module load | **Class A identity / foundation** | the assert IS the immune system; firing is a structural property of the module, not a prediction. |
| (c) literal scrubber + landing-zone gate green | **Class A identity / foundation** | source-level + band-level absence of the α-echo; structural, not predictive. |
| (cross-ref) radiating cold cage → finite Q≈30.8 ≠ 137 | **Class C consistency (chord-vs-echo NEGATIVE, already corpus-canonical)** | this is T3.4's pinned honest negative (`test_l3_mass_cage.py:711`): the α-free cold cage does NOT reproduce 137 ⇒ Q=1/α is an instance-baked ECHO. Stage 0 RE-CONFIRMS this on the spine; it does not re-litigate it. |

**No emergence (Class D) claim anywhere in Stage 0.** No chord. The α-clean spine
is the immune-system foundation everything downstream stands on.

## PREREG (target: α-clean spine lock)

- **Corpus state:** OPEN (first build of re-scoped Gate 0); all primitives exist.
- **My prediction:**
  - (a) the cold **lossless** cage (no radiating channel) rings down to
    **Q=∞** HONESTLY via `ringdown_Q` (the envelope-does-not-decay branch:
    `slope≥0 ⇒ τ=∞ ⇒ Q=∞`). NOT 137. Q measured, not closed-form.
  - (b) the guard triad **fires at module load** on every engine spine module
    (import-time assert; ALPHA/Q_TANK/ELECTRON/RHO_BULK absent from globals).
  - (c) the literal scrubber (no `'137'`/`'0.00729'` in the spine code path) +
    the landing-zone gate (no measured Q in the 117–157 α-leak band for the
    lossless case — it is ∞, far above the band) stay **green**.
- **Why:** a lossless reactive cavity is Hermitian (no dissipative port) ⇒ the
  envelope is flat ⇒ `ringdown_Q` returns ∞ by its own honest branch. The
  spine host imports only α-free constants (verified: `crystal_engine.py:48`
  imports only `NU_VAC, R_II`; `master_equation_fdtd.py` imports only numpy), so
  no α-carrier can reach the read.
- **Discriminating outcomes:**
  - **Outcome A (PASS, expected):** lossless Q=∞ honest; radiating cross-ref
    Q≈30.8 (finite, ≠137); guards fire; scrubber + landing-zone green. ⇒
    α-clean spine established, single grid scaffold stands.
  - **Outcome B (HARD-STOP):** ANY α re-leak — a default kwarg
    `kappa_chiral_from_topology(alpha=ALPHA)` reachable in the spine path, a
    `Q_TANK` class default, a `137`/`0.00729` literal anywhere in the spine, OR
    the measured Q lands in 117–157 (the α-leak band) for the lossless case. ⇒
    REPORT the leak; do NOT patch around it (the leak is the signal).
  - **Outcome C (null/bug):** the lossless cage produces a *decaying* envelope
    (finite Q) when no radiating channel is present ⇒ a spurious-loss BUG in the
    spine (not a leak) — report it; the cage is not a clean reactive short.
- **Falsifier (of the "spine is α-clean" framing):** the measured cold Q
  reproduces 137 from a configuration with NO α in scope. That would mean 137 is
  emerging from the α-free mechanics (a CHORD, not the expected echo) — which
  would overturn the corpus-canonical T3.4 negative and must be surfaced to
  Grant, NOT silently absorbed.

## HARD-STOP triggers (the leak IS the signal — report, do NOT patch)

1. A default kwarg like `kappa_chiral_from_topology(alpha=ALPHA)` reachable from
   the spine import graph.
2. A `Q_TANK` class default / attribute on any spine engine.
3. The literal `137` or `0.00729` anywhere in the spine code path (the scrubber
   catches this).
4. The measured lossless Q lands in the 117–157 band (the landing-zone gate
   catches this).
5. The guard triad does NOT fire at module load (ALPHA/Q_TANK/ELECTRON/RHO_BULK
   reachable in an engine global).
