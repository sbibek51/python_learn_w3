#sets in python
my_set = {'apple','banana','cherry'}
print(my_set)
print(type(my_set))
if 'apple' in my_set:
    print('Yes apple is in set')
#sets are unchangable ,unordered and unindexed
#you can not change a set elements but you can delete or add set elements
# once a set is created you can not change the items but you can add or remove the item
#duplicates is not allowed in set
#The value True and 1 is considered as same in set and considered as a duplicate
set_1 = {'apple','banana','cherry','apple'}
print(set_1)
#found that duplicates values are discarded and considered as same even if we entered the multiple
#compiler does not give an error
set_2 = {'Bibek',True,1,False,0}
print(set_2)
print(len(set_2))


set_3 ={1,7,5,3,9}
print(set_3)


# A set can contain different data types

set_4 = {'Hello',1,3.0,False,1,'apple'}
print(set_4)
