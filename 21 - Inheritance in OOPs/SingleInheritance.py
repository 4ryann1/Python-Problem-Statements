# Problem 1: Basic Single Inheritance
#
# Create a Python program demonstrating basic single inheritance.
#
# Requirements:
# - Create a Parent class named Person.
# - Add a name attribute and a display_name() method.
# - Create a Child class named Student that inherits from Person.
# - Add a roll_number attribute and a display_student() method.
# - Create an object of Student.
# - Display the student's name and roll number.

# Problem 1: Basic Single Inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number

    def display_student(self):
        print("Roll Number:", self.roll_number)


# Create an object of Student
student1 = Student("Aryan", 101)

# Display student's name and roll number
student1.display_name()
student1.display_student()