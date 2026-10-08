# 5. Count Vowels
# Create a function count_vowels(text) that accepts a string and returns the number of vowels.
#
# Example:
#
# Input: "Python Programming"
# Output: 4

def count_vowels(s):
    if s.isalpha():
        count = 0
        for i in s:
            if i in 'aeiou':
                print(f"{i} is a vowel.")
                count += 1
        print(f"There are {count} number of vowels in {s}")

    else:
        raise ValueError


count_vowels("hello")