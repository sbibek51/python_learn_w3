#Bibek Shiwakoti
"""
 Write a Python program to find a missing number from a list. Input : [1,2,3,4,6,7,8] Output : 5
"""


def find_missing_number(my_list):
    my_list.sort()
    missing_list = []
    print('given list is:', my_list)
    for i in range(my_list[0], my_list[len(my_list) - 1]):
        if i not in my_list:
            missing_list.append(i)
    return missing_list


my_list = [1, 2, 3, 4, 6, 7, 8]
find_missing_number(my_list)

# control shifr alt and L to format a code in the pycharm