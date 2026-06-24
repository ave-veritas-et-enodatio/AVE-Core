# Phase-space coupling-winding test — does the (2,3) charge-winding live as a CONSERVED CLOSED TIME-ORBIT in the inter-grade A1↔ω coupling?

**Status:** **FROZEN PRE-REG.** SHA-pin before the run. All four forks Grant-ruled (2026-06-24).
**Class:** CONSISTENCY (confirms/denies a *canonical home* for the charge-winding; the integer source is adopted-by-geometry, NOT a novel chord). Q=137 EMPTY. mass=A1 (#260) UNTOUCHED.
**Branch base:** `analysis/eigensolve-locus-rescope` (#415 — reuses `coupled_eigensolve` + `coupled_cage_winding`; rebase onto main when #415 merges).

**Why this, why now:** the coupled eigensolve (#415) returned DOES-NOT-EXIST but tested the WRONG LOCUS — three ways: real-space (vs phase-space, `CLAUDE.md:22`), longitudinal-mass-V_snap (vs transverse-charge-V_yield, the Q2 sectoral ruling + `#416`), and **static eigenstate (vs dynamic orbit)**. A (2,3) winding is a closed *time-orbit* `θ(t)=2φ+3ψ`; a fixed-point eigenstate has no orbit and cannot host it. This is the proper gate-d **at the canonical locus**: the phase-space inter-grade coupling, traced dynamically.

## §0 SCOPE-LOCK (the load-bearing distinctions)

- **SEED, never FORM.** We seed the already-placed electron and evolve it. We do NOT form it from a free precursor — that is the separately-falsified self-formation slot (keystone energize-lock, leans-falsified), which stays **BARRED**. Guard: the seed is a fully-formed electron config; no precursor/convergence ICs.
- **CONSERVATIVE, never PUMPED.** The generator `H` is Hermitian ⇒ `step()` (Crank-Nicolson/Cayley, `coupled_cage_winding.py:381`) is UNITARY ⇒ joint energy conserved EXACTLY. **NO external drive.** This is the operational line between this test (winding-existence under lossless evolution) and the barred self-formation (which PUMPED `H` at `dt→0`). A winding that appears only under energy injection is an ARTIFACT, not a charge.
- **α-clean / phase-only.** The observable is a pure `arg()` (dimensionless) routed through the κ̃=6/5 winding host; the α-carrier `V_yield=√α·V_snap` divides out of any dimensionless ratio and CANNOT enter an `arg()`. NO Ω-weighting or A*-weighting (those re-import √α). No ALPHA/Q_TANK on the read.
- **Anti-rebuild (Rule 14):** reuse `coupled_cage_winding.step()` (the conservative evolver), `_build_seeded_sim`/`seed_A1_sech`/`seed_winding` (the electron seed), and #415's eigenvectors (Stage-A). New code = the phase-orbit winding reader + the energy ledger + validate-on-known.

## §1 THE FOUR FORKS (all Grant-ruled 2026-06-24)

- **F1 LOCUS:** the winding lives on the **inter-grade A1↔ω relative phase** (transverse Cosserat / shear grade, A1⊥T2), at the **V_yield** cavity — NOT the A1 breather's own (V_inc,V_ref) phasor (honors the Grant-ratified "never wire the winding into the breather phasor" fence). [Q2 sectoral ruling; `#416`]
- **F2 RATIO:** **geometric — two angles of ONE derived Clifford torus** (`2φ` toroidal + `3ψ` poloidal; the Golden-Torus embedding is a *derived* substrate-mechanism, `ch8-alpha-golden-torus.md` R·r=1/4 from Axiom-4 saturation + Nyquist). A **1:1 resonant tank** with an internal 2:3 quadrature winding. **NOT** the 2:3 inter-tank frequency-lock (held back, emergence-burdened, re-opens a closed q-selection negative — a SEPARATE pre-reg if ever).
- **F3 SOLVE:** **dynamical, seed-then-evolve, two-stage** (cheap static pre-filter → expensive dynamical orbit).
- **F4 CONSERVATION:** **two independent reads must AGREE** (orbit unwrap-count AND a circulation integral) before "conserved" is claimed — do NOT inherit the Q_H=p·q adopt-by-formula (the direct helicity integral returns only ~18% of p·q; carry that as a known caveat, not a free PASS).

## §2 THE OBSERVABLE (precise)

- **Inter-grade relative phase:** `φ_rel(t) = arg( Σ_x a_A1(x,t)·conj(b_ω(x,t)) )` — the A1↔ω cross-term phase, which lives in NEITHER tank's self-phasor (honoring F1). `a_A1 = x[:nd]`, `b_ω = x[nd:]` (the complex state present every step).
- **The two Clifford-torus angles:** toroidal `φ` (major/d-axis, counts the "2") and poloidal `ψ` (minor/q-axis, counts the "3"); the winding curve is `θ(t)=2φ(t)+3ψ(t)` (`torus-knot-uniqueness.md:31-35`). The winding integer pair `(p,q)` = windings of the time-traced phasor point around (toroidal, poloidal) over a CLOSED orbit — a Lissajous/quadrature winding, NOT a real-space linking and NOT a cells-per-turn sweep.
- **PHASE-ONLY (α-free):** the read is an argument (dimensionless). The exported conserved scalar is the integer pair; the enclosed AREA and any Ω/A*-weighting are FORBIDDEN on the verdict path (they re-import √α).

## §3 THE EVOLUTION (ports + energy ledger — Grant's directive)

- **Seed (the electron):** `_build_seeded_sim(winding_on=True)` → `seed_A1_sech` (the A1 mass) + `seed_winding` (the transverse (2,3) template) at the **V_yield** transverse-cavity operating point (NOT the V_snap mass core — that was the eigensolve's threshold error).
- **Ports (3, one gate):** (a) A1 **bulk** port (longitudinal mass breather); (b) ω **transverse Cosserat** port (the charge sector); (c) the **coupling port** `Ω = rate·g_front(A)·S(A)` (the S(A)-front-gated A1↔ω inter-grade exchange).
- **Evolver:** `step()` — Crank-Nicolson/Cayley, Hermitian `H` ⇒ unitary ⇒ **energy exact**. NO drive.
- **The energy ledger (track every step):** (1) joint `‖a_A1‖²+‖a_ω‖²` conserved exactly (the S2/S3 energy gate — must hold to ~machine precision; a drift = bug, test void via the backward-Euler-bleed gate); (2) the **sector-exchange** book — energy flowing A1↔ω through the coupling port as the orbit winds. **PASS signature:** energy sloshes conservatively between mass & charge sectors WHILE the (2,3) integer stays put — a topological invariant on a conservative orbit. If the integer moves with the energy, it is NOT topological.

## §4 MAKE-OR-BREAK (pre-stated)

- **PASS:** a closed CONSERVATIVE time-orbit of `φ_rel` (and its two Clifford angles) carries winding **(2,3)** [or `(p,q)` gcd=1, both≥2, minimal ⇒ (2,3)]; the integer is **stable** across the resonant window, **α/m_e-free** (phase-only), the **two reads AGREE** (F4), AND the energy ledger shows **conservative sector-exchange (no pumping)**. ⇒ the charge-winding has the canonical phase-space home the real-space eigensolve missed.
- **BREAK:** `φ_rel` is a single STATIC angle (no orbit / no enclosed winding), OR no commensurate (2,3) appears / a different integer / the integer is α-loaded / it requires energy injection to appear. ⇒ the winding does NOT live in the conservative coupling either; the negative DEEPENS (real-space AND phase-space both null). Per Rule 12 this RETRACTS to "phase-space coupling locus tested NEGATIVE" — it does NOT walk back charge=Link(∂Ω,F) (independently grounded).
- **INCONCLUSIVE (Rule 11):** the inter-grade coordinate is gauge-degenerate (e.g. `b_ω` phase collapses), OR the orbit is unresolved at the available steps-per-period (Nyquist). Report; re-scope — do NOT rescue.

## §5 TWO-STAGE BUILD (F3)

1. **Stage A — cheap static pre-filter (on #415's existing eigenvectors, no solve):** is `φ_rel` a NON-DEGENERATE, definable coordinate on the eigenstates, or is it gauge-collapsed (`V_ref` a read-only projection)? A stationary eigenstate gives only a static angle — Stage A can PROVE the BREAK form "a fixed point hosts no winding" and can KILL the coordinate (→ INCONCLUSIVE-coordinate-wrong, STOP, do not burn the solve). It CANNOT deliver PASS.
2. **Stage B — the dynamical solve:** seed → `step()`-evolve conservatively over ≥ several orbital periods → trace `φ_rel` + the two Clifford angles → read (p,q) by TWO independent methods (unwrap-count AND circulation integral, F4) → with the full energy ledger (§3). Nyquist: ≥ ~10 steps/period; verify resolved or report INCONCLUSIVE.

## §6 VALIDATE-ON-KNOWN

- **Positive control:** inject a SYNTHETIC known phase-space orbit (`a_A1·conj b_ω` phase = a pure `2φ+3ψ` Lissajous) and confirm the reader returns (2,3) and the two methods agree. If it can't read a planted (2,3), the reader is broken — HALT.
- **Null control:** a non-winding orbit (static or `(0,0)`/`(1,1)` Lissajous) must read NOT-(2,3) (no false-positive winding).
- **Energy-gate control:** confirm `step()` conserves joint energy to ~machine precision on the seed (reuse the S2/S3 certification); confirm a deliberately-pumped variant TRIPS the bleed gate (proves the conservative guard is live, not vacuous).

## §7 TRAPS + GUARDS

(i) **Self-formation refill** — seed-not-form; the barred slot stays barred (no precursor ICs, eigen/seed config only). (ii) **Pumped-winding artifact** — conservative-only; the energy gate must hold; the deliberately-pumped negative control must trip. (iii) **α re-import** — phase-only read; NO Ω/A* weighting; κ̃=6/5 host; Q=137 empty. (iv) **Locus-lens** — this is the phase-space INTER-GRADE coordinate at V_yield; do NOT regress to the real-space torus / static eigenstate / V_snap core (the three errors #415 made). (v) **Coincidence-magnet** — if a suggestive integer (½, ¾, √α-ish) appears, report, do NOT headline as a chord. (vi) **Two-reads-agree** — do NOT adopt Q_H=p·q by formula (F4).

## §8 BUILDABILITY

**NEEDS-NEW-SOLVE** (Stage B) + REUSE. Reuse: `step()` (`coupled_cage_winding.py:381`, conservative evolver), `_build_seeded_sim`/`seed_*` (the seed), #415 eigenvectors (Stage A), the S2/S3 energy gate. New: the `φ_rel` phase-orbit winding reader (two methods), the sector-exchange ledger, the validate-on-known harness. No new engine. Mark the dynamical solve `engine_sim` (it's a research-tier time-evolution — keep it off the PR-blocking gate per the #414 partition).

## §9 CONSISTENCY-vs-EMERGENCE

CONSISTENCY-class. PASS confirms a canonical HOME for the charge-winding (the integer is adopted-by-geometry from the derived Clifford torus); it is NOT a novel α-free chord (that's the bench) and NOT an emergence result. A clean BREAK is a legitimate deeper negative (charge has no phase-space coupling home either). Either outcome retires the real-space-locus ambiguity #415 opened.
