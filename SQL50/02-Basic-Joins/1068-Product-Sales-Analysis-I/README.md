# [1068. Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i/)

**Difficulty:** Easy  
**Category:** Basic Joins

## Problem

Write a SQL query that reports the **product_name**, **year** and **price** for each **sale_id** in the **Sales** table.

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

**Table: Product**
```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
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
+---------+------------+------+----------+-------+

Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
```

**Output:**
```
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
```

## Solution Approach

Join the Sales table with Product table to enrich sales data with product names. Use **LEFT JOIN** to ensure all sales records are preserved even if product information is missing (though this would be unusual in practice).

**Key concepts:**
- LEFT JOIN to preserve all sales records
- Join condition on common foreign key (product_id)
- Column selection from both tables in join result
- Data enrichment pattern (adding descriptive information to transactional data)
- Pandas merge() with how='left' for equivalent functionality

**Files:**
- `solution.sql` - Standard LEFT JOIN approach
- `solution_cte.sql` - CTE version for readability
- `solution.py` - Pandas merge implementation