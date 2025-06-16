from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Number of customers (rows in the 2D array)
        m = len(accounts)

        # Number of banks (columns in each row)
        # Assumes all rows are of equal length
        n = len(accounts[0])

        # Variable to track the maximum wealth found
        max_sum = 0

        # Loop through each customer
        for i in range(m):
            # Temporary variable to store the sum of current customer's accounts
            summation = 0

            # Loop through each bank account of the current customer
            for j in range(n):
                summation += accounts[i][j]  # Add bank balance to the sum

            # Update max_sum if the current customer's total is greater
            max_sum = max(max_sum, summation)

        # Return the maximum wealth among all customers
        return max_sum

# Example usage
accounts = [[1, 5], [7, 3], [3, 5]]  # Each sublist represents a customer's accounts in different banks
sol = Solution()
print(sol.maximumWealth(accounts))  # Output: 10 (7 + 3)
