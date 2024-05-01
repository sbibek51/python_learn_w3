#python sets
my_set = {'apple','mango','pomergrenate',True,0,False}
print(my_set)
print(type(my_set))
a= ['apple','banana','cherry']
print(a)
print(type(a))
b=set(a)
print(b)
print(type(b))
newset= (('a','b','c'))
print(newset)

#access set items
print(newset)
for i in newset:
    print(i)

# checck if a appers in a set
if 'd' in newset:
    print('yes \'d\' is in the newset')
else:
    print('there is no \'d\' in newset ')


# change items
#once you create a set you can not change the items
#but you can add or delete an item