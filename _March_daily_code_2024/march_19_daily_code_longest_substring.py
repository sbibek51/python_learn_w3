"""
Given a string s, return the length of the longest substring without repeating
characters. Additionally, return that substring and the number of times it repeats
in your main string. Use an input method to test your code! Example 1:
Input: s = "abcabcbb", Output: 3, abc, 2.
Explanation: The answer is "abc", with the length of 3, and it repeats 2 times.
Example 2: Input: s = "bbbbb", Output: 1, b, 4.
Explanation: The answer is "b", with the length of 1, and it repeats 4 times.

"""


def longest_substring(s):
    max_length = 0
    max_substring = ""
    max_repeats = 0
    char_index_map = {}

    start_index = 0

    for index, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start_index:
            start_index = char_index_map[char] + 1

        substring_length = index - start_index + 1

        if substring_length > max_length:
            max_length = substring_length
            max_substring = s[start_index:index + 1]

        char_index_map[char] = index

        if s[start_index:index + 1] == max_substring:
            if start_index == index - max_length + 1:
                max_repeats += 1

    return max_length, max_substring, max_repeats


# Take user input
s = input("Enter a string: ")

# Call the function with user input
length, substring, repeats = longest_substring(s)

# Print the result
print("Output:", length, ",", substring, ",", repeats)
