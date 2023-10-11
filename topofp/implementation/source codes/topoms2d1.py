import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.spatial import Delaunay
import networkx as nx


def scalar_field_function(x, y):
    return (np.sin(2*x) * np.cos(2*y)) +(x+y)


x = np.linspace(0 * np.pi, 2 * np.pi, 100)
y = np.linspace(0 * np.pi, 2 * np.pi, 100)
X, Y = np.meshgrid(x, y)

Z = scalar_field_function(X, Y)


local_min = argrelextrema(Z, np.less)
local_max = argrelextrema(Z, np.greater)

all_critical_points = np.hstack((local_min, local_max))
xcritic = all_critical_points[1] * (x[1] - x[0]) + x[0]
ycritic = all_critical_points[0] * (y[1] - y[0]) + y[0]

tri = Delaunay(np.column_stack((xcritic, ycritic)))


G = nx.Graph()
for simplex in tri.simplices:
    for i in range(3):
        a, b = sorted((simplex[i], simplex[(i + 1) % 3]))
        G.add_edge(a, b)

# Plot the scalar field
plt.imshow(Z, cmap='magma', extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', alpha=0.8)
plt.colorbar(label='sin(2x)cos(2y)+x+y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Morse-Smale Complex for sin(2x)cos(2y)+x+y')

# Plot the Morse-Smale complex
for edge in G.edges:
    plt.plot([xcritic[edge[0]], xcritic[edge[1]]],
             [ycritic[edge[0]], ycritic[edge[1]]], 'k-')

plt.scatter(local_min[1] * (x[1] - x[0]) + x[0], local_min[0] * (y[1] - y[0]) + y[0], c='red', marker='o', s=50, label='Loc Minima')
plt.scatter(local_max[1] * (x[1] - x[0]) + x[0], local_max[0] * (y[1] - y[0]) + y[0], c='blue', marker='x', s=50, label='Loc Maxima')

plt.legend()
plt.show()
