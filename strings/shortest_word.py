"""
Problem: Shortest Completing Word

Approach:
Count the frequency of alphabetic characters in the license plate.
Sort the words by length and check each word to see if it contains
all required characters with sufficient frequency.
Return the first valid word.

Time Complexity: O(n * k)
Space Complexity: O(1)
"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())

        for word in sorted(words, key=len):
            count = Counter(word.lower())
            valid = True

            for ch in need:
                if count[ch] < need[ch]:
                    valid = False
                    break

            if valid:
                return word
