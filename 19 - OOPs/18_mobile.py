# Problem 18: Create a Mobile class with brand, model, price, and battery_percentage.
# Create call(), charge(amount), and display_status().
# Charging cannot increase battery above 100.
#
# Goal: Represent and change object state.

class Mobile:
    print("------------- M O B I L E ---------------")
    def __init__(self, brand:str, model:str, price:float, battery_percentage:int):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_percentage = self.battery_percentage = max(0, min(100, battery_percentage))

    def call(self,duration:int):
        if self.battery_percentage <= 0:
            print(f"You cannot make a call with {self.battery_percentage}%}")
            return

    def charge(self, amount):
        self.battery_percentage += amount
        return self.battery_percentage

    def display_status(self):
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

