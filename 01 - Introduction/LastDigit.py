# Last Digit of a Number
# Take an integer as input and print its last digit.
# Example: 4587 → 7

number = int(input("Enter a number: "))

last_digit = number % 10
print(f"The last digit of {number} is {last_digit}")