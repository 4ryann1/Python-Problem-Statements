# Problem 2: Constructor in Inheritance

# Create a Python program to understand constructors in inheritance.

# Requirements:
# - Create a parent class named Animal with a constructor that accepts name.
# - Create a child class named Dog that inherits from Animal.
# - The Dog constructor should accept name and breed.
# - Use super() to call the parent constructor.
# - Add a display() method to display the dog's name and breed.
# - Create at least two Dog objects and display their details.

class Animal:
    def __init__(self,name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print(f"\nDog Name: {self.name}")
        print(f"Breed: {self.breed}")

dog1 = Dog("Tommy","Gavthi")
dog2 = Dog("Dogesh Bhau","Labrador")

dog1.display()
dog2.display()