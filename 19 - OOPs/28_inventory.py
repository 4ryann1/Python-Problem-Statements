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

    def add_stock(self):
        self.stock += self.price
        print(self.stock)

    def sell_stock(self):
        if self.stock > 0:
            print("Stock is ready to be sold.")
            self.stock -= self.price
        else:
            print("Stock is not ready to be sold.")

    def calculate_stock(self):
        self.stock += self.price