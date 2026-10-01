Problem 10: Inheritance-Based Employee Salary System

Create a Python program that combines inheritance, constructors, method reuse, and method overriding.

Requirements:
- Create a parent class named Employee with name and base_salary attributes.
- Add a calculate_salary() method that returns the base salary.
- Create a child class named Developer that inherits from Employee.
- Add a bonus attribute.
- Override calculate_salary() so that it returns base salary + bonus.
- Create another child class named Manager.
- Add an allowance attribute.
- Override calculate_salary() so that it returns base salary + allowance.
- Create at least one Employee, one Developer, and one Manager object.
- Display each employee's name and calculated salary.
- Use super() where appropriate.
