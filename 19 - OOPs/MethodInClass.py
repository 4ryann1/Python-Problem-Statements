# Problem 3: Create a Student class with a method display_name() that displays the student's name.
# Create an object, assign a name, and call the method.
#
# Goal: Understand methods and how objects call them.

class Student:
    def diplay(self):
        print(self.name)

student1 = Student()
student1.name = "Aryan"
student1.diplay()