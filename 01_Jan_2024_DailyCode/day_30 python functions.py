#day 30
# today we are going to learn the python functions
# A function is a block of code which runs only when it is claled

# we can pass data known as parameter to the funcionn

# in python function is defined by the keyword def:

def my_function():
    print('Hello World from a function')

# to call a function write a function name followed by a parenthesis

my_function()

# Information can be passed in a function as an argument


# argument are specied after a function name inside a parentheses

def name_printer(fname):
    print('Hello '+fname)

name_printer('Bibek')
name_printer('John')


# parametern is inside the defination
# arguments is passed when the function is called



# number of arguments must match with the number of parameters in the function calling
# otherwise we will get an error




def my_function(fname,lname):
    print('Hello '+fname+' '+lname)


my_function('Bibek','Shiwakoti')



# tomorrow arbitary arguments *args