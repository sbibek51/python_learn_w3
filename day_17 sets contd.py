# sets items can not be changed but you can add or delete an item
this_set = {'apple','banana','cherry'}
print(this_set)
this_set.add('Mango')
print(this_set)

#add elements from one set to another
tree_fruits ={'jackfruit','peaches'}
this_set.update(tree_fruits)
print(this_set)
# also we can add an elements from list to set
list_1 = ['grapes','pomogrenate']
this_set.update(list_1)
print(this_set)

#we can remove an items as well
this_set.remove('grapes')
print(this_set)

this_set.remove('jackfruit')
print(this_set)

this_set.discard('mango')
print(this_set)

#if element does not exists in set discard element DOES NOT throw an exception
this_set.discard('cherries')

#remove a random item by pop method
a = this_set.pop()
print(a, 'is pop randomly form set')
print(this_set)
b = this_set.pop()
print(b, 'is pop randomly form set')
print(this_set)

#clear method clears the set
this_set.clear()
print(this_set)


#del delets the set
del this_set



#loop sets
new_set = {'apple','banana','mango','cherry'}
print(new_set)

for i in new_set:
    print(i)


#JOin two sets
#we can either use insert metnod to add all items from one set to another set union method for union
