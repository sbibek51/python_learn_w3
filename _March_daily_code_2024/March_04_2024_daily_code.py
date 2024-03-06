# Bibek Shiwakoti
# Daily Coding

# to check wheather the values in given lilst are in arithetic progression or not
my_list = [5, 7, 9, 11]


def arithmetic_checker(list):
    diff = list[1] - list[0]
    flag = 1
    for i in range(len(list) - 1):
        if list[i + 1] - list[i] != diff:
            flag = 0

    if flag == 0:
        print(f'given list {list} is not in arithmetic progression')
    else:
        print(f'given list {list} is in arighmetic progression')
    # print(diff)
    # print(list)


arithmetic_checker(my_list)
mylist_2 = [1, 3, 5, 7, 9, 11]
mylist_3 = [1, 3, 5, 7, 9, 12]
arithmetic_checker(mylist_2)
arithmetic_checker(mylist_3)

# control shift alt and L for formatting the code in pycharm
