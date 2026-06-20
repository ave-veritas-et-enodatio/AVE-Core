# Node-Scattering Multiplicity / Containment Gate — RESULT (scope b only)

**Date:** 2026-06-20
**Prereg:** `research/2026-06-20_node-scattering-containment-gate_prereg.md`
(frozen commit `f87914fa`, the FIRST commit of this branch — predictions
pre-committed before any operator was built).
**Module:** `src/ave/solvers/node_scattering_multiplicity.py`
**Tests:** `src/tests/test_node_scattering_multiplicity.py` (13 pass).
**Scope:** (b) ONLY — the multiplicity/sector test (Fork A). Forks B/C/D DEFERRED.

---

## HEADLINE (one line)

**Stage 1 bedrock PASSED (PROCEED, no HALT); Stage 2 Fork-A test returned a clean,
pre-registered REFUTE (outcome R3).** The lattice's node valence DOES set two
structurally-distinct differential multiplicities (2 for srs, 3 for diamond), but
the electron's **longitudinal A1 dilatation scalar is a COMMON-MODE (+1) object,
NOT a differential (−1) object** — so the pre-committed prediction (longitudinal
confinement needs the diamond's 3rd *differential* mode) is **refuted at the
sector level**. Containment of the A1 MASS-"3" routes through the **common mode =
Grant's bulk-saturation channel (Fork B)**, which is the correct next arm and is
DEFERRED per scope.

A REFUTE here is the gate working as designed — it told us the truth before any
core/boundary physics was built on a wrong sector assignment.

## (skeleton — sections filled incrementally per commit)

## 1. Stage 1 — BEDROCK validate-on-known (PASS / PROCEED)

The operator was assembled from the lattice's OWN bond-graph CONNECT map
(`scatter_matrix(n)` + `connect_index()` on `build_srs_net` / `build_diamond_net`),
NOT the dense `TETRA_OFFSETS` cube. This is the first solver call-site on
`build_srs_net` (it had zero before). All anchors PASS:

| Anchor (prereg §) | Result | Pass |
|---|---|---|
| §2a S3 bare spectrum | `{+1×1, −1×2}`, diff mult **2**, S²=I, common mode = port-sum | ✅ |
| §2a S4 bare spectrum | `{+1×1, −1×3}`, diff mult **3**, S²=I, common mode = port-sum | ✅ |
| §2b photon anchor | srs diff mult `2` == photon 2 transverse DOF (`test_l1_photon.py:243-268`) | ✅ |
| §2c winding anchor | seeded `(2,3)` → `Q_link=3`, `w_tor=2`; null → `0` | ✅ |
| §2d α-free invariance | α→2α: spectra bit-identical, `Q_link 3→3`, `dQ/Q = 0` | ✅ |
| H1 distinctness | srs deg-3 (64 nodes, **192 DOF**) vs diamond deg-4 (16 nodes, **64 DOF**); **no collapse** | ✅ |
| global operator sanity | both `𝓢` orthogonal, all eigs on the unit circle | ✅ |

**HALT conditions (prereg §5) all clear:** H1 (collapse) NO — operators distinct;
H2 (wrong spectrum) NO — exact `{+1,−1×(n−1)}`; H3 (~137/~3 artifact) NO — the
only "3"s present are the *legitimate* diamond differential multiplicity (n−1=3)
and the winding integer Q=3, neither a bin-1 artifact; H4 (winding broken) NO —
`(2,3)→3`, null→0; H5 (α-leak) NO — `dQ/Q=0`.

The α-invariance is **structural**: the operator modules import no `ALPHA`
(import-guarded). This is the load-bearing, frame-independent anchor that survives
the eigen-vs-driven mismatch that sank the prior prereg's GATE1 (see the Rule-12
retraction in `research/2026-06-19_electron-Q-coupled-network_prereg.md:40`).

## 2. Stage 2 — the SHOWN port→grade map + the Fork-A verdict (REFUTE-R3)

**The SHOWN map (`port_to_realspace_embedding`, phase-space-coordinate-check
deliverable).** The map from n-PORT space to real-space grade is the
bond-direction embedding `B_u` (rows = `bond_unit[u][p]`,
`chiral_lattice.py:114`). Measured over interior nodes:

| Quantity | srs (deg 3) | diamond (deg 4) | reading |
|---|---|---|---|
| bond-direction sum (per node) | `0.0` | `0.0` | both nets force-balanced |
| common-mode (+1) **scalar** content | `1.732 = √3` | `2.0 = √4` | +1 carries the dilatation SCALAR |
| common-mode (+1) **real-space vector** | `~1e-17` | `0.0` | +1 has NO vector grade |
| differential (−1) **scalar** content | `~3e-16` | `~1e-16` | −1 carries NO scalar |
| differential (−1) **real-space vector** | `1.225` | `1.155` | −1 carries the VECTOR/shear grade |

**The verdict: REFUTE-R3.** The longitudinal A1 dilatation **scalar** is the
**common mode (+1)** — orthogonal to the entire differential (−1) sector (which
carries zero scalar). So the pre-committed prediction (a normalizable confined
longitudinal mode lives in the differential sector and needs the diamond's 3rd
differential mode) is **refuted at the sector level**: the longitudinal scalar is
not a differential object at all. The 2-vs-3 differential-multiplicity distinction
is REAL, but it governs the *transverse/shear* (vector) grade — srs's 2
differential modes are exactly the 2 transverse photon DOF; the diamond's 3rd
differential mode is a *spare shear channel*, not a longitudinal-scalar channel.
The longitudinal containment question is therefore **moot** in the differential
sector.
## 3. Frame labels + coordinate discipline

- **Coordinate systems kept distinct (phase-space-coordinate-check):** `S_n`
  eigenvectors live in **n-PORT space**; the A1 dilatation scalar and the Cosserat
  shear vector live in **real-space**. The port→grade map was SHOWN explicitly
  (§2 table), not assumed. The differential `−1` port-modes project to a
  real-space VECTOR; the common-mode `+1` port-vector projects to a real-space
  SCALAR. The two grades are orthogonal at the embedding level.
- **NO coordinate clash / NO genesis-24 double-count:** the prereg §2e flagged the
  risk that the longitudinal-confinement question could force wiring the A1 scalar
  into a differential-port phasor. It does NOT: the A1 scalar is the **common
  mode**, cleanly orthogonal to the differential vector grade. This is fully
  consistent with `master-equation.md:20` (A1 ⊥ T2; "never wire the winding into
  the breather's own phasor"). The construction respects the no-phasor-wire
  discipline — recorded as a PASS, not flagged.
- **Class label (consistency-vs-emergence):** the bedrock spectrum result is a
  **structural-identity / manifestation** class result (the `(2/n)J−I` spectrum is
  forced linear algebra). The Fork-A REFUTE is a **structural negative** (a sector
  mis-assignment falsified). Neither is an emergence-class claim; no CODATA /
  manuscript-quoted target was input.

## 4. SYMMETRIC-STANDARD assessment (embedding vs DOF-counting) — the load-bearing honesty check

The 2-vs-3 differential multiplicity superficially matches the SM's massless-vector
(2 DOF) vs massive-vector (3 DOF) count. The prereg pre-committed: PASS-as-chord
ONLY IF the port→real-space embedding is DERIVED and predicts something beyond the
DOF count. Assessment:

- **The embedding IS derived** (from `bond_unit` / the lattice geometry), not
  posited — that is genuine substrate content. The srs differential multiplicity
  = 2 = photon transverse DOF is a real structural correspondence, derived from
  node valence rather than put in by representation theory.
- **BUT the result does NOT add the confinement asymmetry the chord required.** The
  pre-committed chord (longitudinal confined on n=4 / not on n=3, via the 3rd
  *differential* mode) was REFUTED — the longitudinal scalar is not a differential
  object. So at the differential-sector level, the result reduces to: *node valence
  n → (n−1) differential modes → matches the 2/3 transverse-DOF count.* That is a
  CHORD of **structure** (valence forces the count) but, for the *longitudinal*
  containment question Fork A actually posed, an **ECHO of DOF-counting**: it
  re-derives the transverse polarization count and says nothing AVE-distinct about
  longitudinal confinement that the SM's massless/massive distinction does not.
- **Symmetric-standard note:** the SM also does not derive WHY 2 vs 3 from a
  lattice — it is a representation-theory input. AVE deriving the *transverse* count
  from node valence is at least at parity and arguably ahead on the transverse
  sector. But the Fork-A *longitudinal* claim is where AVE would have been
  genuinely ahead, and that claim failed. So: **CHORD on the transverse-DOF
  derivation (structure); ECHO/REFUTE on the longitudinal-containment claim
  (the thing the gate was built to test).**

## 5. CHORD / ECHO / REFUTE verdict (against the frozen prereg §4)

| Prereg bin | Status |
|---|---|
| **CHORD** (C1∧C2∧C3) | ❌ — C1 (bedrock) holds, but **C2 fails** (no differential longitudinal confinement; the longitudinal mode is common-mode not differential) and C3's confinement-asymmetry is therefore absent. |
| **ECHO** (E1) | ⚠️ PARTIAL — on the *transverse* sector the 2-vs-3 reduces to the DOF count (E1 applies to the transverse-DOF correspondence). |
| **REFUTE** (R3) | ✅ **PRIMARY VERDICT** — "the bound longitudinal mode does NOT live in `P₋₁`; the longitudinal sector is the common-mode `+1` eigenspace, not the differential `−1`." This is prereg R3 verbatim, and it re-routes the containment picture toward Fork B. |

**Net:** the bedrock is a clean structural PASS (and a genuine fix of the
`graded_vacuum_network` TETRA_OFFSETS collapse). The Fork-A physics hypothesis is
a clean, single-mechanism REFUTE (R3). Honest closure (Rule 11): the branch closes
on a named mechanism (longitudinal = common-mode scalar, not differential), NOT
debugged toward a rescue, NOT re-binned post-hoc.

## 6. What this does and does NOT close + Fork-B handoff

**Closes (positively):**
- The `graded_vacuum_network` dense-`TETRA_OFFSETS` collapse — the srs (deg-3) and
  diamond (deg-4) operators are now built genuinely distinct from the actual
  CONNECT map (192 vs 64 DOF; first `build_srs_net` solver call-site).
- The bare-spectrum validate-on-known + the photon-2 and winding-3 anchors +
  α-free invariance.

**Closes (negatively, the Fork-A hypothesis):**
- Fork A's prediction that longitudinal confinement requires the diamond's 3rd
  *differential* mode is REFUTED (R3). The longitudinal A1 scalar is a common-mode
  object.

**Does NOT close (out of scope b, DEFERRED):**
- **Fork B (Grant's bulk-saturation arm) — now the INDICATED next arm.** The R3
  result points the A1 MASS-"3" containment at the **common mode (+1) = bulk
  saturation / volumetric compression**. Grant's framing (carried verbatim in the
  prereg §7): the `+1` saturation-bag arm is the **unbuilt `Z_core → ∞` operator**
  — an OPEN (reflecting) boundary on the common-mode channel. This gate did NOT
  build it; it surfaces that R3 makes Fork B the correct next test (the A1 scalar
  *is* the channel Fork B operates on). **This is surfaced for Grant's
  adjudication, NOT silently pivoted to.** (flag-don't-fix.)
- Forks C / D — DEFERRED, unframed.

**Reconciliation flag (surfaced, not fixed):** the prior prereg
`research/2026-06-19_electron-Q-coupled-network_prereg.md:40` "GATE1 passed FIRST"
was retracted via Rule 12 in this session's Stage-0 commit (body preserved, red
header, anchor → α-free invariance, no substituted number).

---

**END RESULT (scope b). Fork-A verdict: REFUTE-R3 (clean pre-registered negative).**

