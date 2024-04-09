"""

Q. write a program to chcck wheather the given list is in arithmetric series or not

"""


def check_arithmetic(list_given):
    print(list_given)
    diff = list_given[1] - list_given[0]
    flag = True
    for i in range(0, len(list_given) - 1):
        if list_given[i] + diff != list_given[i + 1]:
            flag = False

    if flag:
        print(f'Given list {list_given} is in arithmetic series')
    else:
        print(f'Given list {list_given} is not in arithmetic progression')


list_1 = [1, 3, 5]
check_arithmetic(list_1)

list_1 = [1, 3, 6]
check_arithmetic(list_1)