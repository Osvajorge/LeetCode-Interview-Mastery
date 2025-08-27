# [1683. Invalid Tweets](https://leetcode.com/problems/invalid-tweets/)

**Difficulty:** Easy  
**Category:** Select

## Problem

Write a SQL query to find the IDs of the invalid tweets. A tweet is **invalid** if the number of characters used in the content of the tweet is **strictly greater than 15**.

**Table: Tweets**
```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
```

**Example:**

**Input:**
```
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
```

**Output:**
```
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
```

**Explanation:**
- Tweet 1 has length 11, which is ≤ 15 (valid)
- Tweet 2 has length 33, which is > 15 (invalid)

## Solution Approach

Filter tweets by string length using LENGTH() function in SQL or str.len() in pandas. This tests understanding of **string functions** and **numeric comparisons** for data validation scenarios.

**Key concepts:**
- String length functions: LENGTH() in SQL vs str.len() in pandas
- Numeric comparison with > operator  
- Data validation patterns for content filtering
- Boolean indexing in pandas for efficient filtering

**Files:**
- `solution.sql` - Standard approach with LENGTH() function
- `solution_cte.sql` - CTE version for practice
- `solution.py` - Pandas implementation with string methods and boolean indexing