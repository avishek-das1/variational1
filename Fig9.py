import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams.update({'font.size': 32})
plt.rc('text', usetex=True)

ldf=np.loadtxt('Fig9/scgferr.txt')
rho=np.loadtxt('Fig9/densityerr.txt')

plt.figure(figsize=(12,8))
plt.plot(np.arange(15),ldf,color='g',lw=3,marker='s',markersize=15,mew=2.5,fillstyle='none',label=r'$\delta\psi(\lambda)$')
plt.plot(np.arange(15),rho,color='b',lw=3,marker='^',markersize=15,mew=2.5,fillstyle='none',label=r'$D(\rho^{ss}_{u}||\rho_{\lambda})$')

plt.yscale('log')
plt.ylabel(r'$\mathrm{Error}$')
plt.xlabel(r'$\mathrm{Optimization~steps}$')
plt.legend(frameon='False',framealpha=0.0,loc='lower left')
plt.savefig('Fig9.eps',bbox_inches='tight',pad_inches=0.1)
#plt.show()

