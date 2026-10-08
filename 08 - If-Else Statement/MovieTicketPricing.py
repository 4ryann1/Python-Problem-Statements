# 18. Movie Ticket Pricing
#
# Take the user's:
#
# Age
# Day of the week
#
# Base ticket price = ₹200.
#
# Apply discounts:
#
# Children below 12 → 50% discount
# Senior citizens 60+ → 30% discount
# Wednesday → Additional 20% discount
#
# Calculate and display the final ticket price.

age = int(input("Enter your age: "))
day = int(input("Enter your day of the week (1-7): "))

ticket = 200

if age <= 12:
    print(f"Yay! You will get 50% discount. The ticket price for you becomes ₹{ticket-(ticket*0.5)}")
elif age>=60:
    print(f"Yay! You will get {ticket-(ticket*0.3)}")
elif day==4:
    print(f"Yay! You will get {ticket-(ticket*0.2)}")