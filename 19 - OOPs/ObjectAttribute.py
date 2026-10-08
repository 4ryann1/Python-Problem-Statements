# Problem 2: Create a Student class.
# Create an object and store the student's name as an attribute.
# Display the name using the object.
#
# Goal: Understand object attributes.

class Student:
    def __init__(self, name):
        self.name = "Aryan"

student1 = Student("Shiv")
# student1.name = "Mayur"
print(student1.name)
