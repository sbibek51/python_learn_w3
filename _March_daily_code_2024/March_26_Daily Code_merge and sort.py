#Bibek Shiwakoti
import datetime
print('Today date and time is:',datetime.datetime.now().strftime(("%Y-%m-%d %H:%M")))

"""
Q1.
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 

and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside 
the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote
 the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
 nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

Output: [1,2,2,3,5,6]

Explanation: The arrays we are merging are [1,2,3] and [2,5,6].

The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.



"""

def merge_and_sort(nums1, m, nums2, n):
    # Pointer for the end of merged nums1
    index1 = m - 1
    # Pointer for the end of nums2
    index2 = n - 1
    # Pointer for the end of merged nums1 (including space for nums2)
    merged_index = m + n - 1

    # Loop until all elements of nums2 are merged
    while index2 >= 0:
        # Check if all elements of nums1 are merged or nums2 has larger element
        if index1 >= 0 and nums1[index1] > nums2[index2]:
            # Assign the larger element from nums1
            nums1[merged_index] = nums1[index1]
            index1 -= 1
        else:
            # Assign the next element from nums2
            nums1[merged_index] = nums2[index2]
            index2 -= 1
        # Move the pointer for merged nums1 to the left
        merged_index -= 1

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge_and_sort(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]


