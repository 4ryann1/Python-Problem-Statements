# Problem 13: Create a Student class with name and marks in three subjects.
# Create calculate_total() and calculate_average(). Display both results.
#
# Goal: Use several object attributes across methods.

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def display(self):
        print("Name:",self.name)
        print("Marks1:",self.marks1)
        print("Marks2:",self.marks2)
        print("Marks3:",self.marks3)

    def calculate_total(self):
        print(f"\n-----{self.name}------")
        total = self.marks1 + self.marks2 + self.marks3
        print("Total Marks:",total)

    def calculate_average(self):
        total = self.marks1 + self.marks2 + self.marks3
        average = total/3
        print(f"Average Marks:{average:.2f}")

s1 = Student("Aryan", 90,98,94)
s2 = Student("Krishna", 91,92,89)
s3 = Student("Mayur", 83,88,78)
s1.calculate_total()
s1.calculate_average()
s2.calculate_total()
s2.calculate_average()
s3.calculate_total()
s3.calculate_average()