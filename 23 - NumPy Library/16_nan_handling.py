# Problem 16: Handling Missing Numerical Values

# Create a 2D NumPy array containing several np.nan values.

# Requirements:
# - Detect missing values using isnan().
# - Count missing values in the complete array.
# - Count missing values feature-wise.
# - Calculate nanmean(), nanmedian(), nanmin(), and nanmax().
# - Replace missing values with the mean of their respective feature.
# - Verify that no NaN values remain.
# - Use NumPy operations and broadcasting where appropriate.

import numpy as np

data = np.array([
    [10, 20, np.nan],
    [15, np.nan, 30],
    [np.nan, 25, 35],
    [20, 30, 40],
    [25, 35, np.nan]
])

# Printing Missing Values
print("Missing Values: ",np.isnan(data))

# Counting Missing Values
print("Total Missing Values: ", np.isnan(data).sum(axis=0))

# Counting missing values feature-wise
print("Couting Missing values feature-wise:", np.isnan(data, axis=0))

# Calculate nanmean(), nanmedian(), nanmin(), nanamax()
print(f"Mean: {np.nanmean(data, axis=0)}")
print(f"Median: {np.nanmedian(data, axis=0)}")
print(f"Max: {np.nanmax(data, axis=0)}")

# Replace missing with respective mean values
feature_means = np.nanmean(data, axis = 0)
data = np.where(np.isnan(data), feature_means, data)
print("Updated Array: ", data)

# Verify no NaN values remain
print("\nRemaining NaN Values:", np.isnan(data).sum())
print("No NaN Remaining:", not np.isnan(data).any())
