#Bibek Shiwakoti



"""
Question:
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
 then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible,
 the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]



"""


"""
Approach
We can follow the below steps -

Scan the array from right to left until an element is found which is smaller than the index at its right. Mark the index of such element as index.
Again scan the array from right to left until an element is found which is greater than the element found in the above step. Mark the index of such elements as j.
Swap the two elements at indices index and j.
Now, reverse the array from index index until the end of the array.
Let’s understand this with an example -

nums = [4,5,3,2,1]

Step 1: scan from right to left and stop at 4 because it less than 5. Here, index = 0
Step 2: Again scan from right to left and stop at 5 because it is greater than 4. Here, j = 1
Step 3: Swap the elements at index and j. The array will become [5,4,3,2,1].
Step 4: Reverse the array after index. The array will become [5,1,2,3,4]

"""


def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def nextPermutation(nums):
    # Length of the array
    n = len(nums)
    # Index of the first element that is smaller than
    # the element to its right.
    index = -1
    # Loop from right to left
    for i in range(n - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            index = i - 1
            break
    # Base condition
    if index == -1:
        reverse(nums, 0, n - 1)
        return
    j = n - 1
    # Again swap from right to left to find first element
    # that is greater than the above find element
    for i in range(n - 1, index, -1):
        if nums[i] > nums[index]:
            j = i
            break
    # Swap the elements
    nums[index], nums[j] = nums[j], nums[index]
    # Reverse the elements from index + 1 to the nums.length
    reverse(nums, index + 1, n - 1)

    return nums




print(nextPermutation([1,2,3]))


# Control shift alt and L to format a code in pycharm