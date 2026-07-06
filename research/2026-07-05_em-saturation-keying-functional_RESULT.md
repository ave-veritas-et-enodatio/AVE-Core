# EM-sector saturation keying functional S_E, S_B — RESULT

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/em-saturation-keying-functional`
**FROZEN prereg (gated on):** `research/2026-07-05_em-saturation-keying-functional_prereg_FROZEN.md`
(freeze commit `bfd897c5`, committed before any result — provable by git ordering).
**Drivers (three independent files, sympy + numpy, ReconcileGate, live positive controls):**
- `src/scripts/verify/em_saturation_keying_secular.py` — piece (a) secular averaging.
- `src/scripts/verify/em_saturation_keying_invariant.py` — piece (b) invariant selection.
- `src/scripts/verify/em_saturation_keying_constraints.py` — the six frozen falsifiers (reuses #539).
**Tests:** `src/tests/test_em_saturation_keying_functional.py` (15 fast-core gating + 1 engine_sim).

## ROUTED BIN: **[CONSTRAINT-KILLED]** — the boxed LOCAL-Poynting functional FAILS constraint 1 on the physical atom.

> **VERDICT RE-BINNED after the orchestrator review of PR #542 (2026-07-05).** The original
> `[FUNCTIONAL-DERIVED]` verdict below the fold is SUPERSEDED and does NOT stand. Two CRITICAL findings
> — both reproduced by this arc's OWN pipeline — force the honest negative. Git carries the original
> body; the corrected verdict is stated here at the top. This is Rule 11 honest closure: the
> pre-registered functional failed decisively on the physical atom, a single mechanism (local-vs-net
> transport) explains it, the branch closes, and the real product is the forward pointer (round 2).

**Why [CONSTRAINT-KILLED] (the frozen bin: "the derived functional violates a constraint"):**

- **CRITICAL-1 — the muonic PASS was an artifact of the `H=0` fiat.** The real muonic atom is NOT
  transport-dead: the proton magnetic moment (+ the 2P orbital moment) creates a PERMANENT static
  `E×H` circulation (hidden-momentum class) — divergence-free (zero net closed-surface flux) but
  LOCALLY nonzero. The boxed functional keys on **LOCAL pointwise `E×H`** ("power flux through a cell
  face") and CANNOT distinguish divergence-free circulation from net transport. Evaluated on the
  PHYSICAL atomic `H(r)` through the #539 bracket-integral machinery, the boxed functional engages at
  **1278× the 2.3 µeV CREMA window** (−2939 µeV at `r_cut=0.5a_μ`); even deleting everything inside
  `2a_μ` leaves **3× the window** (+6.85 µeV). The functional FAILS its own headline constraint.
- **CRITICAL-2 — the aliasing mechanism is refuted by this arc's own piece (a).** The
  secular-averaging computation shows a DC 2nd-order quantity SURVIVES clock-averaging (static
  `<E²>_secular = 1.0` at ω=0). So "boosted-static aliases to ω_C and averages out" contradicts the
  math it rests on; and the coded functional gives `T=5.4×10⁻²⁰ ≠ 0` for the boosted config the prose
  declared blind. **Boost-consistency is OPEN**, not closed structurally.

**What is retracted (MAJORS):**
- **"the substrate FORCES T-POYNT" → "T-POYNT is CONSTRAINT-SELECTED."** T-BEAT was eliminated BY
  Table-I survival — i.e. routed toward the anchored numbers (the visible-target the knife exists for).
  This is a constraint-selection, not a substrate derivation.
- **NORM-YIELD's "Table I unchanged" is a TAUTOLOGY** of the normalization definition (NORM-YIELD is
  defined as the flux reaching 1 at `E=E_c`). The "substrate-consistent" crowning is stripped; the norm
  fork is FULLY OPEN. (Moot for the verdict — the physical-atom overshoot is 10³×, far beyond 4π.)
- Dead contradictory `S_E_transport()` (the REJECTED frequency-suppressed T-BEAT form under a
  "DERIVED" label) removed; hardcoded PVLAS/BMV zeros replaced with a computed `S_B(A_I)` evaluation;
  the muonic `T==0` short-circuit removed (constraint 1 now evaluates the physical H and FAILS).

## THE FORWARD POINTER — the arc's real product (a NEW derivation, round 2, NOT a patch)

The review's own analysis names the surviving candidate: **NET transport** (closed-SURFACE flux —
zero for the atom's divergence-free circulation, nonzero for a propagating wave), **anchored in the
LATTICE REST FRAME**. Net-flux keying dissolves BOTH criticals: (i) the atom's hidden-momentum
circulation is divergence-free, so its closed-surface flux is zero → the atom is blind for the RIGHT
reason (net, not local); (ii) lattice-frame anchoring dissolves the boost contradiction the aliasing
story failed to close — the functional is frame-anchored by the theory's DECLARED preferred frame, so
a boosted observer sees transformed observables, not a re-keyed vacuum. **Round-2 requirements
(pre-registered here for the next arc):**
1. DERIVE net-vs-local from the network dynamics (not SELECT it against Table I).
2. The physical-H atom test is the STANDING falsifier (already landed:
   `test_muonic_physical_H_CONSTRAINT_KILLED`).
3. Recompute the pump engagement under net-flux keying (does a propagating wave still engage?).
4. Carry the coefficient-normalization fork OPEN (no tautological crowning).
5. No constraint-selected eliminations (the knife stays on the visible targets).

## CORRECTED CONSTRAINT STATUS (authoritative — supersedes the ~~PASS~~ table below the fold)

| # | constraint | corrected result | verdict |
|---|---|---|---|
| 1 | **MUONIC-H** (physical H(r)) | boxed LOCAL-Poynting on the physical proton-dipole H(r): −2939 µeV @ r_cut=0.5a_μ = **1278× the 2.3 µeV window**; +6.85 µeV @ r_cut=2a_μ = 3× | **FAIL → [CONSTRAINT-KILLED]** |
| 2 | THE PUMP | NORM-YIELD `𝒯=A²` (tautological match, fork OPEN); NORM-CLOCK ×(1/4π)² | engages, but on the KILLED local form |
| 3/4 | PVLAS / BMV | S_B(A_I) **computed** (A_I=3e-27/1e-25 via Faraday) → δn_μ≈0 | consistent (dual, computed) |
| 5 | DELLIGHT | −¼A² under NORM-YIELD (tautological, fork open) | consistent, on the KILLED local form |
| 6 | **BOOST** | aliasing REFUTED (piece-(a) DC survives; coded T≠0 on boosted config) | **OPEN** (not closed) |

The load-bearing verdict is constraint 1: **the boxed LOCAL-Poynting functional is [CONSTRAINT-KILLED]**.
Constraints 2/5 "engage" only for the local form that is already killed; 3/4 are the computed dual; 6 is
open. The forward pointer (net-flux, lattice-frame) is the round-2 arc.

---

## ORIGINAL VERDICT (SUPERSEDED — preserved below the fold; git is the trail)

> The following was the original `[FUNCTIONAL-DERIVED] + [PARTIAL]` verdict. It is SUPERSEDED by the
> re-bin above. Preserved verbatim for the record.

### ~~ROUTED BIN: [FUNCTIONAL-DERIVED] on structure + all six constraints — with a FLAGGED [PARTIAL] on the coefficient normalization only.~~ (SUPERSEDED)

~~Both pieces of Grant's candidate DERIVE from the substrate; the substrate forces the transport
invariant Grant named (Poynting, T-POYNT); all six frozen constraints PASS as-derived; the Table-I
consequence is quantified (unchanged under the substrate-consistent normalization); the S_B dual is
explicit and demonstrated to be the same transport/secular structure; boost is closed structurally.~~
The ONE piece the substrate does not fully force is the **coefficient normalization** linking the
transport engagement to `(E/E_c)²` — two natural normalizations give `1` (Table I unchanged) or
`1/(4π)` (Table I × 1/(4π)²). Per the frozen bins this coefficient-underdetermination is the
[PARTIAL] arm; the rest is [FUNCTIONAL-DERIVED]. **No dial was turned to satisfy any constraint**
(Rule 11): every constraint that passes does so because a held field carries no transport, not
because a parameter was chosen — and the coefficient fork is reported open, not resolved by fiat.

---

## THE DERIVED FUNCTIONALS (explicit forms)

### S_E — the electric-sector transport functional

$$
\boxed{\; S_E[\mathbf E,\mathbf H] \;=\; \sqrt{1 - c_{\mathcal T}\,\mathcal T},
\qquad
\mathcal T \;=\; \frac{\langle \mathbf E\times\mathbf H\rangle}{S_{\rm yield}}
\;=\; \left(\frac{E}{E_c}\right)^2\!\cdot\!\underbrace{\frac{H}{E/Z_0}}_{\text{co-moving fraction}} \;}
$$

- **The kernel argument is the TRANSPORT content 𝒯 (Poynting flux), NOT the field amplitude
  `(E/E_c)²`.** For a HELD static field `H=0` ⟹ the co-moving fraction `=0` ⟹ `𝒯=0` ⟹ `S_E=1`
  (no engagement — DC-BLIND). For a propagating wave `H=E/Z_0` ⟹ co-moving fraction `=1` ⟹
  `𝒯=(E/E_c)²` (fully engaged).
- `S_yield = c ε₀ E_c² = E_c²/Z_0` is the yield-field Poynting flux (the transport scale that
  self-consistently reaches engagement 1 at `E=E_c`, matching the Letter's kernel calibration).
- `c_𝒯` is the coefficient (see the FORK below): `c_𝒯 = 1` (NORM-YIELD, Table I unchanged) or
  `c_𝒯 = 1/(4π)` (NORM-CLOCK).

### S_B — the magnetic-sector dual (consuming Route C, MERGED)

$$
\boxed{\; S_B[\mathbf B,\partial_t\mathbf B,\nabla\times\mathbf H] \;=\; \sqrt{1 - A_I^2},
\qquad
A_I \;=\; \frac{I_{\rm cell}}{I_{\max}} \;=\; \frac{|\oint \mathbf H\cdot d\boldsymbol\ell|_{\rm norm}}{\xi_{\rm topo}c} \;}
$$

- `I_max = ξ_topo·c = 124.384 A` (`constants.py`, `relativistic-inductor.md`:15,18, clm-p5cf3t).
- Static B → `∇×H=0` → `I_cell=0` → `A_I=0` → `S_B=1` (transparent; clm-pvlas1, [C]-preserved).
- The E-side and B-side are DUALS under the same transport/secular structure: the shared transport
  current is the Poynting flux; the E-circulation `∮E·dℓ` (T-CIRC) is the exact dual of the B-side
  `∮H·dℓ` — both vanish for a curl-free static field and are subsumed by the Poynting transport for a
  propagating wave. **The duality is demonstrated, not asserted.**

---

## PIECE (a) — the secular-averaging result (node-clock aliasing → DC-blindness)

The node clock is exact: `ω_C = c/ℓ_node = 7.763e20 rad/s`, `ℏω_C = m_ec²` (ratio `1.0` to machine
precision). The preferred frame (lattice-rest + node clock) supplies the Park/dq0 reference — this is
the frame's honest work. Cycle-averaging the 2nd-order Axiom-4 kernel engagement over a clock cycle
(sympy PATH A + numpy PATH B, reconcile rel `0`):

| drive | `ω/ω_C` | `<E²>` (naive key) | `<(∂_tE)²>/ω_C²` (transport-gradient) |
|---|---|---|---|
| static (muon) | 0 | **1.0** (NONZERO — engages naively) | **0.0** (DC-BLIND) |
| pump 1.55 eV | 3.03e-6 | 0.5 | 4.60e-12 = `(ω/ω_C)²·½` |
| probe 10 keV | 0.0196 | 0.5 | 1.92e-4 |
| resonant | 1.0 | 0.5 | 0.5 |

**KEY RESULT (confirms Grant's premise):** the naive amplitude engagement `<E²>` does NOT vanish for a
static field (static limit `(E0/E_c)²`, wave limit `(E0/E_c)²/2`) — it distinguishes static from wave
ONLY by the `<cos²>=½` carrier factor, NOT by blindness. **This is exactly why the corpus R2
`A_V=|E|/V_yield` amplitude key fails muonic-H [C-EXCLUDED] (#539).** Grant's piece (b) premise also
holds: naive averaging blinds the pump too (`ω/ω_C=3e-6` is non-secular, same class as static). So the
surviving key must be a DIFFERENT, transport-class invariant — piece (b).

## PIECE (b) — which second-order invariant the substrate forces → T-POYNT

Each cell is a resonant LC tank (node-up:97). Its ε-reactance keys on the potential V∝E, its
μ-reactance on the circulation I∝∮H·dℓ (the keyed-argument duality, node-up:104-106). The Axiom-4
kernel is a LOCAL response to the node's operating point; since `<E²>` is DC-degenerate (piece a), the
engagement that distinguishes transport lives in the ENERGY the LC node EXCHANGES. For an EM field the
instantaneous power flux through a cell face IS the Poynting vector `E×H` (sympy PATH A, LC-node
energy-exchange). Therefore:

| invariant | held static | wave | frequency dependence | Table I |
|---|---|---|---|---|
| **T-POYNT** `<E×H>` | **0** (H=0) | `E²/Z_0` | **INDEPENDENT** | **PRESERVED** |
| T-BEAT `<(∂_tE)²>/ω_C²` | 0 (∂_tE=0) | `(ω/ω_C)²·½·E²` | `(ω/ω_C)²` suppressed | COLLAPSES (pump ×9e-12) |
| T-CIRC `∮E·dℓ` | 0 (curl-free) | dual of `∮H·dℓ` | (same class as Poynting) | subsumed by T-POYNT |

**The substrate forces T-POYNT** (matching Grant's Poynting candidate) because it is (i) the actual
power the LC node exchanges, (ii) zero for held stock, (iii) FREQUENCY-INDEPENDENT so the pump engages
fully (Table I survives — the decisive discriminator vs T-BEAT, which would collapse the pump by
`(3e-6)²=9e-12`), (iv) the `T^{0i}` stress-energy tensor flux, which closes the boost structurally, and
(v) bounded for a wave (a finite `<E²>/Z_0`, NOT the VCA-R01-Blocker-B pointwise singularity
`|∂_tB|/|B|=ω|tan ωt|` that diverges at zero-crossings). Reconcile `<E×H>=<E²>/Z_0` rel `1.6e-16`.

**The coefficient (HONEST, flag-don't-fix).** `𝒯/(E/E_c)² = 1/(4π)` under the rest-energy-per-clock
normalization (`P_C = mc²·ω_C` through a cell face); and the field-energy-density ratio
`u_field(E_c)/u_rest = 1/(8π)` — the `√(8π)` geometric family (clm-bdualb, the same family as the
B-sector dual). These are pure geometric constants, sympy-derived, NOT fitted; they do NOT contain any
mechanical-Q-point number (2/7, 9.7734, √8 — sector-guard test passes). **But the coefficient rides the
normalization choice** (see the fork).

---

## THE COEFFICIENT-NORMALIZATION FORK (the [PARTIAL] arm — reported open, not ruled by fiat)

The invariant CLASS (T-POYNT) is forced; the coefficient `c_𝒯` linking the transport engagement to
`(E/E_c)²` depends on the node-power normalization, and two natural choices give different values:

| normalization | scale | `c_𝒯` | 𝒯(wave) | Table-I `P_flip` |
|---|---|---|---|---|
| **NORM-YIELD** | Poynting vs yield-flux `c ε₀ E_c²` | **1** | `(E/E_c)²` | **× 1.000 (UNCHANGED)** |
| NORM-CLOCK | Poynting vs rest-energy-per-clock `mc²ω_C` | `1/(4π)` | `(1/4π)(E/E_c)²` | × `(1/4π)²=6.3e-3` |

**NORM-YIELD is the substrate-CONSISTENT reading:** it is the normalization for which the kernel
`S_E=√(1−𝒯)` engages at exactly 1 when `E=E_c` — i.e. it is self-consistent with the canonical `E_c`
calibration the Letter already uses (`E_c=√α·E_crit`, `constants.py:500`). Under NORM-YIELD the
transport functional is `𝒯=(E/E_c)²` for a propagating wave, **IDENTICAL to the Letter's `A²` for the
pump** — so Table I is UNCHANGED for the pump — while the muon (H=0) is BLIND (`𝒯=0`). This is the
clean resolution Grant's candidate needs. NORM-CLOCK is reported as the alternate; the substrate does
not by itself force one over the other, so the coefficient is the [PARTIAL] arm. **This is a fork for
the substrate/Grant to close (a dedicated computation on the LC node's power normalization would decide
it); it is NOT resolved here by fiat** (substrate-adjudicates-forks).

---

## THE SIX FROZEN CONSTRAINTS (evaluated as-derived; bands)

> ⚠️ **SUPERSEDED (this table's PASS column is WRONG — see the CORRECTED CONSTRAINT STATUS table above
> the fold).** Constraint 1's "PASS" was the `H=0` artifact; the physical atom FAILS (1278× window).
> Constraint 6's "PASS (closed structurally)" is retracted to OPEN. Preserved verbatim for the record.

| # | constraint | derived S_E/S_B result | verdict |
|---|---|---|---|
| 1 | **MUONIC-H** (reuse #539) | held Coulomb `H=0` → `𝒯=0` → `δ[ΔE]=0` EXACTLY, `< 2.3 µeV` CREMA window | **PASS** |
| 2 | **THE PUMP** (1e21 W/cm², BIREF@HIBEF) | NORM-YIELD `𝒯=A²=5.9e-7` → `δn_bir=−½A²` → P_flip **× 1.000 (Table I unchanged)**; probe dispersion `(qℓ_node)²`={2.94, 3.70, 6.39}e-4 across 8766/9835/12914 eV | **PASS** |
| 3 | **PVLAS** (2.5 T, Hz) | `ω/ω_C~8e-20` (DC in clock frame) → `A_I=0` → `δn_μ=0` (Route C) | **PASS** |
| 4 | **BMV** (ms pulses, ∂B/∂t) | `ω/ω_C~8e-18` (DC) → `δn_μ=0` | **PASS** |
| 5 | **DELLIGHT** (Sagnac common-mode) | propagating pump → `δn_iso=−¼A²` (NORM-YIELD, unchanged) | **PASS** |
| 6 | **BOOST** | motional E(2.5T,370km/s) `A²=6.7e-23` (matches Letter ~7e-23); boosted static = zero-sequence DC drift, aliased to ω_C, averages out | **PASS (closed structurally)** |

**Constraint 1 — the load-bearing result + the null-verdict-liveness proof.** The muon's held Coulomb
field carries zero transport (`H=0`), so the derived S_E is exactly 1 → `δ[ΔE]=0`. This is compared via
the SAME #539 bracket-integral machinery that routed the amplitude key [C-EXCLUDED]. **NULL-VERDICT
LIVENESS (trigger 10):** the identical pipeline fed a BOUNDED transport perturbation returns
`−5.27×10⁴ µeV` (nonzero, finite) — proving the `0` is physics (held stock has no transport), NOT a
structural bookkeeping zero that reads zero for any field. **This RESOLVES the load-bearing
contradiction flagged in the prereg §1.1:** the corpus R2 statement "a static E loads ε on `|E|`"
(node-up:217-218, pvlas-static-b-verdict:128) is what #539 falsified at atomic scales; the derived
TRANSPORT key does not load on a held field, so it passes muonic-H. **The corpus R2 `A_V=|E|`
amplitude-keying is SUPERSEDED by the transport key for the static sector** — surfaced to the auditor
lane (§ CORPUS below); the KB edit is the auditor's to land.

**Constraint 6 — boost closure, structural not numerical.** The Letter's own soft spot (main.tex:305-307:
"S depends on `|E|²`, NOT a Lorentz invariant → stated in the lab frame") is closed by the transport
key: `E×H` is the `T^{0i}` component of the stress-energy tensor — a genuine frame-covariant flux. A
held static field boosted into a moving frame acquires a motional partner field, but its Poynting is a
DC DRIFT (zero-sequence in the Park d/q/0 decomposition: no rotating d/q content). In the node clock
frame this drift is aliased to ω_C — non-secular — and averages out. Only a genuine wave carries d/q
rotating transport that survives the clock average. **Static E ↔ static B both map as zero-sequence
(both blind — consistent); transport ↔ transport (both keyed).** The preferred frame (lattice-rest +
node clock) is declared plainly; the transport key makes the boost closure structural, not a patch on
`A²` smallness.

---

## KNIFE CHECKS (armed)

- **½/¼ derived-only:** the `−½`/`−¼` coefficients are the Letter's DERIVED small-signal kernel
  coefficients (`δn_bir=−½A²`, `δn_iso=−¼A²`), not tells; MY new geometric factors are `1/(4π)`,
  `1/(8π)` (sympy-traced, `√(8π)` family), not `½`/`¼`. No new `½`/`¼` in the derivation.
- **ω_C/9-class thresholds:** the muon PASSES at `𝒯=0` (transport-blind), NOT at a cutoff scale — the
  #539 `9·ℓ_node≈3.5 pm` defeat-scale is not reproduced (the transport key needs no cutoff; that is the
  whole point). No ω_C/9 coincidence.
- **2/7, 9.7734, √8:** sector-guard test explicitly checks the EM coefficient is none of these
  (mechanical Q-point canon, a DIFFERENT sector) — PASS.
- **Suspiciously-exact constraints:** the muon `δ[ΔE]=0` to machine precision is CHECKED for structural
  degeneracy via the live positive control (a transported field gives nonzero) — the zero is physics,
  not bookkeeping.

## SECTOR HEADER + HOMONYM GUARD (honored)

- **EM channel** (ε-varactor / µ-inductor). **NOT the mechanical Q-point sector** (bond-strain / ρ_eff
  / transverse-tangent-stiffness). The pump-probe-tslot / matter-stiffening / channel-resolved-loading
  results (`research/2026-07-05_pump-probe-tslot_result.md`, #518, `..._channel-resolved-loading...`)
  supply a CROSS-SECTOR PRECEDENT that a traveling wave deposits a rectified 2nd-order mean a held field
  does not (⟨A_bond⟩>0 while ⟨y⟩=0) — cited for the MECHANISM CLASS only; NO number crosses the seam.
- **"A²" homonym** resolved: (i) Axiom-4 kernel arg, (ii) Letter `(E/E_c)²`, (iii) mechanical bond
  strain, (iv) MY transport `𝒯` — named distinctly throughout.

## DISCIPLINE

- **substrate-adjudicates-forks:** the invariant class is substrate-forced (Poynting); the coefficient
  fork is reported open for the substrate/Grant to close, not ruled by fiat.
- **consistency-vs-emergence:** the geometric factors `1/(4π)`, `1/(8π)` are CONSISTENCY-class
  magnitudes (they ride the `m_e`-derived `E_c` and the normalization); the CHORD is the STRUCTURE —
  transport-not-stock keying, DC-blindness, frequency-independence (Table I survives), the E↔B duality.
  This is the same "structure is the chord, magnitude echoes α" posture as the B-sector Route C.
- **flag-don't-fix:** the corpus R2 `|E|`-amplitude-loading vs #539 contradiction is surfaced with both
  verbatim citations; RESOLVED by the derivation (transport key), the corpus edit surfaced to the
  auditor lane, NOT silently rewritten here.
- **Rule 11 honest closure:** no post-hoc criterion drops; the coefficient underdetermination is
  reported as [PARTIAL], not converted to a clean [FUNCTIONAL-DERIVED] by picking a normalization.
- **verify-before-cite:** every constant live-derived vs `ave.core.constants` at HEAD `887b44f8`;
  muon mass declared external CODATA; #539 machinery reused by import, not reimplemented.
- Two/three independent code paths per piece + live positive controls + ReconcileGate; Kernel Check
  MATHEMATICALLY PURE; `make verify` green.

## CORPUS-STATE UPDATE (surfaced to the auditor lane — NOT landed here)

The auditor lane lands these; I surface the empirical finding:
1. **`node-up-small-large-signal.md`:217-218 / `pvlas-static-b-verdict.md`:128** — the R2 statement "a
   static E loads ε on `A_V=|E|/V_yield`" is SUPERSEDED for the atomic-static sector by the derived
   TRANSPORT key: a held field (Coulomb, `H=0`) carries no Poynting transport → `S_ε=1` → does NOT load.
   The R2 "E-route birefringence" survives ONLY for a PROPAGATING E-field (a pump/wave with `H≠0`), NOT
   for a held static E. This reconciles the corpus with #539 [C-EXCLUDED] and with the Letter's
   pump-probe (which IS propagating). **KEEP-BOTH candidate:** add the transport-keyed R2′ alongside the
   legacy amplitude-keyed R2 (per the KEEP-BOTH discriminator pattern), do not redefine-in-place.
2. **The Letter** (`papers/2026_birefringence_letter/main.tex`:305-307) — the "|E|² is not a Lorentz
   invariant, stated in the lab frame" soft spot has a structural closure available (the transport
   `E×H` tensor flux); an optional Letter note could cite it. Auditor/Grant decides whether to fold in.
