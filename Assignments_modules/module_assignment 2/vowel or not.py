'''Write a Python program to test whether a passed letter is a vowel or
not.'''

character = input("Enter a character: ")  
    
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
   
if character in vowels:  
    print(f"The character  is a vowel!")  
else:  
    print(f"The character is a not vowel!")  
