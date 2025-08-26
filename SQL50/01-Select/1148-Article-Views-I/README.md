# [1148. Article Views I](https://leetcode.com/problems/article-views-i/)

**Difficulty:** Easy  
**Category:** Select

## Problem

Write a SQL query to find all the **authors that viewed at least one of their own articles**.

Return the result table sorted by `id` in ascending order.

**Table: Views**
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
```

**Example:**

**Input:**
```
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
```

**Output:**
```
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
```

**Explanation:**
- Author 3 never viewed their own articles
- Author 7 viewed article 2 (their own) on 2019-08-01  
- Author 4 viewed article 3 (their own) on 2019-07-21 (twice, but we only count unique authors)

## Solution Approach

Filter for self-viewing behavior where `viewer_id = author_id`, then get unique author IDs. **Key insight**: Use DISTINCT to handle cases where authors view their own articles multiple times.

**Key concepts:**
- Self-join condition with equality comparison
- DISTINCT for deduplication of results
- Column aliasing for output formatting  
- ORDER BY for consistent result presentation
- Pandas method chaining for efficient data pipeline

**Files:**
- `solution.sql` - Standard approach with WHERE filtering
- `solution_cte.sql` - CTE version separating business logic from presentation  
- `solution.py` - Pandas implementation with method chaining optimization