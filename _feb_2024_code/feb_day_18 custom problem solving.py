# Bibek Shiwakoti
# Python daily coding


# find the numbers in list which occurs only one times where other occurs multiple times

my_list = [1, 1, 2, 2, 3, 3, 4]

my_dictionary = {}

for i in my_list:
    my_dictionary[i] = (my_dictionary.get(i, 0) + 1)

print(my_dictionary)

single_count = [i for key, value in my_dictionary.items() if value == 1]

print(single_count)

# Control shift alt and L for the format code in pycharm
