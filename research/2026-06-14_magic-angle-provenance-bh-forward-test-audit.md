# Magic-angle (u₀*) provenance + BH forward-test audit (2026-06-14)

**Status:** AUDIT — verdict **HYBRID (chord-candidate-pending-BH)**. Lands the formal magic-angle provenance verdict, propagates Rule-12 retract-headers over the "u₀* derived" overclaims (retract-don't-substitute), and records the BH forward test as the empirical chord-candidate.
**SHA-pinned:** AVE-Core `origin/main` @ `26f27966` (`26f27966dc466f281bdf227f3da8d5306ff0c08e`) — the true HEAD, **not** the parked-local ancestor `01f735bb`. Cited line numbers re-verified at this HEAD on landing.
**X-links:** `clm-iouqn9` (K4 magic-angle K=2G, u₀*≈0.187, ν_vac=2/7) · `clm-bjceop` (substrate-scale Cosserat prefactors) · `clm-395gps` (AVE merger ringdown 18/49).
**Trigger:** reject the "u₀* derived" framing where the *value* is asserted/back-fit; record the BH forward test; leave the 2/7 homonym as the flagged-open chord-vs-circular gate.
**Skills:** verify-before-cite (SHA-pin currentness + cited lines) · ave-walk-back (Rule-12 retract-headers) · ave-keep-both-discriminator · ave-evidence-framing-discipline · consistency-vs-emergence · ave-discrimination-check.

---

## §1 — Verdict: **HYBRID**

The magic-angle structure is **not one object** — it is three links of very different solidity. The audit grades each:

| Link | Grade | Why |
|---|---|---|
| **ν_vac = 2/7** from K=2G | **FIRM** | exact isotropic-elasticity identity ν=(3K−2G)/(2(3K+G)) = 4G/14G = 2/7 at K=2G (`clm-iouqn9:1023`). The one solid link. |
| **K = 2G** itself | **IMPORTED** | the trace-reversal identity **required by GR** for transverse-traceless graviton propagation (`q-g47-substrate-scale-cosserat-closure.md:28`) — matched to GR, not independently derived. ⟹ the **GR-recovery** BH tests are partly **circular** for the K=2G part. |
| **u₀\* ≈ 0.187** (the locus) | **ECHO** | back-fit, underdetermined — see §2. |

**Bottom line:** one firm link (ν_vac=2/7), one imported (K=2G), one echo (u₀\*). The firm 2/7 is what the **BH forward test** (§4) keys off — that test is the **chord candidate, pending**. Whether it is a *real* chord or circular is gated by the **2/7 homonym** (§5).

---

## §2 — u₀\*≈0.187 is ECHO (asserted / back-fit / underdetermined)

This **ratifies existing corpus caveats** and adds the smoking gun:

- **The verification scripts seed the target.** `q_g47_path_b_k4_eigenmode.py:54–58` hard-codes the "0.187 candidates" (`"u_0_star_A029": 0.187`, `"r_sec_d_minus_1": 0.187`) and `:26` "compare against **target 0.187**"; `q_g47_path_b_plus_cosserat.py:31` states *"λ_G renormalizes from 4/21 **toward (hopefully) 0.187**"*. The value is **seeded and tuned to**, not forward-derived.
- `clm-iouqn9` rationale (`common/claim-quality.md:1023`): *"the functional forms K(u₀), G(u₀) and the value u₀\*≈0.187 are **asserted, not exhibited** … the magic-angle locus itself is the soft link while the ν_vac consequence is firm."*
- `clm-bjceop` caveat (`:1073`): the chain *"takes the K=2G operating-point spring constants **k_a=2/7, k_s=1/7 as given**"*; k_s=1/7 is an explicit *"Path B+ canonical normalization choice"* (`research/2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md:34`).
- **By construction:** u₀\*=0.187 ⟺ r_secondary/d=1.187 is a definitional restatement (r_secondary/d = 1 + u₀\*; `trampoline-analogy-primer.md:472` admits "by construction").
- **Second, structurally-independent grounding (constitutive-side, 2026-06-15, PR #261 Phase 2):** the bond-stiffness ratio is the local impedance squared, ρ=k_a/k_s=Z_eff². On the **SYM branch where K=2G lives** (ε,μ co-scale, Z_eff=Z₀) the operating-point factor (Z_eff/Z₀)²=1 is **invariant for all S** ⟹ **no operating point — including the magic angle u₀\* — can select K=2G** (it would have to come from the cold geometry, which Phase 1 showed is unforced). A *constitutive* argument for the same conclusion as the *evidence* argument above (scripts seed 0.187): u₀\* doesn't fix K=2G. The ECHO is now **doubly-grounded.** See `research/2026-06-15_k2g-constitutive-provenance_result.md`.

### 🔴 RETRACT — don't substitute. **Do NOT refill u₀\*=0.187 with 4/21.**
4/21 ≈ 0.1905 is a **different object**: the soft-shear **E-irrep eigenvalue** λ_G (Keating discretization at K=2G), **forward-derived** and **chirality-blind** to 14 decimals across k_χ∈[0,1] (`trampoline-analogy-primer.md:489`; `claim-quality-closure-roadmap.md:191`). The primer itself (`:492`) calls 4/21-vs-8πα "coincidence between two K4-related small numbers." The back-fit **is** the attempted 4/21→0.187 renormalization (`q_g47_path_b_plus_cosserat.py:31`). So the **0.187-vs-4/21 fork dissolves**: retract the *u₀\*=0.187 derived* framing to "asserted/back-fit, underdetermined" and leave 4/21 where it is — they are not competing values of one quantity.

---

## §3 — Rule-12 retract-header propagation

**Applied by this audit** (original lines preserved per Rule 12; a retract-header added above each; **retract-don't-substitute, do not refill with 4/21**):

| Site | Overclaim | Action |
|---|---|---|
| `claim-quality-closure-roadmap.md:32` | "Q-G47 keystone **u₀\* derivation** … LANDED … delivered magic-angle equation" | RETRACT-HEADER (+ don't-refill-4/21) |
| `claim-quality-closure-roadmap.md:436` (§4.1) + `:446` | "**rigorous u₀\* derivation**" / "the **rigorous u₀\* value**" | RETRACT-HEADER |
| `claim-quality-closure-roadmap.md:290` | closure criterion (a) "**rigorous u₀\***" | sharpen → "operating-point selection (asserted/back-fit)" |
| `common/trampoline-analogy-primer.md:458` | "u₀\*=0.187 = r_secondary/d−1 = p_c = 8πα … is canonical" (forward identity) | RETRACT-HEADER (§6) |
| `common/claim-quality.md:1013` (`clm-iouqn9` caveat) | "u₀\*≈0.187 is **established**" | SOFTEN → "asserted, not exhibited" |

**Left alone (honest):** every "**joint-constrained at** u₀\*≈0.187" Class-E operating-point site (`omega-freeze-cosmic-grain-cascade.md`, `op14-cosmic-horizon-profile.md`, `cosmological-constant-closure.md`, `hubble-tension.md`, …) — u₀\* as the shared anchor, not a forward-derivation claim. (`helium-metamaterial-paradox.md:22`'s "0.187" is a Beryllium-9 table value — unrelated, **not** touched.)

**Additional soften-candidates (follow-up, not edited here):** `q-g47-substrate-scale-cosserat-closure.md:13` ("the magic-angle equation is **explicit** … **Structurally closed**"); `closure-roadmap.md:789`; `vol9/ch12-cosmological-characteristics/index.md:23`.

---

## §4 — The BH forward test (the chord candidate)

The **AVE-distinct, beyond-GR** falsifiers — these key off the FIRM ν_vac=2/7 and are the chord candidate:

| Falsifier | AVE | vs GR | Probe |
|---|---|---|---|
| **2/7-compactness** | 2GM/(c²R) < 2/7 ≈ 0.286 | stricter than Buchdahl 8/9 (`ave-compactness-limit.md:26`) | NS / BH mass–radius |
| **Iron-Kα inner edge** | r_sat = 7GM/c² | GR ISCO 6GM/c² (~17% larger) | X-ray reflection spectroscopy (XRISM / IXPE / Athena) |
| **GW echoes** | Γ_shear = −1 post-merger | absent in GR | LIGO/Virgo/ET — **mechanism contested, OPEN** |

- The "7" in r_sat: r_sat = r_s/ν_vac = (2/ν_vac)·GM/c² = **7GM/c²** (since r_s=2GM/c²; so the factor **7 = 2/ν_vac**, and the ratio r_sat/r_s = 1/ν_vac = 3.5). The Iron-Kα test keys off this 7GM edge.
- **NOT the ringdown.** ω_R·M_g = ℓ(1+ν_vac)/x_sat = **18/49** ≈ 0.3673 (1.7% vs GR 0.3737, `clm-395gps:164`) is a **GR-consistency recovery**, *not* a discriminator — and partly circular via the imported K=2G. Likewise Q=ℓ and the Hawking T_H are consistency-class.
- **Photon-geometric** observables (EHT shadow) do **not** discriminate r_sat from r_s and are correctly de-listed (`ave-bh-horizon-area-theorem.md:79–87`). The surviving falsifiers are **matter/shear** only.

> **⚠ Framing flag (flag-don't-fix).** The corpus does **not** yet frame this BH chain as a u₀\*-*pinning* route. Its stated pinning routes are **α** (EM Q-factor), **G** (Machian integral), **𝒥_cosmic** (CMB/LSS) (`omega-freeze-cosmic-grain-cascade.md:18–21`); the 8-observable u₀\* test list (`:59–68`) includes #8 "CMB QNM matching" (the 18/49 ringdown cross-checked at cosmic scale) but **not** the Iron-Kα / 2/7-compactness handle. So this audit records the BH/Iron-Kα chain as an **audit-proposed** forward test — a grounded AVE-distinct falsifier, **not yet a corpus-canonical pinning route**.

---

## §5 — The 2/7 homonym (FLAGGED OPEN — the chord-vs-circular GATE; Grant's physics call; does NOT block this landing)

The whole HYBRID verdict turns on this. **ν=2/7 carries ≥3 roles that share only the numeral:**

| Role | "2/7" as | Source |
|---|---|---|
| **elasticity** | the vacuum Poisson ratio ν_vac=2/7 (from K=2G) | `clm-iouqn9:1004` |
| **horizon** | the BH compactness bound + the "rigid skeleton fraction" entering the ringdown τ / r_eff=49M_g/9 | `ave-compactness-limit.md:26`; `clm-395gps:166` |
| **electroweak** | sin²θ_W = 2/9 (= 1 − 7/9, "near-2/x"), derived in-corpus from ν_vac=2/7 via E=2G(1+ν_vac) | `vol2/claim-quality.md:105,107` |

**The gate:** if **one physical 2/7 threads elasticity → horizon (→ electroweak)**, that is a **real chord** and the BH forward test is a genuine AVE-distinct prediction. If the three are **glued only by the numeral** (independent appearances of 2/7), then the BH test is **circular too** (it just re-expresses the elasticity 2/7). Recorded as the open gate per the trigger; **does not block this landing.**

*Finer sub-distinction (within elasticity): k_a=2/7 — the K=2G axial **spring constant** (`clm-bjceop:1073`) — is glyph-coincident with ν_vac=2/7 but a physically distinct quantity (a stiffness taken as input; k_s=1/7 a normalization choice). And the **dynamic-radiative** 2/7 (`clm-7tynm2` thrust) is a third role already walked back to candidate 4/49 (`vol4/claim-quality.md:193`). Symbol collision worth noting separately: ν_vac is also "Kinematic Network Mutual Inductance" ≈8.45×10⁻⁷ m²/s in Vol 0.*

---

## §6 — The 8πα conflation (trampoline-primer)

`trampoline-analogy-primer.md:458–490` presents u₀\*=0.187 as a forward geometric identity "= r_secondary/d − 1 = p_c = 8πα … is canonical." Two problems: (1) it **conflates** the K4 magic-angle u₀\* with the EMT percolation threshold p_c=8πα, which `clm-iouqn9:1012` keeps **distinct**; (2) numerically **8πα ≈ 0.1834 ≠ 0.187** (third-digit disagreement; the primer's own line 492 calls the 4/21-vs-8πα proximity "coincidence between two K4-related small numbers"). The retract-header flags the conflation + the by-construction circularity.

---

## §7 — Adjacent findings (flag-don't-fix; NOT edited by this audit)

1. **Arithmetic slip (2 sites).** "factor 7 = 1/ν_vac = 1/(2/7)" at `ave-bh-horizon-area-theorem.md:20` and `lattice-extreme-bh-rationality.md:77` is wrong — **1/(2/7) = 3.5, not 7**. The correct relations: r_sat/r_s = 1/ν_vac = 3.5, and the factor in r_sat=7GM/c² is **7 = 2/ν_vac** (because r_s=2GM/c²). Flagged for a separate fix.
2. **`clm-ir8h78` intra-claim tension.** r_sat=7GM/c² (ε₁₁=1, shear+bulk gauge) vs r_s=2GM/c² (ε₁₁=1, GW/EM gauge) — two radii for ε₁₁=1 in different gauges; the channel-split is canonical but the "ε₁₁=1 at both" phrasing reads as a tension worth a clarifying note.

---

## §8 — Classification

- **HYBRID verdict:** ν_vac=2/7 FIRM, K=2G IMPORTED, u₀\* ECHO. The GR-recovery BH observables (ringdown 18/49, Q=ℓ, Hawking T_H) are **CONSISTENCY** (and partly circular via the imported K=2G); the **AVE-distinct chord candidate** is the BH forward test (2/7-compactness, 7GM Iron-Kα, Γ_shear=−1 echoes), **pending**.
- The verdict is an **evidence-framing / honesty** correction, not a new physics claim. No clm is retired; the magic-angle LOCK and ν_vac=2/7 stand firm; only the "u₀\* derived" *framing* is retracted to "asserted/back-fit, underdetermined" — **retract-don't-substitute, not refilled with 4/21.**

---

*Auditor gate: verify this landed doc matches the audit verdict — HYBRID (FIRM ν_vac=2/7 / IMPORTED K=2G / ECHO u₀\*); every retract-header = "asserted/back-fit, underdetermined" with no 4/21 substitution; no honest joint-constraint site over-retracted; the BH forward test (NOT the ringdown) + the 2/7-homonym chord-vs-circular gate recorded, not resolved.*
