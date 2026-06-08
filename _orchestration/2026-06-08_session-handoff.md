# 2026-06-08 session handoff — electron-synthesis + α-route + soliton-size arc

**Scope.** Distills the §16–§47 arc of the electron-structure synthesis epic
([`2026-06-07_electron-synthesis-epic.md`](2026-06-07_electron-synthesis-epic.md))
into a clean-state handoff. That epic is the detailed phase log (carried by **PR
#120**); this doc is the orientation layer: what resolved, what is scoped-and-
gated, what stays open, the open Grant decisions, the new infrastructure, and the
worktree-prune list.

**Headline.** The session pushed the electron picture to a defensible Class-A/B
consistency structure and then ran the α-value derivation to a clean negative on
every closed route — including walking back the "α to 1.5%" claim. The
honest closing: AVE constrains α's **scale and functional form** (substrate
geometry) but does **not** derive its **value**; the framing (α = a vacuum loss-
tangent / a relationship, not a fundamental constant) is the chord, the value is
a datasheet calibration entry. The new frontier is the soliton-size definition
gap, which surfaced a cluster of dimensional/category errors and is now scoped
for a gated adoption.

**State of the board at handoff:** 21 open PRs (#117–#137), all `MERGEABLE`
against `main` (`origin/main` HEAD `63e6671a`, Merge PR #116). 46 worktrees (21
KEEP / 22 prune-safe / 3 HOLD). Grant reviews each PR himself — see the
companion [`2026-06-08_pr-review-guide.md`](2026-06-08_pr-review-guide.md).

---

## 1. The arc in one screen (§16–§47)

The epic ran two interleaved threads: the **α-value-derivation thread** (does
the substrate read α out?) and the **electron-structure / soliton-size thread**
(what IS the object, and how big is it?). Both closed to honest negatives or
gated-scoped states; nothing in the arc claims an α readout or a derived
soliton size.

| § | topic | verdict |
|---|-------|---------|
| §16 | Water-chapter lessons | z=4 achiral diamond CONFIRMED (water builds it); chirality/spin forced onto the **Cosserat microrotation**, not the net. 2 over-reaches corrected (ice≠dark-energy; voids≠α-valleys). |
| §17 | α-valley-fraction (PR #121) | α-free NEAR-MISS; real-space envelope RULED OUT as the 137-source (valley fraction ~0.49 both frames). |
| §18 | Golden-Torus 137 audit | **FIT** at the exact-value level (1 knob `R·r` hand-set to ¼; substrate's own α-free value forces `R·r→4π²α`). |
| §19 | Paper-#4 extension | one genuine extension: trap → marginal **limit-cycle** (rings at ω_C forever), not a dissipative settle. |
| §20–§22 | φ-winding-stability route (PR #125) | EXHAUSTED. (2,3) is the LEAST-stable golden convergent (corpus selects it by MINIMALITY); (2,3) does NOT force `R/r=φ²`; lepton-tower discriminator does not exist. §18 FIT no longer contingent. |
| §23 | first-principles z₀ (archive pointer) | claimed α derived to 1.5% (z₀=4·(1+\|T\|)=52). **[Later WALKED BACK — see §31.]** |
| §24 | electron-as-cog | belt-trick in gear clothing; NOT a new mechanism. Nyquist-sampling-→½ is wrong 3 ways. |
| §25 | α-derivation history sweep | 15-route ledger; chiral-matching reframe DEAD (chirality is an α-CONSUMER); 2 murky open routes (Path A chirality-EMT; LC-tank Q=1/α). |
| §26 | session-close (first) | interim clean-state; superseded by §31's α walk-back + the soliton-size thread (§42–§47). |
| §27 | PR #126 audit | SOUND code; over-claims in the doc/description layer; walk-backs APPLIED + verified (`891d0f36`). |
| §28 | electron-modeling close-out of record | defensible Class-A/B structure; derives the CONDITIONS for a (2,3) electron, does NOT show the substrate dynamically SELECTS it. Spin-½/Dzhanibekov = 2 facts (T_d point-group + FM topology), NOT 1 mechanism. |
| §29 | Path C amorphous-EMT | Outcome D: z₀→51.65 (0.74%, route confirmed). **[Superseded by §31.]** |
| §30 | force-projection + piezoelectric | force=stress=∂W/∂strain (2 conjugate sectors); vacuum = chiral piezoelectric Cosserat solid; "EM = the vacuum's piezo response" = CONSISTENCY-class. |
| §31 | **Path C physical-lattice verdict (WALK-BACK)** | z₀=52 is NOT physically forced — it counts 48 secondary PATHS to 12 distinct atoms (path-multiplicity, not coordination). Physical z≈16 → 1/α≈49. **α NOT derived even to 1.5%; stays Class-B / calibration.** Supersedes §23/§25/§26/§29. |
| §32 | recent-results carry-forward | wave-impedance (c_L=√(10/3)c P-wave); GW=transverse shear at c; piezo doc (PR #127). |
| §33 | QM-foundations trio (PR #128) | superposition=ALIASING (synthesis) · collapse=SAMPLING/Born-derived (derived) · entanglement=THREAD (canonical). Origin-mislabel fix: aliasing→superposition (Bell-surviving). |
| §34 | phase-space→carrier-envelope mapping | lepton arm clean ((2,3) preserved, Cosserat-torsion ladder); proton (2,5) **real-vs-phase-space TYPE CONFLICT** flagged for Grant. |
| §35 | neutrino + high-E scale-check | ℓ_node = electron reduced Compton (NOT Planck); "electron at cutoff" = IDENTITY; aliasing→fractal-zoo UNGROUNDED; neutrino = GAP. |
| §36 | proton/vacuum/mass cluster | proton=PHASE-space CONFIRMED (walk-back); sub-node body = OPEN tension; +2281× size category-error caught (8π/5 coupling-ratio worn as length). |
| §37 | bulk/shear/torsion channel | muon-vs-proton is NOT bulk-vs-shear (both T2/transverse-EM); the distinction is topology+torsion, **torsion on the LEPTON side**; orchestrator mapping was inverted. |
| §38 | high-E aliasing prereg (PR #131) | well-formed + honest; testable content RELOCATED to the **topological-selection rule** (stable (2,4) would falsify). Adjudication conflict #10: emergence (leaf) vs consistency (prereg). |
| §39 | proton-mass I_scalar=1162 | **DERIVED, not fitted** (forward Faddeev-Skyrme output, no 1836 in loop). Honest magnitude = **+0.74% topology-only**, NOT −0.002% (that rides 1 thermal correction δ_th). Leans CHORD. |
| §40 | mass-spectrum pattern-test | PARTIAL: no-numerology bar 5/5 PASS (echo-killer); strong-chord (forward + ~1% + ≤1 correction) PROTON-ONLY 1/5. Proton's ppm = COINCIDENCE (δ_th over-cancel), not a spectrum property. |
| §41 | lepton-sector audit (PR #135) | μ-α¹/τ-α² premise REFUTED (both α⁻¹); no-numerology holds 5/5, tier degrades to matched-closed-form-no-solver; **√(3/7) MISLABEL confirmed** (dilatational √(1−2ν), not torsion-shear) — flagged for Grant. |
| §42 | r_opt dimensional propagation (PR #133) | self-audit found the r_opt-as-length error in **26 sites** (vs 4 named); 10 fixed, 2 in #132, 14 surfaced; cold-vs-thermal κ_FS split flagged. |
| §43 | r_opt code-use audit | REAL code-level scale bug in 2 files; 6 baryon STLs wrong-scale (~2290–4583×). **[Reopened by §45 as an A-vs-B fork.]** |
| §44 | code-provenance index prototype (PR #136) | 6-seed registry + drift-gate verifier; caught a §41 error (leptons LOOSELY-gated, not ungated). |
| §45 | soliton-size definition | **GAP CONFIRMED** — no canonical soliton-size definition; the conflation is CANONICAL. §43 reopened as an unadjudicated **A (sub-node) vs B (supra-node)** canonical fork. |
| §46 | node-Nyquist size resolution | **COHERENT-BUT-SYNTHESIS** — spine supported (node = spatial Nyquist boundary), A46 refinement (do NOT fuse spatial-Brillouin and phase-space-carrier axes), 3 tensions. SCOPED adoption gated on vocab-disambiguation + greenlight. |
| §47 | soliton-size vocab disambiguation | pedantic directive VINDICATED: **14 ambiguous load-bearing terms**; r_opt has a 2nd genuine-LENGTH meaning (so "r_opt is dimensionless" was half the story). Canon gated on Grant's review of the 14 clarity-risk terms. |


## 2. DONE — resolved / closed this session

- **Fork A (genesis amplitude crux) RESOLVED.** Electron = a parametric
  oscillator at threshold = a marginal Hopf **limit cycle** on the gain=loss
  locus, ringing at ω_C (the Compton clock). The "4× pump" was the lossless-
  parametric tongue with the dark-wake loss switched off; the real α-free loss
  bounds the pump and the m_ec² point sits ~on the locus. [§9/§12/§13/§19.]
- **Lattice = z=4 achiral diamond, water-confirmed.** Spin/chirality lives in
  the **Cosserat microrotation** (the 3 ω-sectors), NOT the net connectivity;
  the z=3 srs "chiral K4" name is decorative for the computational chain
  (λ_G=4/21, Lorentz, trampoline all on z=4). [§8.1/§16/§28.]
- **α-value derivation = NEGATIVE on every closed route (the honest closing).**
  Parametric loss = calibration · dark-wake far-field = 4π not 137 ·
  real-space valley = near-miss · Golden-Torus = FIT · twist = clean negative ·
  φ-winding = wall · z₀-EMT = α-circular · **z₀=52 "1.5%" WALKED BACK** as an
  unforced path-multiplicity count (physical z≈16 → 1/α≈49). **AVE constrains
  α's SCALE (~10², Compton-trap + π³ 3-volume) and FUNCTIONAL FORM
  (`aπ³+bπ²+cπ`, all coefficients forced) but does NOT derive its VALUE.** The
  framing (α = a vacuum loss-tangent / a relationship, not a constant) is the
  chord; the value is a datasheet calibration entry. α stays **Class-B**. [§18/§22/§25/§31.]
- **proton = PHASE-space (2,5)** (per-loop polarization winding in (V_inc,V_ref)),
  parallel to electron (2,3); real-space = 6₂³ Borromean tube-path. Walk-back of
  `proton-identification.md:19,30,32` confirmed (Rule-12). [§36 → PR #132.]
- **proton-mass I_scalar=1162 is DERIVED, not reverse-fitted** (forward
  Faddeev-Skyrme output; no 1836 in the loop). Honest emergence claim =
  **+0.74% topology-only** (κ=8π, c=5, V=2, p_c=8πα); the −0.002% rides one
  named thermal correction δ_th=1/(14π²) and is proton-specific (δ_th over-
  cancels = coincidence), NOT a spectrum property. Leans CHORD (1st datapoint). [§39/§40.]
- **mass-spectrum no-numerology bar holds 5/5** (every mass = a shared named
  constant or an inserted measured value — echo-killer); the forward-derived-
  to-~1% strong-chord is PROTON-ONLY (1/5). [§40/§41.]
- **QM-foundations trio** mechanisms fixed: superposition=aliasing (synthesis,
  consistency-tagged), collapse=sampling/saturation (Born p=2 derived), entangle-
  ment=topological thread (canonical, Bell-surviving). May-2025 origin seed
  re-targeted aliasing→superposition (one slot). [§33 → PR #128.]
- **Piezoelectric framing** (vacuum = chiral piezoelectric Cosserat solid; EM =
  the vacuum's piezo response) landed as CONSISTENCY-class. [§30/§32 → PR #127.]
- **Force-projection grounded** (force=stress=∂W/∂strain, 2 conjugate sectors;
  gravity = REFRACTION not pull). [§30 → folded in #130/#137.]

## 3. SCOPED — planned, gated on Grant

- **Soliton-size adoption (the recommended next workstream).** Verdict
  **COHERENT-BUT-SYNTHESIS** (§46): adopt the node-Nyquist spine + refine
  labels, do NOT promote-as-is. Gated on **(a)** the `w1pc27h3k` vocab-
  disambiguation lock (§47, 14 clarity-risk terms) AND **(b)** Grant's
  greenlight. Full plan in §7 below. SEPARATE from the multi-node-vs-single-node
  call (Grant decision, §4).
- **High-E aliasing prereg FROZEN** (PR #131): testable content RELOCATED from
  the ungrounded fractal-morphology to the **topological-selection rule** (a
  stable (2,4) baryon would falsify). No driver/result yet; corpus-testable now. [§38.]
- **Physics-flag resolutions** (PR #130): c_L=√(10/3)c P-wave canon + piezo
  force-dilution coordination-z0 link — Grant-accepted, staged as a corpus edit. [§32/§37.]

## 4. OPEN — Grant decisions awaiting adjudication

These are the framing-level calls this implementer lane does NOT make. Each is
load-bearing; several gate the soliton-size adoption.

1. **Soliton-size adoption mode** — adopt the node-Nyquist two-size framing
   (two SPATIAL sizes across the Nyquist node + winding as a distinct identity
   axis)? COHERENT-BUT-SYNTHESIS; gated on the vocab-disambiguation lock +
   greenlight. [§46/§47.]
2. **Multi-node-vs-single-node proton** — "proton spans MULTIPLE nodes"
   (`02_baryon_sector.tex:40`) vs "nucleus inside a SINGLE node"
   (`semiconductor_binding_engine.py:68`). SEPARATE from the size adoption;
   decides the §43/§45 A-vs-B fork below. [§46 tension 2.]
3. **§43/§45 A-vs-B canonical fork** — proton body is **A (sub-node**, D_p=0.84fm
   IS the body, r_opt-as-length is a BUG) or **B (supra-node**, r_opt≈5 ℓ_node
   IS the envelope, 0.84fm is an internal RMS feature, STLs are correct-scale)?
   Both canonical, opposite answers — do NOT collapse. Decides whether §43 is a
   code bug or the STLs are right. [§43/§45.]
4. **√(3/7) dilatational-vs-torsion** — √(3/7)=√(1−2ν_vac) at ν=2/7 is EXACTLY
   the DILATATIONAL/compressional (bulk) signature; the muon leaf labels it
   "torsion-shear." Does a torsion route independently reach √(3/7), or is it
   dilatational and the label is wrong? The identity is exact; only the label is
   at-issue. Flag-don't-fix. [§40/§41.]
5. **cold-vs-thermal κ_FS** — the proton leaf quotes COLD 8π/5=5.03 (#132); the
   baryon ladder quotes THERMAL κ_eff/5=4.990. Two proton r_opt numbers, both
   dimensionless + per-file-consistent, cross-file inconsistent. Single canonical
   convention = Grant's call. [§42.]
6. **Manuscript-figure reference** — which figure(s) the electron-genesis /
   photon-engine runs (#129, #134) feed into the manuscript, and at what scale-
   claim tier (the §43/§45 fork gates whether baryon-scale figures assert
   physical or rendering-only scale).
7. **Emergence-vs-consistency for m_p/m_e** (adjudication conflict #10) — the
   prereg classifies 1836.12 (−0.002%) as CONSISTENCY; the canonical leaf
   `torus-knot-ladder-baryons.md:41` self-classifies it as Class-4 EMERGENCE.
   Prereg is stricter; the ratio uses 8πα + topology (not clean single-m_e). [§38.]

## 5. NEW INFRASTRUCTURE

<!-- infra -->

## 6. OPEN TENSIONS (carry into next effort)

<!-- tensions -->

## 7. The scoped soliton-size adoption plan (the recommended next workstream)

<!-- adoption-plan -->

## 8. SKILL-CANDIDATE (watch list)

<!-- skill-candidate -->

## 9. WORKTREE-PRUNE list (list-only — do NOT prune this session)

<!-- worktree-prune -->

## 10. Cross-references

<!-- xrefs -->
