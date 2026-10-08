# Problem 25: Create an ExpenseTracker class containing a list of expenses.
# Create add_expense(description, amount), show_expenses(), calculate_total(),
# and find_highest_expense().
#
# Goal: Practice lists inside objects and several methods using the same data.

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        expense = {
            "description": description,
            "amount": amount
        }
        self.expenses.append(expense)

    def show_expenses(self):
        for expense in self.expenses:
            print(f"{expense['description']}: ₹{expense['amount']}")

    def calculate_total(self):
        total = 0

        for expense in self.expenses:
            total += expense["amount"]

        return total

    def find_highest_expense(self):
        if not self.expenses:
            return None

        highest = self.expenses[0]

        for expense in self.expenses:
            if expense["amount"] > highest["amount"]:
                highest = expense

        return highest


# Create object
tracker = ExpenseTracker()

# Add expenses
tracker.add_expense("Food", 250)
tracker.add_expense("Travel", 120)
tracker.add_expense("Shopping", 800)
tracker.add_expense("Movie", 300)

# Display expenses
print("Expenses:")
tracker.show_expenses()

# Calculate total
print("\nTotal Expense:", tracker.calculate_total())

# Find highest expense
highest = tracker.find_highest_expense()

print("\nHighest Expense:")
print(f"{highest['description']}: ₹{highest['amount']}")