# Problem 10: Create a BankAccount class with account_holder and balance.
# Create deposit(), withdraw(), and display_balance().
# Withdraw only when sufficient balance exists.
#
# Goal: Change object attributes through methods.

class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"The account balance is: {self.balance}")
        else:
            print("Invalid amount. Amount should be greater than zero.")

    def withdraw(self,amount):
        if amount > 0:
            print("The current account balance is: ",self.balance-amount)
        else:
            print("Invalid amount. Amount should be greater than zero.")

    def display_balance(self):
        print(f"The current account balance is: {self.balance}")

s1 = BankAccount("Aryan Mangesh Patil",10000)
s1.display_balance()
s1.deposit(1000)
s1.withdraw(2000)