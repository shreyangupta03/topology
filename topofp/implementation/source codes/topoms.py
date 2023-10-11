import numpy as np
import vtk
from ttk import ttk

# Define the scalar field function
def scalar_field_function(x, y):
    return np.sin(x) * np.cos(y)

# Create a scalar field
grid_size = 100
x_values = np.linspace(0, 2 * np.pi, grid_size)
y_values = np.linspace(0, 2 * np.pi, grid_size)

X, Y = np.meshgrid(x_values, y_values)
scalar_field = scalar_field_function(X, Y)

# Create a VTK structured points dataset
vtk_data = vtk.vtkStructuredPoints()
vtk_data.SetDimensions(grid_size, grid_size, 1)

origin = (0, 0, 0)
spacing = (2 * np.pi / grid_size, 2 * np.pi / grid_size, 1)
vtk_data.SetOrigin(origin)
vtk_data.SetSpacing(spacing)

vtk_scalar_array = vtk.vtkDoubleArray()
vtk_scalar_array.SetNumberOfComponents(1)
vtk_scalar_array.SetName("scalar_field")

for i in range(grid_size):
    for j in range(grid_size):
        vtk_scalar_array.InsertNextTuple((scalar_field[i, j],))

vtk_data.GetPointData().SetScalars(vtk_scalar_array)

# Compute the gradient and Morse-Smale complex using TTK
morse_smale_complex = ttk.MorseSmaleComplex()
morse_smale_complex.SetInputData(vtk_data)
morse_smale_complex.Update()

# The output contains the critical points and separatrices
output = morse_smale_complex.GetOutput()

# Print the critical points
critical_points = output.GetPointData().GetArray("CriticalPoints")
for i in range(critical_points.GetNumberOfTuples()):
    print("Critical point {}: {}".format(i, critical_points.GetTuple(i)))
