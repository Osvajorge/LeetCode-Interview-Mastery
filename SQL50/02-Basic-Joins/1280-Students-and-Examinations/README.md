# [1280. Students and Examinations](https://leetcode.com/problems/students-and-examinations/)

**Difficulty:** Easy  
**Category:** Basic Joins

## Problem

Write a SQL query to find the number of times each student attended each exam.

Return the result table ordered by `student_id` and `subject_name`.

**Table: Students**
```
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
```

**Table: Subjects**
```
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
```

**Table: Examinations**
```
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
+------------+--------------+
```

**Expected Output:**
```
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 2              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 0              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 0              |
| 13         | John         | Physics      | 0              |
| 13         | John         | Programming  | 0              |
+------------+--------------+--------------+----------------+
```

## Solution Approach

This problem requires creating a **complete matrix** of all student-subject combinations, then counting actual exam attendance.

**Key Challenge:** Show ALL students with ALL subjects, even if attendance is 0.

**Strategy:**
1. **CROSS JOIN** Students × Subjects (creates all possible combinations)
2. **LEFT JOIN** with Examinations (preserves all combinations, adds exam data where exists)
3. **COUNT** exam records for each combination
4. **Handle NULL values** properly (convert to 0 for attendance count)

**Critical Insight:** We need every student-subject pair in the result, regardless of whether exams were taken. This requires starting with the complete matrix rather than filtering based on existing exam records.

**Common Mistakes:**
- Starting with Examinations table (loses students with no exams)
- Using only `student_id` in JOIN condition (wrong granularity)
- Incorrect NULL handling in aggregation

**Files:**
- `solution.sql` - Standard CROSS JOIN + LEFT JOIN approach
- `solution_cte.sql` - CTE version for better readability
- `solution.py` - Pandas implementation with proper aggregation