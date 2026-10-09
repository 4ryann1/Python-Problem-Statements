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

array1 = np.arange(0,21,2)

array2 = np.linspace(0,1,10)

array3 = np.linspace(-1,1,11)

array4 = np.linspace(10,100,20)

def array_info(array):
    print(f"\nArray: {array}")
    print(f"Array Shape: {array.shape}")
    print(f"Array Datatype: {array.dtype}\n")

array_info(array1)
array_info(array2)
array_info(array3)
array_info(array4)