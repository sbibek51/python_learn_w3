#Bibek shiwakoti
# feb 13 2024

my_str = 'Hello world'

my_it = iter(my_str)

print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))


#Looping through an iterator

# we can also use for loop to iterate through the iterable object

my_tuple =('apple','banana','cherry')

print(my_tuple)

for i in my_tuple:
    print(i)



# iterate the character of a string

my_str = 'Hellp Nepal'

for i in my_str:
    print(i)


"""The for loop actually creates an iterator object and executes the next method for the loop"""
"""the for loop actually creates the iterator object and calls the next method for each 
element in the loop """

#tomorrow we will create our own iterator