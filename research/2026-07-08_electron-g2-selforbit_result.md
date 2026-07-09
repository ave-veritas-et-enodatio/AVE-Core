# RESULT — Electron g-factor from the (2,3) c-speed self-orbit (analytic + sympy)

**Status:** RUN-COMPLETE. **VERDICT: [G2-FORCED]** (conditional on the canonical double-cover assignment — see §7).
**Prereg (FROZEN):** [`2026-07-08_electron-g2-selforbit_prereg.md`](2026-07-08_electron-g2-selforbit_prereg.md) @ commit `eb05cbf3`.
**Script:** `src/scripts/vol_2_particle_physics/electron_g2_selforbit.py` (sympy-verified — all 6 stages assert-pass).
**Arc:** electron-as-chiral-self-orbit (Grant-walked 2026-07-08). First test of the push.
**Branch:** `analysis/electron-g2-selforbit` (off `origin/main` @ `0341caba`). NO self-merge.
**Classification (`consistency-vs-emergence`):** FORM = chord (a forced dimensionless mechanism) / VALUE = N/A (peer-with-Dirac; g=2 is NOT an AVE-distinct value). Bin: **manifestation** on the substrate-mechanism axis, **consistency** on the observable axis. NO emergence-class value chord minted (§8).

---

## 0. VERDICT (one line)

The AVE (2,3)+A1 c-speed self-orbit **FORCES g = 2** as a pure dimensionless geometric integer, with the physical constants (m_e, e, c, ħ, ƛ_C) algebraically cancelled (firewall clean). The naive single-cover control gives **g = 1**, and — the sharp sub-result — a full **(p,q) torus-knot co-circulation also gives g = 1 for ALL (p,q)**: the winding topology ALONE does not lift g. The lift is supplied by the **A1⊥T2 sector split**, specifically the charge(single-2π-cover) vs mass(4π-double-cover) asymmetry. **WHERE the 2 comes from: g = N_cover**, and N_cover = 2 is the **(2,3) poloidal double-wrap = K4 bipartite 2-sublattice = spin-½ 4π double-cover**.

---

## 1. ★ g — symbolic and numeric

| Path | μ (symbolic) | S (symbolic) | **g** (symbolic) | g (numeric) |
|---|---|---|---|---|
| Naive c-orbit (single cover) | `e·c·ƛ_C/2` (= μ_B) | `m·c·ƛ_C` (= ħ) | **1** | 1 |
| (p,q) torus-knot co-circulation | `(I/2)·p·π(2R²+r²)` | `(mc/L)·p·π(2R²+r²)` | **1** (∀ p,q) | 1 |
| **AVE electron (A1⊥T2, N_cover=2)** | `e·c·ƛ_C/2` (= μ_B) | `m·c·ƛ_C/2` (= ħ/2) | **2** | 2 |
| Cover-degree generalization | — | `m·c·ƛ_C/N_cover` | **g = N_cover** | — |

The z-projected enclosed area of the (p,q) torus knot is derived exactly: `x ẏ − y ẋ = p·ρ²` (ρ = R + r cos qt), giving `∮ = p·π(2R² + r²)` — the **toroidal winding p multiplies the enclosed area**. Both μ_z and S_z inherit this same `p·π(2R²+r²)/L` factor, so it **cancels in g** (the negative control, §3).

**Numeric cross-check (anti-firewall):** substituting CODATA (M_E, C_0, HBAR, e_charge; ƛ_C = ħ/m_e c) into the symbolic g_electron returns **exactly 2** — g is INVARIANT under substitution, confirming the constants are not an input.

---

## 2. ★ WHERE the factor of 2 comes from (the trace)

**g = N_cover**, exactly, with every physical scale cancelled. The factor of 2 is the **cover degree of the spin observable**:

- The **charge / μ is cover-IMMUNE.** μ = I·A = (e/T)·πƛ_C² is a single-2π current loop; the charge encloses one area per traversal regardless of how many traversals the spinor needs to close. μ = μ_B, unchanged.
- The **mass / S IS cover-sensitive.** The A1 spin observable is a **4π double-cover spinor** (spin-½): it carries angular momentum ħ/2, exactly **half** the ħ that a single-cover (2π, g=1) object of the same μ would carry. S = S_naive / 2.
- g = 2m·μ/(e·S) = 2m·μ_B/(e·(ħ/2)) = **2**.

**The 2 is named, not hand-inserted:** it is the integer N_cover = 2, which is the **"2" of the (2,3) phase-space winding** (the poloidal / d-axis double-wrap; `ch8-alpha-golden-torus.md:31`). Per canon this "2" is **the same geometric content** as the **K4 bipartite 2-sublattice lobe-count** (`l3-electron-soliton-synthesis.md:103-105`) and the **SU(2)→SO(3) 4π double-cover / spin-½** (`theorem-3-1-q-factor.md:78`, `finkelstein-misner-spin-half-derivation.md` clm-salw2h) — "the same geometric content viewed at two abstraction layers, NOT two independent factors" (`ch8-alpha-golden-torus.md:73`). The **"3" (q-axis / toroidal winding) does NOT enter g** — it fixes charge/other structure, not the μ/S ratio. So among the three pre-registered candidate homes (§1.1 of prereg), the winner is **(A)=(B)** — the (2,3) poloidal double-wrap ≡ K4 bipartite double-cover; **(C)** the c-speed constraint sets the SCALE (μ_B, ħ) but cancels out of g.

**Coherence note (not an independent derivation):** the SAME "2" underlies spin-½, the zitterbewegung 2ω_C, m_Cosserat = 2m_e, AND now g=2. This is a coherence of one substrate integer across four observables — banked as coherence, not as four independent confirmations (the corpus explicitly frames them as one factor).

---

## 3. Naive-circle control (should be 1) — and the sharper (p,q) negative control

- **Naive c-orbit: g = 1.** ✓ (pre-registered). A single object (charge==mass co-located) circulating at c on one loop of radius ƛ_C gives μ = μ_B, S = ħ, g = 1. The geometry does NOT lift g by itself.
- **(p,q) torus-knot co-circulation: g = 1 for ALL (p,q).** ✓ This is the sharper control and a genuine finding: even on the actual (2,3) Clifford-torus winding, if charge and mass are the SAME circulating object, the toroidal winding factor p multiplies BOTH the enclosed area (→ μ) AND the angular momentum (→ S) identically, so it **cancels in g**. **The (2,3) knot per se is NOT what lifts g** — the A1⊥T2 SECTOR SPLIT is. This makes the discriminator sharp: g=2 is not a generic consequence of "electron is a (2,3) knot"; it requires the specific charge/single-cover vs mass/double-cover asymmetry.

---

## 4. Firewall status (pre-registered §4)

- **Constants cancel:** YES. In every g expression the free-symbol set contains **NONE** of {e, m, c, ƛ_C, ħ, R, r}; each g is a pure Rational (1, 1, 2) or the pure integer symbol N_cover. Machine-asserted `sympy-verified` per `src/scripts/vol_2_particle_physics/electron_g2_selforbit.py`.
- **No M_E / ALPHA / HBAR on the g-path:** YES. `ave.core.constants` is imported ONLY in stage [6] and ONLY to confirm g is invariant under CODATA substitution (a confirmation, not an input). No constant token reaches the symbolic g.
- **No hand-inserted zitter:** YES. ƛ_C/2 and 2ω_C are NOT inputs. The "2" enters solely as the integer cover degree N_cover (a topological winding number). The c-ceiling is imposed as ω·ƛ = c (the physical constraint), not as a plugged 2ω_C.
- **Verdict:** **FIREWALL CLEAN.**

---

## 5. VERDICT ROUTING → [G2-FORCED]

Per prereg §5: [G2-FORCED] requires g=2 (leading order) AND the (2,3)/A1 split provides the lift (naive g=1 AND (p,q) co-circulation g=1) AND firewall clean. **All three hold.** → **[G2-FORCED]**, conditional on the canonical double-cover assignment (§7).

Content: a genuine substrate MECHANISM for g=2 — the charge(single-cover)/mass(double-cover) asymmetry of the A1⊥T2 self-orbit. This is a real handle on the electron's interior: it says WHY g=2 rather than g=1, and pins the 2 to a specific named topological integer (the bipartite double-cover) rather than to the Dirac equation.

---

## 6. flag-don't-fix (surfaced, NOT resolved — for Grant)

`l3-electron-soliton-synthesis.md:103-105` reads BOTH "observable frequency = 2 × medium frequency" AND "m_e (observable) = m_Cosserat (medium)/2". Read against E ∝ ω these two lines point in **opposite directions** on *which* circulation is the fast one (the observable envelope or the Cosserat medium). This is a **corpus-internal direction-of-the-2 tension**, FLAGGED not resolved. **The g-result is robust to it:** the SIZE of the factor (the integer 2) is fixed by the bipartite cover degree regardless of the fast/slow narration; only the physical story of "which sector is the fast circulation" carries the ambiguity, and g = N_cover = 2 either way. (Grant's call on the direction; it does not move the verdict.)

Second flag (verify-before-cite): the coverage matrix has an internal tension on g=2's provenance — `2026-06-17_electron-coverage-matrix.md:52` says "the ratio derives" (clm-uatcql, double-cover ratio), while `:68` says "g=2 POSITED (imported)". **This result narrows that gap:** the ratio does NOT "derive" as a bare group-theory statement, but the FORM g=2 IS forced by the double-cover integer given the A1⊥T2 mechanical construction (g = N_cover, μ cover-immune, S cover-halved). It is neither "purely imported" nor "independently derived from nothing" — it is a forced form conditional on the (canonically-established) double-cover. Surfaced for the auditor to reconcile the two coverage-matrix cells; NOT edited here.

---

## 7. HONEST CAVEATS — the load-bearing modeling choice

**The g=2 is NOT purely integral-forced.** The (p,q) integral (§3) proves the OPPOSITE for a single circulating object: co-circulation gives g=1 for any knot. The ×2 comes entirely from the **asymmetry** that S is halved by the double-cover while μ is not. Two honest caveats:

1. **The load-bearing input is the double-cover halving of S (spin-½).** That the A1 spin observable is a 4π spinor carrying ħ/2 is the canonical Finkelstein–Misner result (`finkelstein-misner-spin-half-derivation.md`, clm-salw2h) — it is **imported into this computation, not re-derived here**. What THIS work adds is: given that halving, the mechanical g = 2m·μ/(qS) construction on the c-orbit **forces g = N_cover = 2** with all constants cancelling, and that the charge/μ is provably cover-immune (so only S is halved, not both). The mechanism (charge-single-cover ⊥ mass-double-cover) is the earned content; the double-cover integer itself is canonical input.

2. **The assignment "charge rides the poloidal 2, mass rides the backbone 1" is a modeling identification** (surfaced pre-freeze, prereg §1.4). It is substrate-SUPPORTED (the (2,3)'s "2" IS the double-cover per `ch8:73`), not ad hoc, but it is an identification, not an independent integral. Had the charge been assigned to the "3" (q-axis), g would be 3 (falsified). The (2,3) with the double-cover living on the "2" is what lands g=2 — consistent with observation, and the identification is the canonical one, but it is the hinge and is named as such.

**Scope (pre-committed, prereg §7):** g=2 is **peer-with-Dirac at the VALUE level** — Dirac's equation gives 2, the classical zitterbewegung construction gives 2, and this gives 2. The AVE-relevant result is g=2 as a **FORCED FORM** from the (2,3)+A1 double-cover geometry (a mechanism for WHY), **NOT an AVE-distinct value**. Do NOT headline g=2 as an emergence-class distinct-value chord.

---

## 8. What this does and does NOT establish

**Does:** (i) a mechanical, firewall-clean derivation that g = N_cover on the c-orbit, so g=2 is the FORM forced by the bipartite double-cover; (ii) a sharp negative control — the (2,3) knot topology alone gives g=1 (co-circulation), so the SECTOR SPLIT is the load-bearing structure; (iii) names the factor's home unambiguously (the poloidal "2", not the "3"; (A)=(B), not (C)).

**Does NOT:** (i) re-derive spin-½ / the double-cover (imported from clm-salw2h); (ii) predict a value distinct from Dirac (peer, by construction); (iii) resolve the corpus direction-of-the-2 tension (§6, flagged for Grant); (iv) touch canon or manuscript (result doc only). The coverage-matrix reconciliation (§6 second flag) is surfaced for the AUDITOR to land, not edited here.
