#Lists
#tomorrow_ add list items
this_list = ['Apple','Ball','Cat','Dog']
print(type(this_list))
print(this_list)
print('Length of this list is:',len(this_list))
List_1 = ['Apple', 123,335.90, True, False,"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in List_1:
    print(i)
print(List_1[1])
print(List_1[2:5])

if 'cherry' in List_1:
    print('Yes \'cherry\' exists in this list')

List_1[0] = 'Mango'
print(List_1)
List_1[1:3] = ['Wamnut','Watermelon']
print(List_1)
List_1.insert(1,'Banana')
print(List_1)