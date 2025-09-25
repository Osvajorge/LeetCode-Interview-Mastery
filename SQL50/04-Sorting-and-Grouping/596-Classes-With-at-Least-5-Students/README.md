# [596. Classes With At Least 5 Students](https://leetcode.com/problems/classes-with-at-least-5-students/)

**Difficulty:** Easy  
**Category:** Sorting and Grouping

## Problem

Write a solution to find all the classes that have **at least 5 students**.

**Table: Courses**
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
```

**Example:**

**Input:**
```
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
```

**Output:**
```
+---------+
| class   |
+---------+
| Math    |
+---------+
```

**Explanation:**
- Math: 6 students {A, C, E, G, H, I} ≥ 5 ✅
- English: 1 student {B} < 5 ❌  
- Biology: 1 student {D} < 5 ❌
- Computer: 1 student {F} < 5 ❌

## Solution Approach

Use **GROUP BY with HAVING clause** to filter groups based on aggregate conditions. **Key insight**: HAVING filters groups after aggregation, perfect for "groups where COUNT ≥ X" problems.

**Why HAVING over subquery?** This is a direct group filtering problem - we want classes (groups) where the count meets a condition. HAVING is designed exactly for this pattern.

**Simple one-step aggregation** - no need for CTEs or subqueries when filtering aggregated groups directly.

**Key concepts:**
- GROUP BY creates groups per class
- HAVING filters groups (vs WHERE filtering rows)  
- COUNT() counts rows in each group
- Direct group filtering without intermediate steps
- Pandas groupby with filter() method for group-level conditions

**Files:**
- `solution.sql` - Direct HAVING approach (optimal)
- `solution_cte.sql` - CTE version (educational, shows alternative)
- `solution.py` - Pandas implementation with groupby filter