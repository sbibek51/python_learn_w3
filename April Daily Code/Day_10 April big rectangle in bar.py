"""

Given an array of integers heights representing the histogram's bar height where the width of each
 bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]

Output: 10

Explanation: The above is a histogram where width of each bar is 1. The largest rectangle is shown
 in the red area, which has an area = 10 units.

Use function and input method"""

"""logic here is to find the two consecutive numbers whose sum is largest
and then when two big numbers are found we need to find the rectangle area mean lowest number times two """


def find_area(heights):
    #     print(heights)
    sum_large = 0
    num1 = 0
    num2 = 0
    for i in range(len(heights) - 1):
        current_sum = heights[i] + heights[i + 1]
        if current_sum > sum_large:
            sum_large = current_sum
            num1 = heights[i]
            num2 = heights[i + 1]
    #     print(sum_large,num1,num2)
    if num1 > num2:
        return num2 * 2
    else:
        return num1 * 2


my_list = []
while True:
    input_1 = input('Enter a bar height to add to the list(q to exit)')
    if input_1.lower() == 'q':
        break
    else:
        input_1 = int(input_1)
        my_list.append(input_1)

print('given lengths of bars are:', my_list)
print(f'heighest area in bar is:{find_area(my_list)}')

# heights = [2,1,5,6,2,3]
# find_area(heights)
