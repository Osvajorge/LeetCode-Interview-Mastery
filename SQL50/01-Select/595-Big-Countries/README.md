# [595. Big Countries](https://leetcode.com/problems/big-countries/)

**Difficulty:** Easy  
**Category:** Select

## Problem

A country is **big** if:
- It has an area of at least 3 million km², **or**
- It has a population of at least 25 million

Write a SQL query to report the `name`, `population`, and `area` of the big countries.

**Table: World**
```
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
```

**Output:**
```
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```

## Solution Approach

Filter countries using OR logic to include those meeting either size criteria. This tests understanding of **inclusive OR operations** and **multiple condition filtering** with different thresholds.

**Key concepts:**
- OR operator for inclusive filtering (either condition satisfies)
- Numeric comparison with >= operator
- Understanding OR vs AND logic in business requirements
- Pandas equivalent with | operator and proper parentheses for precedence

**Files:**
- `solution.sql` - Standard approach with OR condition
- `solution_cte.sql` - CTE version for readability practice  
- `solution.py` - Pandas implementation with boolean indexing