# Problem 9: Sorting ML Feature Values

# Create a 1D NumPy array containing 15 numerical values.

# Requirements:
# - Sort the values in ascending order.
# - Sort them in descending order.
# - Obtain the indices that would sort the original array using argsort().
# - Use those indices to reorder a second array containing corresponding labels or scores.
# - Identify the indices of the three smallest values.
# - Identify the indices of the three largest values.
# - Do not use Python's built-in sorted() or sort().

import numpy as np

arr = np.array([
    14, 7, 21, 3, 19, 8, 25, 12, 5, 18, 2, 22, 10, 6, 16
])

ascending_array = np.sort(arr)
print("Ascending Array: ", ascending_array)

descending_array = ascending_array[::-1]
print("Descending Array:",descending_array)

indices = np.argsort(arr)
print("Indices used for sorting original array.")

