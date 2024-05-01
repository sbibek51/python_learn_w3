#update tuple item

#tomorrow unpack tuple item

#we can not change the tuple
#it is unchangable that is it is immutable
#but there are ways that we can work by converting into a list
thistuple = ('apple','banana','cherry')
print(thistuple)
y= list(thistuple)
y.remove(('apple'))
thistuple=tuple(y)
print(thistuple)

del thistuple
print('tuple deleted')
#print(thistuple)