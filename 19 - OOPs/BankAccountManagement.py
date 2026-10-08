# Problem 27:
# Create a BankAccount class with account_number, account_holder, and balance.
# Add deposit(), withdraw(), check_balance(), and display_account().
# Create multiple accounts and perform operations on them.
#
# Goal: Practice independent object state and multiple operations.

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("\nDeposit Successful")
            print(f"Now the account balance is: {self.balance}")
        else:
            print("\nDeposit Failed")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nWithdraw Failed. Withdrawable amount should not be greater than your balance")
        else:
            self.balance -= amount
            print("\nWithdraw Successful")
            print(f"Now the account balance is: {self.balance}")

    def check_balance(self, amount):
        print("\nChecking balance...")
        print(f"Now the account balance is: {self.balance}")

    def display_balance(self):
        print("\n------ ACCOUNT DETAILS ------")
        print(f"The Account Holder Name: {self.account_holder}")
        print(f"The Account Number: {self.account_number}")
        print(f"The Account Balance: {self.balance}")

acc1 = BankAccount(32010143568,"Aryan Mangesh Patil",12500)
acc1.display_balance()
acc1.deposit(100)
acc1.withdraw(500)
acc1.check_balance(100)
