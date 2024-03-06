# Bibek Shiwakoti
# Python Daily Coding
"""
Symbol Value

I 1

V 5

X 10

L 50

C 100

D 500

M 1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. X can be placed before L (50) and C (100) to make 40 and 90. C can be placed before D (500) and M (1000) to make 400 and 900. Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"

Output: 3

Explanation: III = 3.

Input: s = "LVIII"

Output: 58

Explanation: L = 50, V= 5, III = 3.
"""


def roman_to_numeric(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    final_value = 0
    for i in reversed(roman):
        value = roman_numerals[i]
        if value < prev_value:
            final_value -= value
        else:
            final_value += value
        prev_value = value
    return final_value


print(roman_to_numeric('III'))
print(roman_to_numeric('IV'))
print(roman_to_numeric('VII'))
print(roman_to_numeric('LVIII'))
# control shift alt and L for the code formatting
