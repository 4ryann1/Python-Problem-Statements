# Problem 8: Aggregation Functions

# Create a NumPy array representing 20 daily numerical observations.

# Requirements:
# - Calculate total using sum().
# - Calculate product using prod() on a small safe array.
# - Calculate cumulative sum using cumsum().
# - Calculate cumulative product using cumprod() on a small safe array.
# - Calculate the mean of the observations.
# - Calculate the sum along rows and columns for a 2D version of the data.
# - Use axis correctly for 2D aggregation.

import numpy as np

# Create a NumPy array representing 20 daily numerical observations
data = np.array([
    12, 15, 10, 18, 20,
    14, 16, 22, 25, 19,
    11, 13, 17, 21, 24,
    26, 23, 15, 18, 20
])

print("Daily Observations: ")
print(data)

# 1. Calculate the total using sum()
total = np.sum(data)
print(f"Total Sum: {total}")

# 2. Calculate the product using a small safe array
small_array = np.array([1, 2, 3, 4])
print(f"Small Array: {small_array}")
print("Product:",np.prod(small_array))

# 3. Calculate cumulative sum using cumsum().
cumsum = np.cumsum(data)
print(f"Cumulative Sum of Data: {cumsum}")

# 4. Calculate the mean of the observations.
mean = np.mean(data)
print(f"The Mean: {data}")

# 6. Reshape the 20 observations into a 2D array (4x5)
matrix = data.reshape(4, 5)
print(f"2D Observations (4x5): {matrix}")

# 7. Calculate the sum along rows (axis=1)
row_sum = np.sum(matrix, axis=1)
print(f"The sum of row: {row_sum}")

# 8. Calculate the sum along columns (axis=0)
column_sum = np.sum(matrix, axis=0)
print(f"The sum along columns: {column_sum}")
