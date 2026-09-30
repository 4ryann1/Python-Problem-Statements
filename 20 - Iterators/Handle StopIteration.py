# Problem 3: Handle StopIteration

# Create a Python program that demonstrates the StopIteration exception.

# Requirements:
# - Create an iterator from a list of numbers.
# - Use next() to retrieve every element.
# - After all elements are consumed, call next() one more time.
# - Use try-except to handle StopIteration gracefully.
# - Display a suitable message when the iterator is exhausted.

try:
    list = iter([11,12,13,14,15,16,17,18,19,20])
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))
    print(next(list))

except StopIteration:
    print("Error!! Number of Iterators are greater than the number of elements in the list.")