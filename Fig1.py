import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from matplotlib.patches import Rectangle

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

#mpl.style.use("classic")
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams.update({'font.size': 32})
plt.rc('text', usetex=True)

psiov=np.loadtxt('Fig1/exact_ov.txt')
psiun=np.loadtxt('Fig1/exact_un.txt')
vmcov=np.loadtxt('Fig1/vmc_ov.txt')
vmcun=np.loadtxt('Fig1/vmc_un.txt')
rateov=np.loadtxt('Fig1/rateov_var.txt')
rateun=np.loadtxt('Fig1/rateun_var.txt')
rateove=np.loadtxt('Fig1/rateov_ex.txt')
rateune=np.loadtxt('Fig1/rateun_ex.txt')

fig, axs = plt.subplots(2,figsize=(12,16))
plt.subplots_adjust(hspace=0.2)
arr = mpimg.imread('Fig1/F1_pic.png')
p1,=axs[0].plot(psiov[:,0],psiov[:,1],'b',lw=3,linestyle='-')
p2,=axs[0].plot(psiun[:,0],psiun[:,1],'g',lw=3,linestyle='--')
p3,=axs[0].plot(vmcov[:,0],vmcov[:,1],marker='o',fillstyle='none',lw=5,linestyle='none',markersize=15,mew=2.5,color='b')
p4,=axs[0].plot(vmcov[:,0],vmcun[:,1],marker='s',fillstyle='none',lw=5,linestyle='none',markersize=15,mew=2.5,color='g')
axs[1].plot(rateove[:,0],rateove[:,1],color='b',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='-')
axs[1].plot(rateune[:,0],rateune[:,1],color='g',lw=3,fillstyle='none',markersize=12,mew=2,linestyle='--')
axs[1].plot(rateov[:,0],rateov[:,1],marker='o',color='b',lw=3,fillstyle='none',markersize=15,mew=2.5,linestyle='none')
axs[1].plot(rateun[:,0],rateun[:,1],marker='s',color='g',lw=3,fillstyle='none',markersize=15,mew=2.5,linestyle='none')

axs[0].set(xlabel=r'$\lambda$')
axs[0].set(ylabel=r'$\psi(\lambda)$')
axs[1].set(xlabel=r'$J$')
axs[1].set(ylabel=r'$I(J)$')

#legend_elements=[Line2D([0],[0],color='g',lw=3,marker='s',markersize=15,linestyle='--',mew=2.5,fillstyle='none',label=r'$m/\gamma=1$'),Line2D([0],[0],color='b',lw=3,marker='o',markersize=15,linestyle='-',mew=2.5,fillstyle='none',label=r'$m/\gamma\to0$')]
#axs[0].legend(handles=legend_elements,frameon='False',framealpha=0.0,bbox_to_anchor=(0.5, 1.2),ncol=2,loc='upper center')
legend_handle = [extra, extra, extra, extra, p1, p3, extra, p2, p4]
label_row_1 = ["", r"$\mathrm{Exact}$", r"$\mathrm{Estimated}$"]
label_j_1 = [r"$m/\gamma t^{*}\to0$"]
label_j_2 = [r"$m/\gamma t^{*}=1$"]
label_empty = [""]
legend_labels = np.concatenate([label_row_1, label_j_1, label_empty * 2, label_j_2, label_empty * 2])
axs[0].legend(legend_handle, legend_labels, 
          loc = 'upper center', ncol = 3, columnspacing=1.7,handletextpad = -3.0,borderpad=0.0,frameon='False',framealpha=0.0)#,bbox_to_anchor=(0.5, 1.2))

imagebox = OffsetImage(arr, zoom=0.25)
ab = AnnotationBbox(imagebox, (0.5, 1.2),frameon=False)
axs[1].add_artist(ab)

axs[0].text(-2.0,0.6,r'$\mathrm{a)}$')
axs[0].text(-2.0,-0.3,r'$\mathrm{b)}$')

plt.savefig('Fig1.eps',bbox_inches='tight',pad_inches=0.1)
#plt.show()
