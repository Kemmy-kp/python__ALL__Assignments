#Write a Python program to print all unique values in a dictionary.

L1 = [{"1":"S1"}, {"2": "S2"}, {"3": "S1"}, {"4": "S5"}, {"5":"S5"}, {"6":"S9"},{"7":"S7"}]
print("Original List: ",L1)
unique_value = set( value for dic in L1 for value in dic.values())
print("Unique Values: ",unique_value)
