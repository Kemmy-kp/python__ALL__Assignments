#How will you compare two lists?

The cmp() function
The set() function and == operator
The sort() function and == operator
The collection.counter() function
The reduce() and map() function

Method 1: Using list.sort() and == operator sort() coupled with == operator can achieve this task. We first sort the list, so that if both the lists are identical,
then they have elements at the same position. But this doesn’t take into account the ordering of elements in list.

Method 2: Using collections.Counter() Using Counter(), we usually are able to get the frequency of each element in a list, checking for it, for both lists,
we can check if two lists are identical or not. But this method also ignores the ordering of the elements in the list and only takes into account the frequency of elements.
