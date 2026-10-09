# Problem 6: Transpose and Axis Operations

# Create a 4x5 matrix representing 4 samples and 5 features.

# Requirements:
# - Display the original matrix.
# - Transpose the matrix.
# - Calculate the sum of every row using axis=1.
# - Calculate the sum of every column using axis=0.
# - Calculate the mean of every row.
# - Calculate the mean of every column.
# - Find the minimum and maximum along both axes.
# - Clearly identify what axis=0 and axis=1 mean for this matrix.

import numpy as np

# Declaring and printing original array
arr = np.array([
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [12, 22, 32, 42, 52],
    [18, 28, 38, 48, 58]
])
print(f"Print original Array: \n{arr}")

# Transpose the original array
transpose = arr.T
print(f"Transpose Matrix: {transpose}")

# Sum of every row
row_sum = np.sum(arr, axis=1)
print(f"Sum of every Row: {row_sum}")

# Sum of every column
column_sum = np.sum(arr, axis=0)
print(f"Sum of every Column {column_sum}")

# mean of every row
mean_row = np.mean(arr, axis=0)
print(f"The mean of every row: {mean_row}")

# Mean of every column
mean_column = np.mean(arr,axis=0)
print(f"Mean of every column: {mean_column}")

# Find the minimum and maximum along both axes.
minimum_row = np.min(arr, axis=1)
minimum_column = np.min(arr, axis=0)

maximum_row = np.max(arr, axis=1)
maximum_column = np.max(arr, axis=0)

print(f"Minimum of rows: {minimum_row} \nMaximum of rows: {maximum_row}")
print(f"Minimum of column: {minimum_column} \nMaximum of column: {maximum_column}")