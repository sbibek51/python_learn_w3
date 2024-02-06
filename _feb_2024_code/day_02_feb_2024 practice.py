# Today I am looking at the Python Arrays
# python does not have an data type array but we can use list as an array
# arrays are used to store a multiple value to a single variabla

cars =['Ford','Volvo','Bmw']
print(cars)

# we  access to an array by referring a index
x=cars[0]
print(x)

# length of an array is always 1 higher than the last index
x=len(cars)
print(x)

# we can loop through using the for loops
for i in cars:
    print(i)

# adding array elements
cars.append('Mustang')
print(cars)

# deleting an item eg delete second item
x=cars.pop(1)
print(x)

# sort ,reverse,insert,count,clear are some array Methods
# tomorrow python class and object