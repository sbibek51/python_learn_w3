#changing the dictionaries items
#we can change the value of the key by referring to the keys

car= {
    'Brand' : 'Ford',
    'Model' : 'Mustang',
    'year'  : 1998,
    'colors' : ['Red','Blue','White']
}

print(car)
print(car.items())

print(car.keys())
print(car.values())

car['year']= 2000
print(car['year'])
print(car.items())

car['colors'] =['white','red']
print(car.values())

#we can use the update method as well
#we haveto specify the key value pair in the argument

car.update({'model':'Mustang Nepal'})
print(car.values())
print(car.values())

print(car.items())
print(car.keys())
print(car.values())

car.update({'brand': 'Hyundai'})
print(car)

#tomorrow add and update items

term_2 ={
    'data science':'Ali',
    'visualization': 'Reena',
    'advance python': 'Vahid',
    'NLP': 'Pouria',


}

print(term_2)

print(term_2.values())
print(term_2.keys())

term_2['AI ML Lab'] = 'Simrandeep'
print(term_2)

print(type(term_2))

print(term_2.values())
print(term_2.keys())


term_2.update({'college':'lambton'})

print(term_2)


# Removing items






