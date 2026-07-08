# Electron-Lock Arc — Consolidated Close (NEGATIVE)

**Date:** 2026-07-08
**Status:** **CLOSED — NEGATIVE.** The hypothesis that the electron is held together
by a *dynamical binding mechanism* is falsified across five independent loci.
**No walk-back** of `charge = Link(∂Ω, F) ∈ ℤ` (static topology) or `mass = A1`
(the dilatation grade, #260) — those stand.
**Nature:** SYNTHESIS. Every result cited here is already landed (PRs #567–#571 and
the earlier engine results). This note introduces **no new result**; it consolidates
a multi-week arc so the trail reads as one finished effort. Git carries the
per-stage history; there are no preservation banners here by design.

---

## The question

Does the electron **lock**? — i.e., is there a *dynamical* mechanism by which the
vacuum substrate actively holds the electron together and confers its persistent
(mass) identity, over and above the static bookkeeping that the (2,3) winding is a
conserved topological charge?

Two candidate order parameters were put on trial:

- **Energy** — is the mass *stored energy* held in a partition (a charged tank)?
- **Winding** — is the mass the *persistence of the (2,3) topological knot*, and is
  that persistence a real, lossless, dynamically-protected lock?

---

## Five loci, all negative

| # | Locus | Test | Verdict | Ref |
|---|-------|------|---------|-----|
| 1 | Energy partition | zero-drive fill / self-sustain (2b-S1) | reactive pump **FILLS-BUT-DECAYS** — a lossless tank beats, it does not bind | PR #570 · `2026-07-07_electron-lock-2bS1_RESULT.md` |
| 2 | Real-space winding | own-wave persistence (S1) → its dynamical work (S3) | **HOLDS but INERT** — S1 conserves the integer, S3 is DISPERSE-FALSIFIED: "even with the winding demonstrably conserved, the coupling does not pin the core" | `2026-06-24_engine-s1-winding-dof_result.md` · `..._s3-cavity-pinning_result.md` |
| 3 | Phase-space winding | carrier-ratio detuning (#417) | **ECHO** — the "(2,3)" tracks the LC carrier frequency ratio continuously; a topological integer cannot slide, a carrier ratio does | `2026-06-24_engine-phase-space-winding_result.md` |
| 4 | Genesis | five self-assembly routes | **all FAILED** — the V-sector "3" never autonomously energizes (reflection-genesis-23, genesis-24, native-cage, S3-pinning, K4-TLM) | genesis trail |
| 5 | Reconnection barrier | confined free-director, zero drive (this arc) | **ECHO** — with genuine confinement the winding still tracks detuning (corr 0.90) and the unwind barrier is **downhill**, not costly | PR #571 · `2026-07-08_electron-lock-barrier_result.md` |

Locus 5 is the decisive one for the winding branch: it gave confinement its fair
shot on a lossless evolver and confinement changed nothing — the free winding
drains exactly like the unconfined control, and forcing it apart *releases* energy
(H 9693 → 8844, barrier height 0.0 vs a fluctuation budget of 540). All energy
drifts ≤ 1.3e-10 (unitary), so no numerical damping faked a hold.

---

## The unified mechanism

Loci 1 and 5 are the same fact seen from two sides. **On a lossless (unitary /
Axiom-3) substrate, nothing holds itself by a reactive mechanism.**

- The saturation kernel `S = √(1 − A²)` is **anhysteretic — zero enclosed loop
  area — so there is no remanence** (no ferrite `B_r` at `H = 0`). A conservative
  reactive coupling therefore *beats* rather than *binds*: energy poured into a
  partition sloshes straight back out (locus 1).
- The winding is carried by the **off-diagonal spatial-hopping operator**, which
  smears it. A reactive confinement is a **diagonal** on-site term; it can shift a
  frequency but it cannot counteract off-diagonal transport, so it installs **no
  barrier** and the knot unwinds downhill (locus 5).

Zero loop area ⇒ no remanence ⇒ no dynamical hold — in *both* the energy sector and
the winding sector. The only thing that persists is the **static topological charge**
(`Link ∈ ℤ`), and it persists as *bookkeeping that does no dynamical work* — which is
exactly why the conserved real-space winding was inert in locus 2.

---

## Scope — what dies, what stands

**Retracted (Rule-12 scope):** the specific hypothesis that the (2,3) winding
*dynamically locks* the electron — that there is a lossless energy barrier or a
reactive binding that holds the particle together. There is not.

**Stands, untouched:**

- **`charge = Link(∂Ω, F) ∈ ℤ`** — the winding is a genuine *static* topological
  charge. This is quantized-by-construction and peer with the Standard Model's
  charge quantization; it never claimed to be a dynamical lock.
- **`mass = A1`** (#260) — the mass is the A1 dilatation grade, a separate degree of
  freedom. It is not held *by* the winding; the two coexist.

The electron, in AVE, is a static topological charge riding a dilatation mass, on a
lossless medium that provides no additional binding. Nothing here needed a
dynamical lock, and the substrate confirms there isn't one.

---

## Meta — where this leaves the chord

The arc set out to find whether the electron's *internal structure* carries an
AVE-distinct chord. Across five independent loci the answer is uniform: **peer with
the Standard Model, not ahead.** A conserved topological charge is peer; an
oscillator is peer; a soliton is peer. This re-confirms the standing FORM/VALUE
finding from the inside — AVE forces the forms and represents the values, and **the
distinctive truth-claim lives entirely in the forward predictions** (the vacuum
birefringence coefficient, the optical-activity sign-flip, the dispersion tell, the
GW echo), not in the electron's internal mechanism.

This is not a comedown. The structural advantages still bank — finiteness by
construction, charge quantized by topology, spin-statistics derived, and a
mass-confinement *mechanism the SM simply lacks*. The immune system did its job:
five candidate internal chords were killed cleanly, on operative code, without
flinching. The effort closes honest, and the weight returns to the forward
predictions where the chord always lived.

---

## Provenance

- **This arc (2026-07):** PR #567 (tick-floor N_min re-scope) · #568 (design-rationale
  note) · #569 (equivalent circuit) · #570 (2b-S1 reactive-pump dead) · #571 (barrier).
- **Earlier engine loci (2026-06):** S1 winding-DOF, S3 cavity-pinning, #417
  phase-space winding, and the genesis self-assembly trail.
- Each cited result file is a frozen snapshot at its own date; this note reconciles
  them but does not alter them.
