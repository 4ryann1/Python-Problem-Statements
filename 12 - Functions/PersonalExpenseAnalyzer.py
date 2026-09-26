# 10. Personal Expense Analyzer 💰
# Create functions to analyze a list of expenses.
#
# Example:
#
# expenses = [250, 500, 120, 800, 350, 1000]
#
# Create separate functions:
#
# total_expenses()
# average_expense()
# highest_expense()
# lowest_expense()
# count_expenses()
#
# Example output:
#
# Total Expenses: ₹3020
# Average Expense: ₹503.33
# Highest Expense: ₹1000
# Lowest Expense: ₹120
# Number of Expenses: 6

def main(expenses):
    expenses = [250, 500, 120, 800, 350, 1000]
    def total_expense(expenses):
        total_expense = 0
        for expense in expenses:
            total_expense += expense
        print("Total expense:", total_expense)
    def average_expense(expenses):
        average_expense = total_expense / len(expenses)
        print("Average expense:", average_expense)
    def highest_expense(expenses):
        highest_expense = max(expenses)
        print("Highest expense:", highest_expense)
    def lowest_expense(expenses):
        lowest_expense = min(expenses)
        print("Lowest expense:", lowest_expense)
    def count_expense(expenses):
        count_expense = len(expenses)
        print("Count expense:", count_expense)

expenses = [250, 500, 120, 800, 350, 1000]
main()