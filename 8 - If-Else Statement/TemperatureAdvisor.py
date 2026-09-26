# 9. Temperature Advisor
#
# Take temperature in Celsius.
#
# Below 10 → "Very Cold"
# 10–19 → "Cold"
# 20–29 → "Moderate"
# 30–39 → "Hot"
# 40 or above → "Very Hot"

temp = float(input("Enter temperature in Celsius: "))

if temp<10:
    print("Very Cold")
elif temp< 20 and temp>10:
    print("Cold")
elif temp>20 and temp<30:
    print("Moderate")
elif temp>30 and temp<40:
    print("Hot")
elif temp>40:
    print("Very hot")