import numpy as np
import matplotlib.pyplot as plt

# Define the scalar field function
def scalar_field_function(x, y):
    return np.sin(x) * np.cos(y)

# Create a mesh grid for the scalar field
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.linspace(-2 * np.pi, 2 * np.pi, 100)
X, Y = np.meshgrid(x, y)

# Calculate the scalar field values
Z = scalar_field_function(X, Y)

# Visualize the scalar field using a heatmap
plt.imshow(Z, cmap='viridis', extent=[x.min(), x.max(), y.min(), y.max()])
plt.colorbar(label='sin(x)cos(y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scalar Field sin(x)cos(y)')

plt.show()