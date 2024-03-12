#Bibek Shiwakoti

"""Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 Example 1:

Input: n = 19

Output: true

Explanation:

12 + 92 = 82

82 + 22 = 68

62 + 82 = 100

12 + 02 + 02 = 1

Example 2:

Input: n = 2

Output: false"""

"""Algorithm:
Create a set to store the numbers seen during the process.
While n is not equal to 1:
Convert n to a string and iterate over its digits.
For each digit, square it and add it to the sum.
Update n with the sum.
If n is already in the set, return False (indicating a cycle).
Otherwise, add n to the set.
If the loop terminates (i.e., n becomes 1), return True."""
def is_happy(n):
    seen = set()  # Set to store seen numbers
    while n != 1:
        # Convert n to string, iterate over digits, square them, and sum
        n = sum(int(digit)**2 for digit in str(n))
        # If n is already in seen, it means there's a cycle
        if n in seen:
            return False
        seen.add(n)  # Add n to the set
    return True  # n becomes 1, so it's a happy number

# Test cases
print(is_happy(19))  # Output: True
print(is_happy(2))   # Output: False



# control shift alt and L to format a code in pycharm IDE