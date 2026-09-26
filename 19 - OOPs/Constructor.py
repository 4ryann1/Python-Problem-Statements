# Problem 6: Create a Person class with __init__() accepting name and age.
# Store them as attributes.
# Create an object by passing values during object creation and display the details.
#
# Goal: Understand __init__() and constructor-based initialization.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Person Name:{self.name}; Person Age: {self.age}")

aryan = Person("Aryan",21)
aryan.display()