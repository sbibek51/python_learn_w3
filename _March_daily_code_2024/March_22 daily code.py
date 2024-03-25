#Bibek Shiwakoti

# Q B- Write a Python program to find a missing number from a list. Input : [1,2,3,4,6,7,8] Output : 5


def find_missing_number(my_list):
    first_num = my_list[0]
    last_num = my_list[len(my_list)-1]
    print(first_num)
    print(last_num)
    print(my_list)

    for i in range (first_num,last_num+1):
        if i not in my_list:
            print('number that is not in list:')
            print(i)



given_list = [1,2,3,4,6,7,8]
find_missing_number(given_list)


# Control shift alt and L for the formatting code in pycharm