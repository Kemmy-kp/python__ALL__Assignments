#Write a Python program to read last n lines of a file.

n = int(input("Enter n lines To Read : "))
f = open("2)my file.txt","r")
for line in (f.readline()[-n:]):
    print(line,end="")
f.close()
