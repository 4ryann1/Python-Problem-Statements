# 16. Income Tax Calculator
#
# Take annual income and calculate tax:
#
# ₹0–₹2,50,000 → No tax
# ₹2,50,001–₹5,00,000 → 5%
# ₹5,00,001–₹10,00,000 → 20%
# Above ₹10,00,000 → 30%
#
# Display the calculated tax.
#
# Challenge: Calculate tax progressively rather than applying one percentage to the entire income.

annual_income = float(input("Enter your annual income: "))

if annual_income>0 and annual_income <= 250000:
    print(f"Your annual income is {annual_income}. You don't have to pay tax.")
elif annual_income>250000 and annual_income <= 500000:
    tax = 0.05*annual_income
    print(f"You have to pay tax i.e. 5%. Hence, your income is {annual_income-tax:.2f}.")
elif annual_income>500000 and annual_income <= 1000000:
    tax = 0.20*annual_income
    print(f"You have to pay 20% tax. Your income is {annual_income-tax:.2f}.")
elif annual_income>1000000:
    tax = 0.30*annual_income
    print(f"You have to pay 30% tax. Your income is {annual_income-tax:.2f}.")
else:
    print("Invalid Input")