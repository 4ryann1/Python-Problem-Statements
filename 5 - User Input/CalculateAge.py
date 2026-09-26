# Calculate Age
# Take the user's birth year as input and calculate their approximate age using the current year.

birth_year = int(input("What is your birth year? "))
current_year = int(input("What is your current year? "))

age = current_year - birth_year
print(f"You are {age} years old")