# Problem 1: Create a class named Student.
# Create an object of the class and display a message confirming that the object was created.
#
# Goal: Understand the basic syntax of a class and an object.

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Aryan")
print(s1.name)