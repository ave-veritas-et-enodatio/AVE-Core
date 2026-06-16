# K=2G crystalline provenance — orchestration lane (2026-06-15)

**Lane:** ONE derivation. Re-derive **K=2G (ν_vac=2/7)** on the crystalline **z=4 K4** elastic
structure via lattice dynamics — or show it can't be.
**Arc:** corpus-grep prereg → Rule-11 freeze → auditor-gate → driver/derivation → result →
**adjudicate to Grant** (he calls the provenance verdict; I bring the moduli computation).
**Branch:** `analysis/2026-06-15-k2g-crystalline-provenance` (worktree `/tmp/k2g-wt`, off `origin/main`
@ `40a2a2e7`). **PR only — main is PROTECTED, Grant merges. Do NOT merge.**

---

## The three-way fork (Grant adjudicates; I compute)

- **(a) crystalline-forced** — K=2G derives from the z=4 K4 elastic moduli → ν=2/7 geometrically
  inevitable (chord). Would require the crystal to force the stiffness ratio `k_a = 2·k_s`.
- **(b) GR-imported** — K=2G is the trace-reversal identity *required by GR* for transverse-traceless
  graviton propagation; the substrate moduli are *tuned* to hit it (calibration/matching, echo).
- **(c) amorphous-only** — K=2G derives only via the Feng-Thorpe-Garboczi (FTG) EMT on the
  *amorphous* z₀≈51.25 diluted central-force network (α-circular), which **contradicts** the
  crystal lean of Axiom 1.

**Discriminator.** Crystalline lattice-dynamics yields K=2G as a geometric inevitability →
crystalline provenance (a). Crystal yields K/G = f(k_a/k_s) as a **one-parameter family** not
pinned to 2 → K=2G is NOT crystalline-geometric → it's GR-imported (b) and/or amorphous-only (c).

---

## Corpus state (grep-verified 2026-06-15)

| Artifact | What it is | Provenance grade |
|---|---|---|
| `vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md:20` | FTG-EMT: K/G=2 crosses at p*=8πα on **amorphous z₀≈51.25** net; explicitly **α-circular** (z₀←1.187←p_c=8πα); self-labelled "**consistency illustration**, NOT a derivation" | (c) amorphous, circular |
| `vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md` | ν=2/7 from the isotropic identity ν=(3K−2G)/(2(3K+G)) **given** K=2G | algebraic consequent |
| `common/q-g47-substrate-scale-cosserat-closure.md:28` | "K(u₀*)=2G(u₀*) … This is the trace-reversal identity **required by General Relativity** for TT graviton propagation" | (b) GR-import (verbatim) |
| `research/2026-06-14_magic-angle-provenance-bh-forward-test-audit.md:18` | Landed verdict: **K=2G IMPORTED from GR**, u₀*≈0.187 ECHO, ν=2/7 FIRM | (b), already on main |
| `backmatter/01_appendices.tex:186` | Generic Cauchy/random central-force solid → **K=5/3 G (ν=1/4)**; AVE asserts K=2G as the *departure* | Cauchy default ≠ 2G |
| `backmatter/01_appendices.tex:131` | "Simulation confirms K=2G is an **emergent property of the Chiral LC coupling modulus**" | claim to test |
| `research/_archive/L3_electron_soliton/127_q_g47_path_b_eigenmode_results.md:273-300` | The ONE forward K4 Keating computation: **imposes** K=2G, back-solves `k_s=k_a/7`. Arrow is `K=2G ⟹ ratio`, never `geometry ⟹ K=2G` | imposed, not derived |
| `claim-quality-closure-roadmap.md:829` | **Q-G41** "Derive K=2G from K4 topology as topological inevitability" — roadmap **row only, UNSTARTED** | open, the real gap |

**Existing numerical machinery (do not rebuild):** `src/scripts/verify/q_g47_path_b_k4_eigenmode.py`
(9-DOF Cauchy-Keating K4 unit cell, relaxed K,G via internal-mode min, `find_k_theta_for_K_2G`),
`q_g47_path_b_plus_cosserat.py` (12-DOF Cosserat + chiral k_χ; E-irrep λ_G), `q_g47_session12_*`
(source of `K_0=4k_a+8k_s`, `G_0=8k_s`).

**FLAG surfaced by the sweep — internal 7-vs-2 inconsistency:**
- *Relaxed* (doc 127): `K=4k_a/9`, `G=2k_a·k_s/(k_a+2k_s)` → K=2G ⟹ `k_a/k_s = 7`.
- *Unrelaxed/clamped* (Session-13): `K_0=4k_a+8k_s`, `G_0=8k_s` → K=2G ⟹ `k_a/k_s = 2`.
- Two different stiffness ratios for "the same" K=2G point, depending on internal-strain relaxation.
  **The relaxed moduli are the physical macroscopic elastic constants** (optic modes relax under
  macroscopic strain — Kleinman internal strain). My driver resolves this.

---

## Result (2026-06-15) — Outcome A: crystal does NOT force K=2G

Driver [`src/scripts/verify/k2g_crystalline_provenance.py`](../src/scripts/verify/k2g_crystalline_provenance.py)
(standard diamond Keating lattice dynamics, **validated vs carbon diamond C44 to −0.36%**):

- **z=4 is sub-isostatic** (Maxwell z<2d=6). Central-force only → all shear moduli → 0 (floppy); bulk
  survives. Shear rigidity is **entirely bond-bending** → **K/G is a one-parameter family in ρ=k_a/k_s**.
- **Real z=4 diamond: ν≈0.067, K/G≈0.82** (bending-dominated, K<G) — **far from** K=2G (ν=2/7=0.286).
- K=2G requires a **tuned, averaging-dependent ρ\*** ∈ {3.67 (C′), 5.30 (Voigt), 6.62 (C44)} — none
  geometrically forced; cubic K4 anisotropy (A=1.21) makes "a single G" itself a choice.
- ν=2/7 ⟺ K=2G exact (the one firm link) — but the **consequent** of K=2G, not a derivation of it.

**Fork verdict (computation):** (a) crystalline-forced **REFUTED**; (b) GR-imported **SUPPORTED** (indep.
corroboration of the 2026-06-14 audit's IMPORTED grade); (c) amorphous FTG-EMT stands as a *consistency
illustration* only (α-circular, on the z₀≈51.25 amorphous net). Resolves the corpus's flagged 7-vs-2
ratio split (= relaxed-vs-clamped internal-strain modelling choice). Result doc:
[`research/2026-06-15_k2g-crystalline-provenance_result.md`](../research/2026-06-15_k2g-crystalline-provenance_result.md).

**To Grant (flag-don't-fix):** the provenance verdict is his call. Recommended: ratify (b), log Q-G41
closed-NEGATIVE ("K=2G is the GR trace-reversal operating point, not a K4 topological inevitability"),
cite this driver. The gravity sector already reads K=2G as IMPORTED on main — no canonical edit needed.

## Lane log

- **2026-06-15** — Lane opened. Corpus-grep prereg complete. Worktree + branch off origin/main.
  Cross-repo sweep: NO forward crystalline K=2G derivation in any of 9 repos; K=2G IMPOSED everywhere.
  Prereg frozen (Rule-11, `cdaecb63`) → auditor-gate (running) ∥ driver → result (`6937c8c0`),
  Outcome A confirmed. Awaiting auditor-gate, then PR (Grant merges).

## Status: ACTIVE — result landed, auditor-gate pending, PR-ready
</content>
</invoke>
