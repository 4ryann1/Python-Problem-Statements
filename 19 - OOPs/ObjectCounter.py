# Problem 21: Create a Student class with a class attribute student_count starting at 0. 
# Increase it whenever a Student object is created. Create five objects and display the count.

# Goal: Understand the difference between class and instance attributes.

class Student:
    student_count = 0
    def __init__(self,name):
        self.name = name
        Student.student_count+=1

student1 = Student("Aryan")
student2 = Student("Mayur")
student3 = Student("Rohit")
student4 = Student("Atharva")
student5 = Student("Krishna")
student6 = Student("Ganesh")

print(f"Total students created: {Student.student_count}")