"""
Problem: Ransom Note

Approach:
Use a hashmap to count the frequency of characters in the magazine.
Then iterate through the ransom note and check if each character
is available in the hashmap. Decrease the count as characters are used.
If any character is unavailable, return False.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False

            count[ch] -= 1

        return True
