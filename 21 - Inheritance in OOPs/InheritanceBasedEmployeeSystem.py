# Problem 10: Inheritance-Based Employee Salary System

# Create a Python program that combines inheritance, constructors, method reuse, and method overriding.

# Requirements:
# - Create a parent class named Employee with name and base_salary attributes.
# - Add a calculate_salary() method that returns the base salary.
# - Create a child class named Developer that inherits from Employee.
# - Add a bonus attribute.
# - Override calculate_salary() so that it returns base salary + bonus.
# - Create another child class named Manager.
# - Add an allowance attribute.
# - Override calculate_salary() so that it returns base salary + allowance.
# - Create at least one Employee, one Developer, and one Manager object.
# - Display each employee's name and calculated salary.
# - Use super() where appropriate.

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    def __init__(self, name, bonus, base_salary):
        super().__init__(name, base_salary)
        self.bonus = bonus
    
    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

class Manager(Employee):
    def __init__(self, name, base_salary, allowance):
        super().__init__(name, base_salary)
        self.allowance = allowance

    def calculate_salary(self):
        return super().calculate_salary() + self.allowance

employee = Employee("Aryan", 90000)
developer = Developer("Krishna",40000,10000)
manager = Manager("Rohit",50000,15000)

# Display employee details
print("Employee Name:", employee.name)
print("Calculated Salary:", employee.calculate_salary())

print()

print("Developer Name:", developer.name)
print("Calculated Salary:", developer.calculate_salary())

print()

print("Manager Name:", manager.name)
print("Calculated Salary:", manager.calculate_salary())