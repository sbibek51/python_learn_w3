# Bibek Shiwakoti
# Day 14 of Feb Python basics


my_string = 'Bibek Shiwakoti'

my_it = iter(my_string)

print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
# print(next(my_it)) stop


# Control shift alt and L for the format code in pycharm
# creating a iteraror




class MyNumber:
   def __iter__(self):
      self.a =1
      return self

   def __next__(self):
      x=self.a
      self.a = self.a+1
      return x

obj1 = MyNumber()

myiter = iter(obj1)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



#stopping an iteration
class MyNumber:
   def __iter__(self):
      self.a =1
      return self

   def __next__(self):
     if self.a<= 20:
      x=self.a
      self.a = self.a+1
      return x
     else:
        raise StopIteration
obj1 = MyNumber()

myiter = iter(obj1)



for x in myiter:
   print(x)


# next python polymorphism

