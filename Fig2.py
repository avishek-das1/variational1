import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

#mpl.style.use("classic")
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams.update({'font.size': 32})
plt.rc('text', usetex=True)

aux=np.loadtxt('Fig2/exact_forces.txt')
a=np.loadtxt('Fig2/vmc_coeff.txt')
m0=np.loadtxt('Fig2/vmcerr_M1_0.txt')
m1=np.loadtxt('Fig2/vmcerr_M1_1.txt')
m2=np.loadtxt('Fig2/vmcerr_M1_2.txt')

N=np.shape(a)[0]
M=3
p=100
x=np.linspace(0.0,2.*np.pi,p)
y=np.zeros((N,p))
gamma=1.0
D=1.0
fig, axs = plt.subplots(2,figsize=(12,16))
plt.subplots_adjust(hspace=0.2)
for i in range(N):
    #print(i)
    for j in range(M):
        for k in range(p):
            y[i,k]+=a[i,j+1]*np.cos((j+1)*x[k])+a[i,j+M+1]*np.sin((j+1)*x[k])
    y[i,:]+=gamma+2.*D*a[i,0]
    if i<10:
        axs[0].plot(aux[p*i:p*(i+1),0],aux[p*i:p*(i+1),1],'lightskyblue',lw=3)
        axs[0].plot(x,y[i,:],'g--',lw=3)
    elif i>10:
        axs[0].plot(aux[p*i:p*(i+1),0],aux[p*i:p*(i+1),1],'lightskyblue',lw=3)
        axs[0].plot(x,y[i,:],'g--',lw=3)
    else:
        axs[0].plot(aux[p*i:p*(i+1),0],aux[p*i:p*(i+1),1],'lightskyblue',lw=6)
        axs[0].plot(aux[p*i:p*(i+1),0],aux[p*i:p*(i+1),1],'g--',lw=6)

axs[1].errorbar(m0[:,0],m0[:,1],m0[:,2],color='k',lw=2.5,marker='o',markersize=10,mew=2.5,linestyle='none',fillstyle='none',label=r'$M_{1}=0;$')
axs[1].errorbar(m1[:,0],m1[:,1],m1[:,2],color='b',lw=2.5,marker='^',markersize=10,mew=2.5,linestyle='none',fillstyle='none',label=r'$M_{1}=1;$')
axs[1].errorbar(m2[:,0],m2[:,1],m2[:,2],color='g',lw=2.5,marker='s',markersize=10,mew=2.5,linestyle='none',fillstyle='none',label=r'$M_{1}=2$')

axs[0].set(xlabel=r'$x$')
axs[0].set(ylabel=r'$u^{(1)}(x)$')
axs[1].set(xlabel=r'$\lambda$')
axs[1].set(ylabel=r'$|\delta\psi(\lambda)|$')
axs[1].set(ylim=(-5,2))
axs[1].set(yticks=np.arange(-5,3,1),yticklabels= (r'$10^{-5}$',r'$10^{-4}$',r'$10^{-3}$',r'$10^{-2}$',r'$10^{-1}$',r'$10^{0}$',r'$10^{1}$',r'$10^{2}$'))
axs[1].legend(frameon='False',framealpha=0.0,ncol=3,loc='upper center',columnspacing=0,handletextpad=0)

axs[0].text(-1.5,9,r'$\mathrm{a)}$')
axs[0].text(-1.5,-17,r'$\mathrm{b)}$')

plt.savefig('Fig2.eps',bbox_inches='tight',pad_inches=0.1)
#plt.show()
