str1=input("Enter string:")
word=input("Enter word:")
count=0
a=str1.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:",count)
