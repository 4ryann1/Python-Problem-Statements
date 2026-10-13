# Problem 13: Broadcasting for Feature Operations

# Create a 5x4 feature matrix.

# Requirements:
# - Create a 1D array containing one adjustment value for each feature.
# - Add the feature adjustment array to the matrix using broadcasting.
# - Create a column vector containing one value for each sample.
# - Multiply the feature matrix by the column vector using broadcasting.
# - Demonstrate one valid and one invalid broadcasting shape through comments.
# - Display all resulting shapes.

import numpy as np 

features = np.array([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [25, 35, 45, 55],
    [30, 40, 50, 60]
])

# Create a 1D array containing one adjustment value for each feature.
adjustment = np.array([1, 2, 3, 4])

adjusted = adjustment + features
print("Adjusted Matrix: ",adjusted)
print("ADjusted Matrix Shape: ", adjusted.shape)

sample_values = np.array([1, 2, 3, 4, 5]).reshape(5,1)

print("\nColumn Vector:\n", sample_values)
print("Shape:", sample_values.shape)

# Multiply using broadcasting
result = features * sample_values
print("Result Matrix: ", result)
print("Result Matrix Shape: ",result.shape)

# Valid: (5,4) + (4,) = (5,4)
# Invalid: (5,4) + (3,) = Error

print("\nFinal Shapes:")
print("Features:", features.shape)
print("Adjustment:", adjustment.shape)
print("Adjusted:", adjusted.shape)
print("Column Vector:", sample_values.shape)
print("Multiplied:", result.shape)