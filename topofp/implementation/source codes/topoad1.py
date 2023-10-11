#linear version
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

# Define the scalar field function
def scalar_field_function(x, y):
    return np.sin(x) * np.cos(y)

# Create a mesh grid for the scalar field
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.linspace(-2 * np.pi, 2 * np.pi, 100)
X, Y = np.meshgrid(x, y)

# Calculate the scalar field values
Z = scalar_field_function(X, Y)

# Find critical points
local_min = argrelextrema(Z, np.less)
local_max = argrelextrema(Z, np.greater)

# Visualize the scalar values for critical points
plt.plot(x[local_min[1]], Z[local_min], 'ro', label='Local Minima')
plt.plot(x[local_max[1]], Z[local_max], 'bx', label='Local Maxima')

plt.xlabel('x')
plt.ylabel('sin(x)cos(y)')
plt.title('Critical Points of the Scalar Field sin(x)cos(y)')
plt.legend()
plt.show()
