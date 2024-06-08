#Write a Python program to get unique values from a list.
my_list=[10,20,30,10,40,90,60]
print("original list:",my_list)
my_set=set(my_list)
new_list=list(my_set)
print("list of unique numbers:",new_list)
