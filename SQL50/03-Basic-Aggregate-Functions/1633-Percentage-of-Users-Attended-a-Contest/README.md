# [1633. Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest/)

**Difficulty:** Easy  
**Category:** Basic Aggregate Functions

## Problem

Write a solution to find the percentage of the users registered in each contest rounded to two decimals. Return the result table ordered by `percentage` in **descending order**. In case of a tie, order it by `contest_id` in **ascending order**.

**Table: Users**
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
```
user_id is the primary key (column with unique values) for this table.
Each row of this table contains the name and the id of a user.

**Table: Register**
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+
```
(contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id of a user and the contest they registered into.

**Example:**

**Input:**
```
Users table:
+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |
+---------+-----------+

Register table:
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |
+------------+---------+
```

**Output:**
```
+------------+------------+
| contest_id | percentage |
+------------+------------+
| 208        | 100.0      |
| 209        | 100.0      |
| 210        | 100.0      |
| 215        | 66.67      |
| 207        | 33.33      |
+------------+------------+
```

**Explanation:**
- Contest 208: All 3 users (Alice, Bob, Alex) registered → (3/3) × 100 = 100.0%
- Contest 209: All 3 users (Alice, Bob, Alex) registered → (3/3) × 100 = 100.0%  
- Contest 210: All 3 users (Alice, Bob, Alex) registered → (3/3) × 100 = 100.0%
- Contest 215: 2 users (Alice, Alex) registered → (2/3) × 100 = 66.67%
- Contest 207: 1 user (Bob) registered → (1/3) × 100 = 33.33%

## Solution Approach

Use **Register as main table** since we want one row per contest. Calculate percentage using **fixed denominator pattern**: users per contest ÷ total users × 100. **Key insight**: Start from Register table to get contest-centric view, then use subconsulta for total users count.

**Why start from Register?** We want "one row per contest_id" in final result, so Register (which contains contest_id) should be our main table.

**Critical pattern**: For percentage calculations where denominator is fixed (total users in platform), use subconsulta `(SELECT COUNT(*) FROM Users)` rather than window functions.

**Key concepts:**
- Table selection strategy: main table = desired output granularity
- Fixed denominator pattern with subconsulta
- GROUP BY aggregation on primary dimension (contest_id)
- Handling ties in ORDER BY with multiple columns
- INNER JOIN vs no JOIN: when reference table only provides count

**Files:**
- `solution.sql` - Standard approach with subconsulta
- `solution_cte.sql` - CTE version for enhanced readability
- `solution.py` - Pandas implementation with merge and percentage calculation