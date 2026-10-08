# 13. Triangle Type
# Take three side lengths and determine whether the triangle is:
# Equilateral
# Isosceles
# Scalene
# Invalid triangle


side1 = int(input("Enter first angle: "))
side2 = int(input("Enter second angle: "))
side3 = int(input("Enter third angle: "))

if side1>0 and side2>0 and side3>0 and side1+side2>side3 and side1+side3>side2 and side3+side2>side1:
    if side1==side2==side3:
        print("It is a equilateral triangle")
    elif side1==side2 or side2==side3 or side3==side1:
        print("It is an isosceles triangle")
    elif side1!=side3 or side3!=side2 or side2!=side1:
        print("It is a scalene triangle")
    else:
        print("It is an invalid triangle")
else:
    print("It is an invalid triangle")