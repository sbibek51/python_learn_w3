#function continue
#last time we did code till recursive function
# PYTHON LAMBDA

"""a lambda function is a small anonymous function
    a lambda function can take any number of arguments but can only
have one expression"""

# syntax is lambda arguments : expression
# example

x= lambda a : a + 10

print(x(5))


# lambda function can take any number of arguments
x= lambda a,b : a*b
print(x(5,10))

# summarize the three numbers and return the result
x= lambda a,b,c: a+b+c
print(x(1,2,3))

""" 
why to use lambda function: the power of lambda function is shown when we have to
use them as an anonymous function inside the another function
"""


# examples of anonomously using the lambda

def my_function(n):
    return lambda a: a*n
my_doubler = my_function(2)  #after return it is like my_doubler = lambda a:a*2
print(my_doubler(5))

# when myfunction is called with parameter 2 it returns the lambda function  with n is 2

def my_function(n):
    return lambda a: a*n

my_tripler =my_function(3)
print(my_tripler(66))

# or let us use both in same function

def my_function(n):
    return lambda a : a* n

my_doubler = my_function(2)
my_tripler = my_function(3)

print(my_doubler(50))
print(my_tripler(100))

# use lambda function when an anonymous function is needed for a short period of time

#tomorrow arrays
