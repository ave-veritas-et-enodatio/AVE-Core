"""Photon still (to compare with the electron).  AVE photon = massless TRANSVERSE
Cosserat shear wave at c: flat wavefronts (no Mach cone), no localized core,
spin-1 circular-polarization helix.  Non-dispersive right-mover -> analytic snapshot."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

NX, NY = 560, 440
xx, yy = np.mgrid[0:NX, 0:NY]
xc, yc = NX*0.46, NY/2
k = 2*np.pi/26.0                      # wavelength (de Broglie = the wavelength itself)
Lx, Ly = 150.0, 95.0                  # packet envelope (beam)
env = np.exp(-((xx-xc)/Lx)**2) * np.exp(-((yy-yc)/Ly)**2)
field = env * np.cos(k*(xx-xc))       # TRANSVERSE field; wavefronts _|_ to k (vertical), at c
A = np.clip(field/ (np.abs(field).max() or 1), -1, 1)

EARTHBG='#1E1813'; YLW='#FFD21E'; YLWLT='#FFE886'; BLUE='#2E72FF'
cmap = LinearSegmentedColormap.from_list('w',[(0,'#7A3D22'),(0.5,EARTHBG),(0.72,'#1E4A78'),(0.88,BLUE),(1,'#CFE2FF')])
fig, ax = plt.subplots(figsize=(11.6,7.6)); fig.patch.set_facecolor(EARTHBG); ax.set_facecolor(EARTHBG)
ax.imshow(A.T, origin='lower', cmap=cmap, vmin=-1, vmax=1, interpolation='bilinear', extent=[0,NX,0,NY])
for g in np.arange(0,NX+1,26): ax.axvline(g,color='white',lw=0.25,alpha=0.05)
for g in np.arange(0,NY+1,26): ax.axhline(g,color='white',lw=0.25,alpha=0.05)

# spin-1 circular-polarization HELIX (the photon's identity), pseudo-3D corkscrew
s = np.linspace(-150, 150, 700); ph = k*s*1.0
Ah = 34.0
depth = np.sin(ph); hy = yc + Ah*np.cos(ph); hx = xc + s + 5.5*depth
# draw back-to-front so the corkscrew reads 3D (dim where depth<0)
order = np.argsort(depth)
for i in range(len(s)-1):
    j = i
    al = 0.30 + 0.55*(depth[j]+1)/2
    lw = 2.0 + 1.8*(depth[j]+1)/2
    ax.plot(hx[j:j+2], hy[j:j+2], color=YLW, lw=lw, alpha=al, solid_capstyle='round')
ax.plot(hx, hy, color=YLWLT, lw=0.7, alpha=0.5)             # bright thread
# propagation: v = c arrow
ax.annotate('', xy=(xc+185, yc), xytext=(xc+120, yc),
            arrowprops=dict(arrowstyle='-|>', color='#EDE6D6', lw=2.0))
ax.text(xc+152, yc+14, '$v=c$', color='#EDE6D6', ha='center', fontsize=11)
ax.set_xlim(0,NX); ax.set_ylim(0,NY); ax.set_xticks([]); ax.set_yticks([])
ax.set_title('PHOTON  —  transverse shear wave at $c$  (no wake)', color='#EDE6D6', fontsize=15, fontweight='bold', pad=10)
fig.text(0.5,0.025,'Massless transverse Cosserat shear wave: flat wavefronts $\\perp k$, propagates AT $c$ so no Mach cone; '
         'spin-1 circular-polarization helix; no localized rest-mass core',
         ha='center', color='#9CC0FF', fontsize=9.5)
for sp in ax.spines.values(): sp.set_color('#3A3320')
plt.subplots_adjust(left=0.01,right=0.99,top=0.93,bottom=0.07)
plt.savefig('/tmp/photon_still.png', dpi=150, facecolor=EARTHBG); print('rendered photon')
