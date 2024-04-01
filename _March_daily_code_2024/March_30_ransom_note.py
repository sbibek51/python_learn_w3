"""
Q2 Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
 using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 Example 1:

Input: ransomNote = "a", magazine = "b"

Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"

"""


def can_construct_ransom_note(ransomNote, magazine):
    # Initialize a dictionary to store the frequency of each character in the magazine
    char_freq = {}

    # Populate the char_freq dictionary with the frequency of each character in the magazine
    for char in magazine:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Check if the ransom note can be constructed using the magazine clippings
    for char in ransomNote:
        # If the character is not present in the magazine or its frequency is 0, return False
        if char not in char_freq or char_freq[char] == 0:
            return False
        # Decrement the frequency of the character in the magazine after using it in the ransom note
        char_freq[char] -= 1

    # If we reach here, it means all characters in the ransom note were found in the magazine
    return True


# Example usage:
ransomNote = "aa"
magazine = "aab"
print(can_construct_ransom_note(ransomNote, magazine))  # Output: True
