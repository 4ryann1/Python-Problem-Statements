# #Object is a real-world object introduced within a program
# #Class is the collection of objects.
# #Object Oriented Programming helps in reduce code redundancy and increase code reusability.
#
# Example:
# class Student:
#     name = "Aryan"
#
# Example:
# class Car:
#     brand = "Mercedes"

# class Student:
#     name = "Aryan"
#
# s1 = Student()
# print(s1) #Shows the object stored and the location
# print(s1.name) #Prints the value passed in the function
#
# s2 = Student()
# print(s2)
# print(s2.name)

class Car:
    color = "White"
    model = "GLC 350"
    brand = "Mercedes"

car1 = Car()
print(car1.color)

#Constructor: All classes have the function called __init__(),
# which is always executed when the class is being initiated

#The same class can be written as:

class Student:
    college = "DYPTC"
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1=Student("Aryan", 21)
s2=Student("Krishna", 21)
s3=Student("Ganesh",20)

print(f"{s1.name} is from {s1.college}")