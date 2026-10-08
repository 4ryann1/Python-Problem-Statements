# Problem 8: Create a Circle class with radius initialized through __init__().
# Create calculate_area() using 3.14 × radius × radius.
#
# Goal: Use object data inside a calculation method.

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius

circle1 = Circle(5)
circle2 = Circle(10)

area1 = circle1.area()
area2 = circle2.area()

print(area1)
print(area2)