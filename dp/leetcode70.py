"""
LeetCode Problem: 70. Climbing Stairs
URL             : https://leetcode.com/problems/climbing-stairs/

There is a staircase with `n` steps.
You can either take 1 step or 2 steps at a time.
Determine how many distinct ways you can reach the top.
"""

# ------------------------------ 1. Recursive (Naive) ------------------------------ #
"""
Approach: Recursive (Naive)

Explanation:
    At each step, you have two choices:
    - Take 1 step → solve for (n - 1)
    - Take 2 steps → solve for (n - 2)

    This forms the recurrence:
        f(n) = f(n - 1) + f(n - 2)

Base Cases:
    - If n == 0: 1 way (do nothing)
    - If n < 0 : 0 ways (invalid)

Time Complexity : O(2^n) — exponential due to overlapping subproblems
Space Complexity: O(n)   — maximum recursion depth
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
Approach: Recursive with Memoization (Top-down Dynamic Programming)

Optimization:
    - Use a dictionary to cache results for each subproblem
    - Avoid redundant computations
    - Converts exponential to linear time

Time Complexity : O(n) — each unique subproblem solved once
Space Complexity: O(n) — recursion stack + memoization dictionary
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

# ------------------------------ Optimization Approach ------------------------------ #
"""
Approach: Bottom-Up Dynamic Programming (Tabulation)

Explanation:
    - Initialize dp[1] = 1, dp[2] = 2 (base cases)
    - Iteratively build up dp[i] = dp[i-1] + dp[i-2]
    - This avoids recursion entirely and runs in linear time

Time Complexity : O(n)
Space Complexity: O(n)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2


        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]