# Calculate the cube of all numbers from 1 to a given number

given_number = int(input("Enter the Number: "))

print("The cubes are as follows:")
for i in range(1,given_number+1):
    print(f"The cube of {i} is: {i*i*i}")