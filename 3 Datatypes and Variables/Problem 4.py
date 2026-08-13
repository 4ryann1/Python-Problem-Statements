# # Given a list of mixed values (e.g., 42, "hello", 3.14, True, None, [1,2,3]), 
# write a program that iterates through them and prints each value along with its data type using type()

list = [42, "hello", 3.14, True, None, [1,2,3]]

for item in list:
    print(f"{item} is a {type(item)} datatype in list")