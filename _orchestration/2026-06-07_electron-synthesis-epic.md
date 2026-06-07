# Electron-structure synthesis — workstream epic (2026-06-07)

Stages the follow-ups from the 2026-06-07 deep co-thinking session so the big ones survive compaction. The session built a unified electron picture; this tracks deliverables, the emergence-test candidates, the α-closure thread, and the demo/viz candidates.

## §0 The synthesis (one paragraph)
Electron = a frictionless B-rotor loop orbiting ONE host K4 node (host = the loop's axis), body interstitial (Meissner-expelled, can't touch nodes — maglev), tensioned by its chiral neighbors. **Strain** (not E/B) is fundamental; `E↔node-shunt-C`, `B↔bond-series-L`. Mass `=½LI²` (rotor reactive energy `=ℏω_C`). Spin-½ = chiral neighbor tension imparting a ½-twist (holonomy π) per orbit (the double-cover). `(2,3)` = the real-space **trefoil projection** of the twisted orbit (the phase-space winding's shadow). Charge = the E terminating on the host node. Confinement = the self-dug Meissner cage. Coherence (qubit) = the frictionless rotor; decoherence = the cage leak (**candidate: α**).

## §1 Running deliverables (3 background docs)
- **rotor-synthesis** (`a7f46b8c`) — structure + rotor=zitter & spin-stabilizes proofs. **On land: fold in the fine-structure-tidal forward-prediction (§7).**
- **coherence-Reynolds** (`a0b1b8a8`) — qubit/Cooper/classical `Re_q` map + CFD/Vacuum-Fluid-Dynamics. **On land: reframe §5 — VFD = Vacuum Fluid Dynamics; variable-freq-drive demoted to motor sub-lens.**
- **chiral-holonomy diagnostic** (`a7467a52`) — the ½-twist test (is holonomy π?) + viz #1/#6.
Each → fold-ins → **reviewed PR** (no self-merge, no leaf without Grant).

## §2 Emergence-test candidates (the "does it have teeth?" list)
The synthesis is mostly consistency-class re-description. The genuine emergence candidates (testable *numbers*, not re-descriptions):
1. **Holonomy = π** (running, `a7467a52`) — does chiral geometry yield spin-½? Robust/topological π = emergence.
2. **Fine structure from tidal spin-orbit** (queued, rotor-doc §7) — rotor-resolved atom generates `L·S` splitting with no term inserted.
3. **`Re_q` → decoherence rate** (coherence-doc §5) — does the quantum Reynolds number predict a coherence-time number?
4. **α-closure** (§3) — the big one.

## §3 α-closure thread (BIG follow-up — STAGED, not dispatched)
**Q (Grant): does the rotor-cage-leak picture close or justify α?**
- **Justifies — yes:** α = electron rotor's intrinsic **leak rate into its Meissner cage** = `1/Q` = London-depth coupling = decoherence rate. Grounded in `Q=1/α` (theorem-3-1-q-factor).
- **Closes — candidate path, NOT solved:** α is currently a CALIBRATION INPUT; the corpus `p_c=8πα` chain is **CIRCULAR** (`p_c` defined via α). New path: derive `Q=1/α=137` from the **chiral-cage geometry** (holonomy + London depth + packing), *independent of α*. If geometry → 137, α closed non-circularly (first time).
- **First steps (when adjudicated):** (a) **VERIFY** whether `Q=1/α` is DERIVED (geometric, α-independent) or ASSERTED (`Q≡1/α` definition → circular) in theorem-3-1 — gates viability; (b) extend the holonomy diagnostic to compute the cage **leak** (London-depth coupling / the Q) from geometry — does it give ~137?
- **Honesty (`ave-evidence-framing`):** deriving 137 has eluded everyone. The picture makes the closure WELL-POSED (compute the cage leak), it does NOT solve it. High-value, high-risk. Do NOT overclaim in any doc.

## §4 Demo + visualization candidates
- Viz candidates (9, ADJ/POST): [`2026-06-07_visualization-candidates.md`](2026-06-07_visualization-candidates.md).
- **Physical lab demo (Grant):** RGB LED strip on a loop, color-cycling as it rotates — demonstrates the rotor + the **720° double-cover** (color returns only after *two* rotations = the spinor) + the trefoil path. Save for a lab demo. Added to viz file as #10.

## §5 Open forks + next
- Genesis forks A–D (genesis-scope §9) still open.
- New physics forks: does neighbor coordination **select the ground-state knot** (trefoil=electron, higher-crossing=heavier)? Is the holonomy **topologically** π? Does the cage leak **= α**?
- **Next:** land the 3 docs → fold-ins → PRs. **Watch the holonomy verdict first** (cleanest emergence test). Then adjudicate whether α-closure earns a dedicated derivation push (gated on the `Q=1/α` derived-vs-asserted check).
