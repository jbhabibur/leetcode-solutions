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
Approach: Recursive with Memoization (Top-Down DP)

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


# ------------------------------ Optimization Approach ------------------------------ #

"""
Approach: Dynamic Programming - Tabulation (Bottom-Up)

Description:
    Iterative bottom-up approach to compute the nth Fibonacci number.
    Builds up the solution from the base cases by storing intermediate results in a dp array.

Tabulation Logic:
    - Initialize dp[0] = 0 and dp[1] = 1 (base cases).
    - Iteratively compute dp[i] = dp[i-1] + dp[i-2] for i from 2 to n.
    - Return dp[n] as the final result.

Time Complexity : O(n)  — each subproblem is solved once in a loop
Space Complexity: O(n)  — for the dp array
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# ------------------------------ Optimization Approach ------------------------------ #


"""
Approach: Space Optimized Bottom-Up DP

Description:
    Iterative bottom-up approach to compute the nth Fibonacci number.
    Instead of using a dp array, it keeps track of only the last two computed Fibonacci numbers,
    thereby reducing space usage.

Logic:
    - Initialize two variables to represent dp[0] and dp[1].
    - Iteratively compute the current Fibonacci number as the sum of the previous two.
    - Update the two variables accordingly.
    - Return the last computed Fibonacci number as the final result.

Time Complexity : O(n)  — each Fibonacci number computed once
Space Complexity: O(1)  — constant space for a fixed number of variables
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev2 = 0
        prev1 = 1

        for i in range(2, n + 1):
            current = prev1 + prev2

            prev2 = prev1
            prev1 = current


        return current

