'''Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.'''

#enter a string:pammy
#result: pamy

input_string=input("enter a string:")

if len(input_string)<2:
      result="empty string"
else:
      result=input_string[:2]+input_string[-2:]
print("result:",result)

