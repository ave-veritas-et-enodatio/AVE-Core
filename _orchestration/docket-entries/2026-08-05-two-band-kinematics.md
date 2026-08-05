# 2026-08-05 — Two-band / k·p kinematics of the K4 carrier sector (SVA pilot 4)

**Key:** `two-band-kinematics` · **Branch:** `research/two-band-kinematics` · **PR:** `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`
**Freeze (alone, pre-code):** `f5ddd995805d724e9e4edb769f384a6517eef1e9`
**Prereg:** `research/2026-08-05_two-band-kinematics_prereg-FROZEN.md` · **Result:** `research/2026-08-05_two-band-kinematics_result.md`

## Outcome

- **BIN: `FORM-REPRODUCED-V-MISMATCH`.** The relativistic massive form emerges exactly and
  isotropically on the Cosserat carrier sector; the carrier limiting velocity is not $c_{EM}$.
- **★The mismatch is STRUCTURAL, not a placeholder artifact — this is the headline.** The carrier
  splits into TWO limiting velocities and the splitting is exactly the gap-opening modulus:
  $v^2_\perp - v^2_\parallel = G_c/\rho = (I_\omega/4\rho)\,m^2$. A single carrier limiting velocity
  therefore requires $G_c = 0$, i.e. **no gap**. **No positive moduli give a massive carrier one
  limiting speed, let alone $c_{EM}$.** At the engine's placeholders $v/c_{EM} = \sqrt2$ (×2) and
  $\sqrt3$ (×4) against a frozen $10^{-9}$ tolerance.
- **★And the one branch that IS at $c_{EM}$ gets there by a derived cancellation.** The transverse
  translational (photon) branch has $v^2 = G/\rho \equiv c_{EM}^2$ **identically for all moduli**:
  the direct micropolar stiffness $(G+G_c)/\rho$ minus the k·p level repulsion $G_c/\rho$. The
  photon's speed is protected; the carrier's is not. That asymmetry is the constructive half of the
  LC-1 one-speed question and is arguably the more useful result.
- **★MATERIAL QUALIFIER — do NOT read this as superluminal transport.** The relativistic form's
  validity window closes BEFORE its own relativistic regime opens
  ($k_{\text{break}}/k_{\text{rel}} = 0.387$, $0.424$), and the full-BZ carrier group velocity peaks
  at $0.612\,c_{EM}$. The mismatch is in the **low-energy effective theory's invariant speed**.
  Root cause recorded: with $\ell_{node}\equiv\hbar/(m_ec)$ there is no scale separation between the
  carrier's Compton scale and the lattice cutoff, so no lattice regularisation of this family can
  have a wide relativistic window. **LC-1's arc-level kill is NOT fired** (that needs an
  energy-carrying inter-event channel at $\neq c$; this lane does not establish one).
- **VALUE-PROVENANCE (separate axis): `FACTOR DERIVED / VALUE IMPORTED`.** Factor 4 derived
  (`cosserat-mass-gap.md`:61); $G_c$, $I_\omega$ are engine placeholders (`cosserat_field_3d.py`:12,
  :954 — **no `constants.py` symbol exists for either**); MeV scale imported from CODATA $m_e$ via
  $\ell_{node}$ (`:143`, `:151`). No MeV gap value exists anywhere in the corpus. Frozen
  pre-derivation and quarantined off every verdict path.
- **Structural sub-finding:** the two-band split is **SECTOR**-based ($u$ vs $\omega$, opened by the
  ON-SITE micropolar term), **not** sublattice-based. The K4/diamond bipartite doubling supplies a
  degenerate partner inside each manifold, not the gap — the tetrahedral gradient is a first-moment
  operator with $\sum_\ell p_\ell = 0$, so a uniform A↔B offset costs nothing and the translational
  optical branch is not gapped at $\Gamma$. Not the graphene/staggered-on-site picture.

## Flags raised (verbatim in the result doc §7; none silently resolved)

1. **FLAG-1 — factor-2 tension in the gap's relativistic reading.** Branch bottom $\omega_m=2\omega_C$
   ⇒ $E_g = 4m_ec^2 = 2.044$ MeV, not the 1.022 MeV the Zitterbewegung / pair-threshold
   identification wants; landing $E_g=2m_ec^2$ needs $G_c/I_\omega = 1/4$, not 1. Either the
   placeholder is off by 4, or $\omega_m$ is being read as the full gap rather than the branch
   bottom, or the two "2"s (A-008 frame-vs-field double cover; the KG $\pm$ splitting) are
   double-counted. **Adjudication owed.**
2. **FLAG-2 — the dispatch brief's dispersion-model instruction contradicts the corpus for this
   sector.** The brief directed the arccos / coined-quantum-walk map and called the graph-Laplacian
   map canon-REJECTED; `srs-band-structure.md`:88-89 scopes that to the SCALAR channel and states it
   does NOT generalize to the vector channel. Resolution taken and declared: use the canonical
   Cosserat dynamical-matrix operator (the adjudicated model of the sector that owns the gap; the
   arccos map has no micropolar DOF to gap). **Brief flagged as scope-overreach, not followed.**
3. **FLAG-3 — the canonical Cosserat operator runs on the z=4 diamond CONTROL net**
   (`chiral_lattice.py`:240 verbatim *"Canonical diamond (engine-'K4', degree-4, achiral) control
   net"*), **not** the D1-ratified `srs-z3` production carrier (`:231`). So the sector's own
   canonical mass gap and band structure live on the control connectivity. **Surfaced, not resolved.**
4. **Pre-reg deviation, disclosed: G7a → G7b.** The pre-registered srs z=3 re-run is
   **BLOCKED-STRUCTURAL** and the blocker is MEASURED: every srs site's bond tensor
   $\sum_b \hat d_b\otimes\hat d_b$ has spectrum $\{0, 1.5, 1.5\}$, **rank 2** (trigonal-planar
   coordination), against the diamond control's rank-3 $\tfrac43 I$ — the engine's least-squares
   gradient functional does not exist on z=3. A new bond-based constitutive model was NOT silently
   substituted. Replacement gate G7b demonstrates connectivity-INDEPENDENCE of the $O(k^2)$ result
   (identical exact closed forms on z=6 cubic, z=8 bcc, anisotropic z=4), which is analytically
   why: the least-squares gradient symbol reduces to $i\mathbf k$ exactly for any full-rank
   centro-symmetric bond set. FLAG-3 therefore does not move the $O(k^2)$ verdict, and is NOT
   thereby discharged for $k^4$, band tops, zone-edge structure or chirality.

## Gates (UNRUN ≠ PASSED)

G1 PASS (independent rebuild bit-exact vs canonical; B-reference sign shown to be a unitary gauge) ·
G2 PASS (PR #392 V1–V4 negative control) · G3 PASS ($D(0)$ block structure, off-character weight `0.0`) ·
G4 PASS (Hermitian, lossless) · G5 PASS (k·p vs exact at mpmath 60 dps, worst decade-ratio deviation
$3.5\times10^{-8}$) · G6 PASS ($G_c\to0$ closes gap AND collapses the splitting) ·
**G7a BLOCKED-STRUCTURAL** / G7b PASS · G8 PASS (float64 shadow diverges by $2.9\times10^{9}$ —
a float64-only lane would have reported noise as the $k^4$ term) · deterministic double-run digest
`7d55f51139cc65e92082de1ef95605651f9870810c6e8de72decd20d1a27b135` twice.

Two conditioning defects were caught **at integrator time** (Rule 10) and are recorded: exact-rational
$v^2$ and exact mp direction normalisation are both mandatory — each otherwise produces a residual
that *diverges* as $k\to0$, and the axis direction $[100]$ hides the second one.

## Trigger-6 landing — FIRED, PARTIAL, fenced

The form derivation certified, so the conditional landing fired — **for the two-band / k·p rows only**.
Landed: `manuscript/ave-kb/common/translation-tables/translation-circuit.md` **§4.6.4** (end-append to
the semiconductor tier; line-pin-safe, nothing above edited) + claim card **`clm-2bkp7v`** in
`manuscript/ave-kb/common/claim-quality.md` (confidence 0.72, solidity `*pending*` by inheritance).

**The Zitterbewegung correspondence row was REFUSED, not deferred-by-oversight** — recorded in a
§4.6.4.1 "what is NOT landed here" block per the §4.7.4 precedent. Two reasons, both stated: the
lane's own frozen prereg fences Zitterbewegung out of what it licenses, and FLAG-1's factor-2 tension
sits directly on that identification.

**Confirms an existing canon ruling.** The §4.6.3 dated 2026-07-26 `def-mstar1` block already ruled
that the band-bottom $m^\ast$ read is sector-blind ("the gap divides out and the read hands back
*that branch's own* $c^2$"). This lane's independently pre-registered declaration that
$m^\ast = E_g/(2v^2)$ is TAUTOLOGICAL is the same finding, confirmed with residual `0.0`. What it adds
is the **per-branch $c^2$ inventory in closed form**. **D1 (sector of storage) stays OPEN.**

## Owed / routed (not taken here)

- Adjudicate **FLAG-1**; it gates the $E_g$ identification and hence the Zitterbewegung row.
- Rule on **FLAG-3** — whether the canonical Cosserat gap + band structure being on the CONTROL net
  is acceptable scope, or whether the z=3 bond-based constitutive model is owed.
- Rule on how the velocity mismatch feeds **LC-1** (this lane deliberately does not fire the kill).
- Note for the SVA pilot ledger: this is **pilot case 4**; per-row notes are in the lane return.
