# write a program to reverse a string eg, hello world to world hello
while True:
    given_string = input('Enter a sentence or q to exit:')
    if given_string.lower()=='q':
        break
    else:
        my_words = given_string.split()
        rev = my_words[::-1]
        final_string =' '.join(rev)

    print('given sentence is:',given_string)
    print('reverse is:',final_string)


# Control shift alt and L for the format code in pycharm
