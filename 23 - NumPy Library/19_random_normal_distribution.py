# Problem 19: Synthetic Normally Distributed Features

# Generate synthetic features for an ML experiment.

# Requirements:
# - Generate 1000 values from a normal distribution with a chosen mean and standard deviation.
# - Generate a 1000x3 feature matrix where each feature has a different mean and standard deviation.
# - Calculate mean and standard deviation for every feature.
# - Compare the generated statistics with the intended parameters.
# - Use random.seed or default_rng for reproducibility.


import numpy as np

# 1. Set random seed
np.random.seed(42)

# 2. Generate 1000 normally distributed values
data = np.random.normal(loc=50, scale=10, size=1000)

print("Data Shape:", data.shape)
print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))

# 3. Set different means and standard deviations
means = [50, 100, 150]
stds = [10, 20, 30]

# 4. Generate a 1000x3 feature matrix
features = np.random.normal(
    loc=means,
    scale=stds,
    size=(1000, 3)
)

print("\nFeature Matrix:\n", features)
print("Shape:", features.shape)

# 5. Calculate feature-wise statistics
calculated_means = np.mean(features, axis=0)
calculated_stds = np.std(features, axis=0)

print("\nCalculated Means:", calculated_means)
print("Calculated Std:", calculated_stds)

# 6. Compare intended and calculated statistics
print("\nIntended Means:", means)
print("Generated Means:", calculated_means)

print("\nIntended Std:", stds)
print("Generated Std:", calculated_stds)

# 7. Calculate differences
print("\nMean Differences:",
      calculated_means - means)

print("Std Differences:",
      calculated_stds - stds)
