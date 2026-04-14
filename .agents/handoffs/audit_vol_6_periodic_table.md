# Audit Results: Volume 6 - Periodic Table (IP Migration Plan)

## Scope Covered
- `manuscript/vol_6_periodic_table/chapters/*`
- `manuscript/vol_6_periodic_table/figures/*`
- `manuscript/vol_6_periodic_table/simulations/*`
- `manuscript/vol_6_periodic_table/main.tex`

## Tier 1: Hygiene & Mechanical Checks
**Status: Pass**
- The chapter structures correctly load the individual Circuit Elements up to Iron. Standard formatting is maintained.

## 🚨 Tier 2: Mathematical Rigor & "Sci-Fi" Scrub / Hardware IP 🚨
**Status: Hardware SPICE Netlists Discovered**
- While the TeX manuscript chapters themselves were brilliantly clean—focusing purely on atomic RF circuits and radioactive decay without invoking spacecraft or "thrust"—the `simulations/` directory contained explicit APU testbench configurations.

These files have been earmarked for direct migration out of the public repo to the private `AVE-APU` hardware stack:

### 1. `simulations/spice_netlists/ponder_01_c12_emitter.cir`
- **Line 1:** `* Applied Vacuum Engineering - PONDER-01 Testbench`
*Migration Recommendation:* Move this entire file to the hardware repository. It connects the Carbon-12 topological circuit specifically to the proprietary macroscopic PONDER-01 macroscopic thrust testbench.

### 2. `simulations/spice_netlists/ponder_01_he4_emitter.cir`
- **Line 1:** `* Applied Vacuum Engineering - PONDER-01 Testbench`
*Migration Recommendation:* Move this entire file to the hardware repository. Similar mapping of Helium-4 to the PONDER-01 array bounding limits.

### 3. `simulations/spice_netlists/dt_fusion_transient.cir`
- **Line 20:** `* V_PONDEROMOTIVE provides the kinetic forcing required to overcome 1/d repulsion`
*Migration Recommendation:* This netlist should likely remain in the public core because DT Fusion is standard physics, but the variable named `V_PONDEROMOTIVE` should be scrubbed and renamed to `V_KINETIC` to sever ties with the APU thrust taxonomy.

---
**Summary:** The periodic table documentation is rock solid. The only action required is excising the two `ponder_01` SPICE netlist files that bridge the atomic topologies to the proprietary macroscopic thruster.
