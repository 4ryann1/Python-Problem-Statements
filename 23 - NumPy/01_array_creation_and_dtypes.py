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

arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr_2d = np.array([1.9, 2.9, 3.8, 4.7, 5.6, 6.5, 7.4, 8.3, 9.2, 10.1])



students = np.array([
    [85, 90, 78],  # Student 1
    [76, 88, 92],  # Student 2
    [90, 85, 87],  # Student 3
    [65, 72, 70],  # Student 4
    [95, 91, 89]   # Student 5
])

zeros = np.zeros((4,3))
ones = np.ones((2,5))
identity = np.eye(4)

def array_info(array):
    print("\nArray:\n", array)
    print("Array :", array.shape)
    print("Array Shape:", array.ndim)
    print("Array Size:", array.size)
    print("Array Data Type:", array.dtype)

array_info(arr_1d)
array_info(arr_2d)
array_info(students)
array_info(zeros)
array_info(ones)
array_info(identity)


# print(arr_1d, arr_2d, students, zeros, ones, identity, sep="\n")