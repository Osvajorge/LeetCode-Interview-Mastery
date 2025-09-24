# [1070. Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/)

**Difficulty:** Medium  
**Category:** Sorting and Grouping

## Problem

Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

**Table: Sales**
```
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
```

**Example:**

**Input:**
```
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
| 3       | 200        | 2010 | 8        | 7000  |
| 4       | 300        | 2009 | 20       | 3000  |
| 5       | 300        | 2010 | 25       | 4000  |
+---------+------------+------+----------+-------+
```

**Output:**
```
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+
| 100        | 2008       | 10       | 5000  |
| 200        | 2010       | 8        | 7000  |
| 300        | 2009       | 20       | 3000  |
+------------+------------+----------+-------+
```

**Explanation:**
- Product 100: First sold in 2008 (10 units, $5000)
- Product 200: First sold in 2010 (8 units, $7000) - note 2010 < 2011  
- Product 300: First sold in 2009 (20 units, $3000)

## Solution Approach

Use **RANK() window function with PARTITION BY product_id ORDER BY year** to identify the first year for each product. **Key insight**: Need to rank years within each product group, then filter for rank = 1 to get the earliest year's data.

**Why RANK() over MIN()?** MIN() only gives us the year value, but we need all columns (quantity, price) from that specific first-year record.

**Window function pattern** - PARTITION BY creates separate ranking within each product group, ORDER BY determines what "first" means.

**Key concepts:**
- RANK() vs ROW_NUMBER() vs DENSE_RANK() for handling ties
- PARTITION BY for grouping within window functions  
- Subquery or CTE to filter ranked results
- Window functions for "top-N per group" problems
- Pandas rank() with groupby for equivalent logic

**Files:**
- `solution.sql` - Subquery approach with RANK() window function
- `solution_cte.sql` - CTE version for cleaner separation of logic
- `solution.py` - Pandas implementation with groupby rank() method