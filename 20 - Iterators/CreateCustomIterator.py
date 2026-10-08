# Problem 5: Create a Custom Iterator for Counting

# Create a custom iterator class named Counter that generates numbers from 1 up to a given limit.

# Requirements:
# - Create a Counter class.
# - Implement __iter__().
# - Implement __next__().
# - The iterator should generate numbers starting from 1.
# - Stop iteration after reaching the specified limit.
# - Test the iterator with a limit provided by the user.

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration


# Take limit from the user
limit = int(input("Enter the limit: "))

# Create Counter object
counter = Counter(limit)

# Iterate through the Counter object
for number in counter:
    print(number)