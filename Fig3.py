import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams.update({'font.size': 32})
plt.rc('text', usetex=True)
#mpl.rcParams.update({'font.family': 'serif'})
#mpl.rcParams.update({'font.serif': 'DejaVuSerif'})

y0=np.loadtxt('Fig3/lam-1.1.txt')
y1=np.loadtxt('Fig3/lam-0.2.txt')
y2=np.loadtxt('Fig3/lam0.5.txt')

Mx2=44
Mv2=20
Mx15=77
Mv15=12

with open('Fig3/lam2_exact.txt') as f1:
    Mx2, Mv2 = [int(x) for x in next(f1).split()]
    array1 = np.asarray([[float(x) for x in line.split()] for line in f1])
with open('Fig3/lam2_vmc.txt') as f2:
    Mx2, Mv2 = [int(x) for x in next(f2).split()]
    array2 = np.asarray([[float(x) for x in line.split()] for line in f2])

with open('Fig3/lam-1.5_exact.txt') as f3:
    Mx15, Mv15 = [int(x) for x in next(f3).split()]
    array3 = np.asarray([[float(x) for x in line.split()] for line in f3])
with open('Fig3/lam-1.5_vmc.txt') as f4:
    Mx15, Mv15 = [int(x) for x in next(f4).split()]
    array4 = np.asarray([[float(x) for x in line.split()] for line in f4])


xs2=array1[0:-1:Mv2,0]
vs2=array1[0:Mv2,1]
xs15=array3[0:-1:Mv15,0]
vs15=array3[0:Mv15,1]

lam2exact=np.reshape(array1[:,2],(Mx2,Mv2),'C')
lam2vmc=np.reshape(array2[:,2],(Mx2,Mv2),'C')
lam15exact=np.reshape(array3[:,2],(Mx15,Mv15),'C')
lam15vmc=np.reshape(array4[:,2],(Mx15,Mv15),'C')

fig = plt.figure(figsize=(12,16))
plt.subplots_adjust(hspace=0.15,wspace=0.25)
gs = gridspec.GridSpec(2, 4)
ax1=fig.add_subplot(gs[0,0])
ax2=fig.add_subplot(gs[0,1])
ax3=fig.add_subplot(gs[0,2])
ax4=fig.add_subplot(gs[0,3])
ax5=fig.add_subplot(gs[1,:])

ax5.errorbar(y0[:,0],y0[:,1],yerr=y0[:,2],marker='o',lw=3,markersize=15,color='k',fillstyle='none',mew=2.5)
plt.errorbar(y1[:,0],y1[:,1],yerr=y1[:,2],marker='s',lw=3,markersize=15,color='g',fillstyle='none',mew=2.5)
plt.errorbar(y2[:,0],y2[:,1],yerr=y2[:,2],marker='^',lw=3,markersize=15,color='b',fillstyle='none',mew=2.5)

legend_elements=[Line2D([0],[0],color='k',lw=3,marker='o',markersize=15,fillstyle='none',mew=2.5,label=r'$\lambda=-1.1$'),Line2D([0],[0],color='g',lw=3,marker='s',markersize=15,fillstyle='none',mew=2.5,label=r'$\lambda=-0.2$'),Line2D([0],[0],color='b',lw=3,marker='^',markersize=15,fillstyle='none',mew=2.5,label=r'$\lambda=0.5$')]
ax5.legend(handles=legend_elements,frameon='False',framealpha=0.0,handletextpad=0)
ax5.set(xlabel=r'$\ell$')
ax5.set(ylabel=r'$|\kappa_{\ell}/\ell!|$')
ax5.set(ylim=(-5,0))
ax5.set(yticks=np.arange(-5,1,1),yticklabels= (r'$10^{-5}$',r'$10^{-4}$',r'$10^{-3}$',r'$10^{-2}$',r'$10^{-1}$',r'$10^{0}$'))

ax5.text(0.0,6.2,r'$\mathrm{a)}$')
ax5.text(0.0,-0.2,r'$\mathrm{b)}$')
ax1.text(-2,6.2,r'$v$')
ax2.text(-2,6.2,r'$v$')
ax1.text(3.5,6.2,r'$v$')
ax1.text(6.2,6.2,r'$v$')

ax1.text(-2.6,0.8,r'$\mathrm{Exact}$')
ax2.text(-3.0,0.8,r'$\mathrm{Optimized}$')
ax1.text(3.1,0.8,r'$\mathrm{Exact}$')
ax1.text(5.5,0.8,r'$\mathrm{Optimized}$')

ax1.imshow(lam15exact,extent=(vs15[0],vs15[-1],xs15[-1],xs15[0] ),interpolation='gaussian',cmap=cm.winter,vmin=-4,vmax=0,aspect='auto')
ax2.imshow(lam15vmc,extent=(vs15[0],vs15[-1],xs15[-1],xs15[0] ),interpolation='gaussian',cmap=cm.winter,vmin=-4,vmax=0,aspect='auto')
ax3.imshow(lam2exact,extent=(vs2[0],vs2[-1],xs2[-1],xs2[0] ),interpolation='gaussian',cmap=cm.winter,vmin=3,vmax=7,aspect='auto')
ax4.imshow(lam2vmc,extent=(vs2[0],vs2[-1],xs2[-1],xs2[0] ),interpolation='gaussian',cmap=cm.winter,vmin=3,vmax=7,aspect='auto')

CS1=ax1.contour(lam15exact,extent=(vs15[0],vs15[-1],xs15[-1],xs15[0] ),vmin=-3,vmax=-1,colors='k',origin='upper', linestyles='dashed',linewidths=3,levels=(-4,-3,-2,-1,0))
plt.setp(CS1.collections[2],linestyle='-')
plt.setp(CS1.collections[0:2],linestyle='dotted')
CS2=ax2.contour(lam15vmc,extent=(vs15[0],vs15[-1],xs15[-1],xs15[0] ),vmin=-3,vmax=-1,colors='k',origin='upper', linestyles='dashed',linewidths=3,levels=(-4,-3,-2,-1,0))
plt.setp(CS2.collections[2],linestyle='-')
plt.setp(CS2.collections[0:2],linestyle='dotted')
CS3=ax3.contour(lam2exact,extent=(vs2[0],vs2[-1],xs2[-1],xs2[0] ),vmin=4,vmax=6,colors='k',origin='upper', linestyles='dashed',linewidths=3,levels=(3,4,5,6,7))
plt.setp(CS3.collections[2],linestyle='-')
plt.setp(CS3.collections[0:2],linestyle='dotted')
CS4=ax4.contour(lam2vmc,extent=(vs2[0],vs2[-1],xs2[-1],xs2[0] ),vmin=4,vmax=6,colors='k',origin='upper', linestyles='dashed',linewidths=3,levels=(3,4,5,6,7))
plt.setp(CS4.collections[2],linestyle='-')
plt.setp(CS4.collections[0:2],linestyle='dotted')

ax2.set(yticks=[])
ax3.set(yticks=[])
ax4.set(yticks=[])
ax1.set(xticks=[-3,-1])
ax2.set(xticks=[-3,-1])
ax3.set(xticks=[4,6])
ax4.set(xticks=[4,6])
ax1.set(ylabel=r'$x$')

plt.text(1.1, 1.1, r'$\lambda=-1.5$',horizontalalignment='center',transform = ax1.transAxes)
plt.text(1.1, 1.1, r'$\lambda=2.0$',horizontalalignment='center',transform = ax3.transAxes)

plt.savefig('Fig3.eps',bbox_inches='tight',pad_inches=0.1)
#plt.show()
#print(mpl.__version__)

