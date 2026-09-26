# 9. Simple Calculator Using Functions
# Create separate functions:
#
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)
#
# Create a menu-driven calculator that calls the appropriate function based on the user's choice.
#
# Handle division by zero using try-except.
#
# Example:
#
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Exit

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b

    choice = int(input(f"1. Add \n2. Subtract \n3. Multiply \n4. Divide\n"))
    match choice:
        case 1:
            print(add(a, b))
        case 2:
            print(subtract(a, b))
        case 3:
            print(multiply(a, b))
        case 4:
            print(divide(a, b))
        case _:
            print("Invalid choice")

main()