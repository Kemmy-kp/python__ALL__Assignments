#Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
d1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d1)
sorted_d = sorted(d1.items(), key=operator.itemgetter(1))
print('Ascending order : ',sorted_d)
sorted_d = dict( sorted(d1.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order : ',sorted_d)
