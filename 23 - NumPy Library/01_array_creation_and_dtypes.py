# Problem 1: NumPy Array Creation and Data Types

# Create NumPy arrays representing data that could be used in an ML dataset.

# Requirements:
# - Create a 1D array containing 10 integer values.
# - Create a 1D array containing 10 decimal values.
# - Create a 2D array representing 5 students and 3 features.
# - Create an array of zeros with shape (4, 3).
# - Create an array of ones with shape (2, 5).
# - Create an identity matrix of size 4.
# - Display each array, its shape, ndim, size, and dtype.
# - Create an integer array and convert it to float using NumPy.
# - Use only NumPy for the numerical operations.


import numpy as np

# 1. Create a 1D array containing 10 integer values
int_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# 2. Create a 1D array containing 10 decimal values
decimal_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5,
                          6.6, 7.7, 8.8, 9.9, 10.1])

# 3. Create a 2D array representing 5 students and 3 features
students_array = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94],
    [70, 75, 72],
    [88, 86, 90]
])

# 4. Create an array of zeros with shape (4, 3)
zeros_array = np.zeros((4, 3))

# 5. Create an array of ones with shape (2, 5)
ones_array = np.ones((2, 5))

# 6. Create an identity matrix of size 4
identity_array = np.eye(4)

# 7. Create an integer array and convert it to float
original_array = np.array([1, 2, 3, 4, 5])
float_array = original_array.astype(float)


# Function to display array details
def display_array(name, array):
    print(f"\n{name}:")
    print(array)
    print("Shape:", array.shape)
    print("Dimensions (ndim):", array.ndim)
    print("Size:", array.size)
    print("Data type (dtype):", array.dtype)


# Display details of all arrays
display_array("Integer Array", int_array)
display_array("Decimal Array", decimal_array)
display_array("Students Array", students_array)
display_array("Zeros Array", zeros_array)
display_array("Ones Array", ones_array)
display_array("Identity Matrix", identity_array)
display_array("Original Integer Array", original_array)
display_array("Converted Float Array", float_array)