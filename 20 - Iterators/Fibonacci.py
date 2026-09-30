# Problem 8: Fibonacci Iterator

# Create a custom iterator class named Fibonacci that generates the 
# first N Fibonacci numbers.

# Requirements:
# - Create the Fibonacci class.
# - Accept N as the number of Fibonacci terms.
# - Implement __iter__() and __next__().
# - Generate the sequence starting with 0 and 1.
# - Stop after generating N terms.
# - Display the generated Fibonacci sequence using a for loop.

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            number = self.first

            self.first, self.second = self.second, self.first + self.second

            self.count += 1

            return number
        else:
            raise StopIteration


# Take number of terms from the user
n = int(input("Enter the number of Fibonacci terms: "))

# Create Fibonacci iterator
fibonacci = Fibonacci(n)

# Display Fibonacci sequence
for number in fibonacci:
    print(number)