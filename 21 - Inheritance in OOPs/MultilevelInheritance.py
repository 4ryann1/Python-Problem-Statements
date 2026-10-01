# Problem 7: Multilevel Inheritance

# Create a Python program demonstrating multilevel inheritance.

# Requirements:
# - Create a class named Grandparent with a family_name attribute and a 
# display_family() method.
# - Create a class named Parent that inherits from Grandparent.
# - Add a parent_name attribute and display_parent() method.
# - Create a class named Child that inherits from Parent.
# - Add a child_name attribute and display_child() method.
# - Create a Child object.
# - Use the Child object to access methods from all three classes.

class Grandparent:
    def __init__(self,family_name):
        self.family_name = family_name

    def display_family(self):
        print(f"Family Name: {self.family_name}")

class Parent(Grandparent):
    def __init__(self, family_name, parent_name):
        super().__init__(family_name)
        self.parent_name = parent_name

    def display_parent(self):
        print(f"Parent Name: {self.parent_name}")
        print(f"Family Name: {self.family_name}")

class Child(Parent):
    def __init__(self, name, family_name, parent_name):
        super().__init__(family_name, parent_name)
        self.name = name

    def display(self):
        print(f"\nName: {self.name} {self.parent_name} {self.family_name}")

student1 = Child("Aryan","Patil","Mangesh")
student2 = Child("Shiv","Ingle","Rajesh")
student3 = Child("Mayur","Mahajan","Gajanan")

student1.display()
student2.display()
student3.display()