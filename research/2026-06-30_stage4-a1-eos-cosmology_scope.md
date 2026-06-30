# Scoping / Design: Stage-4 — the A1 Equation of State (cosmology / dark sector)

**Status:** DESIGN/SCOPING (workflow wj4t51lwe, 12 agents; one map-agent died on a StructuredOutput retry-cap, covered by the others). No build, no repo writes beyond this doc.
**Verdict:** the A1-EOS three-branch frame is a **PARTIAL-RHYME** (kernel-shared, not sector-shared); Stage-4 as scoped is **CONSISTENCY-COSMOLOGY** with **exactly one** live chord-candidate — the unbuilt **F6 DE-tracks-matter depletion primitive**, which is greenfield and whose only prior depletion attempt detonates.

---

## 0. The frame, honestly: PARTIAL-RHYME (kernel-shared, NOT sector-shared)

Grant's "one A1 equation of state, three branches (compression=gravity / thermal=radiation·PV=nRT / tension=dark-energy)" is **decorative at the value level and mis-sectored on two of three branches**:

| branch | EOS | sector (canon) | status |
|---|---|---|---|
| **(1) COMPRESSION = gravity/mass** | `P=K·θ`, K=c⁴/7G | **GENUINELY A1** (dilatation=mass, PR#260) | Stages 1-3; consistency |
| **(2) THERMAL = radiation** | `P=⅓ρ` (w=⅓), PV=nRT | **A1-SOURCED, TRANSVERSE-CARRIED** (A1→T2 cross-sector trade — latent heat dumped to the CMB photon gas, cmb-thermal-attractor.md:10) | consistency |
| **(3) TENSION = dark energy** | `w_vac=−1−ρ_latent/ρ_vac<−1` | **ε-SECTOR** (op14:89,91 "the ε-sector projection… not μ-sector") — the OPPOSITE grade from A1 | consistency (value); F6 = the chord |

The frame survives **only in the weak reading**: a shared Axiom-4 kernel `S(A)=√(1−A²)` as common *ancestor*, with the A1 dilatation as the *projection channel for the cost* — **not** matter and DE as one A1 object on opposite branches. Stated strongly ("DE = the A1 tension branch") it **re-introduces the pressure-test-refuted DE=A1.**

**DE-SECTOR RULING.** A1-tension does **not** escape the refutation. The matter↔DE pressure-test refuted DE=A1 on (1) GRADE-attribution (DE is ε-sector, op14:91) and (2) SYMMETRY-inversion (matter breaks the K=2G lock; cosmic-bulk is the symmetric ground, wall-branch-fork:13) — **neither axis is compression-vs-tension.** Relabeling tension≠compression is irrelevant; the kill-shot never used that axis. **Compatible canon:** DE is the **Op14 CROSS-SECTOR TRADE** (op14:72) — the ε-saturation event funds an A1-channel volume-creation cost while expelling latent heat to the transverse CMB. Carry "A1-tension" as framing-scaffolding only; do **not** write it as canon.

---

## 1. Stage-4 is CONSISTENCY-COSMOLOGY (every recovery an echo)

- `ρ_Λ = 3H_∞²/8πG` via Friedmann = "no AVE-distinct content — standard GR" (closure.md:101); the 1.54→exact rescue **consumes Ω_Λ=0.685 as input** (closure.md:78).
- `w≈−1.0001` is ΛCDM-degenerate; `a(t)∝t^(2/3)`, `t^(1/2)` are inherited-GR; PV=nRT / `P=⅓ρ` are explicit consistency.
- Thermal α-running = **FT-1 CLOSED-NEGATIVE** (~31 OOM undershoot, generic-thermal, delta-strain-cosmic-tcc.md:15,125).
- **Drag-not-CDM** = peer-with-MOND on galaxies, but (i) **kernel-conflict** — KB-leaf LINEAR `√(1−g_N/a₀)` (effective-galactic-acceleration-mond.md:15) vs ENGINE QUADRATIC `np.sqrt(1−r²)` (galactic_mond_drag.py:49); the quoted 11.5% SPARC residual rode a kernel the manuscript does not state — and (ii) **CMB-EXPOSED** — zero acoustic-peak / BAO / structure-formation mechanism in corpus (the standard MOND-killer, unaddressed).

Standing meta-finding confirmed: AVE forces FORMS, imports VALUES; the chord lives only in forward predictions.

---

## 2. THE CHORD — exactly one: the unbuilt F6 DE-tracks-matter depletion primitive

ΛCDM's Λ is structurally rigid-homogeneous; it **cannot** make DE inhomogeneity track local matter density. If `ρ_latent` depends LOCALLY on the local A1-binding / matter-formation rate (an irreversible free-store depletion), the joint observable — **DE clustering correlated with matter density** — is ΛCDM-distinct *and* resolves the cosmic-coincidence problem dynamically. DESI/Euclid DE-clustering cross-correlation is the near-term test.

**A chord-CANDIDATE, not a chord:**
- **(a) ZERO prior art** — git-grep at HEAD for any cosmological depletion / tracks-matter / free-store / leaky-fuse primitive returns nothing. Greenfield.
- **(b) The one existing depletion attempt DETONATES** — `crystal_graft_v4.py` `photon_deplete=True` is an indefinite-Hamiltonian **detonation** (only `False` is stable). bemf-smoke verdict: *"the missing primitive is SOURCE DEPLETION, not reaction… a bounded norm-preserving photon→ω helicity-transfer WITHOUT the indefinite-Hamiltonian pump."* So F6 is **NOT** a relabel of an existing reversible operator (that is Stage-3) — it needs **new physics**: a bounded, norm-preserving, irreversible depletion coupling AVE does not yet possess.
- **(c) Earns chord status ONLY IF** the coupling `k` and response `g(·)` **derive substrate-natively from {ℓ_node, α, G}** — hand-set ⇒ fitted inhomogeneity ⇒ echo.

The two FORM-chords — the strong-field **clock-freeze** (`√S` vs `√(1−r_s/r)` peel) and the **latent-heat floor** `¾ρ_latent` — are real functional deviations but ride imported scales (G, ν_vac=2/7) and sit below observability (clock-freeze needs a ruler inside the region of influence; the floor predicts `T_U∼10⁻³⁰ K`, unfalsifiable). FORM-chord / ECHO-magnitude / near-unobservable — forward handles, not the chord.

---

## 3. Foundation caveats (gate everything)

- **(i) The homogeneous FRIEDMANN reduction is UNBUILT.** Stage-3 `solve_backreaction` is a STATIC inhomogeneous elliptic fixed-point, **not** a time-domain `a(t)` evolver. ("Stage-3 = the Friedmann engine run homogeneously" was an over-read.)
- **(ii) `ρ_latent` has ZERO numeric value** anywhere (symbolic only) — the single arithmetic blocker gating any energy-ledger pressure-test of the three-branch frame.
- **(iii) Off-HEAD currency** — `backreaction.py` + the scope docs + the matter-DE pressure-test live on sibling PR branches, not HEAD. "Stages 1-3 DONE" is true on `analysis/grqed-stage3-backreaction`, not main-at-the-scope-time. Don't hard-build Stage-4 until #438 + the scope PRs land (parallel-pressure-test discipline).

---

## 4. Build plan (gated)

| stage | deliverable | gate |
|---|---|---|
| **S4-0 FOUNDATION** | land Stage-3 (#438) + the scope PRs to main FIRST | `git branch --contains` confirms backreaction.py + the DE=A1-refutation text on HEAD |
| **S4-1 ρ_latent** | derive `ρ_latent = ΔE_cryst/node × node-density` from {ℓ_node, α, G} ALONE, in the ε-sector/cross-sector ledger | a numeric `ρ_latent` exists; check the Friedmann route `ρ_Λ=3H_∞²/8πG` equals the latent-heat route |
| **S4-2 Friedmann reduction** | thin homogeneous driver (∇ε₁₁→0 + genesis continuity, integrate `H²=8πGρ/3`) OR show Stage-3 reduces analytically | `a(t)` recovers `t^⅔`/`t^½`; de Sitter `H→H_∞`. EXPLICITLY consistency — chord NOT here |
| **S4-3 Γ_cryst** | derive the crystallization rate (currently ASSERTED `Γ=3Hρ_latent`, closure.md:111) from Op14 horizon | Friedmann and latent-heat routes give the same `ρ_Λ` |
| **★ S4-4 F6 DEPLETION** | the chord-or-bust build: bounded irreversible `dQ_free/dt=−k·J_matter`, `ρ_latent=g(Q_free)`, norm-preserving (non-detonating) | **MAKE-OR-BREAK:** (i) BOUNDED (no indefinite-Hamiltonian runaway); (ii) coupling DERIVES not fits |
| **S4-5 kernel-conflict** | reconcile LINEAR (KB) vs QUADRATIC (engine) drag kernel; SHA-pin the manuscript form; CI-gate | KB-leaf kernel == engine kernel (or the residual is re-run + documented) |

---

## 5. Forks for Grant

- **F1 — DE-sector (load-bearing):** (a) keep DE strictly **ε-sector + Op14 cross-sector-trade** [A1-tension = framing-scaffolding only, NOT canon]; (b) build a derived ε→A1-tension bridge [re-opens A1⊥T2; refutation stands until the bridge exists]. **Rec: (a).**
- **F2 — F6 scope:** build the bounded depleting coupling (the only route to a genuine cosmological chord) vs defer + bank Stage-4 as honest consistency-cosmology. **Rec: build, gate hard on non-detonation + coupling-derives.**
- **F3 — g*=7³/4 primordial-GW number:** run the /7-provenance discriminator (does the K4 stencil FORCE exactly 7 thermal channels?) BEFORE asserting — the /7 is load-bearing elsewhere (c⁴/7G, 2/7, 4/7 PPN), so reuse risks a rhyme. **Rec: run the discriminator first.**
- **F4 — binding-ledger sign:** SUBTRACT (per the 2026-06-29 §13 ruling, `ω_local=ω√S` down-regulation). **Confirmed; verify it survives the homogeneous reduction.**

---

## 6. The whole-arc landing

The engine recovers **GR + QED + derives its own metric + recovers ΛCDM-cosmology** — **all consistency, zero chords inside.** The single shot at an AVE-distinct prediction is **F6** (the DE-tracks-matter depletion operator): genuinely-new physics, greenfield, and blocked by a structural detonation in its only precedent. The chord lives only in forward predictions — exactly the standing meta-finding.
