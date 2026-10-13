# Problem 15: Clipping and Numerical Control

# Create a NumPy array containing values both below and above an acceptable feature range.

# Requirements:
# - Clip all values to a specified minimum and maximum using clip().
# - Round the clipped values to 2 decimal places.
# - Compare the original and clipped arrays.
# - Find which values were changed.
# - Count the changed values.
# - Use NumPy operations instead of explicit loops.

import numpy as np

arr = np.array([-10.5, 5.234, 25.678, 50.456, 85.789, 110.5])
print("Original Array:", arr)

# 1. Set minimum and maximum limits
min_value = 0
max_value = 100

# 2. Clip values between 0 and 100
clipped = np.clip(arr, min_value, max_value)
print("Clipped Array:", clipped)

# 3. Round all values to 2 decimal places
round = np.round(clipped, 2)
print("Rounded Values:", round)

# 4. Compare original and clipped arrays
comparison = arr != clipped

print("\nChanged Positions:", comparison)

# 5. Find original values that were changed
changed_values = arr[comparison]

print("\nChanged Values:", changed_values)

# 6. Count changed values
count = np.count_nonzero(comparison)

print("\nTotal Changed Values:", count)

# 7. Display shapes
print("\nOriginal Shape:", arr.shape)
print("Clipped Shape:", clipped.shape)