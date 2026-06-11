# Genesis v9 — Phase-1 Pre-Registration (DRAFT — NOT FROZEN)

> **STATUS: DRAFT. Returned by the implementer lane for Grant to freeze.**
> This is NOT a frozen pre-registration. It is gated on TWO things, both of which
> precede any freeze:
> 1. **The §0 adjudication** (design doc `2026-06-11_genesis-v9-chiral-lattice_design.md`):
>    v9 re-opens the 2026-06-07 lattice-net resolution-of-record, which settled
>    z=4 achiral diamond as the computed substrate and ordered "Do NOT rebuild on
>    z=3 srs (would invalidate the α + Lorentz chains)." Grant must pick framing
>    **(A) deliberate challenge** or **(B) decoration-model** before freeze.
> 2. **Grant's freeze** of the predictions + thresholds below.
>
> Per Rule 16 (ask BEFORE design), this draft is surfaced now, pre-freeze, not
> after 30 commits. Per substitution-not-retraction (Rule 12), if any prediction
> falsifies, it retracts via 🔴 header; the slot is not refilled in place.

## Phase-0 result that arms this (committed, this branch)
- **Smoke A (consistency gate): PASS.** Trivalent scatter `S_ij = ⅔ − δ_ij` (derived from Op5, n=3)
  unitary to `8.3e-17`; n=4 reduces exactly to canon `½ − δ_ij`; closed-system energy drift `2.2e-14`;
  scalar dispersion isotropy ratio `1.000`. The lattice change did not break the achiral physics.
- **Smoke A (REAL-DYNAMICS extension): PASS.** Standing-wave scalar dispersion `ω(k)` measured by
  scatter+connect time-stepping reproduces the canonical **3D link-line TLM network-velocity invariant
  `c₀/c_link = 1/√3 ≈ 0.5774`** on the chiral srs net (`0.5764`, 0.17% from analytic) AND the cubic
  diamond reference (`0.5774`, 3e-12 from analytic), **identically between enantiomorphs**
  (`|f_R − f_L| = 0`), linear at small k. The CONNECT map is a verified permutation (⇒ the step is unitary
  ⇒ exact energy conservation, analytic backbone). The achiral observable is chirality-invariant — the
  load-bearing "did-not-break-it" gate, now as live dynamics vs the cubic engine vs analytic `c₀`.
  *(driver `chiral_lattice_smoke_dynamics.py`; gates `test_chiral_lattice_dynamics.py`; consistency-class,
  not emergence.)*
- **Smoke B (optical-activity source): PASS.** srs-right ring-writhe `−4.0867e-02`, srs-left `+4.0867e-02`
  (exact sign-flip), diamond control `0.0`; box-independent. The chiral geometry carries signed helicity
  into its shortest circuits — the necessary-condition source of optical activity — natively, with **no**
  injected `κ_chiral = α·pq/(p+q)`.
- **Smoke B (REAL-DYNAMICS transverse channel): ROTATES-ENANTIOMORPH-ODD, with a load-bearing limitation.**
  A transverse polarization frame Bishop-transported along the **exact 4₁ screw orbit** carries a nonzero
  rotation that is **exactly MIRROR-ODD** (`Δθ/L = +75.5°/unit` on srs-R, `−75.5°/unit` on its mirror;
  signed torsion `+0.52 → −0.52` rad). **Two honest limitations refine design §3 and feed P1/P2:**
  (i) the per-length transport **RATE does not cleanly converge at Phase-0** — the discrete 4-gon-per-turn
  orbit gives ~9% end/discreteness wobble; a converged dynamical rate requires the **full vector-TLM
  (Phase-1)**, so the Phase-1 deliverable is now evidence-based, not just asserted; (ii) **a single
  independently-found screw axis is handedness-ambiguous** (srs-R `4₁` and srs-L `4₃` orbit-helices share
  sign, because each enantiomorph space group contains screw axes of both senses) — the clean SIGNED
  discriminator is the **reflection-odd writhe / the mirror operation**, an A46 phase-space-coordinate
  lesson that the Phase-1 controls must respect (the enantiomorph-PAIR difference, not a single ray).

## Phase-1 hypothesis (the genesis question — OUT OF SCOPE for Phase-0)
**H1:** A stable, topologically-charged breathing soliton (the electron ansatz, `(2,3)`) nucleates and
persists on the **bare chiral srs net** under the full **vector-TLM + Op14 saturation** dynamics, **with
its chirality (optical rotation, spin handedness) inherited from the lattice geometry rather than from the
injected one-parameter `κ_chiral`** (`cosserat_field_3d.py:115,131,522-523`).

**H2 (the discriminating claim):** The dynamical optical rotation `Δθ_pol / L` of a transverse packet on
the srs net is **signed per enantiomorph and zero on the diamond control**, and its sign matches the
sign of the Phase-0 circuit writhe.

## Pre-registered predictions (EXECUTABLE gates — to be frozen by Grant)
Each is an executable test with a stated threshold. Thresholds in ⟨angle brackets⟩ are placeholders for
Grant to set/confirm at freeze.

- **P1 — vector-TLM consistency.** The transverse 2-component vector-TLM on the srs net conserves energy
  (closed) to ⟨1e-8⟩ and reproduces Smoke A's isotropy on its achiral observables. *Falsifier:* drift or
  anisotropy beyond threshold ⇒ the vector scatter/connect is broken; fix-or-close before H2.
- **P2 — dynamical optical rotation, signed.** `Δθ_pol/L` measured on a launched transverse packet is
  nonzero on srs, **opposite-sign** on the two enantiomorphs (`|sum| ≤ ⟨10%⟩` of magnitude), and **≤
  ⟨5%⟩** of the srs magnitude on the diamond control. *Falsifier:* control comparable to chiral, or no
  enantiomorph flip ⇒ H2 falsified.
- **P3 — sign concordance.** `sign(Δθ_pol/L)` on srs-right matches `sign(writhe_R)` from Phase-0 (and
  flips together under enantiomorph swap). *Falsifier:* sign mismatch ⇒ the writhe is not the optical-
  activity source (the Phase-0 necessary-condition reading was wrong) ⇒ flag, do not rescue.
- **P4 — native chirality, no injected α.** The measured optical rotation magnitude is reproduced with
  `κ_chiral = 0` (geometry-only). *Falsifier:* rotation collapses to ~0 when `κ_chiral → 0` ⇒ the
  handedness is still injected, not structural ⇒ v9's central hypothesis fails; close the branch.
- **P5 — soliton stability (persistence check — consistency-class, NOT the genesis claim).** A seeded
  `(2,3)` ansatz on the srs net is a stable closed-system eigenmode (topological charge conserved,
  energy bounded) over ⟨N⟩ steps at ⟨N_grid⟩. *Falsifier:* decays / unbinds ⇒ the srs substrate does
  not support the electron soliton ⇒ a structural hit against substrate-migration framing (A).
  *Checkpoint-8 caveat (synthesis-lane amendment, KEEP-BOTH — P5 preserved unchanged in substance,
  P6 added alongside):* planting the finished composite and testing persistence is the pattern
  substrate-native-check Checkpoint 8 warns against; P5 alone can show **hosting**, never **genesis**.
- **P6 — genesis-by-precursor (Checkpoint-8 PRIMARY emergence test — the genesis claim).** Seed the
  **generative precursor, not the end-state**: launch a transverse (photon-class) packet — the simplest
  autonomous action the lattice supports — along a screw axis with **Op14 saturation ON** (`A → 1`
  accessible), closed-system, on srs-right, srs-left, AND the diamond control, plus the `κ_chiral = 0`
  ablation. Let the dynamics build (or fail to build) the bound state. **Outcome bins (frozen by Grant
  BEFORE any run):**
  - **BIN-G (genesis):** the packet self-traps — energy-localization length saturates to a finite
    plateau over ⟨N⟩ steps (not monotone spreading), a nonzero conserved topological charge emerges in
    the trapped region, and the trapped state is **enantiomorph-signed** (chirality inherited from the
    lattice, surviving the `κ_chiral = 0` ablation).
  - **BIN-T (transient):** localization forms then decays — record lifetime vs launch amplitude;
    hosting-adjacent, NOT genesis.
  - **BIN-D (dispersal):** linear-like spreading at every sub-rupture amplitude ⟨bins⟩ — the srs net
    does not self-trap the photon precursor ⇒ structural hit against framing (A).
  *Signed channel per the Phase-0 lesson:* the enantiomorph-PAIR difference (and the mirror operation),
  never a single screw-axis ray. *Relation to P5:* P5-pass + P6-BIN-D = hosting-but-no-genesis — that
  combination MUST NOT be reported as a genesis pass.

## Controls (frozen with the predictions)
- **Enantiomorph pair (srs-right / srs-left)** — the primary discriminator. Any achiral artifact
  (transport mis-scaling, numerical bias) is common-mode and cancels in the native−mirror difference.
- **Diamond achiral control** — the zero-rotation reference. A genuine null here (a pseudoscalar from a
  centrosymmetric net) vs the chiral signal is the second discriminator.
- **`κ_chiral = 0` ablation** — isolates structural vs injected chirality (P4).

## Op14 / empirical-driver discipline carried into Phase-1
- **Local-clock modulation re-enters scope** (Op14 ON, `A → 1`): report eigvec localization vs
  `A²_local` at load-bearing sites; compute `ω_local(r) = ω_global·√(1 − A²(r))`; do not eigsolve at a
  single global σ.
- **PML cell exclusion** on every density extraction (`pml_thickness ≤ idx ≤ N − pml_thickness − 1`),
  density-peak (top-K `|field|²`) sampling, reactance-pair (V_inc/ω AND Φ_link/ω̇) recording.
- **Phase-space coordinate discipline (A46):** optical rotation measured in the polarization-plane /
  chirality coordinate, never real-space lattice-Cartesian vs φ².

## Honest-closure / kill conditions (Rule 11)
- P4 fail (rotation needs injected `κ_chiral`) **or** P3 fail (sign mismatch) ⇒ the lattice-chirality
  hypothesis is falsified; record the mechanism, retract via Rule 12, close the branch. Do not debug
  toward a rescue.
- A single mechanism explaining multiple failures is the discipline working; name it, don't drop the
  adjudication criteria post-hoc.

## What Grant decides at freeze
1. §0 framing: **(A)** challenge the resolution-of-record (and accept the α/Lorentz-chain-invalidation
   warning as the explicit cost), or **(B)** treat the srs net as a decoration-model diagnostic (substrate
   stays diamond).
2. The thresholds in ⟨…⟩.
3. `N_grid`, `N_steps`, the P6 outcome-bin boundaries (the frozen bins), and whether P5/P6 (genesis)
   run in Phase-1 or split to a Phase-2.
