#Day_08
#List_Comperhension

fruits = ['apple', 'cherry', 'banana', 'pineapple']
new_list = []


print(new_list)

for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)


new_list1 = [x for x in range(10) if x<=5]
print(new_list1)


print('new_list before insert is:')
print(new_list)

print('new list after insert is:')
new_list.insert(1,'jackfruit')
print(new_list)

new_list.sort()
print('newlist after sort is:')
print(new_list)



