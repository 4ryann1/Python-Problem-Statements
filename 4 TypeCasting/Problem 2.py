# Write a program that takes a temperature value as a string (e.g., "98.6") and converts it to a float, then converts Celsius to Fahrenheit and vice versa.

temperature = input("Enter the temperature: ")

temp = float(temperature)
fahrenheit = (temp * 1.8)+32
print(f"Fahrentheit = {fahrenheit}")
print(f"Temperature = {temp}")