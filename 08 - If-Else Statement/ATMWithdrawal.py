# 15. ATM Withdrawal
#
# Take:
# Account balance
# Withdrawal amount
#
# Allow withdrawal only if:
#
# Amount is positive
# Amount is a multiple of 100
# Amount does not exceed balance
#
# Otherwise, display an appropriate error message.

account_balance = float(input("Enter your account balance: "))
withdrawal_amount = float(input("Enter your withdrawal amount: "))

if withdrawal_amount>0 and withdrawal_amount%100==0 and account_balance>=withdrawal_amount:
    print(f"You are eligible to withdraw {withdrawal_amount}.")
    print(f"Your account balance after withdrawal is {account_balance-withdrawal_amount}.")
else:
    print("ERROR! Insufficient Funds.")