# Problem 30: 
# Build a basic Student Management System using only fundamental OOP. 
# Student has roll_number, name, age, course, and marks with display_details(), calculate_percentage(), calculate_grade(), and update_marks(). 
# StudentManager stores Student objects and provides add_student(), remove_student(roll_number), search_student(roll_number), display_all_students(), and find_top_student().

# Goal: Combine classes, objects, __init__(), attributes, methods, class attributes where useful, lists/dictionaries, and multiple objects.

# Strictly avoid: inheritance, polymorphism, encapsulation, abstraction, abstract classes, interfaces, decorators, and advanced magic methods.

class Student:
    def __init__(self, roll_number,name,age,course,marks):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display_details(self):
        print(f"Roll Number : {self.roll_number}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Course      : {self.course}")
        print(f"Marks       : {self.marks}")
        print(f"Percentage  : {self.calculate_percentage():.2f}%")
        print(f"Grade       : {self.calculate_grade()}")
        print("-" * 40)

    def calculate_percentage(self):
        total_marks = sum(self.marks)
        percentage = total_marks/len(self.marks)
        return percentage

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 900:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        elif percentage >= 40:
            return "F"
        else:
            return

    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"The marks has been successfully updated for {self.name}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added successfully.")

    def remove_students(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student with Roll Number {roll_number} removed successfully.")
                return
        print("Student not found!")

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print("\nStudent Found:")
                student.display_details
                return student
        print("Student Not Found.")
        return None

    def display_all_students(self):
        if not self.students:
            print("No Students Available.")
            return
        print("\n===== ALL STUDENTS =====")
        
        for student in self.students:
            student.display_details()

    def find_top_student(self):
        if not self.students:
            print("No students available.")
            return None

        top_student = self.students[0]

        for student in self.students:
            if student.calculate_percentage() > top_student.calculate_percentage():
                top_student = student

        print("\n===== TOP STUDENT =====")
        top_student.display_details()
        return top_student

student1 = Student(
    101,
    "Aryan",
    21,
    "AI & DS",
    [85, 90, 88, 92, 87]
)

student2 = Student(
    102,
    "Rahul",
    21,
    "Computer Engineering",
    [78, 82, 75, 80, 77]
)

student3 = Student(
    103,
    "Priya",
    20,
    "AI & DS",
    [92, 95, 90, 94, 96]
)


# Create StudentManager object

manager = StudentManager()


# Add students

manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)


# Display all students

manager.display_all_students()


# Search student

manager.search_student(102)


# Update marks

student2.update_marks([85, 88, 82, 90, 86])


# Display updated student

print("\n===== AFTER MARKS UPDATE =====")
student2.display_details()


# Find top student

manager.find_top_student()


# Remove student

manager.remove_student(102)


# Display students after removal

print("\n===== AFTER REMOVING STUDENT =====")
manager.display_all_students()