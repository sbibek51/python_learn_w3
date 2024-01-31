# today we start from copying dictionaries

my_car ={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 2020,
    'country_made': 'Nepal',
    'service_in': '5 months',
}

print(my_car)
for i in my_car.items():
    print(i)

# now we are going to copy a dictionaries and we can not do it by only using the assignment operator
# because if we only used the assignment operator it will only point the reference

# one way is to use copy() method


my_car2= my_car.copy()
print(my_car2)

# another way is to use the method dict


mycar_3 = dict(my_car)
print(mycar_3)

print(type(my_car))
print(type(my_car2))
print(type(mycar_3))

mycar_4= my_car
print(type(mycar_4))
del [my_car['model']]
print(my_car)
print(mycar_4)
print(mycar_3)




#nested dictionaries
# one dictionaries can contain another dictionaries as a value



my_family = {
    'child_1' : {
        'name': 'harry',
        'email': 'harry@gmail.com',
         'dob': 2001
    },


'child_2' : {
        'name': 'mark',
        'email': 'mark@gmail.com',
         'dob': 2003
    },



'child_3' : {
        'name': 'john',
         'dob': 2004
    }
}



print(my_family.keys())

print(my_family.items())

print(my_family.values())



car = {
    'brand' : 'Ford',
    'Model' :'Mustang',
    'chasis' : '1xCvbijb90'
}

bike = {
    'brand' : 'hyundai',
    'year' : 2020,
    'number_plate': 'p3 5811'
}

mobile = {
    'brand' : 'redmi',
    'Ram' : {
        'internal' : '8gb',
        'added' : '4gb'
    }
}


my_gadgets ={
    'car' : car,
    'bike' : bike,
    'mobile' : mobile
}


print(type(my_gadgets))
print(my_gadgets)

print(my_gadgets['car']['brand'])
print(my_gadgets['mobile']['Ram']['added'])

my_gadgets.clear()
print(my_gadgets)