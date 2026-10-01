# Problem 3: Adding Methods in a Child Class

# Create a program using inheritance where the child class adds its own functionality.

# Requirements:
# - Create a parent class named Vehicle.
# - Add brand and model attributes.
# - Add a display_vehicle() method.
# - Create a child class named Car that inherits from Vehicle.
# - Add a fuel_type attribute.
# - Add a display_car() method that displays all details.
# - Create at least two Car objects.

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print(f"\nCar Brand: {self.brand}")
        print(f"Car Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_car(self):
        print("\n------ CAR DETAILS ------")
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Fuel Type: {self.fuel_type}")

car1 = Car("Mercedes","GLC350","Petrol")
car2 = Car("Hyundai","Venue - HX2","Diesel")
car3 = Car("Suzuki","Baleno","Diesel")

car1.display_car()
car2.display_car()
car3.display_car()