#python inheritance
"""Inheritance allows us to inherit all the methods and  properties from the
 another classes

 base class is the parent class
 child class is the inherited class
 """


class Person:
    def __init__(self,first_name,last_name):
        self.first_name =first_name
        self.last_name=last_name

    def show_detail(self):
        print('first name is: {} and last name is :{}'.format(self.first_name,self.last_name))


p1=Person('Bibek','Shiwakoti')
p1.show_detail()


#now define a class student which interits the class person
class Student(Person):
    pass

#now student has all the properties as of the person
s1 = Student('Mark','Zuckerberg')
s1.show_detail()