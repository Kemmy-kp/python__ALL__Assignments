#Differentiate between append () and extend () methods?

1. append() method:

-->The append() method is used to add a single element to the end of a list.
-->It takes one argument, which is the element you want to add.
-->the element is added as a single item, even if it's a list or any other iterable.

Example:

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

2. extend() method:

-->The extend() method is used to add multiple elements to the end of a list.
-->It takes an iterable (like a list, tuple, or any other sequence) as an argument and adds its elements to the original list.
-->It effectively appends all the elements from the iterable to the end of the list.

Example:


my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
