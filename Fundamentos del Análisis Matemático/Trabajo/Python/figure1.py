import matplotlib.pyplot as plt

# Example data
D1 = [(1, 5), (7, 9), (1, 2)]
D2 = [(2, 7), (6, 9)]

x1, y1 = zip(*D1)
x2, y2 = zip(*D2)

plt.rcParams['text.usetex'] = True

plt.plot([x1[0], x2[0]], [y1[0], y2[0]], color='grey', label='Matching')
plt.plot([x1[1], x2[1]], [y1[1], y2[1]], color='grey')
plt.plot([x1[2], 1.5], [y1[2], 1.5], color='grey')

plt.plot([0, 10], [0, 10], 'k--', label=r'$\Delta$')

plt.scatter(x1, y1, color='#48c9b0', label=r'$D_1$')
plt.scatter(x2, y2, color='#c948a1', label=r'$D_1$')

# Labels and legend
plt.xlabel(r'X')
plt.ylabel(r'Y')
plt.legend(loc='lower right')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('Fundamentos del Análisis Matemático/Trabajo/Figures/figure-1.pdf')
