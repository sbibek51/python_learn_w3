"""

Q1 You are given a large integer represented as an integer array digits, where each digits[i] is
 the ith digit of the integer. The digits are ordered from most significant to least significant
 in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 Example 1:

Input: digits = [1,2,3]

Output: [1,2,4]

Explanation: The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.

Thus, the result should be [1,2,4].

"""

def increment_integer(digits):
    # Start from the least significant digit
    for i in range(len(digits) - 1, -1, -1):
        # Increment the current digit by 1
        digits[i] += 1
        # If there's no carry, return the digits
        if digits[i] < 10:
            return digits
        # If there's a carry, set the current digit to 0 and continue to the next digit
        else:
            digits[i] = 0
    # If we reach here, it means we have a carry after the loop
    # Insert 1 at the beginning of the digits list
    digits.insert(0, 1)
    return digits

# Test the function
digits = [1, 2, 3]
result = increment_integer(digits)
print(result)










# control shift alt and L to format the code in the pycharm