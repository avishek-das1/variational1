import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#mpl.use("pgf")

#mpl.style.use("classic")
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams.update({'font.size': 32})
plt.rc('text', usetex=True)

psungt=np.loadtxt('Fig7/l-0.04_ung.txt',skiprows=1)
psgt=np.loadtxt('Fig7/l-0.04_g.txt',skiprows=1)
huungt=np.loadtxt('Fig7/l0.2_ung.txt',skiprows=1)
hugt=np.loadtxt('Fig7/l0.2_g.txt',skiprows=1)

psungl=np.loadtxt('Fig7/ps_ung.txt')
psgl=np.loadtxt('Fig7/ps_g.txt')
huungl=np.loadtxt('Fig7/hu_ung.txt')
hugl=np.loadtxt('Fig7/hu_g.txt')

fig, axs = plt.subplots(2,figsize=(12,16),sharex=True)
plt.subplots_adjust(hspace=0.1)
axsins1 = inset_axes(axs[0], width='75%', height='100%',bbox_to_anchor=(.11, .25, .5, .5),bbox_transform=axs[0].transAxes)
axsins2 = inset_axes(axs[1], width='75%', height='100%',bbox_to_anchor=(.11, .25, .5, .5),bbox_transform=axs[1].transAxes)

axs[0].loglog(psungt[:,0],psungt[:,4]/psungt[0,4],markevery=0.02,color='b',marker='o',markerfacecolor='none',lw=3,markersize=12,mew=2.5)
axs[0].loglog(psgt[:,0],psgt[:,4]/psgt[0,4],markevery=0.02,color='g',marker='s',markerfacecolor='none',lw=3,markersize=12,mew=2.5)
axsins1.plot(psungl[:,0],psungl[:,1],color='b',marker='o',fillstyle='none',lw=3,markersize=12,mew=2.5)
axsins1.plot(psgl[:,0],psgl[:,1],color='g',marker='s',fillstyle='none',lw=3,markersize=12,mew=2.5)

axs[1].loglog(huungt[:,0],huungt[:,4]/huungt[0,4],markevery=0.02,color='b',marker='o',markerfacecolor='none',lw=3,markersize=12,mew=2.5)
axs[1].loglog(hugt[:,0],hugt[:,4]/hugt[0,4],markevery=0.02,color='g',marker='s',markerfacecolor='none',lw=3,markersize=12,mew=2.5)
axsins2.plot(huungl[:,0],huungl[:,1],color='b',marker='o',fillstyle='none',lw=3,markersize=12,mew=2.5)
axsins2.plot(hugl[:,0],hugl[:,1],color='g',marker='s',fillstyle='none',lw=3,markersize=12,mew=2.5)

axs[0].set(xlim=(0.5,200),ylim=(1e-4,2),ylabel=(r'$f^{c}_{\lambda}(\tau)$'))
axs[1].set(xlim=(0.5,200),ylim=(1e-4,2),xlabel=r'$\tau$',ylabel=(r'$f^{c}_{\lambda}(\tau)$'))
axsins1.set(ylim=(1e-5,1.5),yscale='log')
axsins1.set_xlabel(r'$\lambda$',labelpad=0.0)
axsins1.set_ylabel(r'$f^{c}_{\lambda}(\tau=20)$',labelpad=0.0)
axsins2.set(ylim=(1e-1,1.5),yscale='log')
axsins2.set_xlabel(r'$\lambda$',labelpad=0.0)
axsins2.set_ylabel(r'$f^{c}_{\lambda}(\tau=20)$',labelpad=0.0)

axs[0].text(0.2,1.,r'$\mathrm{a)}$')
axs[1].text(0.2,1.,r'$\mathrm{b)}$')

legend_elements=[Line2D([0],[0],color='b',lw=3,marker='o',markersize=15,linestyle='-',mew=2.5,fillstyle='none',label=r'$\mathrm{Cloning}$'),Line2D([0],[0],color='g',lw=3,marker='s',markersize=12,linestyle='-',mew=2.5,fillstyle='none',label=r'$\mathrm{Guided~cloning}$')]
axs[0].legend(handles=legend_elements,frameon='False',framealpha=0.0,bbox_to_anchor=(0.5, 1.2),ncol=2,loc='upper center')

#plt.set_rasterized(True)
plt.savefig('Fig7.eps',bbox_inches='tight',pad_inches=0.1)
#plt.show()
