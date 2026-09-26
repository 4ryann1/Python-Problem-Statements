"""
Problem 14: Inventory Management

Create an inventory dictionary with product names and quantities.
Provide a menu to add, update, remove, display inventory, and exit.

Write your solution below.
"""

products = {
    "Eggs": 30,
    "Milk": 50,
    "Spices": 10,
    "Butter": 20,
}

while True:
    print("Welcome to the Inventory Tracker!")
    print("Select an option:")
    print("1. Add product")
    print("2. Update product")
    print("3. Remove product")
    print("4. Display inventory")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = input("Enter product name: ")
        value = input("Enter product quantity: ")
        products[key] = value
    elif choice == 2:
        key = input("Enter product name: ")
        if key in products:
            value = input("Enter product quantity: ")
            products[key] = value
        else:
            print("Product not found.")
    elif choice == 3:
        key = input("Enter product name: ")
        if key in products:
           del key
           print("Product deleted.")
        else:
            print("Product not found.")
    elif choice == 4:
        print("The products are as follows:")
        print("-------The Products-------")
        print(f"Products | \tQuantity")
        for key, value in products.items():
            print(f"{key} - \t{value}")
    elif choice == 5:
        print("Exiting...")
        print("Exited")
    else:
        print("Invalid choice.")