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

a20=np.loadtxt('Fig10/dist100_20.txt')
a25=np.loadtxt('Fig10/dist100_25.txt')
a30=np.loadtxt('Fig10/dist100_30.txt')
a35=np.loadtxt('Fig10/dist100_35.txt')
a40=np.loadtxt('Fig10/dist100_40.txt')

fig = plt.figure(figsize=(12,8))

plt.errorbar(a20[:,0],a20[:,1]/2.,yerr=a20[:,2]/2.,color='k',marker='o',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=20$')[0]
plt.errorbar(a25[:,0],a25[:,1]/2.,yerr=a25[:,2]/2.,color='b',marker='^',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=25$')[0]
plt.errorbar(a30[:,0],a30[:,1]/2.,yerr=a30[:,2]/2.,color='limegreen',marker='s',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=30$')[0]
plt.errorbar(a35[:,0],a35[:,1]/2.,yerr=a35[:,2]/2.,color='deepskyblue',marker='D',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=35$')[0]
plt.errorbar(a40[:,0],a40[:,1]/2.,yerr=a40[:,2]/2.,color='darkgreen',marker='x',lw=3,fillstyle='none',markersize=15,mew=2,linestyle='none',label=r'$N=40$')[0]

plt.xlabel(r'$N_{i}/N$')
plt.ylabel(r'$\langle F^{2}_{i}\rangle_{\lambda}/4\gamma k_{B} TN^{2}$')
plt.legend(frameon='False',framealpha=0.0,loc='lower center')
plt.savefig('Fig10.eps',bbox_inches='tight',pad_inches=0.1)

