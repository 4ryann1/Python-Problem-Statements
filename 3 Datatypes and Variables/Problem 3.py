# # Take a temperature value in Celsius (float) and convert it to Fahrenheit and Kelvin. 
# Print all three values with appropriate labels, demonstrating float arithmetic and formatted output.

celsuis = float(input("Enter the Celsuis:"))

fahrenheit = (celsuis*1.8) +32
kelvin = celsius+273.15

print(f"{celsuis} Celsius = {fahrenheit} Fahrenheit")
print(f"{celsuis} Celsius = {kelvin} Kelvin")