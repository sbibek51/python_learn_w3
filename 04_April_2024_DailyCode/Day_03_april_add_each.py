"""

Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
Input : 48
Output : 3
For example given number is 59, the result will be 5.
Step 1: 5 + 9 = 14
Step 1: 1 + 4 = 5

"""


def add_number(number):
    #     print('given number is:',number)

    while number >= 10:
        str_num = str(number)
        sum_1 = 0
        for digit in str_num:
            sum_1 = sum_1 + int(digit)
        number = sum_1

    return number


# print('sum of each digit till less than 10 is:',add_number(1))
# print('sum of each digit till less than 10 is:',add_number(19))
# print('sum of each digit till less than 10 is:',add_number(99))


while True:
    given_number = input('Enter a digit or \'e\' to exit :')
    if (given_number.lower() == 'e'):
        break

    else:
        given_number = int(given_number)
        print(f'Given number is : {given_number} and sum of each digit till less then 10 is:', add_number(given_number))
