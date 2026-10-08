# 19. Student Admission Eligibility
#
# Take:
#
# Mathematics marks
# Physics marks
# Chemistry marks
# Overall percentage
#
# A student is eligible if:
#
# Maths >= 60
# Physics >= 50
# Chemistry >= 50
# Overall percentage >= 60
#
# Additionally, if the student has 90% or above, print "Eligible for Scholarship".
#
# Otherwise, print the reason for rejection.

mathematics = int(input("Enter your Mathematics: "))
physics = int(input("Enter your Physics: "))
chemistry = int(input("Enter your Chemistry: "))

overall = ((mathematics + physics + chemistry)/300)*100

if mathematics >= 60 and physics >= 50 and chemistry >= 50 and overall >= 60:
    if overall >= 90:
        print(f"Yes! You are eligible for admission as well as Scholarship.")
    else:
        print(f"Yes, you are eligible for admission!")
else:
    print(f"Sorry, you are not eligible for admission.")