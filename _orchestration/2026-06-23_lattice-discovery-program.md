# EPIC — Lattice Dynamic-Regime Discovery Program (substrate-native)

**Created:** 2026-06-23 · **Role:** orchestrator-tracked epic (living doc) · **Status:** ACTIVE — lanes mid-flight, all PRs HELD pending substrate-native cleanup
**Origin:** the lattice-characterization white-space survey (`w2jugq7ch`). **Reframed 2026-06-23** after Grant flagged standard-physics-vocab contamination (see §0.5).

---

## 0. North star

Characterize the **driven / many-body / finite-frequency** regime of the chiral micropolar K4 LC lattice and convert it into **bankable, falsifiable forward predictions** (the discovery half of the testing pivot, [[project_state_of_ave_and_testing_pivot]]). The governing law (S(A)=√(1−(A/A_c)²), zero free parameters) is settled; the unbuilt artifacts are driver codes that exercise it. **The AVE-distinct chord lives in the DRIVEN/SATURATED regime, not the cold-linear one** (confirmed by the re-grounding: the lattice's handedness only acts at saturation).

---

## 0.5 THE SUBSTRATE-FIRST DISCIPLINE — mandatory, read before any lane work

Every lane brief, prereg, and deliverable **leads with a sector-declaration BEFORE any standard-physics word**:
1. **WHICH SECTOR** — A1 dilatation/compression, shear, or Cosserat micro-rotation (2,q) — and **does the engine/operator actually CARRY that DOF?**
2. **STRAIN / SATURATION / IMPEDANCE state** — is the claim about the **cold linear** operator or the **driven / near-yield saturated** regime?

**The vacuum's native language is EE/circuit:** the LC mesh, impedance, Γ, the phasor/Lissajous loop on the Clifford torus. Standard-physics names (scattering length, Chern number, Hopf fibration, stress-tensor flux, phonon bands, group velocity) are **subordinate translations only.**

**The common trap (the category-error generator):** riding a standard-physics noun onto a sector the lattice doesn't have, then reading the observable off the wrong sector. It already produced three failures this epic — the D-gate p=2 spinor inversion, the Lane-A stress-tensor (no shear momentum in the compression sector), the Lane-B Chern-on-cold-matrix (handedness is saturation-only). Reasoning from the mesh OUT kills these a priori. See [[feedback_substrate_native_first_sector_header]].

---

## 1. Circuit-native object glossary (so no lane re-imports vortex/scattering vocab)

Per Vol 4 Ch1 (`resonant-lc-solitons.md`, `cvr-phasor-reactance.md`) + Vol 9, verbatim-grounded:

- **The electron = a Resonant LC Tank** (`BoundResonator`). Real-space body = the **0₁ UNKNOT** — a localized standing reactive mode. **NOT a vortex/whirlpool** ("vortex ring" is research-only, not canon).
- **Mass = total stored REACTIVE energy** — the C↔L breather cycling capacitive (E, ∝V²) ↔ inductive (B, ∝I²) 90° out of phase; virial ⟨E_C⟩=⟨E_L⟩=½m_e c² ⇒ **E=mc² IS the stored electrical energy of an LC tank.** A1 dilatation sector → Z_bulk channel.
- **Confinement = the Γ=−1 perfect-short wall** — core dielectric saturation drives C_eff→∞ ⇒ Z_core→0 ⇒ Γ=(0−Z₀)/(0+Z₀)=−1. The particle weaves its own impedance mirror. **Pauli** = two Γ=−1 bubbles can't penetrate.
- **The (2,3) "knot" = a phase-space winding portrait** on the Clifford torus (2 on the d-axis, 3 on the q-axis) — **NOT real-space laps.** It is the **CHARGE / shear sector** (Z_shear, Cosserat micro-rotation), **orthogonal to the mass-phasor (A1⊥T2), never wired into it** (the ontology fence, `master-equation.md:20`).
- **Charge = the (2,3) winding = Beltrami helicity** (the through-linking in Z_shear).
- **Spin = the Γ_spinor=−1 (2π→4π) wall** (T2 sector) — a **distinct** −1 from the mass-confinement −1, numerically coincident.
- **Q_e = 1/α = 137** is the electron's **instance** value. The α-free cold-cage Q≈30.8≠137 is the corpus **clean negative** — α stays an echo, NOT forced by the tank.
- **3-channel network:** Z_EM≡Z₀ (matched/radiative PORT, the per-cycle α leak, |Γ_EM|²=1−α) · Z_bulk (mass/A1, Γ→−1) · Z_shear (charge/T2 winding, Γ→−1).

---

## 2. Lanes (corrected scopes + status)

### Lane A — two-body interaction, charge sector (Z_shear) — P0 lead
- **Path-(a)** (mass-sector, scalar A1 compression engine): **WALL-engine NULL.** The compression sector has no shear-momentum channel, so a "force on a blob" is structurally impossible — the only measurable two-body signal is phase-dependent **strain-overlap** (generic-soliton, not gravity). The stress-tensor T₀ₓ recheck is **substrate-CLOSED** (no shear momentum to flux; and AVE-gravity is *diffraction* off a c_eff(A²) gradient, not a stress-tensor pull, `optical-refraction-gravity.md:17`) — NOT an open choice. PR **#390** → demote to honest WALL-engine negative.
- **Path-(b)** (charge-sector, Cosserat (2,3) winding engine): **REPORTED → PR #391 (AUDIT-PENDING).** DOF **IS** carried (charge=Beltrami helicity; NOT a path-a capability wall). Validate-on-known **PASS at the law level** (`universal_pairwise_energy` clm-gdd70j: far-field exponent −2.000 exact Coulomb + Regime-III repulsive wall). **Chord candidate #1 DERIVED (zero-parameter):** short-range force softens −2.0→−0.47, +16.6% departure from 1/r at r=1.05·d_sat decaying as (d_sat/r)² (Op14 saturation kernel) = MANIFESTATION. Candidates #2 (handedness magnitude) + #3 ((q·ℓ_node)) **gated** on the unbuilt cage⊗winding two-grid engine. **Field-route closed-NEGATIVE:** the un-caged engine carries the winding but not the A1 cage → free windings disperse → like-charge arm == achiral null (prereg HALT fired; `engine-capability-map.md:19` no engine carries >1–2 DOF). **AUDIT OWED** (refute-by-default read-AND-run) — and the writeup needs the substrate-native cleanup pass before merge.

### Lane B — full two-sublattice Cosserat band structure (cold LC-mesh spectrum) — P1
- Prior PR **#389** validated on the **single-node 6×6** + a phenomenological tile-and-scale ansatz coupling (`C=sf_mag·D6`) — so its "full two-sublattice band structure" headline **overstated**. **RE-RUNNING** with the real substrate-native A→B tetrahedral-bond operator.
- Headline **NULL is correct + expected**: the 4₁-screw handedness is **saturation-only** (`cosserat_field_3d.py:570`), so the cold linear bands are parity-symmetric by construction — no topology chord in the cold spectrum. **The chord is the driven/saturated regime** (converges with Lane N). The √2 = a node-twist **stiffness convention** question (flag-don't-fix). Spectrum substrate-native: LC stop-band; the gapped micro-rotation mode IS mass.

### Lane D — why the BoundResonator phase-portrait winds (2,3) — P2
- The **spinor/Hopf route COLLAPSED-TO-FIT** (PR **#388** → demote): it read its cited table BACKWARDS (the 4π cover rides **q=3**, not p; p=major not minor; on a `status:ambiguous` axis). The (2,3) is a **phase-space** winding, and the corpus already factors it as an **instance** field — corroborating the fit. C-α (gcd=1)/C-β (≥2)/odd-q-given-p=2 stand; **C-γ (p=2) is not forced.**
- **NEW substrate-native p=2 route (Grant 2026-06-23 — the live derivation):** the **saturated core drives B force-free (Beltrami)** ⇒ a twist whose minimal closed winding is set by **(a) Nyquist** (≥2 samples/cycle on the discrete mesh — p=1 aliases, can't close a phase loop) and **(b) the monopole double-wind** (need 2 laps to enclose a unit net charge), kept **provably SEPARATE** from the q=3 spin 4π closure. If all three hold + survive Rule-11 → a screw-free **substrate-forced p=2 = a chord.** Derive refute-by-default. *(Caveat: Nyquist-for-m_e is closed-negative `2026-06-11_nyquist-binding-route_CLOSED`; this is Nyquist-for-the-winding-number — different.)*

### Gated / downstream
- **D-full** enumeration — on the p=2 derivation. **Lane T** transport — on path-(b). **Lane N** nonlinear — the chord likely lives here (the driven/saturated chiral regime; converges with Lane B). Lane N's only fresh artifact is the χ³ SI-coefficient (don't re-run walked-back SHG).

---

## 3. Per-lane status tracker (living)

| Lane | Pri | Status | PR | Next |
|---|:---:|---|:---:|---|
| **A path-a** mass-sector | P0 | WALL-engine NULL | #390 | demote to honest-negative (substrate-native cleanup) |
| **A path-b** charge-sector | P0 | REPORTED (audit-pending) | #391 | validate PASS (−2.000); chord #1 (d_sat/r)² DERIVED; #2/#3 gated on cage⊗winding engine; field-route closed-neg (no cage) |
| **B** two-sublattice bands | P1 | RE-RUNNING (real bond operator) | (#389 superseded) | validate-on-known on the real matrix; cold-NULL expected |
| **D** spinor route | P2 | COLLAPSED-TO-FIT | #388 | demote to negative |
| **D** Nyquist/Beltrami/monopole p=2 | P2 | CHARTERED (live route) | — | derive refute-by-default; Rule-11 |
| D-full / T / N | — | GATED / deferred | — | on p=2 deriv / path-b / driven-regime |

---

## 4. Cleanup status (all discovery PRs HELD until done)

The lane docs (#388/#389/#390) + this epic doc were written in standard-physics vocab and carry the contamination. **Nothing merges until each is re-framed substrate-native.** This epic doc is the root and is being cleaned now (2026-06-23). The lane docs get cleanup passes (sector-header first, vortex/scattering/Chern framing removed) before merge.

---

## 5. Discipline (per lane)

1. **Substrate-first sector-header** (§0.5) — mandatory, before any standard-physics word.
2. **Validate-on-known FIRST** (recover the known result before any new number is a prediction).
3. **Refute-by-default orchestrator audit** (read-AND-run, not the self-report) before any landing.
4. **CONSISTENCY vs CHORD** labelling on every result; **symmetric-standard** both ways; **convergence is a tell** (the cleaner the convergent story, the harder I check it).

---

## 6. Standing constraints

`main` PROTECTED, NO self-merge (Grant merges reviewed PRs). Self-isolate in a `/tmp` worktree off `origin/main`; **never** put `build` in a worktree/branch name. PURE-AVE-CORPUS; `ave-canonical-source`; verify-before-cite + grep-completeness; audit-trail-in-git (no editing `_archive`/`*_FROZEN`/result docs). Drivers → `src/scripts/vol_<N>_*/`; preregs/results → `research/`; canonical results KB-leaf-first then manuscript.

---

## 7. Reference

- Survey: `w2jugq7ch`. Re-grounding: `w45xlj19e`. Audits: D-gate `a196…` (collapse), B `a28c…` (single-node flag), substrate-native re-grounding (all 3 lanes).
- Circuit canon: `vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`, `cvr-phasor-reactance.md`, `cvr-reflection-smith.md`; `vol9/ch3-pin-port-configuration/`. Real-space-vs-phase-space: CLAUDE.md:22, vocab-register def-kn0t01/def-3638f2.
- Lane code: A `master_equation_fdtd.py` (path-a) + the Cosserat charge engine (path-b); B `cosserat_field_3d.py` + the two-sublattice driver; D the Nyquist/Beltrami/monopole derivation.
