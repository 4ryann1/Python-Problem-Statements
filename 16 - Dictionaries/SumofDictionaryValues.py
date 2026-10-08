"""Problem 6: Find the Sum of Dictionary Values

Create a dictionary containing numbers as values. Calculate and display the sum of all values.

Write your solution below.
"""

dict = {
    "a": 10,
    "b": 20,
    "c": 30,
}

total_sum = 0
for value in dict.values():
    total_sum += value
print("Sum of all values: ", total_sum)