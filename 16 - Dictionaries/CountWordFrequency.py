"""Problem 9: Count Word Frequency

Accept a sentence and use a dictionary to count how many times each word appears.

Write your solution below.
"""

dict = {}

sentence = input("Enter sentence: ")
for word in sentence.split():
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
print(dict)