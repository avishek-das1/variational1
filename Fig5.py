import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from matplotlib import cm

norm = mpl.colors.Normalize(vmin=-1.0, vmax=1.0)
cmap = cm.winter
m = cm.ScalarMappable(norm=norm, cmap=cmap)

#mpl.style.use("classic")
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams.update({'font.size': 32})
plt.rc('text', usetex=True)

l0=np.loadtxt('Fig5/lam0.0.txt')
lm1=np.loadtxt('Fig5/lam-1.0.txt')
lm02=np.loadtxt('Fig5/lam-0.2.txt')
l02=np.loadtxt('Fig5/lam0.2.txt')
l05=np.loadtxt('Fig5/lam0.5.txt')
l1=np.loadtxt('Fig5/lam1.0.txt')

plt.figure(figsize=(12,8))
p0,=plt.plot(l0[:,0],l0[:,1],fillstyle='none',lw=4,linestyle='-',color='k')
p1,=plt.plot(lm1[:,0],lm1[:,1],fillstyle='none',lw=4,linestyle='--',color='deepskyblue')
p3,=plt.plot(lm02[:,0],lm02[:,1],fillstyle='none',lw=4,linestyle=(0,(5,10)),color='b')
p6,=plt.plot(l02[:,0],l02[:,1],fillstyle='none',lw=4,linestyle=(0,(3,1,1,1,1,1)),color='darkgreen')
p7,=plt.plot(l05[:,0],l05[:,1],fillstyle='none',lw=4,linestyle='-.',color=cmap(norm(0.5)))
p8,=plt.plot(l1[:,0],l1[:,1],fillstyle='none',lw=4,linestyle=':',color='limegreen')

plt.ylim(-7.5,35.)
plt.xlim(-1,40.*2.**(1./6))
plt.xlabel(r'$r$')
plt.ylabel(r'$V^{(2)}(r)$')
plt.legend([p1,p3,p0,p6,p7,p8],[r'$\lambda=-1.0$',r'$\lambda=-0.2$',r'$\lambda=0.0$',r'$\lambda=0.2$',r'$\lambda=0.5$',r'$\lambda=1.0$'],frameon='False',framealpha=0.0,loc='upper right',handlelength=2.5)
plt.savefig('Fig5.eps',bbox_inches='tight',pad_inches=0.1)
#plt.show()
