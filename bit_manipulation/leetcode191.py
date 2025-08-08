"""
LeetCode Problem: 191. Number of 1 Bits
URL: https://leetcode.com/problems/number-of-1-bits/

Problem:
    Write a function that takes the binary representation of an unsigned integer
    and returns the number of '1' bits it has (also known as the Hamming weight).

    Example:
        Input : n = 11 (binary 1011)
        Output: 3

Constraints:
    - The input must be a binary representation fitting in a 32-bit unsigned integer.

Follow-up:
    Could you do it in O(1) space and without converting to a string?
"""


# ------------------------------ String Conversion Approach ------------------------------ #
"""
Approach: Convert to Binary String and Count '1's

Explanation:
    - Convert the number n to its binary string representation using bin().
    - Ignore the '0b' prefix by slicing from index 2 onward.
    - Iterate through the string and count how many characters are '1'.
    - Return the total count.

Time Complexity : O(log n) — converting to binary & iterating over bits
Space Complexity: O(log n) — binary string storage
"""

from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n)[2:]
        count = 0

        for char in binary_string:
            if char == "1":
                count += 1

        return count

# Example usage
n = 11
sol = Solution()
sol.hammingWeight(n)


# ------------------------------ Bitwise Shift Approach ------------------------------ #
"""
Approach: Check Each Bit Using Bitwise Shift

Explanation:
    - Integers are stored in binary form.
    - We can check each bit from most significant (left) to least significant (right)
      using a bitwise right shift (>>).
    - `(n >> k) & 1` isolates the k-th bit (0 or 1).
    - Count how many bits are 1 in the 32-bit representation.

Time Complexity : O(1) — fixed 32-bit loop (constant iterations)
Space Complexity: O(1) — no extra space used
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for k in range(31, -1, -1):  # Check each of the 32 bits
            if (n >> k) & 1 == 1:
                count += 1
        return count