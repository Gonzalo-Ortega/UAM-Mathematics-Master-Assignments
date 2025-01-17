import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
fig, axes = plt.subplots(1, 2, gridspec_kw={'wspace': 0.5})

axes[0].plot([8, 40], [8, 8], color='grey')
axes[0].annotate(r'$4$', (24, 4.8))
                 
axes[0].plot([8, 40], [8, 32], color='grey')
axes[0].annotate(r'$5$', (24, 22.4))

axes[0].plot([40, 40], [8, 32], color='grey')
axes[0].annotate(r'$3$', (40.8, 18.4))

axes[0].scatter(8, 8, color='#48c9b0')
axes[0].annotate(r'$x_1$', (4, 6.4))

axes[0].scatter(40, 8, color='#c948a1')
axes[0].annotate(r'$x_2$', (41.6, 6.4))

axes[0].scatter(40, 32, color='#c9b048')
axes[0].annotate(r'$x_3$', (41.6, 30.4))

axes[0].set_xlim(0, 48)
axes[0].set_ylim(0, 48)
axes[0].axis('off')
axes[0].set_aspect('equal')

# Data for the second subplot
axes[1].scatter([0, 12, 24], [12, 28, 41], color='#48c9b0', label=r'$D_{x_1}$')
axes[1].scatter([0, 12, 24], [16, 24, 39], color='#c948a1', label=r'$D_{x_2}$')
axes[1].scatter([0, 12, 24], [17, 27, 36], color='#c9b048', label=r'$D_{x_3}$')

plt.plot([0, 42], [0, 42], 'k--', label=r'$\Delta$')

axes[0].set_xlim(0, 42)
axes[0].set_ylim(0, 42)
axes[1].set_aspect('equal')
plt.legend(loc='lower right')

plt.savefig('Fundamentos del Análisis Matemático/Trabajo/Figures/figure-2.pdf')
