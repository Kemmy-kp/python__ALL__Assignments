#Write a Python script to print a dictionary where the keys are numbers between
#1 and 15.

l=int(input("Enter the Limit : "))
d = dict()
for x in range(1,l+1):
    d[x]=x**2
print(d)


d=dict()
for x in range(1,5):
    d[x]=x**2
print(d)  
 
