# Problem 14: Create an Employee class with name and basic_salary.
# Create calculate_bonus() for a 10% bonus and calculate_total_salary().
# Display the result.
#
# Goal: Understand methods using results from other methods.

class Employee:
    print("---------------EMPLOYEE DETAILS----------------")
    def __init__(self,name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary
    def calculate_bonus(self):
        print(f"\n--------{self.name}----------")
        self.bonus = self.basic_salary * 0.10
        print("Bonus:",self.bonus)

    def calculate_total_salary(self):
        self.total_salary = self.basic_salary + (self.basic_salary*0.10)
        print("Total Salary:",self.total_salary)

employee1 = Employee("Aryan", 90000)
employee2 = Employee("Krishna", 80000)
employee3 = Employee("Rohit", 70000)

employee1.calculate_bonus()
employee1.calculate_total_salary()
employee2.calculate_bonus()
employee2.calculate_total_salary()
employee3.calculate_bonus()
employee3.calculate_total_salary()
