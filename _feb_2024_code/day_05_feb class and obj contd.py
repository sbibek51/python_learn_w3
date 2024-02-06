#Bibek Shiwakoti
class Person:
    def __init__(self,name,age):
        self.name =name
        self.age=age



p1= Person("Bibek",28)
print('Name:',p1.name)
print('Age:',p1.age)


#*************************
"""If the __str__() function is not initialized than string
representation form of the object is returned for example let us try to 
print the above object (mean printing the object without accessing the parameter)"""





class Car:
    def __init__(self,brand,cc):
        self.brand = brand
        self.cc = cc

c1 = Car('Ford',120)

print(c1)
##############now we use __str__() method so we can print the object

class Car:
    def __init__(self,brand,cc):
        self.brand = brand
        self.cc = cc
    def __str__(self):
        return f" Brand:{self.brand} \n Model: {self.cc}"
c1 = Car('Ford',120)

print(c1)


#*************Object Methods

class Car:
    def __init__(mysillyobject,brand,cc):
        mysillyobject.brand = brand
        mysillyobject.cc = cc
    def __str__(abc):
        return f" Brand:{abc.brand} \n Model: {abc.cc}"
    def say_made_year(self):
        print('Hello this model was built in 2023')
c1 = Car('Ford',120)
print(c1)
c1.say_made_year()

"""The self parameter is the references to the instance of the class
it can have anu name instead self but the thing is it should be the first 
parameter of the object"""

# we can change the object properties
c1.cc= 400

print(c1)

# Delete object properties
# we can delete the objects properties with del keyword
del c1.cc
print('*********')
print(c1.brand)


# we can delete an object by del keyword as well
del c1
print('*********')
# print(c1.brand)


# class defination can not be empty but we in case if we need a class definition without
# a definition we can use a pass statement

class Person:
    pass

# Tomorrow Python inheritances