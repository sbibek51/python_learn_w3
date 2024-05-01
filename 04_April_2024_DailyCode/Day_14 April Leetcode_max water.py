'''

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
'''


class Solution(object):
    def maxArea(self, height):
        water = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                if height[i]>height[j]:
                  if water<height[j]*(j-i):
                      water = height[j]*(j-i)
                else:
                 if water<height[i]*(j-i):
                      water = height[i]*(j-i)
        return water

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))


'''This algorithm is working but its time complexity is O(n**2) because it is using the 
two for loops we can look for optimized way with the O(n)'''