/*
LeetCode Problem: 595. Big Countries
URL: https://leetcode.com/problems/big-countries/

Problem:
    Table: World
        - name        (varchar)
        - continent   (varchar)
        - area        (int)
        - population  (int)
        - gdp         (int)

    Task:
        Write an SQL query to report the name, population, and area of the big countries.
        A country is considered big if:
            - area >= 3000000   OR
            - population >= 25000000

    Example:
        Input:
            +-------------+-----------+---------+-------------+--------------+
            | name        | continent | area    | population  | gdp          |
            +-------------+-----------+---------+-------------+--------------+
            | Afghanistan | Asia      | 652230  | 25500100    | 20343000000  |
            | Albania     | Europe    | 28748   | 2831741     | 12960000000  |
            | Algeria     | Africa    | 2381741 | 37100000    | 188681000000 |
            | Andorra     | Europe    | 468     | 78115       | 3712000000   |
            | Angola      | Africa    | 1246700 | 20609294    | 100990000000 |
            +-------------+-----------+---------+-------------+--------------+

        Output:
            +-------------+-------------+---------+
            | name        | population  | area    |
            +-------------+-------------+---------+
            | Afghanistan | 25500100    | 652230  |
            | Algeria     | 37100000    | 2381741 |
            +-------------+-------------+---------+

Constraints:
    - Each row contains unique country information
*/


-- ------------------------------ Filtering Approach ------------------------------ --
/*
Approach: Use WHERE with OR Condition

Explanation:
    - We want countries that are considered "big."
    - Two possible conditions for being big:
        1. area >= 3000000
        2. population >= 25000000
    - Use OR to combine both conditions.
    - Select only the required columns: name, population, area.

Time Complexity : O(N) — scans all rows in the World table
Space Complexity: O(1) — no extra space, just filtering
*/


-- sql command
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;