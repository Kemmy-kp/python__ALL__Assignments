'''Write python program that swap two number with temp variable and
without temp variable.'''

#'''Using a temporary variable'''
x = 5
y = 10

#x = input('Enter value of x: ')
#y = input('Enter value of y: ')


temp = x
x = y
y = temp

print("The value of x after swapping: ",x)
print("The value of y after swapping: ",y)


#with out temp variable.
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

