#Today we are gonna study and practice about the python class and objects
""" Python is a OOP language and here everything is object with properties
and methods"""

my_adder= lambda x: x+5

print(my_adder(5))

# creating a new class
class MyClass:
    x=5

print(type(MyClass))
print(MyClass)

# now create an object of myclass and print the value of x,

p1 = MyClass()
print(p1.x)


