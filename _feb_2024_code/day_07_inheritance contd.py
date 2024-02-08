#Bibek Shiwakoti
# inheritance continue

# add the init function to the child class
"""so far we have created the child class which inherits the parent class
now we want to add the init function to the child class"""
class Person:
    def __init__(self,first_name,last_name):
        self.first_name =first_name
        self.last_name=last_name

    def show_detail(self):
        print('first name is: {} and last name is :{}'.format(self.first_name,self.last_name))


p1=Person('Bibek','Shiwakoti')
p1.show_detail()

"""when we add the init function to the child class it overrites the main init
from the parent class
to keep the inheritance of the parent we need to add it as follows """
#now define a class student which interits the class person
class Student(Person):
    def __int__(self,fname,lname):
        self.full_name = fname+lname
        super().__init__(first_name,last_name)
#now student has all the properties as of the person
s1 = Student('Mark','Zuckerberg')
s1.show_detail()

"""we can also use the super keyword which will inherit all the properties from the 
parent element"""


#tomorrow super_function() and add methods and properties to the child class