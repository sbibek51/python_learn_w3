#Bibek Shiwakoti
#Feb 16 2024
#Daily python code

# today we are going to learn about the class polymorphism
"""Polymorphism is often used withe the class methods
where we can have multiple class withe the same method name
"""

# for example class car , boat and plane they all have the method called move

class Car:
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model

    def move(self):
        print('Drive')


class Boat:
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model

    def move(self):
        print('Sail')

class Plane:
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model

    def move(self):
        print('Fly')


car1 =Car('Ford','F2.23')
boat1 =Boat('Ibiz',4)
plane1 =Plane("Boeing",'FZ')

for x in (car1,boat1,plane1):
    x.move()




#tomoorrw: Inheritance Class Polymorphism