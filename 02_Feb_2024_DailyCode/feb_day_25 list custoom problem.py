# Bibek Shiwakoti
# Daily Coding
# Q. Write a program that particular number does not occur twice

my_list = [1, 1, 2, 2, 3]
my_dictionary = {}
# print(type(my_dictionary))
for i in my_list:
    my_dictionary[i] = my_dictionary.get(i, 0) + 1

single_count = [i for key, value in my_dictionary.items() if value == 1]

print(my_dictionary)
print(single_count)

# control shift alt and L to format the code int he pycharm
