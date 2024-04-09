#Bibek Shiwakoti
"""Write a Python program to check if a number is a perfect square"""


def perfect_square_finder(num):
    flag = True
    if num < 0:
        print(f'given number {num} is a negative number')
        exit
    else:
        #         print('given number is:',num)
        for i in range(num):
            if i * i == num:
                print(f'Given number {num} is perfect square of {i}')
                flag = False
                break
        if flag:
            print(f'given number is {num} not a perfect square')


perfect_square_finder(-1)
perfect_square_finder(9)
perfect_square_finder(33)


# Control shift alt and L to format a code in pycharm