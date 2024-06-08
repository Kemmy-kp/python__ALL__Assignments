'''43)Why Do You Use the Zip () Method in Python? 


The zip() function returns a zip object, which is an iterator of tuples where
the first item in each passed iterator is paired together, and then the second
item in each passed iterator are paired together etc.If the passed iterables
have different lengths, the iterable with the least
items decides the length of the new iterator.

suntax:
    zip(iterator1, iterator2, iterator3 ...)'''


a = ("pammy", "kemmy", "janvi")
b = ("k", "p", "M", "V")

x = zip(a, b)

print(tuple(x))
