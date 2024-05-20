import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#mpl.style.use("classic")
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams.update({'font.size': 32})
plt.rc('text', usetex=True)

rdfps=np.loadtxt('Fig6/rdf_ps.txt')
rdfhu=np.loadtxt('Fig6/rdf_hu.txt')
struct=np.loadtxt('Fig6/struct.txt')

fig, axs = plt.subplots(2, figsize=(12,14))
axins = inset_axes(axs[0], width='40%', height='35%',loc=1)
#plt.subplots_adjust(hspace=0.)

axs[0].plot(rdfps[:,0],rdfps[:,1],color='b',lw=3)
axins.plot(rdfhu[:,0],rdfhu[:,1],color='b',lw=3)
axs[1].plot(struct[:,0],struct[:,1],marker='o',fillstyle='none',mew=2,linestyle='none',markersize=15,color='k',label=r'$N=20$')
axs[1].plot(struct[:,0],struct[:,2],marker='s',fillstyle='none',mew=2,linestyle='none',markersize=15,color='darkgreen',label=r'$N=30$')
axs[1].plot(struct[:,0],struct[:,3],marker='D',fillstyle='none',mew=2,linestyle='none',markersize=15,color='deepskyblue',label=r'$N=40$')
axs[1].plot(struct[:,0],struct[:,4],marker='^',fillstyle='none',mew=2,linestyle='none',markersize=15,color='b',label=r'$N=80$')

axs[0].set(xlabel=r'$r$',ylabel=r'$g(r)$',ylim=(-2,37),xlim=(0,6.5))
axins.set(ylabel=r'$g(r)$',ylim=(-0.1,2),xlim=(0,6.5))
axins.set_xlabel(xlabel=r'$r$',labelpad=0.0)
axs[1].set(xlabel=r'$q$',ylabel=r'$S(q)$',ylim=(0,0.3*2.*np.pi),xlim=(0,23.))
axs[1].legend(frameon='False',framealpha=0.0,ncol=2,handletextpad=0,columnspacing=0,labelspacing=0.0,loc='lower right')

axs[0].text(-0.7,35,r'$\mathrm{a)}$')
axs[0].text(-0.7,-12,r'$\mathrm{b)}$')

plt.savefig('Fig6.eps',bbox_inches='tight',pad_inches=0.1)
