#Bibek Shiwakoti


## 2-Write a Python program to find the single element appears once in a list where every element appears multiple times except for one.
# Input : [1, 1, 1, 2, 2, 2, 3]
# Output : 3


list_1 = [1,1,1,2,2,2,3,4]
d={}
print(list_1)
# print(d)
for i in list_1:
    d[i]=d.get(i,0)+1
#     print(d)
single_count =  [key for key,value in  d.items() if value ==1]
print('value appears once is:',single_count)




# Control shift alt and L to format the code in pycharm environment