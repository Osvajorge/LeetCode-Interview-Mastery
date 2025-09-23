# [2556. Number of Unique Subjects Taught by Each Teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)

**Difficulty:** Easy  
**Category:** Sorting and Grouping

## Problem

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

**Table: Teacher**
```
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
```

**Example:**

**Input:**
```
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
```

**Output:**
```
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
```

**Explanation:**
- Teacher 1: Teaches subjects {2, 3} → 2 unique subjects
- Teacher 2: Teaches subjects {1, 2, 3, 4} → 4 unique subjects

Note: Teacher 1 teaches subject 2 in both departments 3 and 4, but we count subject 2 only once.

## Solution Approach

Use **GROUP BY with COUNT(DISTINCT)** to count unique subjects per teacher. **Key insight**: Same teacher can teach the same subject in different departments, but we only count each subject once per teacher.

**Why COUNT(DISTINCT)?** Regular COUNT() would count duplicate subject entries, but we need unique subjects only.

**Straightforward aggregation** - no joins needed since all data is in one table.

**Key concepts:**
- GROUP BY for per-teacher aggregation
- COUNT(DISTINCT) vs COUNT() - eliminates duplicates
- Column aliasing for clean output
- Basic pandas groupby with nunique()

**Files:**
- `solution.sql` - Direct GROUP BY approach  
- `solution_cte.sql` - CTE version for readability
- `solution.py` - Pandas implementation with nunique()