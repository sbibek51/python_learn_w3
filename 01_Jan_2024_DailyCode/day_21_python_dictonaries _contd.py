# python dictionaries are used to store epements in key value pair
this_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1987
}

print(this_dict)
print('Model of Ford is: ;', this_dict['model'])

# dictionaries are ordered from python 3.7 and latest version but it was onordered in earlier version
# they are changeble mean we can add remove or edit the dictionaries elements
# dictionaries does not allowed the duplicate item

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1995,
    'year': 1996
}

print(car)
print('in set duplicates key the value will be overwrite')

# printing the dictionaries length
print('length of dictionaries is:', len(car))

# The value of dictionaries can be of any type


my_car = {
    'Brand': 'Ford',
    'Model': 'Mustang',
    'Year': '1997',
    'Electric': False,
    'colors': {'white', 'yellow', 'red'}
}

print(my_car)

print(len(my_car))
print('item popped', my_car.pop('Year'))
print(my_car)
