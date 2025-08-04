"""
LeetCode Problem: 121. Best Time to Buy and Sell Stock
URL             : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
    You are given an array `prices` where prices[i] is the price of a stock on the i-th day.
    You want to maximize your profit by choosing a single day to buy one stock and
    a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
"""


# ---------------------------- 1. Brute Force (Nested Loops) ---------------------------- #
"""
Approach: Brute Force (Try all pairs)

Explanation:
    For each pair of days (i, j) such that i < j:
        - Buy on day i
        - Sell on day j
        - Calculate profit = prices[j] - prices[i]
        - Track the maximum profit over all such pairs

    Return the highest profit found. If no profit is possible, return 0.

Time Complexity : O(n^2) — due to nested loop over all pairs  
Space Complexity: O(1)   — constant space used
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    curr_profit = prices[j] - prices[i]
                    max_profit = max(max_profit, curr_profit)

        return max_profit

# Example usage
prices = [7,6,4,3,1]
sol = Solution()
print(sol.maxProfit(prices))



# ---------------------------- 2. Optimized One-Pass ---------------------------- #
"""
Approach: One-pass Dynamic Programming

Explanation:
    - Track the lowest price encountered so far (best_buy).
    - For each price, calculate profit = current price - best_buy.
    - Update max_profit if this profit is higher.
    - Update best_buy if a new lower price is found.

Time Complexity : O(n) — single traversal of the list  
Space Complexity: O(1) — uses constant extra space
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        best_buy = prices[0]

        for i in range(1, n):
            if prices[i] > best_buy:
                max_profit = max(max_profit, (prices[i] - best_buy))
            best_buy = min(best_buy, prices[i])

        return max_profit