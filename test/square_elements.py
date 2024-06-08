'''WAP to create Function for making square each element in List
	eg : input : [1,2,3,4,5]
	     output : [1,4,9,16,25]'''

list=[1,2,3,4,5]
square_list= []
for i in list:
    square_list.append(i**2)
print(square_list)
    
