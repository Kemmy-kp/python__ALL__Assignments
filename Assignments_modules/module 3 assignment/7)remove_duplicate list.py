#Write a Python program to remove duplicates from a list
a=[10,20,30,40,50,60,30,20]
result=[]

for i in a:
    if i not in result:
        result.append(i)
print(result)
