'''Write a Python program to get the Fibonacci series of given range.'''

x=0
y=1
n= 10


for i in range(n):
    z=x+y
    x=y
    y=z
    print(z)




