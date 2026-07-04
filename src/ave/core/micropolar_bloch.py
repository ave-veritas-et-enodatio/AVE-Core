#!/usr/bin/env python3
"""6-DOF (u, φ) micropolar Bloch dynamical matrix + long-wave elimination.

Stage 2 of the srs elastic-tensor arc (Grant-fired 2026-07-04). Prereg (FROZEN):
research/2026-07-04_srs-chiral-micropolar_prereg_FROZEN.md.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (see prereg — stated before any standard term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : the FULL MICROPOLAR (Cosserat) sector of the chiral srs-z3 net. Per node
           6 DOF = 3 translational u + 3 micro-rotational φ. 8 Wyckoff-8a
           sublattices -> a 48x48 D(k). This is the sector Stage 1 integrated OUT.
           Each z=3 bond carries THREE blocks:
             (1) u<->u : Stage-1 Born tensor Phi_b = k_a*P + k_s*(I-P), P=d^(x)d^.
             (2) phi<->phi : couple-stress gamma*|phi_i-phi_j|^2 (bond curvature).
             (3) u<->phi : THE CHIRAL CROSS-COUPLING (object under test), BLIND two
                 ways (Grant ruling (c) 2026-07-04):
                   (a) GEOMETRY-FIXED LEVER-ARM (zero knobs): the bond attaches at a
                       point offset from the node center by lever arm b (Wyckoff-8a
                       offset + screw pitch). A node rotation phi displaces the
                       attachment by phi x b; the bond force through Phi_b then makes a
                       torque tau = b x f automatically. sigma^A-mediated channel.
                   (b) INDEPENDENT kappa_rot (swept knob): an explicit relative-rotation
                       spring on top of (k_a,k_s). mu-mediated (couple-stress) channel.
  REGIME : cold linear, sub-yield, saturation OFF. The 4_1 handedness enters the COLD
           tensor ONLY through bond GEOMETRY (the lever arm b), NOT kappa_chiral
           (saturation-only). So the chiral B pseudo-tensor is a GEOMETRIC-chirality
           effect of the non-centrosymmetric I4_1 32 point group.
  READOUT COORDS : real-space / spatial-Brillouin. A46-clean.
  CLASS  : CONSISTENCY. alpha-CLEAN, ratios only. NO tuning toward 2/7.

CANONICAL micropolar structure (trampoline-framework.md:185-200, VERIFIED at HEAD):
    rho u.. = div sigma + f
    I_w phi.. = div mu + 2 sigma^A + g          (coupled through sigma^A)
  sigma^A = antisymmetric stress = the moment-per-area that drives microrotation
  (trampoline:87). The lever-arm mechanism (a bond force with a moment arm makes the
  stress tensor asymmetric) is exactly the sigma^A source -> READING (a) is the
  substrate-native geometric channel; kappa_rot enters through mu -> READING (b).

METHOD (Born-Huang, one grade up). The force-constant Bloch matrix Phi(k) over the
6-DOF/node lattice is expanded around k=0. Phi0 has a 6-dim nullspace = 3 uniform
translations + 3 uniform rotations (the acoustic + the rotational-acoustic modes). We
eliminate the OPTIC (relative-sublattice) DOF AND (for the Cauchy-reduced tensor) the
micro-rotation DOF at O(k^2) via the Schur complement — this is the internal-strain
(Kleinman) relaxation, generalized to include the rotational back-reaction. The chiral
pseudo-tensor B lives in the Phi1 (linear-in-k) coupling between the translational and
the rotational subspaces; it is nonzero ONLY when the lattice is non-centrosymmetric.
"""

from __future__ import annotations

import numpy as np

# ---------------------------------------------------------------------------
# §1  Bond blocks (the three per-bond stiffness objects)
# ---------------------------------------------------------------------------
def _skew(v: np.ndarray) -> np.ndarray:
    """[v]_x : the 3x3 skew matrix with [v]_x @ w == v x w (cross product)."""
    return np.array([[0.0, -v[2], v[1]],
                     [v[2], 0.0, -v[0]],
                     [-v[1], v[0], 0.0]])


def bond_6dof_block(d, *, k_axial=1.0, k_shear=1.0, gamma=0.0, kappa_rot=0.0,
                    lever=0.0, reading="a"):
    """The 6x6-per-endpoint force-constant blocks of ONE directed bond i->j.

    DOF ordering per node: (u_x,u_y,u_z, phi_x,phi_y,phi_z).

    Physics (energy of the bond):
      U = 1/2 * Delta . Phi_b . Delta               (translational, Born)
        + 1/2 * gamma * |phi_j - phi_i|^2           (couple-stress, bond curvature)
        + 1/2 * kappa_rot * |phi_j - phi_i|^2        (reading (b) ONLY, swept knob)
      with Delta = (u_j + phi_j x b_j) - (u_i + phi_i x b_i)   [reading (a): lever!=0]
                 =  u_j            -  u_i             [reading (b): lever=0, pure Born u]

    LEVER ARM (reading (a), geometry-fixed). The bond attaches at a point offset from
    the node center by b = lever * (d/2) along the bond, i.e. the strut couples to the
    node at its physical attachment on the node surface, offset by the (geometry-fixed)
    lever fraction. b_i points ALONG +d/2 from node i (toward j); b_j points along -d/2
    from node j (toward i) -- both toward the bond midpoint, the physical attachment.
    A node micro-rotation phi displaces its attachment by phi x b; the Born force
    through Phi_b then makes a torque tau = b x f AUTOMATICALLY. NO new stiffness --
    the coupling constant is set by `lever` (geometry) and (k_a,k_s). This is the
    sigma^A-mediated (asymmetric-stress) channel. `lever` is FIXED by lattice geometry,
    NOT swept (verified geometry-fixed in the driver: lever = strut attachment fraction).

    kappa_rot (reading (b), independent knob). An explicit relative-micro-rotation
    spring carried ON TOP OF (k_a,k_s), structurally a torsional bond spring, SWEPT.
    Enters through the couple-stress (mu) modulus channel -- the independent-stiffness
    reading. In reading (b) we set lever=0 (no geometric cross-coupling) so kappa_rot
    is the ONLY u<->phi/phi source and the family-reduction, if any, is attributable to
    the swept knob (the 1/2-1/4 tell: a reduction that needs a tuned kappa_rot* is the
    import in a third costume).

    Returns dict of 3x3 sub-blocks keyed by (endpoint-pair, dof-pair):
      K_ii, K_ij, K_ji, K_jj  each 6x6, so the bond's contribution to the global
      force-constant matrix is  Phi[i,i]+=K_ii, Phi[i,j]+=K_ij, etc.
    """
    d = np.asarray(d, float)
    dn = d / np.linalg.norm(d)
    P = np.outer(dn, dn)
    Phi_b = k_axial * P + k_shear * (np.eye(3) - P)   # 3x3 translational Born tensor

    # lever arms (reading (a)): attachment offset from node center toward bond midpoint.
    if reading == "a":
        b_i = +0.5 * lever * d      # from node i toward j
        b_j = -0.5 * lever * d      # from node j toward i
    else:  # reading "b": no geometric cross-coupling
        b_i = np.zeros(3)
        b_j = np.zeros(3)

    Bi = _skew(b_i)   # phi_i x b_i = -[b_i]_x phi_i ... careful: phi x b = -(b x phi) = -[b]_x phi
    Bj = _skew(b_j)
    # attachment displacement of endpoint = u + phi x b = u - [b]_x phi = u + [ -[b]_x ] phi
    # Let A_i map node-DOF (u_i,phi_i) -> attachment displacement:  disp_i = u_i - Bi @ phi_i
    #   (since phi x b = -(b x phi) = -[b]_x phi = -Bi @ phi)
    # Delta = disp_j - disp_i.  U = 1/2 Delta.Phi_b.Delta.
    # Build the 6x6 endpoint blocks. Let J_i = [ I3 | -Bi ] (3x6): disp_i = J_i @ q_i.
    I3 = np.eye(3)
    Ji = np.hstack([I3, -Bi])     # 3x6
    Jj = np.hstack([I3, -Bj])     # 3x6

    # translational (Born through the lever): U = 1/2 (Jj q_j - Ji q_i).Phi_b.(Jj q_j - Ji q_i)
    # Hessian blocks:
    K_ii = Ji.T @ Phi_b @ Ji
    K_ij = -Ji.T @ Phi_b @ Jj
    K_ji = -Jj.T @ Phi_b @ Ji
    K_jj = Jj.T @ Phi_b @ Jj

    # couple-stress + kappa_rot: both act on (phi_j - phi_i), a 3x3 identity block in the
    # phi-phi corner. g_tot = gamma + (kappa_rot if reading b else 0).
    g_tot = gamma + (kappa_rot if reading == "b" else 0.0)
    if g_tot != 0.0:
        Gphi = g_tot * I3
        # U = 1/2 g (phi_j - phi_i)^2 -> phi-phi corner (rows/cols 3:6)
        K_ii[3:, 3:] += Gphi
        K_jj[3:, 3:] += Gphi
        K_ij[3:, 3:] += -Gphi
        K_ji[3:, 3:] += -Gphi

    return {"K_ii": K_ii, "K_ij": K_ij, "K_ji": K_ji, "K_jj": K_jj}


# ---------------------------------------------------------------------------
# §2  6-DOF micropolar Bloch force-constant matrix Phi(k)  (48x48 for srs)
# ---------------------------------------------------------------------------
def micropolar_phi(kvec, pos, bonds, *, k_axial=1.0, k_shear=1.0, gamma=0.0,
                   kappa_rot=0.0, lever=0.0, reading="a"):
    """The 6N x 6N Bloch FORCE-CONSTANT matrix Phi(k) (NOT mass-reduced).

    Same Bloch construction as Stage-1's cauchy_bloch_D / acoustic_christoffel `phi`,
    lifted to 6 DOF/node with the §1 bond blocks. `bonds` = list of (i,j,delta) directed
    minimum-image displacements. Hermitized. For a directed bond (i,j,d) we stamp:
        Phi[i,i] += K_ii,  Phi[j,j] += K_jj (via its own reverse listing),
        Phi[i,j] += K_ij * exp(i k.d).
    Because `bonds` lists BOTH directions (i->j with +d and j->i with -d), each
    undirected bond is stamped from both ends; we use the half-energy convention
    (each directed listing contributes half) to avoid double counting the on-site term.
    """
    n = len(pos)
    D = np.zeros((6 * n, 6 * n), dtype=complex)
    for (i, j, d) in bonds:
        blk = bond_6dof_block(d, k_axial=k_axial, k_shear=k_shear, gamma=gamma,
                              kappa_rot=kappa_rot, lever=lever, reading=reading)
        ph = np.exp(1j * np.dot(kvec, d))
        # MATCH Stage-1 srs_elastic_tensor `phi()` EXACTLY: each directed listing stamps
        # the FULL block (no half-energy factor). `bonds` is bidirectional; the final
        # Hermitization reproduces the standard lattice-dynamics Bloch form. M0 pins this.
        D[6 * i:6 * i + 6, 6 * i:6 * i + 6] += blk["K_ii"]
        D[6 * i:6 * i + 6, 6 * j:6 * j + 6] += blk["K_ij"] * ph
    return 0.5 * (D + D.conj().T)


def _acoustic_rotational_subspaces(n):
    """The 6-dim k=0 nullspace basis: 3 uniform translations + 3 uniform micro-rotations.

    Uniform translation along axis al: u=e_al at every node, phi=0.
    Uniform micro-rotation about axis al: phi=e_al at every node, u=0 (the COMPATIBLE
    macro+micro rotation; a rigid rotation of the whole crystal has u_node = theta x r
    AND phi=theta, but at k=0 the translational part is the uniform-u; the pure
    micro-rotation zero-mode is phi=e_al uniform). Both are exact zero-eigenvectors of
    Phi0 for any centro/non-centro lattice (a rigid body costs no energy).

    Returns Ea (6n x 6): columns 0-2 translation, 3-5 micro-rotation.
    """
    Ea = np.zeros((6 * n, 6), dtype=complex)
    for al in range(3):
        # uniform translation
        v = np.zeros(6 * n)
        v[al::6] = 1.0
        v /= np.linalg.norm(v)
        Ea[:, al] = v
        # uniform micro-rotation
        w = np.zeros(6 * n)
        w[3 + al::6] = 1.0
        w /= np.linalg.norm(w)
        Ea[:, 3 + al] = w
    return Ea


# ---------------------------------------------------------------------------
# §3  Long-wave expansion + Schur elimination -> effective Cauchy Gamma(q^)
#     and the chiral pseudo-tensor extraction
# ---------------------------------------------------------------------------
def micropolar_longwave(qhat, pos, bonds, *, k_axial=1.0, k_shear=1.0, gamma=0.0,
                        kappa_rot=0.0, lever=0.0, reading="a", rho=1.0, m=1.0,
                        h=1e-4, cross_coupling=True):
    """Long-wave (Born-Huang) reduction of the 6-DOF micropolar Phi(k) along q^.

    Returns a dict with:
      Gamma_cauchy (3x3)  : the effective TRANSLATIONAL acoustic matrix rho*c^2 with
                            BOTH the optic-translation AND the micro-rotation DOF
                            eliminated at O(k^2). Its eigenvalues are the Cauchy-reduced
                            acoustic slopes INCLUDING the chiral back-reaction.
      Gamma_no_rot (3x3)  : the same with the rotational sector NOT eliminated (rotation
                            clamped) -- the "cross-coupling OFF" baseline. The DIFFERENCE
                            Gamma_cauchy - Gamma_no_rot IS the rotational back-reaction.
      B_coupling (3x3)    : the chiral pseudo-tensor block = the LINEAR-in-k (Phi1)
                            coupling between the uniform-translation and uniform-rotation
                            acoustic subspaces, projected along q^. Nonzero ONLY for a
                            non-centrosymmetric lattice. Parity-odd (flips under
                            enantiomorph). Units: force-constant * length.
      sigmaA_weight, mu_weight : the channel diagnostic -- how much of B rides the
                            asymmetric-stress (lever, reading a) vs couple-stress (mu,
                            reading b) channel.

    METHOD. Phi(k) = Phi0 + k Phi1 + k^2 Phi2 along q^. Subspaces:
      A_t = uniform translation (3), A_r = uniform micro-rotation (3), O = optic (rest).
    Phi0 annihilates A_t and A_r (rigid modes). The effective 6x6 on (A_t,A_r), after
    eliminating the optic block O at O(k^2) (internal strain), is
      M6 = Phi2_aa - Phi1_ao Phi0_oo^{-1} Phi1_oa     (6x6, a in {A_t,A_r})
    M6 has the block form  [[M_tt, M_tr],[M_rt, M_rr]] where:
      M_tt = the clamped-rotation Cauchy matrix (Gamma_no_rot),
      M_tr = M_rt^T = THE CHIRAL COUPLING (translation<->rotation, linear-order in the
             O(k) coupling -> shows up here at O(k^2) after the optic elimination and
             the direct Phi1 t-r term),
      M_rr = the rotational stiffness (couple-stress + kappa_rot + lever back-stiffness).
    Integrating out the micro-rotation (which has NO k=0 restoring force -> relaxes to
    minimize energy given the strain) is the Schur complement:
      Gamma_cauchy = M_tt - M_tr M_rr^{-1} M_rt.
    The chiral pseudo-tensor B is read from M_tr directly (the parity-odd t-r block).
    """
    qhat = np.asarray(qhat, float)
    qhat = qhat / np.linalg.norm(qhat)
    n = len(pos)

    def phi(kv):
        return micropolar_phi(kv, pos, bonds, k_axial=k_axial, k_shear=k_shear,
                              gamma=gamma, kappa_rot=kappa_rot, lever=lever,
                              reading=reading)

    P0 = phi(np.zeros(3))
    Pp = phi(qhat * h)
    Pm = phi(-qhat * h)
    P1 = (Pp - Pm) / (2.0 * h)                      # dPhi/dk (antihermitian)
    P2 = (Pp - 2.0 * P0 + Pm) / (h ** 2) / 2.0      # (1/2) d^2Phi/dk^2

    Ea = _acoustic_rotational_subspaces(n)           # 6n x 6  (0-2 trans, 3-5 rot)
    # optic subspace = nonzero-eigenvalue eigenvectors of P0
    w0, U0 = np.linalg.eigh(P0)
    optic = U0[:, w0 > 1e-7 * max(1.0, w0.max())]

    Paa = Ea.conj().T @ P2 @ Ea                      # 6x6
    P1ao = Ea.conj().T @ P1 @ optic
    P0oo = optic.conj().T @ P0 @ optic
    P1oa = optic.conj().T @ P1 @ Ea
    M6 = Paa - P1ao @ np.linalg.inv(P0oo) @ P1oa
    M6 = 0.5 * (M6 + M6.conj().T)
    M6 = (rho / m) * M6.real

    M_tt = M6[:3, :3]
    M_tr = M6[:3, 3:]
    M_rt = M6[3:, :3]
    M_rr = M6[3:, 3:]

    Gamma_no_rot = M_tt.copy()                       # cross-coupling OFF (rotation clamped)

    # integrate out micro-rotation (Schur complement). M_rr may be singular if the
    # rotational sector has a soft direction (no couple-stress + no lever back-stiffness);
    # regularize with a pseudo-inverse in that case.
    if cross_coupling and np.linalg.norm(M_tr) > 0:
        try:
            Mrr_inv = np.linalg.inv(M_rr)
        except np.linalg.LinAlgError:
            Mrr_inv = np.linalg.pinv(M_rr)
        # guard: if M_rr is near-singular, pinv (the physical relaxed limit)
        if np.linalg.cond(M_rr) > 1e12:
            Mrr_inv = np.linalg.pinv(M_rr, rcond=1e-10)
        Gamma_cauchy = M_tt - M_tr @ Mrr_inv @ M_rt
    else:
        Gamma_cauchy = M_tt.copy()

    Gamma_cauchy = 0.5 * (Gamma_cauchy + Gamma_cauchy.T)

    # the chiral pseudo-tensor block (parity-odd t-r coupling), projected along q^.
    B_coupling = M_tr.copy()

    return {
        "Gamma_cauchy": Gamma_cauchy,
        "Gamma_no_rot": Gamma_no_rot,
        "B_coupling": B_coupling,
        "M_rr": M_rr,
        "M_tr_norm": float(np.linalg.norm(M_tr)),
        "qhat": qhat.tolist(),
    }


# ---------------------------------------------------------------------------
# §4  Cubic C_ij fit from the effective Cauchy Gamma + the B pseudo-tensor invariant
# ---------------------------------------------------------------------------
def _cubic_gamma_row(q, i, jl):
    """Cubic design-matrix row (identical to Stage-1 srs_elastic_tensor)."""
    if i == jl:
        return [q[i] ** 2, 0.0, sum(q[j] ** 2 for j in range(3) if j != i)]
    return [0.0, q[i] * q[jl], q[i] * q[jl]]


def extract_cubic_from_micropolar(pos, bonds, *, k_axial=1.0, k_shear=1.0, gamma=0.0,
                                  kappa_rot=0.0, lever=0.0, reading="a", rho=1.0,
                                  m=1.0, cross_coupling=True, directions=None):
    """Fit cubic (C11,C12,C44) to the effective micropolar-reduced Gamma_cauchy across
    directions, AND accumulate the chiral pseudo-tensor invariant + channel diagnostic.

    Returns C11/C12/C44 (with the chiral back-reaction folded in via the Schur
    complement), the residual, AND:
      B_invariant : a rotation/parity-odd scalar summarizing |B| over the direction set
                    (the frobenius norm of the antisymmetric part of the t-r block,
                    averaged over directions) -- the geometry-fixed magnitude of the
                    chiral pseudo-tensor. Nonzero <=> the acoustic-activity channel is
                    mechanically present.
      B_signed    : the signed pseudoscalar q^.(axial-part of B) averaged over directions
                    -- flips sign under enantiomorph swap (the parity-odd falsifier).
    """
    if directions is None:
        directions = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1],
                      [0, 1, 1], [1, 1, 1], [2, 1, 0], [1, 2, 0], [3, 1, 2]]
    A, b = [], []
    B_norms, B_signed_vals = [], []
    for dd in directions:
        q = np.array(dd, float)
        q /= np.linalg.norm(q)
        res = micropolar_longwave(q, pos, bonds, k_axial=k_axial, k_shear=k_shear,
                                  gamma=gamma, kappa_rot=kappa_rot, lever=lever,
                                  reading=reading, rho=rho, m=m,
                                  cross_coupling=cross_coupling)
        G = res["Gamma_cauchy"]
        Bc = res["B_coupling"]                       # 3x3 t-r block
        # invariant magnitude of the chiral coupling
        B_norms.append(float(np.linalg.norm(Bc)))
        # SIGNED pseudoscalar = trace of the translation<->rotation coupling block.
        # DIAGNOSED (2026-07-04 smoke): the ENTIRE M_tr block flips sign under enantiomorph
        # swap (M_tr(left) = -M_tr(right) exactly, R+L=0 to machine precision, all q^). The
        # t-r block is symmetric; its parity-odd content is the ISOTROPIC part = tr(M_tr) =
        # the acoustic-gyrotropy scalar. tr flips sign with hand (the falsifier); |B| does
        # not. (An axial-vector extraction reads ~0 because the signal lives in the
        # symmetric/isotropic part, not the antisymmetric part -- corrected here.)
        B_signed_vals.append(float(np.trace(Bc).real))
        for i in range(3):
            for jl in range(i, 3):
                A.append(_cubic_gamma_row(q, i, jl))
                b.append(G[i, jl])
    A = np.array(A, float)
    b = np.array(b, float)
    x, *_ = np.linalg.lstsq(A, b, rcond=None)
    fit = A @ x
    resid_rel = float(np.max(np.abs(fit - b)) / (np.max(np.abs(b)) + 1e-30))
    C11, C12, C44 = (float(v) for v in x)
    return {
        "C11": C11, "C12": C12, "C44": C44,
        "max_rel_residual": resid_rel,
        "B_invariant": float(np.mean(B_norms)),
        "B_signed": float(np.mean(B_signed_vals)),
        "B_norms_per_dir": B_norms,
    }


def channel_diagnostic(pos, bonds, *, k_axial=1.0, k_shear=1.0, gamma=0.0,
                       kappa_rot=0.0, lever=0.0, reading="a", rho=1.0, m=1.0,
                       qhat=(1, 1, 1)):
    """Which continuum channel carries B (Grant pointer 2): sigma^A (lever/geometric)
    vs mu (couple-stress/independent-stiffness).

    Diagnostic: compute the chiral coupling B with the couple-stress + kappa_rot zeroed
    (only the lever geometry) vs with the lever zeroed (only kappa_rot/gamma). The ratio
    of the two |B| tells which channel the coupling actually rides in the given reading.
    """
    q = np.asarray(qhat, float); q /= np.linalg.norm(q)
    # sigma^A (lever-only) contribution
    r_lever = micropolar_longwave(q, pos, bonds, k_axial=k_axial, k_shear=k_shear,
                                  gamma=0.0, kappa_rot=0.0, lever=lever, reading="a",
                                  rho=rho, m=m)
    # mu-only (kappa_rot + gamma, no lever) contribution
    r_mu = micropolar_longwave(q, pos, bonds, k_axial=k_axial, k_shear=k_shear,
                               gamma=gamma, kappa_rot=kappa_rot, lever=0.0, reading="b",
                               rho=rho, m=m)
    b_lever = float(np.linalg.norm(r_lever["B_coupling"]))
    b_mu = float(np.linalg.norm(r_mu["B_coupling"]))
    return {
        "B_sigmaA_lever_channel": b_lever,
        "B_mu_couplestress_channel": b_mu,
        "channel": ("sigma^A (geometric/lever)" if b_lever > b_mu
                    else "mu (couple-stress/independent-stiffness)"),
    }
