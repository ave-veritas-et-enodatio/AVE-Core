# Round 12 entry: unknot Cosserat seed canonical, post-bracket-Golden-Torus

**Date:** 2026-04-30 (entry); 2026-05-01 (doc creation)
**Predecessor:** [doc 100 §25 bracket-Golden-Torus reframe](100_a47_v9_reframing_line_687_retraction.md)
**Status:** Round entry — pre-registration pending Rule 16 plumber-physics adjudication on the unknot canonical's (R_loop, r_tube)

---

## §1 — Round 12 context

Doc 100 §25 closed Round 11's A47 v9 RESOLUTION arc by bracketing Vol 1 Ch 8's Golden Torus derivation per Grant 2026-04-30 ("the packing fraction was the og relationship; AVE-Core's Vol 1 Ch 8 Golden Torus was added to try to patch the zero-parameter claim — let's ignore the Golden Torus derivation for now"). The honest empirical state under packing-fraction canonical (parent's α = p_c/(8π) at K/G = 2 trace-reversal + parent's `39e1232` electron-is-unknot) is 6 ✅ + 1 🟡 + 3 ⏸ pending reframe.

Three of those ⏸ items are from Cosserat / AVE-HOPF / Theorem 3.1 Method 2 work that was Golden-Torus-tied. Doc 100 §25.6 surfaced three Rule 16 questions for Grant; in the same-day chat:

- **Q1 (α = p_c/8π chain) closes ✅** per Grant: "yes, it's where bulk-to-shear hits 2 in the lattice." Parent's chain is independent of Golden Torus; bracketing closes cleanly.
- **Q2 (Cosserat reframe) → option (ii):** add `initialize_electron_unknot_sector` to CosseratField3D. Real engineering work.
- **Q3 withdrawn:** Rule 14 failure mode — implementer presented framework-comparison options without walking substrate. AVE-HOPF λ(p,q) operates on (p,q)-torus knots; unknot isn't a torus knot in that sense; cross-anchor row stays ⏸; AVE-HOPF stands ✅ for what it does.

This doc opens Round 12 around the Q2 engineering work. Before pre-registering tests + driver implementation, surfacing the visualization gap that needs Grant's plumber-physics first (Rule 16 + Rule 14 discipline).

## §2 — The visualization gap: unknot's actual (R_loop, r_tube)

[`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md`](../../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md) has two statements about the unknot's geometry that are inconsistent by a factor of π:

**Reading A** (line 9 + Examplebox at lines 11-27):
- Circumference C_loop = ℓ_node = ℏ/(m_e c) (reduced Compton wavelength, exact via Bounding Limit 1)
- Tube radius r_tube = ℓ_node/(2π)
- → R_loop = C_loop/(2π) = ℓ_node/(2π)
- → R_loop = r_tube = ℓ_node/(2π) ≈ 0.159 ℓ_node
- **Geometry: horn torus** (donut hole closes to a point at center)
- Ropelength = C_loop / r_tube = 2π ✓ (matches line 7 + line 55)

**Reading B** (line 55):
- "The minimum discrete diameter of the flux tube is normalised to one fundamental lattice pitch ($d \equiv 1\,l_{node}$)"
- → r_tube ≥ ℓ_node/2 = 0.5 ℓ_node
- If r_tube = ℓ_node/2 exactly: combined with Reading A's C_loop = ℓ_node gives R_loop = ℓ_node/(2π) ≈ 0.159 ℓ_node and r_tube = 0.5 ℓ_node — but R < r is geometrically impossible (would mean tube self-intersects through center)
- More likely: ropelength = 2π gives C_loop = 2π × r_tube = π·ℓ_node, R_loop = ℓ_node/2 = r_tube
- **Geometry: horn torus at twice Reading A's scale**

Note both readings give horn-torus topology (R = r), differing only in absolute scale (factor of π).

**Hypothesis:** Reading B's "$d \equiv 1\,l_{node}$" is importing Vol 1 Ch 8's Nyquist constraint (where Vol 1 Ch 8 uses d = 1 to derive R = φ/2, r = (φ-1)/2 for the Golden Torus). Under bracket-Golden-Torus, the Vol 1 Ch 8 import doesn't carry; Reading A's r_tube = ℓ_node/(2π) stands. But this is a corpus-author call.

**Plumber-physics implication:** at Reading A's geometry, R_loop = r_tube = ℓ_node/(2π) ≈ 0.16 cells in any K4-TLM lattice with cell-size ℓ_node. That's sub-ℓ_node — the unknot is structurally smaller than one substrate cell at K4-TLM resolution. (This connects directly to E-094 Flag 2: "corpus electron's tube radius is ℓ_node/(2π) ≈ 0.16 cells = sub-resolution" per VACUUM_ENGINE_MANUAL.) CosseratField3D's continuous-coordinate JAX-autograd architecture is sub-ℓ_node-capable, so Cosserat CAN host the unknot at Reading A's scale.

At Reading B's geometry, R_loop = r_tube = ℓ_node/2, lattice-resolved at K4-TLM. Different physics consequences.

## §3 — Derivative gaps (follow from §2 ambiguity)

Once (R_loop, r_tube) is fixed, the rest of the unknot Cosserat-seed specification follows. But all three derivatives carry forward the §2 ambiguity:

### §3.1 — Field structure on the unknot loop

For (2,3)-torus-knot Sutcliffe seed at thin-torus geometry (R, r): ω-field has phase = 2φ + 3ψ where φ = toroidal angle (around major circle) and ψ = poloidal angle (around tube cross-section). Hedgehog amplitude profile localized on the tube cross-section.

For unknot at horn torus (R = r): the poloidal angle ψ is **degenerate** (donut hole closed; tube cross-sections meet at the center). What replaces the (2φ + 3ψ) phase pattern?

Candidate forms (need plumber-physics adjudication):
- **(α)** Phase varies as φ alone: ω = ω_0 · f(ρ) · exp(i·φ) where ρ is distance from loop axis. Single toroidal wrap, no poloidal structure.
- **(β)** Phase is constant: ω = ω_0 · f(ρ) — purely radial amplitude profile, no phase winding at all. Unknot has zero topological winding, so phase-constant might be canonical.
- **(γ)** Different ansatz family entirely (Hopfion-like? Skyrmion-like?) — the corpus's "Beltrami standing wave with E and B mutually orthogonal feeding into each other in a closed topological loop" doesn't directly map to the (2,3)-Sutcliffe ansatz family.

### §3.2 — Spin-1/2 mechanism without crossings

For (2,3)-torus-knot: c = 3 crossings (Op10) give the Dirac belt-trick geometrically. The 3-fold winding executes the SO(3) → SU(2) double-cover via the crossing-number topology.

For unknot: c = 0 by definition. The corpus (per `electron-unknot.md` line 9: "macroscopic g=2 Gyroscopic Precession ... Quantum Spin is therefore classically derivable as the continuous optical circulation of this massive electromagnetic light-loop") plus A-008 (SO(3) ω-field full-cover period = 2; SU(2) spinor observable = 1; factor-of-2 = half-cover identification at the medium level) jointly say spin-1/2 lives in the substrate's ω-field, NOT in flux-tube crossings.

But **what's the operational observable** at the field level? For the (2,3) knot, c=3 is what the engine measures via `extract_crossing_count`. For the unknot, c=0; what scalar measurement traces the half-cover behavior? Some Cosserat ω-field rotation rate around the loop? An integrated chirality? A spinor-projected observable that needs new infrastructure?

### §3.3 — Beltrami fundamental k-value at horn torus

The corpus says ∇×A = kA on the unknot. For Reading A geometry (R = r = ℓ_node/(2π)), what's k quantitatively?

Trivial substitution into AVE-HOPF λ(p,q) with (p,q)=(1,0) (single toroidal wrap, no poloidal) gives λ = 1/R = 2π/ℓ_node. That's just the wavenumber at the loop circumference. Whether that's the actual Beltrami fundamental at horn-torus geometry — I haven't seen worked out. The standard Beltrami mode analysis on a torus assumes thin torus (R ≫ r) which doesn't hold here.

## §4 — Rule 16 plumber-physics question for Grant

**Q (Round 12 entry):** Is the unknot's canonical (R_loop, r_tube) = (ℓ_node/(2π), ℓ_node/(2π)) per Reading A — i.e., sub-ℓ_node horn torus — and the Reading B "tube diameter ≥ ℓ_node" line is a Vol 1 Ch 8 import that doesn't carry under bracket-Golden-Torus? Or is the canonical (R_loop, r_tube) = (ℓ_node/2, ℓ_node/2) per a corrected Reading B — i.e., lattice-resolved horn torus — and Reading A's (2π) factor was the inconsistency?

If Reading A is canonical, the unknot is structurally sub-ℓ_node, and CosseratField3D is the right host (continuous-coordinate, JAX-autograd, sub-ℓ_node-capable per E-094 Flag 2). Reading A also makes the unknot circumference = ℓ_node = reduced Compton wavelength self-consistent with Bounding Limit 1.

If Reading B is canonical, the unknot is lattice-resolved at K4-TLM scale, but circumference = π·ℓ_node, NOT ℓ_node — which would unwind the Examplebox derivation and require a different mass relation.

Reading A appears self-consistent with the Bounding Limit 1 mass calculation. Reading B doesn't (needs C_loop = π·ℓ_node, but Examplebox derives C_loop = ℓ_node from m_e c² = T_EM·ℓ_node/c²). My implementer-lane read leans Reading A. But Rule 16: this is corpus-author adjudication, not implementer synthesis.

## §5 — Discipline notes (pre-registration framework, pending §4 adjudication)

Before this round commits to a driver, register the disciplines that closed Round 11's methodology debt:

- **A39 v2 dual-criterion** — any bound-state question gets BOTH frequency criterion AND topology/localization verification on the eigenvector. For unknot: c-extraction returns 0 (unknot's defining feature), so the topology-criterion needs a different observable — probably Hopf charge Q_H (extract_hopf_charge already exists at `cosserat_field_3d.py:1360`, returns Chern-Simons density integral). Pre-register `Q_H = 0` for unknot (zero Hopf charge — unlinked single loop).
- **A40 multi-N + multi-sector** — pre-register at minimum 2 lattice scales (32³, 64³) for scale-dependence detection. Pre-register both vacuum-only (V=0) and ω-only (Cosserat-only) sectors, since unknot may live primarily in ω-sector per A-008 substrate-level spin-1/2 mechanism.
- **A42 corpus-canonical topology measure** — c=3 via Op10 was for (2,3)-torus knot. For unknot, the topology criterion is c=0 + Q_H=0 jointly (both the c-extraction integer AND the Hopf invariant). Lattice-resolved-vs-sub-ℓ_node-resolved is a separate axis (per §4 reading adjudication).
- **A43 v2 anyone-must-grep** — every claim about unknot's canonical geometry needs corpus citation; this doc 101 §2-§3 already grepped the load-bearing electron-unknot.md. No assertions about unknot's canonical without citation chain.
- **A46 phase-space-vs-real-space** — pre-register coordinate system explicitly. Cosserat ω-field is real-space; if unknot's load-bearing observable lives in (V_inc, V_ref) phase-space, real-space Cosserat tests are diagnostic only. Need to walk substrate per Rule 14 BEFORE designing test (avoid §22 + §24 pattern).
- **A47 v11d axiom-chain-required-in-docstring** — any new code (`initialize_electron_unknot_sector`, validation drivers, tests) must include explicit Ax-N + Op-N citations in docstring at PR time. CI gate at claimed tolerance per A47 v13.
- **Rule 11 clean-falsification** — pre-register binary criteria that can fail decisively. Don't license post-hoc reframes (the §16 + §23 pattern Round 11 caught).
- **Rule 12 retraction-preserves-body** — any pre-reg refinement during round goes via Rule 12 retraction header, NOT silent edit.
- **Rule 14 substrate-derives-the-answer** — before presenting framework-comparison menus, walk substrate's structure first. (Round 11 §16/§23/§24 hit this failure mode three times.)
- **Rule 16 ask-Grant-first** — the §4 question gates pre-registration. Forward design holds for adjudication.

## §6 — Forward direction post-§4 adjudication

When Grant adjudicates §4:

**If Reading A canonical (R = r = ℓ_node/(2π), sub-ℓ_node horn torus):**

Step 1 — Walk substrate per Rule 14:
- Identify what observable in CosseratField3D's ω-field traces SU(2)/SO(3) double-cover for the unknot (per A-008 mechanism)
- Determine whether ansatz form (α)/(β)/(γ) from §3.1 matches the corpus Beltrami picture
- Compute the analytical Beltrami fundamental k-value at horn-torus geometry (§3.3)

Step 2 — Implement `initialize_electron_unknot_sector(R = r = ℓ_node/(2π))`:
- New initializer in `cosserat_field_3d.py` (~50-100 lines JAX)
- Axiom-chain in docstring (Ax 1 + 2 + 3 + 4 + Ropelength bound + Reduced Compton wavelength)
- Loop-axis seed (single closed flux tube; ansatz per Step 1 walk)
- Sub-ℓ_node localization on the lattice (R = r ≈ 0.16 cells)

Step 3 — Unit tests (analogous to existing Cosserat tests):
- Loop-axis localization sanity check
- Energy finite + non-negative
- ω-field magnitude profile centered at R_loop
- Hopf charge Q_H ≈ 0 (zero linking for unknot)
- c-extraction returns 0

Step 4 — Validation driver `validate_cosserat_unknot_eigenmode.py`:
- Multi-N (32³, 64³) per A40
- Pre-registered binary criteria per Rule 11
- Both energy-conservation and Q_H = 0 + c = 0 dual-criterion per A39 v2
- Compare vs corpus prediction: m_e from circumference + g=2 from gyroscopic precession claim

Step 5 — Engine-lane cleanup:
- Rename `initialize_electron_2_3_sector` → `initialize_2_3_torus_knot_sector` (per §21.5 recommendation, now decoupled from reading-3 baggage)
- Add `initialize_electron_unknot_sector` as the canonical electron seeder

Step 6 — Doc 101 closure section documenting the Round 12 empirical outcome.

**If Reading B canonical (R = r = ℓ_node/2, lattice-resolved horn torus):**

Different forward path — unknot is lattice-resolved at K4-TLM scale. CosseratField3D still works but isn't sub-ℓ_node-required. Examplebox circumference derivation needs corpus reconciliation (which Bounding Limit gives C = ℓ_node vs C = π·ℓ_node?). Round 12 may need to reopen `electron-unknot.md` consistency before driver work begins.

## §7 — Cost estimate

Given Reading A canonical:
- Step 1 (substrate walk + analytical Beltrami): 1-2 hours
- Step 2 (initializer code): 1-2 hours
- Step 3 (unit tests): 30-60 min
- Step 4 (validation driver + multi-N runs): 1-2 hours
- Step 5 (rename cleanup): 30 min
- Step 6 (closure doc): 30-60 min

Total: ~5-8 hours = full Round 12 session.

Given Reading B canonical: add 1-2 hours for `electron-unknot.md` corpus reconciliation before Step 1.

## §8 — What this doc does NOT do

- Does NOT pre-register the actual Round 12 tests (those wait for §4 adjudication)
- Does NOT modify CosseratField3D (Step 2+ work, post-adjudication)
- Does NOT adjudicate Reading A vs Reading B (Rule 16 surface-to-Grant only)
- Does NOT touch the `electron-unknot.md` chapter prose (manuscript-author lane)
- Does NOT close any of the 3 ⏸ items from doc 100 §25.5 (those resolve via Round 12 outcome)

This is a Round 12 entry doc, surfacing the visualization gap that gates the round's pre-registration. Per Rule 16 + Rule 14 discipline, the gap goes to Grant first; design follows.

— Doc 101 created 2026-05-01 as Round 12 entry per Grant directive 2026-04-30 ("just start the next doc; what's the specific physical picture you can't visualize here?"). The visualization gap is in §2 (line-9-vs-line-55 inconsistency in `electron-unknot.md`); §3 lists the derivative gaps that follow; §4 surfaces the Rule 16 question; §5 pre-registers methodology disciplines; §6 maps forward direction post-adjudication.
