"""Q2- Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1: Input: s = "aa", p = "a"

Output: false

Explanation: "a" does not match the entire string "aa".

Example 2: Input: s = "aa", p = "a*"

Output: true

Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
"""


def isMatch(s: str, p: str) -> bool:  # function return type is bool
    rows, columns = (len(s), len(p))
    # Base conditions
    if rows == 0 and columns == 0:
        return True
    if columns == 0:
        return False

    # DP array
    dp = [[False for j in range(columns + 1)] for i in range(rows + 1)]
    # Since empty string and empty pattern are a match
    dp[0][0] = True

    # Deals with patterns containing *
    for i in range(2, columns + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]

    # For remaining characters
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif j > 1 and p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
    return dp[rows][columns]


print(isMatch('aa', 'a.'))
print(isMatch('aa', 'a'))

# https://redquark.org/leetcode/0010-regular-expression-matching/