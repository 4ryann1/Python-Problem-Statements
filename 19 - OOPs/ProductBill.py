# Problem 15: Create a Product class with name, price, and quantity.
# Create calculate_total() and display_bill().
# Create at least two product objects.
#
# Goal: Build a small real-world OOP problem.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        total = self.price * self.quantity
        return total

    def display_bill(self):
        print(f"{self.name}: {self.price * self.quantity}")
        total = self.price * self.quantity
        # print("The total bill is",total)

product1 = Product("Pen", 10, 10)
product1.display_bill()
product2 = Product("Bottle", 850, 10)
product2.display_bill()
product3 = Product("Notebook", 700, 10)
product3.display_bill()