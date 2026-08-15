# ==============================================================================
# PROBLEM STATEMENT 7: Palindrome Checker
# Task: Determine whether a given word or phrase reads the same forward and backward.
# Goal: Practice string cleaning, slicing/reversing, and conditional evaluation.
# Example: Input: "radar" -> Output: True; Input: "hello" -> Output: False
# ==============================================================================

def is_palindrome(s):
    # Clean string: remove non-alphanumeric and convert to lowercase
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_str = "radar"
    print(f"Is '{test_str}' a palindrome? {is_palindrome(test_str)}")
    
    test_str2 = "hello"
    print(f"Is '{test_str2}' a palindrome? {is_palindrome(test_str2)}")
