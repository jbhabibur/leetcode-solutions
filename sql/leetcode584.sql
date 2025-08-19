/*
LeetCode Problem: 584. Find Customer Referee
URL: https://leetcode.com/problems/find-customer-referee/

Problem:
    Table: Customer
        - id          (int)
        - name        (varchar)
        - referee_id  (int)

    Task:
        Write an SQL query to report the names of customers who are 
        not referred by the customer with id = 2.

    Example:
        Input:
            +----+------+-------------+
            | id | name | referee_id  |
            +----+------+-------------+
            | 1  | Will | null        |
            | 2  | Jane | null        |
            | 3  | Alex | 2           |
            | 4  | Bill | null        |
            | 5  | Zack | 1           |
            | 6  | Mark | 2           |
            +----+------+-------------+

        Output:
            +------+
            | name |
            +------+
            | Will |
            | Jane |
            | Bill |
            | Zack |
            +------+

Constraints:
    - id is the primary key
    - Each referee_id is either null or references an id in the Customer table
*/


-- ------------------------------ Filtering Approach ------------------------------ --
/*
Approach: Use WHERE with OR Condition

Explanation:
    - We need to return customers who are NOT referred by id = 2.
    - So, two valid cases:
        1. referee_id IS NULL   → Customer has no referrer
        2. referee_id != 2      → Customer referred by someone else (not id 2)
    - Use an OR condition to capture both cases.
    - Select only the name column for output.

Time Complexity : O(N) — must scan through all rows
Space Complexity: O(1) — no extra space, just filtering
*/


-- sql commands
select name
from Customer
where referee_id is null or referee_id != 2;
