# [620. Not Boring Movies](https://leetcode.com/problems/not-boring-movies/)

**Difficulty:** Easy  
**Category:** Basic Aggregate Functions

## Problem

Write a SQL query to output all movies that are not boring (description != 'boring') and have an odd id. Order the result by rating in descending order.

**Table: Cinema**
```
+--------+------------+-------------+--------+
| id     | movie      | description | rating |
+--------+------------+-------------+--------+
| 1      | War        | great 3D    | 8.9    |
| 2      | Science    | fiction     | 8.5    |
| 3      | irish      | boring      | 6.2    |
| 4      | Ice song   | Fantacy     | 8.6    |
| 5      | House card | Interesting | 9.1    |
+--------+------------+-------------+--------+
```

**Output:**
```
+--------+------------+-------------+--------+
| id     | movie      | description | rating |
+--------+------------+-------------+--------+
| 5      | House card | Interesting | 9.1    |
| 1      | War        | great 3D    | 8.9    |
+--------+------------+-------------+--------+
```

**Explanation:**
- Movies with id 1 and 5 are not boring and have odd ids
- Results are ordered by rating in descending order (9.1, then 8.9)
- Movie id 3 is excluded because it's boring
- Movies with id 2 and 4 are excluded because they have even ids

## Solution Approach

Use **compound WHERE clause** to filter on both conditions simultaneously, then sort by rating. **Key insight**: Apply both filters in a single WHERE statement for optimal performance.

**Why combine conditions?** Single-pass filtering is more efficient than separating conditions into multiple steps or subqueries.

**Key concepts:**
- Compound filtering with AND operator  
- Modulo operator for odd number detection (`id % 2 = 1`)
- String inequality comparison (`!= 'boring'`)
- ORDER BY with DESC for descending sort
- Single-pass vs multi-pass query execution

**Files:**
- `solution.sql` - Standard approach with combined WHERE conditions
- `solution_cte.sql` - CTE version for readability
- `solution.py` - Pandas implementation