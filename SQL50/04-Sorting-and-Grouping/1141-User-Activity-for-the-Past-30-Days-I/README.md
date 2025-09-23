# [1141. User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/)

**Difficulty:** Easy  
**Category:** Sorting and Grouping

## Problem

Write a solution to find the daily active user count for each date within 30 days ending 2019-07-27. A user is considered active if they made at least one activity on that date.

**Table: Activity**
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
```

**Example:**

**Input:**
```
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 4       | 3          | 2019-06-25    | open_session  |
+---------+------------+---------------+---------------+
```

**Output:**
```
+------------+--------------+
| day        | active_users |
+------------+--------------+
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+
```

**Explanation:**
- 2019-07-20: Users {1, 2} were active → 2 active users
- 2019-07-21: Users {2, 3} were active → 2 active users  
- 2019-06-25: Outside date range (before 2019-06-28)

Note: User 1 had multiple activities on 2019-07-20, but counts as 1 active user.

## Solution Approach

Use **GROUP BY activity_date with COUNT(DISTINCT user_id)** to count unique active users per day. **Key insight**: We want one row per day (GROUP BY date), counting distinct users who had any activity that day.

**Why COUNT(DISTINCT user_id)?** Same user can have multiple activities/sessions per day, but should only be counted once as "active" for that day.

**Date filtering with BETWEEN** to get the exact 30-day window ending on specified date.

**Key concepts:**
- GROUP BY determines output granularity (one row per day)
- COUNT(DISTINCT) for unique user counting  
- Date range filtering with BETWEEN
- Column aliasing for clean output
- Pandas groupby with nunique() for distinct counting

**Files:**
- `solution.sql` - Direct GROUP BY approach
- `solution_cte.sql` - CTE version separating filter and aggregation logic  
- `solution.py` - Pandas implementation with date filtering and nunique()