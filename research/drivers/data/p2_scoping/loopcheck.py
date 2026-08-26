"""Loop-representability of a (p,q) spatial imposition vs L + the common-mode receipt."""
import json, sys
import numpy as np
sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src")
sys.path.insert(0, "/private/tmp/claude-501/-Users-grantlindblom-AVE-staging/91b867e5-bc0e-42d5-9d27-3ec2573c4b62/scratchpad/p2scope")
from ave.core.chiral_lattice import build_srs_net
import ave.solvers.harmonic_balance_srs as hb
from imposition_proto import plane_cut_loop

for L in (2, 3, 4, 6, 8):
    net = build_srs_net(L=L); bt = hb.build_bond_table(net)
    loop = plane_cut_loop(net, bt, 0.5, "fwd")
    phi, psi = loop.ang[:, 0], loop.ang[:, 1]
    n = len(loop.ports)
    out = dict(L=L, n_ports=n,
               n_distinct_phi=int(len(np.unique(np.round(phi, 9)))),
               n_distinct_psi=int(len(np.unique(np.round(psi, 9)))))
    # is exp(i(p phi + q psi)) distinguishable from the uniform vector?
    for (p, q) in ((0, 0), (2, 3), (2*L, 3*L)):
        d = np.exp(1j*(p*phi + q*psi))
        out[f"mean_abs_p{p}_q{q}"] = round(float(np.abs(d.mean())), 6)
    print(json.dumps(out), flush=True)
