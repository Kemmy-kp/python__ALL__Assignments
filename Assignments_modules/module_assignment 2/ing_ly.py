'''Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.'''


input_string = input("enter a string:")
if len(input_string)>= 3 and input_string.endswith('ing'):
  result=input_string[:-3]+'ly'
elif len(input_string)>=3:
  result=input_string+'ing'
else:
  result=input_string
print("result:", result)
