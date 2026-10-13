# Problem 12: Splitting a Dataset

# Create a 2D NumPy array containing 30 samples and 4 features.

# Requirements:
# - Split the dataset into 3 equal parts using array_split().
# - Split it into training-like and testing-like portions using split() where possible.
# - Split columns into separate feature groups.
# - Display the shape of every resulting array.
# - Verify that the split pieces contain all original samples without unintended duplication.

import numpy as np

# Create a data set of 30 samples and 4 features
dataset = np.arange(1, 121).reshape(30, 4)

# Splitting dataset into 3 equal parts
parts = np.array_split(dataset, 3, axis = 0)

for i, part in enumerate(parts):
    print(f"\nPart {i+1}:\n", part)
    print("Shape:", part.shape)

# Split it into training-like and testing-like portions using split() where possible.
# 80% training (24 samples), 20% testing (6 samples)
train, test = np.split(dataset, [24], axis=0)

print("\nTraining Dataset:\n", train)
print("Training Shape:", train.shape)

print("\nTesting Dataset:\n", test)
print("Testing Shape:", test.shape)
