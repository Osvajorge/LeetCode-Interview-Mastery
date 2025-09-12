# [1193. Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/)

**Difficulty:** Medium  
**Category:** Basic Aggregate Functions

## Problem

Write a SQL query to find for each month and country:
- Number of transactions and their total amount
- Number of approved transactions and their total amount

**Table: Transactions**
```
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | null    | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
```

**Expected Output:**
```
+---------+---------+-------------+----------------+--------------------+-----------------------+
| month   | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+---------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12 | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01 | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01 | null    | 1           | 1              | 2000               | 2000                  |
+---------+---------+-------------+----------------+--------------------+-----------------------+
```

## Solution Approach

This problem combines multiple SQL concepts:

**Key Concepts:**
- **Date formatting**: `DATE_FORMAT(trans_date, '%Y-%m')` for month extraction
- **Conditional aggregation**: `COUNT(CASE WHEN condition THEN 1 END)` and `SUM(CASE WHEN condition THEN amount ELSE 0 END)`
- **Multiple aggregations**: Different calculations on same grouped data
- **NULL handling**: Including NULL country values in grouping

**SQL Pattern:**
```sql
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, 
       country,
       COUNT(id) AS trans_count,
       COUNT(CASE WHEN state = 'approved' THEN id END) AS approved_count,
       SUM(amount) AS trans_total_amount,
       SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
```

**Pandas Approach:**
- Create helper columns for conditional calculations
- Use `groupby(dropna=False)` to include NULL countries
- Apply multiple aggregations with `.agg()`

**Files:**
- `solution.sql` - Standard SQL approach with conditional aggregation
- `solution_cte.sql` - CTE version for readability
- `solution.py` - Pandas implementation with pre-calculated conditional columns

## Key Learning Points

1. **Date Formatting**: Converting dates to month-year format for grouping
2. **Conditional Aggregation**: Using CASE WHEN for filtered counts and sums
3. **NULL Handling**: Remember that SQL includes NULLs in GROUP BY, pandas excludes by default
4. **Multiple Metrics**: Calculating different aggregations on the same grouped data
5. **Data Engineering**: Pre-calculating conditional columns for better performance in pandas