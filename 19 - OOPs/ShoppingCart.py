# Problem 24: Create a ShoppingCart class that stores products. 
# Add add_product(name, price, quantity), remove_product(name), calculate_total(), and display_cart(). 
# Allow multiple products.

# Goal: Store and manage a collection of data inside an object.

class ShoppingCart:
    def __init__(self,products):
        self.products = products

    def add_product(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.products = self.products.append(name)

    def remove_product(self,name):
        self.name = name
        self.products.remove(name)
        print(f"The product {self.name} is removed from {self.products}")

    def calculate_total(self):
        total = 0
        total += sum
        return sum

    def display_cart(self):
        for product in self.products:
            print(product)

sc1 = [1,2,3,4,5,7,8]
sc1.display_cart()