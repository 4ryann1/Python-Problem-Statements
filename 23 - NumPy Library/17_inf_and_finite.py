# Problem 17: Detecting Invalid Numerical Values

# Create an array containing normal numbers, np.nan, np.inf, and -np.inf.

# Requirements:
# - Detect NaN values using isnan().
# - Detect infinite values using isinf().
# - Detect finite values using isfinite().
# - Count each category.
# - Replace positive and negative infinity with suitable finite boundary values.
# - Create a final clean numerical array.

import numpy as np

# Create an array with invalid numerical values
data = np.array([10, 20, np.nan, np.inf, 30, -np.inf, 40, 50])

print("Original Array:",data)
print("Missing Values:", np.isnan(data))
print("Infinite Values:", np.inf(data))
print("Finite Values:", np.isfinite(data))

print("Total NaN:", np.isnan(data).sum())
print("Total Infinite:", np.isinf(data).sum())
print("Total Finite:", np.isfinite(data).sum())

finite_values = data[np.isfinite(data)]

minimum = np.min(finite_values)
maximum = np.max(finite_values)

data = np.where(data == np.inf, maximum, data)
data = np.where(data == np.inf, minimum, data)

mean = np.mean(finite_values)

data = np.where(np.isnan(data), mean, data)

print("Clean Array:", data)

print("All values finite:", np.isfinite(data).all())