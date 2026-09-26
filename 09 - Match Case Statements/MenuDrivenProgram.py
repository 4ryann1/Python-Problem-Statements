# 6. Menu-Driven Program
#
# Display this menu:
#
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
#
# Take the user's choice and two numbers. Use match-case to perform the selected operation.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print("------ M E N U ------")
operator = int(input("Enter a operator: \n1. Add \n2. Sub \n3. Multiply \n4. Divide\n"))

match operator:
    case 1:
        print(number1 + number2)
    case 2:
        print(number1 - number2)
    case 3:
        print(number1 * number2)
    case 4:
        if number2 != 0:
            print(number1 / number2)
        else:
            print("Zero Cannot be divided.")
    case _:
        print("Invalid Input")
