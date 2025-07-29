"""
LeetCode Problem: 509. Fibonacci Number
URL             : https://leetcode.com/problems/fibonacci-number/

Approach: Recursive (Naive)

Description:
    The Fibonacci numbers, commonly denoted F(n), form a sequence such that:
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2) for n > 1
    Given an integer n, return F(n).

Recursive Logic:
    - If n is 0 or 1, return n (base case).
    - Otherwise, compute fib(n - 1) + fib(n - 2) recursively.

Time Complexity : O(2^n)  — exponential due to overlapping subproblems
Space Complexity: O(n)    — recursion call stack
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

# Example usage
n = 6
sol = Solution()
print(sol.fib(n))


# ------------------------------ Optimization Approach ------------------------------ #


"""
Approach: Recursive with Memoization

Description:
    Optimized version of the recursive Fibonacci algorithm using memoization.
    Stores the result of each subproblem to avoid redundant calculations.

Memoization Logic:
    - If n is 0 or 1, return n (base case).
    - If n not in memo, compute and store the result.
    - Return the stored result.

Time Complexity : O(n)  — each subproblem is solved once
Space Complexity: O(n)  — for memo dictionary and call stack
"""

class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if n not in self.memo:
            self.memo[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.memo[n]