#Write a Python program to remove an empty tuple(s) from a list of tuples. 
list1=[(),(""),('a','b'),('a','b','c'),('d')]
list1=[i for i in list1 if i]
print(list1)
#empty value not define
