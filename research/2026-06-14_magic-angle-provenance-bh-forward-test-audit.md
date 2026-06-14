# Magic-angle (u₀*) provenance + BH forward-test audit (2026-06-14)

**Status:** AUDIT — lands the u₀*≈0.187 provenance verdict, propagates Rule-12 retract-headers over the "u₀* derived" overclaims, and records the BH forward-test as the empirical path.
**SHA-pinned:** AVE-Core `origin/main` @ `26f27966` (`26f27966dc466f281bdf227f3da8d5306ff0c08e`).
**X-links:** `clm-iouqn9` (K4 magic-angle K=2G, u₀*≈0.187, ν_vac=2/7) · `clm-bjceop` (substrate-scale Cosserat prefactors) · `clm-395gps` (AVE merger ringdown 18/49).
**Trigger:** reject the "u₀* derived" framing wherever the *value* is asserted/back-fit; record the empirical path; leave the 2/7 homonym as a flagged-open physics call.
**Skills:** ave-walk-back (Rule-12 retract-headers) · verify-before-cite · ave-evidence-framing-discipline · consistency-vs-emergence · ave-discrimination-check.

---

## §1 — Verdict

**u₀* ≈ 0.187 — the K4 magic-angle operating point where K(u₀\*) = 2G(u₀\*), from which ν_vac = 2/7 follows — is ASSERTED / BACK-FIT / UNDERDETERMINED, NOT forward-derived from K4 alone.**

This **ratifies existing corpus caveats**; it is not a new contradiction:

- `clm-iouqn9` rationale (`common/claim-quality.md:1023`): *"the functional forms K(u₀), G(u₀) and the value u₀\*≈0.187 are **asserted, not exhibited** in the leaf … the magic-angle locus itself is the soft link while the ν_vac consequence is firm."*
- `clm-bjceop` caveat (`common/claim-quality.md:1073`): *"the closure chain takes the K=2G operating-point spring constants **k_a=2/7, k_s=1/7 as given** rather than deriving them from the K4 unit-cell Cosserat Lagrangian."*
- `q-g47-substrate-scale-cosserat-closure.md:25` boxes "K(u₀\*)=2G(u₀\*), u₀\*≈0.187" but **never exhibits the functional forms K(u₀), G(u₀)**; `:81` identifies 0.187 by *correspondence* ("over-bracing puts the bond's midpoint at A=1"), not by solving an exhibited K(u₀)=2G(u₀).

### What is FIRM (do NOT retract)
- The magic-angle **lock condition** K(u₀\*)=2G(u₀\*) — the GR trace-reversal / TT-propagation identity.
- **ν_vac = 2/7** from K=2G: ν = (3K−2G)/(2(3K+G)) = 4G/14G = 2/7 exactly (rigorous algebra, `clm-iouqn9:1023`).
- The downstream prefactors ξ_K1=8/3, ξ_K2=32 *given* k_a=2/7, k_s=1/7 (`clm-bjceop`, Q-G47 Sessions 19).

### What is BACK-FIT (the underdetermination)
- The **root u₀\*=0.187**: the K(u₀), G(u₀) forms are nowhere written out; 0.187 is identified by correspondence, not by solving an exhibited equation.
- **u₀\*=0.187 ⟺ r_secondary/d = 1.187 is true by construction** (r_secondary/d = 1 + u₀\*; `trampoline-analogy-primer.md:472` admits "by construction").
- **The factor-7 root is a normalization choice:** k_s=1/7 is an explicit *"Path B+ canonical normalization choice"* (`research/2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md:34`), and k_a=2/7 is then forced by the *assumed* K=2G ratio (`:33`). The entire 2/7-family's "7" rests on a normalization choice + the assumed lock, not a forward derivation.

---

## §2 — Rule-12 retract-header propagation

**Applied by this audit** (original lines preserved per Rule 12; a retract-header added above each):

| Site | Overclaim | Action |
|---|---|---|
| `claim-quality-closure-roadmap.md:32` | "Q-G47 keystone **u₀\* derivation** … LANDED … delivered magic-angle equation" | RETRACT-HEADER |
| `claim-quality-closure-roadmap.md:436` (§4.1 heading) + `:446` | "**rigorous u₀\* derivation**" / "the **rigorous u₀\* value**" | RETRACT-HEADER |
| `claim-quality-closure-roadmap.md:290` | closure criterion (a) "**rigorous u₀\***" | sharpen → "u₀\* operating-point selection (asserted/back-fit)" |
| `common/trampoline-analogy-primer.md:458–460` | "u₀\*=0.187 = r_secondary/d−1 = 8πα … is canonical" (forward geometric identity) | RETRACT-HEADER (see §3) |
| `common/claim-quality.md:1013` (`clm-iouqn9` caveat) | "u₀\*≈0.187 is **established**" | SOFTEN → "asserted (see this entry's rationale)" |

**Additional soften-candidates (listed for a follow-up pass; not edited here to keep this landing focused):** `q-g47-substrate-scale-cosserat-closure.md:13` ("the magic-angle equation is **explicit** … **Structurally closed**" — the forms are not exhibited); `claim-quality-closure-roadmap.md:789` (watch-item "closes with u₀\* matching α route"); `vol9/ch12-cosmological-characteristics/index.md:23` ("AVE substrate-physics **derives** … u₀\*").

**Left alone (honest framing — NOT retract targets):** every "**joint-constrained at** u₀\*≈0.187" Class-E operating-point site (`omega-freeze-cosmic-grain-cascade.md`, `op14-cosmic-horizon-profile.md`, `lattice-genesis-hubble-tension.md`, `cosmological-constant-closure.md`, `hubble-tension.md`, …) — there u₀\* is the *shared anchor / joint-constraint*, not a forward-derivation claim. Several even concede non-closure (`zero-parameter-universe.md:54`; `closure-roadmap.md:785` records the falsification-watch "no magic-angle operating point" risk). `helium-metamaterial-paradox.md:22`'s "0.187" is a Beryllium-9 table value — unrelated, **not** touched.

---

## §3 — The 8πα conflation (trampoline-primer)

`trampoline-analogy-primer.md:458–490` presents u₀\*=0.187 as a forward geometric identity "= r_secondary/d − 1 = p_c = 8πα … is canonical." Two problems:

1. It **conflates** the K4 magic-angle u₀\* with the EMT percolation threshold p_c=8πα — which `clm-iouqn9:1012` explicitly says to keep **distinct** (substrate-scale over-bracing vs amorphous-network EMT operating point).
2. Numerically **8πα ≈ 0.1834 ≠ 0.187** — they differ at the third digit; the primer's own line 490 calls it *"coincidence between two K4-related small numbers."*

The retract-header flags the conflation + the by-construction circularity (r_secondary/d = 1+u₀\*). A full de-collision of u₀\* vs 8πα is a separate adjudication.

---

## §4 — The BH forward test (the empirical path)

This audit records the **black-hole compactness + ringdown + Iron-Kα chain** as the empirical path that would constrain the otherwise-underdetermined u₀\* (through its firm ν_vac=2/7 consequence):

| Link | Value | Source |
|---|---|---|
| Saturation horizon | r_sat = 7GM/c² = 3.5 r_s (Axiom 4, ε₁₁(r_sat)=1) | `ave-compactness-limit.md:14–16` |
| **2/7-compactness bound** | 2GM/(c²R) < 2/7 = ν_vac | `ave-compactness-limit.md:23–26` (`clm-x19btt`) |
| Effective radius | r_eff = r_sat/(1+ν_vac) = 49M_g/9 ≈ 5.44 M_g | `clm-395gps` (`vol3/claim-quality.md:166`) |
| Ringdown eigenvalue | ω_R·M_g = ℓ(1+ν_vac)/x_sat = **18/49** ≈ 0.3673 (1.7% vs GR 0.3737) | `clm-395gps:164` |
| **Iron-Kα probe** | inner-disk edge at r_sat=7GM vs GR ISCO 6GM; discrete sub-peaks in the broadened Fe-Kα line from the refractive gradient | `first-principles-predictions.md:12–14`; `ave-bh-horizon-area-theorem.md:84` |

The discriminating falsifiers are **matter/shear** observables (the 2/7-compactness bound, the 7GM Iron-Kα inner edge, Γ_shear=−1 GW echoes); **photon-geometric** observables (EHT shadow) do **not** discriminate r_sat from r_s and were correctly de-listed (`ave-bh-horizon-area-theorem.md:79–87`).

> **⚠ Framing flag (flag-don't-fix).** The corpus does **not** currently frame this BH chain as a u₀\*-*pinning* route. Its three stated u₀\*-pinning routes are **α** (EM Q-factor), **G** (Machian integral), and **𝒥_cosmic** (CMB/LSS) (`omega-freeze-cosmic-grain-cascade.md:18–21`); the 8-observable u₀\* test list (`:59–68`) includes #8 "CMB QNM matching" (the 18/49 ringdown cross-checked at cosmic scale) but **not** the Iron-Kα / 2/7-compactness accretion-disk handle. So this audit records the BH/Iron-Kα chain as an **additional, audit-proposed** forward test that would constrain u₀\* via ν_vac=2/7 — a grounded AVE-distinct falsifier, but **not yet a corpus-canonical pinning route**. Promoting it to one is a follow-up.

---

## §5 — The 2/7 homonym (FLAGGED OPEN — Grant's physics call; does NOT block this landing)

The corpus position (`LIVING_REFERENCE.md:331/352`) is that the many "2/7" instances are **one object** — ν_vac=2/7 projecting through K4/SRS geometry. The audit finds that is *mostly* true, with one genuine glyph-coincidence:

| "2/7" | What it is | Same object as ν_vac? |
|---|---|---|
| **ν_vac = 2/7** | vacuum Poisson ratio, ν=(3K−2G)/(2(3K+G)) at K=2G | — (the canonical object; firm) |
| **k_a = 2/7** | the K=2G operating-point **axial spring constant** (`clm-bjceop:1073`) | **glyph-coincident, physically DISTINCT** — a bond stiffness taken as input; k_s=1/7 a normalization choice |
| 2GM/(c²R) < 2/7 (BH compactness) | the compactness bound = ν_vac | **same** ν_vac |
| static ν_vac=2/7 (`clm-7tynm2` thrust) | the same Poisson ratio | **same** ν_vac (the *dynamic-radiative* reuse is the distinct role — walked back to candidate 4/49, `vol4/claim-quality.md:193`) |
| K_0=16/7, G_0=8/7 (`clm-bjceop:1071`) | discrete moduli, K_0=2G_0 | 7-denominator relatives, **not** 2/7 |
| sin²θ_W = 2/9 (`vol2/claim-quality.md:105`) | **derived** from ν_vac=2/7 (1 − 7/9) | not a 2/7 |

**The open question (Grant's call):** is k_a=2/7 (spring) genuinely the *same* 2/7 as ν_vac (Poisson), or a coincidence of the k_s=1/7 normalization choice + the assumed K=2G? The corpus's "all one object" framing may itself slightly overclaim. Recorded open per the trigger; **does not block this landing.**

*(Separate symbol collision worth flagging: ν_vac is also used for "Kinematic Network Mutual Inductance" ≈ 8.45×10⁻⁷ m²/s in Vol 0 — a different quantity entirely.)*

---

## §6 — Adjacent findings (flag-don't-fix; NOT edited by this audit)

1. **Arithmetic slip (2 sites).** "factor 7 = 1/ν_vac = 1/(2/7)" at `ave-bh-horizon-area-theorem.md:20` and `lattice-extreme-bh-rationality.md:77` is wrong — 1/(2/7) = 3.5, not 7. The correct relation is r_sat/r_s = 7/2 = 3.5 = 1/ν_vac; the "7" is r_sat in units of GM/c² (7GM/c²), **not** 1/ν_vac. Flagged for a separate fix.
2. **`clm-ir8h78` intra-claim tension.** r_sat=7GM/c² (ε₁₁=1, shear+bulk gauge) vs r_s=2GM/c² (ε₁₁=1, GW/EM gauge) — two radii for ε₁₁=1 in different gauges. The channel-split is canonical (r_s = EM/transverse horizon, r_sat = shear+bulk rupture), but the "ε₁₁=1 at both" phrasing reads as a tension worth a clarifying note.

---

## §7 — Classification

- **consistency-vs-emergence:** the GR-recovering BH observables (ringdown 18/49, Q=ℓ, Hawking T_H) are **CONSISTENCY** (<2% recovery of GR at zero free parameters); the **AVE-distinct** content is the 2/7-compactness + 7GM Iron-Kα inner edge + Γ_shear=−1 echoes (matter/shear falsifiers).
- The verdict is an **evidence-framing / honesty** correction (u₀\* asserted, not derived) — **not** a new physics claim. No clm is retired; the magic-angle lock K=2G and ν_vac=2/7 stand firm; only the "u₀\* derived" *framing* is retracted to "asserted/back-fit, underdetermined."

---

*Auditor gate: this doc is to be verified against the audit verdict — that every retract-header matches "u₀\*≈0.187 asserted/back-fit, underdetermined", that no honest joint-constraint site was over-retracted, and that the BH forward-test + 2/7-homonym framings are recorded (not resolved).*
