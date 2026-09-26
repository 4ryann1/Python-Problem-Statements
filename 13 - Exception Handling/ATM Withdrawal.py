# 7. ATM Withdrawal
#
# Create a simple ATM withdrawal program.
#
# The user enters:
#
# Account balance
# Withdrawal amount
#
# Requirements:
#
# Handle non-numeric input.
# Raise a ValueError if the withdrawal amount is negative.
# Raise a custom exception if the withdrawal amount is greater than the balance.
# Display the remaining balance.
#
# Bonus: Create your own exception class:

# Custom exception class
class InsufficientBalanceError(Exception):
    pass


try:
    # 1. Get user inputs
    balance = float(input("Enter account balance: "))
    withdrawal = float(input("Enter withdrawal amount: "))

    # 2. Check logic and raise errors if needed
    if withdrawal < 0:
        raise ValueError("Withdrawal amount cannot be negative.")

    if withdrawal > balance:
        raise InsufficientBalanceError("Withdrawal amount is greater than the balance.")

    # 3. Process withdrawal and show remaining balance
    balance -= withdrawal
    print(f"Remaining balance: {balance}")

# 4. Handle exceptions simply
except ValueError as e:
    # This handles both non-numeric text and the negative amount error
    print(f"Error: {e}")

except InsufficientBalanceError as e:
    print(f"Error: {e}")
