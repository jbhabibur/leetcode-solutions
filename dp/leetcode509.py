"""
LeetCode Problem: 509. Fibonacci Number
URL             : https://leetcode.com/problems/fibonacci-number/

Description (using recursion):
    The Fibonacci numbers, commonly denoted F(n), form a sequence such that:
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2) for n > 1
    Given n, calculate F(n).

Recursive Approach:
    1. If n is 0 or 1, return n directly (base case).
    2. Otherwise, return fib(n - 1) + fib(n - 2) using recursion.

Why this works:
    - The Fibonacci sequence is defined recursively.
    - This method directly follows the definition of Fibonacci numbers.

Time Complexity : O(2^n)  — exponential due to repeated calls
Space Complexity: O(n)    — call stack size in worst case
"""

class Solution:
    def fib(self, n: int) -> int:
        if 1 <= n:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

# Example usage
n = 6
sol = Solution()
print(sol.fib(n))
