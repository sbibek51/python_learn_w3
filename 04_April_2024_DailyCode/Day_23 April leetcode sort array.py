'''

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array_given = nums1 + nums2
        array_given.sort()
        print(array_given)
        if (len(array_given) % 2 != 0):
            return array_given[int(len(array_given) / 2)]
        else:
            a = array_given[(int((len(array_given)) / 2))]
            b = array_given[(int((len(array_given)) / 2) - 1)]
            return (a + b) / 2.0
obj = Solution()
first_array =[1,3]
second_array =[2,4]
print(obj.findMedianSortedArrays(first_array,second_array))