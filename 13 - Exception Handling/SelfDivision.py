# 1. Safe Division
#
# Create a program that takes two numbers from the user and divides the first by the second.
#
# Requirements:
#
# Handle ZeroDivisionError.
# Handle ValueError if the user enters non-numeric input.
# Display appropriate messages.


first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))

def division(first_number, second_number):
    try:
        quotient = first_number / second_number
        print(quotient)
    except ZeroDivisionError:
        print("Division by zero")
    except ValueError:
        print("Invalid input")
    else:
        print("Division by zero")

division(first_number, second_number)