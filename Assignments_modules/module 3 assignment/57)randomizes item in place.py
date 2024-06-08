#How will you randomizes the items of a list in place? 

The method shuffle() can be used to randomize the items of a list in place.
It should be noted that this function is not accessible directly and therefore
we need to import or call this function using random static object.

Syntax:   shuffle (lst)

import random

list = [20, 16, 10, 5];

random.shuffle(list)

print "Reshuffled list : ",  list

random.shuffle(list)

print "Reshuffled list : ",  list

Output : 

Reshuffled list :  [16, 10, 5, 20]

Reshuffled list :  [5, 20, 10, 16]
