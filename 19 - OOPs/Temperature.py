# Problem 16: Create a Temperature class storing Celsius through __init__().
# Create to_fahrenheit() and to_kelvin() using the standard conversion formulas.
#
# Goal: Create multiple methods operating on the same object data.

class Convertor:
    def __init__(self, temp):
        self.temp = temp

    def to_fahrenheit(self):
        print(f"Fahrenheit:{(self.temp * (9/5)+32):.2f}")

    def to_kelvin(self):
        print(f"Kelvin: {self.temp + 273.15}")

temp1 = Convertor(25)
temp2 = Convertor(20)
temp3 = Convertor(37)

temp1.to_fahrenheit()
temp1.to_kelvin()
print()
temp2.to_fahrenheit()
temp2.to_kelvin()
print()
temp3.to_fahrenheit()
temp3.to_kelvin()