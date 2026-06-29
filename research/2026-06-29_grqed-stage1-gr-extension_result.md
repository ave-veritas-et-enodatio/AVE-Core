# RESULT — Stage-1 GR-Extension: the Saturating-Modulus Correction on the Linear GR Core

**Date:** 2026-06-29 · **Lane:** implementer · **Branch:** `analysis/grqed-stage1-gr-extension`
**Status:** Stage-1 increment landed (code + two-test doctrine + clip-independence gate; both test lanes green)
**Scope:** A saturating-modulus correction ON the inherited GR (elastic-Poisson) solver — the FIRST
increment of the GR/QED-extension engine. The inherited linear core is the weak-field limit and is NOT
re-derived here.

---

## 0 · One-paragraph summary

The vacuum is a real saturable elastic medium. The inherited linear core — elastic-Poisson
$-(c^4/7G)\nabla^2\varepsilon_{11}=T_{00}\Rightarrow\varepsilon_{11}=7GM/c^2r$, $n=1+(2/7)\varepsilon_{11}$
— is the **weak-field limit**. Stage-1 adds a **saturating modulus** to the elliptic operator,
$-\nabla\!\cdot[(c^4/7G)\,D(A)\,\nabla\varepsilon_{11}]=T_{00}$ with $A=\varepsilon_{11}/\varepsilon_{yield}$
($\varepsilon_{yield}=1$), $D=1/S(A)$, and the **one** canonical Op14 kernel $S(A)=(1-A^2)^{1/2}$ (REUSED,
not minted). The bulk channel **stiffens** ($D=1/S\to\infty$ at $A=1$, halting the collapse); the shear
channel **softens** ($c_{shear}=c_0\sqrt S\to0$, a derived projection); EM stays **matched**
(`refractive_index()` untouched, spectator). Both two-test-doctrine legs pass — recover-the-known
(consistency) at $r\gg r_{sat}$ and activate-at-the-extreme (manifestation) at $r_{sat}=3.5\,r_s$ — and the
**load-bearing clip-independence gate PASSES**: the yield-shell radius and the integrated source $M_{eff}$
are bit-identical across $S_{min}\in[10^{-4},10^{-2}]$, so the yield-physics (not the numerical clamp) set
the wall.

**Honest framing (do NOT overclaim):** the point singularity is **replaced by a strain-saturated SHELL** at
$r_{sat}=3.5\,r_s$; the density **still diverges** there ($\rho_{eff}=\rho_0/S^3\to\infty$). True removal
needs the yield→rupture→genesis physics (a separate frontier). The strain-cap here is a numerical clip, NOT
modeled yield-physics. This is **RELOCATION** of the singularity to a shell, not regularization / removal of
the infinity.

---

## 1 · Spec (what was built)

## 2 · Substrate-native-check (walked before numerical code)

## 3 · Code delivered (file:line)

## 4 · Test 1 — RECOVER-THE-KNOWN (consistency-class)

## 5 · Test 2 — ACTIVATE-AT-THE-EXTREME (manifestation-class)

## 6 · ★ LOAD-BEARING GATE — clip-independence verdict

## 7 · Honesty — the singularity is RELOCATED, not removed

## 8 · How this integrates: GR's linear core + the saturating-modulus shell

## 9 · Honest flags + spec deviations
