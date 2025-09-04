# [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/)

**Difficulty:** Medium  
**Category:** Basic Joins

## Problem

Write a SQL query to find the names of managers who have at least five direct reports.

**Table: Employee**
```sql
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | NULL      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
| 107 | Bob   | B          | 102       |
+-----+-------+------------+-----------+
```

**Expected Output:**
```sql
+------+
| name |
+------+
| John |
+------+
```

**Explanation:** John is the only manager with at least 5 direct reports (Dan, James, Amy, Anne, and Ron all report to John).

## Solution Approach

This is a **"Find X with Property Y"** pattern problem that requires:

1. **Aggregation**: Count direct reports per manager
2. **Filtering**: Keep only managers with ≥ 5 reports  
3. **Join/Lookup**: Get manager names from the filtered results

**Key insight:** This is a two-step process:
- Step 1: `GROUP BY managerId HAVING COUNT(*) >= 5` (find qualifying manager IDs)
- Step 2: `WHERE id IN (subquery)` or `JOIN` (get names for those IDs)

**Core SQL concepts:**
- GROUP BY with aggregate functions
- HAVING clause for filtering groups
- Subqueries with IN operator
- Self-referencing table relationships
- INNER JOIN for connecting related data

**Alternative approaches:**
1. **Subquery with IN**: Filter main table using subquery results
2. **CTE with JOIN**: More readable, explicit step-by-step approach
3. **Window functions**: Using COUNT() OVER() for advanced scenarios

**Performance considerations:**
- Subquery approach: Simple but may scan table twice
- JOIN approach: Usually more efficient for large datasets
- Both approaches benefit from index on `managerId` column

**Files:**
- `solution.sql` - Subquery with IN approach
- `solution_cte.sql` - CTE with JOIN approach  
- `solution.py` - Pandas implementation with value_counts()

## Pattern Recognition

**Problem Type:** Aggregation + Filtering + Lookup
**When you see:** "Find [entities] with at least/most [number] of [related items]"
**Think:** GROUP BY → HAVING → JOIN/IN
**Similar problems:** 
- Find customers with 3+ orders
- Find products sold in 5+ countries
- Find teachers with 10+ students