"""Write and test a fucntion for the following. Make sure to use input method to test it!

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array 'nums' and an integer 'k', return the 'k-th' smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums. length.

Example 1:

Input: nums = [1,3,1], k = 1

Output: 0

Explanation: Here are all the pairs:

(1,3) -> 2

(1,1) -> 0

(3,1) -> 2

Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:

Input: nums = [1,1,1], k = 2

Output: 0

Example 3:

Input: nums = [1,6,1], k = 3

Output: 5"""


def absolute_diff_finder(my_list, k):
    print('\nGiven list is {}'.format(my_list))
    print('Given value of k is {}:'.format(k))

    # Find the combination of all the list items
    distance_pair = []
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            diff = abs(my_list[i] - my_list[j])  # Take absolute difference
            distance_pair.append(diff)

    distance_pair.sort()

    # Calculate and return the kth smallest distance
    return distance_pair[k - 1]


# Test the function
list_a = [1, 3, 1]
k = 1
print("Output:", absolute_diff_finder(list_a, k))

list_a = [1, 1, 1]
k = 2
print("Output:", absolute_diff_finder(list_a, k))

list_a = [1, 6, 1]
k = 3
print("Output:", absolute_diff_finder(list_a, k))



# might need some correction