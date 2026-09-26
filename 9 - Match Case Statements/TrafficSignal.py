# 4. Traffic Signal
#
# Take a traffic-light color as input:
#
# "red" → Stop
# "yellow" → Get Ready
# "green" → Go
#
# For any other color, print "Invalid signal".

color = input("Enter the color(\"red\",\"yellow\",\"green\"): ")

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go!")
    case _:
        print("Invalid Input")