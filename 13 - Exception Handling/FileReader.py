# 6. File Reader
#
# Ask the user for a filename and open the file.
#
# Requirements:
#
# Display the contents of the file.
# Handle FileNotFoundError.
# Handle other possible exceptions using a general Exception.
# Use finally to display "Program finished."

filename = input("Enter the name of File:")

try:
    with open(filename) as file:
        content = file.read()
        print("-"*10)
        print(content)
        print("-"*10)

except FileNotFoundError:
    print(f"Sorry, {filename} is not available.")

except Exception as error:
    print(f"Error: {error}")

finally:
    print(f"Program Ends.")