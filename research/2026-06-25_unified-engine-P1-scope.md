# Unified-Engine P1 — carrier-unification scope

**Date:** 2026-06-25
**Branch:** `engine/design-doctrine` (worktree `/tmp/doctrine`)
**Class:** CONSISTENCY / ARCHITECTURE — a scope/spec doc, not a result. Mints no number, claims no chord.
**Companion:** [`../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md)
(the design doctrine this scopes the first build-rung of).

---

## §0 — What P1 is, in one paragraph

P1 is the **carrier-unification rung**: take the two K4-family carriers that currently live on *different*
stencils — the chiral $z=3$ srs free-mode (the photon, on the acceptance-suite srs grid) and the diamond
TETRA A1/ω cores (the mass cage + Cosserat winding) — and **re-home them onto ONE chiral $z=3$ srs node
list**, so a single engine carries photon + A1 + ω on the same grid. Then activate the bulk (A1) and Cosserat
(ω) DOFs **dynamically** (flipping the current absence-findings to PRESENT), and prove the unified engine
still reproduces the photon and the L2 in-media physics. P1 is the *medium* rung; it is **gated on Decision-2
only for the electron (P2), not for the medium** (§6).

---

## §1 — P1.1: unify the two carriers onto ONE chiral z=3 srs node list

**The gap.** Today the carriers are split across stencils:
- the **photon / transverse free-mode** runs on the chiral $z=3$ srs vector-TLM grid — the acceptance suite
  (`src/tests/engine_acceptance/`) is GREEN there (T1.1–T1.5 medium-validity, T2.x in-media)
  ([`../manuscript/ave-kb/common/engine-capability-map.md`](../manuscript/ave-kb/common/engine-capability-map.md):48);
- the **A1 mass cage + Cosserat ω** were tested on the **diamond TETRA stencil** (the
  `coupled_cage_winding` / native-K4 reroute campaign).

This split is the engine-capability-map §4 TWO-GRID problem
([`../manuscript/ave-kb/common/engine-capability-map.md`](../manuscript/ave-kb/common/engine-capability-map.md):75)
in its medium form.

**The task.** Re-home the A1 and ω cores from the diamond TETRA stencil onto the chiral $z=3$ srs node list
— ONE node list, ONE connectivity, all carriers. Per the §E connectivity dispatch (Decision-1 RATIFIED
2026-06-25) the production substrate IS the chiral srs net, so the diamond cores are the ones that move.

> ⚠ **Carries the D1 tension forward (flag-don't-fix).** The doctrine §E flags that
> [`../manuscript/common_equations/eq_axiom_1.tex`](../manuscript/common_equations/eq_axiom_1.tex):37
> (the 2026-06-12 D1 adjudication) currently reads diamond=production / srs=instrument-only — the OPPOSITE of
> the 2026-06-25 ratification P1 is built against. P1 re-homing to srs must SHOW the α + Lorentz-suppression
> chains (which the 2026-06-12 text anchored to diamond) survive on srs. That survival is a P1 acceptance
> item (§5), not an assumption. Reconciling the .tex is auditor-lane + Grant, not part of P1's build.

**Anti-rebuild (Rule 14).** Re-home by re-wiring the certified cores onto the srs node list; do NOT write a
new srs stepper inside the unified facade. Reuse `coupled_cage_winding._assemble_H()` (the coupled Hermitian
H), the conservative evolver, and the srs vector-TLM medium the acceptance suite already certifies. The
facade dispatches; it defines no stepper/stencil.

**Native-stencil guard.** The re-homed A1/ω operators must use the substrate-native srs stencil (rank-2 bond
tensor), NOT a Cartesian Laplacian on a parity sublattice (the wpqwmrms0 / RANK-2 bug class — doctrine §H.6).

---

## §2 — P1.2: the continuum-vs-discrete dispatch

Wire the doctrine §D dispatch into the unified engine as an explicit regime switch:
- **continuum PDE core** for linear, long-wavelength ($q\cdot\ell_{node}\ll1$, $A\ll1$): photons, lensing,
  S-params — cheap, $c_0/Z_0$-exact;
- **discrete srs lattice core** at the band edge ($q\cdot\ell_{node}\to1$, the $(q\,\ell_{node})^4$ tell) and
  in the nonlinear/soliton regime ($A\to1$).

The dispatch must be a *regime* switch, not a *resolution* switch: refining $\Delta x$ stays a
numerical-convergence test (doctrine §B), it never crosses into "continuum" by going below $\ell_{node}$.

---

## §3 — P1.3: biquaternion at the coupling layer

Implement the A1↔ω coupling and the saturation wall at the **coupling layer** in the biquaternion language
(doctrine §F): the **chiral A1↔ω port** (handedness intrinsic to the algebra) and the **saturation wall as
the null cone** ($|\Gamma|=1$ = zero-divisor boundary = the $\Gamma=-1$ wall where mass forms). The cores
keep separate-field evolution; the biquaternion appears only at the port and the wall, and is used as
notation — no new substrate primitive, no new number read off it (canonized-to-nothing-as-a-primitive).

---

## §4 — P1.4: flip the bulk (T1.7) and Cosserat (T1.8) absence-findings to PRESENT

The acceptance suite currently records the srs medium as carrying only 2 transverse DOF (the photon), with
the bulk and Cosserat grades ABSENT:
- **T1.7 (bulk)** — `longitudinal_dof_present == False` on the bare srs vector-TLM
  (`src/tests/engine_acceptance/test_l1_multiwave.py`; the absence-finding `⊘`);
- **T1.8 (Cosserat)** — the Cosserat ω grade absent (`src/tests/engine_acceptance/__init__.py`:24-25;
  `carried_dof==2` vs `axiom_dof==6`, A1a finding, `test_l0_axioms.py`:173-174).

P1 **activates these DOFs dynamically** on the unified srs engine, flipping both absence-findings to PRESENT:
- the **longitudinal-A1** grade — the Heaviside-Gibbs-excised PHYSICAL scalar V-sector + the $K=2G$/$\rho$
  bulk constitutive ($c_{bulk}=\sqrt2\,c_0$) + the canonical Master-Equation longitudinal scatter, reusing
  the SAME $S(A)$ kernel. The L3 mass-cage layer already demonstrates this flip on its grid
  (`src/tests/engine_acceptance/test_l3_mass_cage.py`:40-54,229-233: "ADDING the bulk DOF FLIPS the T1.7
  absence-finding from ⊘ to ✅"); P1 brings it onto the unified srs list;
- the **Cosserat-ω** grade — the $(2,3)$ micro-rotation winding host (the S1 winding-DOF result already
  established a host exists, `2026-06-24_engine-s1-winding-dof_result.md`); P1 activates it dynamically on
  the unified srs list.

**Honesty guard (doctrine §H.1):** activating the DOFs is a *medium* activation (the medium is fully
dynamic). It is NOT an electron self-formation — P1 does not seed-and-grow an electron. The two-natured
electron stays ASSEMBLED-not-emergent; bulk self-formation is closed-negative (Stage-2 / S3 / #415 / #59) and
is barred from P1.

---

## §5 — P1.5: reproduce the photon + L2, with acceptance gates per rung

The unified engine must re-pass — on the ONE srs grid, with A1+ω now active — the medium-validity and
in-media physics the split engines passed separately. Acceptance gates, each a live-run unit test:

| Rung | Gate | Anchor (existing test) | Pass condition |
|---|---|---|---|
| photon | $c_0/Z_0$ validate-on-known | T1.1–T1.4 (`test_l1_multiwave.py`, `test_l1_photon.py`) | $c_0$ rel-err $\lesssim10^{-15}$, $Z_0$ rel-err 0 — the CHECK (doctrine §B), HALT on fail |
| photon | lossless chiral rotation ON | T1.5 / A1b | $\mathrm{Im}(\omega)=0$ with rotation active (Axiom 3) |
| L2 | refractive index | T2.1 (`test_l2_em_in_media.py`:57) | $n_{EM}=c_0/c_{EM}=S(A_0)$ via the canonical varactor (note: in-suite this is $S(A_0)$, NOT the orchestration "$1/S$" phrasing — `test_l2_em_in_media.py`:27-33) |
| L2 | SYM achromatic lensing | T2.2 (`test_l2_em_in_media.py`:174) | reflectionless SYM gradient ($Z=Z_0$, $\Gamma=0$), deflection frequency-flat (the gravity bridge) |
| L2 | ASYM Meissner mirror | T2.3 (`test_l2_em_in_media.py`:285) | static-E-only ASYM bias loads ε only → $\Gamma\neq0$ (Op14 vacuum-impedance mirror) |
| L2 | α-invariance | T2.4 (`test_l2_em_in_media.py`:390) | α invariant under SYM scaling via $c_{EM}$ (clm-3zz0f6) |
| bulk | T1.7 flip | `test_l3_mass_cage.py`:229 | `longitudinal_dof_present == True` on the unified srs engine |
| Cosserat | T1.8 flip | (new gate on the unified engine) | Cosserat ω carried dynamically; winding integer conserved |

**Cross-cutting gates (every rung):**
- **energy gate LIVE** — closed-box, NO PML/damping on the verdict path; the GX3/GX5-class negative controls
  must TRIP (doctrine §H.2). Pump-detonation / damping-bought localization is rejected by construction.
- **α-clean** — no baked α (ALPHA/Q_TANK/V_SNAP/κ-chiral) on any verdict-determining path; Q=137 stays
  EMPTY (doctrine §H.4).
- **validate-on-known FIRST** — the $c_0/Z_0$ gate runs before any chord read and HALTs the driver on fail
  (doctrine §H.7).

---

## §6 — Gating: P1 is gated on Decision-2 only for the electron (P2), not for the medium

The base-crack #37 / Decision-2 fork — is the electron a sub-cell node-defect (Reading A, default) or a
sub-$\ell_{node}$-emergent object (Reading B, framework-refactor) — is **GENUINELY OPEN** (doctrine §I.1;
[`_archive/L3_electron_soliton/92_round_11_vi_v10_finer_sampling_structural.md`](_archive/L3_electron_soliton/92_round_11_vi_v10_finer_sampling_structural.md):81,87).

**This does NOT block P1.** P1 is the *medium* rung — unify the carriers, activate the bulk/Cosserat DOFs,
reproduce photon + L2. None of that depends on which reading of the electron is correct: the medium physics
(photon, lensing, Meissner, α-invariance, the bulk/Cosserat wave DOFs) lives at $\ell_{node}$-and-above and
is common to both readings (the 92_round_11 §4.3 "either reading: framework's bulk K4 derivations stand"
point).

**Decision-2 gates P2 (the electron), not P1.** Whether the unified engine then ASSEMBLES an electron — and
at what grid resolution it must be represented (sub-cell node-defect vs sub-$\ell_{node}$) — is the P2
question, and it is gated on the Grant adjudication of Decision-2. P1 builds the medium the electron will sit
in; it does not commit to the electron's substrate-scale ontology.

---

## §7 — Out of scope for P1 (deferred frontier)

- **P3 genesis** (rupture→ω, node-creation, the topology-changing event) — deferred, un-backed (doctrine
  §I.3; capability-map §6).
- **The full two-grid bridge to the standalone continuum-scalar cage grid** — P1 unifies onto srs; any
  residual continuum-scalar-vs-srs bridge beyond the §2 dispatch is a later rung.
- **Electron self-formation** — barred (doctrine §H.1); the electron is assembled.
- **Loop / boost-covariance** — the capability-map §6 open DOFs; not P1.
