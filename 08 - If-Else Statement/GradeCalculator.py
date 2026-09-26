# Take marks from the user and print the grade:
#
# Marks	    Grade
# 90–100	A
# 80–89	    B
# 70–79	    C
# 60–69	    D
# Below 60	F
#
# Also handle marks outside the range 0–100 as "Invalid marks".


marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print(f"Your grade is A")
elif marks >= 80 and marks < 90:
    print(f"Your grade is B")
elif marks >= 70 and marks < 80:
    print(f"Your grade is C")
elif marks >= 60 and marks < 70:
    print(f"Your grade is D")
elif marks >60:
    print(f"Your grade is F")
else:
    print(f"Invalid input: {marks}")