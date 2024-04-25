'''
Given an array of integers heights representing the histogram's bar height where the width of
each bar is 1, return the area of the largest rectangle in the histogram.

'''


class Solution(object):
    def largestRectangleArea(self, heights):
        if (len(heights) == 1):
            return heights[0]
        elif (len(heights) == 2):
            return max((2 * min(heights[0], heights[1]), heights[0], heights[1]))
        else:
            area = 0
            for i in range(0, len(heights)):
                for j in range(i + 1, len(heights)):
                    if heights[i] < heights[j]:

                        area = max(heights[i] * 2, heights[j], area)

                    else:

                        area = max(heights[j] * 2, heights[i], area)

            return area

obj = Solution()
heights = [2,1,5,6,2,3]
print(obj.largestRectangleArea(heights))

# 24/99 Test Case Passed have to work on logic and simplification