'''Write a Python function that takes two lists and returns true if they have
at least one common member.'''

def common(list1,list2):
    result =False
    for i in list1:
        for j in list2:
            if i==j:
                result=True
                return result
#comman value list o/p true and not common value o/p none
print(common([1,2,3,4],[9,5,6,7]))
print(common([1,2,3,4],[1,3,7,8]))
