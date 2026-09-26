# 7. Vowel or Consonant
#
# Take a single alphabet character as input.
#
# Use match-case to check whether it is:
#
# a, e, i, o, u → Vowel
# Other alphabet → Consonant
# Anything else → Invalid input

char = input("Enter a char: ")

if len(char) != 1:
    print("Invalid Input")
else:
    match char:
        case "a":
            print(f"The character {char} is a vowel.")
        case "A":
            print(f"The character {char} is a vowel.")
        case "e":
            print(f"The character {char} is a vowel.")
        case "E":
            print(f"The character {char} is a vowel.")
        case "i":
            print(f"The character {char} is a vowel.")
        case "I":
            print(f"The character {char} is a vowel.")
        case "o":
            print(f"The character {char} is a vowel.")
        case "O":
            print(f"The character {char} is a vowel.")
        case "u":
            print(f"The character {char} is a vowel.")
        case "U":
            print(f"The character {char} is a vowel.")
        case char \
            if char.isalpha():
            print(f"The character {char} is a consonant.")
        case _:
            print(f"The character {char} is not a vowel either consonant.")
