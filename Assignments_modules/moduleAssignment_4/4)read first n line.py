#Write a Python program to read first n lines of a file.

n = int(input("Enter Lines To Read : "))
f = open("file.txt","r")
for i in range(n):
	print(f.readline())
f.close()
