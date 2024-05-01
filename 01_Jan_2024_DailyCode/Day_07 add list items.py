# add list items

#Tomorrow list comrehension



for i in 'Hello World':
    print(i)
    print('\n')

this_list =['Apple', 'Cherry', 'banana']
print(this_list)
this_list.append('Strawberry')
print(this_list)



print('List before insert is:')
print(this_list)

this_list.insert(1,'Watermelon')

print('List after insert is:')
print(this_list)

list_2 =['Letuce', 'Spinach']

this_list.extend(list_2)

print(this_list)


this_tuple = ('Jackfruit', 'Pomegranate', 'Grapes')

this_list.extend(this_tuple)
print(this_list)


this_list.remove('Letuce')
print(this_list)

this_list.remove('Jackfruit')
print(this_list)

print('List before pop is:')
print(this_list)
this_list.pop()

print('List after pop is:')
print(this_list)

this_list.pop(1)
print(this_list)

del this_list[0]
print(this_list)

del this_list[1]
print(this_list)

print('List before clear is :')
print(this_list)


for i in range(len(this_list)):
    print(this_list[i])


# this_list.clear()
# print('Now the list is cleared')
# print(this_list)


print('now displaying the list using while loop:')

i = 0
while i < len(this_list):
    print(this_list[i])
    i += 1

print('Now printing the list using string comparison:')
[print(x) for x in this_list]
