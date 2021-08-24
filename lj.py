import numpy as np
import sys, matplotlib
matplotlib.rc('text', usetex=True)
from matplotlib.ticker import MaxNLocator
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size'] = 22
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'figure.autolayout': True})
#---------------------------------------------------------------------------------------#
fig, ax = plt.subplots()
r = np.arange(0.5,5, 0.001)
rcut = 2.0**(1/6.0)
#---------------------------------------------------------------------------------------#
# LJ
sigma = 1.0
e2 = 1
sbr = sigma/r
ulj = 4 * e2 * (sbr**12 - sbr**6)
ax.plot(r, ulj, 'r', label=r"$U_{LJ}$")
#---------------------------------------------------------------------------------------#
# WCA: Harder repulsion
rsigma = 2.0; rbr = rsigma/r
eR = 0.05
uwca = 4* eR * ( rbr**12 - rbr**6)
uwca[r>=rcut*rsigma]=uwca.min()
uwca -= uwca.min()
for eR in [0.0005, 0.005, 0.01, 0.05, 0.1]:
	uwca = 4* eR * ( rbr**12 - rbr**6)
	uwca[r>=rcut*rsigma]=uwca.min()
	uwca -= uwca.min()
	ax.plot(r, ulj+uwca, label=eR)
#ax.axvline(x=rsigma, color='k', linestyle='--')
#---------------------------------------------------------------------------------------#
# Soft repulsion
rsigma = 2.5; rbr = rsigma/r
eR = 0.1
usoft = eR * ( (rbr)**6 -1 )
usoft[r>=rsigma]=0.0
#ax.plot(r, usoft, 'g', label=r"$U_{R}$")
#ax.axvline(x=rsigma, color='k', linestyle='--')
#---------------------------------------------------------------------------------------#
ax.set_ylim([-1.5,3])
ax.set_xlim([0.5,3])
ax.axhline(y=0.0, color='k', linestyle='--')
ax.legend(loc='best', frameon=False, prop={'size':18})
ax.set_xlabel(r"$r [\sigma]$")
ax.tick_params(axis='x', pad=8)
ax.tick_params(axis='y', pad=8)
ax.xaxis.labelpad = 15
ax.yaxis.labelpad = 15
fig.savefig('clj.png', transparent=True, dpi=1200)
plt.show()
