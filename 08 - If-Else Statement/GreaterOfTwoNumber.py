# 4. Greater of Two Numbers
#
# Take two numbers as input and print the greater number. If both are equal, print "Both are equal".

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if number1 > number2:
    print(f"The number is greater than the number: {number1}")
elif number1 < number2:
    print(f"The number is less than the number: {number2}")
elif number1 == number2:
    print(f"The numbers are equal")
else:
    print(f"Invalid input: {number1} and {number2}")