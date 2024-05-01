# Bibek Shiwakoti
# Daily Coding

# to check wheather the values in given lilst are in geometric progression or not
my_list = [5, 7, 9, 11]


def geometric_checker(list):
    r = list[1] / list[0]
    flag = True
    for i in range(len(list) - 1):
        if list[i + 1] / list[i] != r:
            flag = False

    if flag:
        print(f'given list {list} is in geometric progression')
    else:
        print(f'given list {list} is not in geometric progression')


geometric_checker(my_list)
mylist_2 = [1, 3, 5, 7, 9, 11]
mylist_3 = [1, 3, 9, 27, 81, 243]
geometric_checker(mylist_2)
geometric_checker(mylist_3)

# control shift alt and L for formatting the code in pycharm
