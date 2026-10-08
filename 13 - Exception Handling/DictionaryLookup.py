#      4. Dictionary Lookup
#      Create a dictionary containing student names and their marks.
#      Example:
#
#      students = {
#          "Rahul": 85,
#          "Amit": 72,
#          "Sneha": 91
#      }
#
#      Ask the user for a student's name.
#      Requirements:
#      Display the student's marks.
#      Handle KeyError if the student doesn't exist.

students = {
        "Rahul": 85,
        "Amit": 72,
        "Sneha": 91
        }
name = input("Enter your name: ")
try:
    marks = students[name]
    print(f"{name}'s marks: {marks}")
except KeyError:
    print(f"Sorry, {name}'s marks is not available.")