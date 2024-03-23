#Bibek Shiwakoti
# Daily Code


"""Write a program to check wheather the given number is ugly number or not
Input : 12 Output : True Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
shows the first 10 ugly numbers. Note: 1 is typically treated as an ugly number"""


def ugly_number_checker(num):
    allowed_factors = [2,3,5]

    for i in allowed_factors:
        while num % i ==0:
            num = num//i

    if num == 1: # if dividing continuously by factors leaves 1 remainder
        return True
    else:
        return False



print(ugly_number_checker(1))
print(ugly_number_checker(2))
print(ugly_number_checker(4))
print(ugly_number_checker(7))

given_number = int(input('enter integer number to check if it is ugly number or not: '))
if ugly_number_checker(given_number):
    print(f' Given number {given_number} is Ugly number')
else :
    print(' Given number {} is NOT Ugly number'.format(given_number))


# control shift alt and L for code formatting in the pycharm