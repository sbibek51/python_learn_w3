#Bibek Shiwakoti
# Day 10 of feb on python learning
class Person():
    def __init__(self,fname,lname):
        self.fname =fname
        self.lname =lname

    def show_person(self):
        print('Hello {} {}'.format(self.fname,self.lname))


class Student(Person):
    def __init__(self,fname,lname,roll):
        super().__init__(fname,lname)
        self.roll =roll
        self.graduation_year=2025

    def show_student(self):
        print('Hello {} {} Your roll number is {} and graduation year is {}'.format(self.fname,self.lname,self.roll,self.graduation_year))




p1 = Person('Bibek', 'Shiwakoti')
p1.show_person()


s1 = Student("Bibek",'Shiwakoti',898100)
s1.show_student()