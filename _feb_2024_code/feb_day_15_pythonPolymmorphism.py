# Bibek Shiwakoti
# Today we are learnig the concept of polymorphism in python

# Control shift alt and L for the format code in pycharm

"""The word polymorphism mean many forms it refers to the method / functions/operators
that refers to the same name that can be executed on many objects or classes"""

# Function Polymorphism
# eg. for string len() method returns the number of characters

x = 'Hello World'
print(len(x))

# For tuples len() returns the number of items in the tuple

my_tuple = ('apple', 'banana', 'cherry')
print('lengthe of given tuple is {}.'.format(len(my_tuple)))

# For dictionary len() returnns the length of key value pair in the dictionary

my_dictionary = {
    'Apple': 3,
    'Cherry': 5,
    'Pomorgenate': 7
}
print('length of dictionary is ',len(my_dictionary))


for key,value in my_dictionary.items():
    print(key,value)



    # Tomorrow class polymorphism