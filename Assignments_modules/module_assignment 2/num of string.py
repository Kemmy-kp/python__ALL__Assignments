'''Write a Python program to count the number of characters (character
frequency) in a string'''


string =input("enter a string\n")
char=input("enter the character to count in frequency\n")
count=0

for i in string:
    if(i==char):
        count=count+1
print(f"the frequency of {char}in the string is:{count}")
#character count

'''============================='''
#dictionary key(REMOVED ARE SAME AS TWO ALPHABET)
    
str = "hellohowareyou"

dict = {}

for i in str:

    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1
        
print(dict)
