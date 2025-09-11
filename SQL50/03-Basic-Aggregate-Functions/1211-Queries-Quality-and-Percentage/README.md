# [1211. Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/)

**Difficulty:** Easy  
**Category:** Basic Aggregate Functions

## Problem

Write a solution to find each `query_name`, the `quality` and `poor_query_percentage`. Both `quality` and `poor_query_percentage` should be **rounded to 2 decimal places**. Return the result table in any order.

**Table: Queries**
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
```
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The `position` column has a value from 1 to 500.
The `rating` column has a value from 1 to 5.
Query with `rating` less than 3 is a **poor query**.

**Definitions:**
- **Quality**: The average of the ratio between query rating and its position
- **Poor Query Percentage**: The percentage of all queries with rating less than 3

**Example:**

**Input:**
```
Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+
```

**Output:**
```
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 1.66    | 33.33                 |
+------------+---------+-----------------------+
```

**Explanation:**
- **Dog queries:**
  - Quality = ((5/1) + (5/2) + (1/200)) / 3 = (5.0 + 2.5 + 0.005) / 3 = 2.50
  - Poor queries = 1 (rating=1 < 3) out of 3 total = 33.33%

- **Cat queries:** 
  - Quality = ((2/5) + (3/3) + (4/7)) / 3 = (0.4 + 1.0 + 0.571) / 3 = 1.66
  - Poor queries = 1 (rating=2 < 3) out of 3 total = 33.33%

## Solution Approach

Use **GROUP BY** on `query_name` to calculate two aggregated metrics per group. **Key insight**: Both calculations use different aggregation patterns - quality uses `AVG()` of computed ratios, while poor percentage uses conditional counting.

**Quality Calculation:** Calculate `rating/position` for each row, then take the average of these ratios within each group.

**Poor Query Percentage:** Use conditional aggregation to count rows where `rating < 3`, then divide by total count in group and multiply by 100.

**Critical pattern:** When calculating percentages within groups, use `COUNT(CASE WHEN condition THEN 1 END) / COUNT(*) * 100` for precise conditional counting.

**Key concepts:**
- GROUP BY aggregation with multiple computed metrics
- Conditional counting with CASE WHEN inside aggregate functions
- Mathematical operations within aggregate functions (rating/position)
- Percentage calculations within grouped data
- Proper rounding for decimal precision (ROUND to 2 places)

**Files:**
- `solution.sql` - Standard GROUP BY with AVG and conditional COUNT
- `solution_cte.sql` - CTE version separating calculation logic
- `solution.py` - Pandas implementation with groupby and apply functions