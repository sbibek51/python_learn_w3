"""
Q2. Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]

Output: 3
"""

my_list = []
my_dictionary = {}
while True:
    a = input('Enter an integer number to add to the list or (e to exit): ')
    if a.lower() == 'e':
        break
    else:
        my_list.append(a)

print('Given list is:', my_list)

# Counting the occurrences of each element in the list
for i in my_list:
    my_dictionary[i] = my_dictionary.get(i, 0) + 1


threshold = len(my_list) / 2

# Finding the elements that occur more than n/2 times
majority_elements = [key for key, value in my_dictionary.items() if value > threshold]

print('Elements that occur more than n/2 times:', majority_elements)
