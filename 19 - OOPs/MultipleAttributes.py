# Problem 4: Create a Student class with name and age attributes.
# Create display_details() to display both. Create one object and test it.
#
# Goal: Practice multiple object attributes and methods.

class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def display_details(self,name,age):
        print(f"Student name: {self.name}, age: {self.age}")

s1 = Student("Aryan",21)
s1.display_details(s1.name,s1.age)

s2 = Student("Krishna", 23)
s2.display_details(s2.name,s2.age)

s3 = Student("Shiv", 24)
s3.display_details(s1.name,s1.age)