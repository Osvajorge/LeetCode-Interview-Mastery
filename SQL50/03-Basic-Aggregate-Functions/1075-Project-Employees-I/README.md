# [1075. Project Employees I](https://leetcode.com/problems/project-employees-i/)

**Difficulty:** Easy  
**Category:** Basic Aggregate Functions

## Problem

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits. Return the result table in any order.

**Table: Project**
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
```
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.

**Table: Employee**
```
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
```
employee_id is the primary key of this table.
It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.

**Example:**

**Input:**
```
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
```

**Output:**
```
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
```

**Explanation:**
- Project 1: (3 + 2 + 1) / 3 = 6/3 = 2.00
- Project 2: (3 + 2) / 2 = 5/2 = 2.50

## Solution Approach

Use **INNER JOIN** to connect project assignments with employee data, then calculate **simple average** of experience years per project. **Key insight**: We only need projects that have employees assigned, so INNER JOIN is appropriate here.

**Why INNER JOIN vs LEFT JOIN?** Since we're calculating average experience, we need actual employees. Projects without employees would have undefined average (can't divide by zero), so we exclude them naturally with INNER JOIN.

**Critical insight**: This is a straightforward aggregation problem - no need to preserve empty projects since "average experience of no employees" is mathematically undefined.

**Key concepts:**
- INNER JOIN to match projects with their employees
- Simple GROUP BY aggregation on project_id
- AVG() function with ROUND() for decimal precision
- Foreign key relationship understanding (project_id → employee_id)
- When to use INNER vs LEFT JOIN based on business logic

**Files:**
- `solution.sql` - INNER JOIN with AVG aggregation
- `solution_cte.sql` - CTE version for enhanced readability  
- `solution.py` - Pandas implementation with merge and groupby