# Day 09
#from list copy

#tomorrow list methods


this_list = ['data science', 'visualization', 'NLP', 'advenced python', 'AIML lab']

for i in this_list:
    print(i)
    print('\n')

new_list= []
print(new_list)
new_list = this_list.copy()

print(new_list)

new_list2 = []
print(new_list2)
new_list2 = list(new_list)
print(new_list)

list_2 = [1,3,4,5,6]

list_3 =new_list + list_2

list_3.append('Lambton')

print(new_list2)
new_list2.append('Canada')
print(new_list2)
new_list2.sort()
print(new_list2)


list_4 =[7,8,9,10]

# for x in list_4:
#     list_2.append(x)
# print(list_2)


list_2.extend(list_4)
print(list_2)

