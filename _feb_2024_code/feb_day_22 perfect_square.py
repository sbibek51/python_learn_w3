# Bibek Shiwakoti
# Daily coding

# Q. write a program to check if the given number is perfect square or not.

def find_perfect_square(num):
    if num < 0:
        print('given number is a negative number')
    else:
        flag = False
        for i in range(num):
            if i * i == num:
                print('{} is a perfect square of {}'.format(num, i))
                flag = True
                break

        if flag == False:
            print('{} is not a perfect square'.format(num))


while True:
    num = input('Enter number to check if it is perfect square (q for exit):')
    if (num.lower() == 'q'):
        break
    else:
        num = int(num)
        find_perfect_square(num)

# Control shift alt and L for the format code in pycharm
