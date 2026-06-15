# Weak-C Canonization — Pre-Registration (Rule-12)

**Date:** 2026-06-15
**Branch:** `analysis/2026-06-15-weak-c-photon-continuum`
**Lane:** implementer (producer session for the weak-C canon amendment)
**Dispatch brief:** `C_WEAK_CANONIZATION_PACKET.md` (read-only auditor lane → Grant dispatch)
**Gate trail:** A (photon = lattice DOF) FALSIFIED by its own `a_true` derivation
(gate `wz3xkruoj`) → C FORCED by elimination → C means-test PASSED as **weak-C**
(gate `wejkhvnfb`, CANONIZE-WITH-FLAGS) → **Grant confirmed weak-C 2026-06-14**.

This doc is the Rule-12 pre-registration for the leaf edits landed on this branch.
It records the verbatim claim, the provenance, the corpus-grep inventory, the
classification verdict, and the three over-reach flags. The original bodies of
every leaf edited are PRESERVED; all edits are dated scope-notes layered on top.

---

## 1. The claim to canonize — weak-C (verbatim from brief §1)

> The **free photon is the continuum EM field** — the discrete LC-ladder's
> **long-wavelength regime** (L≫ℓ_node, where Z₀=√(μ/ε) and c=1/√(LC) are
> ℓ_node-independent), taken as the photon's propagation description. The free
> photon is **sub-saturation** (Δφ≪α, Z₀-matched) — it does **not** saturate/lock
> to nodes and carries **no zone-edge (qℓ)² dispersion** (→ no GRB Lorentz
> violation). The discrete K4 lattice is the **matter** substrate: **matter =
> saturation locked to nodes** (the standing entrained structure, smallest =
> electron). **Axiom-4 saturation is the one-way trapping gate** (continuum-light
> → lattice-matter, e.g. pair production), **not** the photon's propagation
> mechanism. The continuum photon **inherits the lattice's cubic symmetry** → it
> retains a tiny **(qℓ)⁴ optical anisotropy/birefringence** (δ≈2.2×10⁻²², the
> surviving forward prediction).

---

## 2. Provenance — why weak-C (for a fresh agent)

- **Branch A** (photon = lattice DOF that disperses at the zone edge) was
  **FALSIFIED by its own derivation.** `ℓ_node ≡ ℏ/m_e c` ⇒ photon zone edge
  `E_zone = N·m_e c²`, N = cells per smallest soliton, forced structurally small
  → zone edge 0.5 MeV–10 GeV → observed GeV–TeV GRB photons crossing ~Gpc
  (GRB090510 31 GeV, LHAASO 221009A 13 TeV) sit 10²–10³× above it → **excluded
  by 10.6–13.3 OOM.** A lattice-DOF photon cannot carry GeV–TeV light across the
  cosmos, yet it demonstrably does ⇒ continuum (C) is FORCED by elimination.
- **C means-tested → weak-C.** Strong-C ("exact ω=ck / δ=0 / no LIV ever /
  decoupling-theorem-as-derived") over-reaches: it would kill `clm-yr6tu4`'s
  surviving (qℓ)⁴ optical birefringence (δ≈2.2×10⁻²², solidity 0.78, NOT
  falsified) AND assert the still-undelivered decoupling theorem as derived.
  **Weak-C** keeps the (qℓ)⁴ prediction and scopes no-dispersion as
  empirically-corroborated-not-derived.
- **Banked (robust):** the A-falsification; C-forced-by-elimination; the weak-C
  means-test pass.

---

## 3. Corpus-grep inventory (ave-prereg Step 2; verified at HEAD 4bc17c7f)

The corpus already supplies the reconciliation — the edits ANCHOR on it, they do
not introduce it. All file:line re-verified at HEAD per `verify-before-cite`
(none had drifted from the brief's cited anchors except where noted in §7).

| Anchor | Content (verbatim, verified) | Role |
|---|---|---|
| `k4-port-irrep-decomposition.md:134` | *"the photon (T₂) needs to be massless when propagating freely (and it does — at sub-saturation amplitudes the T₂ mode is massless); the bound electron's Cosserat shell IS the massive mode that the same T₂ sector hosts at saturation."* | The free-vs-locked split, ALREADY canon — the reconciliation anchor. |
| `master-equation.md:16` | *"In the continuous limit (L ≫ ℓ_node), signal propagation is governed by the classical Maxwell-Heaviside acoustic wave equation"* | Continuum = long-wavelength regime, already canon. |
| `master-equation.md:61` | *"exact only in the leading-order long-wavelength EFT regime … This holds in the linear limit V ≪ V_yield"* | Maxwell is the L≫ℓ_node, sub-yield regime. |
| `z0-derivation.md:40` | *"The lattice pitch cancels identically … independent of the absolute scale ℓ_node"* | Z₀, c are ℓ_node-free → the propagation description is ℓ_node-independent. |
| `photon-identification.md:11` | *"The photon is the K4-TLM's stable T₂-only bound state"* (+ 2026-06-10 PROVENANCE-vs-STATE annotation at :13-32, PRESERVED) | The leaf needing a weak-C scope-note layered on. |
| `photon-identification.md:47, :98, :114` | T₂-only canonical row; "lives entirely in the rotational sector"; "stable bound state … is the photon" | Sub-saturation / continuum-limit relabels. |
| `framing_and_presentation.md:144` | *"The physical vacuum is not a continuum; it is a lattice with pitch ℓ_node"* (inside the Clay-Millennium "B2" anti-pattern section) | Disambiguate: "lattice" = MATTER substrate; B2 matter argument PRESERVED. |
| `binary-kill-switches.md:13` | GRB dispersion ⇒ topological decoupling theorem falsified (= AVE predicts NO photon dispersion) | The correct canonical (no-dispersion) reading. |
| `preferred-frame-and-emergent-lorentz.md:81` | C7-GRB-DISPERSION row, AVE prediction = *"Surviving forward prediction"* | The (qℓ)² GRB-dispersion horn to RETRACT (Rule-12). |
| `vol1/claim-quality.md:1652` (clm-yr6tu4, conf 0.78) | mixes BOTH horns: (qℓ)⁴ optical birefringence (KEEP) + "GRB dispersion at λ→ℓ_node is the surviving forward-prediction" (RETRACT) | The PARTIAL/KEEP-BOTH walk-back target. |
| `vol4/claim-quality.md:521` (clm-gw2wgc, conf 0.7) | GRB-dispersion + neutrino-parity kill-switches, "disclosed-import predictions … not in-leaf derivations of the bandgap/decoupling theorem" | The honestly-scoped upgrade target (§3.F). |
| `divergence-test-substrate-map.md:456` + cross-refs :320/:322/:334/:499/:601/:602 | C7 row "NULL = no dispersion = AVE survives"; cross-refs call C7 "the surviving Trans-Planckian discriminator … where cubic symmetry no longer averages" | OUT OF BRIEF SCOPE; already no-dispersion-compatible. FLAGGED for the reconciliation lane (see §6 + §7). |

**Grep outcome:** the corpus is in a HALF-STATED weak-C posture. The continuum/
lattice regime partition is canon (`master-equation.md`, `z0-derivation.md`,
`k4-port:134`); what is missing is (a) the explicit statement that the FREE
photon rides the continuum regime as its propagation description, and (b) the
resolution of the one pre-existing contradiction — `preferred-frame:81` framing
C7 as AVE *predicting* zone-edge dispersion vs the matrix/kill-switch surfaces
predicting the NULL. This canonization makes (a) explicit and resolves (b)
toward the no-dispersion horn.

---

## 4. The edits (Rule-12; §3.A–G of the brief)

All landed as dated scope-notes; original bodies preserved.

- **A** — `framing_and_presentation.md:144`: scope-note threading "one substrate,
  two regimes." Matter results stay lattice-conditional (B2 reject-continuum-limit
  argument for mass-gap/NS/θ-vacuum INTACT); the free photon rides the continuum
  long-wavelength regime. Does NOT weaken B2 for matter.
- **B** — `photon-identification.md` (:11 layered 2026-06-15 scope-note ABOVE the
  body, BELOW the preserved 2026-06-10 annotation; :47, :98, :114 annotations):
  "bound state" / "lives in the rotational sector" scoped to the FREE /
  sub-saturation / continuum-limit T₂ whose L≫ℓ_node limit is Maxwell. Does NOT
  write "the photon is not a lattice mode at all" (strong-C; excluded).
  `k4-port:26, :121` scoped to the free/continuum-limit T₂ per :134.
- **C** — C7 reconciliation toward no-dispersion: `binary-kill-switches.md:13`
  annotated as the correct canonical (no-dispersion) reading;
  `preferred-frame:81` (qℓ)² GRB-dispersion horn RETRACTED (Rule-12).
- **D** — clm-yr6tu4 PARTIAL/KEEP-BOTH walk-back (`ave-walk-back`): RETRACT the
  (qℓ)² GRB-dispersion horn; KEEP the (qℓ)⁴ optical birefringence
  (δ≈2.2×10⁻²², the surviving forward prediction).
- **E** — (qℓ)² zone-edge dispersion rescoped to MATTER carriers (lattice-locked),
  which the prediction survives FOR. Done within the preferred-frame leaf scope-note.
- **F** — clm-gw2wgc upgrade HONESTLY SCOPED: no-zone-edge-dispersion now
  "regime-grounded + empirically-corroborated prediction." Do NOT assert the
  topological decoupling theorem as derived (the rigorous exact-continuum-limit
  proof is still open; asserting-as-derived = substitution-not-retraction, A47 v11b).
- **G** — orphan-C7 leg: the wrong-carrier kill-shot retraction stands; C7
  resolves to no-photon-dispersion (corroborated). HOPF-A1 closes independently.

---

## 5. Classification (consistency-vs-emergence)

**Verdict: regime-identification consistent with the corpus's own model.**

- **No-dispersion content → Class C (consistency check).** AVE reproduces the
  observed GeV-TeV GRB null via the continuum-regime mechanism. The corpus
  already partitions continuum (Maxwell) vs lattice regimes
  (`master-equation.md:16`, `z0-derivation.md:40`, `k4-port:134`); this makes the
  free photon's residence in the continuum regime explicit and load-bearing.
  It is **NOT** Class D emergence (no new dimensionless observable derived from
  primitives without target input) and **NOT** Class 2 substrate-mechanism
  emergence (the decoupling theorem is NOT derived — asserting it would be the
  strong-C over-reach flag F guards against).
- **(qℓ)⁴ optical birefringence → the forward-prediction (Class E-flavored)
  content.** δ≈2.2×10⁻²² at 633 nm, a substrate-distinct prediction joint-tied
  to the K4 cubic point-group symmetry (first anisotropic invariant is quartic).
  This is the surviving forward prediction; it is KEPT.
- **Promotion check (Step 8c):** this work adds NO new substrate primitive beyond
  what canon carries (clm-yr6tu4 at 0.78, clm-gw2wgc at 0.7). Classification
  therefore stays at the canonical ceiling. The canonization makes explicit what
  canon half-states; it does NOT promote past canonical ceiling.

**Substrate-native-check (continuum-vs-lattice regime):** the free photon = the
T₂ transverse mode at sub-saturation (Δφ≪α), Z₀-matched (Γ=0, no reflection);
its long-wavelength limit (L≫ℓ_node) is the Maxwell continuum where Z₀ and c are
ℓ_node-independent. Matter = saturation locked to nodes (the Γ=−1 TIR wall
rendered as a BOUNDARY condition per Checkpoint 10, not a bulk term). One
substrate, two regimes (free/continuum vs locked/discrete). The A1 longitudinal
scalar stays REAL (the matter sector) — this is NOT a transverse-only / Gauss-
deleted framing.

**EE-first mapping:** the picture is EE-native — the LC-ladder long-wavelength
regime, Z₀=√(L/C), c=1/√(LC), ℓ_node-independent (canonical
`translation-circuit.md` LC-tank / distributed-TL rows; verified
`z0-derivation.md:40`). The free photon = the sub-saturation traveling wave on
the ladder; matter = the boundary-locked standing wave (Γ=−1).

---

## 6. The three flags (weak-C, NOT strong-C — over-reach guard)

1. **No-dispersion = empirically-corroborated + regime-grounded, NOT
   derived-from-a-theorem.** clm-gw2wgc upgraded to "regime-grounded +
   empirically-corroborated prediction"; the topological decoupling theorem is
   NOT asserted as derived.
2. **clm-yr6tu4 walk-back is PARTIAL/KEEP-BOTH** — RETRACT the (qℓ)²
   GRB-dispersion horn; KEEP the (qℓ)⁴ optical birefringence (δ≈2.2×10⁻²²).
3. **Continuum = a regime of the one substrate, NOT a 2nd fundamental field —
   count stays 3** {m_e, α, G}. μ₀/ε₀/Z₀ are SI-definitional/derived, not in the
   input set.

**STOP line:** any edit drifting toward strong-C (exact ω=ck / δ=0 /
no-LIV-as-derived / a coexisting continuum substrate) is NOT landed and is
surfaced in the return.

**Downstream flag (out of brief scope):** `divergence-test-substrate-map.md` C7
row (:456) and cross-refs (:320/:322/:334/:499/:601/:602) describe C7 as "the
surviving Trans-Planckian discriminator where cubic symmetry no longer averages."
The matrix C7 row itself is already no-dispersion-compatible ("NULL = no
dispersion = AVE survives"). These are NOT in the brief's §3 edit list and are
left unedited per surgical scope; flagged here for the reconciliation lane (the
"where cubic symmetry no longer averages" framing is the (qℓ)⁴-suppression-fails-
at-lattice-resolution / birefringence-class content, distinct from the retracted
(qℓ)² zone-edge GRB dispersion).

---

## 7. Anchor-drift + clean-edit log

(populated as edits land — see commit trail + the return to the auditor gate)
