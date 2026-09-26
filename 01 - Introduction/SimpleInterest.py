# Calculate Simple Interest
# Take Principal, Rate, and Time as input and calculate simple interest.
# Formula: SI = (P × R × T) / 100

principal = int(input("Enter principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time of interest: "))

Simple_Interest = principal * rate * time

print(f"The Simple Interest is: {Simple_Interest}")