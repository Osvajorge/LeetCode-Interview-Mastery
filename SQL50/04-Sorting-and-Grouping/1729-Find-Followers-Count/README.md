# [1729. Find Followers Count](https://leetcode.com/problems/find-followers-count/)

**Difficulty:** Easy  
**Category:** Sorting and Grouping

## Problem

Write a solution to find the number of followers for each user. Return the result table ordered by `user_id` in ascending order.

**Table: Followers**
```
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
```

**Example:**

**Input:**
```
Followers table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+
```

**Output:**
```
+---------+----------------+
| user_id | followers_count |
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+
```

**Explanation:**
- User 0: Followed by user 1 → 1 follower
- User 1: Followed by user 0 → 1 follower  
- User 2: Followed by users {0, 1} → 2 followers

## Solution Approach

Use **GROUP BY with COUNT()** to count followers per user, then **ORDER BY** for consistent output. **Key insight**: Each row represents one follower relationship, so counting rows per user gives us the follower count.

**Why GROUP BY user_id?** We want to collapse all follower relationships for each user into a single summary row showing their total follower count.

**Why ORDER BY?** The problem specifically requires results ordered by user_id ascending. This ensures consistent, predictable output regardless of input data order.

**Fundamental aggregation pattern** - transforming detail records (individual follow relationships) into summary statistics (follower counts per user).

**Key concepts:**
- GROUP BY for user-level aggregation
- COUNT() for counting relationships/rows
- ORDER BY for result ordering consistency
- Pandas groupby with automatic index sorting behavior
- Understanding the difference between detail records and summary statistics

**Files:**
- `solution.sql` - Standard GROUP BY approach with explicit ORDER BY
- `solution_cte.sql` - CTE version separating aggregation from presentation logic
- `solution.py` - Pandas implementation leveraging groupby's automatic sorting behavior