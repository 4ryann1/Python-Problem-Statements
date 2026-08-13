# Accept principal (float), rate (float), and time (int) as inputs, calculate simple interest, and display the result rounded to 2 decimal places.

principal = float(input("Enter the principal amount:"))
interest_rate = float(input("Enter the Interest Rate:"))
time = int(float(input("Enter the time:")))

simple_interest = (principal*interest_rate*time)/100

print(f"The Simple Interest is: {simple_interest:.2f}")