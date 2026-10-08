# Problem 6: Using super() with Overridden Methods

# Create a program demonstrating the use of super() when overriding a method.

# Requirements:
# - Create a parent class named Person.
# - Define a display() method that prints the person's name.
# - Create a child class named Student.
# - Override the display() method in Student.
# - Inside Student.display(), first call the parent display() method using super().
# - Then display the student's roll number and course.
# - Create a Student object and call display().

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Person Name: {self.name}")

class Student(Person):
    def __init__(self, name, roll_number, course):
        super().__init__(name)
        self.roll_number = roll_number
        self.course = course

    def display(self):
        print("\n---------- STUDENT DETAILS ------------")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Roll Number: {self.roll_number}")

student1 = Student("Aryan", 101, "ML Engineering")
student2 = Student("Rohit", 102, "AI Engineering")
student3 = Student("Atharva", 103, "Java Developer")

student1.display()
student2.display()
student3.display()