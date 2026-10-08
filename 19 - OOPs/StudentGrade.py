# Problem 23: Create a Student class with name and marks. 
# Create calculate_percentage(), calculate_grade(), and display_result(). 
# Use grades: 90+ A, 75-89 B, 60-74 C, 40-59 D, below 40 F.

# Goal: Combine constructors, calculations, conditions, and methods.

class Student:
    def __init__(self, name:str,  marks:list, total_marks=500):
        self.name = name
        self.marks = marks
        self.total_marks = marks
    
    #Calculate Percentage Function/Method
    def calculate_percentage(self):
        if isinstance(self.marks, list):
            obtained = sum(self.marks)
            max_marks = len(self.marks) * 100
        else:
            obtained = self.marks
            max_marks = self.total_marks
        return (obtained / max_marks) * 100

    #Calculate Grade Function/Method
    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return 'A'
        elif percentage >= 75:
            return 'B'
        elif percentage >= 60:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'

    #Displaying the result
    def display_result(self):
        percentage = self.calculate_percentage()
        grade = self.calculate_grade()
        
        print(f"Student Name: {self.name}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")


s1 = Student("Aryan",[98, 97, 90, 95, 93])
s1.display_result()