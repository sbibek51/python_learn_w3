#tuples
#tomorrow update tuple item
#till access tuples
my_tuple = ('apple','banana','cherry')
print(my_tuple)

#tuples allow double values
my_tuple2= ('apple','banana','cherry','orange','apple')

print(my_tuple2)

print('length of this tuple is {} '.format(len(my_tuple2)))


print('Type  is:',type(my_tuple2))


#tuple can contain different values:
my_new_tuple = ('abc', True, False, 123, 45.50)
print(my_new_tuple)
print(type(my_new_tuple))

nt = tuple(('abc', True, False, 123, 45.50))
print('type of nt is:')
print(type(nt))


print(nt[0])
print('last item of nt tuple is:',nt[-1])

print(nt[2:4])

print(nt[:4])

print('[-4,-1] prints -4 element(included but last index -1 is excluded)')
print(nt[-4:-1])


if 1234 in nt:
    print('Yes 123 exists in nt tuple')
else:
    print('124 does not exists in tuple nt')


