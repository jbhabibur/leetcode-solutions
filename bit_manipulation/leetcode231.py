"""
LeetCode Problem: 231. Power of Two
URL             : https://leetcode.com/problems/power-of-two/

Problem:
    Given an integer `n`, return true if it is a power of two. Otherwise, return false.

    An integer `n` is a power of two if there exists an integer `x` such that:
        n == 2^x

Constraints:
    - -2^31 <= n <= 2^31 - 1

Follow-up:
    Could you solve it without using loops or recursion?
"""

# ------------------------------ Division Approach ------------------------------ #
"""
Approach: Repeated Division by 2

Explanation:
    - A number is a power of two if it can be continuously divided by 2 until it becomes 1.
    - If at any point it cannot be evenly divided by 2, it's not a power of two.
    - Also, all powers of 2 are positive integers, so return False if n <= 0.

Time Complexity : O(log n) — each division by 2 reduces the number size by half
Space Complexity: O(1)     — no extra space used
"""

from typing import List

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A number is a power of 2 if and only if n > 0
        if n <= 0:
            return False

        # While n is divisible by 2, keep dividing it
        # Remainder == 0 means n may be a power of 2
        while n % 2 == 0:
            n //= 2

        # Return True (n == 1) or False (n != 1)
        return n == 1

# Example usage
n = 1
sol = Solution()
print(sol.isPowerOfTwo(n))  # Output: True
