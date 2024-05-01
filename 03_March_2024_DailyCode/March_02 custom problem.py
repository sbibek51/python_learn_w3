#Bibek Shiwakoti
#Daily python coding

"""Write a program to check wheather the given number is beautiful number or not
Input : 12 Output : True Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
shows the first 10 ugly numbers. Note: 1 is typically treated as an beautiful number"""


def beautiful_numbers(num):
    given_number = num
    factors = [2,3,5]
    for i in factors:
        while num % i ==0:
            num = num//i

    if num == 1:
        print(f'given number {given_number} is beautiful number ')
    else:
        print(f'given number {given_number} is not a beautiful number')


# beautiful_numbers(1)
# beautiful_numbers(2)
# beautiful_numbers(5)
# beautiful_numbers(11)
# beautiful_numbers(12)


while True:
    value = input('Enter a number to check if it is beautiful \'q\' to exit:')
    if value.lower()=='q':
        break
    else:
        value= int(value)
        beautiful_numbers(value)
# control shift alt and L for the formatting code in pycharm