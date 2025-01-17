import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 6))

pts = [(1, 1), (5, 1), (5, 4)]
axes[0].plot([1, 5], [1, 1], color='grey', label='Matching')
axes[0].plot([1, 5], [1, 4], color='grey', label='Matching')
axes[0].plot([5, 5], [1, 4], color='grey', label='Matching')

axes[0].scatter(1, 1, color='#48c9b0', label=r'$a$')
axes[0].scatter(5, 1, color='#48c9b0', label=r'$b$')
axes[0].scatter(5, 4, color='#48c9b0', label=r'$c$')



# Annotate distances
axes[0].annotate("0.5", (0.5, 0.5), textcoords="offset points", xytext=(10, -10), fontsize=10)
axes[0].annotate("0.3", (1.5, 1.5), textcoords="offset points", xytext=(-20, -10), fontsize=10)

axes[0].axis('off')
axes[0].set_aspect('equal')

# Data for the second subplot
x_offsets = [0, 2, 4]
y1 = [2, 4, 6]
y2 = [3, 5, 7]

# Second subplot
for i in range(len(x_offsets)):
    axes[1].scatter([x_offsets[i]] * 2, [y1[i], y2[i]], s=100, c=['green', 'blue'])
    axes[1].scatter(x_offsets[i], y1[i] - 1, s=100, c='red')
    axes[1].plot([x_offsets[i], x_offsets[i]], [y1[i], y2[i]], color='black', linestyle='-', linewidth=1)
    axes[1].annotate(f"({x_offsets[i]}, {y1[i]})", (x_offsets[i], y1[i]), textcoords="offset points", xytext=(-15, 10))
    axes[1].annotate(f"({x_offsets[i]}, {y2[i]})", (x_offsets[i], y2[i]), textcoords="offset points", xytext=(-15, -15))

axes[1].set_xlim(-1, 6)
axes[1].set_ylim(0, 8)
axes[1].set_aspect('equal')

plt.savefig('Fundamentos del Análisis Matemático/Trabajo/Figures/figure-2.pdf')
