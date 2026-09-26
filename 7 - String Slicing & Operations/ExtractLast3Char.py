# Extract Last 3 Characters
# Take a string from the user and print its last 3 characters using negative indexing/slicing.

string = input("Enter a string: ")
print(string[len(string)-3:len(string)]) #Could be printed as this also

print(string[-3:])  #Proper way of printing the output