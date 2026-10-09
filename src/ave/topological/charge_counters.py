"""Charged-seed charge counters C-exact, C-link, 4th-order C-det for the AVE K4
unit-quaternion field q on a cubic grid.

Conventions (KTL §0, source: charged-seed-counters-spec_2026-10-08.md sha1 73eb9aeea345
with 22:00 addendum):

  Axes: (i,j,k) = (x,y,z), right-handed.  q = q0 + q1·i + q2·j + q3·k.  Vacuum = q = +1.

  Engine projection (cf:219-221):
    n = R(q)ẑ = q k q̄
    n_x = 2(q1 q3 + q0 q2),  n_y = 2(q2 q3 − q0 q1),  n_z = 1 − 2(q1²+q2²)

  Stereographic chart:  σ(n) = (n_x + i n_y) / (1 + n_z)   (vacuum ẑ maps to 0)

  KTL embedding:  A0 = q0 − i q3,  A1 = q2 − i q1
    ↔  q = (Re A0, −Im A1, Re A1, −Im A0)
    Property: σ(H_engine(q)) = A1/A0 exactly.

  Cross-multiplied projection check (addendum, division-free):
    max |(n_x + i n_y)·A0 − (1 + n_z)·A1| ≤ 1e-12

  C-det orientation (q last column):
    b = (1/2π²)·det[∂x q, ∂y q, ∂z q, q]
    Identity hedgehog q=(cos f, r̂ sin f), f: π→0 gives +1 with this order.

  BCC alive storage (cf:994-998): alive = all-even ∪ all-odd sites.
    dV = h³ dense,  dV = 4 h³ per alive site.

Integer verdict: C-exact and C-link decide the integer charge.
C-det (4th order) is a DRIFT ALARM / continuous monitor only; not the integer verdict.

extract_hopf_charge (cf:2429-2444): LOG-ONLY.
  Returns (1/8π²)∫A·B, which equals 2·Q_H on a dense grid and ≈ deg/8 on alive
  storage (cf:2443 sums mask·dx³, not 4dx³; sparse FFT further attenuates).
  Divide by 2 if used at all; never feed as a verdict.  Use c_exact / c_link.

Sources:
  KTL spec:   charged-seed-counters-spec_2026-10-08.md  sha1 73eb9aeea345
  Change spec: 2026-10-08-charged-seed-K4-change-SPEC_CANDIDATE.md  sha1 0bb84db49105
  Gate ladder: LADDER-charged-seed-K4-2026-10-08.md  sha1 f086d59a4cd0
  Proto:       counters.py sha1 0134414aa632 / seeds.py sha1 facb8725ef0e
  Engine:      src/ave/topological/cosserat_field_3d.py at a2be127d
"""
import itertools
import numpy as np


# ── Engine projection and stereographic chart ─────────────────────────────────

def hopf_engine(q):
    """Engine n = R(q)ẑ = q k q̄ (cf:219-221). q shape (..., 4)."""
    q0, q1, q2, q3 = np.moveaxis(q, -1, 0)
    return np.stack([
        2 * (q1 * q3 + q0 * q2),
        2 * (q2 * q3 - q0 * q1),
        1 - 2 * (q1 * q1 + q2 * q2),
    ], -1)


def stereo(n):
    """Stereographic chart σ(n) = (n_x + i n_y) / (1 + n_z). Vacuum ẑ → 0."""
    return (n[..., 0] + 1j * n[..., 1]) / (1 + n[..., 2])


# ── KTL and spec embeddings ───────────────────────────────────────────────────

def embed_ktl(A0, A1):
    """KTL embedding: A0=q0-iq3, A1=q2-iq1 → q=(Re A0, -Im A1, Re A1, -Im A0).
    Then σ(H_engine(q)) = A1/A0 exactly (KTL §0)."""
    return np.stack([A0.real, -A1.imag, A1.real, -A0.imag], -1)


def embed_spec(A0, A1):
    """Spec-literal embedding q=a+bj: q=(Re a, Im a, Re b, Im b).
    Exposed for mutant testing; gives σ deviation ≈ 150 on the axial seed."""
    return np.stack([A0.real, A0.imag, A1.real, A1.imag], -1)


# ── Grid and seed builders (ported from proto seeds.py facb8725ef0e) ──────────

def grid(n):
    """Centred grid for an n³ box. Returns (X, Y, Z, r)."""
    c = (n - 1) / 2.0
    i = np.arange(n) - c
    X, Y, Z = np.meshgrid(i, i, i, indexing='ij')
    return X, Y, Z, np.sqrt(X ** 2 + Y ** 2 + Z ** 2)


def profile(r, rc, L):
    """f = π·c(r) / (1+(r/rc)²), C² smooth cutoff c=1 for r<3rc → 0 at r=L."""
    s = np.clip((r - 3 * rc) / (L - 3 * rc), 0, 1)
    return np.pi * (1 - (6 * s ** 5 - 15 * s ** 4 + 10 * s ** 3)) / (1 + (r / rc) ** 2)


def Zmap(X, Y, Z, r, f, zsign=-1):
    """KTL base map (zsign=-1): Z0 = cos f − i (z/r) sin f, Z1 = (x+iy) sin f / r.
    zsign=+1 is the spec-literal Z0 (gives mirror-sign; see KTL §3)."""
    rr = np.where(r > 0, r, 1.0)
    s = np.sin(f)
    return np.cos(f) + zsign * 1j * Z / rr * s, (X + 1j * Y) / rr * s


def hedgehog(n, rc, mirror=False):
    """Identity hedgehog (degree +1; -1 if mirror). q=(cos f, r̂ sin f)."""
    X, Y, Z, r = grid(n)
    f = profile(r, rc, n / 2.0)
    rr = np.where(r > 0, r, 1.0)
    s = np.sin(f)
    return np.stack([np.cos(f), X / rr * s, (-Y if mirror else Y) / rr * s, Z / rr * s], -1)


def rational(n, rc, p=2, qq=3, embed=embed_ktl, mirror=False, zsign=-1,
             return_fields=False):
    """Rational map of degree p·qq. (p=2, qq=3) → degree +6 axial seed.
    Uses KTL embedding by default; zsign=-1 per §0 orientation.
    return_fields=True: returns (q, A0, A1) for projection_check gate."""
    X, Y, Z, r = grid(n)
    f = profile(r, rc, n / 2.0)
    Z0, Z1 = Zmap(X, Y, Z, r, f, zsign)
    if mirror:
        Z1 = np.conj(Z1)
    A1 = Z1 ** p
    A0 = Z0 ** qq
    N = np.sqrt(np.abs(A0) ** 2 + np.abs(A1) ** 2)
    A0n, A1n = A0 / N, A1 / N
    q = embed(A0n, A1n)
    if return_fields:
        return q, A0n, A1n
    return q


def cold_control(n, rc, return_fields=False):
    """C0-cold degree-0 control (spec A2.4): same (2,3) structure, f(0)=0.
    f = 0.04·4s²/(1+s²)², s=r/rc. C-det ≈ 0; degree = 0 exactly.
    return_fields=True: returns (q, A0, A1) for projection_check gate."""
    X, Y, Z, r = grid(n)
    s_r = r / rc
    f = 0.04 * 4 * s_r ** 2 / (1 + s_r ** 2) ** 2
    Z0, Z1 = Zmap(X, Y, Z, r, f, zsign=-1)
    A0 = Z0 ** 3
    A1 = Z1 ** 2
    N = np.sqrt(np.abs(A0) ** 2 + np.abs(A1) ** 2)
    N = np.where(N > 1e-10, N, 1.0)
    A0n, A1n = A0 / N, A1 / N
    q = embed_ktl(A0n, A1n)
    if return_fields:
        return q, A0n, A1n
    return q


def _qmul(a, b):
    aw, ax, ay, az = np.moveaxis(a, -1, 0)
    bw, bx, by, bz = np.moveaxis(b, -1, 0)
    return np.stack([
        aw * bw - ax * bx - ay * by - az * bz,
        aw * bx + ax * bw + ay * bz - az * by,
        aw * by - ax * bz + ay * bw + az * bx,
        aw * bz + ax * by - ay * bx + az * bw,
    ], -1)


def _hedgehog_at(n, rc, c, mirror=False, L=None):
    X, Y, Z, _ = grid(n)
    X = X - c[0]; Y = Y - c[1]; Z = Z - c[2]
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    lim = L if L is not None else n / 2.0 - max(abs(np.array(c)))
    f = profile(r, rc, lim)
    rr = np.where(r > 0, r, 1.0)
    s = np.sin(f)
    return np.stack([np.cos(f), X / rr * s, (-Y if mirror else Y) / rr * s, Z / rr * s], -1)


def dipole(n, rc):
    """Hedgehog (+1) at +n/4 × mirror hedgehog (-1) at -n/4; degree 0, 2 hits."""
    d = n / 4.0
    return _qmul(
        _hedgehog_at(n, rc, (d, 0, 0), L=n / 4.0),
        _hedgehog_at(n, rc, (-d, 0, 0), mirror=True, L=n / 4.0),
    )


def hedgehog_sq(n, rc):
    """h·h (degree 2)."""
    h = hedgehog(n, rc)
    return _qmul(h, h)


# ── BCC alive mask ────────────────────────────────────────────────────────────

def bcc_alive_mask(shape):
    """BCC alive mask: True at all-even or all-odd sites (cf:994-998)."""
    I = np.arange(shape[0])[:, None, None]
    J = np.arange(shape[1])[None, :, None]
    K = np.arange(shape[2])[None, None, :]
    return (
        ((I % 2 == 0) & (J % 2 == 0) & (K % 2 == 0)) |
        ((I % 2 == 1) & (J % 2 == 1) & (K % 2 == 1))
    )


# ── 4×4 Leibniz helper (avoids np.stack((n,n,n,4,4))+linalg.det overhead) ────

# Precompute all 24 permutations and signs for the 4×4 Leibniz expansion.
_DET4_TERMS = []
for _p4 in itertools.permutations(range(4)):
    _s4 = 1
    _lst = list(_p4)
    for _a4 in range(4):
        for _b4 in range(_a4 + 1, 4):
            if _lst[_a4] > _lst[_b4]:
                _s4 = -_s4
    _DET4_TERMS.append((_p4, _s4))


def _det4(A, B, C, D):
    """det[A,B,C,D] via Leibniz for spatial fields of shape (...,4).
    Peak allocation: result (...) + one (...)  term — no (n,n,n,4,4) intermediate."""
    cols = (A, B, C, D)
    result = None
    for (i, j, k, l), s in _DET4_TERMS:
        term = cols[0][..., i] * cols[1][..., j]
        term *= cols[2][..., k]
        term *= cols[3][..., l]
        if result is None:
            result = term if s > 0 else -term
        elif s > 0:
            result += term
        else:
            result -= term
    return result


# ── C-det: degree density integrators ────────────────────────────────────────

TETRA_OFFSETS = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))  # cf:134-139


def _roll4_diff(q, ax, h):
    """4th-order 1D central diff along axis ax, in-place to bound peak allocation."""
    out = np.roll(q, -2, ax)    # q[i+2]
    out *= -1.0
    t = np.roll(q, -1, ax)      # q[i+1]
    t *= 8.0
    out += t
    del t
    t = np.roll(q, 1, ax)       # q[i-1]
    t *= -8.0
    out += t
    del t
    t = np.roll(q, 2, ax)       # q[i-2]
    out += t
    del t
    out /= (12.0 * h)
    return out


def c_det(q, h=1.0, weight=None):
    """C-det, 2nd-order central differences (dense grid).
    b = (1/2π²) det[∂x q, ∂y q, ∂z q, q] (q last; hedgehog → +1)."""
    dq = [np.gradient(q, h, axis=a) for a in range(3)]
    d = _det4(dq[0], dq[1], dq[2], q)
    if weight is not None:
        d = d * weight
    return float(d.sum() * h ** 3 / (2 * np.pi ** 2))


def c_det4(q, h=1.0):
    """C-det, 4th-order central differences (dense grid) — DEFAULT for dense grids.
    Uses _roll4_diff (in-place) + _det4 (Leibniz) to bound peak RSS < 250 MB at 96³."""
    d0 = _roll4_diff(q, 0, h)
    d1 = _roll4_diff(q, 1, h)
    d2 = _roll4_diff(q, 2, h)
    return float(_det4(d0, d1, d2, q).sum() * h ** 3 / (2 * np.pi ** 2))


def c_det_alive(q, alive, h=1.0):
    """C-det, 2nd-order central tetra stencil on BCC/alive storage.
    d_j q = (1/8) Σ_l p_l^j [q(x+p_l) - q(x-p_l)], dV = 4h³ per alive site."""
    dq = [np.zeros_like(q) for _ in range(3)]
    for p in TETRA_OFFSETS:
        t_fwd = np.roll(q, (-p[0], -p[1], -p[2]), (0, 1, 2))
        t_bwd = np.roll(q, p, (0, 1, 2))
        t_fwd -= t_bwd
        del t_bwd
        t_fwd /= (8.0 * h)
        for j in range(3):
            if p[j] > 0:
                dq[j] += t_fwd
            elif p[j] < 0:
                dq[j] -= t_fwd
        del t_fwd
    d = _det4(dq[0], dq[1], dq[2], q) * alive
    return float(d.sum() * 4 * h ** 3 / (2 * np.pi ** 2))


def c_det_alive4(q, alive, h=1.0):
    """C-det, 4th-order on BCC/alive storage — DEFAULT for alive grids.
    D_p q = [8(q(x+p)-q(x-p)) − (q(x+2p)−q(x-2p))]/12, dV = 4h³.
    In-place + Leibniz bounds peak RSS < 250 MB at 96³."""
    dq = [np.zeros_like(q) for _ in range(3)]
    for p in TETRA_OFFSETS:
        # 8*(R(1,p)-R(-1,p))
        t1 = np.roll(q, (-p[0], -p[1], -p[2]), (0, 1, 2))
        tm1 = np.roll(q, p, (0, 1, 2))
        t1 -= tm1
        del tm1
        t1 *= 8.0
        # (R(2,p)-R(-2,p))
        t2 = np.roll(q, (-2 * p[0], -2 * p[1], -2 * p[2]), (0, 1, 2))
        tm2 = np.roll(q, (2 * p[0], 2 * p[1], 2 * p[2]), (0, 1, 2))
        t2 -= tm2
        del tm2
        D = t1 - t2
        del t1, t2
        D /= 12.0
        scale = D / (4.0 * h)
        del D
        for j in range(3):
            if p[j] > 0:
                dq[j] += scale
            elif p[j] < 0:
                dq[j] -= scale
        del scale
    d = _det4(dq[0], dq[1], dq[2], q) * alive
    return float(d.sum() * 4 * h ** 3 / (2 * np.pi ** 2))


# ── Freudenthal / BCC tet tables ──────────────────────────────────────────────

_PERMS = list(itertools.permutations(range(3)))


def _perm_sign(p):
    s = 1
    for a in range(3):
        for b in range(a + 1, 3):
            if p[a] > p[b]:
                s = -s
    return s


TETS = []  # (vertex offsets v0..v3, orientation sign)
for _p in _PERMS:
    _v = [np.zeros(3, int)]
    for _ax in _p:
        _w = _v[-1].copy()
        _w[_ax] += 1
        _v.append(_w)
    TETS.append((np.array(_v), _perm_sign(_p)))


def _bcc_tets():
    """Conforming 12-tet split of a side-2 BCC cube (KTL §1): each face split
    along its lowest-corner diagonal; each triangle coned to the odd centre (1,1,1)."""
    out = []
    C = np.array([1, 1, 1])
    for ax in range(3):
        for side in (0, 2):
            others = [a for a in range(3) if a != ax]

            def P(u, v, _ax=ax, _side=side, _oth=others):
                p = np.zeros(3, int)
                p[_ax] = _side
                p[_oth[0]] = u
                p[_oth[1]] = v
                return p

            for tri in ((P(0, 0), P(2, 0), P(2, 2)), (P(0, 0), P(2, 2), P(0, 2))):
                v = np.array([C, *tri])
                o = int(np.sign(np.linalg.det((v[1:] - v[0]).T.astype(float))))
                out.append((v, o))
    return out


BCC_TETS = _bcc_tets()


# ── C-exact helpers ───────────────────────────────────────────────────────────

def random_regular_values(K, seed, max_q0=0.0):
    """K seeded unit quaternions with q0 ≤ max_q0 (far from vacuum q=+1).
    Canonical: K=5, seed=20261008, max_q0=0.0 (setup sheet)."""
    rng = np.random.default_rng(seed)
    out = []
    while len(out) < K:
        v = rng.normal(size=4)
        v /= np.linalg.norm(v)
        if v[0] <= max_q0:
            out.append(v)
    return np.array(out)


def random_n_vectors(K, seed, max_nz=-0.2):
    """K seeded unit 3-vectors with n_z < max_nz (far from vacuum ẑ).
    Canonical: K=4, seed=20261009 (setup sheet)."""
    rng = np.random.default_rng(seed)
    out = []
    while len(out) < K:
        v = rng.normal(size=3)
        v /= np.linalg.norm(v)
        if v[2] < max_nz:
            out.append(v)
    return np.array(out)


def _vertex_slab(F, i, off, s=1):
    """Values of field F at cell-corner offset `off` for all cells in slab i."""
    ny, nz = F.shape[1], F.shape[2]
    return F[i + off[0], off[1]:ny - s + off[1]:s, off[2]:nz - s + off[2]:s]


def _c_exact_qstar(q, qstar, tets=None, s=1, tau_fail=0.0, tau_warn=0.5, lam_eps=1e-12):
    """Signed preimage count for a single regular value qstar (KTL §1).
    Returns dict: N, n_hits, n_bad, n_warn, degenerate."""
    N = 0; hits = 0; bad = 0; warn = 0; degen = 0
    if tets is None:
        tets = TETS
    for i in range(0, q.shape[0] - s, s):
        for verts, orient in tets:
            V = np.stack([_vertex_slab(q, i, o, s) for o in verts], -1)
            V = V.reshape(-1, 4, 4)                        # (cells, comps, verts)
            G = np.einsum('mai,maj->mij', V, V)            # pairwise dot products
            mind = G[:, [0, 0, 0, 1, 1, 2], [1, 2, 3, 2, 3, 3]].min(1)
            bad += int((mind <= tau_fail).sum())
            warn += int((mind <= tau_warn).sum())
            # Prefilter: q* inside spherical hull iff max_i q_i·q* >= mind
            d = V.transpose(0, 2, 1) @ qstar
            cand = d.max(1) >= np.minimum(mind, 0.999999) - 1e-12
            if not cand.any():
                continue
            Vc = V[cand]
            D = np.linalg.det(Vc)
            # Cramer: λ_c · D = det(V with column c replaced by q*)
            LD = np.empty((len(Vc), 4))
            for c in range(4):
                Vi = Vc.copy()
                Vi[:, :, c] = qstar
                LD[:, c] = np.linalg.det(Vi)
            sD = np.sign(D)
            inside = (LD * sD[:, None] > 0).all(1) & (np.abs(D) > 0)
            lam = LD / np.where(np.abs(D) > 0, D, 1.0)[:, None]
            near = (np.abs(lam).min(1) < lam_eps) & (lam > -lam_eps).all(1)
            degen += int(near.sum())
            if inside.any():
                loc = -sD[inside] * orient  # local degree = -sign(det V) · orient(spatial)
                N += int(loc.sum())
                hits += int(inside.sum())
    return dict(N=N, n_hits=hits, n_bad=bad, n_warn=warn, degenerate=degen)


def _boundary_q0_ok(q):
    """True if q[..., 0] > 0.5 on all 6 boundary faces (ensures q* with q0≤0 not on boundary)."""
    return bool(
        q[0, :, :, 0].min() > 0.5 and q[-1, :, :, 0].min() > 0.5 and
        q[:, 0, :, 0].min() > 0.5 and q[:, -1, :, 0].min() > 0.5 and
        q[:, :, 0, 0].min() > 0.5 and q[:, :, -1, 0].min() > 0.5
    )


def c_exact(q, qstars, tets=None, s=1):
    """Signed preimage count using K seeded regular values (KTL §1).

    Args:
        q: quaternion field (..., 4), unit quaternions.
        qstars: (K, 4) array with qstar_0 ≤ 0 (from random_regular_values).
        tets: tet table; None → TETS (dense Freudenthal); BCC_TETS with s=2 for alive.
        s: cell stride (1 = dense, 2 = BCC side-2 cubes).

    Returns dict:
        resolved (bool), value (int or None),
        per_qstar (list[int]), n_bad (int), n_degen (int),
        n_warn (int), n_hits (list[int]), reason (str or None).

    UNRESOLVED if: n_bad > 0, n_degen > 0, qstars disagree, or boundary q0 ≤ 0.5.
    """
    qstars = np.asarray(qstars)
    results = [_c_exact_qstar(q, qs, tets=tets, s=s) for qs in qstars]
    n_bad = results[0]['n_bad']
    n_warn = results[0]['n_warn']
    per_qstar = [r['N'] for r in results]
    n_hits = [r['n_hits'] for r in results]
    n_degen = sum(r['degenerate'] for r in results)

    reason = None
    if n_bad > 0:
        reason = f'BAD_TETS: n_bad={n_bad}'
    elif n_degen > 0:
        reason = f'DEGENERATE: n_degen={n_degen}'
    elif not all(v == per_qstar[0] for v in per_qstar):
        reason = f'QSTAR_DISAGREEMENT: {per_qstar}'
    elif not _boundary_q0_ok(q):
        reason = 'BOUNDARY: boundary q0 not all > 0.5'

    if reason:
        return dict(resolved=False, value=None, per_qstar=per_qstar,
                    n_bad=n_bad, n_degen=n_degen, n_warn=n_warn,
                    n_hits=n_hits, reason=reason)
    return dict(resolved=True, value=per_qstar[0], per_qstar=per_qstar,
                n_bad=n_bad, n_degen=n_degen, n_warn=n_warn,
                n_hits=n_hits, reason=None)


# ── C-link: preimage linking ──────────────────────────────────────────────────

_FACES = [(1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2)]


def preimage_curves(n, nstar, h=1.0, origin=None, tets=None, s=1):
    """Oriented closed polygons {x : n(x) = nstar} by linear interpolation on tets.
    Returns (list_of_curves, info_dict) where info = {'open_tets': int, 'broken': int}."""
    e1, e2, ns = _frame(nstar)
    g = np.stack([n @ e1, n @ e2, n @ ns], -1)
    sh = np.array(n.shape[:3])
    ny, nz = sh[1], sh[2]
    if origin is None:
        origin = -(sh - 1) / 2.0
    gid = lambda I, J, K: (I * ny + J) * nz + K  # noqa: E731
    nxt = {}; pts = {}; open_tets = 0
    if tets is None:
        tets = TETS
    J0, K0 = np.meshgrid(
        np.arange(0, ny - s, s), np.arange(0, nz - s, s), indexing='ij'
    )
    J0 = J0.ravel(); K0 = K0.ravel()
    for i in range(0, sh[0] - s, s):
        for verts, orient in tets:
            gv = np.stack([_vertex_slab(g, i, o, s) for o in verts], 2).reshape(-1, 4, 3)
            ok = (
                (gv[:, :, 0].min(1) <= 0) & (gv[:, :, 0].max(1) >= 0) &
                (gv[:, :, 1].min(1) <= 0) & (gv[:, :, 1].max(1) >= 0) &
                (gv[:, :, 2].max(1) > 0)
            )
            for m in np.nonzero(ok)[0]:
                vx = np.array([[i, J0[m], K0[m]]]) + verts
                ids = gid(vx[:, 0], vx[:, 1], vx[:, 2])
                hits_f = []
                for f in _FACES:
                    A_mat = np.vstack([gv[m, f, 0], gv[m, f, 1], np.ones(3)])
                    try:
                        mu = np.linalg.solve(A_mat, [0.0, 0.0, 1.0])
                    except np.linalg.LinAlgError:
                        continue
                    if (mu > 0).all() and mu @ gv[m, f, 2] > 0:
                        key = tuple(sorted(ids[list(f)]))
                        pts[key] = (origin + mu @ vx[list(f)]) * h
                        hits_f.append(key)
                if len(hits_f) == 0:
                    continue
                if len(hits_f) != 2:
                    open_tets += 1
                    continue
                E = (vx[1:] - vx[0]).astype(float).T * h
                Gm = (gv[m, 1:, :2] - gv[m, 0, :2]).T
                Jm = Gm @ np.linalg.inv(E)
                t = np.cross(Jm[0], Jm[1])
                a, b = hits_f
                if (pts[b] - pts[a]) @ t < 0:
                    a, b = b, a
                nxt[a] = b
    # Chain segments into closed polygons
    comps = []; seen = set(); broken = 0
    for start in list(nxt):
        if start in seen:
            continue
        c = [start]; seen.add(start); cur = nxt[start]
        while cur != start:
            if cur not in nxt or cur in seen:
                broken += 1
                break
            c.append(cur); seen.add(cur); cur = nxt[cur]
        else:
            comps.append(np.array([pts[k] for k in c]))
    return comps, dict(open_tets=open_tets, broken=broken)


def _frame(nstar):
    """Orthonormal frame (e1, e2, nstar) with e1 × e2 = nstar."""
    nstar = nstar / np.linalg.norm(nstar)
    a = np.array([1.0, 0.0, 0.0]) if abs(nstar[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
    e1 = np.cross(nstar, a)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(nstar, e1)
    return e1, e2, nstar


def _segs(comps):
    return np.concatenate([np.stack([c, np.roll(c, -1, 0)], 1) for c in comps], 0)


def gauss_link(compsA, compsB, chunk=4000):
    """Exact polygon Gauss linking (Klenin & Langowski 2000, Biopolymers 54:307)."""
    if not compsA or not compsB:
        return 0.0
    A = _segs(compsA); B = _segs(compsB); tot = 0.0
    for s in range(0, len(A), chunk):
        p1 = A[s:s + chunk, None, 0]; p2 = A[s:s + chunk, None, 1]
        p3 = B[None, :, 0]; p4 = B[None, :, 1]
        r13, r14, r23, r24 = p3 - p1, p4 - p1, p3 - p2, p4 - p2

        def nrm(v):
            return v / np.linalg.norm(v, axis=-1, keepdims=True)

        n1 = nrm(np.cross(r13, r14)); n2 = nrm(np.cross(r14, r24))
        n3 = nrm(np.cross(r24, r23)); n4 = nrm(np.cross(r23, r13))
        dot = lambda a, b: np.clip((a * b).sum(-1), -1, 1)  # noqa: E731
        om = (np.arcsin(dot(n1, n2)) + np.arcsin(dot(n2, n3)) +
              np.arcsin(dot(n3, n4)) + np.arcsin(dot(n4, n1)))
        sg = np.sign((np.cross(p4 - p3, p2 - p1) * r13).sum(-1))
        tot += (om * sg).sum()
    return tot / (4 * np.pi)


def winding_about_z(c):
    """Sum of angular increments Σdφ around the z-axis for curve c."""
    ang = np.arctan2(c[:, 1], c[:, 0])
    d = np.diff(np.append(ang, ang[0]))
    return (d + np.pi) % (2 * np.pi) - np.pi


def _c_link_pair(n, nstar1, nstar2, h=1.0, tets=None, s=1):
    """Compute Lk for one (nstar1, nstar2) pair. Returns (lk, n_open, n_broken, nA, nB)."""
    A, ia = preimage_curves(n, nstar1, h, tets=tets, s=s)
    B, ib = preimage_curves(n, nstar2, h, tets=tets, s=s)
    lk = gauss_link(A, B)
    return lk, ia['open_tets'] + ib['open_tets'], ia['broken'] + ib['broken'], len(A), len(B)


def c_link(n, nstars, h=1.0, tets=None, s=1):
    """Preimage linking number using two (nstar, nstar) pairs (KTL §2).

    Args:
        n: direction field (..., 3), unit vectors.
        nstars: (4, 3) array of unit vectors with n_z < -0.2.
            Pair 1: (nstars[0], nstars[1]).  Pair 2: (nstars[2], nstars[3]).
        tets: tet table; None → TETS; BCC_TETS with s=2 for alive storage.
        s: cell stride.

    Returns dict:
        resolved (bool), value (int or None),
        raw_lk (float, always logged even if UNRESOLVED — ladder Nit N3),
        pair_lk ([lk1, lk2]), n_open (int), n_broken (int),
        n_comps ([(nA1,nB1),(nA2,nB2)]), reason (str or None).

    UNRESOLVED if: degenerate (n1≈n2), open/broken loops, |Lk−round|≥1e-6, or pair disagree.
    Degenerate n1≈n2: returns UNRESOLVED, never 0.
    """
    nstars = np.asarray(nstars)
    n1, n2, n3, n4 = nstars[0], nstars[1], nstars[2], nstars[3]

    # Degenerate: n1 ≈ n2 → self-linking, undefined
    dot12 = float(np.dot(n1 / np.linalg.norm(n1), n2 / np.linalg.norm(n2)))
    if dot12 > 1 - 1e-10:
        return dict(resolved=False, value=None, raw_lk=float('nan'),
                    pair_lk=[float('nan'), None], n_open=0, n_broken=0,
                    n_comps=None, reason='DEGENERATE: n1 ≈ n2')

    lk1, op1, br1, a1, b1 = _c_link_pair(n, n1, n2, h, tets, s)
    lk2, op2, br2, a2, b2 = _c_link_pair(n, n3, n4, h, tets, s)

    pair_lk = [float(lk1), float(lk2)]
    raw_lk = (pair_lk[0] + pair_lk[1]) / 2.0
    n_open = op1 + op2
    n_broken = br1 + br2
    n_comps = [(a1, b1), (a2, b2)]

    reason = None
    r1, r2 = round(lk1), round(lk2)
    tol = 1e-6
    if n_open > 0 or n_broken > 0:
        reason = f'OPEN_OR_BROKEN: open={n_open}, broken={n_broken}'
    elif abs(lk1 - r1) >= tol:
        reason = f'NON_INTEGER pair1: |{lk1} - {r1}| = {abs(lk1 - r1):.2e}'
    elif abs(lk2 - r2) >= tol:
        reason = f'NON_INTEGER pair2: |{lk2} - {r2}| = {abs(lk2 - r2):.2e}'
    elif r1 != r2:
        reason = f'PAIR_DISAGREEMENT: pair1={r1}, pair2={r2}'

    if reason:
        return dict(resolved=False, value=None, raw_lk=raw_lk,
                    pair_lk=pair_lk, n_open=n_open, n_broken=n_broken,
                    n_comps=n_comps, reason=reason)
    return dict(resolved=True, value=r1, raw_lk=raw_lk,
                pair_lk=pair_lk, n_open=n_open, n_broken=n_broken,
                n_comps=n_comps, reason=None)


# ── Cross-multiplied projection check ────────────────────────────────────────

def projection_check(q, A0_seed, A1_seed):
    """Cross-multiplied projection check (KTL addendum 2026-10-08 22:00).

    Checks whether the embedded field q has the KTL property σ(H(q)) = A1/A0:
      max|(n_x + i n_y)·A0_seed − (1 + n_z)·A1_seed| ≤ 1e-12
    where n = hopf_engine(q) and (A0_seed, A1_seed) are from the SEED
    construction — NOT recomputed from q.

    Gate evidence (xmult_box.py sha1 fa5b0c943c79):
      KTL embed:       1.26e-15/1.24e-15/1.40e-15/1.46e-15 at 48/64/96/128³ (PASSES)
      Spec-literal embed q=(Re A0,Im A0,Re A1,Im A1): ≈2.00 at every grid (TRIPS)
      Z0 sign flip (zsign=+1): ≈1e-15 (blind to flip); caught by C-exact = −6 in #3.
    """
    n = hopf_engine(q)
    sigma_n = n[..., 0] + 1j * n[..., 1]
    one_plus_nz = 1.0 + n[..., 2]
    res = sigma_n * A0_seed - one_plus_nz * A1_seed
    return float(np.abs(res).max())
