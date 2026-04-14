# Audit Results: Volume 3 - Macroscopic (IP Migration Plan)

## Scope Covered
- `manuscript/vol_3_macroscopic/chapters/*`
- `manuscript/vol_3_macroscopic/main.tex`

## Tier 1: Hygiene & Mechanical Checks
**Status: Pass**
- Volume 3 handles Cosmology and Thermodynamics. All latex dependencies are structurally sound and cleanly separated.

## Tier 2: Mathematical Rigor & "Sci-Fi" Scrub
**Status: Pass**
- The text continues to use macroscopic electrical engineering metaphors appropriately (e.g., in `13_geophysics.tex`: "The Earth is a highly conductive rotor sweeping through the Sun's magnetic AC stator field..."). Because this is formally used to explain Geodynamo principles rather than proposing a thrust system or spaceship, it remains within the threshold of rigorous Effective Field Theory.

## 🚨 Hardware IP Identified for Migration 🚨
### 1. `manuscript/vol_3_macroscopic/chapters/21_black_hole_interior_regime_iv.tex`
Lines 27-28 contain stray references to the restricted APU test vehicle taxonomy:
```latex
\item \textbf{Regime II:} BCS at $T/T_c \approx 0.5$, PONDER-05 at 30~kV.
\item \textbf{Regime III:} BCS near $T_c$, PONDER-05 at 43~kV.
```

*Recommendation:* Extract these "PONDER-05" string references to the hardware/APU repository documentation. For this public core repository, these should be generalized alongside the BCS references:
```latex
\item \textbf{Regime II:} BCS at $T/T_c \approx 0.5$, Asymmetric Active Capacitor at 30~kV.
\item \textbf{Regime III:} BCS near $T_c$, Asymmetric Active Capacitor at 43~kV.
```
