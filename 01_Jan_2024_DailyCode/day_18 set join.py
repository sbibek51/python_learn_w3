#here today we are gonna join the sets
set1 = {'a','b','c','d'}
set2 = {'1','2','3','4'}
print(set1)
print(set2)
set3 = set1.union(set2)
print(set3)

#or we can use update method as well where
#update method willl isnert all the elements from second set to first one
#both update and union discard the duplicate item
set4={'apple'}
set4.update(set2)
print(set4)


x= {'apple','banana','chery','pomogrenate'}
y= {'mac','windows','microsoft','apple'}
print(x)
print(y)
x.intersection_update(y)
print(x)
print(y)


x= {'apple','banana','chery','pomogrenate'}
y= {'mac','windows','microsoft','apple'}
x.symmetric_difference_update(y)
print(x)
z= x.intersection(y)
print(z)

#symmetric difference gives the elements of both sets that are not common


x= {'apple','banana','chery','pomogrenate'}
y= {'mac','windows','microsoft','apple',0,True}
x.symmetric_difference_update(y)
print(x)

x.add('Toronto')

print(x)
z1 = x.copy()

x.clear()
print(x)
z1.clear()
print(z1)


