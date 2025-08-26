# [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/)

**Difficulty:** Easy  
**Category:** Select

## Problem

Find the names of the customer that are **not referred by** the customer with `id = 2`.

**Table: Customer**
```
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
```

**Output:**
```
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```

## Solution Approach

Filter customers excluding those referred by customer ID 2. **Key insight**: Handle NULL values correctly since `NULL != 2` evaluates to NULL (not true), so we need explicit NULL check with `IS NULL`.

**Key concepts:**
- NULL handling with IS NULL operator
- Boolean logic with OR operator  
- Understanding NULL behavior in SQL comparisons
- Pandas equivalent with isnull() and | operator for boolean operations

**Files:**
- `solution.sql` - Standard approach with NULL handling
- `solution_cte.sql` - CTE version for practice
- `solution.py` - Pandas implementation with isnull()