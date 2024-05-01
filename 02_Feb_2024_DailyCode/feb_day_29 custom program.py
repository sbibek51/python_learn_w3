#Bibek shiwakoti
# Q. find all the digits in the given string

digits=[]
def find_digits(given_str):
    for i in given_str:
        if i.isdigit():
            digits.append(i)

given_str= input('enter a string having digits in it:')
find_digits(given_str)
print('digits in given string {} are {}'.format(given_str,digits) )


# control shift alt and L for formatting the code in pycharm