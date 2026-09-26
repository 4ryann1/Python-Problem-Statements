"""Problem 2: Add and Update Dictionary Elements

Create a dictionary with a person's name and age.
Add a city, update the age, and add a profession. Print the final dictionary.

Write your solution below.
"""

person = {
    "Name": "Aryan",
    "Age": 21,
}

person.update({
    "City": "Pune",
    "Age": 21,
    "Profession": "Engineer"
})
for key, value in person.items():
    print(key, value)