#Python iterators
"""An iterator is an object that contains the countable number of values"""
"""Meaning we can traverse through all the values"""
"""Techniclaly in the python iterator is and object which 
implements the iterator protocol """

"""which consists of __iter__() and __next__()"""

# Iterator vs iterable
# list ,tuple ,dictionaries, and sets all are iterable

my_list = ['apple','banana','cherry']
myit =iter(my_list)

print(next(myit))
print(next(myit))
print(next(myit))


#string is also iterable
#tomorrow we will continue on it