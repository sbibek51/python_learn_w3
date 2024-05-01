# Bibek Shiwakoti
# Daily coding
# Q. Write a program to find a missing number from a list
# eg. [1,2,3,4,6,7,8] output 5


given_list =[1,2,3,4,6,7,8]
missing_list=[]
for i in range (len(given_list)-1):
    if given_list[i]+1 != given_list[i+1]:
        missing_list.append(given_list[i]+1)

print(missing_list)




# control +shift + alt + l for the format code in pycharm