#Write a program that calculates the area of a rectangle. 
# Add a single-line comment explaining the formula used, 
# and a multi-line comment (docstring style) at the top 
# describing what the program does.

def area(l,b):
    l = 20 #Length
    b = 10 #Breadth
    """
    When the length is multiplied with the breadth then it gives Area.
    Here, length is multiplied with breadth.

    Args:
        l (float/int): Length of the rectangle.
        b (float/int): Breadth of the rectangle.

    Returns:
        float/int: The calculated area of the rectangle.
    """
    area = l*b #Formula for Area = Length * Breadth 
    return area

result = area(20, 10)
print(f"The area of a rectangle is {result}")

# 2. Accessing and printing the docstring
print("\n--- Docstring ---")
print(area.__doc__)