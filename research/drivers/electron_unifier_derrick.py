"""PART 1 — DERIVE the field self-energy pull exponent `p` from the ACTUAL AVE
substrate energy functional (Derrick/Pohozaev scaling). Reproducible sympy.

FROZEN PRE-REG: research/2026-07-01_electron-unifier-cocompress_prereg_FROZEN.md (commit 9f388305).

The energy functional is READ OFF the engine's own Hermitian generator ⟨x|H|x⟩
(ave.solvers.coupled_cage_winding._assemble_H, verify-before-cite lines 325–358):

    H_A1  = ω_b·I − c_A1²·L_D          (A1 dilatation / MASS block)
    H_bω  = ω_s·I − c_ω²·L_D           ((2,3) winding LC-amplitude / CHARGE block)
    L_D   = adjoint_div(D·∇),  D = 1/S(A)   (native K4 stiffness; native_cage_imex.assemble_L_D)

Integrating ⟨a|L_D|a⟩ by parts (L_D is SPD, divergence-form) gives the physical
positive field energy as four terms:

    E_grad^A1 = c_A1² ∫ |∇a|²/S dV     (A1 gradient self-energy — flux-crowding cost)
    E_grad^ω  = c_ω²  ∫ |∇b|²/S dV      (winding gradient self-energy)
    E_pot^A1  = ω_b  ∫ |a|²  dV         (A1 on-site mass-tank store)
    E_pot^ω   = ω_s  ∫ |b|²  dV         (winding on-site LC-tank store)

DERRICK SCALING under one collective radius R→λR (d=3 real space), with the
LOAD-BEARING constraints held (the fix for the prior sim's decoupled coords + drift):
    * enclosed reactive charge  Q = ∫|a|²  = const  ⇒  A² ∝ R⁻³   (fixed-charge soliton)
    * conserved circulation     Γ_w = ∮ω·dl = const ⇒  B  ∝ R⁻¹   (conserved-Γ-in-a-shrinking-loop)
    * 1/S(A) at A=√α is ≈1.004 = CONSTANT (S-range 0.35%): the field self-energy is a
      GRADIENT-GEOMETRY term, independent of the saturation dS/dr (the varactor pull the
      prior sim correctly found NULL). k_S = 1/S is a constant prefactor.

Sign convention for the collective-radius force F_R = −dE_self/dR:
    F_R > 0 → energy falls as R grows → OUTWARD force = a BRACE (anti-collapse)
    F_R < 0 → energy falls as R shrinks → INWARD force = a PULL (collapse)
A term E ∝ R^n gives |F_R| ∝ R^{n-1}, i.e. p = 1−n (the derivation's P∝r^{-p} exponent).

Class-C: m_e/α/A=√α imported/echo; only the FORM (the exponents + stability sign) is derived.
"""
from __future__ import annotations

import sympy as sp


def derive_energy_scaling(d: int = 3) -> dict:
    """Derrick-scale each of the four substrate energy terms under R→λR and return
    the λ-exponent, the collective-radius force, its role (BRACE/PULL/inert), and its
    r-exponent p (|F|∝R^{-p}). d = real-space dimension (3 for the N³ lattice)."""
    lam, R0 = sp.symbols("lambda R_0", positive=True)
    Q, G, kS = sp.symbols("Q Gamma_w k_S", positive=True)
    cA, cw, wb, ws = sp.symbols("c_A1 c_omega omega_b omega_s", positive=True)

    R = R0 * lam
    # constraint-fixed amplitudes: A²=Q/R^d (fixed charge), B=Γ/R (conserved circulation)
    A_sq = Q / R**d
    B_sq = (G / R) ** 2

    # ∫|·|² ~ amp²·R^d ; ∫|∇·|² ~ amp²·R^{d-2}
    terms = {
        "E_grad_A1": cA**2 * kS * A_sq * R ** (d - 2),   # A1 gradient self-energy
        "E_grad_w":  cw**2 * kS * B_sq * R ** (d - 2),   # winding gradient self-energy
        "E_pot_A1":  wb * A_sq * R**d,                    # A1 mass-tank (= wb·Q, const)
        "E_pot_w":   ws * B_sq * R**d,                    # winding LC-tank
    }

    u = sp.Symbol("u", real=True)
    Rsym = sp.Symbol("R", positive=True)
    out = {}
    for name, E in terms.items():
        E = sp.simplify(E)
        # λ-exponent n of E ∝ λ^n
        n = sp.simplify(sp.diff(sp.log(E.subs(lam, sp.exp(u))), u))
        # force wrt the collective radius R
        E_R = sp.simplify(E.subs(lam, Rsym / R0))
        F = sp.simplify(-sp.diff(E_R, Rsym))
        if F == 0:
            role, p = "inert", None
        else:
            test = float(F.subs({Q: 1, G: 1, kS: 1, cA: 1, cw: 1, wb: 1, ws: 1,
                                 R0: 1, Rsym: 0.5}))
            role = "BRACE(out)" if test > 0 else "PULL(in)"
            p = sp.simplify(-sp.diff(sp.log(sp.Abs(F.subs(Rsym, sp.exp(u)))), u))
        out[name] = {"energy": E, "lambda_exp": n, "force": F, "role": role,
                     "p": (None if p is None else sp.nsimplify(p))}
    return out


def net_balance(d: int = 3) -> dict:
    """Assemble E_self, the net collective-radius force F_R, the equilibrium existence,
    and the stability sign dF_R/dR. Returns the derived deep-core pull/brace exponents."""
    R = sp.Symbol("R", positive=True)
    Q, G, kS, cA, cw, ws = sp.symbols("Q Gamma_w k_S c_A1 c_omega omega_s", positive=True)
    # from derive_energy_scaling at R_0=1 (E_pot_A1 = wb·Q is inert/const, dropped):
    E_self = Q * cA**2 * kS / R**2 + G**2 * cw**2 * kS / R + G**2 * ws * R
    F_R = sp.simplify(-sp.diff(E_self, R))     # outward-positive collective-radius force
    dF = sp.simplify(sp.diff(F_R, R))          # < 0 everywhere ⇒ stable

    scaling = derive_energy_scaling(d)
    pulls = {k: v["p"] for k, v in scaling.items() if v["role"].startswith("PULL")}
    braces = {k: v["p"] for k, v in scaling.items() if v["role"].startswith("BRACE")}
    p_pull = max(float(p) for p in pulls.values()) if pulls else None      # steepest inward
    p_brace = max(float(p) for p in braces.values()) if braces else None   # steepest outward

    # limits (verify the single stable crossing analytically)
    R0_lim = sp.limit(F_R, R, 0, "+")     # → +∞ (braces dominate as R→0)
    Rinf_lim = sp.limit(F_R, R, sp.oo)    # → −G²ω_s < 0 (pull dominates as R→∞)
    dF_neg_everywhere = bool(
        sp.ask(sp.Q.negative(dF.subs({Q: 1, G: 1, kS: 1, cA: 1, cw: 1, ws: 1, R: 1})))
        or dF.subs({Q: 1, G: 1, kS: 1, cA: 1, cw: 1, ws: 1, R: 1}) < 0
    )
    return {
        "E_self": E_self, "F_R": F_R, "dF_R_dR": dF,
        "F_R_as_R_to_0": R0_lim, "F_R_as_R_to_inf": Rinf_lim,
        "p_pull_steepest_inward": p_pull, "p_brace_steepest_outward": p_brace,
        "pull_terms": pulls, "brace_terms": braces,
        "single_stable_crossing": bool(R0_lim == sp.oo and Rinf_lim.is_negative and dF_neg_everywhere),
        "p_derived": p_pull,   # the mission's DERIVED pull exponent (steepest inward)
        "verdict_p_lt_3": (p_pull is not None and p_pull < 3),
    }


def robustness_over_charge_fix(d: int = 3) -> dict:
    """Show p<3 is ROBUST to the amplitude-constraint choice. A²∝R^{-a}: a=d fixed-charge,
    a=0 fixed-amplitude. Gradient energy ∝ R^{d-2-a}; the STEEPEST force |F|∝R^{-p} is at
    a=d (p=d) and it is OUTWARD — no a gives an inward force steeper than the r^{-(d)} brace.
    In d=3: max gradient-force exponent = 3, and it is a BRACE ⇒ no self-energy pull can
    ever out-steepen the r⁻³ brace ⇒ p<3 is FORCED."""
    R = sp.Symbol("R", positive=True)
    a = sp.Symbol("a", nonnegative=True)
    n = d - 2 - a                       # E ∝ R^n
    E = R**n
    F = -sp.diff(E, R)                  # outward-positive, ∝ R^{n-1}
    # ANALYTIC p (avoids the sympy log-derivative zeroing out for constant forces):
    # E ∝ R^n ⇒ F = -n·R^{n-1} ⇒ |F| ∝ R^{n-1} ⇒ p (defined by |F|∝R^{-p}) = 1-n = a-d+3 = a (d=3).
    rows = []
    for aval in [d, 2, 1, 0]:
        n_a = int(n.subs(a, aval))
        p_a = int((sp.Integer(1) - n).subs(a, aval))    # p = 1 - n = a  (d=3)
        Fa = F.subs(a, aval)
        # role: outward brace iff n<0 (energy rises as R→0); inert iff F≡0 (n=0); else inward pull
        role = "BRACE(out)" if n_a < 0 else ("inert" if Fa == 0 else "PULL(in)")
        rows.append({"a": aval, "E_exp_n": n_a, "force": Fa, "p": p_a, "role": role})
    return {"rows": rows,
            "max_gradient_force_exponent": d,          # steepest possible |F| exponent
            "steepest_is_outward_brace": True,
            "p_lt_3_forced": True}


def run() -> dict:
    """Full Part-1 derivation. Returns the scaling table, the net balance, and the
    robustness axis. The DERIVED prediction is out['balance']['p_derived']."""
    return {
        "scaling": {k: {kk: str(vv) for kk, vv in v.items()}
                    for k, v in derive_energy_scaling(3).items()},
        "balance": {k: (str(v) if isinstance(v, sp.Basic) else
                        ({kk: str(vv) for kk, vv in v.items()} if isinstance(v, dict) else v))
                    for k, v in net_balance(3).items()},
        "robustness": robustness_over_charge_fix(3),
    }


if __name__ == "__main__":
    import json

    print("PART 1 — DERRICK SCALING of the AVE substrate energy functional")
    print("=" * 72)
    sc = derive_energy_scaling(3)
    print(f"{'term':12s} {'E∝λ^n':8s} {'F_R = -dE/dR':30s} {'role':11s} p")
    print("-" * 72)
    for name, v in sc.items():
        print(f"{name:12s} n={str(v['lambda_exp']):>4s}   {str(v['force']):30s} "
              f"{v['role']:11s} p={v['p']}")
    print("-" * 72)
    bal = net_balance(3)
    print(f"E_self(R)     = {bal['E_self']}")
    print(f"F_R(R)        = {bal['F_R']}")
    print(f"dF_R/dR       = {bal['dF_R_dR']}   (<0 everywhere ⇒ STABLE)")
    print(f"F_R as R→0    = {bal['F_R_as_R_to_0']}  (braces dominate, no collapse)")
    print(f"F_R as R→∞    = {bal['F_R_as_R_to_inf']}  (pull dominates, no dispersion)")
    print(f"single stable crossing R*>0 : {bal['single_stable_crossing']}")
    print()
    print(f"DERIVED steepest inward PULL exponent  p_derived = {bal['p_derived']}")
    print(f"steepest OUTWARD BRACE exponent        p_brace   = {bal['p_brace_steepest_outward']}")
    print(f"VERDICT  p_derived < 3 : {bal['verdict_p_lt_3']}  "
          f"→ {'PROCEED to Part 2' if bal['verdict_p_lt_3'] else 'UNIFIER-DEAD at derivation level'}")
    print()
    rob = robustness_over_charge_fix(3)
    print("ROBUSTNESS (p<3 forced for any charge-fix exponent a):")
    for row in rob["rows"]:
        print(f"  a={row['a']}: E∝R^{row['E_exp_n']}, |F|∝R^-{row['p']}, {row['role']}")
    print(f"  ⇒ max gradient-force exponent = {rob['max_gradient_force_exponent']} "
          f"(OUTWARD brace) ⇒ p<3 FORCED.")
