# 12. Triangle Validity
#
# Take three angles as input and check whether they can form a valid triangle.

angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if (angle1>0 and angle2>0 and angle3>0 and angle1+angle2+angle3 == 180):
    print("It is a triangle")
else:
    print("It is not a triangle")