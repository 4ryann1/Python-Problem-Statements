# 14. Electricity Bill Calculator
#
# Calculate an electricity bill based on units consumed:
#
# First 100 units → ₹5/unit
# Next 100 units → ₹7/unit
# Next 200 units → ₹10/unit
# Above 400 units → ₹15/unit
#
# Print the total bill.

units = int(input("Enter number of units: "))

if units>0 and units<=100:
    print(f"The {units} number of units gives the bill of {units*5}.")
elif units>100 and units<=200:
    print(f"The {units} number of units gives the bill of {units*7}.")
elif units>200 and units<=300:
    print(f"The {units} number of units gives the bill of {units*10}.")
elif units>400:
    print(f"The {units} number of units gives the bill of {units*15}.")
else:
    print("Invalid Input")
