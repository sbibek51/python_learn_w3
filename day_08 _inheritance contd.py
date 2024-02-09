#Bibek Shiwakoti
"""Today we are going to practice the inheritance concepts we learned from the
last class
we are going to use the super kayword also"""


class Person():
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname =lname

    def show_name(self):
        print('First Name: {} and Last Name:{}'.format(self.firstname,self.lastname))


p1= Person('Bibek', 'Shiwakoti')
p1.show_name()


class Student(Person):
    def __init__(self,fname,lname,roll):
        self.roll_number = roll
        super().__init__(fname,lname)

    def show_roll(self):
        print('Roll number of {} {} is {} '.format(self.firstname,self.lastname,self.roll_number))


s1 = Student('Bibek','Shiwakoti',3)
s1.show_name()
s1.show_roll()


"""Tomorrow we will see adding the properties and methods to the child class as well"""
#Happy Coding

