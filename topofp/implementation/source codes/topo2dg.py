import numpy as np

# Define the scalar field function
def scalar_field_function(x, y):
    return np.sin(x) * np.cos(y)

# Create a scalar field
grid_size = 100
x_values = np.linspace(0, 2 * np.pi, grid_size)
y_values = np.linspace(0, 2 * np.pi, grid_size)

X, Y = np.meshgrid(x_values, y_values)
scalar_field = scalar_field_function(X, Y)

# Compute the gradient using NumPy
gradient = np.gradient(scalar_field)

# Print the gradient
print("Gradient:", gradient)