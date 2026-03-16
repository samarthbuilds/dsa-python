"""
Problem: Add Binary

Approach:
Start from the end of both binary strings and simulate binary addition.
Use a carry variable just like normal addition. At each step, add the
corresponding digits from both strings along with the carry. Store the
result bit and update the carry. Continue until both strings are fully
processed and no carry remains. Finally reverse the result.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(result[::-1])
