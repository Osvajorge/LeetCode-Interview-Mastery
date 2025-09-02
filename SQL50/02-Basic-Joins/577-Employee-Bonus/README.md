# [577. Employee Bonus](https://leetcode.com/problems/employee-bonus/)

**Difficulty:** Easy  
**Category:** Basic Joins

## Problem

Write a SQL query to report the **name** and **bonus** amount of each employee with a bonus **less than 1000**.

Return the result table in **any order**.

**Table: Employee**
```
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
```

**Table: Bonus**
```
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
```

**Output:**
```
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
```

**Explanation:**
- Brad and John don't appear in the Bonus table, so their bonus is null (< 1000)
- Dan's bonus is 500 (< 1000)  
- Thomas's bonus is 2000 (>= 1000), so excluded

## Solution Approach

This problem requires a **LEFT JOIN** to preserve all employees, even those without bonus records. The key insight is handling NULL values correctly - employees without bonus records should be included since NULL satisfies the "less than 1000" condition.

**Key concepts:**
- LEFT JOIN to preserve all records from the left table
- NULL handling with `IS NULL` condition
- Boolean logic with OR operator for inclusive filtering

**Algorithm:**
1. LEFT JOIN Employee and Bonus tables on empId
2. Filter results where bonus < 1000 OR bonus IS NULL
3. Select only name and bonus columns

**Edge cases to consider:**
- Employees with no bonus record (NULL handling)
- Employees with bonus exactly equal to 1000 (excluded)
- Multiple bonus records per employee (problem assumes 1:1 or 1:0 relationship)

**Files:**
- `solution.sql` - Standard LEFT JOIN approach
- `solution_cte.sql` - CTE version for readability  
- `solution.py` - Pandas implementation with merge