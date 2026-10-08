"""Problem 12: Students in Both Classes

Create sets of students in Python and AI/ML classes. Display students in both, only Python, and only AI/ML.
"""

# Write your solution below.

Python = {"Aryan", "Krishna", "Mayur", "Rohit"}
AIML = {"Aryan", "Krishna", "Bhushan", "Atharva"}

print(f"The students in only Python are {Python.difference(AIML)} and AIML are {AIML.difference(Python)}")