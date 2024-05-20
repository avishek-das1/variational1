import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.gridspec as gridspec

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams.update({'font.size': 32})
plt.rc('text', usetex=True)

a20=np.loadtxt('Fig4/SCGF_20.txt')
a25=np.loadtxt('Fig4/SCGF_25.txt')
a30=np.loadtxt('Fig4/SCGF_30.txt')
a35=np.loadtxt('Fig4/SCGF_35.txt')
a40=np.loadtxt('Fig4/SCGF_40.txt')

b20=np.loadtxt('Fig4/SCGF_20_hu.txt')
b25=np.loadtxt('Fig4/SCGF_25_hu.txt')
b30=np.loadtxt('Fig4/SCGF_30_hu.txt')
b35=np.loadtxt('Fig4/SCGF_35_hu.txt')
b40=np.loadtxt('Fig4/SCGF_40_hu.txt')

c20=np.loadtxt('Fig4/act_20.txt')
c25=np.loadtxt('Fig4/act_25.txt')
c30=np.loadtxt('Fig4/act_30.txt')
c35=np.loadtxt('Fig4/act_35.txt')
c40=np.loadtxt('Fig4/act_40.txt')

arr1 = mpimg.imread('Fig4/F10_pic1.png')
arr2 = mpimg.imread('Fig4/F10_pic2.png')

fig = plt.figure(figsize=(24,8))
plt.subplots_adjust(wspace=0.3)
gs = gridspec.GridSpec(1, 2)
axs=[fig.add_subplot(gs[0,0]),fig.add_subplot(gs[0,1])]

axins = inset_axes(axs[0], width='50%', height='50%',loc=1)

axs[0].errorbar(a20[:,0],a20[:,1],yerr=a20[:,2],color='k',marker='o',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]
axs[0].errorbar(a25[:,0],a25[:,1],yerr=a25[:,2],color='b',marker='^',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]
axs[0].errorbar(a30[:,0],a30[:,1],yerr=a30[:,2],color='limegreen',marker='s',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]
axs[0].errorbar(a35[:,0],a35[:,1],yerr=a35[:,2],color='deepskyblue',marker='D',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]
axs[0].errorbar(a40[:,0],a40[:,1],yerr=a40[:,2],color='darkgreen',marker='x',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]

axins.errorbar(b20[:,0],b20[:,1],yerr=b20[:,2],color='k',marker='o',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]
axins.errorbar(b25[:,0],b25[:,1],yerr=b25[:,2],color='b',marker='^',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]
axins.errorbar(b30[:,0],b30[:,1],yerr=b30[:,2],color='limegreen',marker='s',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]
axins.errorbar(b35[:,0],b35[:,1],yerr=b35[:,2],color='deepskyblue',marker='D',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]
axins.errorbar(b40[:,0],b40[:,1],yerr=b40[:,2],color='darkgreen',marker='x',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none')[0]

p20=axs[1].errorbar(c20[:,0],c20[:,1],yerr=c20[:,2],color='k',marker='o',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=20$')[0]
p25=axs[1].errorbar(c25[:,0],c25[:,1],yerr=c25[:,2],color='b',marker='^',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=25$')[0]
p30=axs[1].errorbar(c30[:,0],c30[:,1],yerr=c30[:,2],color='limegreen',marker='s',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=30$')[0]
p35=axs[1].errorbar(c35[:,0],c35[:,1],yerr=c35[:,2],color='deepskyblue',marker='D',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=35$')[0]
p40=axs[1].errorbar(c40[:,0],c40[:,1],yerr=c40[:,2],color='darkgreen',marker='x',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=40$')[0]

imagebox1 = OffsetImage(arr1, zoom=0.12)
ab1 = AnnotationBbox(imagebox1, (0.5, -0.4),frameon=False)
axs[1].add_artist(ab1)
imagebox2 = OffsetImage(arr2, zoom=0.12)
ab2 = AnnotationBbox(imagebox2, (-0.5, -0.4),frameon=False)
axs[1].add_artist(ab2)

axs[0].text(-1.15,0.65,r'$\mathrm{a)}$')
axs[0].text(1.3,0.65,r'$\mathrm{b)}$')

axs[0].set(xlabel=r'$\lambda$',ylabel=r'$\psi(\lambda)/N^{2}$')
axins.set(xlabel=r'$\lambda$',ylabel=r'$\psi(\lambda)/N$')
axs[1].set(xlabel=r'$\lambda$',ylabel=r'$\langle K\rangle_{\lambda}/N^{2}$',ylim=(-1.4,0.2))
axs[1].legend(frameon='False',framealpha=0.0,loc='center right',bbox_to_anchor=(1.45, 0.5),handletextpad=0)
#axs[1].legend(frameon='False',framealpha=0.0,loc='lower right',bbox_to_anchor=(0.85, 0.0),handletextpad=0)

plt.savefig('Fig4.eps',bbox_inches='tight',pad_inches=0.1)

