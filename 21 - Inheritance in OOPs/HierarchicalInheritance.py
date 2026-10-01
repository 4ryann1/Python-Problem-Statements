# Problem 8: Hierarchical Inheritance

# Create a Python program demonstrating hierarchical inheritance.

# Requirements:
# - Create a parent class named Shape.
# - Add a color attribute and a display_color() method.
# - Create two child classes: Circle and Rectangle.
# - Circle should have a radius and a calculate_area() method.
# - Rectangle should have length and width and a calculate_area() method.
# - Create objects of both Circle and Rectangle.
# - Display their color and calculated area.

class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"\nShape Colour: {self.color}")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        area_circle = 2 * 3.14 * self.radius
        print(f"Area of circle: {area_circle:.2f}")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print(f"Area of Rectangle: {area}")

# Create objects
circle1 = Circle("Red", 5)
rectangle1 = Rectangle("Blue", 10, 5)

# Display Circle details
circle1.display_color()
circle1.calculate_area()

rectangle1.display_color()
rectangle1.calculate_area()