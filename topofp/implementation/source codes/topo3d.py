import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import argrelextrema

# Define the scalar field function
def scalar_field_function(x, y):
    return (np.sin(x) * np.cos(y)) + x + y

# Create a mesh grid for the scalar field
x = np.linspace(0 * np.pi, 2 * np.pi, 100)
y = np.linspace(0 * np.pi, 2 * np.pi, 100)
X, Y = np.meshgrid(x, y)

# Calculate the scalar field values
Z = scalar_field_function(X, Y)

# Find critical points
local_min = argrelextrema(Z, np.less)
local_max = argrelextrema(Z, np.greater)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the scalar field
ax.plot_surface(X, Y, Z, cmap='magma', alpha=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('sin(x)cos(y)+x+y')
ax.set_title('Scalar Field sin(x)cos(y)+x+y')

# Combine local minima and maxima
all_critical_points = np.hstack((local_min, local_max))
xcritic = all_critical_points[1] * (x[1] - x[0]) + x[0]
ycritic = all_critical_points[0] * (y[1] - y[0]) + y[0]
zcritic = scalar_field_function(xcritic, ycritic)

# Plot critical points
ax.scatter(xcritic, ycritic, zcritic, c='red', marker='o', s=100, label='Critical Points', depthshade=False)

plt.legend()
plt.show()
