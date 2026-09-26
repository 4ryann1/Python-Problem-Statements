# 5. Pass or Fail
#
# Take marks as input.
#
# Marks ≥ 40 → "Pass"
# Marks < 40 → "Fail"

marks = int(input("Marks: "))
if marks >= 40:
    print(f"You are Passed!")
elif marks < 40:
    print(f"You are Failed!")
else:
    print(f"Invalid Input!")