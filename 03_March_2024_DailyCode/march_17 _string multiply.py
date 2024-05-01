"""Q1) Given two non - negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built - in BigInteger library or convert the inputs to integer directly.

Example
1:

Input: num1 = "2", num2 = "3"
output : "6"
"""


def multiply_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)

    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            mul = digit1 * digit2

            # Updating the result array considering current and previous digits
            pos1, pos2 = i + j, i + j + 1
            mul_sum = mul + result[pos2]

            result[pos1] += mul_sum // 10
            result[pos2] = mul_sum % 10

    # Converting result list to string
    result_str = ''.join(map(str, result))

    # Removing leading zeros
    return result_str.lstrip('0')


# Testing the function
num1 = "123"
num2 = "15"
print(multiply_strings(num1, num2))