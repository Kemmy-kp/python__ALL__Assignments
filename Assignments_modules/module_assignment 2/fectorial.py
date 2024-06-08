'''Write a Python program to get the Factorial number of given number.'''


num = int(input("Enter a number : "))
fact = 1

for i in range(1, num + 1):
        fact = fact * i
print("The factorial is: ",fact)

#============while loop========
i=int(input("enter number"))
fact=1
while i>0:
    fact=fact*i
    i=i-1
print("factorial=",fact)
