# Step 4 — (2,3) Torus-Knot Selection as the Electron Topology

**Status:** DERIVATION. Step 4 of the two-node-electron derivation
plan (§19 of plan file). Depends on Steps 1+3 (K4 rotation action +
single-bond LC = ω_Compton).

**Goal:** derive WHY the electron's phase pattern is specifically
`(p, q) = (2, 3)`, not `(1, 1)`, `(2, 5)`, `(3, 5)`, or any other
torus-knot winding.

**Falsification criterion:** if the analysis predicts `(1, 1)` or
some other low-(p, q) winding as the electron's stable topology, the
identity electron ↔ (2,3) trefoil is wrong. Hypothesis fails.

**Result:** **CONFIRMED.** (2, 3) is the smallest non-trivial coprime
torus knot, with the lowest crossing number (c=3) of any non-trivial
knot. Coprimality is required for a connected single-component knot
(not a link). Both windings ≥ 2 is required for non-trivial winding
in both directions. (2,3) is uniquely the LIGHTEST stable particle
of the lepton family — i.e., the electron.

---

## §1 The torus-knot family on K4

A `(p, q)` torus knot is a closed curve on a torus `T² = S¹ × S¹`
that wraps `p` times around the toroidal direction (major axis) and
`q` times around the poloidal direction (minor axis). On the K4
substrate, this corresponds to a closed flux-tube loop with phase
winding `θ(t) = pφ(t) + qψ(t)` where `φ, ψ` are the toroidal and
poloidal angles.

Topological characterization:
- **Coprimality `gcd(p, q) = 1`:** required for the path to close
  as a single loop (a true KNOT, not a multi-component LINK).
- **Crossing number** `c(p, q) = min(p(q-1), q(p-1))`: the minimum
  number of self-crossings in any planar projection.
- **Hopf invariant** `Q_H = p · q`: the linking number with itself.
- **Self-linking** `SL = pq - p - q`: Seifert-framing self-link.

## §2 Enumerating low-(p, q) candidates

| (p, q) | gcd | c | Q_H | SL | Topology |
|---|---|---|---|---|---|
| (1, 0) | — | 0 | 0 | — | trivial — single straight loop |
| (1, 1) | 1 | 0 | 1 | -1 | unknot — closed loop, no knotting |
| (1, n) | 1 | 0 | n | n-2 | unknot — n=2,3,... still unknot |
| (n, 1) | 1 | 0 | n | n-2 | unknot — same as (1,n) by symmetry |
| (2, 2) | 2 | 2 | 4 | 0 | composite link, NOT a single knot |
| **(2, 3)** | **1** | **3** | **6** | **1** | **trefoil — smallest non-trivial knot** |
| (3, 2) | 1 | 3 | 6 | 1 | trefoil mirror — same knot type |
| (2, 5) | 1 | 5 | 10 | 3 | (2,5) torus knot (cinquefoil) |
| (3, 4) | 1 | 8 | 12 | 5 | (3,4) torus knot |
| (3, 5) | 1 | 10 | 15 | 7 | (3,5) torus knot |
| (3, 7) | 1 | 14 | 21 | 11 | (3,7) torus knot |

**Observation:** (2, 3) is the SMALLEST coprime pair with both
windings ≥ 2. It has the LOWEST crossing number (c = 3) of any
non-trivial knot.

## §3 Why both p, q ≥ 2 (non-trivial in both directions)

For (1, n) or (n, 1): one of the windings is 1, meaning the loop
goes around that direction only ONCE. No self-crossings (c = 0).
This is topologically equivalent to the UNKNOT — a circle. The
unknot has zero topological charge in the Hopf-invariant sense
(`Q_H = 1` only because of the trivial single self-linkage).

For a NON-TRIVIAL topological structure (a true knot), we need
both `p ≥ 2` AND `q ≥ 2`. This is a basic knot-theoretic fact.

## §4 Why coprime gcd(p, q) = 1

If `gcd(p, q) = d > 1`, the curve doesn't close after one cycle of
the parameter `t ∈ [0, 2π)`; instead it closes after `t ∈ [0, 2π/d)`
and is a `d`-component LINK (multiple disjoint loops linked
together). For a SINGLE-COMPONENT closed loop (true knot), `gcd = 1`
is required.

This rules out (2, 2), (3, 3), (2, 4), (4, 2), (3, 6), etc.

## §5 The smallest non-trivial coprime torus knot is (2, 3)

Combining §3 + §4: both windings ≥ 2 AND coprime.

Smallest pairs:
- (2, 3): smallest with both ≥ 2 and coprime → **trefoil**, c = 3
- (2, 5): next smallest (skipping (2,4) which has gcd=2) → cinquefoil, c = 5
- (3, 4): next → c = 8
- (3, 5): next → c = 10

(2, 3) is uniquely the SMALLEST and SIMPLEST non-trivial torus knot.

## §6 Why the electron is (2, 3)

The electron is the **lightest stable particle of the lepton family**
(stable charged matter at rest). It's the GROUND STATE of charged
fermionic matter.

In the AVE topological-soliton framework:
- Lighter particle = simpler topology = lower-energy stable bound state
- The electron = simplest non-trivial topological knot supporting
  charge + spin-½ + non-trivial linking

**The simplest non-trivial torus knot is (2, 3).** Therefore the
electron MUST be (2, 3) — it's the only assignment consistent with
"electron = lightest non-trivial stable lepton."

This matches:
- Vol 1 Ch 8 explicitly identifies the electron as the trefoil (3₁)
- AVE-HOPF antenna predictions use (2, 3) for the electron
- The crossing count c = 3 matches AVE-HOPF's δ_CP and chirality
  derivations for electron-like topology

## §7 The lepton family extension

If electron = (2, 3), the next stable lepton-family torus knots
should be the next-smallest non-trivial coprime (p, q):

| Lepton candidate | (p, q) | c | Mass scale (predicted via Hopf?) |
|---|---|---|---|
| Electron | (2, 3) | 3 | ~ 0.511 MeV (measured) |
| Muon? | (2, 5) | 5 | ~ ? |
| Tau? | (3, 4) or (3, 5) | 8 or 10 | ~ ? |

The exact mass-from-(p,q) derivation is in Vol 2 (lepton mass spectrum
chapter) and isn't pursued here. The point: (2, 3) is the SIMPLEST
non-trivial torus knot, hence the electron's identity is forced if we
accept "electron = lightest stable lepton = simplest stable knot."

## §8 What this derivation establishes

1. **(2, 3) is uniquely the smallest non-trivial coprime torus knot**
   (gcd = 1, both ≥ 2, smallest sum p+q = 5).
2. **It has the lowest crossing number c = 3** of any non-trivial knot.
3. **It's the unique trefoil topology** (trefoil is THE simplest knot
   in all of knot theory).
4. **The electron MUST be (2, 3)** if we accept it's the lightest
   stable lepton with non-trivial topology.

This is a DERIVATION from basic knot-theoretic facts plus the
identification "electron = lightest stable non-trivial topological
soliton." The knot theory is standard math; the identification is an
AVE physical assertion.

## §9 What this does NOT prove

- Doesn't prove that the K4 substrate STABILIZES (2, 3) bound states
  dynamically (separate question for TLM evolution + crossing-mutual-L)
- Doesn't derive the ELECTRON MASS m_e from (2, 3) topology — only
  the topological IDENTITY of the electron
- Doesn't address why heavier leptons have specific (p, q) values
  (deferred to Vol 2 lepton-mass-spectrum chapter)

## §10 Falsification status

Step 4 PASSES. (2, 3) IS the smallest non-trivial coprime torus knot
by basic knot theory. The identification with the electron follows
from "electron = lightest stable non-trivial lepton."

The hypothesis predicting (1, 1), (1, 2), or (2, 2) as the electron
would have FAILED this analysis — those are unknots or composite
links, not true non-trivial knots. (2, 3) is the unique answer.

## §11 Files referenced

- [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) — electron as trefoil
- [`AVE-HOPF/scripts/beltrami_hopf_coil.py:43-53`](../../../AVE-HOPF/scripts/beltrami_hopf_coil.py#L43) — `harmonic_mean_winding`, `self_linking_number`, `crossing_number_torus_knot` utilities
- [`research/L3_electron_soliton/20_chirality_projection_sub_theorem.md`](20_chirality_projection_sub_theorem.md) — uses (2,3) for chirality derivation
- Standard knot theory: torus-knot crossing number `c(p,q) = min(p(q-1), q(p-1))` (Murasugi, *Knot Theory and Its Applications*)
