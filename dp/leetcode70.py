"""
LeetCode Problem: 70. Climbing Stairs
URL             : https://leetcode.com/problems/climbing-stairs/

Problem:
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


# ------------------------------ 2. Recursive + Memoization ------------------------------ #
"""
Approach: Recursive with Memoization (Top-down Dynamic Programming)

Optimization:
    - Use a dictionary to cache results for each subproblem
    - Avoid redundant computations
    - Converts exponential time to linear time

Base Cases:
    - If n == 0: 1 way (do nothing)
    - If n < 0 : 0 ways (invalid)

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

# ------------------------------ 3. Bottom-Up DP (Tabulation) ------------------------------ #
"""
Approach: Bottom-Up Dynamic Programming (Tabulation)

Explanation:
    - Initialize dp[1] = 1, dp[2] = 2 as base cases
    - Iteratively build up dp[i] = dp[i-1] + dp[i-2]
    - Avoids recursion, runs in linear time

Base Cases:
    - If n == 0: 0 ways (interpreted here as no steps to climb)
    - If n == 1: 1 way
    - If n == 2: 2 ways (1+1 or 2)

Note:
    This differs from the recursive approaches where n == 0 is considered 1 way (doing nothing).

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

# ------------------------------ 4. Bottom-Up DP (Space Optimized) ------------------------------ #
"""
Approach: Bottom-Up Dynamic Programming (Tabulation with Space Optimization)

Explanation:
    - Track only the last two computed values instead of full dp array
      (prev2 = dp[i - 2], prev1 = dp[i - 1])
    - For each step i from 3 to n:
        curr = prev1 + prev2
    - Update prev2 and prev1 accordingly

    This reduces space complexity from O(n) to O(1).

Base Cases:
    - If n == 0: 0 ways (interpreted here as no steps to climb)
    - If n == 1: 1 way
    - If n == 2: 2 ways (1+1 or 2)

Note:
    This differs from the recursive approaches where n == 0 is considered 1 way (doing nothing).

Time Complexity : O(n) — one loop from 3 to n
Space Complexity: O(1) — only three variables used
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2


        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            curr_i = prev1 + prev2

            prev2 = prev1
            prev1 = curr_i

        return curr_i