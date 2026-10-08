# Problem 9: Multiple Inheritance

# Create a Python program demonstrating multiple inheritance.

# Requirements:
# - Create a class named Father with a father_property attribute and display_father_property().
# - Create a class named Mother with a mother_property attribute and display_mother_property().
# - Create a child class named Child that inherits from both Father and Mother.
# - Add a child_name attribute.
# - Create a display() method that displays the child's name and both inherited properties.
# - Create a Child object and demonstrate access to methods from both parent classes.

class Father:
    def __init__(self, father_property):
        self.father_property = father_property

    def display_father_property(self):
        print(f"Father Property: {self.father_property}")

class Mother:
    def __init__(self, mother_property):
        self.mother_property = mother_property

    def display_mother_property(self):
        print(f"Mother Property: {self.mother_property}")

class Child(Father, Mother):
    def __init__(self, name, father_property, mother_property):
        Father.__init__(self,father_property)
        Mother.__init__(self,mother_property)
        self.name = name

    def display(self):
        print(f"\nChild Name: {self.name}")
        self.display_father_property()
        self.display_mother_property()

# Create Child object
child1 = Child("Aryan", "Loan", "Gold")
child2 = Child("Bhushan","House","Maa ka Pyaar")
child3 = Child("Om","Land","Gold and Silver")


# Display child and inherited properties
child1.display()
child2.display()
child3.display()

# Access methods from both parent classes
# child1.display_father_property()
# child1.display_mother_property()