"""Problem 15: Set Operations Menu Program

Create a menu-driven program for two sets supporting union, intersection, both differences, symmetric difference, subset check, and exit.
"""

# Write your solution below.

def menu(set1, set2):
    try:
        while True:
            print("-------------Welcome to the sets menu-------------")
            print("Please select one of the following sets:")
            print("1. Union")
            print("2. Intersection")
            print("3. Difference")
            print("4. Symmetric Difference")
            print("5. Subset")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(f"The Union of Set1 and Set2 are: {set1.union(set2)}")
            elif choice == 2:
                print(f"The Intersection of Set1 and Set2 are: {set1.intersection(set2)}")
            elif choice == 3:
                print(f"The Difference of Set1 and Set2 are: {set1.difference(set2)}")
            elif choice == 4:
                print(f"The symmetric difference of Set1 and Set2 are:{set1.symmetric_difference(set2)}")
            elif choice == 5:
                user_input = eval(input("Enter your choice: "))
                if user_input.issubset(set1) or user_input.issubset(set2):
                    print(f"The {user_input} set is a subset")
                else:
                    print(f"The {user_input} is not a subset")
            elif choice == 6:
                print("Exiting the program")
                break
            else:
                print("Enter a valid choice (0 - 6)")
    except ValueError as ve:
        print("Please enter a valid number.")
        print("Error: ",ve)

    except TypeError as te:
        print("Error", te)

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {11,12,13,14,15,16,17,18,19,20}
menu(set1, set2)