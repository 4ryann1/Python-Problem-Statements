# Check Palindrome
# Take a string from the user and check whether it is a palindrome using string slicing.
# Example: madam → Palindrome


language = "malayalam"
reverse = language[::-1]
print(reverse)
if language == reverse:
    print(f"{language} is a palindrome")
else:
    print(f"{language} is not a palindrome")