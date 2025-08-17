/*
LeetCode Problem: 1757. Recyclable and Low Fat Products
URL: https://leetcode.com/problems/recyclable-and-low-fat-products/

Problem:
    Table: Products
        - product_id (int)
        - low_fats   (enum: 'Y'/'N')
        - recyclable (enum: 'Y'/'N')

    Task:
        Write an SQL query to find the IDs of products that are both
        low fat ('Y') and recyclable ('Y').

    Example:
        Input:
            +-------------+----------+-------------+
            | product_id  | low_fats | recyclable  |
            +-------------+----------+-------------+
            | 0           | Y        | N           |
            | 1           | Y        | Y           |
            | 2           | N        | Y           |
            | 3           | Y        | Y           |
            | 4           | N        | N           |
            +-------------+----------+-------------+

        Output:
            +-------------+
            | product_id  |
            +-------------+
            | 1           |
            | 3           |
            +-------------+

Constraints:
    - product_id is the primary key
    - Each product’s low_fats and recyclable fields are 'Y' or 'N'
*/


-- ------------------------------ Filtering Approach ------------------------------ --
/*
Approach: Use WHERE with AND Condition

Explanation:
    - The Products table contains columns indicating if a product is low fat
      and if it is recyclable.
    - To satisfy the problem, we need only products where:
        low_fats   = 'Y'
        recyclable = 'Y'
    - Apply an AND condition in the WHERE clause.
    - Select only product_id for the output.

Time Complexity : O(N) — must scan through all rows
Space Complexity: O(1) — no extra space, just filtering
*/


-- sql commands
select product_id
from Products
where low_fats = 'Y' and recyclable = 'Y';