# Problem 7: Reverse Iterator

# Create a custom iterator that iterates through the elements of a list in reverse order.

# Requirements:
# - Create a ReverseIterator class.
# - Accept a list through the constructor.
# - Implement __iter__() and __next__().
# - Return the last element first and continue toward the first element.
# - Raise StopIteration after all elements have been returned.
# - Test the iterator with a list of strings.

class ReverseIterator:
    def __init__(self, items):
        self.items = items
        self.index = len(items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            item = self.items[self.index]
            self.index -= 1
            return item
        else:
            raise StopIteration


# Create a list of strings
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# Create ReverseIterator object
reverse_iterator = ReverseIterator(fruits)

# Iterate through the list in reverse order
for fruit in reverse_iterator:
    print(fruit)