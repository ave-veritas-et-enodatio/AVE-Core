"""Steady-state propagating-electron wake (logo still).  2D FDTD; source ramps on
smoothly, runs until the co-moving Mach cone is established, then we crop a
co-moving window that EXCLUDES the launch transient -> steady state only."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

NX, NY = 700, 440
cs = 1.0; dx = 1.0; dt = 0.42
v  = 2.2 * cs                            # narrower cone: sin(theta)=cs/v -> ~27 deg
omegaC = 0.95
y0 = NY/2; x0 = 45.0; nsteps = 520; sig = 2.6

P = np.zeros((NX, NY)); Pold = np.zeros((NX, NY))
xx, yy = np.mgrid[0:NX, 0:NY]
W = 50; damp = np.ones((NX, NY))
for i in range(W):
    d = 1 - 0.05*((W-i)/W)**2
    damp[i,:]*=d; damp[NX-1-i,:]*=d; damp[:,i]*=d; damp[:,NY-1-i]*=d

for n in range(nsteps):
    lap = (np.roll(P,1,0)+np.roll(P,-1,0)+np.roll(P,1,1)+np.roll(P,-1,1)-4*P)
    Pn = 2*P - Pold + (cs*dt/dx)**2*lap
    xs = x0 + v*dt*n
    env = np.tanh(n/70.0)                # smooth ramp -> no impulsive IC
    if xs < NX-80:
        Pn += np.exp(-(((xx-xs)**2+(yy-y0)**2)/(2*sig**2)))*np.sin(omegaC*dt*n)*env*0.9*dt**2
    Pn *= damp; Pold = P; P = Pn
xe = x0 + v*dt*(nsteps-1)
theta = np.degrees(np.arcsin(cs/v))
print("electron x=%.0f/%d  cone half-angle %.1f deg  |P|max %.3f" % (xe, NX, theta, np.abs(P).max()))

# ---- co-moving crop (steady state only; launch region x<ix0 excluded) ----
ix0 = int(xe-360); ix1 = int(xe+55); ix0 = max(ix0, W+5)
Pc = P[ix0:ix1, :]
A = np.clip(Pc/(np.abs(Pc).max() or 1), -1, 1)
EARTHBG='#1E1813'; YLW='#FFD21E'; YLWLT='#FFE886'; BLUE='#2E72FF'
cmap = LinearSegmentedColormap.from_list('w',[(0,'#7A3D22'),(0.5,EARTHBG),(0.72,'#1E4A78'),(0.88,BLUE),(1,'#CFE2FF')])
fig, ax = plt.subplots(figsize=(11.6, 7.6)); fig.patch.set_facecolor(EARTHBG); ax.set_facecolor(EARTHBG)
W_disp = ix1-ix0
ax.imshow(A.T, origin='lower', cmap=cmap, vmin=-1, vmax=1, interpolation='bilinear', extent=[0, W_disp, 0, NY])
for g in np.arange(0, W_disp+1, 26): ax.axvline(g, color='white', lw=0.25, alpha=0.05)
for g in np.arange(0, NY+1, 26):     ax.axhline(g, color='white', lw=0.25, alpha=0.05)
ex = xe-ix0; t = np.linspace(0,2*np.pi,260); sc = 12
kx = ex + sc*(np.sin(t)+2*np.sin(2*t)); ky = y0 + sc*(np.cos(t)-2*np.cos(2*t))
ax.plot(kx,ky,color=YLW,lw=4.6,solid_capstyle='round',alpha=0.5)
ax.plot(kx,ky,color=YLW,lw=2.7,solid_capstyle='round')
ax.plot(kx,ky,color=YLWLT,lw=0.9,solid_capstyle='round')
ax.set_xlim(0,W_disp); ax.set_ylim(0,NY); ax.set_xticks([]); ax.set_yticks([])
ax.set_title('PROPAGATING ELECTRON  —  steady-state substrate wake', color='#EDE6D6', fontsize=15, fontweight='bold', pad=10)
fig.text(0.5,0.025,'2D FDTD, co-moving window (launch transient excluded).  Mach/Cherenkov cone $\\sin\\theta=c_{slow}/v$ ($\\theta\\!\\approx\\!27^\\circ$); Compton-rate ripples',
         ha='center', color='#9CC0FF', fontsize=9.5)
for s in ax.spines.values(): s.set_color('#3A3320')
plt.subplots_adjust(left=0.01,right=0.99,top=0.93,bottom=0.07)
plt.savefig('/tmp/electron_wake.png', dpi=150, facecolor=EARTHBG); print('rendered crop', W_disp, 'x', NY)
