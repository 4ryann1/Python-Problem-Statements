# 9. Food Menu
#
# Create a food menu:
#
# 1 → Pizza - ₹200
# 2 → Burger - ₹120
# 3 → Sandwich - ₹100
# 4 → Pasta - ₹180
# 5 → Coffee - ₹80
#
# Ask the user for a choice and print the selected item and its price.
#
# If the choice is invalid, print "Invalid choice"

choice = int(input("Enter a choice: "))
print("1 → Pizza - ₹200\n2 → Burger - ₹120\n3 → Sandwich - ₹100\n4 → Pasta - ₹180\n5 → Coffee - ₹80")

match choice:
    case 1:
        print(f"You have chosen {choice}. Enjoy your Pizza $200")
    case 2:
        print(f"You have chosen {choice}. Enjoy your Burger $120")
    case 3:
        print(f"You have chosen {choice}. Enjoy your Sandwich $100")
    case 4:
        print(f"You have chosen {choice}. Enjoy your Pasta $180")
    case 5:
        print(f"You have chosen {choice}. Enjoy your Coffee $80")
    case _:
        print("Invalid Choice")