#Bibek Shiwakoti
print('Today date is: Feb 4th 2024')

class MyClass :
    x=5

print(type(MyClass()))
print(MyClass())


obj_1 = MyClass()
print(obj_1.x)

# *******************************************


# The __init__() function?
""" 
To understand the meaning of classes we have to understand the init function
all classes have a __init__() function which is always executed when the class is initiated


use __intit__() function to assign values to object properties , or other operations that are
necessary to do when the object is being created 
"""

#Example

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age =age
p1=Person('John',31)

print(p1.name)
print(p1.age)



class Mountain:
    def __init__(self,name,height):
        self.name =name
        self.height =height


mountain_1 = Mountain('Mt. Everest', 8848.20)
mountain_2 = Mountain('Mt. Gaurishankar', 7134)

print(mountain_1.name," : ", mountain_1.height)
print(mountain_2.name," : ",mountain_2.height)


#The init function is called everytime the class is being created


# tomorrow the __str__() function

