# R3 — Lattice Decoration Discriminator (Result)

**Pre-reg:** `research/2026-06-11_lattice-decoration-discriminator_prereg.md`
**Driver:** `src/scripts/vol_1_foundations/lattice_decoration_discriminator.py`
**Artifact:** `assets/sim_outputs/r3_lattice_decoration_discriminator.json`
**Class:** consistency-class (Arm 3 κ channel) + replication-class (Arms 1–2)

---

## Summary

Three-arm battery executed. **D1 PARTIAL BIN: D1-A** — structural srs chirality is not replaceable by κ decoration at the R3-P5 magnitude gate (ρ ≈ 0.057% of srs Bishop rate). Decoration **does** flip sign with κ (substrate-distinct pairing with Arm 1 κ=0 still pending Phase-1 P4/P6 for full D1).

---

## Numbers (L=6)

| Arm | Observable | Value |
|-----|------------|-------|
| srs-R | writhe | −4.08672e−02 |
| srs-L | writhe | +4.08672e−02 |
| diamond | writhe | 0 |
| srs-R | Bishop Δθ/L | +75.462°/unit |
| srs mirror | Bishop Δθ/L | −75.462°/unit |
| diamond z-line | Bishop Δθ/L | 0 |
| κ=0 | decoration Δproxy | 0 |
| κ=+κ_e | decoration Δproxy | −7.52e−04 |
| κ=−κ_e | decoration Δproxy | +7.51e−04 |
| ρ (decoration/srs) | | **5.71×10−4** |

---

## Gates

| Gate | Result |
|------|--------|
| R3-P1 writhe replay | **PASS** |
| R3-P2 Bishop mirror-odd | **PASS** |
| R3-P3 Arm3 writhe null | **PASS** |
| R3-P4 κ=0 null | **PASS** |
| R3-P5 κ reproduces ≥20% srs | **FAIL** (ρ=0.057%) |

---

## D1 partial bin: **D1-A**

Per prereg §7: R3-P5 FAIL + Arms 1–2 pass → decoration cannot mimic structural channel at this gate; **evidence toward srs-as-substrate**, not a final ruling (Phase-1 P4/P6 still required).

---

## Honest limitations

1. Arm 3 O3 uses **κ-increment on Beltrami ω** (Op14 asymmetric kernels), not Bishop geometry — κ does not move diamond nodes; writhe stays 0.
2. Decoration increment sign-flips with κ but magnitude is **~500× smaller** than srs Bishop rate — D1-B falsified at R3-P5 threshold.
3. Full vector-TLM Phase-1 may shift magnitudes; R3 does not substitute for P4/P6.

---

## Next

1. Grant freeze Phase-1 thresholds (no framing pick).
2. Phase-1 P4 (`κ=0` ablation) + P6 (precursor genesis) on all arms.
3. D1 adjudication memo after Phase-1 bins.
