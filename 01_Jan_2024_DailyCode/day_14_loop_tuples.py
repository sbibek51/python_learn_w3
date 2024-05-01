#day_14
#loop tuples

# tomorrow jan 15 sets


this_tuple = ('apple','orange','cherry','pomogernate')
for x in range (len(this_tuple)):
    print(x,this_tuple[x])

#joun two tuples
tuple_1 = ('a','b','c','d')
tuple_2 = (1,2,3,4)
tuple_3 =tuple_2+tuple_1
print(tuple_3)

#multiply tuples
print(tuple_1*2)
my_tuple=(this_tuple*2)
print(my_tuple)
print(my_tuple.count('orange'))
print('index of orange in tuple is',this_tuple.index('orange'))