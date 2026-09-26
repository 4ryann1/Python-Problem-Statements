# 8. Season Finder
#
# Take a season number:
#
# 1 → Spring
# 2 → Summer
# 3 → Monsoon
# 4 → Autumn
# 5 → Winter
#
# Print the corresponding season using match-case.

season = int(input("Enter a season number: \n1. Spring\n2. Summer\n3. Monsoon\n4. Autumn\n5. Winter\n"))

match season:
    case 1:
        print("The season is Spring")
    case 2:
        print("The season is Summer")
    case 3:
        print("The season is Monsoon")
    case 4:
        print("The season is Autumn")
    case 5:
        print("The season is Winter")
    case _:
        print("Invalid Input")