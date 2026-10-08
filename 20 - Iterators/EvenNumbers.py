# Problem 6: Custom Iterator for Even Numbers

# Create a custom iterator class named EvenNumbers that generates even numbers from a starting value up to a specified maximum value.

# Requirements:
# - Create the EvenNumbers class.
# - Implement __iter__() and __next__().
# - Accept a maximum value.
# - Generate only even numbers.
# - Raise StopIteration when the maximum value is exceeded.
# - Test the iterator using a for loop.

class EvenNumbers:
    def __init__(self, start, maximum):
        self.current = start
        self.maximum = maximum

        # Make sure we start from an even number
        if self.current % 2 != 0:
            self.current += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.maximum:
            number = self.current
            self.current += 2
            return number
        else:
            raise StopIteration


# Take input from the user
start = int(input("Enter starting value: "))
maximum = int(input("Enter maximum value: "))

# Create iterator object
even_numbers = EvenNumbers(start, maximum)

# Iterate through even numbers
for number in even_numbers:
    print(number)