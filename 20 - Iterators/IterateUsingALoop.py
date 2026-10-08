# Problem 4: Iterate Using a for Loop

# Create a Python program that creates an iterator from a tuple and uses a for loop to display all its elements.

# Requirements:
# - Create a tuple containing at least six values.
# - Convert it into an iterator using iter().
# - Use a for loop to traverse the iterator.
# - Display each element.

tuple1 = (10,20,30,40,50,60)

iterator = iter(tuple1)

for number in iterator:
    print(number)