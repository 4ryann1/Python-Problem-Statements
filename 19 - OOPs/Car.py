# Problem 12: Create a Car class with brand, model, and year.
# Initialize them with __init__() and create display_details().
# Create three different car objects.
#
# Goal: Practice multiple objects with different data.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print("-"*5,"Details","-"*5)
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
        print()

car1 = Car("Tata", "Punch", "2022")
car2 = Car("Toyota", "Qualis", "2021")
car3 = Car("Hyundai", "Venue", "2020")
car1.display_details()
car2.display_details()
car3.display_details()