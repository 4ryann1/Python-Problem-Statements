# Problem 2: Generating Numerical Data

# Generate numerical sequences commonly used for ML experimentation.

# Requirements:
# - Generate values from 0 to 20 with a step of 2.
# - Generate 10 equally spaced values between 0 and 1.
# - Generate 11 equally spaced values between -1 and 1.
# - Generate 20 values between 10 and 100.
# - Display the shape and dtype of every generated array.
# - Explain through comments the difference between arange() and linspace().


import numpy as np

# 1. Generate values from 0 to 20 with a step of 2
# arange(start, stop, step) excludes the stop value.
array1 = np.arange(0, 21, 2)

# 2. Generate 10 equally spaced values between 0 and 1
# linspace(start, stop, num) includes both endpoints by default.
array2 = np.linspace(0, 1, 10)

# 3. Generate 11 equally spaced values between -1 and 1
array3 = np.linspace(-1, 1, 11)

# 4. Generate 20 equally spaced values between 10 and 100
array4 = np.linspace(10, 100, 20)


# Function to display array details
def display_array(name, array):
    print(f"\n{name}:")
    print(array)
    print("Shape:", array.shape)
    print("Data type (dtype):", array.dtype)


# Display all generated arrays
display_array("Array 1: Values from 0 to 20 with step 2", array1)
display_array("Array 2: 10 equally spaced values from 0 to 1", array2)
display_array("Array 3: 11 equally spaced values from -1 to 1", array3)
display_array("Array 4: 20 equally spaced values from 10 to 100", array4)