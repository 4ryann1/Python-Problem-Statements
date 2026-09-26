# Problem 14: List-Based To-Do Manager
# Create a menu-driven To-Do List application using a Python list.
# The program should allow the user to:
# 1. Add a task
# 2. View all tasks
# 3. Mark/remove a completed task
# 4. Search for a task
# 5. Clear all tasks
# 6. Exit
#
# Write your solution below.

to_do = []
try:
    while True:
        print("Enter your choice:")
        print("1. Add a Task")
        print("2. View a Task")
        print("3. Mark/remove a completed task")
        print("4. Search for a task")
        print("5. Clear all tasks")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            task = input("Enter your task: ")
            to_do.append(task)
        elif choice == 2:
            idx = int(input("Enter your index: "))
            print(f"The task at index {idx} is {to_do[idx]}")
        elif choice == 3:
            task = input("Enter your task: ")
            to_do.remove(task)
        elif choice == 4:
            task = input("Enter your task to be searched: ")
            if task in to_do:
                print("The task is in the list!")
            else:
                print("The task is not in the list!")
        elif choice == 5:
            to_do.clear()
            print("The list is empty!",to_do)
        elif choice == 6:
            break
        else:
            break
except ValueError as ve:
    print("Error",ve)