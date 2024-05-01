# Bibek Shiwakoti
"""Q. C: Write a Python program to find the single number i
in a list that doesn't occur twice. Input : [5, 3, 4, 3, 4] Output : 5 """


def duplicate_finder(my_list):
    my_set_1 = set(my_list)

    print('original list is:', my_list)
    print('created set is:', my_set_1)
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                # print('duplicate found')
                my_set_1.discard(my_list[i])
    print('value in list that does not occur twice is :', my_set_1)




given_list = [5, 3, 4, 3, 4]
duplicate_finder(given_list)


# Control Shif alt and L to format a code in pycharm ide
