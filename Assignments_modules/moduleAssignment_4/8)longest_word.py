#Write a python program to find the longest words.

f=open("2)my file.txt",'r')
x=f.readline()
print(x.split(' '))
print(len(x.split(' ')))
f.close()
