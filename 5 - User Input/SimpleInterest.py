# Simple Interest
# Take principal, rate, and time from the user and calculate simple interest.

principal = int(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

Simple_Interest = principal * rate * time

print(f"The Simple Interest is {Simple_Interest}")