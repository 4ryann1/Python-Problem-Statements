# Problem 5: Method Overriding

# Create a Python program demonstrating method overriding.

# Requirements:
# - Create a parent class named Animal.
# - Define a method sound() that prints a general animal sound.
# - Create two child classes: Dog and Cat.
# - Override the sound() method in both child classes.
# - Create objects of Animal, Dog, and Cat.
# - Call sound() for each object and observe the different outputs.

class Animal:
    def sound(self):
        print(f"Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print(f"Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

# Call sound() for each object
animal.sound()
dog.sound()
cat.sound()