#Write a Python program to read an entire text file.

f=open("2)my file.txt",'r')
n=int(input("how many  lines you want to read?:"))
for i in range(n):
    print(f.readline(),end="")
f.close()
