"""
LeetCode Problem: 70. Climbing Stairs
URL             : https://leetcode.com/problems/climbing-stairs/

Approach: Recursive (Naive)

Description:
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps.
    Return the number of distinct ways to climb to the top.

Recursive Logic:
    - If n == 0 → return 1 (1 valid way: do nothing)
    - If n <  0 → return 0 (invalid path)
    - Otherwise → climbStairs(n - 1) + climbStairs(n - 2)
      (try taking 1 or 2 steps and sum all valid paths)

Time Complexity : O(2^n)  — exponential due to repeated subproblems
Space Complexity: O(n)    — recursion call stack depth
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case 1:
        # If we've reached exactly 0 steps, there's 1 way (do nothing)
        if n == 0:
            return 1

        # Base case 2:
        # If we've gone below 0, it's an invalid path — no way to climb
        if n == -1:
            return 0

        # Recursive case:
        # Total ways to reach step n = ways from step (n-1) + step (n-2)
        # Since you can take either 1 or 2 steps at a time
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Example usage
n = 3
sol = Solution()
print(sol.climbStairs(n))


# ------------------------------ Optimization Approach ------------------------------ #


"""
Approach: Recursive with Memoization (Top-down DP)

Optimization (Memoization):
    - Store the result for each n in a dictionary (self.memo)
    - Avoid recomputing the same subproblem repeatedly
    - Greatly improves performance from exponential to linear time

Time Complexity : O(n)   — Each subproblem is solved once
Space Complexity: O(n)   — For memoization dictionary and recursion stack
"""

class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == -1:
            return 0

        if n not in self.memo:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memo[n]