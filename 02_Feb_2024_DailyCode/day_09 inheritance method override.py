#Bibek Shiwakoti
#DAy 09 of month febrauary

class Person:
    def __init__(self,fname,lname):
        self.fname =fname
        self .lname =lname
    def show_name(self):
        print('Hello {} {}'.format(self.fname,self.lname))



class Student(Person):
    def __init__(self,fname,lname,roll):
        super().__init__(fname,lname)
        self.roll_number=roll

    def show_student(self):
        print('Hello {} {} your roll number is {}'.format(self.fname,self.lname,self.roll_number))




p1 =Person('Bibek','Shiwakoti')
p1.show_name()

s1 =Student('Bibek','Shiwakoti',898100)
s1.show_name()
s1.show_student()