'''Write a Python function that takes a list of words and returns the length
of the longest one.'''

word_list = ["apple","mango","cherry","watermelon"]

longest_length = 0

for word in word_list:
    if len(word) > longest_length:
        longest_length = len(word)

print("Length of the longest word:", longest_length)
