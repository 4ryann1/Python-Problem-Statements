# Problem 5: Reshaping ML Data

# Create an array containing values from 1 to 24.

# Requirements:
# - Reshape it into a 4x6 matrix.
# - Reshape it into a 3x8 matrix.
# - Reshape it into a 2x3x4 array.
# - Convert the 2D matrix into a 1D array using ravel().
# - Convert it into a 1D array using flatten().
# - Compare the behavior of ravel() and flatten() through comments.
# - Use reshape(-1, 1) to create a column vector.
# - Use reshape(1, -1) to create a row vector.


import numpy as np

arr = np.arange(1,25)

# Reshaped array to 4x6
fourbysix = arr.reshape(4,6)
print(f"The reshaped array is: \n{fourbysix}")

# Reshaped array to 3x8
threebyeight = arr.reshape(3,8)
print(f"The reshaped array is: \n{threebyeight}")

# Reshaped it into 2x3x4
twothreefour = arr.reshape(2,3,4)
print(f"The reshaped array is: \n{twothreefour}")

# Convert 2D matrix into a 1D array using ravel()
raveled_array = fourbysix.ravel()
print(f"Raveled Array: \n{raveled_array}")

# Convert it into a 1D array using flatten().
one_array = arr.flatten()
print(f"Flattened Array: \n{one_array}")

# Difference between ravel() and flatten():
# ravel() returns a view when possible, so changes to the
# result may affect the original array when memory is shared.
# flatten() always returns an independent copy.

# Create a column vector using reshape (-1, 1)
column_vector = arr.reshape(-1,1)
print(f"Column Vector: \n{column_vector}")

# Create a row vector using reshape(1, -1)
row_vector = arr.reshape(1, -1)
print(f"Row Vector: \n{row_vector}")

# Display shapes
print("\nArray Shapes:")
print("Original Array:", arr.shape)
print("4x6 Matrix:", fourbysix.shape)
print("3x8 Matrix:", threebyeight.shape)
print("3D Array:", twothreefour.shape)
print("ravel() Array:", raveled_array.shape)
print("flatten() Array:", one_array.shape)
print("Column Vector:", column_vector.shape)
print("Row Vector:", row_vector.shape)