# Problem 4: Method Reuse Through Inheritance

# Create a program demonstrating how a child class can reuse methods of its parent class.

# Requirements:
# - Create a parent class named Employee.
# - Add name and salary attributes.
# - Create a display_employee() method.
# - Create a child class named Manager that 
# inherits from Employee.
# - Add a department attribute.
# - Create a display_manager() method.
# - Inside display_manager(), reuse display_employee() 
# and then display the department.
# - Create at least two Manager objects.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("\n------- EMPLOYEE DETAILS ------")
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print(f"Department: {self.department}")

manager1 = Manager("Aryan",95000,"IT")
manager2 = Manager("Rohit",52000,"HR")
manager3 = Manager("Atharva",53000,"HR")

manager1.display_manager()
manager2.display_manager()
manager3.display_manager()