#Bibek Shiwakoti
# Daily Code



def pallidrome_finder(a):
    a=str(a)
    rev_a =a[::-1]
    print('given number is',a )
    print('reverse of given number is',rev_a)
    if (int(a)==int(rev_a)):
        print('given number is pallindrome as {} and {} are same'.format(a,rev_a))
    else:
        print('given number {} is not pallindrome:'.format(a))

pallidrome_finder(14)
pallidrome_finder(44)
pallidrome_finder(54)





# Control shift alt and L for the format code in pycharm
