# Problem 20: Random Dataset Shuffling and Selection

# Create a dataset of 50 samples with 4 features and a matching target array.

# Requirements:
# - Generate a reproducible random permutation of sample indices.
# - Shuffle the dataset using those indices.
# - Select the first 40 samples as a training portion and the remaining 10 as a testing portion.
# - Keep features and targets aligned.
# - Verify the shapes.
# - Verify that every original sample appears exactly once after shuffling.
# - Use NumPy only for the split operation.


import numpy as np

# 1. Set random seed
np.random.seed(42)

# 2. Create dataset (50 samples, 4 features)
X = np.arange(200).reshape(50, 4)

# Create matching target array
y = np.arange(50)

print("Original Features Shape:", X.shape)
print("Original Targets Shape:", y.shape)

# 3. Generate random permutation of indices
indices = np.random.permutation(50)

print("\nShuffled Indices:\n", indices)

# 4. Shuffle features and targets together
X_shuffled = X[indices]
y_shuffled = y[indices]

# 5. Split into training and testing portions
X_train = X_shuffled[:40]
X_test = X_shuffled[40:]

y_train = y_shuffled[:40]
y_test = y_shuffled[40:]

# 6. Verify shapes
print("\nTraining Features:", X_train.shape)
print("Testing Features:", X_test.shape)

print("Training Targets:", y_train.shape)
print("Testing Targets:", y_test.shape)

# 7. Verify every original sample appears once
print("\nAll Samples Present:",
      np.array_equal(np.sort(indices), np.arange(50)))

print("No Duplicate Indices:",
      len(np.unique(indices)) == 50)

# 8. Verify features and targets are aligned
print("Features and Targets Aligned:",
      np.array_equal(X_shuffled[:, 0] // 4, y_shuffled))
