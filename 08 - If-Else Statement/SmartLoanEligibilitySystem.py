# 20. Smart Loan Eligibility System 🧠
#
# Create a loan eligibility checker using:
#
# Age
# Monthly income
# Credit score
# Existing loan status
# Employment status
#
# Rules:
#
# Age must be between 21 and 60
# Income must be >= ₹25,000
# Credit score >= 700
# Existing loans must not be overdue
# Applicant must be employed
#
# Output one of:
#
# Loan Approved
# Loan Rejected
# Conditionally Approved
#
# For Conditionally Approved, allow the application when the applicant fails only one requirement but has a credit score ≥ 750.
#
# Challenge: Display exactly which condition caused rejection.

# 1. Inputs
age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
loans_overdue = input("Loans overdue? (yes/no): ")
employed = input("Are you employed? (yes/no): ")

# 2. Count failures & save reasons
failures = 0
reasons = ""

if age < 21 or age > 60:
    failures += 1
    reasons += "- Age must be 21 to 60\n"

if income < 25000:
    failures += 1
    reasons += "- Income must be at least 25000\n"

if credit_score < 700:
    failures += 1
    reasons += "- Credit score must be at least 700\n"

if loans_overdue == "yes":
    failures += 1
    reasons += "- Existing loans must not be overdue\n"

if employed == "no":
    failures += 1
    reasons += "- Applicant must be employed\n"

# 3. Print Output
print("\n---------- Decision ----------")

if failures == 0:
    print("Loan Approved")
elif failures == 1 and credit_score >= 750:
    print("Conditionally Approved")
    print("Failed condition:\n" + reasons)
else:
    print("Loan Rejected")
    print("Rejection reasons:\n" + reasons)