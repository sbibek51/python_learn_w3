#Bibek Shiwakoti
"""You are given a large integer represented as an integer array digits, where each digits[i] is
 the ith digit of the integer. The digits are ordered from most significant to least significant
 in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""
def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

        if carry == 0:
            break

    if carry == 1:
        digits.insert(0, 1)

    return digits

# Example usage:
digits = [1, 2, 4]
print("Input:", digits)
print("Output:", plusOne(digits))



# control shift alt and l for formatting the code in the pycharm community ide