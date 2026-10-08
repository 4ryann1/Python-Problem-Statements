# 10. Basic Command System

# Ask the user to enter a command:
# start
# stop
# pause
# restart
#
# Use match-case to display:
#
# start   → "Program started"
# stop    → "Program stopped"
# pause   → "Program paused"
# restart → "Program restarted"
#
# For any other command, print "Unknown command".

command = input("Enter the command: ")

match command:
    case "start":
        print("Program Started")
    case "stop":
        print("Program Stopped")
    case "pause":
        print("Program Paused")
    case "restart":
        print("Program Restarted")
    case _:
        print("Unknown Command")