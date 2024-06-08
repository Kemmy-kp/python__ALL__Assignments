#Write a Python program to find the highest 3 values in a dictionary

from collections import Counter
my_dict = {'p': 3, 'a': 4, 'm': 6, 'm': 5, 'y': 8}
k = Counter(my_dict)
high = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in high:
   print(i[0]," :",i[1]," ")
