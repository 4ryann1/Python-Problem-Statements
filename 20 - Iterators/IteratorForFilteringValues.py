# Problem 9: Iterator for Filtering Values

# Create a custom iterator named PositiveNumbers that receives a list of integers and returns only the positive numbers.

# Requirements:
# - Create a PositiveNumbers class.
# - Accept a list of integers.
# - Implement __iter__() and __next__().
# - Skip zero and negative values.
# - Return only positive values.
# - Correctly raise StopIteration after all values have been checked.
# - Test the iterator with a list containing positive, negative, and zero values.

class PositiveNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            number = self.numbers[self.index]
            self.index += 1

            if number > 0:
                return number

        raise StopIteration


# Create a list containing positive, negative, and zero values
numbers = [10, -5, 0, 25, -8, 15, 0, -2, 30]

# Create PositiveNumbers iterator
positive_numbers = PositiveNumbers(numbers)

# Display only positive numbers
for number in positive_numbers:
    print(number)