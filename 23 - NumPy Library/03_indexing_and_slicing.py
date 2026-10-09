# Problem 3: Indexing and Slicing Feature Data

# Create a 6x5 NumPy matrix representing 6 samples and 5 features.

# Requirements:
# - Display the first sample.
# - Display the last sample.
# - Display the first feature column.
# - Display the last feature column.
# - Display rows 2 through 5.
# - Display columns 2 through 4.
# - Extract the middle portion of the matrix.
# - Access one specific element using row and column indexing.
# - Modify one selected feature value.
# - Create a copy of the matrix before making modifications.

import numpy as np

matrix = np.matrix([
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [12, 22, 32, 42, 52],
    [18, 28, 38, 48, 58],
    [14, 24, 34, 44, 54],
    [16, 26, 36, 46, 56]
])


print(f"Array First Row: \n{matrix[0]}")
print(f"Array Last Column: \n{matrix[-1,:]}")
print(f"Array First Feature Column: \n{matrix[:,1]}")
print(f"Array Last Feature Column: \n{matrix[:,-1]}")
print(f"Array Rows through 5: \n{matrix[1:5, :]}")
print(f"Array Rows through 4: \n{matrix[:, 1:4]}")
print(f"Array Middle Element: \n{matrix[1:5, 1:4]}")
print(f"Array Specific Element: \n{matrix[2,3]}")
modified_matrix = matrix.copy()
modified_matrix[2,3] = 999
print(f"Modified matrix: \n{modified_matrix}")
print("\nOriginal Matrix After Modification:")
print(matrix)
