# Problem 11: Create a Student class with name, age, and course.
# Create at least three different Student objects and display each object's details.
#
# Goal: Understand that one class can create many independent objects.

class Student:
    def __init__(self,name,age, course):
        self.name = name
        self.age = age
        self.course = course
    def display(self):
        print("Student Name:",self.name)
        print("Student Age:",self.age)
        print("Student Course:",self.course)

student1 = Student("Aryan", 20, "ML Engineering")
student2 = Student("Krishna", 22, "Berozgaar")
student3 = Student("Rohit", 21, "AI Engineering")
#
# print("Student Name:",student1.name,"Student Age:",student1.age,"Student Course",student1.course)
# print("Student Name:",student2.name,"Student Age:",student2.age,"Student Course",student2.course)
# print("Student Name:",student3.name,"Student Age:",student3.age,"Student Course",student3.course)

student1.display()
print()
student2.display()
print()
student3.display()