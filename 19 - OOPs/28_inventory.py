# Problem 28:
# Create a Product class with product_id, name, price, and stock.
# Add add_stock(), sell_product(), calculate_stock_value(), and display_product().
# Selling must fail when stock is insufficient.
#
# Goal: Combine object state, validation,
# and calculations using basic OOP.

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity
        print(f"{quantity} units added successfully.")

    def sell_product(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"{quantity} units sold successfully.")
        else:
            print("Sale failed: Insufficient stock.")

    def calculate_stock_value(self):
        return self.price * self.stock

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price: ₹", self.price)
        print("Stock:", self.stock)
        print("Stock Value: ₹", self.calculate_stock_value())


# Create object
product1 = Product(101, "Keyboard", 1500, 10)

# Display product
product1.display_product()

print("\nAdding Stock:")
product1.add_stock(5)

print("\nSelling Product:")
product1.sell_product(8)

print("\nTrying to sell more than available stock:")
product1.sell_product(20)

print("\nUpdated Product Details:")
product1.display_product()