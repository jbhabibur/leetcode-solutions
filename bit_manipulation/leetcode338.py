"""
LeetCode Problem: 338. Counting Bits
URL             : https://leetcode.com/problems/counting-bits/

Problem:
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
    ans[i] is the number of 1's in the binary representation of i.

Constraints:
    - 0 <= n <= 10^5

Example:
    Input : n = 5
    Output: [0, 1, 1, 2, 1, 2]

Explanation:
    - 0  -> 0b000 -> 0 one
    - 1  -> 0b001 -> 1 one
    - 2  -> 0b010 -> 1 one
    - 3  -> 0b011 -> 2 ones
    - 4  -> 0b100 -> 1 one
    - 5  -> 0b101 -> 2 ones
"""


# ------------------------------ 1. String-Based Brute Force Approach ------------------------------ #
"""
Approach: Convert each number to binary and count the number of '1's.

Explanation:
    - Iterate from 0 to n.
    - For each number, convert it to binary using bin().
    - Strip the '0b' prefix, then count the number of '1's in the string.
    - Append the count to the result list.

Time Complexity : O(n log n) — because converting a number to binary and counting bits takes O(log n)
Space Complexity: O(n)       — to store the result array
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            binary_str = bin(i)[2:]  # Remove '0b' prefix
            count = 0

            for char in binary_str:
                if char == "1":
                    count += 1

            ans.append(count)

        return ans

# Example usage
n = 5
sol = Solution()
print(sol.countBits(n))  # Output: [0, 1, 1, 2, 1, 2]
