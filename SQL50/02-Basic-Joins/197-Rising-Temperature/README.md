# [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/)

**Difficulty:** Easy  
**Category:** Basic Joins

## Problem

Write a SQL query to find all dates' **IDs** with higher temperatures compared to its **previous dates** (yesterday).

**Table: Weather**
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
```

**Example:**

**Input:**
```
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
```

**Output:**
```
+----+
| id |
+----+
| 2  |
| 4  |
+----+
```

**Explanation:**
- In 2015-01-02, the temperature was higher (25) than the previous day (10)
- In 2015-01-03, the temperature was lower (20) than the previous day (25)
- In 2015-01-04, the temperature was higher (30) than the previous day (20)

## Solution Approach

Use **self-join** to compare each date with its previous consecutive day. **Key insight**: Only include strictly consecutive days - if there's a gap in dates, those records should not be compared.

**Why not LAG()?** LAG() compares with the "previous row in order" but doesn't guarantee consecutive dates. For example, if we have data for Jan 1st and Jan 3rd (missing Jan 2nd), LAG() would compare Jan 3rd with Jan 1st, which is incorrect for this problem.

**Self-join approach ensures strict consecutiveness** by only joining when `yesterday = today - 1 day` exactly exists in the dataset.

**Key concepts:**
- Self-join pattern for temporal comparisons
- DATE_SUB() for date arithmetic in MySQL
- INNER JOIN behavior (only matches when both conditions exist)
- Handling gaps in time series data correctly
- Pandas self-merge with datetime operations and Timedelta

**Files:**
- `solution.sql` - Self-join with DATE_SUB for consecutive day comparison
- `solution_cte.sql` - CTE version separating join logic from filtering
- `solution.py` - Pandas self-merge implementation with datetime handling