#accessing items in dictionaries

#Access Items

my_car ={
    'Brand': 'Ford',
    'Model': 'Mustang',
    'year' : 1996,
    'color' : 'red'
}

print(my_car)
print('Model of My car is:',my_car['Model'])

#there is also a method get() which gives the same result

print('Model of car is:',my_car.get('Model'))

#the keys method gives all the keys in dictionaries
print('keys are:',my_car.keys())

print('color before color change is:')
print('color of car is:',my_car['color'])

my_car['color'] = 'blue'
print('color of a car after change is:',my_car.get('color'))


#getting the values
x = my_car.values()
print(x)


my_car['year'] = 1995



#after changing the values it gets updated in list of values as well
x= my_car.values()
print(x)

print('Items in my car is:')
print(my_car.items())

#add a items in dictionaries and see the changes

print('before adding make city')
print(my_car.items())

my_car['make_city'] = 'New York'

print('after adding the new item')
y = my_car.items()
print(y)


#check if specified item is int the dictionaries

if 'make_city' in my_car:
    print('Yes, make city is an element of the my car')

#change dictonaries iitems in next class

















