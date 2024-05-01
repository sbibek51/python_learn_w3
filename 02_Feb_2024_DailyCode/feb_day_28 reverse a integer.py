#Bibek Shiwakoti
#Daily Coding


# Q. write a programt to find a reverse of an integer


def find_reverse(num):
    num = str(num)
    num=num[::-1]
    return int(num)

num = input('enter a numver:')
print('reverse of {} is {}'.format(num,find_reverse(num)))



# control shift alt and L to format a code in the pycharm