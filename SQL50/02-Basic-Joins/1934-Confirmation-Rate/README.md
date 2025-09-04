# [1934. Confirmation Rate](https://leetcode.com/problems/confirmation-rate/)

**Difficulty:** Medium  
**Category:** Basic Joins

## Problem

The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write an SQL query to find the confirmation rate of each user.

**Table: Signups**
```sql
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
```

**Table: Confirmations**
```sql
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+
```

**Expected Output:**
```sql
+---------+-------------------+
| user_id | confirmation_rate |
+---------+-------------------+
| 6       | 0.00              |
| 3       | 0.00              |
| 7       | 1.00              |
| 2       | 0.50              |
+---------+-------------------+
```

**Explanation:**
- User 6 did not request any confirmation messages → confirmation rate = 0.00
- User 3 had 2 timeout messages → confirmation rate = 0/2 = 0.00  
- User 7 had 3 confirmed messages → confirmation rate = 3/3 = 1.00
- User 2 had 1 confirmed and 1 timeout → confirmation rate = 1/2 = 0.50

## Solution Approach

This is a **"Rate Calculation with Missing Data"** pattern that requires:

1. **LEFT JOIN**: Include all users from Signups, even those with no confirmations
2. **Conditional Aggregation**: Count confirmed vs total confirmation attempts
3. **NULL Handling**: Users with no confirmations should get rate = 0.00
4. **Percentage Calculation**: Divide confirmed by total and round to 2 decimals

**Key insight:** This problem has two main challenges:
- **Data completeness**: Some users exist in Signups but not in Confirmations
- **Rate calculation**: Need to safely divide confirmed actions by total actions

**Core SQL concepts:**
- LEFT JOIN to preserve all users
- CASE WHEN for conditional counting
- SUM() and COUNT() for aggregation  
- ROUND() for decimal formatting
- GROUP BY for per-user calculations
- NULL handling with COALESCE (in CTE approach)

**Two main approaches:**
1. **Direct aggregation**: LEFT JOIN in main query, GROUP BY with CASE statements
2. **CTE approach**: Separate confirmation rate calculation, then join with all users

**Performance considerations:**
- LEFT JOIN ensures all users are included without additional subqueries
- Conditional aggregation in single pass is more efficient than multiple queries
- Index on `user_id` in both tables improves join performance

**Edge cases handled:**
- Users with no confirmation attempts: rate = 0.00
- Users with only timeouts: rate = 0.00  
- Users with only confirmations: rate = 1.00
- Division by zero: handled by LEFT JOIN creating NULL actions

## Pattern Recognition

**Problem Type:** Rate/Percentage Calculation with Missing Data
**When you see:** "Calculate rate/percentage for all entities, including those with no activity"
**Think:** LEFT JOIN + Conditional Aggregation + NULL Handling
**Similar problems:**
- Calculate click-through rates for all campaigns
- Find conversion rates for all products (including never-purchased)
- Compute success rates for all students (including no-shows)

**Key pattern indicators:**
- "Rate" or "percentage" in the problem
- Two tables where one might have missing data
- Need to include entities with zero activity
- Division operation with potential NULL values

**Files:**
- `solution.sql` - Direct LEFT JOIN with conditional aggregation
- `solution_cte.sql` - CTE approach with explicit NULL handling
- `solution.py` - Pandas implementation with groupby and merge