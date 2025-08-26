# [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/)

**Difficulty:** Easy  
**Category:** Select

## Problem

Write a SQL query to find the ids of products that are both low fat and recyclable.

**Table: Products**
```
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
```

**Output:**
```
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
```

## Solution Approach

Basic filtering with WHERE clause using AND operator to check both conditions simultaneously.

**Key concepts:**
- Simple WHERE filtering
- Boolean logic with AND
- String comparison with equality operator

**Files:**
- `solution.sql` - Standard approach
- `solution_cte.sql` - CTE version for readability
- `solution.py` - Pandas implementation