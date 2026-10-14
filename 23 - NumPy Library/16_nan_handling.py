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

