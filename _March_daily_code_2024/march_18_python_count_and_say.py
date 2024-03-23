"""Q2) The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
two 3's , three 2's, one 5, and one 1
23+32+15+11
"23321511"


Given a positive integer n, return the nth term of the count-and-say sequence.
"""


def countAndSay(n):
    if n == 1:
        return "1"

    prev = countAndSay(n - 1)
    result = ""
    count = 1

    for i in range(1, len(prev)):
        if prev[i] == prev[i - 1]:
            count += 1
        else:
            result += str(count) + prev[i - 1]
            count = 1

    # Append the count and the last digit of the previous sequence
    result += str(count) + prev[-1]

    return result


# Example usage:
n = 4
print(countAndSay(n))

# https://www.numerade.com/ask/question/texts-problem-2-the-count-and-say-sequence-is-a-sequence-of-digit-strings-defined-by-the-recursive-formula-countandsay1-1-countandsayn-is-the-way-you-would-say-the-digit-string-from-countand-06909/