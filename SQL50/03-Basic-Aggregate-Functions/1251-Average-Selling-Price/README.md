# [1251. Average Selling Price](https://leetcode.com/problems/average-selling-price/)

**Difficulty:** Easy  
**Category:** Basic Aggregate Functions

## Problem

Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.

**Table: Prices**
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
```

**Table: UnitsSold**
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
```

**Example:**

**Input:**
```
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+

UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
```

**Output:**
```
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+
```

**Explanation:**
- Product 1: ((100 × 5) + (15 × 20)) / 115 = 800/115 = 6.96
- Product 2: ((200 × 15) + (30 × 30)) / 230 = 3900/230 = 16.96

## Solution Approach

Use **LEFT JOIN** to preserve all products, then calculate **weighted average** by matching sales with correct price periods. **Key insight**: Products can have multiple price periods, so sales must be matched with the correct price based on purchase_date.

**Why weighted average?** Average price = Total Revenue ÷ Total Units, not simple average of individual prices.

**Critical pitfall**: Don't filter out products before groupby - this removes products with no sales that should show average_price = 0.

**Key concepts:**
- LEFT JOIN to preserve all products
- Date range filtering with BETWEEN conditions  
- Weighted average calculation (SUM(price × units) / SUM(units))
- Handling products with no valid sales (COALESCE or fillna)
- JOIN condition vs WHERE condition placement for preserving rows

**Files:**
- `solution.sql` - LEFT JOIN with date filtering in JOIN condition
- `solution_cte.sql` - CTE version separating join and calculation logic
- `solution.py` - Pandas implementation with groupby and weighted average calculation