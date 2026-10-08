# Problem 4: Find an Element
# Create a program that stores 10 names in a list. Ask the user for a name and check whether that name exists in the list.
# Display an appropriate message depending on whether it is found or not.
#
# # Write your solution below.

#Created a list of Names
list1 = ["Aryan","Rohit","Mayur","Atharva","Krishna","Shiv","Ganesh","Anuj","Aniket","Om"]

name_search = input("Enter the name to be searched: ")

try:
    if name_search in list1:
        print(f"The name {name_search} is in the list at {list1.index(name_search)+1}")
        print("\n\nThe list index are used as natural numbers")
    else:
        print(f"The name {name_search} is not in the list")

except ValueError:
    print("Please enter a valid name!")
