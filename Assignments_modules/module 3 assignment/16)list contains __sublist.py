#Write a Python program to check whether a list contains a sub list

list=['p','q',[1,2,3,4,5,'pammy']]

for i in list:
    if len(i)>1:
        print("sublist is present in list")
        break
    else:
        print("sublist is not present in list")
