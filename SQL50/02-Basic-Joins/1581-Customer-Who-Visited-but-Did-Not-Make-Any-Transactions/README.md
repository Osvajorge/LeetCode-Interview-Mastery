# [1581. Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)

**Difficulty:** Easy  
**Category:** Basic Joins

## Problem

Write a SQL query to find the IDs of the users who **visited without making any transactions** and the **number of times** they made these types of visits.

Return the result table sorted in **any order**.

**Table: Visits**
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
```

**Table: Transactions**  
```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
```

**Example:**

**Input:**
```
Visits:
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+

Transactions:
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
```

**Output:**
```
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+
```

## Solution Approach

Use **LEFT JOIN** to connect all visits with their potential transactions, then filter for visits without transactions. **Critical insight**: Use `COUNT(*)` instead of `COUNT(column)` when counting rows where the column is NULL.

**Key concepts:**
- LEFT JOIN to preserve all visits (including those without transactions)
- WHERE IS NULL to filter visits without transactions  
- GROUP BY customer_id to aggregate by customer
- COUNT(*) vs COUNT(column) behavior with NULL values
- Pandas merge with how='left' and isnull() filtering
- After pandas broup by use .size(), this counts rows by group

**Common Mistake:** Using `COUNT(t.transaction_id)` will return 0 because COUNT() ignores NULL values. Use `COUNT(*)` to count all rows.

**Files:**
- `solution.sql` - Standard LEFT JOIN with COUNT(*) fix
- `solution_cte.sql` - CTE version for better readability
- `solution.py` - Pandas implementation with merge and groupby