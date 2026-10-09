# Problem 7: Statistical Summary of Features

# Create a 10x4 matrix representing 10 samples and 4 numerical features.

# Requirements:
# - Calculate mean, median, standard deviation, variance, minimum, and maximum.
# - Calculate each statistic feature-wise using the correct axis.
# - Calculate the overall mean.
# - Find the index of the minimum and maximum value in the complete array.
# - Find the minimum and maximum for every feature.
# - Calculate the range of every feature using max - min.

import numpy as np

data = np.array([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [12, 22, 32, 42],
    [18, 28, 38, 48],
    [14, 24, 34, 44],
    [16, 26, 36, 46],
    [11, 21, 31, 41],
    [19, 29, 39, 49],
    [13, 23, 33, 43],
    [17, 27, 37, 47]
])

# Calculate mean, median, standard deviation, variance, minimum, and maximum.

mean_data = np.mean(data, axis = 0)
print(f"Feature-wise Mean: {mean_data}")

median_data = np.median(data, axis = 0)
print(f"Feature-wise Median: {median_data}")

standard_deviation = np.std(data, axis = 0)
print(f"Feature-wise Standard Deviation: {standard_deviation}")

variance = np.var(data, axis = 0)
print(f"Feature-wise Variance: {variance}")

minimum = np.min(data, axis=0)
print(f"Feature-wise Minimum: {minimum}")

maximum = np.max(data, axis=0)
print(f"Feature-wise Maximum: {maximum}")

# Calculate each statistic feature-wise using the correct axis.
feature_range = np.min(data, axis=0) - np.max(data, axis=0)
print(f"Feature wise Range: {feature_range}")

# Calculate the overall mean of all 40 values
print(f"Overall Mean: {np.mean(data)}")

# Find the index of the minimum and maximum value in the complete array.
min_index = np.argmin(data)
max_index = np.argmax(data)
print(f"Index of Minimum: {min_index}")
print(f"Index of Maxmum: {max_index}")

# Find the minimum and maximum for every feature.
print("\nMinimum Value in Complete Array:", data.min())
print("Minimum Index (flattened):", min_index)
print("Minimum Position (row, column):", np.unravel_index(min_index, data.shape))

print("\nMaximum Value in Complete Array:", data.max())
print("Maximum Index (flattened):", max_index)
print("Maximum Position (row, column):", np.unravel_index(max_index, data.shape))

# Display matrix properties
print("\nShape:", data.shape)
print("Dimensions:", data.ndim)
print("Total Elements:", data.size)
print("Data Type:", data.dtype)