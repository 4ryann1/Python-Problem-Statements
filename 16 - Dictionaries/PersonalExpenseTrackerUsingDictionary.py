"""Problem 15: Personal Expense Tracker Using Dictionary

Create a menu-driven expense tracker using a dictionary.
Support add, view, total, highest expense, delete, and exit.

Write your solution below.
"""

def menu(dict):
    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = input("Enter your key: ")
        value = input("Enter your value: ")
        dict[key] = value
    elif choice == 2:
        for key, value in dict.items():
            print(f"{key} - {value}")
    elif choice == 3:
        total = 0
        for value in dict.values():
            total += value
        print(total)
    elif choice == 4:
        highest = 0
        for value in dict.values():
            if value > highest:
                highest = value
            else:
                print()
        print(highest)
    elif choice == 5:
        key = input("Enter your key: ")
        if key in dict.keys():
            del dict[key]
            print("The value in dictionary has been deleted.")
    elif choice == 6:
        print("Exiting...")
        print("Exited")
    else:
        print("Invalid choice.")

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}
menu(dict1)