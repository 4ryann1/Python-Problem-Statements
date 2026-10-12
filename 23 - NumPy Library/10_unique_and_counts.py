# Problem 10: Unique Values and Frequency Analysis

# Create an integer NumPy array containing repeated class labels such as 0, 1, and 2.

# Requirements:
# - Find unique values using unique().
# - Count the occurrence of every unique value.
# - Determine which class occurs most frequently.
# - Create a Boolean mask for one selected class.
# - Count the number of samples belonging to each class.
# - Verify that the total class counts equal the number of samples.


import numpy as np

# Create an array with repeated class labels
labels = np.array([0, 1, 2, 1, 0, 2, 1, 1, 0, 2, 1, 0, 2, 1, 1])

print("Class Labels:", labels)

# 1. Find unique values
unique_values = np.unique(labels)
print("Unique Values:", unique_values)

# 2. Count occurrences of each unique value
classes, counts = np.unique(labels, return_counts=True)
print("Class Counts:", counts)

# 3. Find the most frequent class
most_frequent = classes[np.argmax(counts)]
print("Most Frequent Class:", most_frequent)

# 4. Create a Boolean mask for class 1
mask = labels == 1
print("Boolean Mask:", mask)

# 5. Count samples belonging to each class
for cls, count in zip(classes, counts):
    print(f"Class {cls}: {count} samples")

# 6. Verify total counts equal total samples
total_counts = np.sum(counts)
total_samples = labels.size

print("Total Class Counts:", total_counts)
print("Total Samples:", total_samples)
print("Verification:", total_counts == total_samples) 