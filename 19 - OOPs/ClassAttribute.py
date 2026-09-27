# Problem 22: Create a Student class with class attribute school_name = 'ABC College' and instance attributes name, age, and course. 
# Create three objects and display personal details with the common school name.

# Goal: Understand shared class attributes.

class Student:
    college_name = "DYPTC, Varale"
    def __init__(self,name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"\n------ Student Details ------")
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Course: {self.course}")
        print(f"Student College: {self.college_name}")

s1 = Student("Aryan",21,"AI & DS")
s1.display_details()