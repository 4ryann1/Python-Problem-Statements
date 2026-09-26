# Problem 9: Shopping Cart
# Create a simple shopping cart program using a list.
# The user should be able to:
# 1. Add an item
# 2. Remove an item
# 3. View all items
# 4. Search for an item
# 5. Exit
# Use a menu-driven approach.
#
# # Write your solution below.

shopping_list = ["Milk", "Bread", "Spices", "Veggies", "Fruits", "Noodles"]

def menu(list):
    try:
        print("Welcome to the shopping list!")
        while True:
            print("Please select an option:")
            print("1. Add item")
            print("2. Remove item")
            print("3. View items")
            print("4. Search for an item")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                item = input("Enter the name of the item: ")
                list.append(item)
                print("Your new list has been added!", list)
            elif choice == 2:
                item = input("Enter the name of the item: ")
                for i in list:
                    if i in item:
                        list.remove(i)
                else:
                    print("The item you entered is not in the list!")
            elif choice == 3:
                for i in list:
                    print(i, end=" ")
            elif choice == 4:
                item = input("Enter the name of the item: ")
                if item in shopping_list:
                    print("The item you entered is in the shopping list!")
                else:
                    print("The item you entered is not in the shopping list!")
            elif choice == 5:
                break
            else:
                print("Please select an option!")
                print("Invalid Input!")

    except ValueError as ve:
        print("Error",ve)
menu(shopping_list)