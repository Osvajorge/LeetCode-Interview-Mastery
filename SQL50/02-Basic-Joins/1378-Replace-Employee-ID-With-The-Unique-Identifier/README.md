# [1378. Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)

**Difficulty:** Easy  
**Category:** Basic Joins

## Problem

Write a SQL query to show the **unique ID** of each user. If a user does not have a unique ID replace just show **null**.

**Table: Employees**
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
```

**Table: EmployeeUNI**
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
```

**Example:**

**Input:**
```
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+

EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
```

**Output:**
```
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
```

**Explanation:**
- Alice and Bob don't have unique IDs, so they show null
- Meir, Winston, and Jonathan have matching records in EmployeeUNI

## Solution Approach

Use **LEFT JOIN** to preserve all employees from the main table while optionally matching unique IDs. This demonstrates fundamental join concepts and NULL handling in relational databases.

**Key concepts:**
- LEFT JOIN vs INNER JOIN behavior (preserving all left table rows)
- NULL handling when no match exists in right table
- Join condition on common key (id column)
- Column selection from multiple tables
- Pandas merge() with how='left' parameter for equivalent functionality

**Files:**
- `solution.sql` - Standard LEFT JOIN approach
- `solution_cte.sql` - CTE version encapsulating join logic  
- `solution.py` - Pandas merge implementation with left join