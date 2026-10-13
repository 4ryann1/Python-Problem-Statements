# Problem 14: Universal Functions for ML Data

# Create a NumPy array containing positive decimal values.

# Requirements:
# - Calculate square root using sqrt().
# - Calculate square using square().
# - Calculate absolute values using abs().
# - Calculate natural logarithm using log().
# - Calculate log base 10 using log10().
# - Calculate exponential using exp().
# - Round values using round().
# - Demonstrate floor() and ceil().
# - Keep all operations vectorized.

import numpy as np

positive_decimals = np.array([1.5, 2.7, 3.2, 4.8, 5.6])

print(f"Positive Decimals: {positive_decimals}")
print(f"Positive Decimals Shape: {positive_decimals.shape}")

sqrt = np.sqrt(positive_decimals)
print(f"Square Roots: {sqrt}")
print(f"Square Root Shape: {sqrt.shape}")

squared = np.square(positive_decimals)
print("Squared Array:", squared)
print("Squared Array Shape:", squared.shape)

absolute = np.absolute(positive_decimals)
print(f"Absolute Array: {absolute}")
print(f"Absolute Array Shape: {absolute.shape}")

logarithm = np.log(positive_decimals)
print(f"Absolute Array: {logarithm}")
print(f"Absolute Array Shape: {logarithm.shape}")

print("Log Base 10:", np.log10(positive_decimals))

# 6. Exponential (e^x)
print("Exponential:", np.exp(positive_decimals))

# 7. Round to 1 decimal place
print("Rounded:", np.round(positive_decimals, 1))

# 8. Floor (round down)
print("Floor:", np.floor(positive_decimals))

# 9. Ceil (round up)
print("Ceil:", np.ceil(positive_decimals))

# All operations are vectorized (no loops)
print("\nFinal Shape:", positive_decimals.shape)