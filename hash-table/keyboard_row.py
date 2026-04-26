"""
Problem: Keyboard Row

Approach:
Create sets for each keyboard row and convert each word to lowercase.
Check if all characters of the word belong to only one keyboard row
using set subset comparison. If yes, add the word to the result.

Time Complexity: O(n * k)
Space Complexity: O(1)
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            w = set(word.lower())

            if w <= row1 or w <= row2 or w <= row3:
                result.append(word)

        return result
