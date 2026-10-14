# Problem 18: Random Data for ML Experiments

# Use NumPy's random module to generate reproducible synthetic data.

# Requirements:
# - Set a random seed.
# - Generate 20 random values between 0 and 1.
# - Generate a 5x3 matrix from a normal distribution.
# - Generate 100 integer class labels between 0 and 2.
# - Generate random samples from a uniform range.
# - Generate a random 10x4 feature matrix.
# - Display shapes and basic statistics of the generated data.


import numpy as np

# 1. Set random seed for reproducibility
np.random.seed(42)

# 2. Generate 20 random values between 0 and 1
values = np.random.rand(20)

print("Random Values:\n", values)
print("Shape:", values.shape)

# 3. Generate a 5x3 normal distribution matrix
normal_data = np.random.randn(5, 3)

print("\nNormal Distribution:\n", normal_data)
print("Shape:", normal_data.shape)

# 4. Generate 100 integer class labels (0, 1, 2)
labels = np.random.randint(0, 3, 100)

print("\nClass Labels:\n", labels)
print("Shape:", labels.shape)

# 5. Generate 10 random samples between 10 and 50
uniform_data = np.random.uniform(10, 50, 10)

print("\nUniform Samples:\n", uniform_data)
print("Shape:", uniform_data.shape)

# 6. Generate a random 10x4 feature matrix
features = np.random.rand(10, 4)

print("\nFeature Matrix:\n", features)
print("Shape:", features.shape)

# 7. Basic statistics
print("\nMean:", np.mean(features))
print("Median:", np.median(features))
print("Standard Deviation:", np.std(features))
print("Minimum:", np.min(features))
print("Maximum:", np.max(features))

# 8. Feature-wise statistics
print("\nFeature-wise Mean:", np.mean(features, axis=0))
print("Feature-wise Std:", np.std(features, axis=0))
