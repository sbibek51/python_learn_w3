#Bibek Shiwakoti
#Daily coding

"""Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not."""


def find_pallindrome(num):
    print('given number is:', num)
    str_num = str(num)
    rev_str = str_num[::-1]
    if rev_str == str_num:
        print(f'given number {num} is pallindrome.')
    else:
        print(f'given number {num} is NOT pallindrome.')


find_pallindrome(333)
find_pallindrome(334)


# control shift alt and L to format a code in pycharm IDE