#Bibek Shiwakoti
#Daily coding
"""Write a program to check wheather the given number is ugly number or not
Input : 12 Output : True Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
shows the first 10 ugly numbers. Note: 1 is typically treated as an ugly number"""


def find_ugly_number(num):
    copy_number = num
    factors = [2,3,5]
    for i in factors:
        while num % i == 0:
            num = num//i

    if num == 1:
        print(f'given  number {copy_number} is ugly number')
    else:
        print(f'given number {copy_number} is not ugly number')



find_ugly_number(1)
find_ugly_number(2)
find_ugly_number(4)
find_ugly_number(11)
find_ugly_number(12)


#control shift alt and L for formatting the code in pycharm