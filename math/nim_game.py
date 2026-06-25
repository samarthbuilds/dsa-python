"""
Problem: Nim Game

Approach:
In the Nim Game, every multiple of 4 is a losing position
if both players play optimally. Therefore, the first player
can win unless the number of stones is divisible by 4.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
