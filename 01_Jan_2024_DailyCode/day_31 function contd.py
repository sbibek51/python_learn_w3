#day 31
# function args

# if you do not know how many numbers of arguments will be passed
#     add * before the name of parameters which will help
# this way the function will receve a tuple of arguments

def my_function(*kids):
    print('the oldest kid is :' ,kids[0])
my_function('John', 'Bob', 'Mark')



# arbitary arguments are noted by *args in the python documentation

# we can also send the arguments in form of key value pair:

def my_function(child1, child2, child3):
    print('the youngest child is:',child3)

my_function(child1='Harry', child2='John', child3="Josey")


# this kind of keyword arguments are referred as kwargs in python documentaton
# kw=keyword
# args =arguments


# if you do not know how many parameters will be received in keyword argument add **

def my_function(**kid):
    print('last name of person is:',kid['lname'])

my_function(fnane='bibek',lname='shiwakoti',college='lambton')



# **kwargs =arbitary keyword arguments in python documentation



## Default parameter value

# if we call a function without the argument then the default parameter is used

def my_function(country='Nepal'):
    print('I am form :',country)


my_function("Norway")
my_function()
my_function('Canada')


#passing a list as an arguments
# we can pass any datatypes  of arguments to the function(string,list,set,tuple,dictionary etc.)
# and it will be treated as the same data type inside the function


def my_function(food):
    for i in food:
        print(i)



my_function(['Rice','Paneer','Chicken'])
# or food= ['Rice','Paneer','Chicken'] and my_function(food)



# return value:

# we can use the return statement to return from the function

def double_maker(num):
    return 2*num

print('double of 2 is:',double_maker(2))
print('double of 4 is:',double_maker(4))


# **************************************************

# the pass statement
# function defination can not be empty but in case if we need we need to write the pass
def my_function():
    pass


# position only arguments
def my_function1(x,/):#/specifies function takes only positional argument
    print(x)

my_function1(3)

# if ,/ is not specified we can pass keyword argument even if function expects for positional argument
# but after using ./ we need to pass the positional argument only



# keyword only arguments

# *, to specify that function can only have keyword arguments specify *, before the parameter
def my_function(*,x):
    return x
print('x=',my_function(x=5))


#combined positional only and keyword only arguments
def my_function(a,b,/,*,c,d):
    print('a= {} b= {} c={} and d={}'.format(a,b,c,d))
my_function(2,3,c=4,d=5)

# any arguments before /, are positional and after *, are keyword arguments


# Recursion

# python allows to call function by itself called recursive function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(5)



#NEXT CLASS PYTHON LAMBDA