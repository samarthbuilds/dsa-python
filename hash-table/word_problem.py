"""
Problem: Word Pattern

Approach:
Split the string into words and compare its length with the pattern.
Use two hashmaps to maintain a bijection between characters and words.
If a mismatch occurs in either mapping, return False.
If all mappings are consistent, return True.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w

            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c

        return True
