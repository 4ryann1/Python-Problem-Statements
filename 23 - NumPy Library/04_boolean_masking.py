# Problem 4: Boolean Masking and Filtering

# Create a NumPy array containing 20 numerical feature values.

# Requirements:
# - Find all values greater than 50.
# - Find all values less than or equal to 25.
# - Find values between 30 and 70.
# - Count how many values satisfy each condition.
# - Replace all values below 30 with 30.
# - Replace all values above 80 with 80.
# - Create a filtered array containing only values between 30 and 70.
# - Use Boolean indexing rather than Python loops where possible.


import numpy as np

data = np.array([
    10, 25, 35, 45, 55,
    65, 75, 85, 90, 20,
    30, 40, 50, 60, 70,
    80, 15, 28, 72, 95
])

#1 Find all values greater than 50
greater_50 = data[data>50]
print(f"\nValues greater than 50: {greater_50}")
print(f"The Number of values are: {np.count_nonzero(data>50)}")

#2 Find all values less than or equal to 25
less_25 = data[data<=25]
print(f"\nValues smaller or equal to 25: {less_25}")
print(f"Number of values: {np.count_nonzero(data<=25)}")

#3 Find values between 30 and 70
below_30 = data[(data>=30) & (data<=70)]
print(f"\nValues below 30 and 70: {below_30}")
print(f"Number of values replaced by 30 are {np.count_nonzero(data>30) & (data<70)}")

#4 Replace all values below 30 with 30.
modified_matrix = data.copy()
modified_matrix[modified_matrix<30] = 30
print(f"\nValues replaced by 30: {modified_matrix}")

#5 Replace all values above 80 with 80
modified_matrix[modified_matrix>80] = 80
print(f"\nValues greater than 80 replaced by 80: {modified_matrix}")

#6 Create a filtered array containing only values between 30 and 70.
filtered_array = modified_matrix[(modified_matrix>30) & (modified_matrix<70)]
print(f"Filtered Array: {filtered_array}")

