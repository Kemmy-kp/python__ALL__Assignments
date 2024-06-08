'''Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5.'''

#5,5=true
#2+3=true
#10-5=true
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
if x==y or abs(x-y)== 5 or (x+y)==5:
    result= True
else:
    result= False

    #abs method is (-int)makew positive value
print(result)






