"""
Problem: Happy Number

Approach:
Use Floyd’s Cycle Detection (Tortoise and Hare).
Define a function to compute the sum of squares of digits.
Use two pointers: slow moves one step, fast moves two steps.
If fast reaches 1, the number is happy.
If slow and fast meet, a cycle exists → not a happy number.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(x):
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total

        slow = n
        fast = getNext(n)

        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1
