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


import numpy as np

# 1. Create a 1D NumPy array containing 15 numerical values
features = np.array([45, 12, 78, 23, 56, 9, 34, 89, 17, 63, 5, 41, 72, 28, 50])

# Corresponding labels or scores
labels = np.array([
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O"
])

# 2. Sort values in ascending order
ascending = np.sort(features)

# 3. Sort values in descending order
descending = np.sort(features)[::-1]

# 4. Obtain indices that would sort the original array
indices = np.argsort(features)

# 5. Reorder labels using the sorting indices
sorted_labels = labels[indices]

# 6. Indices of the three smallest values
smallest_indices = np.argsort(features)[:3]

# 7. Indices of the three largest values
largest_indices = np.argsort(features)[-3:][::-1]

# Display results
print("Original array:", features)
print("Ascending order:", ascending)
print("Descending order:", descending)
print("Argsort indices:", indices)
print("Labels in ascending order:", sorted_labels)

print("Three smallest values:", features[smallest_indices])
print("Indices of three smallest values:", smallest_indices)

print("Three largest values:", features[largest_indices])
print("Indices of three largest values:", largest_indices)
