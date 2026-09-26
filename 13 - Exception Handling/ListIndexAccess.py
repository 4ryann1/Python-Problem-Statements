# 3. List Index Access
#
# Create a list of 5 numbers and ask the user for an index.
#
# Requirements:
#
# Display the element at that index.
# Handle IndexError if the index doesn't exist.
# Handle ValueError if the user enters something other than an integer.

#Logic 1
list = [10, 20, 30, 40, 50]

try:
    list_index = input("Enter a number: ")
    list_index = int(list_index)
    if list_index > len(list):
        raise IndexError
    else:
        print(f"{list_index} has value {list[list_index]}")
except ValueError:
    print("Please enter a number.")

#Logic 2
numbers = [10, 25, 42, 58, 91]

try:
  user_input = input("Enter an index (0 to 4): ")
  index = int(user_input)
  print(f"The element at index {index} is: {numbers[index]}")

except ValueError:
  print("Error: You must enter a valid integer.")

except IndexError:
  print("Error: That index does not exist in the list.")

