"""
Write a function to find the longest common prefix string amongst an array of strings, use Input
method to test it.

Also you code should return the length of the longest common prefix string amongst an array of
strings

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["Flower","flow","flight"]

Output: "fl", 2

This should work irrespective of upper or lower case!

"""


def find_long_prefix(given_list):
    if not given_list:
        return ''  # return none if there is no string in  list

    given_list.sort()
    print(given_list)

    prefix = given_list[0]
    for i in range(1, len(given_list)):
        for j in range(len(prefix)):
            if prefix[j] != given_list[i][j]:
                prefix = prefix[:j]  # store the longest matching string
                break

    return prefix, len(prefix)


my_list = []
while True:
    input_1 = input('Enter a string to add to the list(q to exit)')
    if input_1.lower() == 'q':
        break
    else:
        #         input_1.lower()
        my_list.append(input_1.lower())

# given_list = ["flower","flow","flight"]
# given_list = []

# find_long_prefix(given_list)
find_long_prefix(my_list)




