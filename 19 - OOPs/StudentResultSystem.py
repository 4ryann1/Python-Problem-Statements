# Problem 26: Create a Student class with name, roll_number, and marks in three subjects. Add calculate_total(), calculate_percentage(), calculate_grade(), and display_result(). Create at least three objects.

# Goal: Build a structured result system using basic OOP.

class Student:
    def __init__(self, name, roll_number, mark1, mark2, mark3):
        self.name = name
        self.roll_number = roll_number
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_total(self):
        return self.mark1 + self.mark2 + self.mark3

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / 3

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display_result(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Total Marks:", self.calculate_total())
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.calculate_grade())
        print("-" * 30)


# Create three Student objects

student1 = Student("Aryan", 101, 85, 90, 88)
