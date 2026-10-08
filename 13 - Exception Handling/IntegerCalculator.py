# 5. Integer Calculator
#
# Create a calculator that accepts two integers and an operator:
#
# +
# -
# *
# /
#
# Requirements:
#
# Handle invalid numbers using ValueError.
# Handle division by zero.
# Handle an invalid operator.
# Use try-except-else.
try:
    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter another number: "))
    operator = input("Enter an operator: ")

    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)
    else:
        raise ValueError

except ValueError as e:
    print(f"Error: {e}")

except ZeroDivisionError:
    print("Zero Division Error")

else:
    print("Invalid Value")