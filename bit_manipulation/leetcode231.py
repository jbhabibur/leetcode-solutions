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


# ------------------------------ Bit Manipulation Approach ------------------------------ #
"""
Approach: Bitwise AND Trick

Explanation:
    - All powers of two in binary have exactly one bit set to 1.
        For example:
            1  = 0001
            2  = 0010
            4  = 0100
            8  = 1000
    - For any power of 2:
        n & (n - 1) == 0
        Why? Because:
            - n       : 00010000 (only one bit is 1)
            - n - 1   : 00001111 (all bits after that 1 become 1)
            - n & (n - 1) == 0
    - Also, make sure n > 0 to exclude 0 or negative numbers.

Time Complexity : O(1) — single operation
Space Complexity: O(1) — no extra space used
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A number is a power of 2 if and only if n > 0
        if n <= 0:
            return False

        # Bitwise trick: only powers of two satisfy this
        return n & (n - 1) == 0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A number is a power of 2 if and only if n > 0
        if n <= 0:
            return False

        return n & (n - 1) == 0