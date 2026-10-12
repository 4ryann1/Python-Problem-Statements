# Problem 11: Combining Feature Data

# Create two NumPy arrays representing two batches of ML samples with the same number of features.

# Requirements:
# - Concatenate them vertically using concatenate().
# - Create another pair of arrays and combine them horizontally.
# - Use vstack() to combine compatible arrays.
# - Use hstack() to combine compatible arrays.
# - Use stack() to add a new dimension.
# - Display the shape after every operation.
# - Add comments explaining when vertical and horizontal combination is useful.

import numpy as np

# Batch 1: 3 samples, 4 features
batch1 = np.array([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50]
])

# Batch 2: 2 samples, 4 features
batch2 = np.array([
    [25, 35, 45, 55],
    [30, 40, 50, 60]
])

# Concatenate two matrices or arrays vertically using concatenate and axis
concatenated = np.concatenate((batch1, batch2), axis = 0)
print(f"The concatenated Array: {concatenated}")

# Create another pair of arrays and combine them horizontally.
pair1 = np.array([
    [12, 13, 14, 15, 16],
    [17, 11, 18, 19, 20]
])

pair2 = np.array([
    [22, 23, 24, 25, 26],
    [21, 27, 28, 29, 30]
])

concatenated_hor = np.concatenate((pair1, pair2), axis = 1)
print(f"The horizontally concatenated: {concatenated_hor}")


# Use vstack() to combine compatible arrays.
vertical_stack = np.vstack((batch1, batch2))
print(f"Vertical Stack: {vertical_stack}")
print(f"Shape: {vertical_stack.shape}")

horizontal_stack = np.hstack((pair1, pair2))
print(f"Horizontal Stack: {horizontal_stack}")
print(f"Shape: {horizontal_stack.shape}")

# Use stack() to add a new dimension.
new_stack = np.stack((pair1, pair2), axis=0)

print("\nStack:\n", new_stack)
print("Shape:", new_stack.shape)