#Write a Python program to replace last value of tuples in a list.

list=[(10,20,30),(40,50,60),(70,80,90)]
print([t1[:-1]+(100,)for t1 in list])
