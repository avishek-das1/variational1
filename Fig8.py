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

delomega=np.loadtxt('Fig8/delomega2.txt')
delomegasq=np.loadtxt('Fig8/delomega2sq.txt')
delomegaerr=(delomegasq-delomega**2)**0.5

m=1
times=(np.arange(0,50)+1)/5
plt.figure(figsize=(12,8))
p1=plt.plot(times[0:-1:m],delomega[0:-1:m,0],color='k',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='-')[0]
p2=plt.plot(times[0:-1:m],delomega[0:-1:m,1],color='b',lw=3,fillstyle='none',markersize=12,mew=2,linestyle=(0,(5,5)))[0]
p3=plt.plot(times[0:-1:m],delomega[0:-1:m,2],color='g',lw=3,fillstyle='none',markersize=12,mew=2,linestyle=(0,(5,10)))[0]
p4=plt.plot(times[0:-1:m],delomega[0:-1:m,3],color='deepskyblue',lw=3,fillstyle='none',markersize=12,mew=2,linestyle=(0,(3,1,1,1,1,1)))[0]
p5=plt.plot(times[0:-1:m],delomega[0:-1:m,4],color='darkgreen',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='-.')[0]
p6=plt.plot(times[0:-1:m],delomega[0:-1:m,5],color='limegreen',lw=3,fillstyle='none',markersize=12,mew=2,linestyle=':')[0]
p7=plt.plot(times[0:-1:m],delomega[0:-1:m,6],color='c',lw=3,fillstyle='none',markersize=12,mew=2,linestyle=(0, (5,1)))[0]

m=5
plt.errorbar(times[0:-1:m],delomega[0:-1:m,0],yerr=delomegaerr[0:-1:m,0],color='k',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='none')
plt.errorbar(times[0:-1:m],delomega[0:-1:m,1],yerr=delomegaerr[0:-1:m,1],color='b',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='none')
plt.errorbar(times[0:-1:m],delomega[0:-1:m,2],yerr=delomegaerr[0:-1:m,2],color='g',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='none')
plt.errorbar(times[0:-1:m],delomega[0:-1:m,3],yerr=delomegaerr[0:-1:m,3],color='deepskyblue',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='none')
plt.errorbar(times[0:-1:m],delomega[0:-1:m,4],yerr=delomegaerr[0:-1:m,4],color='darkgreen',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='none')
plt.errorbar(times[0:-1:m],delomega[0:-1:m,5],yerr=delomegaerr[0:-1:m,5],color='limegreen',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='none')
plt.errorbar(times[0:-1:m],delomega[0:-1:m,6],yerr=delomegaerr[0:-1:m,6],color='c',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='none')

plt.axvspan(4, 7, alpha=0.5, color='lightgrey')
plt.xlabel(r'$\Delta t$')
plt.ylabel(r'$\Omega_{n}(\Delta t)$')

plt.legend([p1,p4,p2,p5,p3,p6,p7],[r'$\Omega_{1}$',r'$\Omega_{-1}$',r'$\Omega_{2}$',r'$\Omega_{-2}$',r'$\Omega_{3}$',r'$\Omega_{-3}$',r'$\Omega_{0}$'],frameon='False',framealpha=0.0,bbox_to_anchor=(0.5, 1.15),ncol=4,loc='upper center',borderpad=0.0,labelspacing=0.0,handletextpad=0.5,borderaxespad=0.0)

plt.savefig('Fig8.eps',bbox_inches='tight',pad_inches=0.1)
#plt.show()
