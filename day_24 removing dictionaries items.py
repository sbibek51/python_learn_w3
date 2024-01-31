# removing an item from the dictionaries
my_car ={
    'brand':'Ford',
    'model': 'Mustang',
    'year': 1995,
    'color': ['Green','Red','Blue']

}

print(my_car)

# we can pop item to delete from an dictionaries by passing key as an argument
x=my_car.pop('model')
print(x)
print(my_car)

my_car['country']='Canada'

print(my_car.values())

# the popitem method removes the last inserted item

y= my_car.popitem()
print(y)
print(my_car)

# del keyword can be used to delete by passing an key
del my_car['year']
print(my_car)

del my_car['color']
print(my_car)


# clear method empties the dictionaried
my_car.clear()
print(my_car)

# del can also be used to delete the whole dictionaries
# del my_car
print(my_car)



print(my_car)


my_mobile ={
    'model': 'redmi',
    'brand': 'xiaomi',
    'bought_year':2019,
    'price':35000
}

print(my_mobile)

for i in my_mobile:
    print(i)

# this is returning the key values
# we can print the values as well
for i in my_mobile:
    print(my_mobile[i])



print('printing using the values method:')
# we can also use values method
for i in my_mobile.values():
    print(i)


# we can use keys methods to return keys as well
print('printing using tee keys method to print only keys')
for i in my_mobile.keys():
    print(i)


# we can use .items method to loop through both keys and values as well

for x,y in my_mobile.items():
    print(x,':',y)


# tomorrow copy dictionaries

