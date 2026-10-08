# Problem 7: Create a Rectangle class.
# Use __init__() for length and width.
# Create calculate_area() that returns length × width.
# Display the result.
#
# Goal: Practice constructors, attributes, and return values.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

area1 = Rectangle(20,10)
print(area1.calculate_area())
